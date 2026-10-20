# Research conversation: Search for the paper "Decompose-and-Formalise" at arXiv 2601.19605. This paper claims to achieve significant improvement

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-afeacd7b847f42f2b.jsonl`
- **Structured JSON:** [`f700e8cbd40a103adb9d.json`](../../sessions/f7/f700e8cbd40a103adb9d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-10T20:33:35.068Z_

Search for the paper "Decompose-and-Formalise" at arXiv 2601.19605. This paper claims to achieve significant improvements on FOLIO (26.2%), ProofWriter (21.7%), and PrOntoQA (21.6%) using theorem prover with local diagnostic-guided refinement.

I need to verify:
1. Does this paper exist?
2. What exactly is the method (entailment trees + theorem prover)?
3. Is the metric "verification rate" or "accuracy" - this matters for comparison with CEDAR
4. Does it use counterexample-guided refinement or just proof error messages?
5. Was it accepted at a venue or just on arXiv?

Search queries:
- "Decompose-and-Formalise recursively verifiable natural language inference arXiv 2601.19605"
- "LLM-TP Tree entailment tree FOLIO ProofWriter 2026"

Use WebFetch to read the abstract if available. Report all details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b6d39c90-30ec-4ab8-b5f9-152931227585",
  "agentId": "afeacd7b847f42f2b",
  "type": "user",
  "uuid": "758b4398-49fb-45f5-b73c-d29c6f2b3adf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T20:33:36.208Z_

I'll search for this paper and verify the details you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "758b4398-49fb-45f5-b73c-d29c6f2b3adf",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXUFAFv7imdcQnfN6Yr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9def2197-4488-4657-a12c-15365b52a44b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011EG7vHs6nrJ18f6QTt5hnv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T20:33:36.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UchAn7y76RD9k6vBCvSesV`</summary>

```json
{
  "query": "Decompose-and-Formalise recursively verifiable natural language inference arXiv 2601.19605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9def2197-4488-4657-a12c-15365b52a44b",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXUFAFv7imdcQnfN6Yr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4a78d48c-51d7-49eb-bba7-ebc81c727bb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011EG7vHs6nrJ18f6QTt5hnv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 662,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T20:33:36.523Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q16xA9iEHti1gXwVvBv46n`</summary>

```json
{
  "query": "LLM-TP Tree entailment tree FOLIO ProofWriter 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a78d48c-51d7-49eb-bba7-ebc81c727bb8",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXUFAFv7imdcQnfN6Yr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "32c20fb7-480e-4bd3-b32d-4da3a703c8d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011EG7vHs6nrJ18f6QTt5hnv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 13789,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 662
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 145,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 662,
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

_source line 5 · 2026-05-10T20:33:42.895Z_

<details><summary>↩ Tool result · `toolu_01Q16xA9iEHti1gXwVvBv46n`</summary>

```text
Web search results for query: "LLM-TP Tree entailment tree FOLIO ProofWriter 2026"

Links: [{"title":"Decompose-and-Formalise: Recursively Verifiable Natural Language Inference","url":"https://arxiv.org/html/2601.19605"},{"title":"Stress-Testing the Reasoning Competence of LLMs with Proofs ...","url":"https://www.preprints.org/frontend/manuscript/c9deae48143449624cf5325db41bbbe0/download_pub"},{"title":"Published as a conference paper at ICLR 2025 LARGE LANGUAGE MODELS MEET","url":"https://arxiv.org/pdf/2502.06563"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=kpT5rbbLdY"},{"title":"Efficient Translation of NL-based Logical Problems to FOL ...","url":"https://arxiv.org/pdf/2506.18383"},{"title":"FoVer: First-Order Logic Verification for Natural Language Reasoning | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.41/133797/FoVer-First-Order-Logic-Verification-for-Natural"},{"title":"GitHub - Mooler0410/LLMsPracticalGuide: A curated list of practical guide resources of LLMs (LLMs Tree, Examples, Papers) · GitHub","url":"https://github.com/Mooler0410/LLMsPracticalGuide"},{"title":"When Reasoning Collapses: A Depth-Aware Probe into LLM Reasoning (Student Abstract) | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/42223"},{"title":"GitHub - teacherpeterpan/Logic-LLM: The project page for \"LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\" · GitHub","url":"https://github.com/teacherpeterpan/Logic-LLM"},{"title":"Strategies for Improving NL-to-FOL Translation with LLMs:","url":"https://arxiv.org/pdf/2409.16461"}]

Based on the web search results, I found relevant information about your query. Here's what I discovered:

LLM-TP Tree is an approach that achieves strong refinement performance on FOLIO, ProofWriter, PrOntoQA, and EntailmentBank datasets, improving the average verification rate significantly. The method works by repeating a process bottom-up to yield a recursively verifiable proof certificate for the entire entailment tree.

LLM-TP Tree shows absolute performance gains over baseline approaches on these logical reasoning tasks. On synthetic benchmarks such as ProofWriter and PrOntoQA, LLM-TP Tree yields substantially higher initial validity than alternative refiners; for instance, on ProofWriter with Qwen3-max, LLM-TP Tree attains 92.00% initial validity.

The neuro-symbolic framework is evaluated from two complementary perspectives: (i) explanation refinement applying theorem-prover checking and refinement, and (ii) logical reasoning, which measures standard end-task accuracy to ensure that enhanced verification and refinement do not come at the cost of predictive performance.

The research indicates this is a recent development from 2026, focusing on improving the logical validity and refinement of explanations across multiple important logical reasoning datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32c20fb7-480e-4bd3-b32d-4da3a703c8d9",
  "isSidechain": true,
  "promptId": "b6d39c90-30ec-4ab8-b5f9-152931227585",
  "agentId": "afeacd7b847f42f2b",
  "type": "user",
  "uuid": "f9ed24e3-5f47-4b58-bb0a-1e0d9b70d662",
  "sourceToolAssistantUUID": "32c20fb7-480e-4bd3-b32d-4da3a703c8d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-10T20:33:43.415Z_

<details><summary>↩ Tool result · `toolu_01UchAn7y76RD9k6vBCvSesV`</summary>

```text
Web search results for query: "Decompose-and-Formalise recursively verifiable natural language inference arXiv 2601.19605"

Links: [{"title":"[2601.19605] Decompose-and-Formalise: Recursively Verifiable Natural Language Inference","url":"https://arxiv.org/abs/2601.19605"},{"title":"Decompose-and-Formalise: Recursively Verifiable Natural Language Inference","url":"https://arxiv.org/html/2601.19605"},{"title":"[2601.05705] Logic-Parametric Neuro-Symbolic NLI: Controlling Logical Formalisms for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.05705"},{"title":"Recursive Language Models","url":"https://arxiv.org/html/2512.24601v2"},{"title":"Enhancing Systematic Decompositional Natural Language Inference Using Informal Logic","url":"https://arxiv.org/html/2402.14798v1"},{"title":"[2512.24601] Recursive Language Models","url":"https://arxiv.org/abs/2512.24601"},{"title":"Modeling Next-Token Prediction as Left-Nested Intuitionistic Implication","url":"https://arxiv.org/html/2601.19915"},{"title":"Logic-Parametric Neuro-Symbolic NLI: Controlling Logical Formalisms for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.05705"},{"title":"Recursive Language Models | Alex L. Zhang","url":"https://alexzhang13.github.io/blog/2025/rlm/"},{"title":"Nathaniel Weir | PhD Student at Johns Hopkins University","url":"https://nweir127.github.io/"}]

I found the paper! Here's information about it:

## Paper Summary

The paper "Decompose-and-Formalise: Recursively Verifiable Natural Language Inference" by Xin Quan, Marco Valentino, Louise A. Dennis, and André Freitas integrates large language models (LLMs) with theorem provers (TPs) in neuro-symbolic pipelines to help with entailment verification and proof-guided refinement of explanations for natural language inference (NLI).

## Key Problem Addressed

The paper addresses the difficulty of scaling refinement to naturalistic NLI: long, syntactically rich inputs and deep multi-step arguments amplify autoformalisation errors, and current methods often handle failures via costly global regeneration due to the difficulty of localising the responsible span or step from prover diagnostics.

## Main Approach

The proposed decompose-and-formalise framework (i) decomposes premise-hypothesis pairs into an entailment tree of atomic steps, (ii) verifies the tree bottom-up to isolate failures to specific nodes, and (iii) performs local diagnostic-guided refinement instead of regenerating the whole explanation.

## Results

Experiments on four datasets with multiple LLM backbones show improved TP-verified explanation rates, more faithful autoformalisation, and reduced refinement drift while maintaining strong end-task reasoning accuracy.

The paper was published on January 27, 2026, and is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a78d48c-51d7-49eb-bba7-ebc81c727bb8",
  "isSidechain": true,
  "promptId": "b6d39c90-30ec-4ab8-b5f9-152931227585",
  "agentId": "afeacd7b847f42f2b",
  "type": "user",
  "uuid": "405e8dea-d739-49e1-a76f-aef74ce72cd8",
  "sourceToolAssistantUUID": "4a78d48c-51d7-49eb-bba7-ebc81c727bb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-10T20:33:45.469Z_

Now let me fetch the actual paper to get the precise details you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "405e8dea-d739-49e1-a76f-aef74ce72cd8",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXUsej1K6MSkPwGQxVM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "836d01c7-dc7e-45be-911d-a35123b44590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EmTSP3YsNMjuZvL6eC2k7d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 928,
      "cache_creation_input_tokens": 1769,
      "cache_read_input_tokens": 14451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1769,
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

_source line 8 · 2026-05-10T20:33:46.322Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ChnpAMnyFVp2mtAMyLdT8R`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.19605",
  "prompt": "What are the exact metrics and improvements on FOLIO ProofWriter PrOntoQA? Is it verification rate or accuracy? Does it use counterexample-guided refinement or diagnostic messages? What refinement method is used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "836d01c7-dc7e-45be-911d-a35123b44590",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXUsej1K6MSkPwGQxVM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d4168f5b-5b42-43af-99ab-b0c77f74214e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EmTSP3YsNMjuZvL6eC2k7d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 928,
      "cache_creation_input_tokens": 1769,
      "cache_read_input_tokens": 14451,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1769
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 928,
          "output_tokens": 147,
          "cache_read_input_tokens": 14451,
          "cache_creation_input_tokens": 1769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1769,
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

_source line 9 · 2026-05-10T20:33:50.595Z_

<details><summary>↩ Tool result · `toolu_01ChnpAMnyFVp2mtAMyLdT8R`</summary>

```text
# Analysis of Paper Metrics and Methods

Based on the abstract provided, I can share the following:

**Metrics and Improvements:**
The paper reports "explanation verification rates" as the primary metric, achieving improvements of "26.2%, 21.7%, 21.6% and 48.9%" over prior work across different datasets. The abstract does not specify which percentages correspond to FOLIO, ProofWriter, or PrOntoQA individually.

**Refinement Approach:**
The method uses "local diagnostic-guided refinement" rather than regenerating entire explanations. The abstract specifically states the framework "performs local diagnostic-guided refinement instead of regenerating the whole explanation," indicating it leverages diagnostic information from the theorem prover rather than counterexample-guided approaches.

**Key Technical Innovation:**
The paper introduces "θ-substitution in an event-based logical form to enforce consistent argument-role bindings" to improve the faithfulness of automatic formalization—the core technical contribution beyond the decomposition strategy.

Unfortunately, the abstract does not provide task-specific breakdowns of which improvements apply to which benchmark datasets, nor does it distinguish between verification rates and accuracy metrics for individual tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4168f5b-5b42-43af-99ab-b0c77f74214e",
  "isSidechain": true,
  "promptId": "b6d39c90-30ec-4ab8-b5f9-152931227585",
  "agentId": "afeacd7b847f42f2b",
  "type": "user",
  "uuid": "0390e707-7201-49b6-a79e-ddc96d4dab1c",
  "sourceToolAssistantUUID": "d4168f5b-5b42-43af-99ab-b0c77f74214e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-10T20:33:51.792Z_

Let me fetch the full HTML version to get more detailed results breakdown.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0390e707-7201-49b6-a79e-ddc96d4dab1c",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXVPZ4XAVHBrDLZHufb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f31e128b-a511-40ec-9262-bbf458aa5ff7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JNvPFjG2iWRHGAMsiTwa7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 16220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1339,
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

_source line 11 · 2026-05-10T20:33:52.368Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BU6NSFTwF7HHhCzsgt5XyA`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.19605",
  "prompt": "Show me the results table with FOLIO ProofWriter PrOntoQA metrics. What are the exact numbers and is it verification rate or accuracy? What are the baseline comparisons?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f31e128b-a511-40ec-9262-bbf458aa5ff7",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXVPZ4XAVHBrDLZHufb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "24dc4e7f-1e88-41de-9677-e745a0249c5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JNvPFjG2iWRHGAMsiTwa7e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 16220,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1339
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 137,
          "cache_read_input_tokens": 16220,
          "cache_creation_input_tokens": 1339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1339,
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

_source line 12 · 2026-05-10T20:33:58.039Z_

<details><summary>↩ Tool result · `toolu_01BU6NSFTwF7HHhCzsgt5XyA`</summary>

```text
# Results Table Summary

## Main Performance Metrics (Table 1)

The paper presents **explanation refinement verification rates** (not standard accuracy) across four datasets:

### FOLIO Results
- **LLM-TP Tree final rates**: 90.16% to 95.08% (depending on LLM backbone)
- **Baseline comparison**: Explanation-Refiner achieved 53.28-68.85%, Faithful-Refiner reached 68.03-84.43%
- **Improvement**: "+26.23 percentage points" over the baseline refiner

### ProofWriter Results
- **LLM-TP Tree final rates**: 91.33% to 98.00%
- **Baseline comparison**: Explanation-Refiner ranged 52.46-78.00%, Faithful-Refiner 65.57-91.33%
- **Improvement**: "+18.66 to +31.33 percentage points"

### PrOntoQA Results
- **LLM-TP Tree final rates**: 91.33% to 100.00%
- **Baseline comparison**: Explanation-Refiner 73.33-78.67%, Faithful-Refiner 80.00-91.33%
- **Improvement**: "+18.66 to +23.33 percentage points"

## Key Distinction

These metrics measure "logically valid" explanations after refinement—meaning they can be verified by an automated theorem prover—rather than traditional task accuracy measures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24dc4e7f-1e88-41de-9677-e745a0249c5c",
  "isSidechain": true,
  "promptId": "b6d39c90-30ec-4ab8-b5f9-152931227585",
  "agentId": "afeacd7b847f42f2b",
  "type": "user",
  "uuid": "4d984c3a-771f-4804-84d9-2b3dd4491d7d",
  "sourceToolAssistantUUID": "24dc4e7f-1e88-41de-9677-e745a0249c5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T20:33:59.134Z_

Perfect! Now let me verify the venue status and get any additional publication details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d984c3a-771f-4804-84d9-2b3dd4491d7d",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXVwLkonFEmQkFBfrQg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea9963da-3371-404c-8a84-1885351ba804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JxcuRr7Z54Cpk5GPAQEbGi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 497,
      "cache_read_input_tokens": 17559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 497,
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

_source line 14 · 2026-05-10T20:33:59.471Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013q2Anhdd28Yr4FJvXCg9US`</summary>

```json
{
  "query": "\"Decompose-and-Formalise\" 2601.19605 ICLR ACL conference accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea9963da-3371-404c-8a84-1885351ba804",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXVwLkonFEmQkFBfrQg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9cdfcc0b-70e5-4c01-bff5-99e0fc96bb08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JxcuRr7Z54Cpk5GPAQEbGi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 497,
      "cache_read_input_tokens": 17559,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 497
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 95,
          "cache_read_input_tokens": 17559,
          "cache_creation_input_tokens": 497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 497,
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

_source line 15 · 2026-05-10T20:34:03.433Z_

<details><summary>↩ Tool result · `toolu_013q2Anhdd28Yr4FJvXCg9US`</summary>

```text
Web search results for query: ""Decompose-and-Formalise" 2601.19605 ICLR ACL conference accepted"

Links: [{"title":"Decompose-and-Formalise: Recursively Verifiable Natural Language Inference","url":"https://arxiv.org/html/2601.19605"},{"title":"Frequently Asked Questions - ACL 2023","url":"https://2023.aclweb.org/faq/"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"Main Conference Papers - acl-ijcnlp 2021","url":"https://2021.aclweb.org/calls/papers/"},{"title":"ICLR Proceedings","url":"https://iclr.cc/FAQ/Proceedings"},{"title":"The 19th Conference of the European Chapter of the Association for Computational LinguisticsRabat, MoroccoMarch 24-29, 2026 -","url":"https://2026.eacl.org/"},{"title":"Beyond NeurIPS: A Student's Guide to ICML, ICLR, AAAI, and Other AI Conferences | Algoverse AI Research","url":"https://algoverseairesearch.org/blog/icml-iclr-aaai-student-guide"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"1st International Conference on Learning Representations (ICLR 2013): Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/1st-international-conference-learning-representations-iclr-2013-call-papers"}]

Based on the search results, I found information about the paper:

"Decompose-and-Formalise: Recursively Verifiable Natural Language Inference" (arxiv 2601.19605) is a paper that proposes a decompose-and-formalise framework integrating LLMs with theorem provers to address challenges in natural language inference by decomposing premise-hypothesis pairs into entailment trees and verifying them bottom-up to isolate failures.

However, the search results do not contain specific information about whether this paper has been accepted to ICLR or ACL conferences. The arxiv page shows the paper was posted on January 27, 2026, but acceptance status to these conferences is not indicated in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cdfcc0b-70e5-4c01-bff5-99e0fc96bb08",
  "isSidechain": true,
  "promptId": "b6d39c90-30ec-4ab8-b5f9-152931227585",
  "agentId": "afeacd7b847f42f2b",
  "type": "user",
  "uuid": "f4b08de2-a3ae-403f-af89-c74f275a3b15",
  "sourceToolAssistantUUID": "9cdfcc0b-70e5-4c01-bff5-99e0fc96bb08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T20:34:04.957Z_

Let me do one more specific search to check venue acceptance status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4b08de2-a3ae-403f-af89-c74f275a3b15",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXWLVXxM1LzvG8MUV9P",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8c0af940-c7df-4b2c-8165-4fee637ec7eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RGvPeKLV6CmiwXk7NuJtWt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 18056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 760,
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

_source line 17 · 2026-05-10T20:34:05.249Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QcdMZcveKxrWYwgCdUxnT2`</summary>

```json
{
  "query": "Xin Quan Marco Valentino \"Decompose-and-Formalise\" venue conference 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c0af940-c7df-4b2c-8165-4fee637ec7eb",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXWLVXxM1LzvG8MUV9P",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3feb80c3-c8f3-4a83-acb6-2dfefd89cdcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RGvPeKLV6CmiwXk7NuJtWt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 18056,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 760
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 18056,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 760,
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

_source line 18 · 2026-05-10T20:34:10.391Z_

<details><summary>↩ Tool result · `toolu_01QcdMZcveKxrWYwgCdUxnT2`</summary>

```text
Web search results for query: "Xin Quan Marco Valentino "Decompose-and-Formalise" venue conference 2026"

Links: [{"title":"[2601.19605] Decompose-and-Formalise: Recursively Verifiable Natural Language Inference","url":"https://arxiv.org/abs/2601.19605"},{"title":"Venue Windsor Convention Center and Hotels - FormaliSE 2026","url":"https://2026.formalise.org/venue/icse-2026-venue"},{"title":"FormaliSE 2026 - Research Track - FormaliSE 2026","url":"https://2026.formalise.org/"},{"title":"[PDF] Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Verification-and-Refinement-of-Natural-Language-Quan-Valentino/6fede93e6b6388a0f4d766a3adf22367e751de93"},{"title":"Faithful and Robust LLM-Driven Theorem Proving for NLI Explanations - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.867/"},{"title":"Catering and Exhibition Hall (Europa I to IV) - FormaliSE 2026","url":"https://2026.formalise.org/room/icse-2026-venue-catering-and-exhibition-hall-(europa-i-to-iv)"},{"title":"Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.172/"},{"title":"[PDF] PEIRCE: Unifying Material and Formal Reasoning via LLM-Driven Neuro-Symbolic Refinement | Semantic Scholar","url":"https://www.semanticscholar.org/paper/PEIRCE:-Unifying-Material-and-Formal-Reasoning-via-Quan-Valentino/4c2e65d3f55297e6f9e383c8876aac72e1a50fe0"},{"title":"Equity, Diversity, and Inclusion Plan for ICSE 2026 - FormaliSE 2026","url":"https://2026.formalise.org/attending/Diversity+and+Inclusion+Plan"},{"title":"Conference in Venice 2025-2026","url":"https://conferenceineurope.net/cities/venice"}]

Based on the search results, I found information about the "Decompose-and-Formalise" paper by Xin Quan and Marco Valentino:

The paper "Decompose-and-Formalise: Recursively Verifiable Natural Language Inference" by Xin Quan and Marco Valentino was submitted on January 27, 2026, and it appears on arXiv (paper 2601.19605).

Regarding the venue and conference for 2026, the search results show that the 14th edition of FormaliSE will take place as a co-located conference of ICSE 2026, and ICSE 2026, including all its co-located conferences and workshops, will be held at the Windsor Oceanico Hotel in Rio de Janeiro, Brazil.

However, the search results do not explicitly confirm whether the "Decompose-and-Formalise" paper will be presented specifically at FormaliSE 2026 or at another 2026 conference venue. The paper appears to be a recent preprint on arXiv, but its official conference publication venue has not been clearly identified in these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3feb80c3-c8f3-4a83-acb6-2dfefd89cdcb",
  "isSidechain": true,
  "promptId": "b6d39c90-30ec-4ab8-b5f9-152931227585",
  "agentId": "afeacd7b847f42f2b",
  "type": "user",
  "uuid": "04cfaf7d-99ec-4f73-9ee6-e8cb0948a639",
  "sourceToolAssistantUUID": "3feb80c3-c8f3-4a83-acb6-2dfefd89cdcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T20:34:11.867Z_

Let me check the arXiv page directly for any "Published at" or "Accepted at" indicators.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04cfaf7d-99ec-4f73-9ee6-e8cb0948a639",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXWrCDhvrzDUN8QSTkq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "55cd6cb4-36b3-4663-a44f-fa01472ad789",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AhL4Snng1Npe6brSyTjkJN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1018,
      "cache_read_input_tokens": 18816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1018,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T20:34:12.445Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HbEACVCQ1u5mVarwkmxMJL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.19605",
  "prompt": "Is there any indication this paper was accepted or published at a conference? What does it say about submission status, venue acceptance, or publication status?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55cd6cb4-36b3-4663-a44f-fa01472ad789",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXWrCDhvrzDUN8QSTkq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de69d09a-4770-446b-ab53-c3e1b3fcab30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AhL4Snng1Npe6brSyTjkJN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1018,
      "cache_read_input_tokens": 18816,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1018
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 135,
          "cache_read_input_tokens": 18816,
          "cache_creation_input_tokens": 1018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1018,
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

_source line 21 · 2026-05-10T20:34:14.490Z_

<details><summary>↩ Tool result · `toolu_01HbEACVCQ1u5mVarwkmxMJL`</summary>

```text
Based on the web page content provided, there is **no indication that this paper has been accepted or published at a conference**.

The submission history shows only: "**\[v1\]** Tue, 27 Jan 2026 13:43:30 UTC (900 KB)" — indicating this is version 1, submitted on January 27, 2026. The page describes it as a preprint on arXiv with the status "Submitted" but contains no mention of conference acceptance, publication venue, or peer review completion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de69d09a-4770-446b-ab53-c3e1b3fcab30",
  "isSidechain": true,
  "promptId": "b6d39c90-30ec-4ab8-b5f9-152931227585",
  "agentId": "afeacd7b847f42f2b",
  "type": "user",
  "uuid": "5ba3b12c-514c-44d7-b9e4-c4f3c26c2b63",
  "sourceToolAssistantUUID": "de69d09a-4770-446b-ab53-c3e1b3fcab30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T20:34:24.711Z_

Perfect! Now I have all the information you need. Let me compile the complete verification report.

## Verification Report: "Decompose-and-Formalise" (arXiv 2601.19605)

### 1. **Paper Existence: CONFIRMED ✓**
The paper exists and is available on arXiv as paper 2601.19605, submitted January 27, 2026.
- Direct link: https://arxiv.org/abs/2601.19605
- HTML version: https://arxiv.org/html/2601.19605

### 2. **Method Details: ENTAILMENT TREE + THEOREM PROVER ✓**
The approach is confirmed to work as described:
- **Decomposition**: Breaks down premise-hypothesis pairs into **entailment trees** of atomic steps
- **Verification**: Verifies the tree **bottom-up** to isolate failures to specific nodes
- **Refinement**: Performs **local diagnostic-guided refinement** on isolated nodes rather than regenerating entire explanations
- **Technical innovation**: Uses θ-substitution in event-based logical form to enforce consistent argument-role bindings for faithful formalization

### 3. **Metric Clarity: VERIFICATION RATE (not accuracy) ✓**
This is critical for CEDAR comparison:
- **Metric used**: **Explanation verification rates** (the percentage of explanations that pass theorem prover validation)
- This is NOT the same as standard task accuracy
- It measures whether generated explanations are logically valid per an automated theorem prover

### 4. **Refinement Approach: DIAGNOSTIC-GUIDED (not counterexample-guided) ✓**
- Uses **diagnostic messages from the theorem prover** to guide refinement
- Explicitly states: "performs local diagnostic-guided refinement instead of regenerating the whole explanation"
- Not counterexample-guided refinement

### 5. **Venue Status: ARXIV PREPRINT ONLY (not yet accepted)**
- **Status**: This is a preprint submission only
- **No conference acceptance**: There is no indication of acceptance at ICLR, ACL, EMNLP, or any other venue
- **Submitted**: January 27, 2026 (version 1, only version on arXiv)
- Only appears on arXiv, not in any conference proceedings

---

## Results Breakdown

The improvements you mentioned are **explanation verification rates**:

| Dataset | LLM-TP Tree Performance | Baseline | Improvement |
|---------|------------------------|----------|-------------|
| **FOLIO** | 90.16-95.08% | 53.28-84.43% | **+26.23 pp** |
| **ProofWriter** | 91.33-98.00% | 52.46-91.33% | +18.66 to +31.33 pp |
| **PrOntoQA** | 91.33-100.00% | 73.33-91.33% | +18.66 to +23.33 pp |

**Important**: These are verification rates (logically valid explanations per theorem prover), not task accuracy metrics.

---

## Key Distinction for CEDAR Comparison

If CEDAR reports accuracy on end-task reasoning performance, these metrics are **not directly comparable** because Decompose-and-Formalise primarily measures explanation validity after refinement, not end-task performance. The paper separately reports end-task accuracy to show refinement doesn't harm prediction, but the main results focus on verification rates.

**Sources:**
- [Decompose-and-Formalise arXiv Abstract](https://arxiv.org/abs/2601.19605)
- [Decompose-and-Formalise arXiv HTML](https://arxiv.org/html/2601.19605)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ba3b12c-514c-44d7-b9e4-c4f3c26c2b63",
  "isSidechain": true,
  "agentId": "afeacd7b847f42f2b",
  "requestId": "req_011CauXX9pcepcw4XYudDCi2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7577b5f9-f357-4331-b22b-1b59b74a447c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44d302-1ae6-47b5-ab4f-02bc5824aae9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WVhUwQbmxxU2hvAXcAoeUX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 264,
      "cache_read_input_tokens": 19834,
      "output_tokens": 892,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 264
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 892,
          "cache_read_input_tokens": 19834,
          "cache_creation_input_tokens": 264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 264,
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
