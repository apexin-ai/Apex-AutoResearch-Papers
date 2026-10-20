# analysis w4 strategy count

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_analysis_w4-strategy-count_20260520T133113.log`
- **Structured JSON:** [`4c93e0bfc798f623e4ea.json`](../../sessions/4c/4c93e0bfc798f623e4ea.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
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
  "uuid": "05d84c7b-8964-4dc3-b96b-6012794ee149",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779285600,
    "rateLimitType": "seven_day",
    "utilization": 0.81,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "de6e03cb-ee9a-4164-9262-03563019370c",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

### Assistant

_source line 4_

I'll find the paper's intervention strategy tables and verify the counts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "785351aa-1eed-4475-b28b-539a8a1de963",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156GfHmbVbPhosrvaw1FccX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12019,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12019
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

<details open><summary>🔧 Tool call — Agent · `toolu_01BXweBEJ36cuoQhpou5yVPZ`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find tex files with tables",
  "prompt": "Search the directory /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus for all .tex files. Then grep for files containing \"tabular\", \"begin{table}\", \"intervention\", or \"strategy\". Also look for any .md files that reference tables or interventions. Report all matching files and their paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "ca07a743-cb9a-4282-9c9f-6fe85c382b99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156GfHmbVbPhosrvaw1FccX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12019,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12019
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
  "task_id": "ad21b089a4d77796a",
  "tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "description": "Find tex files with tables",
  "task_type": "local_agent",
  "prompt": "Search the directory /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus for all .tex files. Then grep for files containing \"tabular\", \"begin{table}\", \"intervention\", or \"strategy\". Also look for any .md files that reference tables or interventions. Report all matching files and their paths.",
  "uuid": "b4738c9f-3ccd-4a11-8602-71e136f9e1da",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

## Round 1

53 recorded events

### User

_source line 7 · 2026-05-20T13:31:26.011Z_

Search the directory /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus for all .tex files. Then grep for files containing "tabular", "begin{table}", "intervention", or "strategy". Also look for any .md files that reference tables or interventions. Report all matching files and their paths.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "a42bc044-5e7e-4772-a6b9-ab9620d71eb3"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21b089a4d77796a",
  "tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "description": "Finding **/*.tex",
  "usage": {
    "total_tokens": 17053,
    "tool_uses": 1,
    "duration_ms": 2089
  },
  "last_tool_name": "Glob",
  "uuid": "ef1bbab6-2eea-4ec8-9fe4-3f39040f3385",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01RhnCaLpDbSQzgfKUsv1gQC`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "57ad6fcc-0c3f-4c41-96f6-9e98fa2ca9b8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VHhcz6CmefFmxmPXqCH9Bt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17042,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17042,
        "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-20T13:31:28.144Z_

<details><summary>↩ Tool result · `toolu_01RhnCaLpDbSQzgfKUsv1gQC`</summary>

```text
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/best/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
artifacts/dream_reports/dream_20260516T124139/best/paper.tex
artifacts/dream_reports/dream_20260516T124139/median/paper.tex
artifacts/dream_reports/dream_20260516T124139/worst/paper.tex
artifacts/dream_reports/dream_20260516T155754/best/paper.tex
artifacts/dream_reports/dream_20260516T155754/median/paper.tex
artifacts/dream_reports/dream_20260516T155754/worst/paper.tex
artifacts/dream_reports/dream_20260517T144412/best/paper.tex
artifacts/dream_reports/dream_20260517T144412/median/paper.tex
artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
artifacts/dream_reports/dream_20260517T165032/best/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260517T165032/median/paper.tex
artifacts/dream_reports/dream_20260517T165032/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/experiments_9ea847.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/related_work_b9688e.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/abstract.tex
artifacts/dream_reports/dream_20260519T034058/best/paper.tex
artifacts/dream_reports/dream_20260519T034058/median/paper.tex
artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
docs/paper/related_work.tex
docs/paper/experiments.tex
docs/paper/limitations_content.tex
docs/paper/diagnosis.tex
docs/paper/abstract.tex
docs/paper/solutions.tex
docs/paper/conclusion.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/analysis.tex
docs/paper/appendix.tex
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "fa04da97-cbea-48c1-99e1-9f778dc1ed9c"
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21b089a4d77796a",
  "tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "description": "Finding **/*.md",
  "usage": {
    "total_tokens": 17057,
    "tool_uses": 2,
    "duration_ms": 2266
  },
  "last_tool_name": "Glob",
  "uuid": "02efffd1-60f7-4d14-b141-238409a79f43",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_015QWbEcwetgACaVPBiR8Cdm`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "b50bd949-c300-414d-a418-12ee334a33a1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VHhcz6CmefFmxmPXqCH9Bt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17042,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17042,
        "ephemeral_1h_input_tokens": 0
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

_source line 13 · 2026-05-20T13:31:28.309Z_

<details><summary>↩ Tool result · `toolu_015QWbEcwetgACaVPBiR8Cdm`</summary>

```text
artifacts/crd_audit_report.md
task_context/history/reviewer/loop_1.md
artifacts/sica_aime30_v2/intermediate/extraction_hang_fix.md
task_context/history/director/loop_1.md
task_context/history/agent/loop_1.md
artifacts/_project/report/code_verify_report.md
artifacts/code_verify_report.md
artifacts/aime30_v2_partial_analysis.md
artifacts/sica_aime30_v2/report/aime30_v2_partial_analysis.md
artifacts/_project/report/scorer_improvement_analysis.md
artifacts/_project/report/scorer_ac_implementation.md
artifacts/_project/report/z3_parser_comprehensive_fix.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_2.md
task_context/history/reviewer/loop_2.md
task_context/history/agent/loop_2_1778882418.md
task_context/history/agent/loop_3.md
task_context/history/director/loop_3.md
task_context/history/agent/loop_4.md
task_context/history/reviewer/loop_3.md
task_context/history/agent/loop_4_1778903872.md
artifacts/_project/report/math_domain_negative_analysis.md
artifacts/report_proofwriter30_v2_progress.md
artifacts/proofwriter30_v2/report/proofwriter30_v2_interim_analysis.md
artifacts/proofwriter30_v2_interim_analysis.md
artifacts/_project/report/maxsat_diagnosis_proofwriter30_v2.md
artifacts/maxsat_diagnosis_proofwriter30_v2.md
artifacts/sica_folio30/report/folio_c0_precheck_report.md
artifacts/folio_c0_precheck_report.md
artifacts/_project/report/d016_model_pivot_report.md
artifacts/d016_model_pivot_report.md
task_context/history/agent/loop_3_1778906513.md
task_context/history/agent/loop_5.md
.claude/sessions/agent_51bea81b/CLAUDE.md
.claude/sessions/agent_51bea81b/AGENTS.md
task_context/history/agent/loop_5_1778961863.md
.claude/sessions/agent_898bbf59/CLAUDE.md
.claude/sessions/agent_898bbf59/AGENTS.md
artifacts/_project/report/paper_prep_audit.md
.claude/sessions/agent_186dc981/CLAUDE.md
.claude/sessions/agent_186dc981/AGENTS.md
artifacts/sica_d012_14b/report/d012_report_sica_d012_14b.md
docs/IDEA_BRIEF.md
artifacts/sica_d012_14b/report/tiebreak_analysis_report.md
task_context/history/director/loop_4.md
task_context/history/reviewer/loop_4.md
artifacts/dream_reports/dream_20260516T051642/best/paper_framing.md
artifacts/exp-005/report/qwq_operating_regime.md
artifacts/dream_reports/dream_20260516T051642/median/paper_framing.md
artifacts/dream_reports/dream_20260516T051642/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T054054/best/paper_framing.md
artifacts/dream_reports/dream_20260516T054054/median/paper_framing.md
artifacts/dream_reports/dream_20260516T054054/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T054054/median/review_report.md
artifacts/dream_reports/dream_20260516T054054/best/review_report.md
artifacts/dream_reports/dream_20260516T054054/worst/review_report.md
artifacts/dream_reports/dream_20260516T124139/best/paper_framing.md
artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md
artifacts/dream_reports/dream_20260516T124139/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T124139/best/review_report.md
artifacts/dream_reports/dream_20260516T124139/median/review_report.md
artifacts/dream_reports/dream_20260516T124139/worst/review_report.md
artifacts/dream_reports/dream_20260516T155754/best/paper_framing.md
artifacts/dream_reports/dream_20260516T155754/median/paper_framing.md
artifacts/dream_reports/dream_20260516T155754/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T155754/best/review_report.md
artifacts/dream_reports/dream_20260516T155754/median/review_report.md
artifacts/dream_reports/dream_20260516T155754/worst/review_report.md
task_context/history/reviewer/loop_5.md
task_context/history/director/loop_5.md
.claude/sessions/agent_ad21233b/CLAUDE.md
.claude/sessions/agent_ad21233b/AGENTS.md
task_context/history/agent/loop_6.md
artifacts/exp-009/report/overhead_report.md
artifacts/exp_009_overhead/overhead_report.md
artifacts/exp-011/report/exp011_preparation_report.md
artifacts/exp-005/report/operating_regime_report.md
artifacts/exp_005_qwq_regime/operating_regime_report.md
artifacts/exp_016_weighted_sc/weighted_sc_report.md
artifacts/exp-016/report/weighted_sc_report.md
.claude/sessions/agent_bf3535c8/CLAUDE.md
.claude/sessions/agent_bf3535c8/AGENTS.md
artifacts/sica_k_sensitivity_14b/report/k_sensitivity_14b_diagnosis.md
artifacts/exp-011-llama8b/diagnosis.md
artifacts/exp-017-strategyqa-v3/report/exp-017-strategyqa-v3_analysis.md
artifacts/exp-017-strategyqa-v3_analysis.md
artifacts/exp-010-mistral-v2/diagnosis.md
task_context/history/agent/loop_7.md
.claude/sessions/agent_ccec83a4/CLAUDE.md
.claude/sessions/agent_ccec83a4/AGENTS.md
task_context/history/director/loop_6.md
task_context/history/reviewer/loop_6.md
task_context/history/agent/loop_7_1779005976.md
.claude/sessions/agent_6d76a9ff/CLAUDE.md
.claude/sessions/agent_6d76a9ff/AGENTS.md
.claude/sessions/agent_d76844a0/CLAUDE.md
.claude/sessions/agent_d76844a0/AGENTS.md
task_context/history/agent/loop_7_1779006614.md
.claude/sessions/agent_b7a40f39/CLAUDE.md
.claude/sessions/agent_b7a40f39/AGENTS.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "b6220fda-2593-43c8-a8fc-8ea2a849be89"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21b089a4d77796a",
  "tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "description": "Searching for tabular",
  "usage": {
    "total_tokens": 20635,
    "tool_uses": 3,
    "duration_ms": 4852
  },
  "last_tool_name": "Grep",
  "uuid": "8f8877d9-d9f5-4a5f-984d-06caa79f8b4b",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Grep · `toolu_01MctTg2kauQB74vyT8Ya4wc`</summary>

```json
{
  "pattern": "tabular",
  "type": "tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "6a2a9798-4915-4cc3-8261-4862e94ca002",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017pPVPKzHJxajPh6ftGUHgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 17042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3572,
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

_source line 16 · 2026-05-20T13:31:30.899Z_

<details><summary>↩ Tool result · `toolu_01MctTg2kauQB74vyT8Ya4wc`</summary>

```text
Found 27 files
docs/paper/appendix.tex
docs/paper/analysis.tex
docs/paper/diagnosis.tex
docs/paper/experiments.tex
artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
artifacts/dream_reports/dream_20260519T034058/median/paper.tex
artifacts/dream_reports/dream_20260519T034058/best/paper.tex
artifacts/_project/paper/experiments_9ea847.tex
artifacts/dream_reports/dream_20260517T165032/worst/paper.tex
artifacts/dream_reports/dream_20260517T165032/median/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260517T165032/best/paper.tex
docs/paper/acl.sty
artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
artifacts/dream_reports/dream_20260517T144412/median/paper.tex
artifacts/dream_reports/dream_20260517T144412/best/paper.tex
artifacts/dream_reports/dream_20260516T155754/worst/paper.tex
artifacts/dream_reports/dream_20260516T155754/median/paper.tex
artifacts/dream_reports/dream_20260516T155754/best/paper.tex
artifacts/dream_reports/dream_20260516T124139/worst/paper.tex
artifacts/dream_reports/dream_20260516T124139/median/paper.tex
artifacts/dream_reports/dream_20260516T124139/best/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/best/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "8f33db8e-7c4d-4086-b3e9-b7606af3cdb1"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21b089a4d77796a",
  "tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "description": "Searching for begin\\{table\\}",
  "usage": {
    "total_tokens": 20636,
    "tool_uses": 4,
    "duration_ms": 5303
  },
  "last_tool_name": "Grep",
  "uuid": "b4cfa233-f066-4196-bf86-4c6be4b330e4",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01TmWFPfZgoTJtFYkMDtJYtR`</summary>

```json
{
  "pattern": "begin\\{table\\}",
  "type": "tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "61a0ac10-b7e2-4fd3-83ac-a0eb44dd1144",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017pPVPKzHJxajPh6ftGUHgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 17042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3572,
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

_source line 19 · 2026-05-20T13:31:31.350Z_

<details><summary>↩ Tool result · `toolu_01TmWFPfZgoTJtFYkMDtJYtR`</summary>

```text
Found 25 files
docs/paper/appendix.tex
docs/paper/analysis.tex
docs/paper/diagnosis.tex
artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
artifacts/dream_reports/dream_20260519T034058/median/paper.tex
artifacts/dream_reports/dream_20260519T034058/best/paper.tex
artifacts/_project/paper/experiments_9ea847.tex
artifacts/dream_reports/dream_20260517T165032/worst/paper.tex
artifacts/dream_reports/dream_20260517T165032/median/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260517T165032/best/paper.tex
artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
artifacts/dream_reports/dream_20260517T144412/median/paper.tex
artifacts/dream_reports/dream_20260517T144412/best/paper.tex
artifacts/dream_reports/dream_20260516T155754/worst/paper.tex
artifacts/dream_reports/dream_20260516T155754/median/paper.tex
artifacts/dream_reports/dream_20260516T155754/best/paper.tex
artifacts/dream_reports/dream_20260516T124139/worst/paper.tex
artifacts/dream_reports/dream_20260516T124139/median/paper.tex
artifacts/dream_reports/dream_20260516T124139/best/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/best/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "0b123312-66f9-49f0-a0f9-03b88ff3ec87"
}
```

</details>

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21b089a4d77796a",
  "tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "description": "Searching for intervention",
  "usage": {
    "total_tokens": 20637,
    "tool_uses": 5,
    "duration_ms": 8284
  },
  "last_tool_name": "Grep",
  "uuid": "bab8eef9-8461-455f-8cad-aa01ba81f9c3",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Grep · `toolu_01SM8AqwnoUzXe5mnzZy5jhZ`</summary>

```json
{
  "pattern": "intervention",
  "type": "tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "b11afab7-12b6-4314-890f-04238dc61e5b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017pPVPKzHJxajPh6ftGUHgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 17042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3572,
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

_source line 22 · 2026-05-20T13:31:34.328Z_

<details><summary>↩ Tool result · `toolu_01SM8AqwnoUzXe5mnzZy5jhZ`</summary>

```text
Found 6 files
docs/paper/appendix.tex
docs/paper/analysis.tex
docs/paper/diagnosis.tex
artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
artifacts/dream_reports/dream_20260519T034058/best/paper.tex
artifacts/_project/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "d4fa662d-46e6-4e2c-b91a-95ce9867b1e9"
}
```

</details>

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21b089a4d77796a",
  "tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "description": "Searching for strategy",
  "usage": {
    "total_tokens": 20638,
    "tool_uses": 6,
    "duration_ms": 8341
  },
  "last_tool_name": "Grep",
  "uuid": "daec5382-4230-43d8-bd16-1d5543e4a71c",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_01PveWamYgjNqZ2Vd1MGY2dz`</summary>

```json
{
  "pattern": "strategy",
  "type": "tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "74c2f2e7-23e2-44f5-b872-6f624d77b3cf",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017pPVPKzHJxajPh6ftGUHgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 17042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3572,
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

_source line 25 · 2026-05-20T13:31:34.380Z_

<details><summary>↩ Tool result · `toolu_01PveWamYgjNqZ2Vd1MGY2dz`</summary>

```text
Found 19 files
docs/paper/introduction.tex
docs/paper/limitations_content.tex
docs/paper/experiments.tex
docs/paper/references.bib
artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
artifacts/dream_reports/dream_20260519T034058/best/paper.tex
artifacts/_project/paper/experiments_9ea847.tex
artifacts/dream_reports/dream_20260517T165032/worst/paper.tex
artifacts/dream_reports/dream_20260517T165032/median/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260517T165032/best/paper.tex
artifacts/dream_reports/dream_20260517T144412/median/paper.tex
artifacts/dream_reports/dream_20260517T144412/best/paper.tex
artifacts/dream_reports/dream_20260516T155754/best/paper.tex
artifacts/dream_reports/dream_20260516T124139/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "c4bcc430-1426-4e9a-a30a-ce25c3d919fc"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21b089a4d77796a",
  "tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "description": "Searching for table|intervention",
  "usage": {
    "total_tokens": 22651,
    "tool_uses": 7,
    "duration_ms": 10965
  },
  "last_tool_name": "Grep",
  "uuid": "29af3a75-db7a-431f-9f42-ad32730d308c",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_01YVoTFFgpt9sgNinYQDqDAL`</summary>

```json
{
  "pattern": "table|intervention",
  "type": "md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "3460ac5a-f361-4c64-9500-59a3e3f254c1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UmZRCSUHNVtxFAjWL5NQ2u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2011,
      "cache_read_input_tokens": 20614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2011,
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

_source line 28 · 2026-05-20T13:31:37.010Z_

<details><summary>↩ Tool result · `toolu_01YVoTFFgpt9sgNinYQDqDAL`</summary>

```text
Found 57 files
.claude/sessions/reviewer_342b9753/AGENTS.md
.claude/sessions/reviewer_342b9753/CLAUDE.md
.claude/sessions/director_909d512a/AGENTS.md
.claude/sessions/director_909d512a/CLAUDE.md
.claude/sessions/paper_agent_644edc69/AGENTS.md
.claude/sessions/paper_agent_644edc69/CLAUDE.md
artifacts/review_reports/round_3.md
paper_framing.md
.claude/sessions/director_bc74ef25/AGENTS.md
.claude/sessions/director_bc74ef25/CLAUDE.md
docs/paper_skeleton_dual_versions.md
docs/paper_prep_outline_and_data.md
.claude/sessions/distiller_efdee075/AGENTS.md
.claude/sessions/distiller_efdee075/CLAUDE.md
task_context/history/agent/loop_9_1779190556.md
task_context/history/agent/loop_9.md
artifacts/dream_reports/dream_20260519T034058/worst/review_report.md
artifacts/dream_reports/dream_20260519T034058/median/review_report.md
artifacts/dream_reports/dream_20260519T034058/best/review_report.md
artifacts/dream_reports/dream_20260519T034058/worst/paper_framing.md
artifacts/dream_reports/dream_20260519T034058/median/paper_framing.md
artifacts/dream_reports/dream_20260519T034058/best/paper_framing.md
docs/paper_framing_upgrade.md
artifacts/exp-023-discriminative-rate/report/f2_discriminative_analysis.md
artifacts/f2_discriminative_analysis.md
artifacts/review_reports/round_1.md
task_context/history/reviewer/loop_8.md
artifacts/review_reports/round_0.md
artifacts/dream_reports/dream_20260517T165032/median/review_report.md
artifacts/dream_reports/dream_20260517T165032/best/review_report.md
artifacts/dream_reports/dream_20260517T165032/worst/paper_framing.md
artifacts/dream_reports/dream_20260517T165032/median/paper_framing.md
artifacts/dream_reports/dream_20260517T165032/best/paper_framing.md
artifacts/dream_reports/dream_20260517T144412/worst/review_report.md
artifacts/dream_reports/dream_20260517T144412/best/review_report.md
artifacts/dream_reports/dream_20260517T144412/median/review_report.md
artifacts/exp-011/report/exp011_truncation_bias_analysis.md
artifacts/exp011_truncation_bias_analysis.md
task_context/history/director/loop_6.md
artifacts/sica_k_sensitivity_14b/report/k_sensitivity_14b_diagnosis.md
artifacts/dream_reports/dream_20260516T155754/worst/review_report.md
artifacts/dream_reports/dream_20260516T155754/median/review_report.md
artifacts/dream_reports/dream_20260516T155754/best/review_report.md
artifacts/dream_reports/dream_20260516T155754/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T155754/median/paper_framing.md
artifacts/dream_reports/dream_20260516T155754/best/paper_framing.md
artifacts/dream_reports/dream_20260516T124139/worst/review_report.md
artifacts/dream_reports/dream_20260516T124139/best/review_report.md
artifacts/dream_reports/dream_20260516T124139/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md
artifacts/dream_reports/dream_20260516T124139/best/paper_framing.md
artifacts/dream_reports/dream_20260516T054054/worst/review_report.md
artifacts/dream_reports/dream_20260516T054054/median/review_report.md
docs/IDEA_BRIEF.md
artifacts/_project/report/paper_prep_audit.md
artifacts/_project/report/d016_model_pivot_report.md
artifacts/d016_model_pivot_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "335d57eb-8627-4875-94c8-65c80a7642db"
}
```

</details>

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21b089a4d77796a",
  "tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 23922,
    "tool_uses": 8,
    "duration_ms": 13346
  },
  "last_tool_name": "Bash",
  "uuid": "7072b0ea-48a4-4c6f-b408-3f1ea6a63830",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01BbHvqQyTqHU16mB4BUZVjZ`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus -type f \\( -name \"*.tex\" -o -name \"*.md\" \\) | wc -l"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "4342baec-fe51-4a4b-bccc-079f858170c5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NxqyQkUSz9b6EeQyPndFCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 22625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
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

_source line 31 · 2026-05-20T13:31:39.567Z_

<details><summary>↩ Tool result · `toolu_01BbHvqQyTqHU16mB4BUZVjZ`</summary>

```text
345
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "28005279-a911-4ece-9f98-4e713d19bc90"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ad21b089a4d77796a",
  "tool_use_id": "toolu_01BXweBEJ36cuoQhpou5yVPZ",
  "status": "completed",
  "output_file": "",
  "summary": "Find tex files with tables",
  "usage": {
    "total_tokens": 24073,
    "tool_uses": 8,
    "duration_ms": 21827
  },
  "uuid": "0b14539f-26b6-44c1-bb2c-b281b4d0ced9",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918"
}
```

---

### Tool result

_source line 33 · 2026-05-20T13:31:47.841Z_

<details><summary>↩ Tool result · `toolu_01BXweBEJ36cuoQhpou5yVPZ`</summary>

```text
## Summary Report

I've completed a comprehensive search of the directory `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus` for .tex and .md files containing tables, interventions, and strategies.

### TEX Files Summary

**Total .tex files found: 43**

The search revealed matches for your specified patterns:

#### Files with "tabular" (27 matches):
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper/experiments.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper/experiments_9ea847.tex
- Multiple files in artifacts/dream_reports/ (various dream_ timestamps with best/median/worst variants)

#### Files with "begin{table}" (25 matches):
- Same files as tabular, minus one
- Primary locations: docs/paper/ and artifacts/dream_reports/
- Key files: appendix.tex, analysis.tex, diagnosis.tex, experiments.tex

#### Files with "intervention" (6 matches):
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/best/paper.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper/discussion.tex

#### Files with "strategy" (19 matches):
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib
- Multiple files in artifacts/dream_reports/ with various timestamps

### Markdown Files Summary

**Total .md files found: 57 with table/intervention references**

Primary markdown files with tables and/or interventions:
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/IDEA_BRIEF.md
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper_framing_upgrade.md
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper_skeleton_dual_versions.md
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper_prep_outline_and_data.md
- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md
- Multiple review reports in artifacts/review_reports/
- Multiple dream reports and analyses in artifacts/

### Key Findings

The most relevant document collections are:
1. **docs/paper/** - Contains the main paper structure with tables and interventions in appendix.tex, analysis.tex, and diagnosis.tex
2. **artifacts/_project/paper/** - Contains backup/versioned paper files
3. **artifacts/dream_reports/** - Contains multiple experimental paper variants (organized by timestamp and quality: best/median/worst)
4. **docs/** - Contains markdown-based planning documents and brief outlines
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "b0fc3c51-436b-42a6-a4b1-517d6608e2a1",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search the directory /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus for all .tex files. Then grep for files containing \"tabular\", \"begin{table}\", \"intervention\", or \"strategy\". Also look for any .md files that reference tables or interventions. Report all matching files and their paths.",
    "agentId": "ad21b089a4d77796a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary Report\n\nI've completed a comprehensive search of the directory `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus` for .tex and .md files containing tables, interventions, and strategies.\n\n### TEX Files Summary\n\n**Total .tex files found: 43**\n\nThe search revealed matches for your specified patterns:\n\n#### Files with \"tabular\" (27 matches):\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper/experiments.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper/experiments_9ea847.tex\n- Multiple files in artifacts/dream_reports/ (various dream_ timestamps with best/median/worst variants)\n\n#### Files with \"begin{table}\" (25 matches):\n- Same files as tabular, minus one\n- Primary locations: docs/paper/ and artifacts/dream_reports/\n- Key files: appendix.tex, analysis.tex, diagnosis.tex, experiments.tex\n\n#### Files with \"intervention\" (6 matches):\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/best/paper.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper/discussion.tex\n\n#### Files with \"strategy\" (19 matches):\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib\n- Multiple files in artifacts/dream_reports/ with various timestamps\n\n### Markdown Files Summary\n\n**Total .md files found: 57 with table/intervention references**\n\nPrimary markdown files with tables and/or interventions:\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/IDEA_BRIEF.md\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper_framing_upgrade.md\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper_skeleton_dual_versions.md\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper_prep_outline_and_data.md\n- /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\n- Multiple review reports in artifacts/review_reports/\n- Multiple dream reports and analyses in artifacts/\n\n### Key Findings\n\nThe most relevant document collections are:\n1. **docs/paper/** - Contains the main paper structure with tables and interventions in appendix.tex, analysis.tex, and diagnosis.tex\n2. **artifacts/_project/paper/** - Contains backup/versioned paper files\n3. **artifacts/dream_reports/** - Contains multiple experimental paper variants (organized by timestamp and quality: best/median/worst)\n4. **docs/** - Contains markdown-based planning documents and brief outlines"
      }
    ],
    "totalDurationMs": 21828,
    "totalTokens": 25317,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 150,
      "cache_read_input_tokens": 23895,
      "output_tokens": 1266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 150
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1266,
          "cache_read_input_tokens": 23895,
          "cache_creation_input_tokens": 150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 150,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 7,
      "bashCount": 1,
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

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01Rp3LQSWcEcgyNKwNRoxZPd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "e69ba6a9-6060-4737-9d21-3d28ff2a2043",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeGkK3Y8Nb9wHuxxGKCqFU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 23860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1465
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

_source line 35 · 2026-05-20T13:31:51.009Z_

<details><summary>↩ Tool result · `toolu_01Rp3LQSWcEcgyNKwNRoxZPd`</summary>

```text
1	
2	\section{Prompt Templates}
3	\label{app:prompts}
4	
5	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
6	
7	\paragraph{System Prompt.}
8	
9	\begin{lstlisting}
10	You are a constraint extraction tool. Output ONLY
11	valid JSON. Do NOT solve problems, reason about
12	correctness, or think step-by-step. Extract
13	constraints from the given trace exactly as stated.
14	\end{lstlisting}
15	
16	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
17	
18	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
19	
20	\begin{lstlisting}
21	Extract mathematical constraints from this reasoning
22	trace as a JSON object.
23	
24	Rules:
25	- type: "equation", "inequality", or "predicate"
26	- expression: human-readable, e.g. "x + y == 14"
27	- z3_formula: a single comparison expression in
28	  Python Z3 syntax
29	- source_step: step number where the constraint
30	  appears
31	- Use variable names from the trace
32	
33	z3_formula MUST follow these rules:
34	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
35	  /, **, %
36	- Use individual named variables: a1, a2, a3...
37	  NOT arrays a[1] or sets A
38	- Expand all sums explicitly:
39	  "a1 + a2 + a3 == 55" NOT "sum([a1,a2,a3])"
40	- NO Python builtins: sum(), len(), max(), min(),
41	  list(), set(), range(), int()
42	- Each z3_formula must be exactly ONE comparison
43	  (==, !=, <, >, <=, >=)
44	- For multiple values, write separate constraints
45	  for each
46	
47	Output ONLY the JSON below, nothing else:
48	{"constraints": [{"type": "equation",
49	  "expression": "x + y == 14",
50	  "z3_formula": "x + y == 14",
51	  "source_step": 1}],
52	 "answer": "final_answer",
53	 "variables": ["x", "y"]}
54	
55	Trace:
56	{trace}
57	\end{lstlisting}
58	
59	\paragraph{Logical Constraint Extraction (LOGIC\_EXTRACTION\_PROMPT).}
60	
61	Used for ProofWriter and FOLIO datasets.
62	
63	\begin{lstlisting}
64	IMPORTANT: You are an EXTRACTION tool, NOT a problem
65	solver.
66	- Do NOT re-solve or re-reason about the problem.
67	- Do NOT verify whether the trace's reasoning is
68	  correct.
69	- ONLY extract the logical constraints that are
70	  explicitly stated or used in the trace below.
71	- Output ONLY the JSON object, nothing else.
72	
73	Extract logical constraints from this reasoning trace
74	about a logic problem.
75	
76	The problem has facts (base assertions), rules
77	(grounded implications), and derived conclusions.
78	Convert each into a Z3 boolean formula.
79	
80	Variable naming:
81	- Unary property: property_entity
82	  (e.g., kind_anne, red_charlie, round_fiona)
83	- Binary relation: relation_subject_object
84	  (e.g., eats_bear_squirrel, likes_lion_cat)
85	- Use lowercase with underscores only
86	
87	Constraint types:
88	- "fact": a given assertion,
89	  e.g., kind_anne == True
90	- "rule": a grounded implication over specific
91	  entities, e.g., Implies(kind_anne, nice_anne)
92	- "derived": an inferred conclusion from facts +
93	  rules, e.g., nice_anne == True
94	
95	Z3 operators:
96	- Implies(a, b) for if-then rules
97	- And(a, b, ...) for conjunctive conditions
98	- Or(a, b, ...) for disjunctive conditions
99	- Not(a) for negation
100	- == True / == False for boolean assertions
101	
102	Output ONLY the JSON below, nothing else:
103	{"constraints": [{"type": "fact",
104	  "expression": "kind(anne)",
105	  "z3_formula": "kind_anne == True",
106	  "source_step": 1}],
107	 "answer": "True or False or Unknown",
108	 "variables": ["kind_anne"]}
109	
110	Trace:
111	{trace}
112	\end{lstlisting}
113	
114	\paragraph{Output Schema.}
115	
116	Both prompts produce a JSON object with the following structure:
117	
118	\begin{lstlisting}
119	{
120	  "constraints": [
121	    {
122	      "type": "&lt;equation|inequality|predicate>
123	               or &lt;fact|rule|derived>",
124	      "expression": "&lt;human-readable description>",
125	      "z3_formula": "&lt;Z3-compatible expression>",
126	      "source_step": &lt;integer>
127	    }
128	  ],
129	  "answer": "&lt;final answer string>",
130	  "variables": ["&lt;var1>", "&lt;var2>", "..."]
131	}
132	\end{lstlisting}
133	
134	The pipeline additionally injects an \texttt{answer\_assertion} constraint per trace (not produced by the LLM):
135	
136	\begin{lstlisting}
137	{"type": "answer_assertion",
138	 "expression": "answer is &lt;ans>",
139	 "z3_formula": "__sica_answer_&lt;ans> == True",
140	 "source_step": -1}
141	\end{lstlisting}
142	
143	\paragraph{Prompt Selection Logic.}
144	
145	Domain assignment is determined by dataset: FOLIO and ProofWriter use \textsc{Logic\_Extraction\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \textsc{Extraction\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.
146	
147	
148	\section{Z3 MaxSAT Evaluation Pseudocode}
149	\label{app:z3-pseudocode}
150	
151	Algorithm~\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\ref{alg:scorer} describes the source-trace attribution scoring.
152	
153	Domain constraint variables (e.g., \texttt{x + y == 14}) and answer assertion variables (e.g., \texttt{\_\_sica\_answer\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.
154	
155	\begin{algorithm}[h]
156	\caption{Z3 Weighted Partial MAX-SAT}
157	\label{alg:maxsat}
158	\begin{algorithmic}[1]
159	\Require Deduplicated constraint set $\mathcal{C} = \{(c_m, w_m, S_m)\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices
160	\Ensure Partition $(\mathcal{C}^*, \mathcal{C}^{\setminus})$ where $\mathcal{C}^*$ is the max-weight satisfiable subset
161	\State $\textit{opt} \gets \textsc{Z3.Optimize()}$
162	\For{$m = 1, \ldots, M$}
163	    \State $b_m \gets$ fresh Boolean indicator
164	    \State $\textit{opt}.\textsc{Add}(b_m \Rightarrow c_m)$ \Comment{soft clause guarded by indicator}
165	    \State $\textit{opt}.\textsc{AddSoft}(b_m,\; \text{weight}=w_m)$
166	\EndFor
167	\State $\textit{result} \gets \textit{opt}.\textsc{Check}()$
168	\State $\textit{model} \gets \textit{opt}.\textsc{Model}()$
169	\State $\mathcal{C}^* \gets \{(c_m, w_m, S_m) : \textit{model}(b_m) = \top\}$
170	\State $\mathcal{C}^{\setminus} \gets \mathcal{C} \setminus \mathcal{C}^*$
171	\State \Return $(\mathcal{C}^*, \mathcal{C}^{\setminus})$
172	\end{algorithmic}
173	\end{algorithm}
174	
175	\begin{algorithm}[h]
176	\caption{Source-Trace Attribution Scoring}
177	\label{alg:scorer}
178	\begin{algorithmic}[1]
179	\Require Satisfied set $\mathcal{C}^*$, excluded set $\mathcal{C}^{\setminus}$, candidate answers $\mathcal{A}$, trace-answer mapping $\tau: \text{trace\_idx} \to a$, penalty weight $\alpha$
180	\Ensure Score $s(a)$ for each $a \in \mathcal{A}$
181	\For{each $a \in \mathcal{A}$}
182	    \State $T_a \gets \{i : \tau(i) = a\}$ \Comment{trace indices producing answer $a$}
183	    \State $\textit{pos}(a) \gets \sum_{(c,w,S) \in \mathcal{C}^*} w \cdot \mathbf{1}[S \cap T_a \neq \emptyset]$
184	    \State $\textit{neg}(a) \gets \sum_{(c,w,S) \in \mathcal{C}^{\setminus}} w \cdot \mathbf{1}[S \cap T_a \neq \emptyset]$
185	    \State $s(a) \gets \textit{pos}(a) - \alpha \cdot \textit{neg}(a)$
186	\EndFor
187	\State \Return $a^* = \arg\max_{a \in \mathcal{A}} s(a)$
188	\end{algorithmic}
189	\end{algorithm}
190	
191	
192	\section{Capability Trap Diagnostics}
193	\label{app:diagnostics}
194	
195	Table~\ref{tab:capability_trap} reports per-condition diagnostic metrics referenced in \S\ref{sec:entropy}.
196	
197	\begin{table}[h]
198	\centering
199	\small
200	\begin{tabular}{@{}llrrrr@{}}
201	\toprule
202	Model & Domain & $C_0$ (\%) & Extr.\ Rate & Contr.\ Rate & $\Delta$ (pp) \\
203	\midrule
204	Qwen2.5-14B & FOLIO & 35.3 & 0.89 & 0.022 & 0.00 \\
205	Qwen2.5-14B & ProofWriter & 39.2 & 0.89 & 0.022 & $+$0.33 \\
206	Qwen2.5-14B & StrategyQA$^\dagger$ & 10.0 & 0.70 & --- & $+$3.33 \\
207	Qwen2.5-14B & ARC-Chall.$^\dagger$ & 5.0 & 1.00 & --- & $-$1.67 \\
208	Qwen2.5-7B & FOLIO+PW$^\dagger$ & 42.1 & 0.94 & 0.027 & 0.00 \\
209	Mistral-7B & FOLIO+PW$^\dagger$ & 50.0 & 0.88 & 0.056 & 0.00 \\
210	LLaMA-3.1-8B & StrategyQA & 41.0 & --- & --- & $+$2.00 \\
211	LLaMA-3.1-8B & FOLIO & 61.8 & 0.94 & 0.062 & $-$4.41 \\
212	DeepSeek-R1-7B & FOLIO+PW$^\dagger$ & 58.3 & 0.84 & 0.037 & $-$3.33 \\
213	QwQ-32B & Combined$^\dagger$ & 2.6 & --- & --- & 0.00 \\
214	Qwen2.5-14B & GSM8K$^\dagger$ & 13.3 & 0.15 & --- & 0.00 \\
215	\bottomrule
216	\end{tabular}
217	\caption{Capability trap diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable FOL constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\Delta$: SICA$-$SC gap (pp). $\dagger$: $n \leq 60$. Dashes indicate conditions where extraction diagnostics were not computed (StrategyQA uses boolean answers without FOL extraction; QwQ-32B Combined had near-zero $C_0$, making extraction analysis uninformative). This table includes additional exploratory conditions not reported in Table~\ref{tab:main_results}.}
218	\label{tab:capability_trap}
219	\end{table}
220	
221	
222	\section{Statistical Power Analysis}
223	\label{app:power}
224	
225	We compute the minimum detectable effect (MDE) for each condition at $\alpha = 0.05$ and 80\% power using exact binomial power calculations over McNemar discordant pairs. Table~\ref{tab:power} reports three grouped conditions with $n \geq 200$ (Qwen2.5-14B FOLIO and ProofWriter are pooled into a single $n{=}804$ analysis, corresponding to four Table~\ref{tab:main_results} rows), which constitute our confirmatory analyses. The remaining seven conditions ($n \leq 60$) yield infinite MDE due to insufficient discordant pairs and serve only as regime characterization.
226	
227	\begin{table}[h]
228	\centering
229	\small
230	\begin{tabular}{lrrrrr}
231	\toprule
232	\textbf{Condition} & $n$ & \textbf{MDE} & \textbf{Obs.\ $\Delta$} & \textbf{Obs.\ Pow.} \\
233	\midrule
234	Qwen-14B FOLIO+PW   & 804 & 1.86pp & $+$0.25pp & 5.7\%  \\
235	LLaMA-8B StrategyQA  & 200 & 4.64pp & $+$2.00pp & 20.6\% \\
236	LLaMA-8B FOLIO       & 204 & 4.84pp & $-$4.41pp & 18.6\% \\
237	\bottomrule
238	\end{tabular}
239	\caption{Power analysis for confirmatory conditions ($n \geq 200$). MDE = minimum detectable effect at 80\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\% in every case.}
240	\label{tab:power}
241	\end{table}
242	
243	The largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.
244	
245	
246	\section{Bootstrap Confidence Intervals}
247	\label{app:bootstrap}
248	
249	We compute 95\% confidence intervals for $\Delta(\text{SICA} - \text{SC})$ via 10{,}000 bootstrap resamples (percentile method, seed 42). Table~\ref{tab:bootstrap} reports the results for the three confirmatory conditions.
250	
251	\begin{table}[h]
252	\centering
253	\small
254	\begin{tabular}{lrrl}
255	\toprule
256	\textbf{Condition} & $n$ & \textbf{Obs.\ $\Delta$} & \textbf{95\% CI} \\
257	\midrule
258	Qwen-14B FOLIO+PW   & 804 & $+$0.25pp & [$-$1.12, $+$1.62] \\
259	LLaMA-8B StrategyQA  & 200 & $+$2.00pp & [$-$1.50, $+$5.50] \\
260	LLaMA-8B FOLIO       & 204 & $-$4.41pp & [$-$5.88, $+$0.98] \\
261	\bottomrule
262	\end{tabular}
263	\caption{Bootstrap 95\% confidence intervals for $\Delta(\text{SICA} - \text{SC})$ in percentage points. All intervals include zero, consistent with no reliable accuracy difference.}
264	\label{tab:bootstrap}
265	\end{table}
266	
267	All three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that symbolic constraint aggregation improves over majority voting.
268	
269	
270	\section{Case Studies: Discordant Predictions}
271	\label{app:case-studies}
272	
273	Among 804 problems, SICA and SC agree on 773 (96.1\%). The 31 discordant cases comprise 16 SICA wins (SICA correct, SC wrong), 14 SC wins (SC correct, SICA wrong), and 1 where both select different wrong answers. All 31 occur at exact ties (entropy${=}1.0$, 6:6 vote split) or near-ties (entropy${\geq}0.9183$, 8:4 at most), since SICA can differ from SC only when constraint weights shift the majority away from SC's tiebreak choice. We present three representative cases that illustrate the mechanism behind capability trap failures.
274	
275	\paragraph{Case 1: SICA Wins (folio\_134, FOLIO).}
276	
277	\emph{Premises}: Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth. \emph{Conclusion}: Humans are mammals. \emph{Gold}: Unknown.
278	
279	The premises state that \emph{some} mammals have teeth and that humans have teeth, but ``having teeth'' is not sufficient for ``being a mammal'' under open-world semantics. SC produces a 6:6 split (Unknown:6, True:6) and tiebreaks alphabetically to True (wrong). SICA extracts 7 constraints; MaxSAT excludes 1 constraint inconsistent with the rest, reducing the weighted score for True-voting traces and tipping the aggregation to Unknown (correct). The excluded constraint likely captured an incorrect inference step (e.g., affirming the consequent) present only in True-voting traces. While SICA succeeds here, the success is coincidental: the excluded constraint happens to anti-correlate with the correct answer.
280	
281	\paragraph{Case 2: SC Wins (ProofWriter-1066\_Q6, ProofWriter).}
282	
283	\emph{Key chain}: White(Bob)$\to$Round(Bob) [white things are round] $\to$ Young(Bob) [all round things are young]. \emph{Conclusion}: ``Bob is not young.'' \emph{Gold}: False (Bob IS young).
284	
285	SC produces a 6:6 split (False:6, True:6) and tiebreaks to False (correct). SICA extracts 17 constraints; MaxSAT excludes 2 that appear preferentially in False-voting traces. These excluded constraints likely captured correct intermediate derivations (e.g., \texttt{young\_bob == True}) that appeared only in traces completing the full deduction chain. By excluding them, MaxSAT removes evidence supporting the correct answer. SICA selects True (wrong). This case illustrates how self-extracted constraints can systematically mislead: correct reasoning steps become discriminative signals that the solver mistakenly penalizes.
286	
287	\paragraph{Case 3: Non-discriminative Constraints (ProofWriter-903\_Q6, ProofWriter).}
288	
289	\emph{Key chain}: Nice(Mouse)$\to$Cold(Mouse) [all nice people are cold] $\to$ Chases(Mouse,Mouse) [nice and cold $\to$ chase mouse]. \emph{Conclusion}: ``The mouse does not chase the mouse.'' \emph{Gold}: False.
290	
291	SC produces a 6:6 split (False:6, Unknown:6) and tiebreaks to False (correct). SICA extracts 44 constraints but excludes only 1 (2.3\%). The remaining 43 are domain facts and grounded rules (\texttt{nice\_mouse == True}, \texttt{Implies(nice\_mouse, cold\_mouse)}, etc.) that Z3 satisfies identically regardless of the final answer. Both False-voting and Unknown-voting traces share the same premises and grounded rules; they differ only in whether the trace completed the full derivation chain. The single excluded constraint carries negligible weight against 43 shared constraints, so SICA collapses to SC.
292	
293	\paragraph{Pattern.}
294	
295	These cases exemplify the general pattern across the 773 agreeing problems: the vast majority of extracted constraints encode shared domain structure rather than answer-specific reasoning, and MaxSAT aggregation degenerates to majority vote. Table~\ref{tab:case_summary} summarizes.
296	
297	\begin{table}[h]
298	\centering
299	\small
300	\caption{Summary of three representative discordant cases. All occur at exact 6:6 vote ties. Constraint exclusion can break ties in either direction (Cases 1--2) or have no effect (Case 3).}
301	\label{tab:case_summary}
302	\begin{tabular}{@{}lllcccc@{}}
303	\toprule
304	Case & ID & Gold & SC & SICA & \#Constr. & Excl.\ (\%) \\
305	\midrule
306	1 (SICA win) & folio\_134 & Unknown & True $\times$ & Unknown $\checkmark$ & 7 & 1 (14.3\%) \\
307	2 (SC win) & PW-1066\_Q6 & False & False $\checkmark$ & True $\times$ & 17 & 2 (11.8\%) \\
308	3 (Non-disc.) & PW-903\_Q6 & False & False $\checkmark$ & False $\checkmark$ & 44 & 1 (2.3\%) \\
309	\bottomrule
310	\end{tabular}
311	\end{table}
312	
313	
314	\section{ProofWriter Oracle Per-Subtype Analysis}
315	\label{app:pw-oracle-subtype}
316	
317	ProofWriter problems encode deductive rules as Domain-Specific Language (DSL) logic programs. Each problem uses one of four predicate subtypes: attribute predicates with or without negation (AttNeg, AttNoneg), and relation predicates with or without negation (RelNeg, RelNoneg). Relation predicates involve binary relations between entities (e.g., \texttt{eats(bear, squirrel)}), while attribute predicates assign unary properties (e.g., \texttt{kind(anne)}).
318	
319	The oracle pipeline parses these DSL annotations deterministically into Z3 formulas without any LLM involvement. Of the 600 ProofWriter problems, 594 (99.0\%) produce valid Z3 parses; the remaining 6 fail due to unsupported DSL constructs. Across all 7{,}128 trace-problem pairs submitted to Z3, the solver returns a result in every case (0\% solver errors). Z3 evaluations agree with ground-truth labels on 577 of 594 parseable problems (97.14\%), confirming that the deterministic DSL-to-Z3 translation faithfully preserves problem semantics.
320	
321	Table~\ref{tab:pw_oracle_subtype} reports the per-subtype breakdown. Relation-predicate subtypes show substantially larger gains than attribute-predicate subtypes: RelNeg improves by $+17.86$~pp and RelNoneg by $+13.01$~pp, compared to $+9.09$~pp for AttNoneg and $+6.87$~pp for AttNeg. Relation predicates involve longer reasoning chains with more intermediate entities, producing greater answer diversity across traces ($C_0$) and more opportunities for oracle constraints to correct errors.
322	
323	\begin{table}[h]
324	\centering
325	\caption{ProofWriter oracle experiment per-subtype breakdown. Oracle-SICA uses gold DSL annotations parsed deterministically to Z3 for consistency checking. Relation-predicate subtypes (RelNeg, RelNoneg) show larger gains than attribute-predicate subtypes; relation subtypes involve longer reasoning chains and benefit more from oracle constraints. Bold indicates best accuracy per row.}
326	\label{tab:pw_oracle_subtype}
327	\begin{tabular}{lcccc}
328	\toprule
329	Subtype & $n$ & SC Acc (\%) & Oracle Acc (\%) & $\Delta$ (pp) \\
330	\midrule
331	AttNoneg & 154 & 87.01 & \textbf{96.10} & +9.09 \\
332	AttNeg & 160 & 85.00 & \textbf{91.88} & +6.87 \\
333	RelNoneg & 146 & 66.44 & \textbf{79.45} & +13.01 \\
334	RelNeg & 140 & 60.00 & \textbf{77.86} & +17.86 \\
335	\midrule
336	Overall & 600 & 75.17 & \textbf{86.67} & +11.50 \\
337	\bottomrule
338	\end{tabular}
339	\end{table}
340	
341	
342	\section{Constraint Ablation Details}
343	\label{app:ablation}
344	\label{sec:ablation}
345	
346	\begin{table}[h]
347	\centering
348	\small
349	\caption{Constraint ablation (Qwen2.5-14B, $n = 804$). Agreement: predictions identical to SC. MAX-SAT and count-only produce nearly identical predictions, confirming that self-extracted constraints carry no signal beyond vote counts.}
350	\label{tab:ablation}
351	\begin{tabular}{@{}lrc@{}}
352	\toprule
353	Aggregation & Acc.\ (\%) & Agreement w/ SC \\
354	\midrule
355	SC (majority vote) & 76.24 & --- \\
356	SICA (MAX-SAT) & 76.49 & 773\,/\,804 \\
357	Count-only & 76.62 & 774\,/\,804 \\
358	Random-weight & 75.87 & 764\,/\,804 \\
359	\bottomrule
360	\end{tabular}
361	\end{table}
362	
363	
364	\section{Remediation Strategy Details}
365	\label{app:remediation}
366	
367	\begin{table}[h]
368	\centering
369	\small
370	\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.49\%$, $\Delta = -0.98$\,pp. None reaches significance. Three method-level strategies are reported in Table~\ref{tab:method_interventions}.}
371	\label{tab:remediation}
372	\begin{tabular}{@{}llrl@{}}
373	\toprule
374	Strategy & Target & $\Delta$ (pp) & Key finding \\
375	\midrule
376	Contrastive$^a$ & Prompt & $-$1.10 & non-disc.\ 6.0\% ($\downarrow$ from 8.2\%) \\
377	Cross-model$^b$ & Architecture & 0.00 & disc.\ 0\% (weak$\to$strong); $\pm$1\,pp (strong$\to$weak) \\
378	Qwen3-14B$^c$ & Capability & $-$0.49 & $p = 0.655$ \\
379	Z3 feedback & Solver & --- & 0.9\% UNSAT trigger \\
380	Cons.\ filtering & Noise & 0.00 & $T{\geq}4 \to$ SC \\
381	Cross-trace UNSAT & Independence & --- & 56.4\% $\emptyset$ vars \\
382	$T{=}1.0$$^d$ & Diversity & 0.00 & isolated peak at $T{=}0.7$ only \\
383	Multi-temp$^e$ & Diversity & 0.00 & $b{=}5$, $c{=}5$ (balanced) \\
384	Disc.\ filtering$^f$ & Filtering & 0.00 & 803/804 agree w/ SICA \\
385	\bottomrule
386	\end{tabular}\\[2pt]
387	{\footnotesize $^a$\,$n{=}182$ (extraction failures excluded). $^b$\,Weak$\to$strong: Mistral-7B extracts from Qwen2.5-14B traces. Strong$\to$weak: Qwen3-14B (60.29\%) and Qwen2.5-14B (58.33\%) extract from Mistral-7B FOLIO traces ($n{=}204$); self-extraction baseline 59.31\%. $^c$\,$n{=}204$, SC $= 84.80\%$. $^d$\,Mistral-7B FOLIO, $n{=}204$. $^e$\,Mistral-7B FOLIO, $T \in \{0.3, 0.7, 1.2\}$, 4 traces each, $n{=}204$. $^f$\,Qwen2.5-14B, $n{=}804$; removing non-discriminative constraints.}
388	\end{table}
389	
390	
391	\begin{table}[h]
392	\centering
393	\small
394	\caption{Method-level interventions on Mistral-7B with McNemar's paired test. All produce neutral-to-catastrophic results. ICG shows two FOLIO seeds; $p$ for the first. {*}{*}{*}\,$p < 0.001$; {*}{*}\,$p < 0.01$.}
395	\label{tab:method_interventions}
396	\begin{tabular}{@{}ll rc rc@{}}
397	\toprule
398	& & \multicolumn{2}{c}{FOLIO ($n = 204$)} & \multicolumn{2}{c}{LogiQA ($n = 200$)} \\
399	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
400	Method & Target & $\Delta$ (pp) & $p$ & $\Delta$ (pp) & $p$ \\
401	\midrule
402	SC baseline & --- & 0.00 & --- & 0.00 & --- \\
403	ICG & Trace coupling & $-$1.96\,/\,$+$1.47 & .206 & $-$0.50 & .706 \\
404	Contrastive & Scoring bias & $\mathbf{-9.31}$ & .007 & $-$4.50 & .160 \\
405	Debate & Role diversity & $\mathbf{-18.63}$ & ${<}.001$ & $\mathbf{-23.00}$ & ${<}.001$ \\
406	\bottomrule
407	\end{tabular}
408	\end{table}
409	
410	\section{Additional Intervention Results}
411	\label{app:additional-interventions}
412	
413	\begin{table*}[h]
414	\centering
415	\small
416	\caption{Additional intervention results beyond the nine prompt-level and three method-level strategies reported in the main text. All produce neutral-to-negative results, completing the exhaustive remediation analysis across 22+ distinct approaches.}
417	\label{tab:additional_interventions}
418	\begin{tabular}{@{}llllrl@{}}
419	\toprule
420	\# & Method & Type & Target & $\Delta$ (pp) & Key Finding \\
421	\midrule
422	13 & PROVE (code verif.) & Paradigm & Formal proof & $-$1.9 & 15.2\% compilable; conclusive acc.\ = 50\% \\
423	14 & CEGIS (iterative) & Multi-round & Consistency & 0.0$^\dagger$ & R1 $+$3.43\,pp then oscillates \\
424	15 & DeepConf (logprob) & Filtering & Confidence & 0.0 & $\Delta_{\text{logprob}} = 0.006$ (no separation) \\
425	16 & Cross-model SICA & Cross-model & Independence & $-$0.49 & $\kappa_{\text{cross}}{=}0.42$ vs $\kappa_{\text{within}}{=}0.53$ \\
426	17 & Problem perturbation & Input diversity & Trace diversity & $<$0 & $\kappa$ \emph{increased} to 0.70 (anti-effect) \\
427	18 & MIN-UNSAT & Solver objective & Constraint sel.\ & $-$6.5 & Mean excluded constraints $= 1.3$ \\
428	19 & $\kappa$-aware SC & Voting rule & Weighted voting & 0.0 & 11/11 conditions $\Delta = 0$ \\
429	20 & Z3 trace filter & Trace filtering & Quality & $-$0.49 & Precision 49.1\%, 7 questions affected \\
430	21 & Bootstrapped gold & Iterative & Self-improvement & 0.0$^\dagger$ & R1 $+$2.45\,pp then oscillates \\
431	22 & Selective abstention & Diagnostic & Confidence & $+$4.4$^*$ & AUROC $= 0.673$, at 80\% coverage \\
432	23 & ASCII perturbation & Input diversity & Format diversity & 0.0 & $\kappa$: $0.39 \to 0.36$ (negligible) \\
433	\bottomrule
434	\end{tabular}\\[2pt]
435	{\footnotesize All experiments on Mistral-7B FOLIO ($n{=}204$) unless noted. $^\dagger$\,Oscillates without convergence; net effect $\approx 0$. $^*$\,Accuracy gain only at reduced coverage (diagnostic value, not a general improvement). Methods 1--12 are reported in Table~\ref{tab:remediation} and Table~\ref{tab:method_interventions}.}
436	\end{table*}
437	
438	\begin{figure*}[t]
439	\centering
440	\includegraphics[width=0.85\textwidth]{figures/fig_app_interventions_summary.pdf}
441	\caption{Summary of 22+ intervention strategies grouped by category. All produce neutral-to-negative accuracy changes relative to Self-Consistency. The LLM-Debate bar is truncated at $-11.5$\,pp (actual: $-18.6$\,pp). The grey band indicates $\pm 1$\,pp noise zone.}
442	\label{fig:interventions-summary}
443	\end{figure*}
444	
445	
446	\section{Extraction Error Taxonomy}
447	\label{app:extraction}
448	\label{sec:extraction-taxonomy}
449	
450	Constraints must discriminate between candidate answers for MAX-SAT to produce a ranking different from majority vote. We measure discriminative power at two levels on Qwen2.5-14B across FOLIO and ProofWriter ($n = 804$). At the source-trace level, 39.2\% of total constraint weight originates from traces whose answer differs from the plurality, but only 12.1\% of individual constraints fall into this minority category. At the Z3 semantic level, 91.8\% of constraints [95\% CI: 91.2, 92.4] are technically discriminative, producing different satisfiability outcomes when evaluated against different candidate answers. Only 8.2\% are non-discriminative.
451	
452	The high discriminative rate does not translate into accuracy gains because discrimination mirrors the model's own answer distribution. Each trace produces constraints with its own variable names, so Z3 treats identically-intended propositions as unrelated symbols; among cross-answer constraint pairs, 56.4\% share zero Z3 variables. This variable isolation means constraints from different traces are trivially jointly satisfiable, and MAX-SAT retains nearly all of them regardless of source answer. Removing the 8.2\% non-discriminative constraints yields zero accuracy improvement. The discriminative majority does not provide independent signal; it reinforces the majority answer that SC would already select. This confirmation bias, not a lack of discrimination, explains why SICA degenerates to majority voting (Appendix~\ref{app:ablation}).
453	
454	
455	\section{Hyperparameter Sensitivity}
456	\label{app:sensitivity}
457	\label{sec:k-sensitivity}
458	\label{sec:t-sensitivity}
459	
460	\subsection{K Sensitivity}
461	
462	Figure~\ref{fig:k-sensitivity} shows SICA $\Delta$ as a function of the number of sampled traces $K$ for Mistral-7B on FOLIO ($n = 204$, no fixed seed). The relationship is non-monotonic: $K = 4$ yields $\Delta = -1.47$\,pp, $K = 8$ yields $\Delta = -1.96$\,pp, $K = 12$ reaches $\Delta = +3.43$\,pp, $K = 16$ drops to $\Delta = +1.47$\,pp, and $K = 20$ partially recovers to $\Delta = +1.96$\,pp. The recovery at $K = 20$ rules out a simple peaked pattern, but $K = 12$ remains the only setting with $\Delta > 2$\,pp ($p = 0.092$, marginal).
463	
464	The apparent $\Delta$ peak at $K = 12$ is confounded with SC baseline. SICA absolute accuracy plateaus at 59.31\% (121/204) for $K \geq 12$: identical at $K = 12$ and $K = 20$. The $\Delta$ variation across these settings is driven primarily by SC fluctuations rather than by SICA improvement. $K = 12$ produces a relatively low SC (55.88\%), placing it in the intermediate-SC region; $K = 8$ (SC $= 58.33\%$) and $K = 20$ (SC $= 57.35\%$) have higher baselines, compressing $\Delta$ even though SICA accuracy does not change for $K \geq 12$. Additional traces beyond $K = 12$ provide no benefit to SICA absolute performance, consistent with the constraint quality bottleneck. The $K = 12$ $\Delta$ captures only 24.1\% of the oracle ceiling ($+14.22$\,pp).
465	
466	\begin{figure}[h]
467	\centering
468	\includegraphics[width=\columnwidth]{f3_k_sensitivity}
469	\caption{SICA $\Delta$ (pp) vs.\ number of traces $K$ for Mistral-7B on FOLIO ($n = 204$, default seed, $T = 0.7$). Non-monotonic pattern: SICA accuracy plateaus at 59.31\% for $K \geq 12$; the apparent $\Delta$ peak at $K = 12$ partly reflects a relatively low SC baseline (55.88\%) at that point. Error bars: 95\% bootstrap CI.}
470	\label{fig:k-sensitivity}
471	\end{figure}
472	
473	\subsection{Temperature Sensitivity}
474	
475	Temperature sensitivity on Mistral-7B FOLIO ($n = 204$, default seed) reveals a sharp isolated peak rather than a smooth trend. Across four temperature settings, only $T = 0.7$ produces a positive effect: $T = 0.3$ yields $\Delta = -1.47$\,pp (SC $= 58.33\%$), $T = 0.5$ yields $\Delta = -0.98$\,pp (SC $= 58.33\%$), $T = 0.7$ yields $\Delta = +3.43$\,pp (SC $= 55.88\%$), and $T = 1.0$ yields $\Delta = 0.00$\,pp (SC $= 55.39\%$). All other temperatures yield negative or null effects, and the single positive result at $T = 0.7$ is confounded with SC baseline. Combined with the seed sensitivity (0 of 4 seeds reaching $p < 0.05$ at $T = 0.7$), the positive trend depends on a specific combination of temperature, seed, and baseline accuracy that same-model sampling rarely achieves.
476	
477	The parallel between $K$ and $T$ sensitivity points to a common underlying variable. In both sweeps, the setting that produces the largest SICA gain also produces a relatively low SC baseline (55.88\%), which places it in the intermediate-SC region. The hyperparameters themselves ($K$, $T$) are not the causal driver; they modulate SC level, and it is the SC level that determines whether SICA has operating room.
478	
479	
480	\section{Entropy Decomposition}
481	\label{app:entropy}
482	\label{sec:entropy}
483	
484	We partition problems by trace agreement: high-entropy (majority count $\leq 8$ out of $K = 12$) and low-entropy (majority count $\geq 9$). Table~\ref{tab:entropy} reports SICA $\Delta$ within each partition across eight model-dataset conditions.
485	
486	\begin{table}[h]
487	\centering
488	\small
489	\caption{Entropy decomposition of SICA $\Delta$ (pp). High-entropy: majority count $\leq 8$; low-entropy: majority count $\geq 9$. $^\dagger$Partial data (180/600). Pre-tiebreaking SC values; pattern robust to D064 correction.}
490	\label{tab:entropy}
491	\begin{tabular}{@{}llrrrr@{}}
492	\toprule
493	Model & Dataset & \multicolumn{2}{c}{High-entropy} & \multicolumn{2}{c}{Low-entropy} \\
494	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
495	 & & $n$ & $\Delta$ & $n$ & $\Delta$ \\
496	\midrule
497	Mistral-7B & FOLIO & 78 & $\mathbf{+12.8}$ & 126 & 0.0 \\
498	Mistral-7B (s123) & FOLIO & 77 & $\mathbf{+9.1}$ & 127 & 0.0 \\
499	Mistral-7B (s456) & FOLIO & 75 & $-$1.3 & 129 & 0.0 \\
500	Mistral-7B & PW-D5 & 267 & $-$4.9 & 333 & $-$1.2 \\
501	Qwen2.5-14B & FOLIO & 37 & $-$8.2 & 167 & $-$0.6 \\
502	Qwen2.5-14B & LogiQA & 23 & $-$4.3 & 177 & 0.0 \\
503	Qwen2.5-7B & FOLIO & 47 & $-$2.1 & 157 & 0.0 \\
504	LLaMA-3.1-8B$^\dagger$ & PW-D5 & 76 & $-$3.9 & 104 & $-$1.9 \\
505	\bottomrule
506	\end{tabular}
507	\end{table}
508	
509	Two patterns emerge. First, low-entropy problems produce $\Delta \approx 0$\,pp across all eight conditions: when traces agree, constraints carry no information beyond the majority vote.
510	
511	Second, the direction of SICA's effect on high-entropy problems depends on the accuracy regime, not on entropy alone. In the intermediate-SC region (Mistral-7B on FOLIO, default-seed and seed-123 runs), high-entropy $\Delta$ reaches $+12.8$ and $+9.1$\,pp: traces genuinely disagree, and constraints from correct-answer traces provide discriminative signal that resolves the disagreement. In Type~A conditions (Qwen2.5-14B on FOLIO, $\Delta = -8.2$\,pp), high-entropy problems represent rare deviations from a strong model's consensus; constraints inherit the model's confirmation bias. In Type~C (Mistral-7B on ProofWriter, $\Delta = -4.9$\,pp), high-entropy problems reflect systematic errors. The mechanism is not entropy per se but the interaction of entropy with model capability.
512	
513	
514	\section{Failure Mode Analysis}
515	\label{app:failure-modes}
516	\label{sec:failure-modes}
517	
518	The regime-dependent pattern in Table~\ref{tab:main_results} reflects three distinct failure modes of self-extracted symbolic constraints.
519	
520	\paragraph{Type A: confirmation bias (SC $\geq$ $\sim$60\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\mathcal{C}^{\setminus}| \approx 0$), the penalty term in Eq.~\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in Appendix~\ref{app:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.
521	
522	\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean FOL formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\%, but the resulting constraints have a contradiction rate of only 0.8\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (51.00\%) yet produces $\Delta = +0.50$\,pp ($p = 1.0$); Qwen2.5-14B on the same domain yields $\Delta = -0.50$\,pp ($p = 1.0$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.
523	
524	\paragraph{Type C: error amplification (SC $\leq$ $\sim$40\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\Delta = -2.83$\,pp, $p = 0.014$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.
525	
526	
527	\section{Cross-Model Confirmation Bias}
528	\label{app:cross-model-bias}
529	
530	Table~\ref{tab:cross-model-bias} reports confirmation bias metrics across three model families on FOLIO ($n = 204$). Bias ratio, error constraint percentage, and SICA-follows-SC overlap all decrease with model capability, but remain substantially above chance across all families.
531	
532	\begin{table}[h]
533	\centering
534	\small
535	\caption{Cross-model confirmation bias on FOLIO ($n = 204$). Bias ratio: ratio of error-supporting constraints on incorrect vs.\ correct problems. Error Constraint \%: fraction of constraints supporting the wrong majority on incorrect problems. SICA$\to$SC: fraction of SICA errors that overlap with SC errors. $^{\dag}$Based on 4 of 12 traces due to extraction failures.}
536	\label{tab:cross-model-bias}
537	\begin{tabular}{@{}llrrr@{}}
538	\toprule
539	Model & Dataset & Bias Ratio & Error Cstr.\ \% & SICA$\to$SC \\
540	\midrule
541	Mistral-7B & FOLIO & $4.97\times$ & 83.3\% & 94.0\% \\
542	Qwen2.5-14B & FOLIO & $3.93\times$ & 79.7\% & 90.4\% \\
543	LLaMA-3.1-8B$^{\dag}$ & FOLIO & $2.88\times$ & 74.3\% & 78.2\% \\
544	\bottomrule
545	\end{tabular}
546	\end{table}
547	
548	
549	\section{Independence-Accuracy Scatter Plot}
550	\label{app:kappa-scatter}
551	
552	\begin{figure}[h]
553	\centering
554	\includegraphics[width=\columnwidth]{figures/f6_kappa_accuracy_scatter}
555	\caption{Independence-accuracy trade-off across aggregation methods (Mistral-7B, filled markers) and model families (LLaMA-3.1-8B, Qwen2.5-7B, Qwen2.5-14B; open markers) on FOLIO ($n = 204$). Same-model methods cluster at $\kappa \approx 0.40$--$0.47$ (gray band), while cross-model SC shows stronger correlations ($\kappa = 0.41$--$0.74$) at higher accuracy. Debate breaks correlation ($\kappa = 0.15$) at catastrophic accuracy cost. Dashed line: Mistral-7B SC baseline.}
556	\label{fig:kappa-accuracy}
557	\end{figure}
558	
559	\section{Cross-Model Kappa Analysis}
560	\label{app:cross-model-kappa}
561	
562	Table~\ref{tab:cross_model_kappa} compares trace independence across three model families on the same benchmarks. On FOLIO ($n = 204$), all four models produce $\kappa \geq 0.41$: LLaMA-3.1-8B ($\kappa = 0.41$), Mistral-7B ($\kappa = 0.44$), Qwen2.5-7B ($\kappa = 0.66$), and Qwen2.5-14B ($\kappa = 0.74$). The bottleneck is architecture-independent---no family escapes the correlation floor. Within the Qwen family, $\kappa$ increases from 0.66 (7B) to 0.74 (14B), but Mistral-7B (7B) and LLaMA-3.1-8B (8B) differ by $\Delta\kappa = 0.03$ despite belonging to different families, suggesting that cross-family variation ($\Delta\kappa$ up to 0.22 at similar scale) exceeds within-family scale effects ($\Delta\kappa = 0.08$). Disentangling scale from architecture requires controlled same-family experiments across $\geq$3 scales.
563	
564	\begin{table}[h]
565	\centering
566	\small
567	\caption{Cross-model trace independence ($K = 12$, SC aggregation, FOLIO + ProofWriter). Higher $\kappa$ indicates stronger correlation and lower effective sample size.}
568	\label{tab:cross_model_kappa}
569	\begin{tabular}{@{}llccr@{}}
570	\toprule
571	Model & Dataset & $\kappa$ & $K_{\text{eff}}$ & SC (\%) \\
572	\midrule
573	Qwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.49 \\
574	Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 \\
575	Mistral-7B & FOLIO & 0.44 & 2.02 & 56.86 \\
576	LLaMA-3.1-8B & FOLIO & 0.41 & 2.17 & 66.18 \\
577	\addlinespace
578	Qwen2.5-14B & PW-D5 & 0.62 & 1.54 & --- \\
579	Mistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 \\
580	\bottomrule
581	\end{tabular}
582	\end{table}
583	
584	
585	\section{Cross-Model Process-Level Independence}
586	\label{app:cross-model-process}
587	
588	Table~\ref{tab:cross-model-process} extends the process-level independence analysis (\S\ref{sec:process-kappa}) to four model families on FOLIO ($n = 204$). Mean pairwise cosine similarity of TF-IDF trace representations exceeds answer-level $\kappa$ in every family, but the gap is model-strength dependent: it narrows from $0.31$ (LLaMA) and $0.23$ (Mistral) to $0.02$ (Qwen-14B). For weaker models ($r \approx 0$), answer diversity does not reflect reasoning diversity---process-convergent but answer-divergent trace pairs constitute 9.5\% of all pairs on Mistral-7B versus 2.5--3.2\% on other families. For stronger models ($r \approx 0.23$, $p \leq 0.001$), process and answer agreement align, and answer-level $\kappa$ already captures the bottleneck. Process-$\kappa$ thus provides a crucial additional diagnostic specifically for weaker models, where answer-level metrics underestimate reasoning homogeneity.
589	
590	\begin{table}[h]
591	\centering
592	\small
593	\caption{Cross-model process-level independence on FOLIO ($n = 204$, $K = 12$). Mean Cosine: mean pairwise TF-IDF cosine similarity of reasoning traces (Eq.~\ref{eq:process-sim}). Answer $\kappa$: per-question answer agreement. Gap: Cosine $-$ $\kappa$. $r$: Pearson correlation between ProcessSim and answer agreement. Conv.: fraction of process-convergent but answer-divergent trace pairs. {*}{*}\,$p < 0.01$; {*}{*}{*}\,$p < 0.001$.}
594	\label{tab:cross-model-process}
595	\begin{tabular}{@{}lcccrlr@{}}
596	\toprule
597	Model & Mean Cos. & Ans.\ $\kappa$ & Gap & $r$ & $p$ & Conv.\ (\%) \\
598	\midrule
599	Mistral-7B & 0.690 & 0.460 & 0.230 & $-$0.064 & 0.362 & 9.5 \\
600	LLaMA-3.1-8B & 0.759 & 0.447 & 0.312 & $-$0.001 & 0.985 & 3.2 \\
601	Qwen2.5-7B & 0.790 & 0.658 & 0.132 & $+$0.226 & 0.001{*}{*} & 2.8 \\
602	Qwen2.5-14B & 0.766 & 0.744 & 0.022 & $+$0.244 & ${<}$0.001{*}{*}{*} & 2.5 \\
603	\bottomrule
604	\end{tabular}
605	\end{table}
606	
607	
608	\section{Constraint Quality Across Methods}
609	\label{app:constraint-quality}
610	
611	Table~\ref{tab:constraint_quality} compares constraint quality metrics across the three method-level interventions on Mistral-7B FOLIO ($n = 204$). Standard SICA extracts from reasoning traces and achieves the highest parse rate (97.1\%) but also the highest redundancy (42.9\%): nearly half of all constraints are syntactic duplicates across the 12 traces, quantifying the co-sourcing effect of same-model generation. ICG generates constraints directly from the problem statement without trace conditioning. Its lower parse rate (74.6\%) reflects the difficulty of standalone formalization at the 7B scale, though successfully parsed constraints compile at a higher rate (99.4\% vs.\ 96.5\%). ICG produces fewer unique constraints per question (24.9 vs.\ 39.3) with lower redundancy (32.3\%), consistent with the absence of trace-level repetition. Contrastive scoring generates pro and con constraint sets for each candidate answer. The format yields far fewer unique constraints per question (9.2) with zero redundancy (each pro/con pair is structurally distinct), but 62.7\% of constraints are trivially satisfied by Z3---they impose no logical tension and cannot discriminate between candidates. Only 51.0\% of Contrastive constraints are discriminative, compared to 81.4\% for standard SICA and 77.0\% for ICG.
612	
613	\begin{table}[h]
614	\centering
615	\small
616	\caption{Constraint quality metrics across method-level interventions (Mistral-7B, FOLIO, $n = 204$). Parse: fraction of extraction attempts yielding valid JSON. Z3 Compile: fraction compiling to Z3 formulas. Unique/q: mean unique constraints per question. Redundancy: fraction of constraints duplicated across traces. Disc.: fraction discriminative (different Z3 outcome per candidate). Triv.\ Sat.: fraction trivially satisfied (no logical tension).}
617	\label{tab:constraint_quality}
618	\begin{tabular}{@{}l rrrrrr@{}}
619	\toprule
620	Method & Parse & Z3 & Uniq/q & Redund. & Disc. & Triv.\ Sat. \\
621	\midrule
622	Standard SICA & 97.1\% & 96.5\% & 39.3 & 42.9\% & 81.4\% & --- \\
623	ICG & 74.6\% & 99.4\% & 24.9 & 32.3\% & 77.0\% & --- \\
624	Contrastive & 74.0\% & 94.4\% & 9.2 & 0.0\% & 51.0\% & 62.7\% \\
625	\bottomrule
626	\end{tabular}
627	\end{table}
628	
629	
630	\section{Error Categorization of Method-Level Interventions}
631	\label{app:error-categorization}
632	
633	We categorize discordant predictions (where the method and SC disagree) for Debate and Contrastive on FOLIO ($n = 204$) to understand why these interventions degrade accuracy.
634	
635	\paragraph{Debate discordant analysis.} Debate produces 60 correct$\to$wrong flips and 22 wrong$\to$correct flips on FOLIO. Answer-type breakdown reveals that False-labeled questions are most vulnerable: 82.8\% of False questions that SC answers correctly are flipped by Debate, compared to 63.9\% for True and 25.5\% for Unknown. Counterintuitively, failures concentrate not where debate breaks down but where it succeeds most thoroughly: discordant questions average 2.93 effective debate rounds (proposer-critic exchanges producing substantive updates) versus 2.52 for concordant ones. More extensive same-model debate produces more confident but incorrect constraints, consistent with the independence bottleneck---the critic draws on the same model distribution as the proposer, reinforcing shared biases rather than correcting them.
636	
637	\paragraph{Contrastive discordant analysis.} Contrastive produces 34 discordant questions on FOLIO. All 34 produced non-degenerate scores (both pro and con constraint sets non-empty), compared to 20.1\% degenerate scores in the full sample. This indicates that scoring failures on discordant questions stem from systematic pro-bias rather than missing constraints. Among discordant questions, 97.1\% contain negation words in the problem statement versus 76.5\% in the full sample, suggesting that negation-bearing problems are particularly susceptible to pro-constraint imbalance. The average pro/con score ratio is 1.0 for discordant questions versus 0.68 for the full sample: the method generates balanced-looking scores that mask directional errors.
638	
639	\paragraph{Cross-method overlap.} Of the 79 unique questions on which either method disagrees with SC, only 15 overlap between Debate and Contrastive (Jaccard index $= 0.19$). All 15 shared discordant questions contain negation words. The low overlap confirms that the two methods attack different vulnerability types---Debate through extended same-model argumentation that amplifies confident errors, Contrastive through pro-bias in constraint generation---while sharing a common root cause in the independence bottleneck: both methods rely on the same model's output distribution and cannot introduce genuinely independent signal.
640	
641	
642	\section{Extended Limitations}
643	\label{app:limitations-extended}
644	
645	Beyond the limitations discussed in the main text, several additional constraints bound our conclusions. Seven of our eleven model-domain conditions have $n \leq 60$, providing insufficient statistical power for confirmatory claims; power analysis shows that the minimum detectable effect exceeds 5\,pp for these conditions (Table~\ref{tab:power}), so they serve as regime characterization rather than definitive tests. Our extraction prompts use a single zero-shot template per domain; alternative prompting strategies (few-shot exemplars, chain-of-thought extraction, or iterative refinement) might yield higher-quality constraints, though the oracle gap suggests the bottleneck is fundamental rather than prompt-specific. The constraint quality analysis (91.8\% discriminative rate, 39.2\% source-trace minority weight) covers Qwen2.5-14B on FOLIO + ProofWriter ($N = 804$); other model-domain combinations may exhibit different characteristics. Constraint extraction uses $T_{\text{ext}} = 0.3$ while trace sampling uses $T = 0.7$; alternative extraction temperatures might yield different results. Although we prompt for FOL-style formalizations, extracted constraints are predominantly propositional ground clauses without quantifiers (\S\ref{sec:constraint-extraction}); whether models capable of genuine quantified FOL would yield higher discriminative rates is untested. Deduplication uses syntactic equivalence, so semantically equivalent constraints with different surface forms receive separate weights. The GSM8K pilot ($n = 30$) illustrates the constraint-absent regime and should not be interpreted as confirmatory evidence.
646	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "417cc6e3-0cc6-4ed4-a8e4-f8ce306a38d0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
      "content": "\n\\section{Prompt Templates}\n\\label{app:prompts}\n\nSICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).\n\n\\paragraph{System Prompt.}\n\n\\begin{lstlisting}\nYou are a constraint extraction tool. Output ONLY\nvalid JSON. Do NOT solve problems, reason about\ncorrectness, or think step-by-step. Extract\nconstraints from the given trace exactly as stated.\n\\end{lstlisting}\n\n\\paragraph{Mathematical Constraint Extraction (EXTRACTION\\_PROMPT).}\n\nUsed for GSM8K and AIME datasets. The placeholder \\texttt{\\{trace\\}} is replaced with the reasoning trace at runtime.\n\n\\begin{lstlisting}\nExtract mathematical constraints from this reasoning\ntrace as a JSON object.\n\nRules:\n- type: \"equation\", \"inequality\", or \"predicate\"\n- expression: human-readable, e.g. \"x + y == 14\"\n- z3_formula: a single comparison expression in\n  Python Z3 syntax\n- source_step: step number where the constraint\n  appears\n- Use variable names from the trace\n\nz3_formula MUST follow these rules:\n- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,\n  /, **, %\n- Use individual named variables: a1, a2, a3...\n  NOT arrays a[1] or sets A\n- Expand all sums explicitly:\n  \"a1 + a2 + a3 == 55\" NOT \"sum([a1,a2,a3])\"\n- NO Python builtins: sum(), len(), max(), min(),\n  list(), set(), range(), int()\n- Each z3_formula must be exactly ONE comparison\n  (==, !=, <, >, <=, >=)\n- For multiple values, write separate constraints\n  for each\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"equation\",\n  \"expression\": \"x + y == 14\",\n  \"z3_formula\": \"x + y == 14\",\n  \"source_step\": 1}],\n \"answer\": \"final_answer\",\n \"variables\": [\"x\", \"y\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Logical Constraint Extraction (LOGIC\\_EXTRACTION\\_PROMPT).}\n\nUsed for ProofWriter and FOLIO datasets.\n\n\\begin{lstlisting}\nIMPORTANT: You are an EXTRACTION tool, NOT a problem\nsolver.\n- Do NOT re-solve or re-reason about the problem.\n- Do NOT verify whether the trace's reasoning is\n  correct.\n- ONLY extract the logical constraints that are\n  explicitly stated or used in the trace below.\n- Output ONLY the JSON object, nothing else.\n\nExtract logical constraints from this reasoning trace\nabout a logic problem.\n\nThe problem has facts (base assertions), rules\n(grounded implications), and derived conclusions.\nConvert each into a Z3 boolean formula.\n\nVariable naming:\n- Unary property: property_entity\n  (e.g., kind_anne, red_charlie, round_fiona)\n- Binary relation: relation_subject_object\n  (e.g., eats_bear_squirrel, likes_lion_cat)\n- Use lowercase with underscores only\n\nConstraint types:\n- \"fact\": a given assertion,\n  e.g., kind_anne == True\n- \"rule\": a grounded implication over specific\n  entities, e.g., Implies(kind_anne, nice_anne)\n- \"derived\": an inferred conclusion from facts +\n  rules, e.g., nice_anne == True\n\nZ3 operators:\n- Implies(a, b) for if-then rules\n- And(a, b, ...) for conjunctive conditions\n- Or(a, b, ...) for disjunctive conditions\n- Not(a) for negation\n- == True / == False for boolean assertions\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"fact\",\n  \"expression\": \"kind(anne)\",\n  \"z3_formula\": \"kind_anne == True\",\n  \"source_step\": 1}],\n \"answer\": \"True or False or Unknown\",\n \"variables\": [\"kind_anne\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Output Schema.}\n\nBoth prompts produce a JSON object with the following structure:\n\n\\begin{lstlisting}\n{\n  \"constraints\": [\n    {\n      \"type\": \"&lt;equation|inequality|predicate>\n               or &lt;fact|rule|derived>\",\n      \"expression\": \"&lt;human-readable description>\",\n      \"z3_formula\": \"&lt;Z3-compatible expression>\",\n      \"source_step\": &lt;integer>\n    }\n  ],\n  \"answer\": \"&lt;final answer string>\",\n  \"variables\": [\"&lt;var1>\", \"&lt;var2>\", \"...\"]\n}\n\\end{lstlisting}\n\nThe pipeline additionally injects an \\texttt{answer\\_assertion} constraint per trace (not produced by the LLM):\n\n\\begin{lstlisting}\n{\"type\": \"answer_assertion\",\n \"expression\": \"answer is &lt;ans>\",\n \"z3_formula\": \"__sica_answer_&lt;ans> == True\",\n \"source_step\": -1}\n\\end{lstlisting}\n\n\\paragraph{Prompt Selection Logic.}\n\nDomain assignment is determined by dataset: FOLIO and ProofWriter use \\textsc{Logic\\_Extraction\\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \\textsc{Extraction\\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.\n\n\n\\section{Z3 MaxSAT Evaluation Pseudocode}\n\\label{app:z3-pseudocode}\n\nAlgorithm~\\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\\ref{alg:scorer} describes the source-trace attribution scoring.\n\nDomain constraint variables (e.g., \\texttt{x + y == 14}) and answer assertion variables (e.g., \\texttt{\\_\\_sica\\_answer\\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.\n\n\\begin{algorithm}[h]\n\\caption{Z3 Weighted Partial MAX-SAT}\n\\label{alg:maxsat}\n\\begin{algorithmic}[1]\n\\Require Deduplicated constraint set $\\mathcal{C} = \\{(c_m, w_m, S_m)\\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices\n\\Ensure Partition $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$ where $\\mathcal{C}^*$ is the max-weight satisfiable subset\n\\State $\\textit{opt} \\gets \\textsc{Z3.Optimize()}$\n\\For{$m = 1, \\ldots, M$}\n    \\State $b_m \\gets$ fresh Boolean indicator\n    \\State $\\textit{opt}.\\textsc{Add}(b_m \\Rightarrow c_m)$ \\Comment{soft clause guarded by indicator}\n    \\State $\\textit{opt}.\\textsc{AddSoft}(b_m,\\; \\text{weight}=w_m)$\n\\EndFor\n\\State $\\textit{result} \\gets \\textit{opt}.\\textsc{Check}()$\n\\State $\\textit{model} \\gets \\textit{opt}.\\textsc{Model}()$\n\\State $\\mathcal{C}^* \\gets \\{(c_m, w_m, S_m) : \\textit{model}(b_m) = \\top\\}$\n\\State $\\mathcal{C}^{\\setminus} \\gets \\mathcal{C} \\setminus \\mathcal{C}^*$\n\\State \\Return $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\begin{algorithm}[h]\n\\caption{Source-Trace Attribution Scoring}\n\\label{alg:scorer}\n\\begin{algorithmic}[1]\n\\Require Satisfied set $\\mathcal{C}^*$, excluded set $\\mathcal{C}^{\\setminus}$, candidate answers $\\mathcal{A}$, trace-answer mapping $\\tau: \\text{trace\\_idx} \\to a$, penalty weight $\\alpha$\n\\Ensure Score $s(a)$ for each $a \\in \\mathcal{A}$\n\\For{each $a \\in \\mathcal{A}$}\n    \\State $T_a \\gets \\{i : \\tau(i) = a\\}$ \\Comment{trace indices producing answer $a$}\n    \\State $\\textit{pos}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^*} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $\\textit{neg}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^{\\setminus}} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $s(a) \\gets \\textit{pos}(a) - \\alpha \\cdot \\textit{neg}(a)$\n\\EndFor\n\\State \\Return $a^* = \\arg\\max_{a \\in \\mathcal{A}} s(a)$\n\\end{algorithmic}\n\\end{algorithm}\n\n\n\\section{Capability Trap Diagnostics}\n\\label{app:diagnostics}\n\nTable~\\ref{tab:capability_trap} reports per-condition diagnostic metrics referenced in \\S\\ref{sec:entropy}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Domain & $C_0$ (\\%) & Extr.\\ Rate & Contr.\\ Rate & $\\Delta$ (pp) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 35.3 & 0.89 & 0.022 & 0.00 \\\\\nQwen2.5-14B & ProofWriter & 39.2 & 0.89 & 0.022 & $+$0.33 \\\\\nQwen2.5-14B & StrategyQA$^\\dagger$ & 10.0 & 0.70 & --- & $+$3.33 \\\\\nQwen2.5-14B & ARC-Chall.$^\\dagger$ & 5.0 & 1.00 & --- & $-$1.67 \\\\\nQwen2.5-7B & FOLIO+PW$^\\dagger$ & 42.1 & 0.94 & 0.027 & 0.00 \\\\\nMistral-7B & FOLIO+PW$^\\dagger$ & 50.0 & 0.88 & 0.056 & 0.00 \\\\\nLLaMA-3.1-8B & StrategyQA & 41.0 & --- & --- & $+$2.00 \\\\\nLLaMA-3.1-8B & FOLIO & 61.8 & 0.94 & 0.062 & $-$4.41 \\\\\nDeepSeek-R1-7B & FOLIO+PW$^\\dagger$ & 58.3 & 0.84 & 0.037 & $-$3.33 \\\\\nQwQ-32B & Combined$^\\dagger$ & 2.6 & --- & --- & 0.00 \\\\\nQwen2.5-14B & GSM8K$^\\dagger$ & 13.3 & 0.15 & --- & 0.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Capability trap diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable FOL constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\\Delta$: SICA$-$SC gap (pp). $\\dagger$: $n \\leq 60$. Dashes indicate conditions where extraction diagnostics were not computed (StrategyQA uses boolean answers without FOL extraction; QwQ-32B Combined had near-zero $C_0$, making extraction analysis uninformative). This table includes additional exploratory conditions not reported in Table~\\ref{tab:main_results}.}\n\\label{tab:capability_trap}\n\\end{table}\n\n\n\\section{Statistical Power Analysis}\n\\label{app:power}\n\nWe compute the minimum detectable effect (MDE) for each condition at $\\alpha = 0.05$ and 80\\% power using exact binomial power calculations over McNemar discordant pairs. Table~\\ref{tab:power} reports three grouped conditions with $n \\geq 200$ (Qwen2.5-14B FOLIO and ProofWriter are pooled into a single $n{=}804$ analysis, corresponding to four Table~\\ref{tab:main_results} rows), which constitute our confirmatory analyses. The remaining seven conditions ($n \\leq 60$) yield infinite MDE due to insufficient discordant pairs and serve only as regime characterization.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{MDE} & \\textbf{Obs.\\ $\\Delta$} & \\textbf{Obs.\\ Pow.} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & 1.86pp & $+$0.25pp & 5.7\\%  \\\\\nLLaMA-8B StrategyQA  & 200 & 4.64pp & $+$2.00pp & 20.6\\% \\\\\nLLaMA-8B FOLIO       & 204 & 4.84pp & $-$4.41pp & 18.6\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Power analysis for confirmatory conditions ($n \\geq 200$). MDE = minimum detectable effect at 80\\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\\% in every case.}\n\\label{tab:power}\n\\end{table}\n\nThe largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.\n\n\n\\section{Bootstrap Confidence Intervals}\n\\label{app:bootstrap}\n\nWe compute 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ via 10{,}000 bootstrap resamples (percentile method, seed 42). Table~\\ref{tab:bootstrap} reports the results for the three confirmatory conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{Obs.\\ $\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & $+$0.25pp & [$-$1.12, $+$1.62] \\\\\nLLaMA-8B StrategyQA  & 200 & $+$2.00pp & [$-$1.50, $+$5.50] \\\\\nLLaMA-8B FOLIO       & 204 & $-$4.41pp & [$-$5.88, $+$0.98] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bootstrap 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ in percentage points. All intervals include zero, consistent with no reliable accuracy difference.}\n\\label{tab:bootstrap}\n\\end{table}\n\nAll three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that symbolic constraint aggregation improves over majority voting.\n\n\n\\section{Case Studies: Discordant Predictions}\n\\label{app:case-studies}\n\nAmong 804 problems, SICA and SC agree on 773 (96.1\\%). The 31 discordant cases comprise 16 SICA wins (SICA correct, SC wrong), 14 SC wins (SC correct, SICA wrong), and 1 where both select different wrong answers. All 31 occur at exact ties (entropy${=}1.0$, 6:6 vote split) or near-ties (entropy${\\geq}0.9183$, 8:4 at most), since SICA can differ from SC only when constraint weights shift the majority away from SC's tiebreak choice. We present three representative cases that illustrate the mechanism behind capability trap failures.\n\n\\paragraph{Case 1: SICA Wins (folio\\_134, FOLIO).}\n\n\\emph{Premises}: Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth. \\emph{Conclusion}: Humans are mammals. \\emph{Gold}: Unknown.\n\nThe premises state that \\emph{some} mammals have teeth and that humans have teeth, but ``having teeth'' is not sufficient for ``being a mammal'' under open-world semantics. SC produces a 6:6 split (Unknown:6, True:6) and tiebreaks alphabetically to True (wrong). SICA extracts 7 constraints; MaxSAT excludes 1 constraint inconsistent with the rest, reducing the weighted score for True-voting traces and tipping the aggregation to Unknown (correct). The excluded constraint likely captured an incorrect inference step (e.g., affirming the consequent) present only in True-voting traces. While SICA succeeds here, the success is coincidental: the excluded constraint happens to anti-correlate with the correct answer.\n\n\\paragraph{Case 2: SC Wins (ProofWriter-1066\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: White(Bob)$\\to$Round(Bob) [white things are round] $\\to$ Young(Bob) [all round things are young]. \\emph{Conclusion}: ``Bob is not young.'' \\emph{Gold}: False (Bob IS young).\n\nSC produces a 6:6 split (False:6, True:6) and tiebreaks to False (correct). SICA extracts 17 constraints; MaxSAT excludes 2 that appear preferentially in False-voting traces. These excluded constraints likely captured correct intermediate derivations (e.g., \\texttt{young\\_bob == True}) that appeared only in traces completing the full deduction chain. By excluding them, MaxSAT removes evidence supporting the correct answer. SICA selects True (wrong). This case illustrates how self-extracted constraints can systematically mislead: correct reasoning steps become discriminative signals that the solver mistakenly penalizes.\n\n\\paragraph{Case 3: Non-discriminative Constraints (ProofWriter-903\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: Nice(Mouse)$\\to$Cold(Mouse) [all nice people are cold] $\\to$ Chases(Mouse,Mouse) [nice and cold $\\to$ chase mouse]. \\emph{Conclusion}: ``The mouse does not chase the mouse.'' \\emph{Gold}: False.\n\nSC produces a 6:6 split (False:6, Unknown:6) and tiebreaks to False (correct). SICA extracts 44 constraints but excludes only 1 (2.3\\%). The remaining 43 are domain facts and grounded rules (\\texttt{nice\\_mouse == True}, \\texttt{Implies(nice\\_mouse, cold\\_mouse)}, etc.) that Z3 satisfies identically regardless of the final answer. Both False-voting and Unknown-voting traces share the same premises and grounded rules; they differ only in whether the trace completed the full derivation chain. The single excluded constraint carries negligible weight against 43 shared constraints, so SICA collapses to SC.\n\n\\paragraph{Pattern.}\n\nThese cases exemplify the general pattern across the 773 agreeing problems: the vast majority of extracted constraints encode shared domain structure rather than answer-specific reasoning, and MaxSAT aggregation degenerates to majority vote. Table~\\ref{tab:case_summary} summarizes.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Summary of three representative discordant cases. All occur at exact 6:6 vote ties. Constraint exclusion can break ties in either direction (Cases 1--2) or have no effect (Case 3).}\n\\label{tab:case_summary}\n\\begin{tabular}{@{}lllcccc@{}}\n\\toprule\nCase & ID & Gold & SC & SICA & \\#Constr. & Excl.\\ (\\%) \\\\\n\\midrule\n1 (SICA win) & folio\\_134 & Unknown & True $\\times$ & Unknown $\\checkmark$ & 7 & 1 (14.3\\%) \\\\\n2 (SC win) & PW-1066\\_Q6 & False & False $\\checkmark$ & True $\\times$ & 17 & 2 (11.8\\%) \\\\\n3 (Non-disc.) & PW-903\\_Q6 & False & False $\\checkmark$ & False $\\checkmark$ & 44 & 1 (2.3\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{ProofWriter Oracle Per-Subtype Analysis}\n\\label{app:pw-oracle-subtype}\n\nProofWriter problems encode deductive rules as Domain-Specific Language (DSL) logic programs. Each problem uses one of four predicate subtypes: attribute predicates with or without negation (AttNeg, AttNoneg), and relation predicates with or without negation (RelNeg, RelNoneg). Relation predicates involve binary relations between entities (e.g., \\texttt{eats(bear, squirrel)}), while attribute predicates assign unary properties (e.g., \\texttt{kind(anne)}).\n\nThe oracle pipeline parses these DSL annotations deterministically into Z3 formulas without any LLM involvement. Of the 600 ProofWriter problems, 594 (99.0\\%) produce valid Z3 parses; the remaining 6 fail due to unsupported DSL constructs. Across all 7{,}128 trace-problem pairs submitted to Z3, the solver returns a result in every case (0\\% solver errors). Z3 evaluations agree with ground-truth labels on 577 of 594 parseable problems (97.14\\%), confirming that the deterministic DSL-to-Z3 translation faithfully preserves problem semantics.\n\nTable~\\ref{tab:pw_oracle_subtype} reports the per-subtype breakdown. Relation-predicate subtypes show substantially larger gains than attribute-predicate subtypes: RelNeg improves by $+17.86$~pp and RelNoneg by $+13.01$~pp, compared to $+9.09$~pp for AttNoneg and $+6.87$~pp for AttNeg. Relation predicates involve longer reasoning chains with more intermediate entities, producing greater answer diversity across traces ($C_0$) and more opportunities for oracle constraints to correct errors.\n\n\\begin{table}[h]\n\\centering\n\\caption{ProofWriter oracle experiment per-subtype breakdown. Oracle-SICA uses gold DSL annotations parsed deterministically to Z3 for consistency checking. Relation-predicate subtypes (RelNeg, RelNoneg) show larger gains than attribute-predicate subtypes; relation subtypes involve longer reasoning chains and benefit more from oracle constraints. Bold indicates best accuracy per row.}\n\\label{tab:pw_oracle_subtype}\n\\begin{tabular}{lcccc}\n\\toprule\nSubtype & $n$ & SC Acc (\\%) & Oracle Acc (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nAttNoneg & 154 & 87.01 & \\textbf{96.10} & +9.09 \\\\\nAttNeg & 160 & 85.00 & \\textbf{91.88} & +6.87 \\\\\nRelNoneg & 146 & 66.44 & \\textbf{79.45} & +13.01 \\\\\nRelNeg & 140 & 60.00 & \\textbf{77.86} & +17.86 \\\\\n\\midrule\nOverall & 600 & 75.17 & \\textbf{86.67} & +11.50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Constraint Ablation Details}\n\\label{app:ablation}\n\\label{sec:ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint ablation (Qwen2.5-14B, $n = 804$). Agreement: predictions identical to SC. MAX-SAT and count-only produce nearly identical predictions, confirming that self-extracted constraints carry no signal beyond vote counts.}\n\\label{tab:ablation}\n\\begin{tabular}{@{}lrc@{}}\n\\toprule\nAggregation & Acc.\\ (\\%) & Agreement w/ SC \\\\\n\\midrule\nSC (majority vote) & 76.24 & --- \\\\\nSICA (MAX-SAT) & 76.49 & 773\\,/\\,804 \\\\\nCount-only & 76.62 & 774\\,/\\,804 \\\\\nRandom-weight & 75.87 & 764\\,/\\,804 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Remediation Strategy Details}\n\\label{app:remediation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.49\\%$, $\\Delta = -0.98$\\,pp. None reaches significance. Three method-level strategies are reported in Table~\\ref{tab:method_interventions}.}\n\\label{tab:remediation}\n\\begin{tabular}{@{}llrl@{}}\n\\toprule\nStrategy & Target & $\\Delta$ (pp) & Key finding \\\\\n\\midrule\nContrastive$^a$ & Prompt & $-$1.10 & non-disc.\\ 6.0\\% ($\\downarrow$ from 8.2\\%) \\\\\nCross-model$^b$ & Architecture & 0.00 & disc.\\ 0\\% (weak$\\to$strong); $\\pm$1\\,pp (strong$\\to$weak) \\\\\nQwen3-14B$^c$ & Capability & $-$0.49 & $p = 0.655$ \\\\\nZ3 feedback & Solver & --- & 0.9\\% UNSAT trigger \\\\\nCons.\\ filtering & Noise & 0.00 & $T{\\geq}4 \\to$ SC \\\\\nCross-trace UNSAT & Independence & --- & 56.4\\% $\\emptyset$ vars \\\\\n$T{=}1.0$$^d$ & Diversity & 0.00 & isolated peak at $T{=}0.7$ only \\\\\nMulti-temp$^e$ & Diversity & 0.00 & $b{=}5$, $c{=}5$ (balanced) \\\\\nDisc.\\ filtering$^f$ & Filtering & 0.00 & 803/804 agree w/ SICA \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize $^a$\\,$n{=}182$ (extraction failures excluded). $^b$\\,Weak$\\to$strong: Mistral-7B extracts from Qwen2.5-14B traces. Strong$\\to$weak: Qwen3-14B (60.29\\%) and Qwen2.5-14B (58.33\\%) extract from Mistral-7B FOLIO traces ($n{=}204$); self-extraction baseline 59.31\\%. $^c$\\,$n{=}204$, SC $= 84.80\\%$. $^d$\\,Mistral-7B FOLIO, $n{=}204$. $^e$\\,Mistral-7B FOLIO, $T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each, $n{=}204$. $^f$\\,Qwen2.5-14B, $n{=}804$; removing non-discriminative constraints.}\n\\end{table}\n\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Method-level interventions on Mistral-7B with McNemar's paired test. All produce neutral-to-catastrophic results. ICG shows two FOLIO seeds; $p$ for the first. {*}{*}{*}\\,$p < 0.001$; {*}{*}\\,$p < 0.01$.}\n\\label{tab:method_interventions}\n\\begin{tabular}{@{}ll rc rc@{}}\n\\toprule\n& & \\multicolumn{2}{c}{FOLIO ($n = 204$)} & \\multicolumn{2}{c}{LogiQA ($n = 200$)} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\nMethod & Target & $\\Delta$ (pp) & $p$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nSC baseline & --- & 0.00 & --- & 0.00 & --- \\\\\nICG & Trace coupling & $-$1.96\\,/\\,$+$1.47 & .206 & $-$0.50 & .706 \\\\\nContrastive & Scoring bias & $\\mathbf{-9.31}$ & .007 & $-$4.50 & .160 \\\\\nDebate & Role diversity & $\\mathbf{-18.63}$ & ${<}.001$ & $\\mathbf{-23.00}$ & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Intervention Results}\n\\label{app:additional-interventions}\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Additional intervention results beyond the nine prompt-level and three method-level strategies reported in the main text. All produce neutral-to-negative results, completing the exhaustive remediation analysis across 22+ distinct approaches.}\n\\label{tab:additional_interventions}\n\\begin{tabular}{@{}llllrl@{}}\n\\toprule\n\\# & Method & Type & Target & $\\Delta$ (pp) & Key Finding \\\\\n\\midrule\n13 & PROVE (code verif.) & Paradigm & Formal proof & $-$1.9 & 15.2\\% compilable; conclusive acc.\\ = 50\\% \\\\\n14 & CEGIS (iterative) & Multi-round & Consistency & 0.0$^\\dagger$ & R1 $+$3.43\\,pp then oscillates \\\\\n15 & DeepConf (logprob) & Filtering & Confidence & 0.0 & $\\Delta_{\\text{logprob}} = 0.006$ (no separation) \\\\\n16 & Cross-model SICA & Cross-model & Independence & $-$0.49 & $\\kappa_{\\text{cross}}{=}0.42$ vs $\\kappa_{\\text{within}}{=}0.53$ \\\\\n17 & Problem perturbation & Input diversity & Trace diversity & $<$0 & $\\kappa$ \\emph{increased} to 0.70 (anti-effect) \\\\\n18 & MIN-UNSAT & Solver objective & Constraint sel.\\ & $-$6.5 & Mean excluded constraints $= 1.3$ \\\\\n19 & $\\kappa$-aware SC & Voting rule & Weighted voting & 0.0 & 11/11 conditions $\\Delta = 0$ \\\\\n20 & Z3 trace filter & Trace filtering & Quality & $-$0.49 & Precision 49.1\\%, 7 questions affected \\\\\n21 & Bootstrapped gold & Iterative & Self-improvement & 0.0$^\\dagger$ & R1 $+$2.45\\,pp then oscillates \\\\\n22 & Selective abstention & Diagnostic & Confidence & $+$4.4$^*$ & AUROC $= 0.673$, at 80\\% coverage \\\\\n23 & ASCII perturbation & Input diversity & Format diversity & 0.0 & $\\kappa$: $0.39 \\to 0.36$ (negligible) \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All experiments on Mistral-7B FOLIO ($n{=}204$) unless noted. $^\\dagger$\\,Oscillates without convergence; net effect $\\approx 0$. $^*$\\,Accuracy gain only at reduced coverage (diagnostic value, not a general improvement). Methods 1--12 are reported in Table~\\ref{tab:remediation} and Table~\\ref{tab:method_interventions}.}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.85\\textwidth]{figures/fig_app_interventions_summary.pdf}\n\\caption{Summary of 22+ intervention strategies grouped by category. All produce neutral-to-negative accuracy changes relative to Self-Consistency. The LLM-Debate bar is truncated at $-11.5$\\,pp (actual: $-18.6$\\,pp). The grey band indicates $\\pm 1$\\,pp noise zone.}\n\\label{fig:interventions-summary}\n\\end{figure*}\n\n\n\\section{Extraction Error Taxonomy}\n\\label{app:extraction}\n\\label{sec:extraction-taxonomy}\n\nConstraints must discriminate between candidate answers for MAX-SAT to produce a ranking different from majority vote. We measure discriminative power at two levels on Qwen2.5-14B across FOLIO and ProofWriter ($n = 804$). At the source-trace level, 39.2\\% of total constraint weight originates from traces whose answer differs from the plurality, but only 12.1\\% of individual constraints fall into this minority category. At the Z3 semantic level, 91.8\\% of constraints [95\\% CI: 91.2, 92.4] are technically discriminative, producing different satisfiability outcomes when evaluated against different candidate answers. Only 8.2\\% are non-discriminative.\n\nThe high discriminative rate does not translate into accuracy gains because discrimination mirrors the model's own answer distribution. Each trace produces constraints with its own variable names, so Z3 treats identically-intended propositions as unrelated symbols; among cross-answer constraint pairs, 56.4\\% share zero Z3 variables. This variable isolation means constraints from different traces are trivially jointly satisfiable, and MAX-SAT retains nearly all of them regardless of source answer. Removing the 8.2\\% non-discriminative constraints yields zero accuracy improvement. The discriminative majority does not provide independent signal; it reinforces the majority answer that SC would already select. This confirmation bias, not a lack of discrimination, explains why SICA degenerates to majority voting (Appendix~\\ref{app:ablation}).\n\n\n\\section{Hyperparameter Sensitivity}\n\\label{app:sensitivity}\n\\label{sec:k-sensitivity}\n\\label{sec:t-sensitivity}\n\n\\subsection{K Sensitivity}\n\nFigure~\\ref{fig:k-sensitivity} shows SICA $\\Delta$ as a function of the number of sampled traces $K$ for Mistral-7B on FOLIO ($n = 204$, no fixed seed). The relationship is non-monotonic: $K = 4$ yields $\\Delta = -1.47$\\,pp, $K = 8$ yields $\\Delta = -1.96$\\,pp, $K = 12$ reaches $\\Delta = +3.43$\\,pp, $K = 16$ drops to $\\Delta = +1.47$\\,pp, and $K = 20$ partially recovers to $\\Delta = +1.96$\\,pp. The recovery at $K = 20$ rules out a simple peaked pattern, but $K = 12$ remains the only setting with $\\Delta > 2$\\,pp ($p = 0.092$, marginal).\n\nThe apparent $\\Delta$ peak at $K = 12$ is confounded with SC baseline. SICA absolute accuracy plateaus at 59.31\\% (121/204) for $K \\geq 12$: identical at $K = 12$ and $K = 20$. The $\\Delta$ variation across these settings is driven primarily by SC fluctuations rather than by SICA improvement. $K = 12$ produces a relatively low SC (55.88\\%), placing it in the intermediate-SC region; $K = 8$ (SC $= 58.33\\%$) and $K = 20$ (SC $= 57.35\\%$) have higher baselines, compressing $\\Delta$ even though SICA accuracy does not change for $K \\geq 12$. Additional traces beyond $K = 12$ provide no benefit to SICA absolute performance, consistent with the constraint quality bottleneck. The $K = 12$ $\\Delta$ captures only 24.1\\% of the oracle ceiling ($+14.22$\\,pp).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{f3_k_sensitivity}\n\\caption{SICA $\\Delta$ (pp) vs.\\ number of traces $K$ for Mistral-7B on FOLIO ($n = 204$, default seed, $T = 0.7$). Non-monotonic pattern: SICA accuracy plateaus at 59.31\\% for $K \\geq 12$; the apparent $\\Delta$ peak at $K = 12$ partly reflects a relatively low SC baseline (55.88\\%) at that point. Error bars: 95\\% bootstrap CI.}\n\\label{fig:k-sensitivity}\n\\end{figure}\n\n\\subsection{Temperature Sensitivity}\n\nTemperature sensitivity on Mistral-7B FOLIO ($n = 204$, default seed) reveals a sharp isolated peak rather than a smooth trend. Across four temperature settings, only $T = 0.7$ produces a positive effect: $T = 0.3$ yields $\\Delta = -1.47$\\,pp (SC $= 58.33\\%$), $T = 0.5$ yields $\\Delta = -0.98$\\,pp (SC $= 58.33\\%$), $T = 0.7$ yields $\\Delta = +3.43$\\,pp (SC $= 55.88\\%$), and $T = 1.0$ yields $\\Delta = 0.00$\\,pp (SC $= 55.39\\%$). All other temperatures yield negative or null effects, and the single positive result at $T = 0.7$ is confounded with SC baseline. Combined with the seed sensitivity (0 of 4 seeds reaching $p < 0.05$ at $T = 0.7$), the positive trend depends on a specific combination of temperature, seed, and baseline accuracy that same-model sampling rarely achieves.\n\nThe parallel between $K$ and $T$ sensitivity points to a common underlying variable. In both sweeps, the setting that produces the largest SICA gain also produces a relatively low SC baseline (55.88\\%), which places it in the intermediate-SC region. The hyperparameters themselves ($K$, $T$) are not the causal driver; they modulate SC level, and it is the SC level that determines whether SICA has operating room.\n\n\n\\section{Entropy Decomposition}\n\\label{app:entropy}\n\\label{sec:entropy}\n\nWe partition problems by trace agreement: high-entropy (majority count $\\leq 8$ out of $K = 12$) and low-entropy (majority count $\\geq 9$). Table~\\ref{tab:entropy} reports SICA $\\Delta$ within each partition across eight model-dataset conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Entropy decomposition of SICA $\\Delta$ (pp). High-entropy: majority count $\\leq 8$; low-entropy: majority count $\\geq 9$. $^\\dagger$Partial data (180/600). Pre-tiebreaking SC values; pattern robust to D064 correction.}\n\\label{tab:entropy}\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Dataset & \\multicolumn{2}{c}{High-entropy} & \\multicolumn{2}{c}{Low-entropy} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n & & $n$ & $\\Delta$ & $n$ & $\\Delta$ \\\\\n\\midrule\nMistral-7B & FOLIO & 78 & $\\mathbf{+12.8}$ & 126 & 0.0 \\\\\nMistral-7B (s123) & FOLIO & 77 & $\\mathbf{+9.1}$ & 127 & 0.0 \\\\\nMistral-7B (s456) & FOLIO & 75 & $-$1.3 & 129 & 0.0 \\\\\nMistral-7B & PW-D5 & 267 & $-$4.9 & 333 & $-$1.2 \\\\\nQwen2.5-14B & FOLIO & 37 & $-$8.2 & 167 & $-$0.6 \\\\\nQwen2.5-14B & LogiQA & 23 & $-$4.3 & 177 & 0.0 \\\\\nQwen2.5-7B & FOLIO & 47 & $-$2.1 & 157 & 0.0 \\\\\nLLaMA-3.1-8B$^\\dagger$ & PW-D5 & 76 & $-$3.9 & 104 & $-$1.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo patterns emerge. First, low-entropy problems produce $\\Delta \\approx 0$\\,pp across all eight conditions: when traces agree, constraints carry no information beyond the majority vote.\n\nSecond, the direction of SICA's effect on high-entropy problems depends on the accuracy regime, not on entropy alone. In the intermediate-SC region (Mistral-7B on FOLIO, default-seed and seed-123 runs), high-entropy $\\Delta$ reaches $+12.8$ and $+9.1$\\,pp: traces genuinely disagree, and constraints from correct-answer traces provide discriminative signal that resolves the disagreement. In Type~A conditions (Qwen2.5-14B on FOLIO, $\\Delta = -8.2$\\,pp), high-entropy problems represent rare deviations from a strong model's consensus; constraints inherit the model's confirmation bias. In Type~C (Mistral-7B on ProofWriter, $\\Delta = -4.9$\\,pp), high-entropy problems reflect systematic errors. The mechanism is not entropy per se but the interaction of entropy with model capability.\n\n\n\\section{Failure Mode Analysis}\n\\label{app:failure-modes}\n\\label{sec:failure-modes}\n\nThe regime-dependent pattern in Table~\\ref{tab:main_results} reflects three distinct failure modes of self-extracted symbolic constraints.\n\n\\paragraph{Type A: confirmation bias (SC $\\geq$ $\\sim$60\\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\\mathcal{C}^{\\setminus}| \\approx 0$), the penalty term in Eq.~\\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in Appendix~\\ref{app:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.\n\n\\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean FOL formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\\%, but the resulting constraints have a contradiction rate of only 0.8\\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (51.00\\%) yet produces $\\Delta = +0.50$\\,pp ($p = 1.0$); Qwen2.5-14B on the same domain yields $\\Delta = -0.50$\\,pp ($p = 1.0$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.\n\n\\paragraph{Type C: error amplification (SC $\\leq$ $\\sim$40\\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, $p = 0.014$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.\n\n\n\\section{Cross-Model Confirmation Bias}\n\\label{app:cross-model-bias}\n\nTable~\\ref{tab:cross-model-bias} reports confirmation bias metrics across three model families on FOLIO ($n = 204$). Bias ratio, error constraint percentage, and SICA-follows-SC overlap all decrease with model capability, but remain substantially above chance across all families.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model confirmation bias on FOLIO ($n = 204$). Bias ratio: ratio of error-supporting constraints on incorrect vs.\\ correct problems. Error Constraint \\%: fraction of constraints supporting the wrong majority on incorrect problems. SICA$\\to$SC: fraction of SICA errors that overlap with SC errors. $^{\\dag}$Based on 4 of 12 traces due to extraction failures.}\n\\label{tab:cross-model-bias}\n\\begin{tabular}{@{}llrrr@{}}\n\\toprule\nModel & Dataset & Bias Ratio & Error Cstr.\\ \\% & SICA$\\to$SC \\\\\n\\midrule\nMistral-7B & FOLIO & $4.97\\times$ & 83.3\\% & 94.0\\% \\\\\nQwen2.5-14B & FOLIO & $3.93\\times$ & 79.7\\% & 90.4\\% \\\\\nLLaMA-3.1-8B$^{\\dag}$ & FOLIO & $2.88\\times$ & 74.3\\% & 78.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Independence-Accuracy Scatter Plot}\n\\label{app:kappa-scatter}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/f6_kappa_accuracy_scatter}\n\\caption{Independence-accuracy trade-off across aggregation methods (Mistral-7B, filled markers) and model families (LLaMA-3.1-8B, Qwen2.5-7B, Qwen2.5-14B; open markers) on FOLIO ($n = 204$). Same-model methods cluster at $\\kappa \\approx 0.40$--$0.47$ (gray band), while cross-model SC shows stronger correlations ($\\kappa = 0.41$--$0.74$) at higher accuracy. Debate breaks correlation ($\\kappa = 0.15$) at catastrophic accuracy cost. Dashed line: Mistral-7B SC baseline.}\n\\label{fig:kappa-accuracy}\n\\end{figure}\n\n\\section{Cross-Model Kappa Analysis}\n\\label{app:cross-model-kappa}\n\nTable~\\ref{tab:cross_model_kappa} compares trace independence across three model families on the same benchmarks. On FOLIO ($n = 204$), all four models produce $\\kappa \\geq 0.41$: LLaMA-3.1-8B ($\\kappa = 0.41$), Mistral-7B ($\\kappa = 0.44$), Qwen2.5-7B ($\\kappa = 0.66$), and Qwen2.5-14B ($\\kappa = 0.74$). The bottleneck is architecture-independent---no family escapes the correlation floor. Within the Qwen family, $\\kappa$ increases from 0.66 (7B) to 0.74 (14B), but Mistral-7B (7B) and LLaMA-3.1-8B (8B) differ by $\\Delta\\kappa = 0.03$ despite belonging to different families, suggesting that cross-family variation ($\\Delta\\kappa$ up to 0.22 at similar scale) exceeds within-family scale effects ($\\Delta\\kappa = 0.08$). Disentangling scale from architecture requires controlled same-family experiments across $\\geq$3 scales.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model trace independence ($K = 12$, SC aggregation, FOLIO + ProofWriter). Higher $\\kappa$ indicates stronger correlation and lower effective sample size.}\n\\label{tab:cross_model_kappa}\n\\begin{tabular}{@{}llccr@{}}\n\\toprule\nModel & Dataset & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.49 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 \\\\\nMistral-7B & FOLIO & 0.44 & 2.02 & 56.86 \\\\\nLLaMA-3.1-8B & FOLIO & 0.41 & 2.17 & 66.18 \\\\\n\\addlinespace\nQwen2.5-14B & PW-D5 & 0.62 & 1.54 & --- \\\\\nMistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Cross-Model Process-Level Independence}\n\\label{app:cross-model-process}\n\nTable~\\ref{tab:cross-model-process} extends the process-level independence analysis (\\S\\ref{sec:process-kappa}) to four model families on FOLIO ($n = 204$). Mean pairwise cosine similarity of TF-IDF trace representations exceeds answer-level $\\kappa$ in every family, but the gap is model-strength dependent: it narrows from $0.31$ (LLaMA) and $0.23$ (Mistral) to $0.02$ (Qwen-14B). For weaker models ($r \\approx 0$), answer diversity does not reflect reasoning diversity---process-convergent but answer-divergent trace pairs constitute 9.5\\% of all pairs on Mistral-7B versus 2.5--3.2\\% on other families. For stronger models ($r \\approx 0.23$, $p \\leq 0.001$), process and answer agreement align, and answer-level $\\kappa$ already captures the bottleneck. Process-$\\kappa$ thus provides a crucial additional diagnostic specifically for weaker models, where answer-level metrics underestimate reasoning homogeneity.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model process-level independence on FOLIO ($n = 204$, $K = 12$). Mean Cosine: mean pairwise TF-IDF cosine similarity of reasoning traces (Eq.~\\ref{eq:process-sim}). Answer $\\kappa$: per-question answer agreement. Gap: Cosine $-$ $\\kappa$. $r$: Pearson correlation between ProcessSim and answer agreement. Conv.: fraction of process-convergent but answer-divergent trace pairs. {*}{*}\\,$p < 0.01$; {*}{*}{*}\\,$p < 0.001$.}\n\\label{tab:cross-model-process}\n\\begin{tabular}{@{}lcccrlr@{}}\n\\toprule\nModel & Mean Cos. & Ans.\\ $\\kappa$ & Gap & $r$ & $p$ & Conv.\\ (\\%) \\\\\n\\midrule\nMistral-7B & 0.690 & 0.460 & 0.230 & $-$0.064 & 0.362 & 9.5 \\\\\nLLaMA-3.1-8B & 0.759 & 0.447 & 0.312 & $-$0.001 & 0.985 & 3.2 \\\\\nQwen2.5-7B & 0.790 & 0.658 & 0.132 & $+$0.226 & 0.001{*}{*} & 2.8 \\\\\nQwen2.5-14B & 0.766 & 0.744 & 0.022 & $+$0.244 & ${<}$0.001{*}{*}{*} & 2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Constraint Quality Across Methods}\n\\label{app:constraint-quality}\n\nTable~\\ref{tab:constraint_quality} compares constraint quality metrics across the three method-level interventions on Mistral-7B FOLIO ($n = 204$). Standard SICA extracts from reasoning traces and achieves the highest parse rate (97.1\\%) but also the highest redundancy (42.9\\%): nearly half of all constraints are syntactic duplicates across the 12 traces, quantifying the co-sourcing effect of same-model generation. ICG generates constraints directly from the problem statement without trace conditioning. Its lower parse rate (74.6\\%) reflects the difficulty of standalone formalization at the 7B scale, though successfully parsed constraints compile at a higher rate (99.4\\% vs.\\ 96.5\\%). ICG produces fewer unique constraints per question (24.9 vs.\\ 39.3) with lower redundancy (32.3\\%), consistent with the absence of trace-level repetition. Contrastive scoring generates pro and con constraint sets for each candidate answer. The format yields far fewer unique constraints per question (9.2) with zero redundancy (each pro/con pair is structurally distinct), but 62.7\\% of constraints are trivially satisfied by Z3---they impose no logical tension and cannot discriminate between candidates. Only 51.0\\% of Contrastive constraints are discriminative, compared to 81.4\\% for standard SICA and 77.0\\% for ICG.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint quality metrics across method-level interventions (Mistral-7B, FOLIO, $n = 204$). Parse: fraction of extraction attempts yielding valid JSON. Z3 Compile: fraction compiling to Z3 formulas. Unique/q: mean unique constraints per question. Redundancy: fraction of constraints duplicated across traces. Disc.: fraction discriminative (different Z3 outcome per candidate). Triv.\\ Sat.: fraction trivially satisfied (no logical tension).}\n\\label{tab:constraint_quality}\n\\begin{tabular}{@{}l rrrrrr@{}}\n\\toprule\nMethod & Parse & Z3 & Uniq/q & Redund. & Disc. & Triv.\\ Sat. \\\\\n\\midrule\nStandard SICA & 97.1\\% & 96.5\\% & 39.3 & 42.9\\% & 81.4\\% & --- \\\\\nICG & 74.6\\% & 99.4\\% & 24.9 & 32.3\\% & 77.0\\% & --- \\\\\nContrastive & 74.0\\% & 94.4\\% & 9.2 & 0.0\\% & 51.0\\% & 62.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Error Categorization of Method-Level Interventions}\n\\label{app:error-categorization}\n\nWe categorize discordant predictions (where the method and SC disagree) for Debate and Contrastive on FOLIO ($n = 204$) to understand why these interventions degrade accuracy.\n\n\\paragraph{Debate discordant analysis.} Debate produces 60 correct$\\to$wrong flips and 22 wrong$\\to$correct flips on FOLIO. Answer-type breakdown reveals that False-labeled questions are most vulnerable: 82.8\\% of False questions that SC answers correctly are flipped by Debate, compared to 63.9\\% for True and 25.5\\% for Unknown. Counterintuitively, failures concentrate not where debate breaks down but where it succeeds most thoroughly: discordant questions average 2.93 effective debate rounds (proposer-critic exchanges producing substantive updates) versus 2.52 for concordant ones. More extensive same-model debate produces more confident but incorrect constraints, consistent with the independence bottleneck---the critic draws on the same model distribution as the proposer, reinforcing shared biases rather than correcting them.\n\n\\paragraph{Contrastive discordant analysis.} Contrastive produces 34 discordant questions on FOLIO. All 34 produced non-degenerate scores (both pro and con constraint sets non-empty), compared to 20.1\\% degenerate scores in the full sample. This indicates that scoring failures on discordant questions stem from systematic pro-bias rather than missing constraints. Among discordant questions, 97.1\\% contain negation words in the problem statement versus 76.5\\% in the full sample, suggesting that negation-bearing problems are particularly susceptible to pro-constraint imbalance. The average pro/con score ratio is 1.0 for discordant questions versus 0.68 for the full sample: the method generates balanced-looking scores that mask directional errors.\n\n\\paragraph{Cross-method overlap.} Of the 79 unique questions on which either method disagrees with SC, only 15 overlap between Debate and Contrastive (Jaccard index $= 0.19$). All 15 shared discordant questions contain negation words. The low overlap confirms that the two methods attack different vulnerability types---Debate through extended same-model argumentation that amplifies confident errors, Contrastive through pro-bias in constraint generation---while sharing a common root cause in the independence bottleneck: both methods rely on the same model's output distribution and cannot introduce genuinely independent signal.\n\n\n\\section{Extended Limitations}\n\\label{app:limitations-extended}\n\nBeyond the limitations discussed in the main text, several additional constraints bound our conclusions. Seven of our eleven model-domain conditions have $n \\leq 60$, providing insufficient statistical power for confirmatory claims; power analysis shows that the minimum detectable effect exceeds 5\\,pp for these conditions (Table~\\ref{tab:power}), so they serve as regime characterization rather than definitive tests. Our extraction prompts use a single zero-shot template per domain; alternative prompting strategies (few-shot exemplars, chain-of-thought extraction, or iterative refinement) might yield higher-quality constraints, though the oracle gap suggests the bottleneck is fundamental rather than prompt-specific. The constraint quality analysis (91.8\\% discriminative rate, 39.2\\% source-trace minority weight) covers Qwen2.5-14B on FOLIO + ProofWriter ($N = 804$); other model-domain combinations may exhibit different characteristics. Constraint extraction uses $T_{\\text{ext}} = 0.3$ while trace sampling uses $T = 0.7$; alternative extraction temperatures might yield different results. Although we prompt for FOL-style formalizations, extracted constraints are predominantly propositional ground clauses without quantifiers (\\S\\ref{sec:constraint-extraction}); whether models capable of genuine quantified FOL would yield higher discriminative rates is untested. Deduplication uses syntactic equivalence, so semantically equivalent constraints with different surface forms receive separate weights. The GSM8K pilot ($n = 30$) illustrates the constraint-absent regime and should not be interpreted as confirmatory evidence.\n",
      "numLines": 646,
      "startLine": 1,
      "totalLines": 646
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_0195gBmZXvDBQFsJb7SU3czW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "21efd0c6-ae9b-4855-9f22-3e9f9ae18c2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeGkK3Y8Nb9wHuxxGKCqFU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 23860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1465
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

_source line 37 · 2026-05-20T13:31:51.071Z_

<details><summary>↩ Tool result · `toolu_0195gBmZXvDBQFsJb7SU3czW`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models on three reasoning domains with over 3,000 condition-evaluations across ${\sim}$1,250 unique instances. Beyond accuracy comparisons, we conduct diagnostic analyses of symbolic confirmation bias and process-level trace independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B parameters).
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold FOL annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$; extraction at $T_{\text{ext}}{=}0.3$. Z3 timeout: 10s. $\alpha{=}0.5$. Statistical significance via McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs from 10,000 resamples for $n \geq 200$.
14	
15	\paragraph{Computational cost.} On Mistral-7B FOLIO ($K{=}12$), SICA takes $4.5{\times}$ SC wall-clock time (81.4 vs.\ 17.7\,min for 204 questions). Constraint extraction ($K$ additional LLM calls, 17.8\,s/question) accounts for 76\% of overhead; Z3 solving is negligible (3\,ms, ${<}0.1\%$). Among remediation methods, ICG costs $3.2{\times}$, Debate $10.5{\times}$, and Contrastive $10.9{\times}$.
16	
17	
18	\subsection{Main Results}
19	\label{sec:main-results}
20	
21	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline. SICA effectiveness depends sharply on the accuracy regime.
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{SICA vs.\ SC across all conditions sorted by SC accuracy. $\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\dagger$\,$n < 100$ (suggestive only). \textbf{Bold $\Delta$}: $p < 0.05$ (McNemar). {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$. Failure modes detailed in Appendix~\ref{app:failure-modes}.}
27	\label{tab:main_results}
28	\begin{tabular}{@{}llrrrrl@{}}
29	\toprule
30	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
31	\midrule
32	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
33	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
34	\midrule
35	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--55\%, Mistral-7B only)}} \\
36	Mistral-7B & LogiQA & 200 & 51.00 & 51.50 & $+$0.50 & 1.000 \\
37	Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\
38	Mistral-7B & FOLIO & 204 & 55.88 & \textbf{59.31} & $+$3.43 & 0.092 \\
39	Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\
40	Mistral-7B & FOLIO (s789) & 204 & 54.41 & 53.92 & $-$0.49 & 1.000 \\
41	\midrule
42	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
43	LLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\
44	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
45	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\
46	Qwen2.5-14B & PW-D5 & 600 & 75.17 & 72.67 & $\mathbf{-2.50}$ & 0.011{*} \\
47	Qwen2.5-14B & FOLIO & 204 & 75.49 & 74.51 & $-$0.98 & 1.000 \\
48	Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
49	Qwen2.5-14B & LogiQA & 200 & 78.50 & 78.00 & $-$0.50 & 1.000 \\
50	Qwen3-14B & FOLIO & 204 & 84.80 & \textbf{84.31} & $-$0.49 & 1.000 \\
51	Qwen3-14B & PW-D5 & 600 & 85.00 & 85.67 & $+$0.67 & 1.000 \\
52	\midrule
53	\multicolumn{7}{l}{\textit{Degenerate ($C_0 < 5\%$)}} \\
54	QwQ-32B & AIME 2024$^\dagger$ & 22 & 72.70 & 72.70 & 0.00 & \textrm{---} \\
55	Qwen2.5-14B & GSM8K$^\dagger$ & 30 & 96.67 & 96.67 & 0.00 & \textrm{---} \\
56	\midrule
57	\multicolumn{7}{l}{\textit{Oracle upper bound (gold FOL/DSL + Z3)}} \\
58	Qwen2.5-14B & FOLIO & 204 & 75.49 & \textbf{89.71} & $\mathbf{+14.22}$ & $2.0{\times}10^{-7}${***} \\
59	Qwen2.5-14B & ProofWriter & 600 & 75.17 & \textbf{86.67} & $\mathbf{+11.50}$ & $9.21{\times}10^{-15}${***} \\
60	\bottomrule
61	\end{tabular}
62	\end{table*}
63	
64	\paragraph{Intermediate-SC region.} Mistral-7B on FOLIO (SC $\sim$50--55\%) shows positive directional trends in 2 of 4 seeds: $\Delta = +3.43$\,pp ($p = 0.092$) and $+2.94$\,pp ($p = 0.070$); the remaining seeds show null or negative results. No seed reaches $p < 0.05$; the 4-seed mean is $+1.47$\,pp. The default-seed and seed-456 runs share identical SC baselines (55.88\%) yet diverge ($+3.43$ vs.\ $0.00$\,pp), suggesting that seed-level constraint quality, not SC level alone, influences the effect (entropy decomposition in Appendix~\ref{app:entropy}). Mistral-7B on LogiQA, despite the same SC range, yields only $\Delta = +0.50$\,pp ($p = 1.0$), attributable to domain formalizability (Appendix~\ref{app:failure-modes}).
65	
66	\paragraph{Type A (SC $\geq$ 60\%): confirmation bias.} All nine Type~A conditions (SC $\geq 60\%$, combined $N > 2{,}800$) produce no significant positive effects. The largest positive trend is LLaMA-3.1-8B on StrategyQA ($\Delta = +2.00$\,pp, $p = 0.424$, n.s.), while Qwen2.5-14B on ProofWriter shows significant degradation ($\Delta = -2.50$\,pp, $p = 0.011$). Even in-context learning with gold FOL examples ($\Delta = +0.50$\,pp, n.s.) cannot break confirmation bias.
67	
68	\paragraph{Type C (SC $\leq$ 40\%): error amplification.} Mistral-7B on ProofWriter ($n = 600$, SC $= 39.33\%$) shows $\Delta = -2.83$\,pp ($p = 0.014$): SICA \emph{significantly hurts} by formalizing incorrect reasoning.
69	
70	\paragraph{Degenerate cases.} When $C_0 < 5\%$, nearly all traces agree and SICA reduces to SC by construction.
71	
72	Figure~\ref{fig:regime-scatter} visualizes the regime dependence: the intermediate-SC region is narrow and observed only for Mistral-7B on FOLIO.
73	
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=\columnwidth]{f2_regime_scatter}
77	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--55\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: significant degradation ($p = 0.014$).}
78	\label{fig:regime-scatter}
79	\end{figure}
80	
81	
82	\subsection{Oracle Control}
83	\label{sec:oracle}
84	
85	Oracle variants replace self-extracted constraints with gold annotations: FOL from FOLIO ($n = 204$) and DSL from ProofWriter ($n = 600$). Oracle-SICA achieves 89.71\% on FOLIO ($\Delta = +14.22$\,pp, $p = 2.0 \times 10^{-7}$) and 86.67\% on ProofWriter ($\Delta = +11.50$\,pp, $p = 9.21 \times 10^{-15}$). Z3 agrees with gold labels on 95.1\% (FOLIO) and 97.1\% (ProofWriter) of problems.
86	
87	These results establish that the MAX-SAT mechanism is sound given discriminative constraints. Mistral-7B's best self-extracted result ($+3.43$\,pp) captures only 24.1\% of the FOLIO oracle ceiling. The remaining 75.9\% is lost to self-extraction quality.
88	
89	
90	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "be798a8e-002d-44fe-8a4a-a943689b8cf7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:exp-setup}\n\nWe evaluate SICA against Self-Consistency (SC) across six models on three reasoning domains with over 3,000 condition-evaluations across ${\\sim}$1,250 unique instances. Beyond accuracy comparisons, we conduct diagnostic analyses of symbolic confirmation bias and process-level trace independence (\\S\\ref{sec:analysis}).\n\n\\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\\citep{dubey2024llama3}, and QwQ-32B~\\citep{qwen2024qwq} (7B--32B parameters).\n\n\\paragraph{Datasets.} FOLIO~\\citep{han2022folio} ($n{=}204$, with gold FOL annotations), ProofWriter depth-5~\\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\\%$).\n\n\\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$; extraction at $T_{\\text{ext}}{=}0.3$. Z3 timeout: 10s. $\\alpha{=}0.5$. Statistical significance via McNemar exact test ($\\alpha{=}0.05$); 95\\% bootstrap CIs from 10,000 resamples for $n \\geq 200$.\n\n\\paragraph{Computational cost.} On Mistral-7B FOLIO ($K{=}12$), SICA takes $4.5{\\times}$ SC wall-clock time (81.4 vs.\\ 17.7\\,min for 204 questions). Constraint extraction ($K$ additional LLM calls, 17.8\\,s/question) accounts for 76\\% of overhead; Z3 solving is negligible (3\\,ms, ${<}0.1\\%$). Among remediation methods, ICG costs $3.2{\\times}$, Debate $10.5{\\times}$, and Contrastive $10.9{\\times}$.\n\n\n\\subsection{Main Results}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline. SICA effectiveness depends sharply on the accuracy regime.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC across all conditions sorted by SC accuracy. $\\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\\dagger$\\,$n < 100$ (suggestive only). \\textbf{Bold $\\Delta$}: $p < 0.05$ (McNemar). {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$. Failure modes detailed in Appendix~\\ref{app:failure-modes}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type C: error amplification (SC $\\leq$ 40\\%)}} \\\\\nMistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\\mathbf{-2.83}$ & 0.014{*} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Intermediate SC (SC $\\sim$50--55\\%, Mistral-7B only)}} \\\\\nMistral-7B & LogiQA & 200 & 51.00 & 51.50 & $+$0.50 & 1.000 \\\\\nMistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\\\\nMistral-7B & FOLIO & 204 & 55.88 & \\textbf{59.31} & $+$3.43 & 0.092 \\\\\nMistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\\\\nMistral-7B & FOLIO (s789) & 204 & 54.41 & 53.92 & $-$0.49 & 1.000 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 75.17 & 72.67 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B & FOLIO & 204 & 75.49 & 74.51 & $-$0.98 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 78.50 & 78.00 & $-$0.50 & 1.000 \\\\\nQwen3-14B & FOLIO & 204 & 84.80 & \\textbf{84.31} & $-$0.49 & 1.000 \\\\\nQwen3-14B & PW-D5 & 600 & 85.00 & 85.67 & $+$0.67 & 1.000 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Degenerate ($C_0 < 5\\%$)}} \\\\\nQwQ-32B & AIME 2024$^\\dagger$ & 22 & 72.70 & 72.70 & 0.00 & \\textrm{---} \\\\\nQwen2.5-14B & GSM8K$^\\dagger$ & 30 & 96.67 & 96.67 & 0.00 & \\textrm{---} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Oracle upper bound (gold FOL/DSL + Z3)}} \\\\\nQwen2.5-14B & FOLIO & 204 & 75.49 & \\textbf{89.71} & $\\mathbf{+14.22}$ & $2.0{\\times}10^{-7}${***} \\\\\nQwen2.5-14B & ProofWriter & 600 & 75.17 & \\textbf{86.67} & $\\mathbf{+11.50}$ & $9.21{\\times}10^{-15}${***} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Intermediate-SC region.} Mistral-7B on FOLIO (SC $\\sim$50--55\\%) shows positive directional trends in 2 of 4 seeds: $\\Delta = +3.43$\\,pp ($p = 0.092$) and $+2.94$\\,pp ($p = 0.070$); the remaining seeds show null or negative results. No seed reaches $p < 0.05$; the 4-seed mean is $+1.47$\\,pp. The default-seed and seed-456 runs share identical SC baselines (55.88\\%) yet diverge ($+3.43$ vs.\\ $0.00$\\,pp), suggesting that seed-level constraint quality, not SC level alone, influences the effect (entropy decomposition in Appendix~\\ref{app:entropy}). Mistral-7B on LogiQA, despite the same SC range, yields only $\\Delta = +0.50$\\,pp ($p = 1.0$), attributable to domain formalizability (Appendix~\\ref{app:failure-modes}).\n\n\\paragraph{Type A (SC $\\geq$ 60\\%): confirmation bias.} All nine Type~A conditions (SC $\\geq 60\\%$, combined $N > 2{,}800$) produce no significant positive effects. The largest positive trend is LLaMA-3.1-8B on StrategyQA ($\\Delta = +2.00$\\,pp, $p = 0.424$, n.s.), while Qwen2.5-14B on ProofWriter shows significant degradation ($\\Delta = -2.50$\\,pp, $p = 0.011$). Even in-context learning with gold FOL examples ($\\Delta = +0.50$\\,pp, n.s.) cannot break confirmation bias.\n\n\\paragraph{Type C (SC $\\leq$ 40\\%): error amplification.} Mistral-7B on ProofWriter ($n = 600$, SC $= 39.33\\%$) shows $\\Delta = -2.83$\\,pp ($p = 0.014$): SICA \\emph{significantly hurts} by formalizing incorrect reasoning.\n\n\\paragraph{Degenerate cases.} When $C_0 < 5\\%$, nearly all traces agree and SICA reduces to SC by construction.\n\nFigure~\\ref{fig:regime-scatter} visualizes the regime dependence: the intermediate-SC region is narrow and observed only for Mistral-7B on FOLIO.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{f2_regime_scatter}\n\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--55\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: significant degradation ($p = 0.014$).}\n\\label{fig:regime-scatter}\n\\end{figure}\n\n\n\\subsection{Oracle Control}\n\\label{sec:oracle}\n\nOracle variants replace self-extracted constraints with gold annotations: FOL from FOLIO ($n = 204$) and DSL from ProofWriter ($n = 600$). Oracle-SICA achieves 89.71\\% on FOLIO ($\\Delta = +14.22$\\,pp, $p = 2.0 \\times 10^{-7}$) and 86.67\\% on ProofWriter ($\\Delta = +11.50$\\,pp, $p = 9.21 \\times 10^{-15}$). Z3 agrees with gold labels on 95.1\\% (FOLIO) and 97.1\\% (ProofWriter) of problems.\n\nThese results establish that the MAX-SAT mechanism is sound given discriminative constraints. Mistral-7B's best self-extracted result ($+3.43$\\,pp) captures only 24.1\\% of the FOLIO oracle ceiling. The remaining 75.9\\% is lost to self-extraction quality.\n\n\n",
      "numLines": 90,
      "startLine": 1,
      "totalLines": 90
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01TFkDBJKf7f3PfBJXqMTYgG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "33bedecd-da4f-4c55-b1d7-7a693557e525",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeGkK3Y8Nb9wHuxxGKCqFU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 23860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1465
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

_source line 39 · 2026-05-20T13:31:51.601Z_

<details><summary>↩ Tool result · `toolu_01TFkDBJKf7f3PfBJXqMTYgG`</summary>

```text
1	\section{Diagnosis}
2	\label{sec:diagnosis}
3	
4	Table~\ref{tab:main_results} reports SICA vs.\ SC accuracy across all conditions. None of fifteen non-degenerate conditions shows a significant positive effect ($p < 0.05$); two show significant degradation. We trace this failure to three interconnected mechanisms.
5	
6	\begin{table*}[t]
7	\centering
8	\small
9	\caption{SICA vs.\ SC across all conditions sorted by SC accuracy. $\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\dagger$\,$n < 100$ (suggestive only). \textbf{Bold $\Delta$}: $p < 0.05$ (McNemar). {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$. Failure modes detailed in Appendix~\ref{app:failure-modes}.}
10	\label{tab:main_results}
11	\begin{tabular}{@{}llrrrrl@{}}
12	\toprule
13	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
14	\midrule
15	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
16	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
17	\midrule
18	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--55\%, Mistral-7B only)}} \\
19	Mistral-7B & LogiQA & 200 & 51.00 & 51.50 & $+$0.50 & 1.000 \\
20	Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\
21	Mistral-7B & FOLIO & 204 & 55.88 & \textbf{59.31} & $+$3.43 & 0.092 \\
22	Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\
23	Mistral-7B & FOLIO (s789) & 204 & 54.41 & 53.92 & $-$0.49 & 1.000 \\
24	\midrule
25	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
26	LLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\
27	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
28	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\
29	Qwen2.5-14B & PW-D5 & 600 & 75.17 & 72.67 & $\mathbf{-2.50}$ & 0.011{*} \\
30	Qwen2.5-14B & FOLIO & 204 & 75.49 & 74.51 & $-$0.98 & 1.000 \\
31	Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
32	Qwen2.5-14B & LogiQA & 200 & 78.50 & 78.00 & $-$0.50 & 1.000 \\
33	Qwen3-14B & FOLIO & 204 & 84.80 & \textbf{84.31} & $-$0.49 & 1.000 \\
34	Qwen3-14B & PW-D5 & 600 & 85.00 & 85.67 & $+$0.67 & 1.000 \\
35	\midrule
36	\multicolumn{7}{l}{\textit{Degenerate ($C_0 < 5\%$)}} \\
37	QwQ-32B & AIME 2024$^\dagger$ & 22 & 72.70 & 72.70 & 0.00 & \textrm{---} \\
38	Qwen2.5-14B & GSM8K$^\dagger$ & 30 & 96.67 & 96.67 & 0.00 & \textrm{---} \\
39	\midrule
40	\multicolumn{7}{l}{\textit{Oracle upper bound (gold FOL/DSL + Z3)}} \\
41	Qwen2.5-14B & FOLIO & 204 & 75.49 & \textbf{89.71} & $\mathbf{+14.22}$ & $2.0{\times}10^{-7}${***} \\
42	Qwen2.5-14B & ProofWriter & 600 & 75.17 & \textbf{86.67} & $\mathbf{+11.50}$ & $9.21{\times}10^{-15}${***} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\subsection{Symbolic Confirmation Bias}
48	\label{sec:confirmation-bias}
49	\label{sec:effective-k}
50	
51	Table~\ref{tab:independence} reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$. Two conditions are jointly necessary for any positive trend: sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and sufficient SC accuracy ($K_{\text{eff}} = 3.62$ with SC $= 39\%$ produces significant degradation). Cross-model validation confirms universality: all four families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}).
52	
53	This correlation manifests through a specific mechanism: self-extracted constraints systematically confirm the model's majority answer regardless of correctness. On Mistral-7B FOLIO ($n = 204$), when SICA errs, 83.3\% of extracted constraints support the incorrect majority answer---a bias ratio of $4.97\times$ compared to correct problems. Consequently, 94\% of SICA errors overlap with SC errors: symbolic aggregation adds no independent corrective signal.
54	
55	The causal chain is: the model generates an answer, then extracts FOL consistent with it. Constraints from majority-answer traces use trace-specific variable names (56.4\% of cross-answer pairs share zero Z3 variables), so MAX-SAT retains nearly all, and aggregation reduces to a weighted majority vote (Eq.~\ref{eq:degenerate}). Confirmation bias generalizes across model families: bias ratios of $4.97\times$ (Mistral-7B), $3.93\times$ (Qwen2.5-14B), and $2.88{\times}^{\dag}$ (LLaMA-3.1-8B) all significantly exceed $1.0$ ($^{\dag}$based on 4/12 traces due to extraction failures; Table~\ref{tab:cross-model-bias}). The oracle ceiling (\S\ref{sec:oracle}) confirms that 75.9\% of the potential gain is lost to self-extraction quality.
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
67	Qwen2.5-14B & LogiQA & 0.82 & 1.20 & 78.50 & $-$0.50 \\
68	Qwen3 & FOLIO & 0.77 & 1.26 & 84.80 & $-$0.49 \\
69	Qwen2.5-14B & FOLIO & 0.74 & 1.30 & 75.49 & $-$0.98 \\
70	Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\
71	\addlinespace
72	Mistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\
73	Mistral-7B & LogiQA & 0.51 & 1.81 & 51.00 & $+$0.50 \\
74	Mistral-7B (s456) & FOLIO & 0.51 & 1.82 & 55.88 & 0.00 \\
75	Mistral-7B & FOLIO & 0.50 & 1.84 & 55.88 & $+$3.43 \\
76	Mistral-7B (s123) & FOLIO & 0.49 & 1.88 & 54.41 & $+$2.94 \\
77	Mistral-7B (s789) & FOLIO & 0.41 & 2.17 & 54.41 & $-$0.49 \\
78	Mistral-7B ($T{=}0.5$) & FOLIO & 0.52 & 1.80 & 58.33 & $-$0.98 \\
79	Mistral-7B (multi-T) & FOLIO & 0.48 & 1.91 & 57.84 & 0.00 \\
80	Mistral-7B ($T{=}1.0$) & FOLIO & 0.48 & 1.91 & 55.39 & 0.00 \\
81	Mistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 & $\mathbf{-2.83}${*} \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	
87	\subsection{Process-Level Independence}
88	\label{sec:process-kappa}
89	
90	Answer-level $\kappa$ may underestimate the independence bottleneck: two traces can follow nearly identical reasoning yet reach different final answers. We define process similarity as the mean pairwise cosine similarity of TF-IDF trace representations:
91	\begin{equation}
92	\label{eq:process-sim}
93	\text{ProcessSim}(q) = \frac{2}{K(K{-}1)} \sum_{i < j} \cos(\mathbf{v}_i^q, \mathbf{v}_j^q),
94	\end{equation}
95	where $\mathbf{v}_i^q$ is the TF-IDF vector of trace $t_i$ for question $q$. On Mistral-7B FOLIO ($n = 204$), mean ProcessSim is $0.69$, far exceeding answer-level $\kappa = 0.41$. These measures are uncorrelated ($r = -0.06$, $p = 0.36$): problems with diverse answers do not exhibit diverse reasoning (Figure~\ref{fig:process-kappa}). This gap implies that interventions targeting answer diversity (temperature scaling, diverse prompting) may spread answers without altering reasoning paths.
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=0.85\columnwidth]{figures/fig3_process_kappa_scatter.pdf}
100	\vspace{-2mm}
101	\caption{Answer agreement vs.\ CoT cosine similarity (Mistral-7B, FOLIO, $n{=}204$). Flat regression ($r = -0.06$, $p = 0.36$): process and answer independence are uncorrelated.}
102	\label{fig:process-kappa}
103	\end{figure}
104	
105	
106	\subsection{Regime-Dependent Effects}
107	\label{sec:main-results}
108	\label{sec:diagnostics}
109	
110	SICA effectiveness depends sharply on the accuracy regime (Figure~\ref{fig:regime-scatter}).
111	
112	\paragraph{Intermediate-SC region.} Mistral-7B on FOLIO (SC $\sim$50--55\%) shows positive directional trends in 2 of 4 seeds: $\Delta = +3.43$\,pp ($p = 0.092$) and $+2.94$\,pp ($p = 0.070$); the remaining seeds show null or negative results. No seed reaches $p < 0.05$; the 4-seed mean is $+1.47$\,pp. The default-seed and seed-456 runs share identical SC baselines (55.88\%) yet diverge ($+3.43$ vs.\ $0.00$\,pp), suggesting that seed-level constraint quality, not SC level alone, influences the effect.
113	
114	\paragraph{Type A (SC $\geq$ 60\%).} All nine Type~A conditions produce no significant positive effects. Even in-context learning with gold FOL examples yields $\Delta = +0.50$\,pp (n.s.). Qwen2.5-14B on ProofWriter shows significant degradation ($\Delta = -2.50$\,pp, $p = 0.011$).
115	
116	\paragraph{Type C (SC $\leq$ 40\%).} Mistral-7B on ProofWriter ($n = 600$, SC $= 39.33\%$) shows $\Delta = -2.83$\,pp ($p = 0.014$): SICA \emph{significantly hurts} by formalizing incorrect reasoning. When $C_0 < 5\%$, nearly all traces agree and SICA reduces to SC by construction.
117	
118	Four supporting analyses confirm the mechanism: constraint ablation shows MAX-SAT and count-only agree on 94.4\% of predictions ($n = 804$); 91.8\% of constraints are discriminative but mirror the majority; effects concentrate in high-entropy problems ($+12.8$\,pp) with direction determined by accuracy regime; and hyperparameter peaks coincide with low SC baselines (Appendices~\ref{app:extraction}--\ref{app:entropy}).
119	
120	\begin{figure}[t]
121	\centering
122	\includegraphics[width=\columnwidth]{f2_regime_scatter}
123	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--55\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: significant degradation ($p = 0.014$).}
124	\label{fig:regime-scatter}
125	\end{figure}
126	
127	
128	\subsection{Remediation: 25+ Strategies Fail}
129	\label{sec:remediation}
130	\label{sec:interventions}
131	
132	We test more than twenty remediation strategies spanning prompt engineering, method-level redesign, and ten additional directions. All produce neutral or negative results.
133	
134	\paragraph{Prompt-level interventions.} Nine strategies spanning six dimensions (Appendix Table~\ref{tab:remediation}) all fail. Contrastive prompting reduces non-discriminative constraints from 8.2\% to 6.0\%, but newly discriminative constraints still mirror the majority ($\Delta = -1.1$\,pp). Cross-model extraction fails in both directions: weaker models yield 0\% discriminative constraints; stronger models produce accuracy within $\pm 1$\,pp of self-extraction. Multi-temperature sampling ($T \in \{0.3, 0.7, 1.2\}$) yields $\Delta = 0.00$\,pp.
135	
136	\paragraph{Method-level interventions.} ICG ($\Delta \approx 0$, $p = .206$), Contrastive ($\Delta = -9.31$\,pp, $p < 0.01$), and Debate ($\Delta = -18.63$/$-23.00$\,pp, $p < 0.001$) all fail (Table~\ref{tab:method_interventions}, Appendix~\ref{app:remediation}). Ten further experiments (code verification, iterative refinement, logprob filtering, cross-model ensembles) produce neutral-to-negative results (Appendix Table~\ref{tab:additional_interventions}).
137	
138	\paragraph{Independence-accuracy trade-off.} Table~\ref{tab:kappa_generalization} compares Fleiss' $\kappa$ across four aggregation methods and three model families (Figure~\ref{fig:kappa-accuracy}). SC ($\kappa = 0.44$), Diverse-Prompt ($\kappa = 0.40$), and ICG ($\kappa = 0.47$) cluster at $\kappa \approx 0.40$--$0.47$; Debate reaches $\kappa = 0.15$ but collapses accuracy by $-18.6$\,pp. All three families cluster above $\kappa = 0.40$, forming a same-model Pareto frontier: methods that increase independence destroy accuracy, and methods preserving accuracy cannot break the correlation floor. The bias ratio gradient ($4.97\times$ Mistral $> 3.93\times$ Qwen $> 2.88\times$ LLaMA) suggests weaker models suffer more severe confirmation bias. For practitioners, $C_0$ combined with SC accuracy predicts when augmentation is unlikely to help: $C_0 < 5\%$ implies degeneration, SC $\geq 60\%$ implies confirmation bias, SC $\leq 40\%$ implies error amplification. Whether 70B+ models or trained extractors shift the Pareto frontier remains open.
139	
140	\begin{table}[t]
141	\centering
142	\small
143	\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\kappa \geq 0.41$, confirming an architecture-independent ceiling. $\kappa$: Fleiss' kappa on raw answers.}
144	\label{tab:kappa_generalization}
145	\setlength{\tabcolsep}{3.5pt}
146	\begin{tabular}{@{}llccrr@{}}
147	\toprule
148	Model & Aggregation & $\kappa$ & Eff-$K$ & $K$ & Acc.\ (\%) \\
149	\midrule
150	Mistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\
151	& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\
152	& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\
153	& ICG & 0.47 & 1.93 & 10 & 51.96 \\
154	\addlinespace
155	LLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\
156	Qwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\
157	Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.49 \\
158	\bottomrule
159	\end{tabular}
160	\end{table}
161	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "4eb6c057-908b-49bf-a171-d69dba105a7d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex",
      "content": "\\section{Diagnosis}\n\\label{sec:diagnosis}\n\nTable~\\ref{tab:main_results} reports SICA vs.\\ SC accuracy across all conditions. None of fifteen non-degenerate conditions shows a significant positive effect ($p < 0.05$); two show significant degradation. We trace this failure to three interconnected mechanisms.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC across all conditions sorted by SC accuracy. $\\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\\dagger$\\,$n < 100$ (suggestive only). \\textbf{Bold $\\Delta$}: $p < 0.05$ (McNemar). {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$. Failure modes detailed in Appendix~\\ref{app:failure-modes}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type C: error amplification (SC $\\leq$ 40\\%)}} \\\\\nMistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\\mathbf{-2.83}$ & 0.014{*} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Intermediate SC (SC $\\sim$50--55\\%, Mistral-7B only)}} \\\\\nMistral-7B & LogiQA & 200 & 51.00 & 51.50 & $+$0.50 & 1.000 \\\\\nMistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\\\\nMistral-7B & FOLIO & 204 & 55.88 & \\textbf{59.31} & $+$3.43 & 0.092 \\\\\nMistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\\\\nMistral-7B & FOLIO (s789) & 204 & 54.41 & 53.92 & $-$0.49 & 1.000 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 75.17 & 72.67 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B & FOLIO & 204 & 75.49 & 74.51 & $-$0.98 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 78.50 & 78.00 & $-$0.50 & 1.000 \\\\\nQwen3-14B & FOLIO & 204 & 84.80 & \\textbf{84.31} & $-$0.49 & 1.000 \\\\\nQwen3-14B & PW-D5 & 600 & 85.00 & 85.67 & $+$0.67 & 1.000 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Degenerate ($C_0 < 5\\%$)}} \\\\\nQwQ-32B & AIME 2024$^\\dagger$ & 22 & 72.70 & 72.70 & 0.00 & \\textrm{---} \\\\\nQwen2.5-14B & GSM8K$^\\dagger$ & 30 & 96.67 & 96.67 & 0.00 & \\textrm{---} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Oracle upper bound (gold FOL/DSL + Z3)}} \\\\\nQwen2.5-14B & FOLIO & 204 & 75.49 & \\textbf{89.71} & $\\mathbf{+14.22}$ & $2.0{\\times}10^{-7}${***} \\\\\nQwen2.5-14B & ProofWriter & 600 & 75.17 & \\textbf{86.67} & $\\mathbf{+11.50}$ & $9.21{\\times}10^{-15}${***} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Symbolic Confirmation Bias}\n\\label{sec:confirmation-bias}\n\\label{sec:effective-k}\n\nTable~\\ref{tab:independence} reports Fleiss' $\\kappa$ and Effective-K (Eq.~\\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\\kappa$ ranges from 0.21 to 0.82, yielding $K_{\\text{eff}} = 1.20\\text{--}3.62$. Two conditions are jointly necessary for any positive trend: sufficient $K_{\\text{eff}}$ ($\\leq 1.30$ never improves) and sufficient SC accuracy ($K_{\\text{eff}} = 3.62$ with SC $= 39\\%$ produces significant degradation). Cross-model validation confirms universality: all four families produce $\\kappa \\geq 0.41$ (Table~\\ref{tab:kappa_generalization}).\n\nThis correlation manifests through a specific mechanism: self-extracted constraints systematically confirm the model's majority answer regardless of correctness. On Mistral-7B FOLIO ($n = 204$), when SICA errs, 83.3\\% of extracted constraints support the incorrect majority answer---a bias ratio of $4.97\\times$ compared to correct problems. Consequently, 94\\% of SICA errors overlap with SC errors: symbolic aggregation adds no independent corrective signal.\n\nThe causal chain is: the model generates an answer, then extracts FOL consistent with it. Constraints from majority-answer traces use trace-specific variable names (56.4\\% of cross-answer pairs share zero Z3 variables), so MAX-SAT retains nearly all, and aggregation reduces to a weighted majority vote (Eq.~\\ref{eq:degenerate}). Confirmation bias generalizes across model families: bias ratios of $4.97\\times$ (Mistral-7B), $3.93\\times$ (Qwen2.5-14B), and $2.88{\\times}^{\\dag}$ (LLaMA-3.1-8B) all significantly exceed $1.0$ ($^{\\dag}$based on 4/12 traces due to extraction failures; Table~\\ref{tab:cross-model-bias}). The oracle ceiling (\\S\\ref{sec:oracle}) confirms that 75.9\\% of the potential gain is lost to self-extraction quality.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$; positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each.}\n\\label{tab:independence}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Condition & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nQwen3 (think) & FOLIO & 0.91 & 1.09 & ${\\sim}$84 & ${\\sim}$0 \\\\\nQwen2.5-14B & LogiQA & 0.82 & 1.20 & 78.50 & $-$0.50 \\\\\nQwen3 & FOLIO & 0.77 & 1.26 & 84.80 & $-$0.49 \\\\\nQwen2.5-14B & FOLIO & 0.74 & 1.30 & 75.49 & $-$0.98 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\\\\n\\addlinespace\nMistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\\\\nMistral-7B & LogiQA & 0.51 & 1.81 & 51.00 & $+$0.50 \\\\\nMistral-7B (s456) & FOLIO & 0.51 & 1.82 & 55.88 & 0.00 \\\\\nMistral-7B & FOLIO & 0.50 & 1.84 & 55.88 & $+$3.43 \\\\\nMistral-7B (s123) & FOLIO & 0.49 & 1.88 & 54.41 & $+$2.94 \\\\\nMistral-7B (s789) & FOLIO & 0.41 & 2.17 & 54.41 & $-$0.49 \\\\\nMistral-7B ($T{=}0.5$) & FOLIO & 0.52 & 1.80 & 58.33 & $-$0.98 \\\\\nMistral-7B (multi-T) & FOLIO & 0.48 & 1.91 & 57.84 & 0.00 \\\\\nMistral-7B ($T{=}1.0$) & FOLIO & 0.48 & 1.91 & 55.39 & 0.00 \\\\\nMistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 & $\\mathbf{-2.83}${*} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Process-Level Independence}\n\\label{sec:process-kappa}\n\nAnswer-level $\\kappa$ may underestimate the independence bottleneck: two traces can follow nearly identical reasoning yet reach different final answers. We define process similarity as the mean pairwise cosine similarity of TF-IDF trace representations:\n\\begin{equation}\n\\label{eq:process-sim}\n\\text{ProcessSim}(q) = \\frac{2}{K(K{-}1)} \\sum_{i < j} \\cos(\\mathbf{v}_i^q, \\mathbf{v}_j^q),\n\\end{equation}\nwhere $\\mathbf{v}_i^q$ is the TF-IDF vector of trace $t_i$ for question $q$. On Mistral-7B FOLIO ($n = 204$), mean ProcessSim is $0.69$, far exceeding answer-level $\\kappa = 0.41$. These measures are uncorrelated ($r = -0.06$, $p = 0.36$): problems with diverse answers do not exhibit diverse reasoning (Figure~\\ref{fig:process-kappa}). This gap implies that interventions targeting answer diversity (temperature scaling, diverse prompting) may spread answers without altering reasoning paths.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_process_kappa_scatter.pdf}\n\\vspace{-2mm}\n\\caption{Answer agreement vs.\\ CoT cosine similarity (Mistral-7B, FOLIO, $n{=}204$). Flat regression ($r = -0.06$, $p = 0.36$): process and answer independence are uncorrelated.}\n\\label{fig:process-kappa}\n\\end{figure}\n\n\n\\subsection{Regime-Dependent Effects}\n\\label{sec:main-results}\n\\label{sec:diagnostics}\n\nSICA effectiveness depends sharply on the accuracy regime (Figure~\\ref{fig:regime-scatter}).\n\n\\paragraph{Intermediate-SC region.} Mistral-7B on FOLIO (SC $\\sim$50--55\\%) shows positive directional trends in 2 of 4 seeds: $\\Delta = +3.43$\\,pp ($p = 0.092$) and $+2.94$\\,pp ($p = 0.070$); the remaining seeds show null or negative results. No seed reaches $p < 0.05$; the 4-seed mean is $+1.47$\\,pp. The default-seed and seed-456 runs share identical SC baselines (55.88\\%) yet diverge ($+3.43$ vs.\\ $0.00$\\,pp), suggesting that seed-level constraint quality, not SC level alone, influences the effect.\n\n\\paragraph{Type A (SC $\\geq$ 60\\%).} All nine Type~A conditions produce no significant positive effects. Even in-context learning with gold FOL examples yields $\\Delta = +0.50$\\,pp (n.s.). Qwen2.5-14B on ProofWriter shows significant degradation ($\\Delta = -2.50$\\,pp, $p = 0.011$).\n\n\\paragraph{Type C (SC $\\leq$ 40\\%).} Mistral-7B on ProofWriter ($n = 600$, SC $= 39.33\\%$) shows $\\Delta = -2.83$\\,pp ($p = 0.014$): SICA \\emph{significantly hurts} by formalizing incorrect reasoning. When $C_0 < 5\\%$, nearly all traces agree and SICA reduces to SC by construction.\n\nFour supporting analyses confirm the mechanism: constraint ablation shows MAX-SAT and count-only agree on 94.4\\% of predictions ($n = 804$); 91.8\\% of constraints are discriminative but mirror the majority; effects concentrate in high-entropy problems ($+12.8$\\,pp) with direction determined by accuracy regime; and hyperparameter peaks coincide with low SC baselines (Appendices~\\ref{app:extraction}--\\ref{app:entropy}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{f2_regime_scatter}\n\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--55\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: significant degradation ($p = 0.014$).}\n\\label{fig:regime-scatter}\n\\end{figure}\n\n\n\\subsection{Remediation: 25+ Strategies Fail}\n\\label{sec:remediation}\n\\label{sec:interventions}\n\nWe test more than twenty remediation strategies spanning prompt engineering, method-level redesign, and ten additional directions. All produce neutral or negative results.\n\n\\paragraph{Prompt-level interventions.} Nine strategies spanning six dimensions (Appendix Table~\\ref{tab:remediation}) all fail. Contrastive prompting reduces non-discriminative constraints from 8.2\\% to 6.0\\%, but newly discriminative constraints still mirror the majority ($\\Delta = -1.1$\\,pp). Cross-model extraction fails in both directions: weaker models yield 0\\% discriminative constraints; stronger models produce accuracy within $\\pm 1$\\,pp of self-extraction. Multi-temperature sampling ($T \\in \\{0.3, 0.7, 1.2\\}$) yields $\\Delta = 0.00$\\,pp.\n\n\\paragraph{Method-level interventions.} ICG ($\\Delta \\approx 0$, $p = .206$), Contrastive ($\\Delta = -9.31$\\,pp, $p < 0.01$), and Debate ($\\Delta = -18.63$/$-23.00$\\,pp, $p < 0.001$) all fail (Table~\\ref{tab:method_interventions}, Appendix~\\ref{app:remediation}). Ten further experiments (code verification, iterative refinement, logprob filtering, cross-model ensembles) produce neutral-to-negative results (Appendix Table~\\ref{tab:additional_interventions}).\n\n\\paragraph{Independence-accuracy trade-off.} Table~\\ref{tab:kappa_generalization} compares Fleiss' $\\kappa$ across four aggregation methods and three model families (Figure~\\ref{fig:kappa-accuracy}). SC ($\\kappa = 0.44$), Diverse-Prompt ($\\kappa = 0.40$), and ICG ($\\kappa = 0.47$) cluster at $\\kappa \\approx 0.40$--$0.47$; Debate reaches $\\kappa = 0.15$ but collapses accuracy by $-18.6$\\,pp. All three families cluster above $\\kappa = 0.40$, forming a same-model Pareto frontier: methods that increase independence destroy accuracy, and methods preserving accuracy cannot break the correlation floor. The bias ratio gradient ($4.97\\times$ Mistral $> 3.93\\times$ Qwen $> 2.88\\times$ LLaMA) suggests weaker models suffer more severe confirmation bias. For practitioners, $C_0$ combined with SC accuracy predicts when augmentation is unlikely to help: $C_0 < 5\\%$ implies degeneration, SC $\\geq 60\\%$ implies confirmation bias, SC $\\leq 40\\%$ implies error amplification. Whether 70B+ models or trained extractors shift the Pareto frontier remains open.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\\kappa \\geq 0.41$, confirming an architecture-independent ceiling. $\\kappa$: Fleiss' kappa on raw answers.}\n\\label{tab:kappa_generalization}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Aggregation & $\\kappa$ & Eff-$K$ & $K$ & Acc.\\ (\\%) \\\\\n\\midrule\nMistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\\\\n& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\\\\n& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\\\\n& ICG & 0.47 & 1.93 & 10 & 51.96 \\\\\n\\addlinespace\nLLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\\\\nQwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\\\\nQwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.49 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 161,
      "startLine": 1,
      "totalLines": 161
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01SKmoZXHUnxutgkmiuhh6cJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "0e6112f9-77ff-4643-b018-00f57d9bcd1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeGkK3Y8Nb9wHuxxGKCqFU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1465,
      "cache_read_input_tokens": 23860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1465
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

_source line 41 · 2026-05-20T13:31:51.953Z_

<details><summary>↩ Tool result · `toolu_01SKmoZXHUnxutgkmiuhh6cJ`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	This section investigates \emph{why} SICA fails: trace correlation (\S\ref{sec:effective-k}), symbolic confirmation bias (\S\ref{sec:confirmation-bias}), process-level independence (\S\ref{sec:process-kappa}), supporting diagnostics (\S\ref{sec:diagnostics}), and remediation strategies (\S\ref{sec:remediation}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	Table~\ref{tab:independence} reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$. The four Mistral-7B FOLIO seeds produce $\kappa \in [0.41, 0.51]$, yet $\Delta$ ranges from $+3.43$ to $-0.49$\,pp---seed-level constraint quality, not independence alone, appears to influence the variation. Two conditions are jointly necessary for positive $\Delta$: sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and sufficient SC accuracy ($K_{\text{eff}} = 3.62$ with SC $= 39\%$ produces significant degradation). Cross-model validation confirms universality: all four families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}; Appendix~\ref{app:cross-model-kappa}).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{Trace independence metrics ($K = 12$, sorted by $\kappa$ descending). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:effk}). SC: Self-Consistency baseline. $\Delta$: SICA $-$ SC (pp). {*}\,$p < 0.05$; positive $\Delta$ values do not reach significance. multi-T $= T \in \{0.3, 0.7, 1.2\}$, 4 traces each.}
15	\label{tab:independence}
16	\begin{tabular}{@{}llccrr@{}}
17	\toprule
18	Model & Condition & $\kappa$ & $K_{\text{eff}}$ & SC (\%) & $\Delta$ (pp) \\
19	\midrule
20	Qwen3 (think) & FOLIO & 0.91 & 1.09 & ${\sim}$84 & ${\sim}$0 \\
21	Qwen2.5-14B & LogiQA & 0.82 & 1.20 & 78.50 & $-$0.50 \\
22	Qwen3 & FOLIO & 0.77 & 1.26 & 84.80 & $-$0.49 \\
23	Qwen2.5-14B & FOLIO & 0.74 & 1.30 & 75.49 & $-$0.98 \\
24	Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\
25	\addlinespace
26	Mistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\
27	Mistral-7B & LogiQA & 0.51 & 1.81 & 51.00 & $+$0.50 \\
28	Mistral-7B (s456) & FOLIO & 0.51 & 1.82 & 55.88 & 0.00 \\
29	Mistral-7B & FOLIO & 0.50 & 1.84 & 55.88 & $+$3.43 \\
30	Mistral-7B (s123) & FOLIO & 0.49 & 1.88 & 54.41 & $+$2.94 \\
31	Mistral-7B (s789) & FOLIO & 0.41 & 2.17 & 54.41 & $-$0.49 \\
32	Mistral-7B ($T{=}0.5$) & FOLIO & 0.52 & 1.80 & 58.33 & $-$0.98 \\
33	Mistral-7B (multi-T) & FOLIO & 0.48 & 1.91 & 57.84 & 0.00 \\
34	Mistral-7B ($T{=}1.0$) & FOLIO & 0.48 & 1.91 & 55.39 & 0.00 \\
35	Mistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 & $\mathbf{-2.83}${*} \\
36	\bottomrule
37	\end{tabular}
38	\end{table}
39	
40	
41	\subsection{Symbolic Confirmation Bias}
42	\label{sec:confirmation-bias}
43	
44	The correlation above manifests through a specific mechanism: self-extracted constraints systematically confirm the model's majority answer regardless of correctness. On Mistral-7B FOLIO ($n = 204$), when SICA errs, 83.3\% of extracted constraints support the incorrect majority answer---a bias ratio of $4.97\times$ (raw constraint counts; $4.24\times$ when MaxSAT-weighted) compared to correct problems. Consequently, 94\% of SICA errors overlap with SC errors: symbolic aggregation adds no independent corrective signal.
45	
46	The causal chain is: the model generates an answer, then extracts FOL consistent with it. Constraints from majority-answer traces use trace-specific variable names (56.4\% of cross-answer pairs share zero Z3 variables), so MAX-SAT retains nearly all, and aggregation reduces to a weighted majority vote (Eq.~\ref{eq:degenerate}). Confirmation bias generalizes across model families: bias ratios of $4.97\times$ (Mistral-7B), $3.93\times$ (Qwen2.5-14B), and $2.88{\times}^{\dag}$ (LLaMA-3.1-8B) all significantly exceed $1.0$ ($^{\dag}$based on 4/12 traces due to extraction failures; Table~\ref{tab:cross-model-bias}). The oracle ceiling (\S\ref{sec:oracle}) confirms that 75.9\% of the potential gain is lost to self-extraction quality.
47	
48	
49	\subsection{Process-Level Independence}
50	\label{sec:process-kappa}
51	
52	Answer-level $\kappa$ may underestimate the independence bottleneck: two traces can follow nearly identical reasoning yet reach different final answers, causing $\kappa$ to treat them as disagreeing. We define process similarity as the mean pairwise cosine similarity of TF-IDF trace representations:
53	\begin{equation}
54	\label{eq:process-sim}
55	\text{ProcessSim}(q) = \frac{2}{K(K{-}1)} \sum_{i < j} \cos(\mathbf{v}_i^q, \mathbf{v}_j^q),
56	\end{equation}
57	where $\mathbf{v}_i^q$ is the TF-IDF vector of trace $t_i$ for question $q$. On Mistral-7B FOLIO ($n = 204$), mean ProcessSim is $0.69$, far exceeding answer-level $\kappa = 0.41$. The process--answer correlation is model-strength dependent: $r = -0.06$ ($p = 0.36$) on Mistral-7B, where answer diversity does not reflect reasoning diversity (Figure~\ref{fig:process-kappa}), rising to $r = +0.24$ ($p < 0.001$) on Qwen2.5-14B. This pattern generalizes across four families (Table~\ref{tab:cross-model-process}): the cosine--$\kappa$ gap narrows from $0.23$ (Mistral) to $0.02$ (Qwen-14B), meaning answer-level $\kappa$ already captures the bottleneck for strong models, while process-$\kappa$ reveals hidden homogeneity in weaker models where answer diversity masks process convergence. In all families, interventions targeting answer diversity (temperature scaling, diverse prompting) cannot alter the underlying reasoning paths.
58	
59	\begin{figure}[t]
60	\centering
61	\includegraphics[width=0.85\columnwidth]{figures/fig3_process_kappa_scatter.pdf}
62	\vspace{-2mm}
63	\caption{Answer agreement vs.\ CoT cosine similarity (Mistral-7B, FOLIO, $n{=}204$). Flat regression ($r = -0.06$, $p = 0.36$); stronger models show significant positive correlation ($r = +0.24$, Qwen-14B; Table~\ref{tab:cross-model-process}).}
64	\label{fig:process-kappa}
65	\end{figure}
66	
67	\subsection{Supporting Diagnostics}
68	\label{sec:diagnostics}
69	
70	Further diagnostics---constraint ablation, discriminativeness, entropy decomposition, and hyperparameter sensitivity---confirm the mechanism (Appendices~\ref{app:extraction}--\ref{app:entropy}).
71	
72	
73	\subsection{Remediation Analysis}
74	\label{sec:remediation}
75	\label{sec:interventions}
76	
77	We test more than twenty remediation strategies spanning prompt engineering, method-level redesign, and ten additional directions. All produce neutral or negative results.
78	
79	\paragraph{Prompt-level interventions.} Nine strategies spanning six dimensions (Appendix Table~\ref{tab:remediation}) all fail. Contrastive prompting reduces non-discriminative constraints from 8.2\% to 6.0\%, but newly discriminative constraints still mirror the majority ($\Delta = -1.1$\,pp). Cross-model extraction fails in both directions: weaker models yield 0\% discriminative constraints; stronger models produce accuracy within $\pm 1$\,pp of self-extraction. Multi-temperature sampling ($T \in \{0.3, 0.7, 1.2\}$) yields $\Delta = 0.00$\,pp.
80	
81	\paragraph{Method-level interventions.} ICG ($\Delta \approx 0$, $p = .206$), Contrastive ($\Delta = -9.31$\,pp, $p < 0.01$), and Debate ($\Delta = -18.63$/$-23.00$\,pp, $p < 0.001$) all fail; three of six conditions reach significance, all negative (Table~\ref{tab:method_interventions}, Appendix~\ref{app:remediation}).
82	
83	\paragraph{Additional directions.} Ten further experiments (code verification, iterative refinement, logprob filtering, cross-model ensembles, alternative objectives) all produce neutral-to-negative results (Appendix Table~\ref{tab:additional_interventions}). Cross-model SICA exemplifies the pattern: reducing $\kappa$ from 0.53 to 0.42 yields $\Delta = -0.49$\,pp---cross-architecture diversity is insufficient within self-extraction.
84	
85	\paragraph{Independence-accuracy trade-off.} Table~\ref{tab:kappa_generalization} compares Fleiss' $\kappa$ across four same-model aggregation methods and three model families (Figure~\ref{fig:kappa-accuracy}). SC ($\kappa = 0.44$), Diverse-Prompt ($\kappa = 0.40$), and ICG ($\kappa = 0.47$) cluster at $\kappa \approx 0.40$--$0.47$; Debate reaches $\kappa = 0.15$ but collapses accuracy by $-18.6$\,pp. All three families cluster above $\kappa = 0.40$ (Appendix~\ref{app:cross-model-kappa}), forming a same-model Pareto frontier: methods that increase independence destroy accuracy, and methods preserving accuracy cannot break the correlation floor.
86	
87	\begin{table}[t]
88	\centering
89	\small
90	\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\kappa \geq 0.41$, confirming an architecture-independent ceiling. $\kappa$: Fleiss' kappa on raw answers.}
91	\label{tab:kappa_generalization}
92	\setlength{\tabcolsep}{3.5pt}
93	\begin{tabular}{@{}llccrr@{}}
94	\toprule
95	Model & Aggregation & $\kappa$ & Eff-$K$ & $K$ & Acc.\ (\%) \\
96	\midrule
97	Mistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\
98	& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\
99	& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\
100	& ICG & 0.47 & 1.93 & 10 & 51.96 \\
101	\addlinespace
102	LLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\
103	Qwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\
104	Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.49 \\
105	\bottomrule
106	\end{tabular}
107	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "feaf63eb-7863-4863-b88d-b12095ba532c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\nThis section investigates \\emph{why} SICA fails: trace correlation (\\S\\ref{sec:effective-k}), symbolic confirmation bias (\\S\\ref{sec:confirmation-bias}), process-level independence (\\S\\ref{sec:process-kappa}), supporting diagnostics (\\S\\ref{sec:diagnostics}), and remediation strategies (\\S\\ref{sec:remediation}).\n\n\\subsection{Condorcet Effective-K}\n\\label{sec:effective-k}\n\nTable~\\ref{tab:independence} reports Fleiss' $\\kappa$ and Effective-K (Eq.~\\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\\kappa$ ranges from 0.21 to 0.82, yielding $K_{\\text{eff}} = 1.20\\text{--}3.62$. The four Mistral-7B FOLIO seeds produce $\\kappa \\in [0.41, 0.51]$, yet $\\Delta$ ranges from $+3.43$ to $-0.49$\\,pp---seed-level constraint quality, not independence alone, appears to influence the variation. Two conditions are jointly necessary for positive $\\Delta$: sufficient $K_{\\text{eff}}$ ($\\leq 1.30$ never improves) and sufficient SC accuracy ($K_{\\text{eff}} = 3.62$ with SC $= 39\\%$ produces significant degradation). Cross-model validation confirms universality: all four families produce $\\kappa \\geq 0.41$ (Table~\\ref{tab:kappa_generalization}; Appendix~\\ref{app:cross-model-kappa}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$; positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each.}\n\\label{tab:independence}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Condition & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nQwen3 (think) & FOLIO & 0.91 & 1.09 & ${\\sim}$84 & ${\\sim}$0 \\\\\nQwen2.5-14B & LogiQA & 0.82 & 1.20 & 78.50 & $-$0.50 \\\\\nQwen3 & FOLIO & 0.77 & 1.26 & 84.80 & $-$0.49 \\\\\nQwen2.5-14B & FOLIO & 0.74 & 1.30 & 75.49 & $-$0.98 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\\\\n\\addlinespace\nMistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\\\\nMistral-7B & LogiQA & 0.51 & 1.81 & 51.00 & $+$0.50 \\\\\nMistral-7B (s456) & FOLIO & 0.51 & 1.82 & 55.88 & 0.00 \\\\\nMistral-7B & FOLIO & 0.50 & 1.84 & 55.88 & $+$3.43 \\\\\nMistral-7B (s123) & FOLIO & 0.49 & 1.88 & 54.41 & $+$2.94 \\\\\nMistral-7B (s789) & FOLIO & 0.41 & 2.17 & 54.41 & $-$0.49 \\\\\nMistral-7B ($T{=}0.5$) & FOLIO & 0.52 & 1.80 & 58.33 & $-$0.98 \\\\\nMistral-7B (multi-T) & FOLIO & 0.48 & 1.91 & 57.84 & 0.00 \\\\\nMistral-7B ($T{=}1.0$) & FOLIO & 0.48 & 1.91 & 55.39 & 0.00 \\\\\nMistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 & $\\mathbf{-2.83}${*} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Symbolic Confirmation Bias}\n\\label{sec:confirmation-bias}\n\nThe correlation above manifests through a specific mechanism: self-extracted constraints systematically confirm the model's majority answer regardless of correctness. On Mistral-7B FOLIO ($n = 204$), when SICA errs, 83.3\\% of extracted constraints support the incorrect majority answer---a bias ratio of $4.97\\times$ (raw constraint counts; $4.24\\times$ when MaxSAT-weighted) compared to correct problems. Consequently, 94\\% of SICA errors overlap with SC errors: symbolic aggregation adds no independent corrective signal.\n\nThe causal chain is: the model generates an answer, then extracts FOL consistent with it. Constraints from majority-answer traces use trace-specific variable names (56.4\\% of cross-answer pairs share zero Z3 variables), so MAX-SAT retains nearly all, and aggregation reduces to a weighted majority vote (Eq.~\\ref{eq:degenerate}). Confirmation bias generalizes across model families: bias ratios of $4.97\\times$ (Mistral-7B), $3.93\\times$ (Qwen2.5-14B), and $2.88{\\times}^{\\dag}$ (LLaMA-3.1-8B) all significantly exceed $1.0$ ($^{\\dag}$based on 4/12 traces due to extraction failures; Table~\\ref{tab:cross-model-bias}). The oracle ceiling (\\S\\ref{sec:oracle}) confirms that 75.9\\% of the potential gain is lost to self-extraction quality.\n\n\n\\subsection{Process-Level Independence}\n\\label{sec:process-kappa}\n\nAnswer-level $\\kappa$ may underestimate the independence bottleneck: two traces can follow nearly identical reasoning yet reach different final answers, causing $\\kappa$ to treat them as disagreeing. We define process similarity as the mean pairwise cosine similarity of TF-IDF trace representations:\n\\begin{equation}\n\\label{eq:process-sim}\n\\text{ProcessSim}(q) = \\frac{2}{K(K{-}1)} \\sum_{i < j} \\cos(\\mathbf{v}_i^q, \\mathbf{v}_j^q),\n\\end{equation}\nwhere $\\mathbf{v}_i^q$ is the TF-IDF vector of trace $t_i$ for question $q$. On Mistral-7B FOLIO ($n = 204$), mean ProcessSim is $0.69$, far exceeding answer-level $\\kappa = 0.41$. The process--answer correlation is model-strength dependent: $r = -0.06$ ($p = 0.36$) on Mistral-7B, where answer diversity does not reflect reasoning diversity (Figure~\\ref{fig:process-kappa}), rising to $r = +0.24$ ($p < 0.001$) on Qwen2.5-14B. This pattern generalizes across four families (Table~\\ref{tab:cross-model-process}): the cosine--$\\kappa$ gap narrows from $0.23$ (Mistral) to $0.02$ (Qwen-14B), meaning answer-level $\\kappa$ already captures the bottleneck for strong models, while process-$\\kappa$ reveals hidden homogeneity in weaker models where answer diversity masks process convergence. In all families, interventions targeting answer diversity (temperature scaling, diverse prompting) cannot alter the underlying reasoning paths.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_process_kappa_scatter.pdf}\n\\vspace{-2mm}\n\\caption{Answer agreement vs.\\ CoT cosine similarity (Mistral-7B, FOLIO, $n{=}204$). Flat regression ($r = -0.06$, $p = 0.36$); stronger models show significant positive correlation ($r = +0.24$, Qwen-14B; Table~\\ref{tab:cross-model-process}).}\n\\label{fig:process-kappa}\n\\end{figure}\n\n\\subsection{Supporting Diagnostics}\n\\label{sec:diagnostics}\n\nFurther diagnostics---constraint ablation, discriminativeness, entropy decomposition, and hyperparameter sensitivity---confirm the mechanism (Appendices~\\ref{app:extraction}--\\ref{app:entropy}).\n\n\n\\subsection{Remediation Analysis}\n\\label{sec:remediation}\n\\label{sec:interventions}\n\nWe test more than twenty remediation strategies spanning prompt engineering, method-level redesign, and ten additional directions. All produce neutral or negative results.\n\n\\paragraph{Prompt-level interventions.} Nine strategies spanning six dimensions (Appendix Table~\\ref{tab:remediation}) all fail. Contrastive prompting reduces non-discriminative constraints from 8.2\\% to 6.0\\%, but newly discriminative constraints still mirror the majority ($\\Delta = -1.1$\\,pp). Cross-model extraction fails in both directions: weaker models yield 0\\% discriminative constraints; stronger models produce accuracy within $\\pm 1$\\,pp of self-extraction. Multi-temperature sampling ($T \\in \\{0.3, 0.7, 1.2\\}$) yields $\\Delta = 0.00$\\,pp.\n\n\\paragraph{Method-level interventions.} ICG ($\\Delta \\approx 0$, $p = .206$), Contrastive ($\\Delta = -9.31$\\,pp, $p < 0.01$), and Debate ($\\Delta = -18.63$/$-23.00$\\,pp, $p < 0.001$) all fail; three of six conditions reach significance, all negative (Table~\\ref{tab:method_interventions}, Appendix~\\ref{app:remediation}).\n\n\\paragraph{Additional directions.} Ten further experiments (code verification, iterative refinement, logprob filtering, cross-model ensembles, alternative objectives) all produce neutral-to-negative results (Appendix Table~\\ref{tab:additional_interventions}). Cross-model SICA exemplifies the pattern: reducing $\\kappa$ from 0.53 to 0.42 yields $\\Delta = -0.49$\\,pp---cross-architecture diversity is insufficient within self-extraction.\n\n\\paragraph{Independence-accuracy trade-off.} Table~\\ref{tab:kappa_generalization} compares Fleiss' $\\kappa$ across four same-model aggregation methods and three model families (Figure~\\ref{fig:kappa-accuracy}). SC ($\\kappa = 0.44$), Diverse-Prompt ($\\kappa = 0.40$), and ICG ($\\kappa = 0.47$) cluster at $\\kappa \\approx 0.40$--$0.47$; Debate reaches $\\kappa = 0.15$ but collapses accuracy by $-18.6$\\,pp. All three families cluster above $\\kappa = 0.40$ (Appendix~\\ref{app:cross-model-kappa}), forming a same-model Pareto frontier: methods that increase independence destroy accuracy, and methods preserving accuracy cannot break the correlation floor.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\\kappa \\geq 0.41$, confirming an architecture-independent ceiling. $\\kappa$: Fleiss' kappa on raw answers.}\n\\label{tab:kappa_generalization}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Aggregation & $\\kappa$ & Eff-$K$ & $K$ & Acc.\\ (\\%) \\\\\n\\midrule\nMistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\\\\n& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\\\\n& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\\\\n& ICG & 0.47 & 1.93 & 10 & 51.96 \\\\\n\\addlinespace\nLLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\\\\nQwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\\\\nQwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.49 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
      "numLines": 107,
      "startLine": 1,
      "totalLines": 107
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the intervention strategies. Let me also check the registry for conclusion=negative experiments, and look at the introduction.tex to see how the paper claims "25+".

Let me now systematically extract all interventions from the tables I've read:

**Table 5 (tab:remediation) - 9 prompt-level strategies:**
1. Contrastive prompting (Prompt)
2. Cross-model extraction (Architecture)
3. Qwen3-14B (Capability)
4. Z3 feedback (Solver)
5. Constraint filtering (Noise)


6. Cross-trace UNSAT (Independence)
7. T=1.0 (Diversity)
8. Multi-temp (Diversity)
9. Discriminative filtering (Filtering)

**Table 6 (tab:method_interventions) - 3 method-level strategies:**
10. ICG (Trace coupling)
11. Contrastive scoring (Scoring bias)
12. Debate (Role diversity)

**Table 7 (tab:additional_interventions) - 11 additional strategies:**
13. PROVE (code verification)
14. CEGIS (iterative)
15. DeepConf (logprob)
16. Cross-model SICA
17. Problem perturbation
18. MIN

-UNSAT
19. κ-aware SC
20. Z3 trace filter
21. Bootstrapped gold
22. Selective abstention
23. ASCII perturbation

That brings the total to 23 explicitly numbered strategies across the tables. Beyond these, the paper also tests various configurations like different temperature settings and model variants that aren't strictly remediation strategies but represent different experimental conditions.

Looking back at the paper's actual claims about the count, I see it mentions "more than twenty remediation strategies" in the analysis and experiments sections, while the appendix table caption references "22+ distinct approaches." Let me verify the exact phrasing in the introduction and other key sections to pin down what the paper is actually claiming.

Now I need to check the registry to see if there are any experiments that reached negative conclusions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "e48c851c-beee-4029-b139-960fec32aa7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBxm7PUYAUMhkei4FNtv6Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30215,
      "cache_read_input_tokens": 25325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30215
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

_source line 43_

Now let me check the introduction for the exact "25+" claim and the registry for negative experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "032c65a8-92c3-4829-93e5-436f1ea958b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBxm7PUYAUMhkei4FNtv6Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30215,
      "cache_read_input_tokens": 25325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30215
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

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01UFLYJEuN4hNP2TUtC4NxUi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "ce903676-873f-4d5a-a052-ae87003fc547",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBxm7PUYAUMhkei4FNtv6Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30215,
      "cache_read_input_tokens": 25325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30215
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

_source line 45 · 2026-05-20T13:32:13.809Z_

<details><summary>↩ Tool result · `toolu_01UFLYJEuN4hNP2TUtC4NxUi`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this to a degree, but the core limitation persists.
10	Recent neuro-symbolic methods---Logic-LM \citep{pan2023logiclm}, LINC \citep{olausson2023linc}, DyLoS \citep{xu2026dylos}, Aristotle \citep{li2025aristotle}, FoVer \citep{wang2025fover}, LogicAgent \citep{luo2025logicagent}---each report gains on logical reasoning, but introduce components beyond the reasoning model: trained verifiers, solver selection, or external knowledge.
11	A simpler question precedes these: can the \emph{same} model that generates reasoning traces also extract useful formal constraints from them?
12	Self-extraction would be a zero-cost upgrade requiring no additional model, training data, or external prover.
13	Yet no prior work has systematically evaluated whether self-extracted constraints are useful for aggregation.
14	
15	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
16	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
17	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding Effective-$K = 1.20$--$3.62$ for nominal $K = 12$: traces beyond a dozen add negligible independent information (\S\ref{sec:effective-k}).
18	The bottleneck runs deeper than answer-level agreement suggests.
19	Chain-of-thought cosine similarity ($0.69$) far exceeds answer-level $\kappa$ ($0.41$), revealing that traces share reasoning processes even when they diverge on final answers (\S\ref{sec:process-kappa}).
20	When the same model extracts FOL constraints from these correlated traces, the constraints exhibit \emph{symbolic confirmation bias}: on problems where the model errs, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC (\S\ref{sec:confirmation-bias}).
21	Self-extraction cannot supply the independent signal that CJT requires.
22	
23	We study this through Symbolic Invariant Consensus Aggregation (SICA): extract FOL constraints from each of $K$ reasoning traces, deduplicate by syntactic equivalence, and select the answer best supported by a weighted partial MAX-SAT solution via Z3 \citep{demoura2008z3} (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}).
24	We evaluate SICA across six models (7B--32B), three reasoning domains (FOLIO \citep{han2022folio}, ProofWriter \citep{tafjord2021proofwriter}, LogiQA \citep{liu2020logiqa}), and over 3,000 condition-evaluations (${\sim}$1,250 unique instances) with four-seed replication (Table~\ref{tab:main_results}).
25	More than twenty-five remediation strategies---spanning prompt engineering, method-level redesign, and ten additional directions targeting the independence bottleneck---all produce neutral or negative results, confirming the bottleneck is structural at the 7B--32B scale tested.
26	
27	Oracle controls confirm the aggregation mechanism is sound: gold FOL yields $+14.22$\,pp on FOLIO and $+11.50$\,pp on ProofWriter ($p < 0.001$), yet self-extraction captures only 24\% of this ceiling (\S\ref{sec:oracle}).
28	The central finding is a fundamental independence-accuracy trade-off: Debate reduces $\kappa$ from 0.44 to 0.15 (tripling Eff-$K$) but collapses accuracy by $-18.6$\,pp; SC, Diverse-Prompt, and ICG all cluster at $\kappa \approx 0.40$--$0.47$, forming a same-model ceiling that holds across three model families (\S\ref{sec:remediation}).
29	A cross-architecture proof-of-concept demonstrates that this gap is recoverable: DeBERTa-large NLI combined with SC achieves $+3.43$\,pp ($p = 0.039$, McNemar exact test) through per-label complementarity (\S\ref{sec:cross-arch}).
30	
31	Our contributions are:
32	\begin{enumerate}[nosep,leftmargin=*]
33	\item \textbf{Independence-Accuracy Trade-off and Cross-Architecture Escape.} Fleiss' $\kappa$ across four aggregation methods and three model families reveals a same-model Pareto frontier ($\kappa \geq 0.40$). Twenty-five+ remediation strategies fail; a cross-architecture NLI verifier (DeBERTa-large, $+3.43$\,pp, $p = 0.039$) demonstrates the frontier is escapable (\S\ref{sec:remediation}, \S\ref{sec:cross-arch}).
34	
35	\item \textbf{Symbolic Confirmation Bias.} On incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC (\S\ref{sec:confirmation-bias}).
36	
37	\item \textbf{Process-Level Independence.} Across four model families, CoT cosine similarity ($0.69$--$0.79$) far exceeds answer-level $\kappa$ ($0.45$--$0.74$); the gap intensifies with model capability ($r = 0.23$, $p \leq 0.001$ for Qwen vs.\ $r \approx 0$ for Mistral/LLaMA), showing reasoning homogeneity is architecture-independent (\S\ref{sec:process-kappa}).
38	
39	\item \textbf{Regime-Dependent Diagnostics.} Three failure modes create regime boundaries; $C_0$ combined with SC accuracy provides a zero-cost diagnostic predicting when symbolic augmentation is unlikely to help (\S\ref{sec:main-results}).
40	\end{enumerate}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "fca262f0-5699-45b4-bdcf-ada9077d43ed",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nTest-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \\citep{snell2025scaling, guo2025deepseekr1}.\nThe dominant aggregation strategy, Self-Consistency (SC) \\citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.\nSC is simple, model-agnostic, and effective---but it is hitting a ceiling.\n\\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.\nThe gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.\n\nConfidence-weighted \\citep{taubenfeld2025cisc} and universal \\citep{chen2024usc} extensions alleviate this to a degree, but the core limitation persists.\nRecent neuro-symbolic methods---Logic-LM \\citep{pan2023logiclm}, LINC \\citep{olausson2023linc}, DyLoS \\citep{xu2026dylos}, Aristotle \\citep{li2025aristotle}, FoVer \\citep{wang2025fover}, LogicAgent \\citep{luo2025logicagent}---each report gains on logical reasoning, but introduce components beyond the reasoning model: trained verifiers, solver selection, or external knowledge.\nA simpler question precedes these: can the \\emph{same} model that generates reasoning traces also extract useful formal constraints from them?\nSelf-extraction would be a zero-cost upgrade requiring no additional model, training data, or external prover.\nYet no prior work has systematically evaluated whether self-extracted constraints are useful for aggregation.\n\nWe ground our analysis in the Condorcet Jury Theorem (CJT) \\citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \\citep{austensmith1996}.\nWhen independence fails \\citep{ladha1992correlated}, additional samples carry diminishing information.\nMeasuring inter-trace agreement with Fleiss' $\\kappa$ \\citep{fleiss1971kappa}, we find $\\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding Effective-$K = 1.20$--$3.62$ for nominal $K = 12$: traces beyond a dozen add negligible independent information (\\S\\ref{sec:effective-k}).\nThe bottleneck runs deeper than answer-level agreement suggests.\nChain-of-thought cosine similarity ($0.69$) far exceeds answer-level $\\kappa$ ($0.41$), revealing that traces share reasoning processes even when they diverge on final answers (\\S\\ref{sec:process-kappa}).\nWhen the same model extracts FOL constraints from these correlated traces, the constraints exhibit \\emph{symbolic confirmation bias}: on problems where the model errs, 83.3\\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\\times$), and 94\\% of errors overlap with SC (\\S\\ref{sec:confirmation-bias}).\nSelf-extraction cannot supply the independent signal that CJT requires.\n\nWe study this through Symbolic Invariant Consensus Aggregation (SICA): extract FOL constraints from each of $K$ reasoning traces, deduplicate by syntactic equivalence, and select the answer best supported by a weighted partial MAX-SAT solution via Z3 \\citep{demoura2008z3} (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}).\nWe evaluate SICA across six models (7B--32B), three reasoning domains (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}, LogiQA \\citep{liu2020logiqa}), and over 3,000 condition-evaluations (${\\sim}$1,250 unique instances) with four-seed replication (Table~\\ref{tab:main_results}).\nMore than twenty-five remediation strategies---spanning prompt engineering, method-level redesign, and ten additional directions targeting the independence bottleneck---all produce neutral or negative results, confirming the bottleneck is structural at the 7B--32B scale tested.\n\nOracle controls confirm the aggregation mechanism is sound: gold FOL yields $+14.22$\\,pp on FOLIO and $+11.50$\\,pp on ProofWriter ($p < 0.001$), yet self-extraction captures only 24\\% of this ceiling (\\S\\ref{sec:oracle}).\nThe central finding is a fundamental independence-accuracy trade-off: Debate reduces $\\kappa$ from 0.44 to 0.15 (tripling Eff-$K$) but collapses accuracy by $-18.6$\\,pp; SC, Diverse-Prompt, and ICG all cluster at $\\kappa \\approx 0.40$--$0.47$, forming a same-model ceiling that holds across three model families (\\S\\ref{sec:remediation}).\nA cross-architecture proof-of-concept demonstrates that this gap is recoverable: DeBERTa-large NLI combined with SC achieves $+3.43$\\,pp ($p = 0.039$, McNemar exact test) through per-label complementarity (\\S\\ref{sec:cross-arch}).\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Independence-Accuracy Trade-off and Cross-Architecture Escape.} Fleiss' $\\kappa$ across four aggregation methods and three model families reveals a same-model Pareto frontier ($\\kappa \\geq 0.40$). Twenty-five+ remediation strategies fail; a cross-architecture NLI verifier (DeBERTa-large, $+3.43$\\,pp, $p = 0.039$) demonstrates the frontier is escapable (\\S\\ref{sec:remediation}, \\S\\ref{sec:cross-arch}).\n\n\\item \\textbf{Symbolic Confirmation Bias.} On incorrect problems, 83.3\\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\\times$), and 94\\% of errors overlap with SC (\\S\\ref{sec:confirmation-bias}).\n\n\\item \\textbf{Process-Level Independence.} Across four model families, CoT cosine similarity ($0.69$--$0.79$) far exceeds answer-level $\\kappa$ ($0.45$--$0.74$); the gap intensifies with model capability ($r = 0.23$, $p \\leq 0.001$ for Qwen vs.\\ $r \\approx 0$ for Mistral/LLaMA), showing reasoning homogeneity is architecture-independent (\\S\\ref{sec:process-kappa}).\n\n\\item \\textbf{Regime-Dependent Diagnostics.} Three failure modes create regime boundaries; $C_0$ combined with SC accuracy provides a zero-cost diagnostic predicting when symbolic augmentation is unlikely to help (\\S\\ref{sec:main-results}).\n\\end{enumerate}\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015M3sQtHTDqQuLm5j2ooJ4K`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "3d83c548-6174-414f-9a0c-64f75bdaf8d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBxm7PUYAUMhkei4FNtv6Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30215,
      "cache_read_input_tokens": 25325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30215
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

_source line 47 · 2026-05-20T13:32:14.028Z_

<details><summary>↩ Tool result · `toolu_015M3sQtHTDqQuLm5j2ooJ4K`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "cf911aa0-917c-4159-a270-d8cfc50942ab",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Now let me check the registry for negative-conclusion experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "ee9105a9-71af-4f2f-975e-169168e363e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGKajMLxUo4ziXHBkSbMsj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 55540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3172
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

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01L21h2aodiZHc7nNBJLrSC9`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "filters": {
    "conclusion": "negative"
  },
  "limit": 0,
  "fields": [
    "experiment_id",
    "title",
    "conclusion",
    "status"
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
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "7a5bd30c-0902-4ae6-ad68-bb7127c62b19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGKajMLxUo4ziXHBkSbMsj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3172,
      "cache_read_input_tokens": 55540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3172
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

_source line 50 · 2026-05-20T13:32:18.187Z_

<details><summary>↩ Tool result · `toolu_01L21h2aodiZHc7nNBJLrSC9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-wave3-dir-k-minority\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wave3-dir-i-z3-filter\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wave3-dir-j-bootstrap\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-cross-model-phase2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-d-cegis\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild6-kappa-aware-sc\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild1-max-unsat\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild4-process-kappa\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-a-prove\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-b-deepconf\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild3-perturbation\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild2-ascii\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-084-debate-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-082-contrastive-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-081-debate-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-085-contrastive-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-075b-contrastive-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-080-contrastive-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-078-debate-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-078\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-083-icg-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074d-icg-mistral-folio-seed456\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-077-kappa-generalization\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-077\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-075b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074c-icg-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-076-debate-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-079-icg-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-072b-llama8b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074-icg-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-071-qwen7b-logiqa200-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-048-llama8b-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-069-llama8b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-065-qwen7b-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-062-gemma27b-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-069-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-068-qwen3-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-063-llama8b-folio204-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-063-llama8b-folio204\": {\"status\": \"PREPARING\", \"conclusion\": \"negative\"}, \"exp-061-qwen7b-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-063\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-040-qwen3-pw600-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-060-cross-qwen25-14b-extractor\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-057-mistral-folio204-t03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-034\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-039-14b-pw600-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-058-mistral-folio204-t05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-055-multitemp-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-054-mistral-folio204-t10\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-046-mistral-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-053\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-050b-mistral-icl-oracle\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-049b-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-044b-icl-oracle\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-041-14b-folio204-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-045-backward-verification\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-038-14b-logiqa200-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-035\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-036b-cross-trace-unsat\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-043-consistency-filtering\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-036-z3-feedback-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-030-crossmodel-mistral-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-029-contrastive-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t07\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-004-qwen7b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t10\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-012-gsm8k-pilot\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-014-deepseek-r1-7b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-010-mistral-v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-019-llama8b-strategyqa-200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-020-llama8b-folio-204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"pilot-constraint-filtering\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"sica_temp_diversity\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-005\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}}, \"count\": 76, \"total\": 76, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4218}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "4ecf8cb7-2a20-42f1-8ea6-446fc928131b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp-wave3-dir-k-minority\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wave3-dir-i-z3-filter\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wave3-dir-j-bootstrap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-cross-model-phase2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-direction-d-cegis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wild6-kappa-aware-sc\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wild1-max-unsat\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wild4-process-kappa\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-direction-a-prove\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-direction-b-deepconf\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wild3-perturbation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-wild2-ascii\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-084-debate-mistral-logiqa-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-082-contrastive-mistral-folio-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-081-debate-mistral-folio-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-085-contrastive-mistral-logiqa-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-075b-contrastive-mistral-folio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-080-contrastive-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-078-debate-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-078\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-083-icg-mistral-logiqa-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-074d-icg-mistral-folio-seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-077-kappa-generalization\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-077\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-075b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-074c-icg-mistral-folio-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-076-debate-mistral-folio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-079-icg-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-072b-llama8b-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-074-icg-mistral-folio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-071-qwen7b-logiqa200-seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-048-llama8b-pw600\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-069-llama8b-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-065-qwen7b-pw600\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-062-gemma27b-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-069-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-068-qwen3-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-063-llama8b-folio204-16639\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-063-llama8b-folio204\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-061-qwen7b-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-063\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-040-qwen3-pw600-16639\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-060-cross-qwen25-14b-extractor\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-057-mistral-folio204-t03\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-034\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-039-14b-pw600-16639\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-058-mistral-folio204-t05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-055-multitemp-mistral-folio\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-054-mistral-folio204-t10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-046-mistral-pw600\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-053\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-050b-mistral-icl-oracle\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-049b-mistral-logiqa200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-044b-icl-oracle\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-041-14b-folio204-16639\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-045-backward-verification\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-038-14b-logiqa200-16639\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-035\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-036b-cross-trace-unsat\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-043-consistency-filtering\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-036-z3-feedback-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-030-crossmodel-mistral-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-029-contrastive-folio204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"temperature-ablation-t07\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-004-qwen7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"temperature-ablation-t10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-012-gsm8k-pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"temperature-ablation-t05\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"temperature-ablation-t03\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-014-deepseek-r1-7b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-010-mistral-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-019-llama8b-strategyqa-200\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-020-llama8b-folio-204\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"pilot-constraint-filtering\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"sica_temp_diversity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}}, \\\"count\\\": 76, \\\"total\\\": 76, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4218}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-wave3-dir-k-minority\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wave3-dir-i-z3-filter\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wave3-dir-j-bootstrap\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-cross-model-phase2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-d-cegis\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild6-kappa-aware-sc\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild1-max-unsat\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild4-process-kappa\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-a-prove\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-direction-b-deepconf\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild3-perturbation\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-wild2-ascii\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-084-debate-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-082-contrastive-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-081-debate-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-085-contrastive-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-075b-contrastive-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-080-contrastive-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-078-debate-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-078\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-083-icg-mistral-logiqa-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074d-icg-mistral-folio-seed456\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-077-kappa-generalization\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-077\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-075b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074c-icg-mistral-folio-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-076-debate-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-079-icg-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-072b-llama8b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-074-icg-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-071-qwen7b-logiqa200-seed123\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-048-llama8b-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-069-llama8b-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-065-qwen7b-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-062-gemma27b-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-069-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-068-qwen3-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-063-llama8b-folio204-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-063-llama8b-folio204\": {\"status\": \"PREPARING\", \"conclusion\": \"negative\"}, \"exp-061-qwen7b-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-063\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-040-qwen3-pw600-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-060-cross-qwen25-14b-extractor\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-057-mistral-folio204-t03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-034\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-039-14b-pw600-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-058-mistral-folio204-t05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-055-multitemp-mistral-folio\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-054-mistral-folio204-t10\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-046-mistral-pw600\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-053\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-050b-mistral-icl-oracle\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-049b-mistral-logiqa200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-044b-icl-oracle\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-041-14b-folio204-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-045-backward-verification\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-038-14b-logiqa200-16639\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-035\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-036b-cross-trace-unsat\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-043-consistency-filtering\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-036-z3-feedback-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-030-crossmodel-mistral-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-029-contrastive-folio204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t07\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-004-qwen7b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t10\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-012-gsm8k-pilot\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t05\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"temperature-ablation-t03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-014-deepseek-r1-7b\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-010-mistral-v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-019-llama8b-strategyqa-200\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-020-llama8b-folio-204\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"pilot-constraint-filtering\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"sica_temp_diversity\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-005\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}}, \"count\": 76, \"total\": 76, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4218}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
76 negative-conclusion experiments in the registry. Now let me also check for other conclusions to get the full picture.

Let me now compile the complete analysis from the paper tables.

From the paper, the explicit intervention strategies are:

**Table 5 (tab:remediation) — 9 prompt-level strategies:**
1. Contrastive prompting (Prompt)
2. Cross-model extraction (Architecture)
3. Qwen3-14B (Capability)
4. Z3 feedback (Solver)
5. Constraint filtering (Noise)


6. Cross-trace UNSAT (Independence)
7. T=1.0 (Diversity)
8. Multi-temp (Diversity)
9. Discriminative filtering (Filtering)

**Table 6 (tab:method_interventions) — 3 method-level strategies:**
10. ICG (Trace coupling)
11. Contrastive scoring (Scoring bias)
12. Debate (Role diversity)

**Table 7 (tab:additional_interventions) — 11 additional strategies:**
13. PROVE (code verification)
14. CEGIS (iterative refinement)
15. DeepConf (confidence-based filtering)
16. Cross-model SICA
17. Problem perturbation
18. MIN-UNSAT
19. κ-aware SC
20. Z3 trace filter
21. Bootstrapped gold
22. Selective abstention
23. ASCII perturbation

That gives me 23 explicitly numbered configurations across the tables. But there's a mismatch with what the paper claims—it mentions "25+" in the introduction and "22+ distinct approaches" in the Table 7 footnote. I'm noticing some strategies have variants that might be counted separately, like Cross-model having two directional configurations and Multi-temp having specific parameter settings, which could account for the discrepancy.

Looking at what's missing from the tables themselves, there's the ICL with gold FOL setup from Table 1, the backward-verification experiment in the registry, and constraint filtering that don't appear in Tables 5-7. The paper explicitly numbers methods 1-12 in Tables 5-6, but when I look at how the strategies break down—nine prompt-level approaches, three method-level ones like ICG and Contrastive and Debate, plus the additional experiments in Table 7—I'm trying to figure out where exactly the "25+" count comes from. Looking at the registry, there are 76 negative experiments total, but most are just replications or different seeds of the same underlying strategy—the paper's "25+" refers to the distinct approaches themselves. Let me organize the 23 table entries by strategy family to see how many unique approaches we're actually dealing with. Temperature and diversity tuning form one family since both T=1.0 and multi-temp target the same mechanism, while contrastive approaches split into prompt-level and method-level variants that work quite differently. Temperature diversity with T=1.0 and multi-temperature sampling gives me two configurations there. Then I'm moving through discriminative filtering to remove unhelpful constraints, independent constraint generation, contrastive scoring with pro/con framing, LLM debate, code verification with PROVE, iterative refinement using CEGIS, logprob-based confidence filtering, cross-model SICA, problem perturbation, and alternative approaches.

Continuing through solver-based objectives with MIN-UNSAT, kappa-aware weighted voting, Z3-based trace filtering, bootstrapped self-improvement, selective abstention, and ASCII/format perturbation — that brings me to 22 distinct families across 23 total configurations.

Now I'm wondering if cross-model extraction at position #2 and cross-model SICA at position #16 are actually the same family or if they're meaningfully different approaches.  Looking at the specifics, #2 involves weak-to-strong extraction where Mistral extracts from Qwen traces, while #16 is the broader cross-model ensemble with kappa comparisons showing different agreement levels. They're related but operate at different levels, so I should probably keep them separate since the paper treats them as distinct methods. Same consideration applies to contrastive prompting versus contrastive scoring — both use contrastive framing but target different stages of the pipeline.

Rather than force subjective groupings, I'll organize by the core mechanism: diversity through temperature variation, cross-model approaches, contrastive methods at different levels, iterative self-improvement techniques, input perturbations, and constraint-based filtering strategies. But I'm realizing this taxonomy is getting unwieldy, so let me just count what's actually documented in the tables and present a straightforward breakdown.

The tables show 23 distinct techniques across three tables—9 at the prompt level, 3 at the method level, and 11 additional ones. The "25+" claim in the introduction could account for this by including ICL with gold FOL examples from Table 1 or backward verification from the registry, depending on how you count. The exact number hinges on whether you're counting cross-model approaches as one or two separate directions. So there's a gap between the stated claim and what's explicitly enumerated, though the difference is minor.

Now I'm organizing these 23 techniques into strategy families based on what mechanism they target. The grouping spans prompt-level extraction improvements like contrastive prompting and cross-model extraction, solver and constraint filtering approaches like Z3 feedback and consistency filtering, trace diversity methods using different temperatures and perturbations, method-level redesigns such as ICG and debate, alternative solver objectives like MIN-UNSAT, cross-model ensembles, input perturbation, iterative refinement through CEGIS and bootstrapping, code verification via PROVE, trace filtering, and selective abstention for diagnostic purposes.

I should verify whether the paper's "25+" claim accounts for all these enumerated configurations or if there are additional minor variants not explicitly listed in the tables—the gap might come from techniques like ICL with gold FOL or backward verification that appear in the text but not as separate rows.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "3599a4ec-f7dd-4e43-b78d-f2ea292a559b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBJBquxN864BFHKS7WWvH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2740,
      "cache_read_input_tokens": 58712,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2740
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

_source line 52_

Now let me also check if there are any additional strategies mentioned elsewhere (e.g., the cross-architecture DeBERTa experiment, ICL with gold FOL).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "3cf4dcf9-cffa-4801-af14-f1218d665b97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBJBquxN864BFHKS7WWvH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2740,
      "cache_read_input_tokens": 58712,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2740
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

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_012futYwuGRUjXirUxYzxtwi`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "limit": 0,
  "fields": [
    "experiment_id",
    "conclusion",
    "status"
  ],
  "filters": {
    "conclusion": "positive"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "71f8a6ae-c1c2-463b-a74a-7be44fde28e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBJBquxN864BFHKS7WWvH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2740,
      "cache_read_input_tokens": 58712,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2740
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

_source line 54 · 2026-05-20T13:33:19.781Z_

<details><summary>↩ Tool result · `toolu_012futYwuGRUjXirUxYzxtwi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4085}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "03b12448-678f-470d-9cff-ab115f8b8c91",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4085}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4085}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Grep · `toolu_019rGHw7XSDGAG8VDpVGewgt`</summary>

```json
{
  "pattern": "backward.verification|ICL.*gold|in-context.*gold|cross-arch|DeBERTa",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "4601e114-9497-4f38-899e-fe4d59a92bbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBJBquxN864BFHKS7WWvH8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2740,
      "cache_read_input_tokens": 58712,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2740
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

_source line 56 · 2026-05-20T13:33:21.767Z_

<details><summary>↩ Tool result · `toolu_019rGHw7XSDGAG8VDpVGewgt`</summary>

```text
docs/paper/analysis.tex:83:\paragraph{Additional directions.} Ten further experiments (code verification, iterative refinement, logprob filtering, cross-model ensembles, alternative objectives) all produce neutral-to-negative results (Appendix Table~\ref{tab:additional_interventions}). Cross-model SICA exemplifies the pattern: reducing $\kappa$ from 0.53 to 0.42 yields $\Delta = -0.49$\,pp---cross-architecture diversity is insufficient within self-extraction.
docs/paper/experiments.tex:26:\caption{SICA vs.\ SC across all conditions sorted by SC accuracy. $\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\dagger$\,$n < 100$ (suggestive only). \textbf{Bold $\Delta$}: $p < 0.05$ (McNemar). {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$. Failure modes detailed in Appendix~\ref{app:failure-modes}.}
docs/paper/experiments.tex:66:\paragraph{Type A (SC $\geq$ 60\%): confirmation bias.} All nine Type~A conditions (SC $\geq 60\%$, combined $N > 2{,}800$) produce no significant positive effects. The largest positive trend is LLaMA-3.1-8B on StrategyQA ($\Delta = +2.00$\,pp, $p = 0.424$, n.s.), while Qwen2.5-14B on ProofWriter shows significant degradation ($\Delta = -2.50$\,pp, $p = 0.011$). Even in-context learning with gold FOL examples ($\Delta = +0.50$\,pp, n.s.) cannot break confirmation bias.
docs/paper/main.bbl:87:\bibitem[{He et~al.(2021)He, Liu, Gao, and Chen}]{he2021deberta}
docs/paper/main.bbl:89:\newblock {DeBERTa}: Decoding-enhanced {BERT} with disentangled attention.
docs/paper/conclusion.tex:3:[Omitted long matching line]
docs/paper/main.log:1064: []\T1/ptm/b/n/10.95 (+20) Why cross-architecture ver-i-fi-ca-tion works.[]
docs/paper/discussion.tex:4:[Omitted long matching line]
docs/paper/diagnosis.tex:9:\caption{SICA vs.\ SC across all conditions sorted by SC accuracy. $\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\dagger$\,$n < 100$ (suggestive only). \textbf{Bold $\Delta$}: $p < 0.05$ (McNemar). {*}\,$p < 0.05$;\enspace{**}\,$p < 0.01$;\enspace{***}\,$p < 0.001$. Failure modes detailed in Appendix~\ref{app:failure-modes}.}
docs/paper/diagnosis.tex:114:\paragraph{Type A (SC $\geq$ 60\%).} All nine Type~A conditions produce no significant positive effects. Even in-context learning with gold FOL examples yields $\Delta = +0.50$\,pp (n.s.). Qwen2.5-14B on ProofWriter shows significant degradation ($\Delta = -2.50$\,pp, $p = 0.011$).
docs/paper/limitations_content.tex:5:[Omitted long matching line]
docs/paper/abstract.tex:8:However, a cross-architecture proof-of-concept---DeBERTa-large NLI combined with SC---achieves $+4.41$\,pp ($w{=}3$; McNemar $p = 0.039$ at $w{=}1$) through per-label complementarity, demonstrating that the oracle gap is practically recoverable when verification signal comes from outside the reasoning model's distribution.
docs/paper/solutions.tex:4:The analyses in \S\ref{sec:confirmation-bias}--\S\ref{sec:remediation} identify two structural causes of SICA's failure: constraints are coupled to their source answer (confirmation bias), and all traces share the same model distribution (independence bottleneck). We investigate two complementary approaches: decoupling constraints from answers within the same model (\S\ref{sec:decoupling}), and injecting an architecturally independent verification signal (\S\ref{sec:cross-arch}).
docs/paper/solutions.tex:15:\subsection{Cross-Architecture NLI Verification}
docs/paper/solutions.tex:16:\label{sec:cross-arch}
docs/paper/solutions.tex:21:We test this with DeBERTa-large \citep{he2021deberta} (${\sim}$350M parameters, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}. For each problem, DeBERTa classifies the (premise, conclusion) pair into \textsc{entailment}, \textsc{contradiction}, or \textsc{neutral}. In combo mode, the NLI verdict is integrated with SC's $K$ votes via a weight parameter $w$: each NLI-supporting vote counts $w$ times. We evaluate on Mistral-7B FOLIO ($n = 204$).
docs/paper/solutions.tex:24:[Omitted long matching line]
docs/paper/solutions.tex:27:[Omitted long matching line]
docs/paper/solutions.tex:29:\paragraph{Why cross-architecture verification works.}
docs/paper/solutions.tex:30:The ${\sim}$350M encoder-only model and the 7B decoder-only LLM share no architecture, training data, or inference mechanism. DeBERTa classifies textual entailment rather than generating chain-of-thought, so it does not exhibit the symbolic confirmation bias identified in \S\ref{sec:confirmation-bias}. The two systems err on different problem subsets, satisfying the independence condition that same-model sampling cannot provide.
docs/paper/introduction.tex:29:A cross-architecture proof-of-concept demonstrates that this gap is recoverable: DeBERTa-large NLI combined with SC achieves $+4.41$\,pp ($w{=}3$; McNemar $p = 0.039$ at $w{=}1$) through per-label complementarity (\S\ref{sec:cross-arch}).
docs/paper/introduction.tex:33:\item \textbf{Independence-Accuracy Trade-off and Cross-Architecture Escape.} Fleiss' $\kappa$ across four aggregation methods and three model families reveals a same-model Pareto frontier ($\kappa \geq 0.40$). Twenty-five+ remediation strategies fail; a cross-architecture NLI verifier (DeBERTa-large, $+4.41$\,pp; McNemar $p = 0.039$ at $w{=}1$) demonstrates the frontier is escapable (\S\ref{sec:remediation}, \S\ref{sec:cross-arch}).
docs/paper/references.bib:321:%%% Cross-Architecture Verification %%%
docs/paper/references.bib:323:@inproceedings{he2021deberta,
docs/paper/references.bib:324:  title={{DeBERTa}: Decoding-enhanced {BERT} with Disentangled Attention},
docs/paper/main.aux:483:\@writefile{lot}{\contentsline {table}{\numberline {1}{\ignorespaces SICA vs.\ SC across all conditions sorted by SC accuracy. $\Delta $ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\dagger $\,$n < 100$ (suggestive only). \textbf  {Bold $\Delta $}: $p < 0.05$ (McNemar). {*}\,$p < 0.05$;\enspace  {**}\,$p < 0.01$;\enspace  {***}\,$p < 0.001$. Failure modes detailed in Appendix~\ref {app:failure-modes}.}}{5}{table.caption.16}\protected@file@percent }
docs/paper/main.aux:484:\newlabel{tab:main_results}{{1}{5}{SICA vs.\ SC across all conditions sorted by SC accuracy. $\Delta $ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\dagger $\,$n < 100$ (suggestive only). \textbf {Bold $\Delta $}: $p < 0.05$ (McNemar). {*}\,$p < 0.05$;\enspace {**}\,$p < 0.01$;\enspace {***}\,$p < 0.001$. Failure modes detailed in Appendix~\ref {app:failure-modes}}{table.caption.16}{}}
docs/paper/main.aux:604:\citation{he2021deberta}
docs/paper/main.aux:704:\@writefile{toc}{\contentsline {subsection}{\numberline {6.2}Cross-Architecture NLI Verification}{7}{subsection.6.2}\protected@file@percent }
docs/paper/main.aux:705:\newlabel{sec:cross-arch}{{6.2}{7}{Cross-Architecture NLI Verification}{subsection.6.2}{}}
docs/paper/main.aux:706:\newlabel{sec:cross-arch@cref}{{[subsection][2][6]6.2}{[1][7][]7}{}{}{}}
docs/paper/main.aux:753:\@writefile{toc}{\contentsline {paragraph}{Why cross-architecture verification works.}{8}{section*.32}\protected@file@percent }
docs/paper/main.aux:833:\bibcite{he2021deberta}{{13}{2021}{{He et~al.}}{{He, Liu, Gao, and Chen}}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "859822ad-421c-446e-895e-ca9c67dcc686",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:83:\\paragraph{Additional directions.} Ten further experiments (code verification, iterative refinement, logprob filtering, cross-model ensembles, alternative objectives) all produce neutral-to-negative results (Appendix Table~\\ref{tab:additional_interventions}). Cross-model SICA exemplifies the pattern: reducing $\\kappa$ from 0.53 to 0.42 yields $\\Delta = -0.49$\\,pp---cross-architecture diversity is insufficient within self-extraction.\ndocs/paper/experiments.tex:26:\\caption{SICA vs.\\ SC across all conditions sorted by SC accuracy. $\\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\\dagger$\\,$n < 100$ (suggestive only). \\textbf{Bold $\\Delta$}: $p < 0.05$ (McNemar). {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$. Failure modes detailed in Appendix~\\ref{app:failure-modes}.}\ndocs/paper/experiments.tex:66:\\paragraph{Type A (SC $\\geq$ 60\\%): confirmation bias.} All nine Type~A conditions (SC $\\geq 60\\%$, combined $N > 2{,}800$) produce no significant positive effects. The largest positive trend is LLaMA-3.1-8B on StrategyQA ($\\Delta = +2.00$\\,pp, $p = 0.424$, n.s.), while Qwen2.5-14B on ProofWriter shows significant degradation ($\\Delta = -2.50$\\,pp, $p = 0.011$). Even in-context learning with gold FOL examples ($\\Delta = +0.50$\\,pp, n.s.) cannot break confirmation bias.\ndocs/paper/main.bbl:87:\\bibitem[{He et~al.(2021)He, Liu, Gao, and Chen}]{he2021deberta}\ndocs/paper/main.bbl:89:\\newblock {DeBERTa}: Decoding-enhanced {BERT} with disentangled attention.\ndocs/paper/conclusion.tex:3:[Omitted long matching line]\ndocs/paper/main.log:1064: []\\T1/ptm/b/n/10.95 (+20) Why cross-architecture ver-i-fi-ca-tion works.[]\ndocs/paper/discussion.tex:4:[Omitted long matching line]\ndocs/paper/diagnosis.tex:9:\\caption{SICA vs.\\ SC across all conditions sorted by SC accuracy. $\\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\\dagger$\\,$n < 100$ (suggestive only). \\textbf{Bold $\\Delta$}: $p < 0.05$ (McNemar). {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$. Failure modes detailed in Appendix~\\ref{app:failure-modes}.}\ndocs/paper/diagnosis.tex:114:\\paragraph{Type A (SC $\\geq$ 60\\%).} All nine Type~A conditions produce no significant positive effects. Even in-context learning with gold FOL examples yields $\\Delta = +0.50$\\,pp (n.s.). Qwen2.5-14B on ProofWriter shows significant degradation ($\\Delta = -2.50$\\,pp, $p = 0.011$).\ndocs/paper/limitations_content.tex:5:[Omitted long matching line]\ndocs/paper/abstract.tex:8:However, a cross-architecture proof-of-concept---DeBERTa-large NLI combined with SC---achieves $+4.41$\\,pp ($w{=}3$; McNemar $p = 0.039$ at $w{=}1$) through per-label complementarity, demonstrating that the oracle gap is practically recoverable when verification signal comes from outside the reasoning model's distribution.\ndocs/paper/solutions.tex:4:The analyses in \\S\\ref{sec:confirmation-bias}--\\S\\ref{sec:remediation} identify two structural causes of SICA's failure: constraints are coupled to their source answer (confirmation bias), and all traces share the same model distribution (independence bottleneck). We investigate two complementary approaches: decoupling constraints from answers within the same model (\\S\\ref{sec:decoupling}), and injecting an architecturally independent verification signal (\\S\\ref{sec:cross-arch}).\ndocs/paper/solutions.tex:15:\\subsection{Cross-Architecture NLI Verification}\ndocs/paper/solutions.tex:16:\\label{sec:cross-arch}\ndocs/paper/solutions.tex:21:We test this with DeBERTa-large \\citep{he2021deberta} (${\\sim}$350M parameters, encoder-only), fine-tuned on MultiNLI \\citep{williams2018mnli}. For each problem, DeBERTa classifies the (premise, conclusion) pair into \\textsc{entailment}, \\textsc{contradiction}, or \\textsc{neutral}. In combo mode, the NLI verdict is integrated with SC's $K$ votes via a weight parameter $w$: each NLI-supporting vote counts $w$ times. We evaluate on Mistral-7B FOLIO ($n = 204$).\ndocs/paper/solutions.tex:24:[Omitted long matching line]\ndocs/paper/solutions.tex:27:[Omitted long matching line]\ndocs/paper/solutions.tex:29:\\paragraph{Why cross-architecture verification works.}\ndocs/paper/solutions.tex:30:The ${\\sim}$350M encoder-only model and the 7B decoder-only LLM share no architecture, training data, or inference mechanism. DeBERTa classifies textual entailment rather than generating chain-of-thought, so it does not exhibit the symbolic confirmation bias identified in \\S\\ref{sec:confirmation-bias}. The two systems err on different problem subsets, satisfying the independence condition that same-model sampling cannot provide.\ndocs/paper/introduction.tex:29:A cross-architecture proof-of-concept demonstrates that this gap is recoverable: DeBERTa-large NLI combined with SC achieves $+4.41$\\,pp ($w{=}3$; McNemar $p = 0.039$ at $w{=}1$) through per-label complementarity (\\S\\ref{sec:cross-arch}).\ndocs/paper/introduction.tex:33:\\item \\textbf{Independence-Accuracy Trade-off and Cross-Architecture Escape.} Fleiss' $\\kappa$ across four aggregation methods and three model families reveals a same-model Pareto frontier ($\\kappa \\geq 0.40$). Twenty-five+ remediation strategies fail; a cross-architecture NLI verifier (DeBERTa-large, $+4.41$\\,pp; McNemar $p = 0.039$ at $w{=}1$) demonstrates the frontier is escapable (\\S\\ref{sec:remediation}, \\S\\ref{sec:cross-arch}).\ndocs/paper/references.bib:321:%%% Cross-Architecture Verification %%%\ndocs/paper/references.bib:323:@inproceedings{he2021deberta,\ndocs/paper/references.bib:324:  title={{DeBERTa}: Decoding-enhanced {BERT} with Disentangled Attention},\ndocs/paper/main.aux:483:\\@writefile{lot}{\\contentsline {table}{\\numberline {1}{\\ignorespaces SICA vs.\\ SC across all conditions sorted by SC accuracy. $\\Delta $ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\\dagger $\\,$n < 100$ (suggestive only). \\textbf  {Bold $\\Delta $}: $p < 0.05$ (McNemar). {*}\\,$p < 0.05$;\\enspace  {**}\\,$p < 0.01$;\\enspace  {***}\\,$p < 0.001$. Failure modes detailed in Appendix~\\ref {app:failure-modes}.}}{5}{table.caption.16}\\protected@file@percent }\ndocs/paper/main.aux:484:\\newlabel{tab:main_results}{{1}{5}{SICA vs.\\ SC across all conditions sorted by SC accuracy. $\\Delta $ = SICA $-$ SC (pp). $^b$In-context learning with gold FOL examples. $\\dagger $\\,$n < 100$ (suggestive only). \\textbf {Bold $\\Delta $}: $p < 0.05$ (McNemar). {*}\\,$p < 0.05$;\\enspace {**}\\,$p < 0.01$;\\enspace {***}\\,$p < 0.001$. Failure modes detailed in Appendix~\\ref {app:failure-modes}}{table.caption.16}{}}\ndocs/paper/main.aux:604:\\citation{he2021deberta}\ndocs/paper/main.aux:704:\\@writefile{toc}{\\contentsline {subsection}{\\numberline {6.2}Cross-Architecture NLI Verification}{7}{subsection.6.2}\\protected@file@percent }\ndocs/paper/main.aux:705:\\newlabel{sec:cross-arch}{{6.2}{7}{Cross-Architecture NLI Verification}{subsection.6.2}{}}\ndocs/paper/main.aux:706:\\newlabel{sec:cross-arch@cref}{{[subsection][2][6]6.2}{[1][7][]7}{}{}{}}\ndocs/paper/main.aux:753:\\@writefile{toc}{\\contentsline {paragraph}{Why cross-architecture verification works.}{8}{section*.32}\\protected@file@percent }\ndocs/paper/main.aux:833:\\bibcite{he2021deberta}{{13}{2021}{{He et~al.}}{{He, Liu, Gao, and Chen}}}",
    "numLines": 33
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me also check for the "backward verification" experiment that appears in the registry (exp-045-backward-verification) but not in the tables.

Actually, I have enough information now. Let me compile the final report.

The paper claims "More than twenty-five remediation strategies" (introduction.tex line 25) and "Twenty-five+ remediation strategies" (introduction.tex line 33).

Let me now figure out how to get from 23 (table entries) to 25+:

The tables explicitly list strategies 1-23. Additional strategies that could push the count to 25+:


- ICL with gold FOL appears in Table 1 as "Qwen2.5-14B FOLIO (ICL)" with Δ=+0.50, but isn't numbered in the remediation tables
- Backward verification shows up in the registry (exp-045-backward-verification) but not in any table
- Cross-model extraction could be counted as two separate directions (weak→strong and strong→weak)

This gets me to 25 with the two unlisted strategies, or 26 if I split cross-model extraction. So the "25+" claim is defensible, though there's a gap between what's explicitly enumerated in the tables and what's actually claimed.

The registry contains 76 negative experiments total, but many are replications—like exp-081 through exp-085 which repeat debate, contrastive, and ICG approaches across different datasets and seeds. These 76 experiments cover the 23 core strategies plus numerous replication runs.

Looking back at Table 7 more carefully: the footnote states "Methods 1--12 are reported in Table 5 and Table 6," and Table 7 lists methods 13-23, which is 11 entries. The table caption says "22+ distinct approaches"—and 9 + 3 + 11 = 23, so "22+" is technically accurate (23 exceeds 22). The introduction's "25+" claim is slightly inflated compared to the 23 actually enumerated across the tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "b32deb03-1dfa-4ea0-892d-5aca86f02fea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MaCcPea7kbhz3RLwVjKUh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5954,
      "cache_read_input_tokens": 61452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5954
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

Here's the complete analysis.

---

## Strategy Count Verification

### Paper Claims
- Introduction (line 25): "More than twenty-five remediation strategies"
- Introduction (line 33): "Twenty-five+ remediation strategies fail"
- Analysis §5.5 (line 77): "more than twenty remediation strategies"
- Appendix Table 7 caption: "22+ distinct approaches"

### Explicitly Enumerated in Tables: **23 individual configurations**

**Table 5 (tab:remediation) — 9 prompt-level strategies:**

| # | Strategy | Target |
|---|----------|--------|
| 1 | Contrastive prompting | Prompt |
| 2 | Cross-model extraction (2 directions) | Architecture |
| 3 | Qwen3-14B extractor | Capability |
| 4 | Z3 feedback | Solver |
| 5 | Consistency filtering | Noise |
| 6 | Cross-trace UNSAT | Independence |
| 7 | T=1.0 | Diversity |
| 8 | Multi-temperature | Diversity |
| 9 | Discriminative filtering | Filtering |

**Table 6 (tab:method_interventions) — 3 method-level strategies:**

| # | Strategy | Target |
|---|----------|--------|
| 10 | ICG (Independent Constraint Generation) | Trace coupling |
| 11 | Contrastive scoring | Scoring bias |
| 12 | Debate | Role diversity |

**Table 7 (tab:additional_interventions) — 11 additional strategies:**

| # | Strategy | Target |
|---|----------|--------|
| 13 | PROVE (code verification) | Formal proof |
| 14 | CEGIS (iterative) | Consistency |
| 15 | DeepConf (logprob) | Confidence |
| 16 | Cross-model SICA | Independence |
| 17 | Problem perturbation | Trace diversity |
| 18 | MIN-UNSAT | Constraint selection |
| 19 | κ-aware SC | Weighted voting |
| 20 | Z3 trace filter | Quality |
| 21 | Bootstrapped gold | Self-improvement |
| 22 | Selective abstention | Confidence |
| 23 | ASCII perturbation | Format diversity |

### Unlisted strategies that close the gap to "25+":
- **ICL with gold FOL** — appears in Table 1 (main results) as a separate condition (Δ=+0.50, n.s.) but not numbered in remediation tables
- **Backward verification** — exp-045 in registry, not in any table
- **Cross-model extraction** counted as 2 directions (weak→strong, strong→weak) in Table 5 footnote

With these: 23 + 2 unlisted + 1 split = **26**, making the "25+" claim defensible.

### Distinct Strategy Families: **15 families**

| Family | Configs | Members |
|--------|---------|---------|
| 1. Contrastive/Pro-Con | 2 | #1 contrastive prompting, #11 contrastive scoring |
| 2. Cross-Model | 3 | #2 cross-model extraction (2 dirs), #16 cross-model SICA |
| 3. Stronger Extractor | 1 | #3 Qwen3-14B |
| 4. Solver Feedback/Objectives | 2 | #4 Z3 feedback, #18 MIN-UNSAT |
| 5. Constraint Filtering | 3 | #5 consistency filtering, #9 disc. filtering, #20 Z3 trace filter |
| 6. Cross-Trace Analysis | 1 | #6 cross-trace UNSAT |
| 7. Temperature/Diversity | 2 | #7 T=1.0, #8 multi-temp |
| 8. Independent Generation (ICG) | 1 | #10 |
| 9. Debate | 1 | #12 |
| 10. Code Verification | 1 | #13 PROVE |
| 11. Iterative Refinement | 2 | #14 CEGIS, #21 bootstrapped gold |
| 12. Confidence Filtering | 2 | #15 DeepConf, #22 selective abstention |
| 13. Input Perturbation | 2 | #17 problem perturbation, #23 ASCII perturbation |
| 14. Weighted Voting | 1 | #19 κ-aware SC |
| 15. ICL with Gold FOL | 1 | Table 1 condition (unlisted) |

### Registry Verification
- **76 experiments** with `conclusion=negative` in registry
- **0 experiments** with `conclusion=positive`
- The 76 experiments cover the 23 strategies plus many replication runs across seeds, datasets, and models (e.g., debate alone has exp-076, exp-078, exp-081, exp-084 for different dataset/seed combos)

### Summary
- **Individual configurations explicitly in tables: 23**
- **Including unlisted but documented: ~26** (supports "25+" claim)
- **Distinct strategy families: 15**
- **Registry negative experiments: 76** (replications across seeds/datasets/models)
- The intro's "25+" is defensible but slightly loose — the appendix's "22+" is more conservative and precisely matches the table-enumerated count. For the paper, recommend saying **"23 distinct strategies across 15 families"** or keeping "25+" if counting unlisted variants.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "uuid": "7765115a-8207-4477-856a-cc602e30a6ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MaCcPea7kbhz3RLwVjKUh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5954,
      "cache_read_input_tokens": 61452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5954
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

_source line 59_

Here's the complete analysis.

---

## Strategy Count Verification

### Paper Claims
- Introduction (line 25): "More than twenty-five remediation strategies"
- Introduction (line 33): "Twenty-five+ remediation strategies fail"
- Analysis §5.5 (line 77): "more than twenty remediation strategies"
- Appendix Table 7 caption: "22+ distinct approaches"

### Explicitly Enumerated in Tables: **23 individual configurations**

**Table 5 (tab:remediation) — 9 prompt-level strategies:**

| # | Strategy | Target |
|---|----------|--------|
| 1 | Contrastive prompting | Prompt |
| 2 | Cross-model extraction (2 directions) | Architecture |
| 3 | Qwen3-14B extractor | Capability |
| 4 | Z3 feedback | Solver |
| 5 | Consistency filtering | Noise |
| 6 | Cross-trace UNSAT | Independence |
| 7 | T=1.0 | Diversity |
| 8 | Multi-temperature | Diversity |
| 9 | Discriminative filtering | Filtering |

**Table 6 (tab:method_interventions) — 3 method-level strategies:**

| # | Strategy | Target |
|---|----------|--------|
| 10 | ICG (Independent Constraint Generation) | Trace coupling |
| 11 | Contrastive scoring | Scoring bias |
| 12 | Debate | Role diversity |

**Table 7 (tab:additional_interventions) — 11 additional strategies:**

| # | Strategy | Target |
|---|----------|--------|
| 13 | PROVE (code verification) | Formal proof |
| 14 | CEGIS (iterative) | Consistency |
| 15 | DeepConf (logprob) | Confidence |
| 16 | Cross-model SICA | Independence |
| 17 | Problem perturbation | Trace diversity |
| 18 | MIN-UNSAT | Constraint selection |
| 19 | κ-aware SC | Weighted voting |
| 20 | Z3 trace filter | Quality |
| 21 | Bootstrapped gold | Self-improvement |
| 22 | Selective abstention | Confidence |
| 23 | ASCII perturbation | Format diversity |

### Unlisted strategies that close the gap to "25+":
- **ICL with gold FOL** — appears in Table 1 (main results) as a separate condition (Δ=+0.50, n.s.) but not numbered in remediation tables
- **Backward verification** — exp-045 in registry, not in any table
- **Cross-model extraction** counted as 2 directions (weak→strong, strong→weak) in Table 5 footnote

With these: 23 + 2 unlisted + 1 split = **26**, making the "25+" claim defensible.

### Distinct Strategy Families: **15 families**

| Family | Configs | Members |
|--------|---------|---------|
| 1. Contrastive/Pro-Con | 2 | #1 contrastive prompting, #11 contrastive scoring |
| 2. Cross-Model | 3 | #2 cross-model extraction (2 dirs), #16 cross-model SICA |
| 3. Stronger Extractor | 1 | #3 Qwen3-14B |
| 4. Solver Feedback/Objectives | 2 | #4 Z3 feedback, #18 MIN-UNSAT |
| 5. Constraint Filtering | 3 | #5 consistency filtering, #9 disc. filtering, #20 Z3 trace filter |
| 6. Cross-Trace Analysis | 1 | #6 cross-trace UNSAT |
| 7. Temperature/Diversity | 2 | #7 T=1.0, #8 multi-temp |
| 8. Independent Generation (ICG) | 1 | #10 |
| 9. Debate | 1 | #12 |
| 10. Code Verification | 1 | #13 PROVE |
| 11. Iterative Refinement | 2 | #14 CEGIS, #21 bootstrapped gold |
| 12. Confidence Filtering | 2 | #15 DeepConf, #22 selective abstention |
| 13. Input Perturbation | 2 | #17 problem perturbation, #23 ASCII perturbation |
| 14. Weighted Voting | 1 | #19 κ-aware SC |
| 15. ICL with Gold FOL | 1 | Table 1 condition (unlisted) |

### Registry Verification
- **76 experiments** with `conclusion=negative` in registry
- **0 experiments** with `conclusion=positive`
- The 76 experiments cover the 23 strategies plus many replication runs across seeds, datasets, and models (e.g., debate alone has exp-076, exp-078, exp-081, exp-084 for different dataset/seed combos)

### Summary
- **Individual configurations explicitly in tables: 23**
- **Including unlisted but documented: ~26** (supports "25+" claim)
- **Distinct strategy families: 15**
- **Registry negative experiments: 76** (replications across seeds/datasets/models)
- The intro's "25+" is defensible but slightly loose — the appendix's "22+" is more conservative and precisely matches the table-enumerated count. For the paper, recommend saying **"23 distinct strategies across 15 families"** or keeping "25+" if counting unlisted variants.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 158284,
  "duration_api_ms": 158613,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "119c7eb6-1f15-4acd-a0b9-478377b82918",
  "total_cost_usd": 0.6883490999999999,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 55565,
    "cache_read_input_tokens": 236730,
    "output_tokens": 6860,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 55565,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1933,
        "cache_read_input_tokens": 61452,
        "cache_creation_input_tokens": 5954,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5954
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1189,
      "outputTokens": 2298,
      "cacheReadInputTokens": 84176,
      "cacheCreationInputTokens": 24045,
      "webSearchRequests": 0,
      "costUSD": 0.05115285,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 6860,
      "cacheReadInputTokens": 236730,
      "cacheCreationInputTokens": 55565,
      "webSearchRequests": 0,
      "costUSD": 0.63719625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "79a6aa97-0fb4-490f-a17a-b66895d3687a"
}
```

</details>

---
