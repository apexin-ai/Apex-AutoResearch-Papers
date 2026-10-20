# Research conversation: Search for and read the paper "A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance" (arXiv 2512

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a14a6f063bfdf7d5b.jsonl`
- **Structured JSON:** [`d60bb77c800af165f716.json`](../../sessions/d6/d60bb77c800af165f716.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-10T20:10:42.323Z_

Search for and read the paper "A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance" (arXiv 2512.07647). I need to understand:
1. What exactly does this paper prove about Top-K attention truncation error?
2. How does the boundary gap between K-th and (K+1)-th logits factor into their bounds?
3. Is this NeurIPS 2025 as claimed?
4. What are the key theorems?

Use WebSearch to find it, then use WebFetch to read the abstract and key results from the arXiv page. Report the key findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a14a6f063bfdf7d5b",
  "type": "user",
  "uuid": "e34f0015-ccd7-4897-ac08-ce3bab444772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:10:42.329Z_

```json
{
  "parentUuid": "e34f0015-ccd7-4897-ac08-ce3bab444772",
  "isSidechain": true,
  "agentId": "a14a6f063bfdf7d5b",
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
      "TodoWrite",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "8103a942-0d61-4856-8b4e-dbe727daa2ff",
  "timestamp": "2026-05-10T20:10:42.329Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T20:10:44.861Z_



I'll search for this paper and fetch its details from arXiv.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8103a942-0d61-4856-8b4e-dbe727daa2ff",
  "isSidechain": true,
  "agentId": "a14a6f063bfdf7d5b",
  "requestId": "req_011CauVj4Yy68iP2oUXnXds1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49449ea4-3759-4751-83c8-0e014c5f4806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbCG6C5mFd1MkFj1vTzXju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8916,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8916,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T20:10:45.105Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019pWvbHjifYqLGsg7FUVBtp`</summary>

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
  "parentUuid": "49449ea4-3759-4751-83c8-0e014c5f4806",
  "isSidechain": true,
  "agentId": "a14a6f063bfdf7d5b",
  "requestId": "req_011CauVj4Yy68iP2oUXnXds1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acb1ddc4-20be-4b41-a765-9c4cfd1f3233",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbCG6C5mFd1MkFj1vTzXju",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8916,
      "cache_read_input_tokens": 0,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8916,
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

_source line 5 · 2026-05-10T20:10:45.110Z_

<details><summary>↩ Tool result · `toolu_019pWvbHjifYqLGsg7FUVBtp`</summary>

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
  "parentUuid": "acb1ddc4-20be-4b41-a765-9c4cfd1f3233",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a14a6f063bfdf7d5b",
  "type": "user",
  "uuid": "4d10d61e-2ccd-41b2-ac50-110cdea1a034",
  "sourceToolAssistantUUID": "acb1ddc4-20be-4b41-a765-9c4cfd1f3233",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T20:10:49.098Z_



Now let me search for the paper and fetch its arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d10d61e-2ccd-41b2-ac50-110cdea1a034",
  "isSidechain": true,
  "agentId": "a14a6f063bfdf7d5b",
  "requestId": "req_011CauVjGKeE8G4QVJQd7xgf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6b64060-ac6c-46d6-a85c-61e7317b3691",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvD86vXGMjSnEjWGN94yAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1905,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1905,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T20:10:50.678Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UnXgKAuZASp3WV6ybif8mn`</summary>

```json
{
  "query": "arXiv 2512.07647 \"A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6b64060-ac6c-46d6-a85c-61e7317b3691",
  "isSidechain": true,
  "agentId": "a14a6f063bfdf7d5b",
  "requestId": "req_011CauVjGKeE8G4QVJQd7xgf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e21b98c-f39a-44c3-b38b-bbf64b0fd118",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvD86vXGMjSnEjWGN94yAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1905,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1905,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T20:10:52.300Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011NEjDBJgqcLzov7pEYzAbG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.07647",
  "prompt": "Extract the full abstract, list of authors, publication venue (is it NeurIPS 2025?), and any key theorem statements or main results mentioned on this page. Include all mathematical details available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e21b98c-f39a-44c3-b38b-bbf64b0fd118",
  "isSidechain": true,
  "agentId": "a14a6f063bfdf7d5b",
  "requestId": "req_011CauVjGKeE8G4QVJQd7xgf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "304dbf44-fa11-4651-b7fe-62c407ea73bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvD86vXGMjSnEjWGN94yAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1905,
      "cache_read_input_tokens": 8916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1905,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T20:10:56.025Z_

<details><summary>↩ Tool result · `toolu_01UnXgKAuZASp3WV6ybif8mn`</summary>

```text
Web search results for query: "arXiv 2512.07647 "A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance""

Links: [{"title":"A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance","url":"https://arxiv.org/html/2512.07647"},{"title":"A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance","url":"https://www.arxiv.org/pdf/2512.07647"}]

Based on the search results, here's what I found about the paper:

**Title:** A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance

**Authors:** Georgios Tzachristas, Lei Deng, Ioannis Tzachristas, Gong Zhang, and Renhai Chen

**Key Contribution:** The paper develops a unified mathematical framework for certified Top-k attention truncation that quantifies approximation error at both the distribution and output levels.

**Main Focus:** The work develops a unified mathematical theory of Top-k attention that quantifies the effect of truncation at both the distribution and output levels, and connects these guarantees to certified sparse-attention algorithms.

**Practical Applications:** The approach scales predictably with context length while preserving the requested bound, making it suitable for long-context inference and resource-constrained deployment.

**Publication Date:** December 8, 2025

The paper addresses the problem of quadratic complexity in transformer attention mechanisms by providing theoretical guarantees for Top-k sparse attention, enabling efficient deployment in large language models with provable error bounds.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e21b98c-f39a-44c3-b38b-bbf64b0fd118",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a14a6f063bfdf7d5b",
  "type": "user",
  "uuid": "666d8df8-a458-423f-9435-f47954eed795",
  "sourceToolAssistantUUID": "3e21b98c-f39a-44c3-b38b-bbf64b0fd118",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T20:10:59.516Z_

<details><summary>↩ Tool result · `toolu_011NEjDBJgqcLzov7pEYzAbG`</summary>

```text
# Paper Summary: Top-k Sparse Attention via Total Variation Distance

**Full Abstract:**
The authors develop a mathematical framework for Top-k attention truncation, showing that "the total-variation distance coincides with the discarded softmax tail mass" via the relationship TV(P,P̂)=1-e^(-KL(P̂||P)). They derive deterministic bounds controlling approximation error using ordered logits, prove output error factorizes as ||Attn(q,K,V)-Attn_k(q,K,V)||₂=τ||μ_tail-μ_head||₂, and establish asymptotic scaling rules for minimal k ensuring TV(P,P̂)≤ε under Gaussian assumptions. Experiments demonstrate "2-4× reduction" in scored keys while maintaining prescribed error budgets.

**Authors:**
- Georgios Tzachristas
- Lei Deng
- Ioannis Tzachristas
- Gong Zhang
- Renhai Chen

**Publication Venue:**
This is an **arXiv preprint (arXiv:2512.07647)**, submitted December 8, 2025. It is **not** a NeurIPS 2025 publication—no venue acceptance is indicated.

**Key Results:**
1. TV(P,P̂) characterization connecting tail mass to KL divergence
2. Head-tail diameter bound: ||error||₂ ≤ τ·diam_{H,T}
3. Asymptotic scaling rule: k_ε/n ≈ Φ_c(σ+Φ^(-1)(ε)) under i.i.d. Gaussian scores
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "304dbf44-fa11-4651-b7fe-62c407ea73bb",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a14a6f063bfdf7d5b",
  "type": "user",
  "uuid": "aa63482b-4645-431c-b0da-e70d96aa5f51",
  "sourceToolAssistantUUID": "304dbf44-fa11-4651-b7fe-62c407ea73bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T20:11:03.231Z_

Good, I have the basics. Let me now fetch the full HTML version to get the detailed theorem statements and the role of the boundary gap.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa63482b-4645-431c-b0da-e70d96aa5f51",
  "isSidechain": true,
  "agentId": "a14a6f063bfdf7d5b",
  "requestId": "req_011CauVkKhKcvckQMF7QPSRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61e7d559-aa04-4ca7-b4d0-1c1b0b14adc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MFyH9fkeoCcb2apdnTv5z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 10821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1043,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T20:11:06.689Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KrX5a26QA8hJRa3m2TPDJU`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.07647",
  "prompt": "Extract the detailed theorem statements (Theorem 1, Theorem 2, Theorem 3, etc.), propositions, and corollaries from this paper. I need:\n1. The exact statement of each key theorem, including all mathematical conditions and bounds.\n2. How the boundary gap (the gap between the K-th and (K+1)-th largest logits) appears in the bounds.\n3. The definition and role of the tail mass tau.\n4. The factorization of the output error.\n5. The asymptotic scaling results for minimal k.\n6. Any mention of NeurIPS 2025 or other venue.\nBe as detailed as possible with the mathematical content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61e7d559-aa04-4ca7-b4d0-1c1b0b14adc9",
  "isSidechain": true,
  "agentId": "a14a6f063bfdf7d5b",
  "requestId": "req_011CauVkKhKcvckQMF7QPSRK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6b2ed5d-4080-4ab1-a9c4-75bc1412b3e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MFyH9fkeoCcb2apdnTv5z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 10821,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1043
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 264,
          "cache_read_input_tokens": 10821,
          "cache_creation_input_tokens": 1043,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1043,
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

_source line 13 · 2026-05-10T20:11:19.292Z_

<details><summary>↩ Tool result · `toolu_01KrX5a26QA8hJRa3m2TPDJU`</summary>

````text
# Key Theoretical Results from "A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance"

## Primary Theorems

### Theorem 4.3 (Exact TV–KL Identity)
The relationship between total variation and Kullback-Leibler divergence for Top-k truncation satisfies:

```
KL(P̂∥P) = log(∑ⱼ₌₁ⁿ eˢʲ / ∑ⱼ₌₁ᵏ eˢʲ)
TV(P,P̂) = 1 - e^(-KL(P̂∥P))
```

This exact identity replaces inequality-based relationships with a sharp equality specific to Top-k truncation.

### Theorem 4.5 (Deterministic Gap Bound)
The boundary gap Δₖ = sₖ - sₖ₊₁ directly controls truncation error:

```
TV(P,P̂) ≤ 1 / (1 + (k/(n-k))·e^Δₖ)
```

**Interpretation**: A large boundary gap exponentially suppresses tail mass. The bound is tight when all top-k scores equal sₖ and all remaining scores equal sₖ₊₁.

### Theorem 5.2 (Exact Head–Tail Decomposition)
The output error factorizes as:

```
||Attn(q,K,V) - Attnₖ(q,K,V)||₂ = τ·||μₜₐᵢₗ - μₕₑₐ𝒹||₂
```

where τ = ∑ᵢ₎ₖ pᵢ represents the discarded softmax tail mass, and μₕₑₐ𝒹, μₜₐᵢₗ are conditional means of value vectors over retained and discarded indices respectively.

### Proposition 5.3 (Head–Tail Diameter Bound)
The cross-set diameter of value vectors provides geometric control:

```
||Attn(q,K,V) - Attnₖ(q,K,V)||₂ ≤ τ·diamₕ,ₜ
```

where diamₕ,ₜ = max{||vᵢ - vⱼ||₂ : i > k, j ≤ k}.

## Role of Boundary Gap

The boundary gap Δₖ appears explicitly in:
- The deterministic gap bound (Theorem 4.5) with exponential dependence e^Δₖ
- Multi-gap bounds (Lemma 4.7) examining sequences of adjacent gaps
- Block-level generalizations (Section 4.5) as inter-block log-mass differences

The exponential sensitivity means even modest gaps (e.g., Δₖ ≈ 15) yield small truncation errors for large n.

## Tail Mass Definition and Role

Lemma 4.1 establishes the fundamental identity: "TV(P,P̂) = ∑ᵢ₎ₖ pᵢ"

The tail mass τ represents the exact total probability discarded by truncation and:
- Equals TV distance (distribution-level)
- Multiplies the diameter bound for output error
- Scales the error linearly when values differ substantially

## Asymptotic Scaling Results (Gaussian Score Model)

Under i.i.d. Gaussian scores sᵢ ~ 𝒩(μ,σ²):

```
kε ≈ n·Φc(σ + Φ⁻¹(ε))
```

where Φc is the standard normal survival function and ε is the target error tolerance.

The minimal k ensuring TV(P,P̂) ≤ ε scales with:
- **n**: linearly with sequence length
- **σ**: exponentially; higher variance requires larger k
- **ε**: via the inverse normal quantile Φ⁻¹(ε)

Empirical validation (Table 2, Figure 1) confirms this prediction remains accurate to within 0.1% relative error for σ ≤ 3.

## Venue Information

The document header does not mention NeurIPS 2025 or other conference venue. The arxiv identifier "2512.07647v1" suggests a recent submission, but specific publication venue is absent from the provided content.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6b2ed5d-4080-4ab1-a9c4-75bc1412b3e5",
  "isSidechain": true,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "agentId": "a14a6f063bfdf7d5b",
  "type": "user",
  "uuid": "1aa07aaf-82b9-49a7-afb5-d42519229af5",
  "sourceToolAssistantUUID": "e6b2ed5d-4080-4ab1-a9c4-75bc1412b3e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T20:11:46.403Z_

Here are the key findings from the paper.

---

**Paper:** "A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance" (arXiv:2512.07647)
**Authors:** Georgios Tzachristas, Lei Deng, Ioannis Tzachristas, Gong Zhang, Renhai Chen
**Submitted:** December 8, 2025

---

### 1. What the paper proves about Top-K attention truncation error

The paper establishes an **exact identity** (not just a bound) between the total-variation distance of the full softmax distribution P and its Top-k truncation P-hat, and the discarded tail mass:

- **Lemma 4.1:** TV(P, P-hat) = sum of p_i for i > k (the tail mass tau). The TV distance *is* exactly the probability mass you throw away.
- **Theorem 4.3 (Exact TV-KL Identity):** KL(P-hat || P) = log(Z / Z_k), and TV(P, P-hat) = 1 - exp(-KL(P-hat || P)). This is a sharp equality, not an inequality, specific to the Top-k truncation structure.
- **Theorem 5.2 (Exact Head-Tail Decomposition):** The output-level error factorizes as:
  `||Attn(q,K,V) - Attn_k(q,K,V)||_2 = tau * ||mu_tail - mu_head||_2`
  where tau is the tail mass, and mu_head / mu_tail are the conditional means of value vectors over retained vs. discarded indices. This cleanly separates the **score-side error** (tau) from the **value-side geometry** (how different the discarded values are from the kept ones).

### 2. How the boundary gap factors into the bounds

The **boundary gap** Delta_k = s_k - s_{k+1} (the difference between the K-th and (K+1)-th largest logits) appears in **Theorem 4.5 (Deterministic Gap Bound)**:

`TV(P, P-hat) <= 1 / (1 + (k / (n-k)) * exp(Delta_k))`

The exponential dependence on Delta_k is the critical insight: even a **modest gap** (e.g., Delta_k around 15) exponentially suppresses the tail mass, making truncation highly accurate. The bound is tight when all top-k scores equal s_k and all remaining scores equal s_{k+1}. This gives practitioners a simple, checkable certificate: if the gap at the truncation boundary is large, the approximation is provably good. The paper also extends this to **multi-gap bounds** (Lemma 4.7) that examine sequences of adjacent gaps, and block-level generalizations.

### 3. Is this NeurIPS 2025?

**No.** The paper is an **arXiv preprint** (arXiv:2512.07647v1, submitted December 2025). There is **no indication** of NeurIPS 2025 acceptance anywhere on the arXiv page. If someone claimed it was a NeurIPS 2025 paper, that claim is not supported by the available metadata.

### 4. Key theorems summary

| Result | Statement |
|---|---|
| **Lemma 4.1** | TV(P, P-hat) = tau (tail mass) -- exact identity |
| **Theorem 4.3** | TV = 1 - exp(-KL), with KL = log(Z/Z_k) -- exact TV-KL relationship |
| **Theorem 4.5** | TV <= 1 / (1 + (k/(n-k)) exp(Delta_k)) -- deterministic gap bound |
| **Theorem 5.2** | Output error = tau * ||mu_tail - mu_head||_2 -- exact factorization |
| **Proposition 5.3** | Output error <= tau * diam_{H,T} -- geometric diameter bound |
| **Asymptotic scaling** | k_epsilon ~ n * Phi_c(sigma + Phi^{-1}(epsilon)) under Gaussian scores -- minimal k scales linearly in n, exponentially in score variance sigma |

The practical upshot: the framework lets you predict how many keys to keep (k) for a given error budget epsilon, and this prediction scales predictably with context length. Experiments show 2-4x reduction in scored keys while maintaining prescribed error budgets, validated to within 0.1% relative error for sigma <= 3.

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2512.07647)
- [arXiv HTML full paper](https://arxiv.org/html/2512.07647)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aa07aaf-82b9-49a7-afb5-d42519229af5",
  "isSidechain": true,
  "agentId": "a14a6f063bfdf7d5b",
  "requestId": "req_011CauVmnb7RrMfXfnjdZFCh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9be44e8-fef7-401b-a93f-53872d47e95c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RYL7JqRmbcNpJVurckodn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1371,
      "cache_read_input_tokens": 11864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1371,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---
