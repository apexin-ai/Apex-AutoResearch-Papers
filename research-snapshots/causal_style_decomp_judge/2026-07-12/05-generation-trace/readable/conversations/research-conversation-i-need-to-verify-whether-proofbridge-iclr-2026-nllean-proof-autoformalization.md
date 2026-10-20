# Research conversation: I need to verify whether ProofBridge (ICLR 2026, NL→Lean proof autoformalization) has open-source code and whether it ca

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a31114d36c9eea32d.jsonl`
- **Structured JSON:** [`88306ad6e4f97e1aa107.json`](../../sessions/88/88306ad6e4f97e1aa107.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-27T11:23:48.596Z_

I need to verify whether ProofBridge (ICLR 2026, NL→Lean proof autoformalization) has open-source code and whether it can be evaluated on ProofFlowBench. Search the web for "ProofBridge autoformalization github" or "ProofBridge ICLR 2026 code" to check code availability. Also search for "ProofBridge ProofFlowBench" to see if they share evaluation benchmarks. Report what you find concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a6827c65-8009-44e1-b06c-1a4c52fae758",
  "agentId": "a31114d36c9eea32d",
  "type": "user",
  "uuid": "b81c987b-2b30-41f4-baa2-5a897f015edf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3cae6bf6-48fd-4b3f-89a7-48e6f2d4d7cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T11:23:48.601Z_

```json
{
  "parentUuid": "b81c987b-2b30-41f4-baa2-5a897f015edf",
  "isSidechain": true,
  "agentId": "a31114d36c9eea32d",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d5a29aae-8dd8-43c3-8831-340f282a7fc3",
  "timestamp": "2026-05-27T11:23:48.601Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3cae6bf6-48fd-4b3f-89a7-48e6f2d4d7cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-27T11:23:50.672Z_

I'll search for information about ProofBridge's code availability and its compatibility with ProofFlowBench.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5a29aae-8dd8-43c3-8831-340f282a7fc3",
  "isSidechain": true,
  "agentId": "a31114d36c9eea32d",
  "requestId": "req_011CbSzJEkBgBnFkamdVhCPW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "34212043-233c-4dc3-9c09-7acfd386072d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3cae6bf6-48fd-4b3f-89a7-48e6f2d4d7cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012n13Ncm1sT8Q9YBcButgfh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16759,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16759,
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

_source line 4 · 2026-05-27T11:23:50.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DVhHebcTzoxrttKSdCc2f8`</summary>

```json
{
  "query": "ProofBridge autoformalization github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34212043-233c-4dc3-9c09-7acfd386072d",
  "isSidechain": true,
  "agentId": "a31114d36c9eea32d",
  "requestId": "req_011CbSzJEkBgBnFkamdVhCPW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fb9eee0c-dbb9-4786-a641-5b3f121bea93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3cae6bf6-48fd-4b3f-89a7-48e6f2d4d7cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012n13Ncm1sT8Q9YBcButgfh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16759,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16759,
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

_source line 5 · 2026-05-27T11:23:50.887Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W49R3yKLxBK8eN7ZsHnb8y`</summary>

```json
{
  "query": "ProofBridge ICLR 2026 code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb9eee0c-dbb9-4786-a641-5b3f121bea93",
  "isSidechain": true,
  "agentId": "a31114d36c9eea32d",
  "requestId": "req_011CbSzJEkBgBnFkamdVhCPW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "878b4163-9fb8-4712-9287-278dcef50240",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3cae6bf6-48fd-4b3f-89a7-48e6f2d4d7cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012n13Ncm1sT8Q9YBcButgfh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16759,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16759,
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

_source line 6 · 2026-05-27T11:23:50.969Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WJr1wUKNw5CTeidjVuNjNu`</summary>

```json
{
  "query": "ProofBridge ProofFlowBench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "878b4163-9fb8-4712-9287-278dcef50240",
  "isSidechain": true,
  "agentId": "a31114d36c9eea32d",
  "requestId": "req_011CbSzJEkBgBnFkamdVhCPW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bec983d5-ef2c-48f5-be46-98f6f55a2927",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3cae6bf6-48fd-4b3f-89a7-48e6f2d4d7cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012n13Ncm1sT8Q9YBcButgfh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16759,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16759,
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

### Tool result

_source line 7 · 2026-05-27T11:23:59.138Z_

<details><summary>↩ Tool result · `toolu_01W49R3yKLxBK8eN7ZsHnb8y`</summary>

```text
Web search results for query: "ProofBridge ICLR 2026 code"

Links: [{"title":"GitHub - PrithwishJana/ProofBridge: [ICLR-2026 main track] ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. · GitHub","url":"https://github.com/PrithwishJana/ProofBridge"},{"title":"GitHub - shreyascasturi/proofbridge-nesy-2026: [ICLR-2026 main track] ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. · GitHub","url":"https://github.com/shreyascasturi/proofbridge-nesy-2026"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings [Quick Review]","url":"https://liner.com/review/proofbridge-autoformalization-of-natural-language-proofs-in-lean-via-joint"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/pdf/2510.15681"},{"title":"ICLR 2026 Papers with Code & Data – Paper Digest","url":"https://www.paperdigest.org/2026/04/iclr-2026-papers-with-code-data/"},{"title":"ICLR 2026 Papers with Code & Data – Resources | Paper Digest","url":"https://resources.paperdigest.org/2026/04/iclr-2026-papers-with-code-data/"},{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"}]

Based on the search results, I found information about ProofBridge and its ICLR 2026 code:

## ProofBridge ICLR 2026

ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. The paper was published at ICLR-2026 (14th International Conference on Learning Representations), held April 23-27, 2026, in Rio de Janeiro, Brazil.

## Code Repositories

There are two GitHub repositories available for ProofBridge:

1. **Primary repository**: https://github.com/PrithwishJana/ProofBridge
2. **Alternative repository**: https://github.com/shreyascasturi/proofbridge-nesy-2026

The pre-print and appendix are available at: https://arxiv.org/abs/2510.15681

The code includes installation instructions for dependencies (pandas, tqdm, datasets, vllm, trl, wandb, poetry) and setup for Lean 4 version 4.15.0, along with scripts for dataset preparation using NuminaMath-LEAN-PF data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "878b4163-9fb8-4712-9287-278dcef50240",
  "isSidechain": true,
  "promptId": "a6827c65-8009-44e1-b06c-1a4c52fae758",
  "agentId": "a31114d36c9eea32d",
  "type": "user",
  "uuid": "2d953ee2-06e6-42a4-a1ad-e7f412e40417",
  "sourceToolAssistantUUID": "878b4163-9fb8-4712-9287-278dcef50240",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3cae6bf6-48fd-4b3f-89a7-48e6f2d4d7cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T11:23:59.288Z_

<details><summary>↩ Tool result · `toolu_01DVhHebcTzoxrttKSdCc2f8`</summary>

```text
Web search results for query: "ProofBridge autoformalization github"

Links: [{"title":"GitHub - PrithwishJana/ProofBridge: [ICLR-2026 main track] ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. · GitHub","url":"https://github.com/PrithwishJana/ProofBridge"},{"title":"GitHub - shreyascasturi/proofbridge-nesy-2026: [ICLR-2026 main track] ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. · GitHub","url":"https://github.com/shreyascasturi/proofbridge-nesy-2026"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings | OpenReview","url":"https://openreview.net/forum?id=U2jxHXuOX9"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/pdf/2510.15681"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings [Quick Review]","url":"https://liner.com/review/proofbridge-autoformalization-of-natural-language-proofs-in-lean-via-joint"},{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings | Request PDF","url":"https://www.researchgate.net/publication/396693100_ProofBridge_Auto-Formalization_of_Natural_Language_Proofs_in_Lean_via_Joint_Embeddings"},{"title":"José A. Alonso on X: \"ProofBridge: Auto-formalization of natural language proofs in Lean via joint embeddings. ~ Prithwish Jana et als. https://t.co/cXfy31wRup #ITP #LeanProver #Autoformalization #LLMs #Math\" / X","url":"https://x.com/Jose_A_Alonso/status/1980233551749808484"}]

Based on the search results, here's what I found about ProofBridge:

## Overview

ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. This was accepted as an ICLR-2026 main track paper.

## Key Features

At its core is a joint embedding model that aligns NL and FL theorem+proof pairs in a shared semantic space, enabling cross-modal retrieval of semantically relevant FL examples to guide translation. ProofBridge integrates retrieval-augmented fine-tuning with iterative proof repair, leveraging Lean's type checker and semantic equivalence feedback to ensure both syntactic correctness and semantic fidelity.

## GitHub Repositories

The project has multiple GitHub repositories:
1. **Primary repository**: https://github.com/PrithwishJana/ProofBridge
2. **Alternative repository**: https://github.com/shreyascasturi/proofbridge-nesy-2026

## Performance

The framework shows substantial improvements in proof auto-formalization over strong baselines (including GPT-5, Gemini-2.5, Kimina-Prover, DeepSeek-Prover), with the retrieval-augmented approach yielding significant gains in semantic correctness and type correctness across pass@k metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb9eee0c-dbb9-4786-a641-5b3f121bea93",
  "isSidechain": true,
  "promptId": "a6827c65-8009-44e1-b06c-1a4c52fae758",
  "agentId": "a31114d36c9eea32d",
  "type": "user",
  "uuid": "4008e347-1eae-4dd4-85ae-91d89e6049b0",
  "sourceToolAssistantUUID": "fb9eee0c-dbb9-4786-a641-5b3f121bea93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3cae6bf6-48fd-4b3f-89a7-48e6f2d4d7cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-27T11:23:59.696Z_

<details><summary>↩ Tool result · `toolu_01WJr1wUKNw5CTeidjVuNjNu`</summary>

```text
Web search results for query: "ProofBridge ProofFlowBench"

Links: [{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings [Quick Review]","url":"https://liner.com/review/proofbridge-autoformalization-of-natural-language-proofs-in-lean-via-joint"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings | OpenReview","url":"https://openreview.net/forum?id=U2jxHXuOX9"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/html/2510.15981v1"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings | Request PDF","url":"https://www.researchgate.net/publication/396693100_ProofBridge_Auto-Formalization_of_Natural_Language_Proofs_in_Lean_via_Joint_Embeddings"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/pdf/2510.15681"},{"title":"ProofBridge - Capture Authentic Customer Stories with Ease","url":"https://www.proofbridge.io/"},{"title":"Paper page - ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://huggingface.co/papers/2510.15681"},{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"}]

Based on the search results, here's information about ProofBridge and ProofFlowBench:

## ProofBridge

ProofBridge is a unified framework for automatically translating entire NL theorems and proofs into Lean 4. At its core is a joint embedding model that aligns NL and FL (NL-FL) theorem+proof pairs in a shared semantic space, enabling cross-modal retrieval of semantically relevant FL examples to guide translation.

ProofBridge integrates retrieval-augmented fine-tuning with iterative proof repair, leveraging Lean's type checker and semantic equivalence feedback to ensure both syntactic correctness and semantic fidelity.

Key performance results: Experiments show substantial improvements in proof auto-formalization over strong baselines (including GPT-5, Gemini-2.5, Kimina-Prover, DeepSeek-Prover), with significant gains in semantic correctness (SC) and type correctness (TC) across pass@k metrics on miniF2F-Test-PF, a dataset they curated.

## ProofFlowBench

ProofFlowBench is a benchmark that is integrated with ProofScore evaluation for comprehensive assessment. This appears to be part of the ProofFlow project, which is a related but distinct system that focuses on proof autoformalization using a dependency graph approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bec983d5-ef2c-48f5-be46-98f6f55a2927",
  "isSidechain": true,
  "promptId": "a6827c65-8009-44e1-b06c-1a4c52fae758",
  "agentId": "a31114d36c9eea32d",
  "type": "user",
  "uuid": "629ea958-a66d-4b54-9a94-1b6f69acbd72",
  "sourceToolAssistantUUID": "bec983d5-ef2c-48f5-be46-98f6f55a2927",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3cae6bf6-48fd-4b3f-89a7-48e6f2d4d7cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-27T11:24:03.801Z_

## Summary

**ProofBridge Code Availability:** Yes, ProofBridge has open-source code available on GitHub:
- **Primary repo**: https://github.com/PrithwishJana/ProofBridge
- **Alternative repo**: https://github.com/shreyascasturi/proofbridge-nesy-2026

The code includes setup instructions, dependencies (pandas, tqdm, datasets, vllm, trl, wandb, poetry), and Lean 4.15.0 configuration. The paper and appendix are available on arXiv.

**ProofBridge and ProofFlowBench Compatibility:** The search results show these are **separate projects**. ProofBridge evaluates on **miniF2F-Test-PF**, a custom dataset they curated. ProofFlow is a related but distinct framework using a dependency graph approach. While both are NL→Lean proof autoformalization systems, they use different benchmarks. ProofFlowBench appears to be integrated with ProofScore evaluation, but there's no direct evidence that ProofBridge was evaluated on ProofFlowBench.

Sources:
- [GitHub - PrithwishJana/ProofBridge](https://github.com/PrithwishJana/ProofBridge)
- [GitHub - shreyascasturi/proofbridge-nesy-2026](https://github.com/shreyascasturi/proofbridge-nesy-2026)
- [ProofBridge on arXiv](https://arxiv.org/abs/2510.15681)
- [ProofFlow on arXiv](https://arxiv.org/html/2510.15981v1)
- [OpenReview Forum](https://openreview.net/forum?id=U2jxHXuOX9)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "629ea958-a66d-4b54-9a94-1b6f69acbd72",
  "isSidechain": true,
  "agentId": "a31114d36c9eea32d",
  "requestId": "req_011CbSzK4CThmCCiJjrWeMjY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "628b149c-174a-4a2b-976f-dd7f2d5f2992",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3cae6bf6-48fd-4b3f-89a7-48e6f2d4d7cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vqwydh9Xp3byXKFuTtjgru",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3024,
      "cache_read_input_tokens": 16759,
      "output_tokens": 426,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3024
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 426,
          "cache_read_input_tokens": 16759,
          "cache_creation_input_tokens": 3024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3024,
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
