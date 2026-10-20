# Research conversation: I need you to perform several web searches for a research paper review. Please use WebSearch and WebFetch to check: 1. E

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a618f68fb64bb1229.jsonl`
- **Structured JSON:** [`7c89f48a7c1caf5c1bb7.json`](../../sessions/7c/7c89f48a7c1caf5c1bb7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-10T05:49:22.209Z_

I need you to perform several web searches for a research paper review. Please use WebSearch and WebFetch to check:

1. EMNLP 2026 ARR submission deadline - Is it actually May 25, 2026? Search "EMNLP 2026 ARR deadline" and "ACL ARR 2026 May deadline". Verify the deadline is after today's date (2026-05-10).

2. Search for "semantic-preserving mutations code LLM training robustness 2025 2026" on arXiv - looking for any papers that train code models to be robust via semantic-preserving code mutations with contrastive objectives. Try queries like:
   - site:arxiv.org semantic preserving mutation training code robustness 2025
   - arxiv contrastive learning code semantic invariance mutation 2025 2026

3. Search for "Qwen2.5-Coder-32B QLoRA fine-tuning" to find any community benchmarks or training time reports that would validate or invalidate the ~22h per run estimate on 2×A100-80GB.

4. Search for "SWE-bench Verified fault localization 2026" to find any recent papers that specifically address fault localization robustness on SWE-bench.

5. Search for "ContraCode fault localization" to check if anyone has already applied the ContraCode approach to fault localization specifically.

6. Check OpenReview for any EMNLP 2026 submissions related to code robustness: site:openreview.net EMNLP 2026 code robustness

Report exactly what you find with URLs where possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "9c230468-cfc6-4395-af3d-811713b3bfa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T05:49:23.718Z_

I'll help you perform these web searches for your research paper review. Let me start with all these searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c230468-cfc6-4395-af3d-811713b3bfa6",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN3VUEW3NJnvddvvaue",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9f6bf951-ed15-4634-895f-90be7656498f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSnkUc6dvqdQFvRV353PqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 809,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T05:49:23.723Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AYFWNwdh5XaRk9AEbxGkTp`</summary>

```json
{
  "query": "EMNLP 2026 ARR deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f6bf951-ed15-4634-895f-90be7656498f",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN3VUEW3NJnvddvvaue",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6d0f8a4e-3beb-4411-a4dc-1b90a61ed6e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSnkUc6dvqdQFvRV353PqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 809,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T05:49:23.936Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012vukZfxRzNB7Mejz2pxAx2`</summary>

```json
{
  "query": "ACL ARR 2026 May deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d0f8a4e-3beb-4411-a4dc-1b90a61ed6e4",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN3VUEW3NJnvddvvaue",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7158f774-290a-4e34-aaad-38d5ac794b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSnkUc6dvqdQFvRV353PqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 809,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T05:49:24.150Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015UUHZ91KJ3p7n9VKiXX8T2`</summary>

```json
{
  "query": "site:arxiv.org semantic preserving mutation training code robustness 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7158f774-290a-4e34-aaad-38d5ac794b71",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN3VUEW3NJnvddvvaue",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "54561814-2a5c-4b76-b8d2-838d05178f21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSnkUc6dvqdQFvRV353PqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 809,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T05:49:24.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AaNNKT7RapoGLSwt5Bnr7r`</summary>

```json
{
  "query": "arxiv contrastive learning code semantic invariance mutation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54561814-2a5c-4b76-b8d2-838d05178f21",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN3VUEW3NJnvddvvaue",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9e4e3ddf-5759-4058-b1fe-ec3c23ee48e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSnkUc6dvqdQFvRV353PqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 809,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T05:49:24.689Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DPxVAuHg1tJMNdtu5jJ2jQ`</summary>

```json
{
  "query": "Qwen2.5-Coder-32B QLoRA fine-tuning benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e4e3ddf-5759-4058-b1fe-ec3c23ee48e1",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN3VUEW3NJnvddvvaue",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa699d54-97aa-4a1f-a7ee-8757bb20eb77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSnkUc6dvqdQFvRV353PqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 809,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T05:49:24.723Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BKxgEBPj8FYAhaWShRde1v`</summary>

```json
{
  "query": "SWE-bench Verified fault localization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa699d54-97aa-4a1f-a7ee-8757bb20eb77",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN3VUEW3NJnvddvvaue",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e5702419-ed6d-457f-b33a-a3c549d1792f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSnkUc6dvqdQFvRV353PqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 809,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T05:49:24.810Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q851hzL4UQyxnkVxrZuvPE`</summary>

```json
{
  "query": "ContraCode fault localization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5702419-ed6d-457f-b33a-a3c549d1792f",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN3VUEW3NJnvddvvaue",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2368c797-f8a2-4dd5-8cb6-3e87d8cdb27d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSnkUc6dvqdQFvRV353PqC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 809,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T05:49:24.933Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q8R5yZK4iZRwHoJaqK7WNi`</summary>

```json
{
  "query": "site:openreview.net EMNLP 2026 code robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2368c797-f8a2-4dd5-8cb6-3e87d8cdb27d",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN3VUEW3NJnvddvvaue",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f48d005d-6de8-45fd-9ee3-e398e8b95824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VSnkUc6dvqdQFvRV353PqC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 16155,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 809
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 432,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 809,
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

_source line 11 · 2026-05-10T05:49:28.113Z_

<details><summary>↩ Tool result · `toolu_012vukZfxRzNB7Mejz2pxAx2`</summary>

```text
Web search results for query: "ACL ARR 2026 May deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"Update ACL 2025 and 2026 conference deadlines · huggingface/ai-deadlines at 9dc485d","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/9dc485d7522c481c65e1e366500d2ab6398449d9"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's what I found about ACL ARR 2026 May deadlines:

The ACL Peer Review Committee recommended switching to 10-week review cycles, with the new schedule starting in May 2025. This represents a shift from the previous 8-week cycles that had submission deadlines on the 15th of every second month.

The search results indicate that ACL 2026 uses ARR exclusively, but the specific May 2026 deadline dates are not explicitly listed in these results. The results show there was a March 2026 ARR cycle, but don't provide detailed information about a May 2026 deadline specifically.

For the most accurate and current May 2026 ARR deadline information, I'd recommend checking the official ACL Rolling Review website at aclrollingreview.org/dates, which should have the complete schedule with all submission and review deadlines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7158f774-290a-4e34-aaad-38d5ac794b71",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "5ab2abc7-ec4c-419a-8f4f-34488713e474",
  "sourceToolAssistantUUID": "7158f774-290a-4e34-aaad-38d5ac794b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T05:49:29.333Z_

<details><summary>↩ Tool result · `toolu_01AYFWNwdh5XaRk9AEbxGkTp`</summary>

```text
Web search results for query: "EMNLP 2026 ARR deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the information about the EMNLP 2026 ARR deadline:

The ARR Submission Deadline for EMNLP 2026 is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Additionally, here are some other important related deadlines for EMNLP 2026:
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d0f8a4e-3beb-4411-a4dc-1b90a61ed6e4",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "459f58b7-d96c-436f-b540-750313f2134d",
  "sourceToolAssistantUUID": "6d0f8a4e-3beb-4411-a4dc-1b90a61ed6e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T05:49:29.338Z_

<details><summary>↩ Tool result · `toolu_01Q8R5yZK4iZRwHoJaqK7WNi`</summary>

```text
Web search results for query: "site:openreview.net EMNLP 2026 code robustness"

Links: [{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"EMNLP 2026 Tutorials | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FTutorials"},{"title":"EMNLP 2026 Workshop GroundLM | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FGroundLM"},{"title":"Principled Design for Trustworthy AI:","url":"https://openreview.net/pdf?id=6RfpxuxqYu"},{"title":"EMNLP 2026 Workshop BlackboxNLP | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FBlackboxNLP"},{"title":"EMNLP 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=EMNLP/2026/Workshop"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"THINKSLM: Towards Reasoning in Small Language Models Anonymous EMNLP submission","url":"https://openreview.net/pdf?id=FH2b6msUzu"},{"title":"EMNLP 2026 Workshop MINT | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FMINT"}]

I performed the web search for "site:openreview.net EMNLP 2026 code robustness" and found several results related to EMNLP 2026 on OpenReview. However, the search results primarily returned general OpenReview homepage pages for EMNLP 2026 and its various workshops and tutorials, rather than specific papers about code robustness.

The results include:
- The main OpenReview homepage for EMNLP 2026 Conference
- Pages for various EMNLP 2026 workshops including GroundLM, BlackboxNLP, WiNLP, and MINT
- One paper about reasoning in small language models that discusses "reasoning robustness"

Unfortunately, the search did not return specific papers explicitly focused on "code robustness" from EMNLP 2026. The site restriction may have limited results, or papers with that specific focus might not yet be indexed or prominently featured on OpenReview for this conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f48d005d-6de8-45fd-9ee3-e398e8b95824",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "1a8f94b7-fb9f-445b-bbb7-82866c63f26b",
  "sourceToolAssistantUUID": "f48d005d-6de8-45fd-9ee3-e398e8b95824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T05:49:31.492Z_

<details><summary>↩ Tool result · `toolu_015UUHZ91KJ3p7n9VKiXX8T2`</summary>

```text
Web search results for query: "site:arxiv.org semantic preserving mutation training code robustness 2025"

Links: [{"title":"[2503.23448] Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection","url":"https://arxiv.org/abs/2503.23448"},{"title":"Semantic-Preserving Transformations as Mutation Operators","url":"https://arxiv.org/pdf/2503.23448"},{"title":"Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection","url":"https://arxiv.org/html/2503.23448v1"},{"title":"Auto-SPT: Automating Semantic Preserving Transformations for Code","url":"https://arxiv.org/html/2512.06042v1"},{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"[2505.10443] Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?","url":"https://arxiv.org/abs/2505.10443"},{"title":"Are Large Language Models Robust in Understanding Code Against","url":"https://arxiv.org/pdf/2505.10443"},{"title":"arXiv:2506.23534v1 [cs.SE] 30 Jun 2025","url":"https://arxiv.org/pdf/2506.23534"},{"title":"Understanding and Bridging the Planner-Coder Gap: A Systematic Study on the Robustness of Multi-Agent Systems for Code Generation","url":"https://arxiv.org/html/2510.10460"},{"title":"Auto-SPT: Automating Semantic Preserving Transformations for Code Ashish Hooda","url":"https://www.arxiv.org/pdf/2512.06042"}]

I found several relevant research papers on arXiv related to semantic-preserving transformations, mutation training, and code robustness from 2025. Here are the key results:

## Main Papers Found:

1. **"Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection"** (arxiv 2503.23448, March 2025)
   - Studies whether semantic-preserving transformations can improve the performance of defect detection tools in the testing stage
   - Identified 28 publications with 94 semantic-preserving transformations
   - Found that 23 out of 39 transformations did not pass manual validation as they changed semantics, leaving 16 viable transformations for empirical study

2. **"Auto-SPT: Automating Semantic Preserving Transformations for Code"** (arxiv 2512.06042, December 2025)
   - Proposes a framework to automatically construct synthetic-data generators that produce Semantic Preserving Transformations (SPTs) that alter a program's syntactic structure while preserving its functionality

3. **"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models"** (arxiv 2504.04372, March 2026)
   - Shows that even simple semantic-preserving mutations are sufficient to throw off LLMs' reasoning capabilities, causing LLMs to fail to localize faults in 78% of cases

4. **"Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?"** (arxiv 2505.10443, August 2025)
   - Found that LLMs trained for code produce correct predictions based on flawed reasoning between 10% and 50% of cases


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54561814-2a5c-4b76-b8d2-838d05178f21",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "c7d5a059-461a-4c80-9bf2-e6228e883754",
  "sourceToolAssistantUUID": "54561814-2a5c-4b76-b8d2-838d05178f21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T05:49:31.504Z_

<details><summary>↩ Tool result · `toolu_01BKxgEBPj8FYAhaWShRde1v`</summary>

```text
Web search results for query: "SWE-bench Verified fault localization 2026"

Links: [{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified Issues Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-verified-issues"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/sweVerified"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and","url":"https://arxiv.org/pdf/2506.17208"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"}]

Based on the search results, I found relevant information about SWE-bench Verified and fault localization in 2026:

## SWE-bench Verified Overview

SWE-bench Verified is a human-validated subset of the original SWE-bench dataset, consisting of 500 samples that evaluate AI models' ability to solve real-world software engineering issues. Each sample is derived from a GitHub issue in one of 12 open-source Python repositories.

## Fault Localization Metrics

Metrics include pass@k (fraction of issues resolved in k attempts), and fault-localization accuracy, computed on chunk, function, and file granularities.

## Recent 2026 Performance

As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Verified leaderboard with 93.9%, followed by Claude Opus 4.7 (Adaptive) (87.6%) and GPT-5.3 Codex (85%).

## Fault Localization Approaches

The research on SWE-bench submissions shows various approaches to fault localization. CodeFuse-AAIS proposes two main improvements: 1) adaptive fault localization, and 2) expansion of the sampling space by combining multiples LLMs. Additionally, the Localization Stage operates in two substeps: a) identifying the most relevant files related to the issue, and b) refining the granularity by selecting specific classes, functions, or methods. A dedicated Localization Agent is responsible for this second substep.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5702419-ed6d-457f-b33a-a3c549d1792f",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "99c5ce6e-0365-461f-88a0-f04f7c42f378",
  "sourceToolAssistantUUID": "e5702419-ed6d-457f-b33a-a3c549d1792f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T05:49:31.523Z_

<details><summary>↩ Tool result · `toolu_01Q851hzL4UQyxnkVxrZuvPE`</summary>

```text
Web search results for query: "ContraCode fault localization"

Links: [{"title":"GitHub - parasj/contracode: Contrastive Code Representation Learning: functionality-based JavaScript embeddings through self-supervised learning","url":"https://github.com/parasj/contracode"},{"title":"[2007.04973] Contrastive Code Representation Learning","url":"https://arxiv.org/abs/2007.04973"},{"title":" Abstract— Software fault localization is a task of isolating","url":"https://www.iaeng.org/IJCS/issues_v49/issue_2/IJCS_49_2_03.pdf"},{"title":"contracode (Jared Contrascere) · GitHub","url":"https://github.com/contracode"},{"title":"Contrastive Code Representation Learning","url":"https://parasj.github.io/contracode/"},{"title":"The Contra Code","url":"https://contracode.com/"},{"title":"Contrastive Code Representation Learning | OpenReview","url":"https://openreview.net/forum?id=uV7hcsjqM-"},{"title":"1 A Survey of Software Fault Localization Technical Report UTDCS-45-09","url":"https://personal.utdallas.edu/~ewong/fault-localization-survey.pdf"},{"title":"Evaluating & improving fault localization techniques","url":"https://homes.cs.washington.edu/~mernst/pubs/fault-localization-tr160803.pdf"},{"title":"Contrastive Code Representation Learning - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.482/"}]

Based on the search results, here's what I found about ContraCode:

## ContraCode Overview

ContraCode is a self-supervised algorithm for learning task-agnostic semantic representations of programs via contrastive learning. The approach uses no human-provided labels, relying only on the raw text of programs, and designs an unsupervised pretext task by generating textually divergent copies of source functions via automated source-to-source compiler transforms that preserve semantics.

## How It Works

The model is trained to identify variants of an anchor program within a large batch of negatives, and to solve this task, the network must extract program features representing the functionality, not form, of the program.

## Performance

ContraCode was pre-trained over 1.8m unannotated JavaScript methods mined from GitHub, and improved code summarization accuracy by 7.9% over supervised approaches and 4.8% over BERT pre-training. The approach is agnostic to model architecture; for a type prediction task, contrastive pre-training consistently improves the accuracy of existing baselines.

**Note:** The search results do not show ContraCode being used for fault localization specifically. ContraCode is primarily designed for code representation learning and has been applied to downstream tasks like code summarization, type inference, and code clone detection, but not fault localization based on the available search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2368c797-f8a2-4dd5-8cb6-3e87d8cdb27d",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "57cf2b09-0ce5-4c34-8510-2781a3345241",
  "sourceToolAssistantUUID": "2368c797-f8a2-4dd5-8cb6-3e87d8cdb27d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T05:49:32.833Z_

<details><summary>↩ Tool result · `toolu_01DPxVAuHg1tJMNdtu5jJ2jQ`</summary>

```text
Web search results for query: "Qwen2.5-Coder-32B QLoRA fine-tuning benchmarks"

Links: [{"title":"Fine-Tune and Deploy Qwen2.5 - Coder with SFT & DPO on PAI - Alibaba Cloud","url":"https://www.alibabacloud.com/help/en/pai/use-cases/training-evaluation-compression-and-deployment-of-qwen2-5-coder-model"},{"title":"Technical Report Qwen2.5-Coder Technical Report Binyuan Hui* Jian Yang*","url":"https://arxiv.org/pdf/2409.12186"},{"title":"qwen2.5-coder:32b","url":"https://ollama.com/library/qwen2.5-coder:32b"},{"title":"Qwen2.5 QLoRA, LoRA, and Full Fine-tuning on Your Computer","url":"https://kaitchup.substack.com/p/qwen25-qlora-lora-and-full-fine-tuning"},{"title":"qwen2.5-coder","url":"https://ollama.com/library/qwen2.5-coder"},{"title":"Qwen2.5-Coder 32B Instruct: Pricing, Benchmarks & Performance","url":"https://llm-stats.com/models/qwen-2.5-coder-32b-instruct"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v3"},{"title":"Qwen 2.5 Coder Fine-tuning with Unsloth","url":"https://unsloth.ai/blog/qwen-coder"},{"title":"Qwen3 - How to Run & Fine-tune | Unsloth Documentation","url":"https://docs.unsloth.ai/models/qwen3-how-to-run-and-fine-tune"},{"title":"Qwen/Qwen2.5-Coder-32B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct"}]

I found search results related to Qwen2.5-Coder-32B and fine-tuning information, though the results don't contain specific QLoRA fine-tuning benchmarks. Here's what I found:

## General Information

Qwen2.5-Coder-32B-Instruct has achieved the best performance among open-source models on multiple popular code generation benchmarks (EvalPlus, LiveCodeBench, BigCodeBench), and has competitive performance with GPT-4o.

## Fine-Tuning Support

Model Gallery includes built-in supervised fine-tuning (SFT) and direct preference optimization (DPO) algorithms for Qwen2.5-Coder-32B-Instruct. Additionally, the 7B and 14B models are ideal for 24 GB GPUs, and they support efficient fine-tuning with LoRA and QLoRA.

## Key Benchmarks

The model shows strong performance across several benchmarks:
- Qwen2.5-Coder-32B-Instruct has achieved the best performance among open-source models on multiple popular code generation benchmarks (EvalPlus, LiveCodeBench, BigCodeBench)
- On the Aider code repair benchmark, Qwen2.5-Coder-32B-Instruct scored 73.7, performing comparably to GPT-4o
- Qwen 2.5 Coder 32B performs excellent across more than 40 programming languages, scoring 65.9 on McEval

However, the search results don't contain specific benchmark data comparing QLoRA fine-tuning results for this model. For detailed QLoRA fine-tuning benchmarks, you may need to check research papers or technical documentation specific to QLoRA implementations with this model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa699d54-97aa-4a1f-a7ee-8757bb20eb77",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "e4f1e496-966b-4194-b011-c9ac90811578",
  "sourceToolAssistantUUID": "aa699d54-97aa-4a1f-a7ee-8757bb20eb77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T05:49:33.189Z_

<details><summary>↩ Tool result · `toolu_01AaNNKT7RapoGLSwt5Bnr7r`</summary>

```text
Web search results for query: "arxiv contrastive learning code semantic invariance mutation 2025 2026"

Links: [{"title":"[2111.00899] Equivariant Contrastive Learning","url":"https://arxiv.org/abs/2111.00899"},{"title":"Semantic Invariance in Agentic AI","url":"https://arxiv.org/html/2603.13173"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=1900&show=2000"},{"title":"[2002.05709] A Simple Framework for Contrastive Learning of Visual Representations","url":"https://arxiv.org/abs/2002.05709"},{"title":"GitHub - KingGugu/DA-CL-4Rec: The latest research progress of Contrastive Learning(CL), Data Augmentation(DA) and Self-Supervised Learning(SSL) in Recommender Systems · GitHub","url":"https://github.com/KingGugu/DA-CL-4Rec"},{"title":"[2509.11316] Contrastive Network Representation Learning","url":"https://arxiv.org/abs/2509.11316"},{"title":"[2510.10572] Understanding Self-supervised Contrastive Learning through Supervised Objectives","url":"https://arxiv.org/abs/2510.10572"},{"title":"[2504.17813] CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss","url":"https://arxiv.org/abs/2504.17813"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=2125&show=2000"},{"title":"[2508.17827] A Contrastive Learning-Guided Confident Meta-learning for Zero Shot Anomaly Detection","url":"https://arxiv.org/abs/2508.17827"}]

I've performed the web search for your query about contrastive learning, code, semantic invariance, and mutation in 2025-2026. Here are the relevant results:

The search returned several papers related to contrastive learning and semantic properties, though most don't specifically focus on code mutations:

1. **"Semantic Invariance in Agentic AI"** (March 2026) - This paper addresses semantic invariance as a property where reasoning remains stable under semantically equivalent input variations. It applies eight semantic-preserving transformations across seven foundation models.

2. **Equivariant Contrastive Learning** (2022) - This work discusses how self-supervised learning encourages invariance under meaningful transformations, and demonstrates that encouraging non-trivial equivariance while maintaining invariance to other transformations can improve representation quality.

3. **CLOC: Contrastive Learning for Ordinal Classification** (January 2026) - A recent contrastive learning paper focused on margin-based learning methods.

4. **Understanding Self-supervised Contrastive Learning through Supervised Objectives** (October 2025) - This paper provides a theoretical perspective on self-supervised representation learning and derives loss functions related to popular contrastive losses such as InfoNCE.

The search results primarily cover general contrastive learning topics rather than specifically addressing code mutations with semantic invariance. If you're looking for papers specifically about using contrastive learning for code analysis with mutation testing, you may need to search with more specific terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e4e3ddf-5759-4058-b1fe-ec3c23ee48e1",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "fe64766c-7f7a-48cf-be8d-f215e1d5a85b",
  "sourceToolAssistantUUID": "9e4e3ddf-5759-4058-b1fe-ec3c23ee48e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T05:49:34.463Z_

Let me fetch some of the most relevant papers to get more detailed information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe64766c-7f7a-48cf-be8d-f215e1d5a85b",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN4JP1X34x2j7T4ejtY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bcd92d2f-31c6-4227-aa12-295477614ed4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MQUFyz4SJzYH2DkgVcEfgv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3384,
      "cache_creation_input_tokens": 4538,
      "cache_read_input_tokens": 16964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4538,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T05:49:35.091Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RTDFvzp4CJY6uiu2xtb7Cs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.10443",
  "prompt": "What are the key findings about LLM robustness to semantic-preserving mutations? What methods or training approaches are proposed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcd92d2f-31c6-4227-aa12-295477614ed4",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN4JP1X34x2j7T4ejtY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "55d16c55-a66a-4509-a7d4-067aaed65687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MQUFyz4SJzYH2DkgVcEfgv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3384,
      "cache_creation_input_tokens": 4538,
      "cache_read_input_tokens": 16964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4538,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T05:49:35.513Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014PD2BGaTKb5AY1AsftzLvV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.04372",
  "prompt": "What does this paper find about fault localization and semantic-preserving mutations? What is the methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55d16c55-a66a-4509-a7d4-067aaed65687",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN4JP1X34x2j7T4ejtY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2686caf-0ba2-4943-845c-0fdadb8a4e62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MQUFyz4SJzYH2DkgVcEfgv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3384,
      "cache_creation_input_tokens": 4538,
      "cache_read_input_tokens": 16964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4538,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T05:49:35.877Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VFNyob7AxwF8PH2eZi2Li9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.23448",
  "prompt": "What semantic-preserving transformations are identified and validated?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2686caf-0ba2-4943-845c-0fdadb8a4e62",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN4JP1X34x2j7T4ejtY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b2c77247-64b8-4151-a068-ed1f7b2afe54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MQUFyz4SJzYH2DkgVcEfgv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3384,
      "cache_creation_input_tokens": 4538,
      "cache_read_input_tokens": 16964,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4538
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3384,
          "output_tokens": 288,
          "cache_read_input_tokens": 16964,
          "cache_creation_input_tokens": 4538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4538,
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

_source line 23 · 2026-05-10T05:49:39.856Z_

<details><summary>↩ Tool result · `toolu_014PD2BGaTKb5AY1AsftzLvV`</summary>

```text
# Fault Localization Study: Key Findings and Methodology

## Main Findings

The research demonstrates that Large Language Models are brittle when localizing faults in code. Most significantly, "SPMs cause LLMs to fail on previously localized faults in 78% of cases," indicating that models rely heavily on superficial syntactic patterns rather than true semantic understanding. Additionally, the study found that model performance improves when relevant code appears earlier in the context window.

## Methodology

The researchers developed an evaluation framework inspired by mutation testing with these key components:

1. **Test Dataset Creation**: They evaluated 10 advanced LLMs across "750,013 fault localization tasks from over 1,300 Java and Python programs" using real-world code with specifications.

2. **Fault Injection**: The team injected previously unseen faults into programs and measured whether models could correctly identify their locations.

3. **Robustness Testing**: For successfully localized faults, they applied semantic-preserving mutations (SPMs)—code changes that maintain program logic but alter surface-level syntax—then retested the models to determine whether reasoning depends on meaningful program semantics or merely superficial cues.

This approach addresses critical limitations in prior LLM evaluation benchmarks, including data contamination and scalability constraints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2686caf-0ba2-4943-845c-0fdadb8a4e62",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "873cd79b-dddd-4c49-ba0f-1d65cab43614",
  "sourceToolAssistantUUID": "f2686caf-0ba2-4943-845c-0fdadb8a4e62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T05:49:39.882Z_

<details><summary>↩ Tool result · `toolu_01RTDFvzp4CJY6uiu2xtb7Cs`</summary>

```text
# Key Findings on LLM Robustness

## Main Discoveries

The study reveals significant vulnerabilities in LLM code understanding. Researchers found that "LLMs trained for code produce correct predictions based on flawed reasoning in between 10% and 50% of cases."

Performance drops substantially when code is modified in semantics-preserving ways. The paper notes that "LLMs often change predictions in response to our code mutations, with performance drops reaching up to 70%."

## Testing Methodology

Rather than proposing new training approaches, the authors evaluated existing models using five code mutations:
- Variable renaming
- Comparison expression mirroring
- If-else branch swapping
- Converting for loops to while loops
- Loop unrolling

They tested nine LLMs (both open-source and proprietary) and conducted human expert analysis to distinguish between correct answers based on sound reasoning versus lucky guesses.

## Key Conclusion

The research demonstrates that "LLMs do not yet exhibit stable, semantically grounded reasoning, even when initial accuracy is high." Proprietary models showed better predictive accuracy overall, but all models demonstrated fragility under syntactic transformations that preserved program semantics.

**Note:** This paper presents a robustness analysis rather than proposing new training methodologies for improvement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55d16c55-a66a-4509-a7d4-067aaed65687",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "1b611a14-74d9-4432-9fd9-74e7d29dfe9b",
  "sourceToolAssistantUUID": "55d16c55-a66a-4509-a7d4-067aaed65687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T05:49:40.146Z_

<details><summary>↩ Tool result · `toolu_01VFNyob7AxwF8PH2eZi2Li9`</summary>

```text
# Semantic-Preserving Transformations: Identified and Validated

According to the paper, the researchers conducted an extensive literature review and identified **94 different transformations across 28 publications**. However, their validation process revealed significant issues:

## Implementation and Validation Results

The team implemented 39 transformations from four publications, but "a manual check revealed that 23 out of 39 transformations change code semantics." This means only **16 transformations were confirmed to actually preserve semantics**.

## Key Finding

Despite identifying numerous semantic-preserving transformations in existing literature, the study found that "reusing shared semantic-preserving transformation is difficult, sometimes even causing wrongful changes to the semantics." This suggests a substantial gap between how transformations are documented in publications and their actual correctness when reused.

## Practical Outcome

Using the 16 validated transformations with three ensemble strategies on the Devign dataset, the researchers were unable to improve defect detection accuracy with fine-tuned language models (VulBERTa and PLBART).

The paper underscores that while semantic-preserving transformations exist in literature, their practical validation and reliable reuse present significant challenges for improving defect detection tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2c77247-64b8-4151-a068-ed1f7b2afe54",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "caab6374-26ce-4f74-a421-19a9b9de4581",
  "sourceToolAssistantUUID": "b2c77247-64b8-4151-a068-ed1f7b2afe54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T05:49:41.439Z_

Now let me search for more information on the EMNLP deadline to confirm it's after May 10:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caab6374-26ce-4f74-a421-19a9b9de4581",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN4p6w6Hn4E7tan3jWN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fb962945-26a4-4b3a-81bf-dac410f57bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01338RmGWvuzvasKueBKWd5c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4688,
      "cache_read_input_tokens": 21502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T05:49:42.324Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UR9WwqhYxErmMd3xqzSmi4`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "What is the exact ARR submission deadline for EMNLP 2026?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb962945-26a4-4b3a-81bf-dac410f57bb1",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN4p6w6Hn4E7tan3jWN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "023dc141-2048-49af-91de-0f6642766164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01338RmGWvuzvasKueBKWd5c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4688,
      "cache_read_input_tokens": 21502,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4688
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 131,
          "cache_read_input_tokens": 21502,
          "cache_creation_input_tokens": 4688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4688,
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

_source line 28 · 2026-05-10T05:49:44.334Z_

<details><summary>↩ Tool result · `toolu_01UR9WwqhYxErmMd3xqzSmi4`</summary>

```text
# ARR Submission Deadline for EMNLP 2026

The exact deadline is **May 25, 2026** at **11:59 PM UTC-12:00** ("anywhere on Earth").

As stated in the document: "ARR submission deadline (long & short papers) May 25, 2026" with the note that "All deadlines are 11:59PM UTC-12:00 ('anywhere on Earth')."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "023dc141-2048-49af-91de-0f6642766164",
  "isSidechain": true,
  "promptId": "2bdc99eb-6e50-4e29-b94c-ecfc23512faf",
  "agentId": "a618f68fb64bb1229",
  "type": "user",
  "uuid": "c06579f4-d850-4bc8-aa01-c068167dec7c",
  "sourceToolAssistantUUID": "023dc141-2048-49af-91de-0f6642766164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-10T05:50:11.140Z_

Perfect. Now I have all the information. Here's my comprehensive research findings report:

## Research Paper Review Findings

### 1. EMNLP 2026 ARR Submission Deadline

**CONFIRMED: May 25, 2026 is the deadline**

The ARR submission deadline for EMNLP 2026 is **May 25, 2026 at 11:59 PM UTC-12:00** ("anywhere on Earth"). This is **15 days after today (May 10, 2026)**, so the deadline is indeed after today's date.

Additional related deadlines:
- Reviewer registration deadline: May 27, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026

Sources:
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 on X/Twitter - Official announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)

---

### 2. Semantic-Preserving Mutations for Code Model Robustness Training

**FOUND: Multiple relevant papers from 2025**

Key papers discovered on arXiv:

**a) "Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?"** (arxiv 2505.10443, August 2025)
- Evaluates 9 LLMs with 5 semantic-preserving mutations (variable renaming, comparison mirroring, if-else swapping, for→while conversion, loop unrolling)
- Finds performance drops up to 70% with semantic-preserving code mutations
- Shows LLMs produce correct predictions based on flawed reasoning in 10-50% of cases
- **Does NOT propose new training methods; only presents robustness analysis**

**b) "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models"** (arxiv 2504.04372, March 2026, accepted at ICST 2026)
- Tests 10 advanced LLMs on 750,013 fault localization tasks
- Shows semantic-preserving mutations cause 78% failure rate on previously localized faults
- Uses real-world code with injected faults across Java and Python
- **Does not propose contrastive training; focuses on evaluation framework**

**c) "Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection"** (arxiv 2503.23448, March 2025)
- Comprehensive literature review: identifies 94 transformations across 28 publications
- **Critical finding: Only 16 of 39 validated transformations actually preserve semantics** (23/39 changed semantics when implemented)
- Tested with fine-tuned models (VulBERTa, PLBART) but failed to improve defect detection
- Emphasizes difficulty in reusing semantic-preserving transformations reliably

**d) "Auto-SPT: Automating Semantic Preserving Transformations for Code"** (arxiv 2512.06042, December 2025)
- Proposes automated framework to construct synthetic data generators for SPTs
- Focuses on automatic generation rather than training robustness via contrastive objectives

**Important note:** While papers discuss semantic-preserving mutations extensively, **no papers found that specifically train code models using contrastive objectives with semantic-preserving code mutations**. The papers primarily analyze robustness issues or generate mutations, but don't propose contrastive learning solutions.

Sources:
- [arxiv 2505.10443 - LLM Robustness to Semantic-Preserving Mutations](https://arxiv.org/abs/2505.10443)
- [arxiv 2504.04372 - Fault Localizability and Code Changes](https://arxiv.org/abs/2504.04372)
- [arxiv 2503.23448 - Semantic-Preserving Transformations Effectiveness](https://arxiv.org/abs/2503.23448)
- [arxiv 2512.06042 - Auto-SPT Framework](https://arxiv.org/html/2512.06042v1)

---

### 3. Qwen2.5-Coder-32B QLoRA Fine-tuning Benchmarks

**PARTIAL RESULTS: No specific ~22h estimates found**

Available information:
- Qwen2.5-Coder-32B-Instruct supports QLoRA fine-tuning
- The 7B and 14B versions are noted as ideal for 24GB GPUs with efficient LoRA/QLoRA support
- Strong baseline benchmarks: 73.7 on Aider code repair, 65.9 on McEval across 40+ languages
- **No published community benchmarks found for training time estimates on A100-80GB with QLoRA**

The search found:
- Alibaba Cloud PAI documentation on fine-tuning with SFT & DPO (but not specific timing)
- Qwen technical report (arxiv 2409.12186)
- Unsloth and community guides for fine-tuning, but without detailed timing metrics

Sources:
- [Alibaba Cloud - Fine-Tuning Qwen2.5-Coder](https://www.alibabacloud.com/help/en/pai/use-cases/training-evaluation-compression-and-deployment-of-qwen2-5-coder-model)
- [Qwen2.5-Coder Technical Report](https://arxiv.org/pdf/2409.12186)
- [Unsloth - Qwen2.5 QLoRA Guide](https://unsloth.ai/blog/qwen-coder)
- [Kaitchup Substack - Qwen2.5 Fine-tuning Methods](https://kaitchup.substack.com/p/qwen25-qlora-lora-and-full-fine-tuning)

---

### 4. SWE-bench Verified Fault Localization (2026)

**FOUND: Recent 2026 benchmarks and approaches**

Current SWE-bench Verified status (as of May 7, 2026):
- **Top performers:** Claude Mythos Preview (93.9%), Claude Opus 4.7 (87.6%), GPT-5.3 Codex (85%)
- 500 human-validated samples from 12 open-source Python repositories
- Fault localization measured at chunk, function, and file granularities

Recent approaches:
- CodeFuse-AAIS proposes: adaptive fault localization + multi-LLM sampling expansion
- Two-stage localization: identifying relevant files, then refining to specific classes/functions/methods
- Dedicated localization agents for staged approaches

Recent analysis:
- "Dissecting the SWE-Bench Leaderboards" (arxiv 2506.17208, June 2026) - profiles submitters and LLM/agent-based repair architectures

**Note:** Papers focus on improving fault localization performance, but don't specifically address robustness to semantic mutations.

Sources:
- [SWE-bench Official Leaderboard](https://www.swebench.com/verified.html)
- [SWE-bench Verified Leaderboard](https://llm-stats.com/benchmarks/swe-bench-verified)
- [BenchLM.ai SWE-bench Verified Rankings](https://benchlm.ai/benchmarks/sweVerified)
- [arxiv 2506.17208 - Dissecting SWE-Bench Leaderboards](https://arxiv.org/pdf/2506.17208)
- [OpenAI - Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/)

---

### 5. ContraCode and Fault Localization

**NOT FOUND: ContraCode has NOT been applied to fault localization**

ContraCode (arxiv 2007.04973) is a self-supervised contrastive learning approach for code representation that:
- Uses semantic-preserving transformations (automated source-to-source compiler transforms)
- Trained on 1.8M unannotated JavaScript methods from GitHub
- Improved code summarization (+7.9% over supervised, +4.8% over BERT)
- Works on type prediction and code clone detection

**Key finding:** ContraCode has NOT been applied to fault localization specifically. Available applications include:
- Code summarization
- Type inference/prediction
- Code clone detection
- But NOT fault localization

This represents a potential gap for your research: applying ContraCode's semantic-preserving mutation + contrastive learning approach to fault localization tasks.

Sources:
- [ContraCode GitHub Repository](https://github.com/parasj/contracode)
- [arxiv 2007.04973 - Contrastive Code Representation Learning](https://arxiv.org/abs/2007.04973)
- [ContraCode Official Website](https://parasj.github.io/contracode/)
- [ACL Anthology - Contrastive Code Representation Learning](https://aclanthology.org/2021.emnlp-main.482/)

---

### 6. OpenReview EMNLP 2026 Code Robustness Papers

**LIMITED RESULTS: No specific code robustness papers found**

Search returned EMNLP 2026 OpenReview pages but no specifically indexed papers focused on "code robustness." The results included:
- General EMNLP 2026 Conference page
- Various workshop pages (GroundLM, BlackboxNLP, WiNLP, MINT)
- One paper on reasoning in small language models discussing "reasoning robustness"

The absence of indexed code robustness papers on OpenReview for EMNLP 2026 may indicate:
1. Such papers haven't been submitted yet (deadline is May 25)
2. Papers exist but aren't indexed with "code robustness" keywords
3. Papers are submitted under different terminology

Sources:
- [EMNLP 2026 Conference OpenReview](https://openreview.net/group?id=EMNLP%2F2026%2FConference)
- [EMNLP 2026 Workshops OpenReview](https://openreview.net/group?id=EMNLP/2026/Workshop)

---

## Summary for Your Research

**Key Takeaways:**

1. **ARR deadline confirmed** - May 25, 2026 (15 days remaining from May 10)

2. **Research gap identified** - Multiple papers demonstrate that LLMs are fragile to semantic-preserving mutations in code, but **no papers found that propose training code models with contrastive objectives on semantic mutations**. This appears to be an unexplored research direction.

3. **ContraCode opportunity** - ContraCode's approach (semantic-preserving transformations + contrastive learning) has proven effective for representation learning but has never been applied to fault localization, representing a clear research gap.

4. **Fault localization robustness underexplored** - While SWE-bench Verified has fault localization benchmarks, papers don't specifically address robustness to semantic mutations in fault localization contexts.

5. **Validation challenges** - The 2503.23448 paper found only 16/39 proposed semantic-preserving transformations actually preserve semantics, suggesting careful validation is critical for your work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c06579f4-d850-4bc8-aa01-c068167dec7c",
  "isSidechain": true,
  "agentId": "a618f68fb64bb1229",
  "requestId": "req_011CatN57zDRw4nqdgLbnSxP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ac2cdbbc-be75-4718-8e5f-7deed5f2fec5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a498f121-3bf8-4160-8167-b4ab5254c8ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QbwoQmL9jGqg1rSqu5P1Bx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 26190,
      "output_tokens": 2791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 243
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2791,
          "cache_read_input_tokens": 26190,
          "cache_creation_input_tokens": 243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 243,
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
