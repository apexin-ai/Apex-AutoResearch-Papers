# research arr submission requirements

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_research_arr_submission_requirements_20260517T073558.log`
- **Structured JSON:** [`11e129dbd112562aed04.json`](../../sessions/11/11e129dbd112562aed04.json)

## Before a recorded user message

47 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
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
  "uuid": "104cfff8-ab94-4835-93e3-39924c4b9cdb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/memory/"
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
    "resetsAt": 1779006600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1a2744ce-f243-4ee2-a02f-fb7632a2fba4",
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670"
}
```

---

### Assistant

_source line 4_

我来调研 ARR May cycle 的投稿要求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "11415be4-d87d-4207-bf58-6d47a599be82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Up4xhehXNZt59QGWqwpZHW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13016,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13016
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NRA72wL1YQGWM6yW4Fcbwq`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "febc4838-104b-4b16-8610-983e2e6de99a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Up4xhehXNZt59QGWqwpZHW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13016,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13016
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

_source line 6 · 2026-05-17T07:36:11.328Z_

<details><summary>↩ Tool result · `toolu_01NRA72wL1YQGWM6yW4Fcbwq`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
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
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "b4221e4c-01c4-4545-81a7-3ef4a8f11386",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me search for ARR submission guidelines and fetch the relevant pages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "394222c0-7dc0-49d8-b1e7-4481577d6704",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3joruCuFAtxyYFwQPeX6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 24857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1119
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

_source line 8_

Starting searches for ARR May cycle submission requirements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "17969ed1-2eda-4d5a-9d74-68a1daf0cba0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3joruCuFAtxyYFwQPeX6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 24857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1119
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NKtSNnReZTC28JD3PLa7Yk`</summary>

```json
{
  "query": "ACL Rolling Review 2025 2026 submission guidelines requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "999c2d24-0257-4b88-b9c4-089e65054e8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3joruCuFAtxyYFwQPeX6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 24857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1119
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_011hfA1jHeXftQuKSyu3LMac`</summary>

```json
{
  "query": "ARR May 2025 cycle deadline EMNLP 2026 submission format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "f1a5799c-ecde-4f48-b364-69065f4a563a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3joruCuFAtxyYFwQPeX6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 24857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1119
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N15v7tij5XyZokQTbEMVHq`</summary>

```json
{
  "query": "ACL responsible NLP research checklist 2025 2026 ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "d7bac343-8a42-43c4-9279-043f75471f41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3joruCuFAtxyYFwQPeX6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 24857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1119
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Saxr6JWG61axgHDcfJQhmb`</summary>

```json
{
  "query": "aclrollingreview.org submission guidelines page limits anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "0f0d9d30-ddc0-4df3-9058-92c16aa2d3ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3joruCuFAtxyYFwQPeX6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 24857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1119
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

_source line 13 · 2026-05-17T07:36:21.156Z_

<details><summary>↩ Tool result · `toolu_01NKtSNnReZTC28JD3PLa7Yk`</summary>

```text
Web search results for query: "ACL Rolling Review 2025 2026 submission guidelines requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here are the key ACL Rolling Review (ARR) 2025-2026 submission guidelines and requirements:

## Submission Requirements

All long, short, and theme papers must follow the ACL Author Guidelines and use the official ACL style template. Papers must not include authors' names and affiliations.

Submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected. All submitted papers are expected to describe original, completed and unpublished work, and reuse of text from other publications should not exceed 10% total tokens.

## Registration and Reviewing Requirements

All authors are expected to complete a registration form within 48 hours after submission deadline (for example, before May 21 EoD AoE for May 2025 cycle, where the submission deadline is May 19). Authors must have an updated OpenReview profile, including affiliation, semantic scholar link, dblp link, ACL anthology link, and an email address where they can receive OpenReview messages.

Starting in May 2025, all authors are expected to contribute to the review process, unless an exemption applies (e.g., authors new to the community, with insufficient experience, or already serving in another capacity). Reviewers are considered qualified if they have published at least two short or long papers in main ACL events or Findings, plus at least one more paper in the ACL Anthology or a major ML/AI venue.

## Penalties for Irresponsibility

Starting from May 2025, the authors who are deemed 'highly irresponsible' as reviewers or chairs may become ineligible to (re-)submit their work to ARR in the subsequent ARR cycle, or commit it to the upcoming *ACL conference.

## Submission Platform

Submission is electronic, using the OpenReview.net platform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "c5b112cf-dee2-4a49-9910-80d5e48313ad",
  "tool_use_result": {
    "query": "ACL Rolling Review 2025 2026 submission guidelines requirements",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NU2YAbe8qWWGpaY2RWozjp",
        "content": [
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Main Conference - ACL 2026",
            "url": "https://2026.aclweb.org/calls/main_conference_papers/"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authorchecklist"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "ACL Rolling Review | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/acl-rolling-review"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          }
        ]
      },
      "Based on the search results, here are the key ACL Rolling Review (ARR) 2025-2026 submission guidelines and requirements:\n\n## Submission Requirements\n\nAll long, short, and theme papers must follow the ACL Author Guidelines and use the official ACL style template. Papers must not include authors' names and affiliations.\n\nSubmissions that exceed the length requirements, or are missing a limitations section, will be desk rejected. All submitted papers are expected to describe original, completed and unpublished work, and reuse of text from other publications should not exceed 10% total tokens.\n\n## Registration and Reviewing Requirements\n\nAll authors are expected to complete a registration form within 48 hours after submission deadline (for example, before May 21 EoD AoE for May 2025 cycle, where the submission deadline is May 19). Authors must have an updated OpenReview profile, including affiliation, semantic scholar link, dblp link, ACL anthology link, and an email address where they can receive OpenReview messages.\n\nStarting in May 2025, all authors are expected to contribute to the review process, unless an exemption applies (e.g., authors new to the community, with insufficient experience, or already serving in another capacity). Reviewers are considered qualified if they have published at least two short or long papers in main ACL events or Findings, plus at least one more paper in the ACL Anthology or a major ML/AI venue.\n\n## Penalties for Irresponsibility\n\nStarting from May 2025, the authors who are deemed 'highly irresponsible' as reviewers or chairs may become ineligible to (re-)submit their work to ARR in the subsequent ARR cycle, or commit it to the upcoming *ACL conference.\n\n## Submission Platform\n\nSubmission is electronic, using the OpenReview.net platform."
    ],
    "durationSeconds": 5.933425001000002
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T07:36:22.648Z_

<details><summary>↩ Tool result · `toolu_01N15v7tij5XyZokQTbEMVHq`</summary>

```text
Web search results for query: "ACL responsible NLP research checklist 2025 2026 ARR"

Links: [{"title":"Responsible NLP Research Checklist","url":"https://aclrollingreview.org/static/responsibleNLPresearch.pdf"},{"title":"ARR Responsible NLP Research checklist","url":"http://aclrollingreview.org/responsibleNLPresearch/"},{"title":"EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/responsible-nlp-checklist-appendices"},{"title":"Responsible NLP Research Checklist","url":"https://openreview.net/attachment?id=yGhYSEj8ln0&name=responsible_NLP_research"},{"title":"Responsible NLP Research Checklist","url":"https://arxiv.org/html/2212.10503"},{"title":"Responsible NLP Checklist","url":"https://aclanthology.org/attachments/2025.emnlp-main.1573.checklist.pdf"},{"title":"EMNLP 2025 on X: \"For EMNLP authors, please note that the responsible NLP research checklists will be included with all papers published at EMNLP (and future *CL conferences) as an additional appendix, as per the updated ARR policy: https://t.co/Uwna96UMTT @ReviewAcl\" / X","url":"https://x.com/emnlpmeeting/status/1933196156995063863"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's what I found about the ACL Responsible NLP Research Checklist for 2025-2026:

## Overview

The ARR Responsible NLP Research checklist is designed to encourage best practices for responsible research, addressing issues of research ethics, societal impact and reproducibility.

## Key Updates for 2025-2026

If your paper gets accepted to EMNLP 2025, your completed responsible NLP checklist will be published alongside your paper as an appendix. This is a new requirement that will also apply to subsequent *ACL conferences.

Starting from December 2024 inappropriately filled checklist can be considered grounds for desk rejection.

## Main Checklist Components

The checklist includes three main sections:

- **Section A**: Mandatory questions for all submissions, including describing limitations and discussing potential risks
- **Section B**: Questions about scientific artifacts (code, data, models), including proper citation and licensing discussions
- **Section C**: Questions for computational experiments

## Important Guidelines for Authors

Common issues with the checklist include just saying 'yes' for all questions, even those not relevant for your paper, and failing to provide section numbers, justifications or extra information when needed.

The checklist was originally developed for NAACL 2022 and updated for ARR October 2024 cycle by Anna Rogers, based on discussions with ARR board.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "5e1e70c5-f659-45a2-854e-2333a610e156",
  "tool_use_result": {
    "query": "ACL responsible NLP research checklist 2025 2026 ARR",
    "results": [
      {
        "tool_use_id": "srvtoolu_017xmDhx2ym8wnqxbhaZYXya",
        "content": [
          {
            "title": "Responsible NLP Research Checklist",
            "url": "https://aclrollingreview.org/static/responsibleNLPresearch.pdf"
          },
          {
            "title": "ARR Responsible NLP Research checklist",
            "url": "http://aclrollingreview.org/responsibleNLPresearch/"
          },
          {
            "title": "EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/responsible-nlp-checklist-appendices"
          },
          {
            "title": "Responsible NLP Research Checklist",
            "url": "https://openreview.net/attachment?id=yGhYSEj8ln0&name=responsible_NLP_research"
          },
          {
            "title": "Responsible NLP Research Checklist",
            "url": "https://arxiv.org/html/2212.10503"
          },
          {
            "title": "Responsible NLP Checklist",
            "url": "https://aclanthology.org/attachments/2025.emnlp-main.1573.checklist.pdf"
          },
          {
            "title": "EMNLP 2025 on X: \"For EMNLP authors, please note that the responsible NLP research checklists will be included with all papers published at EMNLP (and future *CL conferences) as an additional appendix, as per the updated ARR policy: https://t.co/Uwna96UMTT @ReviewAcl\" / X",
            "url": "https://x.com/emnlpmeeting/status/1933196156995063863"
          },
          {
            "title": "Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authorchecklist"
          },
          {
            "title": "Call for Main Conference Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          }
        ]
      },
      "Based on the search results, here's what I found about the ACL Responsible NLP Research Checklist for 2025-2026:\n\n## Overview\n\nThe ARR Responsible NLP Research checklist is designed to encourage best practices for responsible research, addressing issues of research ethics, societal impact and reproducibility.\n\n## Key Updates for 2025-2026\n\nIf your paper gets accepted to EMNLP 2025, your completed responsible NLP checklist will be published alongside your paper as an appendix. This is a new requirement that will also apply to subsequent *ACL conferences.\n\nStarting from December 2024 inappropriately filled checklist can be considered grounds for desk rejection.\n\n## Main Checklist Components\n\nThe checklist includes three main sections:\n\n- **Section A**: Mandatory questions for all submissions, including describing limitations and discussing potential risks\n- **Section B**: Questions about scientific artifacts (code, data, models), including proper citation and licensing discussions\n- **Section C**: Questions for computational experiments\n\n## Important Guidelines for Authors\n\nCommon issues with the checklist include just saying 'yes' for all questions, even those not relevant for your paper, and failing to provide section numbers, justifications or extra information when needed.\n\nThe checklist was originally developed for NAACL 2022 and updated for ARR October 2024 cycle by Anna Rogers, based on discussions with ARR board."
    ],
    "durationSeconds": 6.145541084
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T07:36:24.500Z_

<details><summary>↩ Tool result · `toolu_011hfA1jHeXftQuKSyu3LMac`</summary>

```text
Web search results for query: "ARR May 2025 cycle deadline EMNLP 2026 submission format"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"[EMNLP 2025] Call for Main Conference Papers","url":"https://groups.google.com/g/ml-news/c/HKZ_H_iiM_A"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"}]

Based on the search results, here's the information about the ARR May 2025 cycle deadline and EMNLP 2026 submission format:

## ARR May 2025 Cycle Deadline

The ARR submission deadline for long and short papers is May 25, 2026. Note that this is actually the May 2026 cycle (not 2025), as the new 10-week cycle schedule started in May 2025.

## EMNLP 2026 Submission Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

All long, short, and theme papers must follow the ACL Author Guidelines, and EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Key EMNLP 2026 Policy for May 2026 Submissions

Authors will need to explicitly declare which conference they intend to commit to at submission time, as the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL). This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "cd75b23d-0e15-405c-8d06-b47a776d34e0",
  "tool_use_result": {
    "query": "ARR May 2025 cycle deadline EMNLP 2026 submission format",
    "results": [
      {
        "tool_use_id": "srvtoolu_017F2z5zPAXBonN4ea1SZLd9",
        "content": [
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X",
            "url": "https://x.com/emnlpmeeting/status/1892259536137785419"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "[EMNLP 2025] Call for Main Conference Papers",
            "url": "https://groups.google.com/g/ml-news/c/HKZ_H_iiM_A"
          },
          {
            "title": "Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1",
            "url": "https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"
          },
          {
            "title": "EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/emnlp"
          }
        ]
      },
      "Based on the search results, here's the information about the ARR May 2025 cycle deadline and EMNLP 2026 submission format:\n\n## ARR May 2025 Cycle Deadline\n\nThe ARR submission deadline for long and short papers is May 25, 2026. Note that this is actually the May 2026 cycle (not 2025), as the new 10-week cycle schedule started in May 2025.\n\n## EMNLP 2026 Submission Format\n\nThe format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.\n\nAll long, short, and theme papers must follow the ACL Author Guidelines, and EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.\n\n## Key EMNLP 2026 Policy for May 2026 Submissions\n\nAuthors will need to explicitly declare which conference they intend to commit to at submission time, as the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL). This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026."
    ],
    "durationSeconds": 8.943703915
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T07:36:26.554Z_

<details><summary>↩ Tool result · `toolu_01Saxr6JWG61axgHDcfJQhmb`</summary>

```text
Web search results for query: "aclrollingreview.org submission guidelines page limits anonymity"

Links: [{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Update to Anonymity Policy","url":"http://aclrollingreview.org/anonymity/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"aclrollingreview/authors.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/authors.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results from aclrollingreview.org, here's what the submission guidelines specify regarding page limits and anonymity:

## Page Limits

Papers should be desk-rejected if they exceed the page limit (4 pages for short, 8 for long papers, excluding the ethical considerations and limitations). Sections on ethical considerations and limitations do not count towards page limit. Appendices should come after the references in the submitted pdf and do not count towards the page limit.

## Anonymity Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. However, submissions will remain anonymous during peer review, and ARR will take measures to prioritize reviews by reviewers who are not aware of the author identities.

The new policy incentivizes anonymous submissions by special paper awards and priority in acceptance decisions for borderline papers. Papers must not include authors' names and affiliations, and supplementary materials must be fully anonymized to preserve the two-way anonymized reviewing policy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "87b132ed-13bd-4a5d-9e8f-2901bf9037d3",
  "tool_use_result": {
    "query": "aclrollingreview.org submission guidelines page limits anonymity",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CRAvFsPsRNwtx6Leazjt61",
        "content": [
          {
            "title": "Authors Guidelines",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "Update to Anonymity Policy",
            "url": "http://aclrollingreview.org/anonymity/"
          },
          {
            "title": "ARR Reviewer Guidelines",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "ARR Area Chair Guidelines",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "Authors Beware: Common Submission Problems",
            "url": "http://aclrollingreview.org/authorchecklist"
          },
          {
            "title": "How ARR works – ACL Rolling Review",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"
          },
          {
            "title": "aclrollingreview/authors.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/authors.md"
          },
          {
            "title": "ACL Rolling Review | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/acl-rolling-review"
          }
        ]
      },
      "Based on the search results from aclrollingreview.org, here's what the submission guidelines specify regarding page limits and anonymity:\n\n## Page Limits\n\nPapers should be desk-rejected if they exceed the page limit (4 pages for short, 8 for long papers, excluding the ethical considerations and limitations). Sections on ethical considerations and limitations do not count towards page limit. Appendices should come after the references in the submitted pdf and do not count towards the page limit.\n\n## Anonymity Policy\n\nBeginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. However, submissions will remain anonymous during peer review, and ARR will take measures to prioritize reviews by reviewers who are not aware of the author identities.\n\nThe new policy incentivizes anonymous submissions by special paper awards and priority in acceptance decisions for borderline papers. Papers must not include authors' names and affiliations, and supplementary materials must be fully anonymized to preserve the two-way anonymized reviewing policy."
    ],
    "durationSeconds": 9.765757632
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a lot of initial information. Now let me fetch the specific pages for more details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "c21d2aa2-cce4-4c4a-9c23-102370a3b61a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5a9BHsNveQH3DmWPYexBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3585,
      "cache_read_input_tokens": 25976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3585
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

_source line 18_

Found initial results. Now fetching the detailed pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "ab053751-f42b-4c04-a858-39fcb9f83cd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5a9BHsNveQH3DmWPYexBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3585,
      "cache_read_input_tokens": 25976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3585
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

_source line 19_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q8EsLyEpv93fQFJnxzYE6K`</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract ALL submission requirements: page limits (long/short), what counts towards page limit, what doesn't (references, appendix, limitations, ethics), anonymization rules, required materials, supplementary material rules, LaTeX template info, checklist requirements, and any deadlines. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "167af54c-e8f9-4c54-93f5-57d303fb1ed7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5a9BHsNveQH3DmWPYexBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3585,
      "cache_read_input_tokens": 25976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3585
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

_source line 20_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Uf9TRr6RtCkQRBDi9or15z`</summary>

```json
{
  "url": "https://aclrollingreview.org/authors",
  "prompt": "Extract ALL author guidelines: formatting requirements, page limits, anonymization rules, required sections (limitations, ethics), supplementary material guidelines (format, size limits), checklist requirements, template information, and any submission checklist items. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "567a7f6e-9062-42e3-b90a-6d8ed67049df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5a9BHsNveQH3DmWPYexBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3585,
      "cache_read_input_tokens": 25976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3585
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AFWokaAqrD98EQRXKbHEUg`</summary>

```json
{
  "url": "https://aclrollingreview.org/responsibleNLPresearch/",
  "prompt": "Extract the COMPLETE checklist: all sections (A, B, C, D, E), every individual question/item, what requires Yes/No/NA answers, what requires justification, and how it should be formatted/submitted. List every single checklist item."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "b5fefe75-a4bc-40dc-a1b9-1b078d0acd7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5a9BHsNveQH3DmWPYexBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3585,
      "cache_read_input_tokens": 25976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3585
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XniorPLC7XjGNjUPKbQeAb`</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract ALL dates: every ARR cycle deadline (especially May 2025 and May 2026 cycles), commitment deadlines for EMNLP 2025/2026, notification dates, camera-ready deadlines. Include the full schedule."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "3775dab9-e1e0-4789-b875-36c51658340f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5a9BHsNveQH3DmWPYexBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3585,
      "cache_read_input_tokens": 25976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3585
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

_source line 23 · 2026-05-17T07:36:42.336Z_

<details><summary>↩ Tool result · `toolu_01Uf9TRr6RtCkQRBDi9or15z`</summary>

```text
# ARR Author Guidelines: Comprehensive Extraction

## Formatting Requirements

**Templates & Format Standards:**
- Submissions must adhere to "the formatting in the submission templates, which is available as an Overleaf template"
- Link provided: Association for Computational Linguistics ACL Conference template on Overleaf
- Reference: ACL formatting guidelines at acl-org.github.io/ACLPUB/formatting.html

## Page Limits

**Length Requirements:**
- Short papers: maximum 4 pages
- Long papers: maximum 8 pages
- Author responses must be "text-only" with no external links permitted

## Anonymization Rules

**Core Anonymity Requirements:**
- Submissions must follow "the ACL Policies for Review and Citation"
- Papers must be "properly anonymized as detailed in CFP"
- "Confidential comments in Open Review are visible to ACs, SACs, and PCs. Because authors are anonymous to ACs and SACs, do not include author names or any identifying details in confidential comments"

**Preprint Policy:**
- No anonymity period exists; authors may post non-anonymous preprints while under review
- The system focuses on "the possibility of deanonymization, rather than any specific publication channel such as arXiv"

## Required Sections

**Limitations Section:**
The guidelines specify that limitations should address:
- Methodological caveats for interpreting findings
- Sampling approaches and potential confounding factors
- Practical constraints (e.g., computational intensity)
- Scope clarification regarding generalizability (languages, domains, tasks, models tested)

## Supplementary Material Guidelines

**Format & Size Limits:**
The document does not explicitly specify supplementary material format or size limits. Guidelines reference submission form requirements but provide no supplementary material details.

## Submission Checklist Requirements

**Pre-Submission Verification:**
- "Common submission problems" checklist available at aclrollingreview.org/authorchecklist
- "Responsible NLP checklist" provided at aclrollingreview.org/responsibleNLPresearch/
- Track keyword selection guidance at aclrollingreview.org/areas

**Critical Requirements:**
- System demonstrations should NOT be submitted to ARR
- Papers must be within scope per CFP
- Must adhere to technical submission requirements
- Desk rejection possible for non-compliance at any review cycle stage

## Additional Requirements

**Reviewer Signup (New May 2025):**
- "All submitting authors have to also sign up as reviewers" within 48 hours post-deadline
- Policy penalty applies: authors whose reviewers/chairs act irresponsibly cannot resubmit or commit work during current and next ARR cycle

**Resubmission Documentation:**
When resubmitting, authors must provide:
- Previous submission link
- Explanation of revisions addressing each reviewer's concerns as a PDF
- Optional color-coded paper showing changes vs. relocated content
- Reviewer preference (same or new)
- Meta-reviewer preference (same or new)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "e177e45d-a1eb-40b1-8cdc-b6a9732f1624",
  "tool_use_result": {
    "bytes": 57323,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Author Guidelines: Comprehensive Extraction\n\n## Formatting Requirements\n\n**Templates & Format Standards:**\n- Submissions must adhere to \"the formatting in the submission templates, which is available as an Overleaf template\"\n- Link provided: Association for Computational Linguistics ACL Conference template on Overleaf\n- Reference: ACL formatting guidelines at acl-org.github.io/ACLPUB/formatting.html\n\n## Page Limits\n\n**Length Requirements:**\n- Short papers: maximum 4 pages\n- Long papers: maximum 8 pages\n- Author responses must be \"text-only\" with no external links permitted\n\n## Anonymization Rules\n\n**Core Anonymity Requirements:**\n- Submissions must follow \"the ACL Policies for Review and Citation\"\n- Papers must be \"properly anonymized as detailed in CFP\"\n- \"Confidential comments in Open Review are visible to ACs, SACs, and PCs. Because authors are anonymous to ACs and SACs, do not include author names or any identifying details in confidential comments\"\n\n**Preprint Policy:**\n- No anonymity period exists; authors may post non-anonymous preprints while under review\n- The system focuses on \"the possibility of deanonymization, rather than any specific publication channel such as arXiv\"\n\n## Required Sections\n\n**Limitations Section:**\nThe guidelines specify that limitations should address:\n- Methodological caveats for interpreting findings\n- Sampling approaches and potential confounding factors\n- Practical constraints (e.g., computational intensity)\n- Scope clarification regarding generalizability (languages, domains, tasks, models tested)\n\n## Supplementary Material Guidelines\n\n**Format & Size Limits:**\nThe document does not explicitly specify supplementary material format or size limits. Guidelines reference submission form requirements but provide no supplementary material details.\n\n## Submission Checklist Requirements\n\n**Pre-Submission Verification:**\n- \"Common submission problems\" checklist available at aclrollingreview.org/authorchecklist\n- \"Responsible NLP checklist\" provided at aclrollingreview.org/responsibleNLPresearch/\n- Track keyword selection guidance at aclrollingreview.org/areas\n\n**Critical Requirements:**\n- System demonstrations should NOT be submitted to ARR\n- Papers must be within scope per CFP\n- Must adhere to technical submission requirements\n- Desk rejection possible for non-compliance at any review cycle stage\n\n## Additional Requirements\n\n**Reviewer Signup (New May 2025):**\n- \"All submitting authors have to also sign up as reviewers\" within 48 hours post-deadline\n- Policy penalty applies: authors whose reviewers/chairs act irresponsibly cannot resubmit or commit work during current and next ARR cycle\n\n**Resubmission Documentation:**\nWhen resubmitting, authors must provide:\n- Previous submission link\n- Explanation of revisions addressing each reviewer's concerns as a PDF\n- Optional color-coded paper showing changes vs. relocated content\n- Reviewer preference (same or new)\n- Meta-reviewer preference (same or new)",
    "durationMs": 8301,
    "url": "https://aclrollingreview.org/authors"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T07:36:43.273Z_

<details><summary>↩ Tool result · `toolu_01XniorPLC7XjGNjUPKbQeAb`</summary>

```text
# ARR Cycle Deadlines and Venue Commitment Dates

## Current and Upcoming ARR Cycles

**Schedule Change**: "From October 2022 to February 2025, ARR ran 8-week review cycles" but transitioned to 10-week cycles starting May 2025, reducing from 6 to approximately 5 cycles annually.

### May 2026 Cycle
- Submission: May 25, 2026
- Reviewer registration: May 27, 2026
- Reviews due: June 29, 2026
- Author response: July 7-13, 2026
- Meta-reviews release: July 30, 2026
- Cycle end: August 2, 2026

### March 2026 Cycle
- Submission: March 16, 2026
- Reviewer registration: March 18, 2026
- Reviews due: April 20, 2026
- Author response: April 28-May 4, 2026
- Meta-reviews release: May 21, 2026
- Cycle end: May 24, 2026

### August 2026 and October 2026 Cycles
Dates marked TBA for most review phases; cycle end dates are August 11, 2026 and December 20, 2026 respectively.

## Venue Commitment Deadlines

- **EMNLP 2026**: August 2, 2026 (final ARR submission: May 25, 2026)
- **AACL 2026**: August 26, 2026 (final ARR submission: May 25, 2026)
- **EACL 2027**: October 11, 2026 (final ARR submission: August 3, 2026)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "d8394b3b-08e1-4466-984e-a2829330d20b",
  "tool_use_result": {
    "bytes": 25438,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Cycle Deadlines and Venue Commitment Dates\n\n## Current and Upcoming ARR Cycles\n\n**Schedule Change**: \"From October 2022 to February 2025, ARR ran 8-week review cycles\" but transitioned to 10-week cycles starting May 2025, reducing from 6 to approximately 5 cycles annually.\n\n### May 2026 Cycle\n- Submission: May 25, 2026\n- Reviewer registration: May 27, 2026\n- Reviews due: June 29, 2026\n- Author response: July 7-13, 2026\n- Meta-reviews release: July 30, 2026\n- Cycle end: August 2, 2026\n\n### March 2026 Cycle\n- Submission: March 16, 2026\n- Reviewer registration: March 18, 2026\n- Reviews due: April 20, 2026\n- Author response: April 28-May 4, 2026\n- Meta-reviews release: May 21, 2026\n- Cycle end: May 24, 2026\n\n### August 2026 and October 2026 Cycles\nDates marked TBA for most review phases; cycle end dates are August 11, 2026 and December 20, 2026 respectively.\n\n## Venue Commitment Deadlines\n\n- **EMNLP 2026**: August 2, 2026 (final ARR submission: May 25, 2026)\n- **AACL 2026**: August 26, 2026 (final ARR submission: May 25, 2026)\n- **EACL 2027**: October 11, 2026 (final ARR submission: August 3, 2026)",
    "durationMs": 4349,
    "url": "https://aclrollingreview.org/dates"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T07:36:43.634Z_

<details><summary>↩ Tool result · `toolu_01Q8EsLyEpv93fQFJnxzYE6K`</summary>

```text
# ACL Rolling Review: Complete Submission Requirements

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited references (don't count toward limit)
- Unlimited space for Limitations section (required, doesn't count)
- Unlimited space for optional Ethical Considerations section (doesn't count)

**Short Papers:**
- Up to 4 pages of content
- Unlimited references (don't count toward limit)
- Unlimited space for Limitations section (required, doesn't count)
- Unlimited space for optional Ethical Considerations section (doesn't count)

Papers exceeding length requirements or missing the Limitations section face desk rejection.

## Required Sections

**Limitations Section (Mandatory):**
- Titled "Limitations"
- Placed before references
- Doesn't count toward page limit
- Cannot introduce new methods, analysis, or results
- Papers without this section are desk rejected

**Ethical Considerations (Recommended):**
- Optional section titled "Ethical Considerations"
- Doesn't count toward page limit
- Encouraged but not mandatory

## Anonymization Rules

- No author names or affiliations in submissions
- Avoid self-references revealing identity: use "Smith showed..." instead of "We previously showed..."
- No references to documents unavailable to reviewers
- Supplementary materials must be anonymized
- Cloud storage links tracking downloads (Dropbox, Google Drive) prohibited
- Repositories must use services like Anonymous GitHub
- Two-way anonymized review enforced

## Required Materials at Submission

- Manuscript in ACL style template format
- Completed Responsible NLP Checklist (incorrect/incomplete/misleading entries can trigger desk rejection)
- Author registration form (must complete within 48 hours after submission deadline)
- For resubmissions: link to previous submission and detailed revision summary

## Supplementary Materials (Optional)

- Appendices, software, and data encouraged for reproducibility
- Appendices follow double-column format (with approved exceptions); improper formatting results in desk rejection as of July 2025
- Appendices placed after references, don't count toward page limit
- Software submitted as single .tgz or .zip archive
- Data submitted as separate single .tgz or .zip archive
- All supplementary materials must be fully anonymized
- Reviewers not required to consider appendix material
- Critical content (novelty, claims, technical correctness assessments) belongs in main paper, not appendices

## LaTeX Template Requirements

- Must use official ACL style template available at: "github.com/acl-org/acl-style-files"
- Follow "*ACL" formatting guidelines at: "acl-org.github.io/ACLPUB/formatting.html"
- No modifications to style files permitted
- Templates from other conferences prohibited
- Non-conforming submissions rejected without review
- All text must address human readers exclusively and be clearly visible

## Checklist Requirements

- Responsible NLP Checklist completion mandatory
- Content used in review process
- Incomplete or misleading information can result in desk rejection
- ARR provides submission checklist to help authors avoid common issues
- Updated OpenReview profile required with affiliation, Semantic Scholar link, DBLP link, ACL Anthology link, and email address

## Key Deadlines and Policies

- Metadata fields (including Responsible Checklist) editable for 48 hours after submission deadline
- Author registration must complete within 48 hours post-deadline
- Resubmissions must address previous reviewer feedback or provide justification for not doing so
- Withdrawn submissions more than 48 hours after deadline cannot be resubmitted until second subsequent cycle
- Papers with meta-reviews can be submitted/committed elsewhere without withdrawal

## Additional Submission Rules

- No dual submissions: papers cannot be under review elsewhere during ARR review period
- AI writing assistance must be disclosed in checklist and acknowledgments; exceptions exist for grammar checking and language polishing
- Text re-use limited to 10% total tokens from other publications
- Papers violating originality requirements face desk rejection
- Concurrent papers on related topics by overlapping authors must cite each other and discuss differences
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "04d8d450-2827-427b-866e-cc468f19bc61",
  "tool_use_result": {
    "bytes": 48555,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review: Complete Submission Requirements\n\n## Page Limits\n\n**Long Papers:**\n- Up to 8 pages of content\n- Unlimited references (don't count toward limit)\n- Unlimited space for Limitations section (required, doesn't count)\n- Unlimited space for optional Ethical Considerations section (doesn't count)\n\n**Short Papers:**\n- Up to 4 pages of content\n- Unlimited references (don't count toward limit)\n- Unlimited space for Limitations section (required, doesn't count)\n- Unlimited space for optional Ethical Considerations section (doesn't count)\n\nPapers exceeding length requirements or missing the Limitations section face desk rejection.\n\n## Required Sections\n\n**Limitations Section (Mandatory):**\n- Titled \"Limitations\"\n- Placed before references\n- Doesn't count toward page limit\n- Cannot introduce new methods, analysis, or results\n- Papers without this section are desk rejected\n\n**Ethical Considerations (Recommended):**\n- Optional section titled \"Ethical Considerations\"\n- Doesn't count toward page limit\n- Encouraged but not mandatory\n\n## Anonymization Rules\n\n- No author names or affiliations in submissions\n- Avoid self-references revealing identity: use \"Smith showed...\" instead of \"We previously showed...\"\n- No references to documents unavailable to reviewers\n- Supplementary materials must be anonymized\n- Cloud storage links tracking downloads (Dropbox, Google Drive) prohibited\n- Repositories must use services like Anonymous GitHub\n- Two-way anonymized review enforced\n\n## Required Materials at Submission\n\n- Manuscript in ACL style template format\n- Completed Responsible NLP Checklist (incorrect/incomplete/misleading entries can trigger desk rejection)\n- Author registration form (must complete within 48 hours after submission deadline)\n- For resubmissions: link to previous submission and detailed revision summary\n\n## Supplementary Materials (Optional)\n\n- Appendices, software, and data encouraged for reproducibility\n- Appendices follow double-column format (with approved exceptions); improper formatting results in desk rejection as of July 2025\n- Appendices placed after references, don't count toward page limit\n- Software submitted as single .tgz or .zip archive\n- Data submitted as separate single .tgz or .zip archive\n- All supplementary materials must be fully anonymized\n- Reviewers not required to consider appendix material\n- Critical content (novelty, claims, technical correctness assessments) belongs in main paper, not appendices\n\n## LaTeX Template Requirements\n\n- Must use official ACL style template available at: \"github.com/acl-org/acl-style-files\"\n- Follow \"*ACL\" formatting guidelines at: \"acl-org.github.io/ACLPUB/formatting.html\"\n- No modifications to style files permitted\n- Templates from other conferences prohibited\n- Non-conforming submissions rejected without review\n- All text must address human readers exclusively and be clearly visible\n\n## Checklist Requirements\n\n- Responsible NLP Checklist completion mandatory\n- Content used in review process\n- Incomplete or misleading information can result in desk rejection\n- ARR provides submission checklist to help authors avoid common issues\n- Updated OpenReview profile required with affiliation, Semantic Scholar link, DBLP link, ACL Anthology link, and email address\n\n## Key Deadlines and Policies\n\n- Metadata fields (including Responsible Checklist) editable for 48 hours after submission deadline\n- Author registration must complete within 48 hours post-deadline\n- Resubmissions must address previous reviewer feedback or provide justification for not doing so\n- Withdrawn submissions more than 48 hours after deadline cannot be resubmitted until second subsequent cycle\n- Papers with meta-reviews can be submitted/committed elsewhere without withdrawal\n\n## Additional Submission Rules\n\n- No dual submissions: papers cannot be under review elsewhere during ARR review period\n- AI writing assistance must be disclosed in checklist and acknowledgments; exceptions exist for grammar checking and language polishing\n- Text re-use limited to 10% total tokens from other publications\n- Papers violating originality requirements face desk rejection\n- Concurrent papers on related topics by overlapping authors must cite each other and discuss differences",
    "durationMs": 11343,
    "url": "https://aclrollingreview.org/cfp"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T07:36:48.677Z_

<details><summary>↩ Tool result · `toolu_01AFWokaAqrD98EQRXKbHEUg`</summary>

```text
# ACL Rolling Review Responsible NLP Research Checklist

## Section A: For Every Submission

**A1. Did you describe the limitations of your work?**
- Answer: Yes/No with justification
- Required: Point out assumptions, robustness to violations, scope of claims, factors influencing performance
- Format: Reference section(s) in paper or provide explanation

**A2. Did you discuss any potential risks of your work?**
- Answer: Yes/No with justification
- Required: Address malicious/unintended harms, environmental impact, fairness, privacy, security, overgeneralization, stakeholder impacts, dual-use considerations
- Format: Reference section(s) or provide explanation

---

## Section B: Scientific Artifacts (Code, Data, Models)

**B1. Did you cite the creators of artifacts you used?**
- Answer: Yes/No with justification
- Required: Cite original papers, state versions, include URLs when possible
- Format: Reference section(s) where citations appear

**B2. Did you discuss the license or terms for artifacts?**
- Answer: Yes/No with justification
- Required: State license names (e.g., CC-BY 4.0), copyright, terms of service, original and derived licenses
- Format: Reference section(s) or provide license details

**B3. Did you discuss if artifact use was consistent with intended use?**
- Answer: Yes/No with justification
- Required: Verify license compatibility, specify intended use, confirm safe deployment conditions, address anonymization
- Format: Reference section(s) or provide explanation

**B4. Did you discuss steps checking for identifying information and offensive content?**
- Answer: Yes/No with justification
- Required: Explain detection methods, anonymization techniques, privacy protection measures, harms discussion
- Format: Reference section(s) or provide explanation

**B5. Did you provide artifact documentation?**
- Answer: Yes/No with justification
- Required: Report languages, domains, linguistic phenomena, demographic information; consider data/model cards or datasheets
- Format: Reference section(s) or supplementary materials

**B6. Did you report relevant statistics for data?**
- Answer: Yes/No with justification
- Required: Report example counts, train/test/dev split sizes even for benchmarks
- Format: Reference section(s) where statistics appear

---

## Section C: Computational Experiments

**C1. Did you report model parameters, computational budget, and infrastructure?**
- Answer: Yes/No with justification
- Required: Number of parameters, GPU hours, parallelism details, computing equipment specifications
- Format: Reference section(s) or provide estimates

**C2. Did you discuss experimental setup including hyperparameter search?**
- Answer: Yes/No with justification
- Required: Model selection method, preprocessing details, hyperparameter search results, best-found values, dataset used for tuning
- Format: Main paper or appendix with complete details

**C3. Did you report descriptive statistics about results?**
- Answer: Yes/No with justification
- Required: Error bars, confidence intervals, clarify if reporting max/mean/single run, validation set results
- Format: Reference section(s) where statistics appear

**C4. Did you report implementation details for existing packages?**
- Answer: Yes/No with justification
- Required: Version numbers, parameter settings, citations, modifications made to libraries
- Format: Reference section(s) or supplementary materials

---

## Section D: Human Annotators/Research Participants

**D1. Did you report full text of participant instructions?**
- Answer: Yes/No with justification
- Required: Include screenshots, disclaimers, risk warnings
- Format: Main paper or supplementary materials

**D2. Did you report recruitment, payment, and adequacy of compensation?**
- Answer: Yes/No with justification
- Required: Recruitment method, platform/population details, payment amounts, fairness assessment
- Format: Reference section(s) or provide details

**D3. Did you discuss consent from people whose data you used?**
- Answer: Yes/No with justification
- Required: Explain data usage disclosure to participants
- Format: Reference section(s) or provide explanation

**D4. Was data collection approved by ethics review board?**
- Answer: Yes/No with justification
- Required: State IRB/ethics board approval (anonymized for initial submissions)
- Format: Reference section(s) or provide explanation

**D5. Did you report annotator demographic and geographic characteristics?**
- Answer: Yes/No with justification
- Required: Include data statement, protected information disclosures, self-reported vs. inferred characteristics
- Format: Reference section(s) or supplementary materials

---

## Section E: AI Assistant Use

**E1. If you used AI assistants, did you include information about your use?**
- Answer: Yes/No with justification
- Required: Disclose all AI assistant usage (ChatGPT, Copilot, etc.) in alignment with ACL authorship criteria
- Format: Dedicated section or integrated explanation

---

## Submission Format
- Completed as part of the submission form (post-February 2024)
- For each item: provide section reference if "Yes" or justification if "No"
- **Critical note:** Submissions systematically failing to provide relevant sections or justifications face desk rejection
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "82af1ee6-1640-4008-96d7-f4382a148149",
  "tool_use_result": {
    "bytes": 36573,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Responsible NLP Research Checklist\n\n## Section A: For Every Submission\n\n**A1. Did you describe the limitations of your work?**\n- Answer: Yes/No with justification\n- Required: Point out assumptions, robustness to violations, scope of claims, factors influencing performance\n- Format: Reference section(s) in paper or provide explanation\n\n**A2. Did you discuss any potential risks of your work?**\n- Answer: Yes/No with justification\n- Required: Address malicious/unintended harms, environmental impact, fairness, privacy, security, overgeneralization, stakeholder impacts, dual-use considerations\n- Format: Reference section(s) or provide explanation\n\n---\n\n## Section B: Scientific Artifacts (Code, Data, Models)\n\n**B1. Did you cite the creators of artifacts you used?**\n- Answer: Yes/No with justification\n- Required: Cite original papers, state versions, include URLs when possible\n- Format: Reference section(s) where citations appear\n\n**B2. Did you discuss the license or terms for artifacts?**\n- Answer: Yes/No with justification\n- Required: State license names (e.g., CC-BY 4.0), copyright, terms of service, original and derived licenses\n- Format: Reference section(s) or provide license details\n\n**B3. Did you discuss if artifact use was consistent with intended use?**\n- Answer: Yes/No with justification\n- Required: Verify license compatibility, specify intended use, confirm safe deployment conditions, address anonymization\n- Format: Reference section(s) or provide explanation\n\n**B4. Did you discuss steps checking for identifying information and offensive content?**\n- Answer: Yes/No with justification\n- Required: Explain detection methods, anonymization techniques, privacy protection measures, harms discussion\n- Format: Reference section(s) or provide explanation\n\n**B5. Did you provide artifact documentation?**\n- Answer: Yes/No with justification\n- Required: Report languages, domains, linguistic phenomena, demographic information; consider data/model cards or datasheets\n- Format: Reference section(s) or supplementary materials\n\n**B6. Did you report relevant statistics for data?**\n- Answer: Yes/No with justification\n- Required: Report example counts, train/test/dev split sizes even for benchmarks\n- Format: Reference section(s) where statistics appear\n\n---\n\n## Section C: Computational Experiments\n\n**C1. Did you report model parameters, computational budget, and infrastructure?**\n- Answer: Yes/No with justification\n- Required: Number of parameters, GPU hours, parallelism details, computing equipment specifications\n- Format: Reference section(s) or provide estimates\n\n**C2. Did you discuss experimental setup including hyperparameter search?**\n- Answer: Yes/No with justification\n- Required: Model selection method, preprocessing details, hyperparameter search results, best-found values, dataset used for tuning\n- Format: Main paper or appendix with complete details\n\n**C3. Did you report descriptive statistics about results?**\n- Answer: Yes/No with justification\n- Required: Error bars, confidence intervals, clarify if reporting max/mean/single run, validation set results\n- Format: Reference section(s) where statistics appear\n\n**C4. Did you report implementation details for existing packages?**\n- Answer: Yes/No with justification\n- Required: Version numbers, parameter settings, citations, modifications made to libraries\n- Format: Reference section(s) or supplementary materials\n\n---\n\n## Section D: Human Annotators/Research Participants\n\n**D1. Did you report full text of participant instructions?**\n- Answer: Yes/No with justification\n- Required: Include screenshots, disclaimers, risk warnings\n- Format: Main paper or supplementary materials\n\n**D2. Did you report recruitment, payment, and adequacy of compensation?**\n- Answer: Yes/No with justification\n- Required: Recruitment method, platform/population details, payment amounts, fairness assessment\n- Format: Reference section(s) or provide details\n\n**D3. Did you discuss consent from people whose data you used?**\n- Answer: Yes/No with justification\n- Required: Explain data usage disclosure to participants\n- Format: Reference section(s) or provide explanation\n\n**D4. Was data collection approved by ethics review board?**\n- Answer: Yes/No with justification\n- Required: State IRB/ethics board approval (anonymized for initial submissions)\n- Format: Reference section(s) or provide explanation\n\n**D5. Did you report annotator demographic and geographic characteristics?**\n- Answer: Yes/No with justification\n- Required: Include data statement, protected information disclosures, self-reported vs. inferred characteristics\n- Format: Reference section(s) or supplementary materials\n\n---\n\n## Section E: AI Assistant Use\n\n**E1. If you used AI assistants, did you include information about your use?**\n- Answer: Yes/No with justification\n- Required: Disclose all AI assistant usage (ChatGPT, Copilot, etc.) in alignment with ACL authorship criteria\n- Format: Dedicated section or integrated explanation\n\n---\n\n## Submission Format\n- Completed as part of the submission form (post-February 2024)\n- For each item: provide section reference if \"Yes\" or justification if \"No\"\n- **Critical note:** Submissions systematically failing to provide relevant sections or justifications face desk rejection",
    "durationMs": 12107,
    "url": "https://aclrollingreview.org/responsibleNLPresearch/"
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the EMNLP 2026 call for papers and the anonymity policy page, plus the checklist PDF and the author common problems checklist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "03f176e4-f28d-4785-ae38-ba72621088f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011j1q93gBSL34aJ1yBBQxRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 445,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 29561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
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

_source line 28_

Good, getting more details now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "74530ec5-2039-4b86-9d22-35d084b18486",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011j1q93gBSL34aJ1yBBQxRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 445,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 29561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
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

_source line 29_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M4hRyjwjaSMccGvYbpFgfd`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission requirements for EMNLP 2026: deadlines, page limits, required materials, anonymization, theme, commitment deadline, any EMNLP-specific rules beyond standard ARR requirements. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "edea8076-772b-4285-ad53-9437a48c3db6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011j1q93gBSL34aJ1yBBQxRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 445,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 29561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
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

_source line 30_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018XkDcUuq6ThPDxZK2p51J8`</summary>

```json
{
  "url": "https://aclrollingreview.org/authorchecklist",
  "prompt": "Extract ALL common submission problems listed: formatting issues, anonymization mistakes, checklist problems, supplementary material issues, and any other items authors commonly get wrong. List every single item."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "7074e989-f564-449d-bbb5-c583e538bff9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011j1q93gBSL34aJ1yBBQxRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 445,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 29561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R4mjYRiQbVXpSbng6sM5mJ`</summary>

```json
{
  "url": "https://aclrollingreview.org/anonymity/",
  "prompt": "Extract the COMPLETE anonymity policy: what is allowed, what is not allowed, preprint rules, self-citation rules, anonymous submission rules, any incentives for anonymous submissions. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "e9289925-8506-441d-b3c2-3b48e35483ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011j1q93gBSL34aJ1yBBQxRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 445,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 29561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YFEuxxxDppEqgNG7b6xZVs`</summary>

```json
{
  "query": "ACL 2025 2026 style files LaTeX template acl.sty documentclass options review anonymous"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "132957ec-6eca-4c7c-b98b-30dd82d03a30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011j1q93gBSL34aJ1yBBQxRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 445,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 29561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3578
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

_source line 33 · 2026-05-17T07:37:01.839Z_

<details><summary>↩ Tool result · `toolu_01M4hRyjwjaSMccGvYbpFgfd`</summary>

```text
# EMNLP 2026 Submission Requirements

## Key Deadlines
- **ARR Submission Deadline:** May 25, 2026
- **Reviewer Registration:** May 27, 2026
- **Author Response Period:** July 7-13, 2026
- **Meta Review Release:** July 30, 2026
- **EMNLP Commitment Deadline:** August 2, 2026
- **Acceptance Notification:** August 20, 2026
- **Camera-Ready Due:** September 20, 2026
- **Conference Dates:** October 24-29, 2026

*All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth")*

## Page Limits
- **Long Papers:** 8 pages (9 pages in camera-ready with reviewer feedback)
- **Short Papers:** 4 pages (5 pages in camera-ready with reviewer feedback)

## Required Materials & Policies
Authors must comply with:
- Two-way anonymized review instructions
- "ACL's Publication Ethics Policy, and ARR's Ethics Policy including the responsible NLP research checklist"
- Limitations sections
- Optional supplementary materials permitted
- Writing assistance allowed (with disclosure)
- Responsible disclosure policy for security issues

## EMNLP-Specific Rules

**Binding Conference Declaration:** "ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026"

**Authorship During Commitment:** Author list modifications prohibited; author order changes permitted only

**Paper Integrity:** Desk rejection possible for thinly sliced contributions, hallucinated citations, entirely AI-generated papers, or ethics violations. Affected authors become ineligible for EMNLP 2026 and 2027 commitments.

**Mandatory Reviewer Service:** All authors must register and complete assigned reviews/meta-reviews by specified deadlines or face ineligibility for future submissions.

**Presentation Requirement:** "All accepted papers must be presented at the conference to appear in the proceedings"

## Special Theme Track
"New Missions for NLP Research" welcomes empirical, theoretical, position, and survey papers addressing progress evaluation, systems/ecosystems, scientific understanding, data governance, and LLMs as research tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "07c4cfc5-e43d-4b40-9f30-0936af910a29",
  "tool_use_result": {
    "bytes": 26454,
    "code": 200,
    "codeText": "OK",
    "result": "# EMNLP 2026 Submission Requirements\n\n## Key Deadlines\n- **ARR Submission Deadline:** May 25, 2026\n- **Reviewer Registration:** May 27, 2026\n- **Author Response Period:** July 7-13, 2026\n- **Meta Review Release:** July 30, 2026\n- **EMNLP Commitment Deadline:** August 2, 2026\n- **Acceptance Notification:** August 20, 2026\n- **Camera-Ready Due:** September 20, 2026\n- **Conference Dates:** October 24-29, 2026\n\n*All deadlines are 11:59 PM UTC-12:00 (\"anywhere on Earth\")*\n\n## Page Limits\n- **Long Papers:** 8 pages (9 pages in camera-ready with reviewer feedback)\n- **Short Papers:** 4 pages (5 pages in camera-ready with reviewer feedback)\n\n## Required Materials & Policies\nAuthors must comply with:\n- Two-way anonymized review instructions\n- \"ACL's Publication Ethics Policy, and ARR's Ethics Policy including the responsible NLP research checklist\"\n- Limitations sections\n- Optional supplementary materials permitted\n- Writing assistance allowed (with disclosure)\n- Responsible disclosure policy for security issues\n\n## EMNLP-Specific Rules\n\n**Binding Conference Declaration:** \"ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026\"\n\n**Authorship During Commitment:** Author list modifications prohibited; author order changes permitted only\n\n**Paper Integrity:** Desk rejection possible for thinly sliced contributions, hallucinated citations, entirely AI-generated papers, or ethics violations. Affected authors become ineligible for EMNLP 2026 and 2027 commitments.\n\n**Mandatory Reviewer Service:** All authors must register and complete assigned reviews/meta-reviews by specified deadlines or face ineligibility for future submissions.\n\n**Presentation Requirement:** \"All accepted papers must be presented at the conference to appear in the proceedings\"\n\n## Special Theme Track\n\"New Missions for NLP Research\" welcomes empirical, theoretical, position, and survey papers addressing progress evaluation, systems/ecosystems, scientific understanding, data governance, and LLMs as research tools.",
    "durationMs": 7048,
    "url": "https://2026.emnlp.org/calls/main_conference_papers/"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T07:37:02.312Z_

<details><summary>↩ Tool result · `toolu_01R4mjYRiQbVXpSbng6sM5mJ`</summary>

```text
# ACL Rolling Review Anonymity Policy Summary

Based on the webpage content provided, here's what is stated about the anonymity policy:

## What IS Allowed

**Preprints:** "Authors are free to post and discuss non-anonymous preprints at any time." This represents a significant change from the previous policy.

## What IS NOT Allowed

The policy maintains that "submissions will remain anonymous during peer review," preventing author identity disclosure during the review process.

## Key Implementation Details

**Reviewer Selection:** ARR will "prioritize reviews by reviewers who are not aware of the author identities" to protect anonymity during evaluation.

**Author Awareness:** Authors receive this caution: "widely sharing the work will make it harder to recruit reviewers."

## Incentives for Anonymity

The ACL established "awards for unpublicized work," though these are "decided by program committees, not ARR."

## Policy Scope

The updated policy took effect beginning with ARR's February 15 submission cycle and applies to all future submissions.

---

**Note:** The webpage excerpt does not provide detailed information on self-citation rules or other specific restrictions beyond these points. For the complete policy details, the page references an external link to the full ACL Anonymity Policy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "e6dc8eb7-7b00-4ba2-bb79-567a35dfa991",
  "tool_use_result": {
    "bytes": 16849,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Anonymity Policy Summary\n\nBased on the webpage content provided, here's what is stated about the anonymity policy:\n\n## What IS Allowed\n\n**Preprints:** \"Authors are free to post and discuss non-anonymous preprints at any time.\" This represents a significant change from the previous policy.\n\n## What IS NOT Allowed\n\nThe policy maintains that \"submissions will remain anonymous during peer review,\" preventing author identity disclosure during the review process.\n\n## Key Implementation Details\n\n**Reviewer Selection:** ARR will \"prioritize reviews by reviewers who are not aware of the author identities\" to protect anonymity during evaluation.\n\n**Author Awareness:** Authors receive this caution: \"widely sharing the work will make it harder to recruit reviewers.\"\n\n## Incentives for Anonymity\n\nThe ACL established \"awards for unpublicized work,\" though these are \"decided by program committees, not ARR.\"\n\n## Policy Scope\n\nThe updated policy took effect beginning with ARR's February 15 submission cycle and applies to all future submissions.\n\n---\n\n**Note:** The webpage excerpt does not provide detailed information on self-citation rules or other specific restrictions beyond these points. For the complete policy details, the page references an external link to the full ACL Anonymity Policy.",
    "durationMs": 3598,
    "url": "https://aclrollingreview.org/anonymity/"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-17T07:37:02.698Z_

<details><summary>↩ Tool result · `toolu_018XkDcUuq6ThPDxZK2p51J8`</summary>

```text
# Common Submission Problems for ACL Rolling Review

## Scope Issues
- Paper doesn't align with ARR's focus on computational processing of language

## Author & Registration Problems
- Incomplete author list or incorrect author ordering
- Authors haven't completed OpenReview profiles before submission
- Authors unaware of reviewing requirements or haven't registered within 48 hours
- Missing Semantic Scholar, DBLP, or ACL Anthology profile links

## Dual Submission & Resubmission Errors
- Paper simultaneously under review at other archival venues
- Duplicate submission by same authors
- Related concurrent submissions violating originality requirements
- Salami-sliced papers attempting to divide work inappropriately
- Reframing/improving prior work without acknowledging it as a resubmission
- Missing "summary of changes" document for revised submissions
- Author list changes not disclosed in submission form

## Formatting Violations
- Exceeding page limits (8 for long papers, 4 for short papers)
- Missing "Limitations" section or improperly placed
- Limitations section containing new experiments or analysis
- Non-compliance with ACL formatting guidelines
- Appendices not in double-column format
- Leftover comments or metadata from previous revisions
- Text designed to manipulate machine readers

## Anonymization Breaches
- Explicit references to authors' prior work
- Unprotected supplementary materials revealing identity
- Included acknowledgements section
- Links to non-anonymous repositories or tracking services
- Improper "preprint status" field completion

## Responsible NLP Checklist Problems
- Incomplete or superficial checklist responses
- Checking "yes" for irrelevant questions
- Missing section numbers or justifications
- Undisclosed generative AI usage

## Supplementary Material Issues
- Overly complex supplements; paper incomprehensible without them
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "af23098f-4b4e-4836-bdc1-8a0bd14c339e",
  "tool_use_result": {
    "bytes": 27619,
    "code": 200,
    "codeText": "OK",
    "result": "# Common Submission Problems for ACL Rolling Review\n\n## Scope Issues\n- Paper doesn't align with ARR's focus on computational processing of language\n\n## Author & Registration Problems\n- Incomplete author list or incorrect author ordering\n- Authors haven't completed OpenReview profiles before submission\n- Authors unaware of reviewing requirements or haven't registered within 48 hours\n- Missing Semantic Scholar, DBLP, or ACL Anthology profile links\n\n## Dual Submission & Resubmission Errors\n- Paper simultaneously under review at other archival venues\n- Duplicate submission by same authors\n- Related concurrent submissions violating originality requirements\n- Salami-sliced papers attempting to divide work inappropriately\n- Reframing/improving prior work without acknowledging it as a resubmission\n- Missing \"summary of changes\" document for revised submissions\n- Author list changes not disclosed in submission form\n\n## Formatting Violations\n- Exceeding page limits (8 for long papers, 4 for short papers)\n- Missing \"Limitations\" section or improperly placed\n- Limitations section containing new experiments or analysis\n- Non-compliance with ACL formatting guidelines\n- Appendices not in double-column format\n- Leftover comments or metadata from previous revisions\n- Text designed to manipulate machine readers\n\n## Anonymization Breaches\n- Explicit references to authors' prior work\n- Unprotected supplementary materials revealing identity\n- Included acknowledgements section\n- Links to non-anonymous repositories or tracking services\n- Improper \"preprint status\" field completion\n\n## Responsible NLP Checklist Problems\n- Incomplete or superficial checklist responses\n- Checking \"yes\" for irrelevant questions\n- Missing section numbers or justifications\n- Undisclosed generative AI usage\n\n## Supplementary Material Issues\n- Overly complex supplements; paper incomprehensible without them",
    "durationMs": 5925,
    "url": "https://aclrollingreview.org/authorchecklist"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T07:37:04.984Z_

<details><summary>↩ Tool result · `toolu_01YFEuxxxDppEqgNG7b6xZVs`</summary>

```text
Web search results for query: "ACL 2025 2026 style files LaTeX template acl.sty documentclass options review anonymous"

Links: [{"title":"GitHub - acl-org/acl-style-files: Official style files for papers submitted to venues of the Association for Computational Linguistics · GitHub","url":"https://github.com/acl-org/acl-style-files"},{"title":"Association for Computational Linguistics (ACL) conference - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj"},{"title":"Style Files and Guidelines | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/StyleGuide"},{"title":"ACL Lab Template - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/acl-lab-template/rgdcfpfzshnv"},{"title":"Call for Tutorials -","url":"https://2026.eacl.org/calls/tutorials/"},{"title":"LuaLaTeX and XeLaTeX Template for *ACL Style Files","url":"https://arxiv.org/html/2505.03469v1"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Templates - Journals, CVs, Presentations, Reports and More - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/tagged/acl"},{"title":"ACL Template | Format, Structure, and Guide","url":"https://scispace.com/templates/acl-template-hjmlcd42ar7fdcg"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"}]

Based on the search results, here's what I found about ACL LaTeX template options:

## ACL Style Files and Templates

The ACL provides the latest LaTeX templates for *ACL conferences, and paper submissions to *ACL conferences must use the official ACL style templates. The style files can be found at https://github.com/acl-org/acl-style-files.

## Documentclass and Basic Setup

The first line of the file must be `\documentclass[11pt]{article}`, and to load the style file in the review version, use `\usepackage[review]{acl}`. For the final version, omit the review option and use `\usepackage{acl}`.

## Review and Anonymity Options

You can change "review" to "final" to generate the final (camera-ready) version, or change to "preprint" to generate a non-anonymous version with page numbers.

## LuaLaTeX and XeLaTeX Support

The style file `acl.sty` can also be used with LuaLaTeX and XeLaTeX, which are especially suitable for text in non-Latin scripts.

The official GitHub repository at https://github.com/acl-org/acl-style-files is the canonical source for the most current style files and examples.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "f76b723f-4129-4c08-9aa7-ac72d9d4df17",
  "tool_use_result": {
    "query": "ACL 2025 2026 style files LaTeX template acl.sty documentclass options review anonymous",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FWDYLKqpHvByN7t1quupnB",
        "content": [
          {
            "title": "GitHub - acl-org/acl-style-files: Official style files for papers submitted to venues of the Association for Computational Linguistics · GitHub",
            "url": "https://github.com/acl-org/acl-style-files"
          },
          {
            "title": "Association for Computational Linguistics (ACL) conference - Overleaf, Online LaTeX Editor",
            "url": "https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj"
          },
          {
            "title": "Style Files and Guidelines | Computational Linguistics",
            "url": "https://submissions.cljournal.org/index.php/cljournal/StyleGuide"
          },
          {
            "title": "ACL Lab Template - Overleaf, Online LaTeX Editor",
            "url": "https://www.overleaf.com/latex/templates/acl-lab-template/rgdcfpfzshnv"
          },
          {
            "title": "Call for Tutorials -",
            "url": "https://2026.eacl.org/calls/tutorials/"
          },
          {
            "title": "LuaLaTeX and XeLaTeX Template for *ACL Style Files",
            "url": "https://arxiv.org/html/2505.03469v1"
          },
          {
            "title": "Paper formatting guidelines - ACLPUB",
            "url": "https://acl-org.github.io/ACLPUB/formatting.html"
          },
          {
            "title": "Templates - Journals, CVs, Presentations, Reports and More - Overleaf, Online LaTeX Editor",
            "url": "https://www.overleaf.com/latex/templates/tagged/acl"
          },
          {
            "title": "ACL Template | Format, Structure, and Guide",
            "url": "https://scispace.com/templates/acl-template-hjmlcd42ar7fdcg"
          },
          {
            "title": "EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf",
            "url": "https://www.underleaf.ai/templates/emnlp"
          }
        ]
      },
      "Based on the search results, here's what I found about ACL LaTeX template options:\n\n## ACL Style Files and Templates\n\nThe ACL provides the latest LaTeX templates for *ACL conferences, and paper submissions to *ACL conferences must use the official ACL style templates. The style files can be found at https://github.com/acl-org/acl-style-files.\n\n## Documentclass and Basic Setup\n\nThe first line of the file must be `\\documentclass[11pt]{article}`, and to load the style file in the review version, use `\\usepackage[review]{acl}`. For the final version, omit the review option and use `\\usepackage{acl}`.\n\n## Review and Anonymity Options\n\nYou can change \"review\" to \"final\" to generate the final (camera-ready) version, or change to \"preprint\" to generate a non-anonymous version with page numbers.\n\n## LuaLaTeX and XeLaTeX Support\n\nThe style file `acl.sty` can also be used with LuaLaTeX and XeLaTeX, which are especially suitable for text in non-Latin scripts.\n\nThe official GitHub repository at https://github.com/acl-org/acl-style-files is the canonical source for the most current style files and examples."
    ],
    "durationSeconds": 5.549436607999996
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Let me now fetch the GitHub page for the ACL style files to get the exact template details, and also the ACLPUB formatting page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "a835ece7-24fe-4cb9-86e3-ff7d5471f3a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwcZ3k9yKkLmVGA2NsGHvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3055,
      "cache_read_input_tokens": 33139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3055
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

Let me get the final details on the LaTeX template and formatting page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "52591904-5f22-40e1-8ab8-b4d3130bbb62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwcZ3k9yKkLmVGA2NsGHvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3055,
      "cache_read_input_tokens": 33139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3055
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QVyPoE9jWgwKK9q4aKPnwk`</summary>

```json
{
  "url": "https://github.com/acl-org/acl-style-files",
  "prompt": "Extract: what files are in this repo, the current version of acl.sty, the documentclass and usepackage options (review, final, preprint), bibliography style file name, any recent changes or updates. List all files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "7fbdd125-9545-4f90-ba0b-a417f89f9c17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwcZ3k9yKkLmVGA2NsGHvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3055,
      "cache_read_input_tokens": 33139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3055
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

_source line 40_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QNRukYyCR7wqKet4g2Lg1k`</summary>

```json
{
  "url": "https://acl-org.github.io/ACLPUB/formatting.html",
  "prompt": "Extract ALL formatting requirements: paper size, margins, columns, fonts, font sizes, line spacing, line numbers, section formatting, citation style, bibliography format, figure/table placement, page numbering, header/footer, and any other formatting rules. Be exhaustive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "bc011313-6fc0-4626-b34c-56d8ebebb5fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwcZ3k9yKkLmVGA2NsGHvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3055,
      "cache_read_input_tokens": 33139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3055
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

_source line 41_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017QJSgtoykyvsmmD8H7veC1`</summary>

```json
{
  "url": "https://aclrollingreview.org/responsible-nlp-checklist-appendices",
  "prompt": "Extract details about how the responsible NLP checklist will be included as appendices in published papers. What format, when this policy started, how it affects submission."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "f2505987-a0d5-48a8-8af5-611121e080b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwcZ3k9yKkLmVGA2NsGHvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3055,
      "cache_read_input_tokens": 33139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3055
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

_source line 42 · 2026-05-17T07:37:18.837Z_

<details><summary>↩ Tool result · `toolu_01QVyPoE9jWgwKK9q4aKPnwk`</summary>

```text
# ACL Style Files Repository Summary

## Files in the Repository

The repository contains the following key files:

- `README.md`
- `acl.sty` (style file)
- `acl_latex.tex` (example LaTeX document)
- `acl_lualatex.tex` (LuaLaTeX variant)
- `acl_natbib.bst` (bibliography style)
- `anthology.bib.txt` (sample bibliography)
- `custom.bib` (custom bibliography)
- `formatting.md` (formatting guidelines)

## Current Version

The latest release is from **December 20, 2021** (tagged as "2021-12"). The repository shows **317 commits** on the master branch.

## Document Class Options

The provided content does not explicitly list documentclass or usepackage options (such as review, final, or preprint modes). Authors are directed to review `acl_latex.tex` for examples, but those specific details aren't included in the webpage text.

## Bibliography Style

The designated bibliography style file is **`acl_natbib.bst`**.

## Recent Updates

According to the instructions, modifications should be submitted as pull requests to propagate improvements to future conferences. The repository currently has **18 open issues** and **1 pull request** pending.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "f77809cb-0b12-4b02-8422-731f19e767d9",
  "tool_use_result": {
    "bytes": 265022,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Style Files Repository Summary\n\n## Files in the Repository\n\nThe repository contains the following key files:\n\n- `README.md`\n- `acl.sty` (style file)\n- `acl_latex.tex` (example LaTeX document)\n- `acl_lualatex.tex` (LuaLaTeX variant)\n- `acl_natbib.bst` (bibliography style)\n- `anthology.bib.txt` (sample bibliography)\n- `custom.bib` (custom bibliography)\n- `formatting.md` (formatting guidelines)\n\n## Current Version\n\nThe latest release is from **December 20, 2021** (tagged as \"2021-12\"). The repository shows **317 commits** on the master branch.\n\n## Document Class Options\n\nThe provided content does not explicitly list documentclass or usepackage options (such as review, final, or preprint modes). Authors are directed to review `acl_latex.tex` for examples, but those specific details aren't included in the webpage text.\n\n## Bibliography Style\n\nThe designated bibliography style file is **`acl_natbib.bst`**.\n\n## Recent Updates\n\nAccording to the instructions, modifications should be submitted as pull requests to propagate improvements to future conferences. The repository currently has **18 open issues** and **1 pull request** pending.",
    "durationMs": 7304,
    "url": "https://github.com/acl-org/acl-style-files"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-17T07:37:19.419Z_

<details><summary>↩ Tool result · `toolu_017QJSgtoykyvsmmD8H7veC1`</summary>

```text
# Responsible NLP Checklist as Paper Appendices

## Policy Implementation

Starting with EMNLP 2025, completed responsible NLP checklists will be published alongside accepted papers. This requirement will continue with subsequent *ACL conferences.

## Format and Structure

The checklists appear as appendices and "do not count against page limits." They remain separate from the main paper content while being publicly accessible with the published work.

## Key Changes for Authors

Authors must now recognize that their responses will be visible to the research community if their paper is accepted. This visibility requires extra diligence when completing submissions, as "filling them out incorrectly or misleadingly can result in desk rejection."

## Rationale

The policy aims to enhance transparency by allowing researchers to review how authors addressed ethical considerations, selected datasets, acknowledged limitations, and evaluated work. The organizers believe this public scrutiny encourages more thoughtful engagement with responsible research practices.

## Checklist Coverage Areas

The checklist addresses data collection and annotation methods, dataset selection and constraints, training and evaluation procedures, potential research impacts, and computational requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "e451f747-69ef-4358-ae2b-f9850cfce673",
  "tool_use_result": {
    "bytes": 16631,
    "code": 200,
    "codeText": "OK",
    "result": "# Responsible NLP Checklist as Paper Appendices\n\n## Policy Implementation\n\nStarting with EMNLP 2025, completed responsible NLP checklists will be published alongside accepted papers. This requirement will continue with subsequent *ACL conferences.\n\n## Format and Structure\n\nThe checklists appear as appendices and \"do not count against page limits.\" They remain separate from the main paper content while being publicly accessible with the published work.\n\n## Key Changes for Authors\n\nAuthors must now recognize that their responses will be visible to the research community if their paper is accepted. This visibility requires extra diligence when completing submissions, as \"filling them out incorrectly or misleadingly can result in desk rejection.\"\n\n## Rationale\n\nThe policy aims to enhance transparency by allowing researchers to review how authors addressed ethical considerations, selected datasets, acknowledged limitations, and evaluated work. The organizers believe this public scrutiny encourages more thoughtful engagement with responsible research practices.\n\n## Checklist Coverage Areas\n\nThe checklist addresses data collection and annotation methods, dataset selection and constraints, training and evaluation procedures, potential research impacts, and computational requirements.",
    "durationMs": 3849,
    "url": "https://aclrollingreview.org/responsible-nlp-checklist-appendices"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T07:37:31.073Z_

<details><summary>↩ Tool result · `toolu_01QNRukYyCR7wqKet4g2Lg1k`</summary>

```text
# ACL Paper Formatting Requirements

## Paper Size & Margins
- **Paper format:** A4 (21 cm × 29.7 cm / 8.27 × 11.69 inches)
- **Left margin:** 2.5 cm
- **Right margin:** 2.5 cm
- **Top margin:** 2.5 cm
- **Bottom margin:** 2.5 cm

## Column Layout
- **Format:** Two columns (except title, author information, full-width figures/tables)
- **Column width:** 7.7 cm
- **Gap between columns:** 0.6 cm
- **Column height:** 24.7 cm

## Fonts & Sizes
**Primary font:** Times Roman (or Times New Roman/Computer Modern Roman if unavailable)

| Text Element | Size | Style |
|---|---|---|
| Paper title | 15 pt | bold |
| Author names | 12 pt | bold |
| Author affiliation | 12 pt | regular |
| "Abstract" label | 12 pt | bold |
| Section titles | 12 pt | bold |
| Subsection titles | 11 pt | bold |
| Document text | 11 pt | regular |
| Abstract text | 10 pt | regular |
| Figure/table captions | 10 pt | regular |
| Bibliography | 10 pt | regular |
| Footnotes | 9 pt | regular |

## Spacing
- Text: single-spaced
- Abstract: single-spaced
- New paragraph indent: 0.4 cm (except first paragraph after section headings)

## Page Numbers
- **Review version:** centered in bottom margin
- **Final version:** no page numbers

## Line Numbers (Review Version Only)
- Ruler with line numbers in left and right margins required for review versions
- Not required in final version

## Title & Author Section
- Title positioned 2.5 cm from top
- Centered across both columns
- Long titles on two lines without blank line between
- Title case (not all capitals, except acronyms)
- Body text starts 7.5 cm from top of page
- Author names in full (no initials unless standard)
- Complete addresses required; no footnotes for affiliations
- No extra visual content in title box

## Abstract
- Centered "Abstract" label above body
- Width 0.6 cm narrower on each side than normal column
- Maximum 200 words
- Plain text only (no LaTeX commands)

## Section Formatting
- Use numbered sections (Arabic numerals: 1, 2, 3...)
- Subsections numbered with dot notation (e.g., 2.1, 2.3)

## Footnotes
- Positioned at bottom of page
- 9 pt font
- Separated from text by line

## Figures & Tables
- Place near first reference point
- Minimum one column width
- No wrapped text within columns
- Prefer vector formats (PDF, EPS)
- Avoid low-resolution GIF or JPEG
- Sequential numbering: "Figure 1: Caption" and "Table 1: Caption"
- Captions below in 10 pt
- Single-line captions centered; multi-line captions left-aligned
- Ensure grayscale readability; avoid color-only distinctions
- Legible at print and digital viewing sizes

## Hyperlinks
- Dark blue (hex #000099)
- Not underlined or boxed

## Citations
- **Format in text:** Parenthetical "(Author, Year)" or narrative "Author (Year)"
- Two authors: both names
- Three+ authors: first author "et al."
- Multiple citations: collapsed "(A, 1997; B, 1972)"
- Avoid full citations as sentence constituents

## References
- Unnumbered section titled "References"
- Placed before appendices
- Alphabetical ordering by first author (not citation order)
- Include DOIs when available; otherwise ACL Anthology links
- Full author names (no initials)
- Consistent format throughout
- Complete citation information required

## Special Sections

**Limitations section:**
- Titled "Limitations"
- Placed after conclusion, before references
- No page breaks
- Does not count toward page limit
- No additional experiments, figures, or analysis

**Ethical Considerations (optional):**
- Placed after conclusion, before references
- No page breaks
- Does not count toward page limit
- No additional experiments, figures, or analysis

**Acknowledgments:**
- Immediately before references
- Not numbered
- Does not count toward page limit
- Omit from review version

## Appendices
- Two-column format (exception: math-heavy sections may use single column)
- Lettered sequentially: "Appendix A. Title"
- Placed after references
- Same anonymity requirements as main paper
- Same font/margin specifications as main body

## Supplementary Material
- Non-readable materials (code, data) separate uploads
- Should enhance rather than replace main paper content
- Paper should not rely on it for understanding
- Reviewers not required to review supplementary material
- Same anonymity requirements as main paper

## File Format & Technical Requirements
- **Format:** Adobe PDF
- **All fonts embedded** (critical for Asian languages, symbols, tree diagrams)
- Include all fonts when generating PDF (not just non-standard)
- **Verification command:** `pdffonts mypaper.pdf` (all fonts should show "yes" under "emb")

## Non-English Text
- Accompany with English translations
- Non-Latin scripts require Latin transliteration
- Format: "Original text _transliteration_ 'translation'"

## Paper Length
**Long papers:**
- Review version: 8 pages content + unlimited references
- Final version: 9 pages content + unlimited acknowledgments/references

**Short papers:**
- Review version: 4 pages content + unlimited references
- Final version: 5 pages content + unlimited acknowledgments/references

All figures and tables count toward these limits in main text only.

## Metadata
- Plain Unicode text required (no HTML/LaTeX in metadata fields)
- Should match PDF verbatim or approximate closely
- Tools like unicodeit.net helpful for conversion
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "863c0148-059d-4f6f-8205-399d8cd2c865",
  "tool_use_result": {
    "bytes": 29734,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Paper Formatting Requirements\n\n## Paper Size & Margins\n- **Paper format:** A4 (21 cm × 29.7 cm / 8.27 × 11.69 inches)\n- **Left margin:** 2.5 cm\n- **Right margin:** 2.5 cm\n- **Top margin:** 2.5 cm\n- **Bottom margin:** 2.5 cm\n\n## Column Layout\n- **Format:** Two columns (except title, author information, full-width figures/tables)\n- **Column width:** 7.7 cm\n- **Gap between columns:** 0.6 cm\n- **Column height:** 24.7 cm\n\n## Fonts & Sizes\n**Primary font:** Times Roman (or Times New Roman/Computer Modern Roman if unavailable)\n\n| Text Element | Size | Style |\n|---|---|---|\n| Paper title | 15 pt | bold |\n| Author names | 12 pt | bold |\n| Author affiliation | 12 pt | regular |\n| \"Abstract\" label | 12 pt | bold |\n| Section titles | 12 pt | bold |\n| Subsection titles | 11 pt | bold |\n| Document text | 11 pt | regular |\n| Abstract text | 10 pt | regular |\n| Figure/table captions | 10 pt | regular |\n| Bibliography | 10 pt | regular |\n| Footnotes | 9 pt | regular |\n\n## Spacing\n- Text: single-spaced\n- Abstract: single-spaced\n- New paragraph indent: 0.4 cm (except first paragraph after section headings)\n\n## Page Numbers\n- **Review version:** centered in bottom margin\n- **Final version:** no page numbers\n\n## Line Numbers (Review Version Only)\n- Ruler with line numbers in left and right margins required for review versions\n- Not required in final version\n\n## Title & Author Section\n- Title positioned 2.5 cm from top\n- Centered across both columns\n- Long titles on two lines without blank line between\n- Title case (not all capitals, except acronyms)\n- Body text starts 7.5 cm from top of page\n- Author names in full (no initials unless standard)\n- Complete addresses required; no footnotes for affiliations\n- No extra visual content in title box\n\n## Abstract\n- Centered \"Abstract\" label above body\n- Width 0.6 cm narrower on each side than normal column\n- Maximum 200 words\n- Plain text only (no LaTeX commands)\n\n## Section Formatting\n- Use numbered sections (Arabic numerals: 1, 2, 3...)\n- Subsections numbered with dot notation (e.g., 2.1, 2.3)\n\n## Footnotes\n- Positioned at bottom of page\n- 9 pt font\n- Separated from text by line\n\n## Figures & Tables\n- Place near first reference point\n- Minimum one column width\n- No wrapped text within columns\n- Prefer vector formats (PDF, EPS)\n- Avoid low-resolution GIF or JPEG\n- Sequential numbering: \"Figure 1: Caption\" and \"Table 1: Caption\"\n- Captions below in 10 pt\n- Single-line captions centered; multi-line captions left-aligned\n- Ensure grayscale readability; avoid color-only distinctions\n- Legible at print and digital viewing sizes\n\n## Hyperlinks\n- Dark blue (hex #000099)\n- Not underlined or boxed\n\n## Citations\n- **Format in text:** Parenthetical \"(Author, Year)\" or narrative \"Author (Year)\"\n- Two authors: both names\n- Three+ authors: first author \"et al.\"\n- Multiple citations: collapsed \"(A, 1997; B, 1972)\"\n- Avoid full citations as sentence constituents\n\n## References\n- Unnumbered section titled \"References\"\n- Placed before appendices\n- Alphabetical ordering by first author (not citation order)\n- Include DOIs when available; otherwise ACL Anthology links\n- Full author names (no initials)\n- Consistent format throughout\n- Complete citation information required\n\n## Special Sections\n\n**Limitations section:**\n- Titled \"Limitations\"\n- Placed after conclusion, before references\n- No page breaks\n- Does not count toward page limit\n- No additional experiments, figures, or analysis\n\n**Ethical Considerations (optional):**\n- Placed after conclusion, before references\n- No page breaks\n- Does not count toward page limit\n- No additional experiments, figures, or analysis\n\n**Acknowledgments:**\n- Immediately before references\n- Not numbered\n- Does not count toward page limit\n- Omit from review version\n\n## Appendices\n- Two-column format (exception: math-heavy sections may use single column)\n- Lettered sequentially: \"Appendix A. Title\"\n- Placed after references\n- Same anonymity requirements as main paper\n- Same font/margin specifications as main body\n\n## Supplementary Material\n- Non-readable materials (code, data) separate uploads\n- Should enhance rather than replace main paper content\n- Paper should not rely on it for understanding\n- Reviewers not required to review supplementary material\n- Same anonymity requirements as main paper\n\n## File Format & Technical Requirements\n- **Format:** Adobe PDF\n- **All fonts embedded** (critical for Asian languages, symbols, tree diagrams)\n- Include all fonts when generating PDF (not just non-standard)\n- **Verification command:** `pdffonts mypaper.pdf` (all fonts should show \"yes\" under \"emb\")\n\n## Non-English Text\n- Accompany with English translations\n- Non-Latin scripts require Latin transliteration\n- Format: \"Original text _transliteration_ 'translation'\"\n\n## Paper Length\n**Long papers:**\n- Review version: 8 pages content + unlimited references\n- Final version: 9 pages content + unlimited acknowledgments/references\n\n**Short papers:**\n- Review version: 4 pages content + unlimited references\n- Final version: 5 pages content + unlimited acknowledgments/references\n\nAll figures and tables count toward these limits in main text only.\n\n## Metadata\n- Plain Unicode text required (no HTML/LaTeX in metadata fields)\n- Should match PDF verbatim or approximate closely\n- Tools like unicodeit.net helpful for conversion",
    "durationMs": 17183,
    "url": "https://acl-org.github.io/ACLPUB/formatting.html"
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive information. Let me compile the complete answer.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "7554aa63-f790-4a0b-a3b7-f2bd39551eec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcCJ1oUcQqRdpP9aLqedax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 268,
      "cache_creation_input_tokens": 2233,
      "cache_read_input_tokens": 36194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2233
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

_source line 46_

以下是完整调研结果。

---

## 1. 页数限制

| 类型 | Review 版 | Camera-ready 版 |
|---|---|---|
| Long paper 正文 | **8 页** | **9 页**（多 1 页用于 reviewer feedback） |
| Short paper 正文 | **4 页** | **5 页** |
| References | **不占页数** | **不占页数** |
| Limitations section | **不占页数**（必须有，缺失 = desk reject） | 不占页数 |
| Ethical Considerations | **不占页数**（可选） | 不占页数 |
| Appendix | **不占页数**，放在 references 之后 | 不占页数 |
| Acknowledgments | **Review 版不写**（泄露身份） | 不占页数 |

**Limitations section 位置**: 在 Conclusion 之后、References 之前，不能包含新实验/分析/图表。

**Appendix 格式要求**: 必须使用双栏格式（数学密集部分可例外用单栏）。自 **2025 年 7 月 cycle** 起，Appendix 格式不符将 desk reject。

---

## 2. 匿名化要求

**核心规则**:
- 论文中不能出现作者姓名和单位
- 自引必须用第三人称：用 "Smith (2020) showed..." 而不是 "We previously showed..."
- 不能引用 reviewer 无法获取的文件
- Supplementary material 必须完全匿名
- 禁止使用 Dropbox/Google Drive 等可追踪下载的链接，代码需用 Anonymous GitHub
- **Review 版不写 Acknowledgments**

**预印本政策（2024 年 2 月起更新）**:
- **无匿名期**：随时可发 arXiv 预印本
- 但广泛传播会导致更难招到不知道作者身份的 reviewer
- ACL 对未公开发表的匿名投稿设立了特别奖项激励

**LaTeX 匿名化设置**:
```latex
\documentclass[11pt]{article}
\usepackage[review]{acl}    % review 版：匿名 + 行号 + 页码
% \usepackage{acl}           % camera-ready 版：显示作者，无行号
% \usepackage[preprint]{acl} % preprint 版：显示作者 + 页码
```

---

## 3. 必须提交的材料清单

### 必须提交
| 材料 | 格式 | 说明 |
|---|---|---|
| **主 PDF** | ACL 模板格式 PDF，所有字体嵌入 | `pdffonts mypaper.pdf` 验证 |
| **Responsible NLP Research Checklist** | OpenReview 提交表单中填写 | 每项 Yes/No/NA + section 编号或 justification。填写不当可 desk reject。接受后作为附录公开发表 |
| **Limitations section** | 嵌入主 PDF，Conclusion 之后 References 之前 | 缺失 = desk reject |
| **Author Registration Form** | 提交 deadline 后 48 小时内完成 | OpenReview profile 需含 affiliation、Semantic Scholar、DBLP、ACL Anthology 链接 |
| **Reviewer 注册** | 提交 deadline 后 48 小时内注册 reviewer | 2025 年 5 月起所有作者必须参与审稿 |

### EMNLP 2026 特有
| 材料 | 说明 |
|---|---|
| **会议声明（binding）** | 提交时必须在 ARR 表单中选择 EMNLP 2026，否则无法 commit。**选择具有约束力** |

### 可选提交
| 材料 | 格式 | 说明 |
|---|---|---|
| **Ethical Considerations section** | 嵌入主 PDF | 推荐但非必须 |
| **Appendix** | 主 PDF 中 references 之后，双栏格式 | reviewer 不要求阅读 |
| **Software** | 单个 `.tgz` 或 `.zip` | 必须匿名 |
| **Data** | 单独的 `.tgz` 或 `.zip`（与 software 分开） | 必须匿名 |

### 重投 (Resubmission) 额外材料
- 上一次提交的链接
- **Revision summary PDF**：逐条说明如何 address 每位 reviewer 的意见
- 可选：color-coded 修改标记版论文

### Author Response（审稿后）
- 纯文本，不允许外部链接
- 在 Author Response 期间提交，非投稿时准备

---

## 4. LaTeX 模板

**官方仓库**: [github.com/acl-org/acl-style-files](https://github.com/acl-org/acl-style-files)

**文件列表**:
| 文件 | 用途 |
|---|---|
| `acl.sty` | 主样式文件 |
| `acl_latex.tex` | 示例文档 |
| `acl_lualatex.tex` | LuaLaTeX 变体 |
| `acl_natbib.bst` | 参考文献样式 |
| `custom.bib` | 示例 bib |

**基本设置**:
```latex
\documentclass[11pt]{article}
\usepackage[review]{acl}   % review 版必须用 [review] 选项
```

**`[review]` 选项效果**: 隐藏作者信息、开启行号、显示页码

**格式规格**:
- A4 纸 (21cm x 29.7cm)，四边 margin 2.5cm
- 双栏，栏宽 7.7cm，栏间距 0.6cm
- 正文 11pt Times Roman，单倍行距
- 标题 15pt bold，居中跨双栏
- Abstract 最多 200 words，10pt，两侧各缩进 0.6cm
- 引用格式：`acl_natbib.bst`，作者-年制，alphabetical 排序
- References 部分标题为 "References"，不编号
- 超链接深蓝色 (#000099)，无下划线

**禁止修改 sty 文件**。不符合格式的论文不经审阅直接拒稿。

---

## 5. Responsible NLP Research Checklist（逐项）

每项回答 **Yes / No / NA**，Yes 需给出 section 编号，No/NA 需给出 justification。接受后作为论文附录公开发表。

### Section A: 所有提交必答

| 编号 | 问题 |
|---|---|
| **A1** | 是否描述了工作的 limitations？（假设、鲁棒性、claim 范围、影响因素） |
| **A2** | 是否讨论了潜在风险？（恶意使用、环境影响、公平性、隐私、安全、过度泛化、双重用途） |

### Section B: 使用了科学制品（代码/数据/模型）

| 编号 | 问题 |
|---|---|
| **B1** | 是否引用了所用制品的创建者？（原始论文、版本号、URL） |
| **B2** | 是否讨论了 license/使用条款？ |
| **B3** | 是否讨论了使用方式是否符合制品的 intended use？ |
| **B4** | 是否检查了个人身份信息和冒犯性内容？ |
| **B5** | 是否提供了制品文档？（语言、领域、人口统计信息、data card） |
| **B6** | 是否报告了数据集相关统计？（样本数、train/dev/test 划分） |

### Section C: 计算实验

| 编号 | 问题 |
|---|---|
| **C1** | 是否报告了模型参数量、计算预算、硬件基础设施？ |
| **C2** | 是否讨论了实验设置（含超参搜索）？ |
| **C3** | 是否报告了结果的描述性统计？（error bars、置信区间、max/mean/single run） |
| **C4** | 是否报告了使用的现有包的实现细节？（版本号、参数设置、修改） |

### Section D: 涉及人类标注者/参与者

| 编号 | 问题 |
|---|---|
| **D1** | 是否报告了完整的参与者指令文本？ |
| **D2** | 是否报告了招募方式和报酬？ |
| **D3** | 是否讨论了数据使用的知情同意？ |
| **D4** | 是否经过伦理审查委员会批准？ |
| **D5** | 是否报告了标注者的人口统计和地理特征？ |

### Section E: AI 辅助使用

| 编号 | 问题 |
|---|---|
| **E1** | 如使用了 AI 辅助（ChatGPT、Copilot 等），是否披露？ |

**重要**: AI 写作辅助必须在 checklist + Acknowledgments 中披露（语法检查和语言润色除外）。

---

## 6. 投稿时间线（EMNLP 2026 / ARR May 2026 Cycle）

| 事件 | 日期 |
|---|---|
| **ARR 提交截止** | **2026-05-25**（AoE） |
| Reviewer 注册截止 | 2026-05-27 |
| Reviews due | 2026-06-29 |
| **Author Response** | **2026-07-07 至 07-13** |
| Meta-reviews 发布 | 2026-07-30 |
| **EMNLP 2026 Commitment 截止** | **2026-08-02** |
| **Acceptance Notification** | **2026-08-20** |
| **Camera-ready** | **2026-09-20** |
| **会议日期** | **2026-10-24 至 10-29** |

也可以用 **March 2026 cycle**（提交截止 2026-03-16）的论文在 08-02 之前 commit 到 EMNLP 2026。

---

## 7. 其他关键政策

- **文本复用**: 来自其他出版物的文本不超过总 token 的 10%
- **Dual submission 禁止**: ARR review 期间不能同时在其他 archival venue 投稿
- **Hallucinated citations**: 虚假引用将 desk reject，作者将被禁止 commit EMNLP 2026 和 2027
- **Author list 修改**: commit 阶段禁止修改作者列表（可改顺序）
- **Presentation 要求**: 所有接受论文必须在会议上 present 才能出现在 proceedings 中

Sources:
- [ARR Call for Papers](https://aclrollingreview.org/cfp)
- [ARR Authors Guidelines](https://aclrollingreview.org/authors)
- [ARR Dates and Venues](https://aclrollingreview.org/dates)
- [ARR Anonymity Policy](https://aclrollingreview.org/anonymity/)
- [ARR Responsible NLP Research Checklist](https://aclrollingreview.org/responsibleNLPresearch/)
- [ARR Checklist as Appendices Policy](https://aclrollingreview.org/responsible-nlp-checklist-appendices)
- [ARR Common Submission Problems](https://aclrollingreview.org/authorchecklist)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Style Files (GitHub)](https://github.com/acl-org/acl-style-files)
- [ACLPUB Formatting Guidelines](https://acl-org.github.io/ACLPUB/formatting.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "uuid": "97e875b1-b719-4550-9d10-702d85d88fbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcCJ1oUcQqRdpP9aLqedax",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 268,
      "cache_creation_input_tokens": 2233,
      "cache_read_input_tokens": 36194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2233
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

### Task result

_source line 47_

以下是完整调研结果。

---

## 1. 页数限制

| 类型 | Review 版 | Camera-ready 版 |
|---|---|---|
| Long paper 正文 | **8 页** | **9 页**（多 1 页用于 reviewer feedback） |
| Short paper 正文 | **4 页** | **5 页** |
| References | **不占页数** | **不占页数** |
| Limitations section | **不占页数**（必须有，缺失 = desk reject） | 不占页数 |
| Ethical Considerations | **不占页数**（可选） | 不占页数 |
| Appendix | **不占页数**，放在 references 之后 | 不占页数 |
| Acknowledgments | **Review 版不写**（泄露身份） | 不占页数 |

**Limitations section 位置**: 在 Conclusion 之后、References 之前，不能包含新实验/分析/图表。

**Appendix 格式要求**: 必须使用双栏格式（数学密集部分可例外用单栏）。自 **2025 年 7 月 cycle** 起，Appendix 格式不符将 desk reject。

---

## 2. 匿名化要求

**核心规则**:
- 论文中不能出现作者姓名和单位
- 自引必须用第三人称：用 "Smith (2020) showed..." 而不是 "We previously showed..."
- 不能引用 reviewer 无法获取的文件
- Supplementary material 必须完全匿名
- 禁止使用 Dropbox/Google Drive 等可追踪下载的链接，代码需用 Anonymous GitHub
- **Review 版不写 Acknowledgments**

**预印本政策（2024 年 2 月起更新）**:
- **无匿名期**：随时可发 arXiv 预印本
- 但广泛传播会导致更难招到不知道作者身份的 reviewer
- ACL 对未公开发表的匿名投稿设立了特别奖项激励

**LaTeX 匿名化设置**:
```latex
\documentclass[11pt]{article}
\usepackage[review]{acl}    % review 版：匿名 + 行号 + 页码
% \usepackage{acl}           % camera-ready 版：显示作者，无行号
% \usepackage[preprint]{acl} % preprint 版：显示作者 + 页码
```

---

## 3. 必须提交的材料清单

### 必须提交
| 材料 | 格式 | 说明 |
|---|---|---|
| **主 PDF** | ACL 模板格式 PDF，所有字体嵌入 | `pdffonts mypaper.pdf` 验证 |
| **Responsible NLP Research Checklist** | OpenReview 提交表单中填写 | 每项 Yes/No/NA + section 编号或 justification。填写不当可 desk reject。接受后作为附录公开发表 |
| **Limitations section** | 嵌入主 PDF，Conclusion 之后 References 之前 | 缺失 = desk reject |
| **Author Registration Form** | 提交 deadline 后 48 小时内完成 | OpenReview profile 需含 affiliation、Semantic Scholar、DBLP、ACL Anthology 链接 |
| **Reviewer 注册** | 提交 deadline 后 48 小时内注册 reviewer | 2025 年 5 月起所有作者必须参与审稿 |

### EMNLP 2026 特有
| 材料 | 说明 |
|---|---|
| **会议声明（binding）** | 提交时必须在 ARR 表单中选择 EMNLP 2026，否则无法 commit。**选择具有约束力** |

### 可选提交
| 材料 | 格式 | 说明 |
|---|---|---|
| **Ethical Considerations section** | 嵌入主 PDF | 推荐但非必须 |
| **Appendix** | 主 PDF 中 references 之后，双栏格式 | reviewer 不要求阅读 |
| **Software** | 单个 `.tgz` 或 `.zip` | 必须匿名 |
| **Data** | 单独的 `.tgz` 或 `.zip`（与 software 分开） | 必须匿名 |

### 重投 (Resubmission) 额外材料
- 上一次提交的链接
- **Revision summary PDF**：逐条说明如何 address 每位 reviewer 的意见
- 可选：color-coded 修改标记版论文

### Author Response（审稿后）
- 纯文本，不允许外部链接
- 在 Author Response 期间提交，非投稿时准备

---

## 4. LaTeX 模板

**官方仓库**: [github.com/acl-org/acl-style-files](https://github.com/acl-org/acl-style-files)

**文件列表**:
| 文件 | 用途 |
|---|---|
| `acl.sty` | 主样式文件 |
| `acl_latex.tex` | 示例文档 |
| `acl_lualatex.tex` | LuaLaTeX 变体 |
| `acl_natbib.bst` | 参考文献样式 |
| `custom.bib` | 示例 bib |

**基本设置**:
```latex
\documentclass[11pt]{article}
\usepackage[review]{acl}   % review 版必须用 [review] 选项
```

**`[review]` 选项效果**: 隐藏作者信息、开启行号、显示页码

**格式规格**:
- A4 纸 (21cm x 29.7cm)，四边 margin 2.5cm
- 双栏，栏宽 7.7cm，栏间距 0.6cm
- 正文 11pt Times Roman，单倍行距
- 标题 15pt bold，居中跨双栏
- Abstract 最多 200 words，10pt，两侧各缩进 0.6cm
- 引用格式：`acl_natbib.bst`，作者-年制，alphabetical 排序
- References 部分标题为 "References"，不编号
- 超链接深蓝色 (#000099)，无下划线

**禁止修改 sty 文件**。不符合格式的论文不经审阅直接拒稿。

---

## 5. Responsible NLP Research Checklist（逐项）

每项回答 **Yes / No / NA**，Yes 需给出 section 编号，No/NA 需给出 justification。接受后作为论文附录公开发表。

### Section A: 所有提交必答

| 编号 | 问题 |
|---|---|
| **A1** | 是否描述了工作的 limitations？（假设、鲁棒性、claim 范围、影响因素） |
| **A2** | 是否讨论了潜在风险？（恶意使用、环境影响、公平性、隐私、安全、过度泛化、双重用途） |

### Section B: 使用了科学制品（代码/数据/模型）

| 编号 | 问题 |
|---|---|
| **B1** | 是否引用了所用制品的创建者？（原始论文、版本号、URL） |
| **B2** | 是否讨论了 license/使用条款？ |
| **B3** | 是否讨论了使用方式是否符合制品的 intended use？ |
| **B4** | 是否检查了个人身份信息和冒犯性内容？ |
| **B5** | 是否提供了制品文档？（语言、领域、人口统计信息、data card） |
| **B6** | 是否报告了数据集相关统计？（样本数、train/dev/test 划分） |

### Section C: 计算实验

| 编号 | 问题 |
|---|---|
| **C1** | 是否报告了模型参数量、计算预算、硬件基础设施？ |
| **C2** | 是否讨论了实验设置（含超参搜索）？ |
| **C3** | 是否报告了结果的描述性统计？（error bars、置信区间、max/mean/single run） |
| **C4** | 是否报告了使用的现有包的实现细节？（版本号、参数设置、修改） |

### Section D: 涉及人类标注者/参与者

| 编号 | 问题 |
|---|---|
| **D1** | 是否报告了完整的参与者指令文本？ |
| **D2** | 是否报告了招募方式和报酬？ |
| **D3** | 是否讨论了数据使用的知情同意？ |
| **D4** | 是否经过伦理审查委员会批准？ |
| **D5** | 是否报告了标注者的人口统计和地理特征？ |

### Section E: AI 辅助使用

| 编号 | 问题 |
|---|---|
| **E1** | 如使用了 AI 辅助（ChatGPT、Copilot 等），是否披露？ |

**重要**: AI 写作辅助必须在 checklist + Acknowledgments 中披露（语法检查和语言润色除外）。

---

## 6. 投稿时间线（EMNLP 2026 / ARR May 2026 Cycle）

| 事件 | 日期 |
|---|---|
| **ARR 提交截止** | **2026-05-25**（AoE） |
| Reviewer 注册截止 | 2026-05-27 |
| Reviews due | 2026-06-29 |
| **Author Response** | **2026-07-07 至 07-13** |
| Meta-reviews 发布 | 2026-07-30 |
| **EMNLP 2026 Commitment 截止** | **2026-08-02** |
| **Acceptance Notification** | **2026-08-20** |
| **Camera-ready** | **2026-09-20** |
| **会议日期** | **2026-10-24 至 10-29** |

也可以用 **March 2026 cycle**（提交截止 2026-03-16）的论文在 08-02 之前 commit 到 EMNLP 2026。

---

## 7. 其他关键政策

- **文本复用**: 来自其他出版物的文本不超过总 token 的 10%
- **Dual submission 禁止**: ARR review 期间不能同时在其他 archival venue 投稿
- **Hallucinated citations**: 虚假引用将 desk reject，作者将被禁止 commit EMNLP 2026 和 2027
- **Author list 修改**: commit 阶段禁止修改作者列表（可改顺序）
- **Presentation 要求**: 所有接受论文必须在会议上 present 才能出现在 proceedings 中

Sources:
- [ARR Call for Papers](https://aclrollingreview.org/cfp)
- [ARR Authors Guidelines](https://aclrollingreview.org/authors)
- [ARR Dates and Venues](https://aclrollingreview.org/dates)
- [ARR Anonymity Policy](https://aclrollingreview.org/anonymity/)
- [ARR Responsible NLP Research Checklist](https://aclrollingreview.org/responsibleNLPresearch/)
- [ARR Checklist as Appendices Policy](https://aclrollingreview.org/responsible-nlp-checklist-appendices)
- [ARR Common Submission Problems](https://aclrollingreview.org/authorchecklist)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Style Files (GitHub)](https://github.com/acl-org/acl-style-files)
- [ACLPUB Formatting Guidelines](https://acl-org.github.io/ACLPUB/formatting.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 158972,
  "duration_api_ms": 233928,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "a1352e37-9efa-4fe8-abfb-a68644be2670",
  "total_cost_usd": 0.6043245000000002,
  "usage": {
    "input_tokens": 721,
    "cache_creation_input_tokens": 26586,
    "cache_read_input_tokens": 161568,
    "output_tokens": 5286,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26586,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 268,
        "output_tokens": 3501,
        "cache_read_input_tokens": 36194,
        "cache_creation_input_tokens": 2233,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2233
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 126533,
      "outputTokens": 9018,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 5,
      "costUSD": 0.22162300000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 721,
      "outputTokens": 5286,
      "cacheReadInputTokens": 161568,
      "cacheCreationInputTokens": 26586,
      "webSearchRequests": 0,
      "costUSD": 0.3827015,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7d1becab-f687-4cab-a287-b9d31c75b94f"
}
```

</details>

---
