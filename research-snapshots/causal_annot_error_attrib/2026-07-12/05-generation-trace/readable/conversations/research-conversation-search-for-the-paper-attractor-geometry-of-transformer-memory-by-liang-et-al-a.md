# Research conversation: Search for the paper "Attractor Geometry of Transformer Memory" by Liang et al., arxiv 2605.05686, May 2026 from MIT. I 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a37938b45de9768d2.jsonl`
- **Structured JSON:** [`b0e4a69903cf1463cf04.json`](../../sessions/b0/b0e4a69903cf1463cf04.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-16T10:13:19.805Z_

Search for the paper "Attractor Geometry of Transformer Memory" by Liang et al., arxiv 2605.05686, May 2026 from MIT. I need to verify:
1. Does this paper exist?
2. Does it argue that the LM head is "blind by design" to high-confidence hallucinations?
3. Does it propose "geometric margin" as a monitoring signal?
4. Does it discuss attractor basins for factual recall?

Use WebSearch to find this paper. Try queries like:
- "arxiv 2605.05686"
- "Attractor Geometry Transformer Memory hallucination"
- "attractor basin LLM factual recall 2026"

Also try WebFetch on https://arxiv.org/abs/2605.05686 if possible.

Report what you find about the paper's existence and claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a37938b45de9768d2",
  "type": "user",
  "uuid": "1f1d534f-7b13-4440-8333-e5c3ec353c93",
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

_source line 2 · 2026-05-16T10:13:19.809Z_

```json
{
  "parentUuid": "1f1d534f-7b13-4440-8333-e5c3ec353c93",
  "isSidechain": true,
  "agentId": "a37938b45de9768d2",
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
  "uuid": "14ed761f-18d1-4af5-8acd-5857cd087c3a",
  "timestamp": "2026-05-16T10:13:19.809Z",
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

_source line 3 · 2026-05-16T10:13:22.060Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NLCMj2B6iV5DLcwRS56HkB`</summary>

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
  "parentUuid": "14ed761f-18d1-4af5-8acd-5857cd087c3a",
  "isSidechain": true,
  "agentId": "a37938b45de9768d2",
  "requestId": "req_011Cb652SbskB99ouYXhf81L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6182880-34ac-45c6-867e-f1b34bce311d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7Lf5q5dENAL9Q23LfNfvk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8970,
      "cache_read_input_tokens": 0,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8970
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8970,
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

_source line 4 · 2026-05-16T10:13:22.065Z_

<details><summary>↩ Tool result · `toolu_01NLCMj2B6iV5DLcwRS56HkB`</summary>

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
  "parentUuid": "b6182880-34ac-45c6-867e-f1b34bce311d",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a37938b45de9768d2",
  "type": "user",
  "uuid": "2999dd20-c990-4e4a-af7f-88f6da41c265",
  "sourceToolAssistantUUID": "b6182880-34ac-45c6-867e-f1b34bce311d",
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

_source line 5 · 2026-05-16T10:13:24.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FBrebxsahBA31AjsroR7xt`</summary>

```json
{
  "query": "arxiv 2605.05686"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2999dd20-c990-4e4a-af7f-88f6da41c265",
  "isSidechain": true,
  "agentId": "a37938b45de9768d2",
  "requestId": "req_011Cb652cYfbDvLZYjXjz28k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f21dc2fc-f2f3-480f-98f8-48d05897d046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VYgWEHDLzN31MWaVTJmKF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 6 · 2026-05-16T10:13:24.996Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018tg8ZzArqf8J3vGUPQcW9u`</summary>

```json
{
  "query": "Attractor Geometry Transformer Memory hallucination Liang 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f21dc2fc-f2f3-480f-98f8-48d05897d046",
  "isSidechain": true,
  "agentId": "a37938b45de9768d2",
  "requestId": "req_011Cb652cYfbDvLZYjXjz28k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7fc0188-c119-4159-a982-e194e2e4f638",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VYgWEHDLzN31MWaVTJmKF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 7 · 2026-05-16T10:13:26.133Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PdDbpsfnEeoJCNeHkTCSJs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05686",
  "prompt": "What is the title, authors, and abstract of this paper? Does it discuss attractor basins, geometric margin, hallucination, or LM head being \"blind by design\"?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7fc0188-c119-4159-a982-e194e2e4f638",
  "isSidechain": true,
  "agentId": "a37938b45de9768d2",
  "requestId": "req_011Cb652cYfbDvLZYjXjz28k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8faf1815-89d4-4335-945f-b8b66aed4263",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VYgWEHDLzN31MWaVTJmKF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8970,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 215,
          "cache_read_input_tokens": 8970,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1888,
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

_source line 8 · 2026-05-16T10:13:30.382Z_

<details><summary>↩ Tool result · `toolu_01FBrebxsahBA31AjsroR7xt`</summary>

```text
Web search results for query: "arxiv 2605.05686"

Links: [{"title":"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/html/2605.05686"},{"title":"[2605.05686] Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/abs/2605.05686"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=600&show=100"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2406.05686"},{"title":"Provable Optimization for Adversarial Fair Self-supervised Contrastive Learning","url":"https://arxiv.org/html/2406.05686"},{"title":"Chebyshev pseudosite matrix product state approach for cluster perturbation theory","url":"https://arxiv.org/html/2404.05686"},{"title":"kNN-SVC: Robust Zero-Shot Singing Voice Conversion with Additive Synthesis and Concatenation Smoothness Optimization This project is partially supported by the European Research Council under Europe’s Horizon 2020 program, grant #883313 (ERC REACH).","url":"https://arxiv.org/html/2504.05686"},{"title":"Joint observations of late universe probes: cosmological parameter constraints from gravitational wave and Type Ia supernova data","url":"https://arxiv.org/html/2407.05686"},{"title":"kNN-SVC: Robust Zero-Shot Singing Voice Conversion with","url":"https://arxiv.org/pdf/2504.05686"},{"title":"[1907.05686] And the Bit Goes Down: Revisiting the Quantization of Neural Networks","url":"https://ar5iv.labs.arxiv.org/html/1907.05686"}]

Based on the search results, arxiv 2605.05686 is a paper titled "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination" by Qiyao Liang, Risto Miikkulainen, and Ila Fiete.

The paper studies how language models draw on two knowledge sources—facts baked into weights (parametric memory) and information in context (working memory)—and examines two failure modes: conflict, when these sources disagree and interfere, and hallucination, when the queried fact was never learned. The authors show both failures share a unified geometric account, where learned facts form attractor basins in the hidden-state space of autoregressive generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f21dc2fc-f2f3-480f-98f8-48d05897d046",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a37938b45de9768d2",
  "type": "user",
  "uuid": "eea9680d-116a-4b58-a077-01859fde934d",
  "sourceToolAssistantUUID": "f21dc2fc-f2f3-480f-98f8-48d05897d046",
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

_source line 9 · 2026-05-16T10:13:30.749Z_

<details><summary>↩ Tool result · `toolu_01PdDbpsfnEeoJCNeHkTCSJs`</summary>

```text
# Paper Summary

**Title:** "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination"

**Authors:** Qiyao Liang, Risto Miikkulainen, Ila Fiete

**Yes, the paper discusses all mentioned concepts:**

The abstract explains that "learned facts form attractor basins" in hidden-state space. It describes conflict as "basin competition" where working memory disrupts convergence, and hallucination as "basin absence" where hidden states drift without a memorized basin.

The paper introduces "geometric margin"—defined as "the hidden state's distance to the nearest memorized basin"—as a detection method that outperforms entropy-based approaches.

Regarding the LM head being blind: The authors state the frozen output head "cannot distinguish these cases and fires confidently either way," explaining why output-based monitoring fails to detect these failure modes.

The research demonstrates these geometric principles through controlled experiments with synthetic tasks and validates findings on natural language queries from pretrained models, revealing that "hidden states reliably encode epistemic state; the frozen output head systematically erases it."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8faf1815-89d4-4335-945f-b8b66aed4263",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a37938b45de9768d2",
  "type": "user",
  "uuid": "8ff19f32-a1f2-4a5e-8f6b-c031d0d4cd73",
  "sourceToolAssistantUUID": "8faf1815-89d4-4335-945f-b8b66aed4263",
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

_source line 10 · 2026-05-16T10:13:31.931Z_

<details><summary>↩ Tool result · `toolu_018tg8ZzArqf8J3vGUPQcW9u`</summary>

```text
Web search results for query: "Attractor Geometry Transformer Memory hallucination Liang 2026"

Links: [{"title":"[2605.05686] Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/abs/2605.05686"},{"title":"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/html/2605.05686"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400"},{"title":"[2604.15400] Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/abs/2604.15400"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/30df78bc24ff6fdaefdd8fc6938cb20e2163ea2a.pdf"},{"title":"From Dispersion to Attraction: Spectral Dynamics of Hallucination Across Whisper Model Scales","url":"https://arxiv.org/html/2604.08591v1"},{"title":"Persistent Symbolic Attractor Basins in Memory-Off Transformer Language Models | by Jeffrey Hanley | Medium","url":"https://medium.com/@jeffhanley0/persistent-symbolic-attractor-basins-in-memory-off-transformer-language-models-d801c9b44ea4"},{"title":"RiemannInfer: improving transformer inference through Riemannian geometry | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-37328-x"},{"title":"A Geometric Taxonomy of Hallucination in LLMs","url":"https://arxiv.org/html/2602.13224v3"},{"title":"How Large Language Models are Designed to Hallucinate","url":"https://arxiv.org/pdf/2509.16297"}]

I found relevant research on this topic. Here's what the search results show:

## Main Finding

A paper by Qiyao Liang and 2 other authors studies how language models draw on two knowledge sources: facts baked into weights (parametric memory, PM) and information in context (working memory, WM).

## Key Concepts

The research shows both failure modes share a unified geometric account: in the hidden-state space of autoregressive generation, learned facts form attractor basins. Conflict is basin competition where working memory disrupts convergence to the correct basin without raising output entropy. Hallucination is basin absence where the hidden state drifts freely when no memorized basin exists.

## Technical Approach

Geometric margin—the hidden state's distance to the nearest memorized basin—reads this geometry directly and separates correct recall from hallucination far more cleanly than output entropy, with zero false refusals where entropy-based detection cannot avoid rejecting the vast majority of correct outputs.

## Scaling Behavior

The fraction of confident hallucinations follows a scaling law growing with scale even as overall error rates fall.

The paper appears to be from May 2026 based on the arxiv timestamp, and represents significant research into understanding transformer memory mechanisms through geometric analysis of hidden states.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7fc0188-c119-4159-a982-e194e2e4f638",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a37938b45de9768d2",
  "type": "user",
  "uuid": "9fa4567f-8850-4d0c-9480-ad2881fcae4f",
  "sourceToolAssistantUUID": "b7fc0188-c119-4159-a982-e194e2e4f638",
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

_source line 11 · 2026-05-16T10:13:35.570Z_

Now let me get more details about the paper's specific claims regarding the LM head being "blind by design."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fa4567f-8850-4d0c-9480-ad2881fcae4f",
  "isSidechain": true,
  "agentId": "a37938b45de9768d2",
  "requestId": "req_011Cb653LQqSx68Xo7vxgpGL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "225e008b-87c6-4f7f-8bf9-90f2fd8d0ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf8yp3XsJGzjj78e3sk9CR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 284,
      "cache_creation_input_tokens": 1751,
      "cache_read_input_tokens": 10858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1751,
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

_source line 12 · 2026-05-16T10:13:37.565Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MV9rRC5AUwJEmiEQwoHYWV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05686",
  "prompt": "List the full author affiliations. Is this paper from MIT? What are the key claims about the LM head being \"blind by design\"? What does it say about geometric margin as a monitoring signal? What does it say about attractor basins for factual recall? Please extract any specific quotes about these topics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "225e008b-87c6-4f7f-8bf9-90f2fd8d0ecf",
  "isSidechain": true,
  "agentId": "a37938b45de9768d2",
  "requestId": "req_011Cb653LQqSx68Xo7vxgpGL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2abb05a-a0c5-4b8d-945c-c12076ff4a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf8yp3XsJGzjj78e3sk9CR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 284,
      "cache_creation_input_tokens": 1751,
      "cache_read_input_tokens": 10858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1751,
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

### Tool result

_source line 13 · 2026-05-16T10:13:42.179Z_

<details><summary>↩ Tool result · `toolu_01MV9rRC5AUwJEmiEQwoHYWV`</summary>

```text
# Analysis of arXiv:2605.05686

## Author Affiliations

The paper listing does not provide full institutional affiliations for the authors (Qiyao Liang, Risto Miikkulainen, Ila Fiete). **This is not an MIT paper** based on the available information—no MIT affiliation is indicated.

## Key Claims About the LM Head Being "Blind by Design"

The abstract states: *"Both produce confident output regardless, making output-based monitoring blind by design."* The paper argues that the frozen language model head, optimized for next-token prediction, cannot distinguish between conflict and hallucination scenarios and produces confident predictions in both cases, preventing detection through output entropy monitoring.

## Geometric Margin as a Monitoring Signal

The research proposes that *"Geometric margin...reads this geometry directly and separates correct recall from hallucination far more cleanly than output entropy, with zero false refusals where entropy-based detection cannot avoid rejecting the vast majority of correct outputs."*

## Attractor Basins for Factual Recall

The paper explains that *"In the hidden-state space...learned facts form attractor basins. Conflict is basin competition...Hallucination is basin absence: the hidden state drifts freely when no memorized basin exists."*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2abb05a-a0c5-4b8d-945c-c12076ff4a2d",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a37938b45de9768d2",
  "type": "user",
  "uuid": "402b9d22-1636-464f-8434-eeed5860b699",
  "sourceToolAssistantUUID": "b2abb05a-a0c5-4b8d-945c-c12076ff4a2d",
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

_source line 14 · 2026-05-16T10:13:57.240Z_

Here is my report on the paper:

---

## Findings on "Attractor Geometry of Transformer Memory" (arXiv 2605.05686)

### 1. Does this paper exist?

**Yes.** The paper is real and available on arXiv at `2605.05686`. Its full title is "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination" by Qiyao Liang, Risto Miikkulainen, and Ila Fiete.

**However, one correction:** Based on the information retrieved, the paper does **not** appear to be from MIT. The authors listed are Qiyao Liang, Risto Miikkulainen, and Ila Fiete. While Ila Fiete is indeed affiliated with MIT (she is a professor in MIT's Department of Brain and Cognitive Sciences), Risto Miikkulainen is at UT Austin. So the paper has partial MIT affiliation but is not solely an "MIT paper." The "Liang et al." attribution is correct (first author is Qiyao Liang).

### 2. Does it argue the LM head is "blind by design" to high-confidence hallucinations?

**Yes.** The abstract explicitly states: *"Both produce confident output regardless, making output-based monitoring blind by design."* The paper argues that the frozen language model head fires confidently whether the model is recalling a correct fact, experiencing knowledge conflict, or hallucinating -- making output-based detection fundamentally limited.

### 3. Does it propose "geometric margin" as a monitoring signal?

**Yes.** The paper proposes geometric margin -- defined as the hidden state's distance to the nearest memorized attractor basin -- as a monitoring signal. It claims this metric "separates correct recall from hallucination far more cleanly than output entropy, with zero false refusals" (where entropy-based detection rejects the vast majority of correct outputs).

### 4. Does it discuss attractor basins for factual recall?

**Yes.** This is the central framework of the paper. It argues that learned facts form attractor basins in the hidden-state space of autoregressive generation. The two failure modes are:
- **Conflict = basin competition**: working memory disrupts convergence to the correct basin without raising output entropy.
- **Hallucination = basin absence**: the hidden state drifts freely when no memorized basin exists.

---

**Summary:** All four claims you asked about are verified as present in this paper. The paper exists, discusses the LM head being "blind by design," proposes geometric margin as a monitoring signal, and frames factual recall in terms of attractor basins. The only minor inaccuracy in your description is calling it solely an "MIT" paper -- it appears to have mixed affiliations.

Sources:
- [arXiv:2605.05686 Abstract](https://arxiv.org/abs/2605.05686)
- [arXiv:2605.05686 HTML version](https://arxiv.org/html/2605.05686)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "402b9d22-1636-464f-8434-eeed5860b699",
  "isSidechain": true,
  "agentId": "a37938b45de9768d2",
  "requestId": "req_011Cb6546GpEBmVhwnTmiUmS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b65e91db-fb00-431d-bd5e-658435645e1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VL3d7bhLtgrMGpyEDEKweY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 756,
      "cache_read_input_tokens": 12609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 756,
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
