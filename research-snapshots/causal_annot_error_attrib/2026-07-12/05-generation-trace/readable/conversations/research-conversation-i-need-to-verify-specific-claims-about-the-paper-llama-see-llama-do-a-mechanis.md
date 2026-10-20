# Research conversation: I need to verify specific claims about the paper "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainme

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ae871ea085ea00f36.jsonl`
- **Structured JSON:** [`368f6585e7aff850171a.json`](../../sessions/36/368f6585e7aff850171a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-17T08:55:46.873Z_

I need to verify specific claims about the paper "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs" (ACL 2025, arXiv:2505.09338). 

Use WebSearch and WebFetch to:
1. Confirm this paper exists and was an ACL 2025 Outstanding Paper
2. Read the abstract and key findings - specifically:
   a. Does it find that entrainment heads are 2.9-10.7% of heads per relation?
   b. Does static ablation cause only 0.2-3% ICL degradation?
   c. Does Finding 2 state that context can be beneficial when relevant?
   d. Does the paper say entrainment heads are "not strongly related to how LMs process and utilise contextual information or perform ICL more broadly"?
   e. Does the paper identify heads across 15 LRE relations?
   f. Is code available at github.com/frankniujc/entrainment?
3. Check if this paper has spawned any follow-up work or concurrent papers targeting training-time fixes for entrainment

Report all findings with specific quotes where possible. Be thorough - this is for a strict ML research review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "97f5d267-90e9-4e34-b5f4-04c20392e476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T08:55:46.877Z_

```json
{
  "parentUuid": "97f5d267-90e9-4e34-b5f4-04c20392e476",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
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
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "81ff1a75-e9ff-4072-aac9-ce3d50c397ed",
  "timestamp": "2026-05-17T08:55:46.877Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T08:55:49.154Z_



I'll search for this paper and verify all the claims systematically. Let me start by loading the necessary tools and searching for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81ff1a75-e9ff-4072-aac9-ce3d50c397ed",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rvNX13VpN6a959dJrg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b41935dd-3a4d-4b37-8544-a0724dad2bdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvdbiyrCqQzoUmCoEkM73Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8124,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8124,
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

_source line 4 · 2026-05-17T08:55:49.512Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XJENmoonMT9kzdLS7Lfwt1`</summary>

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
  "parentUuid": "b41935dd-3a4d-4b37-8544-a0724dad2bdd",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rvNX13VpN6a959dJrg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e595c67-4b47-4255-91f6-6ab41ebb0e5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvdbiyrCqQzoUmCoEkM73Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8124,
      "cache_read_input_tokens": 0,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8124
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8124,
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

_source line 5 · 2026-05-17T08:55:49.520Z_

<details><summary>↩ Tool result · `toolu_01XJENmoonMT9kzdLS7Lfwt1`</summary>

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
  "parentUuid": "4e595c67-4b47-4255-91f6-6ab41ebb0e5c",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "3f3d7a3d-9e6a-4ed2-b264-f18a2d18b3e5",
  "sourceToolAssistantUUID": "4e595c67-4b47-4255-91f6-6ab41ebb0e5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-17T08:55:53.933Z_



Now let me search for the paper and fetch it from arXiv.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f3d7a3d-9e6a-4ed2-b264-f18a2d18b3e5",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rva3J2av4BqhTYUMBF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7aa7bd9-4e8c-432b-bd5a-077d5cfb94e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFbd76eTJhWdKByes7fL26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 8124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1918,
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

_source line 7 · 2026-05-17T08:55:55.546Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E2LXcnXQn47182cmd59TQn`</summary>

```json
{
  "query": "arXiv 2505.09338 \"Llama See Llama Do\" mechanistic entrainment LLMs ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7aa7bd9-4e8c-432b-bd5a-077d5cfb94e7",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rva3J2av4BqhTYUMBF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e17bf5f-812e-413c-8806-9dc7331fd7c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFbd76eTJhWdKByes7fL26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 8124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1918,
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

_source line 8 · 2026-05-17T08:55:55.880Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JyJEvEb93j7uXkMPYQJGTS`</summary>

```json
{
  "query": "ACL 2025 Outstanding Paper awards list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e17bf5f-812e-413c-8806-9dc7331fd7c0",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rva3J2av4BqhTYUMBF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7bc7780-d0bf-42be-8902-b57edc4bdfea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFbd76eTJhWdKByes7fL26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 8124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1918,
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

_source line 9 · 2026-05-17T08:55:56.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0158udt1F6N5SG8y79EcfW6Y`</summary>

```json
{
  "query": "github.com/frankniujc/entrainment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7bc7780-d0bf-42be-8902-b57edc4bdfea",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rva3J2av4BqhTYUMBF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bae0f0d-1b5c-44a2-af2c-ce0c0a71e8f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFbd76eTJhWdKByes7fL26",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 8124,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1918
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 191,
          "cache_read_input_tokens": 8124,
          "cache_creation_input_tokens": 1918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1918,
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

_source line 10 · 2026-05-17T08:56:00.777Z_

<details><summary>↩ Tool result · `toolu_01E2LXcnXQn47182cmd59TQn`</summary>

```text
Web search results for query: "arXiv 2505.09338 "Llama See Llama Do" mechanistic entrainment LLMs ACL 2025"

Links: [{"title":"[2505.09338] Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs","url":"https://arxiv.org/abs/2505.09338"},{"title":"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs","url":"https://arxiv.org/html/2505.09338"},{"title":"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.791/"},{"title":"[Literature Review] Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs","url":"https://www.themoonlight.io/en/review/llama-see-llama-do-a-mechanistic-perspective-on-contextual-entrainment-and-distraction-in-llms"},{"title":"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.09338v1"},{"title":"Mechanistic Interpretability","url":"https://www.aussieai.com/research/mechanistic-interpretability"},{"title":"A Mechanistic Perspective On Contextual Entrainment and ...","url":"https://www.scribd.com/document/906807672/2505-09338v2"},{"title":"A Mechanistic Perspective on Contextual Entrainment and ...","url":"https://aclanthology.org/2025.acl-long.791.pdf"},{"title":"LLaMA-Annotate—Visualizing Token-Level Confidences for LLMs","url":"https://www.researchgate.net/publication/393631072_LLaMA-Annotate-Visualizing_Token-Level_Confidences_for_LLMs"},{"title":"Awards - ACL 2025","url":"https://2025.aclweb.org/program/awards/"}]

I found the paper! Here's what I found about arXiv 2505.09338:

## Paper Overview

The paper is titled "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs" by Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, and Amir H. Abdi.

## Key Findings

The paper observes a novel phenomenon called contextual entrainment across a wide range of language models, where LMs assign significantly higher logits (or probabilities) to any tokens that have previously appeared in the context prompt, even for random tokens.

This suggests that contextual entrainment is a mechanistic phenomenon, occurring independently of the relevance or semantic relation of the tokens to the question or the rest of the sentence. However, the magnitude of contextual entrainment is influenced by semantic factors, with counterfactual prompts having a greater effect compared to factual ones.

## Mechanistic Analysis

The authors hypothesize that there is a circuit of attention heads—the entrainment heads—that corresponds to the contextual entrainment phenomenon, and they identify these heads using a novel entrainment head discovery method based on differentiable masking. When these heads are "turned off" by setting their outputs to zero, the effect of contextual entrainment is significantly attenuated.

## Publication

The paper was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e17bf5f-812e-413c-8806-9dc7331fd7c0",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "9506d8d5-fa61-44a3-aa3e-e4535a47fb08",
  "sourceToolAssistantUUID": "2e17bf5f-812e-413c-8806-9dc7331fd7c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T08:56:02.036Z_

<details><summary>↩ Tool result · `toolu_01JyJEvEb93j7uXkMPYQJGTS`</summary>

```text
Web search results for query: "ACL 2025 Outstanding Paper awards list"

Links: [{"title":"Awards - ACL 2025","url":"https://2025.aclweb.org/program/awards/"},{"title":"DeepSeek's Liang Wenfeng & Peking University's Yang Yaodong's Team Win Best Paper Award at ACL 2025 with NSA Paper","url":"https://eu.36kr.com/en/p/3401632759482502"},{"title":"ACL 2026 on X: \"Congratulations to all the outstanding and best paper award winners at #ACL2025NLP! [A few randomly selected photos from the awards session] https://t.co/r0sepRvcD7\" / X","url":"https://x.com/aclmeeting/status/1950745647214161930"},{"title":"Announcement of the 2025 ACL Test-of-Time Paper Award | ACL Member Portal","url":"https://www.aclweb.org/portal/content/announcement-2025-acl-test-time-paper-award"},{"title":"ACL Conference Awards Policy - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Conference_Awards_Policy"},{"title":"ACL 2025 on X: \"🏆 ACL Best Paper Awards: - Mission: Impossible Language Models by Kallini et al. - Semisupervised Neural Proto-Language Reconstruction by Lu et al. - Why are Sensitive Functions Hard for Transformers? By Hahn et al. #NLProc #ACL2024NLP\" / X","url":"https://x.com/aclmeeting/status/1823664612581273959?lang=en"},{"title":"Record Breaking ACL 2025 Crowns Four Game-Changing Papers on Speed, Fairness & Safety for Next-Gen LLMs and Beyond | CSPaper","url":"https://cspaper.org/topic/116/record-breaking-acl-2025-crowns-four-game-changing-papers-on-speed-fairness-safety-for-next-gen-llms-and-beyond"},{"title":"Announcing the TACL 2025 paper awards | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/announcement/view/117"},{"title":"Record Breaking ACL 2025 Crowns Four Game-Changing Papers on Speed, Fairness & Safety for Next-Gen LLMs and Beyond | CSPaper Forum","url":"https://forum.cspaper.org/topic/116/record-breaking-acl-2025-crowns-four-game-changing-papers-on-speed-fairness-safety-for-next-gen-llms-and-beyond"},{"title":"Top 5 Trends in Outstanding Papers from ACL 2025 - AI Realist","url":"https://msukhareva.substack.com/p/top-five-trends-in-acl-2025-outstanding"}]

Based on the search results, I can provide you with information about the ACL 2025 Outstanding Paper awards:

## ACL 2025 Outstanding Paper Awards

There were 26 Outstanding Papers selected at ACL 2025. Here are some of the papers mentioned:

1. A New Formulation of Zipf's Meaning - Frequency Law through Contextual Diversity
2. All That Glitters is Not Novel: Plagiarism in Al Generated Research
3. Between Circuits and Chomsky: Pre-pretraining on Formal Languages Imparts Linguistic Biases
4. Beyond N-Grams: Rethinking Evaluation Metrics and Strategies for Multilingual Abstractive Summarization
5. Bridging the Language Gaps in Large Language Models with inference-Time Cross-Lingual Intervention
6. Byte Latent Transformer: Patches Scale Better Than Tokens
7. Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities

Additional outstanding papers mentioned include:
- PARME: Parallel Corpora for Low-Resourced Middle Eastern Languages, which presents parallel corpora for Middle Eastern languages, facilitating machine translation and NLP research
- Typology-Guided Adaptation for African NLP

For a complete list of all 26 outstanding papers, the official ACL 2025 awards page at https://2025.aclweb.org/program/awards/ would have the comprehensive listing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7bc7780-d0bf-42be-8902-b57edc4bdfea",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "e0c04e2c-52ed-4033-8e82-56231178eba4",
  "sourceToolAssistantUUID": "a7bc7780-d0bf-42be-8902-b57edc4bdfea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T08:56:02.270Z_

<details><summary>↩ Tool result · `toolu_0158udt1F6N5SG8y79EcfW6Y`</summary>

```text
Web search results for query: "github.com/frankniujc/entrainment"

Links: [{"title":"GitHub - frankniujc/entrainment","url":"https://github.com/frankniujc/entrainment"},{"title":"frankniujc (Jingcheng Niu) · GitHub","url":"https://github.com/frankniujc"},{"title":"Frank Niu","url":"https://frankniujc.github.io/"},{"title":"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs","url":"https://arxiv.org/html/2505.09338"},{"title":"Jingcheng (Frank) Niu on X: \"Hey this is me! Our paper: Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs Blog post: https://t.co/x6pRVJhSHt\" / X","url":"https://x.com/frankniujc/status/1950602839010451855"},{"title":"A Mechanistic Perspective on Contextual Entrainment and ...","url":"https://aclanthology.org/2025.acl-long.791.pdf"},{"title":"GitHub - frankniujc/kn_thesis","url":"https://github.com/frankniujc/kn_thesis"},{"title":"entrainment · GitHub Topics","url":"https://github.com/topics/entrainment"},{"title":"GitHub - frankniujc/gridloc_probe: Code, data, and results of COLING 2022 paper Does BERT Rediscover the Classical NLP Pipeline?","url":"https://github.com/frankniujc/gridloc_probe"},{"title":"GitHub - frankniujc/covid_sentiment_analysis: Code, analysis and data for the paper Statistically Evaluating Social Media Sentiment Trends towards COVID-19 Non-Pharmaceutical Interventions with Event Studies.","url":"https://github.com/frankniujc/covid_sentiment_analysis"}]

Based on the search results, here's what I found about the github.com/frankniujc/entrainment repository:

This repository accompanies the paper "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs."

**Research Overview:**

The research observes a novel phenomenon called contextual entrainment across a wide range of language models and prompt settings, providing a new mechanistic perspective on how LMs become distracted by "irrelevant" contextual information in the input prompt. Specifically, language models assign significantly higher logits (or probabilities) to any tokens that have previously appeared in the context prompt, even for random tokens.

**Key Findings:**

The magnitude of contextual entrainment is influenced by semantic factors, with counterfactual prompts having a greater effect compared to factual ones, suggesting that while contextual entrainment is a mechanistic phenomenon, it is modulated by semantic factors.

**Repository Contents:**

The repository contains an end-to-end notebook walking through every finding in the paper and a script to search for entrainment heads.

**Impact:**

The paper "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs" won the Outstanding Paper Award at ACL 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bae0f0d-1b5c-44a2-af2c-ce0c0a71e8f9",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "9c6a39bf-ff50-4c1b-aa13-9dce283cac88",
  "sourceToolAssistantUUID": "2bae0f0d-1b5c-44a2-af2c-ce0c0a71e8f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-17T08:56:05.817Z_

The paper exists, it's at ACL 2025, and the GitHub repo is confirmed. Now let me fetch the detailed content from the arXiv page, the ACL awards page, and the GitHub repo to verify the specific numerical claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c6a39bf-ff50-4c1b-aa13-9dce283cac88",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rwWFsFbUhWQyCZhWTw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63380355-d780-40d0-a6e5-7954c27d12d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pi2WioVXHkwNkvHLqQX4aY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 10042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3173,
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

_source line 14 · 2026-05-17T08:56:07.351Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SVtuZpgYtwhZ65uqRdvUQ1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.09338",
  "prompt": "Extract the full abstract of this paper. Also extract any information about the authors, the venue it was published at, and any version history."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63380355-d780-40d0-a6e5-7954c27d12d9",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rwWFsFbUhWQyCZhWTw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9885a114-867d-474f-ab2f-b100f335b591",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pi2WioVXHkwNkvHLqQX4aY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 10042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3173,
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

_source line 15 · 2026-05-17T08:56:08.777Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011FLorsziUjyr93VXk2c8JL`</summary>

```json
{
  "url": "https://2025.aclweb.org/program/awards/",
  "prompt": "List ALL Outstanding Paper award winners at ACL 2025. Look specifically for \"Llama See, Llama Do\" paper. List every paper title mentioned in the Outstanding Papers category."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9885a114-867d-474f-ab2f-b100f335b591",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rwWFsFbUhWQyCZhWTw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18d1a232-7a39-48fb-bcaa-c4070d246431",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pi2WioVXHkwNkvHLqQX4aY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 10042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3173,
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

_source line 16 · 2026-05-17T08:56:10.662Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VQDYAvym6fPzj9LgtQsQzN`</summary>

```json
{
  "url": "https://github.com/frankniujc/entrainment",
  "prompt": "Extract all information from this GitHub repository page: the README contents, description, any mentions of specific numbers like percentages, findings, relations, LRE, etc. What does the repo contain?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18d1a232-7a39-48fb-bcaa-c4070d246431",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rwWFsFbUhWQyCZhWTw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20a839d3-5d0b-453b-93c9-232157d81b87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pi2WioVXHkwNkvHLqQX4aY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3173,
      "cache_read_input_tokens": 10042,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3173
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 372,
          "cache_read_input_tokens": 10042,
          "cache_creation_input_tokens": 3173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3173,
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

_source line 17 · 2026-05-17T08:56:11.816Z_

<details><summary>↩ Tool result · `toolu_01SVtuZpgYtwhZ65uqRdvUQ1`</summary>

```text
# Paper Summary: "Llama See, Llama Do"

## Full Abstract

The researchers identified a phenomenon called "contextual entrainment" where language models assign higher probabilities to tokens that previously appeared in the input prompt, regardless of relevance. While mechanistic in nature, semantic factors modulate this effect—counterfactual prompts trigger stronger entrainment than factual ones. The team discovered "entrainment heads" (attention head circuits) responsible for this behavior using differentiable masking. Disabling these heads significantly reduces distraction, allowing models to generate outputs as if the distracting context weren't present.

## Authors

- Jingcheng Niu
- Xingdi Yuan
- Tong Wang
- Hamidreza Saghir
- Amir H. Abdi

## Publication Venue

**ACL 2025** (Association for Computational Linguistics)

## Version History

- **v1**: Submitted May 14, 2025 (599 KB)
- **v2**: Revised June 27, 2025 (599 KB) — current version

**arXiv identifier**: 2505.09338
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9885a114-867d-474f-ab2f-b100f335b591",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "ffd7f7e0-df92-476d-bfe9-e42c65773ce0",
  "sourceToolAssistantUUID": "9885a114-867d-474f-ab2f-b100f335b591",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T08:56:15.634Z_

<details><summary>↩ Tool result · `toolu_01VQDYAvym6fPzj9LgtQsQzN`</summary>

```text
# GitHub Repository: frankniujc/entrainment

## Overview
This repository contains research code accompanying the paper **"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs."**

## Key Findings
The research identifies a phenomenon called "contextual entrainment," where language models assign higher probabilities to tokens that previously appeared in context, regardless of relevance. The authors discovered that while this is a mechanistic process, semantic factors modulate its magnitude. They identified specific attention heads responsible for this behavior and demonstrated that disabling these heads reduces the distraction effect.

## Repository Contents

**Files:**
- `entrainment.ipynb` – Comprehensive notebook covering all paper findings
- `head_search.py` – Script for identifying entrainment heads
- Dataset folder: `data/lre_dataset`
- Results folder: `head_search_results`

**Language Composition:**
- Jupyter Notebook: 90.1%
- Python: 9.9%

## Metadata
- **Authors:** Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, Amir H. Abdi
- **License:** MIT
- **Stars:** 13 | **Forks:** 2
- **Publication:** ACL 2025 (Vienna, Austria)
- **Arxiv Link:** 2505.09338
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20a839d3-5d0b-453b-93c9-232157d81b87",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "8e4315e6-95bb-4be7-8b6e-f3c8b48abea2",
  "sourceToolAssistantUUID": "20a839d3-5d0b-453b-93c9-232157d81b87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T08:56:18.485Z_

<details><summary>↩ Tool result · `toolu_011FLorsziUjyr93VXk2c8JL`</summary>

```text
# Outstanding Papers at ACL 2025

The "Outstanding Papers" category includes 26 award-winning papers. Here are all the titles:

1. "A New Formulation of Zipf's Meaning-Frequency Law through Contextual Diversity"
2. "All That Glitters is Not Novel: Plagiarism in AI Generated Research"
3. "Between Circuits and Chomsky: Pre-pretraining on Formal Languages Imparts Linguistic Biases"
4. "Beyond N-Grams: Rethinking Evaluation Metrics and Strategies for Multilingual Abstractive Summarization"
5. "Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention"
6. "Byte Latent Transformer: Patches Scale Better Than Tokens"
7. "Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities for Downstream Task Scaling Law"
8. "From Real to Synthetic: Synthesizing Millions of Diversified and Complicated User Instructions with Attributed Grounding"
9. "HALOGEN: Fantastic LLM Hallucinations and Where to Find Them"
10. "HateDay: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter"
11. "IOT: Embedding Standardization Method Towards Zero Modality Gap"
12. "IndicSynth: A Large-Scale Multilingual Synthetic Speech Dataset for Low-Resource Indian Languages"
13. "LaTIM: Measuring Latent Token-to-Token Interactions in Mamba Models"
14. **"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs"**
15. "LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts"
16. "Mapping 1,000+ Language Models via the Log-Likelihood Vector"
17. "MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models"
18. "PARME: Parallel Corpora for Low-Resourced Middle Eastern Languages"
19. "Past Meets Present: Creating Historical Analogy with Large Language Models"
20. "Pre³: Enabling Deterministic Pushdown Automata for Faster Structured LLM Generation"
21. "Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory"
22. "Revisiting Compositional Generalization Capability of Large Language Models Considering Instruction Following Ability"
23. "Toward Automatic Discovery of a Canine Phonetic Alphabet"
24. "Towards the Law of Capacity Gap in Distilling Language Models"
25. "Turning Trash into Treasure: Accelerating Inference of Large Language Models with Token Recycling"
26. "Typology-Guided Adaptation for African NLP"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18d1a232-7a39-48fb-bcaa-c4070d246431",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "a3ec079f-b000-4bf5-871e-71aee878c462",
  "sourceToolAssistantUUID": "18d1a232-7a39-48fb-bcaa-c4070d246431",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-17T08:56:22.698Z_

Excellent. The paper is confirmed as an ACL 2025 Outstanding Paper (#14 on the list). Now let me fetch the full HTML version of the paper to verify the specific numerical claims about entrainment head percentages, ablation degradation, Finding 2, and the 15 LRE relations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3ec079f-b000-4bf5-871e-71aee878c462",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rxhc2K3bsD2GHFVwDz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40258199-c0c2-44f6-8f3b-12e23bceddbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017daYTMAj6NPQMzsk2Y3Bmk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 1493,
      "cache_read_input_tokens": 13215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1493,
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

_source line 21 · 2026-05-17T08:56:29.078Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DJ5FLbyMAezxcrenpfaP8k`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.09338",
  "prompt": "Extract the following specific information from this paper:\n\n1. The exact percentage range of entrainment heads per relation (looking for claims about 2.9-10.7% or similar percentages)\n2. Any claims about \"static ablation\" causing ICL degradation - what exact percentage range is stated? (looking for 0.2-3% or similar)\n3. The exact text of \"Finding 2\" - what does it say? Is it about context being beneficial when relevant?\n4. Any quote stating entrainment heads are \"not strongly related to how LMs process and utilise contextual information or perform ICL more broadly\" or similar\n5. How many LRE relations are studied? Is it 15?\n6. The exact mention of the GitHub URL github.com/frankniujc/entrainment\n7. Any discussion of training-time fixes or future work suggestions\n\nPlease provide exact quotes where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40258199-c0c2-44f6-8f3b-12e23bceddbf",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rxhc2K3bsD2GHFVwDz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c92b59ab-4278-4b31-a3c5-29632e047e47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017daYTMAj6NPQMzsk2Y3Bmk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 365,
      "cache_creation_input_tokens": 1493,
      "cache_read_input_tokens": 13215,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1493
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 365,
          "output_tokens": 352,
          "cache_read_input_tokens": 13215,
          "cache_creation_input_tokens": 1493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1493,
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

_source line 22 · 2026-05-17T08:56:37.009Z_

<details><summary>↩ Tool result · `toolu_01DJ5FLbyMAezxcrenpfaP8k`</summary>

```text
# Paper Analysis: Contextual Entrainment in LLMs

## 1. Entrainment Heads Percentage Range
**Exact range: 2.9% to 10.7%**

From Table 3: "A small set of attention heads (3.2% to 10.7%) can substantially increase the gap between the logits"

The density percentages across relations span from 2.9% (country language) to 10.7% (product by company).

## 2. ICL Performance Degradation After Head Removal
**Exact range: 0.2% to 3%**

From Table 4 caption: "After removing the entrainment heads (🔧), the model exhibits only a small performance decrease (0.2∼3%) and continues demonstrate strong ICL capabilities"

## 3. Finding 2 - Exact Text
**"'Distracting' context prompts can be beneficial when relevant."**

The finding states that while distracting token probabilities increase consistently, "the direction of change for the correct token (😊) varies based on topic relevance" and that contextual information "can be beneficial, increasing the likelihood that the model generates the correct response."

## 4. ICL Relationship Quote
**"This circuit of entrainment heads collectively corresponds to contextual entrainment rather than other capabilities and phenomena, such as factual recall, and is not strongly related to how LMs process and utilise contextual information or perform ICL more broadly."**

## 5. Number of LRE Relations
**Yes, exactly 15 relations studied**

From Appendix A: "As a result, we select 15 relations, with their statistics listed in Table 5"

## 6. GitHub URL
**Exact mention: "https://github.com/frankniujc/entrainment"**

From the abstract footnote: "The code and data of this work can be found at https://github.com/frankniujc/entrainment"

## 7. Future Work / Training-Time Fixes
The paper explicitly states: "we do not propose an application to mitigate the distraction problem. We believe our findings serve as foundational steps toward addressing this issue...we leave such applications for future research."

No training-time fixes are discussed; the focus remains on mechanistic understanding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c92b59ab-4278-4b31-a3c5-29632e047e47",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "ea2d8203-508f-4fbf-b8d7-8ce6bef1265c",
  "sourceToolAssistantUUID": "c92b59ab-4278-4b31-a3c5-29632e047e47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-17T08:56:40.040Z_

Now let me search for any follow-up or concurrent work that builds on this paper, particularly around training-time fixes for entrainment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea2d8203-508f-4fbf-b8d7-8ce6bef1265c",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rz4n25y2pR2WqP3ixx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1260f2b-8812-4bdd-93b1-b7a31879802b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSoVMQ2rRrX7XwSrH3f4WW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 14708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1253,
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

_source line 24 · 2026-05-17T08:56:41.147Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PfwJHAvEHRXqAMNX1zuP7M`</summary>

```json
{
  "query": "follow-up work \"contextual entrainment\" LLM training-time fix mitigation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1260f2b-8812-4bdd-93b1-b7a31879802b",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rz4n25y2pR2WqP3ixx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1f1e3a3-2652-4455-b76d-0460b61cf402",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSoVMQ2rRrX7XwSrH3f4WW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 14708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1253,
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

_source line 25 · 2026-05-17T08:56:41.595Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L7XU95cYeUTLGHkeRuruMo`</summary>

```json
{
  "query": "papers citing \"Llama See Llama Do\" entrainment heads attention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1f1e3a3-2652-4455-b76d-0460b61cf402",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rz4n25y2pR2WqP3ixx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2ad94d2-1d02-47ca-81ea-199f325c7ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSoVMQ2rRrX7XwSrH3f4WW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 14708,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1253
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 14708,
          "cache_creation_input_tokens": 1253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1253,
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

_source line 26 · 2026-05-17T08:56:45.145Z_

<details><summary>↩ Tool result · `toolu_01L7XU95cYeUTLGHkeRuruMo`</summary>

```text
Web search results for query: "papers citing "Llama See Llama Do" entrainment heads attention 2025 2026"

No links found.

The search didn't return any results for papers citing "Llama See Llama Do" with those specific parameters. This could mean:

1. The paper title might have a slightly different format
2. Papers citing this work might not yet be indexed with this exact query combination
3. The specific focus on entrainment heads and attention mechanisms in 2025-2026 might be too narrow for current indexing

Would you like me to try a modified search with:
- A broader query about "Llama See Llama Do"?
- Just the paper title without the other specific terms?
- A search for recent papers on entrainment or attention heads in transformer models?

Let me know how you'd like me to refine the search!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2ad94d2-1d02-47ca-81ea-199f325c7ad1",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "db4d02fe-a052-446d-9280-4b35a354142c",
  "sourceToolAssistantUUID": "f2ad94d2-1d02-47ca-81ea-199f325c7ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T08:56:49.247Z_

<details><summary>↩ Tool result · `toolu_01PfwJHAvEHRXqAMNX1zuP7M`</summary>

```text
Web search results for query: "follow-up work "contextual entrainment" LLM training-time fix mitigation 2025 2026"

Links: [{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Top LLM Trends 2025: What's the Future of LLMs","url":"https://www.turing.com/resources/top-llm-trends"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"A Survey on LLM Mid-training","url":"https://arxiv.org/html/2510.23081v1"},{"title":"Training LLMs in 2026","url":"https://richardkelley.io/llm-training-in-2026"},{"title":"On the importance of post-training in modern LLM development | Dylan Bourgeois","url":"https://dtsbourg.me/en/articles/post-training"},{"title":"LLM Training Framework for 2026 Tools, Data Strategy & Model Selection","url":"https://kanerika.com/blogs/llm-training/"},{"title":"LMS and professional training: a 2026 overview of a fast-evolving market","url":"https://www.didask.com/en/post/lms-et-formation-professionnelle-etat-des-lieux-un-marche-en-revolution"}]

I found relevant search results for your query. The results contain information about LLM training improvements and mitigation strategies in 2025-2026, though specific work directly titled about "contextual entrainment" doesn't appear in these results.

However, here's what I found related to training-time fixes and mitigation strategies for LLM issues in 2025-2026:

**On Hallucination Mitigation (Training-Time Fixes):**

ML researchers and foundation-model labs are testing concrete ways to reduce hallucinations as an incentive problem through measures that model builders can implement during training, with improvements gradually reaching deployed models. OpenAI's September 2025 paper shows that next-token training objectives and common leaderboards reward confident guessing over calibrated uncertainty, so models learn to bluff. Additionally, Anthropic's work demonstrates how internal "concept vectors" can be steered so that Claude learns when not to answer, turning refusal into a learned policy rather than a fragile prompt trick.

**On Agent Training with Refusal Mechanisms:**

MOSAIC (March 2026) addresses how to train agents that know when to refuse by structuring inference as "plan, check, then act or refuse" using trajectory-level preference learning, showing up to 50% reduction in harmful behavior while preserving task performance.

**On Training Methodology Evolution:**

There's now a clearer division of work between pre-training, capability shaping (methods that improve capabilities that aren't quite pre-training), and alignment shaping (methods that increase alignment).

Would you like me to search more specifically for "contextual entrainment" research, or is there a particular aspect of LLM training-time fixes you'd like to explore further?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1f1e3a3-2652-4455-b76d-0460b61cf402",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "fcfb4cca-ba02-4e8e-9eef-5701b5936cde",
  "sourceToolAssistantUUID": "f1f1e3a3-2652-4455-b76d-0460b61cf402",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T08:56:51.866Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mjpc2c8Em7HuCKoeF1NSAT`</summary>

```json
{
  "query": "\"Llama See Llama Do\" Niu entrainment citation follow-up"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcfb4cca-ba02-4e8e-9eef-5701b5936cde",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rzy8iVeKoyyZRqBevN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea143448-10a2-4000-98e2-91bfb1464f0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7cAR8Xzo6gMZ2tedYqkBW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 251,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 15961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 29 · 2026-05-17T08:56:52.936Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Bi2DrRuQ8RykH8LSzuPG9`</summary>

```json
{
  "query": "LLM distraction context entrainment heads mitigation training fix arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea143448-10a2-4000-98e2-91bfb1464f0a",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rzy8iVeKoyyZRqBevN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a71c763-4c02-4a9a-9bac-7eaab8c9e86a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7cAR8Xzo6gMZ2tedYqkBW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 251,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 15961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 30 · 2026-05-17T08:56:53.151Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bq4aJ2gubKtwbrXecu4cFQ`</summary>

```json
{
  "query": "Semantic Scholar \"Llama See Llama Do\" citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a71c763-4c02-4a9a-9bac-7eaab8c9e86a",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7rzy8iVeKoyyZRqBevN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9fa2907-9360-4e4f-9c29-b47aba61a981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7cAR8Xzo6gMZ2tedYqkBW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 251,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 15961,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1108
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 251,
          "output_tokens": 175,
          "cache_read_input_tokens": 15961,
          "cache_creation_input_tokens": 1108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1108,
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

_source line 31 · 2026-05-17T08:56:55.494Z_

<details><summary>↩ Tool result · `toolu_01Mjpc2c8Em7HuCKoeF1NSAT`</summary>

```text
Web search results for query: ""Llama See Llama Do" Niu entrainment citation follow-up"

No links found.

The search returned no results. This could mean that either the exact phrase "Llama See Llama Do" combined with "Niu entrainment" doesn't have much web presence, or the terms may need to be searched differently.

Would you like me to try alternative search approaches? For example, I could search for:
- Just "Llama See Llama Do" alone
- "Niu entrainment" separately
- Variations of these terms
- Or if you could provide more context about what this relates to (is it academic research, a video, a song, etc.), that might help me refine the search

Let me know how you'd like me to proceed!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea143448-10a2-4000-98e2-91bfb1464f0a",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "606a8b61-618c-494b-ace8-6a1fcc95bba7",
  "sourceToolAssistantUUID": "ea143448-10a2-4000-98e2-91bfb1464f0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T08:56:56.661Z_

<details><summary>↩ Tool result · `toolu_01Bq4aJ2gubKtwbrXecu4cFQ`</summary>

```text
Web search results for query: "Semantic Scholar "Llama See Llama Do" citations"

No links found.

The web search didn't return any results. This could mean that either:

1. The exact phrase "Llama See Llama Do" may not have widespread coverage on the web or in Semantic Scholar
2. The paper or work might be too recent or not widely indexed yet
3. The exact title might be slightly different

Would you like me to try a modified search? For example, I could:
- Search for just "Llama See Llama Do" without specifying Semantic Scholar
- Search for variations of the title
- Search for related terms or authors if you know them

Please let me know how you'd like me to proceed!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9fa2907-9360-4e4f-9c29-b47aba61a981",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "bbe7d83b-6cd6-40f9-9590-1112225f9017",
  "sourceToolAssistantUUID": "d9fa2907-9360-4e4f-9c29-b47aba61a981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T08:57:01.673Z_

<details><summary>↩ Tool result · `toolu_012Bi2DrRuQ8RykH8LSzuPG9`</summary>

```text
Web search results for query: "LLM distraction context entrainment heads mitigation training fix arxiv 2025 2026"

Links: [{"title":"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs","url":"https://arxiv.org/html/2505.09338v2"},{"title":"[2502.01609] Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search","url":"https://arxiv.org/abs/2502.01609"},{"title":"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.791/"},{"title":"A Mechanistic Perspective on Contextual Entrainment and ...","url":"https://aclanthology.org/2025.acl-long.791.pdf"},{"title":"Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search","url":"https://arxiv.org/html/2502.01609v2"},{"title":"How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark","url":"https://arxiv.org/html/2505.18761v2"},{"title":"Attention Steering","url":"https://www.aussieai.com/research/attention-steering"},{"title":"Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://arxiv.org/pdf/2302.00093"},{"title":"[2302.00093] Large Language Models Can Be Easily Distracted by Irrelevant Context","url":"https://arxiv.org/abs/2302.00093"},{"title":"Breaking Focus: Contextual Distraction Curse in Large Language Models","url":"https://arxiv.org/html/2502.01609v1"}]

Based on the web search results, I found several recent papers on LLM distraction, context entrainment, and mitigation strategies from 2025-2026. Here are the key findings:

## Recent Research Papers (2025-2026)

### 1. "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs"

This paper hypothesizes that there is a circuit of attention heads — the entrainment heads — that corresponds to the contextual entrainment phenomenon, and uses a novel entrainment head discovery method based on differentiable masking to identify these heads across various settings. When these heads are "turned off" (set their outputs to zero), the effect of contextual entrainment is significantly attenuated, causing the model to generate output that capitulates to what it would produce if no distracting context were provided. The paper was published at ACL 2025 (July 2025).

### 2. "Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search"

This paper addresses how LLMs often struggle to maintain their original performance when faced with semantically coherent but task-irrelevant contextual information, noting that prior studies using fixed-template or retrieval-based distractions show limited effectiveness against contemporary models. The authors propose a dynamic distraction generation framework based on tree search, where the generation process is guided by model behavior. Mitigation comparisons show that prompt-based optimization methods yield limited gains, whereas post-training approaches (e.g., DPO) significantly enhance the model's contextual robustness. (September 2025)

### 3. "How Is LLM Reasoning Distracted by Irrelevant Context?"

This paper provides a controlled environment for probing LLM reasoning using GSM-DC, combining symbolic DAGs with natural-language templates, and constructed templated prompts with varied surface forms. (September 2025)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a71c763-4c02-4a9a-9bac-7eaab8c9e86a",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "ad27f9ac-52a8-4442-af37-0cb1b6533ea1",
  "sourceToolAssistantUUID": "1a71c763-4c02-4a9a-9bac-7eaab8c9e86a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-17T08:57:06.563Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017sX1EunhVzoogBUmG3pU5H`</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/Llama-See%2C-Llama-Do%3A-A-Mechanistic-Perspective-on-Niu-Yuan/",
  "prompt": "Find the number of citations this paper has received. List the titles of any citing papers if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad27f9ac-52a8-4442-af37-0cb1b6533ea1",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7s1ti6LUhSwnkSAwtXo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8afaa308-6ae7-4e45-ab1f-af3d6d188314",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJcw9mXZNhvgB4pNojsd49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 221,
      "cache_creation_input_tokens": 1640,
      "cache_read_input_tokens": 17069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1640,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 35 · 2026-05-17T08:57:07.912Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VjKHiJ6qMet92ru9c7Zxfz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.01609",
  "prompt": "Extract the abstract. Does this paper cite or build on \"Llama See Llama Do\" or contextual entrainment? Does it propose training-time fixes for LLM distraction?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8afaa308-6ae7-4e45-ab1f-af3d6d188314",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7s1ti6LUhSwnkSAwtXo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55d3e643-a7a6-4d8b-94d8-b774563f4640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJcw9mXZNhvgB4pNojsd49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 221,
      "cache_creation_input_tokens": 1640,
      "cache_read_input_tokens": 17069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1640,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 36 · 2026-05-17T08:57:08.459Z_

<details><summary>↩ Tool result · `toolu_017sX1EunhVzoogBUmG3pU5H`</summary>

```text
I don't have any web page content to analyze. The section marked "Web page content:" appears to be empty, with only dashes shown.

To help you find citation information for a paper, please provide:

1. The URL of the paper's page
2. The title of the paper
3. A link to where the citation data is located

Once you share that information, I can help identify the number of citations and list any available titles of citing papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8afaa308-6ae7-4e45-ab1f-af3d6d188314",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "f0eae0b5-d16c-427a-bb21-29987bc2daf6",
  "sourceToolAssistantUUID": "8afaa308-6ae7-4e45-ab1f-af3d6d188314",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-17T08:57:11.129Z_

<details><summary>↩ Tool result · `toolu_01VjKHiJ6qMet92ru9c7Zxfz`</summary>

```text
# Paper Analysis

## Abstract

"Large Language Models (LLMs) often struggle to maintain their original performance when faced with semantically coherent but task-irrelevant contextual information."

The paper proposes a dynamic distraction generation framework using tree search to stress-test LLMs' contextual robustness. Results show mainstream models experience over 45% performance drops, with post-training approaches like DPO significantly improving robustness.

## Citation Questions

**"Llama See Llama Do" or contextual entrainment:** Not mentioned in the provided content.

**Training-time fixes:** Yes. The paper explicitly discusses post-training approaches, stating that "post-training approaches (e.g., DPO) significantly enhance the model's contextual robustness" as a mitigation strategy, contrasting these with limited gains from prompt-based optimization methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55d3e643-a7a6-4d8b-94d8-b774563f4640",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "58ab37df-0580-45c2-80d6-5ae854cf8220",
  "sourceToolAssistantUUID": "55d3e643-a7a6-4d8b-94d8-b774563f4640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T08:57:11.522Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TnSPfwvJaUhavvkk2RmRay`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.09338v2",
  "prompt": "Find the EXACT text of Finding 2 in this paper. Also find: 1) The exact quote about entrainment heads not being strongly related to ICL. 2) The exact Table 3 data showing percentages of entrainment heads. 3) The exact Table 4 data showing ICL degradation percentages. 4) List all 15 LRE relations studied. 5) Any mention of the GitHub repo URL. Please provide verbatim quotes where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58ab37df-0580-45c2-80d6-5ae854cf8220",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7s1ti6LUhSwnkSAwtXo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "839a280b-e1dd-48bf-a053-afdf1afa1554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJcw9mXZNhvgB4pNojsd49",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 221,
      "cache_creation_input_tokens": 1640,
      "cache_read_input_tokens": 17069,
      "output_tokens": 415,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 221,
          "output_tokens": 415,
          "cache_read_input_tokens": 17069,
          "cache_creation_input_tokens": 1640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1640,
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

_source line 39 · 2026-05-17T08:57:23.629Z_

<details><summary>↩ Tool result · `toolu_01TnSPfwvJaUhavvkk2RmRay`</summary>

```text
# Findings and Data from "Llama See, Llama Do"

## Finding 2 (Exact Text)

"'Distracting' context prompts can be beneficial when relevant."

The full explanation states: "While the probabilities and logits of the distracting tokens consistently increase, the direction of change for the correct token varies based on topic relevance."

## 1) Quote on Entrainment Heads and ICL

"this 'circuit' of entrainment heads collectively corresponds to contextual entrainment rather than other capabilities and phenomena, such as factual recall, and is **not strongly related to how LMs process and utilise contextual information or perform ICL more broadly**."

## 2) Table 3 - Entrainment Head Densities

| Relation | Density |
|----------|---------|
| company hq | 8.8% |
| country capital city | 3.5% |
| country currency | 4.1% |
| country language | 2.9% |
| country largest city | 3.2% |
| food from country | 3.7% |
| fruit inside color | 5.5% |
| fruit outside color | 7.8% |
| landmark in country | 5.8% |
| landmark on continent | 5.1% |
| product by company | 10.7% |
| star constellation name | 7.0% |
| task done by tool | 6.4% |
| task person type | 4.0% |
| work location | 6.6% |

## 3) Table 4 - ICL Task Performance Changes

Maximum degradation observed: **3% decrease** (spelling correction 2-shot: 94.6% → 91.6%)

Most tasks showed **0.2–1% changes**. Translation tasks remained stable.

## 4) All 15 LRE Relations Studied

1. company hq
2. country capital city
3. country currency
4. country language
5. country largest city
6. food from country
7. fruit inside color
8. fruit outside color
9. landmark in country
10. landmark on continent
11. product by company
12. star constellation name
13. task done by tool
14. task person type
15. work location

## 5) GitHub Repository URL

"https://github.com/frankniujc/entrainment"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "839a280b-e1dd-48bf-a053-afdf1afa1554",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "5cec9a1b-6f3b-40b1-b411-d87103ce0632",
  "sourceToolAssistantUUID": "839a280b-e1dd-48bf-a053-afdf1afa1554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-17T08:57:31.522Z_

Let me do one final search to check for any citing papers or concurrent work specifically targeting training-time fixes for entrainment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cec9a1b-6f3b-40b1-b411-d87103ce0632",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7s3jcTTv1FtGrkmkEY7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5657c8c2-3389-465b-8c68-9dd3039aeab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StQzMknBDSY2teodPVYfVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 18709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1668,
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

_source line 41 · 2026-05-17T08:57:32.920Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EGprXSzTgFmVqrxAov1zCh`</summary>

```json
{
  "query": "arxiv 2025 2026 attention head ablation distraction LLM training mitigation \"entrainment\" OR \"copy heads\" OR \"induction heads\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5657c8c2-3389-465b-8c68-9dd3039aeab3",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7s3jcTTv1FtGrkmkEY7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7cec4e7-e8d3-434d-905e-a7f5e1ae48dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StQzMknBDSY2teodPVYfVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 18709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1668,
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

_source line 42 · 2026-05-17T08:57:34.636Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UYUKCMhxzWjFVVDAwo2cTu`</summary>

```json
{
  "url": "https://scholar.google.com/scholar?cites=&as_sdt=2005&sciodt=0,5&hl=en&q=%22Llama+See+Llama+Do%22+entrainment",
  "prompt": "List all papers that cite \"Llama See Llama Do\" or discuss contextual entrainment. Provide paper titles and any available details about whether they propose training-time fixes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7cec4e7-e8d3-434d-905e-a7f5e1ae48dd",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7s3jcTTv1FtGrkmkEY7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "404fc458-1ce8-4962-9f8d-f114cbdf1daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01StQzMknBDSY2teodPVYfVD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1668,
      "cache_read_input_tokens": 18709,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1668
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 18709,
          "cache_creation_input_tokens": 1668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1668,
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

_source line 43 · 2026-05-17T08:57:40.966Z_

<details><summary>↩ Tool result · `toolu_01UYUKCMhxzWjFVVDAwo2cTu`</summary>

```text
# Papers on Contextual Entrainment in LLMs

Based on the Google Scholar search results, here are the papers discussing contextual entrainment:

## Primary Paper
**"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs"** (2025, ACL)
- Authors: J Niu, X Yuan, T Wang, H Saghir, et al.
- Introduces the concept of "entrainment heads" - "a circuit of attention heads" that corresponds to contextual entrainment phenomenon
- Cited by 12 papers
- *No training-time fixes mentioned in the abstract*

## Related Papers

**"Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size"** (2026, arXiv)
- Authors: D Kukreja, K Sah, G Gupta, A Anand, RR Shah, et al.
- Measures how entrainment changes across different model sizes using power law fitting
- *No training-time fixes indicated*

**"Farther the Shift, Sparser the Representation: Analyzing OOD Mechanisms in LLMs"** (2026, arXiv)
- Authors: M Jin, Y Yin, J Niu, Q Zeng, W Xu, M Du, et al.
- Examines how LLMs adapt internal representations under distributional shift
- *No explicit training fixes described*

None of these papers explicitly propose training-time mitigation strategies based on the available abstracts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "404fc458-1ce8-4962-9f8d-f114cbdf1daa",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "0a3af750-75bb-463c-9c05-01f9866d2b03",
  "sourceToolAssistantUUID": "404fc458-1ce8-4962-9f8d-f114cbdf1daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T08:57:43.111Z_

<details><summary>↩ Tool result · `toolu_01EGprXSzTgFmVqrxAov1zCh`</summary>

```text
Web search results for query: "arxiv 2025 2026 attention head ablation distraction LLM training mitigation "entrainment" OR "copy heads" OR "induction heads""

Links: [{"title":"Which Attention Heads Matter for In-Context Learning?","url":"https://arxiv.org/pdf/2502.14010"},{"title":"Published at Building Trust Workshop at ICLR 2025","url":"https://arxiv.org/pdf/2503.03730"},{"title":"[2502.14010] Which Attention Heads Matter for In-Context Learning?","url":"https://arxiv.org/abs/2502.14010"},{"title":"Which Attention Heads Matter for In-Context Learning? | OpenReview","url":"https://openreview.net/forum?id=C7XmEByCFv"},{"title":"Localizing Task Recognition and Task Learning in In-Context Learning via Attention Head Analysis","url":"https://arxiv.org/html/2509.24164"},{"title":"Induction Head Toxicity Mechanistically Explains ...","url":"https://www.arxiv.org/pdf/2505.13514"},{"title":"Understanding and Controlling Repetition Neurons and Induction Heads in In-Context Learning","url":"https://arxiv.org/html/2507.07810"},{"title":"Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence","url":"https://arxiv.org/html/2505.16694v2"},{"title":"A Mechanistic Perspective on Contextual Entrainment and ...","url":"https://aclanthology.org/2025.acl-long.791.pdf"},{"title":"Head Pursuit: Probing Attention Specialization in Multimodal Transformers","url":"https://arxiv.org/html/2510.21518"}]

Based on the search results, I found several highly relevant recent papers from arXiv (2025-2026) that match your query about attention head ablation, distraction, LLM training mitigation, and related concepts:

## Key Papers Found:

### 1. **"Which Attention Heads Matter for In-Context Learning?"** (arXiv:2502.14010, Feb 2025)
This paper compares induction heads that find and copy relevant tokens with function vector (FV) heads whose activations compute a latent encoding of the ICL task, finding that few-shot ICL is driven primarily by FV heads, especially in larger models. The analysis reveals induction heads emerge early in training at around step 1,000, while FV heads appear substantially later at around step 16,000.

### 2. **"Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment"** (ACL 2025)
This paper directly addresses "entrainment" which was one of your search terms. The paper demonstrates that LLMs can be distracted by various types of context, though evidence suggests these "irrelevant" context prompts can benefit LMs' performance.

### 3. **"Induction Head Toxicity Mechanistically Explains..."** (arXiv:2505.13514, 2025)
This paper focuses on induction head behavior and mitigation strategies, examining how induction head mechanisms can cause problematic outputs and approaches to mitigate these effects.

### 4. **"Understanding and Controlling Repetition Neurons and Induction Heads in In-Context Learning"** (arXiv:2507.07810, Nov 2025)
This paper investigates the impact of repetition neurons and induction heads on ICL performance by ablating them. Removing induction heads has been shown to severely impair ICL performance due to their critical role in pattern recognition.

### 5. **"Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence"** (arXiv:2505.16694, June 2025)
This paper extends beyond induction heads, noting that while induction heads can account for ICL when the answer is included in context, practical ICL involves meta-learning how to solve tasks from context rather than just copying answers.

These papers collectively provide comprehensive coverage of attention head mechanisms, their ablation effects, and various mitigation strategies in LLM training and inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7cec4e7-e8d3-434d-905e-a7f5e1ae48dd",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "d647655f-0603-471d-a69a-10070505aa17",
  "sourceToolAssistantUUID": "a7cec4e7-e8d3-434d-905e-a7f5e1ae48dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T08:57:47.421Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AYTKi1aoDuq1bkKKNMdNLD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.01609",
  "prompt": "Does this paper \"Adaptive Distraction\" cite or reference \"Llama See Llama Do\" or Niu et al.? Does it propose DPO or other training-time fixes for LLM distraction? Extract relevant details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d647655f-0603-471d-a69a-10070505aa17",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7s4wNfdSyZADx39GN2z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bda0cb20-9a11-4501-ac56-c7a647a8d304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DjSmfPasW94V25uTaJ8Ci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 399,
      "cache_creation_input_tokens": 1316,
      "cache_read_input_tokens": 20377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1316,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 46 · 2026-05-17T08:57:47.631Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016oK5LdtnXScr9MitFJX2z5`</summary>

```json
{
  "query": "\"Better and Worse with Scale\" \"contextual entrainment\" Kukreja 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bda0cb20-9a11-4501-ac56-c7a647a8d304",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7s4wNfdSyZADx39GN2z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4595145b-b5fa-454f-afbf-b7b1d2444ca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DjSmfPasW94V25uTaJ8Ci",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 399,
      "cache_creation_input_tokens": 1316,
      "cache_read_input_tokens": 20377,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1316
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 399,
          "output_tokens": 193,
          "cache_read_input_tokens": 20377,
          "cache_creation_input_tokens": 1316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1316,
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

_source line 47 · 2026-05-17T08:57:51.253Z_

<details><summary>↩ Tool result · `toolu_01AYTKi1aoDuq1bkKKNMdNLD`</summary>

```text
# Analysis of Paper Content

Based on the provided arXiv page content, I cannot definitively answer whether the paper cites "Llama See Llama Do" or work by Niu et al., as **the full reference list is not included** in the excerpt provided.

## Training-Time Fixes for LLM Distraction

The abstract does address mitigation strategies. The paper states: "Further comparisons of mitigation strategies show that prompt-based optimization methods yield limited gains, whereas post-training approaches (e.g., DPO) significantly enhance the model's contextual robustness."

**Key findings:**
- The authors tested **DPO (Direct Preference Optimization)** as a post-training approach
- This training-time method proved substantially more effective than prompt-based methods at improving robustness against contextual distractions
- The paper indicates the core issue is not knowledge deficiency but rather "a fundamental inability to maintain consistent reasoning under contextual distraction"

The page content does not provide sufficient detail about other specific training-time fixes or the complete reference list needed to confirm citations to the works you mentioned. You would need to access the full PDF to verify those citations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bda0cb20-9a11-4501-ac56-c7a647a8d304",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "60e55b1e-955f-4197-b442-c0e1bbe32fca",
  "sourceToolAssistantUUID": "bda0cb20-9a11-4501-ac56-c7a647a8d304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-17T08:57:52.679Z_

<details><summary>↩ Tool result · `toolu_016oK5LdtnXScr9MitFJX2z5`</summary>

```text
Web search results for query: ""Better and Worse with Scale" "contextual entrainment" Kukreja 2026 arxiv"

Links: [{"title":"Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size","url":"https://arxiv.org/html/2604.13275"},{"title":"[2604.13275] Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size","url":"https://arxiv.org/abs/2604.13275"}]

I found the paper! Here are the search results:

The paper is titled "Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size" by Dikshant Kukreja, Kshitij Sah, Gautam Gupta, Avinash Anand, Rajiv Ratn Shah, Zhengkui Wang, Aik Beng Ng, and Erik Cambria.

The research shows that larger language models become simultaneously better and worse at handling contextual information—better at ignoring false claims, worse at ignoring irrelevant tokens—through the first scaling laws for contextual entrainment, which is the tendency of models to favor tokens that appeared in context regardless of relevance.

Analyzing the Cerebras-GPT (111M-13B) and Pythia (410M-12B) model families, they find entrainment follows predictable power-law scaling, but with opposite trends depending on context type: semantic contexts show decreasing entrainment with scale, while non-semantic contexts show increasing entrainment.

Concretely, the largest models are four times more resistant to counterfactual misinformation than the smallest, yet simultaneously twice as prone to copying arbitrary tokens.

The paper was published on arXiv on April 14, 2026 (arXiv ID: 2604.13275).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4595145b-b5fa-454f-afbf-b7b1d2444ca9",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "fb9f5d9f-7dd0-4df9-9c1e-7aa586a2d5ce",
  "sourceToolAssistantUUID": "4595145b-b5fa-454f-afbf-b7b1d2444ca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-17T08:57:59.418Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MjfGuBUyegugASAZFUUyrz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.13275",
  "prompt": "Extract the full abstract. Does this paper cite \"Llama See, Llama Do\" by Niu et al.? Does it propose any training-time fixes for entrainment, or is it purely analytical? What are the key findings about scaling?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb9f5d9f-7dd0-4df9-9c1e-7aa586a2d5ce",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7s5eMFjZtSgdniy4C9M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34f92928-ca36-409e-8f36-edae3d931a21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDS9De1c24WCtvPqynpT73",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1368,
      "cache_read_input_tokens": 21693,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1368
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 21693,
          "cache_creation_input_tokens": 1368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1368,
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

_source line 50 · 2026-05-17T08:58:05.461Z_

<details><summary>↩ Tool result · `toolu_01MjfGuBUyegugASAZFUUyrz`</summary>

```text
# Analysis of arXiv:2604.13275

## Full Abstract

"Larger language models become simultaneously better and worse at handling contextual information -- better at ignoring false claims, worse at ignoring irrelevant tokens. We formalize this apparent paradox through the first scaling laws for contextual entrainment, the tendency of models to favor tokens that appeared in context regardless of relevance. Analyzing the Cerebras-GPT (111M-13B) and Pythia (410M-12B) model families, we find entrainment follows predictable power-law scaling, but with opposite trends depending on context type: semantic contexts show decreasing entrainment with scale, while non-semantic contexts show increasing entrainment. Concretely, the largest models are four times more resistant to counterfactual misinformation than the smallest, yet simultaneously twice as prone to copying arbitrary tokens. These diverging trends, which replicate across model families, suggest that semantic filtering and mechanical copying are functionally distinct behaviors that scale in opposition -- scaling alone does not resolve context sensitivity, it reshapes it."

## Citation Status

The provided webpage does not list references or citations, so I cannot confirm whether "Llama See, Llama Do" by Niu et al. is cited.

## Approach

This work is **purely analytical**—it documents and formalizes observed phenomena through scaling law analysis rather than proposing training-time interventions.

## Key Scaling Findings

- Power-law scaling patterns exist for contextual entrainment
- **Opposite directional trends**: semantic contexts show *reduced* entrainment at scale; non-semantic contexts show *increased* entrainment
- Largest models demonstrate 4× greater resistance to counterfactual falsehoods but 2× greater susceptibility to arbitrary token copying
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34f92928-ca36-409e-8f36-edae3d931a21",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ae871ea085ea00f36",
  "type": "user",
  "uuid": "20b000ac-4482-4418-b87e-5605656f62e2",
  "sourceToolAssistantUUID": "34f92928-ca36-409e-8f36-edae3d931a21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-17T08:58:51.737Z_

I now have all the information needed to provide a thorough report. Here is the complete verification:

---

## Verification Report: "Llama See, Llama Do" (arXiv:2505.09338)

### 1. Paper existence and award status: CONFIRMED

The paper exists at [arXiv:2505.09338](https://arxiv.org/abs/2505.09338) and is published in ACL 2025 (Proceedings of the 63rd Annual Meeting of the ACL, Volume 1: Long Papers). Authors: Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, Amir H. Abdi. Two arXiv versions: v1 (May 14, 2025) and v2 (June 27, 2025).

**Outstanding Paper: CONFIRMED.** The [official ACL 2025 awards page](https://2025.aclweb.org/program/awards/) lists it as #14 out of 26 Outstanding Papers. It is NOT a Best Paper (those were separate), but it is an Outstanding Paper.

### 2. Specific claim verification

#### 2a. Entrainment heads are 2.9-10.7% of heads per relation: CONFIRMED

Table 3 of the paper shows entrainment head density across all 15 relations. The range spans from **2.9%** (country language) to **10.7%** (product by company). The paper also states: *"A small set of attention heads (3.2% to 10.7%) can substantially increase the gap between the logits"* -- note the slight discrepancy: the text says "3.2% to 10.7%" while the table data shows the actual minimum is 2.9%. The claim of "2.9-10.7%" is consistent with the table data.

#### 2b. Static ablation causes only 0.2-3% ICL degradation: CONFIRMED

Table 4 caption states verbatim: *"After removing the entrainment heads, the model exhibits only a small performance decrease (0.2~3%) and continues demonstrate strong ICL capabilities."* The maximum degradation observed was 3% (spelling correction 2-shot: 94.6% to 91.6%), with most tasks showing 0.2-1% changes.

#### 2c. Finding 2 states context can be beneficial when relevant: CONFIRMED

Finding 2 reads: **"'Distracting' context prompts can be beneficial when relevant."** The elaboration states: *"While the probabilities and logits of the distracting tokens consistently increase, the direction of change for the correct token varies based on topic relevance"* and that contextual information *"can be beneficial, increasing the likelihood that the model generates the correct response."*

#### 2d. Entrainment heads "not strongly related to how LMs process and utilise contextual information or perform ICL more broadly": CONFIRMED

The exact quote from the paper is: *"this 'circuit' of entrainment heads collectively corresponds to contextual entrainment rather than other capabilities and phenomena, such as factual recall, and is **not strongly related to how LMs process and utilise contextual information or perform ICL more broadly**."*

#### 2e. Heads identified across 15 LRE relations: CONFIRMED

From Appendix A: *"As a result, we select 15 relations, with their statistics listed in Table 5."* The 15 relations are: company hq, country capital city, country currency, country language, country largest city, food from country, fruit inside color, fruit outside color, landmark in country, landmark on continent, product by company, star constellation name, task done by tool, task person type, work location.

#### 2f. Code at github.com/frankniujc/entrainment: CONFIRMED

The [repository](https://github.com/frankniujc/entrainment) exists and is active (13 stars, 2 forks, MIT license). It contains `entrainment.ipynb` (end-to-end notebook for all findings), `head_search.py` (entrainment head identification script), and a `data/lre_dataset` folder. The paper's abstract footnote states: *"The code and data of this work can be found at https://github.com/frankniujc/entrainment."*

### 3. Follow-up work and concurrent papers on training-time fixes

**Citations:** Google Scholar shows approximately 12 papers citing this work as of May 2026.

**Direct follow-up on entrainment (analytical, not training-time fix):**
- [**"Better and Worse with Scale: How Contextual Entrainment Diverges with Model Size"**](https://arxiv.org/abs/2604.13275) (Kukreja et al., April 2026, arXiv:2604.13275) -- Provides the first scaling laws for contextual entrainment across Cerebras-GPT (111M-13B) and Pythia (410M-12B) families. Key finding: semantic entrainment *decreases* with scale while non-semantic (mechanical copying) entrainment *increases* with scale. This is purely analytical; **no training-time fixes proposed**.

**Concurrent work on LLM distraction (not directly building on entrainment heads):**
- [**"Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search"**](https://arxiv.org/abs/2502.01609) (Feb 2025, arXiv:2502.01609) -- Uses tree search to generate adversarial distractions. Finds that **post-training approaches (e.g., DPO) significantly enhance contextual robustness**, while prompt-based methods yield limited gains. This is the closest to a "training-time fix" but targets distraction broadly, not entrainment heads specifically, and it is not clear whether it cites the Niu et al. paper.

**Related mechanistic work (not specifically addressing entrainment):**
- "Which Attention Heads Matter for In-Context Learning?" (arXiv:2502.14010) -- Compares induction heads vs. function vector heads for ICL.
- "Induction Head Toxicity Mechanistically Explains..." (arXiv:2505.13514) -- Examines problematic induction head behavior.

**The paper itself explicitly defers mitigation to future work:** *"we do not propose an application to mitigate the distraction problem. We believe our findings serve as foundational steps toward addressing this issue...we leave such applications for future research."*

**Summary on training-time fixes:** No published work as of May 2026 specifically proposes training-time interventions targeting entrainment heads. The Adaptive Distraction paper shows DPO can help with distraction robustness generally, and the Kukreja et al. scaling paper suggests the problem may not be resolvable through scaling alone (non-semantic entrainment gets worse with scale), but neither directly operationalizes the entrainment head findings into a training fix.

---

Sources:
- [arXiv:2505.09338 - Llama See, Llama Do](https://arxiv.org/abs/2505.09338)
- [arXiv HTML version](https://arxiv.org/html/2505.09338v2)
- [ACL Anthology entry](https://aclanthology.org/2025.acl-long.791/)
- [ACL 2025 Awards page](https://2025.aclweb.org/program/awards/)
- [GitHub: frankniujc/entrainment](https://github.com/frankniujc/entrainment)
- [arXiv:2604.13275 - Better and Worse with Scale](https://arxiv.org/abs/2604.13275)
- [arXiv:2502.01609 - Adaptive Distraction](https://arxiv.org/abs/2502.01609)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20b000ac-4482-4418-b87e-5605656f62e2",
  "isSidechain": true,
  "agentId": "ae871ea085ea00f36",
  "requestId": "req_011Cb7s6axPjJmYH51G6dnvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96ae5424-074a-4ddc-87f2-337005ed3536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQNdnp8fJ2vUU11JizV2pz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 23061,
      "output_tokens": 1889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 542
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1889,
          "cache_read_input_tokens": 23061,
          "cache_creation_input_tokens": 542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 542,
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
