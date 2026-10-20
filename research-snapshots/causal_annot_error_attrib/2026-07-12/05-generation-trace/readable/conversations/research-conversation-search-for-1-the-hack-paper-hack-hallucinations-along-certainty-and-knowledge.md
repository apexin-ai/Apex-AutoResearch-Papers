# Research conversation: Search for: 1. The HACK paper - "HACK: Hallucinations Along Certainty and Knowledge Axes" by Simhi et al., arxiv 2510.24

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a76a6d0f00c5bf550.jsonl`
- **Structured JSON:** [`71ba242496cd70e71ba7.json`](../../sessions/71/71ba242496cd70e71ba7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-16T10:13:37.003Z_

Search for:

1. The HACK paper - "HACK: Hallucinations Along Certainty and Knowledge Axes" by Simhi et al., arxiv 2510.24222. Verify:
- Does it exist?
- Who are the authors? (Previous review said the generator incorrectly attributed this to "Uehara et al." - check if this is now fixed to "Simhi et al.")
- What does it propose?

Search: "arxiv 2510.24222", "HACK hallucinations certainty knowledge axes"

2. Also verify the original CHOKE paper: "Trust Me, I'm Wrong" by Simhi et al., arxiv 2502.12964, Findings of EMNLP 2025. Search: "arxiv 2502.12964"

3. Verify EACL 2027 deadline claims. The proposal now targets "EACL 2027 (ARR August 3, 2026 deadline)". Search for:
- "EACL 2027 submission deadline"
- "ARR August 2026 deadline"
- "ACL Rolling Review 2026 schedule"

Report what you find for each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a76a6d0f00c5bf550",
  "type": "user",
  "uuid": "8f51a033-77e0-4c3a-8290-157150e034ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T10:13:37.006Z_

```json
{
  "parentUuid": "8f51a033-77e0-4c3a-8290-157150e034ca",
  "isSidechain": true,
  "agentId": "a76a6d0f00c5bf550",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7f50b972-0ef2-4a2b-a901-0822c1ec9c1b",
  "timestamp": "2026-05-16T10:13:37.006Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T10:13:39.387Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01R4cGkpJ6ZXutTtoMVqxNoT`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f50b972-0ef2-4a2b-a901-0822c1ec9c1b",
  "isSidechain": true,
  "agentId": "a76a6d0f00c5bf550",
  "requestId": "req_011Cb653iB2Zt1RUq7Wu7Ymf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca35c677-9ab7-4703-bbad-0ae76a1f05b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFK1KjXiUMLHdSBn3WzR9M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 825,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 825
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 825,
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

_source line 4 · 2026-05-16T10:13:39.390Z_

<details><summary>↩ Tool result · `toolu_01R4cGkpJ6ZXutTtoMVqxNoT`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca35c677-9ab7-4703-bbad-0ae76a1f05b8",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a76a6d0f00c5bf550",
  "type": "user",
  "uuid": "3ddf0d81-ca52-44eb-9408-6e685e9847fa",
  "sourceToolAssistantUUID": "ca35c677-9ab7-4703-bbad-0ae76a1f05b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T10:13:44.395Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PGhp3Vu2cDvFMwuRxTyyqH`</summary>

```json
{
  "query": "arxiv 2510.24222 HACK hallucinations certainty knowledge axes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ddf0d81-ca52-44eb-9408-6e685e9847fa",
  "isSidechain": true,
  "agentId": "a76a6d0f00c5bf550",
  "requestId": "req_011Cb653tYcZJipbikTr7r2K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebd838a7-3820-44d0-a52c-0304436c081f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhkrU3Nxv3JbkAboRGyKqg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 6 · 2026-05-16T10:13:44.874Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V4nN4uyN8hRVakLcS2da7h`</summary>

```json
{
  "query": "arxiv 2502.12964 \"Trust Me I'm Wrong\" Simhi CHOKE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebd838a7-3820-44d0-a52c-0304436c081f",
  "isSidechain": true,
  "agentId": "a76a6d0f00c5bf550",
  "requestId": "req_011Cb653tYcZJipbikTr7r2K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66389716-b95c-4548-9750-c794bb4247fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhkrU3Nxv3JbkAboRGyKqg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 7 · 2026-05-16T10:13:44.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016BS2mUreh9YAeakv3qmjnB`</summary>

```json
{
  "query": "EACL 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66389716-b95c-4548-9750-c794bb4247fa",
  "isSidechain": true,
  "agentId": "a76a6d0f00c5bf550",
  "requestId": "req_011Cb653tYcZJipbikTr7r2K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25258768-3e7a-4de9-9b02-b3475fec401c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhkrU3Nxv3JbkAboRGyKqg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9048,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 170,
          "cache_read_input_tokens": 9048,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 8 · 2026-05-16T10:13:49.019Z_

<details><summary>↩ Tool result · `toolu_016BS2mUreh9YAeakv3qmjnB`</summary>

```text
Web search results for query: "EACL 2027 submission deadline"

Links: [{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR BIDS TO HOST EACL 2027 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-bids-host-eacl-2027"},{"title":"EACL 2027 Call for Main Conference Papers","url":"https://2027.eacl.org/calls/papers/"},{"title":"eaclmeeting on X: \"📢⚠️ IMPORTANT DATE CORRECTION: the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle! 📚 All areas of CL/NLP + related fields welcome. Full CfP coming soon. #NLProc #EACL2027\" / X","url":"https://x.com/eaclmeeting/status/2051971432171688436"},{"title":"EACL: Conference of the European Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=785"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 36.2662 FYI: Call for Bids to Host the European Chapter of the Association for Computational Linguistics (EACL) Conference 2027 (Online)","url":"https://linguistlist.org/issues/36/2662/"},{"title":"EACL","url":"https://eacl.org/"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"}]

Based on the search results, here's the submission deadline information for EACL 2027:

The ARR submission deadline (long & short papers) for EACL 2027 is August 3, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

It's worth noting that this is an important correction from a previously announced date of August 6, as EACL 2027 is earlier than usual, making this the only viable ARR cycle. EACL 2027 will be held in Athens, Greece, from March 9–14, 2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25258768-3e7a-4de9-9b02-b3475fec401c",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a76a6d0f00c5bf550",
  "type": "user",
  "uuid": "decb8615-9c5c-45cb-9c61-5ae643cf9543",
  "sourceToolAssistantUUID": "25258768-3e7a-4de9-9b02-b3475fec401c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T10:13:52.128Z_

<details><summary>↩ Tool result · `toolu_01PGhp3Vu2cDvFMwuRxTyyqH`</summary>

```text
Web search results for query: "arxiv 2510.24222 HACK hallucinations certainty knowledge axes"

Links: [{"title":"[2510.24222] HACK: Hallucinations Along Certainty and Knowledge Axes","url":"https://arxiv.org/abs/2510.24222"},{"title":"HACK: Hallucinations Along Certainty and Knowledge Axes","url":"https://arxiv.org/html/2510.24222"},{"title":"Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/html/2502.12964v2"},{"title":"Trust Me, I’m Wrong: High-Certainty Hallucinations in LLMs","url":"https://arxiv.org/html/2502.12964v1"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"Multi-Modal Fact-Verification Framework for Reducing Hallucinations in Large Language Models","url":"https://arxiv.org/html/2510.22751"},{"title":"Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration","url":"https://arxiv.org/html/2603.22812v1"},{"title":"[2510.14665v1] Beyond Hallucinations: The Illusion of Understanding in Large Language Models","url":"https://arxiv.org/abs/2510.14665v1"},{"title":"Credal Transformer: A Principled Approach for Quantifying and Mitigating Hallucinations in Large Language Models","url":"https://arxiv.org/html/2510.12137"},{"title":"[2512.00663] Graphing the Truth: Structured Visualizations for Automated Hallucination Detection in LLMs","url":"https://arxiv.org/abs/2512.00663"}]

Based on the search results, here's what I found about arxiv paper 2510.24222:

## HACK: Hallucinations Along Certainty and Knowledge Axes

The paper is titled "HACK: Hallucinations Along Certainty and Knowledge Axes" and was submitted on October 28, 2025 by Adi Simhi, Jonathan Herzig, Itay Itzhak, Dana Arad, Zorik Gekhman, Roi Reichart, Fazl Barez, Gabriel Stanovsky, Idan Szpektor, and Yonatan Belinkov.

### Main Contribution

The paper proposes a framework for categorizing hallucinations along two axes: knowledge and certainty. Existing research usually categorizes hallucinations by their external properties rather than by the LLMs' underlying internal properties.

### Knowledge Axis

Along the knowledge axis, the researchers distinguish between hallucinations caused by a lack of knowledge and those occurring despite the model having the knowledge of the correct response. To validate their framework along the knowledge axis, they apply steering mitigation, which relies on the existence of parametric knowledge to manipulate model activations, addressing the lack of existing methods to validate knowledge categorization by showing a significant difference between the two hallucination types.

### Certainty Axis

Regarding the certainty axis, they identify a particularly concerning subset of hallucinations where models hallucinate with certainty despite having the correct knowledge internally, and introduce a new evaluation metric to measure the effectiveness of mitigation methods on this subset, revealing that while some methods perform well on average, they fail disproportionately on these critical cases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebd838a7-3820-44d0-a52c-0304436c081f",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a76a6d0f00c5bf550",
  "type": "user",
  "uuid": "d112b2c9-5357-4ac0-ab93-ebd38a6215d3",
  "sourceToolAssistantUUID": "ebd838a7-3820-44d0-a52c-0304436c081f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T10:13:53.378Z_

<details><summary>↩ Tool result · `toolu_01V4nN4uyN8hRVakLcS2da7h`</summary>

```text
Web search results for query: "arxiv 2502.12964 "Trust Me I'm Wrong" Simhi CHOKE"

Links: [{"title":"Trust Me, I’m Wrong: High-Certainty Hallucinations in LLMs","url":"https://arxiv.org/html/2502.12964v1"},{"title":"[2502.12964] Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/abs/2502.12964"},{"title":"Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/pdf/2502.12964"},{"title":"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250212964S/abstract"},{"title":"Adventures in Automation: When I Sound Confident But Have No Source, A Note from Claude","url":"https://www.tjmaher.com/2026/05/when-i-sound-confident-but-have-no.html"},{"title":"Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.792/"},{"title":"Aletheia: Quantifying Cognitive Conviction in Reasoning ...","url":"https://www.arxiv.org/pdf/2601.01532"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=135&show=2000"},{"title":"Adi Simhi","url":"https://scholar.google.com/citations?user=64Ba4bcAAAAJ&hl=en"},{"title":"Computer Science Feb 2025","url":"https://www.arxiv.org/list/cs/2025-02?skip=4550&show=2000"}]

I found the paper you were searching for! Here's what I found:

## Paper Overview

"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer" is an arXiv paper (2502.12964) by Adi Simhi and colleagues.

## Main Contribution

The paper defines and investigates a distinct type of hallucination where a model can consistently answer a question correctly, but a seemingly trivial perturbation causes it to produce a hallucinated response with high certainty.

## CHOKE Phenomenon

This phenomenon is called CHOKE (Certain Hallucinations Overriding Known Evidence), and is particularly concerning in high-stakes domains such as medicine or law, where model certainty is often used as a proxy for reliability.

## Key Findings

CHOKE examples are consistent across prompts, occur in different models and datasets, and are fundamentally distinct from other hallucinations. Existing mitigation methods perform worse on CHOKE examples than on general hallucinations, though the authors introduce a probing-based mitigation that outperforms existing methods on CHOKE hallucinations.

The paper was published in the Findings of the Association for Computational Linguistics: EMNLP 2025 (pages 14665–14688) in Suzhou, China.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66389716-b95c-4548-9750-c794bb4247fa",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a76a6d0f00c5bf550",
  "type": "user",
  "uuid": "309698fe-6f0a-44bb-9a3d-fce59906e8aa",
  "sourceToolAssistantUUID": "66389716-b95c-4548-9750-c794bb4247fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T10:13:57.145Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013EA7TYhYqZ9nTvvUwWUbN4`</summary>

```json
{
  "query": "ARR August 2026 deadline \"ACL Rolling Review\" 2026 schedule"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "309698fe-6f0a-44bb-9a3d-fce59906e8aa",
  "isSidechain": true,
  "agentId": "a76a6d0f00c5bf550",
  "requestId": "req_011Cb654v9PSgfvSThiFLDas",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80df6263-2b67-47fd-8f86-81e7d3be4935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwoNYAY7ev24kdSw5mP6mv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 10440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 12 · 2026-05-16T10:13:57.407Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eq6qUkX4qW3QscS5KNge81`</summary>

```json
{
  "query": "arxiv 2510.24222 authors Simhi Uehara"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80df6263-2b67-47fd-8f86-81e7d3be4935",
  "isSidechain": true,
  "agentId": "a76a6d0f00c5bf550",
  "requestId": "req_011Cb654v9PSgfvSThiFLDas",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4a711a5-c7dd-4c2a-9d2a-ecefe1b9738e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwoNYAY7ev24kdSw5mP6mv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 10440,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 733,
          "output_tokens": 121,
          "cache_read_input_tokens": 10440,
          "cache_creation_input_tokens": 1909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1909,
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

_source line 13 · 2026-05-16T10:14:03.395Z_

<details><summary>↩ Tool result · `toolu_01Eq6qUkX4qW3QscS5KNge81`</summary>

```text
Web search results for query: "arxiv 2510.24222 authors Simhi Uehara"

Links: [{"title":"[2510.24222] HACK: Hallucinations Along Certainty and Knowledge Axes","url":"https://arxiv.org/abs/2510.24222"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=3300&show=100"},{"title":"Computer Science authors/titles Oct 2018 (800 skipped)","url":"https://arxiv.org/list/cs/1810?skip=800&show=250"},{"title":"Computer Science authors/titles recent submissions (1597 skipped)","url":"https://aps.arxiv.org/list/cs/pastweek?skip=1597&show=50"},{"title":"[2510.00857] ManagerBench: Evaluating the Safety-Pragmatism Trade-off in Autonomous LLMs","url":"https://arxiv.org/abs/2510.00857"},{"title":"[2510.25786] BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection","url":"https://arxiv.org/abs/2510.25786"},{"title":"Software Engineering authors/titles Dec 2019 (15 skipped)","url":"https://arxiv.org/list/cs.SE/1912?skip=15"},{"title":"Masatoshi Uehara","url":"https://scholar.google.com/citations?user=xuLKJboAAAAJ&hl=en"},{"title":"Computer Science authors/titles recent submissions - arXiv","url":"https://aps.arxiv.org/list/cs/pastweek?show=1331"},{"title":"Computer Science Oct 2025","url":"https://arxiv.org/list/cs/2025-10"}]

Based on the search results, arxiv paper 2510.24222 is titled "HACK: Hallucinations Along Certainty and Knowledge Axes" and has authors: Adi Simhi, Jonathan Herzig, Itay Itzhak, Dana Arad, Zorik Gekhman, Roi Reichart, Fazl Barez, Gabriel Stanovsky, Idan Szpektor, and Yonatan Belinkov.

Note: The search query included "Uehara" as a potential author, but Uehara does not appear to be among the authors of this paper. The paper's focus is on proposing a framework for categorizing hallucinations along two axes: knowledge and certainty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4a711a5-c7dd-4c2a-9d2a-ecefe1b9738e",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a76a6d0f00c5bf550",
  "type": "user",
  "uuid": "ba9d59f2-8f8e-48a2-bd7b-ecce823fccac",
  "sourceToolAssistantUUID": "b4a711a5-c7dd-4c2a-9d2a-ecefe1b9738e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T10:14:03.471Z_

<details><summary>↩ Tool result · `toolu_013EA7TYhYqZ9nTvvUwWUbN4`</summary>

```text
Web search results for query: "ARR August 2026 deadline "ACL Rolling Review" 2026 schedule"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"}]

Based on the search results, I found information about the August 2026 deadline in the ARR 2026 schedule:

For EMNLP 2026, the final ARR submission date is May 25, 2026, with a commitment date of August 2, 2026. For AACL 2026, the final ARR submission date is May 25, 2026, with a commitment date of August 26, 2026.

These August 2026 dates are commitment deadlines—the deadlines by which authors must commit their papers (along with their ARR reviews) to these specific conference venues.

The ACL Peer Review Committee recommended switching from 8-week to 10-week review cycles, which became effective starting in May 2025. This means that instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks and author response.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80df6263-2b67-47fd-8f86-81e7d3be4935",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a76a6d0f00c5bf550",
  "type": "user",
  "uuid": "d70da636-e526-4417-b73c-9b80bc939b6d",
  "sourceToolAssistantUUID": "80df6263-2b67-47fd-8f86-81e7d3be4935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-16T10:14:25.796Z_

Here are my findings for each item:

---

## 1. HACK Paper (arxiv 2510.24222)

**Does it exist?** Yes. The paper is real and accessible on arXiv.

**Title:** "HACK: Hallucinations Along Certainty and Knowledge Axes"

**Authors:** Adi Simhi, Jonathan Herzig, Itay Itzhak, Dana Arad, Zorik Gekhman, Roi Reichart, Fazl Barez, Gabriel Stanovsky, Idan Szpektor, and Yonatan Belinkov.

**Attribution check:** The authors are indeed Simhi et al. (first author: Adi Simhi). There is NO connection to "Uehara et al." -- that was an incorrect attribution. If a previous review version cited this as "Uehara et al.", that was wrong and should be corrected to "Simhi et al."

**What it proposes:** HACK introduces a framework for categorizing LLM hallucinations along two axes:
- **Knowledge axis:** Distinguishes hallucinations caused by lack of knowledge vs. those occurring despite the model having the correct knowledge internally. They validate this using steering-based mitigation.
- **Certainty axis:** Identifies a particularly dangerous subset where models hallucinate with high certainty despite having the correct knowledge. They introduce a new evaluation metric to measure mitigation effectiveness on this subset, revealing that existing methods fail disproportionately on these critical cases.

---

## 2. CHOKE Paper (arxiv 2502.12964)

**Does it exist?** Yes. The paper is real and published.

**Title:** "Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer"

**Authors:** Adi Simhi et al. (same first author as HACK -- this is the predecessor paper)

**Venue:** Findings of EMNLP 2025 (pages 14665-14688), held in Suzhou, China. This is confirmed via the [ACL Anthology listing](https://aclanthology.org/2025.findings-emnlp.792/).

**What it proposes:** Defines and investigates the CHOKE (Certain Hallucinations Overriding Known Evidence) phenomenon -- where a model can consistently answer a question correctly, but a trivial perturbation causes it to produce a hallucinated response with high certainty. CHOKE examples are consistent across prompts, occur in different models/datasets, and are fundamentally distinct from other hallucinations. They introduce a probing-based mitigation that outperforms existing methods on CHOKE hallucinations.

**Relationship to HACK:** HACK (2510.24222) is clearly the follow-up work that generalizes the CHOKE phenomenon into a broader two-axis framework.

---

## 3. EACL 2027 Deadline Claims

**Claim to verify:** "EACL 2027 (ARR August 3, 2026 deadline)"

**Finding: CONFIRMED.** This is accurate.

- **EACL 2027** will be held in Athens, Greece, March 9-14, 2027.
- The **ARR submission deadline** for EACL 2027 is **August 3, 2026** (11:59PM UTC-12:00, "anywhere on Earth").
- There was an official correction from a previously announced date of August 6 to August 3 -- the EACL official Twitter account noted this is the **only viable ARR cycle** for EACL 2027 because the conference is earlier than usual.
- The ARR system in 2026 operates on 10-week review cycles (changed from 8-week cycles starting May 2025), so there are approximately 5 cycles per year.

The proposal's claim of targeting "EACL 2027 (ARR August 3, 2026 deadline)" is factually correct.

---

## Summary

| Item | Status |
|------|--------|
| HACK paper exists | Confirmed |
| HACK authors = Simhi et al. | Confirmed (NOT Uehara et al.) |
| CHOKE paper exists at Findings of EMNLP 2025 | Confirmed |
| EACL 2027 ARR August 3, 2026 deadline | Confirmed |

Sources:
- [HACK: Hallucinations Along Certainty and Knowledge Axes (arxiv 2510.24222)](https://arxiv.org/abs/2510.24222)
- [Trust Me, I'm Wrong (arxiv 2502.12964)](https://arxiv.org/abs/2502.12964)
- [Trust Me, I'm Wrong - ACL Anthology (Findings of EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.792/)
- [EACL 2027 Official Website](https://2027.eacl.org/)
- [EACL 2027 Call for Papers](https://2027.eacl.org/calls/papers/)
- [EACL date correction tweet (ARR Aug 3, 2026)](https://x.com/eaclmeeting/status/2051971432171688436)
- [ACL Rolling Review Dates and Venues](http://aclrollingreview.org/dates)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d70da636-e526-4417-b73c-9b80bc939b6d",
  "isSidechain": true,
  "agentId": "a76a6d0f00c5bf550",
  "requestId": "req_011Cb655fJCEPkEWoSmy3ipw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a1213e4-e3a7-4d27-a673-024e472c38c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RYpi6v8jmzLqJLB7jLPD2p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 671,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 12349,
      "output_tokens": 1283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1589
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 671,
          "output_tokens": 1283,
          "cache_read_input_tokens": 12349,
          "cache_creation_input_tokens": 1589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1589,
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
