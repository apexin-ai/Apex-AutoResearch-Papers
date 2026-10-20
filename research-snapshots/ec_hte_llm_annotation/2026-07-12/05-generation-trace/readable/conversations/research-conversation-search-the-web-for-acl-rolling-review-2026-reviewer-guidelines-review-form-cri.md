# Research conversation: Search the web for "ACL Rolling Review 2026 reviewer guidelines review form criteria" and "ARR review form dimensions sc

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-afd5e907895a8b75a.jsonl`
- **Structured JSON:** [`2a7747d2e38d7b7902a7.json`](../../sessions/2a/2a7747d2e38d7b7902a7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-23T16:40:13.116Z_

Search the web for "ACL Rolling Review 2026 reviewer guidelines review form criteria" and "ARR review form dimensions scoring". I need the official review form dimensions (soundness, excitement, reproducibility, etc.) and their scoring scales. Also search for "EMNLP 2026 reviewer guidelines" and "ACL ARR review form 2025 2026". Report back the exact dimensions and scales used in the ARR review form.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "98ca2875-6cf2-4ad3-8c08-89c0d97fa292",
  "agentId": "afd5e907895a8b75a",
  "type": "user",
  "uuid": "3e1331ec-0a63-4209-a952-1b3c00ce63f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T16:40:14.550Z_

I'll search for the official ACL Rolling Review form dimensions and scoring criteria for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e1331ec-0a63-4209-a952-1b3c00ce63f0",
  "isSidechain": true,
  "agentId": "afd5e907895a8b75a",
  "requestId": "req_011CbKqC1Jp6F4MjZnwPfg7Z",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3c9e9160-1900-476a-a4b8-dd20bbfa00f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018LqM7Q1fxoHzj6K7TxMjp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17987,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17987,
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

_source line 3 · 2026-05-23T16:40:14.704Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ehg1KHf6eBbXJTWrUq7JXQ`</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c9e9160-1900-476a-a4b8-dd20bbfa00f7",
  "isSidechain": true,
  "agentId": "afd5e907895a8b75a",
  "requestId": "req_011CbKqC1Jp6F4MjZnwPfg7Z",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "70f04aa0-9d99-4464-9963-6c81b9a1693d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018LqM7Q1fxoHzj6K7TxMjp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17987,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17987,
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

_source line 4 · 2026-05-23T16:40:14.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HyYAR9KpqzMmJvQXnb9PX7`</summary>

```json
{
  "query": "ARR review form dimensions scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70f04aa0-9d99-4464-9963-6c81b9a1693d",
  "isSidechain": true,
  "agentId": "afd5e907895a8b75a",
  "requestId": "req_011CbKqC1Jp6F4MjZnwPfg7Z",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e324d60-0480-47a0-ae54-ca34d0f0fd74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018LqM7Q1fxoHzj6K7TxMjp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17987,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17987,
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

_source line 5 · 2026-05-23T16:40:14.971Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FsPS4xQNdvnxVXgbpAY2yc`</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e324d60-0480-47a0-ae54-ca34d0f0fd74",
  "isSidechain": true,
  "agentId": "afd5e907895a8b75a",
  "requestId": "req_011CbKqC1Jp6F4MjZnwPfg7Z",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01f989d8-cf02-42b4-b587-0be6d612b69d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018LqM7Q1fxoHzj6K7TxMjp9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17987,
      "cache_read_input_tokens": 0,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17987
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17987,
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

_source line 6 · 2026-05-23T16:40:14.977Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H2AyhocjQwbK4juEhzVt9A`</summary>

```json
{
  "query": "ACL ARR review form 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01f989d8-cf02-42b4-b587-0be6d612b69d",
  "isSidechain": true,
  "agentId": "afd5e907895a8b75a",
  "requestId": "req_011CbKqC1Jp6F4MjZnwPfg7Z",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ae671c3-8e99-4962-a629-9d4934b5b0ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018LqM7Q1fxoHzj6K7TxMjp9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17987,
      "cache_read_input_tokens": 0,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17987
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17987,
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

_source line 7 · 2026-05-23T16:40:21.812Z_

<details><summary>↩ Tool result · `toolu_01Ehg1KHf6eBbXJTWrUq7JXQ`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I've completed the web search for "ACL Rolling Review 2026 reviewer guidelines review form criteria". Here are the key findings:

## Reviewer Guidelines

The recommended workflow is to (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If you feel qualified to review some aspects but not others, please state in the review if you did not check major parts, such as proofs, as this information is helpful for the AC to understand what aspects were not reviewed.

Reviewers should check for academic conflicts of interest and recuse themselves if the submission looks very close to their own work about to be submitted.

## Review Form Criteria

Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-changing. For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## 2026 Policy on Irresponsible Reviews

Starting in May 2025, ARR adopted a new policy on 'highly irresponsible' (meta-)reviewers, where program chairs and ARR EiCs will consider egregious cases including extremely terse reviews, unprofessional tone, and LLM-generated reviews.

You can access the full reviewer guidelines at http://aclrollingreview.org/reviewerguidelines and the review form at http://aclrollingreview.org/reviewform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70f04aa0-9d99-4464-9963-6c81b9a1693d",
  "isSidechain": true,
  "promptId": "98ca2875-6cf2-4ad3-8c08-89c0d97fa292",
  "agentId": "afd5e907895a8b75a",
  "type": "user",
  "uuid": "757d0f46-6fd4-4cbd-93ec-3635f00f0003",
  "sourceToolAssistantUUID": "70f04aa0-9d99-4464-9963-6c81b9a1693d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T16:40:21.829Z_

<details><summary>↩ Tool result · `toolu_01FsPS4xQNdvnxVXgbpAY2yc`</summary>

```text
Web search results for query: "EMNLP 2026 reviewer guidelines"

Links: [{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here is what I found regarding EMNLP 2026 reviewer guidelines:

## Key Reviewer Requirements and Deadlines

All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair, with assignments subsequently based on qualifications.

After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.

If you receive assignments, your reviews must be completed by July 6, or your meta-reviews - by July 29.

## Emergency Procedures

In case of any emergencies, the chairs should be warned via the emergency declaration form.

## Consequences of Non-Compliance

Highly irresponsible reviewers may be ineligible to (re-)submit or commit their work during the next ARR cycle.

## Conference Goals

EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

The conference uses the ACL Rolling Review (ARR) system for reviewing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01f989d8-cf02-42b4-b587-0be6d612b69d",
  "isSidechain": true,
  "promptId": "98ca2875-6cf2-4ad3-8c08-89c0d97fa292",
  "agentId": "afd5e907895a8b75a",
  "type": "user",
  "uuid": "17075274-ea03-4976-8d05-ff2dd627dc04",
  "sourceToolAssistantUUID": "01f989d8-cf02-42b4-b587-0be6d612b69d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T16:40:21.881Z_

<details><summary>↩ Tool result · `toolu_01HyYAR9KpqzMmJvQXnb9PX7`</summary>

```text
Web search results for query: "ARR review form dimensions scoring"

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Survivors, Complainers, and Borderliners: Upward Bias in Online Discussions of Academic Conference Reviews","url":"https://arxiv.org/html/2509.16831v1"},{"title":"ACL 2022 Chair Blog Post FAQ","url":"https://www.2022.aclweb.org/post/acl-2022-chair-blog-post-faq"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Overall score distribution in ARR-3Y and ARR complete reviews. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Overall-score-distribution-in-ARR-3Y-and-ARR-complete-reviews_fig1_358162807"},{"title":"A critical review of scoring options for clinical measurement tools","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4624594/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about the ARR review form dimensions and scoring:

## Review Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Scoring Details

**Excitement Score:** The form asks "How exciting is this paper for you?" with the note that excitement is subjective and does not necessarily follow what is popular in the field. The excitement scale includes ratings such as:
- 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference
- 4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference

**Overall Recommendation:** The overall recommendation scale includes options such as:
- 2 = Resubmit next cycle: I think this paper needs substantial revisions that can be completed by the next ARR cycle
- 1.5 = Resubmit after next cycle: I think this paper needs substantial revisions that cannot be completed by the next ARR cycle
- 1 = Do not resubmit: This paper has to be fully redone, or it is not relevant to the *ACL community (e.g. it is in no way related to computational processing of language)

The soundness scores must be justified by the text of the review.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e324d60-0480-47a0-ae54-ca34d0f0fd74",
  "isSidechain": true,
  "promptId": "98ca2875-6cf2-4ad3-8c08-89c0d97fa292",
  "agentId": "afd5e907895a8b75a",
  "type": "user",
  "uuid": "73b2e08a-54b7-4bfc-9b1e-ffaea0336410",
  "sourceToolAssistantUUID": "4e324d60-0480-47a0-ae54-ca34d0f0fd74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T16:40:22.123Z_

<details><summary>↩ Tool result · `toolu_01H2AyhocjQwbK4juEhzVt9A`</summary>

```text
Web search results for query: "ACL ARR review form 2025 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about the ACL ARR review form for 2025-2026:

## Review Form Overview

The ARR review form uses a rating scale including: 5 = Consider for Award (top 2.5% papers), 2 = Resubmit next cycle (needs substantial revisions by next cycle), 1.5 = Resubmit after next cycle (needs substantial revisions that cannot be completed by next cycle), and 1 = Do not resubmit (paper needs to be fully redone or isn't relevant to the *ACL community).

## Key Review Form Questions

The form includes several important assessment areas:

- Questions about major reasons to publish the paper at a selective *ACL venue, such as novel methodology, insightful empirical results, theoretical analysis, or clear organization of related literature

- Assessment of whether authors have adequately discussed the limitations and potential positive and negative societal impacts of their work

- Evaluation of whether there is enough information in the paper for readers to reproduce main results or build upon the work

- A subjective excitement rating considering transformational breakthroughs, impact on communities, and relevance to reviewers' own research

## 2025-2026 Timeline

For the December 2025 cycle, the registration form deadline is January 7th 2026, reviewer checklists must be completed by January 21st, and the deadline for reviews is February 7th.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ae671c3-8e99-4962-a629-9d4934b5b0ca",
  "isSidechain": true,
  "promptId": "98ca2875-6cf2-4ad3-8c08-89c0d97fa292",
  "agentId": "afd5e907895a8b75a",
  "type": "user",
  "uuid": "0b1187bd-fbb5-40c6-8a14-1a6d52992e2c",
  "sourceToolAssistantUUID": "5ae671c3-8e99-4962-a629-9d4934b5b0ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-23T16:40:28.025Z_

Based on my web search, here are the official ACL Rolling Review (ARR) review form dimensions and scoring scales:

## ARR Review Form Dimensions (as of February 2025)

The current ARR review form uses **three main scoring dimensions**:

1. **Soundness** - Evaluation of the technical quality and correctness of the work. Soundness scores must be justified by the text of the review.

2. **Excitement** - Subjective assessment of how exciting the paper is, independent of what's popular in the field. The excitement scale includes ratings such as:
   - 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference
   - 4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference

3. **Overall Recommendation** - Final recommendation scale with options including:
   - 2 = Resubmit next cycle: Paper needs substantial revisions by the next ARR cycle
   - 1.5 = Resubmit after next cycle: Paper needs substantial revisions that cannot be completed by the next ARR cycle
   - 1 = Do not resubmit: Paper needs to be fully redone or isn't relevant to the *ACL community

## Additional Assessment Areas

The review form also includes questions regarding:
- Major reasons to publish the paper (novel methodology, empirical results, theoretical analysis, etc.)
- Discussion of limitations and societal impacts
- Reproducibility information
- Transformational breakthroughs and impact on communities

For detailed information and the complete form, you can access the official ARR Review Form page.

Sources:
- [Review Form – ACL Rolling Review](http://aclrollingreview.org/reviewform)
- [ARR Reviewer Guidelines](http://aclrollingreview.org/reviewerguidelines)
- [ACL Rolling Review Platform](http://aclrollingreview.org/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b1187bd-fbb5-40c6-8a14-1a6d52992e2c",
  "isSidechain": true,
  "agentId": "afd5e907895a8b75a",
  "requestId": "req_011CbKqCfnLGGFyHz7B6nf1v",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1bfc9c75-f010-47d8-ab81-bcc40d7eca3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_reviewer_2_3ff3bf17",
  "sessionId": "597728ec-64e3-44af-8087-634734232d78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QiTR74Cfus9qHCjzWcVdek",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3908,
      "cache_read_input_tokens": 17987,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3908
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 451,
          "cache_read_input_tokens": 17987,
          "cache_creation_input_tokens": 3908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3908,
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
