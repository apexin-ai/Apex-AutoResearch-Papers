# Research conversation: Search the web for "ARR submission deadline May 2026" or "ACL Rolling Review May 2026 deadline" to verify whether there 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a075189d942fa438d.jsonl`
- **Structured JSON:** [`3f2f694a785c05124ad5.json`](../../sessions/3f/3f2f694a785c05124ad5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-16T09:47:18.716Z_

Search the web for "ARR submission deadline May 2026" or "ACL Rolling Review May 2026 deadline" to verify whether there is an ARR submission deadline around May 25, 2026 for EMNLP 2026. Also check what the EMNLP 2026 commitment deadline is. Use WebSearch.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a075189d942fa438d",
  "type": "user",
  "uuid": "8e19b90a-4d87-4606-976d-7fe86f2c43da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T09:47:18.719Z_

```json
{
  "parentUuid": "8e19b90a-4d87-4606-976d-7fe86f2c43da",
  "isSidechain": true,
  "agentId": "a075189d942fa438d",
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
  "uuid": "b059c068-0f5e-44d3-acb6-36ab2f082ef7",
  "timestamp": "2026-05-16T09:47:18.719Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T09:47:22.039Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0161QxdXwxjgycZL1xdodWWK`</summary>

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
  "parentUuid": "b059c068-0f5e-44d3-acb6-36ab2f082ef7",
  "isSidechain": true,
  "agentId": "a075189d942fa438d",
  "requestId": "req_011Cb633NHidg3VivLB6DiDM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e5160e7-a4ff-47f2-8973-2ac97c6c8d54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzACUYwXRMSUYrkrXAe2k8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 628,
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

_source line 4 · 2026-05-16T09:47:22.042Z_

<details><summary>↩ Tool result · `toolu_0161QxdXwxjgycZL1xdodWWK`</summary>

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
  "parentUuid": "2e5160e7-a4ff-47f2-8973-2ac97c6c8d54",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a075189d942fa438d",
  "type": "user",
  "uuid": "87e755e5-994d-47a7-a7cf-09cb65a4c54d",
  "sourceToolAssistantUUID": "2e5160e7-a4ff-47f2-8973-2ac97c6c8d54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T09:47:24.822Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LdmmbKa5GkcefWtD66y4kg`</summary>

```json
{
  "query": "ARR submission deadline May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87e755e5-994d-47a7-a7cf-09cb65a4c54d",
  "isSidechain": true,
  "agentId": "a075189d942fa438d",
  "requestId": "req_011Cb633cWj95kTTDP4gfGkT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4977e81-b45e-4522-acfe-ea4d380ca0fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5V1gRiyr6n4KcpgLgnwnv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 6 · 2026-05-16T09:47:24.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JEhaVJhhYvs2cyd9wYQr7w`</summary>

```json
{
  "query": "ACL Rolling Review May 2026 deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4977e81-b45e-4522-acfe-ea4d380ca0fd",
  "isSidechain": true,
  "agentId": "a075189d942fa438d",
  "requestId": "req_011Cb633cWj95kTTDP4gfGkT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f660a00c-b51b-4867-954f-603bbc9f8b2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5V1gRiyr6n4KcpgLgnwnv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 7 · 2026-05-16T09:47:25.027Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qm8UkVssnzyYGEhnffUAs6`</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f660a00c-b51b-4867-954f-603bbc9f8b2a",
  "isSidechain": true,
  "agentId": "a075189d942fa438d",
  "requestId": "req_011Cb633cWj95kTTDP4gfGkT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53e98aea-e83e-45e9-b57e-e5b65a966191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5V1gRiyr6n4KcpgLgnwnv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8851,
      "output_tokens": 149,
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
          "output_tokens": 149,
          "cache_read_input_tokens": 8851,
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

_source line 8 · 2026-05-16T09:47:27.653Z_

<details><summary>↩ Tool result · `toolu_01LdmmbKa5GkcefWtD66y4kg`</summary>

```text
Web search results for query: "ARR submission deadline May 2026"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"}]

Based on the search results, the ARR submission deadline for May 2026 is May 25, 2026. This deadline applies to papers being submitted to the ACL Rolling Review system for consideration at conferences like EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4977e81-b45e-4522-acfe-ea4d380ca0fd",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a075189d942fa438d",
  "type": "user",
  "uuid": "350b1a89-23d9-470a-ab5c-af9eedb4c813",
  "sourceToolAssistantUUID": "f4977e81-b45e-4522-acfe-ea4d380ca0fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T09:47:28.194Z_

<details><summary>↩ Tool result · `toolu_01Qm8UkVssnzyYGEhnffUAs6`</summary>

```text
Web search results for query: "EMNLP 2026 commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"}]

Based on the search results, here is the EMNLP 2026 commitment deadline information:

The EMNLP commitment deadline is August 2, 2026.

For additional context, papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53e98aea-e83e-45e9-b57e-e5b65a966191",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a075189d942fa438d",
  "type": "user",
  "uuid": "702cf6b9-7058-44eb-95d5-a86355e19aca",
  "sourceToolAssistantUUID": "53e98aea-e83e-45e9-b57e-e5b65a966191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T09:47:30.020Z_

<details><summary>↩ Tool result · `toolu_01JEhaVJhhYvs2cyd9wYQr7w`</summary>

```text
Web search results for query: "ACL Rolling Review May 2026 deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, I found information about the ACL Rolling Review (ARR) in May 2026. However, the specific May 2026 deadline details weren't explicitly shown in the search results displayed. Let me provide what I found:

The ACL Peer Review Committee recommended switching from 8-week review cycles to 10-week cycles, with the new schedule starting in May 2025. The submission deadline is always the 15th of the month, which would mean the May 2026 ARR cycle submission deadline would be **May 15, 2026**.

The search results show the general ARR cycle structure, but the complete detailed timeline table for May 2026 specifically wasn't fully captured in these results. For the most up-to-date and complete information about the May 2026 ARR cycle deadlines, you can visit the official ACL Rolling Review website at [aclrollingreview.org/dates](http://aclrollingreview.org/dates).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f660a00c-b51b-4867-954f-603bbc9f8b2a",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a075189d942fa438d",
  "type": "user",
  "uuid": "3efc1e32-f946-4c5c-acc7-edaa9f55f609",
  "sourceToolAssistantUUID": "f660a00c-b51b-4867-954f-603bbc9f8b2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T09:47:32.723Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016urhugn6tgxvSg1nx7u1AT`</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR May 25 commitment deadline site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3efc1e32-f946-4c5c-acc7-edaa9f55f609",
  "isSidechain": true,
  "agentId": "a075189d942fa438d",
  "requestId": "req_011Cb634CaqXKxWWNckggAYi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57d27949-05ed-4e1f-8a9f-e30f1bfd2af7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBuvknFu3HRhPKSstpShsc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 637,
      "cache_creation_input_tokens": 1547,
      "cache_read_input_tokens": 10243,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1547
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 637,
          "output_tokens": 82,
          "cache_read_input_tokens": 10243,
          "cache_creation_input_tokens": 1547,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1547,
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

_source line 12 · 2026-05-16T09:47:37.689Z_

<details><summary>↩ Tool result · `toolu_016urhugn6tgxvSg1nx7u1AT`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers ARR May 25 commitment deadline site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"}]

Based on the search results from the EMNLP 2026 website, here's what I found regarding the ARR May 25 commitment deadline:

The ARR 2026 May submission policy for EMNLP requires authors to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026 - ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

Papers must be submitted, at latest, by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.

The search results don't explicitly mention a May 25 commitment deadline. For specific details about the May 25 deadline you mentioned, you may want to check the ARR website directly or contact the EMNLP 2026 organizers at the email provided in the results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57d27949-05ed-4e1f-8a9f-e30f1bfd2af7",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a075189d942fa438d",
  "type": "user",
  "uuid": "56551b82-739f-4dae-94ee-2765bd0baed0",
  "sourceToolAssistantUUID": "57d27949-05ed-4e1f-8a9f-e30f1bfd2af7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-16T09:47:48.989Z_

Here is what I found from the web searches:

## ARR Submission Deadline for EMNLP 2026

There is indeed an **ARR submission deadline of May 25, 2026** for papers targeting EMNLP 2026. This was confirmed by the official EMNLP 2026 Twitter/X account, which announced:

> "ARR Submission Deadline: May 25, 2026"

This means that May 25, 2026 is the last ARR cycle in which you can submit a paper and still have it reviewed in time to commit to EMNLP 2026. Papers submitted to ARR in the May 2026 cycle (or earlier cycles) that receive reviews and a meta-review can then be committed to EMNLP 2026.

**Important note:** According to the EMNLP 2026 submission policy, authors submitting to the ARR May 2026 cycle must explicitly declare that they intend to commit to EMNLP 2026 at submission time, and this choice is binding.

## EMNLP 2026 Commitment Deadline

The **EMNLP 2026 commitment deadline is August 2, 2026**. This is the date by which authors with reviewed ARR papers must commit them to EMNLP 2026 via the commitment link.

## Summary of Key Dates

| Milestone | Date |
|-----------|------|
| ARR Submission Deadline (last cycle for EMNLP 2026) | May 25, 2026 |
| EMNLP 2026 Commitment Deadline | August 2, 2026 |

Sources:
- [Call for Main Conference Papers - EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 on X (ARR Submission Deadline announcement)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)
- [AI Conference Deadlines - EMNLP 2026](https://mlciv.com/ai-deadlines/conference/?id=emnlp26)
- [EMNLP 2026 Conference Deadline Tracker](https://www.getpaperpilot.com/deadlines/emnlp-2026.html)
- [Hugging Face AI Deadlines - EMNLP 2026 update](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56551b82-739f-4dae-94ee-2765bd0baed0",
  "isSidechain": true,
  "agentId": "a075189d942fa438d",
  "requestId": "req_011Cb634mSH35huftn4reEac",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46141c0b-0d3c-4dca-b916-6c3bf90eb945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013aNFUJ19p8wonmebibHLqJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1453,
      "cache_read_input_tokens": 11790,
      "output_tokens": 661,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1453
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 661,
          "cache_read_input_tokens": 11790,
          "cache_creation_input_tokens": 1453,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1453,
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
