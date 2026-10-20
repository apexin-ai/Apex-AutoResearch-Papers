# Research conversation: Use WebSearch to verify the following venue information: 1. Search: "EMNLP 2026 ARR submission deadline May 2026" — veri

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a57e3879490389e48.jsonl`
- **Structured JSON:** [`0121a15fada16b021530.json`](../../sessions/01/0121a15fada16b021530.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-11T23:56:57.673Z_

Use WebSearch to verify the following venue information:

1. Search: "EMNLP 2026 ARR submission deadline May 2026" — verify the ARR submission deadline is indeed May 25, 2026
2. Search: "EMNLP 2026 special theme new missions NLP research" — verify the special theme exists and covers "data contamination, synthetic data feedback loops, data governance"
3. Search: "EMNLP 2026 call for papers" — get the official CFP details
4. Search: "ARR May 2026 deadline" — check the actual ARR cycle deadline

Report exactly what you find about dates and themes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f342112d-0940-42ae-8eec-a331a7f6b54e",
  "agentId": "a57e3879490389e48",
  "type": "user",
  "uuid": "35fcaf97-40d0-41a2-ac43-00b647837ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-11T23:56:58.949Z_

I'll search for information about EMNLP 2026 and ARR deadlines to verify the details you've provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35fcaf97-40d0-41a2-ac43-00b647837ea3",
  "isSidechain": true,
  "agentId": "a57e3879490389e48",
  "requestId": "req_011CawgnfiS6Bbzhg4AchRGt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3ea25fd0-d4fe-471a-afeb-dbeed7afb699",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018r2VAVLEctHk342Eqw7PhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 577,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-11T23:56:59.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WJDFsyYubqSGjkUkeWps7G`</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ea25fd0-d4fe-471a-afeb-dbeed7afb699",
  "isSidechain": true,
  "agentId": "a57e3879490389e48",
  "requestId": "req_011CawgnfiS6Bbzhg4AchRGt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "79f96fad-99b1-4a78-b144-64526efe6496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018r2VAVLEctHk342Eqw7PhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 577,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:56:59.171Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GY29c5EvphJQZokfVpNEw7`</summary>

```json
{
  "query": "EMNLP 2026 special theme new missions NLP research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79f96fad-99b1-4a78-b144-64526efe6496",
  "isSidechain": true,
  "agentId": "a57e3879490389e48",
  "requestId": "req_011CawgnfiS6Bbzhg4AchRGt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7eb24af-aa9e-459e-ad12-2c1598197e27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018r2VAVLEctHk342Eqw7PhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 577,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-11T23:56:59.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019rrEEJaHLhFUW5t2hMKvBw`</summary>

```json
{
  "query": "EMNLP 2026 call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7eb24af-aa9e-459e-ad12-2c1598197e27",
  "isSidechain": true,
  "agentId": "a57e3879490389e48",
  "requestId": "req_011CawgnfiS6Bbzhg4AchRGt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a195cb43-6094-4872-bc60-9e6264310225",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018r2VAVLEctHk342Eqw7PhL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 13789,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 577,
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

### Tool call

_source line 6 · 2026-05-11T23:56:59.434Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CXF5YLNgonPLivNVFW24Wm`</summary>

```json
{
  "query": "ARR May 2026 deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a195cb43-6094-4872-bc60-9e6264310225",
  "isSidechain": true,
  "agentId": "a57e3879490389e48",
  "requestId": "req_011CawgnfiS6Bbzhg4AchRGt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a408bc64-db51-495b-82c8-528de1dbce2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018r2VAVLEctHk342Eqw7PhL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 13789,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 577,
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

_source line 7 · 2026-05-11T23:57:03.441Z_

<details><summary>↩ Tool result · `toolu_01WJDFsyYubqSGjkUkeWps7G`</summary>

```text
Web search results for query: "EMNLP 2026 ARR submission deadline May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here's the information about the EMNLP 2026 ARR submission deadline for May 2026:

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

Additional important dates related to the submission process include:
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026

An important note: Since the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79f96fad-99b1-4a78-b144-64526efe6496",
  "isSidechain": true,
  "promptId": "f342112d-0940-42ae-8eec-a331a7f6b54e",
  "agentId": "a57e3879490389e48",
  "type": "user",
  "uuid": "1417250c-7842-4d2b-8890-ae918dc2a228",
  "sourceToolAssistantUUID": "79f96fad-99b1-4a78-b144-64526efe6496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-11T23:57:04.094Z_

<details><summary>↩ Tool result · `toolu_01CXF5YLNgonPLivNVFW24Wm`</summary>

```text
Web search results for query: "ARR May 2026 deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=arr2601"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"AACL 2026 on X: \"🚨AACL-IJCNLP 2026 will be held in Hengqin, China from November 6-10, 2026. The CFP is now out! ARR submission deadline (long &amp; short papers): May 25, 2026! #NLProc #NLP Dates and full CFP here: https://t.co/4ON2H5M7zQ @aadi_joshi @kta84912 https://t.co/9ZKWmY7Jvv\" / X","url":"https://x.com/aaclmeeting/status/2041832211599733075"}]

Based on the search results, I found relevant information about the ARR May 2026 deadline:

The ARR submission deadline is May 25, 2026. After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.

For the ARR 2026 May cycle, which is aligned with both EMNLP and AACL conferences, authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a408bc64-db51-495b-82c8-528de1dbce2c",
  "isSidechain": true,
  "promptId": "f342112d-0940-42ae-8eec-a331a7f6b54e",
  "agentId": "a57e3879490389e48",
  "type": "user",
  "uuid": "d9701098-73e9-41c2-8e70-c7ff82f6b769",
  "sourceToolAssistantUUID": "a408bc64-db51-495b-82c8-528de1dbce2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-11T23:57:05.584Z_

<details><summary>↩ Tool result · `toolu_01GY29c5EvphJQZokfVpNEw7`</summary>

```text
Web search results for query: "EMNLP 2026 special theme new missions NLP research"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"The center of gravity in NLP is shifting. 🌍 This year's #EMNLP2026 Special Theme is \"New Missions for NLP Research.\" We welcome empirical, theoretical, or position and survey papers that reframe our collective research goals. Find out more: https://t.co/6dttoXBb3B\" / X","url":"https://x.com/emnlpmeeting/status/2029509201580446135"},{"title":"EMNLP 2026: Conference on Empirical Methods in Natural Language Processing","url":"https://www.myhuiban.com/conference/424?lang=en_us"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"NLP for Positive Impact","url":"https://sites.google.com/view/nlp4positiveimpact"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"}]

Based on the search results, here's what I found about EMNLP 2026's special theme:

## EMNLP 2026 Special Theme: "New Missions for NLP Research"

The EMNLP 2026 special theme is titled "New Missions for NLP Research." 

Large language models have rapidly shifted from research prototypes to widely used infrastructure. This new reality is changing the center of gravity of NLP research, and progress can no longer be measured only by fractional improvements in benchmark scores. When strong general-purpose models are increasingly available through open releases and commercial platforms, the field faces a more foundational question: What are the missions of NLP research now, and what kinds of contributions most advance that mission?

The EMNLP 2026 special theme invites papers that articulate, test, and advance visions for NLP in this era. The conference welcomes work that reflects on the mission(s) of NLP research, reframes collective research goals, proposes new evaluation and scientific methodologies, and builds bridges across disciplines.

Submissions may be empirical, theoretical, or position and survey papers, but should be grounded in clear claims, strong evidence, and actionable insights. The theme encompasses topics such as data as a bottleneck and responsibility, and LLMs as research tools in AI-supported research processes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7eb24af-aa9e-459e-ad12-2c1598197e27",
  "isSidechain": true,
  "promptId": "f342112d-0940-42ae-8eec-a331a7f6b54e",
  "agentId": "a57e3879490389e48",
  "type": "user",
  "uuid": "0502c9d4-18ff-4636-a0a5-c6c9ac673e69",
  "sourceToolAssistantUUID": "b7eb24af-aa9e-459e-ad12-2c1598197e27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-11T23:57:08.019Z_

<details><summary>↩ Tool result · `toolu_019rrEEJaHLhFUW5t2hMKvBw`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Bids to Host EMNLP 2025 or 2026 - SIGDAT","url":"https://sigdat.org/calls/bids2025"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here's information about the EMNLP 2026 call for papers:

## Submission Guidelines

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Key Deadlines

The ARR submission deadline is May 25, 2026, with reviewer registration deadline for all authors on May 27, 2026. Author response and author-reviewer discussion runs July 7-13, 2026, meta review is released July 30, 2026, and the EMNLP commitment deadline is August 2, 2026. Notification of acceptance is August 20, 2026, with camera-ready papers due September 20, 2026. The main conference will be held in Budapest, Hungary from October 24th to October 29th, 2026.

## Special Submission Requirements

Authors submitting to the ARR 2026 May cycle will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026. Dual submissions are not allowed.

## Review and Ethics

All authors are expected to sign up to review or serve as an Area Chair or Senior Area Chair, and after submission, all authors must complete the author registration form by May 27, 2026. EMNLP has policies against unethical submissions including thinly sliced contributions, submissions with hallucinated citations, and entirely AI-generated papers. Such submissions may be desk rejected, and all authors involved may be ineligible to commit papers to EMNLP 2026 and EMNLP 2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a195cb43-6094-4872-bc60-9e6264310225",
  "isSidechain": true,
  "promptId": "f342112d-0940-42ae-8eec-a331a7f6b54e",
  "agentId": "a57e3879490389e48",
  "type": "user",
  "uuid": "83040d3c-968e-4d34-9873-f6a853bb4c04",
  "sourceToolAssistantUUID": "a195cb43-6094-4872-bc60-9e6264310225",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-11T23:57:18.218Z_

## Verification Report

Based on my web searches, here's what I found about the EMNLP 2026 venue information:

### 1. ARR Submission Deadline - VERIFIED ✓
**Confirmed: May 25, 2026** is indeed the ARR submission deadline for EMNLP 2026. Additional related deadlines include:
- Reviewer registration deadline for all authors: May 27, 2026
- Author response and author-reviewer discussion: July 7-13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026

### 2. Special Theme - PARTIAL VERIFICATION
**Confirmed: The special theme exists** and is titled **"New Missions for NLP Research"**

However, the specific topics you mentioned ("data contamination, synthetic data feedback loops, data governance") were **NOT found** in the search results. The theme description focuses on:
- The center of gravity of NLP research shifting
- Reflecting on the mission(s) of NLP research and reframing collective research goals
- Proposing new evaluation and scientific methodologies
- Building bridges across disciplines
- Data as a bottleneck and responsibility
- LLMs as research tools in AI-supported research processes

The search results indicate the theme is broader than the specific topics you mentioned, though they may be included within the scope.

### 3. Official CFP Details - VERIFIED ✓
EMNLP 2026 welcomes:
- Long and short papers featuring original, unpublished research
- Empirical, theoretical, position, and survey papers
- Negative findings, resource announcements, and reproductions
- Conference location: Budapest, Hungary
- Dates: October 24-29, 2026

### 4. ARR May 2026 Deadline - VERIFIED ✓
**Confirmed: May 25, 2026** is the official ARR May 2026 cycle deadline. This cycle is shared between EMNLP and AACL, requiring authors to explicitly declare their target conference at submission time, with the choice being binding.

Sources:
- [Call for Main Conference Papers - EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 on X - ARR Deadline Announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 on X - Special Theme](https://x.com/emnlpmeeting/status/2029509201580446135)
- [Dates and Venues - ACL Rolling Review](http://aclrollingreview.org/dates)
- [AACL 2026 on X - ARR Deadline](https://x.com/aaclmeeting/status/2041832211599733075)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83040d3c-968e-4d34-9873-f6a853bb4c04",
  "isSidechain": true,
  "agentId": "a57e3879490389e48",
  "requestId": "req_011CawgoRwyhX1LaUZ7y31Bu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68e2a41b-e443-4920-8544-b6b5620ff9eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "eaa350a7-8868-4fb4-94ad-a106b47451dc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017ccCZEDmwTgqz7mXc3zdos",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 798,
      "cache_creation_input_tokens": 4026,
      "cache_read_input_tokens": 14366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4026,
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
