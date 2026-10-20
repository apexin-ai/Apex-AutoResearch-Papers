# Research conversation: I need to verify the current status of SWE-bench Verified and how SWE-bench-Live is positioned relative to it. Specifica

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a0cadb313022819a6.jsonl`
- **Structured JSON:** [`d00eaef31cf708c74a64.json`](../../sessions/d0/d00eaef31cf708c74a64.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-10T07:14:26.951Z_

I need to verify the current status of SWE-bench Verified and how SWE-bench-Live is positioned relative to it. Specifically:

1. Is SWE-bench Verified "officially abandoned"? Or is it just reaching saturation? What is the official stance?
2. OpenAI's February 2026 announcement about SWE-bench Pro as a replacement — what exactly did it say?
3. How is SWE-bench-Live (arXiv 2505.23419, NeurIPS 2025) positioned relative to SWE-bench Verified?

Please search for:
- "SWE-bench Verified abandoned" or "SWE-bench Verified saturation"
- "SWE-bench Pro replacement" 
- "SWE-bench-Live contamination"
- Any official announcements about SWE-bench Verified deprecation

Also look at the SWE-bench-Live paper (arXiv 2505.23419) abstract and positioning statements.

Report: What is the accurate framing for SWE-bench Verified's current status and where SWE-bench-Live fits in?

This is purely research — no code changes needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "agentId": "a0cadb313022819a6",
  "type": "user",
  "uuid": "acf63543-c2dc-44f6-91f5-b53954957eb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T07:14:28.045Z_

I'll help you verify the current status of SWE-bench Verified and understand how SWE-bench-Live is positioned. Let me search for relevant information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acf63543-c2dc-44f6-91f5-b53954957eb1",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUXnMhzWGaFiTiZ8Y7D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "03138dfc-05f9-49a6-bca2-46a9352b084d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0121NZwVyogm1HyGYvAr8LnA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 699,
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

_source line 3 · 2026-05-10T07:14:28.767Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015sGFUMaFidQNYumxCyKnww`</summary>

```json
{
  "query": "SWE-bench Verified abandoned deprecated saturation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03138dfc-05f9-49a6-bca2-46a9352b084d",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUXnMhzWGaFiTiZ8Y7D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "480714a3-48f6-4941-9aaf-58cd7a95af4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0121NZwVyogm1HyGYvAr8LnA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 699,
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

_source line 4 · 2026-05-10T07:14:28.789Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LjACoHTxmeRCQvPEvXv1zT`</summary>

```json
{
  "query": "OpenAI SWE-bench Pro replacement February 2026 announcement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "480714a3-48f6-4941-9aaf-58cd7a95af4a",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUXnMhzWGaFiTiZ8Y7D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0cdc1b3b-c713-480f-a352-d0958089d9cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0121NZwVyogm1HyGYvAr8LnA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 699,
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

_source line 5 · 2026-05-10T07:14:28.798Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014vv2D1eBCAMxNWUF7iHNyr`</summary>

```json
{
  "query": "SWE-bench-Live arXiv 2505.23419 contamination SWE-bench Verified"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cdc1b3b-c713-480f-a352-d0958089d9cc",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUXnMhzWGaFiTiZ8Y7D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ed803c65-0402-4225-b374-9497f79a9f1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0121NZwVyogm1HyGYvAr8LnA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 699,
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

_source line 6 · 2026-05-10T07:14:28.848Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FMD79Q12L7Gn5KGD5DAzhC`</summary>

```json
{
  "query": "\"SWE-bench-Live\" positioning relative SWE-bench Verified"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed803c65-0402-4225-b374-9497f79a9f1b",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUXnMhzWGaFiTiZ8Y7D",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0090e595-b0be-4387-89f3-17414a0b8155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0121NZwVyogm1HyGYvAr8LnA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 699,
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

_source line 7 · 2026-05-10T07:14:33.846Z_

<details><summary>↩ Tool result · `toolu_015sGFUMaFidQNYumxCyKnww`</summary>

```text
Web search results for query: "SWE-bench Verified abandoned deprecated saturation 2025 2026"

Links: [{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"⚡️The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data","url":"https://www.latent.space/p/swe-bench-dead"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified no longer measures frontier coding capabilities | Hacker News","url":"https://news.ycombinator.com/item?id=47910388"},{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI","url":"https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"}]

Based on the search results, here are the key findings about SWE-bench Verified:

## Abandonment and Deprecation

OpenAI publicly abandoned SWE-Bench Verified and endorsed SWE-Bench Pro, according to a February 2026 announcement. SWE-bench Verified is increasingly contaminated and mismeasures frontier coding progress, with analysis showing flawed tests and training leakage.

## Saturation Status

SWE-bench Verified reached saturation at 93.9% in 2026. The discussion around the saturation of SWE-Bench has been swirling in the community for over a year, with most frontier model numbers consistently reporting around 80%.

## Recent Updates

In February 2026, there was a major upgrade of scaffolding, environments, and token limits. However, despite these updates, OpenAI recommends SWE-bench Pro as an alternative to the now-deprecated Verified benchmark.

## Alternative Benchmarks

SWE-bench Multilingual and SWE-bench Multimodal are still unsaturated, suggesting these are being developed as replacements for the saturated Verified version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "480714a3-48f6-4941-9aaf-58cd7a95af4a",
  "isSidechain": true,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "agentId": "a0cadb313022819a6",
  "type": "user",
  "uuid": "6808c01f-0e89-471e-824e-df502a40b4ce",
  "sourceToolAssistantUUID": "480714a3-48f6-4941-9aaf-58cd7a95af4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T07:14:34.089Z_

<details><summary>↩ Tool result · `toolu_01FMD79Q12L7Gn5KGD5DAzhC`</summary>

```text
Web search results for query: ""SWE-bench-Live" positioning relative SWE-bench Verified"

Links: [{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"SWE-bench-Live/SWE-bench-Live · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live"}]

Based on the search results, here's the positioning of SWE-bench-Live relative to SWE-bench Verified:

## Key Differences

**SWE-bench Verified** is a human-filtered subset of 500 instances from SWE-bench, created in collaboration with OpenAI. This version supersedes the original SWE-bench and SWE-bench Lite test sets.

**SWE-bench-Live**, in contrast, is a newer, continuously evolving benchmark. SWE-bench-Live is built upon the foundation of SWE-bench, and each month, it will add 50 newly verified, high-quality issues to the dataset, while the lite and verified splits will remain frozen, ensuring fair leaderboard comparisons and keeping evaluation costs manageable.

## Dataset Scope

SWE-bench-Live employs an LLM filter to automatically filter the full dataset to create SWE-bench-Live Verified, which contains 500 instances from 2024-07 to 2025-04. This represents a more recent collection of issues compared to SWE-bench Verified, which was released in 2024.

In summary, SWE-bench-Live is a newer, actively maintained alternative that provides continuously updated real-world GitHub issues with rolling monthly updates, while SWE-bench Verified serves as a fixed, human-validated reference set for stable benchmark comparisons.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0090e595-b0be-4387-89f3-17414a0b8155",
  "isSidechain": true,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "agentId": "a0cadb313022819a6",
  "type": "user",
  "uuid": "c40697ce-8080-426d-a215-f1079527ccdd",
  "sourceToolAssistantUUID": "0090e595-b0be-4387-89f3-17414a0b8155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T07:14:36.235Z_

<details><summary>↩ Tool result · `toolu_01LjACoHTxmeRCQvPEvXv1zT`</summary>

```text
Web search results for query: "OpenAI SWE-bench Pro replacement February 2026 announcement"

Links: [{"title":"OpenAI Drops SWE-bench Verified: What It Means for AI","url":"https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/"},{"title":"Everything You Need to Know About GPT-5.5 - Vellum","url":"https://www.vellum.ai/blog/everything-you-need-to-know-about-gpt-5-5"},{"title":"OpenAI Developers on X: \"The standard for frontier coding evals is changing with model maturity. We now recommend reporting SWE-bench Pro and are sharing more detail on why we’re no longer reporting SWE-bench Verified as we work with the industry to establish stronger coding eval standards. SWE-bench\" / X","url":"https://x.com/OpenAIDevs/status/2026002219909427270"},{"title":"Introducing GPT-5.5 | OpenAI","url":"https://openai.com/index/introducing-gpt-5-5/"},{"title":"OpenAI Abandons SWE-bench Verified Over Contamination – AI Herald","url":"https://ai-herald.com/openai-abandons-swe-bench-verified-over-contamination/"},{"title":"Aibreakingwire","url":"https://aibreakingwire.com/news/openai-ditches-swe-bench-verified-cites-critical-flaws"},{"title":"OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed","url":"https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests"},{"title":"Is SWE-bench Verified Contaminated? OpenAI Shifts to SWE-bench Pro | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/news/swe-bench-contamination-debate"},{"title":"⚡️The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data","url":"https://www.latent.space/p/swe-bench-dead"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"}]

Based on the search results, here's what happened with OpenAI's SWE-bench Pro replacement announcement in February 2026:

## The Announcement

OpenAI's decision to stop evaluating against SWE-bench Verified was announced February 23, 2026 by the company's own Frontier Evals team. OpenAI now recommends reporting SWE-bench Pro and are sharing more detail on why they're no longer reporting SWE-bench Verified as they work with the industry to establish stronger coding eval standards.

## Why They Made the Switch

OpenAI retired SWE-bench Verified in February 2026 after finding it saturated and highly contaminated. At least 59.4% of remaining benchmark tasks were found to be flawed or unsolvable under fair evaluation. Additionally, the company's February 23, 2026 analysis also found evidence that all major frontier models—including GPT-5.2, Claude Opus 4.5, and Gemini 3 Flash—had been trained on benchmark solutions, rendering scores meaningless.

## SWE-bench Pro as Replacement

SWE-bench Pro is a benchmark developed by Scale AI, released September 2025, that uses private and copyleft-licensed repositories to minimize training data overlap. Top frontier models score around 70%+ on SWE-bench Verified but drop to approximately 23% on SWE-bench Pro. This dramatic difference reflects how much of the previous benchmark's performance came from training data exposure rather than genuine problem-solving ability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cdc1b3b-c713-480f-a352-d0958089d9cc",
  "isSidechain": true,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "agentId": "a0cadb313022819a6",
  "type": "user",
  "uuid": "4d9c368f-ed9a-4156-8e07-0075eadaf1db",
  "sourceToolAssistantUUID": "0cdc1b3b-c713-480f-a352-d0958089d9cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T07:14:39.665Z_

<details><summary>↩ Tool result · `toolu_014vv2D1eBCAMxNWUF7iHNyr`</summary>

```text
Web search results for query: "SWE-bench-Live arXiv 2505.23419 contamination SWE-bench Verified"

Links: [{"title":"[2505.23419] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"arXiv:2505.23419v2 [cs.SE] 1 Jun 2025 SWE-bench Goes Live! Linghao Zhang","url":"https://arxiv.org/pdf/2505.23419"},{"title":"arXiv:2505.23419v1 [cs.SE] 29 May 2025 SWE-bench Goes Live! Linghao Zhang1∗","url":"https://arxiv.org/pdf/2505.23419v1"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-Universe: Scale Real-World Verifiable Environments to Millions","url":"https://arxiv.org/html/2602.02361v1"},{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v2"},{"title":"[2505.23419v1] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419v1"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"GitHub - microsoft/SWE-bench-Live: [NeurIPS 2025 D&B] 🚀 SWE-bench Goes Live!","url":"https://github.com/microsoft/SWE-bench-Live"}]

Based on the search results, here's what I found about the arXiv paper 2505.23419 and its relationship to contamination and SWE-bench:

## SWE-bench Goes Live (arXiv 2505.23419)

SWE-bench-Live is a live-updatable benchmark consisting of 1,319 tasks derived from real GitHub issues created since 2024, spanning 93 repositories.

### Addressing Contamination

The original SWE-bench and its variants suffer from key limitations including not being updated since release, covering a narrow set of repositories, and depending heavily on manual effort for instance construction and environment setup, which hinders scalability and introduces risks of overfitting and data contamination.

To reduce the risk of data contamination from pretraining, the dataset is restricted to issues created between January 1, 2024, and April 20, 2025.

### Relationship to SWE-bench Verified

SWE-bench-Live results show that OpenHands with Claude 3.7 Sonnet achieves the highest performance on SWE-bench-Live; however, its overall results are significantly lower compared to those achieved on SWE-bench Verified. This suggests that existing models may be overfitting to static benchmarks like SWE-bench, underscoring the importance of developing more dynamic and diverse evaluation settings such as those provided by SWE-bench-Live.

SWE-bench Verified is a human-filtered subset of 500 instances from SWE-bench, created in collaboration with OpenAI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed803c65-0402-4225-b374-9497f79a9f1b",
  "isSidechain": true,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "agentId": "a0cadb313022819a6",
  "type": "user",
  "uuid": "9b1b8aa2-de38-4c16-b760-c95b7dcd8c35",
  "sourceToolAssistantUUID": "ed803c65-0402-4225-b374-9497f79a9f1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T07:14:41.736Z_

Now let me fetch the actual SWE-bench-Live paper to get precise positioning statements from the abstract and introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b1b8aa2-de38-4c16-b760-c95b7dcd8c35",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUYimSKcuBcbUTVZ1Mq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "66e0cb1d-d45a-4925-91cc-c9c6bc59a8c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016AgxSghsuX2ysFbvSFvcsN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 3644,
      "cache_read_input_tokens": 16854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3644,
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

_source line 12 · 2026-05-10T07:14:42.381Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MVQPUhG96oBTvQHvmehSKN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.23419",
  "prompt": "What is SWE-bench-Live's positioning statement relative to SWE-bench Verified? What does the abstract say about saturation and contamination?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66e0cb1d-d45a-4925-91cc-c9c6bc59a8c1",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUYimSKcuBcbUTVZ1Mq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f95822b1-cf9e-4bab-8ad8-1532542f0fde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016AgxSghsuX2ysFbvSFvcsN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 3644,
      "cache_read_input_tokens": 16854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3644,
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

_source line 13 · 2026-05-10T07:14:42.931Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VQbdBMCNBWDA83SPNYK91p`</summary>

```json
{
  "url": "https://www.latent.space/p/swe-bench-dead",
  "prompt": "What is the official announcement about SWE-bench Verified being abandoned? What are the exact findings from OpenAI?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f95822b1-cf9e-4bab-8ad8-1532542f0fde",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUYimSKcuBcbUTVZ1Mq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d8752063-6060-46d0-8b99-47d69a8a101c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016AgxSghsuX2ysFbvSFvcsN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 3644,
      "cache_read_input_tokens": 16854,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3644
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 764,
          "output_tokens": 236,
          "cache_read_input_tokens": 16854,
          "cache_creation_input_tokens": 3644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3644,
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

_source line 14 · 2026-05-10T07:14:47.914Z_

<details><summary>↩ Tool result · `toolu_01MVQPUhG96oBTvQHvmehSKN`</summary>

```text
# SWE-bench-Live Analysis

## Positioning Statement

The provided abstract does not mention "SWE-bench Verified" or explicitly position SWE-bench-Live relative to it. The abstract only references limitations of "SWE-bench and its variants," noting they "have not been updated since their initial releases, cover a narrow set of repositories, and depend heavily on manual effort."

## Saturation and Contamination

The abstract addresses contamination concerns, stating that SWE-bench-Live provides "a fresh, diverse, and executable benchmark grounded in live repository activity" that facilitates "contamination-resistant evaluation of LLMs and agents."

However, the abstract does not explicitly discuss "saturation" in relation to existing benchmarks. It emphasizes the risk factors that SWE-bench-Live aims to mitigate: overfitting and data contamination stemming from static, infrequently updated datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f95822b1-cf9e-4bab-8ad8-1532542f0fde",
  "isSidechain": true,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "agentId": "a0cadb313022819a6",
  "type": "user",
  "uuid": "5603fd4a-68de-40f7-aa6f-1b500da2e763",
  "sourceToolAssistantUUID": "f95822b1-cf9e-4bab-8ad8-1532542f0fde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T07:14:49.142Z_

<details><summary>↩ Tool result · `toolu_01VQbdBMCNBWDA83SPNYK91p`</summary>

```text
# OpenAI's Official Abandonment of SWE-Bench Verified

## The Announcement

OpenAI officially discontinued reporting SWE-Bench Verified scores and publicly endorsed switching to SWE-Bench Pro instead. Mia Glaese and Olivia Watkins, from OpenAI's Frontier Evals team, announced this decision on February 23, 2026.

## Key Findings

OpenAI conducted a deeper analysis of 138 problematic test cases and identified two critical issues:

**1. Test Quality Problems (>60% of remaining problems)**
- 49 tests were overly narrowly defined, rejecting functionally correct solutions
- 26 tests demanded features never mentioned in the problem description
- Tests sometimes required specific function names or implementation details not specified in requirements

**2. Training Data Contamination**
OpenAI found that "ALL frontier models, starting with OpenAI's, being able to reproduce the original gold patch or problem statements from the eval verbatim with minimal prompting" using only task IDs. This included:
- GPT-5.2 producing unspecified test requirements in its reasoning chain
- All major frontier models showing familiarity with SWE-Bench problems
- Problems sourced from popular open-source repositories used in model training

These findings rendered the benchmark unsuitable for measuring genuine coding capability improvements at current performance levels (~80%).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8752063-6060-46d0-8b99-47d69a8a101c",
  "isSidechain": true,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "agentId": "a0cadb313022819a6",
  "type": "user",
  "uuid": "4a15328c-faa9-4913-8c7d-0efdd77a4153",
  "sourceToolAssistantUUID": "d8752063-6060-46d0-8b99-47d69a8a101c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T07:14:50.142Z_

Now let me check the official OpenAI statements directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a15328c-faa9-4913-8c7d-0efdd77a4153",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUZRH12njRcwH3WNca5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d86f7b8a-68ff-4d85-a268-cc735ee84969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jm9ywBFegSGfpgqp4zoLx6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 20498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1571,
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

_source line 17 · 2026-05-10T07:14:50.789Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016XZhDQbFbXHqSBheDZzU2J`</summary>

```json
{
  "url": "https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/",
  "prompt": "What is OpenAI's official stance on why they are no longer evaluating SWE-bench Verified? What are the exact percentages and findings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d86f7b8a-68ff-4d85-a268-cc735ee84969",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUZRH12njRcwH3WNca5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2d0ec927-3551-49db-bfdb-bc2a42bdc2e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jm9ywBFegSGfpgqp4zoLx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 20498,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1571
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 140,
          "cache_read_input_tokens": 20498,
          "cache_creation_input_tokens": 1571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1571,
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

_source line 18 · 2026-05-10T07:14:51.013Z_

<details><summary>↩ Tool result · reported error · `toolu_016XZhDQbFbXHqSBheDZzU2J`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d0ec927-3551-49db-bfdb-bc2a42bdc2e0",
  "isSidechain": true,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "agentId": "a0cadb313022819a6",
  "type": "user",
  "uuid": "cadd2f4a-1aef-4020-aa6c-78fadb77f54a",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "2d0ec927-3551-49db-bfdb-bc2a42bdc2e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T07:14:52.122Z_

Let me try the OpenAI blog post about SWE-bench Verified with a different approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cadd2f4a-1aef-4020-aa6c-78fadb77f54a",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUZZEV5Kee7F2qV4qpc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "472b159b-96f8-4ba8-afea-2353e27d8ee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017x6VxdzWSJnuK3XgzGkMUY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 22069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 270,
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

_source line 20 · 2026-05-10T07:14:52.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ovaGaPdVCGrKjZme39ZaN`</summary>

```json
{
  "query": "\"OpenAI\" \"SWE-bench Verified\" \"no longer evaluate\" February 2026 official announcement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "472b159b-96f8-4ba8-afea-2353e27d8ee6",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUZZEV5Kee7F2qV4qpc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2d73c535-662c-4a79-a477-2f7541d7853e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017x6VxdzWSJnuK3XgzGkMUY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 22069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 270,
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

_source line 21 · 2026-05-10T07:14:52.776Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019YMEv8dfYf8o8eqZBQDct8`</summary>

```json
{
  "url": "https://github.com/microsoft/SWE-bench-Live",
  "prompt": "How does SWE-bench-Live position itself relative to SWE-bench Verified? What are the key improvements mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d73c535-662c-4a79-a477-2f7541d7853e",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUZZEV5Kee7F2qV4qpc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6e34642c-82b0-4a59-a45c-acf9aaf08f2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017x6VxdzWSJnuK3XgzGkMUY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 22069,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 194,
          "cache_read_input_tokens": 22069,
          "cache_creation_input_tokens": 270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 270,
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

_source line 22 · 2026-05-10T07:14:58.957Z_

<details><summary>↩ Tool result · `toolu_019YMEv8dfYf8o8eqZBQDct8`</summary>

```text
# SWE-bench-Live vs SWE-bench Verified

Based on the provided content, SWE-bench-Live distinguishes itself as "a live benchmark for issue resolving, designed to evaluate an AI system's ability to complete real-world software engineering tasks."

## Key Improvements

**Continuous Updates**: The project implements an "automated dataset curation pipeline" enabling monthly updates with new task instances, whereas the original SWE-bench had static datasets.

**Contamination-Free Evaluation**: The framework supports "rigorous and contamination-free evaluation" through scheduled monthly additions of verified instances, with frozen training splits to prevent data leakage.

**Multi-Platform Support**: Recent expansions include language diversity (Multi-Language variant released October 2026) and Windows-specific tasks (August 2026), moving beyond the original Python-only focus.

**Automated Environment Setup**: The integration of RepoLaunch addresses infrastructure challenges by automating containerized environment creation, reducing setup bottlenecks that plagued earlier benchmarks.

**Transparent Curation**: The visible curation pipeline and monthly update schedule (adding "50 newly verified, high-quality issues") provide community confidence in dataset quality and freshness.

The documentation emphasizes this positions SWE-bench-Live as a continuously evolving benchmark rather than a static snapshot.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e34642c-82b0-4a59-a45c-acf9aaf08f2f",
  "isSidechain": true,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "agentId": "a0cadb313022819a6",
  "type": "user",
  "uuid": "608dd58e-20fa-476b-b139-e30c5f518fa3",
  "sourceToolAssistantUUID": "6e34642c-82b0-4a59-a45c-acf9aaf08f2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T07:14:59.082Z_

<details><summary>↩ Tool result · `toolu_017ovaGaPdVCGrKjZme39ZaN`</summary>

```text
Web search results for query: ""OpenAI" "SWE-bench Verified" "no longer evaluate" February 2026 official announcement"

Links: [{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI","url":"https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"},{"title":"OpenAI Developers on X: \"The standard for frontier coding evals is changing with model maturity. We now recommend reporting SWE-bench Pro and are sharing more detail on why we’re no longer reporting SWE-bench Verified as we work with the industry to establish stronger coding eval standards. SWE-bench\" / X","url":"https://x.com/OpenAIDevs/status/2026002219909427270"},{"title":"⚡️The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data","url":"https://www.latent.space/p/swe-bench-dead"},{"title":"OpenAI o3 SWE-Bench Score: What Engineers Aren't Told","url":"https://neuralwired.com/2026/04/13/openai-o3-swe-bench-benchmark/"},{"title":"OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed","url":"https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests"},{"title":"Aibreakingwire","url":"https://aibreakingwire.com/news/openai-ditches-swe-bench-verified-cites-critical-flaws"},{"title":"OpenAI Abandons SWE-bench Verified: 59% Flawed Tests | byteiota","url":"https://byteiota.com/openai-abandons-swe-bench-verified-59-flawed-tests/"},{"title":"Is SWE-bench Verified Contaminated? OpenAI Shifts to SWE-bench Pro | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/news/swe-bench-contamination-debate"},{"title":"OpenAI Drops SWE-bench Verified: What It Means for AI","url":"https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/"},{"title":"SWE-Bench Verified's Sudden Fall: How OpenAI Exposed Flaws in AI Coding's Top Metric","url":"https://www.webpronews.com/swe-bench-verifieds-sudden-fall-how-openai-exposed-flaws-in-ai-codings-top-metric/"}]

Based on the search results, I found the official OpenAI announcement you're looking for:

## Official OpenAI Announcement

On February 23, 2026, OpenAI announced that SWE-bench Verified is increasingly contaminated. OpenAI has stopped reporting SWE-bench Verified scores, and they recommend that other model developers do so too.

## Key Reasons for Discontinuation

OpenAI audited a 27.6% subset of the dataset that models often failed to solve and found that at least 59.4% of the audited problems have flawed test cases that reject functionally correct submissions.

In their analysis, OpenAI found that all frontier models tested were able to reproduce the original, human-written bug fix used as the ground-truth reference. This means that improvements on SWE-bench Verified no longer reflect meaningful improvements in models' real-world software development abilities. Instead, they increasingly reflect how much the model was exposed to the benchmark at training time.

## Recommended Alternative

OpenAI recommends reporting results for SWE-bench Pro.

The official announcement was published on OpenAI's website at openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/, titled "Why SWE-bench Verified no longer measures frontier coding capabilities."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d73c535-662c-4a79-a477-2f7541d7853e",
  "isSidechain": true,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "agentId": "a0cadb313022819a6",
  "type": "user",
  "uuid": "27eb4de1-0daa-4839-934d-b7faec9435d3",
  "sourceToolAssistantUUID": "2d73c535-662c-4a79-a477-2f7541d7853e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T07:15:13.196Z_

Based on my research, here is the accurate framing of SWE-bench Verified's current status and where SWE-bench-Live fits in:

## SWE-bench Verified's Status: NOT "Abandoned" but "Officially Deprecated"

**The official stance is clear deprecation, not just saturation.** On February 23, 2026, OpenAI's Frontier Evals team (Mia Glaese & Olivia Watkins) officially announced that SWE-bench Verified **no longer measures frontier coding capabilities** and should no longer be used for evaluating frontier models.

### The Two-Pronged Problem

OpenAI's analysis identified critical flaws that go beyond saturation:

1. **Test Quality Issues (>60% of remaining problems)**: 
   - 49 tests were overly narrowly defined, rejecting functionally correct solutions
   - 26 tests demanded features never mentioned in problem descriptions
   - Tests sometimes required specific implementation details not specified in requirements
   - At least 59.4% of the audited problems have flawed test cases

2. **Training Data Contamination (100% of frontier models affected)**:
   - ALL frontier models tested—including GPT-5.2, Claude Opus 4.5, and Gemini 3 Flash—could reproduce the original ground-truth bug fixes verbatim with minimal prompting
   - Models showed familiarity with SWE-bench problems from training data exposure
   - Improvements no longer reflect genuine problem-solving ability but rather training data overlap

## OpenAI's February 2026 Announcement

The official stance from OpenAI was published in their blog post "[Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)" and via [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270):

> "The standard for frontier coding evals is changing with model maturity. We now recommend reporting SWE-bench Pro and are sharing more detail on why we're no longer reporting SWE-bench Verified as we work with the industry to establish stronger coding eval standards."

**Key replacement**: SWE-bench Pro (released September 2025 by Scale AI) uses private and copyleft-licensed repositories. Scores dropped from ~70%+ on SWE-bench Verified to ~23% on SWE-bench Pro across frontier models—reflecting genuine problem-solving ability rather than training contamination.

## SWE-bench-Live's Positioning (arXiv 2505.23419, NeurIPS 2025)

SWE-bench-Live is positioned as the **live alternative to the static, contamination-prone SWE-bench Verified**:

### Key Differentiators:

1. **Continuously Updated**: Monthly additions of 50 newly verified, high-quality issues from real GitHub repositories
2. **Fresh Data**: Issues sourced from January 1, 2024 onwards (covering 2024-07 to 2025-04), significantly more recent than SWE-bench Verified
3. **Contamination Resistance**: Dates are carefully chosen to avoid overlap with model training cutoffs (Jan 2024 - April 20, 2025)
4. **Dynamic Evaluation**: Each month adds truly novel problems, preventing overfitting and maintaining fair leaderboard comparisons
5. **1,319 total instances** spanning 93 repositories (much broader than the fixed 500 in SWE-bench Verified)

### Performance Comparison:

The paper explicitly notes that models achieving high scores on SWE-bench Verified (80%+) show "significantly lower" performance on SWE-bench-Live, confirming that the original benchmark suffered from overfitting and contamination.

## Accurate Framing Summary

| Aspect | SWE-bench Verified | SWE-bench-Live |
|--------|-------------------|-----------------|
| **Status** | Officially deprecated (Feb 2026) | NeurIPS 2025 replacement |
| **Cause** | 59%+ flawed tests, 100% training contamination | Fresh, monthly-updated issues |
| **Dataset** | Static 500 instances, pre-2024 | 1,319 instances, continuously updated |
| **Contamination Risk** | Critical | Minimized by date cutoffs & monthly updates |
| **Use Case** | Legacy/historical tracking only | Current frontier model evaluation |

**Verdict**: SWE-bench Verified is not "reaching saturation"—it is fundamentally compromised by flawed test design and universal training data leakage, making scores meaningless for frontier models. SWE-bench-Live directly addresses these issues through continuous updates, fresh real-world issues, and careful contamination avoidance.

Sources:
- [The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data](https://www.latent.space/p/swe-bench-dead)
- [Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)
- [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270)
- [SWE-bench Goes Live! (arXiv 2505.23419)](https://arxiv.org/abs/2505.23419)
- [SWE-bench-Live GitHub Repository](https://github.com/microsoft/SWE-bench-Live)
- [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27eb4de1-0daa-4839-934d-b7faec9435d3",
  "isSidechain": true,
  "agentId": "a0cadb313022819a6",
  "requestId": "req_011CatUa9msj6rVoo8bsyZVR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d824da6c-62e4-4312-b4c8-f8c3c31d3735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lw8aRCvmPf38859gKLU3uh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 323,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 22339,
      "output_tokens": 1396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1221
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 323,
          "output_tokens": 1396,
          "cache_read_input_tokens": 22339,
          "cache_creation_input_tokens": 1221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1221,
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
