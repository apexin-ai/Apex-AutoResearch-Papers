# Research conversation: Search the web to verify the EMNLP 2026 submission deadline and whether it uses ARR (ACL Rolling Review): 1. Is EMNLP 20

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aadef7ac003cab343.jsonl`
- **Structured JSON:** [`c818897971f485f7026a.json`](../../sessions/c8/c818897971f485f7026a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-10T20:07:11.385Z_

Search the web to verify the EMNLP 2026 submission deadline and whether it uses ARR (ACL Rolling Review):

1. Is EMNLP 2026 using ARR?
2. What is the ARR submission deadline for papers targeting EMNLP 2026?
3. Is May 25, 2026 a valid ARR deadline?

Try these searches:
- "EMNLP 2026 submission deadline"
- "ACL Rolling Review 2026 deadlines"
- "ARR May 2026 deadline"
- "EMNLP 2026 call for papers"

Report what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "29c21c28-32d1-43a1-915b-aaa2e5d33c88",
  "agentId": "aadef7ac003cab343",
  "type": "user",
  "uuid": "69c7c5ce-dc28-4721-b626-076d8300a7ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T20:07:12.702Z_

I'll search for information about EMNLP 2026 and its use of ARR submission process.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69c7c5ce-dc28-4721-b626-076d8300a7ba",
  "isSidechain": true,
  "agentId": "aadef7ac003cab343",
  "requestId": "req_011CauVTWJKkmdD6h4EkStfb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "31c363f9-ed13-4b03-9183-d0c54bb4f9f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VU3Smh8o34BHys7wjgpy5i",
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

_source line 3 · 2026-05-10T20:07:12.917Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01URDKv94pE1Yazdwn44pRJG`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31c363f9-ed13-4b03-9183-d0c54bb4f9f6",
  "isSidechain": true,
  "agentId": "aadef7ac003cab343",
  "requestId": "req_011CauVTWJKkmdD6h4EkStfb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7d14b52d-8704-42b0-bd12-a178f9e05494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VU3Smh8o34BHys7wjgpy5i",
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

_source line 4 · 2026-05-10T20:07:13.069Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SHVorQEvR6ua4KWfK59iAg`</summary>

```json
{
  "query": "ACL Rolling Review 2026 deadlines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d14b52d-8704-42b0-bd12-a178f9e05494",
  "isSidechain": true,
  "agentId": "aadef7ac003cab343",
  "requestId": "req_011CauVTWJKkmdD6h4EkStfb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f1160e91-621f-42c3-b59b-522622de1ccc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VU3Smh8o34BHys7wjgpy5i",
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

_source line 5 · 2026-05-10T20:07:13.128Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TYLdeB56nLL1oVRUEsCa6q`</summary>

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
  "parentUuid": "f1160e91-621f-42c3-b59b-522622de1ccc",
  "isSidechain": true,
  "agentId": "aadef7ac003cab343",
  "requestId": "req_011CauVTWJKkmdD6h4EkStfb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "814e6ae5-72af-4e17-bfe1-a914bdea1f09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VU3Smh8o34BHys7wjgpy5i",
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

_source line 6 · 2026-05-10T20:07:13.191Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017q8j9BTXjeeR5LUQWt5PRF`</summary>

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
  "parentUuid": "814e6ae5-72af-4e17-bfe1-a914bdea1f09",
  "isSidechain": true,
  "agentId": "aadef7ac003cab343",
  "requestId": "req_011CauVTWJKkmdD6h4EkStfb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "17291f5f-756d-41fd-95c9-e924f288da5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VU3Smh8o34BHys7wjgpy5i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 13789,
      "output_tokens": 219,
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
          "output_tokens": 219,
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

_source line 7 · 2026-05-10T20:07:17.398Z_

<details><summary>↩ Tool result · `toolu_01TYLdeB56nLL1oVRUEsCa6q`</summary>

```text
Web search results for query: "ARR May 2026 deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=arr2601"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AACL 2026 on X: \"🚨AACL-IJCNLP 2026 will be held in Hengqin, China from November 6-10, 2026. The CFP is now out! ARR submission deadline (long &amp; short papers): May 25, 2026! #NLProc #NLP Dates and full CFP here: https://t.co/4ON2H5M7zQ @aadi_joshi @kta84912 https://t.co/9ZKWmY7Jvv\" / X","url":"https://x.com/aaclmeeting/status/2041832211599733075"}]

Based on the search results, the ARR submission deadline in May 2026 is May 25, 2026. This deadline applies to multiple major NLP conferences, including EMNLP 2026 and AACL 2026.

Additionally, after submission, all authors must complete the author registration form by May 27, 2026 EoD AoE for EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "814e6ae5-72af-4e17-bfe1-a914bdea1f09",
  "isSidechain": true,
  "promptId": "29c21c28-32d1-43a1-915b-aaa2e5d33c88",
  "agentId": "aadef7ac003cab343",
  "type": "user",
  "uuid": "66b2e7df-f961-4ac4-acab-4f46d610304e",
  "sourceToolAssistantUUID": "814e6ae5-72af-4e17-bfe1-a914bdea1f09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T20:07:17.665Z_

<details><summary>↩ Tool result · `toolu_01URDKv94pE1Yazdwn44pRJG`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, I found information about EMNLP 2026:

The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026) will be held in Budapest, Hungary from October 24th to October 29th, 2026.

However, the search results indicate that starting from 2024, all main *ACL conferences used ARR (ACL Rolling Review) exclusively, including EMNLP 2026. This means that paper submissions for EMNLP 2026 go through the ACL Rolling Review system rather than direct conference submission.

The search results mention several deadlines such as reviewer registration deadline (May 27, 2026) and author response period dates (July 7-13, 2026), but the specific paper submission deadline to ARR was not clearly stated in these results. For the most current and detailed submission information, I recommend checking the official EMNLP 2026 website at https://2026.emnlp.org/ or the ARR submission portal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d14b52d-8704-42b0-bd12-a178f9e05494",
  "isSidechain": true,
  "promptId": "29c21c28-32d1-43a1-915b-aaa2e5d33c88",
  "agentId": "aadef7ac003cab343",
  "type": "user",
  "uuid": "59ab51d3-453a-488d-8a4b-5198c78757f8",
  "sourceToolAssistantUUID": "7d14b52d-8704-42b0-bd12-a178f9e05494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T20:07:18.279Z_

<details><summary>↩ Tool result · `toolu_01SHVorQEvR6ua4KWfK59iAg`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 deadlines"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL ARR 2025 February | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FFebruary"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl?lang=en"}]

Based on the search results, here are the key ACL Rolling Review (ARR) deadlines for 2026:

## Submission Deadline
The submission deadline for papers is January 5, 2026.

## Author Registration and Review Deadlines
After submission, all authors must complete the author registration form by January 7th 2026 EoD AoE (End of Day, Anywhere on Earth).

If authors are assigned as reviewers or meta-reviewers, reviews must be completed by February 7th, and meta-reviews by March 3rd.

## Results Timeline
ARR reviews and meta-reviews will be available to authors of the January cycle on March 10, 2026.

For ACL 2026 specifically, the commitment deadline is March 14, 2026, with notification on April 4, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1160e91-621f-42c3-b59b-522622de1ccc",
  "isSidechain": true,
  "promptId": "29c21c28-32d1-43a1-915b-aaa2e5d33c88",
  "agentId": "aadef7ac003cab343",
  "type": "user",
  "uuid": "6f8c5acb-9300-4b23-a865-42e0fdd26142",
  "sourceToolAssistantUUID": "f1160e91-621f-42c3-b59b-522622de1ccc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T20:07:20.683Z_

<details><summary>↩ Tool result · `toolu_017q8j9BTXjeeR5LUQWt5PRF`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for Bids to Host EMNLP 2025 or 2026 - SIGDAT","url":"https://sigdat.org/calls/bids2025"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here's the information about the EMNLP 2026 Call for Papers:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Key Dates

The ARR submission deadline is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026. Author response and author-reviewer discussion is July 7-13, 2026, meta review is released July 30, 2026, and the EMNLP commitment deadline is August 2, 2026. Notification of acceptance is August 20, 2026, and camera-ready papers are due September 20, 2026. The main conference will be held in Budapest, Hungary from October 24-29, 2026.

## Submission Process

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026. Papers must be submitted by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR may be committed to EMNLP via the commitment link.

## Special Theme

The EMNLP 2026 special theme invites papers that articulate, test, and advance visions for NLP in this era.

## Important Requirements

All authors are expected to sign up to review or serve as an Area Chair or Senior Area Chair, and must complete the author registration form by May 27, 2026.

For the complete Call for Papers, you can visit the official EMNLP 2026 website at https://2026.emnlp.org/calls/main_conference_papers/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17291f5f-756d-41fd-95c9-e924f288da5f",
  "isSidechain": true,
  "promptId": "29c21c28-32d1-43a1-915b-aaa2e5d33c88",
  "agentId": "aadef7ac003cab343",
  "type": "user",
  "uuid": "539aaf7b-0025-4198-b1cf-d83386c1bbff",
  "sourceToolAssistantUUID": "17291f5f-756d-41fd-95c9-e924f288da5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T20:07:27.076Z_

Based on my search results, here are the answers to your questions about EMNLP 2026:

## 1. Is EMNLP 2026 using ARR?

**Yes.** EMNLP 2026 uses the ACL Rolling Review (ARR) submission system. According to the official EMNLP 2026 announcement, papers must be submitted through ARR rather than through direct conference submission.

## 2. What is the ARR submission deadline for papers targeting EMNLP 2026?

**May 25, 2026.** This is the official ARR submission deadline for papers intended for EMNLP 2026. Following submission, all authors must complete author registration by May 27, 2026 (EoD AoE - End of Day, Anywhere on Earth).

## 3. Is May 25, 2026 a valid ARR deadline?

**Yes.** May 25, 2026 is the official and valid ARR submission deadline for EMNLP 2026. This deadline applies to both long and short papers. Important to note: the May 25 ARR cycle is aligned with two major conferences (EMNLP 2026 and AACL-IJCNLP 2026), so authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding.

**Important Timeline for EMNLP 2026:**
- ARR Submission Deadline: May 25, 2026
- Author Registration Deadline: May 27, 2026
- Author Response Period: July 7-13, 2026
- Meta-review Release: July 30, 2026
- EMNLP Commitment Deadline: August 2, 2026
- Acceptance Notification: August 20, 2026
- Conference: October 24-29, 2026 in Budapest, Hungary

Sources:
- [EMNLP 2026 on X announcing May 25 deadline](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Rolling Review Dates and Venues](http://aclrollingreview.org/dates)
- [AACL 2026 also using May 25 ARR deadline](https://x.com/aaclmeeting/status/2041832211599733075)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "539aaf7b-0025-4198-b1cf-d83386c1bbff",
  "isSidechain": true,
  "agentId": "aadef7ac003cab343",
  "requestId": "req_011CauVUBzXTzV4UozHeTmnE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "760a5c9b-3a1c-463c-8374-fccd117857ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012LJ6CRCbT1deth8cZAupop",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4351,
      "cache_read_input_tokens": 14366,
      "output_tokens": 599,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4351
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 599,
          "cache_read_input_tokens": 14366,
          "cache_creation_input_tokens": 4351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4351,
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
