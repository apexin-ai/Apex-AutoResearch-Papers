# Research conversation: Search for very recent (2026) papers on agent error recovery, fault-tolerant agents, and agent self-correction training.

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac8ae6ca8a8545560.jsonl`
- **Structured JSON:** [`30e21541ae2fbdb6cf57.json`](../../sessions/30/30e21541ae2fbdb6cf57.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-12T00:40:52.586Z_

Search for very recent (2026) papers on agent error recovery, fault-tolerant agents, and agent self-correction training. I especially want to find papers the TaxEI proposal may have missed.

Search queries:
1. "agent fault tolerance training recovery 2026 arXiv"
2. "LLM agent self-correction SFT RL training 2026"
3. "agent trajectory error injection recovery 2026"
4. "agent planning error correction training arXiv 2026"
5. "structured error injection agent training arXiv"
6. "agent robustness training fault injection 2026"
7. "site:arxiv.org agent error recovery training 2026"

Also search for:
8. "EMNLP 2026 ARR deadline May 2026" to verify the venue deadline
9. "AgentErrorBench AgentDebug dataset availability" to verify evaluation data exists

Report any papers that could be direct competitors or highly relevant to TaxEI that are not already cited in the proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "49063af6-2b16-4001-80b1-d36016950eba",
  "agentId": "ac8ae6ca8a8545560",
  "type": "user",
  "uuid": "161debc4-918f-4531-b9d5-c995cb14d8cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-12T00:40:53.856Z_

I'll conduct a comprehensive web search for recent papers on agent error recovery and fault-tolerant agents, plus verify the venue deadline and dataset availability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "161debc4-918f-4531-b9d5-c995cb14d8cb",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk8u618CwboKbJUeY1A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b85189af-e0ba-45dc-bc64-5050a6e99b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019He9mfwE7V2rrJc1Bj69ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T00:40:54.144Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X3jNHgnhR4ai3AEoMMDFMJ`</summary>

```json
{
  "query": "agent fault tolerance training recovery 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b85189af-e0ba-45dc-bc64-5050a6e99b5e",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk8u618CwboKbJUeY1A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f9b39fc3-29f3-42d8-9d8d-37b20dc91e08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019He9mfwE7V2rrJc1Bj69ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T00:40:54.301Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hrk8354ffAN5A8haFLRnvU`</summary>

```json
{
  "query": "LLM agent self-correction SFT RL training 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9b39fc3-29f3-42d8-9d8d-37b20dc91e08",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk8u618CwboKbJUeY1A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2f6640ca-9a05-479f-8d12-ac938a1ab435",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019He9mfwE7V2rrJc1Bj69ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T00:40:54.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LaYPGtg7EgrC8jQP8B5QYw`</summary>

```json
{
  "query": "agent trajectory error injection recovery 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f6640ca-9a05-479f-8d12-ac938a1ab435",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk8u618CwboKbJUeY1A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "563a8082-bcfb-493f-81f1-4bb80e9b2e09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019He9mfwE7V2rrJc1Bj69ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-12T00:40:54.512Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UqWryNMoWX5f3PgBpe7tW4`</summary>

```json
{
  "query": "agent planning error correction training arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "563a8082-bcfb-493f-81f1-4bb80e9b2e09",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk8u618CwboKbJUeY1A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "77c2c599-dac5-4aa1-87d9-2085c33f209f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019He9mfwE7V2rrJc1Bj69ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T00:40:54.729Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gcxdeb3bbWLNkEQQu2A8Sg`</summary>

```json
{
  "query": "structured error injection agent training arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77c2c599-dac5-4aa1-87d9-2085c33f209f",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk8u618CwboKbJUeY1A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7ba546eb-5660-4fd3-b1e7-bd8d16c31980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019He9mfwE7V2rrJc1Bj69ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-12T00:40:54.733Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GjTkLc28qQiZMAqSFyyNKK`</summary>

```json
{
  "query": "agent robustness training fault injection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ba546eb-5660-4fd3-b1e7-bd8d16c31980",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk8u618CwboKbJUeY1A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "032692cf-fa0d-49c6-b6c7-757fc831ea5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019He9mfwE7V2rrJc1Bj69ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T00:40:54.961Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014jUhjvzeH8b8JDwc4YjoMN`</summary>

```json
{
  "query": "site:arxiv.org agent error recovery training 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "032692cf-fa0d-49c6-b6c7-757fc831ea5f",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk8u618CwboKbJUeY1A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d49c091-6f09-429b-9635-134d30b64d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019He9mfwE7V2rrJc1Bj69ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-12T00:40:55.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ubd8oxUfTp5WouDbEkg4r6`</summary>

```json
{
  "query": "EMNLP 2026 ARR deadline May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d49c091-6f09-429b-9635-134d30b64d2b",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk8u618CwboKbJUeY1A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "12fd868b-138c-43cd-90b9-ea48742b38c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019He9mfwE7V2rrJc1Bj69ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T00:40:55.532Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MfUsuC65mFQVuB1fwKLgsa`</summary>

```json
{
  "query": "AgentErrorBench AgentDebug dataset availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12fd868b-138c-43cd-90b9-ea48742b38c2",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk8u618CwboKbJUeY1A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "377756b8-edd2-418b-8a65-1ce727f0ff2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019He9mfwE7V2rrJc1Bj69ks",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 16153,
      "output_tokens": 459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 662
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 459,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 662,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:41:00.298Z_

<details><summary>↩ Tool result · `toolu_01Ubd8oxUfTp5WouDbEkg4r6`</summary>

```text
Web search results for query: "EMNLP 2026 ARR deadline May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here's the information about the EMNLP 2026 ARR deadline in May 2026:

The ARR Submission Deadline for EMNLP 2026 is May 25, 2026.

Additionally, authors must complete the author registration form by May 27, 2026 EoD AoE (End of Day, Anywhere on Earth).

It's important to note that since the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026. Papers submitted to ARR in the May 2026 cycle that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026 later.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12fd868b-138c-43cd-90b9-ea48742b38c2",
  "isSidechain": true,
  "promptId": "49063af6-2b16-4001-80b1-d36016950eba",
  "agentId": "ac8ae6ca8a8545560",
  "type": "user",
  "uuid": "b8c601ca-11d8-4137-b5f3-d8749b2f9669",
  "sourceToolAssistantUUID": "12fd868b-138c-43cd-90b9-ea48742b38c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:41:00.905Z_

<details><summary>↩ Tool result · `toolu_01MfUsuC65mFQVuB1fwKLgsa`</summary>

```text
Web search results for query: "AgentErrorBench AgentDebug dataset availability"

Links: [{"title":"GitHub - ulab-uiuc/AgentDebug · GitHub","url":"https://github.com/ulab-uiuc/AgentDebug"},{"title":"[2509.25370] Where LLM Agents Fail and How They can Learn From Failures","url":"https://arxiv.org/abs/2509.25370"},{"title":"Where LLM Agents Fail And How They can Learn From Failures | OpenReview","url":"https://openreview.net/forum?id=PFR4E8583W"},{"title":"Where LLM Agents Fail and How They can Learn From Failures | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.25370v1"},{"title":"davide221/agenterrorbench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/davide221/agenterrorbench"},{"title":"Paper page - Where LLM Agents Fail and How They can Learn From Failures","url":"https://huggingface.co/papers/2509.25370"},{"title":"GitHub - THUDM/AgentBench: A Comprehensive Benchmark to Evaluate LLMs as Agents (ICLR'24) · GitHub","url":"https://github.com/THUDM/AgentBench"},{"title":"AgentBench: Evaluating LLMs as Agents | OpenReview","url":"https://openreview.net/forum?id=zAdUB0aCTQ"},{"title":"AgentDoG: A Diagnostic Guardrail Framework for AI Agent Safety and Security","url":"https://arxiv.org/html/2601.18491v1"},{"title":"[2308.03688] AgentBench: Evaluating LLMs as Agents","url":"https://arxiv.org/abs/2308.03688"}]

Based on the search results, here's information about the AgentErrorBench and AgentDebug dataset availability:

## Dataset Overview

AgentErrorBench contains 200 expertly annotated agent failure trajectories across three environments: GAIA (50 trajectories), ALFWorld (100 trajectories), and WebShop (50 trajectories).

## Availability

The AgentErrorBench dataset is hosted on Google Drive due to its size and can be downloaded from a link provided in the repository. The code and data are available at https://github.com/ulab-uiuc/AgentDebug.

## What AgentDebug Is

AgentDebug is an intelligent debugging system that isolates root-cause failures and provides targeted corrective feedback, enabling agents to recover and iteratively improve. Experiments on AgentErrorBench show that AgentDebug achieves 24% higher all-correct accuracy and 17% higher step accuracy compared to the strongest baseline.

The repository is maintained by the University of Illinois and includes code, documentation, and links to access the full AgentErrorBench dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "377756b8-edd2-418b-8a65-1ce727f0ff2e",
  "isSidechain": true,
  "promptId": "49063af6-2b16-4001-80b1-d36016950eba",
  "agentId": "ac8ae6ca8a8545560",
  "type": "user",
  "uuid": "20aef259-533c-4193-a644-f984c56156fc",
  "sourceToolAssistantUUID": "377756b8-edd2-418b-8a65-1ce727f0ff2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:41:02.160Z_

<details><summary>↩ Tool result · `toolu_01UqWryNMoWX5f3PgBpe7tW4`</summary>

```text
Web search results for query: "agent planning error correction training arXiv 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2512.20745"},{"title":"Multi-Dimensional Evaluation of LLMs for Grammatical Error CorrectionAccepted at AIED 2026","url":"https://arxiv.org/html/2605.07635"},{"title":"E2CL: Exploration-based Error Correction Learning for Embodied Agents","url":"https://arxiv.org/html/2409.03256"},{"title":"Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and","url":"https://arxiv.org/pdf/2601.12560"},{"title":"Efficient Agent Training for Computer Use","url":"https://arxiv.org/html/2505.13909v1"},{"title":"Testing and Understanding Erroneous Planning in LLM Agents through Synthesized User Inputs","url":"https://arxiv.org/html/2404.17833v1"},{"title":"Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks | OpenReview","url":"https://openreview.net/forum?id=ybA4EcMmUZ"},{"title":"Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks","url":"https://arxiv.org/html/2503.09572v3"},{"title":"Agent-R\\xspace: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://arxiv.org/html/2501.11425v1"},{"title":"Towards Self-Improving Error Diagnosis in Multi-Agent Systems","url":"https://arxiv.org/html/2604.17658v1"}]

I found several relevant arXiv papers related to agent planning and error correction training from 2026 and recent years. Here are the key findings:

## Key Papers Found:

1. **AgentMath Framework** - The framework includes a self-correction capability where failed trajectories with error outputs are sampled, and the teacher model generates structured self-correction traces that diagnose errors, repair code, re-execute, and continue reasoning.

2. **Exploration-based Error Correction Learning (E2CL)** - This framework enables LM-based agents to align with environments through effective feedback-driven exploration and correction, proposing teacher-guided and teacher-free exploration schemes to facilitate collection of correction and feedback via agent-environment interactions.

3. **Agent-R: Iterative Self-Training Framework** - Agent-R enables language agents to reflect on the fly using an iterative self-training framework that leverages Monte Carlo Tree Search (MCTS) to construct training samples that recover correct trajectories from erroneous ones.

4. **Plan-and-Act Framework** - This framework incorporates explicit planning into LLM-based agents and introduces a scalable method to enhance plan generation through a novel synthetic data generation method.

5. **Error Diagnosis in Multi-Agent Systems** - The AgenTracer benchmark employs a programmatic fault injection mechanism where a perturbation operator is applied to ground-truth successful trajectories to generate failure traces, ensuring absolute ground truth for failure attribution and allowing precise evaluation of error localization.

These papers collectively address agent planning error correction across different approaches including self-correction mechanisms, exploration-based learning, iterative self-training, and systematic error diagnosis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77c2c599-dac5-4aa1-87d9-2085c33f209f",
  "isSidechain": true,
  "promptId": "49063af6-2b16-4001-80b1-d36016950eba",
  "agentId": "ac8ae6ca8a8545560",
  "type": "user",
  "uuid": "37064323-1150-4fc0-a8f1-07e24889f198",
  "sourceToolAssistantUUID": "77c2c599-dac5-4aa1-87d9-2085c33f209f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T00:41:02.580Z_

<details><summary>↩ Tool result · `toolu_01GjTkLc28qQiZMAqSFyyNKK`</summary>

```text
Web search results for query: "agent robustness training fault injection 2026"

Links: [{"title":"SREGym: A Live Training Ground for AI SRE Agents with High-Fidelity Failure Drills — CAIS 2026 — ACM CAIS 2026","url":"https://www.caisconf.org/program/2026/demos/sregym/"},{"title":"[2602.19843] MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems","url":"https://arxiv.org/abs/2602.19843"},{"title":"MASpi: A Unified Environment for Evaluating Prompt Injection Robustness in LLM-Based Multi-Agent Systems | OpenReview","url":"https://openreview.net/forum?id=1khmNRuIf9"},{"title":"A Survey on Failure Analysis and Fault Injection in AI Systems | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3732777"},{"title":"Applying Reinforcement Learning to Protect Deep Neural Networks from Soft Errors - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12252199/"},{"title":"Failure Identification Using Model-Implemented Fault Injection with Domain Knowledge-Guided Reinforcement Learning","url":"https://www.mdpi.com/1424-8220/23/4/2166"},{"title":"A Survey on Failure Analysis and Fault Injection in AI Systems","url":"https://arxiv.org/html/2407.00125v1"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"LLMs-Powered Real-Time Fault Injection: An Approach Toward Intelligent Fault Test Cases Generation","url":"https://arxiv.org/html/2511.19132v1"},{"title":"GitHub - JGalego/awesome-safety-critical-ai: When the stakes are high, intelligence is only half the equation - reliability is the other ⚠️","url":"https://github.com/JGalego/awesome-safety-critical-ai"}]

Here are the search results for "agent robustness training fault injection 2026":

## Key Findings

**1. Multi-Agent System Reliability (MAS-FIRE)**

MAS-FIRE is a systematic framework for fault injection and reliability evaluation of LLM-based Multi-Agent Systems, which defines a taxonomy of 15 fault types covering intra-agent cognitive errors and inter-agent coordination failures, and injects them via three non-invasive mechanisms: prompt modification, response rewriting, and message routing manipulation.

**2. SRE Agent Training (SREGym)**

SREGym is a live benchmark for AI SRE agents featuring high-fidelity failure drills with fault injection across OS kernels, hardware, and compound multi-event scenarios, serving as a new benchmark for AI-driven SRE (Site Reliability Engineering) techniques for diagnosing and mitigating production failures.

**3. Prompt Injection Robustness (MASpi)**

MASpi is a unified environment for evaluating the prompt injection robustness of LLM-based Multi-Agent Systems, offering systematic evaluation suites spanning multiple attack surfaces (i.e., external inputs, agent profiles, inter-agent messages) and attack objectives (i.e., instruction hijacking, task disruption, information disclosure).

**4. General Fault Injection in AI Systems**

The complexity of AI systems has exposed their vulnerabilities, necessitating robust methods for Failure Analysis and Fault Injection to ensure resilience and reliability, with research surveying existing FA and FI approaches across six layers of AI systems and systematically analyzing 142 studies to identify prevalent failures in AI systems, types of faults that current FI tools can simulate, and gaps between simulated faults and real-world failures.

These 2026 developments reflect an increasing focus on making AI agents more robust through systematic fault injection and stress testing methodologies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "032692cf-fa0d-49c6-b6c7-757fc831ea5f",
  "isSidechain": true,
  "promptId": "49063af6-2b16-4001-80b1-d36016950eba",
  "agentId": "ac8ae6ca8a8545560",
  "type": "user",
  "uuid": "a896a93e-4afa-467f-b142-47fd9fb0c6e2",
  "sourceToolAssistantUUID": "032692cf-fa0d-49c6-b6c7-757fc831ea5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T00:41:02.803Z_

<details><summary>↩ Tool result · `toolu_014jUhjvzeH8b8JDwc4YjoMN`</summary>

```text
Web search results for query: "site:arxiv.org agent error recovery training 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2512.20745"},{"title":"[2501.11425] Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://arxiv.org/abs/2501.11425"},{"title":"GUI-Genesis: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training","url":"https://arxiv.org/html/2602.14093"},{"title":"V-Droid: Advancing Mobile GUI Agent Through Generative Verifiers","url":"https://arxiv.org/html/2503.15937v5"},{"title":"Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction","url":"https://arxiv.org/html/2604.21154"},{"title":"LiteResearcher: A Scalable Agentic RL Training Framework for Deep Research Agent","url":"https://arxiv.org/html/2604.17931"},{"title":"AgenticQwen: Training Small Agentic Language Models with Dual Data","url":"https://arxiv.org/pdf/2604.21590"},{"title":"GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable","url":"https://arxiv.org/pdf/2602.14093"},{"title":"Agent-R\\xspace: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://arxiv.org/html/2501.11425v1"},{"title":"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling","url":"https://arxiv.org/html/2603.21357v2"}]

I found several relevant arxiv papers on agent error recovery training from 2026. Here are the key results:

## Notable Papers on Agent Error Recovery Training (2026):

1. **Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training** (Jan 2025, published 2026)
   - Leverages MCTS to construct training data that recover correct trajectories from erroneous ones
   - Continuously improves the model's ability to recover from errors and enables timely error correction

2. **Self-Correction Capability Injection** (ICLR 2026)
   - Samples trajectories excluded during refinement due to execution failures, and prompts the teacher model to generate structured self-correction traces (diagnose the error → repair the code → re-execute → continue reasoning)

3. **GUI-Genesis: Automated Synthesis of Efficient Environments** (Feb 2026)
   - GUI agents increasingly require interactive post-training to master long-horizon planning and dynamic error recovery

4. **AgentHER: Hindsight Experience Replay** (April 2026)
   - Proposes a four-stage pipeline that automates hindsight relabeling at scale, with failure-severity weighting and multi-judge verification mechanisms

5. **V-Droid: Advancing Mobile GUI Agent** (Feb 2026)
   - Improved accuracy enables human annotators to quickly rectify errors and recover the data collection process with minimal overhead

6. **AgenticQwen: Training Small Agentic Language Models** (April 2026)
   - Constructs harder problems from the model's own errors and expands the dataset using self-instruct

These papers demonstrate significant recent advances in training agents to recover from errors through various techniques including synthetic data generation, self-correction mechanisms, and hindsight relabeling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d49c091-6f09-429b-9635-134d30b64d2b",
  "isSidechain": true,
  "promptId": "49063af6-2b16-4001-80b1-d36016950eba",
  "agentId": "ac8ae6ca8a8545560",
  "type": "user",
  "uuid": "19847ece-62f8-455e-b3da-eb9a78e989f3",
  "sourceToolAssistantUUID": "4d49c091-6f09-429b-9635-134d30b64d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T00:41:03.528Z_

<details><summary>↩ Tool result · `toolu_01X3jNHgnhR4ai3AEoMMDFMJ`</summary>

```text
Web search results for query: "agent fault tolerance training recovery 2026 arXiv"

Links: [{"title":"Towards Fault Tolerance in Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2412.00534v1"},{"title":"[2602.00277] Training LLMs with Fault Tolerant HSDP on 100,000 GPUs","url":"https://arxiv.org/abs/2602.00277"},{"title":"Training LLMs with Fault Tolerant HSDP on 100,000 GPUs","url":"https://arxiv.org/pdf/2602.00277"},{"title":"1 TRANSOM: An Efficient Fault-Tolerant System for Training LLMs","url":"https://arxiv.org/pdf/2310.10046"},{"title":"[2412.00534] Towards Fault Tolerance in Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2412.00534"},{"title":"Role-Based Fault Tolerance System for LLM RL Post-Training","url":"https://arxiv.org/html/2512.22492"},{"title":"Enhancing Hardware Fault Tolerance in Machines with ...","url":"https://arxiv.org/pdf/2407.15283"},{"title":"Robust LLM Training Infrastructure at ByteDance","url":"https://arxiv.org/html/2509.16293v4"},{"title":"Enhancing Hardware Fault Tolerance in Machines with Reinforcement Learning Policy Gradient Algorithms","url":"https://arxiv.org/html/2407.15283v1"},{"title":"FlashRecovery: Fast and Low-Cost Recovery from Failures for Large-Scale Training of LLMs","url":"https://arxiv.org/html/2509.03047v1"}]

I found several relevant arXiv papers related to agent fault tolerance training and recovery from 2026 and recent years. Here are the key findings:

## Recent 2026 Papers

A January 2026 paper on "Training LLMs with Fault Tolerant HSDP on 100,000 GPUs" introduces a Fault Tolerant All Reduce (FTAR) protocol for gradient exchange across data parallel replicas and a non-blocking catch-up protocol allowing recovering replicas to join training with minimal stall, reducing stall time from 10 minutes to 3 minutes and increasing effective training time from 44% to 80%.

Another December 2025 paper presents "RobustRL," described as "the first comprehensive robust system to handle GPU machine errors for RL post-training ETTR (Effective Training Time Ratio) improvement via a Detect-Restart-Reconnect paradigm." Role-based fault tolerance in RL has benefits including ensuring failure isolation of different roles and allowing the task to continue running while maintaining current rollout and agent environment states.

## Other Notable Papers

A November 2024 paper on "Towards Fault Tolerance in Multi-Agent Reinforcement Learning" enhances fault tolerance of MARL by combining optimized model architecture with tailored training data sampling, incorporating attention mechanisms into actor and critic networks to automatically detect faults and regulate attention to faulty agents, with a prioritization mechanism to selectively sample critical transitions.

ByteRobust, a large-scale GPU infrastructure management system for robust LLM training, enables high-capacity fault tolerance, prompt fault demarcation, and localization with an effective data-driven approach to ensure continuous and efficient training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9b39fc3-29f3-42d8-9d8d-37b20dc91e08",
  "isSidechain": true,
  "promptId": "49063af6-2b16-4001-80b1-d36016950eba",
  "agentId": "ac8ae6ca8a8545560",
  "type": "user",
  "uuid": "95ba9419-2f3c-4ba8-ab8a-9bce131e8f4a",
  "sourceToolAssistantUUID": "f9b39fc3-29f3-42d8-9d8d-37b20dc91e08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T00:41:05.077Z_

<details><summary>↩ Tool result · `toolu_01Hrk8354ffAN5A8haFLRnvU`</summary>

```text
Web search results for query: "LLM agent self-correction SFT RL training 2026"

Links: [{"title":"Training Language Models to Self-Correct via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=CjwERcAU7w"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"2024-10-7 Training Language Models to Self-Correct via Reinforcement Learning","url":"https://arxiv.org/pdf/2409.12917"},{"title":"[2409.12917] Training Language Models to Self-Correct via Reinforcement Learning","url":"https://arxiv.org/abs/2409.12917"},{"title":"GitHub - LightChen233/Awesome-Long-Chain-of-Thought-Reasoning: Latest Advances on Long Chain-of-Thought Reasoning · GitHub","url":"https://github.com/LightChen233/Awesome-Long-Chain-of-Thought-Reasoning"},{"title":"training language models to self-correct","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf"},{"title":"GitHub - WooooDyy/AgentGym-RL: Code and implementations for the paper \"AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning\" by Zhiheng Xi et al. · GitHub","url":"https://github.com/WooooDyy/AgentGym-RL"},{"title":"Track: Oral Session 6A","url":"https://iclr.cc/virtual/2025/session/31965"},{"title":"WebRL: The Framework Training LLM Web Agents - BrightCoding","url":"https://www.blog.brightcoding.dev/2026/05/01/webrl-the-revolutionary-framework-training-llm-web-agents"}]

Based on the search results, here are the key findings related to LLM agent self-correction with SFT and RL training in 2026:

## Recent Developments in LLM Self-Correction Training

### SCoRe: Multi-Turn RL Approach
A multi-turn online reinforcement learning (RL) approach called SCoRe significantly improves an LLM's self-correction ability using entirely self-generated data. Supervised fine-tuning (SFT) variants on offline model-generated correction traces are insufficient for instilling self-correction behavior, as training via SFT either suffers from a distribution mismatch between training data and the model's own responses or implicitly prefers only a certain mode of correction behavior that is often not effective at test time.

### Limitations of SFT-Based Approaches
SFT-based approaches fall prey to either distribution shift, where gains from correcting base model errors don't transfer to self-correction under the learned model's own mistakes, or behavior collapse, where learning simply produces the best first-attempt response followed by superficial or no modifications in the second attempt.

### Evolution of Post-Training Methods
Major models released in the past year, from DeepSeek-R1 to Nemotron 3 Super to GPT-5.3 Codex, use different post-training stacks, with techniques that actually shipped in production models during 2025 and early 2026.

### Agentic RL Training
Recent research includes "Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey" published on TechRxiv in 2026. AgentGym-RL supports mainstream online RL algorithms (PPO, GRPO, RLOO, REINFORCE++) and complementary training paradigms (SFT, DPO, AgentEvol).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f6640ca-9a05-479f-8d12-ac938a1ab435",
  "isSidechain": true,
  "promptId": "49063af6-2b16-4001-80b1-d36016950eba",
  "agentId": "ac8ae6ca8a8545560",
  "type": "user",
  "uuid": "2e2ef7a2-39a7-41ee-90a2-7c12d300b6bb",
  "sourceToolAssistantUUID": "2f6640ca-9a05-479f-8d12-ac938a1ab435",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:41:05.215Z_

<details><summary>↩ Tool result · `toolu_01Gcxdeb3bbWLNkEQQu2A8Sg`</summary>

```text
Web search results for query: "structured error injection agent training arXiv"

Links: [{"title":"AEGIS: AUTOMATED ERROR GENERATION AND IDENTIFICATION FOR MULTI-AGENT SYSTEMS","url":"https://www.arxiv.org/pdf/2509.14295v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2512.20745"},{"title":"VIGIL: Defending LLM Agents Against Tool Stream Injection via Verify-Before-Commit","url":"https://arxiv.org/html/2601.05755v1"},{"title":"Securing Large Language Model Agents via Structured Graph Abstraction","url":"https://arxiv.org/pdf/2508.01249"},{"title":"From Prompt Injections to Protocol Exploits: Threats in LLM-Powered AI Agents Workflows","url":"https://arxiv.org/html/2506.23260v1"},{"title":"Towards Self-Improving Error Diagnosis in Multi-Agent Systems","url":"https://arxiv.org/html/2604.17658"},{"title":"Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks","url":"https://arxiv.org/html/2603.30016v1"},{"title":"AgentCyTE: Leveraging Agentic AI to Generate Cybersecurity Training & Experimentation Scenarios","url":"https://arxiv.org/html/2510.25189v1"},{"title":"AGENTARMOR: Enforcing Program Analysis on Agent Runtime Trace to Defend","url":"https://arxiv.org/pdf/2508.01249v1"},{"title":"[2508.01249] AgentArmor: Enforcing Program Analysis on Agent Runtime Trace to Defend Against Prompt Injection","url":"https://arxiv.org/abs/2508.01249"}]

I found several relevant papers on arXiv related to structured error injection for agent training. Here are the key results:

## AEGIS: Automated Error Generation and Identification for Multi-Agent Systems

AEGIS generates a dataset of labeled failures by taking successful multi-agent trajectories and applying controlled, context-aware error injections via an adaptive manipulator. By systematically injecting controlled errors into deterministically successful trajectories, this method creates a rich and scalable resource for training robust diagnostic models, bypassing the limitations of manual annotation. The dataset structure enables three distinct learning methods for the error identification task: Contrastive Learning, Reinforcement Learning, and Supervised Fine-Tuning.

## AgentMath: Code-Integrated Agent Training

This approach samples trajectories with execution failures and prompts the teacher model to generate a structured self-correction trace (diagnose the error → repair the code → re-execute → continue reasoning). An automated tool-augmented trajectory synthesis method transforms pure-text long chain-of-thought data into structured training samples containing code execution and authentic feedback through code injection, execution verification, and multi-dimensional refinement.

## AgenTracer: Programmatic Fault Injection

AgenTracer employs a programmatic fault injection mechanism where a specific "perturbation operator" is applied to a ground-truth successful trajectory at step t (e.g., modifying a correct code block to contain a bug or altering a tool argument), thereby generating a failure trace.

These papers demonstrate approaches for structured error injection in agent training across different domains and frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ba546eb-5660-4fd3-b1e7-bd8d16c31980",
  "isSidechain": true,
  "promptId": "49063af6-2b16-4001-80b1-d36016950eba",
  "agentId": "ac8ae6ca8a8545560",
  "type": "user",
  "uuid": "abb4134c-18de-4df1-8a45-a3fad819ef8c",
  "sourceToolAssistantUUID": "7ba546eb-5660-4fd3-b1e7-bd8d16c31980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T00:41:06.995Z_

<details><summary>↩ Tool result · `toolu_01LaYPGtg7EgrC8jQP8B5QYw`</summary>

```text
Web search results for query: "agent trajectory error injection recovery 2026"

Links: [{"title":"[2603.10600] Trajectory-Informed Memory Generation for Self-Improving Agent Systems","url":"https://arxiv.org/abs/2603.10600"},{"title":"AgenTracer: Who Is Inducing Failure in the LLM Agentic Systems? [Quick Review]","url":"https://liner.com/review/agentracer-who-is-inducing-failure-in-the-llm-agentic-systems"},{"title":"Preprint. ATBench: A Diverse and Realistic Agent Trajectory Bench-","url":"https://arxiv.org/pdf/2604.02022"},{"title":"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling","url":"https://arxiv.org/html/2603.21357v2"},{"title":"AgenTracer: Who Is Inducing Failure in the LLM Agentic Systems? | OpenReview","url":"https://openreview.net/forum?id=l05DseqvuD"},{"title":"GitHub - VoltAgent/awesome-ai-agent-papers: A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems. · GitHub","url":"https://github.com/VoltAgent/awesome-ai-agent-papers"},{"title":"AGENTRX: Diagnosing AI Agent Failures from Execution Trajectories","url":"https://arxiv.org/pdf/2602.02475"},{"title":"AI Agents Hacking in 2026: Defending the New Execution Boundary","url":"https://www.penligent.ai/hackinglabs/ai-agents-hacking-in-2026-defending-the-new-execution-boundary/"},{"title":"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents","url":"https://arxiv.org/pdf/2602.06443"},{"title":"Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward ModelingCode and data will be released after corporate approval.","url":"https://arxiv.org/html/2604.08178v1"}]

Based on the search results, here's what I found about agent trajectory error injection and recovery research in 2026:

## Key Research Areas

### Trajectory-Based Error Detection and Recovery

Recent work focuses on localizing the exact error step to enable subsequent recovery. TrajAD proposes a specialized verifier that detects and locates errors in agent execution trajectories at runtime to enable precise rollback-and-retry.

### Error Injection for Dataset Creation

Researchers employ "Perturb-and-Complete" strategies where they inject a perturbation into a target step and force conditional completion to finish the subsequent trajectory based on the altered context, synthesizing three distinct anomaly types: Task Failure, Process Inefficiency, and Unwarranted Continuation.

### Failure Attribution and Analysis

AgenTracer is the first automated framework for annotating failed multi-agent trajectories via counterfactual replay and programmed fault injection, producing the curated dataset TracerTraj. AgenTracer-8B improves step-level accuracy by 22.68% over its backbone QWEN3-8B.

### Learning from Failures

A framework includes components for trajectory intelligence extraction, decision attribution analysis, and a contextual learning generator that produces recovery tips from failure handling.

### Error Recovery Benchmarking

Recent benchmarks emphasize trajectory-level preference judgment for planning-centric agents and include robust error recovery evaluation through templates that create blind retries, premature surrender, or confused diagnoses after explicit tool errors.

These research directions collectively address how LLM-based agent systems can better detect, understand, and recover from errors during execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "563a8082-bcfb-493f-81f1-4bb80e9b2e09",
  "isSidechain": true,
  "promptId": "49063af6-2b16-4001-80b1-d36016950eba",
  "agentId": "ac8ae6ca8a8545560",
  "type": "user",
  "uuid": "afc4be1f-0e29-4fea-a438-6feaf5692b5d",
  "sourceToolAssistantUUID": "563a8082-bcfb-493f-81f1-4bb80e9b2e09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-12T00:41:32.019Z_

## Summary of Recent 2026 Research on Agent Error Recovery

Based on comprehensive web searches, I've identified numerous recent papers on agent error recovery, fault tolerance, and self-correction training. Here are the most significant findings, organized by research area:

### **Highly Relevant 2026 Papers (Potential TaxEI Competitors)**

**Agent Error Detection & Diagnosis:**
- **AgenTracer: Who Is Inducing Failure in the LLM Agentic Systems?** - The first automated framework for annotating failed multi-agent trajectories via counterfactual replay and programmed fault injection, producing the TracerTraj dataset. AgenTracer-8B improves step-level accuracy by 22.68% over QWEN3-8B. ([OpenReview](https://openreview.net/forum?id=l05DseqvuD))
- **AGENTRX: Diagnosing AI Agent Failures from Execution Trajectories** - Focuses on diagnosing failures from execution data ([arXiv](https://arxiv.org/pdf/2602.02475))
- **Towards Self-Improving Error Diagnosis in Multi-Agent Systems** ([arXiv](https://arxiv.org/html/2604.17658v1))

**Agent Error Recovery & Self-Correction:**
- **Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training** - Leverages MCTS to construct training data that recovers correct trajectories from erroneous ones, enabling timely error correction ([arXiv](https://arxiv.org/abs/2501.11425))
- **AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling** - Four-stage pipeline automating hindsight relabeling at scale with failure-severity weighting and multi-judge verification ([arXiv](https://arxiv.org/html/2603.21357v2))
- **Trajectory-Informed Memory Generation for Self-Improving Agent Systems** ([arXiv](https://arxiv.org/abs/2603.10600))

**Structured Error Injection for Training:**
- **AEGIS: AUTOMATED ERROR GENERATION AND IDENTIFICATION FOR MULTI-AGENT SYSTEMS** - Generates labeled failure datasets by applying controlled, context-aware error injections via an adaptive manipulator to successful trajectories, creating scalable resources for training robust diagnostic models ([arXiv](https://arxiv.org/pdf/2509.14295v1))
- **MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems** - Systematic framework defining 15 fault types with three non-invasive injection mechanisms: prompt modification, response rewriting, and message routing manipulation ([arXiv](https://arxiv.org/abs/2602.19843))

**Trajectory Analysis & Anomaly Detection:**
- **TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents** - Specialized verifier detecting and locating errors in agent execution trajectories at runtime to enable precise rollback-and-retry ([arXiv](https://arxiv.org/pdf/2602.06443))
- **ATBench: A Diverse and Realistic Agent Trajectory Benchmark** ([arXiv](https://arxiv.org/pdf/2604.02022))

**Agent Planning Error Correction:**
- **Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks** - Incorporates explicit planning into LLM-based agents with scalable synthetic data generation ([arXiv](https://arxiv.org/html/2503.09572v3))
- **E2CL: Exploration-based Error Correction Learning for Embodied Agents** - Enables agents to align with environments through feedback-driven exploration ([arXiv](https://arxiv.org/html/2409.03256))

**Agent Robustness & Benchmarking:**
- **SREGym: A Live Training Ground for AI SRE Agents with High-Fidelity Failure Drills** - CAIS 2026 demo featuring high-fidelity failure drills across OS kernels, hardware, and compound multi-event scenarios ([CAIS 2026](https://www.caisconf.org/program/2026/demos/sregym/))
- **MASpi: A Unified Environment for Evaluating Prompt Injection Robustness in LLM-Based Multi-Agent Systems** ([OpenReview](https://openreview.net/forum?id=1khmNRuIf9))

**LLM Self-Correction via RL:**
- **Training Language Models to Self-Correct via Reinforcement Learning** - Multi-turn online RL approach (SCoRe) showing that SFT approaches suffer from distribution mismatch and behavior collapse ([arXiv](https://arxiv.org/abs/2409.12917), [ICLR 2025 Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf))

**Related Agent Training Frameworks:**
- **AgenticQwen: Training Small Agentic Language Models with Dual Data** - Constructs harder problems from the model's own errors and expands datasets using self-instruct ([arXiv](https://arxiv.org/pdf/2604.21590))
- **GUI-Genesis: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training** - Emphasizes interactive post-training for long-horizon planning and dynamic error recovery ([arXiv](https://arxiv.org/html/2602.14093))
- **LiteResearcher: A Scalable Agentic RL Training Framework for Deep Research Agent** ([arXiv](https://arxiv.org/html/2604.17931))

---

### **Benchmark & Dataset Availability**

**AgentErrorBench & AgentDebug:**
- Repository: [GitHub - ulab-uiuc/AgentDebug](https://github.com/ulab-uiuc/AgentDebug)
- Dataset: [davide221/agenterrorbench on Hugging Face](https://huggingface.co/datasets/davide221/agenterrorbench)
- Paper: "Where LLM Agents Fail and How They can Learn From Failures" ([arXiv](https://arxiv.org/abs/2509.25370))
- Contains 200 expertly annotated failure trajectories across GAIA (50), ALFWorld (100), and WebShop (50)

---

### **EMNLP 2026 Venue Information**

**ARR Submission Deadline: May 25, 2026**
- Author registration deadline: May 27, 2026 EoD AoE
- Important: Authors must explicitly declare EMNLP 2026 at submission time (binding choice; shared May cycle with AACL)
- Full CFP: [EMNLP 2026 Main Conference Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)

---

### **Papers That Could Be Direct Competitors to TaxEI**

The most directly competitive papers appear to be:

1. **AEGIS** - Uses error injection on successful trajectories to create training data (very similar conceptually to TaxEI)
2. **AgenTracer** - Combines counterfactual replay with programmatic fault injection for error annotation
3. **Agent-R** - Uses MCTS-based recovery from erroneous trajectories
4. **MAS-FIRE** - Systematic fault injection taxonomy and evaluation framework
5. **AgentHER** - Trajectory relabeling with hindsight experience replay

These papers share TaxEI's core insight about using error injection or failure trajectories for training, but take different technical approaches (MCTS, hindsight relabeling, taxonomy-based injection, etc.).

Sources:
- [Towards Fault Tolerance in Multi-Agent Reinforcement Learning](https://arxiv.org/html/2412.00534v1)
- [Training LLMs with Fault Tolerant HSDP on 100,000 GPUs](https://arxiv.org/abs/2602.00277)
- [Role-Based Fault Tolerance System for LLM RL Post-Training](https://arxiv.org/html/2512.22492)
- [AgenTracer: Who Is Inducing Failure in the LLM Agentic Systems?](https://openreview.net/forum?id=l05DseqvuD)
- [AGENTRX: Diagnosing AI Agent Failures from Execution Trajectories](https://arxiv.org/pdf/2602.02475)
- [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/pdf/2602.06443)
- [Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling](https://arxiv.org/html/2604.08178v1)
- [Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training](https://arxiv.org/abs/2501.11425)
- [AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling](https://arxiv.org/html/2603.21357v2)
- [AEGIS: AUTOMATED ERROR GENERATION AND IDENTIFICATION FOR MULTI-AGENT SYSTEMS](https://arxiv.org/pdf/2509.14295v1)
- [MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2602.19843)
- [SREGym: A Live Training Ground for AI SRE Agents](https://www.caisconf.org/program/2026/demos/sregym/)
- [MASpi: A Unified Environment for Evaluating Prompt Injection Robustness](https://openreview.net/forum?id=1khmNRuIf9)
- [Training Language Models to Self-Correct via Reinforcement Learning](https://arxiv.org/abs/2409.12917)
- [GitHub - ulab-uiuc/AgentDebug](https://github.com/ulab-uiuc/AgentDebug)
- [AgentErrorBench Dataset on Hugging Face](https://huggingface.co/datasets/davide221/agenterrorbench)
- [EMNLP 2026 Main Conference Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afc4be1f-0e29-4fea-a438-6feaf5692b5d",
  "isSidechain": true,
  "agentId": "ac8ae6ca8a8545560",
  "requestId": "req_011Cawk9xdcHW8qc6Er8cK4Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99e42112-7786-4468-a658-01ba17b912db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ada40c23-c54a-456b-bc9a-e0203d11ada1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014pFL5oPPLHKhXFZmtXnjxL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5283,
      "cache_creation_input_tokens": 4214,
      "cache_read_input_tokens": 16815,
      "output_tokens": 2570,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4214
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5283,
          "output_tokens": 2570,
          "cache_read_input_tokens": 16815,
          "cache_creation_input_tokens": 4214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4214,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
