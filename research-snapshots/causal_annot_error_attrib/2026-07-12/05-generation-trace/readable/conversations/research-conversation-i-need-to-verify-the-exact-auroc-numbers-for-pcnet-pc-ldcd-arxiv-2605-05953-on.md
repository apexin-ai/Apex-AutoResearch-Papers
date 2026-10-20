# Research conversation: I need to verify the exact AUROC numbers for PCNet/PC-LDCD (arXiv 2605.05953) on TruthfulQA specifically. The paper is "

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a31d343b46aae0e38.jsonl`
- **Structured JSON:** [`e7dca958f9428d7547f4.json`](../../sessions/e7/e7dca958f9428d7547f4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-15T15:06:14.090Z_

I need to verify the exact AUROC numbers for PCNet/PC-LDCD (arXiv 2605.05953) on TruthfulQA specifically. The paper is "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits".

Please:
1. Use WebSearch to find the paper: "PCNet PC-LDCD arXiv 2605.05953 hallucination probabilistic circuits"
2. Use WebFetch to read the paper from arXiv, focusing on the results/experiments section
3. Find the exact AUROC numbers broken down by dataset — I specifically need:
   - TruthfulQA AUROC for each model tested (especially Llama-3.1-8B)
   - CoQA AUROC
   - SQuAD AUROC
   - Any other datasets
4. Also look for: what models were tested, what the method actually does (hidden-state residual stream probes?)

Report exact numbers with table format if possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e5efa5fe-2ea6-41a6-857c-3bacff06c097",
  "agentId": "a31d343b46aae0e38",
  "type": "user",
  "uuid": "876a07ca-a376-4ce0-b259-61c878c944f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T15:06:14.092Z_

```json
{
  "parentUuid": "876a07ca-a376-4ce0-b259-61c878c944f8",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
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
  "uuid": "9092d441-8c4d-4582-ae9e-f8884e6814ba",
  "timestamp": "2026-05-15T15:06:14.092Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T15:06:17.233Z_



I'll help you find the specific AUROC numbers from that paper. Let me start by loading the necessary tools and searching for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9092d441-8c4d-4582-ae9e-f8884e6814ba",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4ZZ17ZpzT9fSS6Nnksh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "387271f8-4d3e-4b86-b775-d658603149d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JisXwqk8ENbZfJDHBsxSjJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 781,
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

_source line 4 · 2026-05-15T15:06:17.410Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GSw9hfnyQkjzH9JRDsiPyn`</summary>

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
  "parentUuid": "387271f8-4d3e-4b86-b775-d658603149d1",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4ZZ17ZpzT9fSS6Nnksh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e27db747-cfaf-4437-986d-e0e708a0a4c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JisXwqk8ENbZfJDHBsxSjJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 8223,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 781
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 781,
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

_source line 5 · 2026-05-15T15:06:17.413Z_

<details><summary>↩ Tool result · `toolu_01GSw9hfnyQkjzH9JRDsiPyn`</summary>

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
  "parentUuid": "e27db747-cfaf-4437-986d-e0e708a0a4c8",
  "isSidechain": true,
  "promptId": "e5efa5fe-2ea6-41a6-857c-3bacff06c097",
  "agentId": "a31d343b46aae0e38",
  "type": "user",
  "uuid": "071b6d5c-c6fe-466b-812a-3e9363eac7c7",
  "sourceToolAssistantUUID": "e27db747-cfaf-4437-986d-e0e708a0a4c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T15:06:20.135Z_



Now let me search for the paper and fetch it from arXiv.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "071b6d5c-c6fe-466b-812a-3e9363eac7c7",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4ZZFWVzCxssjpYkuqkR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "619f0102-0dde-46a0-91cc-2a855f5c4a21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETghtz5CATjVFD7tPWrV7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 7 · 2026-05-15T15:06:20.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SYDq7cKepWAfydhG5gYWkS`</summary>

```json
{
  "query": "PCNet PC-LDCD arXiv 2605.05953 hallucination probabilistic circuits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "619f0102-0dde-46a0-91cc-2a855f5c4a21",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4ZZFWVzCxssjpYkuqkR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb72331c-ce45-4169-b6e9-73c5bc490368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETghtz5CATjVFD7tPWrV7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 8 · 2026-05-15T15:06:21.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014FqbymkqWotk8TCxuTJ1nc`</summary>

```json
{
  "query": "arXiv 2605.05953 \"Hallucination as an Anomaly\" \"Dynamic Intervention via Probabilistic Circuits\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb72331c-ce45-4169-b6e9-73c5bc490368",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4ZZFWVzCxssjpYkuqkR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "359a99ca-9937-4ae8-9fce-287f0af414fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETghtz5CATjVFD7tPWrV7K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9004,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 157,
          "cache_read_input_tokens": 9004,
          "cache_creation_input_tokens": 1919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1919,
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

_source line 9 · 2026-05-15T15:06:26.907Z_

<details><summary>↩ Tool result · `toolu_01SYDq7cKepWAfydhG5gYWkS`</summary>

```text
Web search results for query: "PCNet PC-LDCD arXiv 2605.05953 hallucination probabilistic circuits"

Links: [{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis","url":"https://arxiv.org/html/2502.08663v1"},{"title":"A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation","url":"https://arxiv.org/html/2406.06950v1"},{"title":"[2502.08663] Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis","url":"https://arxiv.org/abs/2502.08663"},{"title":"Probabilistic Guarantees for Reducing Contextual Hallucinations in LLMs","url":"https://arxiv.org/pdf/2601.00641"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=5650&show=25"},{"title":"Computer Science Feb 2023","url":"http://arxiv.org/list/cs/2023-02?skip=2625&show=25"},{"title":"[2406.06950] A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation","url":"https://arxiv.org/abs/2406.06950"},{"title":"[2511.15005] Mathematical Analysis of Hallucination Dynamics in Large Language Models: Uncertainty Quantification, Advanced Decoding, and Principled Mitigation","url":"https://arxiv.org/abs/2511.15005"}]

Great! I found detailed information about the paper. Here's what I found:

## Paper Summary

The paper is titled "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (arXiv 2605.05953).

### Key Contributions

The paper proposes PCNet, a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream that detects hallucinations as geometric anomalies on the factual manifold via exact Negative Log-Likelihood computation, without requiring sampling, external verifiers, or weight modifications.

The second main contribution is PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding), which intervenes only when the latent geometry deviates from factual regions, while leaving correct generations untouched.

### Performance Results

Across four LLMs ranging from 1B to 8B models and four benchmarks, PCNet achieves near-perfect hallucination detection with AUROC reaching up to 99%. PC-LDCD obtains the highest scores on TruthfulQA in three out of four models while reducing the mean corruption rate to 53.7% and achieving a preservation rate of 79.3%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb72331c-ce45-4169-b6e9-73c5bc490368",
  "isSidechain": true,
  "promptId": "e5efa5fe-2ea6-41a6-857c-3bacff06c097",
  "agentId": "a31d343b46aae0e38",
  "type": "user",
  "uuid": "df7258b4-afd6-4607-b43b-d50d7c05f7bf",
  "sourceToolAssistantUUID": "cb72331c-ce45-4169-b6e9-73c5bc490368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T15:06:28.580Z_

<details><summary>↩ Tool result · `toolu_014FqbymkqWotk8TCxuTJ1nc`</summary>

```text
Web search results for query: "arXiv 2605.05953 "Hallucination as an Anomaly" "Dynamic Intervention via Probabilistic Circuits""

Links: [{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation","url":"https://arxiv.org/html/2406.06950"},{"title":"Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis","url":"https://arxiv.org/html/2502.08663"},{"title":"Computer Science Apr 2025","url":"https://arxiv.org/list/cs/2025-04?skip=9925&show=2000"},{"title":"[2601.00641] Probabilistic Guarantees for Reducing Contextual Hallucinations in LLMs","url":"https://arxiv.org/abs/2601.00641"},{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"},{"title":"[2406.06950v1] A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation","url":"https://arxiv.org/abs/2406.06950v1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=202&show=2000"}]

I found the paper you're looking for. Here's the information about arXiv:2605.05953:

**Title:** Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits

**Authors:** Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, Giovanni Iacca

**Submission Date:** 7 May 2026

**Main Contribution:** The paper proposes PCNET, a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream. The method detects hallucinations as geometric anomalies on the factual manifold via exact Negative Log-Likelihood computation, without needing sampling, external verifiers, or weight modifications.

**Key Innovation:** Unlike existing approaches that apply corrections indiscriminately to every token, PCNET is used as a dynamic gate that distinguishes hallucinated from factual hidden states at each decoding step.

**Performance:** Across four LLMs ranging from 1B to 8B models and four benchmarks, PCNET achieves near-perfect hallucination detection with AUROC reaching up to 99%, and obtains the highest scores on TruthfulQA while reducing corruption rate to 53.7% and achieving a preservation rate of 79.3%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "359a99ca-9937-4ae8-9fce-287f0af414fa",
  "isSidechain": true,
  "promptId": "e5efa5fe-2ea6-41a6-857c-3bacff06c097",
  "agentId": "a31d343b46aae0e38",
  "type": "user",
  "uuid": "809b7b75-b366-488c-8443-20a62186743e",
  "sourceToolAssistantUUID": "359a99ca-9937-4ae8-9fce-287f0af414fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T15:06:36.492Z_

I found the paper. Now let me fetch the full HTML version to extract the exact AUROC numbers from the results tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "809b7b75-b366-488c-8443-20a62186743e",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4Za5EeNFfa9UREFsEyq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffd9c061-a7bf-4c69-8410-3cfba0b1529a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkX2xMedBurMy295aCiWf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1797,
      "cache_read_input_tokens": 10923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1797,
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

_source line 12 · 2026-05-15T15:06:40.529Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017VQzoUL5DocRgWRWj2uSNc`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05953",
  "prompt": "Extract ALL AUROC numbers from the results/experiments section. I need: 1) The exact AUROC values for PCNet on EVERY dataset (TruthfulQA, CoQA, SQuAD, and any others) broken down by EVERY model tested (especially Llama-3.1-8B). 2) Present the full detection results table with all rows and columns. 3) Also extract comparison baselines and their AUROC numbers. 4) What models were tested (list all). 5) What layers were probed. 6) The method description - what exactly does PCNet do with the residual stream? Report every single number you can find in any table related to AUROC."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffd9c061-a7bf-4c69-8410-3cfba0b1529a",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4Za5EeNFfa9UREFsEyq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "770d9b86-5f6c-4318-8b44-3118fef5bd6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkX2xMedBurMy295aCiWf8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1797,
      "cache_read_input_tokens": 10923,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1797
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 10923,
          "cache_creation_input_tokens": 1797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1797,
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

_source line 13 · 2026-05-15T15:06:47.664Z_

<details><summary>↩ Tool result · `toolu_017VQzoUL5DocRgWRWj2uSNc`</summary>

```text
# PCNet AUROC Results Extraction

## All Models Tested
Four LLMs were evaluated: Llama-3.2-1B, Qwen3-4B, Mistral-7B-v0.3, and Llama-3.1-8B.

## Complete AUROC Table (Table 1)

| Model | Method | CoQA | SQuAD v2.0 | TriviaQA | TruthfulQA | Average |
|-------|--------|------|-----------|----------|-----------|---------|
| Llama-3.2-1B | PCNet | 0.95±.05 | 0.98±.01 | 0.91±.04 | 0.66±.10 | 0.88±.14 |
| Mistral-7B | PCNet | 0.97±.02 | 0.98±.00 | 0.98±.01 | 0.79±.06 | 0.92±.09 |
| Qwen3-4B | PCNet | 0.96±.06 | 0.97±.01 | 0.95±.04 | 0.81±.02 | 0.92±.07 |
| Llama-3.1-8B | PCNet | 0.98±.02 | 0.98±.02 | 0.97±.02 | 0.75±.06 | 0.92±.11 |

## Baseline Comparisons (AUROC only)

**Token NLL**: Range 0.47–0.82 across datasets/models
**SEP (Semantic Entropy Probes)**: Range 0.33–0.77
**HaloScope**: Range 0.55–0.97
**AutoFact**: Range 0.34–0.80

## Method Description

PCNet is a "tractable density estimator based on Probabilistic Circuits" that operates on "a low-dimensional projection of the LLM's final hidden state." The framework computes exact "Negative Log-Likelihood (NLL) of any latent state in a single forward pass" without sampling or external verifiers. It detects "hallucinations as geometric anomalies on the factual manifold."

## Layers Probed

The final-layer hidden state preceding the embedding layer (h ∈ ℝ^D_LLM), projected through a 2-layer MLP bottleneck to d=128 dimensions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "770d9b86-5f6c-4318-8b44-3118fef5bd6d",
  "isSidechain": true,
  "promptId": "e5efa5fe-2ea6-41a6-857c-3bacff06c097",
  "agentId": "a31d343b46aae0e38",
  "type": "user",
  "uuid": "1fb15303-f02f-4c9f-9801-2c976d739f49",
  "sourceToolAssistantUUID": "770d9b86-5f6c-4318-8b44-3118fef5bd6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-15T15:06:51.089Z_

Good, I have the main detection table. Let me now fetch more details, particularly the full baseline comparison numbers and any additional tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fb15303-f02f-4c9f-9801-2c976d739f49",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4ZbUfpemJ4SUX4aJeAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c87e5379-a409-4a03-a5a7-7f96aefccb96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NC4juGHWuBTCrTiYrLViDQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 12720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 877,
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

_source line 15 · 2026-05-15T15:06:53.778Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BcC46R9k8J9x1qTnsAmSc4`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05953",
  "prompt": "I need the COMPLETE Table 1 with ALL baseline methods and their exact AUROC numbers for every model and dataset. List every single row in the table including: Token NLL, SEP, HaloScope, AutoFact, PCNet, and any other methods. Give me the exact numbers with standard deviations for EVERY cell. Also extract Table 2 if it exists (the generation/intervention results for PC-LDCD). Also find the 'up to 99%' AUROC claim - which specific model/dataset combination achieves 99%?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c87e5379-a409-4a03-a5a7-7f96aefccb96",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4ZbUfpemJ4SUX4aJeAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d28344e0-be49-4cc9-8967-a50fd34d6ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NC4juGHWuBTCrTiYrLViDQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 12720,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 12720,
          "cache_creation_input_tokens": 877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 877,
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

_source line 16 · 2026-05-15T15:07:01.341Z_

<details><summary>↩ Tool result · `toolu_01BcC46R9k8J9x1qTnsAmSc4`</summary>

```text
# Complete Table 1: Hallucination Detection Performance

Based on the document, Table 1 presents detection results across four LLMs and four benchmarks. Here are all the detection methods and their complete results:

## Detection Methods Evaluated:
1. Token NLL
2. SEP (Semantic Entropy Probes)
3. HaloScope
4. AutoFact
5. PCNet (Ours)

## Key Results by Model:

**Llama-3.2-1B** - PCNet achieves best AUROC across all datasets (0.95±.05 CoQA, 0.98±.01 SQuAD, 0.91±.04 TriviaQA, 0.66±.10 TruthfulQA)

**Mistral-7B-v0.3** - PCNet reaches near-perfect separation: 0.97±.02 CoQA, 0.98±.00 SQuAD, 0.98±.01 TriviaQA, 0.79±.06 TruthfulQA

**Qwen3-4B** - PCNet demonstrates strong performance: 0.96±.06 CoQA, 0.97±.01 SQuAD, 0.95±.04 TriviaQA, 0.81±.02 TruthfulQA

**Llama-3.1-8B** - Highest reported AUROC: 0.98±.02 CoQA, 0.98±.02 SQuAD, 0.97±.02 TriviaQA, 0.75±.06 TruthfulQA

## The "99% AUROC" Claim:

The paper states PCNet achieves "AUROC reaching up to 99%" but Table 1 shows the maximum is **0.98 (98%)**, not 99%. This appears to be a rounding or promotional statement in the abstract rather than literal tabular data.

## Table 2: Gating Advantage Results

Table 2 demonstrates the Detection-Correction Asymmetry concept, showing corruption rates (fraction of correct responses degraded) and preservation rates across correction methods. PC-LDCD achieves the lowest mean corruption (53.7%) and highest preservation (79.3%).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d28344e0-be49-4cc9-8967-a50fd34d6ffc",
  "isSidechain": true,
  "promptId": "e5efa5fe-2ea6-41a6-857c-3bacff06c097",
  "agentId": "a31d343b46aae0e38",
  "type": "user",
  "uuid": "f167065a-4e0f-41cb-8733-fd27555a5894",
  "sourceToolAssistantUUID": "d28344e0-be49-4cc9-8967-a50fd34d6ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T15:07:06.868Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Qosf7AExyv3oA5G1kWRzRC`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05953",
  "prompt": "Extract the FULL baseline numbers for ALL methods in Table 1. I need the exact AUROC for Token NLL, SEP, HaloScope, and AutoFact for EVERY model (Llama-3.2-1B, Qwen3-4B, Mistral-7B, Llama-3.1-8B) and EVERY dataset (CoQA, SQuAD, TriviaQA, TruthfulQA). Give me every single number with standard deviations. Also extract Table 3 (TruthfulQA generation scores for PC-LDCD) if it exists - the MC1, MC2, or truthful scores. Also what is the PC-LDCD intervention method exactly?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f167065a-4e0f-41cb-8733-fd27555a5894",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4ZcV8dS1j6CeJJ6kGEv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efb5e038-889c-4849-99a8-e8a82d9aae1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zgUvR4Qe3u8bTwDnYvKwm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 13597,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 789
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 13597,
          "cache_creation_input_tokens": 789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 789,
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

_source line 18 · 2026-05-15T15:07:14.315Z_

<details><summary>↩ Tool result · `toolu_01Qosf7AExyv3oA5G1kWRzRC`</summary>

```text
# Baseline AUROC Numbers from Table 1

## Llama-3.2-1B
- **Token NLL**: CoQA 0.55±.00 | SQuAD 0.61±.01 | TriviaQA 0.76±.06 | TruthfulQA 0.47±.01
- **SEP**: CoQA 0.77±.07 | SQuAD 0.62±.09 | TriviaQA 0.56±.03 | TruthfulQA 0.53±.03
- **HaloScope**: CoQA 0.85±.02 | SQuAD 0.95±.05 | TriviaQA 0.86±.11 | TruthfulQA 0.61±.02
- **AutoFact**: CoQA 0.56±.02 | SQuAD 0.58±.01 | TriviaQA 0.80±.02 | TruthfulQA 0.34±.01

## Mistral-7B-v0.3
- **Token NLL**: CoQA 0.56±.00 | SQuAD 0.62±.00 | TriviaQA 0.82±.01 | TruthfulQA 0.52±.01
- **SEP**: CoQA 0.69±.12 | SQuAD 0.64±.07 | TriviaQA 0.63±.06 | TruthfulQA 0.54±.04
- **HaloScope**: CoQA 0.88±.03 | SQuAD 0.90±.05 | TriviaQA 0.88±.06 | TruthfulQA 0.55±.05
- **AutoFact**: CoQA 0.56±.02 | SQuAD 0.58±.01 | TriviaQA 0.80±.02 | TruthfulQA 0.34±.01

## Qwen3-4B
- **Token NLL**: CoQA 0.55±.00 | SQuAD 0.61±.01 | TriviaQA 0.76±.01 | TruthfulQA 0.53±.01
- **SEP**: CoQA 0.65±.24 | SQuAD 0.42±.09 | TriviaQA 0.69±.02 | TruthfulQA 0.54±.08
- **HaloScope**: CoQA 0.63±.09 | SQuAD 0.82±.09 | TriviaQA 0.72±.08 | TruthfulQA 0.53±.02
- **AutoFact**: CoQA 0.56±.02 | SQuAD 0.58±.01 | TriviaQA 0.80±.02 | TruthfulQA 0.34±.01

## Llama-3.1-8B
- **Token NLL**: CoQA 0.55±.00 | SQuAD 0.61±.01 | TriviaQA 0.82±.01 | TruthfulQA 0.49±.00
- **SEP**: CoQA 0.33±.20 | SQuAD 0.57±.09 | TriviaQA 0.52±.09 | TruthfulQA 0.43±.01
- **HaloScope**: CoQA 0.97±.02 | SQuAD 0.97±.02 | TriviaQA 0.95±.06 | TruthfulQA 0.59±.03
- **AutoFact**: CoQA 0.56±.01 | SQuAD 0.58±.01 | TriviaQA 0.80±.01 | TruthfulQA 0.35±.00

---

# PC-LDCD Intervention Method

The system performs "density-penalized lookahead search in the discrete token space" when geometric anomalies arise. Specifically: "the optimal token is selected by maximizing a penalized log-probability" combining the model's native token likelihood minus a density penalty weighted by intervention strength. This operates entirely in token space rather than modifying hidden states directly, preserving generation fluency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efb5e038-889c-4849-99a8-e8a82d9aae1e",
  "isSidechain": true,
  "promptId": "e5efa5fe-2ea6-41a6-857c-3bacff06c097",
  "agentId": "a31d343b46aae0e38",
  "type": "user",
  "uuid": "a80d7471-3259-44bd-a68d-69fd5942f2fe",
  "sourceToolAssistantUUID": "efb5e038-889c-4849-99a8-e8a82d9aae1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T15:07:19.489Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DfQsLDwgRf8yJ5WoMR7oZK`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05953",
  "prompt": "Extract Table 3 or any table showing TruthfulQA generation scores (MC1, MC2, or truthfulness percentages) for PC-LDCD compared to baselines like DoLa, ITI, Activation Addition, STEER, InferAligner, contrastive decoding, etc. Also extract: What is the corruption rate table (Table 2)? Give me exact numbers. What layer is probed? What is the MLP bottleneck architecture? What is the threshold mechanism for gating?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a80d7471-3259-44bd-a68d-69fd5942f2fe",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4ZdSasAgZ8NzJLg9eQq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71f56b7a-fb88-43b0-ad3a-ec2a05009bdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EdHojg934NBBfcvu6VfEq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1350,
      "cache_read_input_tokens": 14386,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1350
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 14386,
          "cache_creation_input_tokens": 1350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1350,
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

_source line 20 · 2026-05-15T15:07:25.030Z_

<details><summary>↩ Tool result · `toolu_01DfQsLDwgRf8yJ5WoMR7oZK`</summary>

```text
# Key Findings from PC-LDCD Paper

## TruthfulQA Performance (Table 3)

**PC-LDCD scores on TruthfulQA:**
- **Llama-3.2-1B**: T+I 0.50 (no change), MC2 0.51 (+0.10)
- **Qwen3-4B**: T+I 0.78 (+0.28), MC2 0.68 (+0.19)
- **Mistral-7B**: T+I 0.72 (+0.22), MC2 0.72 (+0.22)
- **Llama-3.1-8B**: T+I 0.69 (+0.19), MC2 0.65 (+0.21)

PC-LDCD achieved "highest True+Info, MC2, and MC3 scores on TruthfulQA in three out of four models" compared to baselines including DoLa, ITI, AdaSteer, and SADI.

## Corruption & Preservation Rates (Table 2)

**Mean across all methods:**
- Ungated corruption: 56.5%
- Gated preservation: 78.0%

**PC-LDCD specifically:**
- Corruption rate: 53.7%
- Preservation rate: 79.3%

## Architecture Details

**Probed layer:** "final-layer hidden state corresponding strictly to the last valid token"

**MLP bottleneck:** "2-layer MLP with ReLU activations" projecting from 4096 dimensions to 128 dimensions

**Gating threshold:** Dynamic sigmoid mechanism: β_t = σ(NLL(z_t) − τ), where τ is "calibrated on validation set...selecting the threshold that yields the maximum F1 score"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71f56b7a-fb88-43b0-ad3a-ec2a05009bdc",
  "isSidechain": true,
  "promptId": "e5efa5fe-2ea6-41a6-857c-3bacff06c097",
  "agentId": "a31d343b46aae0e38",
  "type": "user",
  "uuid": "8190b0e1-5d0a-40ed-871b-7e18cf137501",
  "sourceToolAssistantUUID": "71f56b7a-fb88-43b0-ad3a-ec2a05009bdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T15:07:30.057Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QWgrK37GzfuBKvc1iWcaNU`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05953",
  "prompt": "Extract the FULL Table 3 with ALL baseline methods and their TruthfulQA scores. I need every row: DoLa, ITI, AdaSteer, SADI, InferAligner, contrastive decoding, and PC-LDCD for each model. Give me all columns: T+I (True+Informative), MC1, MC2, MC3 if available. Also, what are the absolute base model scores before any intervention? And extract the PCNet AUROC numbers one more time - specifically the average column values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8190b0e1-5d0a-40ed-871b-7e18cf137501",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4ZeEQuhjEHroSdhH5hp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12be3640-ac20-4c32-a0d0-ed18fb511af5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MtvwW1muztdMpAT8Ae8tR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 15736,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 15736,
          "cache_creation_input_tokens": 640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 640,
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

_source line 22 · 2026-05-15T15:07:34.464Z_

<details><summary>↩ Tool result · `toolu_01QWgrK37GzfuBKvc1iWcaNU`</summary>

```text
# Analysis of Table 3 and PCNet Results

## Full Table 3 Extract

Based on the document, Table 3 presents TruthfulQA results in **gated mode only**. The complete table includes:

**Methods evaluated:** Vanilla, DoLa, ITI, AdaSteer, SADI, ICD, and PC-LDCD (Ours)

**Metrics per model:** T+I, MC1, MC2, MC3 with standard deviations and delta values

**Baseline scores (Vanilla - no intervention):**
- Llama-3.2-1B: T+I=0.50, MC1=0.23, MC2=0.41, MC3=0.06
- Qwen3-4B: T+I=0.50, MC1=0.33, MC2=0.50, MC3=0.11
- Mistral-7B: T+I=0.50, MC1=0.34, MC2=0.50, MC3=0.13
- Llama-3.1-8B: T+I=0.50, MC1=0.29, MC2=0.44, MC3=0.08

The document does **not include** InferAligner or standard contrastive decoding as separate baselines in Table 3.

## PCNet AUROC Average Column Values

From Table 1 (hallucination detection performance):

- **Llama-3.2-1B:** 0.88±0.14 AUROC average
- **Mistral-7B-v0.3:** 0.92±0.09 AUROC average
- **Qwen3-4B:** 0.92±0.07 AUROC average
- **Llama-3.1-8B:** 0.92±0.11 AUROC average
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12be3640-ac20-4c32-a0d0-ed18fb511af5",
  "isSidechain": true,
  "promptId": "e5efa5fe-2ea6-41a6-857c-3bacff06c097",
  "agentId": "a31d343b46aae0e38",
  "type": "user",
  "uuid": "94a64be6-e653-4f35-ad4e-4a19c392d50b",
  "sourceToolAssistantUUID": "12be3640-ac20-4c32-a0d0-ed18fb511af5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T15:08:08.570Z_

Now I have all the key data. Here is a comprehensive report.

---

## Paper: "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (arXiv 2605.05953)

**Authors:** Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, Giovanni Iacca (submitted 7 May 2026)

---

### What the Method Does

**PCNet** is a Probabilistic Circuit trained as a tractable density estimator over the LLM's residual stream. It takes the **final-layer hidden state** (corresponding to the last valid token), projects it through a **2-layer MLP bottleneck with ReLU activations** (from D_LLM, e.g. 4096, down to d=128), and then computes exact Negative Log-Likelihood (NLL) in a single forward pass. Hallucinations are detected as **geometric anomalies on the factual manifold** -- high-NLL states are off-manifold.

**PC-LDCD** (Probabilistic Circuit Latent Density Contrastive Decoding) uses PCNet as a dynamic gate. A sigmoid threshold mechanism `beta_t = sigma(NLL(z_t) - tau)` (where tau is calibrated to max F1 on a validation set) decides whether to intervene. When the gate fires, it performs **density-penalized lookahead search in discrete token space** -- maximizing penalized log-probability that combines the model's native token likelihood minus a density penalty. Crucially, it only intervenes on anomalous states, leaving correct generations untouched.

---

### Models Tested

1. Llama-3.2-1B
2. Qwen3-4B
3. Mistral-7B-v0.3
4. Llama-3.1-8B

### Datasets

CoQA, SQuAD v2.0, TriviaQA, TruthfulQA

---

### Table 1: Hallucination Detection AUROC (PCNet vs. Baselines)

#### Llama-3.2-1B

| Method     | CoQA       | SQuAD v2.0 | TriviaQA   | TruthfulQA | Average    |
|------------|------------|------------|------------|------------|------------|
| Token NLL  | 0.55+-.00 | 0.61+-.01 | 0.76+-.06 | 0.47+-.01 | --         |
| SEP        | 0.77+-.07 | 0.62+-.09 | 0.56+-.03 | 0.53+-.03 | --         |
| HaloScope  | 0.85+-.02 | 0.95+-.05 | 0.86+-.11 | 0.61+-.02 | --         |
| AutoFact   | 0.56+-.02 | 0.58+-.01 | 0.80+-.02 | 0.34+-.01 | --         |
| **PCNet**  | **0.95+-.05** | **0.98+-.01** | **0.91+-.04** | **0.66+-.10** | **0.88+-.14** |

#### Qwen3-4B

| Method     | CoQA       | SQuAD v2.0 | TriviaQA   | TruthfulQA | Average    |
|------------|------------|------------|------------|------------|------------|
| Token NLL  | 0.55+-.00 | 0.61+-.01 | 0.76+-.01 | 0.53+-.01 | --         |
| SEP        | 0.65+-.24 | 0.42+-.09 | 0.69+-.02 | 0.54+-.08 | --         |
| HaloScope  | 0.63+-.09 | 0.82+-.09 | 0.72+-.08 | 0.53+-.02 | --         |
| AutoFact   | 0.56+-.02 | 0.58+-.01 | 0.80+-.02 | 0.34+-.01 | --         |
| **PCNet**  | **0.96+-.06** | **0.97+-.01** | **0.95+-.04** | **0.81+-.02** | **0.92+-.07** |

#### Mistral-7B-v0.3

| Method     | CoQA       | SQuAD v2.0 | TriviaQA   | TruthfulQA | Average    |
|------------|------------|------------|------------|------------|------------|
| Token NLL  | 0.56+-.00 | 0.62+-.00 | 0.82+-.01 | 0.52+-.01 | --         |
| SEP        | 0.69+-.12 | 0.64+-.07 | 0.63+-.06 | 0.54+-.04 | --         |
| HaloScope  | 0.88+-.03 | 0.90+-.05 | 0.88+-.06 | 0.55+-.05 | --         |
| AutoFact   | 0.56+-.02 | 0.58+-.01 | 0.80+-.02 | 0.34+-.01 | --         |
| **PCNet**  | **0.97+-.02** | **0.98+-.00** | **0.98+-.01** | **0.79+-.06** | **0.92+-.09** |

#### Llama-3.1-8B (your primary interest)

| Method     | CoQA       | SQuAD v2.0 | TriviaQA   | TruthfulQA | Average    |
|------------|------------|------------|------------|------------|------------|
| Token NLL  | 0.55+-.00 | 0.61+-.01 | 0.82+-.01 | 0.49+-.00 | --         |
| SEP        | 0.33+-.20 | 0.57+-.09 | 0.52+-.09 | 0.43+-.01 | --         |
| HaloScope  | 0.97+-.02 | 0.97+-.02 | 0.95+-.06 | 0.59+-.03 | --         |
| AutoFact   | 0.56+-.01 | 0.58+-.01 | 0.80+-.01 | 0.35+-.00 | --         |
| **PCNet**  | **0.98+-.02** | **0.98+-.02** | **0.97+-.02** | **0.75+-.06** | **0.92+-.11** |

---

### Key Observation on TruthfulQA AUROC

TruthfulQA is the **hardest dataset** for PCNet across all models. The TruthfulQA AUROC values are notably lower than the other three benchmarks:

- Llama-3.2-1B: **0.66** (vs 0.91-0.98 on others)
- Llama-3.1-8B: **0.75** (vs 0.97-0.98 on others)
- Mistral-7B: **0.79** (vs 0.97-0.98 on others)
- Qwen3-4B: **0.81** (vs 0.95-0.97 on others)

The abstract's "up to 99%" claim appears to be a rounding of the 0.98 values seen on SQuAD and CoQA.

---

### Table 3: TruthfulQA Generation Scores (PC-LDCD intervention)

Baseline (Vanilla / no intervention) scores and PC-LDCD deltas:

| Model         | Vanilla T+I | PC-LDCD T+I (delta)  | Vanilla MC2 | PC-LDCD MC2 (delta) |
|---------------|-------------|----------------------|-------------|---------------------|
| Llama-3.2-1B  | 0.50        | 0.50 (+0.00)         | 0.41        | 0.51 (+0.10)        |
| Qwen3-4B      | 0.50        | 0.78 (+0.28)         | 0.50        | 0.68 (+0.19)        |
| Mistral-7B    | 0.50        | 0.72 (+0.22)         | 0.50        | 0.72 (+0.22)        |
| Llama-3.1-8B  | 0.50        | 0.69 (+0.19)         | 0.44        | 0.65 (+0.21)        |

Baselines in Table 3: DoLa, ITI, AdaSteer, SADI, ICD (PC-LDCD achieves highest T+I and MC2 in 3 of 4 models).

---

### Corruption/Preservation (Table 2)

PC-LDCD's gating achieves:
- **Mean corruption rate: 53.7%** (fraction of correct responses degraded)
- **Mean preservation rate: 79.3%**

---

### Summary for Llama-3.1-8B Specifically

- **TruthfulQA AUROC (detection):** 0.75 +/- 0.06
- **CoQA AUROC:** 0.98 +/- 0.02
- **SQuAD v2.0 AUROC:** 0.98 +/- 0.02
- **TriviaQA AUROC:** 0.97 +/- 0.02
- **Average AUROC:** 0.92 +/- 0.11
- **TruthfulQA T+I after PC-LDCD intervention:** 0.69 (+0.19 over vanilla)
- **TruthfulQA MC2 after PC-LDCD intervention:** 0.65 (+0.21 over vanilla)

Sources:
- [arXiv Abstract: 2605.05953](https://arxiv.org/abs/2605.05953)
- [arXiv HTML Full Paper: 2605.05953](https://arxiv.org/html/2605.05953)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94a64be6-e653-4f35-ad4e-4a19c392d50b",
  "isSidechain": true,
  "agentId": "a31d343b46aae0e38",
  "requestId": "req_011Cb4Zevk4F8y3LiF6bRdXm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47e900f1-9f32-4073-b5fc-6b3cb1acb0a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ec03012a-0d53-4930-b928-49d05aafb81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WpRDkYXyEbjWD5WWaz9Msp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 16376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 658,
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
