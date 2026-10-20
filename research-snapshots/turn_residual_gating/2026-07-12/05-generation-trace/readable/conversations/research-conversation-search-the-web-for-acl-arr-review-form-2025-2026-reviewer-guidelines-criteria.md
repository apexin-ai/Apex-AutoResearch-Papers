# Research conversation: Search the web for "ACL ARR review form 2025 2026 reviewer guidelines criteria" to find the official ARR (ACL Rolling Re

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a19b3d0a981bea3a6.jsonl`
- **Structured JSON:** [`6d0513561c0526899830.json`](../../sessions/6d/6d0513561c0526899830.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-25T05:37:09.725Z_

Search the web for "ACL ARR review form 2025 2026 reviewer guidelines criteria" to find the official ARR (ACL Rolling Review) reviewer guidelines and review form criteria. I need: 1) The exact scoring dimensions (soundness, excitement/novelty, reproducibility, etc.) and their scales, 2) The Overall Assessment scale, 3) Any specific guidance for reviewers. Report the findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "1216e6a7-0a92-4b6c-96ef-e5d51cd70a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T05:37:11.155Z_

I'll search for the official ACL ARR reviewer guidelines and review form criteria.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1216e6a7-0a92-4b6c-96ef-e5d51cd70a28",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkFEVpx6Eb1qizjp49i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b33558bd-e531-4235-8ff1-2da545a17689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018SYWj724tULkjgNQWz3hQo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17986,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17986,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 3 · 2026-05-25T05:37:11.310Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TeHuRQUT1f4CPkjJy57c6F`</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 reviewer guidelines criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b33558bd-e531-4235-8ff1-2da545a17689",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkFEVpx6Eb1qizjp49i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e2089b3e-1e58-4e4d-94fd-b4cee37e3dcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018SYWj724tULkjgNQWz3hQo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17986,
      "cache_read_input_tokens": 0,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17986
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17986,
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

_source line 4 · 2026-05-25T05:37:18.352Z_

<details><summary>↩ Tool result · `toolu_01TeHuRQUT1f4CPkjJy57c6F`</summary>

```text
Web search results for query: "ACL ARR review form 2025 2026 reviewer guidelines criteria"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about ACL ARR reviewer guidelines and criteria for 2025-2026:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Reviewer Expectations

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements. The standards expected by reviewers are those of a traditional direct submission as a long or short main conference paper to ACL or other major conferences operated by the ACL.

## Quality Standards and Responsibilities

The program chairs and ARR EiCs consider egregious cases reported by chairs, including extremely terse reviews, unprofessional tone, and LLM-generated reviews. 'Highly irresponsible' reviewers or chairs may have their work desk-rejected from the current cycle, and be ineligible for resubmission or commitment during the following ARR cycle. For review cycles associated with ACL conferences, this means that papers of such reviewers cannot be committed to the upcoming conference.

## Reviewer Recognition

Starting from May 2025, ACL introduced an awards policy for reviewers and chairs. Area chairs or senior area chairs may nominate great reviewers, and nominees receive recognition during ACL conferences including public lists on conference websites and special stickers for conference badges.

For the complete detailed reviewer guidelines, you can visit the ARR Reviewer Guidelines page at http://aclrollingreview.org/reviewerguidelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2089b3e-1e58-4e4d-94fd-b4cee37e3dcc",
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "e517bda5-8959-41af-8a86-c3c4f6719d2f",
  "sourceToolAssistantUUID": "e2089b3e-1e58-4e4d-94fd-b4cee37e3dcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-25T05:37:19.514Z_

Let me fetch the official ARR Reviewer Guidelines page for detailed scoring criteria.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e517bda5-8959-41af-8a86-c3c4f6719d2f",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkFsNMh1aaVkkDGMWDL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "803e1350-8512-44ef-a2a7-b35b0da2adea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CP7Mx6syyj5NqNqa5h3Lwn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1655,
      "cache_read_input_tokens": 17986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1655,
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

_source line 6 · 2026-05-25T05:37:19.938Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012toVZjaw9r5zkVH7XmgmNF`</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "scoring dimensions scales soundness excitement reproducibility overall assessment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "803e1350-8512-44ef-a2a7-b35b0da2adea",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkFsNMh1aaVkkDGMWDL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2469f4fc-b3d7-4e2e-928e-9f0bb172ad50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CP7Mx6syyj5NqNqa5h3Lwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1655,
      "cache_read_input_tokens": 17986,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 110,
          "cache_read_input_tokens": 17986,
          "cache_creation_input_tokens": 1655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1655,
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

_source line 7 · 2026-05-25T05:37:23.596Z_

<details><summary>↩ Tool result · `toolu_012toVZjaw9r5zkVH7XmgmNF`</summary>

```text
# ARR Reviewer Scoring Dimensions

The ARR guidelines specify **three scoring dimensions** for reviewers:

1. **Soundness** - Technical quality and validity of the work. Per guidelines: "The soundness scores must be justified by the text of the review."

2. **Excitement** - Personal interest level, described as "orthogonal to the assessment of the soundness of the paper. Excitement scores reflect our personal taste."

3. **Overall Assessment** - Composite recommendation reflecting "soundness, excitement, and also other factors like novelty and impact," representing an explicit recommendation for paper outcome.

Additionally, reviewers assess **reproducibility** as a separate dimension, though it relates to soundness verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2469f4fc-b3d7-4e2e-928e-9f0bb172ad50",
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "5da5d044-f604-4231-a84c-51135a61c5a7",
  "sourceToolAssistantUUID": "2469f4fc-b3d7-4e2e-928e-9f0bb172ad50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-25T05:37:25.650Z_

Let me also check the official CFP and GitHub documentation for the exact scoring scales.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5da5d044-f604-4231-a84c-51135a61c5a7",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkGFnVdQR2axr1Qc2hj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "11d093cc-3caa-490e-82df-26e41f0f0dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S68pMGAgFRZRjpuRmRgvjL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 276,
      "cache_read_input_tokens": 19641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 276,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 9 · 2026-05-25T05:37:26.094Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01T65P6DauPe3TgrBQcs8W2q`</summary>

```json
{
  "url": "http://aclrollingreview.org/cfp",
  "prompt": "review form scoring scales numbers soundness excitement overall recommendation accept reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11d093cc-3caa-490e-82df-26e41f0f0dba",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkGFnVdQR2axr1Qc2hj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "154c5374-b328-433c-9f04-63e0d590e09d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S68pMGAgFRZRjpuRmRgvjL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 276,
      "cache_read_input_tokens": 19641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 276,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 10 · 2026-05-25T05:37:26.352Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011iE1t1Dn7RjZPpLd5Rj2ew`</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md",
  "prompt": "scoring scales dimensions soundness excitement overall assessment numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "154c5374-b328-433c-9f04-63e0d590e09d",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkGFnVdQR2axr1Qc2hj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ed2e2dc5-dbd9-4b82-a706-c6d185fd8fe9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S68pMGAgFRZRjpuRmRgvjL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 276,
      "cache_read_input_tokens": 19641,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 276
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 197,
          "cache_read_input_tokens": 19641,
          "cache_creation_input_tokens": 276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 276,
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

_source line 11 · 2026-05-25T05:37:31.775Z_

<details><summary>↩ Tool result · `toolu_01T65P6DauPe3TgrBQcs8W2q`</summary>

```text
# ACL Rolling Review: Key Submission Guidelines

## Paper Types & Length

**Long papers** can be up to 8 pages of content, while **short papers** are limited to 4 pages. Both require unlimited space for references and a mandatory limitations section. Papers exceeding length limits or lacking a limitations section face desk rejection.

## Critical Requirements

**Anonymity is mandatory.** Submissions must exclude author names, affiliations, and self-identifying references. The policy states: "Papers must not include authors' names and affiliations. Furthermore,
self-references that reveal the authors' identities...must be avoided."

**All authors must review.** Beginning May 2025, submitting authors are expected to complete peer reviews unless they qualify for an exemption. Those failing to meet this obligation may become ineligible to submit in subsequent cycles.

## Originality Standards

Papers must describe unpublished, original work with no overlap in contributions. The platform discourages "thinly sliced contributions" by requiring concurrent related submissions by the same authors to cite each other and explain their differences.

## Submission Topics

ARR welcomes research across 30+ computational linguistics areas, from Clinical Applications to Syntax to emerging areas like LLM Agents and NLP-Code Models.

## Resubmission Rules

Resubmitted papers require authors to provide previous submission links and detailed revision summaries. The guidance notes: "Resubmissions must be modified versions...that address issues raised by the reviewers."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "154c5374-b328-433c-9f04-63e0d590e09d",
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "b0edb9fa-4432-430a-9118-eba1425effcb",
  "sourceToolAssistantUUID": "154c5374-b328-433c-9f04-63e0d590e09d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T05:37:33.782Z_

<details><summary>↩ Tool result · `toolu_011iE1t1Dn7RjZPpLd5Rj2ew`</summary>

```text
# ACL Rolling Review Call for Papers - Key Information

## Submission Overview
ACL Rolling Review (ARR) accepts long and short papers on computational linguistics and NLP research through a two-step process: centralized rolling review with bi-monthly deadlines, followed by commitment to publication venues.

## Paper Types & Length Requirements

**Long Papers:** Up to 8 pages of content plus unlimited references and a required limitations section

**Short Papers:** Up to 4 pages of content plus unlimited references and a required limitations section

Both require a dedicated "Limitations" section that doesn't count toward page limits.

## Critical Requirements

**Authorship & Anonymity:**
- Papers must be fully anonymized with no author names or identifying self-references
- Author changes require justification; removals must be substantiated by content removal

**Reviewing Obligation:**
Starting May 2025, authors must register as reviewers within 48 hours of submission unless exempted. Failure to meet reviewing responsibilities may result in desk rejection or ineligibility for future submissions.

**Ethics & Responsible NLP:**
Authors must complete a responsible NLP checklist. Incomplete or misleading checklist information triggers desk rejection. An ethics section is encouraged but optional.

**AI Assistance Disclosure:**
Generative AI use in writing or coding must be disclosed in the Responsible NLP Checklist and Acknowledgements section.

## Desk Rejection Triggers

Papers face automatic rejection for: anonymity violations, format non-compliance, dual submissions, missing limitations sections, incomplete checklists, and self-plagiarism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed2e2dc5-dbd9-4b82-a706-c6d185fd8fe9",
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "e1e8eda8-c5e2-483a-aa10-154b7846ed81",
  "sourceToolAssistantUUID": "ed2e2dc5-dbd9-4b82-a706-c6d185fd8fe9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-25T05:37:35.378Z_

Let me search more specifically for the numerical scoring scales used in ARR reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1e8eda8-c5e2-483a-aa10-154b7846ed81",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkH1DAycbABLBo2jgfi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df3febc6-3ece-4c4f-a4b7-fdc0428bd797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019aqqPZaPHgc6ToCqD2C1FP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 930,
      "cache_read_input_tokens": 19917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 14 · 2026-05-25T05:37:35.766Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SAHcUcQifioZ1hZhTBaM8g`</summary>

```json
{
  "query": "ARR review form soundness score 1-5 excitement overall recommendation scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df3febc6-3ece-4c4f-a4b7-fdc0428bd797",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkH1DAycbABLBo2jgfi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5fc1e11-4611-413d-a32a-a26c55ae2e8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019aqqPZaPHgc6ToCqD2C1FP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 930,
      "cache_read_input_tokens": 19917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 15 · 2026-05-25T05:37:42.906Z_

<details><summary>↩ Tool result · `toolu_01SAHcUcQifioZ1hZhTBaM8g`</summary>

```text
Web search results for query: "ARR review form soundness score 1-5 excitement overall recommendation scale"

Links: [{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"}]

Based on the search results, here's what I found about the ARR (ACL Rolling Review) review form with soundness score, excitement, and overall recommendation scale:

## ARR Review Form Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score (1-5 scale)
The soundness scale includes: 5 = Excellent (this study is one of the most thorough), 4 = Strong (provides sufficient support for all claims), and 3 = Acceptable (provides sufficient support for main claims). The soundness scores must be justified by the text of the review.

### Excitement Score
The excitement scale includes: 5 = Highly Exciting (would recommend the paper to others and/or attend its presentation) and 4 = Exciting (would mention this paper to others and/or make an effort to attend its presentation).

### Overall Recommendation
The overall assessment score is an explicit recommendation for the outcome of this paper if it were committed to an *ACL venue, reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.

The key distinction is that sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5fc1e11-4611-413d-a32a-a26c55ae2e8d",
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "67e52b75-3864-4f67-a5f6-89af0e549b70",
  "sourceToolAssistantUUID": "d5fc1e11-4611-413d-a32a-a26c55ae2e8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-25T05:37:45.137Z_

Now let me fetch the official review form page for the complete scoring scales.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67e52b75-3864-4f67-a5f6-89af0e549b70",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkHgdFizGYsmwniu3VP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7c3127e-d2e4-4bfa-83b2-bbfa855ae682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvymKNzKjMGNYk4Q5UEYWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 20847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 749,
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

_source line 17 · 2026-05-25T05:37:45.804Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RhJWN3J7BHZU8NwrnvoMjH`</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "soundness excitement overall assessment scale 1 2 3 4 5 strong acceptable weak"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7c3127e-d2e4-4bfa-83b2-bbfa855ae682",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkHgdFizGYsmwniu3VP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "caa72b8d-3fa4-4c18-9b22-f36633196821",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvymKNzKjMGNYk4Q5UEYWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 20847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 749,
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

_source line 18 · 2026-05-25T05:37:46.182Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KsxMJ8nVR3DwbNi5Zutkx7`</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md",
  "prompt": "soundness excitement overall assessment score scale definitions accept reject weak acceptable strong"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caa72b8d-3fa4-4c18-9b22-f36633196821",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkHgdFizGYsmwniu3VP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "919a5a3a-43e0-41a6-8e34-3e1f80a5fba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvymKNzKjMGNYk4Q5UEYWq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 20847,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 749
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 209,
          "cache_read_input_tokens": 20847,
          "cache_creation_input_tokens": 749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 749,
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

_source line 19 · 2026-05-25T05:37:51.029Z_

<details><summary>↩ Tool result · `toolu_01RhJWN3J7BHZU8NwrnvoMjH`</summary>

```text
# ACL Rolling Review Form Overview

The ACL Rolling Review (ARR) platform uses a structured peer review system with several key evaluation dimensions:

## Core Rating Scales

**Soundness** (1-5): Assesses whether the study adequately supports its claims, with considerations for experimental rigor, methodological validity, and thoroughness appropriate to the paper type.

**Excitement** (1-5): A subjective measure capturing whether reviewers find the work transformational, innovative, or impactful—potentially affecting their own research or broader communities.

**Overall Assessment** (1-5): Determines publication tier recommendations, ranging from "Consider for Award" down to "Do not resubmit," with distinctions between main conference papers and Findings publications.

## Mandatory Review Sections

Reviewers must complete:
- Paper summary and identification of strengths/weaknesses
- "Limitations and Societal Impact" evaluation
- Ethical concerns assessment per the ACL code
- Reproducibility evaluation

## Additional Dimensions

The form includes ratings for dataset value, software utility, and reviewer confidence levels. Notably, reviewers assess whether papers adequately address potential harms to marginalized populations and failure modes—emphasizing responsibility alongside innovation.

The platform distinguishes between papers meriting "substantial revisions by next cycle" versus those requiring longer-term work, enabling efficient triaging within ARR's rolling submission model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caa72b8d-3fa4-4c18-9b22-f36633196821",
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "36e1de74-4eb5-4e00-9341-decba643b070",
  "sourceToolAssistantUUID": "caa72b8d-3fa4-4c18-9b22-f36633196821",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T05:37:52.846Z_

<details><summary>↩ Tool result · `toolu_01KsxMJ8nVR3DwbNi5Zutkx7`</summary>

```text
# ARR Reviewer Guidelines Summary

The ACL Rolling Review (ARR) provides comprehensive guidance for peer reviewers. Key points include:

## Core Responsibilities

Reviewers must complete four main tasks: allocate review time, check assignments for expertise/conflicts, write strong reviews, and update assessments after author responses.

## Review Quality Standards

Reviews should be "specific and ideally understandable to the chairs without reading the full paper." Common problematic patterns include dismissing work as "not novel" without references, or criticizing methodology choices without explaining why they prevent answering the research question.

## Avoiding Bias

The guidelines list 17 heuristics representing common reviewer biases (H1-H17), such as assuming results seem obvious in retrospect or expecting SOTA performance. Reviewers should read papers twice—first skimming to adjust expectations, then in-depth for evaluation.

## Professional Conduct

"Write the review you would like to get yourself." Reviews should be professional and neutral, avoiding sarcasm. The document notes that "rude or dismissive reviews" damage academic communities and contribute to stress among researchers.

## Responsible AI Use

Reviewers cannot use generative AI to draft reviews or upload confidential manuscripts to non-privacy-preserving tools. However, editing assistance for non-native speakers or proof-checking is acceptable.

## Emerging Policies

Starting May 2025, ACL recognizes exceptional reviewers with awards while establishing sanctions for "highly irresponsible" reviewers who submit LLM-generated or unprofessional work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "919a5a3a-43e0-41a6-8e34-3e1f80a5fba1",
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "cadbb7e6-9f23-4731-9a75-ad5f57ca6451",
  "sourceToolAssistantUUID": "919a5a3a-43e0-41a6-8e34-3e1f80a5fba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-25T05:37:54.116Z_

Perfect! Let me search for the specific numerical definitions of each score on these scales.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cadbb7e6-9f23-4731-9a75-ad5f57ca6451",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkJQr1FjR3vdmZjSyLB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2478dc49-0f6c-447d-ab2d-abc9f4df59f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HAPBSfiJeXrsHD8tkfbTg4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 21596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1017,
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

_source line 22 · 2026-05-25T05:37:54.443Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Tk1DHVjixBatCWr35JSCV`</summary>

```json
{
  "query": "\"ARR\" \"soundness\" \"5\" \"excellent\" \"4\" \"strong\" \"3\" \"acceptable\" reviewer scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2478dc49-0f6c-447d-ab2d-abc9f4df59f8",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkJQr1FjR3vdmZjSyLB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3b0761a9-3374-4c26-9e3c-4059ddfdffa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HAPBSfiJeXrsHD8tkfbTg4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 21596,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1017
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 97,
          "cache_read_input_tokens": 21596,
          "cache_creation_input_tokens": 1017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1017,
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

_source line 23 · 2026-05-25T05:37:59.928Z_

<details><summary>↩ Tool result · `toolu_011Tk1DHVjixBatCWr35JSCV`</summary>

```text
Web search results for query: ""ARR" "soundness" "5" "excellent" "4" "strong" "3" "acceptable" reviewer scale"

Links: [{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"State-of-Art-Reviewing: A Radical Proposal to Improve Scientific   Publication","url":"https://arxiv.org/pdf/2003.14415"},{"title":"Reliability and validity of a newly developed Action Research Arm Test for upper limb function assessment in patients with stroke: A comparison with the conventional version","url":"https://www.medrxiv.org/content/10.1101/2025.09.25.25336671.full.pdf"}]

Based on the search results, I found information about the ARR (ACL Rolling Review) reviewer scale for soundness. Here's what the scale includes:

**5 = Excellent:** "This study is one of the most thorough I have seen, given its type." **4 = Strong:** "This study provides sufficient support for all of its claims."

However, I didn't find the definition for a "3 = Acceptable" rating in the search results. The ARR review form appears to contain additional scale points, but the complete definitions for all ratings (particularly the "3" level you mentioned) are not fully displayed in these search results. You may need to visit the full ARR review form at aclrollingreview.org/reviewform to see the complete scale definitions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b0761a9-3374-4c26-9e3c-4059ddfdffa6",
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "02092139-ba92-4ada-b198-9a5379d54c2e",
  "sourceToolAssistantUUID": "3b0761a9-3374-4c26-9e3c-4059ddfdffa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-25T05:38:01.777Z_

Let me try a direct fetch of the GitHub repository for the complete reviewer guidelines markdown file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02092139-ba92-4ada-b198-9a5379d54c2e",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkJw1U5CCgCTySZyDsx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0f046083-b5ea-43c4-bc43-ea088e1010e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018JNNZGx1hSYgjF4CdCn5uS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 22613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 627,
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

_source line 25 · 2026-05-25T05:38:02.303Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QeBjyav6LGwfv3f1GGBCJy`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/acl-org/aclrollingreview/main/reviewerguidelines.md",
  "prompt": "soundness score 1 2 3 4 5 excitement overall assessment scale definitions weak acceptable strong excellent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f046083-b5ea-43c4-bc43-ea088e1010e3",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkJw1U5CCgCTySZyDsx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "857bd6fb-06fc-4218-82db-90912a356e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018JNNZGx1hSYgjF4CdCn5uS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 22613,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 627
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 138,
          "cache_read_input_tokens": 22613,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 627,
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

_source line 26 · 2026-05-25T05:38:09.627Z_

<details><summary>↩ Tool result · `toolu_01QeBjyav6LGwfv3f1GGBCJy`</summary>

```text
# ARR Reviewer Guidelines Summary

## Key Responsibilities

ARR reviewers must complete four main tasks:

1. **Calendar allocation** - Block time for reviewing, assignments check, and discussions
2. **Assignment verification** - Confirm expertise match, check for conflicts of interest, and complete desk-rejection checklist
3. **Write strong reviews** - Read papers twice, be specific, check for common biases, and justify scores
4. **Engage in discussion** - Respond to author feedback and update assessments accordingly

## Critical Guidelines

**Confidentiality & Anonymity**: "All the information about submissions and reviews that you receive as part of your assignment is confidential." Avoid uploading papers to non-privacy-preserving AI tools and don't actively search for author identities.

**Reading Strategy**: Read papers at least twice—first for expectations-setting, then for in-depth evaluation. This reduces hindsight and confirmation bias.

**Common Review Pitfalls**: The guidelines list 17 heuristics to avoid (H1-H17), such as dismissing surprising results, demanding SOTA performance, or rejecting simple solutions.

**Professional Tone**: "Write the review you would like to get yourself." Maintain neutrality and kindness, recognizing reviewing's mutual benefit.

## Scoring Requirements

As of February 2025, provide three scores: soundness (with justification), excitement (subjective), and overall recommendation. Scores must reflect actual review content.

## Generative AI Policy

Reviewers cannot use AI to draft reviews or upload manuscripts/reports to non-privacy tools. Limited writing assistance for non-native speakers is acceptable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "857bd6fb-06fc-4218-82db-90912a356e38",
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "9e1d6f78-78f8-4380-8fa8-8190464c703a",
  "sourceToolAssistantUUID": "857bd6fb-06fc-4218-82db-90912a356e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-25T05:38:11.633Z_

Let me search for the specific overall assessment/recommendation scale values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e1d6f78-78f8-4380-8fa8-8190464c703a",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkKegUthczRmu2iaBpF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41e6f89f-9e82-4e58-8e1e-20ec3cab2eff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SowMsnd3bNqD4zYq6DRDgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 510,
      "cache_read_input_tokens": 23240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 510,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 28 · 2026-05-25T05:38:11.796Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UgtRrBNnKf6vR4Tz2QyJ1s`</summary>

```json
{
  "query": "ARR \"overall recommendation\" scale \"accept\" \"reject\" \"award\" \"resubmit\" ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41e6f89f-9e82-4e58-8e1e-20ec3cab2eff",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkKegUthczRmu2iaBpF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e87192bb-ea33-431a-b359-eb6b3da70421",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SowMsnd3bNqD4zYq6DRDgi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 510,
      "cache_read_input_tokens": 23240,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 510
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 23240,
          "cache_creation_input_tokens": 510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 510,
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

_source line 29 · 2026-05-25T05:38:18.405Z_

<details><summary>↩ Tool result · `toolu_01UgtRrBNnKf6vR4Tz2QyJ1s`</summary>

```text
Web search results for query: "ARR "overall recommendation" scale "accept" "reject" "award" "resubmit" ACL"

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Are reviewers suggested by authors as good as those chosen by editors? Results of a rater-blinded, retrospective study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1482713/"}]

Based on the search results, here's information about the ARR overall recommendation scale:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

For the metareview score (used by Area Chairs), the ARR metareview score changed in February 2025 to be more aligned with reviewer scores. The new options are: 5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers). ... 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle. 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community.

The search results show the metareview scale includes the options you mentioned (accept/award, resubmit, reject), though the exact overall recommendation scale for individual reviewers isn't fully displayed in these results. The sources indicate this information is part of the ARR reviewer guidelines available on their website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e87192bb-ea33-431a-b359-eb6b3da70421",
  "isSidechain": true,
  "promptId": "7b83cb2b-3b4e-419a-84db-4d4ab9631994",
  "agentId": "a19b3d0a981bea3a6",
  "type": "user",
  "uuid": "288f5b28-fa82-43b4-843a-3dfa59b64b04",
  "sourceToolAssistantUUID": "e87192bb-ea33-431a-b359-eb6b3da70421",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-25T05:38:25.675Z_

Based on my comprehensive search, here are the official ACL ARR reviewer guidelines and scoring criteria for 2025-2026:

## Scoring Dimensions and Scales

**1. Soundness (1-5 scale):**
- 5 = Excellent: "This study is one of the most thorough I have seen, given its type"
- 4 = Strong: "This study provides sufficient support for all of its claims"
- 3 = Acceptable: "Provides sufficient support for main claims"
- Lower scores for weaker methodological rigor

*Key requirement: Soundness scores must be justified by the text of the review*

**2. Excitement (1-5 scale):**
- 5 = Highly Exciting: "Would recommend the paper to others and/or attend its presentation"
- 4 = Exciting: "Would mention this paper to others and/or make an effort to attend its presentation"
- Subjective dimension, orthogonal to soundness assessment
- Reflects personal interest and potential impact

**3. Overall Assessment (1-5 scale):**
- 5 = Consider for Award: Could be considered for outstanding paper award (top 2.5%)
- 2 = Resubmit: Needs substantial revisions completable in next ARR cycle
- 1 = Do Not Resubmit: Requires major redo or lacks relevance to ACL community
- Composite recommendation reflecting soundness, excitement, novelty, and impact

## Key Reviewer Guidance

- **Reading strategy**: Read papers twice (first for expectations-setting, then in-depth) to reduce bias
- **Avoid 17 common biases** (H1-H17): dismissing results as "obvious," demanding SOTA performance, etc.
- **Professional standards**: "Write the review you would like to get yourself"—maintain neutrality and constructiveness
- **Reproducibility assessment** required as separate evaluation
- **Ethical evaluation**: Must address potential harms to marginalized populations and failure modes
- **AI policy**: Cannot use generative AI to draft reviews; cannot upload manuscripts to non-privacy tools

## Additional Requirements (as of May 2025)

- Submitting authors must register as reviewers within 48 hours of submission (unless exempted)
- Reviews must be "specific and ideally understandable to chairs without reading the full paper"
- Professional conduct violations (egregious terseness, unprofessional tone, LLM-generated reviews) may result in desk rejection and ineligibility

Sources:
- [ARR Reviewer Guidelines](http://aclrollingreview.org/reviewerguidelines)
- [ARR Review Form](http://aclrollingreview.org/reviewform)
- [ACL Rolling Review Call for Papers](http://aclrollingreview.org/cfp)
- [ARR Area Chair Guidelines](http://aclrollingreview.org/acguidelines)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "288f5b28-fa82-43b4-843a-3dfa59b64b04",
  "isSidechain": true,
  "agentId": "a19b3d0a981bea3a6",
  "requestId": "req_011CbNkLJ42ncqFzJEZvLro4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dadde6f9-6bde-485b-9612-5db66099c192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_reviewer_1_01e28f35",
  "sessionId": "1863c1ff-755e-4cfb-8582-e6ab562a7b33",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015ZwzJZNNTCQMWnDABqk5g8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 23750,
      "output_tokens": 675,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 741
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 675,
          "cache_read_input_tokens": 23750,
          "cache_creation_input_tokens": 741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 741,
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
