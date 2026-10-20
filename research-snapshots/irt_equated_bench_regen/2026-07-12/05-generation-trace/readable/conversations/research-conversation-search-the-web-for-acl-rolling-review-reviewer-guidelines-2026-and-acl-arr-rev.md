# Research conversation: Search the web for "ACL Rolling Review reviewer guidelines 2026" and "ACL ARR review form criteria dimensions" to find t

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad1cdd09de84e8648.jsonl`
- **Structured JSON:** [`08cacf9c60d888971fe2.json`](../../sessions/08/08cacf9c60d888971fe2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-22T16:23:18.807Z_

Search the web for "ACL Rolling Review reviewer guidelines 2026" and "ACL ARR review form criteria dimensions" to find the official review form dimensions and scoring criteria. I need the exact dimensions (like soundness, excitement, reproducibility, etc.) and their scoring scales. Use WebSearch and WebFetch tools to get this information. Report the complete review form structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a05ecaad-fc57-44e5-93b1-947bc3c254e6",
  "agentId": "ad1cdd09de84e8648",
  "type": "user",
  "uuid": "6952e943-2f5b-4650-bca6-a13478c90b2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T16:23:20.354Z_

I'll search for the ACL Rolling Review guidelines and review form criteria for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6952e943-2f5b-4650-bca6-a13478c90b2f",
  "isSidechain": true,
  "agentId": "ad1cdd09de84e8648",
  "requestId": "req_011CbHv6Kd3MBtjv7YMAR8Rt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf9e5546-685e-4df5-9ebe-f03bf5b3904a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Es3Cs4k8BFUDKiXzv9xTBj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17968,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17968,
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

_source line 3 · 2026-05-22T16:23:20.531Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BhLttpQyxc5Y9bS4ABcUvf`</summary>

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
  "parentUuid": "bf9e5546-685e-4df5-9ebe-f03bf5b3904a",
  "isSidechain": true,
  "agentId": "ad1cdd09de84e8648",
  "requestId": "req_011CbHv6Kd3MBtjv7YMAR8Rt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "66ca3a3f-ed72-4736-b6a7-1399b391fb7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Es3Cs4k8BFUDKiXzv9xTBj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17968,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17968,
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

_source line 4 · 2026-05-22T16:23:20.624Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NLYb32ZgtjmFECcJRjeBu8`</summary>

```json
{
  "query": "ACL ARR review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66ca3a3f-ed72-4736-b6a7-1399b391fb7a",
  "isSidechain": true,
  "agentId": "ad1cdd09de84e8648",
  "requestId": "req_011CbHv6Kd3MBtjv7YMAR8Rt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a3447467-6492-4b2c-83c0-9e4f6167a71b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Es3Cs4k8BFUDKiXzv9xTBj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17968,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17968,
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

### Tool result

_source line 5 · 2026-05-22T16:23:27.147Z_

<details><summary>↩ Tool result · `toolu_01NLYb32ZgtjmFECcJRjeBu8`</summary>

```text
Web search results for query: "ACL ARR review form criteria dimensions"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results about the ACL Rolling Review (ARR) review form, here's information about the criteria and dimensions:

## Review Criteria

For Findings papers, the main criteria are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

## Overall Assessment Dimensions

The review form includes a rating scale with the following dimensions:

- 5 = Consider for Award: A paper that could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)
- 2 = Resubmit next cycle: A paper that needs substantial revisions that can be completed by the next ARR cycle
- 1.5 = Resubmit after next cycle: A paper that needs substantial revisions that cannot be completed by the next ARR cycle
- 1 = Do not resubmit: A paper that has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language)

## Reviewer Guidelines

The review forms contain the question 'Knowledge of/educated guess at author identity' to help identify potential bias issues in the reviews.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3447467-6492-4b2c-83c0-9e4f6167a71b",
  "isSidechain": true,
  "promptId": "a05ecaad-fc57-44e5-93b1-947bc3c254e6",
  "agentId": "ad1cdd09de84e8648",
  "type": "user",
  "uuid": "589775fa-e3a5-4776-88a5-4a13ec0118f0",
  "sourceToolAssistantUUID": "a3447467-6492-4b2c-83c0-9e4f6167a71b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T16:23:31.282Z_

<details><summary>↩ Tool result · `toolu_01BhLttpQyxc5Y9bS4ABcUvf`</summary>

```text
Web search results for query: "ACL Rolling Review reviewer guidelines 2026"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's what I found about ACL Rolling Review (ARR) reviewer guidelines for 2026:

## Key Reviewer Guidelines for 2026

ARR has developed detailed guidelines and suggestions for each step of the review process, including a list of common problems in both reviews and NLP papers to watch out for.

### Anonymity and Author Identity

Reviewers for *ACL conferences and TACL should be instructed not to actively try to discover the identity of the authors and not to let any suspicion or knowledge of author identity affect their judgment of the paper. This should not prevent them from searching for related work, but they should take special care and postpone such searches until after they have read the paper completely and formed an initial impression of it.

If a reviewer nevertheless uncovers the identity of the authors (or believes they can identify the authors for other reasons), they should inform the area chair or action editor (but not other reviewers) so that this information can be taken into account when making the final acceptance decision.

### Evaluation Standards

Reviewers should treat the papers as submissions to ACL when evaluating them. ARR reviewers are instructed to write a review as if the paper were being considered for the ACL conference. Thus low scores may indicate the submission is not a good fit for ACL, even if it may be a good fit for other/more specialized venues.

### Awards and Recognition

Starting from May 2025, ACL introduces the awards policy for reviewers & chairs. In short, the area chairs or senior area chairs may nominate the great reviewers, and senior chairs may also nominate area chairs who perform great service. The nominees will then receive more recognition during the ACL conferences (public lists on conference webistes, special stickers for conference badges, more visibility in the program).

### Policy on Highly Irresponsible Reviewers

Starting in May 2025, ARR adopts a new policy on the 'highly irresponsible' (meta-)reviewers. The program chairs and ARR EiCs will consider the egregious cases reported by chairs (on their own judgement or based on author reports), including the cases of extremely terse reviews, unprofessional tone, and LLM-generated reviews. The 'highly irresponsible' reviewers or chairs may have their work desk-rejected from the current cycle, and ineligible for resubmission or commitment during the following ARR cycle.

The full reviewer guidelines are available on the ARR website at http://aclrollingreview.org/reviewerguidelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66ca3a3f-ed72-4736-b6a7-1399b391fb7a",
  "isSidechain": true,
  "promptId": "a05ecaad-fc57-44e5-93b1-947bc3c254e6",
  "agentId": "ad1cdd09de84e8648",
  "type": "user",
  "uuid": "ade8a340-47b3-402f-895f-c1ea4ef9a271",
  "sourceToolAssistantUUID": "66ca3a3f-ed72-4736-b6a7-1399b391fb7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-22T16:23:33.033Z_

Now let me fetch the detailed review form from the official ARR page to get the complete structure with all dimensions and scoring scales.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ade8a340-47b3-402f-895f-c1ea4ef9a271",
  "isSidechain": true,
  "agentId": "ad1cdd09de84e8648",
  "requestId": "req_011CbHv7EvJ3ymRtrVBMKyi3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1c3bae56-b1b1-45df-8238-5e6618ea8c6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GRYYn5QGj9gqQYFf1JfdT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 682,
      "cache_creation_input_tokens": 2010,
      "cache_read_input_tokens": 17968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2010,
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

_source line 8 · 2026-05-22T16:23:33.745Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HnZAkiWcUZVN2RSt1HbLFb`</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "What are all the review form dimensions, criteria, and scoring scales? List each dimension with its scale options."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c3bae56-b1b1-45df-8238-5e6618ea8c6a",
  "isSidechain": true,
  "agentId": "ad1cdd09de84e8648",
  "requestId": "req_011CbHv7EvJ3ymRtrVBMKyi3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5a28f44a-4fda-4b47-bbe8-aec0702a1f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GRYYn5QGj9gqQYFf1JfdT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 682,
      "cache_creation_input_tokens": 2010,
      "cache_read_input_tokens": 17968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2010,
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

_source line 9 · 2026-05-22T16:23:33.888Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HiSUkfedUHctvzCRoVx2aB`</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "What are the specific review criteria and scoring dimensions reviewers should use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a28f44a-4fda-4b47-bbe8-aec0702a1f6b",
  "isSidechain": true,
  "agentId": "ad1cdd09de84e8648",
  "requestId": "req_011CbHv7EvJ3ymRtrVBMKyi3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "198a6cf1-9ba2-4ea6-ae15-c964cc084475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GRYYn5QGj9gqQYFf1JfdT2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 682,
      "cache_creation_input_tokens": 2010,
      "cache_read_input_tokens": 17968,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2010
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 682,
          "output_tokens": 209,
          "cache_read_input_tokens": 17968,
          "cache_creation_input_tokens": 2010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2010,
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

_source line 10 · 2026-05-22T16:23:39.225Z_

<details><summary>↩ Tool result · `toolu_01HiSUkfedUHctvzCRoVx2aB`</summary>

```text
# Review Scoring Dimensions for ARR

According to the ARR Reviewer Guidelines, reviewers should provide three distinct scores:

1. **Soundness**: Evaluates technical quality and validity. As stated, "The _soundness_ scores must be justified by the text of the review." Low soundness ratings require explicit explanation of identified flaws.

2. **Excitement**: Reflects personal interest in the work, orthogonal to soundness assessment. The guidelines note this is "more subjective and should be reflected in a separate _excitement_ score."

3. **Overall Assessment**: A composite recommendation incorporating soundness, excitement, novelty, and potential impact. The guidelines specify that "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

## Key Principle

Scores must align with review content. The guidelines emphasize: "If you give a low _Soundness_ score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it."

This three-dimensional approach acknowledges that technically sound work may not personally excite every reviewer, yet can still merit publication based on its contributions and broader significance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "198a6cf1-9ba2-4ea6-ae15-c964cc084475",
  "isSidechain": true,
  "promptId": "a05ecaad-fc57-44e5-93b1-947bc3c254e6",
  "agentId": "ad1cdd09de84e8648",
  "type": "user",
  "uuid": "d30a22c6-771f-47cb-9690-8df96c75bc99",
  "sourceToolAssistantUUID": "198a6cf1-9ba2-4ea6-ae15-c964cc084475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T16:23:41.649Z_

<details><summary>↩ Tool result · `toolu_01HnZAkiWcUZVN2RSt1HbLFb`</summary>

```text
# ACL Rolling Review Form Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5 = Positive evaluation is correct; very careful read with familiarity of related work
- 4 = Quite sure; important points checked carefully
- 3 = Pretty sure; general area knowledge but details not carefully verified
- 2 = Can defend evaluation but likely missed some details or novelty assessment uncertain
- 1 = Outside expertise area or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- 5 = Excellent: "one of the most thorough" studies of its type
- 4 = Strong: sufficient support for claims; extra experiments optional
- 3 = Acceptable: main claims supported; minor points need extra detail
- 2 = Poor: main claims insufficiently supported; major technical problems
- 1 = Major Issues: insufficient depth or not relevant to ACL

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- 5 = Highly Exciting: would recommend to others or attend presentation
- 4 = Exciting: would mention to others or make effort to attend
- 3 = Interesting: might mention points or attend if time permits
- 2 = Potentially Interesting: does not resonate personally but might with others
- 1 = Not Exciting: lacks relevance to computational linguistics

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- 5 = Consider for Award
- 4.5 = Borderline Award
- 4 = Conference
- 3.5 = Borderline Conference
- 3 = Findings
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5 = Results easily reproducible
- 4 = Mostly reproducible; minor variations possible
- 3 = Reproducible with difficulty; parameters underspecified
- 2 = Hard to reproduce; unavailable data or insufficient details
- 1 = Not reproducible

## 6. **Datasets Value**
Scale: 1-5
- 5 = Enabling: affects research project choices
- 4 = Useful: recommended for ongoing work
- 3 = Potentially useful: might assist some research
- 2 = Documentary: useful for replication only
- 1 = No usable datasets

## 7. **Software Value**
Scale: 1-5
- 5 = Enabling: affects research project choices
- 4 = Useful: recommended for ongoing work
- 3 = Potentially useful: might assist some research
- 2 = Documentary: useful for replication only
- 1 = No usable software

## 8. **Author Identity Knowledge**
Scale: 1-5
- 5 = Know/guess author name from double-blind violation
- 4 = Know/guess from preprint or allowed workshop paper
- 3 = Know/guess from submission contents
- 2 = Know/guess from social media or informal communication
- 1 = No educated guess about identity
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a28f44a-4fda-4b47-bbe8-aec0702a1f6b",
  "isSidechain": true,
  "promptId": "a05ecaad-fc57-44e5-93b1-947bc3c254e6",
  "agentId": "ad1cdd09de84e8648",
  "type": "user",
  "uuid": "157fe256-c86d-4553-ac9c-195e9c092efc",
  "sourceToolAssistantUUID": "5a28f44a-4fda-4b47-bbe8-aec0702a1f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-22T16:23:50.606Z_

Perfect! I've gathered the complete ACL Rolling Review (ARR) review form structure. Here's the comprehensive report:

## Complete ACL ARR Review Form Structure (2026)

The official ACL Rolling Review uses a standardized form with **8 evaluation dimensions**, each with a 1-5 scale (with half-point increments for most dimensions):

### 1. **Soundness** (1-5, half-point increments)
Technical quality and validity of the work:
- 5 = Excellent: one of the most thorough studies of its type
- 4 = Strong: sufficient support for claims; extra experiments optional
- 3 = Acceptable: main claims supported; minor points need extra detail
- 2 = Poor: main claims insufficiently supported; major technical problems
- 1 = Major Issues: insufficient depth or not relevant to ACL

### 2. **Excitement** (1-5, half-point increments)
Personal interest and significance (subjective dimension):
- 5 = Highly Exciting: would recommend to others or attend presentation
- 4 = Exciting: would mention to others or make effort to attend
- 3 = Interesting: might mention points or attend if time permits
- 2 = Potentially Interesting: does not resonate personally but might with others
- 1 = Not Exciting: lacks relevance to computational linguistics

### 3. **Overall Assessment** (1-5, half-point increments)
Composite recommendation incorporating soundness, excitement, novelty, and impact:
- 5 = Consider for Award (top 2.5% papers)
- 4.5 = Borderline Award
- 4 = Conference
- 3.5 = Borderline Conference
- 3 = Findings
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

### 4. **Reproducibility** (1-5)
Ability to reproduce the results:
- 5 = Results easily reproducible
- 4 = Mostly reproducible; minor variations possible
- 3 = Reproducible with difficulty; parameters underspecified
- 2 = Hard to reproduce; unavailable data or insufficient details
- 1 = Not reproducible

### 5. **Reviewer Confidence** (1-5)
Reviewer's confidence in their evaluation:
- 5 = Positive evaluation is correct; very careful read with familiarity of related work
- 4 = Quite sure; important points checked carefully
- 3 = Pretty sure; general area knowledge but details not carefully verified
- 2 = Can defend evaluation but likely missed some details or novelty assessment uncertain
- 1 = Outside expertise area or paper very difficult to understand

### 6. **Datasets Value** (1-5)
Value and usability of any datasets contributed:
- 5 = Enabling: affects research project choices
- 4 = Useful: recommended for ongoing work
- 3 = Potentially useful: might assist some research
- 2 = Documentary: useful for replication only
- 1 = No usable datasets

### 7. **Software Value** (1-5)
Value and usability of any software/code contributed:
- 5 = Enabling: affects research project choices
- 4 = Useful: recommended for ongoing work
- 3 = Potentially useful: might assist some research
- 2 = Documentary: useful for replication only
- 1 = No usable software

### 8. **Author Identity Knowledge** (1-5)
Reviewer awareness of author identity (double-blind verification):
- 5 = Know/guess author name from double-blind violation
- 4 = Know/guess from preprint or allowed workshop paper
- 3 = Know/guess from submission contents
- 2 = Know/guess from social media or informal communication
- 1 = No educated guess about identity

### Key Review Principles

- **Alignment requirement**: Soundness scores must be justified by review text. Low soundness scores require explicit explanation of flaws.
- **Recommendation standards**: All papers recommended for Findings and main conferences must be sufficiently sound and reproducible.
- **Two-dimensional evaluation**: Soundness (technical quality) and Excitement (subjective interest) are evaluated separately, acknowledging that technically sound work may vary in personal appeal.

Sources:
- [Review Form – ACL Rolling Review](http://aclrollingreview.org/reviewform)
- [ARR Reviewer Guidelines – ACL Rolling Review](http://aclrollingreview.org/reviewerguidelines)
- [ACL Rolling Review – A peer review platform](http://aclrollingreview.org/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "157fe256-c86d-4553-ac9c-195e9c092efc",
  "isSidechain": true,
  "agentId": "ad1cdd09de84e8648",
  "requestId": "req_011CbHv81K23vmXEvJizht4a",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "da3d500d-a0a1-413a-86e6-12e51440fee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_reviewer_1_e2787213",
  "sessionId": "3c6fb625-54ad-4ecf-a766-8cfdadf74f6d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019SjFqKwxhsdexARoLpbLdb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 290,
      "cache_creation_input_tokens": 1718,
      "cache_read_input_tokens": 19978,
      "output_tokens": 1120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1718
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 290,
          "output_tokens": 1120,
          "cache_read_input_tokens": 19978,
          "cache_creation_input_tokens": 1718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1718,
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
