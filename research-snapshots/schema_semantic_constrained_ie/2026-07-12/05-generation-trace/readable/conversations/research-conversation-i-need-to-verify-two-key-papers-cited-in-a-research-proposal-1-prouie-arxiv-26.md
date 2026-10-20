# Research conversation: I need to verify two key papers cited in a research proposal: 1. **ProUIE (arXiv 2604.10633, Apr 2026)** — claimed to us

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a27b09cab7f485136.jsonl`
- **Structured JSON:** [`dec5ce37077660d2beb6.json`](../../sessions/de/dec5ce37077660d2beb6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-10T19:27:06.318Z_

I need to verify two key papers cited in a research proposal:

1. **ProUIE (arXiv 2604.10633, Apr 2026)** — claimed to use "stepwise structural rewards with GRPO on Qwen3-4B" achieving "71.17 avg F1" on UIE benchmarks. Verify:
   - Does this paper exist?
   - Does it use Qwen3-4B?
   - What F1 does it achieve?
   - Does it use GRPO with stepwise structural rewards?

2. **EAPO (arXiv 2601.10306, Jan 2026)** — claimed to introduce "Group-Relative Evidence Reward with Adaptive Reward-Policy Co-Evolution" achieving "+5.1% over vanilla GRPO on 8 QA benchmarks". Verify:
   - Does this paper exist?
   - What does it actually propose?
   - What are its actual results?

3. **RuCL (arXiv 2602.21628, Feb 2026)** — claimed "rubric-stratified curriculum with GRPO, +7.83% avg improvement". Verify existence and claims.

4. **RSAT (arXiv 2605.00199, May 2026)** — claimed "NLI-based faithfulness reward for table reasoning with cell-level citations". Verify existence.

Use WebSearch and WebFetch to verify. Report exact findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "840604e5-59fa-4424-a4f4-a0753b52fccf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:27:06.323Z_

```json
{
  "parentUuid": "840604e5-59fa-4424-a4f4-a0753b52fccf",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
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
  "uuid": "d721b8ef-4199-47c5-b63f-28a61cab4936",
  "timestamp": "2026-05-10T19:27:06.323Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:27:10.778Z_



I'll verify each of these papers by searching for them and fetching their arXiv pages. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d721b8ef-4199-47c5-b63f-28a61cab4936",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSQDa4dxZabQFDSNiwd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "245c9519-f654-4090-a7be-95fb6ff5f5a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZwcLmBA8pHjnek2pVoXWU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 891,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:27:11.149Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Tzg5kVUKmdogoDD1wiTZFp`</summary>

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
  "parentUuid": "245c9519-f654-4090-a7be-95fb6ff5f5a9",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSQDa4dxZabQFDSNiwd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a08f3b7f-b2c9-4d75-bf54-0522e0d38b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZwcLmBA8pHjnek2pVoXWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 8223,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 891
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 891,
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

_source line 5 · 2026-05-10T19:27:11.154Z_

<details><summary>↩ Tool result · `toolu_01Tzg5kVUKmdogoDD1wiTZFp`</summary>

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
  "parentUuid": "a08f3b7f-b2c9-4d75-bf54-0522e0d38b6d",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "bb6e3c8c-9da6-4173-9bc5-9f10ccc320eb",
  "sourceToolAssistantUUID": "a08f3b7f-b2c9-4d75-bf54-0522e0d38b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:27:13.554Z_



Now let me search for all four papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb6e3c8c-9da6-4173-9bc5-9f10ccc320eb",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSQaZ8QXX76N2k25ozc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5879aa0f-6e44-4048-a48e-babfac896aa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvMXPDAxEHJke4Fi7hHeB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 7 · 2026-05-10T19:27:14.580Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DJVd48BJAxNSH6byKnJrpA`</summary>

```json
{
  "query": "arXiv 2604.10633 ProUIE stepwise structural rewards GRPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5879aa0f-6e44-4048-a48e-babfac896aa1",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSQaZ8QXX76N2k25ozc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42e53535-3aae-4b9a-90d9-936a3517a17e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvMXPDAxEHJke4Fi7hHeB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 8 · 2026-05-10T19:27:15.569Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G27BqnAxsWmu4hnScXren2`</summary>

```json
{
  "query": "arXiv 2601.10306 EAPO Group-Relative Evidence Reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42e53535-3aae-4b9a-90d9-936a3517a17e",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSQaZ8QXX76N2k25ozc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da39ff45-1a66-42cc-a21a-5c0958e6fc9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvMXPDAxEHJke4Fi7hHeB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 9 · 2026-05-10T19:27:16.587Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LVgYJJAwzfKLiKH51hUxAd`</summary>

```json
{
  "query": "arXiv 2602.21628 RuCL rubric-stratified curriculum GRPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da39ff45-1a66-42cc-a21a-5c0958e6fc9c",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSQaZ8QXX76N2k25ozc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52794668-57b1-46ed-b8c8-939bb095e520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvMXPDAxEHJke4Fi7hHeB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 10 · 2026-05-10T19:27:17.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D3PibKPCMwDp7uHwmptD69`</summary>

```json
{
  "query": "arXiv 2605.00199 RSAT NLI faithfulness reward table reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52794668-57b1-46ed-b8c8-939bb095e520",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSQaZ8QXX76N2k25ozc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "540991f0-19b4-4b61-9ce2-c7fe23597109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvMXPDAxEHJke4Fi7hHeB4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9114,
      "output_tokens": 251,
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
          "output_tokens": 251,
          "cache_read_input_tokens": 9114,
          "cache_creation_input_tokens": 1919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1919,
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

_source line 11 · 2026-05-10T19:27:23.068Z_

<details><summary>↩ Tool result · `toolu_01G27BqnAxsWmu4hnScXren2`</summary>

```text
Web search results for query: "arXiv 2601.10306 EAPO Group-Relative Evidence Reward"

Links: [{"title":"[2601.10306] Evidence-Augmented Policy Optimization with Reward Co-Evolution for Long-Context Reasoning","url":"https://arxiv.org/abs/2601.10306"},{"title":"Evidence-Augmented Policy Optimization with Reward Co-Evolution for Long-Context Reasoning","url":"https://arxiv.org/html/2601.10306"},{"title":"Evidence-Augmented Policy Optimization with Reward Co-Evolution for","url":"https://arxiv.org/pdf/2601.10306"},{"title":"[2601.23058] From Absolute to Relative: Rethinking Reward Shaping in Group-Based Reinforcement Learning","url":"https://arxiv.org/abs/2601.23058"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiv.org/html/2601.05242v1"},{"title":"GDPO: Group reward-Decoupled Normalization Policy ...","url":"https://www.facebook.com/groups/DeepNetGroup/posts/2701204513605747/"},{"title":"[2601.05242] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiv.org/abs/2601.05242"},{"title":"IRPM: Intergroup Relative Preference Modeling for Pointwise Generative Reward Models","url":"https://arxiv.org/html/2601.00677"},{"title":"From Absolute to Relative: Rethinking Reward Shaping in Group-Based Reinforcement Learning","url":"https://arxiv.org/html/2601.23058"},{"title":"Your Group-Relative Advantage Is Biased","url":"https://arxiv.org/pdf/2601.08521"}]

Based on the search results, here's information about arXiv paper 2601.10306:

The paper is titled "Evidence-Augmented Policy Optimization with Reward Co-Evolution for Long-Context Reasoning" by Xin Guan, Zijian Li, Shen Huang, Pengjun Xie, Jingren Zhou, and Jiuxin Cao from Tongyi Lab at Alibaba Group, proposing EAPO (Evidence-Augmented Policy Optimization).

**Main Problem and Solution:**
The paper addresses how applying reinforcement learning to long-context scenarios is hindered by sparsity of outcome rewards, which fails to penalize ungrounded "lucky guesses," leaving evidence retrieval largely unsupervised.

**Group-Relative Evidence Reward:**
EAPO introduces a specialized RL algorithm where a reward model computes a Group-Relative Evidence Reward, providing dense process supervision to explicitly improve evidence quality. This dense, group-relative evidence reward provides fine-grained supervision at the process level, ensuring the model is rewarded not just for being right, but for being right for the high-quality evidence.

**Additional Mechanism:**
To sustain accurate supervision throughout training, the paper incorporates an Adaptive Reward-Policy Co-Evolution mechanism that iteratively refines the reward model using outcome-consistent rollouts to sharpen its discriminative capability.

**Results:**
Comprehensive evaluations across eight benchmarks demonstrate that EAPO significantly enhances long-context reasoning performance compared to state-of-the-art baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da39ff45-1a66-42cc-a21a-5c0958e6fc9c",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "b70fc4c4-ba21-4f12-bd43-ee342064518c",
  "sourceToolAssistantUUID": "da39ff45-1a66-42cc-a21a-5c0958e6fc9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:27:23.526Z_

<details><summary>↩ Tool result · `toolu_01LVgYJJAwzfKLiKH51hUxAd`</summary>

```text
Web search results for query: "arXiv 2602.21628 RuCL rubric-stratified curriculum GRPO"

Links: [{"title":"[2602.21628] RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning","url":"https://arxiv.org/abs/2602.21628"},{"title":"RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning","url":"https://arxiv.org/html/2602.21628"},{"title":"Training AI Co-Scientists Using Rubric Rewards","url":"https://arxiv.org/html/2512.23707"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=rubric-based+approaches"},{"title":"Curriculum Learning for Efficient Chain-of-Thought Distillation via Structure-Aware Masking and GRPO","url":"https://arxiv.org/html/2602.17686"},{"title":"Learning Query-Specific Rubrics from Human Preferences for DeepResearch Report Generation","url":"https://arxiv.org/html/2602.03619v1"},{"title":"Stratified GRPO: Handling Structural Heterogeneity in Reinforcement Learning of LLM Search Agents","url":"https://arxiv.org/html/2510.06214v1"},{"title":"Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning","url":"https://arxiv.org/html/2508.16949v3"},{"title":"Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains","url":"https://arxiv.org/html/2507.17746v2"},{"title":"[2602.17686] Curriculum Learning for Efficient Chain-of-Thought Distillation via Structure-Aware Masking and GRPO","url":"https://arxiv.org/abs/2602.17686"}]

Based on the search results, I found the paper you're looking for:

**RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning** (arXiv:2602.21628)

**Key Details:**

The paper proposes Stratified Rubric-based Curriculum Learning (RuCL), a novel framework that reformulates curriculum learning by shifting the focus from data selection to reward design.

By stratifying evaluation rubrics into foundational and advanced categories, RuCL aligns reward signals with the model's evolving capabilities.

**Problem Addressed:**
The work addresses issues with outcome-only supervision that risks reward hacking (where models learn spurious reasoning patterns to satisfy final answer checks), and the computational costs and inefficient training dynamics of rubric-based approaches that treat all rubrics as equally learnable.

**Integration with GRPO:**
The framework is integrated with GRPO (Group Relative Policy Optimization), and this approach effectively mitigates reward hacking and training instability.

**Results:**
Extensive experiments on various visual reasoning benchmarks show that RuCL yields a remarkable +7.83% average improvement over the Qwen2.5-VL-7B model, achieving a state-of-the-art accuracy of 60.06%.

The paper was submitted on February 25, 2026, with the latest version (v2) updated on March 3, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52794668-57b1-46ed-b8c8-939bb095e520",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "861a57dc-7e81-4f4d-bde7-0700cb640862",
  "sourceToolAssistantUUID": "52794668-57b1-46ed-b8c8-939bb095e520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:27:25.095Z_

<details><summary>↩ Tool result · `toolu_01D3PibKPCMwDp7uHwmptD69`</summary>

```text
Web search results for query: "arXiv 2605.00199 RSAT NLI faithfulness reward table reasoning"

Links: [{"title":"RSAT: Structured Attribution Makes Small Language Models Faithful Table Reasoners","url":"https://arxiv.org/html/2605.00199"},{"title":"[2605.00199] RSAT: Structured Attribution Makes Small Language Models Faithful Table Reasoners","url":"https://arxiv.org/abs/2605.00199"},{"title":"Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of Retrieval Augmented Generation","url":"https://arxiv.org/html/2505.21072v1"},{"title":"Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS","url":"https://arxiv.org/html/2604.10734"},{"title":"Rewarding Faithful Reasoning in Retrieval-Augmented ...","url":"https://arxiv.org/pdf/2510.13272"},{"title":"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision","url":"https://arxiv.org/html/2512.18196"},{"title":"FaithLens: Detecting and Explaining Faithfulness Hallucination","url":"https://arxiv.org/html/2512.20182v1"},{"title":"HalluScan: A Systematic Benchmark for Detecting and Mitigating Hallucinations in Instruction-Following LLMs","url":"https://arxiv.org/html/2605.02443v1"},{"title":"Scope: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation","url":"https://arxiv.org/html/2502.13674"},{"title":"Breaking the Trade-Off Between Faithfulness and Expressiveness for Large Language Models","url":"https://arxiv.org/html/2508.18651"}]

Based on the search results, I found detailed information about the arXiv paper 2605.00199:

## RSAT: Structured Attribution Makes Small Language Models Faithful Table Reasoners

RSAT is a method that trains small language models (SLMs, 1–8B) to produce step-by-step reasoning with cell-level citations grounded in table evidence.

### Training Approach

The method uses a two-phase training process:

1. Phase 1 (SFT) teaches a structured JSON output format from verified reasoning traces.

2. Phase 2 (GRPO) optimizes a composite reward centered on NLI-based faithfulness, alongside citation validity and parsimony.

### Key Results

Across six models from two families—Qwen 2.5 (1.5B/3B/7B) and Llama 3 (1B/3B/8B)—RSAT improves faithfulness 3.7 × over SFT alone (0.224 → 0.826), with near-perfect citation validity (0.992).

### Faithfulness Evaluation

Faithfulness scoring uses DeBERTa-v3-base NLI (cross-encoder/nli-deberta-v3-base) during both training and evaluation, ensuring metric consistency. Faithfulness is both the training reward and the primary evaluation metric, computed by the same DeBERTa-v3 NLI model.

Ablations show the faithfulness reward is essential: removing it drops faithfulness from 0.97 to 0.03.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "540991f0-19b4-4b61-9ce2-c7fe23597109",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "254292d0-f470-4ccf-a351-731f1af04b93",
  "sourceToolAssistantUUID": "540991f0-19b4-4b61-9ce2-c7fe23597109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:27:26.849Z_

<details><summary>↩ Tool result · `toolu_01DJVd48BJAxNSH6byKnJrpA`</summary>

```text
Web search results for query: "arXiv 2604.10633 ProUIE stepwise structural rewards GRPO"

Links: [{"title":"ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction","url":"https://arxiv.org/html/2604.10633"},{"title":"[2604.10633] ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction","url":"https://arxiv.org/abs/2604.10633"},{"title":"Reward-SQL: Boosting Text-to-SQL via Stepwise Reasoning and Process-Supervised Rewards","url":"https://arxiv.org/html/2505.04671"},{"title":"IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning","url":"https://arxiv.org/html/2604.15148"},{"title":"Stepwise Credit Assignment for GRPO on Flow-Matching Models","url":"https://arxiv.org/html/2603.28718"},{"title":"RadAgent: A tool-using AI agent for stepwise interpretation of chest computed tomography","url":"https://arxiv.org/html/2604.15231"},{"title":"Alleviating Sparse Rewards by Modeling Step-Wise and Long-Term Sampling Effects in Flow-Based GRPO","url":"https://arxiv.org/html/2602.06422"},{"title":"Latent-GRPO: Group Relative Policy Optimization for Latent Reasoning","url":"https://arxiv.org/html/2604.27998"},{"title":"GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning","url":"https://arxiv.org/html/2604.20659"},{"title":"Reinforcing 3D Understanding in Point-VLMs via Geometric Reward Credit Assignment","url":"https://arxiv.org/html/2604.21160"}]

I found the paper! Here's what I discovered about arXiv 2604.10633:

## ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction

ProUIE is a Macro-to-Micro progressive learning approach that improves UIE without introducing any external information.

### Three-Stage Approach

ProUIE consists of three stages: (i) macro-level Complete Modeling (CM), which learns NER, RE, and EE along their intrinsic difficulty order on the full training data to build a unified extraction foundation, (ii) meso-level Streamlined Alignment (SA), which operates on sampled data with simplified target formats, streamlining and regularizing structured outputs to make them more concise and controllable, and (iii) micro-level Deep Exploration (DE), which applies GRPO with stepwise fine-grained rewards (SFR) over structural units to guide exploration and improve performance.

### Stepwise Fine-Grained Rewards (SFR)

For NER, SFR defines stepwise rewards at the entity-type and entity-value levels; for RE, at the relation-type, relation-instance, and entity-pair levels; and for EE, at the event-type, trigger, role, and argument levels. By shaping rewards from coarse to fine, DE can directly correct structural errors while still using only the original training data.

### Results

Extensive experiments on 36 public datasets demonstrate that ProUIE consistently outperforms strong baselines, and further delivers clear gains in large-scale production-oriented information extraction.

The paper was published on April 12, 2026, and addresses universal information extraction (UIE) tasks including named entity recognition (NER), relation extraction (RE), and event extraction (EE).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42e53535-3aae-4b9a-90d9-936a3517a17e",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "1f8a8115-e7f9-4ad0-a78c-c1028f18ca13",
  "sourceToolAssistantUUID": "42e53535-3aae-4b9a-90d9-936a3517a17e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T19:27:30.135Z_

Good, all four papers exist. Now let me fetch the actual arXiv pages to get more specific details -- particularly around the model used in ProUIE and the exact results for EAPO.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f8a8115-e7f9-4ad0-a78c-c1028f18ca13",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSRjLjqk1iwTL3eMq2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf627e4f-def7-4096-9208-44219089b07a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUNvgx1Gr1ogLYAHS1uVFY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2625,
      "cache_creation_input_tokens": 1190,
      "cache_read_input_tokens": 11033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1190,
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

_source line 16 · 2026-05-10T19:27:33.035Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GoELYtbZ5ypqcbK6ikxN8Q`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.10633",
  "prompt": "Extract: 1) What base model does ProUIE use (e.g., Qwen3-4B, Qwen2.5, etc.)? 2) What is the exact average F1 score reported? 3) Does it use GRPO with stepwise structural rewards? 4) List the main results/numbers from the abstract or introduction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf627e4f-def7-4096-9208-44219089b07a",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSRjLjqk1iwTL3eMq2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e95d7a0e-aae1-41e2-a460-6d19226c6db6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUNvgx1Gr1ogLYAHS1uVFY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2625,
      "cache_creation_input_tokens": 1190,
      "cache_read_input_tokens": 11033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1190,
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

_source line 17 · 2026-05-10T19:27:36.389Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U34mEZ63EjXMdNndAVNzAc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.10306",
  "prompt": "Extract: 1) What exact method does EAPO propose? 2) Does it use \"Group-Relative Evidence Reward with Adaptive Reward-Policy Co-Evolution\"? 3) What are the exact improvement numbers? Does it claim +5.1% over vanilla GRPO on 8 QA benchmarks? 4) What benchmarks does it evaluate on? List specific numbers if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e95d7a0e-aae1-41e2-a460-6d19226c6db6",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSRjLjqk1iwTL3eMq2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8dcc2a0-6700-434c-99a4-edf918b581b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUNvgx1Gr1ogLYAHS1uVFY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2625,
      "cache_creation_input_tokens": 1190,
      "cache_read_input_tokens": 11033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1190,
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

_source line 18 · 2026-05-10T19:27:37.853Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SXvtMLsvVidP41fDwhJauN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.21628",
  "prompt": "Extract: 1) Does RuCL use \"rubric-stratified curriculum with GRPO\"? 2) Does it claim +7.83% average improvement? 3) What base model is used? 4) What specific benchmarks and results are reported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8dcc2a0-6700-434c-99a4-edf918b581b1",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSRjLjqk1iwTL3eMq2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b3c8038-4149-4f7e-884d-0c60046c5310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUNvgx1Gr1ogLYAHS1uVFY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2625,
      "cache_creation_input_tokens": 1190,
      "cache_read_input_tokens": 11033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1190,
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

### Tool result

_source line 19 · 2026-05-10T19:27:38.039Z_

<details><summary>↩ Tool result · `toolu_01GoELYtbZ5ypqcbK6ikxN8Q`</summary>

```text
Based on the web page content provided, here's what can be determined:

1) **Base model**: Not specified in the abstract or visible content. The page only mentions ProUIE "uses a smaller backbone" compared to baselines, but doesn't name the specific model.

2) **Exact F1 score**: Not reported in the abstract. The abstract states the method "outperforming strong instruction-tuned baselines on average for NER and RE" but no specific numerical F1 scores are provided.

3) **GRPO with stepwise rewards**: Yes, confirmed. The abstract explicitly states: "applies GRPO with stepwise fine-grained rewards (SFR) over structural units to guide exploration and improve performance."

4) **Main results from abstract**:
   - Three-stage approach: Complete Modeling (macro), Streamlined Alignment (meso), and Deep Exploration (micro)
   - Tested on "36 public datasets"
   - Improves unified extraction for NER, RE, and EE
   - Achieves better performance than instruction-tuned baselines while using a smaller model
   - "Demonstrates clear gains in large-scale production-oriented information extraction"

The full paper would need to be accessed for specific F1 scores and base model details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e95d7a0e-aae1-41e2-a460-6d19226c6db6",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "3274f003-4f22-40b3-b7c1-5cdccf86495b",
  "sourceToolAssistantUUID": "e95d7a0e-aae1-41e2-a460-6d19226c6db6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T19:27:39.237Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XJiJi4qairg8CLPtp6Esd2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.00199",
  "prompt": "Extract: 1) Does RSAT use NLI-based faithfulness reward for table reasoning with cell-level citations? 2) Does it use GRPO? 3) What are the exact results? 4) What models does it use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3274f003-4f22-40b3-b7c1-5cdccf86495b",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSRjLjqk1iwTL3eMq2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "482ffb6c-2c5b-4ff3-a419-757774ea8bad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUNvgx1Gr1ogLYAHS1uVFY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2625,
      "cache_creation_input_tokens": 1190,
      "cache_read_input_tokens": 11033,
      "output_tokens": 602,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1190
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2625,
          "output_tokens": 602,
          "cache_read_input_tokens": 11033,
          "cache_creation_input_tokens": 1190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1190,
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

_source line 21 · 2026-05-10T19:27:39.900Z_

<details><summary>↩ Tool result · `toolu_01U34mEZ63EjXMdNndAVNzAc`</summary>

```text
# EAPO Paper Summary

## 1) Exact Method Proposed
EAPO introduces a specialized reinforcement learning algorithm with two key components: (1) a reward model computing "Group-Relative Evidence Reward" for dense process supervision, and (2) an "Adaptive Reward-Policy Co-Evolution mechanism" that iteratively refines the reward model using outcome-consistent rollouts.

## 2) Use of Group-Relative Evidence Reward with Co-Evolution
Yes, confirmed. The abstract explicitly states the approach uses "a Group-Relative Evidence Reward" and incorporates "an Adaptive Reward-Policy Co-Evolution mechanism."

## 3) Exact Improvement Numbers
The provided content does **not include specific improvement percentages**. The abstract only states that EAPO "significantly enhances long-context reasoning performance compared to SOTA baselines" without quantifying the improvements or making claims about "+5.1% over vanilla GRPO."

## 4) Benchmarks Evaluated
The abstract mentions: "Comprehensive evaluations across eight benchmarks" but **does not list specific benchmark names or numerical results** in the content provided. Access to the full PDF would be needed for detailed evaluation metrics and benchmark-specific performance data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8dcc2a0-6700-434c-99a4-edf918b581b1",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "d40107de-382e-4c2f-85c6-f4ad23049d03",
  "sourceToolAssistantUUID": "c8dcc2a0-6700-434c-99a4-edf918b581b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:27:41.183Z_

<details><summary>↩ Tool result · `toolu_01SXvtMLsvVidP41fDwhJauN`</summary>

```text
Based on the provided content:

1) **GRPO mention**: The abstract does not mention "GRPO" specifically. It references "Reinforcement Learning with Verifiable Rewards (RLVR)" as the paradigm.

2) **+7.83% improvement**: Yes, this is confirmed. The abstract states the method "yields a remarkable +7.83% average improvement over the Qwen2.5-VL-7B model."

3) **Base model**: The Qwen2.5-VL-7B model serves as the baseline for evaluation.

4) **Benchmarks and results**: The document mentions "various visual reasoning benchmarks" without specifying individual benchmark names. The only concrete result provided is "state-of-the-art accuracy of 60.06%" (achieved after the improvement).

**Note**: The provided content is the paper's abstract and metadata page only. Specific benchmark names, detailed results, and complete technical details would require viewing the full PDF or HTML version of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b3c8038-4149-4f7e-884d-0c60046c5310",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "0de7cf01-abf6-4b13-a9d5-fb2065ce0802",
  "sourceToolAssistantUUID": "9b3c8038-4149-4f7e-884d-0c60046c5310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T19:27:43.173Z_

<details><summary>↩ Tool result · `toolu_01XJiJi4qairg8CLPtp6Esd2`</summary>

```text
# RSAT Research Findings

**1) NLI-based faithfulness reward:**
Yes. The abstract states that Phase 2 "optimizes a composite reward centered on NLI-based faithfulness, alongside citation validity and parsimony."

**2) GRPO usage:**
Yes. The method employs "Phase 2 (GRPO)" to optimize the reward function for cell-level citations grounded in table evidence.

**3) Exact results:**
- Faithfulness improvement: "3.7× over SFT alone (0.224→0.826)"
- Citation validity: "near-perfect citation validity (0.992)"
- Post-hoc attribution comparison: "collapses below 13% format success"
- Ablation finding: "removing it drops faithfulness from 0.97 to 0.03"

**4) Models tested:**
The research evaluates six models across two families:
- **Qwen 2.5:** 1.5B, 3B, and 7B variants
- **Llama 3:** 1B, 3B, and 8B variants
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "482ffb6c-2c5b-4ff3-a419-757774ea8bad",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "83120558-f83f-4603-a1b9-aecd63ed7e13",
  "sourceToolAssistantUUID": "482ffb6c-2c5b-4ff3-a419-757774ea8bad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T19:27:46.486Z_

Good. I have the abstracts but need more detail on ProUIE's base model and F1 score, and EAPO's specific improvement numbers. Let me fetch the full HTML versions of those papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83120558-f83f-4603-a1b9-aecd63ed7e13",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSSw8CARSxL8eChtKiu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81e405e3-6c53-4e78-ab8a-1273e1de6517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkaHGQFsAa7uYHshVNwmbV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4479,
      "cache_read_input_tokens": 12223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4479,
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

_source line 25 · 2026-05-10T19:27:49.352Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KMJx1oosvHZ4Sm9sbpJ4L1`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.10633",
  "prompt": "Find: 1) What specific base model does ProUIE use? (e.g. Qwen3-4B, Qwen2.5-7B, LLaMA, etc.) 2) What is the average F1 score reported? Look for \"71.17\" or any avg F1 number. 3) List any F1 scores from the main results table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81e405e3-6c53-4e78-ab8a-1273e1de6517",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSSw8CARSxL8eChtKiu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe3a38d7-17b8-43bc-8508-232368cad73d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkaHGQFsAa7uYHshVNwmbV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4479,
      "cache_read_input_tokens": 12223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4479,
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

_source line 26 · 2026-05-10T19:27:51.341Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017uj6YVmTXsoLB61YswNirE`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.10306",
  "prompt": "Find: 1) Does EAPO claim +5.1% improvement over vanilla GRPO? 2) What are the exact numerical results and improvement percentages? 3) What specific benchmarks are evaluated? 4) What base model is used? Look for specific improvement numbers over GRPO or other baselines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe3a38d7-17b8-43bc-8508-232368cad73d",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSSw8CARSxL8eChtKiu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5ccee71-904c-4a90-8461-cba27670d486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkaHGQFsAa7uYHshVNwmbV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4479,
      "cache_read_input_tokens": 12223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4479,
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

_source line 27 · 2026-05-10T19:27:53.015Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AN7T8FLntnb3JswZ6ajMdC`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.21628",
  "prompt": "Find: 1) Does RuCL use GRPO specifically? Search for mentions of \"GRPO\" or \"Group Relative Policy Optimization\". 2) What is the exact training algorithm used? 3) What specific benchmarks are evaluated and what are the individual results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5ccee71-904c-4a90-8461-cba27670d486",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSSw8CARSxL8eChtKiu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f9bf343-7010-48b4-8114-289e51a31805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkaHGQFsAa7uYHshVNwmbV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4479,
      "cache_read_input_tokens": 12223,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 475,
          "cache_read_input_tokens": 12223,
          "cache_creation_input_tokens": 4479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4479,
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

_source line 28 · 2026-05-10T19:27:53.876Z_

<details><summary>↩ Tool result · `toolu_01KMJx1oosvHZ4Sm9sbpJ4L1`</summary>

```text
# ProUIE Research Summary

## 1. Base Model
ProUIE uses **Qwen3-4B** as its backbone model, as stated in the implementation details: "We instantiate ProUIE as a 4B-parameter LLM-based extractor (ProUIE (4B)), built on the Qwen3-4B backbone."

## 2. Average F1 Score
The reported average F1 scores vary by task:
- **NER**: 79.44 F1
- **RE**: 71.17 F1
- **EE**: 61.73 F1 (mixed results across benchmarks)

## 3. Sample F1 Scores from Main Results

**NER highlights:**
- CoNLL2003: 92.41
- bc4chemd: 91.97
- multiNERD: 95.91

**RE highlights:**
- NYT: 96.41
- SciERC: 46.76
- ADE_corpus: 84.30

**EE highlights:**
- PHEE argument extraction: 71.86
- ACE2005 trigger: 70.65

The paper acknowledges weaker EE performance, noting: "ProUIE shows mixed performance on EE...underperforms the strongest baseline for both triggers and arguments."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe3a38d7-17b8-43bc-8508-232368cad73d",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "49b84216-1f5c-4450-a569-dbb068f02dd4",
  "sourceToolAssistantUUID": "fe3a38d7-17b8-43bc-8508-232368cad73d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T19:27:55.891Z_

<details><summary>↩ Tool result · `toolu_017uj6YVmTXsoLB61YswNirE`</summary>

```text
# EAPO Performance Analysis

## 1. Does EAPO claim +5.1% improvement over vanilla GRPO?

Yes. For the Qwen3-30B-A3B-Thinking model, EAPO achieves "a substantial +5.1% gain, achieving a score of 63.1%" compared to the base model's 58.0%.

## 2. Exact numerical results and improvement percentages

**Qwen3-30B-A3B-Thinking results:**
- Base model: 58.0%
- GRPO: 59.2% (+1.2%)
- EAPO: 63.1% (+5.1%)

**Qwen3-30B-A3B-Instruct results:**
- Base model: 48.1%
- GRPO: 53.1% (+5.0%)
- EAPO: 55.6% (+7.5%)

**Qwen3-14B results:**
- Base model: 53.2%
- GRPO: 53.8% (+0.6%)
- EAPO: 55.0% (+1.8%)

## 3. Specific benchmarks evaluated

Eight benchmarks across three categories: SEAL-0, SEAL-Hard, HotpotQA, MuSiQue, 2WikiMultihopQA, Single-Document QA, Multi-Document QA, and Long Structured-Data QA.

## 4. Base models used

Three models tested: Qwen3-14B (Dense), Qwen3-30B-A3B-Instruct (MoE), and Qwen3-30B-A3B-Thinking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5ccee71-904c-4a90-8461-cba27670d486",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "17e05ef9-8a29-447c-8441-c2137e5af683",
  "sourceToolAssistantUUID": "d5ccee71-904c-4a90-8461-cba27670d486",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T19:28:00.216Z_

<details><summary>↩ Tool result · `toolu_01AN7T8FLntnb3JswZ6ajMdC`</summary>

```text
# RuCL Framework Analysis

## 1. Does RuCL use GRPO specifically?

Yes. The paper explicitly states: "We optimize this objective using Group Relative Policy Optimization (GRPO)" and notes that GRPO is "a stable policy-gradient method for RLVR."

## 2. Training Algorithm Details

RuCL employs GRPO as its core optimization mechanism. Rather than requiring a separate critic network, GRPO leverages group-based reward statistics for advantage estimation. The framework samples multiple outputs per input query, normalizes rewards against group statistics, and applies PPO-style clipped objectives with KL-divergence regularization.

The complete reward function combines rule-based answer verification with dynamically-weighted rubric components: foundational rubrics receive initial emphasis, then gradually transition to advanced rubrics as the model demonstrates stable proficiency.

## 3. Benchmark Results (7 Benchmarks Evaluated)

**Mathematical Reasoning:**
- MathVerse: 54.14% (↑5.16% vs baseline)
- MathVision: 28.88% (↑4.70%)
- MathVista: 74.10% (↑3.90%)
- WeMATH: 71.49% (↑12.97%)

**General Visual Reasoning:**
- MMMU: 56.67% (↑5.67%)
- LogicVista: 49.66% (↑10.40%)
- Counting: 85.50% (↑12.00%)

**Overall Average:** 60.06% across all benchmarks, representing a +7.83% improvement over the Qwen2.5-VL-7B baseline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f9bf343-7010-48b4-8114-289e51a31805",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "dd9cf566-9e30-45fd-8215-5fc423b28f0b",
  "sourceToolAssistantUUID": "6f9bf343-7010-48b4-8114-289e51a31805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T19:28:03.353Z_

Now I have comprehensive data on all four papers. Let me also verify the specific claim about EAPO's "+5.1% over vanilla GRPO" more precisely -- the search results suggest the +5.1% is over the **base model**, not over vanilla GRPO. Let me clarify this.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd9cf566-9e30-45fd-8215-5fc423b28f0b",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSUC1fihQptkujwp6HE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba51d7ff-d17b-48a3-8cb0-bf3efa9f180f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJ6ct9GQ9hjZNhfyxadqmz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1665,
      "cache_read_input_tokens": 16702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1665,
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

_source line 32 · 2026-05-10T19:28:07.151Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VTvMSipjeDUkVyAgGo6Zjt`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.10306",
  "prompt": "I need to clarify: Is the +5.1% improvement relative to the BASE MODEL or relative to VANILLA GRPO? The claim to verify is \"+5.1% over vanilla GRPO on 8 QA benchmarks\". Look at the results table for Qwen3-30B-A3B-Thinking: base=58.0, GRPO=59.2, EAPO=63.1. Is the +5.1% calculated as (63.1 - 58.0) = +5.1 over base, or (63.1 - 59.2) = +3.9 over GRPO? Also check if there's any claim specifically about \"+5.1% over vanilla GRPO\" in the abstract or conclusion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba51d7ff-d17b-48a3-8cb0-bf3efa9f180f",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSUC1fihQptkujwp6HE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afb7aa38-cfd4-46f8-8728-df61e8ef1512",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJ6ct9GQ9hjZNhfyxadqmz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1665,
      "cache_read_input_tokens": 16702,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1665
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 323,
          "cache_read_input_tokens": 16702,
          "cache_creation_input_tokens": 1665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1665,
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

_source line 33 · 2026-05-10T19:28:10.763Z_

<details><summary>↩ Tool result · `toolu_01VTvMSipjeDUkVyAgGo6Zjt`</summary>

```text
# Analysis of the +5.1% Improvement Claim

Based on Table 1 in the paper, the improvement metrics are:

- **Qwen3-30B-A3B-Thinking baseline**: 58.0%
- **+ GRPO**: 59.2% (+1.2%)
- **+ EAPO**: 63.1% (+5.1%)

The +5.1% figure represents improvement over the **base model** (58.0%), not over GRPO. The actual EAPO gain over vanilla GRPO is +3.9 percentage points (63.1 - 59.2).

The abstract states: "Comprehensive evaluations across eight benchmarks demonstrate that EAPO **significantly enhances** long-context reasoning performance." This language describes relative improvements without specifying the exact baseline comparison. The paper's primary claim emphasizes EAPO's superiority versus GRPO across "diverse LLMs," but the headline numbers in their results table conflate improvements from both the base model and the RL method itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afb7aa38-cfd4-46f8-8728-df61e8ef1512",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a27b09cab7f485136",
  "type": "user",
  "uuid": "7d04c74b-3401-4b12-af03-316295bece9f",
  "sourceToolAssistantUUID": "afb7aa38-cfd4-46f8-8728-df61e8ef1512",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-10T19:28:43.913Z_

Now I have all the details needed to provide a comprehensive verification report.

---

## Verification Results for All Four Papers

### 1. ProUIE (arXiv:2604.10633, Apr 2026)

**Existence:** CONFIRMED. The paper exists: "ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction."

**Claim: Uses Qwen3-4B** -- CONFIRMED. The paper states: "We instantiate ProUIE as a 4B-parameter LLM-based extractor (ProUIE (4B)), built on the Qwen3-4B backbone."

**Claim: Uses GRPO with stepwise structural rewards** -- PARTIALLY ACCURATE. The paper uses GRPO with what it calls "Stepwise Fine-grained Rewards (SFR)" over structural units. The proposal calls them "stepwise structural rewards," which is a reasonable paraphrase of "stepwise fine-grained rewards over structural units." The rewards are defined at different granularity levels per task (entity-type/value for NER, relation-type/instance/entity-pair for RE, event-type/trigger/role/argument for EE).

**Claim: "71.17 avg F1" on UIE benchmarks** -- MISLEADING. The number 71.17 exists in the paper but it is the F1 on **RE (Relation Extraction) only**, not an overall "avg F1" across all UIE benchmarks. The actual per-task averages are:
- NER: 79.44 F1
- RE: 71.17 F1
- EE: 61.73 F1

Calling 71.17 the "avg F1 on UIE benchmarks" is inaccurate; it cherry-picks the RE-only result.

---

### 2. EAPO (arXiv:2601.10306, Jan 2026)

**Existence:** CONFIRMED. The paper exists: "Evidence-Augmented Policy Optimization with Reward Co-Evolution for Long-Context Reasoning."

**Claim: Introduces "Group-Relative Evidence Reward with Adaptive Reward-Policy Co-Evolution"** -- CONFIRMED. The paper proposes exactly these two components: (1) a Group-Relative Evidence Reward for dense process supervision, and (2) an Adaptive Reward-Policy Co-Evolution mechanism.

**Claim: "+5.1% over vanilla GRPO on 8 QA benchmarks"** -- INACCURATE. The +5.1% figure exists in the paper but refers to the improvement **over the base model** (Qwen3-30B-A3B-Thinking: 58.0% to 63.1%), NOT over vanilla GRPO. The actual improvement over vanilla GRPO is **+3.9 percentage points** (59.2% to 63.1%). The research proposal misattributes the baseline for this number. Results were evaluated on 8 benchmarks across long-context reasoning tasks (SEAL-0, SEAL-Hard, HotpotQA, MuSiQue, 2WikiMultihopQA, and others).

---

### 3. RuCL (arXiv:2602.21628, Feb 2026)

**Existence:** CONFIRMED. The paper exists: "RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning."

**Claim: "rubric-stratified curriculum with GRPO"** -- CONFIRMED. The paper explicitly uses GRPO as its optimization algorithm and introduces stratified rubric-based curriculum learning that transitions from foundational to advanced rubrics.

**Claim: "+7.83% avg improvement"** -- CONFIRMED. The paper reports +7.83% average improvement over the Qwen2.5-VL-7B baseline across 7 visual reasoning benchmarks, achieving 60.06% state-of-the-art accuracy. Individual improvements range from +3.90% (MathVista) to +12.97% (WeMATH).

---

### 4. RSAT (arXiv:2605.00199, May 2026)

**Existence:** CONFIRMED. The paper exists: "RSAT: Structured Attribution Makes Small Language Models Faithful Table Reasoners."

**Claim: "NLI-based faithfulness reward for table reasoning with cell-level citations"** -- CONFIRMED. The paper uses a two-phase approach: Phase 1 (SFT) teaches structured JSON output with cell-level citations, and Phase 2 (GRPO) optimizes a composite reward centered on NLI-based faithfulness (using DeBERTa-v3-base NLI), alongside citation validity and parsimony. Faithfulness improves 3.7x over SFT alone (0.224 to 0.826), with near-perfect citation validity (0.992). Tested across Qwen 2.5 (1.5B/3B/7B) and Llama 3 (1B/3B/8B).

---

## Summary of Issues Found

| Paper | Exists? | Claims Accurate? |
|-------|---------|-----------------|
| ProUIE (2604.10633) | Yes | "71.17 avg F1" is MISLEADING -- that is RE-only F1, not the overall average |
| EAPO (2601.10306) | Yes | "+5.1% over vanilla GRPO" is WRONG -- it is +5.1% over the base model; the gain over GRPO is +3.9% |
| RuCL (2602.21628) | Yes | Claims are ACCURATE |
| RSAT (2605.00199) | Yes | Claims are ACCURATE |

The two problematic citations are ProUIE (misrepresented metric scope) and EAPO (misattributed baseline for the improvement figure).

Sources:
- [ProUIE (arXiv:2604.10633)](https://arxiv.org/abs/2604.10633)
- [EAPO (arXiv:2601.10306)](https://arxiv.org/abs/2601.10306)
- [RuCL (arXiv:2602.21628)](https://arxiv.org/abs/2602.21628)
- [RSAT (arXiv:2605.00199)](https://arxiv.org/abs/2605.00199)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d04c74b-3401-4b12-af03-316295bece9f",
  "isSidechain": true,
  "agentId": "a27b09cab7f485136",
  "requestId": "req_011CauSUy3qJ3y8fxoFA4y1D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9331cd7-ed4b-41a8-89a1-6741a4102e46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wCE9Pudcy3xeWvWaTgUzh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 573,
      "cache_read_input_tokens": 18367,
      "output_tokens": 1532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 573
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1532,
          "cache_read_input_tokens": 18367,
          "cache_creation_input_tokens": 573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 573,
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
