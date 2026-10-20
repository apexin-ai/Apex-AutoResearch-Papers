# Research conversation: Search for "GiGPO verl-agent HuggingFace checkpoints Qwen2.5-7B" and "site:huggingface.co verl-agent GiGPO" and "site:gi

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae6c24d711b3c9137.jsonl`
- **Structured JSON:** [`bf80eaa9c0919809574d.json`](../../sessions/bf/bf80eaa9c0919809574d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-10T19:01:17.457Z_

Search for "GiGPO verl-agent HuggingFace checkpoints Qwen2.5-7B" and "site:huggingface.co verl-agent GiGPO" and "site:github.com verl-agent" to verify that verl-agent has published GiGPO checkpoints on HuggingFace that can be used without retraining. Also search for "GiGPO Group-in-Group Policy Optimization NeurIPS 2025" to confirm GiGPO's venue and reported numbers (90.2% ALFWorld, 75.2% WebShop for w/o std config). Report what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2c71ce81-a737-4243-8ee6-6db7c3c2b875",
  "agentId": "ae6c24d711b3c9137",
  "type": "user",
  "uuid": "4bbd2d53-c999-4314-b78d-2e12c068cb32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T19:01:19.633Z_

I'll search for information about verl-agent's GiGPO checkpoints and the GiGPO paper details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bbd2d53-c999-4314-b78d-2e12c068cb32",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQS3VATuyuCikxZKrTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "02840fe0-8cc8-4259-8905-de8b23fbb7c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EnR3RuM3kuZri32N3cnMve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 584,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T19:01:19.728Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xu4KZ7C8zpbfwUvbsBK4tQ`</summary>

```json
{
  "query": "GiGPO verl-agent HuggingFace checkpoints Qwen2.5-7B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02840fe0-8cc8-4259-8905-de8b23fbb7c0",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQS3VATuyuCikxZKrTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe69aafb-6a1f-4e7e-8271-a5614a668924",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EnR3RuM3kuZri32N3cnMve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 584,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:01:19.747Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ngiBCguoUegK8x1mDmGva`</summary>

```json
{
  "query": "site:huggingface.co verl-agent GiGPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe69aafb-6a1f-4e7e-8271-a5614a668924",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQS3VATuyuCikxZKrTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b5d894ec-97f5-488b-bc92-127966cec473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EnR3RuM3kuZri32N3cnMve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 584,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:01:19.777Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017tQFcNtXkvBxY658eiXy58`</summary>

```json
{
  "query": "site:github.com verl-agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5d894ec-97f5-488b-bc92-127966cec473",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQS3VATuyuCikxZKrTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "96498ed5-6d23-4cf3-ac4d-374646006ac5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EnR3RuM3kuZri32N3cnMve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 584,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T19:01:19.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015J8DLegFkoVUr5Jskuk6t9`</summary>

```json
{
  "query": "GiGPO Group-in-Group Policy Optimization NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96498ed5-6d23-4cf3-ac4d-374646006ac5",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQS3VATuyuCikxZKrTK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6a597c12-21a2-4d4e-badc-33db4ef7d3d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EnR3RuM3kuZri32N3cnMve",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 584,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-10T19:01:26.870Z_

<details><summary>↩ Tool result · `toolu_017ngiBCguoUegK8x1mDmGva`</summary>

```text
Web search results for query: "site:huggingface.co verl-agent GiGPO"

Links: [{"title":"verl-agent - a langfeng01 Collection","url":"https://huggingface.co/collections/langfeng01/verl-agent-684970e8f51babe2a6d98554"},{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld"},{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=step-level+relative+advantage+mechanism"},{"title":"Paper page - Group-in-Group Policy Optimization for LLM Agent Training","url":"https://huggingface.co/papers/2505.10978"},{"title":"verl-0.4.x/README.md · zz1358m/SofT-GRPO-master at main","url":"https://huggingface.co/zz1358m/SofT-GRPO-master/blob/main/verl-0.4.x/README.md"},{"title":"zswzswzsw/GAO_grpo · Hugging Face","url":"https://huggingface.co/zswzswzsw/GAO_grpo"},{"title":"Unlocking Agentic RL Training for GPT-OSS: A Practical Retrospective","url":"https://huggingface.co/blog/LinkedIn/gpt-oss-agentic-rl"},{"title":"https://huggingface.co/api/resolve-cache/datasets/...","url":"https://huggingface.co/api/resolve-cache/datasets/nickhe/GKG-H100-Code-6Aug/2047cd50e281f7f441b84b0e6fb19a32748e8797/verl_zyc/README.md?download=true&etag=%228d4c3f45678be729000d389c8bcf061705581d01%22"},{"title":"zswzswzsw/verl_subquestion · Hugging Face","url":"https://huggingface.co/zswzswzsw/verl_subquestion"}]

Based on the search results, here's what I found about verl-agent and GiGPO on Hugging Face:

## Overview

Open-source models trained via GiGPO and verl-agent are available on Hugging Face, maintained by langfeng01.

## What is GiGPO?

GiGPO (Group-in-Group Policy Optimization) is a novel RL algorithm that achieves fine-grained credit assignment for LLM agents while preserving the appealing properties of group-based RL: critic-free, low memory, and stable convergence.

## How GiGPO Works

GiGPO introduces a two-level structure for estimating relative advantage: at the episode-level, it computes macro relative advantages based on groups of complete trajectories; at the step-level, it introduces an anchor state grouping mechanism that retroactively constructs step-level groups by identifying repeated environment states across trajectories. Actions stemming from the same state are grouped together, enabling micro relative advantage estimation.

## Performance Results

GiGPO achieves performance gains of > 12% on ALFWorld and > 9% on WebShop over the GRPO baseline while maintaining the same GPU memory overhead, identical LLM rollout, and incurring little to no additional time cost.

## Available Models

GiGPO was evaluated on two challenging agent benchmarks, ALFWorld and WebShop, using Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct. Specific models like GiGPO-Qwen2.5-7B-Instruct-ALFWorld and GiGPO-Qwen2.5-7B-Instruct-WebShop are available on the Hugging Face Hub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5d894ec-97f5-488b-bc92-127966cec473",
  "isSidechain": true,
  "promptId": "2c71ce81-a737-4243-8ee6-6db7c3c2b875",
  "agentId": "ae6c24d711b3c9137",
  "type": "user",
  "uuid": "adce9b18-2738-42a1-a289-e222b8acc4d3",
  "sourceToolAssistantUUID": "b5d894ec-97f5-488b-bc92-127966cec473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T19:01:27.612Z_

<details><summary>↩ Tool result · `toolu_017tQFcNtXkvBxY658eiXy58`</summary>

```text
Web search results for query: "site:github.com verl-agent"

Links: [{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengq/verl-agent"},{"title":"GitHub - verl-project/verl: verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework · GitHub","url":"https://github.com/verl-project/verl"},{"title":"GitHub - agentica-project/verl · GitHub","url":"https://github.com/agentica-project/verl"},{"title":"verl-agent/README.md at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/README.md"},{"title":"verl-agent/recipe/hgpo at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/tree/master/recipe/hgpo"},{"title":"Releases · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/releases"},{"title":"verl-agent/examples/data_preprocess/preprocess_search_r1_dataset.py at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/examples/data_preprocess/preprocess_search_r1_dataset.py"},{"title":"verl-agent/verl/trainer/config/ppo_trainer.yaml at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/verl/trainer/config/ppo_trainer.yaml"},{"title":"GitHub - cxcscmu/verl-agent-deepresearch: The deep research agent RL framework for paper https://arxiv.org/abs/2510.06534 · GitHub","url":"https://github.com/cxcscmu/verl-agent-deepresearch"},{"title":"verl-agent/agent_system/environments/base.py at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/agent_system/environments/base.py"}]

Based on the search results, here's what I found about verl-agent:

## Overview

verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper "Group-in-Group Policy Optimization for LLM Agent Training".

## Key Features

**Customizable Memory Module**: verl-agent features a customizable memory module that allows for flexibly choosing what history to include for each step, typically consisting of the current observation along with a concise history summary. Developers can freely define what to include, such as recent steps, key events, summaries, or external knowledge, with no requirement to concatenate the full history.

**Scalability Advantage**: Prior works like RAGEN and Search-R1 concatenate the entire history of states and responses, which causes the context length to grow rapidly with the number of turns, making them difficult to scale to long-horizon scenarios.

**Model Support**: verl-agent supports a wide range of LLMs, including Qwen3, Qwen3-VL, Qwen2.5, LLaMA3.2, Qwen2.5-VL, and others.

**Multi-modal Support**: Beyond text-based agents, verl-agent also supports training vision-language agents, enabling multi-modal reasoning in environments where both visual perception and language understanding are required.

**Environments and Algorithms**: verl-agent offers a diverse set of interactive environments including Search-R1 experiment, embodied AI environments like ALFWorld, visual games such as Sokoban and Gym Cards, and digital interface control tasks like WebShop and AppWorld. verl-agent includes implementations of various RL algorithms, such as GRPO, PPO, DAPO, GSPO, RLOO and a new state-of-the-art algorithm GiGPO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96498ed5-6d23-4cf3-ac4d-374646006ac5",
  "isSidechain": true,
  "promptId": "2c71ce81-a737-4243-8ee6-6db7c3c2b875",
  "agentId": "ae6c24d711b3c9137",
  "type": "user",
  "uuid": "0c8659e1-99e9-4534-8a92-20dc1b60ae52",
  "sourceToolAssistantUUID": "96498ed5-6d23-4cf3-ac4d-374646006ac5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T19:01:29.288Z_

<details><summary>↩ Tool result · `toolu_015J8DLegFkoVUr5Jskuk6t9`</summary>

```text
Web search results for query: "GiGPO Group-in-Group Policy Optimization NeurIPS 2025"

Links: [{"title":"NeurIPS Poster Group-in-Group Policy Optimization for LLM Agent Training","url":"https://neurips.cc/virtual/2025/poster/118123"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | OpenReview","url":"https://openreview.net/forum?id=QXEhBMNrCW"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"[2505.10978] Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/abs/2505.10978"},{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengq/verl-agent"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.10978v1"},{"title":"Paper page - Group-in-Group Policy Optimization for LLM Agent Training","url":"https://huggingface.co/papers/2505.10978"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | Request PDF","url":"https://www.researchgate.net/publication/391857132_Group-in-Group_Policy_Optimization_for_LLM_Agent_Training"},{"title":"NeurIPS Poster GVPO: Group Variance Policy Optimization for Large Language Model Post-Training","url":"https://neurips.cc/virtual/2025/poster/117119"}]

Based on the search results, here's what I found about GiGPO (Group-in-Group Policy Optimization) at NeurIPS 2025:

## Overview

GiGPO is a novel RL algorithm that achieves fine-grained credit assignment for LLM agents while preserving the appealing properties of group-based RL: critic-free, low memory, and stable convergence.

## Key Innovation

GiGPO introduces a two-level structure for estimating relative advantage: at the episode-level, GiGPO computes macro relative advantages based on groups of complete trajectories; at the step-level, GiGPO introduces an anchor state grouping mechanism that retroactively constructs step-level groups by identifying repeated environment states across trajectories.

## Problem Addressed

Recent advances in group-based reinforcement learning have driven frontier large language models in single-turn tasks like mathematical reasoning. However, their scalability to multi-turn LLM agent training remains limited. Unlike static tasks, agent-environment interactions unfold over many steps and often yield sparse or delayed rewards, making credit assignment across individual steps significantly more challenging.

## Performance Results

GiGPO delivers fine-grained per-step credit signals, achieves performance gains of > 12% on ALFWorld and > 9% on WebShop over GRPO, and obtains superior performance on QA tasks (42.1% on 3B and 47.2% on 7B). These gains come without compromising the core strengths of group-based RL (only < 0.002% time cost).

## Evaluation

GiGPO was evaluated on challenging agent benchmarks, including ALFWorld and WebShop, as well as tool-integrated reasoning on search-augmented QA tasks, using Qwen2.5-1.5B/3B/7B-Instruct.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a597c12-21a2-4d4e-badc-33db4ef7d3d0",
  "isSidechain": true,
  "promptId": "2c71ce81-a737-4243-8ee6-6db7c3c2b875",
  "agentId": "ae6c24d711b3c9137",
  "type": "user",
  "uuid": "a22bb633-e16e-4a5d-ab38-561f68f0e5b5",
  "sourceToolAssistantUUID": "6a597c12-21a2-4d4e-badc-33db4ef7d3d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T19:01:29.326Z_

<details><summary>↩ Tool result · `toolu_01Xu4KZ7C8zpbfwUvbsBK4tQ`</summary>

```text
Web search results for query: "GiGPO verl-agent HuggingFace checkpoints Qwen2.5-7B"

Links: [{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop"},{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld"},{"title":"Qwen/Qwen2.5-VL-7B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct"},{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengQ/verl-agent"},{"title":"unsloth/Qwen2.5-VL-7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-GGUF"},{"title":"nvidia/Qwen2.5-VL-7B-Instruct-FP8 · Hugging Face","url":"https://huggingface.co/nvidia/Qwen2.5-VL-7B-Instruct-FP8"},{"title":"Qwen/Qwen2.5-Coder-7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF"},{"title":"Qwen/Qwen2.5-Omni-7B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Omni-7B"},{"title":"nvidia/Qwen2.5-VL-7B-Instruct-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Qwen2.5-VL-7B-Instruct-NVFP4"},{"title":"Qwen/Qwen2.5-7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-GGUF"}]

Based on the web search results, I found relevant information about GiGPO, verl-agent, and Qwen2.5-7B checkpoints on HuggingFace:

## Overview

verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL and is the official code for the paper "Group-in-Group Policy Optimization for LLM Agent Training".

## GiGPO Models on HuggingFace

There is a collection of open-source models trained via GiGPO and verl-agent with 4 items updated June 20. The search results reveal specific GiGPO-trained checkpoints available on HuggingFace:

1. **GiGPO-Qwen2.5-7B-Instruct-WebShop**: This model is trained using GiGPO for the WebShop e-commerce environment.

2. **GiGPO-Qwen2.5-7B-Instruct-ALFWorld**: This model is trained using GiGPO for the ALFRED Embodied Environment.

## Framework Support

verl-agent supports a wide range of LLMs, including Qwen3, Qwen3-VL, Qwen2.5, LLaMA3.2, Qwen2.5-VL, and others. To use these models, users should refer to verl-agent.

## Recent Updates

[2025.05] Code released and paper on GiGPO released, and the performance of GiGPO has improved slightly after the "[2025.06.03] Major Update".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe69aafb-6a1f-4e7e-8271-a5614a668924",
  "isSidechain": true,
  "promptId": "2c71ce81-a737-4243-8ee6-6db7c3c2b875",
  "agentId": "ae6c24d711b3c9137",
  "type": "user",
  "uuid": "94788c87-9e9b-474d-bc50-c56373001ca1",
  "sourceToolAssistantUUID": "fe69aafb-6a1f-4e7e-8271-a5614a668924",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T19:01:31.108Z_

Now let me fetch the NeurIPS paper and arXiv paper to verify the specific performance numbers you mentioned (90.2% ALFWorld, 75.2% WebShop for w/o std config).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94788c87-9e9b-474d-bc50-c56373001ca1",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQSvhuWcatGciD8Zxyu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d7e20224-5f17-4b1c-83d7-3f8d4411d039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01APxHxoHqQ3eGsZVriUhYfU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3226,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 16737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2224,
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

_source line 12 · 2026-05-10T19:01:31.905Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ka2ZdCq5wG7dsMpAEQtQPc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.10978",
  "prompt": "What are the performance numbers for ALFWorld and WebShop without standard deviation configuration? Specifically look for 90.2% ALFWorld and 75.2% WebShop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7e20224-5f17-4b1c-83d7-3f8d4411d039",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQSvhuWcatGciD8Zxyu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fc2738f6-a070-4cdf-ac86-f7c1ff1ab084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01APxHxoHqQ3eGsZVriUhYfU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3226,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 16737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2224,
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

_source line 13 · 2026-05-10T19:01:32.059Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EqZzfxdRY9EUsDr2PtNjde`</summary>

```json
{
  "url": "https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf",
  "prompt": "What are the performance numbers for ALFWorld and WebShop? Look for specific percentages like 90.2% ALFWorld and 75.2% WebShop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc2738f6-a070-4cdf-ac86-f7c1ff1ab084",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQSvhuWcatGciD8Zxyu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "033e3eae-9be4-489c-ba90-4c3aefe3f570",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01APxHxoHqQ3eGsZVriUhYfU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3226,
      "cache_creation_input_tokens": 2224,
      "cache_read_input_tokens": 16737,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3226,
          "output_tokens": 286,
          "cache_read_input_tokens": 16737,
          "cache_creation_input_tokens": 2224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2224,
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

_source line 14 · 2026-05-10T19:01:34.266Z_

<details><summary>↩ Tool result · `toolu_01Ka2ZdCq5wG7dsMpAEQtQPc`</summary>

```text
# Performance Numbers Analysis

Based on the provided arXiv page content, I cannot find the specific performance numbers you're asking about (90.2% for ALFWorld and 75.2% for WebShop).

The abstract mentions that GiGPO "achieves performance gains of > 12% on ALFWorld and > 9% on WebShop over GRPO," but these are comparative improvements rather than absolute performance values. The document does not include detailed numerical results in the visible content.

To locate those specific figures, you would need to access the full paper PDF or HTML version linked on this arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc2738f6-a070-4cdf-ac86-f7c1ff1ab084",
  "isSidechain": true,
  "promptId": "2c71ce81-a737-4243-8ee6-6db7c3c2b875",
  "agentId": "ae6c24d711b3c9137",
  "type": "user",
  "uuid": "83fa9041-02c0-4010-84d4-a51e068370ed",
  "sourceToolAssistantUUID": "fc2738f6-a070-4cdf-ac86-f7c1ff1ab084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T19:01:37.322Z_

<details><summary>↩ Tool result · `toolu_01EqZzfxdRY9EUsDr2PtNjde`</summary>

```text
I apologize, but I cannot extract the specific performance numbers you're requesting from the provided content. The document appears to be a PDF file with encoded/compressed data that doesn't display readable text about ALFWorld and WebShop performance metrics in the format you mentioned (90.2% and 75.2%).

To find these performance numbers, you would need to provide either:
- A readable text version of the document
- The specific page or section containing benchmark results
- A direct link to the source material

If you have access to the original document, I'd be happy to help locate these statistics.

[Binary content (application/pdf, 2MB) also saved to /home/ubuntu/.claude-account-2/projects/-/73cacb99-a11d-4823-af3a-25d235e73069/tool-results/webfetch-1778439694142-d0j5vi.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "033e3eae-9be4-489c-ba90-4c3aefe3f570",
  "isSidechain": true,
  "promptId": "2c71ce81-a737-4243-8ee6-6db7c3c2b875",
  "agentId": "ae6c24d711b3c9137",
  "type": "user",
  "uuid": "fbad3272-d722-449f-b846-35e5c846693e",
  "sourceToolAssistantUUID": "033e3eae-9be4-489c-ba90-4c3aefe3f570",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T19:01:38.978Z_

Let me search more specifically for those performance numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbad3272-d722-449f-b846-35e5c846693e",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQTWRgguhVmwLFzLMSe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "839fc1cc-103a-48a4-9ae4-9c17a0e85da4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011T2wNHjyxuj5F8iFgukd1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3903,
      "cache_read_input_tokens": 18961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3903,
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

_source line 17 · 2026-05-10T19:01:39.455Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JKGLhon8e3ckyFMSC338UC`</summary>

```json
{
  "query": "GiGPO 90.2 ALFWorld 75.2 WebShop performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "839fc1cc-103a-48a4-9ae4-9c17a0e85da4",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQTWRgguhVmwLFzLMSe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7cc78e1a-613c-40ce-8085-6f694237367c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011T2wNHjyxuj5F8iFgukd1T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3903,
      "cache_read_input_tokens": 18961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3903,
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

_source line 18 · 2026-05-10T19:01:39.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tz24tAYd5o1vLfDccUiDVD`</summary>

```json
{
  "query": "\"Group-in-Group Policy Optimization\" ALFWorld WebShop benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cc78e1a-613c-40ce-8085-6f694237367c",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQTWRgguhVmwLFzLMSe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92971a0e-771b-47f8-a158-74079e501ce6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011T2wNHjyxuj5F8iFgukd1T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3903,
      "cache_read_input_tokens": 18961,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 136,
          "cache_read_input_tokens": 18961,
          "cache_creation_input_tokens": 3903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3903,
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

_source line 19 · 2026-05-10T19:01:44.590Z_

<details><summary>↩ Tool result · `toolu_01JKGLhon8e3ckyFMSC338UC`</summary>

```text
Web search results for query: "GiGPO 90.2 ALFWorld 75.2 WebShop performance"

Links: [{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/html/2602.16165"},{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengQ/verl-agent"},{"title":"Phase-Aware Mixture of Experts for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2602.17038"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training - Consensus","url":"https://consensus.app/papers/groupingroup-policy-optimization-for-llm-agent-training-an-feng/ae6de571c22e532d95865b46257f2719/"},{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/html/2603.18859"},{"title":"HiMAC: Hierarchical Macro–Micro Learning for Long-Horizon LLM Agents","url":"https://arxiv.org/html/2603.00977"},{"title":"Graph-Enhanced Policy Optimization in LLM Agent Training","url":"https://arxiv.org/html/2510.26270"},{"title":"Entropy-Modulated Policy Gradients for Long-Horizon LLM ...","url":"https://arxiv.org/pdf/2509.09265"}]

Based on the search results, I found information about GiGPO's performance on ALFWorld and WebShop:

GiGPO achieves 90.8% on ALFWorld and 75.2% on WebShop, which matches the exact numbers in your query. 

GiGPO demonstrates strong performance across both ALFWorld and WebShop benchmarks. More specifically, GiGPO achieves performance improvements of over 12% on ALFWorld and over 9% on WebShop compared to GRPO.

GiGPO injects fine-grained, step-level credit signals that sharpen policy learning of agents over horizons and achieves performance gains of over 12% on ALFWorld and over 9% on WebShop over GRPO. The method achieves fine-grained credit assignment for LLM agents while preserving the appealing properties of group-based RL: critic-free, low memory, and stable convergence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cc78e1a-613c-40ce-8085-6f694237367c",
  "isSidechain": true,
  "promptId": "2c71ce81-a737-4243-8ee6-6db7c3c2b875",
  "agentId": "ae6c24d711b3c9137",
  "type": "user",
  "uuid": "792eb943-5505-4c22-9b47-e0476a4503b1",
  "sourceToolAssistantUUID": "7cc78e1a-613c-40ce-8085-6f694237367c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T19:01:44.786Z_

<details><summary>↩ Tool result · `toolu_01Tz24tAYd5o1vLfDccUiDVD`</summary>

```text
Web search results for query: ""Group-in-Group Policy Optimization" ALFWorld WebShop benchmark results"

Links: [{"title":"[2505.10978] Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/abs/2505.10978"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | OpenReview","url":"https://openreview.net/forum?id=QXEhBMNrCW"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | Request PDF","url":"https://www.researchgate.net/publication/391857132_Group-in-Group_Policy_Optimization_for_LLM_Agent_Training"},{"title":"[2505.10978v2] Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/abs/2505.10978v2"},{"title":"Paper page - Group-in-Group Policy Optimization for LLM Agent Training","url":"https://huggingface.co/papers/2505.10978"},{"title":"Graph-Enhanced Policy Optimization in LLM Agent Training","url":"https://arxiv.org/html/2510.26270"},{"title":"Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks","url":"https://arxiv.org/html/2602.22817"},{"title":"NeurIPS Poster Group-in-Group Policy Optimization for LLM Agent Training","url":"https://neurips.cc/virtual/2025/poster/118123"}]

Based on the search results, here are the key benchmark results for Group-in-Group Policy Optimization (GiGPO) on ALFWorld and WebShop:

## Benchmark Results

GiGPO achieves performance gains of > 12% on ALFWorld and > 9% on WebShop over GRPO. The research evaluated GiGPO using multiple model sizes, including Qwen2.5-1.5B, Qwen2.5-3B, and Qwen2.5-7B-Instruct variants.

## Key Findings

GiGPO is a novel RL algorithm that achieves fine-grained credit assignment for LLM agents while preserving the appealing properties of group-based RL: critic-free, low memory, and stable convergence.

The method effectively captures both global trajectory quality and local step effectiveness without relying on auxiliary models or additional rollouts.

Notably, GiGPO maintains the same GPU memory overhead, identical LLM rollout, and incurs little to no additional time cost while achieving these performance improvements.

The research also evaluated GiGPO on additional tasks beyond the agent benchmarks, with superior performance on QA tasks (42.1% on 3B and 47.2% on 7B).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92971a0e-771b-47f8-a158-74079e501ce6",
  "isSidechain": true,
  "promptId": "2c71ce81-a737-4243-8ee6-6db7c3c2b875",
  "agentId": "ae6c24d711b3c9137",
  "type": "user",
  "uuid": "7b24f573-d1b2-44fc-b505-9def3834b2e5",
  "sourceToolAssistantUUID": "92971a0e-771b-47f8-a158-74079e501ce6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T19:01:46.230Z_

Let me try to access the arXiv HTML version which may be more readable for the specific numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b24f573-d1b2-44fc-b505-9def3834b2e5",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQU4MohnBHMBQykkBHX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b2d2b49-3eef-46d8-80b3-abf9e184cc4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HSBdsg1gpaMXvSqrxbRqui",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1864,
      "cache_read_input_tokens": 22864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1864,
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

_source line 22 · 2026-05-10T19:01:46.802Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KrQwaHQSpmoxneRPmNkzxM`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.10978v1",
  "prompt": "What are the specific performance numbers for ALFWorld and WebShop? Look for exact percentages mentioned in tables or results sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b2d2b49-3eef-46d8-80b3-abf9e184cc4c",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQU4MohnBHMBQykkBHX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6da67b4b-962f-4814-899e-c11afdd9a9f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HSBdsg1gpaMXvSqrxbRqui",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1864,
      "cache_read_input_tokens": 22864,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1864
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 132,
          "cache_read_input_tokens": 22864,
          "cache_creation_input_tokens": 1864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1864,
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

_source line 23 · 2026-05-10T19:01:51.555Z_

<details><summary>↩ Tool result · `toolu_01KrQwaHQSpmoxneRPmNkzxM`</summary>

```text
# GiGPO Performance Results

## ALFWorld (Qwen2.5-1.5B-Instruct)

According to Table 1, GiGPO without standard deviation normalization achieved **86.1% overall success rate**, compared to GRPO's 72.8%. This represents a **13.3 percentage point improvement**.

Breaking down by task category:
- Pick: 96.0%
- Look: 76.5%
- Clean: 91.8%
- Heat: 91.3%
- Cool: 71.7%
- Pick2: 79.5%

## WebShop (Qwen2.5-1.5B-Instruct)

GiGPO achieved a **83.5 score and 67.4% success rate**, compared to GRPO's 75.8 score and 56.8% success rate. This reflects a **10.6 percentage point gain in success rate**.

## 7B Model Performance

With the larger Qwen2.5-7B-Instruct model, GiGPO demonstrated similar advantages: **12.6% improvement on ALFWorld** and **9.1% on WebShop** over the GRPO baseline, while maintaining identical computational costs and memory overhead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6da67b4b-962f-4814-899e-c11afdd9a9f4",
  "isSidechain": true,
  "promptId": "2c71ce81-a737-4243-8ee6-6db7c3c2b875",
  "agentId": "ae6c24d711b3c9137",
  "type": "user",
  "uuid": "d2d48ff6-b010-41ab-a6f8-82145d551c29",
  "sourceToolAssistantUUID": "6da67b4b-962f-4814-899e-c11afdd9a9f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T19:02:00.379Z_

Based on my comprehensive search, here's what I found:

## Summary of Findings

### HuggingFace Checkpoints Verification
**CONFIRMED:** verl-agent has published GiGPO-trained checkpoints on HuggingFace that can be used without retraining:
- **GiGPO-Qwen2.5-7B-Instruct-WebShop** - available at [https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop](https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop)
- **GiGPO-Qwen2.5-7B-Instruct-ALFWorld** - available at [https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld](https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld)

These models are part of the **verl-agent collection** on HuggingFace: [https://huggingface.co/collections/langfeng01/verl-agent-684970e8f51babe2a6d98554](https://huggingface.co/collections/langfeng01/verl-agent-684970e8f51babe2a6d98554)

### GitHub Repository
**CONFIRMED:** The official verl-agent repository is at [https://github.com/langfengQ/verl-agent](https://github.com/langfengQ/verl-agent), which is the official code for the GiGPO paper "Group-in-Group Policy Optimization for LLM Agent Training."

### Venue and Paper Details
**CONFIRMED:** GiGPO was published at **NeurIPS 2025** as a poster presentation. The paper is available:
- NeurIPS poster: [https://neurips.cc/virtual/2025/poster/118123](https://neurips.cc/virtual/2025/poster/118123)
- arXiv: [https://arxiv.org/abs/2505.10978](https://arxiv.org/abs/2505.10978)
- OpenReview: [https://openreview.net/forum?id=QXEhBMNrCW](https://openreview.net/forum?id=QXEhBMNrCW)
- HuggingFace paper page: [https://huggingface.co/papers/2505.10978](https://huggingface.co/papers/2505.10978)

### Performance Numbers - Important Note
**Regarding the specific numbers you mentioned (90.2% ALFWorld, 75.2% WebShop for w/o std config):** My search found slightly different numbers. According to the arXiv paper (v1):

For **Qwen2.5-1.5B-Instruct** without standard deviation normalization:
- **ALFWorld:** 86.1% overall success rate (not 90.2%)
- **WebShop:** 67.4% success rate (not 75.2%)

For **Qwen2.5-7B-Instruct**, GiGPO achieved ~12.6% improvement on ALFWorld and ~9.1% on WebShop over GRPO baseline.

**Note:** The exact performance numbers may vary between different model sizes (1.5B vs 7B) and configurations. I recommend checking the actual paper tables for the most authoritative numbers, as there may be different configurations or model variants that achieve the 90.2% and 75.2% you're referencing.

Sources:
- [langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop · Hugging Face](https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop)
- [langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld · Hugging Face](https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld)
- [verl-agent - a langfeng01 Collection](https://huggingface.co/collections/langfeng01/verl-agent-684970e8f51babe2a6d98554)
- [GitHub - langfengQ/verl-agent](https://github.com/langfengq/verl-agent)
- [Group-in-Group Policy Optimization for LLM Agent Training - arXiv](https://arxiv.org/abs/2505.10978)
- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/118123)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2d48ff6-b010-41ab-a6f8-82145d551c29",
  "isSidechain": true,
  "agentId": "ae6c24d711b3c9137",
  "requestId": "req_011CauQUZHraor3aA1qQ3N38",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ec31d272-fe9b-4eba-96b1-925b4234fd23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73cacb99-a11d-4823-af3a-25d235e73069",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TF9BQqwDdweUJSAwH7HGb2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 440,
      "cache_read_input_tokens": 24728,
      "output_tokens": 1226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 440
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1226,
          "cache_read_input_tokens": 24728,
          "cache_creation_input_tokens": 440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 440,
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
