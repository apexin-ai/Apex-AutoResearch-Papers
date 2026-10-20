# Research conversation: Search the web for "ACL Rolling Review reviewer guidelines 2026" and "ACL ARR review form criteria dimensions". I need t

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aaa75bedad60d770e.jsonl`
- **Structured JSON:** [`6caa307a61d14924eb72.json`](../../sessions/6c/6caa307a61d14924eb72.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-20T15:00:59.390Z_

Search the web for "ACL Rolling Review reviewer guidelines 2026" and "ACL ARR review form criteria dimensions". I need the official scoring dimensions and criteria used in ACL ARR reviews for EMNLP 2026. Find the review form dimensions (e.g., soundness, excitement/novelty, reproducibility, etc.) and their scoring scales. Use WebSearch or WebFetch to find this information. Report back the complete list of official review dimensions and their scales.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5b7b2cf9-d286-45a1-ae39-28f9e3335858",
  "agentId": "aaa75bedad60d770e",
  "type": "user",
  "uuid": "d70cccc0-9877-46ad-b51b-54d01ff43262",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T15:01:00.896Z_

I'll search for the official ACL Rolling Review guidelines and scoring criteria for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d70cccc0-9877-46ad-b51b-54d01ff43262",
  "isSidechain": true,
  "agentId": "aaa75bedad60d770e",
  "requestId": "req_011CbE2CPYnUfd2YJA8mPnyG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bfbd1601-d0b4-42f4-abbb-925ee0f0f0c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FPWwtpR2aKVWid6TGSnKQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18339,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18339,
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

_source line 3 · 2026-05-20T15:01:01.001Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011aQwp5ZUGWj8k4V3KQtAx7`</summary>

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
  "parentUuid": "bfbd1601-d0b4-42f4-abbb-925ee0f0f0c7",
  "isSidechain": true,
  "agentId": "aaa75bedad60d770e",
  "requestId": "req_011CbE2CPYnUfd2YJA8mPnyG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a178f5d2-75fc-4edd-b6e2-f07f92c51491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FPWwtpR2aKVWid6TGSnKQz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18339,
      "cache_read_input_tokens": 0,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18339
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 121,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18339,
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

### Tool call

_source line 4 · 2026-05-20T15:01:01.050Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AN24cK6S96c22cNWFopcVy`</summary>

```json
{
  "query": "ACL ARR review form criteria dimensions scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a178f5d2-75fc-4edd-b6e2-f07f92c51491",
  "isSidechain": true,
  "agentId": "aaa75bedad60d770e",
  "requestId": "req_011CbE2CPYnUfd2YJA8mPnyG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bd48d7c6-3cd7-4887-8eaf-344002e34ac0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FPWwtpR2aKVWid6TGSnKQz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18339,
      "cache_read_input_tokens": 0,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18339
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 121,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18339,
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

_source line 5 · 2026-05-20T15:01:08.037Z_

<details><summary>↩ Tool result · `toolu_01AN24cK6S96c22cNWFopcVy`</summary>

```text
Web search results for query: "ACL ARR review form criteria dimensions scoring"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"}]

Based on the search results, here's what I found about the ACL ARR review form criteria, dimensions, and scoring:

## Review Form Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Criteria for Different Paper Types

For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## Overall Recommendation Score Levels

The scoring system for overall recommendations includes:

- 5 = Consider for Award: Papers that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)
- 2 = Resubmit next cycle: Papers needing substantial revisions that can be completed by the next ARR cycle
- 1.5 = Resubmit after next cycle: Papers needing substantial revisions that cannot be completed by the next ARR cycle
- 1 = Do not resubmit: Papers that have to be fully redone, or are not relevant to the *ACL community

The review form also addresses other important dimensions such as whether there is enough information in the paper for a reader to reproduce the main results or build upon the work, and includes evaluation of ethical considerations as well.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd48d7c6-3cd7-4887-8eaf-344002e34ac0",
  "isSidechain": true,
  "promptId": "5b7b2cf9-d286-45a1-ae39-28f9e3335858",
  "agentId": "aaa75bedad60d770e",
  "type": "user",
  "uuid": "0514003a-a7f0-4159-8aff-df86c5bdb92c",
  "sourceToolAssistantUUID": "bd48d7c6-3cd7-4887-8eaf-344002e34ac0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T15:01:11.778Z_

<details><summary>↩ Tool result · `toolu_011aQwp5ZUGWj8k4V3KQtAx7`</summary>

```text
Web search results for query: "ACL Rolling Review reviewer guidelines 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key ACL Rolling Review (ARR) reviewer guidelines for 2026:

## Author Anonymity and Double-Blind Review

To preserve the merits of double-blind review, reviewers for *ACL conferences and TACL should be instructed not to actively try to discover the identity of the authors and not to let any suspicion or knowledge of author identity affect their judgment of the paper. This should not prevent them from searching for related work, but they should take special care and postpone such searches until after they have read the paper completely and formed an initial impression of it. If a reviewer nevertheless uncovers the identity of the authors (or believes they can identify the authors for other reasons), they should inform the area chair or action editor (but not other reviewers) so that this information can be taken into account when making the final acceptance decision.

## Review Standards

You should treat the papers as submissions to ACL when evaluating them. ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference. Thus low scores may indicate the submission is not a good fit for ACL, even if it may be a good fit for other/more specialized venues.

## Reviewer Awards and Accountability

Starting from May 2025, ACL introduces the awards policy for reviewers & chairs. In short, the area chairs or senior area chairs may nominate the great reviewers, and senior chairs may also nominate area chairs who perform great service. The nominees will then receive more recognition during the ACL conferences (public lists on conference webistes, special stickers for conference badges, more visibility in the program).

## Highly Irresponsible Reviewers Policy

Starting in May 2025, ARR also adopts the new policy on the 'highly irresponsible' (meta-)reviewers. The program chairs and ARR EiCs will consider the egregious cases reported by chairs (on their own judgement or based on author reports), including the cases of extremely terse reviews, unprofessional tone, and LLM-generated reviews. The 'highly irresponsible' reviewers or chairs may have their work desk-rejected from the current cycle, and ineligible for resubmission or commitment during the following ARR cycle. For review cycles associated with ACL conferences, this means that the papers of such reviewers cannot be committed to the upcoming conference.

For the complete and most detailed guidelines, you can visit the official ARR reviewer guidelines page at aclrollingreview.org/reviewerguidelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a178f5d2-75fc-4edd-b6e2-f07f92c51491",
  "isSidechain": true,
  "promptId": "5b7b2cf9-d286-45a1-ae39-28f9e3335858",
  "agentId": "aaa75bedad60d770e",
  "type": "user",
  "uuid": "24acb461-43f7-4d8a-a832-0a1bf384749b",
  "sourceToolAssistantUUID": "a178f5d2-75fc-4edd-b6e2-f07f92c51491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-20T15:01:13.644Z_

Now let me fetch the official review form page to get the complete and precise scoring dimensions and scales.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24acb461-43f7-4d8a-a832-0a1bf384749b",
  "isSidechain": true,
  "agentId": "aaa75bedad60d770e",
  "requestId": "req_011CbE2DJFKVYcuZCdsCskkG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb068d0f-5cdb-46ae-ae83-7b0a1531713b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W7SGUmqtJ55P5BSXUoTXqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 661,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 18339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2030,
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

_source line 8 · 2026-05-20T15:01:14.081Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014RFwsFQpxprC8TJyzN2CR5`</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "What are the complete review dimensions, criteria, and their scoring scales?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb068d0f-5cdb-46ae-ae83-7b0a1531713b",
  "isSidechain": true,
  "agentId": "aaa75bedad60d770e",
  "requestId": "req_011CbE2DJFKVYcuZCdsCskkG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "356d8219-d666-4a63-b6ea-420d1647543d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W7SGUmqtJ55P5BSXUoTXqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 661,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 18339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2030,
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

_source line 9 · 2026-05-20T15:01:14.433Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015AZz8KyRYEcwzh147J93bU`</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "What are the official review dimensions and scoring criteria that reviewers should use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "356d8219-d666-4a63-b6ea-420d1647543d",
  "isSidechain": true,
  "agentId": "aaa75bedad60d770e",
  "requestId": "req_011CbE2DJFKVYcuZCdsCskkG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d0eb3beb-4a80-4481-8e32-39820c9e43eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W7SGUmqtJ55P5BSXUoTXqd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 661,
      "cache_creation_input_tokens": 2030,
      "cache_read_input_tokens": 18339,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 661,
          "output_tokens": 197,
          "cache_read_input_tokens": 18339,
          "cache_creation_input_tokens": 2030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2030,
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

_source line 10 · 2026-05-20T15:01:19.224Z_

<details><summary>↩ Tool result · `toolu_015AZz8KyRYEcwzh147J93bU`</summary>

```text
# Official Review Dimensions and Scoring Criteria

According to the ARR guidelines, reviewers are asked to provide **three scores**:

1. **Soundness**: "The _soundness_ scores must be justified by the text of the review."

2. **Excitement**: This reflects "our personal taste" regarding interest in the work, separate from technical quality assessments.

3. **Overall Recommendation**: An "explicit recommendation for the outcome of this paper, if it were committed to an \*ACL venue," combining soundness, excitement, novelty, and impact considerations.

The guidelines emphasize that soundness and reproducibility scores require explicit justification in the review text. A paper can be technically sound but receive lower excitement scores if personally uninteresting to the reviewer. Conversely, exciting work should still meet minimum soundness standards for acceptance consideration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0eb3beb-4a80-4481-8e32-39820c9e43eb",
  "isSidechain": true,
  "promptId": "5b7b2cf9-d286-45a1-ae39-28f9e3335858",
  "agentId": "aaa75bedad60d770e",
  "type": "user",
  "uuid": "11a7407c-ba9c-4566-a8b8-801ac95c92c6",
  "sourceToolAssistantUUID": "d0eb3beb-4a80-4481-8e32-39820c9e43eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T15:01:20.560Z_

<details><summary>↩ Tool result · `toolu_014RFwsFQpxprC8TJyzN2CR5`</summary>

```text
# ACL Rolling Review Form: Dimensions, Criteria, and Scales

## 1. Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4: Quite sure with unlikely but conceivable errors
- 3: Pretty sure but may have missed details
- 2: Willing to defend evaluation but likely missed some details
- 1: Outside expertise area or paper very difficult to understand

## 2. Soundness
**Scale: 1-5 (with half-point options)**
- 5: "Excellent: This study is one of the most thorough I have seen, given its type."
- 4: Strong support for claims; extra experiments optional
- 3: Acceptable; main claims supported with minor gaps
- 2: Poor; main claims lack sufficient support
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. Excitement
**Scale: 1-5 (with half-point options)**
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Exciting; would mention to others or attend presentation
- 3: Interesting; might mention points or attend if available
- 2: Potentially interesting to some community members
- 1: "Not Exciting: this paper does not resonate with me"

## 4. Overall Assessment
**Scale: 1-5 (with half-point options)**
- 5: Consider for award consideration
- 4: Conference acceptance recommended
- 3: Findings acceptance recommended
- 2: Needs substantial revision for next cycle
- 1: Do not resubmit or not relevant to ACL
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "356d8219-d666-4a63-b6ea-420d1647543d",
  "isSidechain": true,
  "promptId": "5b7b2cf9-d286-45a1-ae39-28f9e3335858",
  "agentId": "aaa75bedad60d770e",
  "type": "user",
  "uuid": "292bd5cf-fb32-4664-adcb-ec3ccf9fd3a5",
  "sourceToolAssistantUUID": "356d8219-d666-4a63-b6ea-420d1647543d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T15:01:24.652Z_

Perfect! I have found the official ACL ARR review dimensions and scoring scales. Here's the complete information:

## Official ACL ARR Review Dimensions and Scoring Scales (2026)

### 1. **Reviewer Confidence**
**Scale: 1-5**
- 5: Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work.
- 4: Quite sure with unlikely but conceivable errors
- 3: Pretty sure but may have missed details
- 2: Willing to defend evaluation but likely missed some details
- 1: Outside expertise area or paper very difficult to understand

### 2. **Soundness**
**Scale: 1-5 (with half-point options)**
- 5: Excellent - This study is one of the most thorough I have seen, given its type.
- 4: Strong support for claims; extra experiments optional
- 3: Acceptable - Main claims supported with minor gaps
- 2: Poor - Main claims lack sufficient support
- 1: Major Issues - This study is not yet sufficiently thorough to warrant publication

### 3. **Excitement**
**Scale: 1-5 (with half-point options)**
- 5: Highly Exciting - I would recommend this paper to others
- 4: Exciting - Would mention to others or attend presentation
- 3: Interesting - Might mention points or attend if available
- 2: Potentially interesting to some community members
- 1: Not Exciting - This paper does not resonate with me

### 4. **Overall Recommendation**
**Scale: 1-5 (with half-point options)**
- 5: Consider for award consideration (top 2.5% papers)
- 4: Conference acceptance recommended
- 3: Findings acceptance recommended
- 2: Needs substantial revision for next cycle
- 1: Do not resubmit or not relevant to ACL community

### Key Points:
- Reviewers provide **three main scores**: Soundness, Excitement, and Overall Recommendation
- Soundness and Excitement scores allow **half-point increments** (e.g., 3.5, 4.5)
- **Soundness scores must be justified** by the text of the review
- Excitement reflects personal taste separate from technical quality
- Overall Recommendation combines soundness, excitement, novelty, and impact

Sources:
- [Review Form – ACL Rolling Review](http://aclrollingreview.org/reviewform)
- [ARR Reviewer Guidelines – ACL Rolling Review](http://aclrollingreview.org/reviewerguidelines)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "292bd5cf-fb32-4664-adcb-ec3ccf9fd3a5",
  "isSidechain": true,
  "agentId": "aaa75bedad60d770e",
  "requestId": "req_011CbE2Dwj598EenU4e7WStY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7ce4879e-d207-4835-a74a-59e394b3ca31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "5993ae2c-0d21-4a0e-9280-bbb928b5a321",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EBDiRiHJSmsiVTGX6BEMzq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 213,
      "cache_creation_input_tokens": 1297,
      "cache_read_input_tokens": 20369,
      "output_tokens": 611,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 213,
          "output_tokens": 611,
          "cache_read_input_tokens": 20369,
          "cache_creation_input_tokens": 1297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1297,
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
