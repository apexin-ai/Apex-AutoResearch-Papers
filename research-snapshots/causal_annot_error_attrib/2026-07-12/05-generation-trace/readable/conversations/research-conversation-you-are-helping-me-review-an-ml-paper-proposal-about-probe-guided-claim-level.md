# Research conversation: You are helping me review an ML paper proposal about "probe-guided claim-level confidence calibration for long-form gene

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 103
- **Recorded user turns:** 1
- **Tool calls:** 46
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aea0f367b90d6b2a7.jsonl`
- **Structured JSON:** [`746592d82afeb6d441f1.json`](../../sessions/74/746592d82afeb6d441f1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

103 recorded events

### User

_source line 1 · 2026-05-15T14:16:20.189Z_

You are helping me review an ML paper proposal about "probe-guided claim-level confidence calibration for long-form generation." The idea combines claim-level factuality probes with activation steering to calibrate verbalized confidence during long-form text generation. I need you to search for MISSING competitors or concurrent work that the proposal may have overlooked.

The proposal already cites: Han et al. (EMNLP 2025), Miao & Ungar (2026), CORAL (2026), CLAS (2026), ITI (NeurIPS 2023), ActCab/CoDec (EMNLP 2024), CURE (2026), CAG (2026), LoVeC (2025), PCNET (2026), SteerConf (NeurIPS 2025), ACT (WWW 2025), CSS (2026), Selective Abstraction (2026), Kumaran et al. (2026), Obeso et al. (2025), Scaling Laws for Activation Steering (ICML 2025), ESR (2026).

Please search for work the proposal may have MISSED using the following queries (use WebSearch):

1. "claim-level calibration long-form generation 2025 2026" — any claim-level calibration work for long-form text
2. "activation steering confidence calibration 2026" — concurrent steering-for-calibration work  
3. "probe guided decoding hallucination 2026" — probe-guided generation approaches
4. "verbalized uncertainty long-form 2025 2026" — verbalized uncertainty in long-form settings
5. "inference time intervention hallucination reduction 2026" — ITI-style approaches for hallucinations
6. "linear probes hallucination detection steering 2026" — probe+steering combinations
7. "site:arxiv.org claim level uncertainty calibration LLM 2026" — arxiv-specific search
8. "faithfulness calibration generation ACL EMNLP 2026" — venue-specific recent work
9. "activation engineering confidence LLM 2025 2026" — activation engineering for confidence
10. "Rewarding Doubt hallucination 2026" OR "self-aware generation LLM 2026" — alternative approaches

For each search, report: (a) the query used, (b) any papers found that are NOT in the cited list above, (c) how relevant they are to the proposal (high/medium/low), and (d) whether they threaten the novelty claim.

Focus especially on papers from January-May 2026 that might be concurrent work. If you find something highly relevant, use WebFetch to read more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "a7fd1741-a684-4fcb-aa04-8638877b43e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T14:16:20.192Z_

```json
{
  "parentUuid": "a7fd1741-a684-4fcb-aa04-8638877b43e3",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
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
  "uuid": "a533a7f2-167d-4f30-b0a4-1d950ff282cf",
  "timestamp": "2026-05-15T14:16:20.192Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T14:16:23.196Z_



I'll conduct a systematic search for missing competitors and concurrent work. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a533a7f2-167d-4f30-b0a4-1d950ff282cf",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VkJtjYHY4ima2Teoti",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dfe9ef5-d2a4-4833-9aa1-db96fd298e22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NPxiitCWYU2jis6VT3xEv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1168,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1168,
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

_source line 4 · 2026-05-15T14:16:23.371Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LTq9Y83Xt6LsNSQWyYUX35`</summary>

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
  "parentUuid": "0dfe9ef5-d2a4-4833-9aa1-db96fd298e22",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VkJtjYHY4ima2Teoti",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "beda85a5-ad3b-45c9-8ff0-7e814f639a4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NPxiitCWYU2jis6VT3xEv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1168,
      "cache_read_input_tokens": 8223,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1168
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 1168,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1168,
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

_source line 5 · 2026-05-15T14:16:23.374Z_

<details><summary>↩ Tool result · `toolu_01LTq9Y83Xt6LsNSQWyYUX35`</summary>

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
  "parentUuid": "beda85a5-ad3b-45c9-8ff0-7e814f639a4d",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "25fafd42-6f9e-4196-8951-38eaa0b9e7f8",
  "sourceToolAssistantUUID": "beda85a5-ad3b-45c9-8ff0-7e814f639a4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T14:16:26.949Z_



Now let me run all 10 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25fafd42-6f9e-4196-8951-38eaa0b9e7f8",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VkYxpWsEJDTBDsn4Cm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8ad8764-259a-4194-89c0-458858725ac8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFsFSbx8SYj7BSWotecdAq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 7 · 2026-05-15T14:16:27.420Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011f6NPBCAc5qWPNMxKksNGS`</summary>

```json
{
  "query": "claim-level calibration long-form generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8ad8764-259a-4194-89c0-458858725ac8",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VkYxpWsEJDTBDsn4Cm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b62a863c-2b1c-47f9-ad16-8987e1d9578a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFsFSbx8SYj7BSWotecdAq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 8 · 2026-05-15T14:16:27.851Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013cChLAGQm5Dph2QR1MRpHi`</summary>

```json
{
  "query": "activation steering confidence calibration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b62a863c-2b1c-47f9-ad16-8987e1d9578a",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VkYxpWsEJDTBDsn4Cm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6aa8b1b8-995f-4ac7-9965-367fa1c6e1f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFsFSbx8SYj7BSWotecdAq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 9 · 2026-05-15T14:16:27.883Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M7mwrAWCRMC3sLpE4HWsGg`</summary>

```json
{
  "query": "probe guided decoding hallucination 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aa8b1b8-995f-4ac7-9965-367fa1c6e1f1",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VkYxpWsEJDTBDsn4Cm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5aa9e0ad-c3bd-42ce-9d66-c9cd60fd2e99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFsFSbx8SYj7BSWotecdAq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 10 · 2026-05-15T14:16:28.474Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011E8TJ1GXzbtketLoR7UQjq`</summary>

```json
{
  "query": "verbalized uncertainty long-form 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aa9e0ad-c3bd-42ce-9d66-c9cd60fd2e99",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VkYxpWsEJDTBDsn4Cm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d3e2267-f9e3-4f07-b12a-2c43c499db4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFsFSbx8SYj7BSWotecdAq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 11 · 2026-05-15T14:16:28.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017458sfdnB4hbUk1V2t5NTM`</summary>

```json
{
  "query": "inference time intervention hallucination reduction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d3e2267-f9e3-4f07-b12a-2c43c499db4e",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VkYxpWsEJDTBDsn4Cm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42faa0df-e65f-4635-9e38-282ffcb1cd44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFsFSbx8SYj7BSWotecdAq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 12 · 2026-05-15T14:16:35.623Z_

<details><summary>↩ Tool result · `toolu_011E8TJ1GXzbtketLoR7UQjq`</summary>

```text
Web search results for query: "verbalized uncertainty long-form 2025 2026"

Links: [{"title":"(PDF) Confronting verbalized uncertainty: Understanding how LLM ’s verbalized uncertainty influences users in AI-assisted decision-making","url":"https://www.researchgate.net/publication/388821876_Confronting_verbalized_uncertainty_Understanding_how_LLM_'s_verbalized_uncertainty_influences_users_in_AI-assisted_decision-making"},{"title":"Verbalized Confidence Triggers Self-Verification : Emergent Behavior Without Explicit Reasoning Supervision | OpenReview","url":"https://openreview.net/forum?id=Ub3eXwQ0uA"},{"title":"Confronting verbalized uncertainty: : Understanding how LLM’s verbalized uncertainty influences users in AI-assisted decision-making: International Journal of Human-Computer Studies: Vol 197, No C","url":"https://dl.acm.org/doi/abs/10.1016/j.ijhcs.2025.103455"},{"title":"Agentic Uncertainty Quantification","url":"https://arxiv.org/html/2601.15703"},{"title":"On Verbalized Confidence Scores for LLMs","url":"https://arxiv.org/html/2412.14737v2"},{"title":"BayesAgent: Bayesian Agentic Reasoning Under Uncertainty via Verbalized Probabilistic Graphical Modeling","url":"https://arxiv.org/html/2406.05516v4"},{"title":"What Verbalized Uncertainty in Language Models is Missing","url":"https://arxiv.org/pdf/2507.10587"},{"title":"Confronting verbalized uncertainty: Understanding how LLM’s verbalized uncertainty influences users in AI-assisted decision-making - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1071581925000126"},{"title":"Confronting Verbalized Uncertainty Understanding Ho 2025 International Jour | PDF | Artificial Intelligence | Intelligence (AI) & Semantics","url":"https://www.scribd.com/document/930284092/Confronting-Verbalized-Uncertainty-Understanding-Ho-2025-International-Jour"},{"title":"Uncertainty is certain for 2026 | UNC Kenan-Flagler","url":"https://www.kenan-flagler.unc.edu/news/uncertainty-is-certain-for-2026/"}]

Based on the search results, here's what I found on verbalized uncertainty in long-form contexts for 2025-2026:

## Recent Research on Verbalized Uncertainty

Large language models (LLMs) often express uncertainty in their outputs through "verbalized uncertainty", which can appear in phrases such as "I'm sure that [...]" or "It could be [...]".

### Key 2025-2026 Findings

**For Long-Form Reasoning:**
Uncertainty calibration is essential for the safe deployment of large language models, particularly when users rely on verbalized confidence estimates, though confidence calibration for chain-of-thought (CoT) reasoning remains largely unexplored. However, supervised fine-tuning with scalar confidence labels alone suffices to elicit self-verification behavior, allowing models to generate longer and self-checking responses for low-confidence queries while providing more concise answers for high-confidence ones.

**Impact on Decision-Making:**
Medium verbalized uncertainty in LLM expressions consistently leads to higher user trust, satisfaction, and task performance compared to high and low verbalized uncertainty.

**For Agentic Systems:**
Recent work transforms verbalized uncertainty into active, bi-directional control signals comprising uncertainty-aware memory and reflection mechanisms to prevent blind decision-making and balance efficient execution with deep deliberation.

These research developments show significant progress in understanding and leveraging verbalized uncertainty in both long-form reasoning and agentic AI systems during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d3e2267-f9e3-4f07-b12a-2c43c499db4e",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "876c8d8f-b65e-4859-a428-fd421a8569db",
  "sourceToolAssistantUUID": "9d3e2267-f9e3-4f07-b12a-2c43c499db4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T14:16:35.852Z_

<details><summary>↩ Tool result · `toolu_011f6NPBCAc5qWPNMxKksNGS`</summary>

```text
Web search results for query: "claim-level calibration long-form generation 2025 2026"

Links: [{"title":"Atomic Calibration of LLMs in Long-Form Generations","url":"https://arxiv.org/pdf/2410.13246"},{"title":"[2410.13246] Atomic Calibration of LLMs in Long-Form Generations","url":"https://arxiv.org/abs/2410.13246"},{"title":"arXiv:2506.07461v1 [cs.CL] 9 Jun 2025","url":"https://arxiv.org/pdf/2506.07461"},{"title":"2025 Data Points to Fewer Claims, More Collision Repair Complexity in 2026 - Autobody News","url":"https://www.autobodynews.com/news/2025-data-points-to-fewer-claims-more-collision-repair-complexity-in-2026"},{"title":"Conformal Linguistic Calibration: Trading-off between ...","url":"https://openreview.net/pdf/55aa4de08b2f5bcfa9155bb9c656e887cfb2d7e5.pdf"},{"title":"Atomic Calibration of LLMs in Long-Form Generations","url":"https://aclanthology.org/2025.findings-ijcnlp.9.pdf"},{"title":"Linguistic Calibration of Long-Form Generations - GitHub","url":"https://raw.githubusercontent.com/mlresearch/v235/main/assets/band24a/band24a.pdf"},{"title":"Fact-Level Calibration and Correction for Long-Form ...","url":"https://dl.acm.org/doi/pdf/10.1145/3726302.3730195"},{"title":"Atomic Calibration of LLMs in Long-Form Generations - ACL Anthology","url":"https://aclanthology.org/2025.findings-ijcnlp.9/"},{"title":"Calibrating Long-form Generations from Large Language ...","url":"https://aclanthology.org/2024.findings-emnlp.785.pdf"}]

Based on the search results, here's what I found regarding claim-level calibration in long-form generation for 2025-2026:

## Key Research on Atomic/Claim-Level Calibration

Recent work systematically studies atomic calibration, which evaluates factuality calibration at a fine-grained level by decomposing long responses into atomic claims. Prior work mainly focused on short-form tasks using a single response-level score (macro calibration), which is insufficient for long-form outputs that may contain both accurate and inaccurate claims.

## Main Findings

LLMs exhibit poorer calibration at the atomic level during long-form generation. Researchers have categorized existing confidence elicitation methods into discriminative and generative types, and proposed new confidence fusion strategies to improve calibration.

## Recent Approaches

One notable development is Conformal Linguistic Calibration, which provides a novel unifying view for this challenge. This approach answers all questions while still enhancing factuality, offering an advantage over traditional abstention methods.

The research in this area appears to be active, with recent papers and conference presentations in 2025 focusing on improving how LLMs calibrate their confidence at the individual claim level during long-form text generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b62a863c-2b1c-47f9-ad16-8987e1d9578a",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "df70ff97-5e4e-4e18-be60-ae4a000de2e1",
  "sourceToolAssistantUUID": "b62a863c-2b1c-47f9-ad16-8987e1d9578a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T14:16:36.538Z_

<details><summary>↩ Tool result · `toolu_01M7mwrAWCRMC3sLpE4HWsGg`</summary>

```text
Web search results for query: "probe guided decoding hallucination 2026"

Links: [{"title":"VCGD: Visual Clue Guided Decoding with Caption Model for Mitigating Hallucination in Multimodal Large Language Models | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/39089"},{"title":"[2603.20314] VGS-Decoding: Visual Grounding Score Guided Decoding for Hallucination Mitigation in Medical VLMs","url":"https://arxiv.org/abs/2603.20314"},{"title":"VGS-Decoding: Visual Grounding Score Guided Decoding for Hallucination Mitigation in Medical VLMs","url":"https://arxiv.org/html/2603.20314"},{"title":"HALP: Detecting Hallucinations in Vision-Language ...","url":"https://aclanthology.org/2026.eacl-long.287.pdf"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"[2604.06165] HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models","url":"https://arxiv.org/abs/2604.06165"},{"title":"Decoding by Perturbation: Mitigating MLLM Hallucinations via Dynamic Textual Perturbation","url":"https://arxiv.org/html/2604.12424"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"CoHalLo: code hallucination localization via probing hidden layer vector","url":"https://www.arxiv.org/pdf/2512.24183"},{"title":"[2604.12424] Decoding by Perturbation: Mitigating MLLM Hallucinations via Dynamic Textual Perturbation","url":"https://arxiv.org/abs/2604.12424"}]

Based on the web search results, here are several recent research papers (from 2026) combining probing-based approaches with guided decoding to mitigate hallucinations:

## Key Papers on Probe-Guided Decoding for Hallucination Mitigation

**HaloProbe** - A Bayesian framework that factorizes external description statistics and internal decoding signals to estimate token-level hallucination probabilities, using balanced training to isolate internal evidence and combining it with a learned prior over external features. HaloProbe-guided decoding reduces hallucinations more effectively than state-of-the-art intervention-based methods while preserving utility.

**VGS-Decoding** - A training-free method to mitigate hallucinations during inference that introduces the Visual Grounding Score (VGS), which measures each token's visual dependency by comparing distributions from original and distorted images. During decoding, it reweights probabilities by amplifying visually grounded tokens while suppressing hallucinations.

**Decoding by Perturbation (DeP)** - A training-free framework mitigating prior-induced hallucinations via controlled textual interventions that employs a dynamic probe applying multi-level textual perturbations to elicit latent language priors, leveraging attention variance to enhance stable evidence regions while suppressing suspicious noise in the feature space.

**VCGD** - Leverages high-quality visual descriptions to guide MLLMs in correcting perceptual biases while generating answers.

**HALP** - Investigates whether hallucination risk can be predicted before any token is generated by probing a model's internal representations in a single forward pass.

These approaches represent a shift toward detecting and mitigating hallucinations at the decoding stage rather than post-hoc detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5aa9e0ad-c3bd-42ce-9d66-c9cd60fd2e99",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "5ead3128-bd1f-4704-9a0a-6ad3e0682459",
  "sourceToolAssistantUUID": "5aa9e0ad-c3bd-42ce-9d66-c9cd60fd2e99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T14:16:36.612Z_

<details><summary>↩ Tool result · `toolu_017458sfdnB4hbUk1V2t5NTM`</summary>

```text
Web search results for query: "inference time intervention hallucination reduction 2026"

Links: [{"title":"Rethinking Visual Attention for Reducing Hallucination in Large Vision–Language Models","url":"https://www.mdpi.com/2076-3417/16/9/4143"},{"title":"ACT Now: Preempting LVLM Hallucinations via Adaptive Context Integration","url":"https://arxiv.org/html/2604.00983v1"},{"title":"Attention-space Contrastive Guidance for Efficient Hallucination Mitigation in LVLMs","url":"https://arxiv.org/html/2601.13707"},{"title":"Mitigating Hallucination in Large Language Models (LLMs): An Application-Oriented Survey on RAG, Reasoning, and Agentic Systems","url":"https://arxiv.org/html/2510.24476v1"},{"title":"AI Hallucination Rates & Benchmarks in 2026","url":"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"},{"title":"AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing [Quick Review]","url":"https://liner.com/review/after-mitigating-the-object-hallucination-of-lvlm-via-adaptive-factualguided"},{"title":"Mitigating Hallucinations in Large Language Models via Causal Reasoning","url":"https://arxiv.org/pdf/2508.12495"},{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"Seeing Far and Clearly: Mitigating Hallucinations in MLLMs with Attention Causal Decoding - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12425127/"}]

Based on the search results, here's what recent research shows about inference-time intervention methods for hallucination reduction in 2026:

## Key Approaches

One recent method proposes a tuning-free attention intervention approach applied at inference time, which applies structured rescaling to attention logits associated with visual tokens to introduce structural bias in the visual subspace.

Another approach called Adaptive Context Integration (ACT) is a training-free inference intervention method that mitigates hallucination through adaptive integration of contextual information. Specifically, it leverages spatio-temporal profiling to adaptively amplify attention heads responsible for visual exploration, and proposes semantic context aggregation to effectively aggregate visual evidence.

Attention-space Contrastive Guidance (ACG) is described as a simple inference-time intervention that can substantially improve faithfulness at low additional cost by directly reshaping attention toward visual evidence.

## Broader Context

Inference-Time Intervention (ITI) is a white-box technique that seeks to steer the model's internal state toward more truthful representations by identifying sparse sets of attention heads whose activations correlate with truthful responses, then adding a small learned vector to these attention heads at each generation step, which improves truthfulness with minimal computational overhead.

AFTER (Adaptive Factual-guided Visual-Textual Editing) is an activation editing approach that adaptively steers activations toward factual-augmented semantics, using Factual-Augmented Activation Steering (FAS) to provide positive textual guidance for LVLM activation editing.

These methods represent recent advances in reducing hallucinations through lightweight, model-agnostic interventions during the inference phase.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42faa0df-e65f-4635-9e38-282ffcb1cd44",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "72da532b-5b2a-48f1-9fe8-1c1ad5d1ab3d",
  "sourceToolAssistantUUID": "42faa0df-e65f-4635-9e38-282ffcb1cd44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T14:16:36.716Z_

<details><summary>↩ Tool result · `toolu_013cChLAGQm5Dph2QR1MRpHi`</summary>

```text
Web search results for query: "activation steering confidence calibration 2026"

Links: [{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Steering Awareness: Models Can Be Trained to Detect ...","url":"https://www.lesswrong.com/posts/D7zQkrDjAKaa293EA/steering-awareness-models-can-be-trained-to-detect"},{"title":"Activation Steering for Chain-of-Thought Compression Seyedarmin Azizi∗","url":"https://arxiv.org/pdf/2507.04742"},{"title":"Steering Evaluation-Aware Models to Act Like They Are ...","url":"https://www.alignmentforum.org/posts/peKrvZ6t9PSCzoQDa/steering-evaluation-aware-models-to-act-like-they-are"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/html/2602.08169v1"},{"title":"Refusal Steering: Fine-grained Control over LLM Refusal Behaviour","url":"https://arxiv.org/pdf/2512.16602"},{"title":"Steering Awareness: Detecting Activation Steering from Within","url":"https://arxiv.org/html/2511.21399v3"},{"title":"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment | OpenReview","url":"https://openreview.net/forum?id=CFewUmgIIL"},{"title":"Steering Angle Sensor Adaptations and Calibrations","url":"https://www.tomorrowstechnician.com/steering-angle-sensor-adaptations-and-calibrations/"},{"title":"Activation Steering Methods Overview","url":"https://www.emergentmind.com/topics/activation-steering-methods"}]

Based on the search results, here's what I found about activation steering, confidence calibration, and related research from 2026:

## Key Findings on Activation Steering and Confidence Calibration (2026)

### Calibration of Steering Strength
A principled method for calibrating steering strength explicitly bounds the KL divergence between original and steered output distributions, providing a closed-form formula that accounts for both the local sensitivity and curvature of the model's output relative to the intervention, allowing reliable and provably controlled distribution shifts.

Steering can shift model calibration - adding an uncertainty vector doesn't just change how the model talks about its confidence, but can actually shift the distribution of token probabilities.

### Recent Advances in Steering Methods

Steering Vector Fields (Feb 2026) propose using a differentiable scoring function whose gradient defines the steering direction at each activation, instead of a static vector applied uniformly, enabling context-dependent steering.

AUSteer decomposes activations into single-dimension "atomic units" and steers only the discriminative ones with adaptive per-input strengths, outperforming block-level baselines while touching fewer activations.

### Model Awareness of Steering
After fine-tuning, instruction-tuned models develop strong steering awareness - a model's ability to infer during its own forward pass that a steering vector was injected and what concept it encodes, with the best models reaching 95.5% detection and 71.2% concept identification.

### Theoretical Frameworks
An ODE-based theoretical framework for activation steering shows that conventional activation addition can be interpreted as a first-order approximation to the solution of an ODE, where identifying a steering direction becomes equivalent to designing a barrier function from control theory.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6aa8b1b8-995f-4ac7-9965-367fa1c6e1f1",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "1f6dce93-0b8a-4513-8af3-ff93c4703678",
  "sourceToolAssistantUUID": "6aa8b1b8-995f-4ac7-9965-367fa1c6e1f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T14:16:39.572Z_

Good, now let me run the remaining 5 searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f6dce93-0b8a-4513-8af3-ff93c4703678",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VmXbzVceyEZ4EZsaba",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03d14c12-b899-495b-a1e6-a24b719d8483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111fE2GDRhkx1zRyYubxpzT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2950,
      "cache_creation_input_tokens": 2023,
      "cache_read_input_tokens": 11308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2023,
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

_source line 18 · 2026-05-15T14:16:40.075Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TZE4cFjJ4SS9uv1JtRZDca`</summary>

```json
{
  "query": "linear probes hallucination detection steering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03d14c12-b899-495b-a1e6-a24b719d8483",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VmXbzVceyEZ4EZsaba",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96132133-3b65-4156-b729-14db85ca2cba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111fE2GDRhkx1zRyYubxpzT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2950,
      "cache_creation_input_tokens": 2023,
      "cache_read_input_tokens": 11308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2023,
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

_source line 19 · 2026-05-15T14:16:40.559Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VewL7rHRVNd2Qp65FJFfnW`</summary>

```json
{
  "query": "site:arxiv.org claim level uncertainty calibration LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96132133-3b65-4156-b729-14db85ca2cba",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VmXbzVceyEZ4EZsaba",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a4adb8c-452f-41b1-930a-175329619722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111fE2GDRhkx1zRyYubxpzT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2950,
      "cache_creation_input_tokens": 2023,
      "cache_read_input_tokens": 11308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2023,
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

_source line 20 · 2026-05-15T14:16:41.077Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014bGi4tXxo4LnFmKhNBoUp7`</summary>

```json
{
  "query": "faithfulness calibration generation ACL EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a4adb8c-452f-41b1-930a-175329619722",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VmXbzVceyEZ4EZsaba",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9229e65-6963-4f46-a8b8-5a8659e1253d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111fE2GDRhkx1zRyYubxpzT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2950,
      "cache_creation_input_tokens": 2023,
      "cache_read_input_tokens": 11308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2023,
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

_source line 21 · 2026-05-15T14:16:41.483Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016H5VwKtbBAq7d19anqUEpf`</summary>

```json
{
  "query": "activation engineering confidence LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9229e65-6963-4f46-a8b8-5a8659e1253d",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VmXbzVceyEZ4EZsaba",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc0d0971-23b0-4f94-af0d-c0392878d847",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111fE2GDRhkx1zRyYubxpzT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2950,
      "cache_creation_input_tokens": 2023,
      "cache_read_input_tokens": 11308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2023,
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

_source line 22 · 2026-05-15T14:16:42.725Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sp5a2VM6jqqBEAgZLtB3QT`</summary>

```json
{
  "query": "\"Rewarding Doubt\" hallucination 2026 OR \"self-aware generation\" LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc0d0971-23b0-4f94-af0d-c0392878d847",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VmXbzVceyEZ4EZsaba",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "231c6339-03ec-4015-983c-d889f7a42652",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111fE2GDRhkx1zRyYubxpzT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2950,
      "cache_creation_input_tokens": 2023,
      "cache_read_input_tokens": 11308,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2023
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2950,
          "output_tokens": 283,
          "cache_read_input_tokens": 11308,
          "cache_creation_input_tokens": 2023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2023,
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

_source line 23 · 2026-05-15T14:16:47.233Z_

<details><summary>↩ Tool result · `toolu_01Sp5a2VM6jqqBEAgZLtB3QT`</summary>

```text
Web search results for query: ""Rewarding Doubt" hallucination 2026 OR "self-aware generation" LLM 2026"

Links: [{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"}]

Based on the search results, I found relevant information about "Rewarding Doubt" in the context of LLM hallucination research:

"Rewarding Doubt" (2025) integrates confidence calibration into reinforcement learning, penalising both over- and underconfidence so model certainty better matches correctness. 

This method addresses the core misalignment that OpenAI's 2025 paper highlights: today's training and evaluation still incentivise confident guessing over admitting uncertainty.

The search results indicate that training objectives and benchmarks often reward confident guessing over calibrated uncertainty, and this insight drives a new generation of mitigations focused on calibration-aware rewards and uncertainty-friendly evaluation metrics.

However, I did not find specific results for "self-aware generation" LLM research in these search results. The focus appears to be on addressing hallucinations through uncertainty calibration and reward mechanisms rather than "self-aware generation" per se.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "231c6339-03ec-4015-983c-d889f7a42652",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "2b6a737f-bf64-45fe-aef8-5131d688bb45",
  "sourceToolAssistantUUID": "231c6339-03ec-4015-983c-d889f7a42652",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T14:16:47.501Z_

<details><summary>↩ Tool result · `toolu_01VewL7rHRVNd2Qp65FJFfnW`</summary>

```text
Web search results for query: "site:arxiv.org claim level uncertainty calibration LLM 2026"

Links: [{"title":"[2604.12046] Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration","url":"https://arxiv.org/abs/2604.12046"},{"title":"Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration","url":"https://arxiv.org/html/2604.12046"},{"title":"LLM Uncertainty Quantification Should Be More Human- ...","url":"https://arxiv.org/pdf/2506.07461"},{"title":"LLMs Should Express Uncertainty Explicitly","url":"https://arxiv.org/html/2604.05306"},{"title":"Mind the Gap: Benchmarking LLM Uncertainty and Calibration with Specialty-Aware Clinical QA and Reasoning-Based Behavioural Features","url":"https://arxiv.org/html/2506.10769v3"},{"title":"Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation","url":"https://arxiv.org/html/2603.05881v1"},{"title":"Uncertainty Quantification in LLM Agents: Foundations, Emerging Challenges, and Opportunities","url":"https://arxiv.org/html/2602.05073v2"},{"title":"Towards Reliable Truth-Aligned Uncertainty Estimation in Large Language Models","url":"https://arxiv.org/html/2604.00445"},{"title":"Uncertainty Quantification and Confidence Calibration in ...","url":"https://arxiv.org/pdf/2503.15850"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/html/2512.22245v1"}]

Based on the search results, I found several relevant papers from arXiv related to claim-level uncertainty calibration in LLMs from 2026:

## Key Finding

The most directly relevant paper is **CURE: Think Through Uncertainty**, which proposes a framework that improves long-form factuality by teaching LLMs to reason about uncertainty at the claim level. This approach structures outputs into atomic claims paired with explicit confidence estimates.

## Framework Details

CURE uses a multi-stage training pipeline that aligns model confidence with claims' correctness and optimizes on factuality, with calibrated confidence enabling selective prediction where the model can abstain from uncertain claims at inference time.

## Performance Results

Experiments on four long-form factuality benchmarks show CURE consistently improves factual accuracy, with claim-level accuracy improving by up to 39.9% on Biography generation, accompanied by a 16.0% increase in AUROC on FactBench.

## Related Work

Other 2026 papers addressing similar themes include studies on calibrating confidence scores displayed to users for particular claims within generations, and exploring different uncertainty presentation schemes including claim-level numeric probabilities, hedged linguistic uncertainty, and hedges with anthropomorphic cues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a4adb8c-452f-41b1-930a-175329619722",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "73f17f11-83b8-477d-a029-3d5e6dbc0d1c",
  "sourceToolAssistantUUID": "2a4adb8c-452f-41b1-930a-175329619722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T14:16:48.022Z_

<details><summary>↩ Tool result · `toolu_01TZE4cFjJ4SS9uv1JtRZDca`</summary>

```text
Web search results for query: "linear probes hallucination detection steering 2026"

Links: [{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe Exposes and Steers Contextual Hallucinations","url":"https://arxiv.org/html/2507.23221v1"},{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe","url":"https://arxiv.org/pdf/2507.23221"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400"},{"title":"Do transformers notice their own mistakes? Finding a linear hallucination detector inside LLMs","url":"https://parsed.com/research/do-transformers-notice-their-own-mistakes-finding-a-linear-hallucination-detector-inside-llms"},{"title":"Simple Factuality Probes Detect Hallucinations in Long- ...","url":"https://aclanthology.org/2025.findings-emnlp.880.pdf"},{"title":"Neural Probe–Based Hallucination Detection for Large Language Models","url":"https://arxiv.org/html/2512.20949"},{"title":"[2512.20949] Neural Probe-Based Hallucination Detection for Large Language Models","url":"https://arxiv.org/abs/2512.20949"},{"title":"REAL-TIME DETECTION OF HALLUCINATED ENTITIES","url":"https://openreview.net/pdf?id=YxJEMTflww"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Hallucination Probes","url":"https://www.hallucination-probes.com/"}]

I found several recent research papers and resources on linear probes for hallucination detection and steering. Here's what the search revealed:

## Key Research Developments

**Main Finding: "A Single Direction of Truth"**

A generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream. The consistent mid-layer plateau across four observer models supports the hypothesis that contextual hallucinations are encoded along a common linear direction in activation space.

**Detection and Steering Capabilities**

A single, highly linear residual-stream direction robustly separates hallucinated from supported spans across domains and remains readable by comparatively small observer models, offering an actionable insight into model representations. Additionally, manipulating activity along this axis in a generator steerably reduces or amplifies hallucination prevalence.

**Performance Metrics**

A single linear probe (logistic regression) achieves > 0.95 F₁ across layers 12-30 on news data and > 0.70 on logical contradictions, achieving high F₁ scores (up to 0.99 on news benchmarks).

**Token-Level Detection**

More recent work (December 2025) focuses on token-level detection: Lightweight linear probes are trained to predict from hidden activations whether a token is part of a hallucinated entity. In long-form settings, linear probes substantially outperform uncertainty-based baselines at detecting hallucinated entities, achieving 0.87 AUC on Llama-3.3-70B.

This represents an active area of research in mechanistic interpretability with promising applications for AI safety and reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96132133-3b65-4156-b729-14db85ca2cba",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "191c7f7d-8bdd-4b40-8814-72ec9abc58c2",
  "sourceToolAssistantUUID": "96132133-3b65-4156-b729-14db85ca2cba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T14:16:48.306Z_

<details><summary>↩ Tool result · `toolu_014bGi4tXxo4LnFmKhNBoUp7`</summary>

```text
Web search results for query: "faithfulness calibration generation ACL EMNLP 2026"

Links: [{"title":"The Second Workshop on Evaluation for Multimodal Generation | EvalMG26 @ SIGIR 2026","url":"https://evalmg.github.io/"},{"title":"Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-industry.54/"},{"title":"King's College London NLP","url":"https://kclnlp.github.io/publications.html"},{"title":"Area Keywords at ARR – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/areas"},{"title":"Faithful Natural Language Uncertainty Expression in LLMs","url":"https://aclanthology.org/2025.emnlp-main.1505.pdf"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Synchronous Faithfulness Monitoring for Trustworthy Retrieval-Augmented Generation - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.527/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Automated Interpretability-Driven Model Auditing and Control: A Research Agenda","url":"https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"},{"title":"Explainability and Interpretability of Multilingual Large ...","url":"https://aclanthology.org/2025.emnlp-main.1033.pdf"}]

Based on the search results, here's what I found regarding your query on faithfulness calibration and generation related to ACL/EMNLP 2026:

## Recent Research on Faithfulness and Calibration

There is active research on metrics for faithfulness and calibration in multimodal generation, which is a topic area being discussed at workshops like the Second Workshop on Evaluation for Multimodal Generation (EvalMG26) at SIGIR 2026.

Recent work includes FaithJudge, an LLM-as-a-judge framework that leverages human-annotated hallucination examples to improve automated hallucination evaluation, with an enhanced leaderboard that benchmarks LLMs on RAG faithfulness in summarization, question-answering, and data-to-text generation tasks.

## Calibration in ACL/EMNLP Research

Calibration is recognized as a key research area in interpretability and analysis of models for NLP, alongside related topics like explanation faithfulness and uncertainty in the ACL Rolling Review framework used by both ACL and EMNLP.

There is specific research on calibrating LLMs with preference optimization on thought trees for generating rationales in science question scoring, published in the Findings of EMNLP 2024.

Authors are welcome to submit papers accepted to ACL and EMNLP to related workshops, including work on generation and evaluation topics.

The search results indicate active research in this area, though there don't appear to be specific 2026 ACL/EMNLP papers specifically titled with "faithfulness calibration generation" in the available results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9229e65-6963-4f46-a8b8-5a8659e1253d",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "04d450f3-19cc-4fb8-b0f3-3a7581ee564f",
  "sourceToolAssistantUUID": "f9229e65-6963-4f46-a8b8-5a8659e1253d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T14:16:48.617Z_

<details><summary>↩ Tool result · `toolu_016H5VwKtbBAq7d19anqUEpf`</summary>

```text
Web search results for query: "activation engineering confidence LLM 2025 2026"

Links: [{"title":"LLM Testing Tools and Frameworks in 2026: The Engineering Guide","url":"https://contextqa.com/blog/llm-testing-tools-frameworks-2026/"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"2025: The year in LLMs","url":"https://simonwillison.net/2025/Dec/31/the-year-in-llms/"},{"title":"[2308.10248] Steering Language Models With Activation Engineering","url":"https://arxiv.org/abs/2308.10248"},{"title":"Evaluation of LLM-Based Software Engineering Tools: Practices, Challenges, and Future Directions","url":"https://arxiv.org/html/2604.24621v1"},{"title":"Multi-Turn LLM Evaluation in 2026: What You Need to Know - Confident AI","url":"https://www.confident-ai.com/blog/multi-turn-llm-evaluation-in-2026"},{"title":"LLM News Today (May 2026) – AI Model Releases","url":"https://llm-stats.com/ai-news"},{"title":"The Silent Evolution of LLMs in 2026 - DEV Community","url":"https://dev.to/synergy_shock/the-silent-evolution-of-llms-in-2026-2mc4"},{"title":"Privacy-Preserving LLM Inference in Practice: A","url":"https://eprint.iacr.org/2026/105.pdf"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"}]

Based on the search results, here's what I found about activation engineering, confidence, and LLMs in 2025-2026:

## Activation Engineering

Activation engineering is the inference-time modification of activations in order to control (or steer) model outputs. It involves computing steering vectors from contrasting prompts and adding them during the forward pass to shift model behavior at inference time.

Steering vectors work effectively for some behaviors like refusal, sentiment, and formality, but fail for others like factual recall and complex reasoning.

## Key 2025-2026 Developments

A significant recent advance is Conditional Activation Steering (CAST), presented at ICLR 2025, which solves the problem of steering being always-on by analyzing activation patterns during inference to decide whether to steer, projecting the hidden state onto a condition vector.

Additionally, PID-based Activation Steering frames the problem as a control system with proportional, integral, and derivative terms managing injection strength dynamically, handling strength degradation over long generation (proposed by Nguyen et al. in October 2025).

## Confidence in LLM Evaluation

Regarding confidence in LLM systems, evaluation outcomes shape both organizational confidence and individual reliance on these systems as LLMs increasingly influence developer decisions. Without explicit strategies for repeated evaluation, aggregation, or uncertainty reporting, evaluation outcomes can give a false sense of confidence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc0d0971-23b0-4f94-af0d-c0392878d847",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "1ffd1c1f-969c-4031-b172-1b2c3b3856c1",
  "sourceToolAssistantUUID": "bc0d0971-23b0-4f94-af0d-c0392878d847",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T14:16:52.279Z_

Excellent. Now let me do some targeted follow-up searches on the most promising leads I found, and fetch details on the most relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ffd1c1f-969c-4031-b172-1b2c3b3856c1",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VnQYcNwN94edw3Atqc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ffbb52d-3ff4-4a45-9f5e-3c27dcf14952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMcUhZV6ZJtxaJHwMXgSnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 376,
      "cache_creation_input_tokens": 6586,
      "cache_read_input_tokens": 13331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6586,
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

_source line 29 · 2026-05-15T14:16:53.679Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RPcpqKs7z79zPLMkrVPvkw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.12046",
  "prompt": "Extract the full title, authors, date, abstract, and key methods of this paper. Is this about claim-level confidence calibration for long-form generation? What techniques does it use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ffbb52d-3ff4-4a45-9f5e-3c27dcf14952",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VnQYcNwN94edw3Atqc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b64c5a24-36aa-4d24-8f5b-36178915048c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMcUhZV6ZJtxaJHwMXgSnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 376,
      "cache_creation_input_tokens": 6586,
      "cache_read_input_tokens": 13331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6586,
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

_source line 30 · 2026-05-15T14:16:54.626Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017pirzbKRmLhawAawAjJTKh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.06165",
  "prompt": "Extract the full title, authors, date, abstract, and key methods. Does this paper use probes to detect hallucinations and then steer generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b64c5a24-36aa-4d24-8f5b-36178915048c",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VnQYcNwN94edw3Atqc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2000e37-21d3-4131-abf0-c20eb1499278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMcUhZV6ZJtxaJHwMXgSnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 376,
      "cache_creation_input_tokens": 6586,
      "cache_read_input_tokens": 13331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6586,
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

_source line 31 · 2026-05-15T14:16:56.042Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DJPLCMT65gHPRPw7fXHTtd`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.23221v1",
  "prompt": "Extract the full title, authors, date, abstract, and key methods. Does this paper combine linear probes with activation steering to reduce hallucinations? What is the core approach?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2000e37-21d3-4131-abf0-c20eb1499278",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VnQYcNwN94edw3Atqc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b94c6c9-21c0-4aa6-b667-4a2292aa9cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMcUhZV6ZJtxaJHwMXgSnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 376,
      "cache_creation_input_tokens": 6586,
      "cache_read_input_tokens": 13331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6586,
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

_source line 32 · 2026-05-15T14:16:57.044Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LwJsVZzWi1oCzo4eNbFMYy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.20949",
  "prompt": "Extract the full title, authors, date, abstract, and key methods. Does this paper use neural probes for hallucination detection in LLMs? How does it relate to steering or calibration?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b94c6c9-21c0-4aa6-b667-4a2292aa9cd1",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VnQYcNwN94edw3Atqc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33c3c4d4-e5be-4bff-b841-a5d96578d8a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMcUhZV6ZJtxaJHwMXgSnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 376,
      "cache_creation_input_tokens": 6586,
      "cache_read_input_tokens": 13331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6586,
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

_source line 33 · 2026-05-15T14:16:57.927Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0112eJJtzzn19SD3rBWpmWAd`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.08169v1",
  "prompt": "Extract the full title, authors, date, abstract, and key methods. What is Spherical Steering and how does it differ from standard activation steering?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33c3c4d4-e5be-4bff-b841-a5d96578d8a4",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VnQYcNwN94edw3Atqc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "467153bd-537c-49e3-acc2-d2fefb872b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LMcUhZV6ZJtxaJHwMXgSnw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 376,
      "cache_creation_input_tokens": 6586,
      "cache_read_input_tokens": 13331,
      "output_tokens": 559,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 376,
          "output_tokens": 559,
          "cache_read_input_tokens": 13331,
          "cache_creation_input_tokens": 6586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6586,
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

_source line 34 · 2026-05-15T14:16:59.000Z_

<details><summary>↩ Tool result · `toolu_01RPcpqKs7z79zPLMkrVPvkw`</summary>

```text
# Paper Summary

**Full Title:** "Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration"

**Authors:** Xin Liu and Lu Wang

**Submission Date:** April 13, 2026

**Abstract Summary:**
The paper addresses hallucination in long-form LLM outputs by introducing CURE, a framework that teaches models to reason about uncertainty at the claim level rather than providing a single confidence score for entire responses.

---

## Yes, This Is About Claim-Level Confidence Calibration

The research directly targets "uncertainty at the claim level," recognizing that "uncertainty varies across individual claims" in extended generations.

---

## Key Methods

**1. Claim-Aware Reasoning Protocol**
The approach structures outputs into "atomic claims paired with explicit confidence estimates," enabling granular assessment rather than holistic scoring.

**2. Multi-Stage Training Pipeline**
The framework implements sequential optimization: first aligning confidence estimates with actual claim correctness, then optimizing for overall factual accuracy.

**3. Selective Prediction**
The calibrated confidence enables "the model to abstain from uncertain claims at inference time," allowing controlled abstention rather than confident errors.

---

## Results

Improvements include up to 39.9% gain in claim-level accuracy on biography generation and a 16.0% increase in AUROC on FactBench, demonstrating both enhanced factuality and improved calibration quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b64c5a24-36aa-4d24-8f5b-36178915048c",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "db42087c-540d-4d28-ab49-85a93e599ded",
  "sourceToolAssistantUUID": "b64c5a24-36aa-4d24-8f5b-36178915048c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T14:16:59.064Z_

<details><summary>↩ Tool result · `toolu_017pirzbKRmLhawAawAjJTKh`</summary>

```text
# HaloProbe Paper Summary

**Full Title:** HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models

**Authors:** Reihaneh Zohrabi, Hosein Hasani, Akshita Gupta, Mahdieh Soleymani Baghshah, Anna Rohrbach, Marcus Rohrbach

**Date:** Submitted April 7, 2026; revised April 10, 2026

**Abstract:** The paper addresses object hallucinations in vision-language model outputs. The authors reveal that attention-weight analysis is unreliable due to confounders like token position and object repetition, causing "Simpson's paradox" where aggregated statistics reverse trends. They introduce HaloProbe, which "factorizes external description statistics and internal decoding signals to estimate token-level hallucination probabilities."

## Does it use probes to detect and steer generation?

**Yes.** The approach uses HaloProbe as "an external scoring signal for non-invasive mitigation" through guided decoding. Rather than modifying model internals, the method detects hallucinations via a Bayesian framework and then applies this detection signal to steer the generation process, reducing hallucinations while "preserving utility."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2000e37-21d3-4131-abf0-c20eb1499278",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "754e8134-681c-4201-8017-ea43688d6d22",
  "sourceToolAssistantUUID": "e2000e37-21d3-4131-abf0-c20eb1499278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T14:17:01.381Z_

<details><summary>↩ Tool result · `toolu_01LwJsVZzWi1oCzo4eNbFMYy`</summary>

```text
# Paper Analysis: Neural Probe-Based Hallucination Detection for LLMs

## Full Citation Details
- **Title:** Neural Probe-Based Hallucination Detection for Large Language Models
- **Authors:** Shize Liang, Hongzhi Wang
- **Date:** Submitted December 24, 2025
- **arXiv ID:** 2512.20949

## Abstract Summary
The paper addresses the problem of LLMs generating false information with high confidence. The researchers propose using "lightweight MLP probes to perform nonlinear modeling" of hidden layer states while keeping language model parameters frozen.

## Key Methods
1. **Neural probe approach:** Employs multi-layer perceptron probes inserted at specific layers
2. **Optimization strategy:** Uses Bayesian optimization to determine optimal probe placement layers
3. **Training objective:** Implements a multi-objective joint loss function designed to enhance detection stability
4. **Token-level detection:** Operates at the individual token level rather than document level

## Does It Use Neural Probes?
Yes, definitively. The core innovation involves replacing traditional linear probes with neural network-based probes to capture nonlinear relationships in semantic spaces.

## Relation to Steering/Calibration
The paper does not appear to address steering or calibration directly. Instead, it focuses on **detection** of hallucinations post-hoc. The frozen language model parameters indicate this is an inspection method rather than an intervention that would modify model behavior or confidence calibration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33c3c4d4-e5be-4bff-b841-a5d96578d8a4",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "06185887-8495-4fa4-b2c6-c7b8ae0d5417",
  "sourceToolAssistantUUID": "33c3c4d4-e5be-4bff-b841-a5d96578d8a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T14:17:02.305Z_

<details><summary>↩ Tool result · `toolu_01DJPLCMT65gHPRPw7fXHTtd`</summary>

```text
# Paper Summary

**Title:** "A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations"

**Authors:** Charles O'Neill, Slava Chalnev, Chi Chi Zhao, Max Kirkby, Mudith Jayasekara

**Date:** 2507.23221v1 (July 2025 preprint)

**Abstract:** The researchers demonstrate that a generator-agnostic observer model detects contextual hallucinations through "a single forward pass and a linear probe on its residual stream." They show this approach identifies a "single, transferable linear direction" separating hallucinated from faithful text, outperforming baselines by 5–27 points.

## Core Approach

**Yes, this paper combines linear probes with activation steering.** The fundamental strategy involves:

1. **Detection Phase:** A frozen transformer ("observer model") processes concatenated source + continuation text. A logistic regression probe trained on mid-layer residual activations classifies whether the final sentence is hallucinated.

2. **Steering Phase:** The learned probe weight vector is injected into a generator's layer 10 during generation, scaled by varying coefficients. Positive scaling amplifies hallucination rates; negative scaling reduces them—demonstrating causal control over the phenomenon.

3. **Mechanistic Insight:** Gradient-times-activation attribution reveals the signal concentrates in specific late-layer MLPs (layers 7–9), creating a sparse, interpretable circuit for hallucination awareness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b94c6c9-21c0-4aa6-b667-4a2292aa9cd1",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "a84a4962-847a-458a-99a9-ffec25c7903a",
  "sourceToolAssistantUUID": "7b94c6c9-21c0-4aa6-b667-4a2292aa9cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T14:17:04.311Z_

<details><summary>↩ Tool result · `toolu_0112eJJtzzn19SD3rBWpmWAd`</summary>

```text
# Spherical Steering: Paper Summary

**Full Title:** "Spherical Steering: Geometry-Aware Activation Rotation for Language Models"

**Authors:** Zejia You (Tufts University), Chunyuan Deng (Rice University), Hanjie Chen (Rice University)

**Date:** February 2026 (arxiv 2602.08169v1)

## Abstract Overview

The paper proposes a training-free method for controlling language models by rotating internal activations rather than adding fixed vectors. The approach "rotates activations along a geodesic toward a target direction" while preserving signal magnitude, addressing the representation collapse issues inherent in traditional addition-based steering.

## Key Methods

**Spherical Steering differs from standard activation steering in three ways:**

1. **Rotation vs. Addition:** Traditional methods apply linear offsets (h' = h + λμ), which alter activation magnitudes unpredictably. Spherical Steering uses spherical linear interpolation (Slerp) to rotate normalized activations toward target directions while maintaining their original magnitude: "h' = ||h|| · Slerp(ĥ, μ_T, t)"

2. **Geometric Foundation:** The method treats normalized hidden states as directions on a unit hypersphere, leveraging the architectural bias of normalization layers that stabilize magnitudes while encoding meaning directionally.

3. **Adaptive Gating:** A von Mises-Fisher confidence gate dynamically modulates steering strength based on input uncertainty, applying stronger corrections only when needed rather than uniform intervention.

## Performance Results

Experiments show Spherical Steering achieves substantial gains: up to +15% accuracy on multiple-choice benchmarks while simultaneously improving open-ended generation quality—a Pareto improvement that addition-based methods cannot match.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "467153bd-537c-49e3-acc2-d2fefb872b1d",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "0de39ee0-c8ed-486f-9551-97fac21ae2fe",
  "sourceToolAssistantUUID": "467153bd-537c-49e3-acc2-d2fefb872b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-15T14:17:06.977Z_

Several very relevant findings. Let me now do additional targeted searches for more potential missing competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0de39ee0-c8ed-486f-9551-97fac21ae2fe",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VoZYsmyw7D4RrmVirK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8719fca-a47c-4a2c-8067-b4b1e297c77a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5qxJrjHowCgwJdRD9hJcz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2758,
      "cache_read_input_tokens": 19917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2758,
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

_source line 40 · 2026-05-15T14:17:07.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012uGWkyEV7qTz7HEeSifP23`</summary>

```json
{
  "query": "\"AFTER\" adaptive factual activation editing hallucination LVLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8719fca-a47c-4a2c-8067-b4b1e297c77a",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VoZYsmyw7D4RrmVirK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cfb3a51-3625-4047-be47-d55e76e8a39d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5qxJrjHowCgwJdRD9hJcz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2758,
      "cache_read_input_tokens": 19917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2758,
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

_source line 41 · 2026-05-15T14:17:08.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EooGy6ndEzjdmP6XcE5mQB`</summary>

```json
{
  "query": "ODESteer ODE activation steering alignment 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cfb3a51-3625-4047-be47-d55e76e8a39d",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VoZYsmyw7D4RrmVirK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86921c30-65fe-4fbb-ba51-baa7d8b2d3d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5qxJrjHowCgwJdRD9hJcz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2758,
      "cache_read_input_tokens": 19917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2758,
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

_source line 42 · 2026-05-15T14:17:09.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lh69mfo1n3SwRgiDtFwvCP`</summary>

```json
{
  "query": "\"Confidence Before Answering\" LLM uncertainty estimation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86921c30-65fe-4fbb-ba51-baa7d8b2d3d9",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VoZYsmyw7D4RrmVirK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f20e5beb-037b-4ed2-aac0-e2a5086a09aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5qxJrjHowCgwJdRD9hJcz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2758,
      "cache_read_input_tokens": 19917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2758,
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

_source line 43 · 2026-05-15T14:17:09.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D1qwEXBJEUj33medQnP949`</summary>

```json
{
  "query": "\"verbalized confidence\" self-verification LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f20e5beb-037b-4ed2-aac0-e2a5086a09aa",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VoZYsmyw7D4RrmVirK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f92ba573-c549-4656-b374-5e11cd6e93c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5qxJrjHowCgwJdRD9hJcz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2758,
      "cache_read_input_tokens": 19917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2758,
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

_source line 44 · 2026-05-15T14:17:10.242Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0119refop5R55oTr1KMznvb1`</summary>

```json
{
  "query": "CAST conditional activation steering hallucination confidence ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f92ba573-c549-4656-b374-5e11cd6e93c1",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VoZYsmyw7D4RrmVirK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "256dde0e-1fb8-4495-936c-2b8a8dbddec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5qxJrjHowCgwJdRD9hJcz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2758,
      "cache_read_input_tokens": 19917,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2758
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 19917,
          "cache_creation_input_tokens": 2758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2758,
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

_source line 45 · 2026-05-15T14:17:14.678Z_

<details><summary>↩ Tool result · `toolu_01EooGy6ndEzjdmP6XcE5mQB`</summary>

```text
Web search results for query: "ODESteer ODE activation steering alignment 2026"

Links: [{"title":"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment | OpenReview","url":"https://openreview.net/forum?id=CFewUmgIIL"},{"title":"[2602.17560v1] ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment","url":"https://arxiv.org/abs/2602.17560v1"},{"title":"ODESTEER","url":"https://odesteer.github.io/"},{"title":"[2602.17560] ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment","url":"https://arxiv.org/abs/2602.17560"},{"title":"GitHub - ZhaoHongjue/odesteer: Code for \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment\" · GitHub","url":"https://github.com/ZhaoHongjue/odesteer"},{"title":"(PDF) ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment","url":"https://www.researchgate.net/publication/400971006_ODESteer_A_Unified_ODE-Based_Steering_Framework_for_LLM_Alignment"},{"title":"ICLR Poster ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment","url":"https://iclr.cc/virtual/2026/poster/10010874"},{"title":"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment","url":"https://arxiv.org/html/2602.17560v1"},{"title":"Activation steering for LLM alignment","url":"https://openreview.net/pdf/f933859674dd8327470d752a7fe861e73fd6b6b2.pdf"},{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"}]

Based on the search results, here's what I found about ODESteer:

## Overview

ODESteer proposes a unified ordinary differential equations (ODEs)-based theoretical framework for activation steering in LLM alignment. This is a novel activation steering approach based on ordinary differential equations and barrier functions from control theory.

## Key Technical Approach

ODESteer identifies steering directions by defining the barrier function as the log-density ratio between positive and negative activations, and employs it to construct an ODE for multi-step and adaptive steering. Conventional activation addition can be interpreted as a first-order approximation to the solution of an ODE, and based on this ODE perspective, identifying a steering direction becomes equivalent to designing a barrier function from control theory.

## Performance

ODESteer achieves consistent empirical improvements on diverse LLM alignment benchmarks, with a notable 5.7% improvement over TruthfulQA, 2.5% over UltraFeedback, and 2.4% over RealToxicityPrompts.

## Publication

This is the official implementation of the paper "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment" (ICLR 2026). The paper was submitted on 19 Feb 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86921c30-65fe-4fbb-ba51-baa7d8b2d3d9",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "3c2d4e1f-0df7-4884-885c-b132039536d9",
  "sourceToolAssistantUUID": "86921c30-65fe-4fbb-ba51-baa7d8b2d3d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T14:17:14.711Z_

<details><summary>↩ Tool result · `toolu_012uGWkyEV7qTz7HEeSifP23`</summary>

```text
Web search results for query: ""AFTER" adaptive factual activation editing hallucination LVLM 2026"

Links: [{"title":"AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing [Quick Review]","url":"https://liner.com/review/after-mitigating-the-object-hallucination-of-lvlm-via-adaptive-factualguided"},{"title":"[2601.01957] AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing","url":"https://arxiv.org/abs/2601.01957"},{"title":"AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing","url":"https://arxiv.org/html/2601.01957v1"},{"title":"AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing | OpenReview","url":"https://openreview.net/forum?id=ggycXmhrrG"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"},{"title":"AFTER: MITIGATING THE OBJECT HALLUCINATION","url":"https://openreview.net/pdf/bd4e4b8446712bd63cb2b2ee5f9a07b3c285dd84.pdf"},{"title":"ACT Now: Preempting LVLM Hallucinations via Adaptive Context Integration","url":"https://arxiv.org/html/2604.00983v1"},{"title":"[2604.00983] ACT Now: Preempting LVLM Hallucinations via Adaptive Context Integration","url":"https://arxiv.org/abs/2604.00983"},{"title":"[2602.18711] HIME: Mitigating Object Hallucinations in LVLMs via Hallucination Insensitivity Model Editing","url":"https://arxiv.org/abs/2602.18711"},{"title":"Adaptive Residual-Update Steering for Low-Overhead Hallucination Mitigation in Large Vision Language Models","url":"https://arxiv.org/html/2511.10292"}]

Based on the search results, here's what I found about AFTER:

## AFTER: Adaptive Factual-Guided Activation Editing

AFTER is an ICLR 2026 paper that proposes a method for mitigating object hallucination in LVLMs via adaptive factual-guided activation editing.

### Problem Addressed
Large Vision-Language Models (LVLMs) exhibit significant object hallucination, categorizable into category, attribute, and relation types, impeding trustworthy AI applications.

### Methodology
AFTER is an effective activation editing approach that adaptively steers original activations toward factual-augmented semantics for hallucination mitigation, introducing Factual-Augmented Activation Steering (FAS) to provide positive and explicit textual guidance for LVLM activation editing by leveraging factual textual semantics.

The method comprises two main components: Factual-Augmented Activation Steering (FAS) and Query-Adaptive Offset Optimization (QAO), where FAS provides factual and general guidance for activation editing by explicitly modeling precise visual-textual associations, and QAO introduces a query-aware offset estimator to establish query-specific editing from the general steering vector.

### Performance Results
On the POPE benchmark, AFTER achieves an average improvement of 4.1% in accuracy and 2.6% in F1-score over baselines, surpassing ICT by 1.3% and 0.9% respectively. AFTER achieves up to a 16.3% reduction of hallucination over baseline on the AMBER benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cfb3a51-3625-4047-be47-d55e76e8a39d",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "fc5e5e55-4ef0-4e06-ba72-1cf204c74942",
  "sourceToolAssistantUUID": "3cfb3a51-3625-4047-be47-d55e76e8a39d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T14:17:16.615Z_

<details><summary>↩ Tool result · `toolu_01Lh69mfo1n3SwRgiDtFwvCP`</summary>

```text
Web search results for query: ""Confidence Before Answering" LLM uncertainty estimation 2026"

Links: [{"title":"[2603.05881] Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation","url":"https://arxiv.org/abs/2603.05881"},{"title":"Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation","url":"https://arxiv.org/html/2603.05881v1"}]

Based on the search results, I found a recent paper on this topic:

"Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation" was submitted on March 6, 2026.

**Key Details:**

Existing uncertainty estimation methods are predominantly answer-first, producing confidence only after generating an answer. This paper proposes a confidence-first paradigm where the model outputs its confidence before answering, interpreting this score as the model's probability of answering the question correctly under its current policy.

**The Proposed Method:**

The paper proposes CoCA (Co-optimized Confidence and Answers), a GRPO reinforcement learning framework that jointly optimizes confidence calibration and answer accuracy via segmented credit assignment. By assigning separate rewards and group-relative advantages to confidence and answer segments, CoCA enables stable joint optimization and avoids reward hacking.

**Results:**

Experiments across math, code, and factual QA benchmarks show improved calibration and uncertainty discrimination while preserving answer quality.

The paper's authors are Changcheng Li, Jiancan Wu, Hengheng Zhang, Zhengsu Chen, Guo An, Junxiang Qiu, Xiang Wang, and Qi Tian, and it has been submitted to arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f20e5beb-037b-4ed2-aac0-e2a5086a09aa",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "746e3ca9-9a31-45a9-8dc7-d6cd64641687",
  "sourceToolAssistantUUID": "f20e5beb-037b-4ed2-aac0-e2a5086a09aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T14:17:18.093Z_

<details><summary>↩ Tool result · `toolu_01D1qwEXBJEUj33medQnP949`</summary>

```text
Web search results for query: ""verbalized confidence" self-verification LLM 2026"

Links: [{"title":"VERBALIZED CONFIDENCE TRIGGERS SELF- VERIFICATION","url":"https://openreview.net/pdf/b8857b1f5781186957ee6dd362e5942c235e3584.pdf"},{"title":"Calibrating Verbalized Confidence with Self-Generated Distractors | OpenReview","url":"https://openreview.net/forum?id=pZs4hhemXc"},{"title":"Verbalized Confidence Triggers Self-Verification: Emergent Behavior Without Explicit Reasoning Supervision | OpenReview","url":"https://openreview.net/forum?id=P2o8wOzZMX"},{"title":"On Verbalized Confidence Scores for LLMs","url":"https://arxiv.org/html/2412.14737v2"},{"title":"LLMs Should Express Uncertainty Explicitly","url":"https://arxiv.org/html/2604.05306"},{"title":"Emergent Self-Verification in LLMs","url":"https://www.emergentmind.com/topics/emergent-self-verification"},{"title":"On Verbalized Confidence Scores for LLMs Daniel Yang∗ ETH Zurich","url":"https://arxiv.org/pdf/2412.14737"},{"title":"LLM Confidence and Calibration: A Survey of What the Research Actually Shows - Beancount.io","url":"https://beancount.io/bean-labs/research-logs/2026/07/09/confidence-estimation-calibration-llms-survey"},{"title":"Are LLM Decisions Faithful to Verbal Confidence? Jiawei Wang Yanfei Zhou","url":"https://arxiv.org/pdf/2601.07767"},{"title":"Preprint 2026 FACT-CHECKING WITH LARGE LANGUAGE MODELS","url":"https://www.arxiv.org/pdf/2601.02574"}]

I found several relevant papers on verbalized confidence and self-verification in LLMs from 2025-2026. Here are the key findings:

## Main Research Direction

Large language models (LLMs) are increasingly used as reasoning partners in domains such as mathematics, coding, and decision support, where reliable expression of confidence is essential for human–AI interaction.

## Key Paper: CSFT Method

The most prominent recent work is "Confidence-Supervised Fine-Tuning (CSFT), a simple method that trains models to output both an answer and an explicit confidence statement." CSFT substantially reduces calibration errors while also improving accuracy, induces emergent self-verification behaviors such as self-checking under low confidence, and although trained only on reasoning tasks, CSFT generalizes to non-reasoning benchmarks such as MMLU.

## Emergent Self-Verification Phenomenon

Emergent self-verification is the spontaneous ability of LLMs to assess the correctness of outputs using internal confidence signals without explicit external supervision. Fine-tuning with scalar confidence targets alone, without explicit reasoning labels or reward signals, triggers spontaneous emergence of self-verifying behavior.

## Challenges and Alternative Approaches

However, there are important caveats: verbalized LLM-generated confidence scores have empirically been found to be miscalibrated, reporting high confidence on instances with low accuracy and thereby harming trust and safety. Recent work explores alternative methods, such as Distractor-Normalized Coherence (DINCO), which estimates and accounts for an LLM's suggestibility bias by having the model verbalize its confidence independently across several self-generated distractors (i.e. alternative claims), and normalizes by the total verbalized confidence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f92ba573-c549-4656-b374-5e11cd6e93c1",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "ea2bc266-3c64-4829-9dcd-a4c13b963129",
  "sourceToolAssistantUUID": "f92ba573-c549-4656-b374-5e11cd6e93c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T14:17:18.949Z_

<details><summary>↩ Tool result · `toolu_0119refop5R55oTr1KMznvb1`</summary>

```text
Web search results for query: "CAST conditional activation steering hallucination confidence ICLR 2025"

Links: [{"title":"PROGRAMMING REFUSAL WITH CONDITIONAL ACTIVATION STEERING for ICLR 2025 - IBM Research","url":"https://research.ibm.com/publications/programming-refusal-with-conditional-activation-steering--1"},{"title":"Paper Code 50+ ! Conditional Activation Steering Programming Refusal with","url":"https://iclr.cc/media/iclr-2025/Slides/29806.pdf"},{"title":"Programming Refusal with Conditional Activation Steering | OpenReview","url":"https://openreview.net/forum?id=Oi47wc10sm"},{"title":"activation-steering/docs/faq.md at main · IBM/activation-steering","url":"https://github.com/IBM/activation-steering/blob/main/docs/faq.md"},{"title":"Published as a conference paper at ICLR 2025 PROGRAMMING REFUSAL WITH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf"},{"title":"Programming Refusal with Conditional Activation Steering","url":"https://arxiv.org/html/2409.05907v3"},{"title":"[2409.05907] Programming Refusal with Conditional Activation Steering","url":"https://arxiv.org/abs/2409.05907"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"[2605.04641] CAST: Mitigating Object Hallucination in Large Vision-Language Models via Caption-Guided Visual Attention Steering","url":"https://arxiv.org/abs/2605.04641"}]

Based on the search results, I found information about CAST and ICLR 2025:

## Conditional Activation Steering (CAST) - ICLR 2025

CAST analyzes LLM activation patterns during inference to selectively apply or withhold activation steering based on the input context. The method is based on the observation that different categories of prompts activate distinct patterns in the model's hidden states.

**Key Innovation:**
CAST uses two types of vectors: Behavior vectors that modify the model's behavior, and Condition vectors that represent certain activation patterns induced by the prompt during the inference process. The key idea of CAST is to apply the behavior vector only when a certain condition is met.

**Applications:**
Using CAST, one can systematically control LLM behavior with rules like "if input is about hate speech or adult content, then refuse" or "if input is not about legal advice, then refuse."

**Advantages:**
CAST maintains the data, runtime, and compute efficiency of activation steering while adding controllability, enabling the implementation of behavioral rules in LLMs without significant costs.

The paper was presented as a Spotlight at ICLR 2025, and an open-source implementation is available at github.com/IBM/activation-steering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "256dde0e-1fb8-4495-936c-2b8a8dbddec2",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "01172e8a-dbfb-456b-aec2-dc7230879f57",
  "sourceToolAssistantUUID": "256dde0e-1fb8-4495-936c-2b8a8dbddec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-15T14:17:21.704Z_

Let me fetch more details on a few more promising leads and do additional searches for things I haven't covered yet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01172e8a-dbfb-456b-aec2-dc7230879f57",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VpeEBrJWfsJhdP4hED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3553734a-ec97-424b-bbfd-9cfd9ec4a313",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAJakK3knCi4Uf7hEbVUCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4388,
      "cache_read_input_tokens": 22675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4388,
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

_source line 51 · 2026-05-15T14:17:23.604Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013xuooVzZm6kUDcuq4gm5yV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.05306",
  "prompt": "Extract the full title, authors, date, abstract, and key methods. Does this paper address verbalized uncertainty in long-form LLM generation? What is the core contribution?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3553734a-ec97-424b-bbfd-9cfd9ec4a313",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VpeEBrJWfsJhdP4hED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0ff57b1-a09e-4f40-bf1b-12192942f6eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAJakK3knCi4Uf7hEbVUCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4388,
      "cache_read_input_tokens": 22675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4388,
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

_source line 52 · 2026-05-15T14:17:24.546Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AWqHLtEvrShuNJcP9aXFP6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.01957",
  "prompt": "Extract the full title, authors, date, and abstract. What are the core methods - does it combine factual probes with activation steering?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0ff57b1-a09e-4f40-bf1b-12192942f6eb",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VpeEBrJWfsJhdP4hED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49bd7f49-f6bb-4bb3-a313-8d0652420cea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAJakK3knCi4Uf7hEbVUCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4388,
      "cache_read_input_tokens": 22675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4388,
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

_source line 53 · 2026-05-15T14:17:25.483Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L6CNLbphouJLAmwYGbxoVT`</summary>

```json
{
  "query": "\"steering vector\" \"factuality\" \"confidence\" LLM arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49bd7f49-f6bb-4bb3-a313-8d0652420cea",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VpeEBrJWfsJhdP4hED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e3210bb-00f7-4ba4-ad53-d35b793e39ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAJakK3knCi4Uf7hEbVUCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4388,
      "cache_read_input_tokens": 22675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4388,
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

_source line 54 · 2026-05-15T14:17:25.954Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pv6wAxpuffESL5BHapuMAy`</summary>

```json
{
  "query": "PID activation steering long generation hallucination Nguyen 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e3210bb-00f7-4ba4-ad53-d35b793e39ff",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VpeEBrJWfsJhdP4hED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60a1bd0d-c831-4e6b-ad50-f3d1aba520c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAJakK3knCi4Uf7hEbVUCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4388,
      "cache_read_input_tokens": 22675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4388,
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

_source line 55 · 2026-05-15T14:17:26.428Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LnmzXsCZbpuwMmkiC7fDmr`</summary>

```json
{
  "query": "\"AUSteer\" atomic unit activation steering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60a1bd0d-c831-4e6b-ad50-f3d1aba520c7",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VpeEBrJWfsJhdP4hED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6475a1e6-c749-4383-bdd1-811640a9756f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAJakK3knCi4Uf7hEbVUCZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4388,
      "cache_read_input_tokens": 22675,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4388
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 386,
          "cache_read_input_tokens": 22675,
          "cache_creation_input_tokens": 4388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4388,
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

_source line 56 · 2026-05-15T14:17:29.059Z_

<details><summary>↩ Tool result · `toolu_01AWqHLtEvrShuNJcP9aXFP6`</summary>

```text
# Paper Summary

**Full Title:** "AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing"

**Authors:** Tianbo Wang, Yuqing Ma, Kewei Liao, Zhange Zhang, Simin Li, Jinyang Guo, Xianglong Liu

**Date:** Submitted January 5, 2026

**Abstract:** The research addresses object hallucination in Large Vision-Language Models by proposing "Adaptive Factual-guided Visual-Textual Editing for hallucination mitigation (AFTER)." The approach "achieves up to a 16.3% reduction of hallucination over baseline on the AMBER benchmark."

## Core Methods

Yes, the approach combines factual semantics with activation steering:

1. **Factual-Augmented Activation Steering (FAS)**: This component "provide[s] factual and general guidance for activation editing," establishing connections between visual and textual information.

2. **Query-Adaptive Offset Optimization (QAO)**: This introduces "a query-aware offset estimator to establish query-specific editing from the general steering vector," enabling customized interventions per input.

The method differs from prior work by explicitly leveraging factual textual semantics to combat language bias rather than applying generic editing strategies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49bd7f49-f6bb-4bb3-a313-8d0652420cea",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "9a02437c-8fb6-49b6-9527-7be8ffb37096",
  "sourceToolAssistantUUID": "49bd7f49-f6bb-4bb3-a313-8d0652420cea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T14:17:29.101Z_

<details><summary>↩ Tool result · `toolu_013xuooVzZm6kUDcuq4gm5yV`</summary>

```text
# Paper Summary

**Full Title:** LLMs Should Express Uncertainty Explicitly

**Authors:** Junyu Guo, Shangding Gu, Ming Jin, Costas Spanos, Javad Lavaei

**Date:** Submitted April 7, 2026; revised May 13, 2026

**Abstract Summary:**
The paper addresses how large language models can be trained to signal uncertainty within their responses. It investigates two approaches: "end-of-reasoning self-assessment" where models verbalize confidence scores, and "during-reasoning self-assessment" using `&lt;uncertain>` markers when reasoning appears unreliable.

## Does It Address Verbalized Uncertainty?

Yes, directly. The research explicitly examines training methods to make uncertainty "explicit," comparing confidence verbalization at response completion versus uncertainty signals during the reasoning process itself.

## Core Contributions

1. **Two uncertainty signaling mechanisms:** The paper contrasts end-of-response confidence verbalization with in-process uncertainty markers, demonstrating both reduce overconfident errors.

2. **Practical improvements:** Both approaches trigger better retrieval-augmented generation (RAG) integration and improve answer quality across factual reasoning tasks.

3. **Mechanistic insights:** Analysis reveals that verbalized confidence "sharpens a confidence-related structure already present in the pretrained model," while `&lt;uncertain>` markers teach models to flag high-risk reasoning steps, with changes concentrated in later model layers.

The work directly targets the problem of confident-yet-incorrect LLM responses through transparent uncertainty expression mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0ff57b1-a09e-4f40-bf1b-12192942f6eb",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "f9737f0c-d0ef-4400-abba-e3faefdb9987",
  "sourceToolAssistantUUID": "d0ff57b1-a09e-4f40-bf1b-12192942f6eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T14:17:32.425Z_

<details><summary>↩ Tool result · `toolu_01Pv6wAxpuffESL5BHapuMAy`</summary>

```text
Web search results for query: "PID activation steering long generation hallucination Nguyen 2025"

Links: [{"title":"Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.634/"},{"title":"Activation Steering Decoding: Mitigating Hallucination in ...","url":"https://aclanthology.org/2025.acl-long.634.pdf"},{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/html/2602.21704v1"},{"title":"Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention","url":"https://chatpaper.com/paper/176030"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention | Request PDF","url":"https://www.researchgate.net/publication/394298568_Activation_Steering_Decoding_Mitigating_Hallucination_in_Large_Vision-Language_Models_through_Bidirectional_Hidden_State_Intervention"},{"title":"The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering | OpenReview","url":"https://openreview.net/forum?id=7BKcLeHQsm"},{"title":"Adaptive Residual-Update Steering for Low-Overhead Hallucination Mitigation in Large Vision Language Models","url":"https://arxiv.org/html/2511.10292"},{"title":"ICML Poster The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering","url":"https://icml.cc/virtual/2025/poster/46338"},{"title":"SteerVLM: Robust Model Control through Lightweight ...","url":"https://aclanthology.org/2025.findings-emnlp.1285.pdf"}]

Based on the search results, I found relevant research on activation steering and hallucination mitigation in large vision-language models from 2025:

## Key Research Findings

The research identifies directional patterns of hallucination in the activation space using a small calibration set, then employs a contrast decoding mechanism that computes the difference between positive and negative steering predictions.

This approach effectively suppresses hallucination patterns while preserving the model's general capabilities, with extensive experiments demonstrating significant hallucination reduction across multiple benchmarks while maintaining performance on general visual understanding tasks.

### Notable Approaches:

1. **Activation Steering Decoding (ASD)**: ASD operates by identifying directional patterns of hallucination in the activation space using a small calibration set, then employing a contrast decoding mechanism that effectively suppresses hallucination patterns while preserving the model's general capabilities.

2. **Dynamic Multimodal Activation Steering**: This is a training-free approach to mitigate hallucination in LVLMs by dynamically intervening in attention heads during inference time.

3. **VISTA**: VISTA (Visual Information Steering with Token-logit Augmentation) is a training-free inference-time intervention framework that works by combining visual information reinforcement in activation space and leveraging early layer activations to promote semantically meaningful decoding.

All these methods share the common benefit that they require no model re-training or architectural modifications, making them readily applicable to existing deployed models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60a1bd0d-c831-4e6b-ad50-f3d1aba520c7",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "c7aaf3b5-6824-4a51-855b-e26ec96617e7",
  "sourceToolAssistantUUID": "60a1bd0d-c831-4e6b-ad50-f3d1aba520c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T14:17:32.565Z_

<details><summary>↩ Tool result · `toolu_01L6CNLbphouJLAmwYGbxoVT`</summary>

```text
Web search results for query: ""steering vector" "factuality" "confidence" LLM arxiv 2026"

Links: [{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/html/2503.02863v2"},{"title":"Steering Vector Fields for Context-Aware Inference-Time ...","url":"https://www.arxiv.org/pdf/2602.01654"},{"title":"Enhancing LLM Steering through Sparse Autoencoder-Based Vector Refinement","url":"https://arxiv.org/html/2509.23799v1"},{"title":"One-shot Optimized Steering Vectors Mediate Safety- ...","url":"https://arxiv.org/pdf/2502.18862"},{"title":"Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics","url":"https://arxiv.org/html/2512.16602"},{"title":"Investigating Generalization of One-shot LLM Steering Vectors","url":"https://arxiv.org/html/2502.18862v1"},{"title":"Towards Inference-time Category-wise Safety Steering for Large Language Models","url":"https://arxiv.org/html/2410.01174v1"},{"title":"[2505.17760] But what is your honest answer? Aiding LLM-judges with honest alternatives using steering vectors","url":"https://arxiv.org/abs/2505.17760"},{"title":"Analysing the Safety Pitfalls of Steering Vectors","url":"https://arxiv.org/html/2603.24543v1"},{"title":"[2512.16602] Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics","url":"https://arxiv.org/abs/2512.16602"}]

I found several recent papers on arxiv from 2025-2026 related to steering vectors for LLMs. Here are the key findings:

## Main Results

SteerConf introduces a steering prompt strategy that guides LLMs to produce confidence scores in specified directions (e.g., conservative or optimistic), along with a steered confidence consistency measure and calibration method.

A paper on "Steering Vector Fields for Context-Aware Inference-Time" was published on February 3, 2026, and discusses how a global steering vector can become misaligned with locally effective directions, and context-dependent steering can mitigate this failure mode.

JUSSA (Judge Using Safety-Steered Alternatives) is a framework that leverages a model's internal representations to optimize an honesty-promoting steering vector from a single training example.

Researchers derive steering vectors from differences in residual stream activations between positive and negative examples of behaviors (e.g., factual vs. hallucinatory responses).

The Refusal Steering method uses an LLM-as-a-judge to assign refusal confidence scores and proposes a ridge-regularized variant to compute steering vectors that better isolate the refusal-compliance direction.

These papers explore the intersection of steering vectors, factuality, and confidence in LLMs through various inference-time techniques that don't require model retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e3210bb-00f7-4ba4-ad53-d35b793e39ff",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "879af0cd-d07a-4370-8bf2-e63256cd46dd",
  "sourceToolAssistantUUID": "3e3210bb-00f7-4ba4-ad53-d35b793e39ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T14:17:34.928Z_

<details><summary>↩ Tool result · `toolu_01LnmzXsCZbpuwMmkiC7fDmr`</summary>

```text
Web search results for query: ""AUSteer" atomic unit activation steering 2026"

Links: [{"title":"GitHub - zijian678/AUSteer: ICLR 2026 Fine-Grained Activation Steering: Steering Less, Achieving More · GitHub","url":"https://github.com/zijian678/AUSteer"},{"title":"[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/abs/2602.04428"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/html/2602.04428v1"},{"title":"Published as a conference paper at ICLR 2026 FINE-GRAINED ACTIVATION STEERING:","url":"https://openreview.net/pdf?id=guSVafqhrB"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"WSTS 2026 Tutorial: Atomic Clocks as Primary Frequency Sources - YouTube","url":"https://www.youtube.com/watch?v=uQMoJbGOfE8"},{"title":"James Bridle / Austeer","url":"https://jamesbridle.com/works/austeer"},{"title":"Automatically Reengage the Tesla's Autosteer","url":"https://www.enhauto.com/blogs/all/automatically-re-engage-the-autosteer-all-tesla-models"},{"title":"Atomic Redster S9 FIS SL Ski 2026 – Skiis & Biikes","url":"https://skiisandbiikes.com/products/atomic-redster-s9-fis-sl-ski-2026"},{"title":"Steering Awareness: Detecting Activation Steering from Within","url":"https://arxiv.org/html/2511.21399v3"}]

Based on the search results, here's what I found about AUSteer:

## Overview

AUSteer is a method for fine-grained activation steering that breaks LLM blocks into fine-grained atomic units (AUs) for targeted intervention, published at ICLR 2026.

## The Problem It Addresses

Existing activation steering methods typically intervene at the block level, steering bundled activations of selected attention heads and feedforward networks, but block-level activations are inherently heterogeneous, entangling beneficial, irrelevant, and harmful features, making block-level steering coarse, inefficient, and intrusive.

## How AUSteer Works

AUSteer decomposes block activations into fine-grained atomic unit (AU)-level activations, where each AU-level activation corresponds to a single dimension of the block activation, and each AU denotes a slice of the block weight matrix.

AUSteer is a simple and efficient method that operates at the AU level, first identifying discriminative AUs globally by computing activation momenta on contrastive samples, then assigning adaptive steering strengths tailored to diverse inputs and selected AU activations.

## Key Results

Comprehensive experiments on multiple LLMs and tasks show that AUSteer consistently surpasses advanced baselines while steering considerably fewer activations, demonstrating that steering less achieves more.

The work is available on [arXiv](https://arxiv.org/abs/2602.04428) and has been published at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6475a1e6-c749-4383-bdd1-811640a9756f",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "7c5d8071-fb9e-4aa2-97e3-708d3e591ad1",
  "sourceToolAssistantUUID": "6475a1e6-c749-4383-bdd1-811640a9756f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-15T14:17:37.376Z_

Let me now search for a few more specific areas that could be relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c5d8071-fb9e-4aa2-97e3-708d3e591ad1",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VqpT81GTx3Qn5wF6vj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59ac622a-3087-4e47-a95d-c9fe23a2d0d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoyPvJ7NP5jyRHS81NiQxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3720,
      "cache_read_input_tokens": 27063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3720,
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

_source line 62 · 2026-05-15T14:17:38.794Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S7wZBFPriqx4JH3mToNdJ8`</summary>

```json
{
  "query": "\"Fact-Level Calibration\" \"Correction\" long-form generation ACM WWW 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59ac622a-3087-4e47-a95d-c9fe23a2d0d0",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VqpT81GTx3Qn5wF6vj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69b7ba71-f7ee-4969-87bd-519389db816f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoyPvJ7NP5jyRHS81NiQxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3720,
      "cache_read_input_tokens": 27063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3720,
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

_source line 63 · 2026-05-15T14:17:39.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WtdYtJuAn2eg7tcXBFefNq`</summary>

```json
{
  "query": "\"Steering Vector Fields\" context-aware inference 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69b7ba71-f7ee-4969-87bd-519389db816f",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VqpT81GTx3Qn5wF6vj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f22f2e19-3726-4134-9402-3e2b0d421902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoyPvJ7NP5jyRHS81NiQxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3720,
      "cache_read_input_tokens": 27063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3720,
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

_source line 64 · 2026-05-15T14:17:40.214Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E6Y5QycXyAPGKxQaT8ye59`</summary>

```json
{
  "query": "DINCO \"distractor normalized coherence\" verbalized confidence calibration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f22f2e19-3726-4134-9402-3e2b0d421902",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VqpT81GTx3Qn5wF6vj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3461835-3eda-42ce-abdc-cd7820db3099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoyPvJ7NP5jyRHS81NiQxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3720,
      "cache_read_input_tokens": 27063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3720,
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

_source line 65 · 2026-05-15T14:17:40.717Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HZxFwPnfZtitWrHynovjDd`</summary>

```json
{
  "query": "\"hallucination trajectory\" \"attractor dynamics\" transformer generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3461835-3eda-42ce-abdc-cd7820db3099",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VqpT81GTx3Qn5wF6vj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2865c803-d658-4336-893d-c55102ab001e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoyPvJ7NP5jyRHS81NiQxD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3720,
      "cache_read_input_tokens": 27063,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 27063,
          "cache_creation_input_tokens": 3720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3720,
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

_source line 66 · 2026-05-15T14:17:44.784Z_

<details><summary>↩ Tool result · `toolu_01S7wZBFPriqx4JH3mToNdJ8`</summary>

```text
Web search results for query: ""Fact-Level Calibration" "Correction" long-form generation ACM WWW 2025"

Links: [{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730195"},{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Request PDF","url":"https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations"},{"title":"Fact-Level Calibration and Correction for Long-Form ...","url":"https://dl.acm.org/doi/pdf/10.1145/3726302.3730195"},{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://doi.org/10.1145/3726302.3730195"},{"title":"Atomic Calibration of LLMs in Long-Form Generations","url":"https://arxiv.org/html/2410.13246"},{"title":"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality","url":"https://arxiv.org/html/2605.01749"},{"title":"Fact-Level Confidence Calibration and Self-Correction","url":"https://arxiv.org/html/2411.13343v1"},{"title":"Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration","url":"https://arxiv.org/html/2604.12046"},{"title":"[2411.13343] Fact-Level Confidence Calibration and Self-Correction","url":"https://arxiv.org/abs/2411.13343"},{"title":"[2410.13246] Atomic Calibration of LLMs in Long-Form Generations","url":"https://arxiv.org/abs/2410.13246"}]

I found the paper you're looking for! Here's what I found:

The paper proposes a fact-level confidence calibration framework that evaluates and adjusts confidence at the granularity of individual facts, incorporating both relevance and correctness. Based on this framework, the authors introduce CARE (Confidence-Aware Fact Correction), a method that leverages high-confidence facts to iteratively refine and correct low-confidence ones.

The research addresses how large language models (LLMs) generate hallucinations as a critical reliability issue. While confidence calibration can help align a model's confidence with its actual accuracy, traditional confidence calibration at the response level is inadequate for long-form generation, which involves complex outputs composed of multiple atomic facts, each with varying confidence, correctness, and relevance to the query.

Experimental results demonstrate that CARE effectively improves the quality of generated content. The code is available at https://github.com/yuanyige/fact-calibration.

The paper was published in the Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '25).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69b7ba71-f7ee-4969-87bd-519389db816f",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "e4cacf50-d05e-46f5-8c3f-f253944b6a8a",
  "sourceToolAssistantUUID": "69b7ba71-f7ee-4969-87bd-519389db816f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-15T14:17:46.407Z_

<details><summary>↩ Tool result · `toolu_01WtdYtJuAn2eg7tcXBFefNq`</summary>

```text
Web search results for query: ""Steering Vector Fields" context-aware inference 2026 arxiv"

Links: [{"title":"[2602.01654] Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models","url":"https://arxiv.org/abs/2602.01654"},{"title":"Steering Vector Fields for Context-Aware Inference-Time ...","url":"https://www.arxiv.org/pdf/2602.01654"},{"title":"Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models","url":"https://arxiv.org/html/2602.01654"},{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"},{"title":"[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/abs/2605.05892"},{"title":"Reliable Control-Point Selection for Steering Reasoning in ...","url":"https://arxiv.org/pdf/2604.02113"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Analysing the Safety Pitfalls of Steering Vectors","url":"https://arxiv.org/html/2603.24543v1"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326v2"},{"title":"A Unified Understanding and Evaluation of Steering Methods","url":"https://arxiv.org/html/2502.02716v2"}]

I found relevant research on Steering Vector Fields for context-aware inference. Here's what the latest work shows:

## Steering Vector Fields (SVF)

Steering vectors offer a lightweight way to control large language models at inference time by shifting hidden activations, providing a practical middle ground between prompting and fine-tuning. However, steering vectors can be unreliable in practice, with some concepts being unsteerable, backfiring for a fraction of inputs, and reliability degrading in long-form generation and multi-attribute steering.

A static steering vector applies the same update vector everywhere in representation space, implicitly assuming that the concept-improving direction is constant across contexts, but when the locally effective direction varies with the current activation, a single global vector can become misaligned, yielding weak or reversed effects.

## The SVF Approach

Steering Vector Fields learns a differentiable concept scoring function whose local gradient defines the steering direction at each activation, making interventions explicitly context-dependent. This formulation supports coordinated multi-layer interventions in a shared, aligned concept space, and enables efficient long-form and multi-attribute control within a unified framework.

The paper was submitted on February 2, 2026, by authors Jiaqian Li, Yanshu Li, and Kuan-Hao Huang and is available on arXiv as paper 2602.01654.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f22f2e19-3726-4134-9402-3e2b0d421902",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "62c66e03-9c79-48e7-be60-b0ac2bebf495",
  "sourceToolAssistantUUID": "f22f2e19-3726-4134-9402-3e2b0d421902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T14:17:47.376Z_

<details><summary>↩ Tool result · `toolu_01E6Y5QycXyAPGKxQaT8ye59`</summary>

```text
Web search results for query: "DINCO "distractor normalized coherence" verbalized confidence calibration 2026"

Links: [{"title":"Calibrating Verbalized Confidence with Self-Generated Distractors | OpenReview","url":"https://openreview.net/forum?id=pZs4hhemXc"},{"title":"Calibrating Verbalized Confidence with Self-Generated Distractors","url":"https://arxiv.org/html/2509.25532"},{"title":"CALIBRATING VERBALIZED CONFIDENCE WITH SELF- GENERATED DISTRACTORS Victor Wang","url":"https://www.arxiv.org/pdf/2509.25532"},{"title":"Elias Stengel-Eskin on X: \"🚨 Introducing DINCO, a zero-resource calibration method for verbalized LLM confidence. We normalize over self-generated distractors to enforce coherence ➡️ better-calibrated and less saturated (more usable) confidence! ⚠️ Problem: Standard verbalized confidence is overconfident https://t.co/Q1HgeDPq8a\" / X","url":"https://x.com/EliasEskin/status/1973795473296122277"},{"title":"CALIBRATING VERBALIZED CONFIDENCE WITH SELF","url":"https://openreview.net/pdf/3388c3931e254457b3b649ec3728c4dbbc7ebcf8.pdf"},{"title":"GitHub - victorwang37/dinco · GitHub","url":"https://github.com/victorwang37/dinco"},{"title":"Self-Calibrating Language Models via Test-Time Discriminative Distillation","url":"https://arxiv.org/html/2604.09624"},{"title":"Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models","url":"https://arxiv.org/html/2502.11028v3"},{"title":"Overconfidence, Calibration, and Distractor Effects in Large ...","url":"https://openreview.net/pdf?id=lyaHnHDdZl"},{"title":"BEYOND BINARY REWARDS: TRAINING LMS TO REASON ABOUT THEIR UNCERTAINTY","url":"https://arxiv.org/pdf/2507.16806"}]

Based on the web search results, I found comprehensive information about DINCO and its related concepts:

## DINCO: Distractor-Normalized Coherence

DINCO (Distractor-Normalized Coherence) is a method that estimates and accounts for an LLM's suggestibility bias by having the model verbalize its confidence independently across several self-generated distractors (alternative claims), and normalizes by the total verbalized confidence.

## The Problem It Addresses

Verbalized LLM-generated confidence scores have empirically been found to be miscalibrated, reporting high confidence on instances with low accuracy and thereby harming trust and safety. This overconfidence often stems from an LLM's heightened suggestibility when faced with claims that it encodes little information about.

## How DINCO Works

DINCO integrates self-consistency (leveraging coherence across sampled generations) with normalized verbalized confidence (leveraging coherence across validations on incompatible claims) into a single approach. DINCO has the LLM verbalize its confidence independently on several self-generated distractors to estimate and correct for the bias caused by suggestibility.

## Performance Results

DINCO provides less saturated – and therefore more usable – confidence estimates, with DINCO at 10 runs outperforming self-consistency at 100. DINCO is able to leverage incoherence across related claims to normalize verbalized confidence and achieve strong calibration.

The research was published in 2025-2026, with code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3461835-3eda-42ce-abdc-cd7820db3099",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "4b0a5c58-e3cd-4d7c-af65-9dc393fd0e0f",
  "sourceToolAssistantUUID": "c3461835-3eda-42ce-abdc-cd7820db3099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-15T14:17:50.536Z_

<details><summary>↩ Tool result · `toolu_01HZxFwPnfZtitWrHynovjDd`</summary>

```text
Web search results for query: ""hallucination trajectory" "attractor dynamics" transformer generation 2026"

Links: [{"title":"[2604.15400] Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/abs/2604.15400"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400"},{"title":"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/html/2605.05686"},{"title":"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/html/2604.04743"},{"title":"From Dispersion to Attraction: Spectral Dynamics of Hallucination Across Whisper Model Scales","url":"https://arxiv.org/html/2604.08591v1"},{"title":"From Noise to Narrative: Tracing the Origins of Hallucinations in Transformers","url":"https://arxiv.org/html/2509.06938v1"},{"title":"Bridging known and unknown dynamics by transformer-based machine-learning inference from sparse observations | Nature Communications","url":"https://www.nature.com/articles/s41467-025-63019-8"},{"title":"From Noise to Narrative: Tracing the Origins of Hallucinations in Transformers | OpenReview","url":"https://openreview.net/forum?id=xd7cXU2P4G"},{"title":"[2605.05686] Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/abs/2605.05686"},{"title":"Transformer Dynamics: A Neuroscientific Approach to Interpretability of Large","url":"https://2025.ccneuro.org/abstract_pdf/Fernando_2025_Transformer_Dynamics_A_Neuroscientific_Approach_Interpretability.pdf"}]

I found several highly relevant research papers on this topic. Here's what the search results reveal:

## Key Research Findings

### Hallucination as Trajectory Commitment

A recent paper presents causal evidence that hallucination in autoregressive language models is an early trajectory commitment governed by asymmetric attractor dynamics. On the Qwen2.5-1.5B model across 61 prompts spanning six categories, 27 prompts (44.3%) bifurcate with factual and hallucinated trajectories diverging at the first generated token.

The asymmetry is interpreted through dynamical systems: hallucination operates as a locally stable attractor basin in the residual stream state space, characterized by easy entry and difficult escape. Activation patching reveals that injecting hallucinated activations into correct trajectories corrupts output in 87.5% of trials, while the reverse recovers only 33.3%; window patching shows correction requires sustained multi-step intervention, whereas corruption needs only a single perturbation.

### Attractor Geometry of Transformer Memory

Another recent work analyzes how memory sources interact through attractor geometry. In the hidden-state space of autoregressive generation, learned facts form attractor basins; conflict occurs when working memory disrupts convergence to the correct basin without raising output entropy, and hallucination occurs when the hidden state drifts freely when no memorized basin exists.

### Hallucination Basins Framework

Research reframes hallucinations as a dynamical systems phenomenon: attractor-like hallucination basins in layerwise latent spaces. Pushing factual representation vectors towards hallucination basins increases the probability of hallucination, directly indicating the presence of an attractor-like basin.

These papers represent cutting-edge 2026 research on understanding hallucinations through the lens of dynamical systems and attractor dynamics in transformer models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2865c803-d658-4336-893d-c55102ab001e",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "bbe4e2cb-7c4c-4826-8951-a2bb881dd705",
  "sourceToolAssistantUUID": "2865c803-d658-4336-893d-c55102ab001e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-15T14:17:54.207Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KhC3AW6Chw6x75rWi53Sgf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.01749",
  "prompt": "Extract the full title, authors, date, abstract, and key methods. What is the core approach - does it address calibration-aware generation for long-form factuality?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbe4e2cb-7c4c-4826-8951-a2bb881dd705",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VryA2ctRGKWXQSajsB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57e9a30c-df7f-4568-8c4a-a0e5e75ee8df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9vBoFJ7xR4uNRpa56NiVN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 30783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3783,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 71 · 2026-05-15T14:17:55.151Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CcbEKL9D7fM92PxQ13ZbFf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05892",
  "prompt": "Extract the full title, authors, date, abstract, and key methods. What is the core approach of this flow-based activation steering paper?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57e9a30c-df7f-4568-8c4a-a0e5e75ee8df",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VryA2ctRGKWXQSajsB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26d138e6-b1bb-42bf-b0b6-4e71429389ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9vBoFJ7xR4uNRpa56NiVN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 30783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3783,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 72 · 2026-05-15T14:17:55.662Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FboGe7EzJZt5vrbHcqEc3z`</summary>

```json
{
  "query": "\"Only Say What You Know\" calibration-aware generation long-form factuality 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26d138e6-b1bb-42bf-b0b6-4e71429389ca",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VryA2ctRGKWXQSajsB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5ae6a4f-8db9-42e2-94e3-4c37a2612d37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9vBoFJ7xR4uNRpa56NiVN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 30783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3783,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 73 · 2026-05-15T14:17:56.109Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LJLm6Aav51Q9X5vRJJgfn9`</summary>

```json
{
  "query": "CoCA \"co-optimized confidence\" GRPO reinforcement learning calibration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5ae6a4f-8db9-42e2-94e3-4c37a2612d37",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VryA2ctRGKWXQSajsB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dae840b-1e87-4e7a-a500-27a692883a26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9vBoFJ7xR4uNRpa56NiVN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3783,
      "cache_read_input_tokens": 30783,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3783
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 30783,
          "cache_creation_input_tokens": 3783,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3783,
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

_source line 74 · 2026-05-15T14:17:59.305Z_

<details><summary>↩ Tool result · `toolu_01KhC3AW6Chw6x75rWi53Sgf`</summary>

```text
# Paper Summary: Calibration-Aware Generation for Long-Form Factuality

**Full Title:** "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality"

**Authors:** Wen Luo, Guangyue Peng, Liang Wang, Nan Yang, Wei Li, Yuhan Song, Shaohang Wei, Feifan Song, Furu Wei, and Houfeng Wang

**Submission Date:** May 3, 2026

**Core Abstract:** The paper addresses hallucinations in large reasoning models during long-form generation by proposing "Calibration-Aware Generation (CAG)," a framework that "equips models with end-to-end, calibration-aware generation capabilities."

**Key Approach:**

The methodology introduces an "Exploration-Commitment Decoupling" paradigm that separates knowledge exploration from final output commitment. Rather than propagating all intermediate reasoning to conclusions, the system incorporates "calibrated reliability estimates" and prioritizes dependable information in final responses. This enables models to "explore with awareness while answering cautiously."

**Results:** Testing across five factuality benchmarks demonstrated factuality improvements reaching 13% while reducing decoding time by approximately 37% across multiple model families.

**Core Innovation:** The fundamental contribution involves decoupling reasoning exploration from output commitment, enabling more selective and reliable information integration rather than unconditionally preserving intermediate steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57e9a30c-df7f-4568-8c4a-a0e5e75ee8df",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "0edd7629-3e68-44be-961b-514081f2b59a",
  "sourceToolAssistantUUID": "57e9a30c-df7f-4568-8c4a-a0e5e75ee8df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-15T14:18:00.327Z_

<details><summary>↩ Tool result · `toolu_01CcbEKL9D7fM92PxQ13ZbFf`</summary>

```text
# Flow-based Activation Steering Paper Summary

**Full Title:** Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention

**Authors:** Zehao Jin, Ruixuan Deng, Junran Wang, Xinjie Shen, Chao Zhang

**Submission Date:** May 7, 2026

**Abstract:**
The paper addresses limitations in existing activation steering methods. The researchers note that "activation steering has emerged as a promising alternative for controlling language-model behavior at inference time" while keeping parameters frozen. However, current approaches underperform simple prompting and struggle with generalization.

**Core Approach:**

FLAS (Flow-based Activation Steering) represents a fundamental departure from prior methods. Rather than using fixed, single-step transformations, the approach "learns a general, concept-conditioned velocity field" that guides activation transformations across multiple steps and positions.

**Key Innovation:**

The learned flow demonstrates "curved, multi-step, token-varying trajectories," suggesting that activation space geometry is more complex than previously theorized. On AxBench benchmarks, FLAS achieved harmonic means of 1.015 (Gemma-2-2B-IT) and 1.113 (Gemma-2-9B-IT), becoming the first learned method to consistently surpass prompting baselines without requiring per-concept tuning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26d138e6-b1bb-42bf-b0b6-4e71429389ca",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "0fec15aa-5e1f-4f39-9f13-03cc4be847e2",
  "sourceToolAssistantUUID": "26d138e6-b1bb-42bf-b0b6-4e71429389ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-15T14:18:02.491Z_

<details><summary>↩ Tool result · `toolu_01FboGe7EzJZt5vrbHcqEc3z`</summary>

```text
Web search results for query: ""Only Say What You Know" calibration-aware generation long-form factuality 2026"

Links: [{"title":"[2605.01749] Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality","url":"https://arxiv.org/abs/2605.01749"},{"title":"Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality","url":"https://arxiv.org/html/2605.01749"},{"title":"Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control for Agentic Systems","url":"https://arxiv.org/html/2604.17487"},{"title":"Conformal Linguistic Calibration: Trading-off between ...","url":"https://openreview.net/pdf/55aa4de08b2f5bcfa9155bb9c656e887cfb2d7e5.pdf"},{"title":"DeepMind FACTS Framework 2026: LLM Factual Accuracy Guide","url":"https://galileo.ai/blog/deepmind-facts-framework-llm-factual-accuracy"},{"title":"Towards Dependable Retrieval-Augmented Generation Using Factual Confidence Prediction","url":"https://arxiv.org/html/2605.05244v1"},{"title":"The FACTS Leaderboard: A Comprehensive Benchmark for ...","url":"https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf"},{"title":"The Second Workshop on Evaluation for Multimodal Generation | EvalMG26 @ SIGIR 2026","url":"https://evalmg.github.io/"},{"title":"Mitigating Hallucinations in LLMs via Self-Evaluation","url":"https://aclanthology.org/2024.acl-long.107.pdf"},{"title":"Factuality in LLMs: Key Metrics and Improvement Strategies","url":"https://www.turing.com/resources/llm-factuality-guide"}]

Based on the search results, here's what I found about "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality":

## Overview

This is an arXiv paper (2605.01749) titled "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality", submitted on May 3, 2026.

## Core Problem and Approach

Large Reasoning Models achieve strong performance on complex tasks but remain prone to hallucinations, particularly in long-form generation where errors compound across reasoning steps. The paper proposes an Exploration-Commitment Decoupling paradigm that disentangles knowledge exploration from final commitment, enabling models to explore with awareness while answering cautiously, instantiated through Calibration-Aware Generation (CAG), a framework that augments intermediate reasoning with calibrated reliability estimates and prioritizes reliable content in final outputs.

## Results

Across five long-form factuality benchmarks and multiple model families, CAG improves factuality by up to 13%, while reducing decoding time by up to 37%.

## Key Insight

The work highlights decoupling as a principled approach for more reliable long-form generation, offering directions for trustworthy and self-aware generative systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5ae6a4f-8db9-42e2-94e3-4c37a2612d37",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "c5442cdf-3cca-4c5a-97a1-4386f79c6483",
  "sourceToolAssistantUUID": "a5ae6a4f-8db9-42e2-94e3-4c37a2612d37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-15T14:18:02.873Z_

<details><summary>↩ Tool result · `toolu_01LJLm6Aav51Q9X5vRJJgfn9`</summary>

```text
Web search results for query: "CoCA "co-optimized confidence" GRPO reinforcement learning calibration 2026"

Links: [{"title":"Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation","url":"https://arxiv.org/html/2603.05881v1"},{"title":"Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards","url":"https://arxiv.org/html/2603.09117"},{"title":"GRPO++: A Controlled Differentiable Reinforcement Learning Reranking Method for Retrieval-Augmented Generation | Research Square","url":"https://www.researchsquare.com/article/rs-8088895/v1"},{"title":"Paper page - Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards","url":"https://huggingface.co/papers/2603.09117"},{"title":"Balancing Classification and Calibration Performance in Decision-Making LLMs via Calibration Aware Reinforcement Learning","url":"https://arxiv.org/html/2601.13284"},{"title":"VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning","url":"https://arxiv.org/html/2604.09529"},{"title":"Co-GRPO: Co-Optimized Group Relative Policy Optimization for Masked Diffusion Model","url":"https://co-grpo.github.io/"},{"title":"Cooper: Co-Optimizing Policy and Reward Models in Reinforcement Learning for Large Language Models","url":"https://arxiv.org/html/2508.05613v1"},{"title":"Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning","url":"https://arxiv.org/html/2512.19920v3"},{"title":"CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs","url":"https://arxiv.org/html/2602.03048"}]

Based on the search results, I found relevant information about CoCA and its relationship to GRPO reinforcement learning and calibration:

## Summary of Key Findings

CoCA (Co-optimized Confidence and Answers) is an end-to-end, confidence-first learning framework that jointly optimizes confidence calibration and answer quality without requiring separate modules or frozen labels.

The key idea is to have the model verbalize its confidence before generating the answer, then co-optimize both through a unified policy gradient objective with segment-specific credit assignment.

### Technical Approach with GRPO

The algorithm separates the generation of confidence and answer into two distinct segments, and applies segment-specific rewards via a modified group-based reinforcement learning procedure. CoCA builds upon Group Relative Policy Optimization (GRPO) and introduces dynamic confidence targets, aligning confidence targets to group-wise empirical success rates observed during policy rollouts, grounding confidence in the model's real-time performance so estimates naturally track evolving model capabilities without requiring re-labeling.

### Performance Results

CoCA consistently attains lower calibration error, higher AUROC, and stronger selective accuracy, while maintaining comparable accuracy relative to RLVR.

The research paper appears to have been published in March 2026, making it a very recent contribution to the field of LLM confidence calibration using reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dae840b-1e87-4e7a-a500-27a692883a26",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "bddc5836-d88f-4a12-981e-88addd50abf0",
  "sourceToolAssistantUUID": "8dae840b-1e87-4e7a-a500-27a692883a26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-15T14:18:06.581Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019DdodkenmyT2YcqEGxMSNj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.09117",
  "prompt": "Extract the full title, authors, date, abstract, and key methods. Does this paper address decoupling reasoning from confidence calibration in LLMs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bddc5836-d88f-4a12-981e-88addd50abf0",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VssvYCbCXETu7CF4PD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b0ac612-6029-4999-9f54-942ff26dd1de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YWhhVYukLqefBvi4P8ywC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2689,
      "cache_read_input_tokens": 34566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2689,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 79 · 2026-05-15T14:18:07.626Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015PxUM6UavvdMuddsJthbHs`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.17487",
  "prompt": "Extract the full title, authors, date, abstract, and key methods. Does this paper address claim-level specificity or confidence calibration in agentic or long-form settings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b0ac612-6029-4999-9f54-942ff26dd1de",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VssvYCbCXETu7CF4PD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecd5420a-9233-4a76-a84a-0fc8c64a2223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YWhhVYukLqefBvi4P8ywC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2689,
      "cache_read_input_tokens": 34566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2689,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 80 · 2026-05-15T14:18:08.065Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WLoGKLUJRTP4Rae5bA9rW5`</summary>

```json
{
  "query": "\"behaviorally calibrated reinforcement learning\" hallucination LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecd5420a-9233-4a76-a84a-0fc8c64a2223",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VssvYCbCXETu7CF4PD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9760ddd9-d509-48e5-9a3d-f04f89eae23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YWhhVYukLqefBvi4P8ywC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2689,
      "cache_read_input_tokens": 34566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2689,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 81 · 2026-05-15T14:18:08.278Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RPdPKAc9qoCqpKnfCdKd4v`</summary>

```json
{
  "query": "\"Conformal Linguistic Calibration\" long-form abstention 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9760ddd9-d509-48e5-9a3d-f04f89eae23a",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VssvYCbCXETu7CF4PD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc1c3d92-abf1-41e7-b47d-f7fe14333460",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YWhhVYukLqefBvi4P8ywC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2689,
      "cache_read_input_tokens": 34566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2689,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 82 · 2026-05-15T14:18:11.219Z_

<details><summary>↩ Tool result · `toolu_019DdodkenmyT2YcqEGxMSNj`</summary>

```text
# Paper Summary

**Full Title:** Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards

**Authors:** Zhengzhao Ma, Xueru Wen, Boxi Cao, Yaojie Lu, Hongyu Lin, Jinglin Yang, Min He, Xianpei Han, Le Sun

**Date:** Submitted March 10, 2026; revised April 30, 2026

**Abstract:** The research identifies a critical problem in reasoning-enhanced large language models: when trained on verifiable rewards, these systems become "excessively over-confident in incorrect answers." The authors demonstrate a fundamental conflict between optimizing for accuracy and calibrating confidence levels.

**Key Methods:** The paper proposes DCPO, a framework that "systematically decouples reasoning and calibration objectives." Rather than combining both goals into a single optimization target, this separation allows the model to maintain accuracy performance while independently improving confidence calibration.

**Does it address the core question?** Yes, directly. The paper's entire premise revolves around solving the decoupling of reasoning from confidence calibration—this is explicitly stated in the title and developed throughout their theoretical analysis and proposed solution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b0ac612-6029-4999-9f54-942ff26dd1de",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "181af9c3-b7e4-4762-bc56-be30e1472ff4",
  "sourceToolAssistantUUID": "2b0ac612-6029-4999-9f54-942ff26dd1de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-15T14:18:13.853Z_

<details><summary>↩ Tool result · `toolu_015PxUM6UavvdMuddsJthbHs`</summary>

```text
# Paper Summary

**Title:** "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control for Agentic Systems"

**Authors:** Tianyi Huang, Samuel Xu, Jason Tansong Dang, Samuel Yan, Kimberley Yin

**Date:** April 19, 2026 (arXiv:2604.17487v1)

## Abstract
The paper addresses how agentic systems often fail by being "too precise" rather than entirely wrong. It introduces compositional selective specificity (CSS), a post-generation layer that decomposes answers into claims and emits each claim "at the most specific calibrated level that appears admissible." The method expresses uncertainty through localized semantic backoff rather than whole-answer refusal. On LongFact evaluation, calibrated CSS improves utility from 0.846 to 0.913 while maintaining 0.938 specificity retention.

## Key Methods
1. **Claim Decomposition:** Extracting atomic claims from draft responses
2. **Backoff Ladder:** For each claim, offering fine-grained, coarse, or omit options
3. **Support Scoring:** Evaluating evidence alignment for each formulation
4. **Calibrated Selection:** Using Clopper-Pearson confidence bounds to set thresholds maximizing utility while constraining unsupported emissions

## Relevance
Yes—this paper directly addresses claim-level specificity control and uncertainty calibration in agentic/long-form settings, treating overcommitment as a compositional control problem rather than binary accept/reject.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecd5420a-9233-4a76-a84a-0fc8c64a2223",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "5291b8ec-e786-4f51-8f15-0bd7addf737b",
  "sourceToolAssistantUUID": "ecd5420a-9233-4a76-a84a-0fc8c64a2223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T14:18:14.822Z_

<details><summary>↩ Tool result · `toolu_01RPdPKAc9qoCqpKnfCdKd4v`</summary>

```text
Web search results for query: ""Conformal Linguistic Calibration" long-form abstention 2026"

Links: [{"title":"Conformal Linguistic Calibration: Trading-off between Factuality and Specificity","url":"https://arxiv.org/html/2502.19110v1"},{"title":"Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/html/2604.27914"},{"title":"Conformal Linguistic Calibration: Trading-off between ...","url":"https://openreview.net/pdf/55aa4de08b2f5bcfa9155bb9c656e887cfb2d7e5.pdf"},{"title":"[2502.19110] Conformal Linguistic Calibration: Trading-off between Factuality and Specificity","url":"https://arxiv.org/abs/2502.19110"},{"title":"[2604.27914] Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/abs/2604.27914"},{"title":"[PDF] Conformal Linguistic Calibration: Trading-off between Factuality and Specificity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Conformal-Linguistic-Calibration:-Trading-off-and-Jiang-Liu/ea16dc1da90be36ee67e6e7d5181005234dd7e8f"},{"title":"(PDF) Conformal Linguistic Calibration: Trading-off between Factuality and Specificity","url":"https://www.researchgate.net/publication/389391889_Conformal_Linguistic_Calibration_Trading-off_between_Factuality_and_Specificity"},{"title":"Linguistic Calibration of Long-Form Generations","url":"https://storage.prod.researchhub.com/uploads/papers/2024/06/07/2404.00474_3qeRnOG.pdf"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"},{"title":"[Literature Review] Conformal Linguistic Calibration: Trading-off between Factuality and Specificity","url":"https://www.themoonlight.io/en/review/conformal-linguistic-calibration-trading-off-between-factuality-and-specificity"}]

Based on the search results, I found relevant information about Conformal Linguistic Calibration and its relationship to abstention:

## Conformal Linguistic Calibration Overview

Conformal Linguistic Calibration (CLC) is a method that captures model uncertainty through the generation of responses that commit to more or less possible worlds. CLC reinterprets linguistic calibration as answer set prediction.

## Connection to Abstention

Linguistic calibration can be viewed as a form of "soft abstension", where traditional "abstention" corresponds to committing to a universal set of all possible worlds. This represents a key conceptual link between the two approaches.

## Key Advantages Over Traditional Abstention

While abstention improves factuality by answering only a small subset of questions, CLC answers all questions while still enhancing factuality. Additionally, on challenging datasets like SimpleQA—where models struggle to confidently answer even a few questions—CLC significantly outperforms abstention, and yields more consistent factuality gains as the relaxation percentage increases, whereas abstention becomes unstable at higher abstention ratios.

## Long-Form Applications

The method produces calibrated outputs with conformal guarantees on factual accuracy and enables fine-tuning models to perform uncertainty-aware adaptive claim rewriting, offering a controllable balance between factuality and specificity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc1c3d92-abf1-41e7-b47d-f7fe14333460",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "7e60372b-f110-4aa7-abd6-c1084700ebc0",
  "sourceToolAssistantUUID": "fc1c3d92-abf1-41e7-b47d-f7fe14333460",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-15T14:18:16.097Z_

<details><summary>↩ Tool result · `toolu_01WLoGKLUJRTP4Rae5bA9rW5`</summary>

```text
Web search results for query: ""behaviorally calibrated reinforcement learning" hallucination LLM 2026"

Links: [{"title":"[2512.19920] Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning","url":"https://arxiv.org/abs/2512.19920"},{"title":"Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning","url":"https://arxiv.org/html/2512.19920v1"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"Mitigating LLM Hallucination via Behaviorally Calibrated ...","url":"https://www.researchgate.net/publication/399026655_Mitigating_LLM_Hallucination_via_Behaviorally_Calibrated_Reinforcement_Learning"},{"title":"Mitigating LLM Hallucination via Behaviorally Calibrated ...","url":"https://chatpaper.com/chatpaper/paper/221228"},{"title":"Thinking, Faithful and Stable: Mitigating Hallucinations in LLMs","url":"https://cs224r.stanford.edu/projects/pdfs/Final_Report_CS224r.pdf"},{"title":"TruthRL: Incentivizing Truthful LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2509.25760"},{"title":"Why Language Models Hallucinate Adam Tauman Kalai∗ OpenAI Ofir Nachum OpenAI","url":"https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf"},{"title":"[2604.22779] KARL: Mitigating Hallucinations in LLMs via Knowledge-Boundary-Aware Reinforcement Learning","url":"https://arxiv.org/abs/2604.22779"},{"title":"Evaluating large language models for accuracy incentivizes hallucinations | Nature","url":"https://www.nature.com/articles/s41586-026-10549-w"}]

I found relevant research on this topic. Here are the key findings from the search results:

## Overview

LLM deployment in critical domains is currently impeded by persistent hallucinations—generating plausible but factually incorrect assertions.

## The Core Problem with Standard Training

Standard RLVR paradigms, utilizing binary reward signals, inadvertently incentivize models as good test-takers rather than honest communicators, encouraging guessing whenever correctness probability exceeds zero. Hallucination is not merely stochastic error but a predictable statistical consequence of training objectives prioritizing mimicking data distribution over epistemic honesty.

## Behavioral Calibration Approach

Behavioral calibration incentivizes models to stochastically admit uncertainty by abstaining when not confident, aligning model behavior with accuracy. Rather than requiring the model to output a probabilistic confidence, it must formulate the most useful response in which it is at least t confident. Behavioral calibration can be audited by comparing accuracy and error rates across thresholds.

## Recent 2026 Research Results

A recent paper from January 2026 demonstrates promising results: Empirical analysis reveals behavior-calibrated reinforcement learning allows smaller models to surpass frontier models in uncertainty quantification—a transferable meta-skill decouplable from raw predictive accuracy. A 4B LLM achieves zero-shot calibration error on par with frontier models including Grok-4 and Gemini-2.5-Pro, even though its factual accuracy is much lower.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9760ddd9-d509-48e5-9a3d-f04f89eae23a",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "ec7dcb57-da1c-4f9c-ad44-3a26542dc408",
  "sourceToolAssistantUUID": "9760ddd9-d509-48e5-9a3d-f04f89eae23a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-15T14:18:19.352Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018ii93UZA5tjcjb83jQkQMd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.19920",
  "prompt": "Extract the full title, authors, date, abstract. Is this paper about calibrated RL for reducing hallucination? What venue was it published at?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec7dcb57-da1c-4f9c-ad44-3a26542dc408",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VtrS262C9fTHMMwkEE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cba798e2-c352-4102-b827-c59e9f83afb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTd8wkVCniZsMq7Cz116io",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 1987,
      "cache_read_input_tokens": 37255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1987,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 87 · 2026-05-15T14:18:20.282Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Dzf4Hiw1RavpHXgm9djqMC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.19110",
  "prompt": "Extract the full title, authors, date, abstract. What is the venue? Does it do claim-level rewriting for calibration?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cba798e2-c352-4102-b827-c59e9f83afb3",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VtrS262C9fTHMMwkEE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfd17919-275d-4cd2-ae32-ca714ffd5dc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTd8wkVCniZsMq7Cz116io",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 1987,
      "cache_read_input_tokens": 37255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1987,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 88 · 2026-05-15T14:18:21.208Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pc2ZZHaEzRg2m7XHSwbXeQ`</summary>

```json
{
  "query": "\"CARE\" fact-level confidence correction long-form SIGIR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfd17919-275d-4cd2-ae32-ca714ffd5dc6",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VtrS262C9fTHMMwkEE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e20a5f58-7bcc-4aaf-a52d-170debde509b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTd8wkVCniZsMq7Cz116io",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 1987,
      "cache_read_input_tokens": 37255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1987,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 89 · 2026-05-15T14:18:21.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MXKjr8yQyrMGvRUFN4hbj2`</summary>

```json
{
  "query": "\"Atomic Calibration\" long-form generation LLM IJCNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e20a5f58-7bcc-4aaf-a52d-170debde509b",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VtrS262C9fTHMMwkEE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31a248cb-9894-4ed2-b9cc-61c974a4c264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTd8wkVCniZsMq7Cz116io",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 1987,
      "cache_read_input_tokens": 37255,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1987
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 929,
          "output_tokens": 316,
          "cache_read_input_tokens": 37255,
          "cache_creation_input_tokens": 1987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1987,
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

_source line 90 · 2026-05-15T14:18:23.586Z_

<details><summary>↩ Tool result · `toolu_018ii93UZA5tjcjb83jQkQMd`</summary>

```text
# Paper Summary

**Full Title:** "Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning"

**Authors:** Jiayun Wu, Jiashuo Liu, Zhiyuan Zeng, Tianyang Zhan, Tianle Cai, Wenhao Huang

**Date:** Submitted December 22, 2025; last revised January 28, 2026 (arXiv:2512.19920)

**Is this about calibrated RL for reducing hallucination?** Yes. The paper proposes "behavioral calibration, which incentivizes models to stochastically admit uncertainty by abstaining when not confident, aligning model behavior with accuracy." This approach uses reinforcement learning optimized with strictly proper scoring rules to address hallucination problems.

**Venue:** This is an arXiv preprint (not yet published in a peer-reviewed venue). It's categorized under Machine Learning (cs.LG) and Artificial Intelligence (cs.AI).

**Abstract Summary:** The research demonstrates that smaller models trained with this approach can surpass frontier models in uncertainty quantification, achieving calibration performance comparable to GPT-5 and Gemini-2.5-Pro on cross-domain factual QA tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cba798e2-c352-4102-b827-c59e9f83afb3",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "c98df793-5350-4efa-8ca3-0ff8905953bf",
  "sourceToolAssistantUUID": "cba798e2-c352-4102-b827-c59e9f83afb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-15T14:18:27.017Z_

<details><summary>↩ Tool result · `toolu_01Dzf4Hiw1RavpHXgm9djqMC`</summary>

```text
# Paper Summary

**Title:** "Conformal Linguistic Calibration: Trading-off between Factuality and Specificity"

**Authors:** Zhengping Jiang, Anqi Liu, Benjamin Van Durme

**Date:** Submitted February 26, 2025 (latest version August 11, 2025)

**Abstract:** The authors propose a unified framework that interprets linguistic calibration as answer set prediction. They present a method connecting abstention and hedged statements through linguistic pragmatics, enabling controlled imprecision in model responses with "conformal guarantees on factual accuracy."

**Venue:** This is a preprint on arXiv in the Computer Science > Computation and Language category (cs.CL), not yet published at a peer-reviewed conference or journal.

**Claim-Level Rewriting:** Yes. The paper explicitly states their approach "enables fine-tuning models to perform uncertainty-aware adaptive claim rewriting, offering a controllable balance between factuality and specificity."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfd17919-275d-4cd2-ae32-ca714ffd5dc6",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "89ca9c7c-b45b-4e5a-9d07-107b72ea4bcd",
  "sourceToolAssistantUUID": "dfd17919-275d-4cd2-ae32-ca714ffd5dc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-15T14:18:27.270Z_

<details><summary>↩ Tool result · `toolu_01Pc2ZZHaEzRg2m7XHSwbXeQ`</summary>

```text
Web search results for query: ""CARE" fact-level confidence correction long-form SIGIR 2025"

Links: [{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Request PDF","url":"https://www.researchgate.net/publication/393657638_Fact-Level_Calibration_and_Correction_for_Long-Form_Generations"},{"title":"Fact-Level Calibration and Correction for Long-Form Generations | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730195"},{"title":"SIGIR 2025, Padua, 13-18 July | Accepted Papers - Unipd","url":"https://sigir2025.dei.unipd.it/accepted-papers.html"},{"title":"Fact Verification in Knowledge Graphs Using LLMs","url":"https://www.dei.unipd.it/~silvello/papers/2025-SIGIR_Demo_LLM.pdf"},{"title":"(PDF) SIGIR 2025 -- LiveRAG Challenge Report","url":"https://www.researchgate.net/publication/393477229_SIGIR_2025_--_LiveRAG_Challenge_Report"},{"title":"PAPER Chat as Learning in Interactive Information Retrieval and Generation","url":"https://www.sigir.org/wp-content/uploads/2025/09/p02.pdf"},{"title":"SIGIR-AP 2025","url":"https://www.sigir-ap.org/sigir-ap-2025/accepted-papers/index.html"},{"title":"The Great Nugget Recall: Automating Fact Extraction and RAG Evaluation with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/393658928_The_Great_Nugget_Recall_Automating_Fact_Extraction_and_RAG_Evaluation_with_Large_Language_Models"},{"title":"Fact sheet | SIGIR","url":"https://sigir.org/general-information/fact-sheet/"},{"title":"Chapter 14: Completing ‘Summary of findings’ tables and grading the certainty of the evidence | Cochrane","url":"https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14"}]

Based on the search results, here's what I found about CARE and fact-level confidence correction for long-form generation at SIGIR 2025:

Large language models (LLMs) have achieved remarkable progress across various domains, yet their tendency to generate hallucinations remains a critical barrier to their practical reliability. Confidence calibration addresses this challenge by aligning a model's confidence with its actual accuracy, improving self-evaluation and trustworthiness.

The research proposes a fact-level confidence calibration framework that evaluates and adjusts confidence at the granularity of individual facts, incorporating both relevance and correctness. Based on this framework, CARE (Confidence-Aware Fact Correction) is introduced as a method that leverages high-confidence facts to iteratively refine and correct low-confidence ones.

Experimental results demonstrate that CARE effectively improves the quality of generated content. The code is available at https://github.com/yuanyige/fact-calibration.

The paper "Fact-Level Calibration and Correction for Long-Form Generations" by Yige Yuan, Bingbing Xu, Hexiang Tan, Fei Sun, Teng Xiao, Wei Li, Huawei Shen, and Xueqi Cheng was accepted to SIGIR 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e20a5f58-7bcc-4aaf-a52d-170debde509b",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "c7211354-7b55-4794-aa58-75ca031518d0",
  "sourceToolAssistantUUID": "e20a5f58-7bcc-4aaf-a52d-170debde509b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-15T14:18:28.048Z_

<details><summary>↩ Tool result · `toolu_01MXKjr8yQyrMGvRUFN4hbj2`</summary>

```text
Web search results for query: ""Atomic Calibration" long-form generation LLM IJCNLP 2025"

Links: [{"title":"Atomic Calibration of LLMs in Long-Form Generations - ACL Anthology","url":"https://aclanthology.org/2025.findings-ijcnlp.9/"},{"title":"Atomic Calibration of LLMs in Long-Form Generations","url":"https://aclanthology.org/2025.findings-ijcnlp.9.pdf"},{"title":"Atomic Calibration of LLMs in Long-Form Generations","url":"https://arxiv.org/html/2410.13246"},{"title":"[2410.13246] Atomic Calibration of LLMs in Long-Form Generations","url":"https://arxiv.org/abs/2410.13246"},{"title":"Atomic Calibration of LLMs in Long-Form Generations","url":"https://www.researchgate.net/publication/385010223_Atomic_Calibration_of_LLMs_in_Long-Form_Generations"},{"title":"dblp: IJCNLP-AACL 2025 - Long Papers","url":"https://dblp.org/db/conf/ijcnlp/ijcnlp2025-l.html"},{"title":"Atomic Calibration of LLMs in Long-Form Generations | OpenReview","url":"https://openreview.net/forum?id=rzsjUC45xf"},{"title":"Atomic Consistency Preference Optimization for Long-Form Question Answering - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.106/"},{"title":"Simple Factuality Probes Detect Hallucinations in Long- ...","url":"https://aclanthology.org/2025.findings-emnlp.880.pdf"},{"title":"IUQ: Interrogative Uncertainty Quantification for Long-Form Large Language Model Generation","url":"https://arxiv.org/html/2604.15109v1"}]

Based on the search results, here's what I found about "Atomic Calibration" for LLM long-form generation at IJCNLP 2025:

## Paper Overview

The paper "Atomic Calibration of LLMs in Long-Form Generations" was presented at the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics in Mumbai, India. The authors are Caiqi Zhang, Ruihan Yang, Zhisong Zhang, Xinting Huang, Sen Yang, Dong Yu, and Nigel Collier.

## Key Contribution

The work systematically studies atomic calibration, which evaluates factuality calibration at a fine-grained level by decomposing long responses into atomic claims. Prior work mainly focuses on short-form tasks using a single response-level score (macro calibration), which is insufficient for long-form outputs that may contain both accurate and inaccurate claims.

## Main Findings

The experiments demonstrate that LLMs exhibit poorer calibration at the atomic level during long-form generation, and atomic calibration uncovers insightful patterns regarding the alignment of confidence methods and the changes of confidence throughout generation.

## Methodology

The work categorizes existing confidence elicitation methods into discriminative and generative types, and proposes two new confidence fusion strategies to improve calibration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31a248cb-9894-4ed2-b9cc-61c974a4c264",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "18fe6df6-14fb-477a-b0f2-062ed289157b",
  "sourceToolAssistantUUID": "31a248cb-9894-4ed2-b9cc-61c974a4c264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 94 · 2026-05-15T14:18:30.321Z_

Let me do a few more targeted searches to ensure comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18fe6df6-14fb-477a-b0f2-062ed289157b",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VujfkYtciBi42kyQUZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09c30492-0acc-4109-b64d-af6b090cc95f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Hy4dEtdKEx1QuB96RPRfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 39242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3600,
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

_source line 95 · 2026-05-15T14:18:30.771Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016vs3EGQ4miUZC6S2M9xH9F`</summary>

```json
{
  "query": "\"Simple Factuality Probes\" hallucinations long-form EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09c30492-0acc-4109-b64d-af6b090cc95f",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VujfkYtciBi42kyQUZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f056a816-57cd-46f2-b25e-871d94fc4486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Hy4dEtdKEx1QuB96RPRfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 39242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3600,
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

_source line 96 · 2026-05-15T14:18:31.745Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QaVKRDhEgziBfUQmmt2Bws`</summary>

```json
{
  "query": "\"CSFT\" \"confidence supervised fine-tuning\" self-verification LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f056a816-57cd-46f2-b25e-871d94fc4486",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VujfkYtciBi42kyQUZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eba7e12a-f309-4cf1-a5c6-e3d588466f8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Hy4dEtdKEx1QuB96RPRfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 39242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3600,
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

_source line 97 · 2026-05-15T14:18:32.206Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01888MZ2LxmtUgcdbNANaQdZ`</summary>

```json
{
  "query": "\"Geometry-Calibrated Conformal Abstention\" language models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eba7e12a-f309-4cf1-a5c6-e3d588466f8a",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VujfkYtciBi42kyQUZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4931d449-e41a-42fd-9b31-a33f092968bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Hy4dEtdKEx1QuB96RPRfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 39242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3600,
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

_source line 98 · 2026-05-15T14:18:32.951Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014U2Q12PCdXzqjW4f92DQRq`</summary>

```json
{
  "query": "\"HALP\" hallucination prediction internal representations single forward pass 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4931d449-e41a-42fd-9b31-a33f092968bb",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VujfkYtciBi42kyQUZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d9110b5-0242-4264-938c-544184458d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Hy4dEtdKEx1QuB96RPRfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 39242,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3600
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 39242,
          "cache_creation_input_tokens": 3600,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3600,
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

_source line 99 · 2026-05-15T14:18:37.060Z_

<details><summary>↩ Tool result · `toolu_016vs3EGQ4miUZC6S2M9xH9F`</summary>

```text
Web search results for query: ""Simple Factuality Probes" hallucinations long-form EMNLP 2025"

Links: [{"title":"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.880/"},{"title":"Simple Factuality Probes Detect Hallucinations in Long- ...","url":"https://aclanthology.org/2025.findings-emnlp.880.pdf"},{"title":"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.findings-emnlp.880@ACL"},{"title":"Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation | Request PDF","url":"https://www.researchgate.net/publication/397419109_Simple_Factuality_Probes_Detect_Hallucinations_in_Long-Form_Natural_Language_Generation"},{"title":"An Empirical Study on Hallucinations in Embodied Agents ...","url":"https://aclanthology.org/2025.findings-emnlp.1158.pdf"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Published as a conference paper at ICLR 2025","url":"https://belinkov.com/assets/pdf/iclr2025-know.pdf"},{"title":"The Mirage of Hallucination Detection","url":"https://aclanthology.org/2025.findings-emnlp.1035.pdf"},{"title":"Hallucination Detection in LLMs Using Spectral Features of ...","url":"https://aclanthology.org/2025.emnlp-main.1239.pdf"}]

I found the paper you're looking for! Here are the key details:

## Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation

This paper was published in the Findings of the Association for Computational Linguistics: EMNLP 2025 in November 2025. The authors are Jiatong Han, Neil Band, Muhammed Razzak, Jannik Kossen, Tim G. J. Rudner, and Yarin Gal.

### Main Contributions

The paper presents a remarkably simple baseline for detecting hallucinations in long-form LLM generations, with performance comparable to expensive multi-sample approaches while drawing only a single sample from the LLM generator.

The key finding is that LLM hidden states are highly predictive of factuality in long-form natural language generation and that this information can be efficiently extracted at inference time using a lightweight probe.

### Performance Results

The approach achieves competitive performance with up to 100x fewer FLOPs when benchmarked across open-weight models up to 405B parameters. Additionally, the probes generalize to out-of-distribution model outputs, evaluated using hidden states of smaller open-source models.

The paper is available at the ACL Anthology: https://aclanthology.org/2025.findings-emnlp.880/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f056a816-57cd-46f2-b25e-871d94fc4486",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "aad5c1c2-0eb5-4fce-824b-b9863ce66d66",
  "sourceToolAssistantUUID": "f056a816-57cd-46f2-b25e-871d94fc4486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-15T14:18:38.847Z_

<details><summary>↩ Tool result · `toolu_01QaVKRDhEgziBfUQmmt2Bws`</summary>

```text
Web search results for query: ""CSFT" "confidence supervised fine-tuning" self-verification LLM 2026"

Links: [{"title":"Confidence-Supervised Fine-Tuning","url":"https://www.emergentmind.com/topics/confidence-supervised-fine-tuning-csft"},{"title":"Verbalized Confidence Triggers Self-Verification: Emergent Behavior Without Explicit Reasoning Supervision | OpenReview","url":"https://openreview.net/forum?id=P2o8wOzZMX"},{"title":"Verbalized Confidence Triggers Self-Verification : Emergent Behavior Without Explicit Reasoning Supervision","url":"https://arxiv.org/html/2506.03723v1"},{"title":"[2604.24070] Distilling Self-Consistency into Verbal Confidence: A Pre-Registered Negative Result and Post-Hoc Rescue on Gemma 3 4B","url":"https://arxiv.org/abs/2604.24070"},{"title":"Supervised Fine-Tuning (SFT) for LLMs - GeeksforGeeks","url":"https://www.geeksforgeeks.org/artificial-intelligence/supervised-fine-tuning-sft-for-llms/"},{"title":"Supervised fine-tuning (SFT) — Klu","url":"https://klu.ai/glossary/supervised-fine-tuning"},{"title":"Supervised Fine-Tuning · Hugging Face","url":"https://huggingface.co/learn/llm-course/en/chapter11/3"},{"title":"Continuous Supervised Fine-Tuning (CSFT)","url":"https://www.emergentmind.com/topics/continuous-supervised-fine-tuning-csft"},{"title":"V-STaR: Training Verifiers for Self-Taught Reasoners","url":"https://openreview.net/pdf?id=stmqBSW2dV"},{"title":"SFT: Supervised Fine Tuning Overview","url":"https://www.emergentmind.com/topics/supervised-fine-tuning-sft-8be35a93-039c-48d1-aade-59b226ca72cb"}]

I found comprehensive information about CSFT and self-verification in LLMs. Here are the key findings:

## What is CSFT?

Confidence-Supervised Fine-Tuning (CSFT) is a simple method that trains models to output both an answer and an explicit confidence statement. It is an effective method for calibrating verbalized confidence in LLMs under reasoning scenarios, without requiring explicit supervision of the reasoning process, and fine-tunes the model to calibrate its verbalized confidence while also producing a CoT reasoning trace and final answer.

## Self-Verification Behavior

One of the most notable findings is that self-verification rates in LLMs increase from <1.5% to ~20% overall (and nearly 100% in the lowest-confidence bin) after CSFT. CSFT elicits the emergence of self-verification behavior, particularly in low-confidence scenarios, despite not providing any explicit supervision related to reasoning strategies during training.

## Performance Improvements

LLMs fine-tuned with CSFT achieve substantial improvements across multiple evaluation metrics—including accuracy and ECE—on both the GSM8K test split and out-of-domain benchmarks. RLSC yields sizable accuracy gains, e.g., +21.2 pts on MATH500.

## Practical Applications

Confidence calibration is positioned as essential for safe LLM deployment in high-stakes applications (science, law, healthcare), with improved self-correction and model cascading enabled by accurately verbalized confidence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eba7e12a-f309-4cf1-a5c6-e3d588466f8a",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "6f6fe9dd-f9ad-452c-93de-239793dd1ad2",
  "sourceToolAssistantUUID": "eba7e12a-f309-4cf1-a5c6-e3d588466f8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-15T14:18:39.488Z_

<details><summary>↩ Tool result · `toolu_01888MZ2LxmtUgcdbNANaQdZ`</summary>

```text
Web search results for query: ""Geometry-Calibrated Conformal Abstention" language models 2026"

Links: [{"title":"[2604.27914] Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/abs/2604.27914"},{"title":"Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/html/2604.27914"},{"title":"LLMs Uncertainty Quantification via Adaptive Conformal Semantic Entropy","url":"https://arxiv.org/html/2605.04295"},{"title":"Conformal Linguistic Calibration: Trading-off between Factuality and Specificity","url":"https://arxiv.org/html/2502.19110"},{"title":"SAFER: Risk-Constrained Sample-then-Filter in Large Language Models","url":"https://arxiv.org/html/2510.10193"},{"title":"STRAPPED CONFORMAL RISK CONTROL FOR LLMS","url":"https://openreview.net/pdf?id=uX7LznCUF5"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models","url":"https://arxiv.org/html/2502.06884v1"},{"title":"Large language model validity via enhanced conformal prediction methods","url":"https://www.researchgate.net/publication/397200904_Large_language_model_validity_via_enhanced_conformal_prediction_methods"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/pdf/2405.01563"},{"title":"[2405.01563] Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/abs/2405.01563"}]

Based on the search results, I found information about the "Geometry-Calibrated Conformal Abstention for Language Models" paper. Here's what the research reveals:

## Overview

The paper proposes a post hoc framework, Conformal Abstention (CA), adapted from conformal prediction (CP) to determine whether to abstain from answering a query.

## Problem Being Addressed

When language models lack relevant knowledge for a given query, they frequently generate plausible responses that can be hallucinations, rather than admitting being agnostic about the answer. Retraining models to reward admitting ignorance can lead to overly conservative behaviors and poor generalization due to scarce evaluation benchmarks.

## Key Technical Contributions

CA provides finite-sample guarantees on both the probability of participation (i.e., not abstaining) and the probability that the generated response is correct. 

Importantly, the abstention decision relies on prediction confidence rather than the non-conformity scores used in CP, which are intractable for open-ended generation. To better align prediction confidence with the model's ignorance, the researchers introduce a calibration strategy using representation geometry within the model to measure knowledge.

## Experimental Performance

The experimental results using LLaMA-3.2-3B-Instruct and LLaMA-3-8B-Instruct show that the proposed method consistently outperforms the baselines across both AUROC and AUPRC metrics, demonstrating stronger discriminative capability in separating correct from incorrect predictions.

The paper was published approximately 2 weeks ago on arXiv (in April 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4931d449-e41a-42fd-9b31-a33f092968bb",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "86ea6701-ff70-4e53-9ad8-080938f779d6",
  "sourceToolAssistantUUID": "4931d449-e41a-42fd-9b31-a33f092968bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-15T14:18:41.425Z_

<details><summary>↩ Tool result · `toolu_014U2Q12PCdXzqjW4f92DQRq`</summary>

```text
Web search results for query: ""HALP" hallucination prediction internal representations single forward pass 2026"

Links: [{"title":"HALP: Detecting Hallucinations in Vision-Language ...","url":"https://aclanthology.org/2026.eacl-long.287.pdf"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"HALP: Catching Hallucinations Before They Happen / HALP:在幻觉发生之前就将其捕获 | Alan Hou","url":"https://alanhou.org/blog/arxiv-halp-detecting-hallucinations-in-vision-language/"},{"title":"[2603.05465] HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/abs/2603.05465"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.287/"},{"title":"Are you hallucinated? Insights into large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405959525002115"},{"title":"Internal Representations as Indicators of Hallucinations in Agent Tool Selection | OpenReview","url":"https://openreview.net/forum?id=QbuBZvwcDZ"},{"title":"When Do Hallucinations Arise? A Graph Perspective on the Evolution of Path Reuse and Path Compression","url":"https://arxiv.org/html/2604.03557v1"},{"title":"GPTZero uncovers 50+ Hallucinations in ICLR 2026","url":"https://gptzero.me/news/iclr-2026/"},{"title":"AI Hallucination Statistics 2026: 50+ Sourced Data Points - Suprmind","url":"https://suprmind.ai/hub/insights/ai-hallucination-statistics-research-report-2026/"}]

Based on my search results, I found comprehensive information about HALP, a recent research paper from 2026:

## HALP: Detecting Hallucinations Before Generation

HALP is a method for detecting hallucinations in vision-language models (VLMs) without generating a single token, recently presented at the EACL 2026 conference.

### Core Innovation

The research investigates whether hallucination risk can be predicted before any token is generated by probing a model's internal representations in a single forward pass. This represents a significant departure from existing approaches, since existing detection methods typically operate after text generation, making intervention both costly and untimely.

### Technical Approach

The method examines three families of internal representations: (i) visual-only features without multimodal fusion, (ii) vision-token representations within the text decoder, and (iii) query-token representations that integrate visual and textual information before generation.

### Results

Probes trained on these representations achieve strong hallucination-detection performance without decoding, reaching up to 0.93 AUROC on Gemma-3-12B, Phi-4-VL 5.6B, and Molmo 7B. However, late query-token states are the most predictive for most models, while visual or mid layer features dominate in a few architectures (e.g., ~0.79 AUROC for Qwen2.5-VL-7B using visual-only features).

### Implications

These results demonstrate that hallucination risk is detectable pre-generation, the most informative layer and modality vary across architectures, and lightweight probes has the potential to enable early abstention, selective routing, and adaptive decoding to improve both safety and efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d9110b5-0242-4264-938c-544184458d09",
  "isSidechain": true,
  "promptId": "d0af2fce-b877-4a83-b1a2-3e65f7ded303",
  "agentId": "aea0f367b90d6b2a7",
  "type": "user",
  "uuid": "e859d137-e208-469b-b79d-9db5e2147d06",
  "sourceToolAssistantUUID": "7d9110b5-0242-4264-938c-544184458d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 103 · 2026-05-15T14:20:31.572Z_

Now I have comprehensive results. Let me compile the final report.

---

Here is a systematic analysis of potentially missing competitors and concurrent work, organized by search query. I focus on papers **not already cited** in the proposal.

---

## QUERY 1: "claim-level calibration long-form generation 2025 2026"

### Papers Found (NOT in cited list):

**1. "Atomic Calibration of LLMs in Long-Form Generations"** -- Zhang et al., Findings of IJCNLP-AACL 2025 ([arXiv:2410.13246](https://arxiv.org/abs/2410.13246))
- Systematically studies atomic (claim-level) calibration by decomposing long responses into atomic claims. Categorizes confidence elicitation methods into discriminative vs. generative types and proposes confidence fusion strategies.
- **Relevance: HIGH.** This is a direct predecessor to the proposal's claim-level approach. It provides the empirical foundation showing LLMs are poorly calibrated at the atomic level in long-form generation.
- **Novelty threat: MEDIUM.** It diagnoses the problem your proposal solves but does not use probes or activation steering as a remedy.

**2. CARE: "Fact-Level Calibration and Correction for Long-Form Generations"** -- Yuan et al., SIGIR 2025 ([ACM](https://dl.acm.org/doi/10.1145/3726302.3730195))
- Proposes a fact-level confidence calibration framework incorporating both relevance and correctness, plus CARE (Confidence-Aware Fact Correction) that uses high-confidence facts to iteratively refine low-confidence ones.
- **Relevance: HIGH.** Operates at the same granularity (fact/claim-level) in long-form generation with calibration + correction.
- **Novelty threat: MEDIUM.** Uses iterative correction rather than activation steering, so the mechanism differs, but the problem formulation overlaps substantially.

**3. "Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality" (CAG)** -- Luo et al., May 2026 ([arXiv:2605.01749](https://arxiv.org/abs/2605.01749))
- Proposes "Exploration-Commitment Decoupling" separating knowledge exploration from final output commitment, with calibrated reliability estimates. Up to 13% factuality improvement.
- **Relevance: HIGH.** Note: The proposal already cites "CAG (2026)" -- verify this is the same paper. If so, no issue.
- **Novelty threat: LOW if already cited.**

**4. "Conformal Linguistic Calibration: Trading-off between Factuality and Specificity"** -- Jiang et al., Feb 2025 ([arXiv:2502.19110](https://arxiv.org/abs/2502.19110))
- Reinterprets linguistic calibration as answer set prediction with conformal guarantees. Enables uncertainty-aware adaptive claim rewriting.
- **Relevance: MEDIUM-HIGH.** Addresses calibration at the claim level via semantic "backoff" rather than abstention.
- **Novelty threat: LOW.** Different mechanism (conformal prediction / linguistic hedging) vs. activation steering.

---

## QUERY 2: "activation steering confidence calibration 2026"

### Papers Found (NOT in cited list):

**5. "Spherical Steering: Geometry-Aware Activation Rotation for Language Models"** -- You et al., Feb 2026 ([arXiv:2602.08169](https://arxiv.org/abs/2602.08169))
- Proposes rotation-based (rather than addition-based) steering using spherical linear interpolation, with adaptive von Mises-Fisher confidence gating. Up to +15% accuracy.
- **Relevance: MEDIUM-HIGH.** Directly relevant as a better steering mechanism that could be applied to confidence calibration. The confidence-gated aspect is particularly relevant.
- **Novelty threat: MEDIUM.** If someone combines Spherical Steering with factuality probes, it subsumes part of the proposal's contribution.

**6. ODESteer: "A Unified ODE-Based Steering Framework for LLM Alignment"** -- Zhao et al., ICLR 2026 ([arXiv:2602.17560](https://arxiv.org/abs/2602.17560))
- Interprets activation addition as first-order approximation of an ODE; uses barrier functions from control theory for multi-step adaptive steering. +5.7% on TruthfulQA.
- **Relevance: MEDIUM.** General steering framework that could be applied to confidence/factuality steering. Provides theoretical grounding.
- **Novelty threat: LOW-MEDIUM.** Different theoretical framework but potentially applicable to the proposal's setting.

**7. AUSteer: "Fine-Grained Activation Steering: Steering Less, Achieving More"** -- ICLR 2026 ([arXiv:2602.04428](https://arxiv.org/abs/2602.04428))
- Decomposes block activations into atomic units, selects discriminative ones via activation momenta, applies adaptive per-input steering strengths.
- **Relevance: MEDIUM.** Fine-grained steering method that could be combined with probe-guided approaches. Relevant as a baseline/alternative steering mechanism.
- **Novelty threat: LOW-MEDIUM.** Different target (general alignment, not confidence calibration specifically).

**8. "Steering Vector Fields for Context-Aware Inference-Time Control in LLMs"** -- Li et al., Feb 2026 ([arXiv:2602.01654](https://arxiv.org/abs/2602.01654))
- Learns a differentiable concept scoring function whose gradient defines context-dependent steering direction (rather than a fixed vector). Supports multi-layer coordinated intervention.
- **Relevance: MEDIUM.** Addresses the limitation that static steering vectors fail in long-form generation -- directly relevant to the proposal's setting.
- **Novelty threat: LOW-MEDIUM.** General steering methodology, not specifically applied to confidence calibration.

**9. FLAS: "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention"** -- Jin et al., May 2026 ([arXiv:2605.05892](https://arxiv.org/abs/2605.05892))
- Learns concept-conditioned velocity field for multi-step, token-varying activation transformations. First learned method to consistently surpass prompting baselines.
- **Relevance: MEDIUM.** Another advanced steering mechanism that supersedes static vector approaches.
- **Novelty threat: LOW.** General framework, not applied to confidence.

---

## QUERY 3: "probe guided decoding hallucination 2026"

### Papers Found (NOT in cited list):

**10. "A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations"** -- O'Neill et al., July 2025 ([arXiv:2507.23221](https://arxiv.org/abs/2507.23221))
- **THIS IS THE MOST IMPORTANT FIND.** Uses a linear probe on an observer model's residual stream to detect hallucinations (>0.95 F1), then uses the probe weight vector as a steering vector injected into a generator to reduce/amplify hallucination prevalence.
- **Relevance: VERY HIGH.** This is extremely close to the proposal's approach -- it combines linear probes with activation steering for hallucination control. The key difference is it uses an external observer model and targets contextual hallucination, while the proposal targets confidence calibration.
- **Novelty threat: HIGH.** The core probe-to-steering pipeline is very similar. The proposal must differentiate clearly (e.g., claim-level granularity, confidence calibration vs. binary hallucination, self-probing vs. observer model).

**11. HaloProbe: "Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models"** -- Zohrabi et al., April 2026 ([arXiv:2604.06165](https://arxiv.org/abs/2604.06165))
- Bayesian framework combining external description statistics with internal decoding signals for token-level hallucination probability estimation, used for guided decoding.
- **Relevance: MEDIUM.** Probe-guided decoding for hallucination mitigation, but in the vision-language setting.
- **Novelty threat: LOW.** Different modality (VLMs) and approach (Bayesian, not linear probe + steering).

**12. "Neural Probe-Based Hallucination Detection for Large Language Models"** -- Liang & Wang, Dec 2025 ([arXiv:2512.20949](https://arxiv.org/abs/2512.20949))
- Uses lightweight MLP probes (not just linear) with Bayesian-optimized layer selection and multi-objective loss for token-level hallucination detection.
- **Relevance: MEDIUM.** Probe-based detection, but detection-only (no steering or calibration component).
- **Novelty threat: LOW.** Detection only, no intervention.

**13. HALP: "Detecting Hallucinations in Vision-Language Models without Generating a Single Token"** -- EACL 2026 ([arXiv:2603.05465](https://arxiv.org/abs/2603.05465))
- Probes internal representations pre-generation to predict hallucination risk (up to 0.93 AUROC), enabling early abstention or adaptive decoding.
- **Relevance: MEDIUM.** Pre-generation probing for hallucination detection, though in VLMs.
- **Novelty threat: LOW.** Different modality and no steering mechanism.

---

## QUERY 4: "verbalized uncertainty long-form 2025 2026"

### Papers Found (NOT in cited list):

**14. "LLMs Should Express Uncertainty Explicitly"** -- Guo et al., April 2026 ([arXiv:2604.05306](https://arxiv.org/abs/2604.05306))
- Compares end-of-reasoning self-assessment (confidence scores) with during-reasoning `&lt;uncertain>` markers. Finds both reduce overconfident errors and improve RAG integration.
- **Relevance: MEDIUM-HIGH.** Directly addresses verbalized uncertainty with mechanistic insights (changes concentrate in later layers, sharpening existing structures).
- **Novelty threat: LOW.** Training-based approach without probes or steering.

**15. CSFT: "Verbalized Confidence Triggers Self-Verification: Emergent Behavior Without Explicit Reasoning Supervision"** -- 2026 ([OpenReview](https://openreview.net/forum?id=P2o8wOzZMX))
- Confidence-supervised fine-tuning triggers emergent self-verification (from <1.5% to ~20% rates) without explicit reasoning supervision.
- **Relevance: MEDIUM.** Shows that confidence training alone can elicit sophisticated calibration behavior.
- **Novelty threat: LOW.** SFT-based, not inference-time intervention.

**16. DINCO: "Calibrating Verbalized Confidence with Self-Generated Distractors"** -- Wang et al., 2025 ([arXiv:2509.25532](https://arxiv.org/abs/2509.25532))
- Normalizes verbalized confidence across self-generated distractors to correct for suggestibility bias. DINCO at 10 runs outperforms self-consistency at 100.
- **Relevance: MEDIUM.** Alternative calibration approach for verbalized confidence.
- **Novelty threat: LOW.** Purely sampling-based, orthogonal to probe+steering approach.

---

## QUERY 5: "inference time intervention hallucination reduction 2026"

### Papers Found (NOT in cited list):

**17. AFTER: "Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing"** -- Wang et al., ICLR 2026 ([arXiv:2601.01957](https://arxiv.org/abs/2601.01957))
- Combines Factual-Augmented Activation Steering (FAS) with Query-Adaptive Offset Optimization (QAO) for input-specific steering from a general factual steering vector. Up to 16.3% hallucination reduction.
- **Relevance: MEDIUM-HIGH.** Adaptive, query-aware steering for factuality -- conceptually related to probe-guided steering for confidence.
- **Novelty threat: MEDIUM.** Different domain (VLMs), but the adaptive factual-guided steering mechanism has significant conceptual overlap.

---

## QUERY 6: "linear probes hallucination detection steering 2026"

**Key finding already covered above (#10, "A Single Direction of Truth").** Also:

**18. "Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation"** -- Han et al., Findings of EMNLP 2025 ([ACL Anthology](https://aclanthology.org/2025.findings-emnlp.880/))
- LLM hidden states are highly predictive of factuality; lightweight probes achieve competitive performance with up to 100x fewer FLOPs.
- **Relevance: HIGH.** Note: The proposal already cites "Han et al. (EMNLP 2025)" -- likely this paper. Confirm.
- **Novelty threat: N/A if cited.**

---

## QUERY 7: "site:arxiv.org claim level uncertainty calibration LLM 2026"

### Papers Found (NOT in cited list):

**19. CoCA: "Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation"** -- Li et al., March 2026 ([arXiv:2603.05881](https://arxiv.org/abs/2603.05881))
- GRPO-based RL that jointly optimizes confidence calibration and answer accuracy via confidence-first generation with segmented credit assignment.
- **Relevance: MEDIUM-HIGH.** Addresses confidence calibration through RL training rather than inference-time intervention.
- **Novelty threat: LOW.** Different mechanism (RL training vs. probe+steering).

**20. DCPO: "Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards"** -- Ma et al., March 2026 ([arXiv:2603.09117](https://arxiv.org/abs/2603.09117))
- Identifies that RLVR training makes models overconfident on incorrect answers; proposes decoupling reasoning and calibration objectives.
- **Relevance: MEDIUM.** Addresses the overconfidence problem through training rather than inference-time.
- **Novelty threat: LOW.** Complementary approach.

**21. "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation"** -- Dec 2025 ([arXiv:2512.22245](https://arxiv.org/abs/2512.22245))
- Uses linear probes on LLM-as-judge hidden states for uncertainty estimation.
- **Relevance: MEDIUM.** Probes for calibration, but in the LLM-as-judge setting.
- **Novelty threat: LOW.** Different application context.

---

## QUERY 8: "faithfulness calibration generation ACL EMNLP 2026"

### Papers Found (NOT in cited list):

**22. CSS: "Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control for Agentic Systems"** -- Huang et al., April 2026 ([arXiv:2604.17487](https://arxiv.org/abs/2604.17487))
- Decomposes answers into claims, uses Clopper-Pearson confidence bounds for calibrated specificity selection (fine-grained, coarse, or omit). Improves utility from 0.846 to 0.913 on LongFact.
- **Relevance: HIGH.** Note: The proposal already cites "CSS (2026)" -- likely this paper. Confirm it is the same.
- **Novelty threat: N/A if cited.**

---

## QUERY 9: "activation engineering confidence LLM 2025 2026"

### Papers Found (NOT in cited list):

**23. CAST: "Programming Refusal with Conditional Activation Steering"** -- IBM, ICLR 2025 (Spotlight) ([arXiv:2409.05907](https://arxiv.org/abs/2409.05907))
- Conditional steering that applies behavior vectors only when activation patterns match a condition vector. Adds controllability without extra compute.
- **Relevance: MEDIUM.** The conditional application mechanism (steer only when condition is met) is relevant -- analogous to "steer only when probe detects low confidence."
- **Novelty threat: LOW-MEDIUM.** General mechanism, but the conditional steering paradigm is conceptually close.

---

## QUERY 10: "Rewarding Doubt hallucination 2026" / "self-aware generation LLM 2026"

### Papers Found (NOT in cited list):

**24. "Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning"** -- Wu et al., Dec 2025/Jan 2026 ([arXiv:2512.19920](https://arxiv.org/abs/2512.19920))
- Uses behavioral calibration in RL with strictly proper scoring rules so models learn to abstain when not confident. A 4B model matches frontier models in calibration error.
- **Relevance: MEDIUM.** RL-based approach to calibrated uncertainty expression.
- **Novelty threat: LOW.** Training-based, not inference-time.

---

## SUMMARY OF MOST CRITICAL MISSING CITATIONS

Ranked by urgency:

| Priority | Paper | Why It Matters |
|----------|-------|---------------|
| **CRITICAL** | "A Single Direction of Truth" (O'Neill et al., 2025) | **Combines linear probes with activation steering for hallucination control** -- the closest existing work to the proposal's core mechanism |
| **HIGH** | "Atomic Calibration of LLMs in Long-Form Generations" (Zhang et al., IJCNLP 2025) | Foundational work on claim-level calibration in long-form generation |
| **HIGH** | CARE / "Fact-Level Calibration and Correction" (Yuan et al., SIGIR 2025) | Fact-level calibration + correction for long-form, same problem formulation |
| **HIGH** | Spherical Steering (You et al., Feb 2026) | Better steering mechanism with confidence-gated application |
| **HIGH** | AFTER (Wang et al., ICLR 2026) | Adaptive factual-guided activation steering with query-aware offsets |
| **MEDIUM-HIGH** | "LLMs Should Express Uncertainty Explicitly" (Guo et al., Apr 2026) | Explicit uncertainty expression with mechanistic insights |
| **MEDIUM-HIGH** | CoCA (Li et al., Mar 2026) | Confidence-first RL framework for calibration |
| **MEDIUM-HIGH** | Conformal Linguistic Calibration (Jiang et al., 2025) | Claim-level rewriting with conformal guarantees |
| **MEDIUM** | ODESteer (ICLR 2026), AUSteer (ICLR 2026), SVF (Feb 2026), FLAS (May 2026) | Advanced steering methods that could serve as baselines |
| **MEDIUM** | CAST (IBM, ICLR 2025) | Conditional steering paradigm |
| **MEDIUM** | DCPO (Ma et al., Mar 2026) | Decoupled calibration in RL training |

## KEY NOVELTY ASSESSMENT

The **most threatening** paper to novelty is **"A Single Direction of Truth"** (O'Neill et al., 2025). It already demonstrates the probe-to-steering pipeline for hallucination control. The proposal must clearly differentiate on:
1. **Claim-level granularity** (vs. span-level binary hallucination detection)
2. **Confidence calibration** (continuous scores, not binary factual/hallucinated)
3. **Self-probing** within the generating model (vs. external observer model)
4. **Verbalized confidence alignment** (steering to calibrate expressed confidence, not just reduce hallucinations)

The other critical gap is the **"Atomic Calibration"** and **CARE** papers which establish the problem space the proposal operates in and should be cited as motivating work.

Sources:
- [Atomic Calibration of LLMs in Long-Form Generations](https://arxiv.org/abs/2410.13246)
- [Fact-Level Calibration and Correction for Long-Form Generations (CARE)](https://dl.acm.org/doi/10.1145/3726302.3730195)
- [Only Say What You Know: Calibration-Aware Generation](https://arxiv.org/abs/2605.01749)
- [Conformal Linguistic Calibration](https://arxiv.org/abs/2502.19110)
- [Spherical Steering](https://arxiv.org/abs/2602.08169)
- [ODESteer](https://arxiv.org/abs/2602.17560)
- [AUSteer](https://arxiv.org/abs/2602.04428)
- [Steering Vector Fields](https://arxiv.org/abs/2602.01654)
- [FLAS: Flow-based Activation Steering](https://arxiv.org/abs/2605.05892)
- [A Single Direction of Truth](https://arxiv.org/abs/2507.23221)
- [HaloProbe](https://arxiv.org/abs/2604.06165)
- [Neural Probe-Based Hallucination Detection](https://arxiv.org/abs/2512.20949)
- [HALP](https://arxiv.org/abs/2603.05465)
- [LLMs Should Express Uncertainty Explicitly](https://arxiv.org/abs/2604.05306)
- [CSFT: Verbalized Confidence Triggers Self-Verification](https://openreview.net/forum?id=P2o8wOzZMX)
- [DINCO](https://arxiv.org/abs/2509.25532)
- [AFTER](https://arxiv.org/abs/2601.01957)
- [Simple Factuality Probes](https://aclanthology.org/2025.findings-emnlp.880/)
- [CoCA: Confidence Before Answering](https://arxiv.org/abs/2603.05881)
- [DCPO: Decoupling Reasoning and Confidence](https://arxiv.org/abs/2603.09117)
- [CSS: Calibrated Claim-Level Specificity Control](https://arxiv.org/abs/2604.17487)
- [CAST: Conditional Activation Steering](https://arxiv.org/abs/2409.05907)
- [Behaviorally Calibrated RL](https://arxiv.org/abs/2512.19920)
- [Calibrating LLM Judges with Linear Probes](https://arxiv.org/abs/2512.22245)
- [Geometry-Calibrated Conformal Abstention](https://arxiv.org/abs/2604.27914)
- [Activation Steering Field Guide (blog)](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e859d137-e208-469b-b79d-9db5e2147d06",
  "isSidechain": true,
  "agentId": "aea0f367b90d6b2a7",
  "requestId": "req_011Cb4VvimCyxxqNoRtW9FL3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4b577e3-7472-4768-ba5f-381c5fe0e00d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e709fca-c93a-4e70-85b1-fd9313a35a19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsNNcyCLeeBBam9tAh77G6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3895,
      "cache_read_input_tokens": 42842,
      "output_tokens": 5810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3895
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5810,
          "cache_read_input_tokens": 42842,
          "cache_creation_input_tokens": 3895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3895,
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
