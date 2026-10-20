# paper table2 llama fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/workers/worker_paper_table2_llama_fix_20260520T111247.log`
- **Structured JSON:** [`188215d45e8773468abd.json`](../../sessions/18/188215d45e8773468abd.json)

## Before a recorded user message

81 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
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
  "uuid": "d6bc5861-8e99-4eff-9281-7a6b6c176ad1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/memory/"
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
    "resetsAt": 1779283200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0e12b869-15bc-4d81-bd6f-9ac660cb2391",
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685"
}
```

---

### Assistant

_source line 4_

Let me read the file first to locate the table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "823e8a99-5111-4245-937e-e168954e6c62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWMbPLpWKdQH7n26hN8vTW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12363,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12363
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

<details open><summary>🔧 Tool call — Read · `toolu_01WbFL6AwQF4TPTEhLvPFEJx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "d95cb25e-baea-4f57-9261-4ec2fd60d416",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWMbPLpWKdQH7n26hN8vTW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12363,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12363
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

_source line 6 · 2026-05-20T11:12:59.660Z_

<details><summary>↩ Tool result · reported error · `toolu_01WbFL6AwQF4TPTEhLvPFEJx`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "f767f629-ce46-4758-baa4-78de8230949c",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01NLP3S1X7Kn8d2H5prMn6C3`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "d5df5075-4daf-469c-8a08-5a7c002904c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3SVE8BBc9mX1E2tp4Yy67",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 171,
      "cache_read_input_tokens": 24204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 171
      },
      "output_tokens": 55,
      "service_tier": "standard",
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

_source line 8 · 2026-05-20T11:13:01.786Z_

<details><summary>↩ Tool result · reported error · `toolu_01NLP3S1X7Kn8d2H5prMn6C3`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "829fe056-3100-4a15-aead-b912790e448d",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie."
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_015RzrC4MLGrTPhjBkXtkBWb`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "2ae87acd-7644-45b2-8b2c-2bb93f13561e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CTJ59L1wKycSHAXTzj1w5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 24375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 209
      },
      "output_tokens": 55,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Glob · `toolu_0147t9KZ8TyAbv7KW4L2W4W6`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "538447d9-1951-417b-84f9-985b6a96732b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CTJ59L1wKycSHAXTzj1w5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 24375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 209
      },
      "output_tokens": 55,
      "service_tier": "standard",
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

_source line 11 · 2026-05-20T11:13:05.777Z_

<details><summary>↩ Tool result · `toolu_0147t9KZ8TyAbv7KW4L2W4W6`</summary>

```text
artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/abstract_fd4b26.tex
artifacts/_project/paper/abstract_d3264e.tex
artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
artifacts/dream_reports/dream_20260514T094226/best/paper.tex
artifacts/dream_reports/dream_20260514T094226/median/paper.tex
artifacts/dream_reports/dream_20260514T094226/worst/paper.tex
artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
artifacts/_project/paper/section6_relwork_additions.tex
artifacts/_project/paper/discussion_paragraphs.tex
artifacts/dream_reports/dream_20260514T205155/best/paper.tex
artifacts/dream_reports/dream_20260514T205155/median/paper.tex
artifacts/dream_reports/dream_20260514T205155/worst/paper.tex
artifacts/_project/paper/section6_relwork_outline.tex
artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
artifacts/dream_reports/dream_20260516T021434/best/paper.tex
artifacts/dream_reports/dream_20260516T021434/median/paper.tex
artifacts/dream_reports/dream_20260516T021434/worst/paper.tex
artifacts/dream_reports/dream_20260516T173022/best/paper.tex
artifacts/dream_reports/dream_20260516T173022/median/paper.tex
artifacts/_project/paper/paper_tables_draft.tex
artifacts/appendix_sampling_table.tex
artifacts/_project/paper/appendix_prompts.tex
artifacts/_project/paper/section5_docred_draft_9b84f1.tex
artifacts/_project/paper/p3_case_studies.tex
artifacts/_project/paper/p3_case_studies_861a0d.tex
artifacts/p3_case_studies.tex
artifacts/dream_reports/dream_20260518T162745/best/paper.tex
artifacts/dream_reports/dream_20260518T162745/median/paper.tex
artifacts/dream_reports/dream_20260518T162745/worst/paper.tex
artifacts/_project/paper/appendix_sampling_table.tex
artifacts/_project/paper/appendix_full_ft.tex
artifacts/_project/paper/appendix_doc_length.tex
artifacts/_project/paper/appendix_prompt_sensitivity.tex
artifacts/_project/paper/appendix_llama_per_relation.tex
artifacts/_project/paper/appendix_case_studies.tex
artifacts/_project/paper/section5_crossmodel_draft.tex
artifacts/_project/paper/section3_violation_landscape.tex
artifacts/_project/paper/section2_background.tex
artifacts/_project/paper/appendix_scalability.tex
artifacts/_project/paper/checklist.tex
artifacts/_project/paper/section5_docred_draft.tex
artifacts/_project/paper/appendix_related_work.tex
artifacts/_project/paper/case_study_kappa_dr.tex
artifacts/figures/case_study_kappa_dr.tex
artifacts/_project/paper/appendix_kappa_case_study.tex
artifacts/_project/paper/section5_wikievents_draft.tex
artifacts/_project/paper/section4_composition_draft.tex
artifacts/_project/paper/section3_method_draft.tex
artifacts/_project/paper/appendix_tcr.tex
artifacts/_project/paper/section5_runtime.tex
artifacts/_project/paper/section7_conclusion_compressed.tex
artifacts/d066_beam_sweep/beam_sweep_table.tex
artifacts/_project/paper/appendix_reproducibility.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_beam_search.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/section1_introduction_draft.tex
artifacts/_project/paper/section6_related_work.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/appendix_discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "a412b97e-0fb0-4b4a-b6d6-8d3fa9d7c0ae",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/section5_scierc_draft_4796e8.tex",
      "artifacts/_project/paper/abstract_fd4b26.tex",
      "artifacts/_project/paper/abstract_d3264e.tex",
      "artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex",
      "artifacts/dream_reports/dream_20260514T094226/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T094226/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T094226/worst/paper.tex",
      "artifacts/_project/paper/discussion_paragraphs_cf83d1.tex",
      "artifacts/_project/paper/section6_relwork_additions.tex",
      "artifacts/_project/paper/discussion_paragraphs.tex",
      "artifacts/dream_reports/dream_20260514T205155/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T205155/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T205155/worst/paper.tex",
      "artifacts/_project/paper/section6_relwork_outline.tex",
      "artifacts/_project/paper/section7_conclusion_DEPRECATED.tex",
      "artifacts/dream_reports/dream_20260516T021434/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T021434/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T021434/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T173022/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T173022/median/paper.tex",
      "artifacts/_project/paper/paper_tables_draft.tex",
      "artifacts/appendix_sampling_table.tex",
      "artifacts/_project/paper/appendix_prompts.tex",
      "artifacts/_project/paper/section5_docred_draft_9b84f1.tex",
      "artifacts/_project/paper/p3_case_studies.tex",
      "artifacts/_project/paper/p3_case_studies_861a0d.tex",
      "artifacts/p3_case_studies.tex",
      "artifacts/dream_reports/dream_20260518T162745/best/paper.tex",
      "artifacts/dream_reports/dream_20260518T162745/median/paper.tex",
      "artifacts/dream_reports/dream_20260518T162745/worst/paper.tex",
      "artifacts/_project/paper/appendix_sampling_table.tex",
      "artifacts/_project/paper/appendix_full_ft.tex",
      "artifacts/_project/paper/appendix_doc_length.tex",
      "artifacts/_project/paper/appendix_prompt_sensitivity.tex",
      "artifacts/_project/paper/appendix_llama_per_relation.tex",
      "artifacts/_project/paper/appendix_case_studies.tex",
      "artifacts/_project/paper/section5_crossmodel_draft.tex",
      "artifacts/_project/paper/section3_violation_landscape.tex",
      "artifacts/_project/paper/section2_background.tex",
      "artifacts/_project/paper/appendix_scalability.tex",
      "artifacts/_project/paper/checklist.tex",
      "artifacts/_project/paper/section5_docred_draft.tex",
      "artifacts/_project/paper/appendix_related_work.tex",
      "artifacts/_project/paper/case_study_kappa_dr.tex",
      "artifacts/figures/case_study_kappa_dr.tex",
      "artifacts/_project/paper/appendix_kappa_case_study.tex",
      "artifacts/_project/paper/section5_wikievents_draft.tex",
      "artifacts/_project/paper/section4_composition_draft.tex",
      "artifacts/_project/paper/section3_method_draft.tex",
      "artifacts/_project/paper/appendix_tcr.tex",
      "artifacts/_project/paper/section5_runtime.tex",
      "artifacts/_project/paper/section7_conclusion_compressed.tex",
      "artifacts/d066_beam_sweep/beam_sweep_table.tex",
      "artifacts/_project/paper/appendix_reproducibility.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/appendix_beam_search.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/section1_introduction_draft.tex",
      "artifacts/_project/paper/section6_related_work.tex",
      "artifacts/_project/paper/section5_scierc_draft.tex",
      "artifacts/_project/paper/appendix_discussion.tex"
    ],
    "durationMs": 58,
    "numFiles": 61,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T11:13:05.850Z_

<details><summary>↩ Tool result · `toolu_015RzrC4MLGrTPhjBkXtkBWb`</summary>

```text
AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
analyze_cf_fallback.py
analyze_cf_violations.py
artifacts
checkpoints
compiler
data
decisions.lock
decisions.yaml
distill_tmp
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.lock
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper_framing.md
registry.lock
registry.yaml
report.md
run_extraction_docred.py
scripts
study_status.lock
task_context
violation_checker.py
violation_checker_docred.py
writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "c3316e15-febc-494c-beb2-4111cf1e0de2",
  "tool_use_result": {
    "stdout": "AGENTS.md\nROADMAP.lock\nROADMAP.md\n_last_visual_review.json\nanalyze_cf_fallback.py\nanalyze_cf_violations.py\nartifacts\ncheckpoints\ncompiler\ndata\ndecisions.lock\ndecisions.yaml\ndistill_tmp\ndocs\ndream_registry.lock\ndream_registry.yaml\ndream_registry.yaml.bak\nexperiment_plan.lock\nexperiment_plan.yaml\nfigures\nliterature_map.lock\nliterature_map.yaml\nlogs\nmemory.md\nmistakes.lock\nmistakes.yaml\npaper_framing.md\nregistry.lock\nregistry.yaml\nreport.md\nrun_extraction_docred.py\nscripts\nstudy_status.lock\ntask_context\nviolation_checker.py\nviolation_checker_docred.py\nwriting_plan.yaml",
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

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
The paper files are in `artifacts/_project/paper/`. Let me read the relevant file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "d2c94b3f-b1da-4b5a-a499-e1e9db69c060",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaDcbAG981HpAKXjnmf96X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1042,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 24584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
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

_source line 14_

Paper is at `artifacts/_project/paper/`. Let me read the table file and check for old values in other files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "e3285d5f-6fd5-4ef4-921f-57d8ea4dfc70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaDcbAG981HpAKXjnmf96X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1042,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 24584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01KZ3H5kV41M4yNt3BisDLeR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "cca3ce13-695b-4b41-80bf-f758e2cbd25c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaDcbAG981HpAKXjnmf96X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1042,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 24584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
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

_source line 16 · 2026-05-20T11:13:11.029Z_

<details><summary>↩ Tool result · `toolu_01KZ3H5kV41M4yNt3BisDLeR`</summary>

```text
1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71  & 14.36
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation burden).
60	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
61	F1 $\times$100. Bootstrap: 10{,}000 iterations.
62	S1 = single-pass (\S\ref{sec:strategies}), S2 = two-pass (\S\ref{sec:s2}).
63	Grammar-only represents the ceiling of grammar-constrained decoding~\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}
64	\label{tab:scierc-ablation}
65	\end{table}
66	
67	% ──────────────────────────────────────────
68	%  (a) Core result
69	% ──────────────────────────────────────────
70	\paragraph{Zero-shot diagnostic.}
71	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
72	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
73	% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
74	Full S1 reduces DR from 15.37\% to 0.93\% ($\downarrow$94\%) while R-F1 is unchanged (8.23\,$\to$\,8.36, $p{=}0.58$).
75	Per-relation DR drops to $\leq$2.82\%, reaching 0\% on 4/7 relations (Appendix~\ref{app:per-relation-landscape}).
76	Post-hoc filtering achieves slightly higher F1 via precision gains but discards up to 48\% of predictions including true positives (Appendix~\ref{app:posthoc-extended}).
77	CF rises from 0.08\% to 9.90\% (\S\ref{sec:discussion}).
78	
79	% ──────────────────────────────────────────
80	%  (b) Grammar layer
81	% ──────────────────────────────────────────
82	\paragraph{Layer contributions.}
83	% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823
84	Grammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\%, the ceiling of grammar-based decoding~\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\%), so CF originates from the semantic layer.
85	Semantic-only reduces DR by only 24\% and cannot eliminate RV or ET; this is the \emph{enabling dependency}: adding the grammar layer yields a further 92\% reduction (11.65\%\,$\to$\,0.93\%).
86	
87	% ──────────────────────────────────────────
88	%  (d) S1 vs S2
89	% ──────────────────────────────────────────
90	\paragraph{S1 vs.\ S2.}
91	S2 achieves comparable DR (0.97\%) but lower R-F1 (8.03 vs.\ 8.36) with fewer triples (1{,}644 vs.\ 1{,}729) and does not resolve the CF trade-off (8.03\% vs.\ 9.90\%); we adopt S1 as the primary configuration.
92	% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644
93	
94	% ──────────────────────────────────────────
95	%  (e) Composability with Fine-Tuning
96	%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,
97	%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,
98	%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,
99	%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval
100	% ──────────────────────────────────────────
101	\paragraph{Composability with fine-tuning.}
102	\label{sec:composability}
103	Fine-tuning alone reduces DR to 1--2\% but leaves residual violations that vary by schema tightness (Table~\ref{tab:composability}).
104	On SciERC ($\bar{\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\%\,$\to$\,0\%, Llama 1.11\%\,$\to$\,0.09\%, with R-F1 within $\pm$0.1\,pp.
105	On DocRED ($\bar{\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\% to 0.01\% (Qwen, $\downarrow$99\%) and 0.49\% to 0.20\% (Llama, $\downarrow$59\%); R-F1 changes are $-$0.30\,pp and $+$0.51\,pp.
106	The lower Llama-DocRED reduction (59\% vs.\ 92--100\%) traces to higher tightness ($\bar{\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.
107	Across all four model-dataset settings, DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp.
108	CF interference drops from $+$9.82\,pp (zero-shot SciERC) to $+$1.18\,pp (fine-tuned), tracing to \textsc{Generic}$\leftrightarrow$X ambiguity (Appendix~\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\% of DR reduction under fine-tuning (\S\ref{sec:composition}).
109	LoRA + greedy S1 is the recommended fast deployment configuration: DR\,$\leq$\,0.20\%, CF\,$\leq$\,1.2\% at R-F1 40--46, with $+$10\% latency overhead (\S\ref{sec:runtime}).
110	Beam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \S\ref{sec:beam-results}).
111	
112	\begin{table}[t]
113	\centering
114	\small
115	\setlength{\tabcolsep}{3pt}
116	\resizebox{\columnwidth}{!}{%
117	\begin{tabular}{@{}lll rrrr r@{}}
118	\toprule
119	\textbf{Model} & \textbf{Dataset} & \textbf{Mode}
120	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
121	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
122	  & \textbf{$\Delta$DR} \\
123	\midrule
124	\multirow{4}{*}{Qwen3-8B}
125	  & \multirow{2}{*}{SciERC}
126	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
127	  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
128	\cmidrule(l){2-8}
129	  & \multirow{2}{*}{DocRED}
130	    & Unconstr.\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\
131	  & & Full S1    & \textbf{0.01} & 0.27 & 40.56 & 81.43 & $\downarrow$99\% \\
132	\midrule
133	\multirow{4}{*}{\shortstack[l]{Llama\\3.1-8B}}
134	  & \multirow{2}{*}{SciERC}
135	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
136	  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
137	\cmidrule(l){2-8}
138	  & \multirow{2}{*}{DocRED}
139	    & Unconstr.\ &  0.49 & ---  & 43.72 & 83.93 & --- \\
140	  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\downarrow$59\% \\
141	\bottomrule
142	\end{tabular}}%
143	\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
144	DR\,$\leq$\,0.20\% across both datasets with R-F1 within $\pm$0.6\,pp.
145	F1\,$\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.
146	E-F1 includes parse-failure documents (Qwen PF: 7--9\%; Llama PF: 2--3\%); excluding parse failures, E-F1 is stable for both models ($\pm$0.1\,pp).}
147	\label{tab:composability}
148	\end{table}
149	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "c22ab6ad-0e01-48bc-9f34-b418252d4afe",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
      "content": "% Section 5 — SciERC Results (Draft)\n% Data source: Phase 2 SciERC registry experiments\n% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,\n%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2\n% All numbers verified against registry 2026-05-14.\n\n\\subsection{Ablation and Composability with Fine-Tuning}\n\\label{sec:scierc-results}\n\nTable~\\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.\n\n% ──────────────────────────────────────────\n%  Table: SciERC five-way ablation\n% ──────────────────────────────────────────\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 15.37 & ---\n  & 1.39  & 0.40\n  & 0.08  & 15.45\n  & 8.23  & 31.01 \\\\\nGrammar\n  & 14.84 & $\\downarrow$3\\%\n  & \\textbf{0} & \\textbf{0}\n  & 0.08  & 14.92\n  & 8.23  & 30.98 \\\\\nSemantic\n  & 11.65 & $\\downarrow$24\\%\n  & 1.51  & 0.40\n  & 2.71  & 14.36\n  & 8.15  & 31.01 \\\\\nFull (S1)\n  & \\textbf{0.93} & $\\downarrow$\\textbf{94\\%}\n  & \\textbf{0} & \\textbf{0}\n  & 9.90  & \\textbf{10.83}\n  & \\textbf{8.36} & 30.98 \\\\\nFull (S2)\n  & 0.97  & $\\downarrow$94\\%\n  & \\textbf{0} & \\textbf{0}\n  & 8.03  & \\textbf{9.00}\n  & 8.03  & \\textbf{31.90} \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained.\nTot.\\ = DR + CF (total type-violation burden).\nBest per column in \\textbf{bold} (CF excluded; Tot.\\ included).\nF1 $\\times$100. Bootstrap: 10{,}000 iterations.\nS1 = single-pass (\\S\\ref{sec:strategies}), S2 = two-pass (\\S\\ref{sec:s2}).\nGrammar-only represents the ceiling of grammar-constrained decoding~\\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}\n\\label{tab:scierc-ablation}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (a) Core result\n% ──────────────────────────────────────────\n\\paragraph{Zero-shot diagnostic.}\n% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093\n% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836\n% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824\nFull S1 reduces DR from 15.37\\% to 0.93\\% ($\\downarrow$94\\%) while R-F1 is unchanged (8.23\\,$\\to$\\,8.36, $p{=}0.58$).\nPer-relation DR drops to $\\leq$2.82\\%, reaching 0\\% on 4/7 relations (Appendix~\\ref{app:per-relation-landscape}).\nPost-hoc filtering achieves slightly higher F1 via precision gains but discards up to 48\\% of predictions including true positives (Appendix~\\ref{app:posthoc-extended}).\nCF rises from 0.08\\% to 9.90\\% (\\S\\ref{sec:discussion}).\n\n% ──────────────────────────────────────────\n%  (b) Grammar layer\n% ──────────────────────────────────────────\n\\paragraph{Layer contributions.}\n% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823\nGrammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\\%, the ceiling of grammar-based decoding~\\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\\%), so CF originates from the semantic layer.\nSemantic-only reduces DR by only 24\\% and cannot eliminate RV or ET; this is the \\emph{enabling dependency}: adding the grammar layer yields a further 92\\% reduction (11.65\\%\\,$\\to$\\,0.93\\%).\n\n% ──────────────────────────────────────────\n%  (d) S1 vs S2\n% ──────────────────────────────────────────\n\\paragraph{S1 vs.\\ S2.}\nS2 achieves comparable DR (0.97\\%) but lower R-F1 (8.03 vs.\\ 8.36) with fewer triples (1{,}644 vs.\\ 1{,}729) and does not resolve the CF trade-off (8.03\\% vs.\\ 9.90\\%); we adopt S1 as the primary configuration.\n% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644\n\n% ──────────────────────────────────────────\n%  (e) Composability with Fine-Tuning\n%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,\n%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,\n%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,\n%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval\n% ──────────────────────────────────────────\n\\paragraph{Composability with fine-tuning.}\n\\label{sec:composability}\nFine-tuning alone reduces DR to 1--2\\% but leaves residual violations that vary by schema tightness (Table~\\ref{tab:composability}).\nOn SciERC ($\\bar{\\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\\%\\,$\\to$\\,0\\%, Llama 1.11\\%\\,$\\to$\\,0.09\\%, with R-F1 within $\\pm$0.1\\,pp.\nOn DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.20\\% (Llama, $\\downarrow$59\\%); R-F1 changes are $-$0.30\\,pp and $+$0.51\\,pp.\nThe lower Llama-DocRED reduction (59\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.\nAcross all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.\nCF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition}).\nLoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).\nBeam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \\S\\ref{sec:beam-results}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrr r@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$}\n  & \\textbf{$\\Delta$DR} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen3-8B}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\\n  & & Full S1    & \\textbf{0} & 1.18 & 43.77 & 67.05 & $\\downarrow$100\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\\\\n  & & Full S1    & \\textbf{0.01} & 0.27 & 40.56 & 81.43 & $\\downarrow$99\\% \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.11 & 0    & 45.45 & 67.76 & --- \\\\\n  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.49 & ---  & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\\downarrow$59\\% \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nDR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.\nF1\\,$\\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.\nE-F1 includes parse-failure documents (Qwen PF: 7--9\\%; Llama PF: 2--3\\%); excluding parse failures, E-F1 is stable for both models ($\\pm$0.1\\,pp).}\n\\label{tab:composability}\n\\end{table}\n",
      "numLines": 149,
      "startLine": 1,
      "totalLines": 149
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01JFExtmnj9LrE4LZtxSJ8rk`</summary>

```json
{
  "pattern": "0\\.20|0\\.26|44\\.23",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true,
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
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "8c9e6dc5-3b60-4eab-984a-5c39cf7f5246",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaDcbAG981HpAKXjnmf96X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1042,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 24584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
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

_source line 18 · 2026-05-20T11:13:12.426Z_

<details><summary>↩ Tool result · `toolu_01JFExtmnj9LrE4LZtxSJ8rk`</summary>

```text
artifacts/_project/paper/section5_docred_draft_9b84f1.tex:107:% phase2_docred_grammar_only: DR=0.2617
artifacts/_project/paper/section5_docred_draft_9b84f1.tex:146:% phase2_docred_full_s1: DR=0.1019; delta=(13.84-10.19)/13.84=0.264
artifacts/_project/paper/main.tex:81:Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\,$\leq$\,0.20\%, R-F1 within $\pm$0.6\,pp; EE: RoV$\to$0\%, AC$\leq$0.8\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
artifacts/_project/paper/section5_crossmodel_draft.tex:59:Fine-tuning resolves both: DR\,$\leq$\,0.20\%, CF\,$\leq$\,1.18\%, R-F1 $\pm$0.6\,pp (\S\ref{sec:composability}).
artifacts/_project/paper/section5_scierc_draft.tex:105:On DocRED ($\bar{\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\% to 0.01\% (Qwen, $\downarrow$99\%) and 0.49\% to 0.20\% (Llama, $\downarrow$59\%); R-F1 changes are $-$0.30\,pp and $+$0.51\,pp.
artifacts/_project/paper/section5_scierc_draft.tex:107:Across all four model-dataset settings, DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp.
artifacts/_project/paper/section5_scierc_draft.tex:109:LoRA + greedy S1 is the recommended fast deployment configuration: DR\,$\leq$\,0.20\%, CF\,$\leq$\,1.2\% at R-F1 40--46, with $+$10\% latency overhead (\S\ref{sec:runtime}).
artifacts/_project/paper/section5_scierc_draft.tex:110:Beam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \S\ref{sec:beam-results}).
artifacts/_project/paper/section5_scierc_draft.tex:140:  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\downarrow$59\% \\
artifacts/_project/paper/section5_scierc_draft.tex:144:DR\,$\leq$\,0.20\% across both datasets with R-F1 within $\pm$0.6\,pp.
artifacts/_project/paper/appendix_tcr.tex:63:  & Llama   &  0.36 & \textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\
artifacts/_project/paper/appendix_discussion.tex:262:  & & Full S1       & \textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\
artifacts/_project/paper/appendix_discussion.tex:275:Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.20\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
artifacts/_project/paper/appendix_discussion.tex:329:  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\
artifacts/_project/paper/section5_docred_draft.tex:71:Under fine-tuning, residual narrows to 0.01--0.20\% (Table~\ref{tab:composability}).
artifacts/_project/paper/appendix_beam_search.tex:135:Adding beam search ($k{=}4$) eliminates all residual CF violations (1.18\%\,$\to$\,0\%), yielding zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) while preserving extraction quality (E-F1=66.88, R-F1=44.23; changes within $\pm$0.5\,pp).
artifacts/_project/paper/appendix_beam_search.tex:161:  & Greedy con & 0 & 0 & 0 & 0.26 & 84.71 & 44.70 & 2.6 \\ % d065: 4096 context
artifacts/_project/paper/section4_composition_draft.tex:31:$\bar{\kappa}$ provides deployment guidance: schemas with $\bar{\kappa} < 0.5$ achieve near-complete DR elimination under zero-shot S1 (94--99\% reduction); schemas with $\bar{\kappa} > 0.8$ require fine-tuning to narrow the fallback regime (DR\,0.01--0.20\%).
artifacts/_project/paper/section4_composition_draft.tex:40:Fine-tuning narrows the fallback regime: DR drops to $\leq$\,0.20\% and CF to $\leq$\,1.18\%, with R-F1 within $\pm$0.6\,pp; the grammar layer becomes a no-op and the semantic layer alone reduces residual DR by 39--72\% (\S\ref{sec:composability}).
artifacts/_project/paper/section7_conclusion_compressed.tex:4:OntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\,$\leq$\,0.20\%, CF\,$\leq$\,1.2\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "b49c5be0-3cf2-4f63-b43d-2cf5bc4f2072",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/section5_docred_draft_9b84f1.tex:107:% phase2_docred_grammar_only: DR=0.2617\nartifacts/_project/paper/section5_docred_draft_9b84f1.tex:146:% phase2_docred_full_s1: DR=0.1019; delta=(13.84-10.19)/13.84=0.264\nartifacts/_project/paper/main.tex:81:Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\\,$\\leq$\\,0.20\\%, R-F1 within $\\pm$0.6\\,pp; EE: RoV$\\to$0\\%, AC$\\leq$0.8\\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\\%, Llama 0.46\\% on SciERC) traces to schema-level type ambiguity (\\textsc{Generic}$\\leftrightarrow$X) rather than enforcement failure.\nartifacts/_project/paper/section5_crossmodel_draft.tex:59:Fine-tuning resolves both: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.18\\%, R-F1 $\\pm$0.6\\,pp (\\S\\ref{sec:composability}).\nartifacts/_project/paper/section5_scierc_draft.tex:105:On DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.20\\% (Llama, $\\downarrow$59\\%); R-F1 changes are $-$0.30\\,pp and $+$0.51\\,pp.\nartifacts/_project/paper/section5_scierc_draft.tex:107:Across all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.\nartifacts/_project/paper/section5_scierc_draft.tex:109:LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).\nartifacts/_project/paper/section5_scierc_draft.tex:110:Beam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \\S\\ref{sec:beam-results}).\nartifacts/_project/paper/section5_scierc_draft.tex:140:  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\\downarrow$59\\% \\\\\nartifacts/_project/paper/section5_scierc_draft.tex:144:DR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.\nartifacts/_project/paper/appendix_tcr.tex:63:  & Llama   &  0.36 & \\textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\\\\nartifacts/_project/paper/appendix_discussion.tex:262:  & & Full S1       & \\textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\\\\nartifacts/_project/paper/appendix_discussion.tex:275:Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.20\\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.\nartifacts/_project/paper/appendix_discussion.tex:329:  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\\nartifacts/_project/paper/section5_docred_draft.tex:71:Under fine-tuning, residual narrows to 0.01--0.20\\% (Table~\\ref{tab:composability}).\nartifacts/_project/paper/appendix_beam_search.tex:135:Adding beam search ($k{=}4$) eliminates all residual CF violations (1.18\\%\\,$\\to$\\,0\\%), yielding zero violations across all four metrics (ET=0\\%, RV=0\\%, DR=0\\%, CF=0\\%) while preserving extraction quality (E-F1=66.88, R-F1=44.23; changes within $\\pm$0.5\\,pp).\nartifacts/_project/paper/appendix_beam_search.tex:161:  & Greedy con & 0 & 0 & 0 & 0.26 & 84.71 & 44.70 & 2.6 \\\\ % d065: 4096 context\nartifacts/_project/paper/section4_composition_draft.tex:31:$\\bar{\\kappa}$ provides deployment guidance: schemas with $\\bar{\\kappa} < 0.5$ achieve near-complete DR elimination under zero-shot S1 (94--99\\% reduction); schemas with $\\bar{\\kappa} > 0.8$ require fine-tuning to narrow the fallback regime (DR\\,0.01--0.20\\%).\nartifacts/_project/paper/section4_composition_draft.tex:40:Fine-tuning narrows the fallback regime: DR drops to $\\leq$\\,0.20\\% and CF to $\\leq$\\,1.18\\%, with R-F1 within $\\pm$0.6\\,pp; the grammar layer becomes a no-op and the semantic layer alone reduces residual DR by 39--72\\% (\\S\\ref{sec:composability}).\nartifacts/_project/paper/section7_conclusion_compressed.tex:4:OntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\\times$ latency); zero-shot DR drops 76--99\\% for calibrated models.",
    "numLines": 20
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I can see the table at lines 112-148. The Llama DocRED LoRA rows are at lines 139-140:

Line 139: `    & Unconstr.\ &  0.49 & ---  & 43.72 & 83.93 & --- \\`
Line 140: `  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\downarrow$59\% \\`

The 4 corrections needed:
1. **Llama con DR%**: 0.20 → 0.21 (line 140)


2. **Llama con CF%**: 0.26 → 0.21 (line 140)
3. **Llama con R-F1**: 44.23 → 43.78 (line 140)
4. **Llama unc CF%**: "---" → 0.08 (line 139)

So line 139 becomes: `    & Unconstr.\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\`
And line 140 becomes: `  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\downarrow$59\% \\`

Now I need to verify the prose references match these updates. Looking at line 105, the CF% change from 0.49 to 0.21 represents a 57% reduction, and the R-F1 change is now 0.06pp instead of 0.51pp, so I need to recalculate that percentage shift. 0.5714 ≈ 57%. So 59% → 57%? Wait, let me check more carefully.

Actually the user said just to fix the 4 values in the table. Let me check what else needs updating.

Wait, the user said to also check appendix for references to old values. Let me also look at derived values in the prose.

Let me think about what prose references need updating:

**Line 105**: `0.49\% to 0.20\% (Llama, $\downarrow$59\%); R-F1 changes are $-$0.30\,pp and $+$0.51\,pp.`
- 0.20 → 0.21
- 59% → need to recalculate: (0.49 - 0.21)/0.49 = 57.14% ≈ 57%
- R-F1 change: was +0.51pp (44.23 - 43.72), now +0.06pp (43.78 - 43.72). That's a significant change.

The user's instructions are clear—I need to fix prose references too, but only where they cite the Llama DocRED con data. Let me trace through all the places this appears and update them systematically. I need to be careful here—the 44.23 and 46.11 values on line 110 are actually from beam search results on SciERC, not the greedy DocRED results I was tracking, so those shouldn't be changed even though the numbers happen to match. Moving on to check the table caption on line 144, which also has the 0.20% threshold that needs updating to 0.21%, and then I'll need to look at the appendix file for any other instances.

In the appendix table around line 262, there's a Llama DocRED full S1 row where I need to update 0.20 to 0.21, change 0.26 to 0.21, and correct 44.23 to 43.78. Line 275 has another caption with the same 0.20% threshold needing the 0.21% fix. Then on line 329, there's another instance of 44.23 for Llama DocRED R-F1 that needs to become 43.78.

Moving through the other files, I'm finding the same 0.20% to 0.21% threshold corrections needed across section5_docred_draft.tex, section4_composition_draft.tex, main.tex, and section7_conclusion_compressed.tex. There's also a potential issue in appendix_beam_search.tex where an R-F1 value of 44.23 appears, but I need to verify whether that's actually about SciERC rather than DocRED before making changes.

Looking at the context around that beam search result, it's describing how adding beam search eliminates violations across metrics while maintaining extraction quality. The 1.18% to 0% improvement in CF violations matches the SciERC numbers, so that 44.23 is indeed the Qwen SciERC result, not a DocRED value—I should leave it as is. The table row I'm examining shows greedy decoding results with specific metric values.

Now I'm checking the TCR appendix table to see if those 0.20 and 0.21 values correspond to the same Llama DocRED experiments or if they're from a different evaluation entirely. I need to understand what the TCR table is measuring before assuming these are related values. I need to be systematic about this. Let me start by updating the table values first, then work through the prose references to make sure I'm only changing the Llama DocRED data points and not accidentally modifying other numbers that happen to match.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "70db3836-ded8-4486-a2f1-bf3daf20d35d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCLcVFkmYVNPikDAGKcABX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6831,
      "cache_read_input_tokens": 24969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6831
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

_source line 20_

Found the table at lines 139-140. I also see references to these values in multiple files. Let me read the appendix files for context, then make all edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "25504ab3-d98a-4680-82e9-44525cea1af4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCLcVFkmYVNPikDAGKcABX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6831,
      "cache_read_input_tokens": 24969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6831
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01FEqadjHiHGW6gcdaRGGv1R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": 250,
  "limit": 90
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "9c231d98-2b57-4cb7-8f7e-d6edd43c7244",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCLcVFkmYVNPikDAGKcABX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6831,
      "cache_read_input_tokens": 24969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6831
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

_source line 22 · 2026-05-20T11:14:09.291Z_

<details><summary>↩ Tool result · `toolu_01FEqadjHiHGW6gcdaRGGv1R`</summary>

```text
250	\midrule
251	\multirow{8}{*}{DocRED}
252	  & \multirow{4}{*}{Qwen3-8B}
253	    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.09 & 7.11 & 82.15 & 40.86 \\
254	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
255	  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\
256	  & & Full S1       & \textbf{0.01} & 0.00 & 0.00 & 0.27 & 8.52 & 81.43 & 40.56 \\
257	  \cmidrule(l){2-10}
258	  & \multirow{4}{*}{Llama-3.1-8B}
259	    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\
260	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\
261	  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\
262	  & & Full S1       & \textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\
263	\bottomrule
264	\end{tabular}}%
265	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
266	DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
267	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
268	Semantic layer is the sole effective DR defense, providing 39--72\% reduction.
269	F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED full vs.\ unconstrained).}
270	\label{tab:ft-ablation}
271	\end{table}
272	
273	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
274	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$72\%, Llama $-$39\%).
275	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.20\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
276	F1 cost is negligible: the maximum R-F1 decrease across all 16 model$\times$dataset$\times$mode combinations is $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained), attributable to parse failure increase (7.11\%\,$\to$\,8.52\%) rather than constraint-induced extraction degradation.
277	
278	%%% Residual DR Error Analysis (Fine-Tuned) %%%
279	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
280	
281	\paragraph{Residual DR Error Analysis.}
282	\label{app:residual-dr-analysis}
283	
284	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ full S1), only 36 domain/range violations remain.
285	Manual inspection reveals four root causes:
286	
287	\begin{enumerate}[nosep,leftmargin=*]
288	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
289	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
290	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
291	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
292	\end{enumerate}
293	
294	Two dataset-specific patterns emerge.
295	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
296	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
297	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.
298	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
299	
300	%%% Post-Hoc Filtering Comparison (Extended) %%%
301	% exp_ids: posthoc_*_zs, posthoc_*_ft
302	
303	\paragraph{Post-Hoc Filtering: Extended Comparison.}
304	\label{app:posthoc-extended}
305	
306	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
307	
308	\begin{table}[t]
309	\centering
310	\small
311	\setlength{\tabcolsep}{3pt}
312	\resizebox{\columnwidth}{!}{%
313	\begin{tabular}{@{}lll rrr l@{}}
314	\toprule
315	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
316	\midrule
317	\multirow{6}{*}{ZS}
318	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
319	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
320	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
321	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
322	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
323	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
324	\midrule
325	\multirow{4}{*}{FT}
326	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
327	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
328	  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\
329	  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\
330	\bottomrule
331	\end{tabular}}%
332	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
333	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
334	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
335	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
336	F1 $\times$100.}
337	\label{tab:posthoc-extended}
338	\end{table}
339	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "96fe387a-9f48-4132-a7ef-f9a84c113572",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
      "content": "\\midrule\n\\multirow{8}{*}{DocRED}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.09 & 7.11 & 82.15 & 40.86 \\\\\n  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\\\\n  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\\\\n  & & Full S1       & \\textbf{0.01} & 0.00 & 0.00 & 0.27 & 8.52 & 81.43 & 40.56 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\\\\n  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\\\\n  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\\\\n  & & Full S1       & \\textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\\times$ 2 datasets).\nDR/RV/ET/CF: violation rates (\\%); PF: parse failure rate (\\%); F1 $\\times$100.\nGrammar layer is a no-op post-fine-tuning (DR change $<$0.2\\,pp in all 4 settings; RV and ET already 0\\% without constraints).\nSemantic layer is the sole effective DR defense, providing 39--72\\% reduction.\nF1 cost is negligible: max $\\Delta$R-F1 = $-$0.30\\,pp (Qwen DocRED full vs.\\ unconstrained).}\n\\label{tab:ft-ablation}\n\\end{table}\n\nThe grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\\% without constraints, and grammar-only DR change is $<$0.2\\,pp (4/4 settings).\nThe semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\\% across all settings (SciERC: Qwen $-$69\\%, Llama $-$41\\%; DocRED: Qwen $-$72\\%, Llama $-$39\\%).\nAdding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.20\\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.\nF1 cost is negligible: the maximum R-F1 decrease across all 16 model$\\times$dataset$\\times$mode combinations is $-$0.30\\,pp (Qwen DocRED, full vs.\\ unconstrained), attributable to parse failure increase (7.11\\%\\,$\\to$\\,8.52\\%) rather than constraint-induced extraction degradation.\n\n%%% Residual DR Error Analysis (Fine-Tuned) %%%\n% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*\n\n\\paragraph{Residual DR Error Analysis.}\n\\label{app:residual-dr-analysis}\n\nAcross all fine-tuned settings (2 models $\\times$ 2 datasets $\\times$ full S1), only 36 domain/range violations remain.\nManual inspection reveals four root causes:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\emph{Entity type errors} (39\\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \\textsc{LOC} when the gold standard requires \\textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.\n\\item \\emph{Schema coverage gaps} (33\\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.\n\\item \\emph{Incorrect relation selection} (17\\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.\n\\item \\emph{Direction reversal} (11\\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.\n\\end{enumerate}\n\nTwo dataset-specific patterns emerge.\nOutside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.\nOn DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\\%), with entity type errors as the dominant cause (14/33, 42\\%).\nThis asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.\nThe implication is twofold: (i)~the irreducible floor from schema gaps is small ($\\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.\n\n%%% Post-Hoc Filtering Comparison (Extended) %%%\n% exp_ids: posthoc_*_zs, posthoc_*_ft\n\n\\paragraph{Post-Hoc Filtering: Extended Comparison.}\n\\label{app:posthoc-extended}\n\nTable~\\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrr l@{}}\n\\toprule\n\\textbf{Setting} & \\textbf{Model} & \\textbf{Dataset} & \\textbf{Reject\\%} & \\textbf{R-F1$_{\\text{ph}}$} & \\textbf{R-F1$_{\\text{cd}}$} & \\textbf{Winner} \\\\\n\\midrule\n\\multirow{6}{*}{ZS}\n  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\\\\n  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\\\\n  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\\\\n  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\\\\n  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\\\\n  & Mistral & DocRED & \\textbf{73.7} & 3.85  & \\textbf{5.52} & cd \\\\\n\\midrule\n\\multirow{4}{*}{FT}\n  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\\\\n  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\\\\n  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\\\\n  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Post-hoc filtering (ph) vs.\\ constrained decoding (cd).\nIn zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.\nAt reject rate $>$70\\% (Mistral DocRED), post-hoc F1 collapses below constrained.\nUnder fine-tuning, rejection rates drop to 0.6--2.0\\% and the two strategies are equivalent ($\\Delta \\leq 0.55$\\,pp; each wins two groups).\nF1 $\\times$100.}\n\\label{tab:posthoc-extended}\n\\end{table}\n",
      "numLines": 90,
      "startLine": 250,
      "totalLines": 420
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01C2cyBkDMMjUzro6QoNqYhZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex",
  "offset": 55,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "2c7fac73-8084-4697-9e35-431b4acf2035",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCLcVFkmYVNPikDAGKcABX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6831,
      "cache_read_input_tokens": 24969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6831
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

_source line 24 · 2026-05-20T11:14:10.115Z_

<details><summary>↩ Tool result · `toolu_01C2cyBkDMMjUzro6QoNqYhZ`</summary>

```text
55	\midrule
56	\multirow{3}{*}{Zero-shot}
57	  & Qwen    & 13.11 & \textbf{0} & 10.21 & 11.74 & $-$3.44 & 13.52 \\
58	  & Llama   & 23.71 & \textbf{0} &  2.55 & 11.93 & $-$5.21 & 22.78 \\
59	  & 70B     & 11.61 & \textbf{0} &  0    &  4.20 & $-$5.98 & 18.26 \\
60	\midrule
61	\multirow{2}{*}{LoRA}
62	  & Qwen    &  0.42 & \textbf{0} &  0.01 &  0.14 & $-$0.16 & 12.16 \\
63	  & Llama   &  0.36 & \textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\
64	\bottomrule
65	\end{tabular}
66	\caption{TCR on DocRED ($\bar{\kappa}{=}0.842$, 998 docs).
67	Under zero-shot, TCR introduces substantial DR regressions (up to $+$9.38\,pp for Llama) and E-F1 drops (up to $-$5.98\,pp for 70B).
68	Fundamental conflict rates are 12--23\%, an order of magnitude higher than SciERC.
69	Under LoRA, low baseline CF (0.36--0.42\%) limits both TCR impact and DR cost.}
70	\label{tab:tcr-docred}
71	\end{table}
72	
73	\paragraph{Analysis.}
74	TCR effectiveness correlates inversely with schema constraint tightness $\bar{\kappa}$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "55fa640a-ca08-4857-9a7a-4a3577233ac9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex",
      "content": "\\midrule\n\\multirow{3}{*}{Zero-shot}\n  & Qwen    & 13.11 & \\textbf{0} & 10.21 & 11.74 & $-$3.44 & 13.52 \\\\\n  & Llama   & 23.71 & \\textbf{0} &  2.55 & 11.93 & $-$5.21 & 22.78 \\\\\n  & 70B     & 11.61 & \\textbf{0} &  0    &  4.20 & $-$5.98 & 18.26 \\\\\n\\midrule\n\\multirow{2}{*}{LoRA}\n  & Qwen    &  0.42 & \\textbf{0} &  0.01 &  0.14 & $-$0.16 & 12.16 \\\\\n  & Llama   &  0.36 & \\textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{TCR on DocRED ($\\bar{\\kappa}{=}0.842$, 998 docs).\nUnder zero-shot, TCR introduces substantial DR regressions (up to $+$9.38\\,pp for Llama) and E-F1 drops (up to $-$5.98\\,pp for 70B).\nFundamental conflict rates are 12--23\\%, an order of magnitude higher than SciERC.\nUnder LoRA, low baseline CF (0.36--0.42\\%) limits both TCR impact and DR cost.}\n\\label{tab:tcr-docred}\n\\end{table}\n\n\\paragraph{Analysis.}\nTCR effectiveness correlates inversely with schema constraint tightness $\\bar{\\kappa}$.",
      "numLines": 20,
      "startLine": 55,
      "totalLines": 84
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01MUuobKRK9uepAfQzcx4zXG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
  "offset": 65,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "a5ea5833-2e05-4525-8170-1f21efafebf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCLcVFkmYVNPikDAGKcABX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6831,
      "cache_read_input_tokens": 24969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6831
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

_source line 26 · 2026-05-20T11:14:11.056Z_

<details><summary>↩ Tool result · `toolu_01MUuobKRK9uepAfQzcx4zXG`</summary>

```text
65	
66	% exp_ids: phase2_docred_grammar_only, phase2_docred_semantic_only, phase2_docred_full_s1
67	\paragraph{Layer contributions.}
68	Grammar-only eliminates RV and ET but \emph{increases} DR to 26.17\%: OOV triples (29.66\% baseline) become evaluable and expose latent type incompatibilities.\footnote{The grammar-only DR increase reflects constraint-altered generation trajectories in long documents, where vocabulary restriction shifts token probabilities away from natural but type-violating sequences.}
69	Semantic-only reduces DR by 25\% but cannot eliminate RV or ET, the same enabling dependency observed on SciERC.
70	Residual DR (10.21\% vs.\ SciERC's 0.93\%) reflects higher tightness ($\bar{\kappa}{=}0.842$ vs.\ 0.333), which forces frequent fallback; effective semantic coverage is $\sim$90\% (Appendix~\ref{app:fallback-coverage}).
71	Under fine-tuning, residual narrows to 0.01--0.20\% (Table~\ref{tab:composability}).
72	The increase in Llama parse failures under constraints (6.8\%\,$\to$\,9.1\%) reflects an inherent trade-off: constraint masking alters token probability distributions, which can push generation toward suboptimal paths in long documents.
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "fd27545d-65f5-4631-94d7-b1f90e6eba6c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
      "content": "\n% exp_ids: phase2_docred_grammar_only, phase2_docred_semantic_only, phase2_docred_full_s1\n\\paragraph{Layer contributions.}\nGrammar-only eliminates RV and ET but \\emph{increases} DR to 26.17\\%: OOV triples (29.66\\% baseline) become evaluable and expose latent type incompatibilities.\\footnote{The grammar-only DR increase reflects constraint-altered generation trajectories in long documents, where vocabulary restriction shifts token probabilities away from natural but type-violating sequences.}\nSemantic-only reduces DR by 25\\% but cannot eliminate RV or ET, the same enabling dependency observed on SciERC.\nResidual DR (10.21\\% vs.\\ SciERC's 0.93\\%) reflects higher tightness ($\\bar{\\kappa}{=}0.842$ vs.\\ 0.333), which forces frequent fallback; effective semantic coverage is $\\sim$90\\% (Appendix~\\ref{app:fallback-coverage}).\nUnder fine-tuning, residual narrows to 0.01--0.20\\% (Table~\\ref{tab:composability}).\nThe increase in Llama parse failures under constraints (6.8\\%\\,$\\to$\\,9.1\\%) reflects an inherent trade-off: constraint masking alters token probability distributions, which can push generation toward suboptimal paths in long documents.\n",
      "numLines": 9,
      "startLine": 65,
      "totalLines": 73
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01Lyhmffmje6UeTDQrNMcwwM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex",
  "offset": 125,
  "limit": 45
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "1662f8fd-1556-47c7-8ac2-e251fc7d5363",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCLcVFkmYVNPikDAGKcABX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6831,
      "cache_read_input_tokens": 24969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6831
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

_source line 28 · 2026-05-20T11:14:11.768Z_

<details><summary>↩ Tool result · `toolu_01Lyhmffmje6UeTDQrNMcwwM`</summary>

```text
125	\midrule
126	\multirow{2}{*}{8}
127	 & \textsc{unc} & 66.40 & 43.17 & 1.77 & 0    & 4.194 & 1.68$\times$ \\
128	 & \textsc{con} & 66.36 & 43.65 & \textbf{0} & 0    & 5.058 & 2.03$\times$ \\
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	\paragraph{Composability with fine-tuning.}
134	Under greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with full S1 constraints already achieves DR=0\% but retains CF=1.18\% (21 cross-field violations across 551 documents), with E-F1=67.05 and R-F1=43.77.
135	Adding beam search ($k{=}4$) eliminates all residual CF violations (1.18\%\,$\to$\,0\%), yielding zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) while preserving extraction quality (E-F1=66.88, R-F1=44.23; changes within $\pm$0.5\,pp).
136	Llama-3.1-8B (LoRA, SciERC) with full S1 constraints and beam search ($k{=}4$) likewise achieves zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) with R-F1=46.11; the zero-violation result thus generalizes across calibrated model families.
137	% exp_id: q1_llama_ft_beam_scierc
138	The three constraint mechanisms (grammar masking, semantic domain-range filtering, and beam exploration) are thus fully composable: each addresses a distinct violation source without interfering with the others or degrading task performance.
139	
140	Beam search on DocRED (zero-shot, 50 documents) introduces a modest increase in parse failures (3/50, 6\%) compared to greedy (1.1\%), as longer beam-generated sequences occasionally produce malformed JSON in complex documents.
141	With DR=0 in 50 DocRED documents for both calibrated models, the Clopper-Pearson 95\% CI upper bound is 5.8\%; the full-scale LoRA evaluation below (998 documents, CI${\approx}$0.3\%) provides stronger statistical confirmation.
142	
143	Table~\ref{tab:beam-docred-lora} reports LoRA + beam-4 results on the full DocRED dev set (998 documents), extending the fine-tuning composability evaluation from SciERC to the higher-$\bar{\kappa}$ regime.
144	Parse failure rates under LoRA beam-4 range from 1.3\% to 3.5\%, lower than the zero-shot rate.
145	
146	\begin{table}[h]
147	\centering
148	\small
149	\caption{LoRA greedy vs.\ beam search ($k{=}4$) on DocRED (998 dev documents) under full S1 constraints.
150	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field violation rates (\%); PF = parse failure rate (\%); F1 $\times$ 100.}
151	\label{tab:beam-docred-lora}
152	\begin{tabular}{@{}llccccccc@{}}
153	\toprule
154	\textbf{Model} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ & PF \\
155	\midrule
156	\multirow{2}{*}{Qwen3-8B}
157	  & Greedy con & \multicolumn{7}{c}{\textit{pending}} \\
158	  & Beam-4 con & 0 & \textbf{0} & \textbf{0} & 0.01 & 84.00 & 44.46 & 2.9 \\
159	\midrule
160	\multirow{2}{*}{Llama-3.1-8B}
161	  & Greedy con & 0 & 0 & 0 & 0.26 & 84.71 & 44.70 & 2.6 \\ % d065: 4096 context
162	  & Beam-4 con & 0 & 0 & 0 & \textbf{0} & \textbf{85.23} & \textbf{47.17} & \textbf{1.3} \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	Llama-3.1-8B achieves zero violations across all four metrics (ET, RV, DR, CF = 0\%) on DocRED with LoRA + beam-4, extending the zero-violation result from SciERC to the high-$\bar{\kappa}$ regime.
168	Qwen3-8B achieves DR=0\% with near-zero CF (0.01\%); R-F1 is preserved ($\pm$0.06\,pp).
169	Combined with the sampling robustness results (Appendix~\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "b424f067-8815-46ad-ad6c-1be08fad61cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex",
      "content": "\\midrule\n\\multirow{2}{*}{8}\n & \\textsc{unc} & 66.40 & 43.17 & 1.77 & 0    & 4.194 & 1.68$\\times$ \\\\\n & \\textsc{con} & 66.36 & 43.65 & \\textbf{0} & 0    & 5.058 & 2.03$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Composability with fine-tuning.}\nUnder greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with full S1 constraints already achieves DR=0\\% but retains CF=1.18\\% (21 cross-field violations across 551 documents), with E-F1=67.05 and R-F1=43.77.\nAdding beam search ($k{=}4$) eliminates all residual CF violations (1.18\\%\\,$\\to$\\,0\\%), yielding zero violations across all four metrics (ET=0\\%, RV=0\\%, DR=0\\%, CF=0\\%) while preserving extraction quality (E-F1=66.88, R-F1=44.23; changes within $\\pm$0.5\\,pp).\nLlama-3.1-8B (LoRA, SciERC) with full S1 constraints and beam search ($k{=}4$) likewise achieves zero violations across all four metrics (ET=0\\%, RV=0\\%, DR=0\\%, CF=0\\%) with R-F1=46.11; the zero-violation result thus generalizes across calibrated model families.\n% exp_id: q1_llama_ft_beam_scierc\nThe three constraint mechanisms (grammar masking, semantic domain-range filtering, and beam exploration) are thus fully composable: each addresses a distinct violation source without interfering with the others or degrading task performance.\n\nBeam search on DocRED (zero-shot, 50 documents) introduces a modest increase in parse failures (3/50, 6\\%) compared to greedy (1.1\\%), as longer beam-generated sequences occasionally produce malformed JSON in complex documents.\nWith DR=0 in 50 DocRED documents for both calibrated models, the Clopper-Pearson 95\\% CI upper bound is 5.8\\%; the full-scale LoRA evaluation below (998 documents, CI${\\approx}$0.3\\%) provides stronger statistical confirmation.\n\nTable~\\ref{tab:beam-docred-lora} reports LoRA + beam-4 results on the full DocRED dev set (998 documents), extending the fine-tuning composability evaluation from SciERC to the higher-$\\bar{\\kappa}$ regime.\nParse failure rates under LoRA beam-4 range from 1.3\\% to 3.5\\%, lower than the zero-shot rate.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LoRA greedy vs.\\ beam search ($k{=}4$) on DocRED (998 dev documents) under full S1 constraints.\nET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field violation rates (\\%); PF = parse failure rate (\\%); F1 $\\times$ 100.}\n\\label{tab:beam-docred-lora}\n\\begin{tabular}{@{}llccccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Decoding} & ET & RV & DR$\\,\\downarrow$ & CF$\\,\\downarrow$ & E-F1$\\,\\uparrow$ & R-F1$\\,\\uparrow$ & PF \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-8B}\n  & Greedy con & \\multicolumn{7}{c}{\\textit{pending}} \\\\\n  & Beam-4 con & 0 & \\textbf{0} & \\textbf{0} & 0.01 & 84.00 & 44.46 & 2.9 \\\\\n\\midrule\n\\multirow{2}{*}{Llama-3.1-8B}\n  & Greedy con & 0 & 0 & 0 & 0.26 & 84.71 & 44.70 & 2.6 \\\\ % d065: 4096 context\n  & Beam-4 con & 0 & 0 & 0 & \\textbf{0} & \\textbf{85.23} & \\textbf{47.17} & \\textbf{1.3} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLlama-3.1-8B achieves zero violations across all four metrics (ET, RV, DR, CF = 0\\%) on DocRED with LoRA + beam-4, extending the zero-violation result from SciERC to the high-$\\bar{\\kappa}$ regime.\nQwen3-8B achieves DR=0\\% with near-zero CF (0.01\\%); R-F1 is preserved ($\\pm$0.06\\,pp).\nCombined with the sampling robustness results (Appendix~\\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.",
      "numLines": 45,
      "startLine": 125,
      "totalLines": 198
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

````text
Now I have all the context I need. Let me also read the other files that reference these values.

Let me now trace through every reference that needs updating:

### Table edits (section5_scierc_draft.tex)

**Line 139** (Llama DocRED Unconstrained):
```
    & Unconstr.\ &  0.49 & ---  & 43.72 & 83.93 & --- \\
```
→ Change `---` (CF) to `0.08`:


```
    & Unconstr.\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\
```

**Line 140** (Llama DocRED Full S1):
```
  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\downarrow$59\% \\
```
→ Change 0.20→0.21, 0.26→0.21, 44.23→43.78:
```
  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\downarrow$57\% \\
```

I also need to update the percentage from 59% to 57% since the F1 score changed.

Let me verify: (0.49-0.21)/0.49 = 57.14%, so $\downarrow$57\% is correct.

Now for the prose edits in section5_scierc_draft.tex:

**Line 105**: 
`0.49\% to 0.20\% (Llama, $\downarrow$59\%); R-F1 changes are $-$0.30\,pp and $+$0.51\,pp.`
→ `0.49\% to 0.21\% (Llama, $\downarrow$57\%); R-F1 changes are $-$0.30\,pp and $+$0.06\,pp.`

The R-F1 change for Llama DocRED is 43.78 - 43.72 = 0.06pp, so that's correct.

Actually, I need to clarify — the "$-$0.30\,pp and $+$0.51\,pp" refers to both Qwen and Llama DocRED R-F1 changes. Checking: Qwen DocRED is 40.56 - 40.86 = -0.30pp, and Llama DocRED is 43.78 - 43.72 = +0.06pp (not +0.51pp). So the line should read: `$-$0.30\,pp and $+$0.06\,pp`

**Line 106**:
`The lower Llama-DocRED reduction (59\% vs.\ 92--100\%)`
→ `The lower Llama-DocRED reduction (57\% vs.\ 92--100\%)`

**Lines 107 and 109**:
`DR\,$\leq$\,0.20\%` → `DR\,$\leq$\,0.21\%`

**Line 110**:
The R-F1 values 44.23 and 46.11 are for beam search on SciERC, not DocRED, so I'll leave those unchanged.

**Line 144** (caption):
`DR\,$\leq$\,0.20\%` → `DR\,$\leq$\,0.21\%`

Now checking appendix_discussion.tex for the Llama DocRED Unconstrained values...

Updating the CF column from `---` to `0.08` in that row, and I need to verify the column order against the table headers to make sure I'm placing the values correctly. Looking at the corrections needed for the Llama DocRED Full S1 row, I need to update the DR value from 0.20 to 0.21, change the CF value from 0.26 to 0.21, and adjust the R-F1 score from 44.23 to 43.78.

Then I need to find line 275 where it mentions DR ≤ 0.20% and update that threshold to 0.21%, and finally locate the post-hoc filtering table at line 329 to correct the R-F1_cd value from 44.23 to 43.78 while keeping the Reject% at 0.64 and R-F1_ph at 43.92. Now I need to update several other files with the same correction—changing the residual and DR ranges from 0.20% to 0.21% across multiple sections in the LaTeX documents.

However, I'm noticing the TCR-specific values in the appendix are from a different experiment with different metrics, so I should leave those untouched. The beam search result for Qwen SciERC is the one I already updated.

Now looking at the Llama-3.1-8B Greedy configuration in the beam search table—the E-F1 and R-F1 values differ from the main table because this is from a separate d065 experiment with 4096 context, so this is a distinct evaluation that shouldn't be modified.

Let me also recalculate the $\Delta$DR percentage since the Llama con DR% changed from 0.20 to 0.21, which affects the downstream delta calculation. Now I need to locate and update those specific percentages across the three files—section4_composition_draft.tex, main.tex, and section7_conclusion_compressed.tex—to ensure the 59% references become 57% where they correspond to the semantic-only layer reduction.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "5c2009ca-3a80-49da-8fb5-2d19c4c29450",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JLgzh4KducbehnL1G6c1A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8559,
      "cache_read_input_tokens": 31800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8559
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

_source line 30_

Now I have full context. Let me read the remaining files that need edits and start making changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "f53431c1-b4a9-4d9d-85d3-3d74e959f2e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JLgzh4KducbehnL1G6c1A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8559,
      "cache_read_input_tokens": 31800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8559
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01DX2CFaiUXYMeKKtAg49FwU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
  "offset": 25,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "a23eedab-ff72-4fe5-95bd-20a50f04fff3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JLgzh4KducbehnL1G6c1A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8559,
      "cache_read_input_tokens": 31800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8559
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

_source line 32 · 2026-05-20T11:15:16.425Z_

<details><summary>↩ Tool result · `toolu_01DX2CFaiUXYMeKKtAg49FwU`</summary>

```text
25	%
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes schema restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions; fallback frequency and residual DR increase accordingly.
28	This dual-factor pattern (tightness $\times$ baseline violation rate; $n{=}4$ model--dataset pairs, descriptive) aligns with the cross-dataset results: SciERC ($\bar{\kappa}{=}0.333$) achieves 94--99\% DR reduction vs.\ DocRED ($\bar{\kappa}{=}0.842$) at 45--90\%; the full range across three models is 42--99\% (\S\ref{sec:cross-model}; Appendix~\ref{app:dual-factor}).
29	The pattern extends to WikiEvents EE ($\bar{\kappa}{=}0.82$; Appendix~\ref{app:wikievents-kappa}).
30	However, $\kappa$ is necessary but not sufficient for high violation rates: per-relation analysis shows that high-$\kappa$ relations with unambiguous entity types (\textsc{place\_of\_birth}, $\kappa{=}0.92$, DR${=}$0\%) have zero violations, while relations with comparable $\kappa$ but confusable types (\textsc{basin\_country}, $\kappa{=}0.97$, DR${=}$74.6\%) are highly vulnerable (Appendix~\ref{app:kappa-case-study}).
31	$\bar{\kappa}$ provides deployment guidance: schemas with $\bar{\kappa} < 0.5$ achieve near-complete DR elimination under zero-shot S1 (94--99\% reduction); schemas with $\bar{\kappa} > 0.8$ require fine-tuning to narrow the fallback regime (DR\,0.01--0.20\%).
32	$\bar{\kappa}$ also determines post-hoc resolution feasibility: low-$\bar{\kappa}$ schemas ($<$0.5) benefit from TCR with negligible DR regression ($\leq$0.28\,pp), while high-$\bar{\kappa}$ schemas ($>$0.8) suffer harmful DR increases (up to $+$9.38\,pp; Appendix~\ref{app:tcr}).
33	
34	\paragraph{Non-Rectangularity and Sequential Masking.}
35	\label{sec:rectangularity}
36	% Data source: artifacts/rebuttal/w2_rectangularity_report.md
37	Sequential masking is necessary because ontology type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED relations satisfy $\sigma(r) = \operatorname{dom}(r) \times \operatorname{range}(r)$); independent enforcement would admit 33--37\% spurious pairs.
38	
39	\paragraph{Composability with fine-tuning.}
40	Fine-tuning narrows the fallback regime: DR drops to $\leq$\,0.20\% and CF to $\leq$\,1.18\%, with R-F1 within $\pm$0.6\,pp; the grammar layer becomes a no-op and the semantic layer alone reduces residual DR by 39--72\% (\S\ref{sec:composability}).
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "df663c3c-4ceb-4cbb-bcad-5451b53e15cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
      "content": "%\nThe mean tightness $\\bar{\\kappa} = \\frac{1}{|\\mathcal{R}|}\\sum_{r} \\kappa(r)$ characterizes schema restrictiveness.\nTighter constraints eliminate more grammar-valid tokens at type-bearing positions; fallback frequency and residual DR increase accordingly.\nThis dual-factor pattern (tightness $\\times$ baseline violation rate; $n{=}4$ model--dataset pairs, descriptive) aligns with the cross-dataset results: SciERC ($\\bar{\\kappa}{=}0.333$) achieves 94--99\\% DR reduction vs.\\ DocRED ($\\bar{\\kappa}{=}0.842$) at 45--90\\%; the full range across three models is 42--99\\% (\\S\\ref{sec:cross-model}; Appendix~\\ref{app:dual-factor}).\nThe pattern extends to WikiEvents EE ($\\bar{\\kappa}{=}0.82$; Appendix~\\ref{app:wikievents-kappa}).\nHowever, $\\kappa$ is necessary but not sufficient for high violation rates: per-relation analysis shows that high-$\\kappa$ relations with unambiguous entity types (\\textsc{place\\_of\\_birth}, $\\kappa{=}0.92$, DR${=}$0\\%) have zero violations, while relations with comparable $\\kappa$ but confusable types (\\textsc{basin\\_country}, $\\kappa{=}0.97$, DR${=}$74.6\\%) are highly vulnerable (Appendix~\\ref{app:kappa-case-study}).\n$\\bar{\\kappa}$ provides deployment guidance: schemas with $\\bar{\\kappa} < 0.5$ achieve near-complete DR elimination under zero-shot S1 (94--99\\% reduction); schemas with $\\bar{\\kappa} > 0.8$ require fine-tuning to narrow the fallback regime (DR\\,0.01--0.20\\%).\n$\\bar{\\kappa}$ also determines post-hoc resolution feasibility: low-$\\bar{\\kappa}$ schemas ($<$0.5) benefit from TCR with negligible DR regression ($\\leq$0.28\\,pp), while high-$\\bar{\\kappa}$ schemas ($>$0.8) suffer harmful DR increases (up to $+$9.38\\,pp; Appendix~\\ref{app:tcr}).\n\n\\paragraph{Non-Rectangularity and Sequential Masking.}\n\\label{sec:rectangularity}\n% Data source: artifacts/rebuttal/w2_rectangularity_report.md\nSequential masking is necessary because ontology type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED relations satisfy $\\sigma(r) = \\operatorname{dom}(r) \\times \\operatorname{range}(r)$); independent enforcement would admit 33--37\\% spurious pairs.\n\n\\paragraph{Composability with fine-tuning.}\nFine-tuning narrows the fallback regime: DR drops to $\\leq$\\,0.20\\% and CF to $\\leq$\\,1.18\\%, with R-F1 within $\\pm$0.6\\,pp; the grammar layer becomes a no-op and the semantic layer alone reduces residual DR by 39--72\\% (\\S\\ref{sec:composability}).\n",
      "numLines": 17,
      "startLine": 25,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01UR6C3ef8c7Bn1AKmPi8nCN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
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
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "9dca3aca-27a6-48d2-8ad7-f4ca12e3b569",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JLgzh4KducbehnL1G6c1A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8559,
      "cache_read_input_tokens": 31800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8559
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

_source line 34 · 2026-05-20T11:15:17.358Z_

<details><summary>↩ Tool result · `toolu_01UR6C3ef8c7Bn1AKmPi8nCN`</summary>

```text
75	Schema coverage gaps (one-third of residual violations) arise because RE constraints are extracted from training-data type pairs, which may not cover all valid combinations; larger training sets or manual constraint table completion can reduce this gap.
76	
77	\paragraph{Evaluation coverage.}
78	Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
79	Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated only on 8B-class models.
80	Scaling to smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
81	Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\,$\leq$\,0.20\%, R-F1 within $\pm$0.6\,pp; EE: RoV$\to$0\%, AC$\leq$0.8\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
82	WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).
83	All main experiments use greedy decoding; our evaluation of beam search on the full SciERC test set (551 documents) and DocRED (50 zero-shot, 998 fine-tuned documents) across three models confirms compatibility (Appendices~\ref{app:sampling},~\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.
84	
85	\paragraph{Engineering considerations.}
86	Scalability benchmarks up to 200 entity types and 1,000 relations show constant 2--3\% inference overhead and sub-second compilation ($<$0.5\,s; Appendix~\ref{app:scalability}); however, the first-token uniqueness requirement for continuation masking may become a tokenizer-dependent bottleneck beyond this scale.
87	Evaluation covers LoRA and full fine-tuning on 8B-class models; full fine-tuning with an untuned learning rate underperforms LoRA (R-F1 37.89 vs.\ 43.77 on SciERC) but confirms that constraints remain effective across fine-tuning methods (DR 2.74\%\,$\to$\,0\%; Appendix~\ref{app:full-ft}).
88	
89	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "908b56f0-a71e-461c-b06b-a08337c06ee2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
      "content": "Schema coverage gaps (one-third of residual violations) arise because RE constraints are extracted from training-data type pairs, which may not cover all valid combinations; larger training sets or manual constraint table completion can reduce this gap.\n\n\\paragraph{Evaluation coverage.}\nZero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\\% compared to $\\sim$45\\% for fine-tuned systems.\nZero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated only on 8B-class models.\nScaling to smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.\nComposability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\\,$\\leq$\\,0.20\\%, R-F1 within $\\pm$0.6\\,pp; EE: RoV$\\to$0\\%, AC$\\leq$0.8\\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\\%, Llama 0.46\\% on SciERC) traces to schema-level type ambiguity (\\textsc{Generic}$\\leftrightarrow$X) rather than enforcement failure.\nWikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).\nAll main experiments use greedy decoding; our evaluation of beam search on the full SciERC test set (551 documents) and DocRED (50 zero-shot, 998 fine-tuned documents) across three models confirms compatibility (Appendices~\\ref{app:sampling},~\\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.\n\n\\paragraph{Engineering considerations.}\nScalability benchmarks up to 200 entity types and 1,000 relations show constant 2--3\\% inference overhead and sub-second compilation ($<$0.5\\,s; Appendix~\\ref{app:scalability}); however, the first-token uniqueness requirement for continuation masking may become a tokenizer-dependent bottleneck beyond this scale.\nEvaluation covers LoRA and full fine-tuning on 8B-class models; full fine-tuning with an untuned learning rate underperforms LoRA (R-F1 37.89 vs.\\ 43.77 on SciERC) but confirms that constraints remain effective across fine-tuning methods (DR 2.74\\%\\,$\\to$\\,0\\%; Appendix~\\ref{app:full-ft}).\n\n",
      "numLines": 15,
      "startLine": 75,
      "totalLines": 123
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01Ae7n2WzyWC2Gc5jgqmc6PR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex",
  "offset": 1,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "794c11aa-1753-4b7a-a8df-221c82aebbc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JLgzh4KducbehnL1G6c1A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8559,
      "cache_read_input_tokens": 31800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8559
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

_source line 36 · 2026-05-20T11:15:18.016Z_

<details><summary>↩ Tool result · `toolu_01Ae7n2WzyWC2Gc5jgqmc6PR`</summary>

```text
1	% Section 7 — Discussion and Conclusion
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\,$\leq$\,0.20\%, CF\,$\leq$\,1.2\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models.
5	$\bar{\kappa}$ characterizes constraint regimes, with entity type confusability as the critical co-factor (Appendix~\ref{app:kappa-case-study}); the decidability taxonomy and $\bar{\kappa}$ diagnostic yield a principled deployment workflow.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "54406ebc-2f2e-4689-ba7d-662ff9786e7e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex",
      "content": "% Section 7 — Discussion and Conclusion\n% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.\n\nOntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\\times$ latency); zero-shot DR drops 76--99\\% for calibrated models.\n$\\bar{\\kappa}$ characterizes constraint regimes, with entity type confusability as the critical co-factor (Appendix~\\ref{app:kappa-case-study}); the decidability taxonomy and $\\bar{\\kappa}$ diagnostic yield a principled deployment workflow.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context. Let me also check whether R-F1 within ±0.6pp is still valid. The largest R-F1 change across all 4 settings:
- Qwen SciERC: 43.77 - 43.86 = -0.09pp
- Qwen DocRED: 40.56 - 40.86 = -0.30pp
- Llama SciERC: 45.47 - 45.45 = +0.02pp
- Llama DocRED: 43.78 - 43.72 = +0.06pp


The maximum change is -0.30pp, so the ±0.6pp bound still holds—it was originally set as an upper bound when the largest positive change was +0.51pp. I could tighten it to ±0.3pp, but since the user didn't ask for that and the original claim remains valid, I'll keep it as is. Now let me verify the CF interference claim about the drop from +9.82pp in zero-shot SciERC to +1.18pp when fine-tuned.

Looking at the fine-tuned CF values across the table, the maximum is still 1.18pp from Qwen SciERC, so that claim checks out. The LaTeX notation for the 1.2% bound also remains accurate since 1.18% is still the highest CF value across all fine-tuned settings.

Now I'm going through the document systematically to apply all the corrections. I need to recalculate a few derived metrics: the relative decrease for Llama DocRED works out to 57%, and the R-F1 change is just +0.06pp. The 0.21 value does push the DR bound up to 0.21%, so I'll need to update that claim as well. I'm starting with the primary table and prose in the main section, then moving through the other files to catch all the places where these values appear. The remaining "---" entries are all in the ΔDR column for unconstrained rows, which makes sense since there's no delta to compute for the baseline. The caption note about "---: not computed" still applies, so I can proceed with the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "cfa59563-aed5-4025-b0ad-31237c2d36f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKibko2cmLXRRnMcCXnmAL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5423,
      "cache_read_input_tokens": 40359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5423
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

_source line 38_

Now I'll make all the edits. Starting with the primary table in section5_scierc_draft.tex, then prose references, then other files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "15d54a4c-5f7e-461d-9f14-b3833e7ca199",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKibko2cmLXRRnMcCXnmAL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5423,
      "cache_read_input_tokens": 40359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5423
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

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_01R2iFDM4nmHA2u7Hz5ntsRS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "    & Unconstr.\\ &  0.49 & ---  & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\\downarrow$59\\% \\\\",
  "new_string": "    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "1a724e8b-4a57-45e4-9d39-c671ee476f1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKibko2cmLXRRnMcCXnmAL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5423,
      "cache_read_input_tokens": 40359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5423
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

_source line 40 · 2026-05-20T11:15:52.966Z_

<details><summary>↩ Tool result · `toolu_01R2iFDM4nmHA2u7Hz5ntsRS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "1b5f5e63-1599-499e-9de7-13ce92207fa9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "oldString": "    & Unconstr.\\ &  0.49 & ---  & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\\downarrow$59\\% \\\\",
    "newString": "    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\",
    "originalFile": "% Section 5 — SciERC Results (Draft)\n% Data source: Phase 2 SciERC registry experiments\n% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,\n%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2\n% All numbers verified against registry 2026-05-14.\n\n\\subsection{Ablation and Composability with Fine-Tuning}\n\\label{sec:scierc-results}\n\nTable~\\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.\n\n% ──────────────────────────────────────────\n%  Table: SciERC five-way ablation\n% ──────────────────────────────────────────\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 15.37 & ---\n  & 1.39  & 0.40\n  & 0.08  & 15.45\n  & 8.23  & 31.01 \\\\\nGrammar\n  & 14.84 & $\\downarrow$3\\%\n  & \\textbf{0} & \\textbf{0}\n  & 0.08  & 14.92\n  & 8.23  & 30.98 \\\\\nSemantic\n  & 11.65 & $\\downarrow$24\\%\n  & 1.51  & 0.40\n  & 2.71  & 14.36\n  & 8.15  & 31.01 \\\\\nFull (S1)\n  & \\textbf{0.93} & $\\downarrow$\\textbf{94\\%}\n  & \\textbf{0} & \\textbf{0}\n  & 9.90  & \\textbf{10.83}\n  & \\textbf{8.36} & 30.98 \\\\\nFull (S2)\n  & 0.97  & $\\downarrow$94\\%\n  & \\textbf{0} & \\textbf{0}\n  & 8.03  & \\textbf{9.00}\n  & 8.03  & \\textbf{31.90} \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained.\nTot.\\ = DR + CF (total type-violation burden).\nBest per column in \\textbf{bold} (CF excluded; Tot.\\ included).\nF1 $\\times$100. Bootstrap: 10{,}000 iterations.\nS1 = single-pass (\\S\\ref{sec:strategies}), S2 = two-pass (\\S\\ref{sec:s2}).\nGrammar-only represents the ceiling of grammar-constrained decoding~\\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}\n\\label{tab:scierc-ablation}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (a) Core result\n% ──────────────────────────────────────────\n\\paragraph{Zero-shot diagnostic.}\n% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093\n% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836\n% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824\nFull S1 reduces DR from 15.37\\% to 0.93\\% ($\\downarrow$94\\%) while R-F1 is unchanged (8.23\\,$\\to$\\,8.36, $p{=}0.58$).\nPer-relation DR drops to $\\leq$2.82\\%, reaching 0\\% on 4/7 relations (Appendix~\\ref{app:per-relation-landscape}).\nPost-hoc filtering achieves slightly higher F1 via precision gains but discards up to 48\\% of predictions including true positives (Appendix~\\ref{app:posthoc-extended}).\nCF rises from 0.08\\% to 9.90\\% (\\S\\ref{sec:discussion}).\n\n% ──────────────────────────────────────────\n%  (b) Grammar layer\n% ──────────────────────────────────────────\n\\paragraph{Layer contributions.}\n% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823\nGrammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\\%, the ceiling of grammar-based decoding~\\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\\%), so CF originates from the semantic layer.\nSemantic-only reduces DR by only 24\\% and cannot eliminate RV or ET; this is the \\emph{enabling dependency}: adding the grammar layer yields a further 92\\% reduction (11.65\\%\\,$\\to$\\,0.93\\%).\n\n% ──────────────────────────────────────────\n%  (d) S1 vs S2\n% ──────────────────────────────────────────\n\\paragraph{S1 vs.\\ S2.}\nS2 achieves comparable DR (0.97\\%) but lower R-F1 (8.03 vs.\\ 8.36) with fewer triples (1{,}644 vs.\\ 1{,}729) and does not resolve the CF trade-off (8.03\\% vs.\\ 9.90\\%); we adopt S1 as the primary configuration.\n% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644\n\n% ──────────────────────────────────────────\n%  (e) Composability with Fine-Tuning\n%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,\n%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,\n%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,\n%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval\n% ──────────────────────────────────────────\n\\paragraph{Composability with fine-tuning.}\n\\label{sec:composability}\nFine-tuning alone reduces DR to 1--2\\% but leaves residual violations that vary by schema tightness (Table~\\ref{tab:composability}).\nOn SciERC ($\\bar{\\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\\%\\,$\\to$\\,0\\%, Llama 1.11\\%\\,$\\to$\\,0.09\\%, with R-F1 within $\\pm$0.1\\,pp.\nOn DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.20\\% (Llama, $\\downarrow$59\\%); R-F1 changes are $-$0.30\\,pp and $+$0.51\\,pp.\nThe lower Llama-DocRED reduction (59\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.\nAcross all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.\nCF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition}).\nLoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).\nBeam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \\S\\ref{sec:beam-results}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrr r@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$}\n  & \\textbf{$\\Delta$DR} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen3-8B}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\\n  & & Full S1    & \\textbf{0} & 1.18 & 43.77 & 67.05 & $\\downarrow$100\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\\\\n  & & Full S1    & \\textbf{0.01} & 0.27 & 40.56 & 81.43 & $\\downarrow$99\\% \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.11 & 0    & 45.45 & 67.76 & --- \\\\\n  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.49 & ---  & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\\downarrow$59\\% \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nDR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.\nF1\\,$\\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.\nE-F1 includes parse-failure documents (Qwen PF: 7--9\\%; Llama PF: 2--3\\%); excluding parse failures, E-F1 is stable for both models ($\\pm$0.1\\,pp).}\n\\label{tab:composability}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 136,
        "oldLines": 8,
        "newStart": 136,
        "newLines": 8,
        "lines": [
          "   & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\",
          " \\cmidrule(l){2-8}",
          "   & \\multirow{2}{*}{DocRED}",
          "-    & Unconstr.\\ &  0.49 & ---  & 43.72 & 83.93 & --- \\\\",
          "-  & & Full S1    &  0.20 & 0.26 & 44.23 & 83.94 & $\\downarrow$59\\% \\\\",
          "+    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\",
          "+  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\",
          " \\bottomrule",
          " \\end{tabular}}%",
          " \\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs)."
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

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_01NNTkimr7RoVcbZfUS1bjpP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "0.49\\% to 0.20\\% (Llama, $\\downarrow$59\\%); R-F1 changes are $-$0.30\\,pp and $+$0.51\\,pp.",
  "new_string": "0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "e84dbec8-4f06-484d-8097-d330cf08b3cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKibko2cmLXRRnMcCXnmAL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5423,
      "cache_read_input_tokens": 40359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5423
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

_source line 42 · 2026-05-20T11:15:55.328Z_

<details><summary>↩ Tool result · `toolu_01NNTkimr7RoVcbZfUS1bjpP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "81dfdfc4-587a-4f36-9a44-c3603cd41db9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "oldString": "0.49\\% to 0.20\\% (Llama, $\\downarrow$59\\%); R-F1 changes are $-$0.30\\,pp and $+$0.51\\,pp.",
    "newString": "0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp.",
    "originalFile": "% Section 5 — SciERC Results (Draft)\n% Data source: Phase 2 SciERC registry experiments\n% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,\n%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2\n% All numbers verified against registry 2026-05-14.\n\n\\subsection{Ablation and Composability with Fine-Tuning}\n\\label{sec:scierc-results}\n\nTable~\\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.\n\n% ──────────────────────────────────────────\n%  Table: SciERC five-way ablation\n% ──────────────────────────────────────────\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 15.37 & ---\n  & 1.39  & 0.40\n  & 0.08  & 15.45\n  & 8.23  & 31.01 \\\\\nGrammar\n  & 14.84 & $\\downarrow$3\\%\n  & \\textbf{0} & \\textbf{0}\n  & 0.08  & 14.92\n  & 8.23  & 30.98 \\\\\nSemantic\n  & 11.65 & $\\downarrow$24\\%\n  & 1.51  & 0.40\n  & 2.71  & 14.36\n  & 8.15  & 31.01 \\\\\nFull (S1)\n  & \\textbf{0.93} & $\\downarrow$\\textbf{94\\%}\n  & \\textbf{0} & \\textbf{0}\n  & 9.90  & \\textbf{10.83}\n  & \\textbf{8.36} & 30.98 \\\\\nFull (S2)\n  & 0.97  & $\\downarrow$94\\%\n  & \\textbf{0} & \\textbf{0}\n  & 8.03  & \\textbf{9.00}\n  & 8.03  & \\textbf{31.90} \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained.\nTot.\\ = DR + CF (total type-violation burden).\nBest per column in \\textbf{bold} (CF excluded; Tot.\\ included).\nF1 $\\times$100. Bootstrap: 10{,}000 iterations.\nS1 = single-pass (\\S\\ref{sec:strategies}), S2 = two-pass (\\S\\ref{sec:s2}).\nGrammar-only represents the ceiling of grammar-constrained decoding~\\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}\n\\label{tab:scierc-ablation}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (a) Core result\n% ──────────────────────────────────────────\n\\paragraph{Zero-shot diagnostic.}\n% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093\n% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836\n% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824\nFull S1 reduces DR from 15.37\\% to 0.93\\% ($\\downarrow$94\\%) while R-F1 is unchanged (8.23\\,$\\to$\\,8.36, $p{=}0.58$).\nPer-relation DR drops to $\\leq$2.82\\%, reaching 0\\% on 4/7 relations (Appendix~\\ref{app:per-relation-landscape}).\nPost-hoc filtering achieves slightly higher F1 via precision gains but discards up to 48\\% of predictions including true positives (Appendix~\\ref{app:posthoc-extended}).\nCF rises from 0.08\\% to 9.90\\% (\\S\\ref{sec:discussion}).\n\n% ──────────────────────────────────────────\n%  (b) Grammar layer\n% ──────────────────────────────────────────\n\\paragraph{Layer contributions.}\n% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823\nGrammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\\%, the ceiling of grammar-based decoding~\\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\\%), so CF originates from the semantic layer.\nSemantic-only reduces DR by only 24\\% and cannot eliminate RV or ET; this is the \\emph{enabling dependency}: adding the grammar layer yields a further 92\\% reduction (11.65\\%\\,$\\to$\\,0.93\\%).\n\n% ──────────────────────────────────────────\n%  (d) S1 vs S2\n% ──────────────────────────────────────────\n\\paragraph{S1 vs.\\ S2.}\nS2 achieves comparable DR (0.97\\%) but lower R-F1 (8.03 vs.\\ 8.36) with fewer triples (1{,}644 vs.\\ 1{,}729) and does not resolve the CF trade-off (8.03\\% vs.\\ 9.90\\%); we adopt S1 as the primary configuration.\n% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644\n\n% ──────────────────────────────────────────\n%  (e) Composability with Fine-Tuning\n%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,\n%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,\n%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,\n%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval\n% ──────────────────────────────────────────\n\\paragraph{Composability with fine-tuning.}\n\\label{sec:composability}\nFine-tuning alone reduces DR to 1--2\\% but leaves residual violations that vary by schema tightness (Table~\\ref{tab:composability}).\nOn SciERC ($\\bar{\\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\\%\\,$\\to$\\,0\\%, Llama 1.11\\%\\,$\\to$\\,0.09\\%, with R-F1 within $\\pm$0.1\\,pp.\nOn DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.20\\% (Llama, $\\downarrow$59\\%); R-F1 changes are $-$0.30\\,pp and $+$0.51\\,pp.\nThe lower Llama-DocRED reduction (59\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.\nAcross all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.\nCF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition}).\nLoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).\nBeam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \\S\\ref{sec:beam-results}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrr r@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$}\n  & \\textbf{$\\Delta$DR} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen3-8B}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\\n  & & Full S1    & \\textbf{0} & 1.18 & 43.77 & 67.05 & $\\downarrow$100\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\\\\n  & & Full S1    & \\textbf{0.01} & 0.27 & 40.56 & 81.43 & $\\downarrow$99\\% \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.11 & 0    & 45.45 & 67.76 & --- \\\\\n  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nDR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.\nF1\\,$\\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.\nE-F1 includes parse-failure documents (Qwen PF: 7--9\\%; Llama PF: 2--3\\%); excluding parse failures, E-F1 is stable for both models ($\\pm$0.1\\,pp).}\n\\label{tab:composability}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 102,
        "oldLines": 7,
        "newStart": 102,
        "newLines": 7,
        "lines": [
          " \\label{sec:composability}",
          " Fine-tuning alone reduces DR to 1--2\\% but leaves residual violations that vary by schema tightness (Table~\\ref{tab:composability}).",
          " On SciERC ($\\bar{\\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\\%\\,$\\to$\\,0\\%, Llama 1.11\\%\\,$\\to$\\,0.09\\%, with R-F1 within $\\pm$0.1\\,pp.",
          "-On DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.20\\% (Llama, $\\downarrow$59\\%); R-F1 changes are $-$0.30\\,pp and $+$0.51\\,pp.",
          "+On DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp.",
          " The lower Llama-DocRED reduction (59\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.",
          " Across all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.",
          " CF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition})."
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

_source line 43_

<details open><summary>🔧 Tool call — Edit · `toolu_01QhePNYerHQPjRQHCd5sh24`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "The lower Llama-DocRED reduction (59\\% vs.\\ 92--100\\%)",
  "new_string": "The lower Llama-DocRED reduction (57\\% vs.\\ 92--100\\%)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "9cd12a77-a150-49f1-8e8f-aeb94fbe19c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKibko2cmLXRRnMcCXnmAL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5423,
      "cache_read_input_tokens": 40359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5423
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

_source line 44 · 2026-05-20T11:15:57.040Z_

<details><summary>↩ Tool result · `toolu_01QhePNYerHQPjRQHCd5sh24`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "4abbfc2f-9534-4a15-8a29-281f9f470876",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "oldString": "The lower Llama-DocRED reduction (59\\% vs.\\ 92--100\\%)",
    "newString": "The lower Llama-DocRED reduction (57\\% vs.\\ 92--100\\%)",
    "originalFile": "% Section 5 — SciERC Results (Draft)\n% Data source: Phase 2 SciERC registry experiments\n% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,\n%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2\n% All numbers verified against registry 2026-05-14.\n\n\\subsection{Ablation and Composability with Fine-Tuning}\n\\label{sec:scierc-results}\n\nTable~\\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.\n\n% ──────────────────────────────────────────\n%  Table: SciERC five-way ablation\n% ──────────────────────────────────────────\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 15.37 & ---\n  & 1.39  & 0.40\n  & 0.08  & 15.45\n  & 8.23  & 31.01 \\\\\nGrammar\n  & 14.84 & $\\downarrow$3\\%\n  & \\textbf{0} & \\textbf{0}\n  & 0.08  & 14.92\n  & 8.23  & 30.98 \\\\\nSemantic\n  & 11.65 & $\\downarrow$24\\%\n  & 1.51  & 0.40\n  & 2.71  & 14.36\n  & 8.15  & 31.01 \\\\\nFull (S1)\n  & \\textbf{0.93} & $\\downarrow$\\textbf{94\\%}\n  & \\textbf{0} & \\textbf{0}\n  & 9.90  & \\textbf{10.83}\n  & \\textbf{8.36} & 30.98 \\\\\nFull (S2)\n  & 0.97  & $\\downarrow$94\\%\n  & \\textbf{0} & \\textbf{0}\n  & 8.03  & \\textbf{9.00}\n  & 8.03  & \\textbf{31.90} \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained.\nTot.\\ = DR + CF (total type-violation burden).\nBest per column in \\textbf{bold} (CF excluded; Tot.\\ included).\nF1 $\\times$100. Bootstrap: 10{,}000 iterations.\nS1 = single-pass (\\S\\ref{sec:strategies}), S2 = two-pass (\\S\\ref{sec:s2}).\nGrammar-only represents the ceiling of grammar-constrained decoding~\\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}\n\\label{tab:scierc-ablation}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (a) Core result\n% ──────────────────────────────────────────\n\\paragraph{Zero-shot diagnostic.}\n% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093\n% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836\n% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824\nFull S1 reduces DR from 15.37\\% to 0.93\\% ($\\downarrow$94\\%) while R-F1 is unchanged (8.23\\,$\\to$\\,8.36, $p{=}0.58$).\nPer-relation DR drops to $\\leq$2.82\\%, reaching 0\\% on 4/7 relations (Appendix~\\ref{app:per-relation-landscape}).\nPost-hoc filtering achieves slightly higher F1 via precision gains but discards up to 48\\% of predictions including true positives (Appendix~\\ref{app:posthoc-extended}).\nCF rises from 0.08\\% to 9.90\\% (\\S\\ref{sec:discussion}).\n\n% ──────────────────────────────────────────\n%  (b) Grammar layer\n% ──────────────────────────────────────────\n\\paragraph{Layer contributions.}\n% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823\nGrammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\\%, the ceiling of grammar-based decoding~\\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\\%), so CF originates from the semantic layer.\nSemantic-only reduces DR by only 24\\% and cannot eliminate RV or ET; this is the \\emph{enabling dependency}: adding the grammar layer yields a further 92\\% reduction (11.65\\%\\,$\\to$\\,0.93\\%).\n\n% ──────────────────────────────────────────\n%  (d) S1 vs S2\n% ──────────────────────────────────────────\n\\paragraph{S1 vs.\\ S2.}\nS2 achieves comparable DR (0.97\\%) but lower R-F1 (8.03 vs.\\ 8.36) with fewer triples (1{,}644 vs.\\ 1{,}729) and does not resolve the CF trade-off (8.03\\% vs.\\ 9.90\\%); we adopt S1 as the primary configuration.\n% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644\n\n% ──────────────────────────────────────────\n%  (e) Composability with Fine-Tuning\n%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,\n%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,\n%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,\n%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval\n% ──────────────────────────────────────────\n\\paragraph{Composability with fine-tuning.}\n\\label{sec:composability}\nFine-tuning alone reduces DR to 1--2\\% but leaves residual violations that vary by schema tightness (Table~\\ref{tab:composability}).\nOn SciERC ($\\bar{\\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\\%\\,$\\to$\\,0\\%, Llama 1.11\\%\\,$\\to$\\,0.09\\%, with R-F1 within $\\pm$0.1\\,pp.\nOn DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp.\nThe lower Llama-DocRED reduction (59\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.\nAcross all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.\nCF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition}).\nLoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).\nBeam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \\S\\ref{sec:beam-results}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrr r@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$}\n  & \\textbf{$\\Delta$DR} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen3-8B}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\\n  & & Full S1    & \\textbf{0} & 1.18 & 43.77 & 67.05 & $\\downarrow$100\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\\\\n  & & Full S1    & \\textbf{0.01} & 0.27 & 40.56 & 81.43 & $\\downarrow$99\\% \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.11 & 0    & 45.45 & 67.76 & --- \\\\\n  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nDR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.\nF1\\,$\\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.\nE-F1 includes parse-failure documents (Qwen PF: 7--9\\%; Llama PF: 2--3\\%); excluding parse failures, E-F1 is stable for both models ($\\pm$0.1\\,pp).}\n\\label{tab:composability}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 103,
        "oldLines": 7,
        "newStart": 103,
        "newLines": 7,
        "lines": [
          " Fine-tuning alone reduces DR to 1--2\\% but leaves residual violations that vary by schema tightness (Table~\\ref{tab:composability}).",
          " On SciERC ($\\bar{\\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\\%\\,$\\to$\\,0\\%, Llama 1.11\\%\\,$\\to$\\,0.09\\%, with R-F1 within $\\pm$0.1\\,pp.",
          " On DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp.",
          "-The lower Llama-DocRED reduction (59\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.",
          "+The lower Llama-DocRED reduction (57\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.",
          " Across all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.",
          " CF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition}).",
          " LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime})."
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

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_01MpjpKBCDvF5kteLAuUimgP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "Across all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.",
  "new_string": "Across all four model-dataset settings, DR\\,$\\leq$\\,0.21\\% with R-F1 within $\\pm$0.6\\,pp."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "08254f13-e67b-477d-9bba-1e108b18b96b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JTRqvmox9VyRMwUgzSCn7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2058,
      "cache_read_input_tokens": 45782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2058
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

_source line 46 · 2026-05-20T11:16:01.777Z_

<details><summary>↩ Tool result · `toolu_01MpjpKBCDvF5kteLAuUimgP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "294fc385-8932-4d2a-8324-2e67bec543e3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "oldString": "Across all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.",
    "newString": "Across all four model-dataset settings, DR\\,$\\leq$\\,0.21\\% with R-F1 within $\\pm$0.6\\,pp.",
    "originalFile": "% Section 5 — SciERC Results (Draft)\n% Data source: Phase 2 SciERC registry experiments\n% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,\n%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2\n% All numbers verified against registry 2026-05-14.\n\n\\subsection{Ablation and Composability with Fine-Tuning}\n\\label{sec:scierc-results}\n\nTable~\\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.\n\n% ──────────────────────────────────────────\n%  Table: SciERC five-way ablation\n% ──────────────────────────────────────────\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 15.37 & ---\n  & 1.39  & 0.40\n  & 0.08  & 15.45\n  & 8.23  & 31.01 \\\\\nGrammar\n  & 14.84 & $\\downarrow$3\\%\n  & \\textbf{0} & \\textbf{0}\n  & 0.08  & 14.92\n  & 8.23  & 30.98 \\\\\nSemantic\n  & 11.65 & $\\downarrow$24\\%\n  & 1.51  & 0.40\n  & 2.71  & 14.36\n  & 8.15  & 31.01 \\\\\nFull (S1)\n  & \\textbf{0.93} & $\\downarrow$\\textbf{94\\%}\n  & \\textbf{0} & \\textbf{0}\n  & 9.90  & \\textbf{10.83}\n  & \\textbf{8.36} & 30.98 \\\\\nFull (S2)\n  & 0.97  & $\\downarrow$94\\%\n  & \\textbf{0} & \\textbf{0}\n  & 8.03  & \\textbf{9.00}\n  & 8.03  & \\textbf{31.90} \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained.\nTot.\\ = DR + CF (total type-violation burden).\nBest per column in \\textbf{bold} (CF excluded; Tot.\\ included).\nF1 $\\times$100. Bootstrap: 10{,}000 iterations.\nS1 = single-pass (\\S\\ref{sec:strategies}), S2 = two-pass (\\S\\ref{sec:s2}).\nGrammar-only represents the ceiling of grammar-constrained decoding~\\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}\n\\label{tab:scierc-ablation}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (a) Core result\n% ──────────────────────────────────────────\n\\paragraph{Zero-shot diagnostic.}\n% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093\n% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836\n% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824\nFull S1 reduces DR from 15.37\\% to 0.93\\% ($\\downarrow$94\\%) while R-F1 is unchanged (8.23\\,$\\to$\\,8.36, $p{=}0.58$).\nPer-relation DR drops to $\\leq$2.82\\%, reaching 0\\% on 4/7 relations (Appendix~\\ref{app:per-relation-landscape}).\nPost-hoc filtering achieves slightly higher F1 via precision gains but discards up to 48\\% of predictions including true positives (Appendix~\\ref{app:posthoc-extended}).\nCF rises from 0.08\\% to 9.90\\% (\\S\\ref{sec:discussion}).\n\n% ──────────────────────────────────────────\n%  (b) Grammar layer\n% ──────────────────────────────────────────\n\\paragraph{Layer contributions.}\n% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823\nGrammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\\%, the ceiling of grammar-based decoding~\\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\\%), so CF originates from the semantic layer.\nSemantic-only reduces DR by only 24\\% and cannot eliminate RV or ET; this is the \\emph{enabling dependency}: adding the grammar layer yields a further 92\\% reduction (11.65\\%\\,$\\to$\\,0.93\\%).\n\n% ──────────────────────────────────────────\n%  (d) S1 vs S2\n% ──────────────────────────────────────────\n\\paragraph{S1 vs.\\ S2.}\nS2 achieves comparable DR (0.97\\%) but lower R-F1 (8.03 vs.\\ 8.36) with fewer triples (1{,}644 vs.\\ 1{,}729) and does not resolve the CF trade-off (8.03\\% vs.\\ 9.90\\%); we adopt S1 as the primary configuration.\n% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644\n\n% ──────────────────────────────────────────\n%  (e) Composability with Fine-Tuning\n%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,\n%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,\n%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,\n%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval\n% ──────────────────────────────────────────\n\\paragraph{Composability with fine-tuning.}\n\\label{sec:composability}\nFine-tuning alone reduces DR to 1--2\\% but leaves residual violations that vary by schema tightness (Table~\\ref{tab:composability}).\nOn SciERC ($\\bar{\\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\\%\\,$\\to$\\,0\\%, Llama 1.11\\%\\,$\\to$\\,0.09\\%, with R-F1 within $\\pm$0.1\\,pp.\nOn DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp.\nThe lower Llama-DocRED reduction (57\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.\nAcross all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.\nCF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition}).\nLoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).\nBeam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \\S\\ref{sec:beam-results}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrr r@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$}\n  & \\textbf{$\\Delta$DR} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen3-8B}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\\n  & & Full S1    & \\textbf{0} & 1.18 & 43.77 & 67.05 & $\\downarrow$100\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\\\\n  & & Full S1    & \\textbf{0.01} & 0.27 & 40.56 & 81.43 & $\\downarrow$99\\% \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.11 & 0    & 45.45 & 67.76 & --- \\\\\n  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nDR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.\nF1\\,$\\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.\nE-F1 includes parse-failure documents (Qwen PF: 7--9\\%; Llama PF: 2--3\\%); excluding parse failures, E-F1 is stable for both models ($\\pm$0.1\\,pp).}\n\\label{tab:composability}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 104,
        "oldLines": 7,
        "newStart": 104,
        "newLines": 7,
        "lines": [
          " On SciERC ($\\bar{\\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\\%\\,$\\to$\\,0\\%, Llama 1.11\\%\\,$\\to$\\,0.09\\%, with R-F1 within $\\pm$0.1\\,pp.",
          " On DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp.",
          " The lower Llama-DocRED reduction (57\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.",
          "-Across all four model-dataset settings, DR\\,$\\leq$\\,0.20\\% with R-F1 within $\\pm$0.6\\,pp.",
          "+Across all four model-dataset settings, DR\\,$\\leq$\\,0.21\\% with R-F1 within $\\pm$0.6\\,pp.",
          " CF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition}).",
          " LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).",
          " Beam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \\S\\ref{sec:beam-results})."
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

_source line 47_

<details open><summary>🔧 Tool call — Edit · `toolu_01R5TCvf1nBASveZYA39nLjg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).",
  "new_string": "LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.21\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "73756c90-2e23-4aef-9fd1-be67dba0b4c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JTRqvmox9VyRMwUgzSCn7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2058,
      "cache_read_input_tokens": 45782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2058
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

_source line 48 · 2026-05-20T11:16:05.597Z_

<details><summary>↩ Tool result · `toolu_01R5TCvf1nBASveZYA39nLjg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "5007ed33-435d-4845-b3ba-f392f40afa8f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "oldString": "LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).",
    "newString": "LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.21\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).",
    "originalFile": "% Section 5 — SciERC Results (Draft)\n% Data source: Phase 2 SciERC registry experiments\n% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,\n%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2\n% All numbers verified against registry 2026-05-14.\n\n\\subsection{Ablation and Composability with Fine-Tuning}\n\\label{sec:scierc-results}\n\nTable~\\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.\n\n% ──────────────────────────────────────────\n%  Table: SciERC five-way ablation\n% ──────────────────────────────────────────\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 15.37 & ---\n  & 1.39  & 0.40\n  & 0.08  & 15.45\n  & 8.23  & 31.01 \\\\\nGrammar\n  & 14.84 & $\\downarrow$3\\%\n  & \\textbf{0} & \\textbf{0}\n  & 0.08  & 14.92\n  & 8.23  & 30.98 \\\\\nSemantic\n  & 11.65 & $\\downarrow$24\\%\n  & 1.51  & 0.40\n  & 2.71  & 14.36\n  & 8.15  & 31.01 \\\\\nFull (S1)\n  & \\textbf{0.93} & $\\downarrow$\\textbf{94\\%}\n  & \\textbf{0} & \\textbf{0}\n  & 9.90  & \\textbf{10.83}\n  & \\textbf{8.36} & 30.98 \\\\\nFull (S2)\n  & 0.97  & $\\downarrow$94\\%\n  & \\textbf{0} & \\textbf{0}\n  & 8.03  & \\textbf{9.00}\n  & 8.03  & \\textbf{31.90} \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained.\nTot.\\ = DR + CF (total type-violation burden).\nBest per column in \\textbf{bold} (CF excluded; Tot.\\ included).\nF1 $\\times$100. Bootstrap: 10{,}000 iterations.\nS1 = single-pass (\\S\\ref{sec:strategies}), S2 = two-pass (\\S\\ref{sec:s2}).\nGrammar-only represents the ceiling of grammar-constrained decoding~\\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}\n\\label{tab:scierc-ablation}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (a) Core result\n% ──────────────────────────────────────────\n\\paragraph{Zero-shot diagnostic.}\n% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093\n% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836\n% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824\nFull S1 reduces DR from 15.37\\% to 0.93\\% ($\\downarrow$94\\%) while R-F1 is unchanged (8.23\\,$\\to$\\,8.36, $p{=}0.58$).\nPer-relation DR drops to $\\leq$2.82\\%, reaching 0\\% on 4/7 relations (Appendix~\\ref{app:per-relation-landscape}).\nPost-hoc filtering achieves slightly higher F1 via precision gains but discards up to 48\\% of predictions including true positives (Appendix~\\ref{app:posthoc-extended}).\nCF rises from 0.08\\% to 9.90\\% (\\S\\ref{sec:discussion}).\n\n% ──────────────────────────────────────────\n%  (b) Grammar layer\n% ──────────────────────────────────────────\n\\paragraph{Layer contributions.}\n% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823\nGrammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\\%, the ceiling of grammar-based decoding~\\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\\%), so CF originates from the semantic layer.\nSemantic-only reduces DR by only 24\\% and cannot eliminate RV or ET; this is the \\emph{enabling dependency}: adding the grammar layer yields a further 92\\% reduction (11.65\\%\\,$\\to$\\,0.93\\%).\n\n% ──────────────────────────────────────────\n%  (d) S1 vs S2\n% ──────────────────────────────────────────\n\\paragraph{S1 vs.\\ S2.}\nS2 achieves comparable DR (0.97\\%) but lower R-F1 (8.03 vs.\\ 8.36) with fewer triples (1{,}644 vs.\\ 1{,}729) and does not resolve the CF trade-off (8.03\\% vs.\\ 9.90\\%); we adopt S1 as the primary configuration.\n% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644\n\n% ──────────────────────────────────────────\n%  (e) Composability with Fine-Tuning\n%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,\n%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,\n%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,\n%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval\n% ──────────────────────────────────────────\n\\paragraph{Composability with fine-tuning.}\n\\label{sec:composability}\nFine-tuning alone reduces DR to 1--2\\% but leaves residual violations that vary by schema tightness (Table~\\ref{tab:composability}).\nOn SciERC ($\\bar{\\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\\%\\,$\\to$\\,0\\%, Llama 1.11\\%\\,$\\to$\\,0.09\\%, with R-F1 within $\\pm$0.1\\,pp.\nOn DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp.\nThe lower Llama-DocRED reduction (57\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.\nAcross all four model-dataset settings, DR\\,$\\leq$\\,0.21\\% with R-F1 within $\\pm$0.6\\,pp.\nCF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition}).\nLoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).\nBeam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \\S\\ref{sec:beam-results}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrr r@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$}\n  & \\textbf{$\\Delta$DR} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen3-8B}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\\n  & & Full S1    & \\textbf{0} & 1.18 & 43.77 & 67.05 & $\\downarrow$100\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\\\\n  & & Full S1    & \\textbf{0.01} & 0.27 & 40.56 & 81.43 & $\\downarrow$99\\% \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.11 & 0    & 45.45 & 67.76 & --- \\\\\n  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nDR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.\nF1\\,$\\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.\nE-F1 includes parse-failure documents (Qwen PF: 7--9\\%; Llama PF: 2--3\\%); excluding parse failures, E-F1 is stable for both models ($\\pm$0.1\\,pp).}\n\\label{tab:composability}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 106,
        "oldLines": 7,
        "newStart": 106,
        "newLines": 7,
        "lines": [
          " The lower Llama-DocRED reduction (57\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.",
          " Across all four model-dataset settings, DR\\,$\\leq$\\,0.21\\% with R-F1 within $\\pm$0.6\\,pp.",
          " CF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition}).",
          "-LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).",
          "+LoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.21\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).",
          " Beam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \\S\\ref{sec:beam-results}).",
          " ",
          " \\begin{table}[t]"
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

_source line 49_

<details open><summary>🔧 Tool call — Edit · `toolu_018KAPr9aaLmbfjszL39H94j`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "DR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.",
  "new_string": "DR\\,$\\leq$\\,0.21\\% across both datasets with R-F1 within $\\pm$0.6\\,pp."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "93f91186-bbf2-4aef-903a-9cfd7a8a98c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JTRqvmox9VyRMwUgzSCn7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2058,
      "cache_read_input_tokens": 45782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2058
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

_source line 50 · 2026-05-20T11:16:06.806Z_

<details><summary>↩ Tool result · `toolu_018KAPr9aaLmbfjszL39H94j`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "4bfbc109-6dc8-4b13-851e-8ff7127d1cc8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "oldString": "DR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.",
    "newString": "DR\\,$\\leq$\\,0.21\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.",
    "originalFile": "% Section 5 — SciERC Results (Draft)\n% Data source: Phase 2 SciERC registry experiments\n% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,\n%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2\n% All numbers verified against registry 2026-05-14.\n\n\\subsection{Ablation and Composability with Fine-Tuning}\n\\label{sec:scierc-results}\n\nTable~\\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.\n\n% ──────────────────────────────────────────\n%  Table: SciERC five-way ablation\n% ──────────────────────────────────────────\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 15.37 & ---\n  & 1.39  & 0.40\n  & 0.08  & 15.45\n  & 8.23  & 31.01 \\\\\nGrammar\n  & 14.84 & $\\downarrow$3\\%\n  & \\textbf{0} & \\textbf{0}\n  & 0.08  & 14.92\n  & 8.23  & 30.98 \\\\\nSemantic\n  & 11.65 & $\\downarrow$24\\%\n  & 1.51  & 0.40\n  & 2.71  & 14.36\n  & 8.15  & 31.01 \\\\\nFull (S1)\n  & \\textbf{0.93} & $\\downarrow$\\textbf{94\\%}\n  & \\textbf{0} & \\textbf{0}\n  & 9.90  & \\textbf{10.83}\n  & \\textbf{8.36} & 30.98 \\\\\nFull (S2)\n  & 0.97  & $\\downarrow$94\\%\n  & \\textbf{0} & \\textbf{0}\n  & 8.03  & \\textbf{9.00}\n  & 8.03  & \\textbf{31.90} \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained.\nTot.\\ = DR + CF (total type-violation burden).\nBest per column in \\textbf{bold} (CF excluded; Tot.\\ included).\nF1 $\\times$100. Bootstrap: 10{,}000 iterations.\nS1 = single-pass (\\S\\ref{sec:strategies}), S2 = two-pass (\\S\\ref{sec:s2}).\nGrammar-only represents the ceiling of grammar-constrained decoding~\\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}\n\\label{tab:scierc-ablation}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (a) Core result\n% ──────────────────────────────────────────\n\\paragraph{Zero-shot diagnostic.}\n% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093\n% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836\n% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824\nFull S1 reduces DR from 15.37\\% to 0.93\\% ($\\downarrow$94\\%) while R-F1 is unchanged (8.23\\,$\\to$\\,8.36, $p{=}0.58$).\nPer-relation DR drops to $\\leq$2.82\\%, reaching 0\\% on 4/7 relations (Appendix~\\ref{app:per-relation-landscape}).\nPost-hoc filtering achieves slightly higher F1 via precision gains but discards up to 48\\% of predictions including true positives (Appendix~\\ref{app:posthoc-extended}).\nCF rises from 0.08\\% to 9.90\\% (\\S\\ref{sec:discussion}).\n\n% ──────────────────────────────────────────\n%  (b) Grammar layer\n% ──────────────────────────────────────────\n\\paragraph{Layer contributions.}\n% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823\nGrammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\\%, the ceiling of grammar-based decoding~\\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\\%), so CF originates from the semantic layer.\nSemantic-only reduces DR by only 24\\% and cannot eliminate RV or ET; this is the \\emph{enabling dependency}: adding the grammar layer yields a further 92\\% reduction (11.65\\%\\,$\\to$\\,0.93\\%).\n\n% ──────────────────────────────────────────\n%  (d) S1 vs S2\n% ──────────────────────────────────────────\n\\paragraph{S1 vs.\\ S2.}\nS2 achieves comparable DR (0.97\\%) but lower R-F1 (8.03 vs.\\ 8.36) with fewer triples (1{,}644 vs.\\ 1{,}729) and does not resolve the CF trade-off (8.03\\% vs.\\ 9.90\\%); we adopt S1 as the primary configuration.\n% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644\n\n% ──────────────────────────────────────────\n%  (e) Composability with Fine-Tuning\n%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,\n%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,\n%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,\n%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval\n% ──────────────────────────────────────────\n\\paragraph{Composability with fine-tuning.}\n\\label{sec:composability}\nFine-tuning alone reduces DR to 1--2\\% but leaves residual violations that vary by schema tightness (Table~\\ref{tab:composability}).\nOn SciERC ($\\bar{\\kappa}{=}0.333$), adding S1 eliminates or near-eliminates DR: Qwen 1.95\\%\\,$\\to$\\,0\\%, Llama 1.11\\%\\,$\\to$\\,0.09\\%, with R-F1 within $\\pm$0.1\\,pp.\nOn DocRED ($\\bar{\\kappa}{=}0.842$, 96 relations), S1 reduces DR from 0.76\\% to 0.01\\% (Qwen, $\\downarrow$99\\%) and 0.49\\% to 0.21\\% (Llama, $\\downarrow$57\\%); R-F1 changes are $-$0.30\\,pp and $+$0.06\\,pp.\nThe lower Llama-DocRED reduction (57\\% vs.\\ 92--100\\%) traces to higher tightness ($\\bar{\\kappa}{=}0.842$), which triggers grammar-first fallback more frequently.\nAcross all four model-dataset settings, DR\\,$\\leq$\\,0.21\\% with R-F1 within $\\pm$0.6\\,pp.\nCF interference drops from $+$9.82\\,pp (zero-shot SciERC) to $+$1.18\\,pp (fine-tuned), tracing to \\textsc{Generic}$\\leftrightarrow$X ambiguity (Appendix~\\ref{app:cf-distribution}); the semantic layer alone accounts for 39--72\\% of DR reduction under fine-tuning (\\S\\ref{sec:composition}).\nLoRA + greedy S1 is the recommended fast deployment configuration: DR\\,$\\leq$\\,0.21\\%, CF\\,$\\leq$\\,1.2\\% at R-F1 40--46, with $+$10\\% latency overhead (\\S\\ref{sec:runtime}).\nBeam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; \\S\\ref{sec:beam-results}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrr r@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$}\n  & \\textbf{$\\Delta$DR} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen3-8B}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\\n  & & Full S1    & \\textbf{0} & 1.18 & 43.77 & 67.05 & $\\downarrow$100\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\\\\n  & & Full S1    & \\textbf{0.01} & 0.27 & 40.56 & 81.43 & $\\downarrow$99\\% \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.11 & 0    & 45.45 & 67.76 & --- \\\\\n  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nDR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.\nF1\\,$\\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.\nE-F1 includes parse-failure documents (Qwen PF: 7--9\\%; Llama PF: 2--3\\%); excluding parse failures, E-F1 is stable for both models ($\\pm$0.1\\,pp).}\n\\label{tab:composability}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 141,
        "oldLines": 7,
        "newStart": 141,
        "newLines": 7,
        "lines": [
          " \\bottomrule",
          " \\end{tabular}}%",
          " \\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).",
          "-DR\\,$\\leq$\\,0.20\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.",
          "+DR\\,$\\leq$\\,0.21\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.",
          " F1\\,$\\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.",
          " E-F1 includes parse-failure documents (Qwen PF: 7--9\\%; Llama PF: 2--3\\%); excluding parse failures, E-F1 is stable for both models ($\\pm$0.1\\,pp).}",
          " \\label{tab:composability}"
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

_source line 51_

Now editing the other files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "05160fe9-c6e3-4b0a-be0a-4694a2ed4561",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJydBNEEAPssnBuBpAY44v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 47840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01BcwSHphFALvuS9L5vX5s76`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\\\",
  "new_string": "    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "458d6547-2de4-44bd-87e8-fb3ed24e7530",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJydBNEEAPssnBuBpAY44v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 47840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 53 · 2026-05-20T11:16:12.303Z_

<details><summary>↩ Tool result · `toolu_01BcwSHphFALvuS9L5vX5s76`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "f24771f1-a2a7-4535-bb95-12fe95ea36cc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "oldString": "    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\\\",
    "newString": "    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\\\",
    "originalFile": "% Appendix B — Extended Discussion\n% Contains discussion paragraphs moved from the main text during compression.\n\n\\section{Extended Discussion}\\label{app:discussion}\n\n%%% CF Dual Mechanism %%%\n% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1\n\n\\paragraph{CF Dual Mechanism.}\nCF violations arise from two distinct mechanisms:\n(1)~\\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.\nThe entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.\n(2)~\\emph{Grammar-first fallback} (\\S\\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.\n\nThese mechanisms have sharply different model profiles.\nQwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\\% of its CF violations to registry override.\nLlama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.\nThis asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\\,=\\,2.57\\% on DocRED vs.\\ Llama's 12.02\\%, despite both using identical constraint configurations.\nThe difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.\n\n%%% Fallback Behavior and Effective Coverage %%%\n% exp_ids: cf_fallback_ablation_scierc (final data)\n\n\\paragraph{Fallback Behavior and Effective Coverage.}\n\\label{app:fallback-coverage}\nThe two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.\n\\emph{Grammar-first fallback} (36.6\\% of type-bearing positions on SciERC) occurs when $S(t) \\cap G(t) = \\emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations. These events account for the residual DR that persists after constraint enforcement.\n\\emph{Registry-consistent fallback} (4.5\\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.\nTogether, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.\n\nWe define \\emph{effective semantic constraint coverage} as $1 - f_{\\text{gf}}$, where $f_{\\text{gf}}$ is the grammar-first fallback rate.\nOn SciERC, Llama-3.1-8B shows $f_{\\text{gf}} = 36.6\\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\\% effective coverage.\nOn DocRED, by contrast, Qwen3-8B shows $f_{\\text{gf}} = 0.08\\%$ (46 of 54{,}859), yielding 99.9\\% coverage.\nThe large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \\textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.\nDocRED types (\\textsc{PER}, \\textsc{ORG}, \\textsc{LOC}, \\textsc{TIME}, \\textsc{NUM}, \\textsc{MISC}) are all single-token, eliminating this inflation.\nThis metric directly quantifies the enabling dependency (\\S\\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.\nQwen3-8B, with zero grammar-first fallbacks, achieves 100\\% effective coverage on SciERC, consistent with its lower residual DR (0.93\\% vs.\\ Llama's 0.08\\%).\n\n%%% CF-DR Trade-off Analysis %%%\n% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)\n\n\\paragraph{CF-DR Trade-off Analysis.}\n\\label{app:cf-dr-tradeoff}\n\nCF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\\% on SciERC, up to 12.02\\% on Llama DocRED).\nWe treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.\nTable~\\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\\sigma(r)$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}l rrrr@{}}\n\\toprule\n\\textbf{Configuration} & \\textbf{DR\\,(\\%)} & \\textbf{CF\\,(\\%)} & \\textbf{DR+CF} & \\textbf{$f_{\\text{gf}}$\\,(\\%)} \\\\\n\\midrule\nFull S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\\\\nCF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\\\\n\\midrule\n$\\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \\texttt{w1\\_cf\\_fallback\\_scierc\\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\\,pp. $f_{\\text{gf}}$: grammar-first fallback rate at type-bearing positions.}\n\\label{tab:cf-dr-tradeoff}\n\\end{table}\n\nThe CF fallback variant nearly eliminates CF (9.90\\%\\,$\\to$\\,0.04\\%, $-$9.86\\,pp) but at the cost of a 15.9$\\times$ increase in DR (0.93\\%\\,$\\to$\\,14.78\\%, $+$13.85\\,pp).\n% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664\nThis is not a net improvement: total violations (DR+CF) rise from 10.83\\% to 14.82\\% ($+$3.99\\,pp), so the change \\emph{re-routes} violations rather than reducing them.\nThe mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.\nThe grammar-first fallback is triggered at 36.64\\% of type-bearing positions; this conflict is structural, not a tunable hyperparameter.\n\nWe interpret this as a fundamental tension in composable constraint systems with \\emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.\nWithin this design, the current full S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\\% DR at the cost of 9.90\\% CF.\nThe direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\\times$ 2 datasets), DR and CF are inversely associated (Spearman $\\rho = -0.77$, $n{=}6$), with no setting showing both high DR and high CF simultaneously (Table~\\ref{tab:cross-model}).\nThe pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\\%), making the trade-off most visible.\nWhile the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.\nThe CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\\% of CF violations on SciERC involve the catch-all \\textsc{Generic} type (Table~\\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.\n\nTwo complementary paths can lower CF without re-routing it to DR.\n(i)~\\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\\% relative to the zero-shot setting (9.90\\%\\,$\\to$\\,1.18\\%; Table~\\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.\n% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118\nThe remaining 1.18\\% still traces to \\textsc{Generic}$\\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.\n(ii)~\\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.\n\n%%% Dual-Factor Quantitative Analysis %%%\n% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,\n%          llama_scierc_full_s1, llama_docred_full_s1\n\n\\paragraph{Dual-Factor Quantitative Analysis.}\n\\label{app:dual-factor}\n\nFigure~\\ref{fig:dual-factor-scatter} plots residual DR against the product $\\bar{\\kappa} \\times \\text{RV}_{\\text{baseline}}$ for model$\\times$dataset configurations.\nFor \\emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \\approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.\nThe strong fit supports the dual-factor pattern from \\S\\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.\nMistral-7B (unconstrained ET${=}$7.58\\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.\nThis motivates a principled exclusion criterion: models with unconstrained ET${>}$5\\% on either dataset fall outside the regime where the tightness$\\times$RV product is the primary DR driver.\nThe two DocRED points (high $\\bar{\\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\\bar{\\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/dual_factor_scatter.pdf}\n\\caption{Residual DR vs.\\ $\\bar{\\kappa} \\times \\text{RV}_{\\text{baseline}}$ across four model$\\times$dataset configurations.\nLinear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification.}\n\\label{fig:dual-factor-scatter}\n\\end{figure}\n\n%%% Dataset-Dependent F1 Impact (moved from §7) %%%\n% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),\n%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)\n\n\\paragraph{Dataset-Dependent F1 Impact.}\nThe divergence in F1 significance between DocRED ($+$0.50\\,pp, $p < 0.001$) and SciERC ($+$0.13\\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.\nDocRED's baseline RV of 29.66\\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.\nSciERC's baseline RV is only 1.39\\% (24 OOV predictions), too few to produce a detectable F1 effect.\nLlama-3.1-8B's lower baseline RV (16.03\\%) yields a smaller but directionally consistent improvement ($+$0.29\\,pp vs.\\ $+$0.50\\,pp); F1 gain magnitude is proportional to baseline OOV rate.\n% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained\n% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)\n\n%%% Paragraph 1: Low F1 Practical Significance %%%\n% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),\n%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)\n\n\\paragraph{Practical Significance of Zero-Shot F1.}\nOur reported relation F1 of approximately 8\\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.\nFor reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\\% relation F1 with full training data~\\citep{zhong2021frustratingly,ye2022packed}.\nConstraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.\nEven after LoRA fine-tuning, residual DR of 1--2\\% persists on tight-constraint relations (Table~\\ref{tab:composability}); constraints remain necessary at deployment-grade quality.\n% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval\nIn our evaluation, F1 serves as a \\emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.\nThe contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\\S\\ref{sec:composability}) validates practical deployment value.\n\n%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%\n% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),\n%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)\n\n\\paragraph{Decoding-Time vs.\\ Post-Hoc Enforcement.}\nPost-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\\ 8.36; DocRED 9.61 vs.\\ 8.23).\n% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23\nHowever, this precision gain comes at substantial cost.\nOn DocRED, post-hoc filtering discards 48.1\\% of all predicted triples, including 127 true positives (11.2\\% of correct predictions); recall drops from 9.46\\% to 8.40\\%.\n% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40\nEntity type violations remain unresolved (ET\\,=\\,2.47\\% vs.\\ OntoCoDec's 0\\%), as filtering targets only domain/range and vocabulary violations.\n% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%\nOntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.\nThe two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.\n\n%%% CF Violation Distribution %%%\n% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),\n%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)\n\n\\paragraph{Cross-Field Violation Distribution.}\n\\label{app:cf-distribution}\n\nTable~\\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC full S1 (245 CF violations, all pairwise; no mention triggered $\\geq$3 types).\nConflicts involving the \\textsc{Generic} type account for 63.3\\% (155/245) of all violations.\n\\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.\n\nThe pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \\textsc{Generic}$\\leftrightarrow$\\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\\%); on DocRED, the analogous catch-all type \\textsc{MISC} drives 76.6\\% of Qwen's CF violations.\nUnder unconstrained decoding, CF rates collapse to $\\leq$1\\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lr r@{}}\n\\toprule\n\\textbf{Conflicting Type Pair} & \\textbf{Count} & \\textbf{\\%} \\\\\n\\midrule\nGeneric $\\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\\\\nGeneric $\\leftrightarrow$ Material & 35 & 14.3 \\\\\nGeneric $\\leftrightarrow$ Metric & 30 & 12.2 \\\\\nMethod $\\leftrightarrow$ Task & 20 & 8.2 \\\\\nMaterial $\\leftrightarrow$ Method & 17 & 6.9 \\\\\nOtherScientificTerm $\\leftrightarrow$ Task & 12 & 4.9 \\\\\n\\midrule\n10 further pairs (each $\\leq$3.3\\%) & 46 & 18.8 \\\\\n\\midrule\n\\textbf{Total} & \\textbf{245} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF violation distribution on SciERC full S1 (Qwen3-8B, 551 documents).\nAll 245 violations are pairwise conflicts.\nConflicts involving \\textsc{Generic} account for 63.3\\%.}\n\\label{tab:cf-distribution}\n\\end{table}\n\n%%% Per-Relation DR Elimination under Fine-Tuning %%%\n% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1\n\n\\paragraph{Per-Relation DR Elimination under Fine-Tuning.}\n\\label{app:lora-per-relation}\n\nTable~\\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.\nFine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \\textsc{Evaluate-for} ($\\kappa{=}0.361$, 13.13\\%), \\textsc{Part-of} ($\\kappa{=}0.417$, 5.77\\%), and \\textsc{Compare} ($\\kappa{=}0.528$, 5.00\\%).\nAdding OntoCoDec constraints eliminates all remaining violations across all relations.\nOne \\textsc{Evaluate-for} triple (99\\,$\\to$\\,98) is redirected to \\textsc{Used-for} (634\\,$\\to$\\,635) by token-level masking: the head entity's registered type falls outside \\textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}l r rr rr@{}}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{LoRA Unconstr.}} & \\multicolumn{2}{c}{\\textbf{LoRA + S1}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(l){5-6}\n\\textbf{Relation} & $\\kappa$ & DR\\,(\\%) & $n$ & DR\\,(\\%) & $n$ \\\\\n\\midrule\nEvaluate-for & 0.361 & 13.13 & 99 & \\textbf{0} & 98 \\\\\nPart-of      & 0.417 & 5.77  & 52 & \\textbf{0} & 52 \\\\\nCompare      & 0.528 & 5.00  & 40 & \\textbf{0} & 40 \\\\\nConjunction  & 0.306 & 1.31  & 153 & \\textbf{0} & 153 \\\\\nFeature-of   & 0.278 & 1.35  & 74 & \\textbf{0} & 74 \\\\\nUsed-for     & 0.028 & 0.16  & 634 & \\textbf{0} & 635 \\\\\nHyponym-of   & 0.417 & 0     & --- & \\textbf{0} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).\n$\\kappa$: constraint tightness; $n$: predicted triple count.\nUsed-for gains one triple from Evaluate-for redirection.}\n\\label{tab:lora-per-relation}\n\\end{table}\n\n%%% Fine-Tuned Four-Way Ablation %%%\n% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*\n\n\\paragraph{Fine-Tuned Four-Way Ablation.}\n\\label{app:ft-ablation}\n\nTable~\\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrrr rr@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Model} & \\textbf{Mode} & \\textbf{DR\\,$\\downarrow$} & \\textbf{RV\\,$\\downarrow$} & \\textbf{ET\\,$\\downarrow$} & \\textbf{CF} & \\textbf{PF} & \\textbf{E-F1\\,$\\uparrow$} & \\textbf{R-F1\\,$\\uparrow$} \\\\\n\\midrule\n\\multirow{8}{*}{SciERC}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\\n  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\\n  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\\\\n  & & Full S1       & \\textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\\\\n  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\\\\n  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\\\\n  & & Full S1       & \\textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\\\\n\\midrule\n\\multirow{8}{*}{DocRED}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.09 & 7.11 & 82.15 & 40.86 \\\\\n  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\\\\n  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\\\\n  & & Full S1       & \\textbf{0.01} & 0.00 & 0.00 & 0.27 & 8.52 & 81.43 & 40.56 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\\\\n  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\\\\n  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\\\\n  & & Full S1       & \\textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\\times$ 2 datasets).\nDR/RV/ET/CF: violation rates (\\%); PF: parse failure rate (\\%); F1 $\\times$100.\nGrammar layer is a no-op post-fine-tuning (DR change $<$0.2\\,pp in all 4 settings; RV and ET already 0\\% without constraints).\nSemantic layer is the sole effective DR defense, providing 39--72\\% reduction.\nF1 cost is negligible: max $\\Delta$R-F1 = $-$0.30\\,pp (Qwen DocRED full vs.\\ unconstrained).}\n\\label{tab:ft-ablation}\n\\end{table}\n\nThe grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\\% without constraints, and grammar-only DR change is $<$0.2\\,pp (4/4 settings).\nThe semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\\% across all settings (SciERC: Qwen $-$69\\%, Llama $-$41\\%; DocRED: Qwen $-$72\\%, Llama $-$39\\%).\nAdding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.20\\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.\nF1 cost is negligible: the maximum R-F1 decrease across all 16 model$\\times$dataset$\\times$mode combinations is $-$0.30\\,pp (Qwen DocRED, full vs.\\ unconstrained), attributable to parse failure increase (7.11\\%\\,$\\to$\\,8.52\\%) rather than constraint-induced extraction degradation.\n\n%%% Residual DR Error Analysis (Fine-Tuned) %%%\n% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*\n\n\\paragraph{Residual DR Error Analysis.}\n\\label{app:residual-dr-analysis}\n\nAcross all fine-tuned settings (2 models $\\times$ 2 datasets $\\times$ full S1), only 36 domain/range violations remain.\nManual inspection reveals four root causes:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\emph{Entity type errors} (39\\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \\textsc{LOC} when the gold standard requires \\textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.\n\\item \\emph{Schema coverage gaps} (33\\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.\n\\item \\emph{Incorrect relation selection} (17\\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.\n\\item \\emph{Direction reversal} (11\\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.\n\\end{enumerate}\n\nTwo dataset-specific patterns emerge.\nOutside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.\nOn DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\\%), with entity type errors as the dominant cause (14/33, 42\\%).\nThis asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.\nThe implication is twofold: (i)~the irreducible floor from schema gaps is small ($\\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.\n\n%%% Post-Hoc Filtering Comparison (Extended) %%%\n% exp_ids: posthoc_*_zs, posthoc_*_ft\n\n\\paragraph{Post-Hoc Filtering: Extended Comparison.}\n\\label{app:posthoc-extended}\n\nTable~\\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrr l@{}}\n\\toprule\n\\textbf{Setting} & \\textbf{Model} & \\textbf{Dataset} & \\textbf{Reject\\%} & \\textbf{R-F1$_{\\text{ph}}$} & \\textbf{R-F1$_{\\text{cd}}$} & \\textbf{Winner} \\\\\n\\midrule\n\\multirow{6}{*}{ZS}\n  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\\\\n  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\\\\n  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\\\\n  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\\\\n  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\\\\n  & Mistral & DocRED & \\textbf{73.7} & 3.85  & \\textbf{5.52} & cd \\\\\n\\midrule\n\\multirow{4}{*}{FT}\n  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\\\\n  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\\\\n  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\\\\n  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Post-hoc filtering (ph) vs.\\ constrained decoding (cd).\nIn zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.\nAt reject rate $>$70\\% (Mistral DocRED), post-hoc F1 collapses below constrained.\nUnder fine-tuning, rejection rates drop to 0.6--2.0\\% and the two strategies are equivalent ($\\Delta \\leq 0.55$\\,pp; each wins two groups).\nF1 $\\times$100.}\n\\label{tab:posthoc-extended}\n\\end{table}\n\nThe crossover point occurs when post-hoc rejection exceeds $\\sim$70\\%: Mistral DocRED rejects 73.7\\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\\,pp).\nOntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.\nUnder fine-tuning, both strategies converge because few violations remain to filter or constrain ($\\Delta \\leq 0.55$\\,pp across all four FT groups, with each strategy winning two).\n\n%%% Zero-Shot Runtime Profiling %%%\n\n\\paragraph{Zero-Shot Runtime Profiling.}\n\\label{app:runtime}\n\nOn SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\\,s/doc and Full S1 constrained decoding averages 4.710\\,s/doc ($+$13.1\\% overhead).\nOn DocRED (same configuration), unconstrained inference averages 19.34\\,s/doc and Full S1 averages 19.81\\,s/doc ($+$2.43\\% overhead).\nThe lower relative overhead on DocRED reflects amortization: the fixed per-token constraint cost is spread over longer generation sequences.\nXGrammar automaton compilation takes 0.044\\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\\,s on SciERC (Table~\\ref{tab:scalability}), amortized to zero over the evaluation set.\n\n% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified\n\\paragraph{Fine-Tuned Latency Profiling.}\n\\label{app:ft-latency}\nUnder LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\\,s/doc and Full S1 constrained decoding averages 2.873\\,s/doc ($+$10.0\\% overhead, $n{=}551$).\nFine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\\,s vs.\\ 4.163\\,s/doc unconstrained); absolute generation time drops by 37\\%.\nThe relative overhead ($+$10.0\\%) is slightly lower than zero-shot ($+$13.1\\%), consistent with shorter sequences requiring fewer constraint checks per document.\n\n%%% Fuzzy Relation Matching %%%\n\n\\paragraph{Relation Matching Protocol.}\n\\label{app:fuzzy-matching}\nRelation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\\ spaces, abbreviations).\nA predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\\% \\emph{and} edit distance $\\leq 2$.\nThis protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\\_of\\_government'' for ``head of government'').\nOn Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\\,pp R-F1; strict R-F1\\,=\\,3.50\\% vs.\\ fuzzy 4.34\\%).\nFor Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).\nAll F1 figures in the main text use fuzzy normalization consistently across all models and conditions.\n\n%%% Per-Relation Violation Landscape %%%\n\n\\paragraph{Per-Relation Violation Landscape.}\n\\label{app:per-relation-landscape}\n\nTable~\\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.\nFigure~\\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Violation rates (\\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}\n\\label{tab:prompt_comparison}\n\\begin{tabular}{ll cccc}\n\\toprule\nDataset & Prompt & DR$\\downarrow$ & RV$\\downarrow$ & ET$\\downarrow$ & CF$\\downarrow$ \\\\\n\\midrule\n\\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\\\\n & Schema-informed & 5.8 & 0.3 & \\textbf{0.0} & --- \\\\\n\\midrule\n\\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\\\\n & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_per_relation_dr.pdf}\n\\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\\kappa(r)$.}\n\\label{fig:per_relation_dr}\n\\end{figure}\n\n%%% WikiEvents Extended %%%\n\n\\paragraph{WikiEvents Dataset Details.}\n\\label{app:wikievents}\nWikiEvents~\\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.\nIt defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\\_type, role)$\\to$allowed\\_entity\\_types constraints.\nThe grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.\n\n\\paragraph{Constraint Tightness in WikiEvents.}\n\\label{app:wikievents-kappa}\n% Data source: artifacts/w1c_wikievents_kappa_results.md\nWikiEvents role-level tightness (Eq.~\\ref{eq:tightness}, with $|\\mathcal{E}|{=}27$) has mean $\\bar{\\kappa}{=}0.82$ and median 0.89; 84\\% of roles have $\\kappa \\geq 0.80$ (4 or fewer valid entity types out of 27).\nThe tightness-violation pattern extends to event extraction: roles with $\\kappa \\geq 0.90$ exhibit the highest AC rate (50\\%), compared to 21\\% for medium-tightness ($0.80 \\leq \\kappa < 0.90$) and 30\\% for loose ($\\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.\nHowever, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\\to$VEH) show 0\\% AC despite $\\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\\to$CRM, Sentence$\\to$SEN) show near-100\\% AC because LLMs default to common types (PER, ORG).\nThe loose group's elevated rate (30\\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\\% AC, $\\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.\n",
    "structuredPatch": [
      {
        "oldStart": 256,
        "oldLines": 7,
        "newStart": 256,
        "newLines": 7,
        "lines": [
          "   & & Full S1       & \\textbf{0.01} & 0.00 & 0.00 & 0.27 & 8.52 & 81.43 & 40.56 \\\\",
          "   \\cmidrule(l){2-10}",
          "   & \\multirow{4}{*}{Llama-3.1-8B}",
          "-    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\\\",
          "+    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\\\",
          "   & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\\\",
          "   & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\\\",
          "   & & Full S1       & \\textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\\\"
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

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_01BFLYjqa2QGwrGekZTJ832T`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "  & & Full S1       & \\textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\\\",
  "new_string": "  & & Full S1       & \\textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "88014904-6541-46db-8b90-64cfd14415a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJydBNEEAPssnBuBpAY44v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 47840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 55 · 2026-05-20T11:16:14.652Z_

<details><summary>↩ Tool result · `toolu_01BFLYjqa2QGwrGekZTJ832T`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "31355a49-59be-4e31-88f0-86d03fee18f8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "oldString": "  & & Full S1       & \\textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\\\",
    "newString": "  & & Full S1       & \\textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\\\",
    "originalFile": "% Appendix B — Extended Discussion\n% Contains discussion paragraphs moved from the main text during compression.\n\n\\section{Extended Discussion}\\label{app:discussion}\n\n%%% CF Dual Mechanism %%%\n% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1\n\n\\paragraph{CF Dual Mechanism.}\nCF violations arise from two distinct mechanisms:\n(1)~\\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.\nThe entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.\n(2)~\\emph{Grammar-first fallback} (\\S\\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.\n\nThese mechanisms have sharply different model profiles.\nQwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\\% of its CF violations to registry override.\nLlama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.\nThis asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\\,=\\,2.57\\% on DocRED vs.\\ Llama's 12.02\\%, despite both using identical constraint configurations.\nThe difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.\n\n%%% Fallback Behavior and Effective Coverage %%%\n% exp_ids: cf_fallback_ablation_scierc (final data)\n\n\\paragraph{Fallback Behavior and Effective Coverage.}\n\\label{app:fallback-coverage}\nThe two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.\n\\emph{Grammar-first fallback} (36.6\\% of type-bearing positions on SciERC) occurs when $S(t) \\cap G(t) = \\emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations. These events account for the residual DR that persists after constraint enforcement.\n\\emph{Registry-consistent fallback} (4.5\\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.\nTogether, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.\n\nWe define \\emph{effective semantic constraint coverage} as $1 - f_{\\text{gf}}$, where $f_{\\text{gf}}$ is the grammar-first fallback rate.\nOn SciERC, Llama-3.1-8B shows $f_{\\text{gf}} = 36.6\\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\\% effective coverage.\nOn DocRED, by contrast, Qwen3-8B shows $f_{\\text{gf}} = 0.08\\%$ (46 of 54{,}859), yielding 99.9\\% coverage.\nThe large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \\textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.\nDocRED types (\\textsc{PER}, \\textsc{ORG}, \\textsc{LOC}, \\textsc{TIME}, \\textsc{NUM}, \\textsc{MISC}) are all single-token, eliminating this inflation.\nThis metric directly quantifies the enabling dependency (\\S\\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.\nQwen3-8B, with zero grammar-first fallbacks, achieves 100\\% effective coverage on SciERC, consistent with its lower residual DR (0.93\\% vs.\\ Llama's 0.08\\%).\n\n%%% CF-DR Trade-off Analysis %%%\n% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)\n\n\\paragraph{CF-DR Trade-off Analysis.}\n\\label{app:cf-dr-tradeoff}\n\nCF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\\% on SciERC, up to 12.02\\% on Llama DocRED).\nWe treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.\nTable~\\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\\sigma(r)$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}l rrrr@{}}\n\\toprule\n\\textbf{Configuration} & \\textbf{DR\\,(\\%)} & \\textbf{CF\\,(\\%)} & \\textbf{DR+CF} & \\textbf{$f_{\\text{gf}}$\\,(\\%)} \\\\\n\\midrule\nFull S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\\\\nCF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\\\\n\\midrule\n$\\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \\texttt{w1\\_cf\\_fallback\\_scierc\\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\\,pp. $f_{\\text{gf}}$: grammar-first fallback rate at type-bearing positions.}\n\\label{tab:cf-dr-tradeoff}\n\\end{table}\n\nThe CF fallback variant nearly eliminates CF (9.90\\%\\,$\\to$\\,0.04\\%, $-$9.86\\,pp) but at the cost of a 15.9$\\times$ increase in DR (0.93\\%\\,$\\to$\\,14.78\\%, $+$13.85\\,pp).\n% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664\nThis is not a net improvement: total violations (DR+CF) rise from 10.83\\% to 14.82\\% ($+$3.99\\,pp), so the change \\emph{re-routes} violations rather than reducing them.\nThe mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.\nThe grammar-first fallback is triggered at 36.64\\% of type-bearing positions; this conflict is structural, not a tunable hyperparameter.\n\nWe interpret this as a fundamental tension in composable constraint systems with \\emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.\nWithin this design, the current full S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\\% DR at the cost of 9.90\\% CF.\nThe direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\\times$ 2 datasets), DR and CF are inversely associated (Spearman $\\rho = -0.77$, $n{=}6$), with no setting showing both high DR and high CF simultaneously (Table~\\ref{tab:cross-model}).\nThe pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\\%), making the trade-off most visible.\nWhile the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.\nThe CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\\% of CF violations on SciERC involve the catch-all \\textsc{Generic} type (Table~\\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.\n\nTwo complementary paths can lower CF without re-routing it to DR.\n(i)~\\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\\% relative to the zero-shot setting (9.90\\%\\,$\\to$\\,1.18\\%; Table~\\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.\n% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118\nThe remaining 1.18\\% still traces to \\textsc{Generic}$\\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.\n(ii)~\\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.\n\n%%% Dual-Factor Quantitative Analysis %%%\n% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,\n%          llama_scierc_full_s1, llama_docred_full_s1\n\n\\paragraph{Dual-Factor Quantitative Analysis.}\n\\label{app:dual-factor}\n\nFigure~\\ref{fig:dual-factor-scatter} plots residual DR against the product $\\bar{\\kappa} \\times \\text{RV}_{\\text{baseline}}$ for model$\\times$dataset configurations.\nFor \\emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \\approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.\nThe strong fit supports the dual-factor pattern from \\S\\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.\nMistral-7B (unconstrained ET${=}$7.58\\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.\nThis motivates a principled exclusion criterion: models with unconstrained ET${>}$5\\% on either dataset fall outside the regime where the tightness$\\times$RV product is the primary DR driver.\nThe two DocRED points (high $\\bar{\\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\\bar{\\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/dual_factor_scatter.pdf}\n\\caption{Residual DR vs.\\ $\\bar{\\kappa} \\times \\text{RV}_{\\text{baseline}}$ across four model$\\times$dataset configurations.\nLinear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification.}\n\\label{fig:dual-factor-scatter}\n\\end{figure}\n\n%%% Dataset-Dependent F1 Impact (moved from §7) %%%\n% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),\n%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)\n\n\\paragraph{Dataset-Dependent F1 Impact.}\nThe divergence in F1 significance between DocRED ($+$0.50\\,pp, $p < 0.001$) and SciERC ($+$0.13\\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.\nDocRED's baseline RV of 29.66\\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.\nSciERC's baseline RV is only 1.39\\% (24 OOV predictions), too few to produce a detectable F1 effect.\nLlama-3.1-8B's lower baseline RV (16.03\\%) yields a smaller but directionally consistent improvement ($+$0.29\\,pp vs.\\ $+$0.50\\,pp); F1 gain magnitude is proportional to baseline OOV rate.\n% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained\n% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)\n\n%%% Paragraph 1: Low F1 Practical Significance %%%\n% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),\n%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)\n\n\\paragraph{Practical Significance of Zero-Shot F1.}\nOur reported relation F1 of approximately 8\\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.\nFor reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\\% relation F1 with full training data~\\citep{zhong2021frustratingly,ye2022packed}.\nConstraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.\nEven after LoRA fine-tuning, residual DR of 1--2\\% persists on tight-constraint relations (Table~\\ref{tab:composability}); constraints remain necessary at deployment-grade quality.\n% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval\nIn our evaluation, F1 serves as a \\emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.\nThe contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\\S\\ref{sec:composability}) validates practical deployment value.\n\n%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%\n% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),\n%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)\n\n\\paragraph{Decoding-Time vs.\\ Post-Hoc Enforcement.}\nPost-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\\ 8.36; DocRED 9.61 vs.\\ 8.23).\n% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23\nHowever, this precision gain comes at substantial cost.\nOn DocRED, post-hoc filtering discards 48.1\\% of all predicted triples, including 127 true positives (11.2\\% of correct predictions); recall drops from 9.46\\% to 8.40\\%.\n% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40\nEntity type violations remain unresolved (ET\\,=\\,2.47\\% vs.\\ OntoCoDec's 0\\%), as filtering targets only domain/range and vocabulary violations.\n% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%\nOntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.\nThe two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.\n\n%%% CF Violation Distribution %%%\n% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),\n%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)\n\n\\paragraph{Cross-Field Violation Distribution.}\n\\label{app:cf-distribution}\n\nTable~\\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC full S1 (245 CF violations, all pairwise; no mention triggered $\\geq$3 types).\nConflicts involving the \\textsc{Generic} type account for 63.3\\% (155/245) of all violations.\n\\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.\n\nThe pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \\textsc{Generic}$\\leftrightarrow$\\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\\%); on DocRED, the analogous catch-all type \\textsc{MISC} drives 76.6\\% of Qwen's CF violations.\nUnder unconstrained decoding, CF rates collapse to $\\leq$1\\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lr r@{}}\n\\toprule\n\\textbf{Conflicting Type Pair} & \\textbf{Count} & \\textbf{\\%} \\\\\n\\midrule\nGeneric $\\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\\\\nGeneric $\\leftrightarrow$ Material & 35 & 14.3 \\\\\nGeneric $\\leftrightarrow$ Metric & 30 & 12.2 \\\\\nMethod $\\leftrightarrow$ Task & 20 & 8.2 \\\\\nMaterial $\\leftrightarrow$ Method & 17 & 6.9 \\\\\nOtherScientificTerm $\\leftrightarrow$ Task & 12 & 4.9 \\\\\n\\midrule\n10 further pairs (each $\\leq$3.3\\%) & 46 & 18.8 \\\\\n\\midrule\n\\textbf{Total} & \\textbf{245} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF violation distribution on SciERC full S1 (Qwen3-8B, 551 documents).\nAll 245 violations are pairwise conflicts.\nConflicts involving \\textsc{Generic} account for 63.3\\%.}\n\\label{tab:cf-distribution}\n\\end{table}\n\n%%% Per-Relation DR Elimination under Fine-Tuning %%%\n% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1\n\n\\paragraph{Per-Relation DR Elimination under Fine-Tuning.}\n\\label{app:lora-per-relation}\n\nTable~\\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.\nFine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \\textsc{Evaluate-for} ($\\kappa{=}0.361$, 13.13\\%), \\textsc{Part-of} ($\\kappa{=}0.417$, 5.77\\%), and \\textsc{Compare} ($\\kappa{=}0.528$, 5.00\\%).\nAdding OntoCoDec constraints eliminates all remaining violations across all relations.\nOne \\textsc{Evaluate-for} triple (99\\,$\\to$\\,98) is redirected to \\textsc{Used-for} (634\\,$\\to$\\,635) by token-level masking: the head entity's registered type falls outside \\textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}l r rr rr@{}}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{LoRA Unconstr.}} & \\multicolumn{2}{c}{\\textbf{LoRA + S1}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(l){5-6}\n\\textbf{Relation} & $\\kappa$ & DR\\,(\\%) & $n$ & DR\\,(\\%) & $n$ \\\\\n\\midrule\nEvaluate-for & 0.361 & 13.13 & 99 & \\textbf{0} & 98 \\\\\nPart-of      & 0.417 & 5.77  & 52 & \\textbf{0} & 52 \\\\\nCompare      & 0.528 & 5.00  & 40 & \\textbf{0} & 40 \\\\\nConjunction  & 0.306 & 1.31  & 153 & \\textbf{0} & 153 \\\\\nFeature-of   & 0.278 & 1.35  & 74 & \\textbf{0} & 74 \\\\\nUsed-for     & 0.028 & 0.16  & 634 & \\textbf{0} & 635 \\\\\nHyponym-of   & 0.417 & 0     & --- & \\textbf{0} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).\n$\\kappa$: constraint tightness; $n$: predicted triple count.\nUsed-for gains one triple from Evaluate-for redirection.}\n\\label{tab:lora-per-relation}\n\\end{table}\n\n%%% Fine-Tuned Four-Way Ablation %%%\n% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*\n\n\\paragraph{Fine-Tuned Four-Way Ablation.}\n\\label{app:ft-ablation}\n\nTable~\\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrrr rr@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Model} & \\textbf{Mode} & \\textbf{DR\\,$\\downarrow$} & \\textbf{RV\\,$\\downarrow$} & \\textbf{ET\\,$\\downarrow$} & \\textbf{CF} & \\textbf{PF} & \\textbf{E-F1\\,$\\uparrow$} & \\textbf{R-F1\\,$\\uparrow$} \\\\\n\\midrule\n\\multirow{8}{*}{SciERC}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\\n  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\\n  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\\\\n  & & Full S1       & \\textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\\\\n  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\\\\n  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\\\\n  & & Full S1       & \\textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\\\\n\\midrule\n\\multirow{8}{*}{DocRED}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.09 & 7.11 & 82.15 & 40.86 \\\\\n  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\\\\n  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\\\\n  & & Full S1       & \\textbf{0.01} & 0.00 & 0.00 & 0.27 & 8.52 & 81.43 & 40.56 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\\\\n  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\\\\n  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\\\\n  & & Full S1       & \\textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\\times$ 2 datasets).\nDR/RV/ET/CF: violation rates (\\%); PF: parse failure rate (\\%); F1 $\\times$100.\nGrammar layer is a no-op post-fine-tuning (DR change $<$0.2\\,pp in all 4 settings; RV and ET already 0\\% without constraints).\nSemantic layer is the sole effective DR defense, providing 39--72\\% reduction.\nF1 cost is negligible: max $\\Delta$R-F1 = $-$0.30\\,pp (Qwen DocRED full vs.\\ unconstrained).}\n\\label{tab:ft-ablation}\n\\end{table}\n\nThe grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\\% without constraints, and grammar-only DR change is $<$0.2\\,pp (4/4 settings).\nThe semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\\% across all settings (SciERC: Qwen $-$69\\%, Llama $-$41\\%; DocRED: Qwen $-$72\\%, Llama $-$39\\%).\nAdding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.20\\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.\nF1 cost is negligible: the maximum R-F1 decrease across all 16 model$\\times$dataset$\\times$mode combinations is $-$0.30\\,pp (Qwen DocRED, full vs.\\ unconstrained), attributable to parse failure increase (7.11\\%\\,$\\to$\\,8.52\\%) rather than constraint-induced extraction degradation.\n\n%%% Residual DR Error Analysis (Fine-Tuned) %%%\n% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*\n\n\\paragraph{Residual DR Error Analysis.}\n\\label{app:residual-dr-analysis}\n\nAcross all fine-tuned settings (2 models $\\times$ 2 datasets $\\times$ full S1), only 36 domain/range violations remain.\nManual inspection reveals four root causes:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\emph{Entity type errors} (39\\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \\textsc{LOC} when the gold standard requires \\textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.\n\\item \\emph{Schema coverage gaps} (33\\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.\n\\item \\emph{Incorrect relation selection} (17\\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.\n\\item \\emph{Direction reversal} (11\\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.\n\\end{enumerate}\n\nTwo dataset-specific patterns emerge.\nOutside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.\nOn DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\\%), with entity type errors as the dominant cause (14/33, 42\\%).\nThis asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.\nThe implication is twofold: (i)~the irreducible floor from schema gaps is small ($\\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.\n\n%%% Post-Hoc Filtering Comparison (Extended) %%%\n% exp_ids: posthoc_*_zs, posthoc_*_ft\n\n\\paragraph{Post-Hoc Filtering: Extended Comparison.}\n\\label{app:posthoc-extended}\n\nTable~\\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrr l@{}}\n\\toprule\n\\textbf{Setting} & \\textbf{Model} & \\textbf{Dataset} & \\textbf{Reject\\%} & \\textbf{R-F1$_{\\text{ph}}$} & \\textbf{R-F1$_{\\text{cd}}$} & \\textbf{Winner} \\\\\n\\midrule\n\\multirow{6}{*}{ZS}\n  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\\\\n  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\\\\n  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\\\\n  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\\\\n  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\\\\n  & Mistral & DocRED & \\textbf{73.7} & 3.85  & \\textbf{5.52} & cd \\\\\n\\midrule\n\\multirow{4}{*}{FT}\n  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\\\\n  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\\\\n  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\\\\n  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Post-hoc filtering (ph) vs.\\ constrained decoding (cd).\nIn zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.\nAt reject rate $>$70\\% (Mistral DocRED), post-hoc F1 collapses below constrained.\nUnder fine-tuning, rejection rates drop to 0.6--2.0\\% and the two strategies are equivalent ($\\Delta \\leq 0.55$\\,pp; each wins two groups).\nF1 $\\times$100.}\n\\label{tab:posthoc-extended}\n\\end{table}\n\nThe crossover point occurs when post-hoc rejection exceeds $\\sim$70\\%: Mistral DocRED rejects 73.7\\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\\,pp).\nOntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.\nUnder fine-tuning, both strategies converge because few violations remain to filter or constrain ($\\Delta \\leq 0.55$\\,pp across all four FT groups, with each strategy winning two).\n\n%%% Zero-Shot Runtime Profiling %%%\n\n\\paragraph{Zero-Shot Runtime Profiling.}\n\\label{app:runtime}\n\nOn SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\\,s/doc and Full S1 constrained decoding averages 4.710\\,s/doc ($+$13.1\\% overhead).\nOn DocRED (same configuration), unconstrained inference averages 19.34\\,s/doc and Full S1 averages 19.81\\,s/doc ($+$2.43\\% overhead).\nThe lower relative overhead on DocRED reflects amortization: the fixed per-token constraint cost is spread over longer generation sequences.\nXGrammar automaton compilation takes 0.044\\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\\,s on SciERC (Table~\\ref{tab:scalability}), amortized to zero over the evaluation set.\n\n% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified\n\\paragraph{Fine-Tuned Latency Profiling.}\n\\label{app:ft-latency}\nUnder LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\\,s/doc and Full S1 constrained decoding averages 2.873\\,s/doc ($+$10.0\\% overhead, $n{=}551$).\nFine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\\,s vs.\\ 4.163\\,s/doc unconstrained); absolute generation time drops by 37\\%.\nThe relative overhead ($+$10.0\\%) is slightly lower than zero-shot ($+$13.1\\%), consistent with shorter sequences requiring fewer constraint checks per document.\n\n%%% Fuzzy Relation Matching %%%\n\n\\paragraph{Relation Matching Protocol.}\n\\label{app:fuzzy-matching}\nRelation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\\ spaces, abbreviations).\nA predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\\% \\emph{and} edit distance $\\leq 2$.\nThis protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\\_of\\_government'' for ``head of government'').\nOn Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\\,pp R-F1; strict R-F1\\,=\\,3.50\\% vs.\\ fuzzy 4.34\\%).\nFor Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).\nAll F1 figures in the main text use fuzzy normalization consistently across all models and conditions.\n\n%%% Per-Relation Violation Landscape %%%\n\n\\paragraph{Per-Relation Violation Landscape.}\n\\label{app:per-relation-landscape}\n\nTable~\\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.\nFigure~\\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Violation rates (\\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}\n\\label{tab:prompt_comparison}\n\\begin{tabular}{ll cccc}\n\\toprule\nDataset & Prompt & DR$\\downarrow$ & RV$\\downarrow$ & ET$\\downarrow$ & CF$\\downarrow$ \\\\\n\\midrule\n\\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\\\\n & Schema-informed & 5.8 & 0.3 & \\textbf{0.0} & --- \\\\\n\\midrule\n\\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\\\\n & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_per_relation_dr.pdf}\n\\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\\kappa(r)$.}\n\\label{fig:per_relation_dr}\n\\end{figure}\n\n%%% WikiEvents Extended %%%\n\n\\paragraph{WikiEvents Dataset Details.}\n\\label{app:wikievents}\nWikiEvents~\\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.\nIt defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\\_type, role)$\\to$allowed\\_entity\\_types constraints.\nThe grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.\n\n\\paragraph{Constraint Tightness in WikiEvents.}\n\\label{app:wikievents-kappa}\n% Data source: artifacts/w1c_wikievents_kappa_results.md\nWikiEvents role-level tightness (Eq.~\\ref{eq:tightness}, with $|\\mathcal{E}|{=}27$) has mean $\\bar{\\kappa}{=}0.82$ and median 0.89; 84\\% of roles have $\\kappa \\geq 0.80$ (4 or fewer valid entity types out of 27).\nThe tightness-violation pattern extends to event extraction: roles with $\\kappa \\geq 0.90$ exhibit the highest AC rate (50\\%), compared to 21\\% for medium-tightness ($0.80 \\leq \\kappa < 0.90$) and 30\\% for loose ($\\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.\nHowever, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\\to$VEH) show 0\\% AC despite $\\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\\to$CRM, Sentence$\\to$SEN) show near-100\\% AC because LLMs default to common types (PER, ORG).\nThe loose group's elevated rate (30\\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\\% AC, $\\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.\n",
    "structuredPatch": [
      {
        "oldStart": 259,
        "oldLines": 7,
        "newStart": 259,
        "newLines": 7,
        "lines": [
          "     & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\\\",
          "   & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\\\",
          "   & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\\\",
          "-  & & Full S1       & \\textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 83.94 & 44.23 \\\\",
          "+  & & Full S1       & \\textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\\\",
          " \\bottomrule",
          " \\end{tabular}}%",
          " \\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\\times$ 2 datasets)."
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

_source line 56_

<details open><summary>🔧 Tool call — Edit · `toolu_01M9n98bkehFVvYk6b11wKxZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.20\\% in all 4 settings)",
  "new_string": "Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.21\\% in all 4 settings)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "a12d0e0c-232d-4708-9130-7ef303e8efd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJydBNEEAPssnBuBpAY44v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 47840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 57 · 2026-05-20T11:16:16.559Z_

<details><summary>↩ Tool result · `toolu_01M9n98bkehFVvYk6b11wKxZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "3ec7041b-729c-4c2c-b6ce-6c2427bc93f7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "oldString": "Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.20\\% in all 4 settings)",
    "newString": "Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.21\\% in all 4 settings)",
    "originalFile": "% Appendix B — Extended Discussion\n% Contains discussion paragraphs moved from the main text during compression.\n\n\\section{Extended Discussion}\\label{app:discussion}\n\n%%% CF Dual Mechanism %%%\n% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1\n\n\\paragraph{CF Dual Mechanism.}\nCF violations arise from two distinct mechanisms:\n(1)~\\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.\nThe entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.\n(2)~\\emph{Grammar-first fallback} (\\S\\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.\n\nThese mechanisms have sharply different model profiles.\nQwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\\% of its CF violations to registry override.\nLlama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.\nThis asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\\,=\\,2.57\\% on DocRED vs.\\ Llama's 12.02\\%, despite both using identical constraint configurations.\nThe difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.\n\n%%% Fallback Behavior and Effective Coverage %%%\n% exp_ids: cf_fallback_ablation_scierc (final data)\n\n\\paragraph{Fallback Behavior and Effective Coverage.}\n\\label{app:fallback-coverage}\nThe two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.\n\\emph{Grammar-first fallback} (36.6\\% of type-bearing positions on SciERC) occurs when $S(t) \\cap G(t) = \\emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations. These events account for the residual DR that persists after constraint enforcement.\n\\emph{Registry-consistent fallback} (4.5\\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.\nTogether, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.\n\nWe define \\emph{effective semantic constraint coverage} as $1 - f_{\\text{gf}}$, where $f_{\\text{gf}}$ is the grammar-first fallback rate.\nOn SciERC, Llama-3.1-8B shows $f_{\\text{gf}} = 36.6\\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\\% effective coverage.\nOn DocRED, by contrast, Qwen3-8B shows $f_{\\text{gf}} = 0.08\\%$ (46 of 54{,}859), yielding 99.9\\% coverage.\nThe large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \\textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.\nDocRED types (\\textsc{PER}, \\textsc{ORG}, \\textsc{LOC}, \\textsc{TIME}, \\textsc{NUM}, \\textsc{MISC}) are all single-token, eliminating this inflation.\nThis metric directly quantifies the enabling dependency (\\S\\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.\nQwen3-8B, with zero grammar-first fallbacks, achieves 100\\% effective coverage on SciERC, consistent with its lower residual DR (0.93\\% vs.\\ Llama's 0.08\\%).\n\n%%% CF-DR Trade-off Analysis %%%\n% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)\n\n\\paragraph{CF-DR Trade-off Analysis.}\n\\label{app:cf-dr-tradeoff}\n\nCF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\\% on SciERC, up to 12.02\\% on Llama DocRED).\nWe treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.\nTable~\\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\\sigma(r)$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}l rrrr@{}}\n\\toprule\n\\textbf{Configuration} & \\textbf{DR\\,(\\%)} & \\textbf{CF\\,(\\%)} & \\textbf{DR+CF} & \\textbf{$f_{\\text{gf}}$\\,(\\%)} \\\\\n\\midrule\nFull S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\\\\nCF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\\\\n\\midrule\n$\\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \\texttt{w1\\_cf\\_fallback\\_scierc\\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\\,pp. $f_{\\text{gf}}$: grammar-first fallback rate at type-bearing positions.}\n\\label{tab:cf-dr-tradeoff}\n\\end{table}\n\nThe CF fallback variant nearly eliminates CF (9.90\\%\\,$\\to$\\,0.04\\%, $-$9.86\\,pp) but at the cost of a 15.9$\\times$ increase in DR (0.93\\%\\,$\\to$\\,14.78\\%, $+$13.85\\,pp).\n% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664\nThis is not a net improvement: total violations (DR+CF) rise from 10.83\\% to 14.82\\% ($+$3.99\\,pp), so the change \\emph{re-routes} violations rather than reducing them.\nThe mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.\nThe grammar-first fallback is triggered at 36.64\\% of type-bearing positions; this conflict is structural, not a tunable hyperparameter.\n\nWe interpret this as a fundamental tension in composable constraint systems with \\emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.\nWithin this design, the current full S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\\% DR at the cost of 9.90\\% CF.\nThe direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\\times$ 2 datasets), DR and CF are inversely associated (Spearman $\\rho = -0.77$, $n{=}6$), with no setting showing both high DR and high CF simultaneously (Table~\\ref{tab:cross-model}).\nThe pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\\%), making the trade-off most visible.\nWhile the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.\nThe CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\\% of CF violations on SciERC involve the catch-all \\textsc{Generic} type (Table~\\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.\n\nTwo complementary paths can lower CF without re-routing it to DR.\n(i)~\\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\\% relative to the zero-shot setting (9.90\\%\\,$\\to$\\,1.18\\%; Table~\\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.\n% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118\nThe remaining 1.18\\% still traces to \\textsc{Generic}$\\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.\n(ii)~\\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.\n\n%%% Dual-Factor Quantitative Analysis %%%\n% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,\n%          llama_scierc_full_s1, llama_docred_full_s1\n\n\\paragraph{Dual-Factor Quantitative Analysis.}\n\\label{app:dual-factor}\n\nFigure~\\ref{fig:dual-factor-scatter} plots residual DR against the product $\\bar{\\kappa} \\times \\text{RV}_{\\text{baseline}}$ for model$\\times$dataset configurations.\nFor \\emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \\approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.\nThe strong fit supports the dual-factor pattern from \\S\\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.\nMistral-7B (unconstrained ET${=}$7.58\\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.\nThis motivates a principled exclusion criterion: models with unconstrained ET${>}$5\\% on either dataset fall outside the regime where the tightness$\\times$RV product is the primary DR driver.\nThe two DocRED points (high $\\bar{\\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\\bar{\\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/dual_factor_scatter.pdf}\n\\caption{Residual DR vs.\\ $\\bar{\\kappa} \\times \\text{RV}_{\\text{baseline}}$ across four model$\\times$dataset configurations.\nLinear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification.}\n\\label{fig:dual-factor-scatter}\n\\end{figure}\n\n%%% Dataset-Dependent F1 Impact (moved from §7) %%%\n% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),\n%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)\n\n\\paragraph{Dataset-Dependent F1 Impact.}\nThe divergence in F1 significance between DocRED ($+$0.50\\,pp, $p < 0.001$) and SciERC ($+$0.13\\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.\nDocRED's baseline RV of 29.66\\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.\nSciERC's baseline RV is only 1.39\\% (24 OOV predictions), too few to produce a detectable F1 effect.\nLlama-3.1-8B's lower baseline RV (16.03\\%) yields a smaller but directionally consistent improvement ($+$0.29\\,pp vs.\\ $+$0.50\\,pp); F1 gain magnitude is proportional to baseline OOV rate.\n% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained\n% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)\n\n%%% Paragraph 1: Low F1 Practical Significance %%%\n% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),\n%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)\n\n\\paragraph{Practical Significance of Zero-Shot F1.}\nOur reported relation F1 of approximately 8\\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.\nFor reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\\% relation F1 with full training data~\\citep{zhong2021frustratingly,ye2022packed}.\nConstraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.\nEven after LoRA fine-tuning, residual DR of 1--2\\% persists on tight-constraint relations (Table~\\ref{tab:composability}); constraints remain necessary at deployment-grade quality.\n% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval\nIn our evaluation, F1 serves as a \\emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.\nThe contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\\S\\ref{sec:composability}) validates practical deployment value.\n\n%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%\n% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),\n%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)\n\n\\paragraph{Decoding-Time vs.\\ Post-Hoc Enforcement.}\nPost-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\\ 8.36; DocRED 9.61 vs.\\ 8.23).\n% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23\nHowever, this precision gain comes at substantial cost.\nOn DocRED, post-hoc filtering discards 48.1\\% of all predicted triples, including 127 true positives (11.2\\% of correct predictions); recall drops from 9.46\\% to 8.40\\%.\n% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40\nEntity type violations remain unresolved (ET\\,=\\,2.47\\% vs.\\ OntoCoDec's 0\\%), as filtering targets only domain/range and vocabulary violations.\n% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%\nOntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.\nThe two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.\n\n%%% CF Violation Distribution %%%\n% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),\n%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)\n\n\\paragraph{Cross-Field Violation Distribution.}\n\\label{app:cf-distribution}\n\nTable~\\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC full S1 (245 CF violations, all pairwise; no mention triggered $\\geq$3 types).\nConflicts involving the \\textsc{Generic} type account for 63.3\\% (155/245) of all violations.\n\\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.\n\nThe pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \\textsc{Generic}$\\leftrightarrow$\\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\\%); on DocRED, the analogous catch-all type \\textsc{MISC} drives 76.6\\% of Qwen's CF violations.\nUnder unconstrained decoding, CF rates collapse to $\\leq$1\\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lr r@{}}\n\\toprule\n\\textbf{Conflicting Type Pair} & \\textbf{Count} & \\textbf{\\%} \\\\\n\\midrule\nGeneric $\\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\\\\nGeneric $\\leftrightarrow$ Material & 35 & 14.3 \\\\\nGeneric $\\leftrightarrow$ Metric & 30 & 12.2 \\\\\nMethod $\\leftrightarrow$ Task & 20 & 8.2 \\\\\nMaterial $\\leftrightarrow$ Method & 17 & 6.9 \\\\\nOtherScientificTerm $\\leftrightarrow$ Task & 12 & 4.9 \\\\\n\\midrule\n10 further pairs (each $\\leq$3.3\\%) & 46 & 18.8 \\\\\n\\midrule\n\\textbf{Total} & \\textbf{245} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF violation distribution on SciERC full S1 (Qwen3-8B, 551 documents).\nAll 245 violations are pairwise conflicts.\nConflicts involving \\textsc{Generic} account for 63.3\\%.}\n\\label{tab:cf-distribution}\n\\end{table}\n\n%%% Per-Relation DR Elimination under Fine-Tuning %%%\n% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1\n\n\\paragraph{Per-Relation DR Elimination under Fine-Tuning.}\n\\label{app:lora-per-relation}\n\nTable~\\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.\nFine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \\textsc{Evaluate-for} ($\\kappa{=}0.361$, 13.13\\%), \\textsc{Part-of} ($\\kappa{=}0.417$, 5.77\\%), and \\textsc{Compare} ($\\kappa{=}0.528$, 5.00\\%).\nAdding OntoCoDec constraints eliminates all remaining violations across all relations.\nOne \\textsc{Evaluate-for} triple (99\\,$\\to$\\,98) is redirected to \\textsc{Used-for} (634\\,$\\to$\\,635) by token-level masking: the head entity's registered type falls outside \\textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}l r rr rr@{}}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{LoRA Unconstr.}} & \\multicolumn{2}{c}{\\textbf{LoRA + S1}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(l){5-6}\n\\textbf{Relation} & $\\kappa$ & DR\\,(\\%) & $n$ & DR\\,(\\%) & $n$ \\\\\n\\midrule\nEvaluate-for & 0.361 & 13.13 & 99 & \\textbf{0} & 98 \\\\\nPart-of      & 0.417 & 5.77  & 52 & \\textbf{0} & 52 \\\\\nCompare      & 0.528 & 5.00  & 40 & \\textbf{0} & 40 \\\\\nConjunction  & 0.306 & 1.31  & 153 & \\textbf{0} & 153 \\\\\nFeature-of   & 0.278 & 1.35  & 74 & \\textbf{0} & 74 \\\\\nUsed-for     & 0.028 & 0.16  & 634 & \\textbf{0} & 635 \\\\\nHyponym-of   & 0.417 & 0     & --- & \\textbf{0} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).\n$\\kappa$: constraint tightness; $n$: predicted triple count.\nUsed-for gains one triple from Evaluate-for redirection.}\n\\label{tab:lora-per-relation}\n\\end{table}\n\n%%% Fine-Tuned Four-Way Ablation %%%\n% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*\n\n\\paragraph{Fine-Tuned Four-Way Ablation.}\n\\label{app:ft-ablation}\n\nTable~\\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrrr rr@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Model} & \\textbf{Mode} & \\textbf{DR\\,$\\downarrow$} & \\textbf{RV\\,$\\downarrow$} & \\textbf{ET\\,$\\downarrow$} & \\textbf{CF} & \\textbf{PF} & \\textbf{E-F1\\,$\\uparrow$} & \\textbf{R-F1\\,$\\uparrow$} \\\\\n\\midrule\n\\multirow{8}{*}{SciERC}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\\n  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\\n  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\\\\n  & & Full S1       & \\textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\\\\n  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\\\\n  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\\\\n  & & Full S1       & \\textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\\\\n\\midrule\n\\multirow{8}{*}{DocRED}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.09 & 7.11 & 82.15 & 40.86 \\\\\n  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\\\\n  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\\\\n  & & Full S1       & \\textbf{0.01} & 0.00 & 0.00 & 0.27 & 8.52 & 81.43 & 40.56 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\\\\n  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\\\\n  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\\\\n  & & Full S1       & \\textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\\times$ 2 datasets).\nDR/RV/ET/CF: violation rates (\\%); PF: parse failure rate (\\%); F1 $\\times$100.\nGrammar layer is a no-op post-fine-tuning (DR change $<$0.2\\,pp in all 4 settings; RV and ET already 0\\% without constraints).\nSemantic layer is the sole effective DR defense, providing 39--72\\% reduction.\nF1 cost is negligible: max $\\Delta$R-F1 = $-$0.30\\,pp (Qwen DocRED full vs.\\ unconstrained).}\n\\label{tab:ft-ablation}\n\\end{table}\n\nThe grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\\% without constraints, and grammar-only DR change is $<$0.2\\,pp (4/4 settings).\nThe semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\\% across all settings (SciERC: Qwen $-$69\\%, Llama $-$41\\%; DocRED: Qwen $-$72\\%, Llama $-$39\\%).\nAdding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.20\\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.\nF1 cost is negligible: the maximum R-F1 decrease across all 16 model$\\times$dataset$\\times$mode combinations is $-$0.30\\,pp (Qwen DocRED, full vs.\\ unconstrained), attributable to parse failure increase (7.11\\%\\,$\\to$\\,8.52\\%) rather than constraint-induced extraction degradation.\n\n%%% Residual DR Error Analysis (Fine-Tuned) %%%\n% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*\n\n\\paragraph{Residual DR Error Analysis.}\n\\label{app:residual-dr-analysis}\n\nAcross all fine-tuned settings (2 models $\\times$ 2 datasets $\\times$ full S1), only 36 domain/range violations remain.\nManual inspection reveals four root causes:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\emph{Entity type errors} (39\\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \\textsc{LOC} when the gold standard requires \\textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.\n\\item \\emph{Schema coverage gaps} (33\\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.\n\\item \\emph{Incorrect relation selection} (17\\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.\n\\item \\emph{Direction reversal} (11\\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.\n\\end{enumerate}\n\nTwo dataset-specific patterns emerge.\nOutside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.\nOn DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\\%), with entity type errors as the dominant cause (14/33, 42\\%).\nThis asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.\nThe implication is twofold: (i)~the irreducible floor from schema gaps is small ($\\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.\n\n%%% Post-Hoc Filtering Comparison (Extended) %%%\n% exp_ids: posthoc_*_zs, posthoc_*_ft\n\n\\paragraph{Post-Hoc Filtering: Extended Comparison.}\n\\label{app:posthoc-extended}\n\nTable~\\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrr l@{}}\n\\toprule\n\\textbf{Setting} & \\textbf{Model} & \\textbf{Dataset} & \\textbf{Reject\\%} & \\textbf{R-F1$_{\\text{ph}}$} & \\textbf{R-F1$_{\\text{cd}}$} & \\textbf{Winner} \\\\\n\\midrule\n\\multirow{6}{*}{ZS}\n  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\\\\n  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\\\\n  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\\\\n  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\\\\n  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\\\\n  & Mistral & DocRED & \\textbf{73.7} & 3.85  & \\textbf{5.52} & cd \\\\\n\\midrule\n\\multirow{4}{*}{FT}\n  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\\\\n  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\\\\n  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\\\\n  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Post-hoc filtering (ph) vs.\\ constrained decoding (cd).\nIn zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.\nAt reject rate $>$70\\% (Mistral DocRED), post-hoc F1 collapses below constrained.\nUnder fine-tuning, rejection rates drop to 0.6--2.0\\% and the two strategies are equivalent ($\\Delta \\leq 0.55$\\,pp; each wins two groups).\nF1 $\\times$100.}\n\\label{tab:posthoc-extended}\n\\end{table}\n\nThe crossover point occurs when post-hoc rejection exceeds $\\sim$70\\%: Mistral DocRED rejects 73.7\\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\\,pp).\nOntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.\nUnder fine-tuning, both strategies converge because few violations remain to filter or constrain ($\\Delta \\leq 0.55$\\,pp across all four FT groups, with each strategy winning two).\n\n%%% Zero-Shot Runtime Profiling %%%\n\n\\paragraph{Zero-Shot Runtime Profiling.}\n\\label{app:runtime}\n\nOn SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\\,s/doc and Full S1 constrained decoding averages 4.710\\,s/doc ($+$13.1\\% overhead).\nOn DocRED (same configuration), unconstrained inference averages 19.34\\,s/doc and Full S1 averages 19.81\\,s/doc ($+$2.43\\% overhead).\nThe lower relative overhead on DocRED reflects amortization: the fixed per-token constraint cost is spread over longer generation sequences.\nXGrammar automaton compilation takes 0.044\\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\\,s on SciERC (Table~\\ref{tab:scalability}), amortized to zero over the evaluation set.\n\n% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified\n\\paragraph{Fine-Tuned Latency Profiling.}\n\\label{app:ft-latency}\nUnder LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\\,s/doc and Full S1 constrained decoding averages 2.873\\,s/doc ($+$10.0\\% overhead, $n{=}551$).\nFine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\\,s vs.\\ 4.163\\,s/doc unconstrained); absolute generation time drops by 37\\%.\nThe relative overhead ($+$10.0\\%) is slightly lower than zero-shot ($+$13.1\\%), consistent with shorter sequences requiring fewer constraint checks per document.\n\n%%% Fuzzy Relation Matching %%%\n\n\\paragraph{Relation Matching Protocol.}\n\\label{app:fuzzy-matching}\nRelation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\\ spaces, abbreviations).\nA predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\\% \\emph{and} edit distance $\\leq 2$.\nThis protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\\_of\\_government'' for ``head of government'').\nOn Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\\,pp R-F1; strict R-F1\\,=\\,3.50\\% vs.\\ fuzzy 4.34\\%).\nFor Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).\nAll F1 figures in the main text use fuzzy normalization consistently across all models and conditions.\n\n%%% Per-Relation Violation Landscape %%%\n\n\\paragraph{Per-Relation Violation Landscape.}\n\\label{app:per-relation-landscape}\n\nTable~\\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.\nFigure~\\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Violation rates (\\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}\n\\label{tab:prompt_comparison}\n\\begin{tabular}{ll cccc}\n\\toprule\nDataset & Prompt & DR$\\downarrow$ & RV$\\downarrow$ & ET$\\downarrow$ & CF$\\downarrow$ \\\\\n\\midrule\n\\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\\\\n & Schema-informed & 5.8 & 0.3 & \\textbf{0.0} & --- \\\\\n\\midrule\n\\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\\\\n & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_per_relation_dr.pdf}\n\\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\\kappa(r)$.}\n\\label{fig:per_relation_dr}\n\\end{figure}\n\n%%% WikiEvents Extended %%%\n\n\\paragraph{WikiEvents Dataset Details.}\n\\label{app:wikievents}\nWikiEvents~\\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.\nIt defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\\_type, role)$\\to$allowed\\_entity\\_types constraints.\nThe grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.\n\n\\paragraph{Constraint Tightness in WikiEvents.}\n\\label{app:wikievents-kappa}\n% Data source: artifacts/w1c_wikievents_kappa_results.md\nWikiEvents role-level tightness (Eq.~\\ref{eq:tightness}, with $|\\mathcal{E}|{=}27$) has mean $\\bar{\\kappa}{=}0.82$ and median 0.89; 84\\% of roles have $\\kappa \\geq 0.80$ (4 or fewer valid entity types out of 27).\nThe tightness-violation pattern extends to event extraction: roles with $\\kappa \\geq 0.90$ exhibit the highest AC rate (50\\%), compared to 21\\% for medium-tightness ($0.80 \\leq \\kappa < 0.90$) and 30\\% for loose ($\\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.\nHowever, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\\to$VEH) show 0\\% AC despite $\\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\\to$CRM, Sentence$\\to$SEN) show near-100\\% AC because LLMs default to common types (PER, ORG).\nThe loose group's elevated rate (30\\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\\% AC, $\\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.\n",
    "structuredPatch": [
      {
        "oldStart": 272,
        "oldLines": 7,
        "newStart": 272,
        "newLines": 7,
        "lines": [
          " ",
          " The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\\% without constraints, and grammar-only DR change is $<$0.2\\,pp (4/4 settings).",
          " The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\\% across all settings (SciERC: Qwen $-$69\\%, Llama $-$41\\%; DocRED: Qwen $-$72\\%, Llama $-$39\\%).",
          "-Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.20\\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.",
          "+Adding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.21\\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.",
          " F1 cost is negligible: the maximum R-F1 decrease across all 16 model$\\times$dataset$\\times$mode combinations is $-$0.30\\,pp (Qwen DocRED, full vs.\\ unconstrained), attributable to parse failure increase (7.11\\%\\,$\\to$\\,8.52\\%) rather than constraint-induced extraction degradation.",
          " ",
          " %%% Residual DR Error Analysis (Fine-Tuned) %%%"
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

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_01QNDvx4iDrPpcp5CUfVRkQp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\",
  "new_string": "  & Llama   & DocRED & 0.64 & 43.92 & 43.78 & cd \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "df300c9d-d3ec-4976-aeb4-7ddbefc01053",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJydBNEEAPssnBuBpAY44v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 47840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 59 · 2026-05-20T11:16:22.318Z_

<details><summary>↩ Tool result · `toolu_01QNDvx4iDrPpcp5CUfVRkQp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "2953a355-b2c7-422b-87f0-840b4db4138c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "oldString": "  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\",
    "newString": "  & Llama   & DocRED & 0.64 & 43.92 & 43.78 & cd \\\\",
    "originalFile": "% Appendix B — Extended Discussion\n% Contains discussion paragraphs moved from the main text during compression.\n\n\\section{Extended Discussion}\\label{app:discussion}\n\n%%% CF Dual Mechanism %%%\n% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1\n\n\\paragraph{CF Dual Mechanism.}\nCF violations arise from two distinct mechanisms:\n(1)~\\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.\nThe entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.\n(2)~\\emph{Grammar-first fallback} (\\S\\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.\n\nThese mechanisms have sharply different model profiles.\nQwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\\% of its CF violations to registry override.\nLlama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.\nThis asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\\,=\\,2.57\\% on DocRED vs.\\ Llama's 12.02\\%, despite both using identical constraint configurations.\nThe difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.\n\n%%% Fallback Behavior and Effective Coverage %%%\n% exp_ids: cf_fallback_ablation_scierc (final data)\n\n\\paragraph{Fallback Behavior and Effective Coverage.}\n\\label{app:fallback-coverage}\nThe two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.\n\\emph{Grammar-first fallback} (36.6\\% of type-bearing positions on SciERC) occurs when $S(t) \\cap G(t) = \\emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations. These events account for the residual DR that persists after constraint enforcement.\n\\emph{Registry-consistent fallback} (4.5\\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.\nTogether, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.\n\nWe define \\emph{effective semantic constraint coverage} as $1 - f_{\\text{gf}}$, where $f_{\\text{gf}}$ is the grammar-first fallback rate.\nOn SciERC, Llama-3.1-8B shows $f_{\\text{gf}} = 36.6\\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\\% effective coverage.\nOn DocRED, by contrast, Qwen3-8B shows $f_{\\text{gf}} = 0.08\\%$ (46 of 54{,}859), yielding 99.9\\% coverage.\nThe large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \\textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.\nDocRED types (\\textsc{PER}, \\textsc{ORG}, \\textsc{LOC}, \\textsc{TIME}, \\textsc{NUM}, \\textsc{MISC}) are all single-token, eliminating this inflation.\nThis metric directly quantifies the enabling dependency (\\S\\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.\nQwen3-8B, with zero grammar-first fallbacks, achieves 100\\% effective coverage on SciERC, consistent with its lower residual DR (0.93\\% vs.\\ Llama's 0.08\\%).\n\n%%% CF-DR Trade-off Analysis %%%\n% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)\n\n\\paragraph{CF-DR Trade-off Analysis.}\n\\label{app:cf-dr-tradeoff}\n\nCF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\\% on SciERC, up to 12.02\\% on Llama DocRED).\nWe treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.\nTable~\\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\\sigma(r)$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}l rrrr@{}}\n\\toprule\n\\textbf{Configuration} & \\textbf{DR\\,(\\%)} & \\textbf{CF\\,(\\%)} & \\textbf{DR+CF} & \\textbf{$f_{\\text{gf}}$\\,(\\%)} \\\\\n\\midrule\nFull S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\\\\nCF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\\\\n\\midrule\n$\\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \\texttt{w1\\_cf\\_fallback\\_scierc\\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\\,pp. $f_{\\text{gf}}$: grammar-first fallback rate at type-bearing positions.}\n\\label{tab:cf-dr-tradeoff}\n\\end{table}\n\nThe CF fallback variant nearly eliminates CF (9.90\\%\\,$\\to$\\,0.04\\%, $-$9.86\\,pp) but at the cost of a 15.9$\\times$ increase in DR (0.93\\%\\,$\\to$\\,14.78\\%, $+$13.85\\,pp).\n% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664\nThis is not a net improvement: total violations (DR+CF) rise from 10.83\\% to 14.82\\% ($+$3.99\\,pp), so the change \\emph{re-routes} violations rather than reducing them.\nThe mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.\nThe grammar-first fallback is triggered at 36.64\\% of type-bearing positions; this conflict is structural, not a tunable hyperparameter.\n\nWe interpret this as a fundamental tension in composable constraint systems with \\emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.\nWithin this design, the current full S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\\% DR at the cost of 9.90\\% CF.\nThe direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\\times$ 2 datasets), DR and CF are inversely associated (Spearman $\\rho = -0.77$, $n{=}6$), with no setting showing both high DR and high CF simultaneously (Table~\\ref{tab:cross-model}).\nThe pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\\%), making the trade-off most visible.\nWhile the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.\nThe CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\\% of CF violations on SciERC involve the catch-all \\textsc{Generic} type (Table~\\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.\n\nTwo complementary paths can lower CF without re-routing it to DR.\n(i)~\\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\\% relative to the zero-shot setting (9.90\\%\\,$\\to$\\,1.18\\%; Table~\\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.\n% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118\nThe remaining 1.18\\% still traces to \\textsc{Generic}$\\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.\n(ii)~\\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.\n\n%%% Dual-Factor Quantitative Analysis %%%\n% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,\n%          llama_scierc_full_s1, llama_docred_full_s1\n\n\\paragraph{Dual-Factor Quantitative Analysis.}\n\\label{app:dual-factor}\n\nFigure~\\ref{fig:dual-factor-scatter} plots residual DR against the product $\\bar{\\kappa} \\times \\text{RV}_{\\text{baseline}}$ for model$\\times$dataset configurations.\nFor \\emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \\approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.\nThe strong fit supports the dual-factor pattern from \\S\\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.\nMistral-7B (unconstrained ET${=}$7.58\\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.\nThis motivates a principled exclusion criterion: models with unconstrained ET${>}$5\\% on either dataset fall outside the regime where the tightness$\\times$RV product is the primary DR driver.\nThe two DocRED points (high $\\bar{\\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\\bar{\\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/dual_factor_scatter.pdf}\n\\caption{Residual DR vs.\\ $\\bar{\\kappa} \\times \\text{RV}_{\\text{baseline}}$ across four model$\\times$dataset configurations.\nLinear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification.}\n\\label{fig:dual-factor-scatter}\n\\end{figure}\n\n%%% Dataset-Dependent F1 Impact (moved from §7) %%%\n% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),\n%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)\n\n\\paragraph{Dataset-Dependent F1 Impact.}\nThe divergence in F1 significance between DocRED ($+$0.50\\,pp, $p < 0.001$) and SciERC ($+$0.13\\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.\nDocRED's baseline RV of 29.66\\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.\nSciERC's baseline RV is only 1.39\\% (24 OOV predictions), too few to produce a detectable F1 effect.\nLlama-3.1-8B's lower baseline RV (16.03\\%) yields a smaller but directionally consistent improvement ($+$0.29\\,pp vs.\\ $+$0.50\\,pp); F1 gain magnitude is proportional to baseline OOV rate.\n% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained\n% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)\n\n%%% Paragraph 1: Low F1 Practical Significance %%%\n% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),\n%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)\n\n\\paragraph{Practical Significance of Zero-Shot F1.}\nOur reported relation F1 of approximately 8\\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.\nFor reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\\% relation F1 with full training data~\\citep{zhong2021frustratingly,ye2022packed}.\nConstraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.\nEven after LoRA fine-tuning, residual DR of 1--2\\% persists on tight-constraint relations (Table~\\ref{tab:composability}); constraints remain necessary at deployment-grade quality.\n% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval\nIn our evaluation, F1 serves as a \\emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.\nThe contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\\S\\ref{sec:composability}) validates practical deployment value.\n\n%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%\n% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),\n%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)\n\n\\paragraph{Decoding-Time vs.\\ Post-Hoc Enforcement.}\nPost-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\\ 8.36; DocRED 9.61 vs.\\ 8.23).\n% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23\nHowever, this precision gain comes at substantial cost.\nOn DocRED, post-hoc filtering discards 48.1\\% of all predicted triples, including 127 true positives (11.2\\% of correct predictions); recall drops from 9.46\\% to 8.40\\%.\n% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40\nEntity type violations remain unresolved (ET\\,=\\,2.47\\% vs.\\ OntoCoDec's 0\\%), as filtering targets only domain/range and vocabulary violations.\n% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%\nOntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.\nThe two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.\n\n%%% CF Violation Distribution %%%\n% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),\n%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)\n\n\\paragraph{Cross-Field Violation Distribution.}\n\\label{app:cf-distribution}\n\nTable~\\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC full S1 (245 CF violations, all pairwise; no mention triggered $\\geq$3 types).\nConflicts involving the \\textsc{Generic} type account for 63.3\\% (155/245) of all violations.\n\\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.\n\nThe pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \\textsc{Generic}$\\leftrightarrow$\\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\\%); on DocRED, the analogous catch-all type \\textsc{MISC} drives 76.6\\% of Qwen's CF violations.\nUnder unconstrained decoding, CF rates collapse to $\\leq$1\\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lr r@{}}\n\\toprule\n\\textbf{Conflicting Type Pair} & \\textbf{Count} & \\textbf{\\%} \\\\\n\\midrule\nGeneric $\\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\\\\nGeneric $\\leftrightarrow$ Material & 35 & 14.3 \\\\\nGeneric $\\leftrightarrow$ Metric & 30 & 12.2 \\\\\nMethod $\\leftrightarrow$ Task & 20 & 8.2 \\\\\nMaterial $\\leftrightarrow$ Method & 17 & 6.9 \\\\\nOtherScientificTerm $\\leftrightarrow$ Task & 12 & 4.9 \\\\\n\\midrule\n10 further pairs (each $\\leq$3.3\\%) & 46 & 18.8 \\\\\n\\midrule\n\\textbf{Total} & \\textbf{245} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF violation distribution on SciERC full S1 (Qwen3-8B, 551 documents).\nAll 245 violations are pairwise conflicts.\nConflicts involving \\textsc{Generic} account for 63.3\\%.}\n\\label{tab:cf-distribution}\n\\end{table}\n\n%%% Per-Relation DR Elimination under Fine-Tuning %%%\n% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1\n\n\\paragraph{Per-Relation DR Elimination under Fine-Tuning.}\n\\label{app:lora-per-relation}\n\nTable~\\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.\nFine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \\textsc{Evaluate-for} ($\\kappa{=}0.361$, 13.13\\%), \\textsc{Part-of} ($\\kappa{=}0.417$, 5.77\\%), and \\textsc{Compare} ($\\kappa{=}0.528$, 5.00\\%).\nAdding OntoCoDec constraints eliminates all remaining violations across all relations.\nOne \\textsc{Evaluate-for} triple (99\\,$\\to$\\,98) is redirected to \\textsc{Used-for} (634\\,$\\to$\\,635) by token-level masking: the head entity's registered type falls outside \\textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}l r rr rr@{}}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{LoRA Unconstr.}} & \\multicolumn{2}{c}{\\textbf{LoRA + S1}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(l){5-6}\n\\textbf{Relation} & $\\kappa$ & DR\\,(\\%) & $n$ & DR\\,(\\%) & $n$ \\\\\n\\midrule\nEvaluate-for & 0.361 & 13.13 & 99 & \\textbf{0} & 98 \\\\\nPart-of      & 0.417 & 5.77  & 52 & \\textbf{0} & 52 \\\\\nCompare      & 0.528 & 5.00  & 40 & \\textbf{0} & 40 \\\\\nConjunction  & 0.306 & 1.31  & 153 & \\textbf{0} & 153 \\\\\nFeature-of   & 0.278 & 1.35  & 74 & \\textbf{0} & 74 \\\\\nUsed-for     & 0.028 & 0.16  & 634 & \\textbf{0} & 635 \\\\\nHyponym-of   & 0.417 & 0     & --- & \\textbf{0} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).\n$\\kappa$: constraint tightness; $n$: predicted triple count.\nUsed-for gains one triple from Evaluate-for redirection.}\n\\label{tab:lora-per-relation}\n\\end{table}\n\n%%% Fine-Tuned Four-Way Ablation %%%\n% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*\n\n\\paragraph{Fine-Tuned Four-Way Ablation.}\n\\label{app:ft-ablation}\n\nTable~\\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrrr rr@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Model} & \\textbf{Mode} & \\textbf{DR\\,$\\downarrow$} & \\textbf{RV\\,$\\downarrow$} & \\textbf{ET\\,$\\downarrow$} & \\textbf{CF} & \\textbf{PF} & \\textbf{E-F1\\,$\\uparrow$} & \\textbf{R-F1\\,$\\uparrow$} \\\\\n\\midrule\n\\multirow{8}{*}{SciERC}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\\n  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\\n  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\\\\n  & & Full S1       & \\textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\\\\n  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\\\\n  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\\\\n  & & Full S1       & \\textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\\\\n\\midrule\n\\multirow{8}{*}{DocRED}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.09 & 7.11 & 82.15 & 40.86 \\\\\n  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\\\\n  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\\\\n  & & Full S1       & \\textbf{0.01} & 0.00 & 0.00 & 0.27 & 8.52 & 81.43 & 40.56 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\\\\n  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\\\\n  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\\\\n  & & Full S1       & \\textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\\times$ 2 datasets).\nDR/RV/ET/CF: violation rates (\\%); PF: parse failure rate (\\%); F1 $\\times$100.\nGrammar layer is a no-op post-fine-tuning (DR change $<$0.2\\,pp in all 4 settings; RV and ET already 0\\% without constraints).\nSemantic layer is the sole effective DR defense, providing 39--72\\% reduction.\nF1 cost is negligible: max $\\Delta$R-F1 = $-$0.30\\,pp (Qwen DocRED full vs.\\ unconstrained).}\n\\label{tab:ft-ablation}\n\\end{table}\n\nThe grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\\% without constraints, and grammar-only DR change is $<$0.2\\,pp (4/4 settings).\nThe semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\\% across all settings (SciERC: Qwen $-$69\\%, Llama $-$41\\%; DocRED: Qwen $-$72\\%, Llama $-$39\\%).\nAdding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.21\\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.\nF1 cost is negligible: the maximum R-F1 decrease across all 16 model$\\times$dataset$\\times$mode combinations is $-$0.30\\,pp (Qwen DocRED, full vs.\\ unconstrained), attributable to parse failure increase (7.11\\%\\,$\\to$\\,8.52\\%) rather than constraint-induced extraction degradation.\n\n%%% Residual DR Error Analysis (Fine-Tuned) %%%\n% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*\n\n\\paragraph{Residual DR Error Analysis.}\n\\label{app:residual-dr-analysis}\n\nAcross all fine-tuned settings (2 models $\\times$ 2 datasets $\\times$ full S1), only 36 domain/range violations remain.\nManual inspection reveals four root causes:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\emph{Entity type errors} (39\\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \\textsc{LOC} when the gold standard requires \\textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.\n\\item \\emph{Schema coverage gaps} (33\\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.\n\\item \\emph{Incorrect relation selection} (17\\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.\n\\item \\emph{Direction reversal} (11\\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.\n\\end{enumerate}\n\nTwo dataset-specific patterns emerge.\nOutside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.\nOn DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\\%), with entity type errors as the dominant cause (14/33, 42\\%).\nThis asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.\nThe implication is twofold: (i)~the irreducible floor from schema gaps is small ($\\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.\n\n%%% Post-Hoc Filtering Comparison (Extended) %%%\n% exp_ids: posthoc_*_zs, posthoc_*_ft\n\n\\paragraph{Post-Hoc Filtering: Extended Comparison.}\n\\label{app:posthoc-extended}\n\nTable~\\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrr l@{}}\n\\toprule\n\\textbf{Setting} & \\textbf{Model} & \\textbf{Dataset} & \\textbf{Reject\\%} & \\textbf{R-F1$_{\\text{ph}}$} & \\textbf{R-F1$_{\\text{cd}}$} & \\textbf{Winner} \\\\\n\\midrule\n\\multirow{6}{*}{ZS}\n  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\\\\n  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\\\\n  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\\\\n  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\\\\n  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\\\\n  & Mistral & DocRED & \\textbf{73.7} & 3.85  & \\textbf{5.52} & cd \\\\\n\\midrule\n\\multirow{4}{*}{FT}\n  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\\\\n  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\\\\n  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\\\\n  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Post-hoc filtering (ph) vs.\\ constrained decoding (cd).\nIn zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.\nAt reject rate $>$70\\% (Mistral DocRED), post-hoc F1 collapses below constrained.\nUnder fine-tuning, rejection rates drop to 0.6--2.0\\% and the two strategies are equivalent ($\\Delta \\leq 0.55$\\,pp; each wins two groups).\nF1 $\\times$100.}\n\\label{tab:posthoc-extended}\n\\end{table}\n\nThe crossover point occurs when post-hoc rejection exceeds $\\sim$70\\%: Mistral DocRED rejects 73.7\\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\\,pp).\nOntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.\nUnder fine-tuning, both strategies converge because few violations remain to filter or constrain ($\\Delta \\leq 0.55$\\,pp across all four FT groups, with each strategy winning two).\n\n%%% Zero-Shot Runtime Profiling %%%\n\n\\paragraph{Zero-Shot Runtime Profiling.}\n\\label{app:runtime}\n\nOn SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\\,s/doc and Full S1 constrained decoding averages 4.710\\,s/doc ($+$13.1\\% overhead).\nOn DocRED (same configuration), unconstrained inference averages 19.34\\,s/doc and Full S1 averages 19.81\\,s/doc ($+$2.43\\% overhead).\nThe lower relative overhead on DocRED reflects amortization: the fixed per-token constraint cost is spread over longer generation sequences.\nXGrammar automaton compilation takes 0.044\\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\\,s on SciERC (Table~\\ref{tab:scalability}), amortized to zero over the evaluation set.\n\n% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified\n\\paragraph{Fine-Tuned Latency Profiling.}\n\\label{app:ft-latency}\nUnder LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\\,s/doc and Full S1 constrained decoding averages 2.873\\,s/doc ($+$10.0\\% overhead, $n{=}551$).\nFine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\\,s vs.\\ 4.163\\,s/doc unconstrained); absolute generation time drops by 37\\%.\nThe relative overhead ($+$10.0\\%) is slightly lower than zero-shot ($+$13.1\\%), consistent with shorter sequences requiring fewer constraint checks per document.\n\n%%% Fuzzy Relation Matching %%%\n\n\\paragraph{Relation Matching Protocol.}\n\\label{app:fuzzy-matching}\nRelation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\\ spaces, abbreviations).\nA predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\\% \\emph{and} edit distance $\\leq 2$.\nThis protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\\_of\\_government'' for ``head of government'').\nOn Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\\,pp R-F1; strict R-F1\\,=\\,3.50\\% vs.\\ fuzzy 4.34\\%).\nFor Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).\nAll F1 figures in the main text use fuzzy normalization consistently across all models and conditions.\n\n%%% Per-Relation Violation Landscape %%%\n\n\\paragraph{Per-Relation Violation Landscape.}\n\\label{app:per-relation-landscape}\n\nTable~\\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.\nFigure~\\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Violation rates (\\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}\n\\label{tab:prompt_comparison}\n\\begin{tabular}{ll cccc}\n\\toprule\nDataset & Prompt & DR$\\downarrow$ & RV$\\downarrow$ & ET$\\downarrow$ & CF$\\downarrow$ \\\\\n\\midrule\n\\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\\\\n & Schema-informed & 5.8 & 0.3 & \\textbf{0.0} & --- \\\\\n\\midrule\n\\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\\\\n & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_per_relation_dr.pdf}\n\\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\\kappa(r)$.}\n\\label{fig:per_relation_dr}\n\\end{figure}\n\n%%% WikiEvents Extended %%%\n\n\\paragraph{WikiEvents Dataset Details.}\n\\label{app:wikievents}\nWikiEvents~\\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.\nIt defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\\_type, role)$\\to$allowed\\_entity\\_types constraints.\nThe grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.\n\n\\paragraph{Constraint Tightness in WikiEvents.}\n\\label{app:wikievents-kappa}\n% Data source: artifacts/w1c_wikievents_kappa_results.md\nWikiEvents role-level tightness (Eq.~\\ref{eq:tightness}, with $|\\mathcal{E}|{=}27$) has mean $\\bar{\\kappa}{=}0.82$ and median 0.89; 84\\% of roles have $\\kappa \\geq 0.80$ (4 or fewer valid entity types out of 27).\nThe tightness-violation pattern extends to event extraction: roles with $\\kappa \\geq 0.90$ exhibit the highest AC rate (50\\%), compared to 21\\% for medium-tightness ($0.80 \\leq \\kappa < 0.90$) and 30\\% for loose ($\\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.\nHowever, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\\to$VEH) show 0\\% AC despite $\\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\\to$CRM, Sentence$\\to$SEN) show near-100\\% AC because LLMs default to common types (PER, ORG).\nThe loose group's elevated rate (30\\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\\% AC, $\\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.\n",
    "structuredPatch": [
      {
        "oldStart": 326,
        "oldLines": 7,
        "newStart": 326,
        "newLines": 7,
        "lines": [
          "   & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\\\",
          "   & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\\\",
          "   & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\\\",
          "-  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\\\",
          "+  & Llama   & DocRED & 0.64 & 43.92 & 43.78 & cd \\\\",
          " \\bottomrule",
          " \\end{tabular}}%",
          " \\caption{Post-hoc filtering (ph) vs.\\ constrained decoding (cd)."
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

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_01F4QAMT87ovguVQNx2JcEpS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
  "old_string": "residual narrows to 0.01--0.20\\%",
  "new_string": "residual narrows to 0.01--0.21\\%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "bb23c318-6680-4fed-83dd-9336659b9e62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJydBNEEAPssnBuBpAY44v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 47840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 61 · 2026-05-20T11:16:22.571Z_

<details><summary>↩ Tool result · `toolu_01F4QAMT87ovguVQNx2JcEpS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "cb677397-47a5-44b0-888b-cd03844256e4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
    "oldString": "residual narrows to 0.01--0.20\\%",
    "newString": "residual narrows to 0.01--0.21\\%",
    "originalFile": "% Section 5 — DocRED Results (compressed, 1450→~600 words)\n% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,\n%          phase2_docred_semantic_only, phase2_docred_full_s1\n% All numbers verified against registry 2026-05-14.\n\n\\subsection{Cross-Dataset Validation on DocRED}\n\\label{sec:docred-results}\n\nTable~\\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).\n\n% ──────────────────────────────────────────\n%  Table: DocRED four-way ablation\n% ──────────────────────────────────────────\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 18.46 & ---\n  & 29.66 & 2.48\n  & 0.10  & 18.56\n  & 7.74  & 58.15 \\\\\nGrammar\n  & 26.17 & $\\uparrow$42\\%\n  & \\textbf{0.03} & \\textbf{0}\n  & 0.07  & 26.24\n  & \\textbf{8.31}  & \\textbf{59.38} \\\\\nSemantic\n  & 13.84 & $\\downarrow$25\\%\n  & 29.87 & 4.22\n  & 1.05  & 14.89\n  & 7.70  & 57.81 \\\\\nFull (S1)\n  & \\textbf{10.21} & $\\downarrow$\\textbf{45\\%}\n  & \\textbf{0.03} & \\textbf{0}\n  & 2.57  & \\textbf{12.78}\n  & 8.23  & 59.37 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained.\nTot.\\ = DR + CF (total type-violation burden).\nBest per column in \\textbf{bold} (CF excluded; Tot.\\ included).\nF1 $\\times$100. Bootstrap significance: R-F1 $+$0.50\\,pp ($p < 0.001$).\nGrammar-only $\\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see text).}\n\\label{tab:docred-ablation}\n\\end{table}\n\n% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1\n\\paragraph{Zero-shot diagnostic.}\nFull S1 reduces DR from 18.46\\% to 10.21\\% ($\\downarrow$45\\%), eliminates ET ($\\to$\\,0\\%), and near-eliminates RV (29.66\\%\\,$\\to$\\,0.03\\%).\\footnote{The residual 0.03\\% RV traces to a rare XGrammar automaton edge case where subword tokens from different enum entries combine into chimeric values (e.g., \\texttt{member} + \\texttt{icipant\\_of} from \\texttt{member\\_of} and \\texttt{participant\\_of}). This is not a fundamental limitation of the approach.}\nR-F1 improves from 7.74 to 8.23 ($+$0.50\\,pp; $p < 0.001$), attributable to elimination of 5{,}189 OOV relation predictions.\nCF increases modestly (0.10\\%\\,$\\to$\\,2.57\\%), consistent with the CF$\\leftrightarrow$DR trade-off (\\S\\ref{sec:discussion}).\n\n% exp_ids: phase2_docred_grammar_only, phase2_docred_semantic_only, phase2_docred_full_s1\n\\paragraph{Layer contributions.}\nGrammar-only eliminates RV and ET but \\emph{increases} DR to 26.17\\%: OOV triples (29.66\\% baseline) become evaluable and expose latent type incompatibilities.\\footnote{The grammar-only DR increase reflects constraint-altered generation trajectories in long documents, where vocabulary restriction shifts token probabilities away from natural but type-violating sequences.}\nSemantic-only reduces DR by 25\\% but cannot eliminate RV or ET, the same enabling dependency observed on SciERC.\nResidual DR (10.21\\% vs.\\ SciERC's 0.93\\%) reflects higher tightness ($\\bar{\\kappa}{=}0.842$ vs.\\ 0.333), which forces frequent fallback; effective semantic coverage is $\\sim$90\\% (Appendix~\\ref{app:fallback-coverage}).\nUnder fine-tuning, residual narrows to 0.01--0.20\\% (Table~\\ref{tab:composability}).\nThe increase in Llama parse failures under constraints (6.8\\%\\,$\\to$\\,9.1\\%) reflects an inherent trade-off: constraint masking alters token probability distributions, which can push generation toward suboptimal paths in long documents.\n",
    "structuredPatch": [
      {
        "oldStart": 68,
        "oldLines": 5,
        "newStart": 68,
        "newLines": 5,
        "lines": [
          " Grammar-only eliminates RV and ET but \\emph{increases} DR to 26.17\\%: OOV triples (29.66\\% baseline) become evaluable and expose latent type incompatibilities.\\footnote{The grammar-only DR increase reflects constraint-altered generation trajectories in long documents, where vocabulary restriction shifts token probabilities away from natural but type-violating sequences.}",
          " Semantic-only reduces DR by 25\\% but cannot eliminate RV or ET, the same enabling dependency observed on SciERC.",
          " Residual DR (10.21\\% vs.\\ SciERC's 0.93\\%) reflects higher tightness ($\\bar{\\kappa}{=}0.842$ vs.\\ 0.333), which forces frequent fallback; effective semantic coverage is $\\sim$90\\% (Appendix~\\ref{app:fallback-coverage}).",
          "-Under fine-tuning, residual narrows to 0.01--0.20\\% (Table~\\ref{tab:composability}).",
          "+Under fine-tuning, residual narrows to 0.01--0.21\\% (Table~\\ref{tab:composability}).",
          " The increase in Llama parse failures under constraints (6.8\\%\\,$\\to$\\,9.1\\%) reflects an inherent trade-off: constraint masking alters token probability distributions, which can push generation toward suboptimal paths in long documents."
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

_source line 62_

<details open><summary>🔧 Tool call — Edit · `toolu_01CyQRa61cQpjjUpQvJ45SEz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
  "old_string": "DR\\,0.01--0.20\\%",
  "new_string": "DR\\,0.01--0.21\\%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "e3ac6251-b9e6-4b06-a24d-55b2b67a0178",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJydBNEEAPssnBuBpAY44v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 47840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 63 · 2026-05-20T11:16:22.643Z_

<details><summary>↩ Tool result · `toolu_01CyQRa61cQpjjUpQvJ45SEz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "8bfac01c-8561-4b05-932c-c6da090d187c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
    "oldString": "DR\\,0.01--0.20\\%",
    "newString": "DR\\,0.01--0.21\\%",
    "originalFile": "% Section: Constraint Composition (compressed, 787→~500 words)\n\nAt each decoding step $t$, let $G(t) \\subseteq V$ and $S(t) \\subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.\nThe final mask is their conjunction:\n%\n\\begin{equation}\\label{eq:composition}\n  M_{\\text{final}}(t) = M_{\\text{grammar}}(t) \\;\\wedge\\; M_{\\text{semantic}}(t),\n\\end{equation}\n%\nso a token is allowed only if it satisfies \\emph{both} structural and type-level constraints.\nThe conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\\S\\ref{sec:method}): the semantic layer requires the relation type to belong to $\\mathcal{R}$, a property guaranteed only by the grammar layer.\n\n\\paragraph{Grammar-First Fallback.}\nWhen $S(t) \\cap G(t) = \\emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\\\"{\\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.\nWe enforce a \\emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.\nStructural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.\nAmong type violations, DR and CF differ in severity: a DR violation renders the triple ontologically invalid (the entity type lies outside the relation's domain or range), whereas a CF violation means each triple is individually schema-valid but the same entity receives different type assignments across triples.\n\n\\paragraph{Constraint Tightness.}\nRecall the tightness of relation $r$ (\\S\\ref{sec:bg:ontology}):\\footnote{For symmetric relations, $|\\sigma(r)|$ counts ordered pairs; the normalization $|\\mathcal{E}|^2$ remains appropriate since we evaluate on directed triples.}\n%\n\\begin{equation}\\label{eq:tightness}\n  \\kappa(r) = 1 - \\frac{|\\sigma(r)|}{|\\mathcal{E}|^2},\n\\end{equation}\n%\nThe mean tightness $\\bar{\\kappa} = \\frac{1}{|\\mathcal{R}|}\\sum_{r} \\kappa(r)$ characterizes schema restrictiveness.\nTighter constraints eliminate more grammar-valid tokens at type-bearing positions; fallback frequency and residual DR increase accordingly.\nThis dual-factor pattern (tightness $\\times$ baseline violation rate; $n{=}4$ model--dataset pairs, descriptive) aligns with the cross-dataset results: SciERC ($\\bar{\\kappa}{=}0.333$) achieves 94--99\\% DR reduction vs.\\ DocRED ($\\bar{\\kappa}{=}0.842$) at 45--90\\%; the full range across three models is 42--99\\% (\\S\\ref{sec:cross-model}; Appendix~\\ref{app:dual-factor}).\nThe pattern extends to WikiEvents EE ($\\bar{\\kappa}{=}0.82$; Appendix~\\ref{app:wikievents-kappa}).\nHowever, $\\kappa$ is necessary but not sufficient for high violation rates: per-relation analysis shows that high-$\\kappa$ relations with unambiguous entity types (\\textsc{place\\_of\\_birth}, $\\kappa{=}0.92$, DR${=}$0\\%) have zero violations, while relations with comparable $\\kappa$ but confusable types (\\textsc{basin\\_country}, $\\kappa{=}0.97$, DR${=}$74.6\\%) are highly vulnerable (Appendix~\\ref{app:kappa-case-study}).\n$\\bar{\\kappa}$ provides deployment guidance: schemas with $\\bar{\\kappa} < 0.5$ achieve near-complete DR elimination under zero-shot S1 (94--99\\% reduction); schemas with $\\bar{\\kappa} > 0.8$ require fine-tuning to narrow the fallback regime (DR\\,0.01--0.20\\%).\n$\\bar{\\kappa}$ also determines post-hoc resolution feasibility: low-$\\bar{\\kappa}$ schemas ($<$0.5) benefit from TCR with negligible DR regression ($\\leq$0.28\\,pp), while high-$\\bar{\\kappa}$ schemas ($>$0.8) suffer harmful DR increases (up to $+$9.38\\,pp; Appendix~\\ref{app:tcr}).\n\n\\paragraph{Non-Rectangularity and Sequential Masking.}\n\\label{sec:rectangularity}\n% Data source: artifacts/rebuttal/w2_rectangularity_report.md\nSequential masking is necessary because ontology type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED relations satisfy $\\sigma(r) = \\operatorname{dom}(r) \\times \\operatorname{range}(r)$); independent enforcement would admit 33--37\\% spurious pairs.\n\n\\paragraph{Composability with fine-tuning.}\nFine-tuning narrows the fallback regime: DR drops to $\\leq$\\,0.20\\% and CF to $\\leq$\\,1.18\\%, with R-F1 within $\\pm$0.6\\,pp; the grammar layer becomes a no-op and the semantic layer alone reduces residual DR by 39--72\\% (\\S\\ref{sec:composability}).\n",
    "structuredPatch": [
      {
        "oldStart": 28,
        "oldLines": 7,
        "newStart": 28,
        "newLines": 7,
        "lines": [
          " This dual-factor pattern (tightness $\\times$ baseline violation rate; $n{=}4$ model--dataset pairs, descriptive) aligns with the cross-dataset results: SciERC ($\\bar{\\kappa}{=}0.333$) achieves 94--99\\% DR reduction vs.\\ DocRED ($\\bar{\\kappa}{=}0.842$) at 45--90\\%; the full range across three models is 42--99\\% (\\S\\ref{sec:cross-model}; Appendix~\\ref{app:dual-factor}).",
          " The pattern extends to WikiEvents EE ($\\bar{\\kappa}{=}0.82$; Appendix~\\ref{app:wikievents-kappa}).",
          " However, $\\kappa$ is necessary but not sufficient for high violation rates: per-relation analysis shows that high-$\\kappa$ relations with unambiguous entity types (\\textsc{place\\_of\\_birth}, $\\kappa{=}0.92$, DR${=}$0\\%) have zero violations, while relations with comparable $\\kappa$ but confusable types (\\textsc{basin\\_country}, $\\kappa{=}0.97$, DR${=}$74.6\\%) are highly vulnerable (Appendix~\\ref{app:kappa-case-study}).",
          "-$\\bar{\\kappa}$ provides deployment guidance: schemas with $\\bar{\\kappa} < 0.5$ achieve near-complete DR elimination under zero-shot S1 (94--99\\% reduction); schemas with $\\bar{\\kappa} > 0.8$ require fine-tuning to narrow the fallback regime (DR\\,0.01--0.20\\%).",
          "+$\\bar{\\kappa}$ provides deployment guidance: schemas with $\\bar{\\kappa} < 0.5$ achieve near-complete DR elimination under zero-shot S1 (94--99\\% reduction); schemas with $\\bar{\\kappa} > 0.8$ require fine-tuning to narrow the fallback regime (DR\\,0.01--0.21\\%).",
          " $\\bar{\\kappa}$ also determines post-hoc resolution feasibility: low-$\\bar{\\kappa}$ schemas ($<$0.5) benefit from TCR with negligible DR regression ($\\leq$0.28\\,pp), while high-$\\bar{\\kappa}$ schemas ($>$0.8) suffer harmful DR increases (up to $+$9.38\\,pp; Appendix~\\ref{app:tcr}).",
          " ",
          " \\paragraph{Non-Rectangularity and Sequential Masking.}"
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

_source line 64_

<details open><summary>🔧 Tool call — Edit · `toolu_01X7c9zqZMtjGMdynfkdPB8Q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
  "old_string": "DR drops to $\\leq$\\,0.20\\%",
  "new_string": "DR drops to $\\leq$\\,0.21\\%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "cfabbfce-96f9-4ff8-891e-4c8b8c30a583",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJydBNEEAPssnBuBpAY44v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 47840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 65 · 2026-05-20T11:16:22.716Z_

<details><summary>↩ Tool result · `toolu_01X7c9zqZMtjGMdynfkdPB8Q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "24aaec12-d064-4a59-bc08-a2bc5e696786",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
    "oldString": "DR drops to $\\leq$\\,0.20\\%",
    "newString": "DR drops to $\\leq$\\,0.21\\%",
    "originalFile": "% Section: Constraint Composition (compressed, 787→~500 words)\n\nAt each decoding step $t$, let $G(t) \\subseteq V$ and $S(t) \\subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.\nThe final mask is their conjunction:\n%\n\\begin{equation}\\label{eq:composition}\n  M_{\\text{final}}(t) = M_{\\text{grammar}}(t) \\;\\wedge\\; M_{\\text{semantic}}(t),\n\\end{equation}\n%\nso a token is allowed only if it satisfies \\emph{both} structural and type-level constraints.\nThe conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\\S\\ref{sec:method}): the semantic layer requires the relation type to belong to $\\mathcal{R}$, a property guaranteed only by the grammar layer.\n\n\\paragraph{Grammar-First Fallback.}\nWhen $S(t) \\cap G(t) = \\emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\\\"{\\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.\nWe enforce a \\emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.\nStructural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.\nAmong type violations, DR and CF differ in severity: a DR violation renders the triple ontologically invalid (the entity type lies outside the relation's domain or range), whereas a CF violation means each triple is individually schema-valid but the same entity receives different type assignments across triples.\n\n\\paragraph{Constraint Tightness.}\nRecall the tightness of relation $r$ (\\S\\ref{sec:bg:ontology}):\\footnote{For symmetric relations, $|\\sigma(r)|$ counts ordered pairs; the normalization $|\\mathcal{E}|^2$ remains appropriate since we evaluate on directed triples.}\n%\n\\begin{equation}\\label{eq:tightness}\n  \\kappa(r) = 1 - \\frac{|\\sigma(r)|}{|\\mathcal{E}|^2},\n\\end{equation}\n%\nThe mean tightness $\\bar{\\kappa} = \\frac{1}{|\\mathcal{R}|}\\sum_{r} \\kappa(r)$ characterizes schema restrictiveness.\nTighter constraints eliminate more grammar-valid tokens at type-bearing positions; fallback frequency and residual DR increase accordingly.\nThis dual-factor pattern (tightness $\\times$ baseline violation rate; $n{=}4$ model--dataset pairs, descriptive) aligns with the cross-dataset results: SciERC ($\\bar{\\kappa}{=}0.333$) achieves 94--99\\% DR reduction vs.\\ DocRED ($\\bar{\\kappa}{=}0.842$) at 45--90\\%; the full range across three models is 42--99\\% (\\S\\ref{sec:cross-model}; Appendix~\\ref{app:dual-factor}).\nThe pattern extends to WikiEvents EE ($\\bar{\\kappa}{=}0.82$; Appendix~\\ref{app:wikievents-kappa}).\nHowever, $\\kappa$ is necessary but not sufficient for high violation rates: per-relation analysis shows that high-$\\kappa$ relations with unambiguous entity types (\\textsc{place\\_of\\_birth}, $\\kappa{=}0.92$, DR${=}$0\\%) have zero violations, while relations with comparable $\\kappa$ but confusable types (\\textsc{basin\\_country}, $\\kappa{=}0.97$, DR${=}$74.6\\%) are highly vulnerable (Appendix~\\ref{app:kappa-case-study}).\n$\\bar{\\kappa}$ provides deployment guidance: schemas with $\\bar{\\kappa} < 0.5$ achieve near-complete DR elimination under zero-shot S1 (94--99\\% reduction); schemas with $\\bar{\\kappa} > 0.8$ require fine-tuning to narrow the fallback regime (DR\\,0.01--0.21\\%).\n$\\bar{\\kappa}$ also determines post-hoc resolution feasibility: low-$\\bar{\\kappa}$ schemas ($<$0.5) benefit from TCR with negligible DR regression ($\\leq$0.28\\,pp), while high-$\\bar{\\kappa}$ schemas ($>$0.8) suffer harmful DR increases (up to $+$9.38\\,pp; Appendix~\\ref{app:tcr}).\n\n\\paragraph{Non-Rectangularity and Sequential Masking.}\n\\label{sec:rectangularity}\n% Data source: artifacts/rebuttal/w2_rectangularity_report.md\nSequential masking is necessary because ontology type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED relations satisfy $\\sigma(r) = \\operatorname{dom}(r) \\times \\operatorname{range}(r)$); independent enforcement would admit 33--37\\% spurious pairs.\n\n\\paragraph{Composability with fine-tuning.}\nFine-tuning narrows the fallback regime: DR drops to $\\leq$\\,0.20\\% and CF to $\\leq$\\,1.18\\%, with R-F1 within $\\pm$0.6\\,pp; the grammar layer becomes a no-op and the semantic layer alone reduces residual DR by 39--72\\% (\\S\\ref{sec:composability}).\n",
    "structuredPatch": [
      {
        "oldStart": 37,
        "oldLines": 4,
        "newStart": 37,
        "newLines": 4,
        "lines": [
          " Sequential masking is necessary because ontology type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED relations satisfy $\\sigma(r) = \\operatorname{dom}(r) \\times \\operatorname{range}(r)$); independent enforcement would admit 33--37\\% spurious pairs.",
          " ",
          " \\paragraph{Composability with fine-tuning.}",
          "-Fine-tuning narrows the fallback regime: DR drops to $\\leq$\\,0.20\\% and CF to $\\leq$\\,1.18\\%, with R-F1 within $\\pm$0.6\\,pp; the grammar layer becomes a no-op and the semantic layer alone reduces residual DR by 39--72\\% (\\S\\ref{sec:composability}).",
          "+Fine-tuning narrows the fallback regime: DR drops to $\\leq$\\,0.21\\% and CF to $\\leq$\\,1.18\\%, with R-F1 within $\\pm$0.6\\,pp; the grammar layer becomes a no-op and the semantic layer alone reduces residual DR by 39--72\\% (\\S\\ref{sec:composability})."
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

_source line 66_

<details open><summary>🔧 Tool call — Edit · `toolu_01XG1R92Nq313v5Ne4BW5nzp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "old_string": "DR\\,$\\leq$\\,0.20\\%, R-F1 within $\\pm$0.6\\,pp",
  "new_string": "DR\\,$\\leq$\\,0.21\\%, R-F1 within $\\pm$0.6\\,pp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "73cd0dfc-730b-4a39-8e3b-257d6cf5c6b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJydBNEEAPssnBuBpAY44v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 47840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 67 · 2026-05-20T11:16:24.528Z_

<details><summary>↩ Tool result · `toolu_01XG1R92Nq313v5Ne4BW5nzp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "40d9983f-c396-4c6d-8e86-6ec0e9891e4b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "oldString": "DR\\,$\\leq$\\,0.20\\%, R-F1 within $\\pm$0.6\\,pp",
    "newString": "DR\\,$\\leq$\\,0.21\\%, R-F1 within $\\pm$0.6\\,pp",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage[table]{xcolor}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{enumitem}\n\\usepackage{pifont}\n\\newcommand{\\TBD}[1]{\\textcolor{red}{#1}}\n\n\\title{OntoCoDec: Type-Constrained Information Extraction\\\\via Compiled Schema Constraints}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\input{abstract}\n\n% === §1 Introduction ===\n\\input{section1_introduction_draft}\n\n% === §2 Background ===\n\\input{section2_background}\n\n% === §3 Method ===\n\\input{section3_method_draft}\n\n% === §4 Constraint Composition ===\n\\section{Constraint Composition}\n\\label{sec:composition}\n\\input{section4_composition_draft}\n\n% === §5 Experiments ===\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\input{section3_violation_landscape}\n\n\\input{section5_scierc_draft}\n\\input{section5_docred_draft}\n\\input{section5_crossmodel_draft}\n\\input{section5_wikievents_draft}\n\\input{section5_runtime}\n\n% === §6 Related Work ===\n\\input{section6_related_work}\n\n% === §7 Discussion and Conclusion ===\n\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\\input{section7_conclusion_compressed}\n\n% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===\n\\clearpage\n\\section*{Limitations}\n\n\\paragraph{Constraint scope.}\nCF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\\%\\,$\\to$\\,1.27\\%) by constraining type assignments to schema-valid values.\nCF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\\,pp). CF$\\leftrightarrow$DR thus represents a fundamental trade-off in composable constraint systems rather than an independently resolvable limitation (Appendix~\\ref{app:cf-dr-tradeoff}).\nGlobal entity-level type consensus during decoding offers the most direct path to resolving CF violations.\nCF type inconsistencies may propagate to downstream tasks that consume extracted triples (e.g., knowledge graph construction, question answering); the impact of such propagation has not been evaluated.\nEntity F1 impact is model-dependent ($+$1.22\\,pp for Qwen vs.\\ $-$0.64\\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\\% vs.\\ 6.8\\%).\nResidual DR under fine-tuning (36 violations across all fine-tuned settings, both models and both datasets) decomposes into entity type errors (39\\%), schema coverage gaps (33\\%), and model generation errors correctly caught by constraints (28\\%); Llama DocRED alone accounts for 33 of 36 residual violations (92\\%), reflecting weaker entity typing (Appendix~\\ref{app:residual-dr-analysis}).\nSchema coverage gaps (one-third of residual violations) arise because RE constraints are extracted from training-data type pairs, which may not cover all valid combinations; larger training sets or manual constraint table completion can reduce this gap.\n\n\\paragraph{Evaluation coverage.}\nZero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\\% compared to $\\sim$45\\% for fine-tuned systems.\nZero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated only on 8B-class models.\nScaling to smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.\nComposability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\\,$\\leq$\\,0.20\\%, R-F1 within $\\pm$0.6\\,pp; EE: RoV$\\to$0\\%, AC$\\leq$0.8\\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\\%, Llama 0.46\\% on SciERC) traces to schema-level type ambiguity (\\textsc{Generic}$\\leftrightarrow$X) rather than enforcement failure.\nWikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).\nAll main experiments use greedy decoding; our evaluation of beam search on the full SciERC test set (551 documents) and DocRED (50 zero-shot, 998 fine-tuned documents) across three models confirms compatibility (Appendices~\\ref{app:sampling},~\\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.\n\n\\paragraph{Engineering considerations.}\nScalability benchmarks up to 200 entity types and 1,000 relations show constant 2--3\\% inference overhead and sub-second compilation ($<$0.5\\,s; Appendix~\\ref{app:scalability}); however, the first-token uniqueness requirement for continuation masking may become a tokenizer-dependent bottleneck beyond this scale.\nEvaluation covers LoRA and full fine-tuning on 8B-class models; full fine-tuning with an untuned learning rate underperforms LoRA (R-F1 37.89 vs.\\ 43.77 on SciERC) but confirms that constraints remain effective across fine-tuning methods (DR 2.74\\%\\,$\\to$\\,0\\%; Appendix~\\ref{app:full-ft}).\n\n\n% === Ethics Statement ===\n\\section*{Ethics Statement}\n\nThis work uses publicly available benchmark datasets (SciERC, DocRED, and WikiEvents) with no personally identifiable information.\nNo human subjects were involved in the experiments.\nThe constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.\nCode and data will be released upon acceptance.\n\n% === ARR Responsible NLP Research Checklist ===\n\\input{checklist}\n\n% === Bibliography ===\n\\bibliography{relwork_new_entries}\n\n% === Appendix ===\n\\appendix\n\n\\input{appendix_prompts}\n\\input{appendix_related_work}\n\\input{appendix_discussion}\n\\input{appendix_llama_per_relation}\n\\input{appendix_sampling_table}\n\\input{appendix_beam_search}\n\\input{appendix_reproducibility}\n\\input{appendix_doc_length}\n\\input{appendix_prompt_sensitivity}\n\\input{appendix_case_studies}\n\\input{appendix_scalability}\n\\input{appendix_full_ft}\n\\input{appendix_tcr}\n\\input{appendix_kappa_case_study}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 78,
        "oldLines": 7,
        "newStart": 78,
        "newLines": 7,
        "lines": [
          " Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\\% compared to $\\sim$45\\% for fine-tuned systems.",
          " Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated only on 8B-class models.",
          " Scaling to smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.",
          "-Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\\,$\\leq$\\,0.20\\%, R-F1 within $\\pm$0.6\\,pp; EE: RoV$\\to$0\\%, AC$\\leq$0.8\\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\\%, Llama 0.46\\% on SciERC) traces to schema-level type ambiguity (\\textsc{Generic}$\\leftrightarrow$X) rather than enforcement failure.",
          "+Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\\,$\\leq$\\,0.21\\%, R-F1 within $\\pm$0.6\\,pp; EE: RoV$\\to$0\\%, AC$\\leq$0.8\\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\\%, Llama 0.46\\% on SciERC) traces to schema-level type ambiguity (\\textsc{Generic}$\\leftrightarrow$X) rather than enforcement failure.",
          " WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).",
          " All main experiments use greedy decoding; our evaluation of beam search on the full SciERC test set (551 documents) and DocRED (50 zero-shot, 998 fine-tuned documents) across three models confirms compatibility (Appendices~\\ref{app:sampling},~\\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.",
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

_source line 68_

<details open><summary>🔧 Tool call — Edit · `toolu_01HXWBDB5igpzdUkYYZcd5VV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex",
  "old_string": "DR\\,$\\leq$\\,0.20\\%",
  "new_string": "DR\\,$\\leq$\\,0.21\\%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "14ed68f4-0e21-454d-8ff8-c55da970866a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJydBNEEAPssnBuBpAY44v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 47840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 69 · 2026-05-20T11:16:25.521Z_

<details><summary>↩ Tool result · `toolu_01HXWBDB5igpzdUkYYZcd5VV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "01690c80-8a36-46b8-8a5e-0858b90a9a12",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex",
    "oldString": "DR\\,$\\leq$\\,0.20\\%",
    "newString": "DR\\,$\\leq$\\,0.21\\%",
    "originalFile": "% Section 7 — Discussion and Conclusion\n% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.\n\nOntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\\times$ latency); zero-shot DR drops 76--99\\% for calibrated models.\n$\\bar{\\kappa}$ characterizes constraint regimes, with entity type confusability as the critical co-factor (Appendix~\\ref{app:kappa-case-study}); the decidability taxonomy and $\\bar{\\kappa}$ diagnostic yield a principled deployment workflow.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " % Section 7 — Discussion and Conclusion",
          " % Full discussion in Appendix; Mistral boundary condition in app:dual-factor.",
          " ",
          "-OntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\\,$\\leq$\\,0.20\\%, CF\\,$\\leq$\\,1.2\\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\\times$ latency); zero-shot DR drops 76--99\\% for calibrated models.",
          "+OntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\\,$\\leq$\\,0.21\\%, CF\\,$\\leq$\\,1.2\\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\\times$ latency); zero-shot DR drops 76--99\\% for calibrated models.",
          " $\\bar{\\kappa}$ characterizes constraint regimes, with entity type confusability as the critical co-factor (Appendix~\\ref{app:kappa-case-study}); the decidability taxonomy and $\\bar{\\kappa}$ diagnostic yield a principled deployment workflow."
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

_source line 70_

All edits done. Now compiling the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "3ceee159-dc46-479d-b67a-8504629e18f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETApkHmQF3QsYzMkzBkai7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2503,
      "cache_read_input_tokens": 48909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2503
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

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_01N8kqvZmy7G1Uge1dRDqErh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && latexmk -pdf main.tex 2>&1 | tail -30",
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
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "235d674f-5d32-43fb-8405-f12c8704d4e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETApkHmQF3QsYzMkzBkai7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2503,
      "cache_read_input_tokens": 48909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2503
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

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bx4wbjxe3",
  "tool_use_id": "toolu_01N8kqvZmy7G1Uge1dRDqErh",
  "description": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && latexmk -pdf main.tex 2>&1 | tail -30",
  "task_type": "local_bash",
  "uuid": "6636d120-7f4f-4843-bb03-0e5196426fad",
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685"
}
```

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bx4wbjxe3",
  "tool_use_id": "toolu_01N8kqvZmy7G1Uge1dRDqErh",
  "status": "completed",
  "output_file": "",
  "summary": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper && latexmk -pdf main.tex 2>&1 | tail -30",
  "uuid": "8404cc1e-1c3c-4f12-b843-d382a2f8095b",
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685"
}
```

---

### Tool result

_source line 74 · 2026-05-20T11:16:34.394Z_

<details><summary>↩ Tool result · `toolu_01N8kqvZmy7G1Uge1dRDqErh`</summary>

```text
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/
ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/zapfding/uzdr.pfb>
Output written on main.pdf (31 pages, 503393 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./relwork_new_entries.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "0a8040c9-e770-47c0-8b78-9157ebe89534",
  "tool_use_result": {
    "stdout": "lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/\nucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmri8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/zapfding/uzdr.pfb>\nOutput written on main.pdf (31 pages, 503393 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./relwork_new_entries.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_01HAW5g4i26Jw6icFPWquitq`</summary>

```json
{
  "command": "grep -c \"LaTeX Error\\|Undefined control sequence\\|undefined references\" main.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "c59c0af0-1c7a-4581-bada-81a02ec33097",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmsRrUuFQCuhivCGLeMgQo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 51412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1004
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 76 · 2026-05-20T11:16:37.455Z_

<details><summary>↩ Tool result · `toolu_01HAW5g4i26Jw6icFPWquitq`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "956ba2fe-7534-4ced-90e3-391cab8cbbb4",
  "tool_use_result": {
    "stdout": "0",
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

_source line 77_

编译成功，0 errors。验证修改后的表格内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "0cafcecd-2eb6-43fa-9629-b5cdddeaf360",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQcCV73EWtZ3i7AFKzWGTW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 85,
      "cache_read_input_tokens": 52416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 85
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

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_01ArdfwSqhR3YASGKzvDsRNM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "offset": 112,
  "limit": 37
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "2986044f-92d6-4c6f-99ff-d1fc7ceed2ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQcCV73EWtZ3i7AFKzWGTW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 85,
      "cache_read_input_tokens": 52416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 85
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

_source line 79 · 2026-05-20T11:16:44.037Z_

<details><summary>↩ Tool result · `toolu_01ArdfwSqhR3YASGKzvDsRNM`</summary>

```text
112	\begin{table}[t]
113	\centering
114	\small
115	\setlength{\tabcolsep}{3pt}
116	\resizebox{\columnwidth}{!}{%
117	\begin{tabular}{@{}lll rrrr r@{}}
118	\toprule
119	\textbf{Model} & \textbf{Dataset} & \textbf{Mode}
120	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
121	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
122	  & \textbf{$\Delta$DR} \\
123	\midrule
124	\multirow{4}{*}{Qwen3-8B}
125	  & \multirow{2}{*}{SciERC}
126	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
127	  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
128	\cmidrule(l){2-8}
129	  & \multirow{2}{*}{DocRED}
130	    & Unconstr.\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\
131	  & & Full S1    & \textbf{0.01} & 0.27 & 40.56 & 81.43 & $\downarrow$99\% \\
132	\midrule
133	\multirow{4}{*}{\shortstack[l]{Llama\\3.1-8B}}
134	  & \multirow{2}{*}{SciERC}
135	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
136	  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
137	\cmidrule(l){2-8}
138	  & \multirow{2}{*}{DocRED}
139	    & Unconstr.\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\
140	  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\downarrow$57\% \\
141	\bottomrule
142	\end{tabular}}%
143	\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
144	DR\,$\leq$\,0.21\% across both datasets with R-F1 within $\pm$0.6\,pp.
145	F1\,$\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.
146	E-F1 includes parse-failure documents (Qwen PF: 7--9\%; Llama PF: 2--3\%); excluding parse failures, E-F1 is stable for both models ($\pm$0.1\,pp).}
147	\label{tab:composability}
148	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "c6eacabb-b011-414a-945f-42eec9342c30",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrr r@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$}\n  & \\textbf{$\\Delta$DR} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen3-8B}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\\n  & & Full S1    & \\textbf{0} & 1.18 & 43.77 & 67.05 & $\\downarrow$100\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.76 & 0.09 & 40.86 & 82.15 & --- \\\\\n  & & Full S1    & \\textbf{0.01} & 0.27 & 40.56 & 81.43 & $\\downarrow$99\\% \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.11 & 0    & 45.45 & 67.76 & --- \\\\\n  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.49 & 0.08 & 43.72 & 83.93 & --- \\\\\n  & & Full S1    &  0.21 & 0.21 & 43.78 & 83.94 & $\\downarrow$57\\% \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nDR\\,$\\leq$\\,0.21\\% across both datasets with R-F1 within $\\pm$0.6\\,pp.\nF1\\,$\\times$100. Bootstrap: 10{,}000 iterations. ---: not computed.\nE-F1 includes parse-failure documents (Qwen PF: 7--9\\%; Llama PF: 2--3\\%); excluding parse failures, E-F1 is stable for both models ($\\pm$0.1\\,pp).}\n\\label{tab:composability}\n\\end{table}",
      "numLines": 37,
      "startLine": 112,
      "totalLines": 149
    }
  }
}
```

</details>

---

### Assistant

_source line 80_

Table 2 验证通过，与 eval 结果完全一致：

| | E-F1 | R-F1 | DR% | CF% |
|---|------|------|-----|-----|
| Qwen unc | 82.15 | 40.86 | 0.76 | 0.09 |
| Qwen con | 81.43 | 40.56 | 0.01 | 0.27 |
| Llama unc | 83.93 | 43.72 | 0.49 | 0.08 |
| Llama con | 83.94 | 43.78 | 0.21 | 0.21 |

## 修改汇总

### Table 2 (section5_scierc_draft.tex:139-140)
| 位置 | 旧值 | 新值 |
|------|------|------|
| Llama unc CF | `---` | `0.08` |
| Llama con DR | `0.20` | `0.21` |
| Llama con CF | `0.26` | `0.21` |
| Llama con R-F1 | `44.23` | `43.78` |
| Llama con ΔDR | `59%` | `57%` |

### 正文连带修改 (section5_scierc_draft.tex)
- L105: DR `0.20→0.21`, ΔDR `59%→57%`, R-F1变化 `+0.51pp→+0.06pp`
- L106: `59%→57%`
- L107, L109, L144: `DR≤0.20%→DR≤0.21%`

### Appendix 连带修改 (appendix_discussion.tex)
- L259: Llama DocRED unc CF `---→0.08`
- L262: DR `0.20→0.21`, CF `0.26→0.21`, R-F1 `44.23→43.78`
- L275: `DR≤0.20%→DR≤0.21%`
- L329: post-hoc表 R-F1_cd `44.23→43.78`

### 其他文件连带修改
- section5_docred_draft.tex L71: `0.01--0.20%→0.01--0.21%`
- section4_composition_draft.tex L31, L40: `0.20%→0.21%`
- main.tex L81: `DR≤0.20%→DR≤0.21%`
- section7_conclusion_compressed.tex L4: `DR≤0.20%→DR≤0.21%`

### 未修改（非 Llama DocRED con 数据）
- appendix_beam_search.tex L135 `R-F1=44.23` — Qwen SciERC beam 结果
- appendix_beam_search.tex L161 `CF=0.26` — d065 4096-context 独立实验
- appendix_tcr.tex L63 `0.21/0.20` — TCR 独立指标

编译通过，31 pages，0 errors。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "uuid": "ef78c55b-e231-4701-896a-73db997ced86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Th4my3Kq9E2TZmuQMHXRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 52501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1069
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

_source line 81_

Table 2 验证通过，与 eval 结果完全一致：

| | E-F1 | R-F1 | DR% | CF% |
|---|------|------|-----|-----|
| Qwen unc | 82.15 | 40.86 | 0.76 | 0.09 |
| Qwen con | 81.43 | 40.56 | 0.01 | 0.27 |
| Llama unc | 83.93 | 43.72 | 0.49 | 0.08 |
| Llama con | 83.94 | 43.78 | 0.21 | 0.21 |

## 修改汇总

### Table 2 (section5_scierc_draft.tex:139-140)
| 位置 | 旧值 | 新值 |
|------|------|------|
| Llama unc CF | `---` | `0.08` |
| Llama con DR | `0.20` | `0.21` |
| Llama con CF | `0.26` | `0.21` |
| Llama con R-F1 | `44.23` | `43.78` |
| Llama con ΔDR | `59%` | `57%` |

### 正文连带修改 (section5_scierc_draft.tex)
- L105: DR `0.20→0.21`, ΔDR `59%→57%`, R-F1变化 `+0.51pp→+0.06pp`
- L106: `59%→57%`
- L107, L109, L144: `DR≤0.20%→DR≤0.21%`

### Appendix 连带修改 (appendix_discussion.tex)
- L259: Llama DocRED unc CF `---→0.08`
- L262: DR `0.20→0.21`, CF `0.26→0.21`, R-F1 `44.23→43.78`
- L275: `DR≤0.20%→DR≤0.21%`
- L329: post-hoc表 R-F1_cd `44.23→43.78`

### 其他文件连带修改
- section5_docred_draft.tex L71: `0.01--0.20%→0.01--0.21%`
- section4_composition_draft.tex L31, L40: `0.20%→0.21%`
- main.tex L81: `DR≤0.20%→DR≤0.21%`
- section7_conclusion_compressed.tex L4: `DR≤0.20%→DR≤0.21%`

### 未修改（非 Llama DocRED con 数据）
- appendix_beam_search.tex L135 `R-F1=44.23` — Qwen SciERC beam 结果
- appendix_beam_search.tex L161 `CF=0.26` — d065 4096-context 独立实验
- appendix_tcr.tex L63 `0.21/0.20` — TCR 独立指标

编译通过，31 pages，0 errors。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 244219,
  "duration_api_ms": 239839,
  "num_turns": 32,
  "stop_reason": "end_turn",
  "session_id": "10d0c9c7-c52b-48b1-a067-0b8aaf432685",
  "total_cost_usd": 0.8345692500000002,
  "usage": {
    "input_tokens": 1056,
    "cache_creation_input_tokens": 41729,
    "cache_read_input_tokens": 480992,
    "output_tokens": 13053,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41729,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 835,
        "cache_read_input_tokens": 52501,
        "cache_creation_input_tokens": 1069,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1069
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1537,
      "outputTokens": 25,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0016619999999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1056,
      "outputTokens": 13053,
      "cacheReadInputTokens": 480992,
      "cacheCreationInputTokens": 41729,
      "webSearchRequests": 0,
      "costUSD": 0.8329072500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cc866ab2-101b-4eb4-9ae3-d6c0ec706ee6"
}
```

</details>

---
