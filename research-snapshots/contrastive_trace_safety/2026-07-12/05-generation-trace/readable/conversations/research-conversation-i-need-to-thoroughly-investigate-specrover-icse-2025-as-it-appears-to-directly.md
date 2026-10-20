# Research conversation: I need to thoroughly investigate SpecRover (ICSE 2025) as it appears to directly compete with the idea of extracting str

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a3b320e09a3f42f08.jsonl`
- **Structured JSON:** [`7379d6b4e1b422b5ea46.json`](../../sessions/73/7379d6b4e1b422b5ea46.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-10T06:31:03.432Z_

I need to thoroughly investigate SpecRover (ICSE 2025) as it appears to directly compete with the idea of extracting structured specifications from bug reports for program repair.

1. WebFetch the SpecRover paper at https://abhikrc.com/pdf/ICSE25.pdf - read the abstract, introduction, and method sections carefully. What exactly does it extract? Does it do supervised training on a labeled dataset? Does it produce pre/post-conditions, affected interfaces, expected vs actual behavior?

2. WebSearch for "SpecRover code intent extraction LLM ICSE 2025" to find more details and citations.

3. Also search for "Qwen3-Coder model release 2025 2026" - verify this model actually exists (the proposal plans to fine-tune it)

4. WebSearch for "DeepSeek-V4 model 2025 2026" - verify this model exists (the proposal uses it as a teacher)

5. WebSearch for "SWE-bench Verified 2026 leaderboard best" to get accurate current SOTA numbers.

Report exactly what you find for each item.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9ab205c0-03d5-4838-b76d-c6b02ccf0a6f",
  "agentId": "a3b320e09a3f42f08",
  "type": "user",
  "uuid": "30dd3a89-31b4-49b6-ac07-71fb3db9405e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T06:31:04.664Z_

I'll investigate these items systematically. Let me start with fetching the SpecRover paper and then do the web searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30dd3a89-31b4-49b6-ac07-71fb3db9405e",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatRDsJGkEtobZEsyMyL9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e053db22-dfd6-4159-97b4-f249a25a2df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VsF98Zx7MLmuhff778eDGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 683,
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

_source line 3 · 2026-05-10T06:31:05.031Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D8kTHP2V6eHfgv83CZca2h`</summary>

```json
{
  "url": "https://abhikrc.com/pdf/ICSE25.pdf",
  "prompt": "Read the abstract, introduction, and method sections. What exactly does SpecRover extract? Does it do supervised training on a labeled dataset? Does it produce pre/post-conditions, affected interfaces, expected vs actual behavior?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e053db22-dfd6-4159-97b4-f249a25a2df8",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatRDsJGkEtobZEsyMyL9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "84a56a31-4923-4ec9-8ccc-74aace7028c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VsF98Zx7MLmuhff778eDGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 683,
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

_source line 4 · 2026-05-10T06:31:05.242Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012H2aMVA9dMm9SxN2iM7J9q`</summary>

```json
{
  "query": "SpecRover code intent extraction LLM ICSE 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84a56a31-4923-4ec9-8ccc-74aace7028c6",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatRDsJGkEtobZEsyMyL9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2726dfe-50dd-480e-9dcf-9fa8417baa42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VsF98Zx7MLmuhff778eDGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 683,
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

_source line 5 · 2026-05-10T06:31:05.247Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JqjSjifFMLgaxPdUSJoAwn`</summary>

```json
{
  "query": "Qwen3-Coder model release 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2726dfe-50dd-480e-9dcf-9fa8417baa42",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatRDsJGkEtobZEsyMyL9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "56496afb-8ac8-4291-b932-fc083f79dc4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VsF98Zx7MLmuhff778eDGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 683,
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

_source line 6 · 2026-05-10T06:31:05.438Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TCeMXrv73BYh4YzcNbL7vh`</summary>

```json
{
  "query": "DeepSeek-V4 model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56496afb-8ac8-4291-b932-fc083f79dc4d",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatRDsJGkEtobZEsyMyL9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2314249c-ec54-4284-9497-4c01babe777b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VsF98Zx7MLmuhff778eDGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 683,
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

_source line 7 · 2026-05-10T06:31:05.531Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NtWLRbMsXbm9Q1XqLhBiSH`</summary>

```json
{
  "query": "SWE-bench Verified 2026 leaderboard best"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2314249c-ec54-4284-9497-4c01babe777b",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatRDsJGkEtobZEsyMyL9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ce53908-45b1-4392-892e-20757575de65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VsF98Zx7MLmuhff778eDGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 683,
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

### Tool result

_source line 8 · 2026-05-10T06:31:08.913Z_

<details><summary>↩ Tool result · `toolu_01D8kTHP2V6eHfgv83CZca2h`</summary>

```text
I cannot provide a meaningful analysis of this document. The content you've shared appears to be raw PDF binary data (showing internal PDF structure objects, streams, and encoding) rather than readable text.

To answer your questions about SpecRover's extraction capabilities, I would need:
- The actual readable text content of the paper
- Access to sections like abstract, introduction, and methods in plain text format

If you have a PDF of this research paper, I'd recommend:
1. Converting it to plain text or copying the readable sections
2. Sharing those specific passages
3. Then I can analyze what SpecRover extracts, whether it uses supervised learning, and what outputs it produces

Could you provide the paper content in a readable format?

[Binary content (application/pdf, 661.6KB) also saved to /home/ubuntu/.claude-account-1/projects/-/7b3e7966-7e1e-48c4-9b8f-d1f614574b66/tool-results/webfetch-1778394665571-c9zac9.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84a56a31-4923-4ec9-8ccc-74aace7028c6",
  "isSidechain": true,
  "promptId": "9ab205c0-03d5-4838-b76d-c6b02ccf0a6f",
  "agentId": "a3b320e09a3f42f08",
  "type": "user",
  "uuid": "15f134a1-08a0-426f-89c2-69217fa7e2e3",
  "sourceToolAssistantUUID": "84a56a31-4923-4ec9-8ccc-74aace7028c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T06:31:11.567Z_

<details><summary>↩ Tool result · `toolu_01NtWLRbMsXbm9Q1XqLhBiSH`</summary>

```text
Web search results for query: "SWE-bench Verified 2026 leaderboard best"

Links: [{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/sweVerified"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"}]

Based on the search results, here's what's currently leading the SWE-bench Verified 2026 leaderboard:

## Top Performers on SWE-bench Verified 2026

As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Verified leaderboard with 93.9%, followed by Claude Opus 4.7 (Adaptive) at 87.6% and GPT-5.3 Codex at 85%.

However, it's important to note that OpenAI stopped reporting Verified scores in early 2026 and now recommends SWE-bench Pro instead. This is because Claude Opus 4.5 scores 80.9% on SWE-bench Verified, but the same model on SWE-bench Pro, using standardised scaffolding, scores 45.9%.

OpenAI's audit found that every frontier model tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches or problem statement specifics for certain SWE-Bench Verified tasks. This suggests that the Verified benchmark may have data contamination issues, making SWE-bench Pro the more reliable benchmark for evaluating true model capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ce53908-45b1-4392-892e-20757575de65",
  "isSidechain": true,
  "promptId": "9ab205c0-03d5-4838-b76d-c6b02ccf0a6f",
  "agentId": "a3b320e09a3f42f08",
  "type": "user",
  "uuid": "e216547e-0378-488d-9b9b-6b303ee7f8c0",
  "sourceToolAssistantUUID": "1ce53908-45b1-4392-892e-20757575de65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T06:31:13.339Z_

<details><summary>↩ Tool result · `toolu_01TCeMXrv73BYh4YzcNbL7vh`</summary>

```text
Web search results for query: "DeepSeek-V4 model 2025 2026"

Links: [{"title":"Three reasons why DeepSeek’s new model matters | MIT Technology Review","url":"https://www.technologyreview.com/2026/04/24/1136422/why-deepseeks-v4-matters/"},{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"},{"title":"DeepSeek V4 Preview Release | DeepSeek API Docs","url":"https://api-docs.deepseek.com/news/news260424"},{"title":"The Sequel That Stumbled: DeepSeek's V4 and the Converging Pressures of Competition and State Control — Foreign Affairs Forum","url":"https://www.faf.ae/home/2026/5/3/the-sequel-that-stumbled-deepseeks-v4-and-the-converging-pressures-of-competition-and-state-control"},{"title":"DeepSeek V4—almost on the frontier, a fraction of the price","url":"https://simonwillison.net/2026/Apr/24/deepseek-v4/"},{"title":"DeepSeek V4: The Open-Source Model That Rivals Closed Frontier Models | MindStudio","url":"https://www.mindstudio.ai/blog/deepseek-v4-open-source-frontier-model-review"},{"title":"China's DeepSeek releases preview of long-awaited V4 model as AI race intensifies","url":"https://www.cnbc.com/2026/04/24/deepseek-v4-llm-preview-open-source-ai-competition-china.html"},{"title":"China’s AI upstart DeepSeek drops new model. Will it make waves like last year? | CNN Business","url":"https://www.cnn.com/2026/04/24/tech/chinas-ai-deepseek-v4-intl-hnk"},{"title":"CAISI Evaluation of DeepSeek V4 Pro | NIST","url":"https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro"},{"title":"Everything to know about DeepSeek’s new AI model V4","url":"https://www.euronews.com/next/2026/04/24/chinas-deepseek-releases-new-ai-model-v4-heres-everything-to-know-as-the-ai-race-speeds-up"}]

Based on the search results, here's what I found about DeepSeek-V4 model in 2025-2026:

## Release and Timeline

V4 marks DeepSeek's most significant release since R1, the reasoning model it launched in January 2025. The Hangzhou-based lab unveiled V4 on April twenty-fourth, 2026.

## Model Variants

DeepSeek-V4 series includes two strong Mixture-of-Experts (MoE) language models — DeepSeek-V4-Pro with 1.6T parameters (49B activated) and DeepSeek-V4-Flash with 284B parameters (13B activated) — both supporting a context length of one million tokens.

## Performance

DeepSeek claims that V4's performance rivals the best models available at a fraction of the price. However, performance assessments vary: DeepSeek-V4-Pro-Max demonstrates superior performance relative to GPT-5.2 and Gemini-3.0-Pro on standard reasoning benchmarks, but its performance falls marginally short of GPT-5.4 and Gemini-3.1-Pro, suggesting a developmental trajectory that trails state-of-the-art frontier models by approximately 3 to 6 months.

## Pricing

DeepSeek is charging $0.14/million tokens input and $0.28/million tokens output for Flash, and $1.74/million input and $3.48/million output for Pro. DeepSeek V4 Pro matches GPT-5.5 and Claude Opus 4.7 on most agentic benchmarks at roughly 10–13x lower API cost per output token.

## Key Features

DeepSeek-V4 series incorporate a hybrid attention mechanism combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) to dramatically improve long-context efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2314249c-ec54-4284-9497-4c01babe777b",
  "isSidechain": true,
  "promptId": "9ab205c0-03d5-4838-b76d-c6b02ccf0a6f",
  "agentId": "a3b320e09a3f42f08",
  "type": "user",
  "uuid": "c39cd142-c604-41de-880e-144c502837f8",
  "sourceToolAssistantUUID": "2314249c-ec54-4284-9497-4c01babe777b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T06:31:16.719Z_

<details><summary>↩ Tool result · `toolu_01JqjSjifFMLgaxPdUSJoAwn`</summary>

```text
Web search results for query: "Qwen3-Coder model release 2025 2026"

Links: [{"title":"Qwen3-Coder-Next: Pushing Small Hybrid Models","url":"https://qwen.ai/blog?id=qwen3-coder-next"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen/Qwen3-Coder-Next · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Coder-Next"},{"title":"Qwen - Wikipedia","url":"https://en.wikipedia.org/wiki/Qwen"},{"title":"Qwen3-Coder-Next: The Complete 2026 Guide to Running Powerful AI Coding Agents Locally - DEV Community","url":"https://dev.to/sienna/qwen3-coder-next-the-complete-2026-guide-to-running-powerful-ai-coding-agents-locally-1k95"},{"title":"Qwen 3 in 2026: The Best Free Coding AI — With a Catch","url":"https://ucstrategies.com/news/qwen-3-in-2026-the-best-free-coding-ai-with-a-catch/"},{"title":"GitHub - QwenLM/Qwen3-Coder: Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. · GitHub","url":"https://github.com/QwenLM/Qwen3-Coder"},{"title":"2026-03-03 Qwen3-Coder-Next Technical Report Qwen Team","url":"https://arxiv.org/pdf/2603.00729v1"},{"title":"Qwen3-Coder: Agentic Coding in the World","url":"https://qwen.ai/blog?id=qwen3-coder"},{"title":"Qwen Team Releases Qwen3-Coder-Next: An Open-Weight Language Model Designed Specifically for Coding Agents and Local Development - MarkTechPost","url":"https://www.marktechpost.com/2026/02/03/qwen-team-releases-qwen3-coder-next-an-open-weight-language-model-designed-specifically-for-coding-agents-and-local-development/"}]

Based on the web search results, here's what I found about Qwen3-Coder model releases in 2025 and 2026:

## Qwen3-Coder Releases

Qwen3-Coder is available in multiple sizes, including Qwen3-Coder-480B-A35B-Instruct, Qwen3-Coder-30B-A3B-Instruct, and Qwen3-Coder-Next.

### Qwen3-Coder-480B-A35B (2025)
Qwen3-Coder-480B-A35B-Instruct is a 480B-parameter Mixture-of-Experts model with 35B active parameters which supports the context length of 256K tokens natively and 1M tokens with extrapolation methods. This model sets new state-of-the-art results among open models on Agentic Coding, Agentic Browser-Use, and Agentic Tool-Use, comparable to Claude Sonnet 4.

### Qwen3-Coder-Next (February 2026)
Qwen3-Coder-Next is an open-weight language model released by Alibaba's Qwen team in February 2026, specifically designed for coding agents and local development environments. Built on top of Qwen3-Next-80B-A3B-Base, which adopts a novel architecture with hybrid attention and MoE, Qwen3-Coder-Next has been agentically trained at scale on large-scale executable task synthesis, environment interaction, and reinforcement learning.

Qwen3-Coder-Next achieves over 70% on SWE-Bench Verified using the SWE-Agent scaffold, with only 3B activated parameters (80B total parameters), achieving performance comparable to models with 10–20x more active parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56496afb-8ac8-4291-b932-fc083f79dc4d",
  "isSidechain": true,
  "promptId": "9ab205c0-03d5-4838-b76d-c6b02ccf0a6f",
  "agentId": "a3b320e09a3f42f08",
  "type": "user",
  "uuid": "15d7708d-f0c8-4d4e-b238-1e6cd2038dab",
  "sourceToolAssistantUUID": "56496afb-8ac8-4291-b932-fc083f79dc4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T06:31:18.792Z_

<details><summary>↩ Tool result · `toolu_012H2aMVA9dMm9SxN2iM7J9q`</summary>

```text
Web search results for query: "SpecRover code intent extraction LLM ICSE 2025"

Links: [{"title":"SpecRover: Code Intent Extraction via LLMs (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/68/SpecRover-Code-Intent-Extraction-via-LLMs"},{"title":"[2408.02232] SpecRover: Code Intent Extraction via LLMs","url":"https://arxiv.org/abs/2408.02232"},{"title":"SpecRover: Code Intent Extraction via LLMs | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00080"},{"title":"SpecRover: Code Intent Extraction via LLMs","url":"https://www.computer.org/csdl/proceedings-article/icse/2025/056900a617/251mFZysrIc"},{"title":"publications | Yuntong Zhang","url":"https://yuntongzhang.github.io/publications/"},{"title":"SpecRover: Code Intent Extraction via LLMs | Request PDF","url":"https://www.researchgate.net/publication/392958739_SpecRover_Code_Intent_Extraction_via_LLMs"},{"title":"SpecRover: Code Intent Extraction via LLMs Haifeng Ruan* Yuntong Zhang*","url":"https://abhikrc.com/pdf/ICSE25.pdf"},{"title":"SpecRover: Code Intent Extraction via LLMs *Joint first authors, ordered alphabetically.","url":"https://arxiv.org/html/2408.02232v3"},{"title":"SpecRover: Code Intent Extraction via LLMs | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11029735/;jsessionid=12C5290F1B543D969546A39E1B3A5345"},{"title":"GitHub - FudanSELab/Agent4SE-Paper-List: Repository for the paper \"Large Language Model-Based Agents for Software Engineering: A Survey\". Keep updating. · GitHub","url":"https://github.com/FudanSELab/Agent4SE-Paper-List"}]

Based on the search results, here's information about SpecRover:

## Overview

SpecRover is designed to conduct iterative code search accompanied by specification inference to infer intent from both the project structure and behavior when given a GitHub issue to be resolved in a software project.

## Key Features

SpecRover (AutoCodeRover-v2) is built on the open-source LLM agent AutoCodeRover. The work examines the role of specification inference in LLM guided autonomous software engineering and suggests iterative specification inference to guide patching in LLM oriented program repair workflows.

The system includes a reviewer agent for code review which reconciles specifications, tests and natural language requirements, conducting comprehensive patch validation and producing evidence of correctness of automatically generated fixes.

## Performance

In an evaluation on the full SWE-Bench consisting of 2294 GitHub issues, it shows more than 50% improvement in efficacy over AutoCodeRover. The work shows modest cost ($0.65 per issue) in resolving an average GitHub issue in SWE-Bench lite.

## Publication

SpecRover is authored by Haifeng Ruan, Yuntong Zhang, and Abhik Roychoudhury, and was presented at the 47th International Conference on Software Engineering (ICSE) in Ottawa, Canada, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2726dfe-50dd-480e-9dcf-9fa8417baa42",
  "isSidechain": true,
  "promptId": "9ab205c0-03d5-4838-b76d-c6b02ccf0a6f",
  "agentId": "a3b320e09a3f42f08",
  "type": "user",
  "uuid": "65cfa43f-8420-41f3-a2e4-1aefd9990b57",
  "sourceToolAssistantUUID": "f2726dfe-50dd-480e-9dcf-9fa8417baa42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T06:31:20.358Z_

Now let me search for the ArXiv version of SpecRover to get the technical details you need:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65cfa43f-8420-41f3-a2e4-1aefd9990b57",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatREzwBaQNcGZLcsZMkq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0805a96a-ff07-402b-9f8d-90e6182c21ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018FpiSm7cPscdFmhcNAG5di",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3000,
      "cache_creation_input_tokens": 2362,
      "cache_read_input_tokens": 16838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2362,
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

_source line 14 · 2026-05-10T06:31:21.213Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EoYXWdBh7qtXwr73B2tuGk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2408.02232",
  "prompt": "What exactly does SpecRover extract? Does it do supervised training on labeled datasets? What are the specifications produced - pre/post-conditions, affected interfaces, expected vs actual behavior?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0805a96a-ff07-402b-9f8d-90e6182c21ba",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatREzwBaQNcGZLcsZMkq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "311c4ab0-ff06-4e86-8c0a-b40e1ec70db1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018FpiSm7cPscdFmhcNAG5di",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3000,
      "cache_creation_input_tokens": 2362,
      "cache_read_input_tokens": 16838,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2362
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3000,
          "output_tokens": 144,
          "cache_read_input_tokens": 16838,
          "cache_creation_input_tokens": 2362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2362,
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

_source line 15 · 2026-05-10T06:31:25.890Z_

<details><summary>↩ Tool result · `toolu_01EoYXWdBh7qtXwr73B2tuGk`</summary>

```text
# SpecRover Extraction and Training Details

Based on the provided content, here's what can be determined:

## What SpecRover Extracts

The abstract indicates that SpecRover extracts **code intent** through "iterative specification inference" by conducting "iterative code search accompanied by specification inference — thereby inferring intent from both the project structure and behavior."

However, the webpage does not specify the exact format of these specifications (whether they are preconditions, postconditions, interface descriptions, or behavioral assertions).

## Supervised Training

The content provides **no information** about supervised training on labeled datasets. SpecRover is described as being "built on the open-source LLM agent AutoCodeRover" but uses LLM capabilities rather than traditional supervised learning approaches.

## Specification Format

The document does not detail the precise structure of produced specifications. It only mentions that "the production of explanation by SpecRover allows for a better 'signal' to be given to the developer, on when the suggested patches can be accepted with confidence."

To answer these questions comprehensively, you would need to consult the full paper rather than this abstract page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "311c4ab0-ff06-4e86-8c0a-b40e1ec70db1",
  "isSidechain": true,
  "promptId": "9ab205c0-03d5-4838-b76d-c6b02ccf0a6f",
  "agentId": "a3b320e09a3f42f08",
  "type": "user",
  "uuid": "f92aaa49-42d6-4886-a05a-15e527d474b9",
  "sourceToolAssistantUUID": "311c4ab0-ff06-4e86-8c0a-b40e1ec70db1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T06:31:27.059Z_

Let me try to access the HTML version of the ArXiv paper which might be more readable:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f92aaa49-42d6-4886-a05a-15e527d474b9",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatRFXFKXGm2yZf8QaD6b",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "338ee82d-828a-47f7-81ff-3c4526602077",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vw4iM6dqz3DUexBGADVjmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3401,
      "cache_read_input_tokens": 19200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3401,
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

_source line 17 · 2026-05-10T06:31:27.575Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012JYUsgeYFmKZJqqjJxQiz8`</summary>

```json
{
  "url": "https://arxiv.org/html/2408.02232v3",
  "prompt": "What exactly does SpecRover extract as specifications? Does it use supervised training on labeled datasets? What specific outputs does it produce - pre/post-conditions, interface specifications, expected vs actual behavior comparisons?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "338ee82d-828a-47f7-81ff-3c4526602077",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatRFXFKXGm2yZf8QaD6b",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e54138fa-8e23-4975-9841-69fb2febd09c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vw4iM6dqz3DUexBGADVjmG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3401,
      "cache_read_input_tokens": 19200,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3401
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 148,
          "cache_read_input_tokens": 19200,
          "cache_creation_input_tokens": 3401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3401,
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

_source line 18 · 2026-05-10T06:31:32.919Z_

<details><summary>↩ Tool result · `toolu_012JYUsgeYFmKZJqqjJxQiz8`</summary>

```text
# SpecRover's Specification Extraction

## What SpecRover Extracts

SpecRover extracts three main types of specifications:

1. **Function Summaries**: "natural-language summary of how a function should behave to meet the requirements specified in the high-level problem description." These capture intended behavior at the function level.

2. **Reproducer Tests**: Automatically generated test cases that reproduce the reported issue, creating executable specifications of expected behavior.

3. **Reviewer Feedback**: Meta-specifications that evaluate patch correctness and provide explanations for why patches succeed or fail.

## Training Approach

SpecRover does **not** use supervised training on labeled datasets. Instead, it employs an iterative, **unsupervised agent-based workflow** using LLMs (Claude 3.5 Sonnet and GPT-4o) with prompt engineering. The system uses chain-of-thought reasoning within LLM agents rather than training.

## Specific Outputs

The tool produces evidence artifacts including:

- Buggy locations paired with their intended behaviors
- Generated reproducer tests
- Approval rationale from the reviewer agent
- Patch selection justifications
- Natural language explanations suitable as commit messages

Rather than formal pre/post-conditions, SpecRover emphasizes "natural language artifacts" that help developers understand patches and integrate them into codebases.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e54138fa-8e23-4975-9841-69fb2febd09c",
  "isSidechain": true,
  "promptId": "9ab205c0-03d5-4838-b76d-c6b02ccf0a6f",
  "agentId": "a3b320e09a3f42f08",
  "type": "user",
  "uuid": "9538e35d-bf0a-4d20-a82d-350ccab02604",
  "sourceToolAssistantUUID": "e54138fa-8e23-4975-9841-69fb2febd09c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T06:31:47.323Z_

Perfect! Now I have comprehensive information on all your requests. Let me compile the complete findings:

## Investigation Summary

### 1. SpecRover Paper (ICSE 2025) - Technical Details

**What SpecRover Extracts:**
SpecRover extracts three main specification types:
- **Function Summaries**: Natural language summaries describing how functions should behave to meet requirements
- **Reproducer Tests**: Automatically generated test cases that reproduce the reported issue
- **Reviewer Feedback**: Meta-specifications evaluating patch correctness

**Supervised Training:**
SpecRover does **NOT** use supervised training on labeled datasets. It employs an iterative, unsupervised agent-based workflow using LLMs (Claude 3.5 Sonnet and GPT-4o) with prompt engineering and chain-of-thought reasoning.

**Specification Format:**
Rather than formal pre/post-conditions or interface specifications, SpecRover produces:
- Buggy locations paired with intended behaviors
- Generated reproducer tests
- Natural language approval rationale
- Patch selection justifications
- Natural language explanations for commit messages

**Key Finding for Your Work**: SpecRover does not produce structured specifications like pre/post-conditions or formal interface contracts. It generates natural language artifacts and test-based specifications. This is a meaningful difference from the structured specification extraction you're proposing.

### 2. SpecRover Research Details (ICSE 2025)

SpecRover is authored by Haifeng Ruan, Yuntong Zhang, and Abhik Roychoudhury. It builds on AutoCodeRover-v2 and showed >50% improvement in efficacy over the base AutoCodeRover on the full SWE-Bench (2294 GitHub issues) with modest cost ($0.65 per issue).

Sources:
- [SpecRover on ICSE Conference](https://conf.researchr.org/details/icse-2025/icse-2025-research-track/68/SpecRover-Code-Intent-Extraction-via-LLMs)
- [SpecRover on ArXiv](https://arxiv.org/abs/2408.02232)

### 3. Qwen3-Coder Model - VERIFIED

**Qwen3-Coder-480B-A35B (2025)**: 480B parameters (35B active), supports 256K tokens natively and 1M tokens with extrapolation. Sets SOTA among open models on agentic coding, comparable to Claude Sonnet 4.

**Qwen3-Coder-Next (February 2026)**: Released by Alibaba's Qwen team specifically for coding agents. Built on Qwen3-Next-80B-A3B-Base with hybrid attention and MoE. Achieves **over 70% on SWE-Bench Verified** using SWE-Agent scaffold with only 3B activated parameters (80B total).

The model is actively available on Hugging Face (Qwen/Qwen3-Coder-Next).

Sources:
- [Qwen3-Coder-Next Blog](https://qwen.ai/blog?id=qwen3-coder-next)
- [Qwen3-Coder-Next on Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-Next)

### 4. DeepSeek-V4 Model - VERIFIED

**DeepSeek-V4** was released on April 24, 2026 (very recent). Two main variants exist:
- **DeepSeek-V4-Pro**: 1.6T parameters (49B activated), supports 1M token context
- **DeepSeek-V4-Flash**: 284B parameters (13B activated), supports 1M token context

**Performance**: DeepSeek-V4-Pro matches GPT-5.5 and Claude Opus 4.7 on agentic benchmarks at roughly 10-13x lower API cost per output token.

**Architecture**: Uses hybrid attention combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) for improved long-context efficiency.

Sources:
- [DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424)
- [DeepSeek V4 on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

### 5. SWE-bench Verified 2026 Leaderboard - Current SOTA

**Important Caveat**: OpenAI stopped reporting Verified scores in early 2026 and now recommends SWE-bench Pro instead due to potential data contamination issues.

**SWE-bench Verified Leaders (as of May 7, 2026)**:
- **Claude Mythos Preview**: 93.9% (highest)
- **Claude Opus 4.7 (Adaptive)**: 87.6%
- **GPT-5.3 Codex**: 85%

**Critical Issue**: Frontier models like Claude Opus 4.5 (80.9% on Verified) score only 45.9% on the more reliable SWE-bench Pro with standardized scaffolding. OpenAI's audit found evidence of verbatim gold patch reproduction, suggesting Verified may have data contamination.

**Recommendation**: Use SWE-bench Pro for reliable evaluation instead of Verified.

Sources:
- [SWE-bench Verified Leaderboard](https://llm-stats.com/benchmarks/swe-bench-verified)
- [SWE-bench Official](https://www.swebench.com/)
- [SWE-bench Analysis 2026](https://www.codeant.ai/blogs/swe-bench-scores)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9538e35d-bf0a-4d20-a82d-350ccab02604",
  "isSidechain": true,
  "agentId": "a3b320e09a3f42f08",
  "requestId": "req_011CatRG3K5qHZwKwD2jrVye",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "61f282dd-db19-4794-a5db-a85b44bc544d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7b3e7966-7e1e-48c4-9b8f-d1f614574b66",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hya44k7qdLokxJUdAb9f3L",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 22601,
      "output_tokens": 1389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 569
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 1389,
          "cache_read_input_tokens": 22601,
          "cache_creation_input_tokens": 569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 569,
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
