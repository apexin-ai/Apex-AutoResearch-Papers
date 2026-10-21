# paper research evidence docre

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_paper_research_evidence_docre_20260517T152414.log`
- **Structured JSON:** [`d887cab7daaa881135ad.json`](../../sessions/d8/d887cab7daaa881135ad.json)

## Before a recorded user message

57 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
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
  "uuid": "1fd69bac-586f-49b3-a1d5-3c71af207c47",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
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
    "resetsAt": 1779040800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b5f1605e-c3ff-49aa-933b-77e9859d7671",
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to verify key papers in the evidence-grounded DocRE (Document-level Relation Extraction) domain and fill gaps with additional papers. I need to use WebSearch to verify paper details. Let me load the WebSearch tool first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "816473e1-b2d8-4832-af20-1f38c4118b44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiwH8H1dM7FkdeyFNMz3eB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14023,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14023
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

我来验证这些文献。先加载搜索工具，然后并行验证 DREEAM 和 SAIS。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "405e8a96-dd3d-4dd4-8486-b3417bd08c04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiwH8H1dM7FkdeyFNMz3eB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14023,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14023
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Q9sL3RPq93GJtStNQy3mnx`</summary>

```json
{
  "query": "select:WebSearch",
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
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "b3e67a2f-762b-416b-87c6-8198e117a23d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiwH8H1dM7FkdeyFNMz3eB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14023,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14023
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 7 · 2026-05-17T15:24:30.607Z_

<details><summary>↩ Tool result · `toolu_01Q9sL3RPq93GJtStNQy3mnx`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "8abfcd90-ff03-4414-bfad-b842f0f4c6d8",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 50
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for DREEAM and SAIS in parallel to verify them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "a63fa503-0e2c-404f-a3f1-35ddf91cc175",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkdEG9GEXaHeAQGxJykFUA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 25864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 709
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 9_

开始并行验证 DREEAM 和 SAIS。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "33a2192d-3645-42ce-a629-92bef5f0e2c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkdEG9GEXaHeAQGxJykFUA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 25864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 709
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XGGBvg1HUG3MepoL25YszL`</summary>

```json
{
  "query": "DREEAM \"Guiding Attention with Evidence for Improving Document-Level Relation Extraction\" site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "2cc83fab-331c-4bee-ba9a-8b87345ed981",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkdEG9GEXaHeAQGxJykFUA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 25864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 709
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SrTJbWEhgYe4XCbmQN63Jy`</summary>

```json
{
  "query": "SAIS \"Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\" site:aclanthology.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "3d0faeb4-cb9d-4cc5-bba3-7761d09306f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkdEG9GEXaHeAQGxJykFUA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 25864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 709
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 12 · 2026-05-17T15:24:38.547Z_

<details><summary>↩ Tool result · `toolu_01SrTJbWEhgYe4XCbmQN63Jy`</summary>

```text
Web search results for query: "SAIS "Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction" site:aclanthology.org"

Links: [{"title":"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.171/"}]

Perfect! I found the paper. Here are the results:

**SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction** by Yuxin Xiao, Zecheng Zhang, Yuning Mao, Carl Yang, and Jiawei Han was published in 2022 in the Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL).

The paper proposes to explicitly teach the model to capture relevant contexts and entity types by supervising and augmenting intermediate steps (SAIS) for relation extraction, which not only extracts relations of better quality due to more effective supervision, but also retrieves the corresponding supporting evidence more accurately. By assessing model uncertainty, SAIS further boosts the performance via evidence-based data augmentation and ensemble inference while reducing the computational cost.

The full paper is available at: https://aclanthology.org/2022.naacl-main.171/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "48993aaa-688e-4226-ac72-1380b92ca4c4",
  "tool_use_result": {
    "query": "SAIS \"Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\" site:aclanthology.org",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y5TwadLVBHe9McJmdK7D6J",
        "content": [
          {
            "title": "SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction - ACL Anthology",
            "url": "https://aclanthology.org/2022.naacl-main.171/"
          }
        ]
      },
      "Perfect! I found the paper. Here are the results:\n\n**SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction** by Yuxin Xiao, Zecheng Zhang, Yuning Mao, Carl Yang, and Jiawei Han was published in 2022 in the Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL).\n\nThe paper proposes to explicitly teach the model to capture relevant contexts and entity types by supervising and augmenting intermediate steps (SAIS) for relation extraction, which not only extracts relations of better quality due to more effective supervision, but also retrieves the corresponding supporting evidence more accurately. By assessing model uncertainty, SAIS further boosts the performance via evidence-based data augmentation and ensemble inference while reducing the computational cost.\n\nThe full paper is available at: https://aclanthology.org/2022.naacl-main.171/"
    ],
    "durationSeconds": 3.1774426590000004
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T15:24:39.775Z_

<details><summary>↩ Tool result · `toolu_01XGGBvg1HUG3MepoL25YszL`</summary>

```text
Web search results for query: "DREEAM "Guiding Attention with Evidence for Improving Document-Level Relation Extraction" site:arxiv.org"

Links: [{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://arxiv.org/abs/2302.08675"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/html/2407.21384v1"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757v2"},{"title":"TTM-RE: Memory-Augmented Document-Level Relation Extraction","url":"https://arxiv.org/html/2406.05906v1"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v1"},{"title":"A LayoutLMv3-Based Model for Enhanced Relation Extraction in Visually-Rich Documents","url":"https://arxiv.org/html/2404.10848v1"},{"title":"Building a Japanese Document-Level Relation Extraction Dataset Assisted by Cross-Lingual Transfer","url":"https://arxiv.org/html/2404.16506"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"WISTERIA: Weak Implicit Signal-based Temporal Relation Extraction with Attention","url":"https://arxiv.org/html/2603.23319"},{"title":"Augmenting Document-level Relation Extraction with Efficient Multi-Supervision","url":"https://arxiv.org/html/2407.01026v1"}]

I found the paper! Here are the search results for DREEAM:

DREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal, thereby guiding the attention modules of the DocRE system to assign high weights to evidence.

The paper is titled "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction" by Youmi Ma and 2 other authors.

**Key Details:**
- **Paper ID:** arXiv:2302.08675
- **Direct Link:** https://arxiv.org/abs/2302.08675
- **Published:** February 17, 2023

The paper addresses how evidence (defined as sentences containing clues for the relationship between an entity pair) helps DocRE systems focus on relevant texts to improve relation extraction, while tackling two major issues: high memory consumption and limited availability of annotations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "bb82a9a9-7cbf-4317-b8aa-9a7987854a36",
  "tool_use_result": {
    "query": "DREEAM \"Guiding Attention with Evidence for Improving Document-Level Relation Extraction\" site:arxiv.org",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BzATtEefnwaZFGHWfxwwgL",
        "content": [
          {
            "title": "[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction",
            "url": "https://arxiv.org/abs/2302.08675"
          },
          {
            "title": "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2407.21384v1"
          },
          {
            "title": "GLiDRE: Generalist Lightweight model for Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2508.00757v2"
          },
          {
            "title": "TTM-RE: Memory-Augmented Document-Level Relation Extraction",
            "url": "https://arxiv.org/html/2406.05906v1"
          },
          {
            "title": "LLM with Relation Classifier for Document-Level Relation Extraction",
            "url": "https://arxiv.org/html/2408.13889v1"
          },
          {
            "title": "A LayoutLMv3-Based Model for Enhanced Relation Extraction in Visually-Rich Documents",
            "url": "https://arxiv.org/html/2404.10848v1"
          },
          {
            "title": "Building a Japanese Document-Level Relation Extraction Dataset Assisted by Cross-Lingual Transfer",
            "url": "https://arxiv.org/html/2404.16506"
          },
          {
            "title": "CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2504.06529"
          },
          {
            "title": "WISTERIA: Weak Implicit Signal-based Temporal Relation Extraction with Attention",
            "url": "https://arxiv.org/html/2603.23319"
          },
          {
            "title": "Augmenting Document-level Relation Extraction with Efficient Multi-Supervision",
            "url": "https://arxiv.org/html/2407.01026v1"
          }
        ]
      },
      "I found the paper! Here are the search results for DREEAM:\n\nDREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal, thereby guiding the attention modules of the DocRE system to assign high weights to evidence.\n\nThe paper is titled \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\" by Youmi Ma and 2 other authors.\n\n**Key Details:**\n- **Paper ID:** arXiv:2302.08675\n- **Direct Link:** https://arxiv.org/abs/2302.08675\n- **Published:** February 17, 2023\n\nThe paper addresses how evidence (defined as sentences containing clues for the relationship between an entity pair) helps DocRE systems focus on relevant texts to improve relation extraction, while tackling two major issues: high memory consumption and limited availability of annotations."
    ],
    "durationSeconds": 4.937084086999997
  }
}
```

</details>

---

### Assistant

_source line 14_

DREEAM 和 SAIS 均已确认。现在搜索更多细节并验证 gap-fill 候选论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "155c38ad-3f00-4a8d-8dc9-e0cd95c055c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dtmpJDb8hv6HugJ6hfgpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 378,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 26573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JobmUMY3o6wEJEF58569g6`</summary>

```json
{
  "query": "DREEAM \"Youmi Ma\" EACL 2023 document relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "aa905d24-4709-45d3-a1f5-e7e3773ccada",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dtmpJDb8hv6HugJ6hfgpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 378,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 26573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0133ji5x49Hj9XvbqEKNAKgH`</summary>

```json
{
  "query": "SAIS Xiao NAACL 2022 arxiv document relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "81a128b3-eb44-4403-8ce9-6095939abc8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dtmpJDb8hv6HugJ6hfgpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 378,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 26573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YRFrJSR6UpcQqVmj4z6yF9`</summary>

```json
{
  "query": "EACL 2023 DREEAM \"Youmi Ma\" site:aclanthology.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "2ec7b9e0-efdd-4eda-8fb8-d4a871ae3e97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dtmpJDb8hv6HugJ6hfgpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 378,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 26573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 18 · 2026-05-17T15:24:52.839Z_

<details><summary>↩ Tool result · `toolu_01JobmUMY3o6wEJEF58569g6`</summary>

```text
Web search results for query: "DREEAM "Youmi Ma" EACL 2023 document relation extraction"

Links: [{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.eacl-main.145/"},{"title":"GitHub - YoumiMa/dreeam: source code for {D}ocument-level {R}elation {E}xtraction with {E}vidence-guided {A}ttention {M}echanism · GitHub","url":"https://github.com/YoumiMa/dreeam"},{"title":"DREEAM: Guiding Attention with Evidence for Improving ...","url":"https://aclanthology.org/2023.eacl-main.145.pdf"},{"title":"dreeam/README.md at main · YoumiMa/dreeam","url":"https://github.com/YoumiMa/dreeam/blob/main/README.md"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/373811777_DREEAM_Guiding_Attention_with_Evidence_for_Improving_Document-Level_Relation_Extraction"},{"title":"Youmi Ma","url":"https://www.catalyzex.com/author/Youmi%20Ma"},{"title":"dblp: Youmi Ma","url":"https://dblp.org/pid/268/1357.html"},{"title":"(PDF) Until the Completion of “Incorporating Evidence Retrieval into Document-Level Relation Extraction”「文書レベル関係抽出における根拠認識の統合」の完成まで","url":"https://www.researchgate.net/publication/373932566_Until_the_Completion_of_Incorporating_Evidence_Retrieval_into_Document-Level_Relation_Extractionwenshureberuguanxichouchuniokerugenjurenshinotonghenowanchengmade"},{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://arxiv.org/abs/2302.08675"},{"title":"Main Conference Accepted Papers - EACL 2023","url":"https://2023.eacl.org/program/accepted/"}]

I found comprehensive information about the DREEAM paper. Here are the key details:

## Paper Overview

DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction is authored by Youmi Ma, An Wang, and Naoaki Okazaki and was published at EACL 2023.

## What is DREEAM?

Document-level relation extraction (DocRE) is the task of identifying all relations between each entity pair in a document. Evidence, defined as sentences containing clues for the relationship between an entity pair, has been shown to help DocRE systems focus on relevant texts, thus improving relation extraction.

## The Problem it Addresses

Evidence retrieval (ER) in DocRE faces two major issues: high memory consumption and limited availability of annotations.

## The Solution

DREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal, thereby guiding the attention modules of the DocRE system to assign high weights to evidence. Additionally, the approach proposes a self-training strategy for DREEAM to learn ER from automatically-generated evidence on massive data without evidence annotations.

## Results and Significance

Experimental results reveal that the approach exhibits state-of-the-art performance on the DocRED benchmark for both DocRE and ER. Notably, DREEAM is the first approach to employ ER self-training.

You can access the full paper at the ACL Anthology: https://aclanthology.org/2023.eacl-main.145/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "db56d70d-d3de-4f2a-80d4-61ec7ece1fb8",
  "tool_use_result": {
    "query": "DREEAM \"Youmi Ma\" EACL 2023 document relation extraction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Wh9eYh5Abv1yEy9gnR1Yf6",
        "content": [
          {
            "title": "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology",
            "url": "https://aclanthology.org/2023.eacl-main.145/"
          },
          {
            "title": "GitHub - YoumiMa/dreeam: source code for {D}ocument-level {R}elation {E}xtraction with {E}vidence-guided {A}ttention {M}echanism · GitHub",
            "url": "https://github.com/YoumiMa/dreeam"
          },
          {
            "title": "DREEAM: Guiding Attention with Evidence for Improving ...",
            "url": "https://aclanthology.org/2023.eacl-main.145.pdf"
          },
          {
            "title": "dreeam/README.md at main · YoumiMa/dreeam",
            "url": "https://github.com/YoumiMa/dreeam/blob/main/README.md"
          },
          {
            "title": "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction",
            "url": "https://www.researchgate.net/publication/373811777_DREEAM_Guiding_Attention_with_Evidence_for_Improving_Document-Level_Relation_Extraction"
          },
          {
            "title": "Youmi Ma",
            "url": "https://www.catalyzex.com/author/Youmi%20Ma"
          },
          {
            "title": "dblp: Youmi Ma",
            "url": "https://dblp.org/pid/268/1357.html"
          },
          {
            "title": "(PDF) Until the Completion of “Incorporating Evidence Retrieval into Document-Level Relation Extraction”「文書レベル関係抽出における根拠認識の統合」の完成まで",
            "url": "https://www.researchgate.net/publication/373932566_Until_the_Completion_of_Incorporating_Evidence_Retrieval_into_Document-Level_Relation_Extractionwenshureberuguanxichouchuniokerugenjurenshinotonghenowanchengmade"
          },
          {
            "title": "[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction",
            "url": "https://arxiv.org/abs/2302.08675"
          },
          {
            "title": "Main Conference Accepted Papers - EACL 2023",
            "url": "https://2023.eacl.org/program/accepted/"
          }
        ]
      },
      "I found comprehensive information about the DREEAM paper. Here are the key details:\n\n## Paper Overview\n\nDREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction is authored by Youmi Ma, An Wang, and Naoaki Okazaki and was published at EACL 2023.\n\n## What is DREEAM?\n\nDocument-level relation extraction (DocRE) is the task of identifying all relations between each entity pair in a document. Evidence, defined as sentences containing clues for the relationship between an entity pair, has been shown to help DocRE systems focus on relevant texts, thus improving relation extraction.\n\n## The Problem it Addresses\n\nEvidence retrieval (ER) in DocRE faces two major issues: high memory consumption and limited availability of annotations.\n\n## The Solution\n\nDREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal, thereby guiding the attention modules of the DocRE system to assign high weights to evidence. Additionally, the approach proposes a self-training strategy for DREEAM to learn ER from automatically-generated evidence on massive data without evidence annotations.\n\n## Results and Significance\n\nExperimental results reveal that the approach exhibits state-of-the-art performance on the DocRED benchmark for both DocRE and ER. Notably, DREEAM is the first approach to employ ER self-training.\n\nYou can access the full paper at the ACL Anthology: https://aclanthology.org/2023.eacl-main.145/"
    ],
    "durationSeconds": 7.068988457000003
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T15:24:53.565Z_

<details><summary>↩ Tool result · `toolu_0133ji5x49Hj9XvbqEKNAKgH`</summary>

```text
Web search results for query: "SAIS Xiao NAACL 2022 arxiv document relation extraction"

Links: [{"title":"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.171/"},{"title":"GitHub - xiaoyuxin1002/SAIS: SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction","url":"https://github.com/xiaoyuxin1002/SAIS"},{"title":"[2109.12093] SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction","url":"https://arxiv.org/abs/2109.12093"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Rethinking Document-Level Relation Extraction: A Reality Check","url":"https://arxiv.org/html/2306.08953"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"SAIS: Supervising and Augmenting Intermediate Steps for ...","url":"https://aclanthology.org/2022.naacl-main.171.pdf"},{"title":"document-level in-context few-shot relation extraction via ...","url":"https://arxiv.org/pdf/2310.11085"},{"title":"Document-Level Relation Extraction Based on Fine-Grained Information Guidance | Advanced Intelligent Computing Technology and Applications","url":"https://dl.acm.org/doi/10.1007/978-981-97-5669-8_31"},{"title":"Few-Shot Document-Level Relation Extraction","url":"https://aclanthology.org/anthology-files/pdf/naacl/2022.naacl-main.421.pdf"}]

I found comprehensive information about the SAIS paper. Here's what I discovered:

SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction is a paper by Yuxin Xiao, Zecheng Zhang, Yuning Mao, Carl Yang, and Jiawei Han, published at NAACL 2022. The paper is also available on arXiv as arXiv:2109.12093.

The paper proposes to explicitly teach the model to capture relevant contexts and entity types by supervising and augmenting intermediate steps (SAIS) for relation extraction. Based on carefully designed tasks, the SAIS method extracts relations of better quality due to more effective supervision and retrieves corresponding supporting evidence more accurately to enhance interpretability.

By assessing model uncertainty, SAIS further boosts performance via evidence-based data augmentation and ensemble inference while reducing computational cost. The method delivers state-of-the-art relation extraction results on three benchmarks (DocRED, CDR, and GDA) and outperforms the runner-up by 5.04% relatively in F1 score in evidence retrieval on DocRED.

The approach employs language models such as BERT, RoBERTa, and SciBERT to encode extensive contextual dependencies, addressing the complexities of capturing extended contexts and nuanced interactions among entities in document-level relation extraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "ac64d4ec-8443-48bd-b24f-12b4b552a811",
  "tool_use_result": {
    "query": "SAIS Xiao NAACL 2022 arxiv document relation extraction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VmG1jdSZx5764vUyu5hgLJ",
        "content": [
          {
            "title": "SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction - ACL Anthology",
            "url": "https://aclanthology.org/2022.naacl-main.171/"
          },
          {
            "title": "GitHub - xiaoyuxin1002/SAIS: SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction",
            "url": "https://github.com/xiaoyuxin1002/SAIS"
          },
          {
            "title": "[2109.12093] SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction",
            "url": "https://arxiv.org/abs/2109.12093"
          },
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-025-11280-0"
          },
          {
            "title": "Rethinking Document-Level Relation Extraction: A Reality Check",
            "url": "https://arxiv.org/html/2306.08953"
          },
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models",
            "url": "https://arxiv.org/html/2411.18157v1"
          },
          {
            "title": "SAIS: Supervising and Augmenting Intermediate Steps for ...",
            "url": "https://aclanthology.org/2022.naacl-main.171.pdf"
          },
          {
            "title": "document-level in-context few-shot relation extraction via ...",
            "url": "https://arxiv.org/pdf/2310.11085"
          },
          {
            "title": "Document-Level Relation Extraction Based on Fine-Grained Information Guidance | Advanced Intelligent Computing Technology and Applications",
            "url": "https://dl.acm.org/doi/10.1007/978-981-97-5669-8_31"
          },
          {
            "title": "Few-Shot Document-Level Relation Extraction",
            "url": "https://aclanthology.org/anthology-files/pdf/naacl/2022.naacl-main.421.pdf"
          }
        ]
      },
      "I found comprehensive information about the SAIS paper. Here's what I discovered:\n\nSAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction is a paper by Yuxin Xiao, Zecheng Zhang, Yuning Mao, Carl Yang, and Jiawei Han, published at NAACL 2022. The paper is also available on arXiv as arXiv:2109.12093.\n\nThe paper proposes to explicitly teach the model to capture relevant contexts and entity types by supervising and augmenting intermediate steps (SAIS) for relation extraction. Based on carefully designed tasks, the SAIS method extracts relations of better quality due to more effective supervision and retrieves corresponding supporting evidence more accurately to enhance interpretability.\n\nBy assessing model uncertainty, SAIS further boosts performance via evidence-based data augmentation and ensemble inference while reducing computational cost. The method delivers state-of-the-art relation extraction results on three benchmarks (DocRED, CDR, and GDA) and outperforms the runner-up by 5.04% relatively in F1 score in evidence retrieval on DocRED.\n\nThe approach employs language models such as BERT, RoBERTa, and SciBERT to encode extensive contextual dependencies, addressing the complexities of capturing extended contexts and nuanced interactions among entities in document-level relation extraction."
    ],
    "durationSeconds": 6.777232463999997
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T15:24:53.586Z_

<details><summary>↩ Tool result · `toolu_01YRFrJSR6UpcQqVmj4z6yF9`</summary>

```text
Web search results for query: "EACL 2023 DREEAM "Youmi Ma" site:aclanthology.org"

Links: [{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.eacl-main.145/"},{"title":"DREEAM: Guiding Attention with Evidence for Improving ...","url":"https://aclanthology.org/2023.eacl-main.145.pdf"},{"title":"Youmi Ma - ACL Anthology","url":"https://aclanthology.org/people/y/youmi-ma/"},{"title":"Improving Cross-Lingual Transfer for Open Information Extraction with Linguistic Feature Projection - ACL Anthology","url":"https://aclanthology.org/2023.mrl-1.11/"},{"title":"Generative Data Augmentation for Aspect Sentiment Quad Prediction - ACL Anthology","url":"https://aclanthology.org/2023.starsem-1.12/"},{"title":"Proceedings of the 3rd Workshop on Multi-lingual Representation Learning (MRL) - ACL Anthology","url":"https://aclanthology.org/volumes/2023.mrl-1/"},{"title":"EACL 2026 The 19th Conference of the European Chapter of the","url":"https://aclanthology.org/2026.eacl-short.0.pdf"}]

The search returned results about the paper "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction" from EACL 2023 with Youmi Ma as an author.

Here are the key findings:

## Paper Details

The paper "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction" was authored by Youmi Ma, An Wang, and Naoaki Okazaki and presented at EACL 2023.

## Paper Content

Document-level relation extraction (DocRE) is the task of identifying all relations between each entity pair in a document. Evidence, defined as sentences containing clues for the relationship between an entity pair, has been shown to help DocRE systems focus on relevant texts, thus improving relation extraction.

## Key Contribution

DREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal, thereby guiding the attention modules of the DocRE system to assign high weights to evidence.

## Results

The experimental results reveal that their approach exhibits state-of-the-art performance on the DocRED benchmark for both DocRE and ER, and to the best of their knowledge, DREEAM is the first approach to employ ER self-training.

The full paper is available at: https://aclanthology.org/2023.eacl-main.145/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "ed27f089-8986-4b9e-b1aa-e0f329fd0b23",
  "tool_use_result": {
    "query": "EACL 2023 DREEAM \"Youmi Ma\" site:aclanthology.org",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EVRmqD3CHZvdwbnrfFoc3r",
        "content": [
          {
            "title": "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology",
            "url": "https://aclanthology.org/2023.eacl-main.145/"
          },
          {
            "title": "DREEAM: Guiding Attention with Evidence for Improving ...",
            "url": "https://aclanthology.org/2023.eacl-main.145.pdf"
          },
          {
            "title": "Youmi Ma - ACL Anthology",
            "url": "https://aclanthology.org/people/y/youmi-ma/"
          },
          {
            "title": "Improving Cross-Lingual Transfer for Open Information Extraction with Linguistic Feature Projection - ACL Anthology",
            "url": "https://aclanthology.org/2023.mrl-1.11/"
          },
          {
            "title": "Generative Data Augmentation for Aspect Sentiment Quad Prediction - ACL Anthology",
            "url": "https://aclanthology.org/2023.starsem-1.12/"
          },
          {
            "title": "Proceedings of the 3rd Workshop on Multi-lingual Representation Learning (MRL) - ACL Anthology",
            "url": "https://aclanthology.org/volumes/2023.mrl-1/"
          },
          {
            "title": "EACL 2026 The 19th Conference of the European Chapter of the",
            "url": "https://aclanthology.org/2026.eacl-short.0.pdf"
          }
        ]
      },
      "The search returned results about the paper \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\" from EACL 2023 with Youmi Ma as an author.\n\nHere are the key findings:\n\n## Paper Details\n\nThe paper \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\" was authored by Youmi Ma, An Wang, and Naoaki Okazaki and presented at EACL 2023.\n\n## Paper Content\n\nDocument-level relation extraction (DocRE) is the task of identifying all relations between each entity pair in a document. Evidence, defined as sentences containing clues for the relationship between an entity pair, has been shown to help DocRE systems focus on relevant texts, thus improving relation extraction.\n\n## Key Contribution\n\nDREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal, thereby guiding the attention modules of the DocRE system to assign high weights to evidence.\n\n## Results\n\nThe experimental results reveal that their approach exhibits state-of-the-art performance on the DocRED benchmark for both DocRE and ER, and to the best of their knowledge, DREEAM is the first approach to employ ER self-training.\n\nThe full paper is available at: https://aclanthology.org/2023.eacl-main.145/"
    ],
    "durationSeconds": 6.666602455999997
  }
}
```

</details>

---

### Assistant

_source line 21_

DREEAM 和 SAIS 验证完毕。现在并行搜索 gap-fill 候选论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "197c0d55-4f3c-4727-ac26-310d2b06b49c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdHX1q9JCEAtJz4pMdDo84",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3209,
      "cache_read_input_tokens": 27502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3209
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

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J2c82CxuJNSiJrKoT4F9sS`</summary>

```json
{
  "query": "GEGA \"Graph Convolutional Networks and Evidence Retrieval Guided Attention\" document relation extraction arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "806f9d96-db1d-48f3-8772-a6dc016cea60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdHX1q9JCEAtJz4pMdDo84",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3209,
      "cache_read_input_tokens": 27502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3209
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

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0115nzmB31jyXmuXQF3UYdQD`</summary>

```json
{
  "query": "DocGNRE \"document-level relation extraction\" evidence generation arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "e583bc91-7a55-42e4-aadf-3e53ed0fb0a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdHX1q9JCEAtJz4pMdDo84",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3209,
      "cache_read_input_tokens": 27502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3209
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GwbTxMqneDqdMwiWCgJuhw`</summary>

```json
{
  "query": "CDER \"Collaborative Evidence Retrieval\" document-level relation extraction arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "bf642fe0-0df2-4fb5-aabd-a2c0ea8f13a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdHX1q9JCEAtJz4pMdDo84",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3209,
      "cache_read_input_tokens": 27502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3209
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016kCTRV3PefpxwDjW3XBA4q`</summary>

```json
{
  "query": "ERID \"Evidence Retrieval for Document-Level Relation Extraction\" arxiv OR aclanthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "f673bce9-d51b-4e17-b668-655946b54bb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdHX1q9JCEAtJz4pMdDo84",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3209,
      "cache_read_input_tokens": 27502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3209
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

_source line 26 · 2026-05-17T15:25:08.890Z_

<details><summary>↩ Tool result · `toolu_01J2c82CxuJNSiJrKoT4F9sS`</summary>

```text
Web search results for query: "GEGA "Graph Convolutional Networks and Evidence Retrieval Guided Attention" document relation extraction arxiv"

Links: [{"title":"[2407.21384] GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/abs/2407.21384"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/html/2407.21384v1"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10889649/"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=oUMKv7Nlav"},{"title":"[1906.07510] Attention Guided Graph Convolutional Networks for Relation Extraction","url":"https://arxiv.org/abs/1906.07510"},{"title":"Revisiting Document-Level Relation Extraction with Context-Guided Link Prediction","url":"https://www.emergentmind.com/papers/2401.11800"},{"title":"GitHub - Cartus/AGGCN: Attention Guided Graph Convolutional Networks for Relation Extraction (authors' PyTorch implementation for the ACL19 paper) · GitHub","url":"https://github.com/Cartus/AGGCN"},{"title":"Attention Guided Graph Convolutional Networks for Relation Extraction","url":"https://arxiv.org/pdf/1906.07510"},{"title":"Document-level relation extraction model guided by global information and external contextual knowledge | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-07467-5"},{"title":"(PDF) Attention Guided Graph Convolutional Networks for Relation Extraction","url":"https://www.researchgate.net/publication/333865746_Attention_Guided_Graph_Convolutional_Networks_for_Relation_Extraction"}]

I found the GEGA paper on arXiv! Here are the key details:

**Paper Title:** GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction

**Authors:** By Yanxu Mao and 5 other authors

**arXiv ID:** 2407.21384

**Publication Date:** First version: July 31, 2024; Second version: September 8, 2024

**Paper Overview:**

Document-level relation extraction (DocRE) aims to extract relations between entities from unstructured document text. Compared to sentence-level relation extraction, it requires more complex semantic understanding from a broader text context.

**Key Challenges Addressed:** DocRE suffers from two challenges: firstly, the relevance between evidence and entity pairs is weak; secondly, there is insufficient extraction of complex cross-relations between long-distance multi-entities.

**Proposed Solution:** The model leverages graph neural networks to construct multiple weight matrices, guiding attention allocation to evidence sentences. It also employs multi-scale representation aggregation to enhance ER.

**Evaluation:** The GEGA model was evaluated on three widely used benchmark datasets: DocRED, Re-DocRED, and Revisit-DocRED. The experimental results indicate that the model has achieved comprehensive improvements compared to the existing SOTA model.

The paper is available at: https://arxiv.org/abs/2407.21384


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "7e1a177c-fbc2-4a4e-be3d-9c9919e42e79",
  "tool_use_result": {
    "query": "GEGA \"Graph Convolutional Networks and Evidence Retrieval Guided Attention\" document relation extraction arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_013Xexik3jSa64gw4vySNoDC",
        "content": [
          {
            "title": "[2407.21384] GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction",
            "url": "https://arxiv.org/abs/2407.21384"
          },
          {
            "title": "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2407.21384v1"
          },
          {
            "title": "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/10889649/"
          },
          {
            "title": "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction | OpenReview",
            "url": "https://openreview.net/forum?id=oUMKv7Nlav"
          },
          {
            "title": "[1906.07510] Attention Guided Graph Convolutional Networks for Relation Extraction",
            "url": "https://arxiv.org/abs/1906.07510"
          },
          {
            "title": "Revisiting Document-Level Relation Extraction with Context-Guided Link Prediction",
            "url": "https://www.emergentmind.com/papers/2401.11800"
          },
          {
            "title": "GitHub - Cartus/AGGCN: Attention Guided Graph Convolutional Networks for Relation Extraction (authors' PyTorch implementation for the ACL19 paper) · GitHub",
            "url": "https://github.com/Cartus/AGGCN"
          },
          {
            "title": "Attention Guided Graph Convolutional Networks for Relation Extraction",
            "url": "https://arxiv.org/pdf/1906.07510"
          },
          {
            "title": "Document-level relation extraction model guided by global information and external contextual knowledge | The Journal of Supercomputing | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11227-025-07467-5"
          },
          {
            "title": "(PDF) Attention Guided Graph Convolutional Networks for Relation Extraction",
            "url": "https://www.researchgate.net/publication/333865746_Attention_Guided_Graph_Convolutional_Networks_for_Relation_Extraction"
          }
        ]
      },
      "I found the GEGA paper on arXiv! Here are the key details:\n\n**Paper Title:** GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction\n\n**Authors:** By Yanxu Mao and 5 other authors\n\n**arXiv ID:** 2407.21384\n\n**Publication Date:** First version: July 31, 2024; Second version: September 8, 2024\n\n**Paper Overview:**\n\nDocument-level relation extraction (DocRE) aims to extract relations between entities from unstructured document text. Compared to sentence-level relation extraction, it requires more complex semantic understanding from a broader text context.\n\n**Key Challenges Addressed:** DocRE suffers from two challenges: firstly, the relevance between evidence and entity pairs is weak; secondly, there is insufficient extraction of complex cross-relations between long-distance multi-entities.\n\n**Proposed Solution:** The model leverages graph neural networks to construct multiple weight matrices, guiding attention allocation to evidence sentences. It also employs multi-scale representation aggregation to enhance ER.\n\n**Evaluation:** The GEGA model was evaluated on three widely used benchmark datasets: DocRED, Re-DocRED, and Revisit-DocRED. The experimental results indicate that the model has achieved comprehensive improvements compared to the existing SOTA model.\n\nThe paper is available at: https://arxiv.org/abs/2407.21384"
    ],
    "durationSeconds": 6.5805185029999995
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T15:25:09.593Z_

<details><summary>↩ Tool result · `toolu_01GwbTxMqneDqdMwiWCgJuhw`</summary>

```text
Web search results for query: "CDER "Collaborative Evidence Retrieval" document-level relation extraction arxiv"

Links: [{"title":"[2504.06529] CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/abs/2504.06529"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-97-4982-9_3"},{"title":"[PDF] CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CDER:-Collaborative-Evidence-Retrieval-for-Relation-Tran-Li/07f36e6f29c07f0edce7465f4d005bd34ac659ce"},{"title":"(PDF) CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/390638674_CDER_Collaborative_Evidence_Retrieval_for_Document-level_Relation_Extraction"},{"title":"CDER: Collaborative Evidence Retrieval for Document- ...","url":"https://www.researchgate.net/publication/382280635_CDER_Collaborative_Evidence_Retrieval_for_Document-Level_Relation_Extraction"},{"title":"open source AI","url":"https://bytez.com/docs/arxiv/2504.06529/paper"},{"title":"CDER: Collaborative evidence retrieval for document-level ...","url":"https://espace.library.uq.edu.au/view/UQ:f699039"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level ...","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2504.06529"},{"title":"publications | Khai Tran - GitHub Pages","url":"https://khaitran22.github.io/publications/"}]

I found the paper you're looking for! Here are the key details:

## CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction

**Paper Location:** arxiv.org/abs/2504.06529 (published April 9, 2025)

**Authors:** Khai Phan Tran and Xue Li

**Overview:**
Document-level Relation Extraction (DocRE) involves identifying relations between entities across multiple sentences in a document, with evidence sentences crucial for precise entity pair relationships identification.

**Problem Addressed:**
Existing evidence retrieval systems often overlook the collaborative nature among semantically similar entity pairs in the same document, hindering the effectiveness of the evidence retrieval task.

**Solution:**
CDER employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval.

**Technical Architecture:**
CDER transforms the document into a bipartite graph with entity pair and sentence nodes, partitioning it into three sub-graphs: (i) Entity Pair sub-graph models collaboration, (ii) Entity Pair-Sentence sub-graph captures semantic relationships, and (iii) Sentence sub-graph aids co-reference reasoning.

**Results:**
Experimental results on the benchmark DocRE dataset show that CDER not only excels in the evidence retrieval task but also enhances overall performance of existing DocRE system.

The code is available at: https://github.com/khaitran22/CDER


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "ca34b040-ec97-4643-a83e-548722cba66a",
  "tool_use_result": {
    "query": "CDER \"Collaborative Evidence Retrieval\" document-level relation extraction arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AqTW3T6d88k7yDNazvzZ9F",
        "content": [
          {
            "title": "[2504.06529] CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction",
            "url": "https://arxiv.org/abs/2504.06529"
          },
          {
            "title": "CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2504.06529"
          },
          {
            "title": "CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-981-97-4982-9_3"
          },
          {
            "title": "[PDF] CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/CDER:-Collaborative-Evidence-Retrieval-for-Relation-Tran-Li/07f36e6f29c07f0edce7465f4d005bd34ac659ce"
          },
          {
            "title": "(PDF) CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction",
            "url": "https://www.researchgate.net/publication/390638674_CDER_Collaborative_Evidence_Retrieval_for_Document-level_Relation_Extraction"
          },
          {
            "title": "CDER: Collaborative Evidence Retrieval for Document- ...",
            "url": "https://www.researchgate.net/publication/382280635_CDER_Collaborative_Evidence_Retrieval_for_Document-Level_Relation_Extraction"
          },
          {
            "title": "open source AI",
            "url": "https://bytez.com/docs/arxiv/2504.06529/paper"
          },
          {
            "title": "CDER: Collaborative evidence retrieval for document-level ...",
            "url": "https://espace.library.uq.edu.au/view/UQ:f699039"
          },
          {
            "title": "CDER: Collaborative Evidence Retrieval for Document-level ...",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2504.06529"
          },
          {
            "title": "publications | Khai Tran - GitHub Pages",
            "url": "https://khaitran22.github.io/publications/"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n## CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction\n\n**Paper Location:** arxiv.org/abs/2504.06529 (published April 9, 2025)\n\n**Authors:** Khai Phan Tran and Xue Li\n\n**Overview:**\nDocument-level Relation Extraction (DocRE) involves identifying relations between entities across multiple sentences in a document, with evidence sentences crucial for precise entity pair relationships identification.\n\n**Problem Addressed:**\nExisting evidence retrieval systems often overlook the collaborative nature among semantically similar entity pairs in the same document, hindering the effectiveness of the evidence retrieval task.\n\n**Solution:**\nCDER employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval.\n\n**Technical Architecture:**\nCDER transforms the document into a bipartite graph with entity pair and sentence nodes, partitioning it into three sub-graphs: (i) Entity Pair sub-graph models collaboration, (ii) Entity Pair-Sentence sub-graph captures semantic relationships, and (iii) Sentence sub-graph aids co-reference reasoning.\n\n**Results:**\nExperimental results on the benchmark DocRE dataset show that CDER not only excels in the evidence retrieval task but also enhances overall performance of existing DocRE system.\n\nThe code is available at: https://github.com/khaitran22/CDER"
    ],
    "durationSeconds": 6.33928226
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T15:25:10.054Z_

<details><summary>↩ Tool result · `toolu_016kCTRV3PefpxwDjW3XBA4q`</summary>

```text
Web search results for query: "ERID "Evidence Retrieval for Document-Level Relation Extraction" arxiv OR aclanthology"

Links: [{"title":"EIDER: Empowering Document-level Relation Extraction ...","url":"https://aclanthology.org/2022.findings-acl.23.pdf"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.23/"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.eacl-main.145/"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Entity and Evidence Guided Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2021.repl4nlp-1.30/"},{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"[2303.03912] Document-level Relation Extraction with Cross-sentence Reasoning Graph","url":"https://arxiv.org/abs/2303.03912"},{"title":"A Comprehensive Survey on Document-Level Information ...","url":"https://aclanthology.org/2024.futured-1.6.pdf"}]

Based on the search results, I found several papers related to evidence retrieval for document-level relation extraction, though I did not find a paper specifically titled "ERID: Evidence Retrieval for Document-Level Relation Extraction."

The search results show related work in this area:

1. **EIDER** - Eider is an evidence-enhanced framework that empowers DocRE by efficiently extracting evidence and effectively fusing the extracted evidence in inference. This paper was published on arXiv (2106.08657) and in the Findings of ACL 2022.

2. **CDER** - CDER is a novel evidence retrieval framework that employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval.

3. **DREEAM** - DREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal to guide the attention modules of the DocRE system, with a self-training strategy to learn ER from automatically-generated evidence on massive data without evidence annotations.

If you're looking for a specific paper with the exact title "ERID: Evidence Retrieval for Document-Level Relation Extraction," it may not be indexed in the results, or you might be looking for one of these related papers instead. Would you like me to search more specifically or provide additional information about any of these papers?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "173bfa87-76ee-4731-b335-b5f121532bdd",
  "tool_use_result": {
    "query": "ERID \"Evidence Retrieval for Document-Level Relation Extraction\" arxiv OR aclanthology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Lp2UUy6AvTgNesaah3PW3G",
        "content": [
          {
            "title": "EIDER: Empowering Document-level Relation Extraction ...",
            "url": "https://aclanthology.org/2022.findings-acl.23.pdf"
          },
          {
            "title": "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ACL Anthology",
            "url": "https://aclanthology.org/2022.findings-acl.23/"
          },
          {
            "title": "CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2504.06529"
          },
          {
            "title": "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology",
            "url": "https://aclanthology.org/2023.eacl-main.145/"
          },
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models",
            "url": "https://arxiv.org/html/2411.18157v1"
          },
          {
            "title": "Entity and Evidence Guided Document-Level Relation Extraction - ACL Anthology",
            "url": "https://aclanthology.org/2021.repl4nlp-1.30/"
          },
          {
            "title": "[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion",
            "url": "https://arxiv.org/abs/2106.08657"
          },
          {
            "title": "DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology",
            "url": "https://aclanthology.org/P19-1074/"
          },
          {
            "title": "[2303.03912] Document-level Relation Extraction with Cross-sentence Reasoning Graph",
            "url": "https://arxiv.org/abs/2303.03912"
          },
          {
            "title": "A Comprehensive Survey on Document-Level Information ...",
            "url": "https://aclanthology.org/2024.futured-1.6.pdf"
          }
        ]
      },
      "Based on the search results, I found several papers related to evidence retrieval for document-level relation extraction, though I did not find a paper specifically titled \"ERID: Evidence Retrieval for Document-Level Relation Extraction.\"\n\nThe search results show related work in this area:\n\n1. **EIDER** - Eider is an evidence-enhanced framework that empowers DocRE by efficiently extracting evidence and effectively fusing the extracted evidence in inference. This paper was published on arXiv (2106.08657) and in the Findings of ACL 2022.\n\n2. **CDER** - CDER is a novel evidence retrieval framework that employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval.\n\n3. **DREEAM** - DREEAM is a memory-efficient approach that adopts evidence information as the supervisory signal to guide the attention modules of the DocRE system, with a self-training strategy to learn ER from automatically-generated evidence on massive data without evidence annotations.\n\nIf you're looking for a specific paper with the exact title \"ERID: Evidence Retrieval for Document-Level Relation Extraction,\" it may not be indexed in the results, or you might be looking for one of these related papers instead. Would you like me to search more specifically or provide additional information about any of these papers?"
    ],
    "durationSeconds": 6.358722079
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T15:25:10.456Z_

<details><summary>↩ Tool result · `toolu_0115nzmB31jyXmuXQF3UYdQD`</summary>

```text
Web search results for query: "DocGNRE "document-level relation extraction" evidence generation arxiv"

Links: [{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://arxiv.org/abs/2302.08675"},{"title":"Document-Level Relation Extraction with Relation Correlation Enhancement","url":"https://arxiv.org/html/2310.13000"},{"title":"A Comprehensive Survey of Document-level Relation Extraction (2016-2023)","url":"https://web3.arxiv.org/pdf/2309.16396v2"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/html/2407.21384"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"[2407.21384] GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/abs/2407.21384"},{"title":"[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283"},{"title":"[2204.12679] Document-Level Relation Extraction with Sentences Importance Estimation and Focusing","url":"https://arxiv.org/abs/2204.12679"},{"title":"Consistent Document-Level Relation Extraction via Counterfactuals","url":"https://arxiv.org/html/2407.06699v2"}]

Based on the search results, I found several relevant papers on document-level relation extraction with evidence generation on arXiv. Here are the key findings:

## Main Results

The search didn't return a specific paper titled "DocGNRE" with that exact name, but it did reveal several closely related papers on document-level relation extraction (DocRE) with evidence generation:

### Key Papers Found:

1. **EIDER (2022)** - An evidence-enhanced framework that empowers DocRE by efficiently extracting evidence and effectively fusing the extracted evidence in inference, jointly training an RE model with a lightweight evidence extraction model, and designing an inference process that makes RE predictions on both extracted evidence and the full document, then fuses the predictions through a blending layer.

2. **DREEAM (2023)** - A memory-efficient approach that adopts evidence information as the supervisory signal to guide attention modules of the DocRE system, and proposes a self-training strategy to learn ER from automatically-generated evidence on massive data without evidence annotations.

3. **GEGA (2024)** - A study utilizing logical rules within evidence sentences to enhance DocRE performance, and in data without provided evidence sentences, obtaining a list of evidence sentences for the entire document through evidence retrieval (ER).

4. **CDER (2025)** - A novel evidence retrieval framework that employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval.

If you're looking for a specific paper called "DocGNRE," you may want to search with a slightly different query or check if it might be a recent or lesser-known work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "3a88e079-2f74-4bd7-9186-6eeee1e40bce",
  "tool_use_result": {
    "query": "DocGNRE \"document-level relation extraction\" evidence generation arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JzE3tvzLpaHRz1WgUDnTcG",
        "content": [
          {
            "title": "[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion",
            "url": "https://arxiv.org/abs/2106.08657"
          },
          {
            "title": "[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction",
            "url": "https://arxiv.org/abs/2302.08675"
          },
          {
            "title": "Document-Level Relation Extraction with Relation Correlation Enhancement",
            "url": "https://arxiv.org/html/2310.13000"
          },
          {
            "title": "A Comprehensive Survey of Document-level Relation Extraction (2016-2023)",
            "url": "https://web3.arxiv.org/pdf/2309.16396v2"
          },
          {
            "title": "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2407.21384"
          },
          {
            "title": "CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2504.06529"
          },
          {
            "title": "[2407.21384] GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction",
            "url": "https://arxiv.org/abs/2407.21384"
          },
          {
            "title": "[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED",
            "url": "https://arxiv.org/abs/2008.12283"
          },
          {
            "title": "[2204.12679] Document-Level Relation Extraction with Sentences Importance Estimation and Focusing",
            "url": "https://arxiv.org/abs/2204.12679"
          },
          {
            "title": "Consistent Document-Level Relation Extraction via Counterfactuals",
            "url": "https://arxiv.org/html/2407.06699v2"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on document-level relation extraction with evidence generation on arXiv. Here are the key findings:\n\n## Main Results\n\nThe search didn't return a specific paper titled \"DocGNRE\" with that exact name, but it did reveal several closely related papers on document-level relation extraction (DocRE) with evidence generation:\n\n### Key Papers Found:\n\n1. **EIDER (2022)** - An evidence-enhanced framework that empowers DocRE by efficiently extracting evidence and effectively fusing the extracted evidence in inference, jointly training an RE model with a lightweight evidence extraction model, and designing an inference process that makes RE predictions on both extracted evidence and the full document, then fuses the predictions through a blending layer.\n\n2. **DREEAM (2023)** - A memory-efficient approach that adopts evidence information as the supervisory signal to guide attention modules of the DocRE system, and proposes a self-training strategy to learn ER from automatically-generated evidence on massive data without evidence annotations.\n\n3. **GEGA (2024)** - A study utilizing logical rules within evidence sentences to enhance DocRE performance, and in data without provided evidence sentences, obtaining a list of evidence sentences for the entire document through evidence retrieval (ER).\n\n4. **CDER (2025)** - A novel evidence retrieval framework that employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval.\n\nIf you're looking for a specific paper called \"DocGNRE,\" you may want to search with a slightly different query or check if it might be a recent or lesser-known work."
    ],
    "durationSeconds": 7.670218320999993
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Good, I've found GEGA and CDER. DocGNRE wasn't found directly. Let me search for the remaining candidates: EIDER (which appeared in results), COREX, and the "Entity and Evidence Guided" paper. Let me also search for DocGNRE more specifically, and EIDER which seems very relevant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "4d253a5e-a35b-43a0-97d9-392e9d4894f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoAfTryVCxynvew2dy85a4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2239,
      "cache_read_input_tokens": 30711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2239
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

_source line 31_

找到了 GEGA 和 CDER。继续搜索剩余候选论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "29dc5275-eea7-48e8-a53f-742d592315ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoAfTryVCxynvew2dy85a4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2239,
      "cache_read_input_tokens": 30711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2239
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QnJFCfcHwRP3dvEsbjy57g`</summary>

```json
{
  "query": "EIDER \"Empowering Document-level Relation Extraction with Efficient Evidence Extraction\" Xie ACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "7a443352-1051-40d6-a7a6-e3d2ff558558",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoAfTryVCxynvew2dy85a4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2239,
      "cache_read_input_tokens": 30711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2239
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

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WYftFNW2zYNzDZ8piXibgq`</summary>

```json
{
  "query": "DocGNRE \"document relation extraction\" evidence generation natural language explanation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "43075b12-5b6b-4209-a481-fbbae02e30a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoAfTryVCxynvew2dy85a4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2239,
      "cache_read_input_tokens": 30711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2239
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

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AdcT4MdgmzpqxRT11gMxKB`</summary>

```json
{
  "query": "COREX document-level relation extraction evidence arxiv aclanthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "897d68aa-d10a-4007-8891-b3fc70def5b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoAfTryVCxynvew2dy85a4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2239,
      "cache_read_input_tokens": 30711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2239
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UV1xkZEaPbv5ohTKHweKd6`</summary>

```json
{
  "query": "\"Entity and Evidence Guided Relation Extraction for DocRED\" arxiv 2008.12283"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "0420e715-3e76-46da-8375-a28942d2111a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NoAfTryVCxynvew2dy85a4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1792,
      "cache_creation_input_tokens": 2239,
      "cache_read_input_tokens": 30711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2239
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

_source line 36 · 2026-05-17T15:25:22.324Z_

<details><summary>↩ Tool result · `toolu_01QnJFCfcHwRP3dvEsbjy57g`</summary>

```text
Web search results for query: "EIDER "Empowering Document-level Relation Extraction with Efficient Evidence Extraction" Xie ACL 2022"

Links: [{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.23/"},{"title":"EIDER: Empowering Document-level Relation Extraction ...","url":"https://aclanthology.org/2022.findings-acl.23.pdf"},{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"GitHub - yiqingxyq/Eider: Source code for paper \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", ACL Findings, 2022","url":"https://github.com/yiqingxyq/Eider"},{"title":"[PDF] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/dbf1e5a17b3adead7016eb52ddc3007673ed382f"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Request PDF","url":"https://www.researchgate.net/publication/361056993_Eider_Empowering_Document-level_Relation_Extraction_with_Efficient_Evidence_Extraction_and_Inference-stage_Fusion"},{"title":"EIDER: Empowering Document-level Relation Extraction ...","url":"https://par.nsf.gov/servlets/purl/10633878"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/27f08f257f990b9db00aa60922f7eef1c/dblp"},{"title":"EIDER: Evidence-enhanced Document-level Relation Extraction","url":"https://research.google/pubs/eider-evidence-enhanced-document-level-relation-extraction/"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210608657X/abstract"}]

I found the research paper you're looking for. Here are the key details:

## Paper Summary

**EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion** was published in the Findings of the Association for Computational Linguistics: ACL 2022, pages 257–268, Dublin, Ireland.

**Authors:** Yiqing Xie, Jiaming Shen, Sha Li, Yuning Mao, and Jiawei Han

## Key Contributions

The paper proposes an evidence-enhanced framework, EIDER, that empowers document-level relation extraction (DocRE) by efficiently extracting evidence and effectively fusing the extracted evidence in inference. The authors jointly train a relation extraction model with a lightweight evidence extraction model, which is efficient in both memory and runtime.

The framework makes RE predictions on both extracted evidence and the full document, then fuses the predictions through a blending layer, allowing EIDER to focus on important sentences while still having access to the complete information in the document.

## Results

Extensive experiments show that EIDER outperforms state-of-the-art methods on three benchmark datasets (e.g., by 1.37/1.26 Ign F1/F1 on DocRED).

The paper is available on the [ACL Anthology](https://aclanthology.org/2022.findings-acl.23/) and the source code is available on [GitHub](https://github.com/yiqingxyq/Eider).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "fba512e5-c6a3-424f-b906-d254518eb6d9",
  "tool_use_result": {
    "query": "EIDER \"Empowering Document-level Relation Extraction with Efficient Evidence Extraction\" Xie ACL 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QLq4G6vCLoaqaP2d3cuaCp",
        "content": [
          {
            "title": "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ACL Anthology",
            "url": "https://aclanthology.org/2022.findings-acl.23/"
          },
          {
            "title": "EIDER: Empowering Document-level Relation Extraction ...",
            "url": "https://aclanthology.org/2022.findings-acl.23.pdf"
          },
          {
            "title": "[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion",
            "url": "https://arxiv.org/abs/2106.08657"
          },
          {
            "title": "GitHub - yiqingxyq/Eider: Source code for paper \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", ACL Findings, 2022",
            "url": "https://github.com/yiqingxyq/Eider"
          },
          {
            "title": "[PDF] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/dbf1e5a17b3adead7016eb52ddc3007673ed382f"
          },
          {
            "title": "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Request PDF",
            "url": "https://www.researchgate.net/publication/361056993_Eider_Empowering_Document-level_Relation_Extraction_with_Efficient_Evidence_Extraction_and_Inference-stage_Fusion"
          },
          {
            "title": "EIDER: Empowering Document-level Relation Extraction ...",
            "url": "https://par.nsf.gov/servlets/purl/10633878"
          },
          {
            "title": "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion. | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/27f08f257f990b9db00aa60922f7eef1c/dblp"
          },
          {
            "title": "EIDER: Evidence-enhanced Document-level Relation Extraction",
            "url": "https://research.google/pubs/eider-evidence-enhanced-document-level-relation-extraction/"
          },
          {
            "title": "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021arXiv210608657X/abstract"
          }
        ]
      },
      "I found the research paper you're looking for. Here are the key details:\n\n## Paper Summary\n\n**EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion** was published in the Findings of the Association for Computational Linguistics: ACL 2022, pages 257–268, Dublin, Ireland.\n\n**Authors:** Yiqing Xie, Jiaming Shen, Sha Li, Yuning Mao, and Jiawei Han\n\n## Key Contributions\n\nThe paper proposes an evidence-enhanced framework, EIDER, that empowers document-level relation extraction (DocRE) by efficiently extracting evidence and effectively fusing the extracted evidence in inference. The authors jointly train a relation extraction model with a lightweight evidence extraction model, which is efficient in both memory and runtime.\n\nThe framework makes RE predictions on both extracted evidence and the full document, then fuses the predictions through a blending layer, allowing EIDER to focus on important sentences while still having access to the complete information in the document.\n\n## Results\n\nExtensive experiments show that EIDER outperforms state-of-the-art methods on three benchmark datasets (e.g., by 1.37/1.26 Ign F1/F1 on DocRED).\n\nThe paper is available on the [ACL Anthology](https://aclanthology.org/2022.findings-acl.23/) and the source code is available on [GitHub](https://github.com/yiqingxyq/Eider)."
    ],
    "durationSeconds": 5.73495766
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-17T15:25:23.214Z_

<details><summary>↩ Tool result · `toolu_01UV1xkZEaPbv5ohTKHweKd6`</summary>

```text
Web search results for query: ""Entity and Evidence Guided Relation Extraction for DocRED" arxiv 2008.12283"

Links: [{"title":"[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED | Request PDF","url":"https://www.researchgate.net/publication/343931511_Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"},{"title":"[2008.12283v1] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283v1"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200812283H/abstract"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED","url":"https://www.catalyzex.com/paper/arxiv:2008.12283"},{"title":"[PDF] Entity and Evidence Guided Relation Extraction for DocRED | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Relation-Extraction-for-Huang-Qi/172678d3fb74bc56c9ac58f024b4eb43e0470e78"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED - Paper Detail","url":"https://deeplearn.org/arxiv/153393/entity-and-evidence-guided-relation-extraction-for-docred"},{"title":"(PDF) Entity and Evidence Guided Relation Extraction for DocRED","url":"https://www.academia.edu/103732963/Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"},{"title":"Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557313"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED | DeepAI","url":"https://deepai.org/publication/entity-and-evidence-guided-relation-extraction-for-docred"}]

I found the paper! Here's a summary of the search results for arxiv 2008.12283:

**Title:** Entity and Evidence Guided Relation Extraction for DocRED

**Authors:** Kevin Huang, Guangtao Wang, Tengyu Ma, and Jing Huang

**Submission Date:** August 27, 2020

**Summary:** The paper addresses document-level relation extraction, a challenging task which requires reasoning over multiple sentences in order to predict relations in a document. The authors propose a joint training framework called E2GRE (Entity and Evidence Guided Relation Extraction) for this task.

**Key Approach:** The method has two main components:
1. It introduces entity-guided sequences as inputs to a pre-trained language model (e.g. BERT, RoBERTa), which help the language model focus on areas of the document related to the entity.
2. It guides the fine-tuning of the pre-trained language model by using its internal attention probabilities as additional features for evidence prediction.

**Results:** The approach achieves state-of-the-art results on the public leaderboard across all metrics, showing that E2GRE is both effective and synergistic on relation extraction and evidence prediction.

The paper is available on arXiv at https://arxiv.org/abs/2008.12283


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "e934533c-433c-4437-82c3-b703806bb1bd",
  "tool_use_result": {
    "query": "\"Entity and Evidence Guided Relation Extraction for DocRED\" arxiv 2008.12283",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LfSUrUt1cZEE8KVSAJLQf8",
        "content": [
          {
            "title": "[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED",
            "url": "https://arxiv.org/abs/2008.12283"
          },
          {
            "title": "Entity and Evidence Guided Relation Extraction for DocRED | Request PDF",
            "url": "https://www.researchgate.net/publication/343931511_Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"
          },
          {
            "title": "[2008.12283v1] Entity and Evidence Guided Relation Extraction for DocRED",
            "url": "https://arxiv.org/abs/2008.12283v1"
          },
          {
            "title": "Entity and Evidence Guided Relation Extraction for DocRED - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2020arXiv200812283H/abstract"
          },
          {
            "title": "Entity and Evidence Guided Relation Extraction for DocRED",
            "url": "https://www.catalyzex.com/paper/arxiv:2008.12283"
          },
          {
            "title": "[PDF] Entity and Evidence Guided Relation Extraction for DocRED | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Relation-Extraction-for-Huang-Qi/172678d3fb74bc56c9ac58f024b4eb43e0470e78"
          },
          {
            "title": "Entity and Evidence Guided Relation Extraction for DocRED - Paper Detail",
            "url": "https://deeplearn.org/arxiv/153393/entity-and-evidence-guided-relation-extraction-for-docred"
          },
          {
            "title": "(PDF) Entity and Evidence Guided Relation Extraction for DocRED",
            "url": "https://www.academia.edu/103732963/Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"
          },
          {
            "title": "Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management",
            "url": "https://dl.acm.org/doi/10.1145/3511808.3557313"
          },
          {
            "title": "Entity and Evidence Guided Relation Extraction for DocRED | DeepAI",
            "url": "https://deepai.org/publication/entity-and-evidence-guided-relation-extraction-for-docred"
          }
        ]
      },
      "I found the paper! Here's a summary of the search results for arxiv 2008.12283:\n\n**Title:** Entity and Evidence Guided Relation Extraction for DocRED\n\n**Authors:** Kevin Huang, Guangtao Wang, Tengyu Ma, and Jing Huang\n\n**Submission Date:** August 27, 2020\n\n**Summary:** The paper addresses document-level relation extraction, a challenging task which requires reasoning over multiple sentences in order to predict relations in a document. The authors propose a joint training framework called E2GRE (Entity and Evidence Guided Relation Extraction) for this task.\n\n**Key Approach:** The method has two main components:\n1. It introduces entity-guided sequences as inputs to a pre-trained language model (e.g. BERT, RoBERTa), which help the language model focus on areas of the document related to the entity.\n2. It guides the fine-tuning of the pre-trained language model by using its internal attention probabilities as additional features for evidence prediction.\n\n**Results:** The approach achieves state-of-the-art results on the public leaderboard across all metrics, showing that E2GRE is both effective and synergistic on relation extraction and evidence prediction.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2008.12283"
    ],
    "durationSeconds": 4.988001575000002
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T15:25:23.911Z_

<details><summary>↩ Tool result · `toolu_01WYftFNW2zYNzDZ8piXibgq`</summary>

```text
Web search results for query: "DocGNRE "document relation extraction" evidence generation natural language explanation"

Links: [{"title":"Evidence and Axial Attention Guided Document-level Relation Extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116"},{"title":"(PDF) Enhancing Document-Level Relation Extraction with Relation-Specific Entity Representation and Evidence Sentence Augmentation","url":"https://www.researchgate.net/publication/374298993_Enhancing_Document-Level_Relation_Extraction_with_Relation-Specific_Entity_Representation_and_Evidence_Sentence_Augmentation"},{"title":"Document-Level Relation Extraction with Path Reasoning | ACM Transactions on Asian and Low-Resource Language Information Processing","url":"https://dl.acm.org/doi/10.1145/3572898"},{"title":"Document-Level Relation Extraction with Reconstruction | Request PDF","url":"https://www.researchgate.net/publication/363410025_Document-Level_Relation_Extraction_with_Reconstruction"},{"title":"Document-level multiple relations extraction method via evidence guidance and relation correlation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494624011657"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Document-level relation extraction with entity mentions deep attention - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0885230823000931"},{"title":"Document-level relation extraction based on sememe knowledge-enhanced abstract meaning representation and reasoning | Complex & Intelligent Systems","url":"https://link.springer.com/article/10.1007/s40747-023-01084-6"},{"title":"Document-Level Relation Extraction with Sentences Importance Estimation and Focusing - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.212/"},{"title":"Document-level relation extraction via commonsense knowledge enhanced graph representation learning | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-024-05985-y"}]

Based on the search results, I found information about document-level relation extraction and evidence generation, though the specific "DocGNRE" system wasn't directly featured in these results. However, I can provide you with relevant context about document-level relation extraction with evidence generation and natural language explanations:

## Document-Level Relation Extraction Overview

Document-level Relation Extraction (DocRE) aims to extract semantic relations between entity pairs, spanning multiple sentences, paragraphs or even the entire document. DocRE aims to reason about complex relational facts among entities by reading, inferring, and aggregating among entities over multiple sentences in a document.

## Evidence Generation and Guidance

A key aspect of modern document-level relation extraction involves evidence identification. Evidence selection refers to identifying and selecting relevant sentences or text from a document that provides crucial information to determine relationships between entities. A method called DREEAM uses evidence information to guide the attention modules to emphasize important evidence.

The SIEF framework for DocRE designs a sentence importance score and a sentence focusing loss, encouraging DocRE models to focus on evidence sentences.

## Related Approaches

E2GRE is a model designed for document-level relation extraction that tackles the challenge of handling relations spanning multiple sentences by jointly extracting relations and their supporting evidence sentences using BERT as an input encoder.

If you need more specific information about DocGNRE, you may want to search for the paper directly or provide additional context about the research you're investigating.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "6e0b1d9c-8b02-4d8b-9ff8-ed500fbd7f3f",
  "tool_use_result": {
    "query": "DocGNRE \"document relation extraction\" evidence generation natural language explanation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UxzhbH7JUz1yJHvchRBAHE",
        "content": [
          {
            "title": "Evidence and Axial Attention Guided Document-level Relation Extraction - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116"
          },
          {
            "title": "(PDF) Enhancing Document-Level Relation Extraction with Relation-Specific Entity Representation and Evidence Sentence Augmentation",
            "url": "https://www.researchgate.net/publication/374298993_Enhancing_Document-Level_Relation_Extraction_with_Relation-Specific_Entity_Representation_and_Evidence_Sentence_Augmentation"
          },
          {
            "title": "Document-Level Relation Extraction with Path Reasoning | ACM Transactions on Asian and Low-Resource Language Information Processing",
            "url": "https://dl.acm.org/doi/10.1145/3572898"
          },
          {
            "title": "Document-Level Relation Extraction with Reconstruction | Request PDF",
            "url": "https://www.researchgate.net/publication/363410025_Document-Level_Relation_Extraction_with_Reconstruction"
          },
          {
            "title": "Document-level multiple relations extraction method via evidence guidance and relation correlation - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S1568494624011657"
          },
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-025-11280-0"
          },
          {
            "title": "Document-level relation extraction with entity mentions deep attention - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0885230823000931"
          },
          {
            "title": "Document-level relation extraction based on sememe knowledge-enhanced abstract meaning representation and reasoning | Complex & Intelligent Systems",
            "url": "https://link.springer.com/article/10.1007/s40747-023-01084-6"
          },
          {
            "title": "Document-Level Relation Extraction with Sentences Importance Estimation and Focusing - ACL Anthology",
            "url": "https://aclanthology.org/2022.naacl-main.212/"
          },
          {
            "title": "Document-level relation extraction via commonsense knowledge enhanced graph representation learning | Applied Intelligence | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10489-024-05985-y"
          }
        ]
      },
      "Based on the search results, I found information about document-level relation extraction and evidence generation, though the specific \"DocGNRE\" system wasn't directly featured in these results. However, I can provide you with relevant context about document-level relation extraction with evidence generation and natural language explanations:\n\n## Document-Level Relation Extraction Overview\n\nDocument-level Relation Extraction (DocRE) aims to extract semantic relations between entity pairs, spanning multiple sentences, paragraphs or even the entire document. DocRE aims to reason about complex relational facts among entities by reading, inferring, and aggregating among entities over multiple sentences in a document.\n\n## Evidence Generation and Guidance\n\nA key aspect of modern document-level relation extraction involves evidence identification. Evidence selection refers to identifying and selecting relevant sentences or text from a document that provides crucial information to determine relationships between entities. A method called DREEAM uses evidence information to guide the attention modules to emphasize important evidence.\n\nThe SIEF framework for DocRE designs a sentence importance score and a sentence focusing loss, encouraging DocRE models to focus on evidence sentences.\n\n## Related Approaches\n\nE2GRE is a model designed for document-level relation extraction that tackles the challenge of handling relations spanning multiple sentences by jointly extracting relations and their supporting evidence sentences using BERT as an input encoder.\n\nIf you need more specific information about DocGNRE, you may want to search for the paper directly or provide additional context about the research you're investigating."
    ],
    "durationSeconds": 6.850953359999999
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T15:25:24.265Z_

<details><summary>↩ Tool result · `toolu_01AdcT4MdgmzpqxRT11gMxKB`</summary>

```text
Web search results for query: "COREX document-level relation extraction evidence arxiv aclanthology"

Links: [{"title":"A Comprehensive Survey on Document-Level Information ...","url":"https://aclanthology.org/2024.futured-1.6.pdf"},{"title":"[2303.03912] Document-level Relation Extraction with Cross-sentence Reasoning Graph","url":"https://arxiv.org/abs/2303.03912"},{"title":"EIDER: Empowering Document-level Relation Extraction ...","url":"https://aclanthology.org/2022.findings-acl.23.pdf"},{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10650330/"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Entity and Evidence Guided Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2021.repl4nlp-1.30/"},{"title":"A systematic review of relation extraction task since the emergence of","url":"https://arxiv.org/pdf/2511.03610"},{"title":"Rethinking Document-Level Relation Extraction","url":"https://aclanthology.org/2023.findings-acl.353.pdf"},{"title":"Multidisciplinary End-to-End Document-Level Relation Extraction from Scientific Literature | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-04627-7_15"}]

Based on the search results, I found information about COREX, a document-level relation extraction framework. Here are the key findings:

## COREX: Document-Level Relation Extraction Framework

COREX focuses on document-level relation extraction (DocRE), which involves identifying relationships between entities within a document and understanding relationships over longer distances, including across sentences or paragraphs.

### Key Features and Challenges Addressed:

A major challenge in DocRE is to focus on crucial evidence and bridge entities, defined as entities that link others in relationships spanning multiple sentences.

### Technical Approach:

The framework proposes a novel, efficient representation to support two-hop reasoning, supervised by evidence prediction and relation extraction, which notably improves long-distance reasoning capabilities in DocRE.

To address the issue of class imbalance in DocRE, the framework revises the Adaptive Focal Loss (AFL) and incorporates it, along with a Weighted Fusion Layer designed to optimize the utilization of evidence.

The search results indicate that COREX is a comprehensive framework designed to handle multi-hop reasoning and evidence-based prediction in document-level relation extraction, with specific innovations around evidence selection and class imbalance handling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "596eb404-22e9-4448-94f9-bce580e9952e",
  "tool_use_result": {
    "query": "COREX document-level relation extraction evidence arxiv aclanthology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NBh3Zbya6AVuiiq4BsgX8P",
        "content": [
          {
            "title": "A Comprehensive Survey on Document-Level Information ...",
            "url": "https://aclanthology.org/2024.futured-1.6.pdf"
          },
          {
            "title": "[2303.03912] Document-level Relation Extraction with Cross-sentence Reasoning Graph",
            "url": "https://arxiv.org/abs/2303.03912"
          },
          {
            "title": "EIDER: Empowering Document-level Relation Extraction ...",
            "url": "https://aclanthology.org/2022.findings-acl.23.pdf"
          },
          {
            "title": "Document-Level Relation Extraction with Global ...",
            "url": "https://aclanthology.org/2025.findings-acl.1002.pdf"
          },
          {
            "title": "COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/10650330/"
          },
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models",
            "url": "https://arxiv.org/html/2411.18157v1"
          },
          {
            "title": "Entity and Evidence Guided Document-Level Relation Extraction - ACL Anthology",
            "url": "https://aclanthology.org/2021.repl4nlp-1.30/"
          },
          {
            "title": "A systematic review of relation extraction task since the emergence of",
            "url": "https://arxiv.org/pdf/2511.03610"
          },
          {
            "title": "Rethinking Document-Level Relation Extraction",
            "url": "https://aclanthology.org/2023.findings-acl.353.pdf"
          },
          {
            "title": "Multidisciplinary End-to-End Document-Level Relation Extraction from Scientific Literature | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-04627-7_15"
          }
        ]
      },
      "Based on the search results, I found information about COREX, a document-level relation extraction framework. Here are the key findings:\n\n## COREX: Document-Level Relation Extraction Framework\n\nCOREX focuses on document-level relation extraction (DocRE), which involves identifying relationships between entities within a document and understanding relationships over longer distances, including across sentences or paragraphs.\n\n### Key Features and Challenges Addressed:\n\nA major challenge in DocRE is to focus on crucial evidence and bridge entities, defined as entities that link others in relationships spanning multiple sentences.\n\n### Technical Approach:\n\nThe framework proposes a novel, efficient representation to support two-hop reasoning, supervised by evidence prediction and relation extraction, which notably improves long-distance reasoning capabilities in DocRE.\n\nTo address the issue of class imbalance in DocRE, the framework revises the Adaptive Focal Loss (AFL) and incorporates it, along with a Weighted Fusion Layer designed to optimize the utilization of evidence.\n\nThe search results indicate that COREX is a comprehensive framework designed to handle multi-hop reasoning and evidence-based prediction in document-level relation extraction, with specific innovations around evidence selection and class imbalance handling."
    ],
    "durationSeconds": 6.697097636999999
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Let me now get more details on the remaining papers. I've found GEGA, CDER, EIDER, E2GRE (Entity and Evidence Guided), and COREX. Let me verify GEGA's venue, CDER's venue, and COREX's venue more precisely. DocGNRE wasn't found - let me search for it specifically. Also let me search for the EIDER authors more precisely.

I need to choose the 4 best gap-fill papers. The most relevant ones for "evidence supervision/retrieval in DocRE" are:


EIDER from ACL 2022 Findings with its evidence extraction and inference fusion approach, GEGA from an IEEE conference using evidence retrieval guided attention, CDER focusing on collaborative evidence retrieval, and E2GRE with its entity and evidence guidance. COREX appears less mainstream on IEEE Xplore, so I should verify the venues more carefully and reconsider which papers best match what the user originally asked for.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "2d8c9169-e11d-4e2d-bebd-6148aec09689",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHKoP1uG9rdn5sDWUexMU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 4953,
      "cache_read_input_tokens": 32950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4953
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

_source line 41_

继续搜索更多候选论文的细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "04a7774d-21e4-4956-b39c-39607134accc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHKoP1uG9rdn5sDWUexMU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 4953,
      "cache_read_input_tokens": 32950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4953
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

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CnJDdhzkPaGWXKhpbibhLa`</summary>

```json
{
  "query": "\"Evidence-aware Document-level Relation Extraction\" CIKM 2022 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "7b1d5be2-0fc6-4c11-b37f-7c918a1c9286",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHKoP1uG9rdn5sDWUexMU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 4953,
      "cache_read_input_tokens": 32950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4953
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

_source line 43_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FXE1tUgypAFgmTemL4JrmW`</summary>

```json
{
  "query": "GEGA \"Yanxu Mao\" document relation extraction venue conference 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "e23b785e-01a5-4c9c-bf47-84a9480c795c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHKoP1uG9rdn5sDWUexMU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 4953,
      "cache_read_input_tokens": 32950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4953
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GzEumWvSzq4fMM7wbbRo3W`</summary>

```json
{
  "query": "COREX \"Consistent Two-Hop Reasoning and Evidence Sentence Prediction\" document relation extraction authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "9b409642-f8b7-4d05-b3c2-5193960dda5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHKoP1uG9rdn5sDWUexMU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 4953,
      "cache_read_input_tokens": 32950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4953
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

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017sYDZmxb2fhDt3GmW4mEeb`</summary>

```json
{
  "query": "CDER \"Khai Phan Tran\" collaborative evidence retrieval venue PRICAI 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "5bec8c5b-0ab2-4d5d-a738-fba3e14c71bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHKoP1uG9rdn5sDWUexMU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 4953,
      "cache_read_input_tokens": 32950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4953
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

_source line 46 · 2026-05-17T15:25:45.606Z_

<details><summary>↩ Tool result · `toolu_01CnJDdhzkPaGWXKhpbibhLa`</summary>

```text
Web search results for query: ""Evidence-aware Document-level Relation Extraction" CIKM 2022 arxiv"

Links: [{"title":"Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557313"},{"title":"Evidence-aware Document-level Relation Extraction - PolyU Scholars Hub","url":"https://research.polyu.edu.hk/en/publications/evidence-aware-document-level-relation-extraction"},{"title":"Document-Level In-Context Few-Shot Relation Extraction via Pre-Trained Language Models","url":"https://arxiv.org/html/2310.11085v4"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"Rethinking Document-Level Relation Extraction: A Reality Check","url":"https://arxiv.org/html/2306.08953"},{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"Document-Level Relation Extraction Based on Heterogeneous Graph Reasoning | Proceedings of the 33rd ACM International Conference on Information and Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3627673.3679899"},{"title":"Evidence-aware Document-level Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=JMyPmI06JN"},{"title":"Document-Level Relation Extraction with Additional Evidence and Entity Type Information | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-981-97-5669-8_19"},{"title":"Improving Graph-based Document-Level Relation Extraction Model with Novel Graph Structure | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557615"}]

Based on the search results, I found information about the "Evidence-aware Document-level Relation Extraction" paper presented at CIKM 2022:

## Paper Overview

"Evidence-aware Document-level Relation Extraction" was published in CIKM 2022 - Proceedings of the 31st ACM International Conference on Information and Knowledge Management (pages 2311-2320).

## Research Focus

The paper addresses Document-level Relation Extraction (RE), which aims at identifying relations of multiple entity pairs in a document. The key insight is that in most cases, a relational fact can be expressed sufficiently via a small subset of sentences from the document, namely evidence sentences.

## Citation Information

The paper's authors include Xu, Tianyu; Hua, Wen; Qu, Jianfeng and others. The paper's DOI is 10.1145/3511808.3557313.

The paper appears to be available through the ACM Digital Library and was presented at the conference held October 17-21, 2022 in Atlanta, United States.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "c00cd2bb-6fe7-4d71-9f43-aaf2b87b04b8",
  "tool_use_result": {
    "query": "\"Evidence-aware Document-level Relation Extraction\" CIKM 2022 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LXyc7UYteXMsj9TcvyFne7",
        "content": [
          {
            "title": "Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management",
            "url": "https://dl.acm.org/doi/10.1145/3511808.3557313"
          },
          {
            "title": "Evidence-aware Document-level Relation Extraction - PolyU Scholars Hub",
            "url": "https://research.polyu.edu.hk/en/publications/evidence-aware-document-level-relation-extraction"
          },
          {
            "title": "Document-Level In-Context Few-Shot Relation Extraction via Pre-Trained Language Models",
            "url": "https://arxiv.org/html/2310.11085v4"
          },
          {
            "title": "CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2504.06529"
          },
          {
            "title": "Rethinking Document-Level Relation Extraction: A Reality Check",
            "url": "https://arxiv.org/html/2306.08953"
          },
          {
            "title": "[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion",
            "url": "https://arxiv.org/abs/2106.08657"
          },
          {
            "title": "Document-Level Relation Extraction Based on Heterogeneous Graph Reasoning | Proceedings of the 33rd ACM International Conference on Information and Knowledge Management",
            "url": "https://dl.acm.org/doi/10.1145/3627673.3679899"
          },
          {
            "title": "Evidence-aware Document-level Relation Extraction | OpenReview",
            "url": "https://openreview.net/forum?id=JMyPmI06JN"
          },
          {
            "title": "Document-Level Relation Extraction with Additional Evidence and Entity Type Information | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-981-97-5669-8_19"
          },
          {
            "title": "Improving Graph-based Document-Level Relation Extraction Model with Novel Graph Structure | Proceedings of the 31st ACM International Conference on Information & Knowledge Management",
            "url": "https://dl.acm.org/doi/10.1145/3511808.3557615"
          }
        ]
      },
      "Based on the search results, I found information about the \"Evidence-aware Document-level Relation Extraction\" paper presented at CIKM 2022:\n\n## Paper Overview\n\n\"Evidence-aware Document-level Relation Extraction\" was published in CIKM 2022 - Proceedings of the 31st ACM International Conference on Information and Knowledge Management (pages 2311-2320).\n\n## Research Focus\n\nThe paper addresses Document-level Relation Extraction (RE), which aims at identifying relations of multiple entity pairs in a document. The key insight is that in most cases, a relational fact can be expressed sufficiently via a small subset of sentences from the document, namely evidence sentences.\n\n## Citation Information\n\nThe paper's authors include Xu, Tianyu; Hua, Wen; Qu, Jianfeng and others. The paper's DOI is 10.1145/3511808.3557313.\n\nThe paper appears to be available through the ACM Digital Library and was presented at the conference held October 17-21, 2022 in Atlanta, United States."
    ],
    "durationSeconds": 5.232328886999996
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-17T15:25:47.217Z_

<details><summary>↩ Tool result · `toolu_01FXE1tUgypAFgmTemL4JrmW`</summary>

```text
Web search results for query: "GEGA "Yanxu Mao" document relation extraction venue conference 2024"

Links: [{"title":"[2407.21384] GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction","url":"https://arxiv.org/abs/2407.21384"},{"title":"A Comprehensive Survey on Document-Level Information ...","url":"https://aclanthology.org/2024.futured-1.6.pdf"},{"title":"Anaphor Assisted Document-Level Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/376393382_Anaphor_Assisted_Document-Level_Relation_Extraction"},{"title":"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10889649/"},{"title":"Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-12099-8"},{"title":"Document-level relation extraction model guided by global information and external contextual knowledge | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-07467-5"},{"title":"GraphFormer: Document-Level Relation Extractor for Open Source Cyber Threat Intelligence by Peipei Liu, Yanxu Mao, Kaixiang Liu, Hongsong Zhu, Limin Sun :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6660730"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3674501"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Text2NKG: Fine-Grained N-ary Relation Extraction for ... - NIPS","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/305b2288122d46bf0641bdd86c9a7921-Paper-Conference.pdf"}]

Based on the search results, I found information about the GEGA paper by Yanxu Mao on document-level relation extraction:

GEGA is a novel model for document-level relation extraction (DocRE). The model leverages graph neural networks to construct multiple weight matrices, guiding attention allocation to evidence sentences, and employs multi-scale representation aggregation to enhance evidence retrieval (ER).

The GEGA model was evaluated on three widely used benchmark datasets: DocRED, Re-DocRED, and Revisit-DocRED. The experimental results indicate that the model achieved comprehensive improvements compared to the existing SOTA (state-of-the-art) model.

Regarding the venue, the paper by Mao Y, Chen X, Liu P, Cui T, Yue Z, Li Z on GEGA was published at ICASSP 2025—the 2025 IEEE International Conference on Acoustics, Speech and Signal Processing. The paper was initially posted on arXiv in July 2024, with a second version in September 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "19c515db-5e0c-411a-be91-825192e9c8f3",
  "tool_use_result": {
    "query": "GEGA \"Yanxu Mao\" document relation extraction venue conference 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SNaceeGyz5zGaUDuMT9x3W",
        "content": [
          {
            "title": "[2407.21384] GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction",
            "url": "https://arxiv.org/abs/2407.21384"
          },
          {
            "title": "A Comprehensive Survey on Document-Level Information ...",
            "url": "https://aclanthology.org/2024.futured-1.6.pdf"
          },
          {
            "title": "Anaphor Assisted Document-Level Relation Extraction | Request PDF",
            "url": "https://www.researchgate.net/publication/376393382_Anaphor_Assisted_Document-Level_Relation_Extraction"
          },
          {
            "title": "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/10889649/"
          },
          {
            "title": "Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s00521-026-12099-8"
          },
          {
            "title": "Document-level relation extraction model guided by global information and external contextual knowledge | The Journal of Supercomputing | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11227-025-07467-5"
          },
          {
            "title": "GraphFormer: Document-Level Relation Extractor for Open Source Cyber Threat Intelligence by Peipei Liu, Yanxu Mao, Kaixiang Liu, Hongsong Zhu, Limin Sun :: SSRN",
            "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6660730"
          },
          {
            "title": "A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3674501"
          },
          {
            "title": "Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11704-024-40555-y"
          },
          {
            "title": "Text2NKG: Fine-Grained N-ary Relation Extraction for ... - NIPS",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/305b2288122d46bf0641bdd86c9a7921-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the GEGA paper by Yanxu Mao on document-level relation extraction:\n\nGEGA is a novel model for document-level relation extraction (DocRE). The model leverages graph neural networks to construct multiple weight matrices, guiding attention allocation to evidence sentences, and employs multi-scale representation aggregation to enhance evidence retrieval (ER).\n\nThe GEGA model was evaluated on three widely used benchmark datasets: DocRED, Re-DocRED, and Revisit-DocRED. The experimental results indicate that the model achieved comprehensive improvements compared to the existing SOTA (state-of-the-art) model.\n\nRegarding the venue, the paper by Mao Y, Chen X, Liu P, Cui T, Yue Z, Li Z on GEGA was published at ICASSP 2025—the 2025 IEEE International Conference on Acoustics, Speech and Signal Processing. The paper was initially posted on arXiv in July 2024, with a second version in September 2024."
    ],
    "durationSeconds": 5.948248779999995
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-17T15:25:48.492Z_

<details><summary>↩ Tool result · `toolu_01GzEumWvSzq4fMM7wbbRo3W`</summary>

```text
Web search results for query: "COREX "Consistent Two-Hop Reasoning and Evidence Sentence Prediction" document relation extraction authors venue"

Links: [{"title":"COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10650330/"},{"title":"Knowledge enhancement and full utilization of document information for document-level biomedical relation extraction | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-32931-w"},{"title":"Multi-Relation Extraction in Entity Pairs using Global Context","url":"https://arxiv.org/html/2507.22926"},{"title":"Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation | Request PDF","url":"https://www.researchgate.net/publication/361058021_Document-Level_Relation_Extraction_with_Adaptive_Focal_Loss_and_Knowledge_Distillation"},{"title":"MRN: A Locally and Globally Mention-Based Reasoning Network for Document-Level Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/353492714_MRN_A_Locally_and_Globally_Mention-Based_Reasoning_Network_for_Document-Level_Relation_Extraction"},{"title":"[2303.03912] Document-level Relation Extraction with Cross-sentence Reasoning Graph","url":"https://arxiv.org/abs/2303.03912"},{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"},{"title":"Document-Level Relation Extraction with Sentences ...","url":"https://aclanthology.org/2022.naacl-main.212.pdf"},{"title":"Document-Level Relation Extraction with Cross-sentence Reasoning Graph | Request PDF","url":"https://www.researchgate.net/publication/371085966_Document-Level_Relation_Extraction_with_Cross-sentence_Reasoning_Graph"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-relation-extraction"}]

Based on the search results, I found information about COREX:

**Title:** COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction

**Authors:** S. Zhao and C. Li

**Venue:** 2024 International Joint Conference on Neural Networks (IJCNN)

**Overview:** The framework addresses the challenge in document-level relation extraction of identifying crucial evidence and bridge entities that link other entities across multiple sentences, using a novel representation that supports two-hop reasoning that is supervised by evidence prediction and relation extraction. The framework also addresses class imbalance through a revised Adaptive Focal Loss and includes a Weighted Fusion Layer designed to optimize the utilization of evidence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "163a93d3-2cb5-4672-8a79-462f593cfc70",
  "tool_use_result": {
    "query": "COREX \"Consistent Two-Hop Reasoning and Evidence Sentence Prediction\" document relation extraction authors venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D7jVcycF5ynqjpGjdM6Ftd",
        "content": [
          {
            "title": "COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/10650330/"
          },
          {
            "title": "Knowledge enhancement and full utilization of document information for document-level biomedical relation extraction | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-32931-w"
          },
          {
            "title": "Multi-Relation Extraction in Entity Pairs using Global Context",
            "url": "https://arxiv.org/html/2507.22926"
          },
          {
            "title": "Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation | Request PDF",
            "url": "https://www.researchgate.net/publication/361058021_Document-Level_Relation_Extraction_with_Adaptive_Focal_Loss_and_Knowledge_Distillation"
          },
          {
            "title": "MRN: A Locally and Globally Mention-Based Reasoning Network for Document-Level Relation Extraction | Request PDF",
            "url": "https://www.researchgate.net/publication/353492714_MRN_A_Locally_and_Globally_Mention-Based_Reasoning_Network_for_Document-Level_Relation_Extraction"
          },
          {
            "title": "[2303.03912] Document-level Relation Extraction with Cross-sentence Reasoning Graph",
            "url": "https://arxiv.org/abs/2303.03912"
          },
          {
            "title": "Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"
          },
          {
            "title": "Document-Level Relation Extraction with Sentences ...",
            "url": "https://aclanthology.org/2022.naacl-main.212.pdf"
          },
          {
            "title": "Document-Level Relation Extraction with Cross-sentence Reasoning Graph | Request PDF",
            "url": "https://www.researchgate.net/publication/371085966_Document-Level_Relation_Extraction_with_Cross-sentence_Reasoning_Graph"
          },
          {
            "title": "Document-Level Relation Extraction",
            "url": "https://www.emergentmind.com/topics/document-level-relation-extraction"
          }
        ]
      },
      "Based on the search results, I found information about COREX:\n\n**Title:** COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction\n\n**Authors:** S. Zhao and C. Li\n\n**Venue:** 2024 International Joint Conference on Neural Networks (IJCNN)\n\n**Overview:** The framework addresses the challenge in document-level relation extraction of identifying crucial evidence and bridge entities that link other entities across multiple sentences, using a novel representation that supports two-hop reasoning that is supervised by evidence prediction and relation extraction. The framework also addresses class imbalance through a revised Adaptive Focal Loss and includes a Weighted Fusion Layer designed to optimize the utilization of evidence."
    ],
    "durationSeconds": 6.163683638000002
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-17T15:25:49.270Z_

<details><summary>↩ Tool result · `toolu_017sYDZmxb2fhDt3GmW4mEeb`</summary>

```text
Web search results for query: "CDER "Khai Phan Tran" collaborative evidence retrieval venue PRICAI 2024"

Links: [{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529v1"},{"title":"CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/content/pdf/10.1007/978-981-97-4982-9_3"},{"title":"[2504.06529] CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/abs/2504.06529"},{"title":"dblp: Khai Phan Tran","url":"https://dblp.org/pid/316/8206.html"},{"title":"[PDF] CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CDER:-Collaborative-Evidence-Retrieval-for-Relation-Tran-Li/07f36e6f29c07f0edce7465f4d005bd34ac659ce"},{"title":"(PDF) CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/390638674_CDER_Collaborative_Evidence_Retrieval_for_Document-level_Relation_Extraction"}]

Based on the search results, I found information about CDER and Khai Phan Tran, though I should note that the venue mentioned in the results differs slightly from what you specified:

CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction was authored by Khai Phan Tran and Xue Li. However, the paper was published in 2024 at ACIIDS 2024 (the 16th Asian Conference on Intelligent Information and Database Systems), not PRICAI 2024.

CDER is a novel evidence retrieval framework that employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval. The framework addresses Document-level Relation Extraction (DocRE), which involves identifying relations between entities across multiple sentences in a document, with evidence sentences being crucial for precise entity pair relationships identification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "fe99072f-4975-4ba6-b3fb-f6237e732018",
  "tool_use_result": {
    "query": "CDER \"Khai Phan Tran\" collaborative evidence retrieval venue PRICAI 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AThqpWXvYfJ5HX1ve4K2Uy",
        "content": [
          {
            "title": "CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2504.06529v1"
          },
          {
            "title": "CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Springer Nature Link",
            "url": "https://link.springer.com/content/pdf/10.1007/978-981-97-4982-9_3"
          },
          {
            "title": "[2504.06529] CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction",
            "url": "https://arxiv.org/abs/2504.06529"
          },
          {
            "title": "dblp: Khai Phan Tran",
            "url": "https://dblp.org/pid/316/8206.html"
          },
          {
            "title": "[PDF] CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/CDER:-Collaborative-Evidence-Retrieval-for-Relation-Tran-Li/07f36e6f29c07f0edce7465f4d005bd34ac659ce"
          },
          {
            "title": "(PDF) CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction",
            "url": "https://www.researchgate.net/publication/390638674_CDER_Collaborative_Evidence_Retrieval_for_Document-level_Relation_Extraction"
          }
        ]
      },
      "Based on the search results, I found information about CDER and Khai Phan Tran, though I should note that the venue mentioned in the results differs slightly from what you specified:\n\nCDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction was authored by Khai Phan Tran and Xue Li. However, the paper was published in 2024 at ACIIDS 2024 (the 16th Asian Conference on Intelligent Information and Database Systems), not PRICAI 2024.\n\nCDER is a novel evidence retrieval framework that employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval. The framework addresses Document-level Relation Extraction (DocRE), which involves identifying relations between entities across multiple sentences in a document, with evidence sentences being crucial for precise entity pair relationships identification."
    ],
    "durationSeconds": 6.314764993000004
  }
}
```

</details>

---

### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information for the verification. Let me compile the results.

Papers verified:
1. DREEAM - Ma et al., EACL 2023, arXiv: 2302.08675 ✓
2. SAIS - Xiao et al., NAACL 2022, arXiv: 2109.12093 ✓

For gap-fill, the most relevant 4 papers from the candidates:
1. EIDER - Xie et al., Findings of ACL 2022, arXiv: 2106.08657 - very relevant (evidence extraction + inference fusion)


2. GEGA - Mao et al., ICASSP 2025, arXiv: 2407.21384 - evidence retrieval guided attention
3. CDER - Tran & Li, ACIIDS 2024, arXiv: 2504.06529 - collaborative evidence retrieval
4. "Evidence-aware Document-level Relation Extraction" - Xu et al., CIKM 2022 - evidence-aware approach

I'm also noting COREX, E2GRE, and a few other candidates that incorporate two-hop reasoning and entity-guided evidence mechanisms, though these are slightly less central to the core gap.

Looking at which papers would be most impactful to cite, EIDER stands out as the strongest choice given its publication at ACL Findings and direct focus on evidence extraction paired with inference fusion. The CIKM 2022 evidence-aware paper is also quite relevant for its venue prestige and direct alignment with the task.

For the remaining two slots, I'm weighing GEGA's recent work on evidence-guided attention mechanisms against CDER's focus on collaborative evidence retrieval, though both are somewhat less established than the top tier options. I should also verify E2GRE's publication status—it appears to have been published at RepL4NLP 2021 workshop rather than just existing as an arXiv preprint, which would make it a legitimate venue publication worth considering.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "24a6bb42-e34e-40c4-b51d-fd0e06617323",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaUEEbDEAnZe4eafzhSa1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4921,
      "cache_read_input_tokens": 37903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4921
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

_source line 51_

最后确认一下"Evidence-aware"论文作者信息和 EIDER 的详细信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "592185fe-bb7a-49f4-b038-8bc56c98c64b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaUEEbDEAnZe4eafzhSa1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4921,
      "cache_read_input_tokens": 37903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4921
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

_source line 52_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RuSjnUtjKD4kFt8WMDWvax`</summary>

```json
{
  "query": "\"Evidence-aware Document-level Relation Extraction\" Xu Hua Qu CIKM 2022 authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "114decd3-ebb4-4b1e-b48e-c7e1433d4e98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaUEEbDEAnZe4eafzhSa1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4921,
      "cache_read_input_tokens": 37903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4921
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0118nQHBgN7YxC1qZzGjkT8w`</summary>

```json
{
  "query": "EIDER \"Yiqing Xie\" \"Jiaming Shen\" Findings ACL 2022 arxiv 2106.08657"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "c601cf36-e737-499f-998c-7f351031c45d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaUEEbDEAnZe4eafzhSa1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4921,
      "cache_read_input_tokens": 37903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4921
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

_source line 54 · 2026-05-17T15:26:14.508Z_

<details><summary>↩ Tool result · `toolu_01RuSjnUtjKD4kFt8WMDWvax`</summary>

```text
Web search results for query: ""Evidence-aware Document-level Relation Extraction" Xu Hua Qu CIKM 2022 authors full list"

Links: [{"title":"Evidence-aware Document-level Relation Extraction - PolyU Scholars Hub","url":"https://research.polyu.edu.hk/en/publications/evidence-aware-document-level-relation-extraction"},{"title":"Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557313"},{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"},{"title":"Evidence-aware Document-level Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=JMyPmI06JN"},{"title":"Document-level relation extraction via commonsense knowledge enhanced graph representation learning | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-024-05985-y"},{"title":"[PDF] Entity and Evidence Guided Relation Extraction for DocRED | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Relation-Extraction-for-Huang-Qi/172678d3fb74bc56c9ac58f024b4eb43e0470e78"},{"title":"Evidence Reasoning and Curriculum Learning for Document-Level Relation Extraction | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10174655/"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-relation-extraction"},{"title":"Document-level relation extraction via commonsense knowledge enhanced graph representation learning: Document-level relation extraction via commonsense knowledge...: Applied Intelligence: Vol 55, No 2","url":"https://dl.acm.org/doi/10.1007/s10489-024-05985-y"},{"title":"Document-level relation extraction using evidence reasoning on RST-GRAPH | Request PDF","url":"https://www.researchgate.net/publication/353031046_Document-level_relation_extraction_using_evidence_reasoning_on_RST-GRAPH"}]

Based on the search results, I found the full list of authors for the paper "Evidence-aware Document-level Relation Extraction" published at CIKM 2022:

The authors are: Tianyu Xu, Wen Hua, Jianfeng Qu, Zhixu Li, Jiajie Xu, An Liu, and Lei Zhao.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "dca8a9a1-0f5a-4e4f-b146-efbd52138eaf",
  "tool_use_result": {
    "query": "\"Evidence-aware Document-level Relation Extraction\" Xu Hua Qu CIKM 2022 authors full list",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W7fZ1yf1HGFJDvRGbfPHTi",
        "content": [
          {
            "title": "Evidence-aware Document-level Relation Extraction - PolyU Scholars Hub",
            "url": "https://research.polyu.edu.hk/en/publications/evidence-aware-document-level-relation-extraction"
          },
          {
            "title": "Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management",
            "url": "https://dl.acm.org/doi/10.1145/3511808.3557313"
          },
          {
            "title": "Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"
          },
          {
            "title": "Evidence-aware Document-level Relation Extraction | OpenReview",
            "url": "https://openreview.net/forum?id=JMyPmI06JN"
          },
          {
            "title": "Document-level relation extraction via commonsense knowledge enhanced graph representation learning | Applied Intelligence | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10489-024-05985-y"
          },
          {
            "title": "[PDF] Entity and Evidence Guided Relation Extraction for DocRED | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Relation-Extraction-for-Huang-Qi/172678d3fb74bc56c9ac58f024b4eb43e0470e78"
          },
          {
            "title": "Evidence Reasoning and Curriculum Learning for Document-Level Relation Extraction | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/10174655/"
          },
          {
            "title": "Document-Level Relation Extraction",
            "url": "https://www.emergentmind.com/topics/document-level-relation-extraction"
          },
          {
            "title": "Document-level relation extraction via commonsense knowledge enhanced graph representation learning: Document-level relation extraction via commonsense knowledge...: Applied Intelligence: Vol 55, No 2",
            "url": "https://dl.acm.org/doi/10.1007/s10489-024-05985-y"
          },
          {
            "title": "Document-level relation extraction using evidence reasoning on RST-GRAPH | Request PDF",
            "url": "https://www.researchgate.net/publication/353031046_Document-level_relation_extraction_using_evidence_reasoning_on_RST-GRAPH"
          }
        ]
      },
      "Based on the search results, I found the full list of authors for the paper \"Evidence-aware Document-level Relation Extraction\" published at CIKM 2022:\n\nThe authors are: Tianyu Xu, Wen Hua, Jianfeng Qu, Zhixu Li, Jiajie Xu, An Liu, and Lei Zhao."
    ],
    "durationSeconds": 3.3609927860000024
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-17T15:26:19.069Z_

<details><summary>↩ Tool result · `toolu_0118nQHBgN7YxC1qZzGjkT8w`</summary>

```text
Web search results for query: "EIDER "Yiqing Xie" "Jiaming Shen" Findings ACL 2022 arxiv 2106.08657"

Links: [{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"Jiaming Shen - ACL Anthology","url":"https://aclanthology.org/people/jiaming-shen/"},{"title":"Eider: Evidence-enhanced Document-level Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/352477694_Eider_Evidence-enhanced_Document-level_Relation_Extraction"},{"title":"GitHub - yiqingxyq/Eider: Source code for paper \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", ACL Findings, 2022","url":"https://github.com/yiqingxyq/Eider"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.23/"},{"title":"[PDF] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Eider:-Empowering-Document-level-Relation-with-and-Xie-Shen/dbf1e5a17b3adead7016eb52ddc3007673ed382f"},{"title":"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Request PDF","url":"https://www.researchgate.net/publication/361056993_Eider_Empowering_Document-level_Relation_Extraction_with_Efficient_Evidence_Extraction_and_Inference-stage_Fusion"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2204.01320"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=235&show=1000"}]

Based on the search results, I found information about the EIDER paper:

## Overview
EIDER is an evidence-enhanced framework that empowers document-level relation extraction (DocRE) by efficiently extracting evidence and effectively fusing the extracted evidence in inference, with a lightweight evidence extraction model that is efficient in both memory and runtime.

## Key Findings
Typical DocRE methods blindly take the full document as input, while a subset of the sentences in the document, noted as the evidence, are often sufficient for humans to predict the relation of an entity pair.

The framework makes RE predictions on both extracted evidence and the full document, then fuses the predictions through a blending layer.

Training the evidence model on silver labels constructed by heuristic rules can lead to better RE performance.

## Empirical Results
Extensive experiments show that Eider outperforms state-of-the-art methods on three benchmark datasets (e.g., by 1.37/1.26 Ign F1/F1 on DocRED).

## Publication
The paper was published in the Findings of the Association for Computational Linguistics: ACL 2022. The arXiv paper is 2106.08657, authored by Yiqing Xie, Jiaming Shen, Sha Li, Yuning Mao, and Jiawei Han.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "76ab610c-bb83-496d-86e1-1eb81da17812",
  "tool_use_result": {
    "query": "EIDER \"Yiqing Xie\" \"Jiaming Shen\" Findings ACL 2022 arxiv 2106.08657",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YRtiTjMC5vSMxTt725h411",
        "content": [
          {
            "title": "[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion",
            "url": "https://arxiv.org/abs/2106.08657"
          },
          {
            "title": "Jiaming Shen - ACL Anthology",
            "url": "https://aclanthology.org/people/jiaming-shen/"
          },
          {
            "title": "Eider: Evidence-enhanced Document-level Relation Extraction | Request PDF",
            "url": "https://www.researchgate.net/publication/352477694_Eider_Evidence-enhanced_Document-level_Relation_Extraction"
          },
          {
            "title": "GitHub - yiqingxyq/Eider: Source code for paper \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\", ACL Findings, 2022",
            "url": "https://github.com/yiqingxyq/Eider"
          },
          {
            "title": "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion - ACL Anthology",
            "url": "https://aclanthology.org/2022.findings-acl.23/"
          },
          {
            "title": "[PDF] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Eider:-Empowering-Document-level-Relation-with-and-Xie-Shen/dbf1e5a17b3adead7016eb52ddc3007673ed382f"
          },
          {
            "title": "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Request PDF",
            "url": "https://www.researchgate.net/publication/361056993_Eider_Empowering_Document-level_Relation_Extraction_with_Efficient_Evidence_Extraction_and_Inference-stage_Fusion"
          },
          {
            "title": "Arxiv",
            "url": "https://arxiv.org/pdf/2204.01320"
          },
          {
            "title": "arXiv.org e-Print archive",
            "url": "https://arxiv.org/"
          },
          {
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/pastweek?skip=235&show=1000"
          }
        ]
      },
      "Based on the search results, I found information about the EIDER paper:\n\n## Overview\nEIDER is an evidence-enhanced framework that empowers document-level relation extraction (DocRE) by efficiently extracting evidence and effectively fusing the extracted evidence in inference, with a lightweight evidence extraction model that is efficient in both memory and runtime.\n\n## Key Findings\nTypical DocRE methods blindly take the full document as input, while a subset of the sentences in the document, noted as the evidence, are often sufficient for humans to predict the relation of an entity pair.\n\nThe framework makes RE predictions on both extracted evidence and the full document, then fuses the predictions through a blending layer.\n\nTraining the evidence model on silver labels constructed by heuristic rules can lead to better RE performance.\n\n## Empirical Results\nExtensive experiments show that Eider outperforms state-of-the-art methods on three benchmark datasets (e.g., by 1.37/1.26 Ign F1/F1 on DocRED).\n\n## Publication\nThe paper was published in the Findings of the Association for Computational Linguistics: ACL 2022. The arXiv paper is 2106.08657, authored by Yiqing Xie, Jiaming Shen, Sha Li, Yuning Mao, and Jiawei Han."
    ],
    "durationSeconds": 6.991302108999997
  }
}
```

</details>

---

### Assistant

_source line 56_

所有论文验证完毕。以下是 6 篇验证结果：

---

## [DREEAM]
- title: DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction
- authors: Youmi Ma, An Wang, Naoaki Okazaki
- venue: EACL 2023
- year: 2023
- arxiv: 2302.08675
- doi: 10.18653/v1/2023.eacl-main.145
- bibtex_key: ma2023dreeam
- verified: true
- relevance: 首次将 evidence 作为监督信号引导 attention 模块，并提出 evidence retrieval 自训练策略
- verification_note: 预期信息全部正确，第一作者 Youmi Ma (not Tan)，原始预期 "Tan et al." 有误

## [SAIS]
- title: SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction
- authors: Yuxin Xiao, Zecheng Zhang, Yuning Mao, Carl Yang, Jiawei Han
- venue: NAACL 2022
- year: 2022
- arxiv: 2109.12093
- doi: 10.18653/v1/2022.naacl-main.171
- bibtex_key: xiao2022sais
- verified: true
- relevance: 通过监督中间步骤（evidence retrieval + entity typing）提升 DocRE，并利用 evidence 做数据增强和 ensemble 推理
- verification_note: 预期信息全部正确，第一作者 Xiao 确认

## [EIDER]
- title: Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion
- authors: Yiqing Xie, Jiaming Shen, Sha Li, Yuning Mao, Jiawei Han
- venue: Findings of ACL 2022
- year: 2022
- arxiv: 2106.08657
- doi: 10.18653/v1/2022.findings-acl.23
- bibtex_key: xie2022eider
- verified: true
- relevance: 联合训练轻量 evidence extraction 模型，推理阶段融合 evidence 预测与全文预测，是 evidence-enhanced DocRE 的代表工作
- verification_note: 不在原始候选列表中，但与 evidence-based DocRE 高度相关且发表于 top venue，替换未找到的 DocGNRE

## [Evidence-aware DocRE]
- title: Evidence-aware Document-level Relation Extraction
- authors: Tianyu Xu, Wen Hua, Jianfeng Qu, Zhixu Li, Jiajie Xu, An Liu, Lei Zhao
- venue: CIKM 2022
- year: 2022
- arxiv: not found
- doi: 10.1145/3511808.3557313
- bibtex_key: xu2022evidenceaware
- verified: true
- relevance: 直接将 evidence awareness 融入 DocRE 模型设计，evidence sentence 子集即可预测 entity pair 关系
- verification_note: 原始候选列表中的 "Evidence-aware Document-level RE"，无 arXiv 预印本，仅在 ACM DL 发表

## [GEGA]
- title: GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction
- authors: Yanxu Mao, Xiaolin Chen, Peipei Liu, Tiehan Cui, Zibo Yue, Zhixiao Li
- venue: ICASSP 2025
- year: 2025
- arxiv: 2407.21384
- doi: 10.1109/ICASSP49660.2025.10889649
- bibtex_key: mao2025gega
- verified: true
- relevance: 构建于 DREEAM 之上，用 GCN 构造多权重矩阵引导 attention 到 evidence sentences，在 DocRED/Re-DocRED 上超越 DREEAM
- verification_note: 原始候选列表中的 GEGA，arXiv 预印本 2024 年 7 月，正式发表于 ICASSP 2025

## [CDER]
- title: CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction
- authors: Khai Phan Tran, Xue Li
- venue: ACIIDS 2024 (Springer LNCS)
- year: 2024
- arxiv: 2504.06529
- doi: 10.1007/978-981-97-4982-9_3
- bibtex_key: tran2024cder
- verified: true
- relevance: 将文档建模为二部图捕捉 entity pair 间的协作 evidence 检索模式，专注于 evidence retrieval 子任务
- verification_note: 原始候选列表中的 CDER，arXiv 版本为 2025 年 4 月更新版，会议发表于 ACIIDS 2024

---

**汇总**：
- 6/6 全部 verified
- DREEAM 预期作者 "Tan et al." 有误，实际为 Ma et al.
- DocGNRE 未能检索到对应论文，用 EIDER (Findings of ACL 2022) 替换，该论文与 evidence-based DocRE 直接相关且 venue 更强
- COREX (IJCNN 2024) 和 E2GRE (arXiv 2020) 也与 evidence 相关但 venue 较弱或未正式发表，未纳入最终 6 篇

Sources:
- [DREEAM - arXiv](https://arxiv.org/abs/2302.08675)
- [DREEAM - ACL Anthology](https://aclanthology.org/2023.eacl-main.145/)
- [SAIS - ACL Anthology](https://aclanthology.org/2022.naacl-main.171/)
- [SAIS - arXiv](https://arxiv.org/abs/2109.12093)
- [EIDER - ACL Anthology](https://aclanthology.org/2022.findings-acl.23/)
- [EIDER - arXiv](https://arxiv.org/abs/2106.08657)
- [Evidence-aware DocRE - ACM DL](https://dl.acm.org/doi/10.1145/3511808.3557313)
- [GEGA - arXiv](https://arxiv.org/abs/2407.21384)
- [GEGA - IEEE Xplore](https://ieeexplore.ieee.org/document/10889649/)
- [CDER - arXiv](https://arxiv.org/abs/2504.06529)
- [CDER - Springer](https://link.springer.com/chapter/10.1007/978-981-97-4982-9_3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "uuid": "2ecaffc6-263e-45bc-a48c-d5d319efa3a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dcPxYSXxCRUzSoqZAnpoz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2813,
      "cache_read_input_tokens": 42824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2813
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

_source line 57_

所有论文验证完毕。以下是 6 篇验证结果：

---

## [DREEAM]
- title: DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction
- authors: Youmi Ma, An Wang, Naoaki Okazaki
- venue: EACL 2023
- year: 2023
- arxiv: 2302.08675
- doi: 10.18653/v1/2023.eacl-main.145
- bibtex_key: ma2023dreeam
- verified: true
- relevance: 首次将 evidence 作为监督信号引导 attention 模块，并提出 evidence retrieval 自训练策略
- verification_note: 预期信息全部正确，第一作者 Youmi Ma (not Tan)，原始预期 "Tan et al." 有误

## [SAIS]
- title: SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction
- authors: Yuxin Xiao, Zecheng Zhang, Yuning Mao, Carl Yang, Jiawei Han
- venue: NAACL 2022
- year: 2022
- arxiv: 2109.12093
- doi: 10.18653/v1/2022.naacl-main.171
- bibtex_key: xiao2022sais
- verified: true
- relevance: 通过监督中间步骤（evidence retrieval + entity typing）提升 DocRE，并利用 evidence 做数据增强和 ensemble 推理
- verification_note: 预期信息全部正确，第一作者 Xiao 确认

## [EIDER]
- title: Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion
- authors: Yiqing Xie, Jiaming Shen, Sha Li, Yuning Mao, Jiawei Han
- venue: Findings of ACL 2022
- year: 2022
- arxiv: 2106.08657
- doi: 10.18653/v1/2022.findings-acl.23
- bibtex_key: xie2022eider
- verified: true
- relevance: 联合训练轻量 evidence extraction 模型，推理阶段融合 evidence 预测与全文预测，是 evidence-enhanced DocRE 的代表工作
- verification_note: 不在原始候选列表中，但与 evidence-based DocRE 高度相关且发表于 top venue，替换未找到的 DocGNRE

## [Evidence-aware DocRE]
- title: Evidence-aware Document-level Relation Extraction
- authors: Tianyu Xu, Wen Hua, Jianfeng Qu, Zhixu Li, Jiajie Xu, An Liu, Lei Zhao
- venue: CIKM 2022
- year: 2022
- arxiv: not found
- doi: 10.1145/3511808.3557313
- bibtex_key: xu2022evidenceaware
- verified: true
- relevance: 直接将 evidence awareness 融入 DocRE 模型设计，evidence sentence 子集即可预测 entity pair 关系
- verification_note: 原始候选列表中的 "Evidence-aware Document-level RE"，无 arXiv 预印本，仅在 ACM DL 发表

## [GEGA]
- title: GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction
- authors: Yanxu Mao, Xiaolin Chen, Peipei Liu, Tiehan Cui, Zibo Yue, Zhixiao Li
- venue: ICASSP 2025
- year: 2025
- arxiv: 2407.21384
- doi: 10.1109/ICASSP49660.2025.10889649
- bibtex_key: mao2025gega
- verified: true
- relevance: 构建于 DREEAM 之上，用 GCN 构造多权重矩阵引导 attention 到 evidence sentences，在 DocRED/Re-DocRED 上超越 DREEAM
- verification_note: 原始候选列表中的 GEGA，arXiv 预印本 2024 年 7 月，正式发表于 ICASSP 2025

## [CDER]
- title: CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction
- authors: Khai Phan Tran, Xue Li
- venue: ACIIDS 2024 (Springer LNCS)
- year: 2024
- arxiv: 2504.06529
- doi: 10.1007/978-981-97-4982-9_3
- bibtex_key: tran2024cder
- verified: true
- relevance: 将文档建模为二部图捕捉 entity pair 间的协作 evidence 检索模式，专注于 evidence retrieval 子任务
- verification_note: 原始候选列表中的 CDER，arXiv 版本为 2025 年 4 月更新版，会议发表于 ACIIDS 2024

---

**汇总**：
- 6/6 全部 verified
- DREEAM 预期作者 "Tan et al." 有误，实际为 Ma et al.
- DocGNRE 未能检索到对应论文，用 EIDER (Findings of ACL 2022) 替换，该论文与 evidence-based DocRE 直接相关且 venue 更强
- COREX (IJCNN 2024) 和 E2GRE (arXiv 2020) 也与 evidence 相关但 venue 较弱或未正式发表，未纳入最终 6 篇

Sources:
- [DREEAM - arXiv](https://arxiv.org/abs/2302.08675)
- [DREEAM - ACL Anthology](https://aclanthology.org/2023.eacl-main.145/)
- [SAIS - ACL Anthology](https://aclanthology.org/2022.naacl-main.171/)
- [SAIS - arXiv](https://arxiv.org/abs/2109.12093)
- [EIDER - ACL Anthology](https://aclanthology.org/2022.findings-acl.23/)
- [EIDER - arXiv](https://arxiv.org/abs/2106.08657)
- [Evidence-aware DocRE - ACM DL](https://dl.acm.org/doi/10.1145/3511808.3557313)
- [GEGA - arXiv](https://arxiv.org/abs/2407.21384)
- [GEGA - IEEE Xplore](https://ieeexplore.ieee.org/document/10889649/)
- [CDER - arXiv](https://arxiv.org/abs/2504.06529)
- [CDER - Springer](https://link.springer.com/chapter/10.1007/978-981-97-4982-9_3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 149864,
  "duration_api_ms": 228047,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "84ac3179-4b46-4bda-81c5-1c97f39f7952",
  "total_cost_usd": 1.002257,
  "usage": {
    "input_tokens": 3099,
    "cache_creation_input_tokens": 33796,
    "cache_read_input_tokens": 236168,
    "output_tokens": 5001,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33796,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1913,
        "cache_read_input_tokens": 42824,
        "cache_creation_input_tokens": 2813,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2813
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 302378,
      "outputTokens": 8010,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 19,
      "costUSD": 0.5324280000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3099,
      "outputTokens": 5001,
      "cacheReadInputTokens": 236168,
      "cacheCreationInputTokens": 33796,
      "webSearchRequests": 0,
      "costUSD": 0.46982900000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6f0b1f20-2d2a-4a31-8282-fb043cb19077"
}
```

</details>

---
