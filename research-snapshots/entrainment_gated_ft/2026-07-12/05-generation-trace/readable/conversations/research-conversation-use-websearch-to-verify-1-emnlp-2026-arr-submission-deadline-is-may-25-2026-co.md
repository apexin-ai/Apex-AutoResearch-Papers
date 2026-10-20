# Research conversation: Use WebSearch to verify: 1. EMNLP 2026 ARR submission deadline — is May 25, 2026 correct? 2. AAAI 2027 submission deadli

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aca6618e3faf8da9f.jsonl`
- **Structured JSON:** [`fd50e868072e7f5bc929.json`](../../sessions/fd/fd50e868072e7f5bc929.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-11T23:41:53.974Z_

Use WebSearch to verify:
1. EMNLP 2026 ARR submission deadline — is May 25, 2026 correct?
2. AAAI 2027 submission deadlines — abstract deadline July 25, 2026 and paper deadline August 1, 2026?
3. ICLR 2027 expected deadline — around September 2026?

Search for:
1. "EMNLP 2026" deadline submission ARR
2. "AAAI 2027" deadline submission
3. "ICLR 2027" deadline submission
4. "ACL Rolling Review" May 2026 deadline

Report exact dates found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aca6618e3faf8da9f",
  "type": "user",
  "uuid": "8acd7285-2c21-49ad-b7ef-2873ab698c35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-11T23:41:55.957Z_

I'll search for the submission deadlines for these conferences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8acd7285-2c21-49ad-b7ef-2873ab698c35",
  "isSidechain": true,
  "agentId": "aca6618e3faf8da9f",
  "requestId": "req_011Cawfe3zm7p1wQVEme12iz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dc052f09-f601-43d6-9697-e509c0e062a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018TjRPPkLan2z4SwE8Kjjpo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-11T23:41:56.211Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HjEjfvnWaLYyGtJaBbmKkk`</summary>

```json
{
  "query": "EMNLP 2026 deadline submission ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc052f09-f601-43d6-9697-e509c0e062a4",
  "isSidechain": true,
  "agentId": "aca6618e3faf8da9f",
  "requestId": "req_011Cawfe3zm7p1wQVEme12iz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a072a9d3-dcc8-40c7-a681-8d2c7fdb5d69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018TjRPPkLan2z4SwE8Kjjpo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:41:56.405Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wc8gbbSAESV2Xghov2wN9Z`</summary>

```json
{
  "query": "AAAI 2027 deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a072a9d3-dcc8-40c7-a681-8d2c7fdb5d69",
  "isSidechain": true,
  "agentId": "aca6618e3faf8da9f",
  "requestId": "req_011Cawfe3zm7p1wQVEme12iz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4561647c-b17a-42b5-baf0-9ca052914bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018TjRPPkLan2z4SwE8Kjjpo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-11T23:41:56.419Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012UUp6yJNPUxK7bRnYwtMbE`</summary>

```json
{
  "query": "ICLR 2027 deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4561647c-b17a-42b5-baf0-9ca052914bbc",
  "isSidechain": true,
  "agentId": "aca6618e3faf8da9f",
  "requestId": "req_011Cawfe3zm7p1wQVEme12iz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7082a417-a569-4b06-9c03-9fcf2f666913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018TjRPPkLan2z4SwE8Kjjpo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-11T23:41:56.533Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KJQ4hwuuBpbw6ipNSXGfHJ`</summary>

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
  "parentUuid": "7082a417-a569-4b06-9c03-9fcf2f666913",
  "isSidechain": true,
  "agentId": "aca6618e3faf8da9f",
  "requestId": "req_011Cawfe3zm7p1wQVEme12iz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ab558ea-effd-4d09-bc8b-f02b852bd1df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018TjRPPkLan2z4SwE8Kjjpo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 16153,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 209,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 585,
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

_source line 7 · 2026-05-11T23:42:00.612Z_

<details><summary>↩ Tool result · `toolu_01Wc8gbbSAESV2Xghov2wN9Z`</summary>

```text
Web search results for query: "AAAI 2027 deadline submission"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"}]

Based on the search results, here's what I found about AAAI 2027 submission deadlines:

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027.

However, the AAAI 2027 paper submission deadline is TBD (To Be Determined). No deadlines have been announced yet.

That said, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

For the most up-to-date information, you can check the official AAAI 2027 call for papers at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4561647c-b17a-42b5-baf0-9ca052914bbc",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aca6618e3faf8da9f",
  "type": "user",
  "uuid": "917ec18b-0187-4ddc-a0c2-531d8c178540",
  "sourceToolAssistantUUID": "4561647c-b17a-42b5-baf0-9ca052914bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-11T23:42:01.361Z_

<details><summary>↩ Tool result · `toolu_012UUp6yJNPUxK7bRnYwtMbE`</summary>

```text
Web search results for query: "ICLR 2027 deadline submission"

Links: [{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"}]

Based on the search results, I was unable to find specific submission deadline information for ICLR 2027. The search results primarily contain information about ICLR 2026 and earlier years.

Here's what I found:

- ICLR is a machine learning conference typically held in late April or early May each year
- The search results show details for ICLR 2026, which had a September 24 submission deadline
- One source mentions that ICLR 2027 is predicted for July 31, 2027, based on the 2026 schedule pattern, though this is not official information

Since ICLR 2027 is still over a year away, the official call for papers and submission deadline have likely not been announced yet. I recommend checking the official ICLR website (iclr.cc) directly or signing up for their mailing list to be notified when the official deadline is announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7082a417-a569-4b06-9c03-9fcf2f666913",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aca6618e3faf8da9f",
  "type": "user",
  "uuid": "f787206d-dbe6-48e7-962e-f59695e5d349",
  "sourceToolAssistantUUID": "7082a417-a569-4b06-9c03-9fcf2f666913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-11T23:42:01.797Z_

<details><summary>↩ Tool result · `toolu_01HjEjfvnWaLYyGtJaBbmKkk`</summary>

```text
Web search results for query: "EMNLP 2026 deadline submission ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"EMNLP 2026 on X: \"The EMNLP call for System Demonstrations has now been posted! The submission deadline is July 4th, with additional details available here: https://t.co/BQvAw3vHxT\" / X","url":"https://x.com/emnlpmeeting/status/1915050634501660921"}]

Based on the search results, here are the key findings for EMNLP 2026 deadline and submission information:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## Important Dates

Key dates include:
- Reviewer registration deadline for all authors: May 27, 2026
- Author response and author-reviewer discussion: July 7-13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026
- Camera-ready papers due: September 20, 2026

## Submission Requirements

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Important Policy Note

For the ARR 2026 May cycle aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: papers that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a072a9d3-dcc8-40c7-a681-8d2c7fdb5d69",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aca6618e3faf8da9f",
  "type": "user",
  "uuid": "7a8a5203-fe28-46d7-a3ab-6a210b1ec816",
  "sourceToolAssistantUUID": "a072a9d3-dcc8-40c7-a681-8d2c7fdb5d69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-11T23:42:01.800Z_

<details><summary>↩ Tool result · `toolu_01KJQ4hwuuBpbw6ipNSXGfHJ`</summary>

```text
Web search results for query: "ACL Rolling Review May 2026 deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, I found information about ACL Rolling Review (ARR) deadlines for 2026. However, the search results don't show a specific May 2026 submission deadline. Instead, they indicate that:

ACL switched to 10-week review cycles starting in May 2025, which changed the submission schedule. Instead of 6 cycles a year there are generally 5, with submissions happening every two months rather than every month.

For ACL 2026 specifically, papers may be submitted to the ARR 2025 October cycle and ARR 2026 January cycle. The January 2026 cycle appears to be the relevant submission period for papers to be reviewed in time for ACL 2026.

If you're looking for a specific May 2026 deadline related to a particular conference or event using ARR, you may want to clarify which specific conference or submission cycle you're interested in, as the May 2026 deadline might be for a different purpose (such as a rebuttal or commitment deadline) rather than a paper submission deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ab558ea-effd-4d09-bc8b-f02b852bd1df",
  "isSidechain": true,
  "promptId": "5f8853e8-2aef-4a0e-9dac-2c5462711b71",
  "agentId": "aca6618e3faf8da9f",
  "type": "user",
  "uuid": "f2c80b3d-b19f-4d4f-84ee-7141f68983f4",
  "sourceToolAssistantUUID": "5ab558ea-effd-4d09-bc8b-f02b852bd1df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-11T23:42:09.361Z_

## Verification Results

Based on my search, here are the exact dates I found:

### 1. EMNLP 2026 ARR Submission Deadline
**CONFIRMED - May 25, 2026 is CORRECT**
- The official EMNLP 2026 social media confirmed the ARR submission deadline is May 25, 2026
- Additional milestone: Reviewer registration deadline is May 27, 2026

### 2. AAAI 2027 Submission Deadlines
**NOT CONFIRMED - Dates Not Yet Announced**
- The search results show that AAAI 2027 submission deadlines are **TBD (To Be Determined)**
- No official announcement has been made yet for the abstract deadline (July 25, 2026) or paper deadline (August 1, 2026)
- Historical patterns suggest deadlines would be expected around July-August 2026, but these specific dates cannot be verified as official

### 3. ICLR 2027 Expected Deadline
**NOT CONFIRMED - Official Dates Not Yet Available**
- ICLR 2027 is over a year away and the official call for papers has not been announced yet
- The search did not find September 2026 as an official deadline
- For context: ICLR 2026 had a September 24 submission deadline, so similar timing might be expected, but this is not confirmed

### 4. ACL Rolling Review May 2026 Deadline
**CLARIFICATION NEEDED**
- ACL switched to 10-week review cycles starting May 2025, with 5 cycles per year instead of 6
- The May 2026 date does not appear to be a standard ARR submission deadline
- For ACL 2026, relevant submission periods appear to be the ARR 2025 October cycle and ARR 2026 January cycle

**Summary**: Only the EMNLP 2026 ARR deadline (May 25, 2026) is confirmed. AAAI 2027 and ICLR 2027 deadlines have not been officially announced yet.

Sources:
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 ARR Deadline Announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)
- [AAAI Conference Official Site](https://aaai.org/conference/aaai/)
- [ICLR Official Site](https://iclr.cc/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2c80b3d-b19f-4d4f-84ee-7141f68983f4",
  "isSidechain": true,
  "agentId": "aca6618e3faf8da9f",
  "requestId": "req_011CawfedRvjFeo5y9zXxHRQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "40441e8f-21ff-4ed3-9e30-e0e2f47b4974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fa720f96-7204-45f0-b6dd-b08abd474ce8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GM7grYjYcCHVoSSCdVRHCm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4068,
      "cache_read_input_tokens": 16738,
      "output_tokens": 641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4068
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 641,
          "cache_read_input_tokens": 16738,
          "cache_creation_input_tokens": 4068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4068,
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
