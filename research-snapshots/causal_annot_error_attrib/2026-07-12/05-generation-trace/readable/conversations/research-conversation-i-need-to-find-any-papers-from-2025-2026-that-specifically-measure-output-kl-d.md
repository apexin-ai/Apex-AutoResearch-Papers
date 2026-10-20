# Research conversation: I need to find any papers from 2025-2026 that specifically measure output KL divergence under intermediate-layer perturb

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae77757c9de41a3b3.jsonl`
- **Structured JSON:** [`935e0fe50eda591f1e20.json`](../../sessions/93/935e0fe50eda591f1e20.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-16T10:15:43.503Z_

I need to find any papers from 2025-2026 that specifically measure output KL divergence under intermediate-layer perturbation for hallucination detection or confidence calibration. This is the core method of a proposal called "Logit Sensitivity Probing" (LSP) and I need to check if anyone has already done this.

Search for:
1. "intermediate layer perturbation KL divergence hallucination 2025 2026"
2. "residual stream perturbation output KL hallucination"
3. "layer-wise noise injection logit sensitivity"
4. "causal tracing perturbation hallucination detection"
5. "forward-only sharpness estimation hallucination"
6. "geometric margin proxy hallucination detection"

Also specifically check:
- Has anyone combined causal tracing (from ROME/Meng et al. 2022) with perturbation-based hallucination detection?
- Is there any work from 2025-2026 that uses adaptive layer selection for perturbation-based methods?

Also search for: "Pan et al optimal stability KL divergence Gaussian perturbations arxiv 2604.11026" - verify this paper exists.

And search for: "Aletheia quantifying cognitive conviction reasoning models arxiv 2601.01532" - verify this exists.

Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "e5886623-e1ba-40b4-b12c-966c78326a04",
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

_source line 2 · 2026-05-16T10:15:43.507Z_

```json
{
  "parentUuid": "e5886623-e1ba-40b4-b12c-966c78326a04",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
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
  "uuid": "f75382d1-530b-4ff1-82cf-9c6140493657",
  "timestamp": "2026-05-16T10:15:43.507Z",
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

_source line 3 · 2026-05-16T10:15:46.414Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MnWh3jBD4aURhP6grKPpKz`</summary>

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
  "parentUuid": "f75382d1-530b-4ff1-82cf-9c6140493657",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65D2ysSSnhbhbFrUQXH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2375d1c4-db4b-4882-9633-86be78288c88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtuMDNVpDXoCAKnm3kWqGz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 859
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 859,
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

_source line 4 · 2026-05-16T10:15:46.417Z_

<details><summary>↩ Tool result · `toolu_01MnWh3jBD4aURhP6grKPpKz`</summary>

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
  "parentUuid": "2375d1c4-db4b-4882-9633-86be78288c88",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "1759c791-8b45-44c1-bcc2-1fd7877f5c2b",
  "sourceToolAssistantUUID": "2375d1c4-db4b-4882-9633-86be78288c88",
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

_source line 5 · 2026-05-16T10:15:50.614Z_

I'll search for each of these queries to check for prior work on the LSP concept.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1759c791-8b45-44c1-bcc2-1fd7877f5c2b",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65DFect3z3SRVdEjgfH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "415a911f-770c-420f-a8aa-9acb3099acc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDSEsp5NFk4XBSXyRbmcur",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 6 · 2026-05-16T10:15:50.936Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H1xZYZsWbEqXRvxc9JU52P`</summary>

```json
{
  "query": "intermediate layer perturbation KL divergence hallucination detection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "415a911f-770c-420f-a8aa-9acb3099acc6",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65DFect3z3SRVdEjgfH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35de2d8f-c9bc-4677-b6e2-9b57b7faf4a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDSEsp5NFk4XBSXyRbmcur",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-16T10:15:51.396Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E6jWzstafzcrGofrbKgE2t`</summary>

```json
{
  "query": "residual stream perturbation output KL hallucination LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35de2d8f-c9bc-4677-b6e2-9b57b7faf4a7",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65DFect3z3SRVdEjgfH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "018d8022-34e1-4f07-b7b2-896e899db144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDSEsp5NFk4XBSXyRbmcur",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9082,
      "output_tokens": 184,
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
          "output_tokens": 184,
          "cache_read_input_tokens": 9082,
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

### Tool call

_source line 8 · 2026-05-16T10:15:51.402Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QYFJfSMjHBxKtXgCMnL8a6`</summary>

```json
{
  "query": "layer-wise noise injection logit sensitivity hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "018d8022-34e1-4f07-b7b2-896e899db144",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65DFect3z3SRVdEjgfH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36b06fba-3123-4dfa-a0aa-3af7106b2bd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDSEsp5NFk4XBSXyRbmcur",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9082,
      "output_tokens": 184,
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
          "output_tokens": 184,
          "cache_read_input_tokens": 9082,
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

_source line 9 · 2026-05-16T10:15:58.438Z_

<details><summary>↩ Tool result · `toolu_01H1xZYZsWbEqXRvxc9JU52P`</summary>

```text
Web search results for query: "intermediate layer perturbation KL divergence hallucination detection 2025 2026"

Links: [{"title":"Neural Probe–Based Hallucination Detection for Large Language Models","url":"https://arxiv.org/html/2512.20949v1"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/html/2407.05474v1"},{"title":"Diverging Towards Hallucination: Detection of Failures in Vision-Language Models via Multi-token Aggregation","url":"https://arxiv.org/html/2505.11741v1"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v2"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.20026"},{"title":"[2605.05025] Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/abs/2605.05025"}]

Based on the web search results, I found several relevant papers on intermediate layer perturbation, KL divergence, and hallucination detection from 2025-2026:

## Key Research Papers

**1. Neural Probe–Based Hallucination Detection (December 2025)**

A multi-objective joint loss combines token-level focal loss, soft span aggregation, sparsity regularization, and KL-divergence constraints to enhance detection stability and semantic discrimination. The approach establishes a layer-position–probe-performance model and introduces a Bayesian optimization–based strategy that replaces heuristic probe layer selection.

**2. Internal Attention Divergence Signals (May 2026)**

The method computes the Kullback–Leibler (KL) divergence between each attention head's distribution and a uniform reference distribution representing maximum uncertainty. These divergence signals are aggregated across heads and layers and a lightweight lasso-regularized probe is used to predict answer correctness.

**3. Perturbation-Based Detection (June 2025)**

Sample-Specific Prompting (SSP) leverages the differential sensitivity of intermediate representations as a signal for hallucination detection. Truthful and hallucinated responses exhibit distinct representational shifts under input perturbations, as factual knowledge is typically encoded in well-structured internal representations that are tightly coupled with the input and exhibit greater sensitivity in intermediate layers when perturbed.

**4. Entity Perturbation Impact Method (September 2025)**

Low Entity Perturbation Impact measured by KL divergence strongly indicates fabricated text, as its tokens are weakly tied to key entities.

These papers represent the latest advances in combining intermediate layer analysis with KL divergence metrics for detecting LLM hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35de2d8f-c9bc-4677-b6e2-9b57b7faf4a7",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "4404731a-3d41-4255-b851-939fb815444d",
  "sourceToolAssistantUUID": "35de2d8f-c9bc-4677-b6e2-9b57b7faf4a7",
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

_source line 10 · 2026-05-16T10:15:58.930Z_

<details><summary>↩ Tool result · `toolu_01QYFJfSMjHBxKtXgCMnL8a6`</summary>

```text
Web search results for query: "layer-wise noise injection logit sensitivity hallucination"

Links: [{"title":"Enhancing Hallucination Detection through Noise Injection","url":"https://arxiv.org/html/2502.03799"},{"title":"Noise Augmented Fine Tuning for Mitigating Hallucinations in Large Language Models","url":"https://arxiv.org/html/2504.03302v2"},{"title":"Depth Gives a False Sense of Privacy: LLM Internal States ...","url":"https://www.usenix.org/system/files/usenixsecurity25-dong-tian.pdf"},{"title":"LISA: A Layer-wise Integration and Suppression Approach for Hallucination Mitigation in Multimodal Large Language Models","url":"https://arxiv.org/html/2507.19110v1"},{"title":"LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://openreview.net/pdf?id=LYx4w3CAgy"},{"title":"Enhancing Hallucination Detection with Noise Injection | OpenReview","url":"https://openreview.net/forum?id=2bWf4M5tRo"},{"title":"Context and Layers in Harmony: A Unified Strategy for Mitigating LLM Hallucinations","url":"https://www.mdpi.com/2227-7390/13/11/1831"},{"title":"Rethinking Layer-wise Gaussian Noise Injection: Bridging Implicit Objectives and Privacy Budget Allocation","url":"https://arxiv.org/html/2509.04232v1"},{"title":"[2507.19110] LISA: A Layer-wise Integration and Suppression Approach for Hallucination Mitigation in Multimodal Large Language Models","url":"https://arxiv.org/abs/2507.19110"},{"title":"Audio Hallucination QA Dataset","url":"https://www.emergentmind.com/topics/audio-hallucination-qa-dataset"}]

Based on the search results, here's what I found about layer-wise noise injection and logit sensitivity in the context of hallucination detection:

## Key Findings

Noise injection induces epistemic uncertainty, where the LLM shows greater uncertainty for hallucinations than non-hallucinations, as reflected by larger answer entropy. This approach addresses hallucination detection in large language models.

### Layer-wise Noise Injection Strategy

Shared layer-wise noise outperforms independent noise, validating the design choice to inject shared noise across layers to mitigate cancellation effects. The research shows that constraining noise application to specific layer subsets—such as those with the highest or lowest signal-to-noise ratios—enables more precise control over performance modulation, highlighting the utility of structurally selective noise injection.

### Logit Sensitivity and Hallucination Detection

Output logits represent meaning at a much lower, syntactic level, potentially making stability of hidden activations a better candidate to assess a model's faithfulness to the prompt in the context of detecting hallucinations. Rather than relying solely on logit outputs, the purpose of sampling for hallucination detection is to estimate the coherence among sampled responses to a prompt, via a kind of "sensitivity analysis" that makes it possible to assess the likelihood of a given prompt to elicit a hallucination in a model.

### Combining Approaches

Combining noise injection with prediction layer sampling improves hallucination/non-hallucination separation compared to using prediction layer sampling alone, highlighting the importance of combining epistemic uncertainty with aleatoric uncertainty in sampling for hallucination detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36b06fba-3123-4dfa-a0aa-3af7106b2bd4",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "dee7151d-f2b2-478f-b658-223150c953a6",
  "sourceToolAssistantUUID": "36b06fba-3123-4dfa-a0aa-3af7106b2bd4",
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

_source line 11 · 2026-05-16T10:16:00.612Z_

<details><summary>↩ Tool result · `toolu_01E6jWzstafzcrGofrbKgE2t`</summary>

```text
Web search results for query: "residual stream perturbation output KL hallucination LLM"

Links: [{"title":"Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/html/2407.05474v1"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689v4"},{"title":"Hallucinations in LLMs Are Not a Bug in the Data | Towards Data Science","url":"https://towardsdatascience.com/hallucinations-in-llms-are-not-a-bug-in-the-data/"},{"title":"LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction","url":"https://arxiv.org/html/2512.18623"},{"title":"Constructing Benchmarks and Interventions for Combating Hallucinations in LLMs","url":"https://arxiv.org/pdf/2404.09971"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://seongheon-96.github.io/assets/pdf/shaking.pdf"},{"title":"Detect, Classify, and Fix: Zero-Shot Hallucination Reasoning for LLMs | by Anna Alexandra Grigoryan | Medium","url":"https://thegrigorian.medium.com/detect-classify-and-fix-zero-shot-hallucination-reasoning-for-llms-e1086bb11bca"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"Semantic Uncertainty Quantification of Hallucinations in LLMs: A Quantum Tensor Network Based Method","url":"https://arxiv.org/html/2601.20026"}]

Based on the search results, I found several relevant papers and resources on your query about residual stream perturbation, output KL divergence, and LLM hallucination detection:

## Key Research Findings

**Entity Perturbation and KL Divergence for Hallucination Detection:**

Low Entity Perturbation Impact measured by KL divergence strongly indicates fabricated text, as its tokens are weakly tied to key entities. This finding comes from research on SHINE, a hallucination probing method. In aligned responses, tokens relevant to the subject have high KL divergence, whereas fabricated text's tokens exhibit near-zero KL divergence, indicating their weak association with the LLM's knowledge.

**Residual Stream Analysis:**

Research tracks the trajectory of the residual stream — the internal representation vector — layer by layer through the network. When a LLM hallucinates, the internal representation does not go blank. It rotates. Both paths — correct and incorrect — travel the same distance through the model's representation space. What separates them is direction, not magnitude.

**Intervention on Residual Stream:**

Intervening on the residual has a model's performance compromise, which is mitigated to some extent when intervening dynamically; intervention on the attention component is preferred over the MLP part.

**Perturbation-Based Detection Methods:**

Sample-Specific Prompting (SSP) improves self-assessment by analyzing perturbation sensitivity at intermediate representations. These representations, being less influenced by model bias, offer a more faithful view of the model's latent reasoning process.

These approaches collectively demonstrate how internal model representations and perturbation-based methods can effectively detect different types of hallucinations in LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "018d8022-34e1-4f07-b7b2-896e899db144",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "1ae83cec-cc54-4f55-8776-61c41e65a662",
  "sourceToolAssistantUUID": "018d8022-34e1-4f07-b7b2-896e899db144",
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

_source line 12 · 2026-05-16T10:16:05.163Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AqAp6DZpiVrdbFV9MjpXgt`</summary>

```json
{
  "query": "causal tracing perturbation hallucination detection ROME Meng 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ae83cec-cc54-4f55-8776-61c41e65a662",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65EJJtUNNqnjKyfMAH7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41080960-de4e-47bf-bd38-fe09966e4d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ujt3RCoFN3Fjxu9B7oGpB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 899,
      "cache_creation_input_tokens": 2066,
      "cache_read_input_tokens": 10474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2066,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 13 · 2026-05-16T10:16:06.085Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016TptcbUEtGPrubxK12d7aE`</summary>

```json
{
  "query": "forward-only sharpness estimation hallucination LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41080960-de4e-47bf-bd38-fe09966e4d7c",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65EJJtUNNqnjKyfMAH7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1be665ba-c930-4ac5-bbac-adfb801c961e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ujt3RCoFN3Fjxu9B7oGpB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 899,
      "cache_creation_input_tokens": 2066,
      "cache_read_input_tokens": 10474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2066,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 14 · 2026-05-16T10:16:06.316Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P1TXczBEXBS7KbFxjwrF95`</summary>

```json
{
  "query": "geometric margin proxy hallucination detection neural network"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1be665ba-c930-4ac5-bbac-adfb801c961e",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65EJJtUNNqnjKyfMAH7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c40280a3-c772-4503-a14a-730a963c64ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ujt3RCoFN3Fjxu9B7oGpB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 899,
      "cache_creation_input_tokens": 2066,
      "cache_read_input_tokens": 10474,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2066
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 899,
          "output_tokens": 163,
          "cache_read_input_tokens": 10474,
          "cache_creation_input_tokens": 2066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2066,
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

_source line 15 · 2026-05-16T10:16:12.580Z_

<details><summary>↩ Tool result · `toolu_016TptcbUEtGPrubxK12d7aE`</summary>

```text
Web search results for query: "forward-only sharpness estimation hallucination LLM"

Links: [{"title":"[2403.01548] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://arxiv.org/abs/2403.01548"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"},{"title":"In-Context Sharpness as Alerts: An Inner Representation...","url":"https://www.emergentmind.com/papers/2403.01548"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"},{"title":"[Quick Review] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://liner.com/review/incontext-sharpness-as-alerts-inner-representation-perspective-for-hallucination-mitigation"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation | OpenReview","url":"https://openreview.net/forum?id=s3e8poX3kb"},{"title":"LLM Hallucinations 101","url":"https://neptune.ai/blog/llm-hallucinations"},{"title":"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3703155"},{"title":"Reducing LLM Hallucinations: A Developer's Guide | Zep","url":"https://www.getzep.com/ai-agents/reducing-llm-hallucinations/"},{"title":"Why Language Models Hallucinate Adam Tauman Kalai∗ OpenAI Ofir Nachum OpenAI","url":"https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf"}]

Based on the web search results, I found relevant information about sharpness estimation and hallucination mitigation in LLMs:

Research has discovered a pattern associated with hallucinations: correct generations tend to have sharper context activations in the hidden states of the in-context tokens, compared to incorrect ones.

Researchers have proposed an entropy-based metric to quantify the "sharpness" among in-context hidden states and incorporated it into the decoding process to formulate a constrained decoding approach. This entropy-based metric is used to quantify in-context sharpness and is incorporated into the decoding process to enhance the factuality of generated outputs.

Lower entropy (sharper activations) is associated with more factual outputs. A constrained decoding approach, named Activation Decoding, is proposed, utilizing the sharpness metric to improve the factuality of LLM outputs.

Experiments on various knowledge-seeking and hallucination benchmarks demonstrate this approach's consistent effectiveness, for example, achieving up to an 8.6 point improvement on TruthfulQA.

This research appears to fall within the broader field of strategies for hallucination detection based on the premise that LLM hallucinations are inherently tied to the model's uncertainty, and that by estimating the uncertainty of the factual content generated by the model, it becomes feasible to detect hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1be665ba-c930-4ac5-bbac-adfb801c961e",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "47f57470-656b-4cdd-8b49-83cfca6a1ed3",
  "sourceToolAssistantUUID": "1be665ba-c930-4ac5-bbac-adfb801c961e",
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

_source line 16 · 2026-05-16T10:16:13.080Z_

<details><summary>↩ Tool result · `toolu_01P1TXczBEXBS7KbFxjwrF95`</summary>

```text
Web search results for query: "geometric margin proxy hallucination detection neural network"

Links: [{"title":"[2510.04933] The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2510.04933"},{"title":"The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection","url":"https://arxiv.org/pdf/2510.04933"},{"title":"The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2510.04933v1"},{"title":"[2510.04933v1] The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2510.04933v1"},{"title":"The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251004933H/abstract"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"},{"title":"A Geometric Method to Spot Hallucinations Without an LLM Judge | Towards Data Science","url":"https://towardsdatascience.com/the-red-bird/"},{"title":"Geometric Uncertainty for Detecting and Correcting Hallucinations in LLMs","url":"https://arxiv.org/html/2509.13813v1"},{"title":"Neural Uncertainty Principle: A Unified View of Adversarial Fragility and LLM Hallucination","url":"https://arxiv.org/html/2603.19562v1"},{"title":"ICML What do Geometric Hallucination Detection Metrics Actually Measure?","url":"https://icml.cc/virtual/2025/50931"}]

Based on the search results, I found several relevant research papers on geometric methods for hallucination detection in neural networks. Here's what the search revealed:

## Key Research Areas

**Layer-wise Semantic Dynamics (LSD):**
LSD presents a geometric framework for hallucination detection that analyzes the evolution of hidden-state semantics across transformer layers. Using margin-based contrastive learning, LSD aligns hidden activations with ground-truth embeddings, revealing a distinct separation in semantic trajectories: factual responses preserve stable alignment, while hallucinations exhibit pronounced semantic drift across depth.

**Transport Geometry Approach:**
Another approach uses transport geometry for hallucination detection. This formulates hallucination detection as a problem of trajectory dynamics in hidden-state space, characterizing a first reasoning error as a localized transport excursion away from the manifold of locally coherent transitions.

**Geometric Uncertainty Methods:**
A geometric framework for detecting hallucinations uses only black-box access, where Geometric Volume quantifies semantic dispersion through convex hull analysis of archetypes and provides a principled proxy for uncertainty.

**Neural Uncertainty Principle:**
Research reveals that adversarial vulnerability and hallucination share a common geometric origin, formalizing a Neural Uncertainty Principle where in near-bound regimes, weak prompt–gradient coupling leaves generation under-constrained, leading to hallucination.

These approaches demonstrate that geometric properties of neural representations can effectively detect hallucinations without requiring external verification sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c40280a3-c772-4503-a14a-730a963c64ed",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "e1061bbf-9098-4393-b26a-03143a09780c",
  "sourceToolAssistantUUID": "c40280a3-c772-4503-a14a-730a963c64ed",
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

_source line 17 · 2026-05-16T10:16:14.312Z_

<details><summary>↩ Tool result · `toolu_01AqAp6DZpiVrdbFV9MjpXgt`</summary>

```text
Web search results for query: "causal tracing perturbation hallucination detection ROME Meng 2025 2026"

Links: [{"title":"Causal Tracing of Object Representations in Large Vision Language Models: Mechanistic Interpretability and Hallucination Mitigation","url":"https://arxiv.org/html/2511.05923v3"},{"title":"Mechanisms of Non-Factual Hallucination in Language Models","url":"https://arxiv.org/html/2403.18167v1"},{"title":"Interpreting and Editing Vision-Language Representations to ...","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-45.pdf"},{"title":"LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction","url":"https://arxiv.org/html/2512.18623"},{"title":"(PDF) A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation","url":"https://www.researchgate.net/publication/396593833_A_Survey_on_Hallucination_in_Large_Language_Models_Definitions_Detection_and_Mitigation"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"Published as a conference paper at ICLR 2025 REDEEP: DETECTING HALLUCINATION IN","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf"},{"title":"Mitigating Hallucinations in MLLMs with Attention Causal ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_Seeing_Far_and_Clearly_Mitigating_Hallucinations_in_MLLMs_with_Attention_CVPR_2025_paper.pdf"},{"title":"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3703155"},{"title":"Seeing Far and Clearly: Mitigating Hallucinations in MLLMs with Attention Causal Decoding - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12425127/"}]

Based on the web search results, I found several relevant papers and research on causal tracing, perturbation, hallucination detection, and related topics:

## Key Findings

**Causal Tracing with Perturbation for Hallucination Detection:**

Recent work employs controlled Gaussian perturbations to input images to induce measurable drops in output probabilities, then restores specific activations using clean activations from the original image input, quantifying the recovery in outputs to precisely estimate the causal effect on visual object perception for each core component across token types and layers.

**ROME (Rank-One Model Editing) and Meng's Work:**

Knowledge tracing within Language Models has gained substantial attention, with researchers investigating specific layers and neurons responsible for storing factual information, following work by Meng et al. (2022a) and others. Approaches follow a "locate-then-edit" paradigm, first identifying model parameters most relevant to a target fact via causal tracing.

**Hallucination Detection Methods:**

Causal indirect effect features best predict model hallucinations on all datasets, consistently exceeding all baseline models. Recent work decouples confounders between parametric knowledge and external context using mechanistic interpretability, incorporating them as covariates to improve hallucination detection.

**Recent 2025-2026 Research:**

Recent work employs causal tracing with Gaussian noise to precisely quantify the functional roles of MHSA, FFN, and hidden states for both visual and textual tokens across layers, enabling fine-grained analysis of how LVLMs perceive and process visual object information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41080960-de4e-47bf-bd38-fe09966e4d7c",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "785f89ae-c3da-4f40-b5f6-e7767753b357",
  "sourceToolAssistantUUID": "41080960-de4e-47bf-bd38-fe09966e4d7c",
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

_source line 18 · 2026-05-16T10:16:17.769Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014dLsfF78FtmcfvWdG643ah`</summary>

```json
{
  "query": "Pan et al \"optimal stability\" KL divergence Gaussian perturbations arxiv 2604.11026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "785f89ae-c3da-4f40-b5f6-e7767753b357",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65FJfzTxx9JY6GmMgDw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e0cb660-7c0b-4d73-9f0a-46a01d19d761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWJs3mqbbQsSyhGnZZqH1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1815,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 12540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2126,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 19 · 2026-05-16T10:16:18.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dzv4dE6FiUwfWmrSaHeYYk`</summary>

```json
{
  "query": "Aletheia \"quantifying cognitive conviction\" reasoning models arxiv 2601.01532"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e0cb660-7c0b-4d73-9f0a-46a01d19d761",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65FJfzTxx9JY6GmMgDw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfac40c9-63f2-47bc-b48a-8e2ed16af34f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWJs3mqbbQsSyhGnZZqH1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1815,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 12540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2126,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 20 · 2026-05-16T10:16:19.280Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NtziPV9xmGAUv9LjRTUCd7`</summary>

```json
{
  "query": "adaptive layer selection perturbation hallucination detection LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfac40c9-63f2-47bc-b48a-8e2ed16af34f",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65FJfzTxx9JY6GmMgDw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f709fb13-96c2-4fa8-9b5b-fa93fd42dde3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWJs3mqbbQsSyhGnZZqH1s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1815,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 12540,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1815,
          "output_tokens": 182,
          "cache_read_input_tokens": 12540,
          "cache_creation_input_tokens": 2126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2126,
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

_source line 21 · 2026-05-16T10:16:23.514Z_

<details><summary>↩ Tool result · `toolu_014dLsfF78FtmcfvWdG643ah`</summary>

```text
Web search results for query: "Pan et al "optimal stability" KL divergence Gaussian perturbations arxiv 2604.11026"

Links: [{"title":"[2604.11026] Optimal Stability of KL Divergence under Gaussian Perturbations","url":"https://arxiv.org/abs/2604.11026"},{"title":"Optimal Stability of KL Divergence under Gaussian Perturbations","url":"https://arxiv.org/html/2604.11026"},{"title":"arXiv:1712.07196v2 [cs.LG] 11 Jun 2018 Calibrating Noise to Variance","url":"https://arxiv.org/pdf/1712.07196"},{"title":"Adaptive Symmetrization of the KL Divergence","url":"https://arxiv.org/pdf/2511.11159"},{"title":"KL Divergence Between Gaussians: A Step-by-Step Derivation for the Variational Autoencoder Objective","url":"https://arxiv.org/html/2604.11744"},{"title":"Information Theoretic Learning for Diffusion Models with Warm Start Yirong Shen","url":"https://arxiv.org/pdf/2510.20903"},{"title":"Divergence-Guided Particle Swarm Optimization","url":"https://arxiv.org/html/2604.12001"},{"title":"[2604.11744] KL Divergence Between Gaussians: A Step-by-Step Derivation for the Variational Autoencoder Objective","url":"https://arxiv.org/abs/2604.11744"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2101.09258"},{"title":"Stability Evaluation via Distributional Perturbation Analysis","url":"https://arxiv.org/html/2405.03198v1"}]

I found the paper! Here's what the search returned:

The paper studies the stability of Kullback-Leibler (KL) divergence under Gaussian perturbations beyond Gaussian families, establishing a sharp stability bound between an arbitrary distribution and Gaussian families under mild moment conditions.

For a distribution P with finite second moment and multivariate Gaussian distributions N₁ and N₂, the authors show that if KL(P||N₁) is large and KL(N₁||N₂) is at most ε, then KL(P||N₂) ≥ KL(P||N₁) - O(√ε). Moreover, they prove that this √ε rate is optimal in general, even within the Gaussian family.

Existing relaxed triangle inequalities for KL divergence critically rely on the assumption that all involved distributions are Gaussian, which limits their applicability in modern applications such as out-of-distribution (OOD) detection with flow-based generative models. The paper removes this restriction.

The authors are Jialu Pan, Yufeng Zhang, Nan Hu, Zhenbang Chen, Ji Wang, and Keqin Li.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e0cb660-7c0b-4d73-9f0a-46a01d19d761",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "bafd8574-7b5a-4c07-b99e-b670c77c7795",
  "sourceToolAssistantUUID": "9e0cb660-7c0b-4d73-9f0a-46a01d19d761",
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

_source line 22 · 2026-05-16T10:16:25.072Z_

<details><summary>↩ Tool result · `toolu_01NtziPV9xmGAUv9LjRTUCd7`</summary>

```text
Web search results for query: "adaptive layer selection perturbation hallucination detection LLM 2025 2026"

Links: [{"title":"[2504.07863] Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/abs/2504.07863"},{"title":"Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/html/2504.07863v2"},{"title":"GitHub - mala-lab/HaMI: [NeurIPS 2025] Official implementation for ''Robust Hallucination Detection in LLMs via Adaptive Token Selection'' https://arxiv.org/abs/2504.07863 · GitHub","url":"https://github.com/mala-lab/HaMI"},{"title":"Hallucinations","url":"https://www.aussieai.com/research/hallucinations"},{"title":"[Literature Review] Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://www.themoonlight.io/en/review/robust-hallucination-detection-in-llms-via-adaptive-token-selection"},{"title":"Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration","url":"https://arxiv.org/html/2603.22812v1"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"Detecting LLM Hallucination Through Layer-wise ...","url":"https://aclanthology.org/2025.emnlp-main.1644.pdf"},{"title":"How to evaluate LLM hallucination rates in engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/how-to-evaluate-llm-hallucination-rates-in-engineering/"},{"title":"Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://openreview.net/pdf/6e36e6ecbe04ac41b08bdb225a947bda56a47410.pdf"}]

Based on the web search results, I found several relevant papers and research on hallucination detection in LLMs from 2025-2026:

## Primary Research

HaMI is a novel approach that enables robust detection of hallucinations through adaptive selection and learning of critical tokens that are most indicative of hallucinations. The MIL-driven hallucination detector is optimized to assign hallucination scores to individual token instances and adaptively select the most indicative tokens in both positive and negative bags for sequence-level prediction, distinguishing the most hallucinated token instances from hard negative token instances. This work was presented at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025).

## Related Perturbation-Based Approaches

A perturbation-based importance sampling strategy is developed to systematically explore the semantic space in hallucination detection. Additionally, a guided semantic exploration strategy with importance sampling discovers diverse semantic interpretations by perturbing critical tokens, accelerating convergence compared to random sampling.

## Layer-wise Analysis

Research on detecting LLM hallucination through layer-wise information deficiency analyzes ambiguous prompts and unanswerable questions.

The search results demonstrate active research in 2025-2026 on using adaptive selection mechanisms, perturbation strategies, and internal representation analysis for robust hallucination detection in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f709fb13-96c2-4fa8-9b5b-fa93fd42dde3",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "25cbb0a1-2f9d-43b0-a166-75ecdfb002ad",
  "sourceToolAssistantUUID": "f709fb13-96c2-4fa8-9b5b-fa93fd42dde3",
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

_source line 23 · 2026-05-16T10:16:27.286Z_

<details><summary>↩ Tool result · `toolu_01Dzv4dE6FiUwfWmrSaHeYYk`</summary>

```text
Web search results for query: "Aletheia "quantifying cognitive conviction" reasoning models arxiv 2601.01532"

Links: [{"title":"[2601.01532] Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix","url":"https://arxiv.org/abs/2601.01532"},{"title":"Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix","url":"https://arxiv.org/html/2601.01532"},{"title":"Aletheia: Quantifying Cognitive Conviction in Reasoning ...","url":"https://www.arxiv.org/pdf/2601.01532"},{"title":"Aletheia: Quantifying Cognitive Conviction in Reasoning ...","url":"https://web3.arxiv.org/pdf/2601.01532"},{"title":"(PDF) Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix","url":"https://www.researchgate.net/publication/399477532_Aletheia_Quantifying_Cognitive_Conviction_in_Reasoning_Models_via_Regularized_Inverse_Confusion_Matrix"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=842&show=2000"},{"title":"Project Aletheia: Verifier-Guided Distillation of Backtracking for Small Language Models","url":"https://arxiv.org/html/2601.14290v1"},{"title":"[2601.14290] Project Aletheia: Verifier-Guided Distillation of Backtracking for Small Language Models","url":"https://arxiv.org/abs/2601.14290"},{"title":"Paper page - Towards Autonomous Mathematics Research","url":"https://huggingface.co/papers/2602.10177"},{"title":"Towards Autonomous Mathematics Research","url":"https://arxiv.org/html/2602.10177v1"}]

I found the paper you're looking for. Here's what the search revealed about arXiv paper 2601.01532:

## Aletheia: Quantifying Cognitive Conviction in Reasoning Models

Project Aletheia is a cognitive physics framework that employs Tikhonov Regularization to invert the judge's confusion matrix.

**Key Problem**: Current evaluation paradigms face an epistemological crisis, with static benchmarks measuring knowledge breadth but failing to quantify the depth of belief.

**Main Contribution**: The framework extends previous work to quantify "Cognitive Conviction" in System 2 reasoning models. To validate this methodology without relying on opaque private data, the authors implement a Synthetic Proxy Protocol.

**Key Findings**: A preliminary pilot study on 2025 baselines (e.g., DeepSeek-R1, OpenAI o1) suggests that while reasoning models act as a "cognitive buffer," they may exhibit "Defensive OverThinking" under adversarial pressure.

**Safety Consideration**: The authors introduce the Aligned Conviction Score (S_aligned) to verify that conviction does not compromise safety.

The paper was submitted on January 4, 2026, and is authored by Fanzhe Fu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfac40c9-63f2-47bc-b48a-8e2ed16af34f",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "282ff6a0-3ebc-4222-9a6c-e0b72f9077d5",
  "sourceToolAssistantUUID": "bfac40c9-63f2-47bc-b48a-8e2ed16af34f",
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

_source line 24 · 2026-05-16T10:16:31.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BURAcuPBM9X8CZ3rjSZGco`</summary>

```json
{
  "query": "\"Shaking to Reveal\" perturbation detection LLM hallucinations 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "282ff6a0-3ebc-4222-9a6c-e0b72f9077d5",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65GG9Dg63NveHrorX2d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba530ece-c07d-4b06-9c50-6d3a59bd15fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USYHeJyNZF9tDdvWxpD8R6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 899,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 14666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 25 · 2026-05-16T10:16:32.454Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019pS9A2Dek7QFnA5GAkYYJY`</summary>

```json
{
  "query": "\"Enhancing Hallucination Detection through Noise Injection\" arxiv 2502.03799 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba530ece-c07d-4b06-9c50-6d3a59bd15fb",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65GG9Dg63NveHrorX2d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc51e8bc-1f7a-417d-b353-7e8ee47d40a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USYHeJyNZF9tDdvWxpD8R6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 899,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 14666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 26 · 2026-05-16T10:16:33.333Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NcQsVdrB5rnHncuLVMYkRj`</summary>

```json
{
  "query": "\"In-Context Sharpness as Alerts\" hallucination inner representation 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc51e8bc-1f7a-417d-b353-7e8ee47d40a4",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65GG9Dg63NveHrorX2d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd6c40e2-e909-4694-b377-0dd04bb34da8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USYHeJyNZF9tDdvWxpD8R6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 899,
      "cache_creation_input_tokens": 3588,
      "cache_read_input_tokens": 14666,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3588
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 899,
          "output_tokens": 189,
          "cache_read_input_tokens": 14666,
          "cache_creation_input_tokens": 3588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3588,
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

_source line 27 · 2026-05-16T10:16:38.532Z_

<details><summary>↩ Tool result · `toolu_01BURAcuPBM9X8CZ3rjSZGco`</summary>

```text
Web search results for query: ""Shaking to Reveal" perturbation detection LLM hallucinations 2025 arxiv"

Links: [{"title":"[2506.02696] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696"},{"title":"[2506.02696v1] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://www.researchgate.net/publication/392371301_Shaking_to_Reveal_Perturbation-Based_Detection_of_LLM_Hallucinations"},{"title":"[Literature Review] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://www.themoonlight.io/en/review/shaking-to-reveal-perturbation-based-detection-of-llm-hallucinations"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/pdf/2506.02696"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689v4"},{"title":"Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/html/2502.12964"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://www.alphaxiv.org/overview/2506.02696v1"},{"title":"arXiv:2507.02870v1 [cs.CL] 6 Jun 2025 1","url":"https://arxiv.org/pdf/2507.02870"}]

I found the paper "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations"! Here's what the research is about:

## Overview

Hallucination remains a key obstacle to the reliable deployment of large language models (LLMs) in real-world question answering tasks.

## The Proposed Approach

The researchers propose Sample-Specific Prompting (SSP), a new framework that improves self-assessment by analyzing perturbation sensitivity at intermediate representations, which are less influenced by model bias and offer a more faithful view of the model's latent reasoning process.

## How It Works

SSP dynamically generates noise prompts for each input and employs a lightweight encoder to amplify the changes in representations caused by the perturbation, with a contrastive distance metric then used to quantify these differences and separate truthful from hallucinated responses.

## Key Innovation

The authors are the first to leverage the sensitivity of LLMs to input perturbations as a signal for hallucination detection, providing a novel perspective on this problem.

## Results

The method improves hallucination detection accuracy by 4.78% (AUROC) on the challenging TruthfulQA benchmark. Extensive experiments demonstrate that SSP significantly outperforms prior methods across a range of hallucination detection benchmarks.

The paper was submitted to arXiv on June 3, 2025 (arXiv:2506.02696).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba530ece-c07d-4b06-9c50-6d3a59bd15fb",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "0ce3dd4c-af6d-4d5b-9d52-6061783decf1",
  "sourceToolAssistantUUID": "ba530ece-c07d-4b06-9c50-6d3a59bd15fb",
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

_source line 28 · 2026-05-16T10:16:38.561Z_

<details><summary>↩ Tool result · `toolu_01NcQsVdrB5rnHncuLVMYkRj`</summary>

```text
Web search results for query: ""In-Context Sharpness as Alerts" hallucination inner representation 2024"

Links: [{"title":"[2403.01548] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://arxiv.org/abs/2403.01548"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://proceedings.mlr.press/v235/chen24av.html"},{"title":"GitHub - hkust-nlp/Activation_Decoding: In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation (ICML 2024)","url":"https://github.com/hkust-nlp/activation_decoding"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation - Paper Detail","url":"https://deeplearn.org/arxiv/464750/in-context-sharpness-as-alerts:-an-inner-representation-perspective-for-hallucination-mitigation"},{"title":"[PDF] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/In-Context-Sharpness-as-Alerts:-An-Inner-for-Chen-Xiong/ed8f46f493abce9498851e647d900a4628f6ff7f"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation | OpenReview","url":"https://openreview.net/forum?id=s3e8poX3kb"},{"title":"In-Context Sharpness as Alerts: An Inner Representation...","url":"https://www.emergentmind.com/papers/2403.01548"},{"title":"ICML Poster In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://icml.cc/virtual/2024/poster/32930"},{"title":"IN-CONTEXT SHARPNESS AS ALERTS: AN INNER REP","url":"https://openreview.net/pdf?id=24U6vAHnYM"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://paperreading.club/page?id=212632"}]

I found comprehensive information about this paper. Here are the key findings:

## Overview

"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation" is a 2024 research paper that investigates hallucinations in large language models through the lens of inner representations.

## Main Discovery

The study discovers a salient pattern associated with hallucinations: correct generations tend to have sharper context activations in the hidden states of the in-context tokens, compared to the incorrect ones.

## Proposed Solution

The researchers propose an entropy-based metric to quantify the "sharpness" among the in-context hidden states and incorporate it into the decoding process to formulate a constrained decoding approach. Lower entropy (sharper activations) is associated with more factual outputs.

## Results

Experiments on various knowledge-seeking and hallucination benchmarks demonstrate the approach's consistent effectiveness, for example, achieving up to an 8.6 point improvement on TruthfulQA. The experiments were conducted on knowledge-seeking datasets (Natural Questions, HotpotQA, TriviaQA) and hallucination benchmark (TruthfulQA).

## Publication

The paper was published in March 2024 on arXiv and accepted to ICML 2024. Code for the approach, called "Activation Decoding," is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd6c40e2-e909-4694-b377-0dd04bb34da8",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "ff8e4fdf-546e-446d-bf15-f295d372e168",
  "sourceToolAssistantUUID": "cd6c40e2-e909-4694-b377-0dd04bb34da8",
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

_source line 29 · 2026-05-16T10:16:39.138Z_

<details><summary>↩ Tool result · `toolu_019pS9A2Dek7QFnA5GAkYYJY`</summary>

```text
Web search results for query: ""Enhancing Hallucination Detection through Noise Injection" arxiv 2502.03799 2025"

Links: [{"title":"[2502.03799] Enhancing Hallucination Detection through Noise Injection","url":"https://arxiv.org/abs/2502.03799"},{"title":"Enhancing Hallucination Detection through Noise Injection","url":"https://arxiv.org/html/2502.03799"},{"title":"Enhancing Hallucination Detection through Noise Injection | alphaXiv","url":"https://www.alphaxiv.org/ja/overview/2502.03799v1"},{"title":"Noise Augmented Fine Tuning for Mitigating Hallucinations in Large Language Models","url":"https://arxiv.org/html/2504.03302v2"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=1875&show=2000"},{"title":"Enhancing Hallucination Detection with Noise Injection | OpenReview","url":"https://openreview.net/forum?id=2bWf4M5tRo"},{"title":"Demystifying Hallucination in Speech Foundation Models","url":"https://aclanthology.org/2025.findings-acl.1190.pdf"},{"title":"[2407.05474] Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/abs/2407.05474"},{"title":"Hallucination Detection: A Probabilistic Framework Using Embeddings Distance Analysis","url":"https://arxiv.org/html/2502.08663v1"},{"title":"Hallucinations","url":"https://www.aussieai.com/research/hallucinations"}]

I found the paper! Here's what I found about "Enhancing Hallucination Detection through Noise Injection" (arxiv 2502.03799):

**Paper Details:**
The paper is authored by Litian Liu, Reza Pourreza, Sunny Panchal, Apratim Bhattacharyya, Yubing Jian, Yao Qin, and Roland Memisevic, submitted on February 6, 2025, with the latest version (v3) revised on March 1, 2026.

**Research Focus:**
The paper addresses how Large Language Models (LLMs) are prone to generating plausible yet incorrect responses, known as hallucinations, and emphasizes that effectively detecting hallucinations is crucial for the safe deployment of LLMs.

**Key Contribution:**
While recent research has linked hallucinations to model uncertainty and suggests detecting them by measuring dispersion over answer distributions from multiple model samples, the authors argue that drawing from the token distribution defined by the model is suboptimal for hallucination detection.

**Proposed Solution:**
The authors show that detection can be improved significantly by taking into account model uncertainty in the Bayesian sense, proposing an approach that perturbs an appropriate subset of model parameters or hidden unit activations during sampling.

The paper was accepted as a main conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc51e8bc-1f7a-417d-b353-7e8ee47d40a4",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "0ae96f5f-5778-4b86-ac33-c182b568a638",
  "sourceToolAssistantUUID": "cc51e8bc-1f7a-417d-b353-7e8ee47d40a4",
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

_source line 30 · 2026-05-16T10:16:42.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A7oPc9a1Dy2DomoaqMwFbi`</summary>

```json
{
  "query": "\"Probing LLM Hallucination from Within\" perturbation-driven internal knowledge 2024 arxiv 2411.09689"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ae96f5f-5778-4b86-ac33-c182b568a638",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65H8sgr7gqjwGFzFYtW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ff79a98-5236-4d14-80ce-ea7d2bf11a9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJ9wXBqfk7dBXKfnBsz1Yz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 988,
      "cache_creation_input_tokens": 2808,
      "cache_read_input_tokens": 18254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2808,
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

_source line 31 · 2026-05-16T10:16:43.761Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TkvH1GmDYpTyLbKLZrPcfm`</summary>

```json
{
  "query": "\"Neural Probe-Based Hallucination Detection\" Bayesian optimization probe layer selection arxiv 2512.20949"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ff79a98-5236-4d14-80ce-ea7d2bf11a9b",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65H8sgr7gqjwGFzFYtW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ee38717-c5d1-46b8-b26f-70dca65ef44f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJ9wXBqfk7dBXKfnBsz1Yz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 988,
      "cache_creation_input_tokens": 2808,
      "cache_read_input_tokens": 18254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2808,
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

_source line 32 · 2026-05-16T10:16:44.228Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AHJcj9TW2JgT65JReYA3iP`</summary>

```json
{
  "query": "\"LLM-CAS\" dynamic neuron perturbation real-time hallucination correction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ee38717-c5d1-46b8-b26f-70dca65ef44f",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65H8sgr7gqjwGFzFYtW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "616339a4-cf23-4b00-8722-56b0e0b4db17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJ9wXBqfk7dBXKfnBsz1Yz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 988,
      "cache_creation_input_tokens": 2808,
      "cache_read_input_tokens": 18254,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2808
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 988,
          "output_tokens": 203,
          "cache_read_input_tokens": 18254,
          "cache_creation_input_tokens": 2808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2808,
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

_source line 33 · 2026-05-16T10:16:48.813Z_

<details><summary>↩ Tool result · `toolu_01A7oPc9a1Dy2DomoaqMwFbi`</summary>

```text
Web search results for query: ""Probing LLM Hallucination from Within" perturbation-driven internal knowledge 2024 arxiv 2411.09689"

Links: [{"title":"[2411.09689] Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/abs/2411.09689"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge — Seongmin Lee","url":"https://seongmin.xyz/papers/llm-hallucination-probing"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Method via Internal Knowledge | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11402288/"},{"title":"LLM Hallucination Reasoning with Zero-shot Knowledge Test","url":"https://arxiv.org/html/2411.09689v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"Case Study: Predictive Coding and Information Bottleneck for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2601.15652"},{"title":"Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/html/2502.12964v2"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v2"},{"title":"Trust Me, I’m Wrong: High-Certainty Hallucinations in LLMs","url":"https://arxiv.org/html/2502.12964v1"}]

I found the paper you're looking for! Here's information about "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge":

## Overview

The paper addresses LLM hallucination, where unfaithful text is generated, which presents a critical challenge for LLMs' practical applications.

## Key Contributions

The authors introduce hallucination probing, a new task that classifies LLM-generated text into three categories: aligned, misaligned, and fabricated.

They propose SHINE (Systematic Hallucination Inspection with Noisy Entity), a novel hallucination probing method that is driven by their discovery that perturbing key entities in prompts affects LLM's generation of these three types of text differently, and crucially, it does not require external knowledge, supervised training, or LLM fine-tuning.

## Advantages Over Existing Methods

Current detection methods often resort to external knowledge, LLM fine-tuning, or supervised training with large hallucination-labeled datasets. Moreover, these approaches do not distinguish between different types of hallucinations, which is crucial for enhancing detection performance.

## Authors and Publication

The paper was submitted on November 14, 2024 with authors Seongmin Lee, Hsiang Hsu, Chun-Fu Chen, and Duen Horng Chau.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ff79a98-5236-4d14-80ce-ea7d2bf11a9b",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "38b97409-6cec-496e-8932-3ce590607264",
  "sourceToolAssistantUUID": "5ff79a98-5236-4d14-80ce-ea7d2bf11a9b",
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

_source line 34 · 2026-05-16T10:16:49.618Z_

<details><summary>↩ Tool result · `toolu_01TkvH1GmDYpTyLbKLZrPcfm`</summary>

```text
Web search results for query: ""Neural Probe-Based Hallucination Detection" Bayesian optimization probe layer selection arxiv 2512.20949"

Links: [{"title":"[2512.20949] Neural Probe-Based Hallucination Detection for Large Language Models","url":"https://arxiv.org/abs/2512.20949"},{"title":"Neural Probe–Based Hallucination Detection for Large Language Models","url":"https://arxiv.org/html/2512.20949v1"},{"title":"Neural Probe-Based Hallucination Detection for Large ...","url":"https://chatpaper.com/de/paper/221617"},{"title":"[2603.22812v1] Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration","url":"https://arxiv.org/abs/2603.22812v1"},{"title":"Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration","url":"https://arxiv.org/html/2603.22812v1"},{"title":"Hallucination-Associated Neurons in LLMs","url":"https://www.emergentmind.com/topics/hallucination-associated-neurons-h-neurons"},{"title":"[2603.22812] Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration","url":"https://arxiv.org/abs/2603.22812"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"Hallucination Detection on a Budget: Efficient Bayesian Estimation of Semantic Entropy","url":"https://arxiv.org/html/2504.03579"},{"title":"Hallucination Detection with the Internal Layers of LLMs","url":"https://www.arxiv.org/pdf/2509.14254"}]

Based on the search results, I found the paper you're looking for. Here's what arxiv paper 2512.20949 is about:

## Neural Probe-Based Hallucination Detection for Large Language Models

Large language models (LLMs) excel at text generation and knowledge question-answering tasks, but they are prone to generating hallucinated content, severely limiting their application in high-risk domains.

### The Proposed Approach

The paper proposes a neural network-based framework for token-level hallucination detection, where traditional linear probes struggle to capture nonlinear structures in deep semantic spaces. By freezing language model parameters, the framework employs lightweight MLP probes to perform nonlinear modeling of high-level hidden states.

### Key Innovation: Bayesian Optimization for Layer Selection

The paper proposes a distribution-based layer separability metric and a Bayesian optimization-based search to automatically locate optimal probe layers. Additionally, the method uses Bayesian optimization to adaptively locate the optimal probe layer.

### Results

The results on LongFact, HealthBench, and TriviaQA demonstrate that MLP probes significantly outperform state-of-the-art methods in accuracy, recall, and detection capability under low false-positive conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ee38717-c5d1-46b8-b26f-70dca65ef44f",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "4c63c3bb-d289-437d-9260-fc498559a45a",
  "sourceToolAssistantUUID": "6ee38717-c5d1-46b8-b26f-70dca65ef44f",
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

_source line 35 · 2026-05-16T10:16:50.398Z_

<details><summary>↩ Tool result · `toolu_01AHJcj9TW2JgT65JReYA3iP`</summary>

```text
Web search results for query: ""LLM-CAS" dynamic neuron perturbation real-time hallucination correction 2025"

Links: [{"title":"[2512.18623] LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction","url":"https://arxiv.org/abs/2512.18623"},{"title":"LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction","url":"https://arxiv.org/html/2512.18623"},{"title":"LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction","url":"https://ojs.aaai.org/index.php/AAAI/article/download/40776/44737"},{"title":"GitHub - zjunlp/Deco: [ICLR 2025] MLLM can see? Dynamic Correction Decoding for Hallucination Mitigation","url":"https://github.com/zjunlp/Deco"},{"title":"H-Neurons: On the Existence, Impact, and Origin of Hallucination-Associated Neurons in LLMs","url":"https://arxiv.org/html/2512.01797v2"},{"title":"ArXiv Papers Browser - Teng Wang","url":"http://ttengwang.com/arxiv-papers.html"},{"title":"Review Not peer-reviewed version A Survey on Hallucination in Large","url":"https://www.preprints.org/manuscript/202510.0540/v1/download"},{"title":"GitHub - showlab/Awesome-MLLM-Hallucination: 📖 A curated list of resources dedicated to hallucination of multimodal large language models (MLLM).","url":"https://github.com/showlab/Awesome-MLLM-Hallucination"},{"title":"How to evaluate LLM hallucination rates in engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/how-to-evaluate-llm-hallucination-rates-in-engineering/"},{"title":"Mitigating Hallucinations in MLLMs with Attention Causal ...","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_Seeing_Far_and_Clearly_Mitigating_Hallucinations_in_MLLMs_with_Attention_CVPR_2025_paper.pdf"}]

Based on the search results, here's what I found about LLM-CAS:

## LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction

LLM-CAS is a framework submitted on December 21, 2025, that addresses how large language models (LLMs) often generate hallucinated content that lacks factual or contextual grounding.

### Problem and Approach

Existing approaches such as supervised fine-tuning and reinforcement learning from human feedback are data intensive and computationally expensive, while static parameter editing methods struggle with context dependent errors and catastrophic forgetting. 

The framework formulates real-time hallucination correction as a hierarchical reinforcement learning problem. Unlike static parameter editing, LLM-CAS avoids permanent parameter modification altogether, instead performing dynamic and temporary perturbations on neuron activations during inference.

### Technical Framework

LLM-CAS trains an agent to learn a sophisticated policy, dynamically selecting optimal, temporary neuron perturbations during inference based on the immediate context. The novelty of the approach lies in the hierarchical application: a high-level policy selects a macro-level intervention target, while a low-level policy determines the fine-grained perturbation details.

The Adaptive Mask dynamically adjusts both the number and positions of neurons to identify the optimal perturbation strategy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "616339a4-cf23-4b00-8722-56b0e0b4db17",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "7b8267bd-c943-4d08-a19e-15deb50dc7b8",
  "sourceToolAssistantUUID": "616339a4-cf23-4b00-8722-56b0e0b4db17",
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

_source line 36 · 2026-05-16T10:16:53.792Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Z9UjG6z1D3NAZLpyUhza5`</summary>

```json
{
  "query": "\"Geometry of Truth\" layer-wise semantic dynamics hallucination detection arxiv 2510.04933"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b8267bd-c943-4d08-a19e-15deb50dc7b8",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65HxyABvb4APSapeFt1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "425f8736-785f-46a2-8f10-482fa72dcb32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149khKBCcGL45SA2DwtL1hT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3835,
      "cache_read_input_tokens": 21062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3835,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 37 · 2026-05-16T10:16:54.600Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019JeKTjG27g81MuK4Rsyt8C`</summary>

```json
{
  "query": "perturbation hidden state KL divergence confidence calibration LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "425f8736-785f-46a2-8f10-482fa72dcb32",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65HxyABvb4APSapeFt1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcd99fd4-5708-45e2-b5bb-21749311f188",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149khKBCcGL45SA2DwtL1hT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3835,
      "cache_read_input_tokens": 21062,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3835
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 21062,
          "cache_creation_input_tokens": 3835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3835,
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

_source line 38 · 2026-05-16T10:17:00.685Z_

<details><summary>↩ Tool result · `toolu_017Z9UjG6z1D3NAZLpyUhza5`</summary>

```text
Web search results for query: ""Geometry of Truth" layer-wise semantic dynamics hallucination detection arxiv 2510.04933"

Links: [{"title":"[2510.04933] The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2510.04933"},{"title":"The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2510.04933v1"},{"title":"The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251004933H/abstract"},{"title":"[2510.04933v1] The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2510.04933v1"},{"title":"The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection","url":"https://arxiv.org/pdf/2510.04933"},{"title":"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness","url":"https://arxiv.org/html/2601.14210v2"},{"title":"[Literature Review] The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models","url":"https://www.themoonlight.io/en/review/the-geometry-of-truth-layer-wise-semantic-dynamics-for-hallucination-detection-in-large-language-models"},{"title":"aamirhameed (Amir Hameed Mir)","url":"https://huggingface.co/aamirhameed"},{"title":"Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://arxiv.org/html/2502.17598v2"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Layer+of+Truth"}]

Perfect! I found comprehensive information about the paper. Here's a summary of the search results:

## "The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models"

Layer-wise Semantic Dynamics (LSD) is a geometric framework for hallucination detection that analyzes the evolution of hidden-state semantics across transformer layers.

### Key Approach
Unlike prior methods that rely on multiple sampling passes or external verification sources, LSD operates intrinsically within the model's representational space. Using margin-based contrastive learning, LSD aligns hidden activations with ground-truth embeddings derived from a factual encoder, revealing a distinct separation in semantic trajectories: factual responses preserve stable alignment, while hallucinations exhibit pronounced semantic drift across depth.

### Performance Results
Evaluated on the TruthfulQA and synthetic factual-hallucination datasets, LSD achieves an F1-score of 0.92, AUROC of 0.96, and clustering accuracy of 0.89, outperforming SelfCheckGPT and Semantic Entropy baselines while requiring only a single forward pass. This efficiency yields a 5-20x speedup over sampling-based methods without sacrificing precision or interpretability.

### Broader Impact
LSD offers a scalable, model-agnostic mechanism for real-time hallucination monitoring and provides new insights into the geometry of factual consistency within large language models.

The paper was submitted to arXiv on October 6, 2025 (arxiv:2510.04933) by Amir Hameed Mir.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "425f8736-785f-46a2-8f10-482fa72dcb32",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "d83a51c9-96d3-43e7-863c-e69968f1e5ae",
  "sourceToolAssistantUUID": "425f8736-785f-46a2-8f10-482fa72dcb32",
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

_source line 39 · 2026-05-16T10:17:04.536Z_

<details><summary>↩ Tool result · `toolu_019JeKTjG27g81MuK4Rsyt8C`</summary>

```text
Web search results for query: "perturbation hidden state KL divergence confidence calibration LLM 2025 2026"

Links: [{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"CCPS: Calibrating LLM Confidence via Perturbation Stability – EMNLP 2025 | Hacker News","url":"https://news.ycombinator.com/item?id=45055315"},{"title":"Confidence-Guided Probing Methods","url":"https://www.emergentmind.com/topics/confidence-guided-probing-method"},{"title":"Calibrating LLM Confidence by Probing Perturbed ...","url":"https://aclanthology.org/2025.emnlp-main.530.pdf"},{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs | medRxiv","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v3.full"},{"title":"Confidence Calibration in LLMs","url":"https://www.emergentmind.com/topics/confidence-calibration-in-llms"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.10816"}]

Based on the search results, I found several highly relevant recent papers and research developments on this topic. Here's a summary of the key findings:

## Main Research: CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability)

CCPS is a novel method that analyzes internal representational stability in LLMs by applying targeted adversarial perturbations to final hidden states, extracting features reflecting the model's response to these perturbations, and using a lightweight classifier to predict answer correctness.

The underlying premise is that if an LLM is truly confident, its internal decision-making process for a token should be stable against relevant adversarial nudges, and features derived from this internal stability analysis serve as effective proxies for confidence.

## Performance Results

When evaluated on LLMs from 8B to 32B parameters across Llama, Qwen, and Mistral architectures using MMLU and MMLU-Pro benchmarks, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points.

## Key Technical Features

The method derives KL divergence statistics from the original and perturbed representational data. The approach probes LLM hidden states with slight perturbations to check answer stability—where stable implies confidence and unstable implies uncertainty.

## Related Work: PING Framework

Another complementary approach is PING (Probing INternal states of Generative models), a framework that trains lightweight probes on frozen transformers to deliver structured predictions with minimal compute overhead, reducing Expected Calibration Error by up to 96% across diverse models and benchmarks.

These methods represent cutting-edge research in LLM confidence calibration from 2025-2026, with CCPS being formally presented at EMNLP 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcd99fd4-5708-45e2-b5bb-21749311f188",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "7ef08856-73d9-4359-991d-53d087502e0d",
  "sourceToolAssistantUUID": "fcd99fd4-5708-45e2-b5bb-21749311f188",
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

_source line 40 · 2026-05-16T10:17:07.977Z_

This last result is extremely relevant. Let me get more details on the CCPS paper as it appears to be very close to the LSP concept.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ef08856-73d9-4359-991d-53d087502e0d",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65K1T1r8JzbYGwak99R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "752f843c-b9db-4511-a8fb-59599986f5c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjeeGroYdFvyL3PhiFHQbV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2060,
      "cache_read_input_tokens": 24897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2060,
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

_source line 41 · 2026-05-16T10:17:08.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015rwPr79Bj7VcBm19jjC3aC`</summary>

```json
{
  "query": "CCPS \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" method details KL divergence layer perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "752f843c-b9db-4511-a8fb-59599986f5c5",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65K1T1r8JzbYGwak99R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d1ce1e6-d916-4087-8d47-faa60886198d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjeeGroYdFvyL3PhiFHQbV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2060,
      "cache_read_input_tokens": 24897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2060,
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

_source line 42 · 2026-05-16T10:17:09.777Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BmLcoc6awvfsAsDdndhaK9`</summary>

```json
{
  "query": "\"Detecting LLM Hallucination Through Layer-wise\" information deficiency EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d1ce1e6-d916-4087-8d47-faa60886198d",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65K1T1r8JzbYGwak99R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7170779d-ce89-48a0-bdaf-5a37e80bad74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjeeGroYdFvyL3PhiFHQbV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2060,
      "cache_read_input_tokens": 24897,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2060
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 24897,
          "cache_creation_input_tokens": 2060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2060,
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

_source line 43 · 2026-05-16T10:17:16.351Z_

<details><summary>↩ Tool result · `toolu_015rwPr79Bj7VcBm19jjC3aC`</summary>

```text
Web search results for query: "CCPS "Calibrating LLM Confidence by Probing Perturbed Representation Stability" method details KL divergence layer perturbation"

Links: [{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | alphaXiv","url":"https://www.alphaxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250521772K/abstract"},{"title":"[Literature Review] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.themoonlight.io/en/review/calibrating-llm-confidence-by-probing-perturbed-representation-stability"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=LLM+distribution+confidence"},{"title":"CCPS: Calibrating LLM Confidence via Perturbation Stability – EMNLP 2025 | Hacker News","url":"https://news.ycombinator.com/item?id=45055315"}]

## CCPS Method Details

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method that analyzes internal representational stability in LLMs by applying targeted adversarial perturbations to final hidden states, extracting features reflecting the model's response to these perturbations, and using a lightweight classifier to predict answer correctness.

### Core Mechanism

CCPS operates on frozen base LLMs, applying targeted adversarial perturbations to the final hidden states that generate an answer's tokens, then extracting a rich feature set from the LLM's response to these perturbations to train a lightweight classifier that predicts answer correctness, offering a model-agnostic probing approach without modifying the base LLM.

The high-level approach probes LLM hidden states with slight perturbations to check answer stability—stable responses imply confidence while unstable responses imply uncertainty.

### Features and Analysis

The method extracts features that capture original state characteristics, perturbation stability indicators, and trajectory divergence statistics derived from the original and perturbed representational data.

### Evaluation and Results

CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats.

Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points, all relative to the strongest prior method.

The paper was published at EMNLP 2025 and is available on arXiv (2505.21772) with source code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d1ce1e6-d916-4087-8d47-faa60886198d",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "e2de27cf-60b1-40d5-aaa9-4caf83ec4990",
  "sourceToolAssistantUUID": "2d1ce1e6-d916-4087-8d47-faa60886198d",
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

_source line 44 · 2026-05-16T10:17:17.530Z_

<details><summary>↩ Tool result · `toolu_01BmLcoc6awvfsAsDdndhaK9`</summary>

```text
Web search results for query: ""Detecting LLM Hallucination Through Layer-wise" information deficiency EMNLP 2025"

Links: [{"title":"Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1644/"},{"title":"Detecting LLM Hallucination Through Layer-wise ...","url":"https://aclanthology.org/2025.emnlp-main.1644.pdf"},{"title":"[2412.10246v2] Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions","url":"https://arxiv.org/abs/2412.10246v2"},{"title":"Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Unanswerable Questions and Ambiguous Prompts","url":"https://www.researchgate.net/publication/387078638_Detecting_LLM_Hallucination_Through_Layer-wise_Information_Deficiency_Analysis_of_Unanswerable_Questions_and_Ambiguous_Prompts"},{"title":"Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions","url":"https://arxiv.org/html/2412.10246v2"},{"title":"[2412.10246] Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Unanswerable Questions and Ambiguous Prompts","url":"https://arxiv.org/abs/2412.10246"},{"title":"Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Unanswerable Questions and Ambiguous Prompts","url":"https://arxiv.org/html/2412.10246"},{"title":"Re-evaluating Hallucination Detection in LLMs","url":"https://aclanthology.org/2025.emnlp-main.1761.pdf"},{"title":"Hallucination Detection in LLMs Using Spectral Features of ...","url":"https://aclanthology.org/2025.emnlp-main.1239.pdf"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"}]

I found comprehensive information about the paper you're looking for. Here are the key findings:

## Paper Overview

The paper "Detecting LLM Hallucination Through Layer-wise Information Deficiency: Analysis of Ambiguous Prompts and Unanswerable Questions" by Kim, Lamb, Bibi, Torr, and Gal was published at EMNLP 2025 in Suzhou, China.

## Main Contribution

The paper presents a novel, test-time approach to detecting model hallucination through systematic analysis of information flow across model layers, targeting cases when LLMs process inputs with ambiguous or insufficient context.

## Key Findings

The investigation reveals that hallucination manifests as usable information deficiencies in inter-layer transmissions. While existing approaches primarily focus on final-layer output analysis, they demonstrate that tracking cross-layer information dynamics (ℒI) provides robust indicators of model reliability, accounting for both information gain and loss during computation.

## Significance

The approach improves model reliability by immediately integrating with universal LLMs without additional training or architectural modifications.

The paper is available through the ACL Anthology and arXiv, offering both a published version and pre-print formats for access.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7170779d-ce89-48a0-bdaf-5a37e80bad74",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "fb4c0002-6244-4c85-9b6e-05399e03d76e",
  "sourceToolAssistantUUID": "7170779d-ce89-48a0-bdaf-5a37e80bad74",
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

_source line 45 · 2026-05-16T10:17:21.045Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018WHczmfdFNRsT1q5RC967Y`</summary>

```json
{
  "query": "CCPS arxiv 2505.21772 intermediate layer perturbation OR \"final hidden state\" OR \"all layers\" method specifics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb4c0002-6244-4c85-9b6e-05399e03d76e",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65KxzD4nSjJNeftFxxj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b50e389c-d590-4594-8efe-12c53899fd4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwrwYCYQX6jhZe8WgyfjbQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2208,
      "cache_read_input_tokens": 26957,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2208
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 26957,
          "cache_creation_input_tokens": 2208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2208,
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

_source line 46 · 2026-05-16T10:17:28.203Z_

<details><summary>↩ Tool result · `toolu_018WHczmfdFNRsT1q5RC967Y`</summary>

```text
Web search results for query: "CCPS arxiv 2505.21772 intermediate layer perturbation OR "final hidden state" OR "all layers" method specifics"

Links: [{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772"},{"title":"[2505.20789] Integrating Intermediate Layer Optimization and Projected Gradient Descent for Solving Inverse Problems with Diffusion Models","url":"https://arxiv.org/abs/2505.20789"},{"title":"arXiv:2505.05922v2 [cs.CR] 15 May 2025","url":"https://arxiv.org/pdf/2505.05922"},{"title":"Integrating Intermediate Layer Optimization and Projected Gradient Descent for Solving Inverse Problems with Diffusion Models","url":"https://arxiv.org/html/2505.20789v1"},{"title":"Degradation-Aware Feature Perturbation for All-in-One Image Restoration","url":"https://arxiv.org/html/2505.12630v1"},{"title":"iMacHSR: Intermediate Multi-Access Heterogeneous Supervision and Regularization Scheme Toward Architecture-Agnostic Training","url":"https://arxiv.org/html/2505.00404"},{"title":"CAPE: Context-Aware Prompt Perturbation Mechanism with Differential Privacy","url":"https://arxiv.org/html/2505.05922v1"},{"title":"From GNNs to Trees: Multi-Granular Interpretability for Graph Neural Networks","url":"https://arxiv.org/html/2505.00364v1"},{"title":"Matched Asymptotic Expansions-Based Transferable Neural Networks for Singular Perturbation Problems","url":"https://arxiv.org/html/2505.08368v1"}]

Based on the search results, I found detailed information about the CCPS paper (arxiv 2505.21772). Here are the method specifics:

## CCPS Method Overview

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method analyzing internal representational stability in LLMs.

## Key Method Specifics

**Perturbation Target:** CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness.

**Operational Details:** CCPS operates on frozen base LLMs, applying targeted adversarial perturbations to the final hidden states that generate an answer's tokens. From the LLM's response to these perturbations, it extracts a rich feature set and trains a lightweight classifier to predict answer correctness.

## Performance Results

CCPS reduces average ECE by approximately 55% (up to 88%) and Brier score by 21% (up to 45%), while also increasing average Accuracy by 5 percentage points (up to +14 pp), AUCPR by 4 pp (up to +13 pp), and AUROC by 6 pp (up to +17 pp), relative to the best performing baseline.

## Evaluation Scope

CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats.

The paper specifically focuses on perturbations to **final hidden states** rather than intermediate layers, and uses a feature extraction and lightweight classification approach for confidence calibration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b50e389c-d590-4594-8efe-12c53899fd4b",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "ae77757c9de41a3b3",
  "type": "user",
  "uuid": "b8c95191-ef8a-4a4c-ae66-72eb1e0a2951",
  "sourceToolAssistantUUID": "b50e389c-d590-4594-8efe-12c53899fd4b",
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

_source line 47 · 2026-05-16T10:18:14.725Z_

Now I have enough information to provide a comprehensive report. Here is my analysis:

---

## Summary of Findings for "Logit Sensitivity Probing" (LSP) Prior Art Search

### CRITICAL FINDING: Highly Overlapping Work Exists

**The most directly relevant paper to LSP is CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability)** -- published at EMNLP 2025 (arXiv:2505.21772). This paper applies targeted adversarial perturbations to hidden states, measures the model's response stability, extracts KL divergence statistics between original and perturbed representations, and uses a lightweight classifier to predict answer correctness. It reduces ECE by ~55% and Brier score by 21%.

**Key difference from LSP:** CCPS perturbs *final* hidden states only, not intermediate layers. It also uses a trained classifier rather than a direct KL-based scalar score. However, the core intuition (perturbation stability of internal representations as a confidence proxy) is essentially the same.

---

### Papers Closely Related to LSP's Core Method

| Paper | Year/Venue | Overlap with LSP |
|-------|-----------|------------------|
| **CCPS** (arXiv:2505.21772) | EMNLP 2025 | Perturbs hidden states, measures KL divergence for confidence calibration. Final-layer only. **HIGH overlap.** |
| **"Enhancing Hallucination Detection through Noise Injection"** (arXiv:2502.03799) | ICLR 2026 | Perturbs model parameters/hidden activations during sampling to enhance hallucination detection via uncertainty. **HIGH overlap.** |
| **"Shaking to Reveal" (SSP)** (arXiv:2506.02696) | June 2025 | Analyzes perturbation sensitivity at intermediate representations for hallucination detection. Uses contrastive distance metric. **HIGH overlap.** |
| **SHINE** (arXiv:2411.09689) | Nov 2024 | Perturbs key entities in prompts; measures KL divergence of output distributions to classify hallucination types. **MODERATE overlap** (input perturbation, not layer perturbation). |
| **LLM-CAS** (arXiv:2512.18623) | Dec 2025 / AAAI | Dynamic neuron perturbation during inference with adaptive layer/neuron selection for hallucination correction. **MODERATE overlap** (correction not detection, but same mechanism). |
| **Neural Probe-Based** (arXiv:2512.20949) | Dec 2025 | Uses Bayesian optimization for adaptive probe layer selection + KL-divergence constraints. **MODERATE overlap** (probes not perturbation, but adaptive layer selection is shared). |
| **"Geometry of Truth" (LSD)** (arXiv:2510.04933) | Oct 2025 | Layer-wise analysis of representation trajectories for hallucination detection using margin-based contrastive learning. Single forward pass. **MODERATE overlap.** |
| **Layer-wise Information Deficiency** (arXiv:2412.10246) | EMNLP 2025 | Tracks cross-layer information dynamics for hallucination detection. **MODERATE overlap** (layer-wise analysis but different metric). |
| **In-Context Sharpness** (arXiv:2403.01548) | ICML 2024 | Uses entropy of hidden state activations across context as sharpness metric for hallucination. **LOW-MODERATE overlap** (sharpness/entropy, not perturbation-based). |

---

### Specific Questions Answered

**Has anyone combined causal tracing (ROME/Meng et al. 2022) with perturbation-based hallucination detection?**
Yes, partially. Work on causal tracing in VLMs (arXiv:2511.05923) uses Gaussian perturbations and activation restoration to quantify causal effects on hallucination per layer. LLM-CAS also draws on the "locate-then-edit" paradigm from ROME for its dynamic neuron perturbation. However, no paper precisely replicates causal tracing's noise-then-restore methodology purely for hallucination *detection* (vs. correction/mitigation) in text-only LLMs in 2025-2026.

**Is there work from 2025-2026 using adaptive layer selection for perturbation-based methods?**
Yes. The Neural Probe paper (arXiv:2512.20949, Dec 2025) explicitly uses Bayesian optimization to adaptively select optimal probe layers. LLM-CAS uses a hierarchical RL policy for dynamic layer/neuron selection. These are direct precedents for adaptive layer selection.

---

### Paper Verification

**Pan et al., "Optimal Stability of KL Divergence under Gaussian Perturbations" (arXiv:2604.11026):** CONFIRMED to exist. Authors: Jialu Pan, Yufeng Zhang, Nan Hu, Zhenbang Chen, Ji Wang, Keqin Li. It establishes sharp stability bounds for KL divergence under Gaussian perturbations beyond the Gaussian family, proving the sqrt(epsilon) rate is optimal.

**"Aletheia: Quantifying Cognitive Conviction in Reasoning Models" (arXiv:2601.01532):** CONFIRMED to exist. Author: Fanzhe Fu. Submitted January 4, 2026. Uses Tikhonov Regularization to invert a confusion matrix for quantifying "Cognitive Conviction" in reasoning models, with experiments on DeepSeek-R1 and OpenAI o1.

---

### Bottom Line for LSP Novelty

The LSP proposal's core idea -- perturbing intermediate layers and measuring output KL divergence as a hallucination/confidence signal -- has **substantial overlap** with existing 2025-2026 work:

1. **CCPS** does essentially the same thing but only at the final layer. Extending to intermediate layers is incremental.
2. **"Shaking to Reveal" (SSP)** explicitly leverages perturbation sensitivity at intermediate representations for hallucination detection.
3. **"Enhancing Hallucination Detection through Noise Injection" (ICLR 2026)** perturbs hidden activations for hallucination detection.

If LSP's unique contributions are (a) specifically measuring output KL (not just contrastive features) under (b) *intermediate*-layer Gaussian perturbation with (c) adaptive layer selection, then there is a narrow novelty window -- but it requires careful positioning against CCPS (final-layer only), SSP (intermediate but uses contrastive distance not raw output KL), and the Neural Probe paper (adaptive layer selection via Bayesian optimization). The combination of all three elements in one method may still be novel, but each component individually has clear precedent.

Sources:
- [CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability](https://arxiv.org/abs/2505.21772)
- [Enhancing Hallucination Detection through Noise Injection](https://arxiv.org/abs/2502.03799)
- [Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations](https://arxiv.org/abs/2506.02696)
- [SHINE: Probing LLM Hallucination from Within](https://arxiv.org/abs/2411.09689)
- [LLM-CAS: Dynamic Neuron Perturbation for Real-Time Hallucination Correction](https://arxiv.org/abs/2512.18623)
- [Neural Probe-Based Hallucination Detection](https://arxiv.org/abs/2512.20949)
- [The Geometry of Truth: Layer-wise Semantic Dynamics](https://arxiv.org/abs/2510.04933)
- [Detecting LLM Hallucination Through Layer-wise Information Deficiency](https://arxiv.org/abs/2412.10246)
- [In-Context Sharpness as Alerts](https://arxiv.org/abs/2403.01548)
- [Pan et al. - Optimal Stability of KL Divergence under Gaussian Perturbations](https://arxiv.org/abs/2604.11026)
- [Aletheia: Quantifying Cognitive Conviction](https://arxiv.org/abs/2601.01532)
- [Causal Tracing of Object Representations in LVLMs](https://arxiv.org/abs/2511.05923)
- [Detecting Hallucinations via Internal Attention Divergence Signals](https://arxiv.org/abs/2605.05025)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8c95191-ef8a-4a4c-ae66-72eb1e0a2951",
  "isSidechain": true,
  "agentId": "ae77757c9de41a3b3",
  "requestId": "req_011Cb65LkbrSon2ueovEnsEY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecd0a1c1-f350-47a1-b4ca-55dcc59b52fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMqtjzmdtkH3uT5BwRbtSA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1028,
      "cache_read_input_tokens": 29165,
      "output_tokens": 2107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1028
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2107,
          "cache_read_input_tokens": 29165,
          "cache_creation_input_tokens": 1028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1028,
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
