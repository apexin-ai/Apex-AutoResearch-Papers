# Research conversation: Search the web for the official ACL Rolling Review (ARR) reviewer guidelines and review form criteria for 2026. I need: 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a452e83b9a7c247ae.jsonl`
- **Structured JSON:** [`cb1c17c74c8974d6e4e5.json`](../../sessions/cb/cb1c17c74c8974d6e4e5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-23T14:29:08.931Z_

Search the web for the official ACL Rolling Review (ARR) reviewer guidelines and review form criteria for 2026. I need:
1. The official review form dimensions (e.g., soundness, excitement/novelty, reproducibility, clarity, etc.)
2. The scoring scale for each dimension
3. Any specific instructions for reviewers

Search queries to try:
- "ACL Rolling Review reviewer guidelines 2026"
- "ACL ARR review form criteria"
- "aclrollingreview.org reviewer guidelines"

Report the full scoring rubric and dimensions. Be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "f412b8d5-b619-4d27-9aac-692c365458ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T14:29:08.935Z_

```json
{
  "parentUuid": "f412b8d5-b619-4d27-9aac-692c365458ec",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "3b05ff85-1b03-40d7-a96c-6cb3f3f17329",
  "timestamp": "2026-05-23T14:29:08.935Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-23T14:29:11.072Z_



I'll search for the ACL Rolling Review reviewer guidelines and review form criteria.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b05ff85-1b03-40d7-a96c-6cb3f3f17329",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfCJW1DEqFrB25ZtyQx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e53a05df-e23d-4e0c-a2c8-bd5b1ed3791c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KT6rPaBS7G9GaRwD9zWPQg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18225,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18225,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 4 · 2026-05-23T14:29:11.699Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GNAn42tPRMxgFeqNLuiNkR`</summary>

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
  "parentUuid": "e53a05df-e23d-4e0c-a2c8-bd5b1ed3791c",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfCJW1DEqFrB25ZtyQx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3aeb13aa-caef-4c36-b46e-ea9e736d4828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KT6rPaBS7G9GaRwD9zWPQg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18225,
      "cache_read_input_tokens": 0,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18225
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18225,
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

_source line 5 · 2026-05-23T14:29:11.703Z_

<details><summary>↩ Tool result · `toolu_01GNAn42tPRMxgFeqNLuiNkR`</summary>

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
  "parentUuid": "3aeb13aa-caef-4c36-b46e-ea9e736d4828",
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "5839b0cf-15bd-4483-be70-16ffcb42afc6",
  "sourceToolAssistantUUID": "3aeb13aa-caef-4c36-b46e-ea9e736d4828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-23T14:29:14.493Z_



Now let me search for the ARR reviewer guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5839b0cf-15bd-4483-be70-16ffcb42afc6",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfCWe1BcTUb7y6Q2fFz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9836212d-d188-40f8-b241-dd29b72989b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8tHqoDPLR6LvpdoHeJM5Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1953,
      "cache_read_input_tokens": 18225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1953,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-23T14:29:14.972Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ToKVoncr2Pt41gLUxoZkc5`</summary>

```json
{
  "query": "ACL Rolling Review reviewer guidelines 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9836212d-d188-40f8-b241-dd29b72989b8",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfCWe1BcTUb7y6Q2fFz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7a3e758-2c6f-46d8-b22b-65b984b1c22b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8tHqoDPLR6LvpdoHeJM5Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1953,
      "cache_read_input_tokens": 18225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1953,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-23T14:29:15.466Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JwU51kBFRLEbben3kUuGiA`</summary>

```json
{
  "query": "ACL ARR review form criteria scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a3e758-2c6f-46d8-b22b-65b984b1c22b",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfCWe1BcTUb7y6Q2fFz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cebecbe-dbe6-4a99-bc2e-ef27d2ccf067",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8tHqoDPLR6LvpdoHeJM5Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1953,
      "cache_read_input_tokens": 18225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1953,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 9 · 2026-05-23T14:29:16.082Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VNdenqv6v5xrW9ZdDhzK9Y`</summary>

```json
{
  "query": "aclrollingreview.org reviewer guidelines review form"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cebecbe-dbe6-4a99-bc2e-ef27d2ccf067",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfCWe1BcTUb7y6Q2fFz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d63342e7-1099-4c36-ae3d-4f3578f8d619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8tHqoDPLR6LvpdoHeJM5Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1953,
      "cache_read_input_tokens": 18225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1953,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T14:29:22.473Z_

<details><summary>↩ Tool result · `toolu_01JwU51kBFRLEbben3kUuGiA`</summary>

```text
Web search results for query: "ACL ARR review form criteria scoring dimensions"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL ARR review form criteria and scoring dimensions:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Main Criteria

The main criteria for Findings are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

## Overall Recommendation Scale

The overall recommendation uses the following scoring options:

- 5 = Consider for Award: papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)
- 2 = Resubmit next cycle: papers that need substantial revisions completable by the next ARR cycle
- 1.5 = Resubmit after next cycle: papers that need substantial revisions that cannot be completed by the next ARR cycle
- 1 = Do not resubmit: papers that have to be fully redone, or are not relevant to the *ACL community

## Additional Review Considerations

Reviewers assess whether there is enough information in the paper for a reader to reproduce the main results, use results presented in the paper in future work, or build upon the work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cebecbe-dbe6-4a99-bc2e-ef27d2ccf067",
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "849adada-a732-42e6-9a61-15f4abd84fe1",
  "sourceToolAssistantUUID": "4cebecbe-dbe6-4a99-bc2e-ef27d2ccf067",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T14:29:23.650Z_

<details><summary>↩ Tool result · `toolu_01VNdenqv6v5xrW9ZdDhzK9Y`</summary>

```text
Web search results for query: "aclrollingreview.org reviewer guidelines review form"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"}]

Based on my search results, I found information about the ACL Rolling Review (ARR) reviewer guidelines and review form. Here are the key findings:

## Reviewer Guidelines

As a fresh reviewer, you should form your own opinion of the paper. You will not initially see the previous reviews or the authors' revision notes, but after you submit your review, you will gain access to the old reviews and the revision notes.

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

ARR developed detailed guidelines and suggestions for each step of the process, including a list of common problems in both reviews and NLP papers to watch out for.

## Review Form

Quick links include the Reviewer Guidelines, Reviewers' Guide to OpenReview, and Review Form.

The review form includes sections for:
- Describing what the paper is about to help action editors and area chairs understand the topic and highlight any possible misunderstandings
- Major reasons to publish the paper at a selective *ACL venue, including novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature
- Concerns about the paper that would cause you to favor prioritizing other high-quality papers
- Ethical considerations, with instructions to review the ACL code of ethics and describe any ethical issues
- Reproducibility assessment of the paper

The full reviewer guidelines and review form are available at aclrollingreview.org/reviewerguidelines and aclrollingreview.org/reviewform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d63342e7-1099-4c36-ae3d-4f3578f8d619",
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "fa8aef96-630d-42d1-ad7d-83a48cf14891",
  "sourceToolAssistantUUID": "d63342e7-1099-4c36-ae3d-4f3578f8d619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T14:29:26.807Z_

<details><summary>↩ Tool result · `toolu_01ToKVoncr2Pt41gLUxoZkc5`</summary>

```text
Web search results for query: "ACL Rolling Review reviewer guidelines 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

I found comprehensive information about ACL Rolling Review reviewer guidelines for 2026. Here are the key highlights:

## Reviewer Guidelines Overview

ARR developed detailed guidelines and suggestions for each step of the review process, including a list of common problems in both reviews and NLP papers to watch out for.

## Key Reviewing Standards

ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference. Thus low scores may indicate the submission is not a good fit for ACL, even if it may be a good fit for other/more specialized venues.

## Author Anonymity Guidelines

Reviewers for *ACL conferences and TACL should be instructed not to actively try to discover the identity of the authors and not to let any suspicion or knowledge of author identity affect their judgment of the paper. This should not prevent them from searching for related work, but they should take special care and postpone such searches until after they have read the paper completely and formed an initial impression of it.

## Reporting Issues

Since the reviewer and AC guidelines may also be seen by the authors during the response period, some sections of these guidelines now have codes for (meta-)review issues (I1-I12) that can be reported by the authors.

## Incentives and Accountability

Starting from May 2025, ACL introduces the awards policy for reviewers & chairs. In short, the area chairs or senior area chairs may nominate the great reviewers, and senior chairs may also nominate area chairs who perform great service. The nominees will then receive more recognition during the ACL conferences.

Starting in May 2025, ARR also adopts the new policy on the 'highly irresponsible' (meta-)reviewers. The program chairs and ARR EiCs will consider the egregious cases reported by chairs, including the cases of extremely terse reviews, unprofessional tone, and LLM-generated reviews. The 'highly irresponsible' reviewers or chairs may have their work desk-rejected from the current cycle, and ineligible for resubmission or commitment during the following ARR cycle.

For the complete reviewer guidelines, you can visit the official ACL Rolling Review Reviewer Guidelines page at http://aclrollingreview.org/reviewerguidelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7a3e758-2c6f-46d8-b22b-65b984b1c22b",
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "faaec872-bda2-4953-b912-aeb4f2545ea0",
  "sourceToolAssistantUUID": "c7a3e758-2c6f-46d8-b22b-65b984b1c22b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T14:29:32.418Z_

Now let me fetch the actual review form page and reviewer guidelines page for the complete details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faaec872-bda2-4953-b912-aeb4f2545ea0",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfDcspoLgguyBY19WGx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9c152bd-507f-48df-8cac-cea75f38e5e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsKb2vE8odXr6jM64kJRsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1475,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 20178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1151,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 14 · 2026-05-23T14:29:36.171Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VBQXHoZ5sgb1xroKaUV9KQ`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL fields, ALL scoring dimensions, ALL scoring scales with every option listed, and ALL instructions for each field. I need the full rubric including soundness, excitement, overall assessment, and any other scored dimensions. Include the exact text of each scale option (e.g., 5 = ..., 4 = ..., etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9c152bd-507f-48df-8cac-cea75f38e5e1",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfDcspoLgguyBY19WGx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93a032a4-c01e-4cb9-a272-0e92c51be788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsKb2vE8odXr6jM64kJRsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1475,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 20178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1151,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 15 · 2026-05-23T14:29:36.920Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NyoYjcpFLhnvyX4UjiJhuU`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the COMPLETE reviewer guidelines text, including all sections, all instructions for reviewers, common problems to watch for, and any scoring guidance. I need the full text of the guidelines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93a032a4-c01e-4cb9-a272-0e92c51be788",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfDcspoLgguyBY19WGx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2cc2d00-f843-4a0f-bd1e-e87cfe0ccca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsKb2vE8odXr6jM64kJRsg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1475,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 20178,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1151
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1475,
          "output_tokens": 280,
          "cache_read_input_tokens": 20178,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1151,
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

_source line 16 · 2026-05-23T14:29:45.086Z_

<details><summary>↩ Tool result · `toolu_01VBQXHoZ5sgb1xroKaUV9KQ`</summary>

```text
# ACL Rolling Review Form - Complete Rubric

## Core Evaluation Sections

**Paper Summary**
Authors describe the paper's topic to help editors and chairs understand the work.

**Summary of Strengths**
Identify major publication reasons, such as novel methodology, empirical results, theoretical analysis, or literature organization.

**Summary of Weaknesses**
Number concerns about correctness, limited impact, clarity, or other factors affecting publication priority.

**Comments/Suggestions/Typos**
Additional improvement suggestions beyond addressing main concerns.

## Scoring Dimensions

### Reviewer Confidence
- 5 = "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4 = "Quite sure. I tried to check the important points carefully."
- 3 = "Pretty sure, but there's a chance I missed something."
- 2 = "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- 1 = "Not my area, or paper is very hard to understand."

### Soundness
- 5 = "Excellent: This study is one of the most thorough I have seen."
- 4 = "Strong: This study provides sufficient support for all of its claims."
- 3 = "Acceptable: This study provides sufficient support for its main claims."
- 2 = "Poor: Some of the main claims are not sufficiently supported."
- 1 = "Major Issues: This study is not yet sufficiently thorough to warrant publication."

### Excitement
- 5 = "Highly Exciting: I would recommend this paper to others."
- 4 = "Exciting: I would mention this paper to others."
- 3 = "Interesting: I might mention some points of this paper to others."
- 2 = "Potentially Interesting: this paper does not resonate with me."
- 1 = "Not Exciting: this paper does not resonate with me."

### Overall Assessment
- 5 = Consider for Award (top 2.5%)
- 4.5 = Borderline Award
- 4 = Conference acceptance
- 3.5 = Borderline Conference
- 3 = Findings acceptance
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

## Additional Questions

**Limitations and Societal Impact** - Evaluate author discussion of limitations and potential impacts.

**Ethical Concerns** - Review against ACL code of ethics and author checklist.

**Needs Ethics Review** - Identify papers requiring in-depth ethics committee examination.

**Reproducibility** (1-5 scale) - Assess whether readers can reproduce results.

**Datasets** (1-5 scale) - Rate value of released datasets if applicable.

**Software** (1-5 scale) - Rate value of released software if applicable.

**Author Identity Knowledge** (1-5 scale) - Disclose any identity information sources.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93a032a4-c01e-4cb9-a272-0e92c51be788",
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "d9d70550-3c44-4b9b-93e3-a2cf71406744",
  "sourceToolAssistantUUID": "93a032a4-c01e-4cb9-a272-0e92c51be788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T14:29:47.115Z_

<details><summary>↩ Tool result · `toolu_01NyoYjcpFLhnvyX4UjiJhuU`</summary>

```text
# ACL Rolling Review (ARR) Reviewer Guidelines - Summary

I can provide a comprehensive overview of the ARR reviewer guidelines rather than reproducing the full text. Here are the key components:

## Core Tasks for Reviewers

**Task 1: Time Management**
Reviewers should allocate calendar time for reading assignments, writing reviews, and participating in discussion periods. The guidelines suggest estimating time based on paper length and complexity.

**Task 2: Assignment Verification**
- Check expertise match and potential conflicts of interest
- Complete a desk-rejection checklist covering appropriateness, hallucinated references, anonymity violations, formatting issues, missing limitations sections, and ethics concerns

**Task 3: Writing Strong Reviews**
The guidelines emphasize: "read the paper at least twice: skimming and in-depth reading" to avoid hindsight and confirmation biases. Key requirements include being specific with criticisms, avoiding common review pitfalls, and ensuring tone remains professional.

**Task 4: Post-Response Updates**
Reviewers should acknowledge author responses and update assessments based on clarifications or new information.

## Scoring Framework (February 2025 onwards)
Three scores required: soundness, excitement, and overall recommendation. The guidance notes that "soundness scores must be justified by the text of the review."

## Common Review Pitfalls (17 Heuristics Listed)
Including assumptions like "results are surprising = bad," "simple methods are inferior," and "non-English work won't generalize."

## Common NLP Paper Problems
Categories: Methodology (M1-M5), Artifact Sourcing (T1-T2), Results (R1-R5), General Issues (G1-G5).

## Confidentiality, Generative AI, and Ethics
Detailed policies on anonymity, prohibitions against uploading papers to commercial AI tools, and guidance on ethics flagging.

Would you like me to elaborate on any specific section?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2cc2d00-f843-4a0f-bd1e-e87cfe0ccca4",
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "b294389e-884b-426c-be5f-6dbe1eac0f90",
  "sourceToolAssistantUUID": "e2cc2d00-f843-4a0f-bd1e-e87cfe0ccca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-23T14:29:50.050Z_

Good, I have the core dimensions. Let me fetch more details on the reviewer guidelines, particularly the common problems and the full scoring guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b294389e-884b-426c-be5f-6dbe1eac0f90",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfF7jgWWwgimp9xjmVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0897c5d9-8664-42a1-8313-3576ae8511f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VN6hJyvANMnuhSN7wvAi27",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2965,
      "cache_read_input_tokens": 21329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2965,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 19 · 2026-05-23T14:29:52.559Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012DT9NhFBFNRiTvTuuT2J98`</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewform.md",
  "prompt": "Extract the COMPLETE review form markdown text, including ALL fields, ALL scoring options with their full descriptions, and ALL instructions. I need every single field and every single scale option with exact wording."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0897c5d9-8664-42a1-8313-3576ae8511f7",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfF7jgWWwgimp9xjmVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59a5411c-caba-494e-bb93-5f724caa279a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VN6hJyvANMnuhSN7wvAi27",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2965,
      "cache_read_input_tokens": 21329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2965,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 20 · 2026-05-23T14:29:54.424Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AwkZsKsd25uvu712jbAWh1`</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md",
  "prompt": "Extract the COMPLETE reviewer guidelines markdown text. Include ALL sections: the scoring guidance, common review pitfalls/heuristics, common NLP paper problems (M1-M5, T1-T2, R1-R5, G1-G5), desk-rejection checklist, and all other guidance. I need the full text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59a5411c-caba-494e-bb93-5f724caa279a",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfF7jgWWwgimp9xjmVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "150009ea-dae5-49e7-baf1-71ae3cc3587f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VN6hJyvANMnuhSN7wvAi27",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2965,
      "cache_read_input_tokens": 21329,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2965
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 314,
          "cache_read_input_tokens": 21329,
          "cache_creation_input_tokens": 2965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2965,
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

_source line 21 · 2026-05-23T14:30:04.610Z_

<details><summary>↩ Tool result · `toolu_012DT9NhFBFNRiTvTuuT2J98`</summary>

```text
# ACL Rolling Review Form - Complete Extraction

## Core Review Sections

**Paper Summary**: "Describe what this paper is about. This should help action editors and area chairs to understand the topic"

**Summary of Strengths**: Solicits reasons to publish at selective *ACL venues, including novel methodology, empirical results, theoretical analysis, and literature organization.

**Summary of Weaknesses**: Requests concerns prioritizing other papers, including correctness issues, limited impact, clarity problems, and numbered concerns for author response.

**Comments/Suggestions/Typos**: Space for improvement suggestions beyond main concerns.

## Evaluation Scales

**Reviewer Confidence** (1-5):
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure... unlikely, though conceivable, that I missed something"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend... fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

**Soundness** (1-5 with half-points):
- 5: "One of the most thorough I have seen, given its type"
- 4: "Provides sufficient support for all claims"
- 3: "Sufficient support for main claims. Some minor points may need extra support"
- 2: "Main claims not sufficiently supported. Major technical/methodological problems"
- 1: "Not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 with half-points):
- 5: "I would recommend this paper to others and/or attend its presentation"
- 4: "I would mention this paper to others"
- 3: "I might mention some points... if there's time"
- 2: "Does not resonate with me, but might with others"
- 1: "Does not resonate with me... not related to computational processing of language"

**Overall Assessment** (1-5 with half-points):
- 5: "Consider for Award: could be considered for outstanding paper award (top 2.5%)"
- 4: "Conference: could be accepted to *ACL conference"
- 3: "Findings: could be accepted to Findings of the ACL"
- 2: "Resubmit next cycle: needs substantial revisions"
- 1: "Do not resubmit: fully redone or not relevant to *ACL community"

**Best Paper Justification**: Required if rating is 5 or 4.5.

## Additional Questions

**Limitations and Societal Impact**: Assessment of author discussion regarding limitations, positive/negative impacts, exclusion, overgeneralization, bias, and failure modes.

**Ethical Concerns**: Review against ACL code of ethics and ARR checklist.

**Needs Ethics Review**: Determination if paper requires special ethics committee review.

**Reproducibility** (1-5):
- 5: "Could easily reproduce results"
- 4: "Could mostly reproduce... may have some variation"
- 3: "Could reproduce... with some difficulty"
- 2: "Would be hard pressed to reproduce"
- 1: "Would not be able to reproduce"

**Datasets** (1-5):
- 5: "Enabling: should affect research project choices"
- 4: "Useful: would recommend to others"
- 3: "Potentially useful"
- 2: "Documentary: useful for replication"
- 1: "No usable datasets"

**Software** (1-5):
- 5: "Enabling: should affect development project choices"
- 4: "Useful: would recommend"
- 3: "Potentially useful"
- 2: "Documentary: useful for replication"
- 1: "No usable software released"

**Author Identity Knowledge** (1-5):
- 5: "Know/can guess author name from submission violations"
- 4: "Know/can guess from preprint or workshop paper"
- 3: "Know/can guess from submission contents"
- 2: "Know/can guess from social media or informal communication"
- 1: "No educated guess about author identity"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59a5411c-caba-494e-bb93-5f724caa279a",
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "ba07beca-5f20-4174-a76c-21719c90fe4c",
  "sourceToolAssistantUUID": "59a5411c-caba-494e-bb93-5f724caa279a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T14:30:04.742Z_

<details><summary>↩ Tool result · `toolu_01AwkZsKsd25uvu712jbAWh1`</summary>

```text
# Summary of ACL Rolling Review (ARR) Reviewer Guidelines

I can provide a **summary** of the key guidelines rather than reproducing the full text, which would exceed appropriate length limits.

## Core Reviewing Tasks

**Task 1: Time Management** – Block calendar time for reviewing and discussion periods, accounting for reading, writing (~half page), and revision time.

**Task 2: Assignment Check** – Verify you're qualified to review by assessing expertise match, author anonymity concerns, and conflicts of interest. Flag reassignments if needed.

**Task 3: Write Strong Reviews** – Read papers twice (skim then in-depth), adjust expectations based on contribution type rather than personal methodology preferences, be specific with critiques.

**Task 4: Engage Post-Response** – Acknowledge author responses and update assessments; discuss with other reviewers.

## Common Review Pitfalls (Heuristics H1-H17)

Reviewers should avoid claiming work is "not novel" without references, requiring state-of-the-art results, demanding unnecessary experiments, or dismissing contributions for using "simple" methods, non-English languages, or negative results. These often reflect unconscious bias rather than valid weaknesses.

## Common NLP Paper Problems

- **Methodology (M1-M5):** LLM-only evaluation without validation, reproducibility gaps, undisclosed data issues, unmotivated selections, incomplete proofs
- **Artifacts (T1-T2):** Ethics violations in data collection, unclear licensing
- **Results (R1-R5):** Statistical issues, inappropriate claim scope, speculation presented as fact, overclaiming
- **General (G1-G5):** Unclear research questions, problematic precedents, missing/misrepresented related work, vague terminology, misleading citations

## Desk-Rejection Checklist

Papers may be rejected early for: inappropriateness to ARR, hallucinated references, anonymity violations, style/length violations, missing limitations, egregious responsible NLP checklist failures, or significant ethics issues requiring separate review.

## Professional Standards

Scores must align with review justification. Maintain professional tone, avoid sarcasm, and remember that reviewing involves colleagues deserving respectful feedback. Use generative AI responsibly—never upload manuscripts or reviews to non-private tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "150009ea-dae5-49e7-baf1-71ae3cc3587f",
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "3010a5bb-7cca-446b-9788-e226008a5bbe",
  "sourceToolAssistantUUID": "150009ea-dae5-49e7-baf1-71ae3cc3587f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-23T14:30:07.987Z_

Let me also get the full details on the half-point overall assessment scale and the specific desk-rejection checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3010a5bb-7cca-446b-9788-e226008a5bbe",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfGRAxEH5Caug3QtQaA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c37c809-f81c-4c2b-8c19-6765c2d53123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HqXhdQtM16BVEaVQFqqrRL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 24294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1982,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 24 · 2026-05-23T14:30:08.813Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TPZbqspLNhr6rdD6RZfnkK`</summary>

```json
{
  "query": "ACL ARR review form \"overall assessment\" \"4.5\" \"3.5\" \"2.5\" \"1.5\" full scale descriptions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c37c809-f81c-4c2b-8c19-6765c2d53123",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfGRAxEH5Caug3QtQaA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f325302d-4dd5-4dba-8bb4-46d008a44fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HqXhdQtM16BVEaVQFqqrRL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 24294,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1982
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 24294,
          "cache_creation_input_tokens": 1982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1982,
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

_source line 25 · 2026-05-23T14:30:30.129Z_

<details><summary>↩ Tool result · `toolu_01TPZbqspLNhr6rdD6RZfnkK`</summary>

```text
Web search results for query: "ACL ARR review form "overall assessment" "4.5" "3.5" "2.5" "1.5" full scale descriptions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Action Editor Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/actioneditorform"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Let me search more specifically for the full scale descriptions with those specific numerical values:

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Assessment of Anterior Cruciate Ligament Injury Risk Based on Human Key   Points Detection Algorithm","url":"https://arxiv.org/pdf/2305.14612"},{"title":"Can a knee sleeve influence ground reaction forces and knee joint power during a step-down hop in participants following ACL reconstruction? An explanatory analysis","url":"https://www.medrxiv.org/content/10.1101/2022.08.17.22278057.full.pdf"},{"title":"Anterior cruciate ligament—Return to sport after injury scale brief version after ACL reconstruction: Persian translation, cross‐cultural adaptation and validation","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11228620/"},{"title":"Responsiveness of the Various Short-Form Versions of the Knee Injury and Osteoarthritis Outcome Score Between 2 and 5 Years After Anterior Cruciate Ligament Reconstruction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10960337/"},{"title":"Anterior cruciate ligament—return to sport after injury scale: validation of the Norwegian language version","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7429529/"},{"title":"Content validity, interpretability, and internal consistency of the “Quality First” assessment to evaluate movement quality in hop tests following ACL rehabilitation. A cross-sectional study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10313111/"}]

Let me search for the complete ARR review form with all scale descriptions:

Links: [{"title":"ACL 2022 Chair Blog Post FAQ","url":"https://www.2022.aclweb.org/post/acl-2022-chair-blog-post-faq"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL 2022 Chair Blog Post FAQ","url":"https://2022.aclweb.org/post/acl-2022-chair-blog-post-faq.html"}]

Let me try one more search for the current/full ARR review form with decimal scores:

Links: [{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Action Editor Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/actioneditorform"},{"title":"Review Forms","url":"https://aclrollingreview.org/reviewforms/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Perfect! I found the information. Let me search for any additional descriptions, particularly for the 4.5 and 5.0 scores:

Links: [{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"}]

Perfect! I now have all the information needed. Based on my web search results, here is the ACL ARR review form's overall assessment scale with full descriptions:

## ACL ARR Review Form - Overall Assessment Scale

**5 = Consider for Award:** "I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)."

**4.5 = Borderline Award**

**4 = Conference:** "I think this paper could be accepted to an *ACL conference."

**3.5 = Borderline Conference**

**3 = Findings:** "I think this paper could be accepted to the Findings of the ACL."

**2.5 = Borderline Findings**

**2 = Resubmit next cycle:** "I think this paper needs substantial revisions that can be completed by the next ARR cycle."

**1.5 = Resubmit after next cycle:** "I think this paper needs substantial revisions that cannot be completed by the next ARR cycle."

**1 = Do not resubmit:** "This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language)."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f325302d-4dd5-4dba-8bb4-46d008a44fb6",
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "7fe185bf-1be5-410e-be54-e8b9a5435565",
  "sourceToolAssistantUUID": "f325302d-4dd5-4dba-8bb4-46d008a44fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-23T14:30:34.159Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WX6SB4WKWcK1nNg2EnheCP`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewforms/",
  "prompt": "Extract the COMPLETE review form specifications. Include ALL fields, ALL scoring scales with exact wording for each option, and ALL instructions. I need the full details of every dimension including soundness, excitement, overall assessment, reproducibility, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fe185bf-1be5-410e-be54-e8b9a5435565",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfJHc6AfYdLGY9sH632",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a66e7ba4-34d1-461b-b91f-e2d13b97a044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWkuh18qVZUSScMuQViCGA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2039,
      "cache_read_input_tokens": 26276,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 26276,
          "cache_creation_input_tokens": 2039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2039,
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

_source line 27 · 2026-05-23T14:30:38.101Z_

<details><summary>↩ Tool result · `toolu_01WX6SB4WKWcK1nNg2EnheCP`</summary>

```text
I cannot provide the complete review form specifications you've requested because **the web page content provided does not contain that information**.

The page is merely an announcement stating: "The draft review forms are up at [here](/reviewers)!" It links to the reviewers section but doesn't include the actual form details, scoring scales, or evaluation criteria.

To obtain the complete review form specifications with all fields, scoring options, and instructions, you would need to:

1. Visit the `/reviewers` page referenced in the announcement
2. Check the [Reviewer guidelines](/reviewerguidelines) page
3. Access the full documentation on the ACL Rolling Review platform

The current content only confirms that forms exist and that volunteer reviewers are being recruited—it doesn't detail the forms themselves.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a66e7ba4-34d1-461b-b91f-e2d13b97a044",
  "isSidechain": true,
  "promptId": "01d00af2-eb9e-4f5a-b3be-ecbaf36ea613",
  "agentId": "a452e83b9a7c247ae",
  "type": "user",
  "uuid": "f5f06032-3e4f-4af8-8853-256c511265f2",
  "sourceToolAssistantUUID": "a66e7ba4-34d1-461b-b91f-e2d13b97a044",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-23T14:31:28.794Z_

I now have comprehensive information. Here is the full report.

---

## ACL Rolling Review (ARR) Official Review Form and Reviewer Guidelines

### Review Form Dimensions and Scoring Scales

The ARR review form (as of February 2025 onwards, still current for 2026) consists of the following sections and scored dimensions:

---

#### 1. Paper Summary (text field)
"Describe what this paper is about. This should help action editors and area chairs to understand the topic of the paper and highlight any possible misunderstandings."

#### 2. Summary of Strengths (text field)
Identify major reasons to publish at a selective *ACL venue, including: novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature.

#### 3. Summary of Weaknesses (text field)
Number your concerns about the paper that would cause you to favor prioritizing other high-quality papers. Include: correctness issues, limited impact, clarity problems, or other factors.

#### 4. Comments / Suggestions / Typos (text field)
Additional improvement suggestions beyond addressing main concerns.

---

### Scored Dimensions

#### A. Soundness (1-5 scale, half-points allowed)

| Score | Label | Description |
|-------|-------|-------------|
| 5 | Excellent | "This study is one of the most thorough I have seen, given its type." |
| 4 | Strong | "This study provides sufficient support for all of its claims/findings." |
| 3 | Acceptable | "This study provides sufficient support for its main claims/findings. Some minor points may need extra support or details." |
| 2 | Poor | "Some of the main claims/findings are not sufficiently supported. There are major technical/methodological problems." |
| 1 | Major Issues | "This study is not yet sufficiently thorough to warrant publication." |

#### B. Excitement (1-5 scale, half-points allowed)

| Score | Label | Description |
|-------|-------|-------------|
| 5 | Highly Exciting | "I would recommend this paper to others and/or attend its presentation." |
| 4 | Exciting | "I would mention this paper to others." |
| 3 | Interesting | "I might mention some points of this paper to others, if there's time." |
| 2 | Potentially Interesting | "This paper does not resonate with me, but might with others." |
| 1 | Not Exciting | "This paper does not resonate with me... not related to computational processing of language." |

#### C. Overall Assessment (1-5 scale, half-point increments)

| Score | Label | Description |
|-------|-------|-------------|
| 5 | Consider for Award | "Could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)." |
| 4.5 | Borderline Award | (borderline between Award and Conference) |
| 4 | Conference | "Could be accepted to an *ACL conference." |
| 3.5 | Borderline Conference | (borderline between Conference and Findings) |
| 3 | Findings | "Could be accepted to the Findings of the ACL." |
| 2.5 | Borderline Findings | (borderline between Findings and Resubmit) |
| 2 | Resubmit next cycle | "Needs substantial revisions that can be completed by the next ARR cycle." |
| 1.5 | Resubmit after next cycle | "Needs substantial revisions that cannot be completed by the next ARR cycle." |
| 1 | Do not resubmit | "Has to be fully redone, or is not relevant to the *ACL community." |

**Note:** If rating is 5 or 4.5, a **Best Paper Justification** text field is required.

#### D. Reviewer Confidence (1-5 scale)

| Score | Description |
|-------|-------------|
| 5 | "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work." |
| 4 | "Quite sure. I tried to check the important points carefully. It is unlikely, though conceivable, that I missed something." |
| 3 | "Pretty sure, but there's a chance I missed something. Although I have a good feel for this topic, I did not carefully check all details." |
| 2 | "Willing to defend my evaluation, but it is fairly likely that I missed some details, didn't understand some central points, or can't be sure about the novelty." |
| 1 | "Not my area, or paper is very hard to understand. My evaluation is just an educated guess." |

#### E. Reproducibility (1-5 scale)

| Score | Description |
|-------|-------------|
| 5 | "Could easily reproduce the results." |
| 4 | "Could mostly reproduce the results, but there may be some variation." |
| 3 | "Could reproduce the results with some difficulty." |
| 2 | "Would be hard pressed to reproduce the results." |
| 1 | "Would not be able to reproduce the results." |

#### F. Datasets (1-5 scale, if applicable)

| Score | Description |
|-------|-------------|
| 5 | "Enabling: should affect research project choices." |
| 4 | "Useful: would recommend to others." |
| 3 | "Potentially useful." |
| 2 | "Documentary: useful for replication only." |
| 1 | "No usable datasets submitted." |

#### G. Software (1-5 scale, if applicable)

| Score | Description |
|-------|-------------|
| 5 | "Enabling: should affect development project choices." |
| 4 | "Useful: would recommend to others." |
| 3 | "Potentially useful." |
| 2 | "Documentary: useful for replication only." |
| 1 | "No usable software released." |

#### H. Author Identity Knowledge (1-5 scale)

| Score | Description |
|-------|-------------|
| 5 | "Know/can guess author name from submission policy violations." |
| 4 | "Know/can guess from preprint or workshop paper." |
| 3 | "Know/can guess from submission contents." |
| 2 | "Know/can guess from social media or informal communication." |
| 1 | "No educated guess about author identity." |

---

### Additional Non-Scored Fields

- **Limitations and Societal Impact**: Evaluate the author's discussion of limitations, positive/negative impacts, exclusion, overgeneralization, bias, and failure modes.
- **Ethical Concerns**: Review against the ACL code of ethics and the responsible NLP checklist.
- **Needs Ethics Review**: Flag if paper requires in-depth ethics committee examination.

---

### Key Reviewer Instructions

**Scoring alignment**: The three primary scores (Soundness, Excitement, Overall Assessment) must be justified by the text of the review. Scores must align with written justification.

**Main criteria for Findings**: soundness and reproducibility. Conference recommendations may also consider novelty, impact, and other factors.

**Reading protocol**: Read the paper at least twice (skim then in-depth reading) to avoid hindsight and confirmation biases.

**Common NLP paper problems to check for**:
- **Methodology (M1-M5)**: LLM-only evaluation without validation, reproducibility gaps, undisclosed data issues, unmotivated method selections, incomplete proofs
- **Artifacts (T1-T2)**: Ethics violations in data collection, unclear licensing
- **Results (R1-R5)**: Statistical issues, inappropriate claim scope, speculation as fact, overclaiming
- **General (G1-G5)**: Unclear research questions, problematic precedents, missing/misrepresented related work, vague terminology, misleading citations

**Desk-rejection checklist**: Papers may be rejected for: inappropriateness to ARR, hallucinated references, anonymity violations, style/length violations, missing limitations section, egregious responsible NLP checklist failures, or significant ethics issues.

**Policy on generative AI**: Reviewers must not upload manuscripts or reviews to non-private AI tools.

**Irresponsible reviewer policy** (from May 2025): Extremely terse reviews, unprofessional tone, and LLM-generated reviews may result in desk-rejection of the reviewer's own work and ineligibility for the following ARR cycle.

Sources:
- [ARR Review Form](https://aclrollingreview.org/reviewform)
- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)
- [ARR Review Form (GitHub source)](https://github.com/acl-org/aclrollingreview/blob/main/reviewform.md)
- [ARR Reviewer Guidelines (GitHub source)](https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR Incentives 2026](https://aclrollingreview.org/incentives2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5f06032-3e4f-4af8-8853-256c511265f2",
  "isSidechain": true,
  "agentId": "a452e83b9a7c247ae",
  "requestId": "req_011CbKfJsiw3EGSzGh6XKyV8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d43c51f2-54cd-479f-aaf5-233d114b3fee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "37f8dc98-4501-4796-b2b3-37a2f989f4d8",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbcqUUoUPm5FX3MgAnSD3B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 28315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 305,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
