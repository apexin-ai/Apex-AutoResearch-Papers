# Research conversation: Search the web for the paper "An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning" with a

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ade6ff91ac9e1dd8d.jsonl`
- **Structured JSON:** [`cd20fbe0ed9803ccca1f.json`](../../sessions/cd/cd20fbe0ed9803ccca1f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-13T19:39:31.756Z_

Search the web for the paper "An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning" with arXiv ID 2504.13368. I need to verify: (1) Does this paper actually exist? (2) Was it actually accepted at ICLR 2025? (3) What exactly does it do? Search on arxiv.org, openreview.net, and Google Scholar. Also search for "IDRL discriminator weighted imitation ICLR 2025". Report what you find with URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ade6ff91ac9e1dd8d",
  "type": "user",
  "uuid": "8a570ed8-a14d-4a2c-afec-8849980c14de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T19:39:31.758Z_

```json
{
  "parentUuid": "8a570ed8-a14d-4a2c-afec-8849980c14de",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
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
  "uuid": "2ce8ca4c-62ad-4447-b9da-a0efb7daf7d8",
  "timestamp": "2026-05-13T19:39:31.758Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T19:39:34.095Z_



I'll search multiple sources to verify this paper. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ce8ca4c-62ad-4447-b9da-a0efb7daf7d8",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18muwxMUe3ij96dRMtx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7bc202f-fe90-4c50-9fce-4a06061ba87e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNsycQFR38vKNSb35v1Rj4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 663,
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

_source line 4 · 2026-05-13T19:39:34.206Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KqhfTJRMBJFBWEgTbUdPQf`</summary>

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
  "parentUuid": "f7bc202f-fe90-4c50-9fce-4a06061ba87e",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18muwxMUe3ij96dRMtx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a638e456-8848-48c8-ab82-0b8a0911f863",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNsycQFR38vKNSb35v1Rj4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 663,
      "cache_read_input_tokens": 8223,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 663
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 663,
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

_source line 5 · 2026-05-13T19:39:34.210Z_

<details><summary>↩ Tool result · `toolu_01KqhfTJRMBJFBWEgTbUdPQf`</summary>

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
  "parentUuid": "a638e456-8848-48c8-ab82-0b8a0911f863",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ade6ff91ac9e1dd8d",
  "type": "user",
  "uuid": "ae75b6b5-fb42-40de-a149-871afe1d329e",
  "sourceToolAssistantUUID": "a638e456-8848-48c8-ab82-0b8a0911f863",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T19:39:37.536Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae75b6b5-fb42-40de-a149-871afe1d329e",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18n6xjo4BGA6N4yELSA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05294412-2304-4865-ba4d-7f575b961db0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hmhpf9sGdmY1wLj7J2PiMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 7 · 2026-05-13T19:39:39.197Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uyn1wvVqQswgyvZcDC5AYZ`</summary>

```json
{
  "query": "arxiv 2504.13368 \"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning\"",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05294412-2304-4865-ba4d-7f575b961db0",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18n6xjo4BGA6N4yELSA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76cb5975-2011-4d7e-b9f4-78769ebf259a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hmhpf9sGdmY1wLj7J2PiMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 8 · 2026-05-13T19:39:40.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011xgdQVDUkx1dPkSgw5Trpj`</summary>

```json
{
  "query": "\"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning\" ICLR 2025 openreview",
  "allowed_domains": [
    "openreview.net"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76cb5975-2011-4d7e-b9f4-78769ebf259a",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18n6xjo4BGA6N4yELSA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f751bfe5-52e0-4cee-a1ef-24ec7224d375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hmhpf9sGdmY1wLj7J2PiMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 9 · 2026-05-13T19:39:40.497Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RrEGUSTwRm2DHpJRFEymZo`</summary>

```json
{
  "query": "\"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning\" site:scholar.google.com OR site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f751bfe5-52e0-4cee-a1ef-24ec7224d375",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18n6xjo4BGA6N4yELSA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14c9f350-a640-4dec-b9ee-aaf04147776f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hmhpf9sGdmY1wLj7J2PiMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 10 · 2026-05-13T19:39:41.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D54pDf55DvYVNJLbtq2LGE`</summary>

```json
{
  "query": "IDRL discriminator weighted imitation ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14c9f350-a640-4dec-b9ee-aaf04147776f",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18n6xjo4BGA6N4yELSA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee20102e-c351-4113-b13a-beab9edaa9f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hmhpf9sGdmY1wLj7J2PiMQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8886,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1914
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 323,
          "cache_read_input_tokens": 8886,
          "cache_creation_input_tokens": 1914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1914,
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

_source line 11 · 2026-05-13T19:39:47.763Z_

<details><summary>↩ Tool result · `toolu_01Uyn1wvVqQswgyvZcDC5AYZ`</summary>

```text
Web search results for query: "arxiv 2504.13368 "An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning""

Links: [{"title":"[2504.13368] An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://arxiv.org/abs/2504.13368"},{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://arxiv.org/html/2504.13368"},{"title":"[2207.10050] Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/abs/2207.10050"},{"title":"Robust Offline Imitation Learning from Diverse Auxiliary Data","url":"https://arxiv.org/html/2410.03626"},{"title":"Imitating from auxiliary imperfect demonstrations via Adversarial Density Weighted Regression","url":"https://arxiv.org/html/2405.20351"},{"title":"Adversarial Imitation Learning via Boosting","url":"https://arxiv.org/html/2404.08513v1"},{"title":"[2207.10050v1] Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/abs/2207.10050v1"},{"title":"Imitation Learning from Suboptimal Demonstrations via Meta-Learning An Action Ranker","url":"https://arxiv.org/html/2412.20193v1"},{"title":"Proceedings of Machine Learning Research vol 242:1–15, 2024","url":"https://arxiv.org/pdf/2405.13193v1"},{"title":"Offline Imitation Learning with Variational Counterfactual Reasoning","url":"https://arxiv.org/html/2310.04706v4"}]

I found the paper you're searching for! Here's what I found:

## arxiv 2504.13368: "An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning"

The paper introduces Iterative Dual Reinforcement Learning (IDRL), a new method that takes an optimal discriminator-weighted imitation view of solving RL.

**Key Motivation and Approach:**

The method is motivated by a simple experiment in which training a discriminator using the offline dataset plus an additional expert dataset and then performing discriminator-weighted behavior cloning gives strong results on various types of datasets.

**Main Contributions:**

The optimal discriminator weight is quite similar to the learned visitation distribution ratio in Dual-RL, however, the authors find that current Dual-RL methods do not correctly estimate that ratio. In IDRL, they propose a correction method to iteratively approach the optimal visitation distribution ratio in the offline dataset given no additional expert dataset.

During each iteration, IDRL removes zero-weight suboptimal transitions using the learned ratio from the previous iteration and runs Dual-RL on the remaining subdataset.

**Paper Details:**
- **arXiv ID:** 2504.13368
- **Submitted:** April 17, 2025
- **Authors:** Haoran Xu, Shuozhe Li, Harshit Sikchi, Scott Niekum, Amy Zhang

You can access the full paper at https://arxiv.org/abs/2504.13368 or view the HTML version at https://arxiv.org/html/2504.13368


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76cb5975-2011-4d7e-b9f4-78769ebf259a",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ade6ff91ac9e1dd8d",
  "type": "user",
  "uuid": "31ba549c-f8dc-402b-b29b-e48f25275307",
  "sourceToolAssistantUUID": "76cb5975-2011-4d7e-b9f4-78769ebf259a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T19:39:48.403Z_

<details><summary>↩ Tool result · `toolu_011xgdQVDUkx1dPkSgw5Trpj`</summary>

```text
Web search results for query: ""An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning" ICLR 2025 openreview"

Links: [{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=9JtG4nN7ql"},{"title":"AN OPTIMAL DISCRIMINATOR WEIGHTED IMITATION ...","url":"https://openreview.net/pdf/599e783547a2ce1b35d5540a0162a0641b26f45b.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=0e2pcSxQJS"},{"title":"Under review as a conference paper at ICLR 2022 DISCRIMINATOR-WEIGHTED OFFLINE","url":"https://openreview.net/pdf?id=hW2kwAcXq5w"},{"title":"LATENT WASSERSTEIN ADVERSARIAL IMITATION ...","url":"https://openreview.net/pdf/7cc335b28c298ed15d76132f114fd460758b2ae6.pdf"},{"title":"Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations | OpenReview","url":"https://openreview.net/forum?id=hW2kwAcXq5w"},{"title":"LEARNING A DENSE REASONING REWARD MODEL","url":"https://openreview.net/pdf/d3f758c7684267fa1b220430337488e1bf8e752d.pdf"},{"title":"RILE: REINFORCED IMITATION LEARNING","url":"https://openreview.net/pdf/e1c6d07c3f9a57cd479657d6be0561d4590b771b.pdf"},{"title":"ICLR 2025 Conference Submissions","url":"https://openreview.net/submissions?page=324&venue=ICLR.cc/2025/Conference"},{"title":"Published as a conference paper at ICLR 2020 IMITATION LEARNING VIA OFF-POLICY","url":"https://openreview.net/pdf?id=Hyg-JC4FDr"}]

I found the paper you're looking for! Here's what I found:

## Paper Information

The paper "An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning" was published as a conference paper at ICLR 2025 by authors Haoran Xu, Shuozhe Li, Harshit Sikchi, Scott Niekum, and Amy Zhang from the University of Texas at Austin, UMass Amherst, and Meta AI.

## Overview

The paper introduces Iterative Dual Reinforcement Learning (IDRL), a new method that takes an optimal discriminator-weighted imitation view of solving RL. 

The method is motivated by an experiment where training a discriminator using the offline dataset plus an additional expert dataset and then performing discriminator-weighted behavior cloning gives strong results on various types of datasets.

## Key Contribution

In IDRL, the authors propose a correction method to iteratively approach the optimal visitation distribution ratio in the offline dataset given no additional expert dataset. During each iteration, IDRL removes zero-weight suboptimal transitions using the learned ratio from the previous iteration and runs Dual-RL on the remaining subdataset.

## Results

The effectiveness of IDRL is verified on various kinds of offline datasets, including D4RL datasets and more realistic corrupted demonstrations, and IDRL beats strong Primal-RL and Dual-RL baselines in terms of both performance and stability on all datasets.

The paper is available on OpenReview at https://openreview.net/forum?id=9JtG4nN7ql


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f751bfe5-52e0-4cee-a1ef-24ec7224d375",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ade6ff91ac9e1dd8d",
  "type": "user",
  "uuid": "130075ba-023a-4e86-b331-891b970788ee",
  "sourceToolAssistantUUID": "f751bfe5-52e0-4cee-a1ef-24ec7224d375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T19:39:50.153Z_

<details><summary>↩ Tool result · `toolu_01D54pDf55DvYVNJLbtq2LGE`</summary>

```text
Web search results for query: "IDRL discriminator weighted imitation ICLR 2025"

Links: [{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/3ef61f7e4afacf9a2c5b71c726172b86-Abstract-Conference.html"},{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=9JtG4nN7ql"},{"title":"[2504.13368] An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://arxiv.org/abs/2504.13368"},{"title":"AN OPTIMAL DISCRIMINATOR WEIGHTED IMITATION ...","url":"https://openreview.net/pdf/599e783547a2ce1b35d5540a0162a0641b26f45b.pdf"},{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://arxiv.org/html/2504.13368"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=0e2pcSxQJS"},{"title":"GitHub - moatifbutt/awesome-diffusion-iclr-2025: List of diffusion related active submissions on OpenReview for ICLR 2025. · GitHub","url":"https://github.com/moatifbutt/awesome-diffusion-iclr-2025"},{"title":"GitHub - yunke-wang/dp-il: [ICML 2024] Imitation Learning from Purified Demonstrations · GitHub","url":"https://github.com/yunke-wang/dp-il"},{"title":"arXiv:2506.20307v1 [cs.LG] 25 Jun 2025","url":"https://arxiv.org/pdf/2506.20307"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/3c7435bc2086a5fe2421dfd1dfc6e407-Paper-Conference.pdf"}]

Based on the search results, here's what I found about IDRL and discriminator weighted imitation learning at ICLR 2025:

## IDRL: An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning

Iterative Dual Reinforcement Learning (IDRL) is a new method that takes an optimal discriminator-weighted imitation view of solving RL, presented at ICLR 2025.

### Key Motivation

The method is motivated by a simple experiment in which training a discriminator using the offline dataset plus an additional expert dataset and then performing discriminator-weighted behavior cloning gives strong results on various types of datasets.

### The Core Problem Addressed

The optimal discriminator weight is quite similar to the learned visitation distribution ratio in Dual-RL, however, current Dual-RL methods do not correctly estimate that ratio. IDRL proposes a correction method to iteratively approach the optimal visitation distribution ratio in the offline dataset given no additional expert dataset.

### How IDRL Works

During each iteration, IDRL removes zero-weight suboptimal transitions using the learned ratio from the previous iteration and runs Dual-RL on the remaining subdataset. This can be seen as replacing the behavior visitation distribution with the optimized visitation distribution from the previous iteration, which theoretically gives a curriculum of improved visitation distribution ratios that are closer to the optimal discriminator weight.

### Empirical Results

IDRL's effectiveness has been verified on various kinds of offline datasets, including D4RL datasets and more realistic corrupted demonstrations. IDRL beats strong Primal-RL and Dual-RL baselines in terms of both performance and stability, on all datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee20102e-c351-4113-b13a-beab9edaa9f9",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ade6ff91ac9e1dd8d",
  "type": "user",
  "uuid": "44e4bdd5-1695-44c4-8a73-01af77478b8f",
  "sourceToolAssistantUUID": "ee20102e-c351-4113-b13a-beab9edaa9f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T19:39:52.379Z_

<details><summary>↩ Tool result · `toolu_01RrEGUSTwRm2DHpJRFEymZo`</summary>

```text
Web search results for query: ""An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning" site:scholar.google.com OR site:arxiv.org"

Links: [{"title":"[2504.13368] An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://arxiv.org/abs/2504.13368"},{"title":"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning","url":"https://arxiv.org/html/2504.13368"},{"title":"[2207.10050] Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/abs/2207.10050"},{"title":"Imitation Learning from Suboptimal Demonstrations via Meta-Learning An Action Ranker","url":"https://arxiv.org/html/2412.20193v1"},{"title":"Discriminator-Weighted Ofﬂine Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/pdf/2207.10050"},{"title":"[2207.10050v1] Discriminator-Weighted Offline Imitation Learning from Suboptimal Demonstrations","url":"https://arxiv.org/abs/2207.10050v1"},{"title":"Robust Offline Imitation Learning from Diverse Auxiliary Data","url":"https://arxiv.org/html/2410.03626"},{"title":"Offline Imitation Learning with Variational Counterfactual Reasoning","url":"https://arxiv.org/html/2310.04706v4"},{"title":"RILe: Reinforced Imitation Learning","url":"https://arxiv.org/html/2406.08472v1"},{"title":"Active Third-Person Imitation Learning Timo Klein University of Vienna","url":"https://arxiv.org/pdf/2312.16365"}]

I found the paper you're looking for! 

The paper introduces Iterative Dual Reinforcement Learning (IDRL), a new method that takes an optimal discriminator-weighted imitation view of solving RL. It's authored by Haoran Xu and 4 other authors, and was posted on arxiv on April 17, 2025.

Here's what the paper covers:

**Key Contribution:** The method is motivated by finding that training a discriminator using the offline dataset plus an additional expert dataset and then performing discriminator-weighted behavior cloning gives strong results on various types of datasets.

**Main Innovation:** IDRL proposes a correction method to iteratively approach the optimal visitation distribution ratio in the offline dataset given no additional expert dataset. During each iteration, IDRL removes zero-weight suboptimal transitions using the learned ratio from the previous iteration and runs Dual-RL on the remaining subdataset. This can be seen as replacing the behavior visitation distribution with the optimized visitation distribution from the previous iteration, which theoretically gives a curriculum of improved visitation distribution ratios that are closer to the optimal discriminator weight.

**Results:** The authors verified the effectiveness of IDRL on various kinds of offline datasets, including D4RL datasets and more realistic corrupted demonstrations. IDRL beats strong Primal-RL and Dual-RL baselines in terms of both performance and stability, on all datasets.

You can find the full paper at https://arxiv.org/abs/2504.13368.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14c9f350-a640-4dec-b9ee-aaf04147776f",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ade6ff91ac9e1dd8d",
  "type": "user",
  "uuid": "2c0c8a70-ce0f-4bb0-b806-11f3a48f2a52",
  "sourceToolAssistantUUID": "14c9f350-a640-4dec-b9ee-aaf04147776f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-13T19:39:55.150Z_

Now let me fetch the actual arXiv page and the OpenReview page to get more precise details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c0c8a70-ce0f-4bb0-b806-11f3a48f2a52",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18oS9gDpAVfVw4hrbg8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dee6a2a4-a39e-4d16-84c2-ed903dfd8b06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxuGWTNueHCud81KWWjXBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 10800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3002,
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

_source line 16 · 2026-05-13T19:39:57.193Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019BHBUn52jbA9U2JLmBjZJk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.13368",
  "prompt": "Extract the full title, authors, submission date, abstract, and any mention of ICLR 2025 or conference acceptance. Also note the arXiv categories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dee6a2a4-a39e-4d16-84c2-ed903dfd8b06",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18oS9gDpAVfVw4hrbg8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4c29750-8680-47bb-9e4d-346bab149a56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxuGWTNueHCud81KWWjXBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 10800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3002,
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

_source line 17 · 2026-05-13T19:39:58.614Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JRy6MWVoWmAPvvv5cyLHc1`</summary>

```json
{
  "url": "https://openreview.net/forum?id=9JtG4nN7ql",
  "prompt": "Extract the paper title, authors, venue, acceptance status (was it accepted at ICLR 2025?), ratings, decision, and any key details about the review process."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4c29750-8680-47bb-9e4d-346bab149a56",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18oS9gDpAVfVw4hrbg8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74193599-fe76-4c84-87ed-9b668438e6fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxuGWTNueHCud81KWWjXBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 10800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3002,
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

_source line 18 · 2026-05-13T19:39:59.657Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016yxdDFLGUA5duNJFtrYZ2A`</summary>

```json
{
  "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/3ef61f7e4afacf9a2c5b71c726172b86-Abstract-Conference.html",
  "prompt": "Extract all information about this paper from the ICLR 2025 proceedings page: title, authors, abstract, and any other details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74193599-fe76-4c84-87ed-9b668438e6fe",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18oS9gDpAVfVw4hrbg8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ce03f6d-01b8-4f42-91b2-cd2faeefb6c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxuGWTNueHCud81KWWjXBe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1002,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 10800,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3002
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1002,
          "output_tokens": 379,
          "cache_read_input_tokens": 10800,
          "cache_creation_input_tokens": 3002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3002,
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

_source line 19 · 2026-05-13T19:40:01.294Z_

<details><summary>↩ Tool result · `toolu_019BHBUn52jbA9U2JLmBjZJk`</summary>

```text
# Paper Summary

**Full Title:** "An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning"

**Authors:** Haoran Xu, Shuozhe Li, Harshit Sikchi, Scott Niekum, Amy Zhang

**Submission Date:** April 17, 2025

**arXiv Categories:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

**Conference:** ICLR 2025

**Abstract Summary:**
The paper introduces Iterative Dual Reinforcement Learning (IDRL), which frames RL as an optimization problem using "discriminator-weighted imitation." The key innovation involves training a discriminator on offline and expert datasets, then applying behavior cloning weighted by discriminator outputs. The authors propose an iterative correction method that progressively refines visitation distribution ratios by removing suboptimal transitions, creating what they describe as "a curriculum of improved visitation distribution ratios." Experiments demonstrate IDRL outperforms baseline methods across D4RL datasets and corrupted demonstration scenarios in both performance and stability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4c29750-8680-47bb-9e4d-346bab149a56",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ade6ff91ac9e1dd8d",
  "type": "user",
  "uuid": "03e62085-231c-4c89-bfaa-f1c2ecb720f7",
  "sourceToolAssistantUUID": "b4c29750-8680-47bb-9e4d-346bab149a56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T19:40:03.038Z_

<details><summary>↩ Tool result · `toolu_01JRy6MWVoWmAPvvv5cyLHc1`</summary>

```text
# Paper Summary

**Title:** "An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning"

**Authors:** Haoran Xu, Shuozhe Li, Harshit Sikchi, Scott Niekum, Amy Zhang

**Venue:** ICLR 2025 Conference

**Acceptance Status:** Accepted as a poster paper (published January 22, 2025)

**Ratings/Decision:** The webpage does not display individual reviewer ratings or detailed decision information.

**Key Details:**

The paper introduces Iterative Dual Reinforcement Learning (IDRL), a novel approach that frames RL through "an optimal discriminator-weighted imitation view." The core contribution involves using a discriminator trained on offline data combined with expert demonstrations to guide behavior cloning, then iteratively refining the visitation distribution ratio without requiring additional expert data.

The authors report that IDRL "beats strong Primal-RL and Dual-RL baselines in terms of both performance and stability, on all datasets" tested, including D4RL benchmarks and corrupted demonstrations.

The work is licensed under Creative Commons Attribution 4.0 International and was last modified March 16, 2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74193599-fe76-4c84-87ed-9b668438e6fe",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ade6ff91ac9e1dd8d",
  "type": "user",
  "uuid": "a58d6fd4-aca6-4fa0-be72-23432f73ff2d",
  "sourceToolAssistantUUID": "74193599-fe76-4c84-87ed-9b668438e6fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T19:40:03.687Z_

<details><summary>↩ Tool result · `toolu_016yxdDFLGUA5duNJFtrYZ2A`</summary>

```text
# ICLR 2025 Paper Information

**Title:** An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning

**Authors:** Haoran Xu, Shuozhe Li, Harshit Sikchi, Scott Niekum, Amy Zhang

**Conference:** International Conference on Learning Representations 2025 (ICLR 2025)

**Abstract Summary:**

The researchers introduce Iterative Dual Reinforcement Learning (IDRL), which frames reinforcement learning through the lens of "optimal discriminator-weighted imitation." Their core finding demonstrates that training a discriminator on both offline and expert datasets, then applying discriminator-weighted behavior cloning, yields strong performance across diverse datasets.

The key innovation involves addressing what the authors identify as a limitation in existing Dual-RL approaches: inaccurate estimation of visitation distribution ratios. IDRL employs an iterative refinement strategy, removing suboptimal transitions with zero weights during each cycle and progressively improving the estimated ratio. This process creates what they describe as "a curriculum of improved visitation distribution ratios closer to the optimal discriminator weight."

The method demonstrates superior performance and stability compared to both Primal-RL and Dual-RL baselines when tested on D4RL datasets and corrupted demonstration scenarios.

**Available Resources:** Paper PDF and BibTeX citation available on the proceedings page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ce03f6d-01b8-4f42-91b2-cd2faeefb6c1",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ade6ff91ac9e1dd8d",
  "type": "user",
  "uuid": "b35f9cc4-faaf-4495-8981-a51b9178a9a5",
  "sourceToolAssistantUUID": "6ce03f6d-01b8-4f42-91b2-cd2faeefb6c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-13T19:40:25.363Z_

Here are the findings from searching across all requested sources:

---

## (1) Does the paper exist? -- YES

The paper **"An Optimal Discriminator Weighted Imitation Perspective for Reinforcement Learning"** with arXiv ID **2504.13368** is real and verified across multiple sources:

- **arXiv:** [https://arxiv.org/abs/2504.13368](https://arxiv.org/abs/2504.13368) -- Submitted April 17, 2025. Categories: cs.LG, cs.AI.
- **OpenReview:** [https://openreview.net/forum?id=9JtG4nN7ql](https://openreview.net/forum?id=9JtG4nN7ql)
- **ICLR 2025 Proceedings:** [https://proceedings.iclr.cc/paper_files/paper/2025/hash/3ef61f7e4afacf9a2c5b71c726172b86-Abstract-Conference.html](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3ef61f7e4afacf9a2c5b71c726172b86-Abstract-Conference.html)

**Authors:** Haoran Xu, Shuozhe Li, Harshit Sikchi, Scott Niekum, Amy Zhang (affiliations include UT Austin, UMass Amherst, and Meta AI).

---

## (2) Was it accepted at ICLR 2025? -- YES

The paper was **accepted as a poster at ICLR 2025**. This is confirmed by:

- The OpenReview page explicitly lists it under the ICLR 2025 Conference venue, with acceptance status as a poster paper (published January 22, 2025).
- It appears in the official ICLR 2025 proceedings at `proceedings.iclr.cc`.
- The arXiv page itself notes it as an ICLR 2025 paper.

---

## (3) What does it do?

The paper introduces **Iterative Dual Reinforcement Learning (IDRL)**, a new offline RL method. Here is what it does:

- **Motivating observation:** The authors show that if you train a binary discriminator to distinguish between an offline dataset and an expert dataset, and then use the discriminator's output as weights for behavior cloning (imitation learning), you get surprisingly strong results across many dataset types.

- **Connection to Dual-RL:** They observe that the optimal discriminator weight is mathematically very similar to the visitation distribution ratio learned in Dual-RL methods. However, they find that existing Dual-RL methods do **not** correctly estimate this ratio.

- **The IDRL algorithm:** IDRL proposes an iterative correction procedure to approach the optimal visitation distribution ratio **without requiring an additional expert dataset**. In each iteration, IDRL:
  1. Uses the visitation distribution ratio learned from the previous iteration to identify and **remove zero-weight (suboptimal) transitions** from the dataset.
  2. Runs Dual-RL on the remaining (cleaned) subdataset.
  3. This effectively replaces the behavior visitation distribution with the optimized one from the prior iteration, creating a **curriculum of progressively improved visitation distribution ratios** that converge toward the optimal discriminator weight.

- **Results:** IDRL outperforms strong Primal-RL and Dual-RL baselines in both **performance and stability** across D4RL benchmark datasets and more realistic corrupted demonstration scenarios.

---

## Search for "IDRL discriminator weighted imitation ICLR 2025"

This search confirmed the same paper across all three sources (arXiv, OpenReview, and ICLR proceedings). No ambiguity -- there is exactly one paper matching this description.

---

Sources:
- [arXiv: 2504.13368](https://arxiv.org/abs/2504.13368)
- [arXiv HTML version](https://arxiv.org/html/2504.13368)
- [OpenReview forum](https://openreview.net/forum?id=9JtG4nN7ql)
- [OpenReview PDF](https://openreview.net/pdf/599e783547a2ce1b35d5540a0162a0641b26f45b.pdf)
- [ICLR 2025 Proceedings page](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3ef61f7e4afacf9a2c5b71c726172b86-Abstract-Conference.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b35f9cc4-faaf-4495-8981-a51b9178a9a5",
  "isSidechain": true,
  "agentId": "ade6ff91ac9e1dd8d",
  "requestId": "req_011Cb18pGWGXowAuN1577Lbd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdfe87eb-03da-4ca8-9c4d-3971711a895c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6Au4rK6uWqVBd9SkanLQ8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2288,
      "cache_read_input_tokens": 13802,
      "output_tokens": 1109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2288
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1109,
          "cache_read_input_tokens": 13802,
          "cache_creation_input_tokens": 2288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2288,
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
