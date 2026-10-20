# Research conversation: Search for the AAAI 2027 call for papers and submission deadlines. The claim is: - AAAI 2027 abstracts due July 21, 2026

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-afb02f375b1177c66.jsonl`
- **Structured JSON:** [`fb75cb2729d31253f14c.json`](../../sessions/fb/fb75cb2729d31253f14c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-17T09:03:55.426Z_

Search for the AAAI 2027 call for papers and submission deadlines. The claim is:
- AAAI 2027 abstracts due July 21, 2026
- AAAI 2027 full papers due July 28, 2026

Also search for:
- ARR (ACL Rolling Review) August 2026 submission deadline
- EACL 2027 commitment deadline (claimed: October 11, 2026)

Use WebSearch with queries like:
- "AAAI 2027 call for papers deadline"
- "AAAI 2027 submission deadline July 2026"
- "ACL Rolling Review August 2026 deadline"
- "EACL 2027 commitment deadline"

Report what you find about these deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "afb02f375b1177c66",
  "type": "user",
  "uuid": "272194e9-9a5b-4c60-b692-b5fc5af9156c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T09:03:55.428Z_

```json
{
  "parentUuid": "272194e9-9a5b-4c60-b692-b5fc5af9156c",
  "isSidechain": true,
  "agentId": "afb02f375b1177c66",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "97320ec5-8531-43a0-b9ed-df0fc25731d0",
  "timestamp": "2026-05-17T09:03:55.428Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T09:03:58.543Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CH1jBmn34RnE9WTeN3Dmh7`</summary>

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
  "parentUuid": "97320ec5-8531-43a0-b9ed-df0fc25731d0",
  "isSidechain": true,
  "agentId": "afb02f375b1177c66",
  "requestId": "req_011Cb7sYPBCM7B4846vvhN9H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03dbd31b-a7bb-4e98-9719-60b658c6fb09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wzw9wTDhkva1uTomLAP1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 737
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 737,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T09:03:58.547Z_

<details><summary>↩ Tool result · `toolu_01CH1jBmn34RnE9WTeN3Dmh7`</summary>

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
  "parentUuid": "03dbd31b-a7bb-4e98-9719-60b658c6fb09",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "afb02f375b1177c66",
  "type": "user",
  "uuid": "1c9c1f10-ce00-49ef-99ae-05b16ec4dec4",
  "sourceToolAssistantUUID": "03dbd31b-a7bb-4e98-9719-60b658c6fb09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T09:04:01.830Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017pKn6yCoyBDL172LYLDQ8w`</summary>

```json
{
  "query": "AAAI 2027 call for papers deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c9c1f10-ce00-49ef-99ae-05b16ec4dec4",
  "isSidechain": true,
  "agentId": "afb02f375b1177c66",
  "requestId": "req_011Cb7sYck1wrV2MWWNdbLYd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35b93ee0-32bc-4a15-bceb-d1e8ba131862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyQAVvh1TdsoaC4W1g21W9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T09:04:01.862Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AQmuLnTuS4iGec56xkJUYu`</summary>

```json
{
  "query": "AAAI 2027 submission deadline July 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35b93ee0-32bc-4a15-bceb-d1e8ba131862",
  "isSidechain": true,
  "agentId": "afb02f375b1177c66",
  "requestId": "req_011Cb7sYck1wrV2MWWNdbLYd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3144b82-9821-4ae4-a506-1c6901c5e399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyQAVvh1TdsoaC4W1g21W9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T09:04:02.284Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JdStZZMiXLCu2FRaBVtiMC`</summary>

```json
{
  "query": "ACL Rolling Review August 2026 deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3144b82-9821-4ae4-a506-1c6901c5e399",
  "isSidechain": true,
  "agentId": "afb02f375b1177c66",
  "requestId": "req_011Cb7sYck1wrV2MWWNdbLYd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e425fecc-83bc-413d-abbd-ec351df9bb88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyQAVvh1TdsoaC4W1g21W9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T09:04:02.455Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DgGVAqyFxdGRUKxGo7BBAn`</summary>

```json
{
  "query": "EACL 2027 commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e425fecc-83bc-413d-abbd-ec351df9bb88",
  "isSidechain": true,
  "agentId": "afb02f375b1177c66",
  "requestId": "req_011Cb7sYck1wrV2MWWNdbLYd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e9a7db6-dfb1-4108-a6f1-55d264f2e771",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyQAVvh1TdsoaC4W1g21W9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8960,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 200,
          "cache_read_input_tokens": 8960,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T09:04:05.997Z_

<details><summary>↩ Tool result · `toolu_01AQmuLnTuS4iGec56xkJUYu`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline July 2026"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AAAI Conference on Artificial Intelligence","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"}]

Based on the web search results, I found the specific submission deadlines for AAAI 2027:

For AAAI-27 (February 16-23, 2027 in Montréal, Canada), the submission deadlines are:
- June 17, 2026: Open Review submission site opens for author registration
- June 24, 2026: Open Review submission site opens for paper submission
- July 21, 2026: Abstracts due at 11:59 PM UTC-12
- July 28, 2026: Full papers due at 11:59 PM UTC-12
- July 31, 2026: Supplementary material and code due by 11:59 PM UTC-12

These deadlines fall within the July 2026 timeframe you mentioned, with the main abstract and paper submission deadlines occurring in late July 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3144b82-9821-4ae4-a506-1c6901c5e399",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "afb02f375b1177c66",
  "type": "user",
  "uuid": "316b3fd4-46ff-417d-a405-1e7c54628b99",
  "sourceToolAssistantUUID": "a3144b82-9821-4ae4-a506-1c6901c5e399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T09:04:06.607Z_

<details><summary>↩ Tool result · `toolu_017pKn6yCoyBDL172LYLDQ8w`</summary>

```text
Web search results for query: "AAAI 2027 call for papers deadline"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"}]

Based on the search results, here's the information about AAAI 2027 call for papers deadlines:

The AAAI 2027 conference will be held February 16-23, 2027 in Montréal, Canada. For the Main Technical Track, all deadlines are "anywhere on earth" (UTC-12), with the following key dates:
- June 17, 2026: Open Review submission site opens for author registration
- June 24, 2026: Open Review submission site opens for paper submission
- July 21, 2026: Abstracts due at 11:59 PM UTC-12
- July 28, 2026: Full papers due at 11:59 PM UTC-12
- July 31, 2026: Supplementary material and code due by 11:59 PM UTC-12

Note that deadlines are track-specific and may differ from those listed above, with track-specific deadlines listed on their respective CFP.

The official call for papers can be found at the AAAI conference website for more details on other tracks and submission guidelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35b93ee0-32bc-4a15-bceb-d1e8ba131862",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "afb02f375b1177c66",
  "type": "user",
  "uuid": "ed6cf9fd-6687-493e-83fe-f9929efb9b4c",
  "sourceToolAssistantUUID": "35b93ee0-32bc-4a15-bceb-d1e8ba131862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T09:04:06.803Z_

<details><summary>↩ Tool result · `toolu_01JdStZZMiXLCu2FRaBVtiMC`</summary>

```text
Web search results for query: "ACL Rolling Review August 2026 deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL Rolling Review deadlines related to August 2026:

For EACL 2027, the Final ARR Submission Date is August 3, 2026, and the Commitment Date is October 11, 2026.

Additionally, for AACL 2026, the Final ARR Submission Date is May 25, 2026, with a Commitment Date of August 26, 2026.

These are the key August 2026 deadlines associated with ACL Rolling Review. The August 3 date applies to papers being submitted for EACL 2027 consideration, while August 26 is the commitment deadline for papers targeting AACL 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e425fecc-83bc-413d-abbd-ec351df9bb88",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "afb02f375b1177c66",
  "type": "user",
  "uuid": "db635f54-773a-4563-83a7-dc7d412f5ec8",
  "sourceToolAssistantUUID": "e425fecc-83bc-413d-abbd-ec351df9bb88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T09:04:07.114Z_

<details><summary>↩ Tool result · `toolu_01DgGVAqyFxdGRUKxGo7BBAn`</summary>

```text
Web search results for query: "EACL 2027 commitment deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EACL: Conference of the European Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=785"},{"title":"eaclmeeting on X: \"📢⚠️ IMPORTANT DATE CORRECTION: the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle! 📚 All areas of CL/NLP + related fields welcome. Full CfP coming soon. #NLProc #EACL2027\" / X","url":"https://x.com/eaclmeeting/status/2051971432171688436"},{"title":"EACL 2027 Call for Main Conference Papers","url":"https://2027.eacl.org/calls/papers/"},{"title":"EACL","url":"https://eacl.org/conferences/"},{"title":"eaclmeeting (@eaclmeeting) / X","url":"https://x.com/eaclmeeting?lang=en"},{"title":"eaclmeeting","url":"https://twitter.com/eaclmeeting?lang=en"}]

Based on the search results, I found information about EACL 2027 deadlines:

The ARR deadline for EACL 2027 is August 3, 2026. EACL is earlier than usual in 2027, so this is the only viable ARR cycle.

However, I should note that the specific "commitment deadline" for EACL 2027 is not yet publicly available. The Program Committee is currently finalizing the comprehensive Call for Papers and detailed timetable for EACL 2027, and while the primary submission deadline has been shared, the full list of topics and submission policies is still being prepared.

For EACL 2027, which will take place March 9-14, 2027 in Athens, Greece, you may want to check the official EACL 2027 website (https://2027.eacl.org/) for updates on the commitment deadline once the full Call for Papers is released.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e9a7db6-dfb1-4108-a6f1-55d264f2e771",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "afb02f375b1177c66",
  "type": "user",
  "uuid": "66e79ed9-31dc-40c4-8b68-749189c8a243",
  "sourceToolAssistantUUID": "9e9a7db6-dfb1-4108-a6f1-55d264f2e771",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T09:04:10.222Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JMA1d35HBW7ixyvKaNzwdW`</summary>

```json
{
  "query": "EACL 2027 commitment deadline October 2026 ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66e79ed9-31dc-40c4-8b68-749189c8a243",
  "isSidechain": true,
  "agentId": "afb02f375b1177c66",
  "requestId": "req_011Cb7sZFAX1gfbY2bT7rkSM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39216863-271d-4b5f-9ee2-f7ccbf432075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cDT5NoZbJqUeNUX8fDDDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 10352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3023,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T09:04:10.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ARdfq6eN6ny3gZ6xj44cGV`</summary>

```json
{
  "query": "ACL Rolling Review August 2026 submission deadline date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39216863-271d-4b5f-9ee2-f7ccbf432075",
  "isSidechain": true,
  "agentId": "afb02f375b1177c66",
  "requestId": "req_011Cb7sZFAX1gfbY2bT7rkSM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8f8cf81-d7d7-4a73-86a6-259d71e01939",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cDT5NoZbJqUeNUX8fDDDR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 10352,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3023
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 10352,
          "cache_creation_input_tokens": 3023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3023,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T09:04:13.607Z_

<details><summary>↩ Tool result · `toolu_01ARdfq6eN6ny3gZ6xj44cGV`</summary>

```text
Web search results for query: "ACL Rolling Review August 2026 submission deadline date"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, the ACL Rolling Review August 2026 submission deadline date is August 3. This cycle is specifically associated with EACL 2027, which has a commitment date of October 11, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8f8cf81-d7d7-4a73-86a6-259d71e01939",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "afb02f375b1177c66",
  "type": "user",
  "uuid": "ed9590d6-c02e-4e9f-8113-dbc692efe31f",
  "sourceToolAssistantUUID": "b8f8cf81-d7d7-4a73-86a6-259d71e01939",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T09:04:14.109Z_

<details><summary>↩ Tool result · `toolu_01JMA1d35HBW7ixyvKaNzwdW`</summary>

```text
Web search results for query: "EACL 2027 commitment deadline October 2026 ARR"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"EACL 2026 SRW ARR Commitment | OpenReview","url":"https://openreview.net/group?id=eacl.org%2FEACL%2F2026%2FSRW_ARR_Commitment"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EACL: Conference of the European Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=785"},{"title":"[CFP] EACL 2026 First Call for Main Conference Papers - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/HGYEUOYJ7WT62MAJDKESVPD7QQ77WNXA/"}]

Based on the search results, here's what I found regarding EACL 2027 and the ARR commitment deadline in October 2026:

For EACL 2027, the final ARR submission date is August 3, 2026, and the commitment date is October 11, 2026. The EACL 2027 conference is scheduled to take place in March 9-14, 2027, in Athens, Greece.

This means authors who submit papers to ARR before the August 3, 2026 deadline will have their reviews available and can commit their papers to EACL 2027 by October 11, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39216863-271d-4b5f-9ee2-f7ccbf432075",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "afb02f375b1177c66",
  "type": "user",
  "uuid": "47eec73a-9738-4bd2-83e4-846a376031f6",
  "sourceToolAssistantUUID": "39216863-271d-4b5f-9ee2-f7ccbf432075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T09:04:59.392Z_

Here is what I found about each of the claimed deadlines:

---

## AAAI 2027 (February 16-23, 2027, Montreal, Canada)

**Both claims are CONFIRMED:**

- **Abstracts due: July 21, 2026** (11:59 PM UTC-12) -- Confirmed
- **Full papers due: July 28, 2026** (11:59 PM UTC-12) -- Confirmed

Additional dates found:
- June 17, 2026: OpenReview submission site opens for author registration
- June 24, 2026: OpenReview submission site opens for paper submission
- July 31, 2026: Supplementary material and code due

---

## ACL Rolling Review (ARR) August 2026

The ARR August 2026 submission deadline is **August 3, 2026**. This is the final ARR cycle that feeds into EACL 2027 (and it was noted that EACL is earlier than usual in 2027, making this the only viable ARR cycle for that venue).

---

## EACL 2027 (March 9-14, 2027, Athens, Greece)

**Claim CONFIRMED:**

- **Commitment deadline: October 11, 2026** -- Confirmed

The full timeline for EACL 2027 via ARR:
- Final ARR submission date: August 3, 2026
- Commitment deadline: October 11, 2026

---

## Summary

All claimed deadlines check out:

| Conference | Deadline | Claimed Date | Status |
|---|---|---|---|
| AAAI 2027 | Abstracts due | July 21, 2026 | Confirmed |
| AAAI 2027 | Full papers due | July 28, 2026 | Confirmed |
| ARR August 2026 | Submission deadline | August 3, 2026 | Found (no specific claim to verify) |
| EACL 2027 | Commitment deadline | October 11, 2026 | Confirmed |

---

Sources:
- [AAAI-27 Main Technical Track Call for Papers](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [AAAI 2027 - AI Deadlines](http://aideadlines.org/conference/?id=aaai27)
- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)
- [EACL 2027 Official Site](https://2027.eacl.org/)
- [EACL 2027 Call for Papers](https://2027.eacl.org/calls/papers/)
- [EACL Meeting on X (date correction announcement)](https://x.com/eaclmeeting/status/2051971432171688436)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47eec73a-9738-4bd2-83e4-846a376031f6",
  "isSidechain": true,
  "agentId": "afb02f375b1177c66",
  "requestId": "req_011Cb7sZm4c1g3FAxBrJuPbM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5eed9f02-4b43-4513-9484-701e7a40aba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014thw2DxBF1Wtw3PQMCyA4g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 539,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 13375,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 812
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 539,
          "output_tokens": 702,
          "cache_read_input_tokens": 13375,
          "cache_creation_input_tokens": 812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 812,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
