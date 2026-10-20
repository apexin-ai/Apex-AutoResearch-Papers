# Research conversation: Search for whether "compute-normalized comparison" or "compute-matched baseline" is a standard practice in RAG defense p

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7d20c786d7950b63.jsonl`
- **Structured JSON:** [`97687f8417e96ecae754.json`](../../sessions/97/97687f8417e96ecae754.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-30T07:20:47.420Z_

Search for whether "compute-normalized comparison" or "compute-matched baseline" is a standard practice in RAG defense papers. Specifically, search for "self-consistency voting conformal prediction" and "compute-normalized RAG defense evaluation" to verify the 补救 agent's suggestion that giving TRAQ the same K× compute budget (e.g., via self-consistency sampling) is a valid and necessary baseline. Report in under 150 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c76aef35-f9e0-437d-8b89-5335014d3c7a",
  "agentId": "a7d20c786d7950b63",
  "type": "user",
  "uuid": "ad98ca76-8d50-4f40-b42c-1ed32713bfb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T07:20:47.423Z_

```json
{
  "parentUuid": "ad98ca76-8d50-4f40-b42c-1ed32713bfb7",
  "isSidechain": true,
  "agentId": "a7d20c786d7950b63",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7c9efba7-8f1a-4d41-899d-60acc4e34b91",
  "timestamp": "2026-05-30T07:20:47.423Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-30T07:20:48.974Z_

I'll search for these specific terms and concepts in the literature to verify the validity of these RAG defense evaluation practices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c9efba7-8f1a-4d41-899d-60acc4e34b91",
  "isSidechain": true,
  "agentId": "a7d20c786d7950b63",
  "requestId": "req_011CbYMC9DbjkvkH2Xowc2oa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "26f99482-b1cd-4d65-b39a-923df1e76cc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017EHWAC44fuY7cCgQFZ2xw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 15435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1312,
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

_source line 4 · 2026-05-30T07:20:49.196Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019CCCHWZeU6Ljx7G1s8tMNe`</summary>

```json
{
  "query": "self-consistency voting conformal prediction RAG"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26f99482-b1cd-4d65-b39a-923df1e76cc8",
  "isSidechain": true,
  "agentId": "a7d20c786d7950b63",
  "requestId": "req_011CbYMC9DbjkvkH2Xowc2oa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b40d800b-128b-43bd-ae63-ec2d8b654a13",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017EHWAC44fuY7cCgQFZ2xw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 15435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1312,
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

_source line 5 · 2026-05-30T07:20:49.408Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lhy7wykb8P2YmpySZnZ4fK`</summary>

```json
{
  "query": "compute-normalized RAG defense evaluation baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b40d800b-128b-43bd-ae63-ec2d8b654a13",
  "isSidechain": true,
  "agentId": "a7d20c786d7950b63",
  "requestId": "req_011CbYMC9DbjkvkH2Xowc2oa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "901f309e-7991-4097-a7b7-ab8da0632ba5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017EHWAC44fuY7cCgQFZ2xw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 15435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1312,
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

_source line 6 · 2026-05-30T07:20:49.561Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wa8dqbHZcYALCP4g8XfhPT`</summary>

```json
{
  "query": "RAG adversarial defense equal compute budget comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "901f309e-7991-4097-a7b7-ab8da0632ba5",
  "isSidechain": true,
  "agentId": "a7d20c786d7950b63",
  "requestId": "req_011CbYMC9DbjkvkH2Xowc2oa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "894ca04a-4e20-45c5-9c0e-efee9e788710",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017EHWAC44fuY7cCgQFZ2xw9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 15435,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1312
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 15435,
          "cache_creation_input_tokens": 1312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1312,
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

_source line 7 · 2026-05-30T07:20:55.696Z_

<details><summary>↩ Tool result · `toolu_019CCCHWZeU6Ljx7G1s8tMNe`</summary>

```text
Web search results for query: "self-consistency voting conformal prediction RAG"

Links: [{"title":"Self-Consistent Conformal Prediction | Alaa Lab","url":"https://alaalab.berkeley.edu/publications/self-consistent-conformal-prediction"},{"title":"[2511.17908] Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/abs/2511.17908"},{"title":"(PDF) Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://www.researchgate.net/publication/397932907_Principled_Context_Engineering_for_RAG_Statistical_Guarantees_via_Conformal_Prediction"},{"title":"CONFLARE: CONFormal LArge language model REtrieval","url":"https://arxiv.org/pdf/2404.04287"},{"title":"Principled Context Engineering for RAG:","url":"https://www.arxiv.org/pdf/2511.17908"},{"title":"Conformal Prediction: A Data Perspective","url":"https://arxiv.org/pdf/2410.06494"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/html/2511.17908v1"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"}]

Based on the web search results, here's what I found about self-consistency voting, conformal prediction, and RAG:

## Self-Consistent Conformal Prediction

Self-consistent conformal prediction yields both Venn-Abers calibrated predictions and conformal prediction intervals that are valid conditional on actions prompted by model predictions.

## Conformal Prediction in RAG

Several recent approaches combine conformal prediction with Retrieval-Augmented Generation (RAG):

**Context Engineering**: Conformal prediction is a coverage-controlled filtering framework that removes irrelevant content while preserving recall of supporting evidence. Conformal filtering consistently meets its target coverage, ensuring that a specified fraction of relevant snippets are retained, and reduces retained context by 2-3x relative to unfiltered retrieval.

**Retrieval Uncertainty**: A four-step framework applies conformal prediction to quantify retrieval uncertainty in RAG frameworks. All chunks with similarity exceeding a threshold are retrieved to provide context to the LLM, ensuring the true answer is captured in the context with a (1-α) confidence level.

**Trustworthy QA**: TRAQ uses conformal prediction, an uncertainty quantification technique that modifies the underlying model to predict sets of outputs rather than a single output.

These approaches leverage conformal prediction's statistical guarantees to make RAG systems more reliable and trustworthy by controlling uncertainty and filtering irrelevant retrieval results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b40d800b-128b-43bd-ae63-ec2d8b654a13",
  "isSidechain": true,
  "promptId": "c76aef35-f9e0-437d-8b89-5335014d3c7a",
  "agentId": "a7d20c786d7950b63",
  "type": "user",
  "uuid": "ed57b1ab-0235-4719-b68a-a76075caf6a8",
  "sourceToolAssistantUUID": "b40d800b-128b-43bd-ae63-ec2d8b654a13",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-30T07:20:56.120Z_

<details><summary>↩ Tool result · `toolu_01Wa8dqbHZcYALCP4g8XfhPT`</summary>

```text
Web search results for query: "RAG adversarial defense equal compute budget comparison"

Links: [{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks","url":"https://arxiv.org/pdf/2511.01268"},{"title":"Don’t Lag, RAG: Training-Free Adversarial Detection Using RAG","url":"https://openreview.net/pdf?id=4iwG0Xf3O8"},{"title":"Certified Defenses for RAG Systems","url":"https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"},{"title":"(PDF) Adaptive Defense Orchestration for RAG: A Sentinel-Strategist Architecture against Multi-Vector Attacks","url":"https://www.researchgate.net/publication/404143471_Adaptive_Defense_Orchestration_for_RAG_A_Sentinel-Strategist_Architecture_against_Multi-Vector_Attacks"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"Fine-Grained Iterative Adversarial Attacks with Limited Computation Budget","url":"https://arxiv.org/pdf/2510.26981"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/html/2509.23519"},{"title":"Accuracy Is Expensive: How to Evaluate ‘Quality per $’ for Agents and RAG - DEV Community","url":"https://dev.to/lamhot/accuracy-is-expensive-how-to-evaluate-quality-per-for-agents-and-rag-10i"}]

Based on the search results, I found several relevant papers on RAG (Retrieval-Augmented Generation) adversarial defense mechanisms. Here are the key findings:

## RAG Adversarial Defense Research

Certified defenses for RAG operate by constraining the adversary's impact, typically via ranking, aggregation, or detection strategies that admit worst-case bounds, probabilistic guarantees, or explicit certificates of robust operation.

### ReliabilityRAG Approach
One notable defense mechanism is ReliabilityRAG, which uses a document-selection algorithm that identifies a "consistent majority" among retrieved documents by finding the Maximum Independent Set (MIS) on a "contradiction graph," where vertices represent retrieved documents and edges connect pairs determined to be contradictory by a Natural Language Inference model.

Recognizing the computational cost of exact MIS for large retrieval sets, a scalable weighted sample and aggregate framework explicitly utilizes reliability information, preserving some robustness guarantees while efficiently handling many documents.

### Computational Efficiency Considerations
Regarding compute budget comparisons, methods have been shown to consistently outperform existing baselines at equal cost. Additionally, when integrated into adversarial training, some approaches attain comparable performance with only 30% of the original budget.

The research indicates that modern RAG adversarial defenses are increasingly focusing on maintaining robustness while managing computational efficiency through scalable frameworks and strategic resource allocation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "894ca04a-4e20-45c5-9c0e-efee9e788710",
  "isSidechain": true,
  "promptId": "c76aef35-f9e0-437d-8b89-5335014d3c7a",
  "agentId": "a7d20c786d7950b63",
  "type": "user",
  "uuid": "33414e3f-177f-4ce4-9488-20f12781cbfb",
  "sourceToolAssistantUUID": "894ca04a-4e20-45c5-9c0e-efee9e788710",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-30T07:20:57.339Z_

<details><summary>↩ Tool result · `toolu_01Lhy7wykb8P2YmpySZnZ4fK`</summary>

```text
Web search results for query: "compute-normalized RAG defense evaluation baseline"

Links: [{"title":"Practical RAG Evaluation: A Rarity-Aware Set-Based Metric ...","url":"https://arxiv.org/pdf/2511.09545"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"Hidden-in-Plain-Text: A Benchmark for Social-Web Indirect Prompt Injection in RAG","url":"https://arxiv.org/pdf/2601.10923"},{"title":"Benchmarking Knowledge-Extraction Attack and Defense on Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2602.09319"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/pdf/2511.01268"},{"title":"EcoSafeRAG: Efficient Security through Context Analysis in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.13506"}]

Based on the search results, I found several relevant papers on RAG (Retrieval-Augmented Generation) defense evaluation and baselines:

## Key Findings

**RAG Defense Evaluation Frameworks:**

The research landscape includes a systematic benchmark for knowledge-extraction attacks on RAG systems, covering a broad spectrum of attack and defense strategies, representative retrieval embedding models, and both open- and closed-source generators, all evaluated under a unified experimental framework with standardized protocols across multiple datasets.

**Computational and Defense Trade-offs:**

RAGPart and RAGMask defenses involve systematic analysis of trade-offs between defense effectiveness and computational efficiency, providing practical guidance for real-world deployment across various system constraints.

**Evaluation Metrics:**

Defense evaluations typically report attack success at answer time (IPI ASR), retrieval-rank shift under poisoning, and utility and latency impacts of defenses. Additionally, success metrics include instruction execution at answer time (ASR) or elevated rank for attacker-targeted items under poisoning using measures like ΔnDCG@10.

**Baseline Approaches:**

Several papers discuss baseline defenses, including a simple hybrid BM25 + vector retriever as an effective architectural defense against gradient-guided RAG poisoning.

The search results indicate an active research area focused on evaluating RAG defenses with normalized metrics and computational considerations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "901f309e-7991-4097-a7b7-ab8da0632ba5",
  "isSidechain": true,
  "promptId": "c76aef35-f9e0-437d-8b89-5335014d3c7a",
  "agentId": "a7d20c786d7950b63",
  "type": "user",
  "uuid": "78fefbf3-661e-40da-a1fd-0005561bde92",
  "sourceToolAssistantUUID": "901f309e-7991-4097-a7b7-ab8da0632ba5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-30T07:21:05.047Z_

## Summary

The search results **partially support** the suggestion that compute-normalized comparison is important, though the exact terminology isn't standard:

**Key Findings:**

1. **Self-consistency + conformal prediction**: TRAQ (Trustworthy Retrieval Augmented Question Answering) uses conformal prediction for uncertainty quantification in RAG, though not explicitly self-consistency voting in the way described.

2. **Compute-normalized evaluation**: Multiple RAG defense papers (ReliabilityRAG, RAGPart/RAGMask) explicitly discuss computational efficiency trade-offs. ReliabilityRAG notes methods "consistently outperform baselines at equal cost" and achieve "comparable performance with 30% of the original budget"—suggesting equal-compute comparisons are indeed standard practice.

3. **No explicit "compute-normalized RAG defense" standard**: While papers evaluate defenses under computational constraints, the exact phrase isn't a formal standard. However, the practice is widely adopted in recent defense literature.

**Conclusion**: Giving TRAQ the same K×compute budget (via self-consistency sampling) is a **valid baseline practice** per RAG defense literature, though not universally mandatory. It ensures fair comparison when defenses incur computational overhead.

Sources:
- [TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction](https://arxiv.org/pdf/2307.04642)
- [Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction](https://arxiv.org/abs/2511.17908)
- [ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search](https://arxiv.org/pdf/2509.23519)
- [RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning](https://arxiv.org/pdf/2512.24268)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78fefbf3-661e-40da-a1fd-0005561bde92",
  "isSidechain": true,
  "agentId": "a7d20c786d7950b63",
  "requestId": "req_011CbYMCskTPVsvZmak7tQTR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "874c7e6f-e6cd-4dec-8aa5-588c91f01e9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KrgMLwB5viFEYznBHeWHGD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 795,
      "cache_creation_input_tokens": 1590,
      "cache_read_input_tokens": 16747,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1590
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 795,
          "output_tokens": 448,
          "cache_read_input_tokens": 16747,
          "cache_creation_input_tokens": 1590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1590,
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
