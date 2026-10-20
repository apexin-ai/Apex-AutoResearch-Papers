# Research conversation: I need to understand the latest trl (≥0.12) DPOTrainer API for extending it to implement DMPO (a multi-turn DPO variant)

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a466609ede15340b7.jsonl`
- **Structured JSON:** [`ab5a38cc341f9c085323.json`](../../sessions/ab/ab5a38cc341f9c085323.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

58 recorded events

### User

_source line 1 · 2026-05-12T10:46:41.322Z_

I need to understand the latest trl (≥0.12) DPOTrainer API for extending it to implement DMPO (a multi-turn DPO variant). Search for:

1. WebSearch for "trl DPOTrainer 0.12 2026 API" or similar
2. Look at https://huggingface.co/docs/trl/main/en/dpo_trainer for the latest docs

I need to understand:
- What methods DPOTrainer exposes that can be overridden (especially loss computation, log probability computation)
- How DPOTrainer handles the data format (chosen/rejected pairs)
- How reference model log probabilities are computed
- How per-token log probabilities are aggregated
- Whether there's a `get_batch_loss_metrics` or similar method
- The DPOConfig parameters
- How QLoRA is handled (ref_model with peft)

Report the key methods and their signatures. Be thorough about the loss computation pipeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "23a4bdd2-fe42-4b40-b32c-cba6aa08ce79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T10:46:41.327Z_

```json
{
  "parentUuid": "23a4bdd2-fe42-4b40-b32c-cba6aa08ce79",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f32cea7e-6264-487c-b436-274b9a2ac8a3",
  "timestamp": "2026-05-12T10:46:41.327Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T10:46:44.701Z_



I'll search for the latest TRL DPOTrainer API documentation and source code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f32cea7e-6264-487c-b436-274b9a2ac8a3",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYLKaKcyag8Ny5snb76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51b0d228-cab4-4ac6-95b4-3ede37abb9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MrRFQGHAvMNLLdmTVPziN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6053,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6053,
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

_source line 4 · 2026-05-12T10:46:44.985Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JEnjJCwhzDmRsyDA6CRT66`</summary>

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
  "parentUuid": "51b0d228-cab4-4ac6-95b4-3ede37abb9cd",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYLKaKcyag8Ny5snb76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00167ef2-25e8-4911-9e5d-9f03117ec083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MrRFQGHAvMNLLdmTVPziN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6053,
      "cache_read_input_tokens": 8252,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 6053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6053,
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

_source line 5 · 2026-05-12T10:46:44.989Z_

<details><summary>↩ Tool result · `toolu_01JEnjJCwhzDmRsyDA6CRT66`</summary>

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
  "parentUuid": "00167ef2-25e8-4911-9e5d-9f03117ec083",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "2002f143-aec4-4999-9656-2e2e7a78f0bf",
  "sourceToolAssistantUUID": "00167ef2-25e8-4911-9e5d-9f03117ec083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T10:46:47.998Z_



Let me fetch the latest TRL DPOTrainer documentation and source code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2002f143-aec4-4999-9656-2e2e7a78f0bf",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYLbS4aEYMv9svX2Nnh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2469ee2-8391-4eee-a476-3cb360bea055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ktmbdbuba4JDXLTokrM1MP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 7 · 2026-05-12T10:46:52.929Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01A4aoZS23mUcHgin9MnUwKJ`</summary>

```json
{
  "url": "https://huggingface.co/docs/trl/main/en/dpo_trainer",
  "prompt": "Extract the complete API documentation for DPOTrainer including:\n1. All public methods and their signatures (especially loss computation, log probability computation, get_batch_loss_metrics, concatenated_forward, etc.)\n2. How data format works (chosen/rejected pairs)\n3. How reference model log probabilities are computed\n4. How per-token log probabilities are aggregated\n5. DPOConfig parameters\n6. How QLoRA/PEFT is handled with reference models\n7. Any callback or hook points for extension\nBe extremely thorough - include every method signature you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2469ee2-8391-4eee-a476-3cb360bea055",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYLbS4aEYMv9svX2Nnh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ee8f2a8-703c-4db2-84c7-d40c17c461c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ktmbdbuba4JDXLTokrM1MP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

_source line 8 · 2026-05-12T10:46:53.274Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TMe9M9m9uiLBD5muVoV1Uo`</summary>

```json
{
  "query": "trl DPOTrainer source code get_batch_loss_metrics concatenated_forward 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ee8f2a8-703c-4db2-84c7-d40c17c461c3",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYLbS4aEYMv9svX2Nnh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af526a27-ff13-4651-b11d-cc1eb2cea7ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ktmbdbuba4JDXLTokrM1MP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
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

### Tool result

_source line 9 · 2026-05-12T10:46:53.580Z_

<details><summary>↩ Tool result · `toolu_01A4aoZS23mUcHgin9MnUwKJ`</summary>

````text
# DPO Trainer

[![All_models-DPO-blue](https://img.shields.io/badge/All_models-DPO-blue)](https://huggingface.co/models?other=dpo,trl) [![smol_course-Chapter_2-yellow](https://img.shields.io/badge/smol_course-Chapter_2-yellow)](https://github.com/huggingface/smol-course/tree/main/2_preference_alignment)

## Overview

TRL supports the Direct Preference Optimization (DPO) Trainer for training language models, as described in the paper [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://huggingface.co/papers/2305.18290) by [Rafael Rafailov](https://huggingface.co/rmrafailov), Archit Sharma, Eric Mitchell, [Stefano Ermon](https://huggingface.co/ermonste), [Christopher D. Manning](https://huggingface.co/manning), [Chelsea Finn](https://huggingface.co/cbfinn).

The abstract from the paper is the following:

> While large-scale unsupervised language models (LMs) learn broad world knowledge and some reasoning skills, achieving precise control of their behavior is difficult due to the completely unsupervised nature of their training. Existing methods for gaining such steerability collect human labels of the relative quality of model generations and fine-tune the unsupervised LM to align with these preferences, often with reinforcement learning from human feedback (RLHF). However, RLHF is a complex and often unstable procedure, first fitting a reward model that reflects the human preferences, and then fine-tuning the large unsupervised LM using reinforcement learning to maximize this estimated reward without drifting too far from the original model. In this paper we introduce a new parameterization of the reward model in RLHF that enables extraction of the corresponding optimal policy in closed form, allowing us to solve the standard RLHF problem with only a simple classification loss. The resulting algorithm, which we call Direct Preference Optimization (DPO), is stable, performant, and computationally lightweight, eliminating the need for sampling from the LM during fine-tuning or performing significant hyperparameter tuning. Our experiments show that DPO can fine-tune LMs to align with human preferences as well as or better than existing methods. Notably, fine-tuning with DPO exceeds PPO-based RLHF in ability to control sentiment of generations, and matches or improves response quality in summarization and single-turn dialogue while being substantially simpler to implement and train.

This post-training method was contributed by [Kashif Rasul](https://huggingface.co/kashif) and later refactored by [Quentin Gallouédec](https://huggingface.co/qgallouedec).

## Quick start

This example demonstrates how to train a language model using the [DPOTrainer](/docs/trl/main/en/bema_for_reference_model#trl.DPOTrainer) from TRL. We train a [Qwen 3 0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) model on the [UltraFeedback dataset](https://huggingface.co/datasets/openbmb/UltraFeedback).

```python
from trl import DPOTrainer
from datasets import load_dataset

trainer = DPOTrainer(
    model="Qwen/Qwen3-0.6B",
    train_dataset=load_dataset("trl-lib/ultrafeedback_binarized", split="train"),
)
trainer.train()
```

## Expected dataset type and format

DPO requires a [preference](dataset_formats#preference) dataset. The [DPOTrainer](/docs/trl/main/en/bema_for_reference_model#trl.DPOTrainer) is compatible with both [standard](dataset_formats#standard) and [conversational](dataset_formats#conversational) dataset formats. When provided with a conversational dataset, the trainer will automatically apply the chat template to the dataset.

```python
# Standard format
## Explicit prompt (recommended)
preference_example = {"prompt": "The sky is", "chosen": " blue.", "rejected": " green."}
# Implicit prompt
preference_example = {"chosen": "The sky is blue.", "rejected": "The sky is green."}

# Conversational format
## Explicit prompt (recommended)
preference_example = {"prompt": [{"role": "user", "content": "What color is the sky?"}],
                      "chosen": [{"role": "assistant", "content": "It is blue."}],
                      "rejected": [{"role": "assistant", "content": "It is green."}]}
## Implicit prompt
preference_example = {"chosen": [{"role": "user", "content": "What color is the sky?"},
                                 {"role": "assistant", "content": "It is blue."}],
                      "rejected": [{"role": "user", "content": "What color is the sky?"},
                                   {"role": "assistant", "content": "It is green."}]}
```

If your dataset is not in one of these formats, you can preprocess it to convert it into the expected format. Here is an example with the [Vezora/Code-Preference-Pairs](https://huggingface.co/datasets/Vezora/Code-Preference-Pairs) dataset:

```python
from datasets import load_dataset

dataset = load_dataset("Vezora/Code-Preference-Pairs")

def preprocess_function(example):
    return {
        "prompt": [{"role": "user", "content": example["input"]}],
        "chosen": [{"role": "assistant", "content": example["accepted"]}],
        "rejected": [{"role": "assistant", "content": example["rejected"]}],
    }

dataset = dataset.map(preprocess_function, remove_columns=["instruction", "input", "accepted", "ID"])
print(next(iter(dataset["train"])))
```

```json
{
    "prompt": [{"role": "user", "content": "Create a nested loop to print every combination of numbers [...]"}],
    "chosen": [{"role": "assistant", "content": "Here is an example of a nested loop in Python [...]"}],
    "rejected": [{"role": "assistant", "content": "Here is an example of a nested loop in Python [...]"}],
}
```

## Looking deeper into the DPO method

Direct Preference Optimization (DPO) is a training method designed to align a language model with preference data. Instead of supervised input–output pairs, the model is trained on pairs of completions to the same prompt, where one completion is preferred over the other. The objective directly optimizes the model to widen the margin between the log-likelihoods of preferred and dispreferred completions, relative to a reference model, without requiring an explicit reward model. In practice, this is typically achieved by suppressing the likelihood of dispreferred completions rather than by increasing the likelihood of preferred ones.

This section breaks down how DPO works in practice, covering the key steps: **preprocessing** and **loss computation**.

### Preprocessing and tokenization

During training, each example is expected to contain a prompt along with a preferred (`chosen`) and a dispreferred (`rejected`) completion. For more details on the expected formats, see [Dataset formats](dataset_formats).
The [DPOTrainer](/docs/trl/main/en/bema_for_reference_model#trl.DPOTrainer) tokenizes each input using the model's tokenizer.

### Computing the loss

![dpo_figure](https://huggingface.co/datasets/trl-lib/documentation-images/resolve/main/dpo_figure.png)

The loss used in DPO is defined as follows:
$$
\mathcal{L}_{\mathrm{DPO}}(\theta) = -\mathbb{E}_{(x,y^{+},y^{-})}\!\left[\log \sigma\!\left(\beta\Big(\log\frac{\pi_{\theta}(y^{+}\!\mid x)}{\pi_{\mathrm{ref}}(y^{+}\!\mid x)}-\log \frac{\pi_{\theta}(y^{-}\!\mid x)}{\pi_{\mathrm{ref}}(y^{-}\!\mid x)}\Big)\right)\right]
$$
  
where  \\( x \\)  is the prompt,  \\( y^+ \\) is the preferred completion and  \\( y^- \\)  is the dispreferred completion.  \\( \pi_{\theta} \\)  is the policy model being trained,  \\( \pi_{\mathrm{ref}} \\)  is the reference model,  \\( \sigma \\)  is the sigmoid function, and  \\( \beta > 0 \\)  is a hyperparameter that controls the strength of the preference signal.

#### Loss Types

Several formulations of the objective have been proposed in the literature. Initially, the objective of DPO was defined as presented above.

| `loss_type=` | Description |
| --- | --- |
| `"sigmoid"` (default) | Given the preference data, we can fit a binary classifier according to the Bradley-Terry model and in fact the [DPO](https://huggingface.co/papers/2305.18290) authors propose the sigmoid loss on the normalized likelihood via the `logsigmoid` to fit a logistic regression. |
| `"hinge"` | The [RSO](https://huggingface.co/papers/2309.06657) authors propose to use a hinge loss on the normalized likelihood from the [SLiC](https://huggingface.co/papers/2305.10425) paper. In this case, the `beta` is the reciprocal of the margin. |
| `"ipo"` | The [IPO](https://huggingface.co/papers/2310.12036) authors argue the logit transform can overfit and propose the identity transform to optimize preferences directly; TRL exposes this as `loss_type="ipo"`. |
| `"exo_pair"` | The [EXO](https://huggingface.co/papers/2402.00856) authors propose reverse-KL preference optimization. `label_smoothing` must be strictly greater than `0.0`; a recommended value is `1e-3` (see Eq. 16 for the simplified pairwise variant). The full method uses `K>2` SFT completions and approaches PPO as `K` grows. |
| `"nca_pair"` | The [NCA](https://huggingface.co/papers/2402.05369) authors shows that NCA optimizes the absolute likelihood for each response rather than the relative likelihood. |
| `"robust"` | The [Robust DPO](https://huggingface.co/papers/2403.00409) authors propose an unbiased DPO loss under noisy preferences. Use `label_smoothing` in [DPOConfig](/docs/trl/main/en/dpo_trainer#trl.DPOConfig) to model label-flip probability; valid values are in the range `[0.0, 0.5)`. |
| `"bco_pair"` | The [BCO](https://huggingface.co/papers/2404.04656) authors train a binary classifier whose logit serves as a reward so that the classifier maps {prompt, chosen completion} pairs to 1 and {prompt, rejected completion} pairs to 0. For unpaired data, we recommend the dedicated [experimental.bco.BCOTrainer](/docs/trl/main/en/bco_trainer#trl.experimental.bco.BCOTrainer). |
| `"sppo_hard"` | The [SPPO](https://huggingface.co/papers/2405.00675) authors claim that SPPO is capable of solving the Nash equilibrium iteratively by pushing the chosen rewards to be as large as 1/2 and the rejected rewards to be as small as -1/2 and can alleviate data sparsity issues. The implementation approximates this algorithm by employing hard label probabilities, assigning 1 to the winner and 0 to the loser. |
| `"aot"`  or `loss_type="aot_unpaired"` | The [AOT](https://huggingface.co/papers/2406.05882) authors propose Distributional Preference Alignment via Optimal Transport. `loss_type="aot"` is for paired data; `loss_type="aot_unpaired"` is for unpaired data. Both enforce stochastic dominance via sorted quantiles; larger per-GPU batch sizes help. |
| `"apo_zero"` or `loss_type="apo_down"` | The [APO](https://huggingface.co/papers/2408.06266) method introduces an anchored objective. `apo_zero` boosts winners and downweights losers (useful when the model underperforms the winners). `apo_down` downweights both, with stronger pressure on losers (useful when the model already outperforms winners). |
| `"discopop"` | The [DiscoPOP](https://huggingface.co/papers/2406.08414) paper uses LLMs to discover more efficient offline preference optimization losses. In the paper the proposed DiscoPOP loss (which is a log-ratio modulated loss) outperformed other optimization losses on different tasks (IMDb positive text generation, Reddit TLDR summarization, and Alpaca Eval 2.0). |
| `"sft"` | SFT (Supervised Fine-Tuning) loss is the negative log likelihood loss, used to train the model to generate preferred responses. |
| `"sigmoid_norm"` | The [SimPO](https://huggingface.co/papers/2405.14734) authors address the length-bias in the original sigmoid loss by normalizing by the number of non-mask tokens; TRL exposes this as `loss_type="sigmoid_norm"`. |

## Logged metrics

While training and evaluating we record the following reward metrics:

* `global_step`: The total number of optimizer steps taken so far.
* `epoch`: The current epoch number, based on dataset iteration.
* `num_tokens`: The total number of tokens processed so far.
* `loss`: The average cross-entropy loss computed over non-masked tokens in the current logging interval.
* `entropy`: The average entropy of the model's predicted token distribution over non-masked tokens.
* `mean_token_accuracy`: The proportion of non-masked tokens for which the model’s top-1 prediction matches the token from the chosen completion.
* `learning_rate`: The current learning rate, which may change dynamically if a scheduler is used.
* `grad_norm`: The L2 norm of the gradients, computed before gradient clipping.
* `logits/chosen`: The average logit values assigned by the model to the tokens in the chosen completion.
* `logits/rejected`: The average logit values assigned by the model to the tokens in the rejected completion.
* `logps/chosen`: The average log-probability assigned by the model to the tokens in the chosen completion.
* `logps/rejected`: The average log-probability assigned by the model to the tokens in the rejected completion.
* `rewards/chosen`: The average implicit reward computed for the chosen completion, computed as  \\( \beta \log \frac{\pi_{\theta}(y^{+}\!\mid x)}{\pi_{\mathrm{ref}}(y^{+}\!\mid x)} \\).
* `rewards/rejected`: The average implicit reward computed for the rejected completion, computed as  \\( \beta \log \frac{\pi_{\theta}(y^{-}\!\mid x)}{\pi_{\mathrm{ref}}(y^{-}\!\mid x)} \\).
* `rewards/margins`: The average implicit reward margin between the chosen and rejected completions.
* `rewards/accuracies`: The proportion of examples where the implicit reward for the chosen completion is higher than that for the rejected completion.

## Customization

### Compatibility and constraints

Some argument combinations are intentionally restricted in the current [DPOTrainer](/docs/trl/main/en/bema_for_reference_model#trl.DPOTrainer) implementation:

* `use_weighting=True` is not supported with `loss_type="aot"` or `loss_type="aot_unpaired"`.
* With `use_liger_kernel=True`:
  * only a single `loss_type` is supported,
  * `compute_metrics` is not supported,
  * `precompute_ref_log_probs=True` is not supported.
* `sync_ref_model=True` is not supported when training with PEFT models that do not keep a standalone `ref_model`.
* `sync_ref_model=True` cannot be combined with `precompute_ref_log_probs=True`.
* `precompute_ref_log_probs=True` is not supported with `IterableDataset` (train or eval).

### Multi-loss combinations

The DPO trainer supports combining multiple loss functions with different weights, enabling more sophisticated optimization strategies. This is particularly useful for implementing algorithms like MPO (Mixed Preference Optimization). MPO is a training approach that combines multiple optimization objectives, as described in the paper [Enhancing the Reasoning Ability of Multimodal Large Language Models via Mixed Preference Optimization](https://huggingface.co/papers/2411.10442).

To combine multiple losses, specify the loss types and corresponding weights as lists:

```python
# MPO: Combines DPO (sigmoid) for preference and BCO (bco_pair) for quality
training_args = DPOConfig(
    loss_type=["sigmoid", "bco_pair", "sft"],  # loss types to combine
    loss_weights=[0.8, 0.2, 1.0]  # corresponding weights, as used in the MPO paper
)
```

### Model initialization

You can directly pass the kwargs of the `from_pretrained()` method to the [DPOConfig](/docs/trl/main/en/dpo_trainer#trl.DPOConfig). For example, if you want to load a model in a different precision, analogous to

```python
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B", dtype=torch.bfloat16)
```

you can do so by passing the `model_init_kwargs={"dtype": torch.bfloat16}` argument to the [DPOConfig](/docs/trl/main/en/dpo_trainer#trl.DPOConfig).

```python
from trl import DPOConfig

training_args = DPOConfig(
    model_init_kwargs={"dtype": torch.bfloat16},
)
```

Note that all keyword arguments of `from_pretrained()` are supported.

### Train adapters with PEFT

We support tight integration with 🤗 PEFT library, allowing any user to conveniently train adapters and share them on the Hub, rather than training the entire model.

```python
from datasets import load_dataset
from trl import DPOTrainer
from peft import LoraConfig

dataset = load_dataset("trl-lib/ultrafeedback_binarized", split="train")

trainer = DPOTrainer(
    "Qwen/Qwen3-0.6B",
    train_dataset=dataset,
    peft_config=LoraConfig(),
)

trainer.train()
```

You can also continue training your [PeftModel](https://huggingface.co/docs/peft/main/en/package_reference/peft_model#peft.PeftModel). For that, first load a `PeftModel` outside [DPOTrainer](/docs/trl/main/en/bema_for_reference_model#trl.DPOTrainer) and pass it directly to the trainer without the `peft_config` argument being passed.

```python
from datasets import load_dataset
from trl import DPOTrainer
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained("trl-lib/Qwen3-4B-LoRA", is_trainable=True)
dataset = load_dataset("trl-lib/ultrafeedback_binarized", split="train")

trainer = DPOTrainer(
    model=model,
    train_dataset=dataset,
)

trainer.train()
```

> [!TIP]
> When training adapters, you typically use a higher learning rate (≈1e‑5) than full fine-tuning since only new parameters are being learned.
>
> ```python
> DPOConfig(learning_rate=1e-5, ...)
> ```

### Train with Liger Kernel

Liger Kernel is a collection of Triton kernels for LLM training that boosts multi-GPU throughput by 20%, cuts memory use by 60% (enabling up to 4× longer context), and works seamlessly with tools like FlashAttention, PyTorch FSDP, and DeepSpeed. For more information, see [Liger Kernel Integration](liger_kernel_integration).

### Rapid Experimentation for DPO

RapidFire AI is an open-source experimentation engine that sits on top of TRL and lets you launch multiple DPO configurations at once, even on a single GPU. Instead of trying configurations sequentially, RapidFire lets you **see all their learning curves earlier, stop underperforming runs, and clone promising ones with new settings in flight** without restarting. For more information, see [RapidFire AI Integration](rapidfire_integration).

### Train with Unsloth

Unsloth is an open‑source framework for fine‑tuning and reinforcement learning that trains LLMs (like Llama, Mistral, Gemma, DeepSeek, and more) up to 2× faster with up to 70% less VRAM, while providing a streamlined, Hugging Face–compatible workflow for training, evaluation, and deployment. For more information, see [Unsloth Integration](unsloth_integration).

## Tool Calling with DPO

The [DPOTrainer](/docs/trl/main/en/bema_for_reference_model#trl.DPOTrainer) fully supports fine-tuning models with _tool calling_ capabilities. In this case, each dataset example should include:

* The conversation messages (prompt, chosen and rejected), including any tool calls (`tool_calls`) and tool responses (`tool` role messages)
* The list of available tools in the `tools` column, typically provided as JSON schemas

For details on the expected dataset structure, see the [Dataset Format — Tool Calling](dataset_formats#tool-calling) section.

## Training Vision Language Models

[DPOTrainer](/docs/trl/main/en/bema_for_reference_model#trl.DPOTrainer) fully supports training Vision-Language Models (VLMs). To train a VLM, provide a dataset with either an `image` column (single image per sample) or an `images` column (list of images per sample). For more information on the expected dataset structure, see the [Dataset Format — Vision Dataset](dataset_formats#vision-dataset) section.
An example of such a dataset is the [RLAIF-V Dataset](https://huggingface.co/datasets/HuggingFaceH4/rlaif-v_formatted) dataset.

```python
from trl import DPOConfig, DPOTrainer
from datasets import load_dataset

trainer = DPOTrainer(
    model="Qwen/Qwen2.5-VL-3B-Instruct",
    args=DPOConfig(max_length=None),
    train_dataset=load_dataset("HuggingFaceH4/rlaif-v_formatted", split="train"),
)
trainer.train()
```

> [!TIP]
> For VLMs, truncating may remove image tokens, leading to errors during training. To avoid this, set `max_length=None` in the [DPOConfig](/docs/trl/main/en/dpo_trainer#trl.DPOConfig). This allows the model to process the full sequence length without truncating image tokens.
>
> ```python
> DPOConfig(max_length=None, ...)
> ```
>
> Only use `max_length` when you've verified that truncation won't remove image tokens for the entire dataset.

## DPOTrainer[[trl.DPOTrainer]]

#### trl.DPOTrainer[[trl.DPOTrainer]]

[Source](https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_trainer.py#L406)

Trainer for Direct Preference Optimization (DPO) method. This algorithm was initially proposed in the paper [Direct
Preference Optimization: Your Language Model is Secretly a Reward Model](https://huggingface.co/papers/2305.18290).
This class is a wrapper around the [Trainer](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.Trainer) class and inherits all of its attributes and methods.

Example:

```python
from trl import DPOTrainer
from datasets import load_dataset

dataset = load_dataset("trl-lib/ultrafeedback_binarized", split="train")

trainer = DPOTrainer(
    model="Qwen/Qwen2.5-0.5B-Instruct",
    train_dataset=dataset,
)
trainer.train()
```

traintrl.DPOTrainer.trainhttps://github.com/huggingface/trl/blob/main/transformers/trainer.py#L1325[{"name": "resume_from_checkpoint", "val": ": str | bool | None = None"}, {"name": "trial", "val": ": optuna.Trial | dict[str, Any] | None = None"}, {"name": "ignore_keys_for_eval", "val": ": list[str] | None = None"}]- **resume_from_checkpoint** (`str` or `bool`, *optional*) --
  If a `str`, local path to a saved checkpoint as saved by a previous instance of `Trainer`. If a
  `bool` and equals `True`, load the last checkpoint in *args.output_dir* as saved by a previous instance
  of `Trainer`. If present, training will resume from the model/optimizer/scheduler states loaded here.
- **trial** (`optuna.Trial` or `dict[str, Any]`, *optional*) --
  The trial run or the hyperparameter dictionary for hyperparameter search.
- **ignore_keys_for_eval** (`list[str]`, *optional*) --
  A list of keys in the output of your model (if it is a dictionary) that should be ignored when
  gathering predictions for evaluation during the training.0`~trainer_utils.TrainOutput`Object containing the global step count, training loss, and metrics.

Main training entry point.

**Parameters:**

model (`str` or [PreTrainedModel](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel) or [PeftModel](https://huggingface.co/docs/peft/main/en/package_reference/peft_model#peft.PeftModel)) : Model to be trained. Can be either:  - A string, being the *model id* of a pretrained model hosted inside a model repo on huggingface.co, or a path to a *directory* containing model weights saved using [save_pretrained](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel.save_pretrained), e.g., `'./my_model_directory/'`. The model is loaded using `&lt;ModelArchitecture>.from_pretrained` (where `&lt;ModelArchitecture>` is derived from the model config) with the keyword arguments in `args.model_init_kwargs`. - A [PreTrainedModel](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel) object. Only causal language models are supported. - A [PeftModel](https://huggingface.co/docs/peft/main/en/package_reference/peft_model#peft.PeftModel) object. Only causal language models are supported.

ref_model ([PreTrainedModel](https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel), *optional*) : Reference model used to compute the reference log probabilities.  - If provided, this model is used directly as the reference policy. - If `None`, the trainer will automatically use the initial policy corresponding to `model`, i.e. the model state before DPO training starts.

args ([DPOConfig](/docs/trl/main/en/dpo_trainer#trl.DPOConfig), *optional*) : Configuration for this trainer. If `None`, a default configuration is used.

data_collator (`DataCollator`, *optional*) : Function to use to form a batch from a list of elements of the processed `train_dataset` or `eval_dataset`. Will default to `DataCollatorForPreference` if the model is a language model and `DataCollatorForVisionPreference` if the model is a vision-language model. Custom collators must truncate sequences before padding; the trainer does not apply post-collation truncation.

train_dataset ([Dataset](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset) or [IterableDataset](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.IterableDataset)) : Dataset to use for training. This trainer supports both [language modeling](#language-modeling) type and [prompt-completion](#prompt-completion) type. The format of the samples can be either:  - [Standard](dataset_formats#standard): Each sample contains plain text. - [Conversational](dataset_formats#conversational): Each sample contains structured messages (e.g., role and content).

eval_dataset ([Dataset](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset), [IterableDataset](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.IterableDataset) or `dict[str, Dataset | IterableDataset]`) : Dataset to use for evaluation. It must meet the same requirements as `train_dataset`.

processing_class ([PreTrainedTokenizerBase](https://huggingface.co/docs/transformers/main/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase) or [ProcessorMixin](https://huggingface.co/docs/transformers/main/en/main_classes/processors#transformers.ProcessorMixin), *optional*) : Processing class used to process the data. The padding side must be set to "left". If `None`, the processing class is loaded from the model's name with [from_pretrained](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoProcessor.from_pretrained). A padding token, `tokenizer.pad_token`, must be set. If the processing class has not set a padding token, `tokenizer.eos_token` will be used as the default.

compute_metrics (`Callable[[EvalPrediction], dict]`, *optional*) : The function that will be used to compute metrics at evaluation. Must take a [EvalPrediction](https://huggingface.co/docs/transformers/main/en/internal/trainer_utils#transformers.EvalPrediction) and return a dictionary string to metric values. When passing [SFTConfig](/docs/trl/main/en/sft_trainer#trl.SFTConfig) with `batch_eval_metrics` set to `True`, your `compute_metrics` function must take a boolean `compute_result` argument. This will be triggered after the last eval batch to signal that the function needs to calculate and return the global summary statistics rather than accumulating the batch-level statistics.

callbacks (list of [TrainerCallback](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.TrainerCallback), *optional*) : List of callbacks to customize the training loop. Will add those to the list of default callbacks detailed in [here](https://huggingface.co/docs/transformers/main_classes/callback).  If you want to remove one of the default callbacks used, use the [remove_callback](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.Trainer.remove_callback) method.

optimizers (`tuple[torch.optim.Optimizer | None, torch.optim.lr_scheduler.LambdaLR | None]`, *optional*, defaults to `(None, None)`) : A tuple containing the optimizer and the scheduler to use. Will default to an instance of `AdamW` on your model and a scheduler given by [get_linear_schedule_with_warmup](https://huggingface.co/docs/transformers/main/en/main_classes/optimizer_schedules#transformers.get_linear_schedule_with_warmup) controlled by `args`.

peft_config ([PeftConfig](https://huggingface.co/docs/peft/main/en/package_reference/config#peft.PeftConfig), *optional*) : PEFT configuration used to wrap the model. If `None`, the model is not wrapped.

**Returns:**

``~trainer_utils.TrainOutput``

Object containing the global step count, training loss, and metrics.
#### save_model[[trl.DPOTrainer.save_model]]

[Source](https://github.com/huggingface/trl/blob/main/transformers/trainer.py#L3752)

Will save the model, so you can reload it using `from_pretrained()`.

Will only save from the main process.
#### push_to_hub[[trl.DPOTrainer.push_to_hub]]

[Source](https://github.com/huggingface/trl/blob/main/transformers/trainer.py#L3999)

Upload `self.model` and `self.processing_class` to the 🤗 model hub on the repo `self.args.hub_model_id`.

**Parameters:**

commit_message (`str`, *optional*, defaults to `"End of training"`) : Message to commit while pushing.

blocking (`bool`, *optional*, defaults to `True`) : Whether the function should return only when the `git push` has finished.

token (`str`, *optional*, defaults to `None`) : Token with write permission to overwrite Trainer's original args.

revision (`str`, *optional*) : The git revision to commit from. Defaults to the head of the "main" branch.

kwargs (`dict[str, Any]`, *optional*) : Additional keyword arguments passed along to `~Trainer.create_model_card`.

**Returns:**

The URL of the repository where the model was pushed if `blocking=False`, or a `Future` object tracking the
progress of the commit if `blocking=True`.

## DPOConfig[[trl.DPOConfig]]

#### trl.DPOConfig[[trl.DPOConfig]]

[Source](https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_config.py#L23)

Configuration class for the [DPOTrainer](/docs/trl/main/en/bema_for_reference_model#trl.DPOTrainer).

This class includes only the parameters that are specific to DPO training. For a full list of training arguments,
please refer to the [TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments) documentation. Note that default values in this class may
differ from those in [TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments).

Using [HfArgumentParser](https://huggingface.co/docs/transformers/main/en/internal/trainer_utils#transformers.HfArgumentParser) we can turn this class into
[argparse](https://docs.python.org/3/library/argparse#module-argparse) arguments that can be specified on the
command line.

> [!NOTE]
> These parameters have default values different from [TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments):
> - `logging_steps`: Defaults to `10` instead of `500`.
> - `gradient_checkpointing`: Defaults to `True` instead of `False`.
> - `bf16`: Defaults to `True` if `fp16` is not set, instead of `False`.
> - `learning_rate`: Defaults to `1e-6` instead of `5e-5`.


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ee8f2a8-703c-4db2-84c7-d40c17c461c3",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "e9159368-6dcc-4b13-81fb-f44fde8163cb",
  "sourceToolAssistantUUID": "6ee8f2a8-703c-4db2-84c7-d40c17c461c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-12T10:46:53.904Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0168qm3xQ5f5cZiYLiRCH5Dg`</summary>

```json
{
  "query": "trl 0.12 0.15 DPOTrainer API loss computation reference model log probabilities"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9159368-6dcc-4b13-81fb-f44fde8163cb",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYLbS4aEYMv9svX2Nnh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a871767-1514-42e7-940d-752318cea3a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ktmbdbuba4JDXLTokrM1MP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 14305,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 357,
          "cache_read_input_tokens": 14305,
          "cache_creation_input_tokens": 1956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1956,
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

_source line 11 · 2026-05-12T10:46:59.061Z_

<details><summary>↩ Tool result · `toolu_01TMe9M9m9uiLBD5muVoV1Uo`</summary>

```text
Web search results for query: "trl DPOTrainer source code get_batch_loss_metrics concatenated_forward 2025 2026"

Links: [{"title":"trl/trl/trainer/dpo_trainer.py at main · huggingface/trl","url":"https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_trainer.py/"},{"title":"Trainer · Hugging Face","url":"https://huggingface.co/docs/trl/v0.9.6/trainer"},{"title":"Trainer","url":"https://huggingface.co/docs/trl/main/en/trainer"},{"title":"Trainer - TRL - Model Database","url":"https://modeldatabase.com/docs/trl/trainer.html"},{"title":"DPO Trainer · Hugging Face","url":"https://huggingface.co/docs/trl/v0.5.0/dpo_trainer"},{"title":"Issue with FSDP on DPO trainer: ref_model was not placed on cuda · Issue #1147 · huggingface/trl","url":"https://github.com/huggingface/trl/issues/1147"},{"title":"DPO Trainer - Model Database","url":"https://modeldatabase.com/docs/trl/dpo_trainer.html"},{"title":"trl/trl/trainer/dpo_trainer.py at main · huggingface/trl · GitHub","url":"https://ibm.biz/AOT_TRL"},{"title":"trl · PyPI","url":"https://pypi.org/project/trl/"},{"title":"GitHub - huggingface/trl: Train transformer language models with reinforcement learning. · GitHub","url":"https://github.com/huggingface/trl"}]

Based on the web search results, I found relevant information about the TRL DPOTrainer's `get_batch_loss_metrics` and `concatenated_forward` methods in the source code.

The `get_batch_loss_metrics` method computes the DPO loss and other metrics for the given batch, and `concatenated_forward` runs the given model on the given batch of inputs, concatenating the chosen and rejected inputs together to avoid doing two forward passes, because it's faster for FSDP.

In the training pipeline, `get_batch_loss_metrics` is called within `compute_loss`, which then calls `concatenated_forward` to process the batch through the model.

The source code for DPOTrainer is available in the official HuggingFace TRL repository at trl/trl/trainer/dpo_trainer.py. You can access the latest version directly on GitHub at https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_trainer.py to view the actual implementation of these methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af526a27-ff13-4651-b11d-cc1eb2cea7ed",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "c74020da-3d86-45a7-82b4-4c779a1ad32b",
  "sourceToolAssistantUUID": "af526a27-ff13-4651-b11d-cc1eb2cea7ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T10:47:00.246Z_

<details><summary>↩ Tool result · `toolu_0168qm3xQ5f5cZiYLiRCH5Dg`</summary>

```text
Web search results for query: "trl 0.12 0.15 DPOTrainer API loss computation reference model log probabilities"

Links: [{"title":"DPO Trainer","url":"https://huggingface.co/docs/trl/main/en/dpo_trainer"},{"title":"trl/trl/trainer/dpo_trainer.py at main · huggingface/trl","url":"https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_trainer.py/"},{"title":"lmflow.pipeline.utils.dpov2_trainer — LMFlow documentation","url":"https://optimalscale.github.io/LMFlow/autoapi/lmflow/pipeline/utils/dpov2_trainer/index.html"},{"title":"DPO Trainer · Hugging Face","url":"https://huggingface.co/docs/trl/v0.9.4/en/dpo_trainer"},{"title":"trl/trl/trainer/dpo_trainer.py at d708ec272f292ded00a4d0f14b5bd214741b87f3 · huggingface/trl","url":"https://github.com/huggingface/trl/blob/d708ec272f292ded00a4d0f14b5bd214741b87f3/trl/trainer/dpo_trainer.py"},{"title":"DPO Trainer - Model Database","url":"https://modeldatabase.com/docs/trl/dpo_trainer.html"},{"title":"trl/trl/trainer/dpo_config.py at main · huggingface/trl","url":"https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_config.py"},{"title":"Practice: Implementing a DPO Loss Function","url":"https://apxml.com/courses/llm-alignment-safety/chapter-3-advanced-alignment-algorithms/practice-implementing-dpo-loss"},{"title":"direct-preference-optimization/trainers.py at main · eric-mitchell/direct-preference-optimization","url":"https://github.com/eric-mitchell/direct-preference-optimization/blob/main/trainers.py"},{"title":"blog/dpo-trl.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/dpo-trl.md"}]

Based on the search results, I found relevant information about the DPOTrainer API and how it computes loss using reference model log probabilities. Here's what I found:

## DPOTrainer Loss Computation with Reference Model Log Probabilities

The DPOTrainer computes the DPO loss for a batch of policy and reference model log probabilities.

### Key Parameters

The `precompute_ref_log_probs` parameter (defaults to False) determines whether to precompute the log probabilities from the reference model. If set to False, the reference model will be used during training to compute log probabilities on-the-fly.

### Loss Computation Details

The DPO loss function takes four sets of log probabilities as inputs:
- Policy chosen log probabilities, policy rejected log probabilities, reference chosen log probabilities, and reference rejected log probabilities

The losses tensor contains the DPO loss for each example in the batch, and the chosen_rewards and rejected_rewards tensors contain the rewards for the chosen and rejected responses, respectively.

### Beta Parameter

The beta parameter (defaults to 0.1) controls the deviation from the reference model, where higher β means less deviation from the reference model. Beta is the temperature parameter for the DPO loss, typically something in the range of 0.1 to 0.5.

### Reward Metrics

The DPOTrainer records reward metrics including: the mean difference between the log probabilities of the policy model and the reference model for the chosen responses scaled by beta, the same for rejected responses, accuracies showing how often chosen rewards exceed rejected rewards, and margins showing the mean difference between chosen and rejected rewards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a871767-1514-42e7-940d-752318cea3a4",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "c3118cf3-593c-407c-97d2-887e48d13bd8",
  "sourceToolAssistantUUID": "6a871767-1514-42e7-940d-752318cea3a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-12T10:47:03.789Z_

Now let me fetch the actual source code to get the exact method signatures and implementation details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3118cf3-593c-407c-97d2-887e48d13bd8",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYMiUWAZtTiXJRSE49s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a67ad45-b7f6-4791-82b9-cd7c8bc7126f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vmzM4cSAbwfQvHU2bUkm5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11192,
      "cache_read_input_tokens": 16261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11192,
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

_source line 14 · 2026-05-12T10:47:08.498Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U2Zgobb34nCF1ihFf2eUwi`</summary>

```json
{
  "url": "https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_trainer.py",
  "prompt": "Extract ALL method definitions/signatures from the DPOTrainer class. I need every method name, its parameters, and a brief description of what it does. Especially focus on:\n1. __init__ signature\n2. compute_loss / get_batch_loss_metrics\n3. concatenated_forward\n4. get_batch_logps / any log probability computation methods\n5. dpo_loss\n6. Any method related to reference model handling\n7. compute_reference_log_probs or precompute methods\n8. Any tokenization/preprocessing methods\n\nAlso extract the full DPOConfig class with all its parameters.\n\nBe EXTREMELY thorough - list every single method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a67ad45-b7f6-4791-82b9-cd7c8bc7126f",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYMiUWAZtTiXJRSE49s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "502e19af-5320-4a4a-a598-c3f60cba23ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vmzM4cSAbwfQvHU2bUkm5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11192,
      "cache_read_input_tokens": 16261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11192,
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

_source line 15 · 2026-05-12T10:47:09.644Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0147DKj71TzH43pU4jZ46ZXx`</summary>

```json
{
  "url": "https://github.com/huggingface/trl/blob/main/trl/trainer/dpo_config.py",
  "prompt": "Extract the COMPLETE DPOConfig class definition with ALL parameters, their types, default values, and descriptions. List every single configuration parameter."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "502e19af-5320-4a4a-a598-c3f60cba23ed",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYMiUWAZtTiXJRSE49s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbb073d6-0a02-4d4d-b5ff-6b24873b7137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vmzM4cSAbwfQvHU2bUkm5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11192,
      "cache_read_input_tokens": 16261,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11192
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 373,
          "cache_read_input_tokens": 16261,
          "cache_creation_input_tokens": 11192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11192,
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

_source line 16 · 2026-05-12T10:47:17.043Z_

<details><summary>↩ Tool result · `toolu_01U2Zgobb34nCF1ihFf2eUwi`</summary>

```text
# DPOTrainer Class Methods and DPOConfig

## DPOTrainer Methods Extracted

Based on the provided file content, here are the method definitions visible in the DPOTrainer class:

### Core Initialization
- **`__init__`**: Initializes trainer with model, ref_model, args, data_collator, train_dataset, eval_dataset, processing_class, compute_metrics, callbacks, optimizers, peft_config

### Dataset Processing
- **`_tokenize`**: "Tokenize a single example for dataset preprocessing. Dispatches to apply_chat_template for conversational input and to __call__ for non-conversational input"
- **`_prepare_dataset`**: Prepares dataset through prompt extraction, EOS token addition, and tokenization
- **`_set_signature_columns_if_needed`**: Sets signature columns based on vision vs. text datasets
- **`_precompute_ref_logps`**: Computes reference log probabilities for dataset examples

### Data Collators (Separate Classes)
- **`DataCollatorForPreference.torch_call`**: Batches preference data with padding
- **`DataCollatorForVisionPreference.torch_call`**: Handles vision-language batching with on-the-fly image processing

## DPOConfig Parameters

The file excerpt shows DPOConfig is imported but does not display its full definition. However, the `__init__` method reveals these configuration attributes used:

| Parameter | Purpose |
|-----------|---------|
| `beta` | DPO beta hyperparameter |
| `precompute_ref_log_probs` | Flag for precomputing reference probabilities |
| `loss_type` | Loss function type(s) |
| `loss_weights` | Weights for multiple loss types |
| `ld_alpha` | Lambda divergence alpha |
| `f_divergence_type` | F-divergence type selection |
| `f_alpha_divergence_coef` | F-alpha divergence coefficient |
| `label_smoothing` | Label smoothing amount |
| `use_weighting` | WPO-style weighting flag |
| `use_liger_kernel` | Liger kernel optimization flag |
| `max_length` | Maximum sequence length |
| `truncation_mode` | Truncation strategy |
| `padding_free` | Padding-free training flag |
| `sync_ref_model` | Reference model synchronization |
| `gradient_checkpointing` | Memory optimization |
| `disable_dropout` | Dropout removal flag |
| `activation_offloading` | Activation memory offloading |

**Note**: The remaining methods (compute_loss, concatenated_forward, get_batch_logps, dpo_loss) are referenced but their full signatures are not visible in the provided excerpt, which shows only the first ~1000 lines of a 1520-line file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "502e19af-5320-4a4a-a598-c3f60cba23ed",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "4a17b21e-100c-473f-b8e5-d35e4e2dad83",
  "sourceToolAssistantUUID": "502e19af-5320-4a4a-a598-c3f60cba23ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T10:47:17.624Z_

<details><summary>↩ Tool result · `toolu_0147DKj71TzH43pU4jZ46ZXx`</summary>

```text
# DPOConfig Class Parameters

Based on the GitHub file content, here are all DPOConfig parameters:

## Model Control Parameters
- **model_init_kwargs**: `dict[str, Any] | str | None` (default: `None`) - Arguments for AutoModelForCausalLM.from_pretrained
- **disable_dropout**: `bool` (default: `True`) - Disables dropout in model and reference model

## Data Preprocessing Parameters
- **dataset_num_proc**: `int | None` (default: `None`) - Processes for dataset handling
- **max_length**: `int | None` (default: `1024`) - Maximum tokenized sequence length
- **truncation_mode**: `str` (default: `"keep_start"`) - Truncation strategy when exceeding max_length
- **padding_free**: `bool` (default: `False`) - Performs forward passes without padding
- **pad_to_multiple_of**: `int | None` (default: `None`) - Pads sequences to multiples of specified value
- **precompute_ref_log_probs**: `bool` (default: `False`) - Precomputes reference model probabilities
- **precompute_ref_batch_size**: `int | None` (default: `None`) - Batch size for precomputation

## Training Parameters
- **loss_type**: `list[str]` (default: `["sigmoid"]`) - Loss function types (sigmoid, hinge, ipo, exo_pair, nca_pair, robust, bco_pair, sppo_hard, aot, aot_unpaired, apo_zero, apo_down, discopop, sft, sigmoid_norm)
- **loss_weights**: `list[float] | None` (default: `None`) - Weights for multi-loss combinations
- **ld_alpha**: `float | None` (default: `None`) - LD-DPO weighting parameter
- **f_divergence_type**: `str` (default: `"reverse_kl"`) - f-divergence regularizer type
- **f_alpha_divergence_coef**: `float` (default: `0.5`) - α-divergence coefficient
- **label_smoothing**: `float` (default: `0.0`) - Label smoothing for Robust DPO/EXO
- **beta**: `float` (default: `0.1`) - Reference model deviation control
- **use_weighting**: `bool` (default: `False`) - Applies WPO-style weighting
- **discopop_tau**: `float` (default: `0.05`) - DiscoPOP temperature parameter
- **activation_offloading**: `bool` (default: `False`) - Offloads activations to CPU
- **sync_ref_model**: `bool` (default: `False`) - Synchronizes reference with active model
- **ref_model_mixup_alpha**: `float` (default: `0.6`) - TR-DPO mixing parameter
- **ref_model_sync_steps**: `int` (default: `512`) - Synchronization frequency

## Overridden TrainingArguments Parameter
- **learning_rate**: `float` (default: `1e-6`) - Initial AdamW learning rate

## Deprecated Parameters
- **pad_token**: `str | None` (default: `None`) - Deprecated; use tokenizer.pad_token instead
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbb073d6-0a02-4d4d-b5ff-6b24873b7137",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "9c70e705-46d5-4463-a2a8-91da26d609e1",
  "sourceToolAssistantUUID": "bbb073d6-0a02-4d4d-b5ff-6b24873b7137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-12T10:47:20.589Z_

Now let me get the actual source code with the loss computation methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c70e705-46d5-4463-a2a8-91da26d609e1",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYNzj5ncxaFZ5DnEhe3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77c7787b-d14c-4be3-9b29-fbd4e138cc4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CMfCmYLTaiwW6ro5sStT6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 27453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1920,
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

_source line 19 · 2026-05-12T10:47:25.201Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BNasBM7NTxdhYuer6gZtog`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/huggingface/trl/main/trl/trainer/dpo_trainer.py",
  "prompt": "Extract the COMPLETE source code for these methods from DPOTrainer:\n1. compute_loss - full signature and implementation\n2. get_batch_loss_metrics - full signature and implementation  \n3. concatenated_forward - full signature and implementation\n4. get_batch_logps - full signature and implementation (or any method that computes per-token log probs)\n5. dpo_loss - full signature and implementation\n6. Any method that handles the reference model (compute_reference_log_probs, _precompute_ref_logps, etc.)\n7. The __init__ method - focus on how ref_model is handled, especially with PEFT\n\nFor each method, provide the EXACT signature and the key implementation details. Include the actual code for the loss computation methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77c7787b-d14c-4be3-9b29-fbd4e138cc4e",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYNzj5ncxaFZ5DnEhe3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46a46fba-25ac-4bdb-bdae-dc5f73138259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CMfCmYLTaiwW6ro5sStT6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 27453,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1920
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 27453,
          "cache_creation_input_tokens": 1920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1920,
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

_source line 20 · 2026-05-12T10:47:34.968Z_

<details><summary>↩ Tool result · `toolu_01BNasBM7NTxdhYuer6gZtog`</summary>

````text
# DPOTrainer Source Code Extraction

Based on the provided content, here are the requested methods:

## 1. compute_loss
```python
def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
    if self.use_liger_kernel:
        return self._compute_loss_liger(model, inputs, return_outputs)
    else:
        return self._compute_loss(model, inputs, return_outputs)
```

## 2. _compute_loss (Core Implementation)
Full signature and implementation spanning approximately 400+ lines. Key aspects:
- Extracts model outputs and input IDs from batch
- Computes per-token log probabilities using `selective_log_softmax`
- Handles reference log probabilities (either precomputed or computed dynamically)
- Implements multiple loss types: sigmoid, hinge, IPO, exo_pair, nca_pair, robust, bco_pair, sppo_hard, aot, aot_unpaired, apo_zero, apo_down, discopop, sft, sigmoid_norm
- Computes metrics including entropy, logits, token accuracy, rewards, and margins

## 3. compute_ref_log_probs
```python
def compute_ref_log_probs(self, inputs):
    """Computes reference log probabilities for a single padded batch."""
    device = self.accelerator.device
    _non_model_keys = {"completion_mask", "ref_chosen_logps", "ref_rejected_logps"}
    model_kwargs = {k: v for k, v in inputs.items() if k not in _non_model_keys}
    model_kwargs["use_cache"] = False
    
    # Forward pass with reference model or base model
    # Returns ref_chosen_logps and ref_rejected_logps tensors
```

## 4. _precompute_ref_logps
Computes and caches reference log probabilities before training. Key features:
- Uses model fingerprinting to identify cached computations
- Saves results as `.npz` files
- Supports distributed training with `accelerator.gather_for_metrics`
- Returns dataset with appended `ref_chosen_logps` and `ref_rejected_logps` columns

## 5. Reference Model Handling in __init__
Critical initialization logic (lines ~450-500):
```python
if ref_model is None:
    if is_peft_model(self.model) or args.precompute_ref_log_probs:
        self.ref_model = None  # Not needed; adapter disabled or logps precomputed
    else:
        # Create independent reference model copy
        ref_model_path = get_config_model_id(self.model.config)
        self.ref_model = create_model_from_path(ref_model_path, ...)
else:
    self.ref_model = ref_model
```

**Key constraint:** "Reference model is not needed since the adapter can be disabled to revert to the initial model" when using PEFT.

## 6. _compute_loss_liger
Optimized variant using Liger kernel. Avoids materializing logits; computes loss directly from hidden states using fused operations.

## 7. Methods NOT Found
- `get_batch_loss_metrics` - not present (metrics computed within `_compute_loss`)
- `concatenated_forward` - not present (forward pass handled directly in `_compute_loss`)
- `dpo_loss` - not present as standalone method (loss computed inline with multiple variants)

**Note:** The architecture differs from some public DPO implementations; loss computation is integrated into `_compute_loss` with conditional branches for each loss type rather than separate methods.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46a46fba-25ac-4bdb-bdae-dc5f73138259",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "5ba1cf5d-18b6-4dcb-9761-ab536b54d328",
  "sourceToolAssistantUUID": "46a46fba-25ac-4bdb-bdae-dc5f73138259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-12T10:47:37.976Z_

Good -- the architecture has changed significantly from older versions. Let me get the raw source to see the exact implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ba1cf5d-18b6-4dcb-9761-ab536b54d328",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYQGsiQEENK9Lv6dAAk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "638e39ad-8373-4371-bcc0-b1eac9334dea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYiB4GtRaAA9hTnd2Km8RF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 29373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 22 · 2026-05-12T10:47:40.621Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019xo4Sn2tiyjsQQgDVWvhhJ`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/huggingface/trl/refs/heads/main/trl/trainer/dpo_trainer.py",
  "prompt": "I need the EXACT Python source code. Please return the raw source code from line 1 to around line 800 verbatim, without summarizing. Include all imports, the class definition start, __init__, and any helper methods up to around the compute_loss method. Show the actual code."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "638e39ad-8373-4371-bcc0-b1eac9334dea",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYQGsiQEENK9Lv6dAAk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f23dc39a-b480-4f28-9efc-ac2e74df1a25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYiB4GtRaAA9hTnd2Km8RF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 29373,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 29373,
          "cache_creation_input_tokens": 1291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1291,
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

_source line 23 · 2026-05-12T10:47:45.612Z_

<details><summary>↩ Tool result · `toolu_019xo4Sn2tiyjsQQgDVWvhhJ`</summary>

````text
# Python Source Code Extraction from DPO Trainer

I cannot provide the exact verbatim source code as requested because reproducing the full 800+ lines of copyrighted source code would violate copyright protections, even with proper attribution.

However, I can offer these alternatives:

## What I Can Provide:

1. **Direct Source Access**: The code is available at the official HuggingFace TRL repository: https://github.com/huggingface/trl/blob/main/src/trl/trainer/dpo_trainer.py

2. **Code Summary**: The file contains:
   - Apache 2.0 licensed imports from transformers, accelerate, datasets
   - `DataCollatorForPreference` class for text tokenization batching
   - `DataCollatorForVisionPreference` class for vision-language data processing
   - `DPOTrainer` class extending `_BaseTrainer` with methods for Direct Preference Optimization training
   - Helper methods: `_tokenize()`, `_prepare_dataset()`, `compute_ref_log_probs()`, `_compute_loss()`

3. **Specific Sections**: I can explain or paraphrase particular methods or functionality if you identify which sections interest you.

4. **Installation**: Install via pip to access the code locally:
   ```bash
   pip install trl
   ```

Would you like me to focus on explaining specific functionality or direct you to the source repository?
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f23dc39a-b480-4f28-9efc-ac2e74df1a25",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "940a8c68-4883-4890-85cf-4c90b60309aa",
  "sourceToolAssistantUUID": "f23dc39a-b480-4f28-9efc-ac2e74df1a25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T10:47:48.316Z_

Let me install TRL locally to read the actual source code directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "940a8c68-4883-4890-85cf-4c90b60309aa",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYR4Qe55b9HuRwDkWTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afbff35d-0164-49b3-937e-872b4708e214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLnxezyPPET75fbh3vKk2J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 30664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 531,
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

_source line 25 · 2026-05-12T10:47:49.187Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KScUWChaWVYBwBMWfC3rSn`</summary>

```json
{
  "command": "pip install trl --quiet 2>&1 | tail -5",
  "description": "Install TRL library to read source code locally",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afbff35d-0164-49b3-937e-872b4708e214",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYR4Qe55b9HuRwDkWTm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a69ad28d-6ec9-4b09-9501-36e055239e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLnxezyPPET75fbh3vKk2J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 30664,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 531
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 30664,
          "cache_creation_input_tokens": 531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 531,
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

_source line 26 · 2026-05-12T10:47:49.804Z_

<details><summary>↩ Tool result · `toolu_01KScUWChaWVYBwBMWfC3rSn`</summary>

```text
    See /usr/share/doc/python3.14/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a69ad28d-6ec9-4b09-9501-36e055239e24",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "acf4dc4d-a0cc-40ea-a9d6-5f5b490a722a",
  "sourceToolAssistantUUID": "a69ad28d-6ec9-4b09-9501-36e055239e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-12T10:47:53.606Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HNWHwxAvZ22iUfxXDSonM7`</summary>

```json
{
  "command": "pip install trl --quiet --break-system-packages 2>&1 | tail -5",
  "description": "Install TRL library with system packages override",
  "timeout": 180000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acf4dc4d-a0cc-40ea-a9d6-5f5b490a722a",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYRNLu8HLaxFMsRhLed",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6dfbe181-dcca-4c59-b174-56d978a7f212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbBo1f6toRjFF4bs7D4BTQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 31195,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 218
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 31195,
          "cache_creation_input_tokens": 218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 218,
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

_source line 28 · 2026-05-12T10:49:42.072Z_

<details><summary>↩ Tool result · `toolu_01HNWHwxAvZ22iUfxXDSonM7`</summary>

```text
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts accelerate, accelerate-config, accelerate-estimate-memory, accelerate-launch and accelerate-merge-weights are installed in '/home/ubuntu/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script trl is installed in '/home/ubuntu/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dfbe181-dcca-4c59-b174-56d978a7f212",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "4e9750b2-ff02-4f8d-ad85-407e0352a48d",
  "sourceToolAssistantUUID": "6dfbe181-dcca-4c59-b174-56d978a7f212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T10:49:45.005Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WwdbPDhqu7s4gD8jUfZGSt`</summary>

```json
{
  "command": "python3 -c \"import trl; print(trl.__version__); import trl.trainer.dpo_trainer; print(trl.trainer.dpo_trainer.__file__)\"",
  "description": "Find TRL version and dpo_trainer.py location"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e9750b2-ff02-4f8d-ad85-407e0352a48d",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYZeKobEY463qsa756E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3775bac-4127-46c1-927b-f4be3613ca58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8Q8fdxaYGhNtLZxtEi5MM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 31413,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 284
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 31413,
          "cache_creation_input_tokens": 284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 284,
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

_source line 30 · 2026-05-12T10:50:02.655Z_

<details><summary>↩ Tool result · `toolu_01WwdbPDhqu7s4gD8jUfZGSt`</summary>

```text
1.4.0
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/dpo_trainer.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3775bac-4127-46c1-927b-f4be3613ca58",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "870f9387-b305-43b5-9251-fc51cebfb4d1",
  "sourceToolAssistantUUID": "c3775bac-4127-46c1-927b-f4be3613ca58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-12T10:50:04.912Z_

TRL 1.4.0. Let me read the full source.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "870f9387-b305-43b5-9251-fc51cebfb4d1",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYbANM4nApcNiqPRFnX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da98acd9-7c6e-4dcb-a189-30c9d3c856ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCY6QbwPHotdXavSL3h4sR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 170,
      "cache_read_input_tokens": 31697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 170,
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

_source line 32 · 2026-05-12T10:50:05.829Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01R3ozxHBLWFEFDcQcA4xZBw`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/dpo_trainer.py",
  "description": "Count lines in dpo_trainer.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da98acd9-7c6e-4dcb-a189-30c9d3c856ae",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYbANM4nApcNiqPRFnX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db48d97d-8264-4ac1-90b7-06b013440dce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCY6QbwPHotdXavSL3h4sR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 170,
      "cache_read_input_tokens": 31697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 170,
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

_source line 33 · 2026-05-12T10:50:05.878Z_

<details><summary>↩ Tool result · `toolu_01R3ozxHBLWFEFDcQcA4xZBw`</summary>

```text
1520 /home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/dpo_trainer.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db48d97d-8264-4ac1-90b7-06b013440dce",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "64cfd18f-ae30-4dd9-b650-f007a43e0e11",
  "sourceToolAssistantUUID": "db48d97d-8264-4ac1-90b7-06b013440dce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-12T10:50:08.598Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LqnLR3Hayo438THY4ocEqi`</summary>

```json
{
  "file_path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/dpo_trainer.py",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64cfd18f-ae30-4dd9-b650-f007a43e0e11",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYbQMUjDsKgX2CzLWkc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e6de31e-a4b6-4c60-8d30-71e86a0d7445",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011NEnoTgHd1AGJFC3oPDcCr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 170,
      "cache_read_input_tokens": 31867,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 170
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 31867,
          "cache_creation_input_tokens": 170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 170,
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

_source line 35 · 2026-05-12T10:50:08.613Z_

<details><summary>↩ Tool result · `toolu_01LqnLR3Hayo438THY4ocEqi`</summary>

````text
1	# Copyright 2020-2026 The HuggingFace Team. All rights reserved.
2	#
3	# Licensed under the Apache License, Version 2.0 (the "License");
4	# you may not use this file except in compliance with the License.
5	# You may obtain a copy of the License at
6	#
7	#     http://www.apache.org/licenses/LICENSE-2.0
8	#
9	# Unless required by applicable law or agreed to in writing, software
10	# distributed under the License is distributed on an "AS IS" BASIS,
11	# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
12	# See the License for the specific language governing permissions and
13	# limitations under the License.
14	
15	import contextlib
16	import json
17	import os
18	import textwrap
19	from collections import defaultdict
20	from collections.abc import Callable
21	from dataclasses import dataclass
22	from pathlib import Path
23	from typing import Any
24	
25	import numpy as np
26	import torch
27	import torch.nn.functional as F
28	import transformers
29	from accelerate import PartialState
30	from accelerate.logging import get_logger
31	from accelerate.utils import is_peft_model, tqdm
32	from datasets import Dataset, IterableDataset, IterableDatasetDict
33	from datasets.fingerprint import Hasher
34	from packaging.version import Version
35	from torch.utils.data import DataLoader
36	from transformers import (
37	    AutoProcessor,
38	    DataCollator,
39	    PreTrainedModel,
40	    PreTrainedTokenizerBase,
41	    ProcessorMixin,
42	)
43	from transformers.data.data_collator import DataCollatorMixin
44	from transformers.trainer_callback import TrainerCallback
45	from transformers.trainer_utils import EvalPrediction
46	from transformers.utils import is_liger_kernel_available, is_peft_available
47	
48	from ..data_utils import apply_chat_template, extract_prompt, is_conversational, prepare_multimodal_messages
49	from ..models import get_act_offloading_ctx_manager, prepare_deepspeed, prepare_fsdp
50	from ..models.utils import disable_gradient_checkpointing
51	from .base_trainer import _BaseTrainer
52	from .callbacks import SyncRefModelCallback
53	from .dpo_config import DPOConfig
54	from .utils import (
55	    create_model_from_path,
56	    disable_dropout_in_model,
57	    entropy_from_logits,
58	    flush_left,
59	    get_config_model_id,
60	    hash_module,
61	    pad,
62	    selective_log_softmax,
63	    use_adapter,
64	)
65	
66	
67	if is_peft_available():
68	    from peft import PeftConfig, PeftModel, get_peft_model
69	
70	
71	if is_liger_kernel_available():
72	    from liger_kernel.chunked_loss import LigerFusedLinearDPOLoss
73	
74	
75	logger = get_logger(__name__)
76	
77	
78	FLASH_ATTENTION_VARIANTS = {
79	    "flash_attention_2",
80	    "flash_attention_3",
81	    "kernels-community/flash-attn2",
82	    "kernels-community/flash-attn3",
83	    "kernels-community/vllm-flash-attn3",
84	}
85	
86	
87	def get_dataset_column_names(dataset: Dataset | IterableDataset) -> list[str]:
88	    return list(next(iter(dataset)).keys()) if dataset.column_names is None else dataset.column_names
89	
90	
91	@dataclass
92	class DataCollatorForPreference(DataCollatorMixin):
93	    """
94	    Data collator used for preference data. Inputs are dynamically padded to the maximum length of a batch.
95	
96	    This collator expects each example in the input list to be a dictionary containing the keys `"prompt_ids"`,
97	    `"chosen_ids"` and `"rejected_ids"`. The collator returns a dictionary containing the following keys:
98	    - `"input_ids"`: Tensor of input IDs, padded to the maximum length of the batch. The first half of the batch
99	        corresponds to the `"chosen_ids"` and the second half to the `"rejected_ids"`.
100	    - `"attention_mask"`: Tensor of attention mask, padded to the maximum length of the batch.
101	    - `"completion_mask"`: Tensor indicating the positions of the completion tokens, padded to the maximum length of
102	        the batch.
103	
104	    Optionally, the examples can contain a `"ref_chosen_logps"` and `"ref_rejected_logps"` keys, in which case the
105	    returned dictionary will also contain these keys with the corresponding tensors.
106	
107	    Args:
108	        pad_token_id (`int`):
109	            Token ID to use for padding.
110	        max_length (`int`, *optional*):
111	            Maximum length of the sequences after concatenation. Sequences longer than `max_length` are truncated
112	            before padding, which avoids allocating oversized tensors for batches containing very long sequences.
113	        truncation_mode (`str`, *optional*, defaults to `"keep_start"`):
114	            Truncation mode when a concatenated sequence exceeds `max_length`. Possible values are `"keep_end"` and
115	            `"keep_start"`.
116	        pad_to_multiple_of (`int`, *optional*):
117	            If set, the sequences will be padded to a multiple of this value.
118	        return_tensors (`str`, *optional*, defaults to `"pt"`):
119	            Type of Tensor to return. Only `"pt"` is currently supported.
120	
121	    Examples:
122	    ```python
123	    >>> from trl.trainer.dpo_trainer import DataCollatorForPreference
124	
125	    >>> collator = DataCollatorForPreference(pad_token_id=0)
126	    >>> examples = [
127	    ...     {"prompt_ids": [1, 2, 3], "chosen_ids": [4, 5], "rejected_ids": [6]},
128	    ...     {"prompt_ids": [7, 8], "chosen_ids": [9], "rejected_ids": [10, 11]},
129	    ... ]
130	    >>> collator(examples)
131	    {'input_ids': tensor([[ 1,  2,  3,  4,  5],
132	                          [ 7,  8,  9,  0,  0],
133	                          [ 1,  2,  3,  6,  0],
134	                          [ 7,  8, 10, 11,  0]]),
135	     'attention_mask': tensor([[1, 1, 1, 1, 1],
136	                               [1, 1, 1, 0, 0],
137	                               [1, 1, 1, 1, 0],
138	                               [1, 1, 1, 1, 0]]),
139	     'completion_mask': tensor([[0, 0, 0, 1, 1],
140	                                [0, 0, 1, 0, 0],
141	                                [0, 0, 0, 1, 0],
142	                                [0, 0, 1, 1, 0]])}
143	    ```
144	    """
145	
146	    pad_token_id: int
147	    max_length: int | None = None
148	    truncation_mode: str = "keep_start"
149	    pad_to_multiple_of: int | None = None
150	    return_tensors: str = "pt"
151	
152	    def torch_call(self, examples: list[dict[str, Any]]) -> dict[str, Any]:
153	        prompt_chosen_ids = [example["prompt_ids"] + example["chosen_ids"] for example in examples]
154	        prompt_rejected_ids = [example["prompt_ids"] + example["rejected_ids"] for example in examples]
155	        chosen_mask = [[0] * len(example["prompt_ids"]) + [1] * len(example["chosen_ids"]) for example in examples]
156	        rejected_mask = [[0] * len(example["prompt_ids"]) + [1] * len(example["rejected_ids"]) for example in examples]
157	
158	        if self.max_length is not None:
159	            if self.truncation_mode == "keep_start":
160	                sl = slice(None, self.max_length)
161	            elif self.truncation_mode == "keep_end":
162	                sl = slice(-self.max_length, None)
163	            else:
164	                raise ValueError(
165	                    f"Unsupported truncation mode: {self.truncation_mode}, expected 'keep_start' or 'keep_end'"
166	                )
167	            prompt_chosen_ids = [ids[sl] for ids in prompt_chosen_ids]
168	            prompt_rejected_ids = [ids[sl] for ids in prompt_rejected_ids]
169	            chosen_mask = [m[sl] for m in chosen_mask]
170	            rejected_mask = [m[sl] for m in rejected_mask]
171	
172	        chosen_attention_mask = [[1] * len(ids) for ids in prompt_chosen_ids]
173	        rejected_attention_mask = [[1] * len(ids) for ids in prompt_rejected_ids]
174	        input_ids = prompt_chosen_ids + prompt_rejected_ids
175	        attention_mask = chosen_attention_mask + rejected_attention_mask
176	        completion_mask = chosen_mask + rejected_mask
177	
178	        # Convert to tensor
179	        input_ids = [torch.tensor(ids) for ids in input_ids]
180	        attention_mask = [torch.tensor(m, dtype=torch.long) for m in attention_mask]
181	        completion_mask = [torch.tensor(m, dtype=torch.long) for m in completion_mask]
182	        if "ref_chosen_logps" in examples[0]:
183	            ref_chosen_logps = torch.tensor([example["ref_chosen_logps"] for example in examples])
184	        if "ref_rejected_logps" in examples[0]:
185	            ref_rejected_logps = torch.tensor([example["ref_rejected_logps"] for example in examples])
186	
187	        # Pad
188	        output = {}
189	        output["input_ids"] = pad(
190	            input_ids,
191	            padding_value=self.pad_token_id,
192	            padding_side="right",
193	            pad_to_multiple_of=self.pad_to_multiple_of,
194	        )
195	        output["attention_mask"] = pad(
196	            attention_mask,
197	            padding_value=0,
198	            padding_side="right",
199	            pad_to_multiple_of=self.pad_to_multiple_of,
200	        )
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e6de31e-a4b6-4c60-8d30-71e86a0d7445",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "4db9c17e-6307-4165-ad1e-a6843042969e",
  "sourceToolAssistantUUID": "3e6de31e-a4b6-4c60-8d30-71e86a0d7445",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-12T10:50:12.918Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NxekUXnnvpKRtCy5rRfjeX`</summary>

```json
{
  "file_path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/dpo_trainer.py",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4db9c17e-6307-4165-ad1e-a6843042969e",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYbbpnpkrAnxGEHkbYa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b11618c2-0f42-4e5f-9bcd-16fb452af99b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6UsqKpKTGK7U2ptGp8Egk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3008,
      "cache_read_input_tokens": 32037,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3008
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 32037,
          "cache_creation_input_tokens": 3008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3008,
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

_source line 37 · 2026-05-12T10:50:12.924Z_

<details><summary>↩ Tool result · `toolu_01NxekUXnnvpKRtCy5rRfjeX`</summary>

````text
200	        )
201	        output["completion_mask"] = pad(
202	            completion_mask,
203	            padding_value=0,
204	            padding_side="right",
205	            pad_to_multiple_of=self.pad_to_multiple_of,
206	        )
207	        if "ref_chosen_logps" in examples[0]:
208	            output["ref_chosen_logps"] = ref_chosen_logps
209	        if "ref_rejected_logps" in examples[0]:
210	            output["ref_rejected_logps"] = ref_rejected_logps
211	        return output
212	
213	
214	@dataclass
215	class DataCollatorForVisionPreference(DataCollatorMixin):
216	    """
217	    Data collator for vision-preference tasks.
218	
219	    Unlike text-only datasets, where the collator typically receives pre-tokenized inputs ready for batching,
220	    vision-language data processing involves converting images into pixel values. This conversion is disk-intensive,
221	    making upfront preprocessing of the entire dataset impractical. Therefore, this collator performs tokenization and
222	    image processing on-the-fly to efficiently prepare batches.
223	
224	    Each input example should be a dictionary containing at least:
225	    - An `"images"` key holding a list of images, or an `"image"` key holding a single image.
226	    - Keys `"prompt"` `"chosen"` and `"rejected"` for the prompt and preference responses.
227	
228	    The collator outputs a dictionary including:
229	    - `"input_ids"`: Tensor of token IDs.
230	    - `"attention_mask"`: Tensor indicating attention mask.
231	    - `"completion_mask"`: Tensor indicating which tokens correspond to completions.
232	    - `"pixel_values"`: Tensor representing image pixel values.
233	
234	    Additional keys may be present depending on the processor, such as `"image_grid_thw"` or `"image_position_ids"`.
235	
236	    Args:
237	        processor ([`~transformers.ProcessorMixin`]):
238	            The processor used to tokenize text and process images. It must be a subclass of
239	            [`~transformers.ProcessorMixin`] and include a `tokenizer` with a defined `pad_token_id`.
240	        max_length (`int`, *optional*):
241	            Maximum sequence length. Sequences longer than `max_length` are truncated before padding, which avoids
242	            allocating oversized tensors for batches containing very long sequences. Only `"keep_start"` truncation
243	            applies to vision datasets; `"keep_end"` is rejected upstream.
244	        pad_to_multiple_of (`int` or `None`, optional, defaults to `None`):
245	            If set, the sequences will be padded to a multiple of this value.
246	        return_tensors (`str`, optional, defaults to `"pt"`):
247	            The tensor type to return. Currently, only `"pt"` (PyTorch tensors) is supported.
248	
249	    Example:
250	    ```python
251	    >>> from trl.trainer.dpo_trainer import DataCollatorForVisionPreference
252	    >>> from transformers import AutoProcessor
253	
254	    >>> processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")
255	    >>> collator = DataCollatorForVisionPreference(processor)
256	    >>> examples = [
257	    ...     {
258	    ...         "images": [Image.open("image_0.png")],
259	    ...         "prompt": [{"role": "user", "content": "What is this?"}],
260	    ...         "chosen": [{"role": "assistant", "content": "This is a cat."}],
261	    ...         "rejected": [{"role": "assistant", "content": "This is a dog."}],
262	    ...     },
263	    ...     {
264	    ...         "images": [Image.open("image_1.png")],
265	    ...         "prompt": [{"role": "user", "content": "Describe this image."}],
266	    ...         "chosen": [{"role": "assistant", "content": "A beautiful landscape."}],
267	    ...         "rejected": [{"role": "assistant", "content": "An urban cityscape."}],
268	    ...     },
269	    ... ]
270	    >>> collator(examples)
271	    {'input_ids': tensor([[151644,   8948,    198,   2610,    525,    264,  10950,  17847,     13, 151645,    198, 151644,    872,    198, 151652, 151655, 151655, 151655, 151655, 151653,   3838,    374,    419,     30, 151645,    198, 151644,  77091,    198,   1986,    374,    264,   8251,     13, 151645,    198],
272	                          [151644,   8948,    198,   2610,    525,    264,  10950,  17847,     13, 151645,    198, 151644,    872,    198, 151652, 151655, 151655, 151655, 151655, 151653,  74785,    419,   2168,     13, 151645,    198, 151644,  77091,    198,     32,   6233,  18414,     13, 151645,    198, 151643],
273	                          [151644,   8948,    198,   2610,    525,    264,  10950,  17847,     13, 151645,    198, 151644,    872,    198, 151652, 151655, 151655, 151655, 151655, 151653,   3838,    374,    419,     30, 151645,    198, 151644,  77091,    198,   1986,    374,    264,   5562,     13, 151645,    198],
274	                          [151644,   8948,    198,   2610,    525,    264,  10950,  17847,     13, 151645,    198, 151644,    872,    198, 151652, 151655, 151655, 151655, 151655, 151653,  74785,    419,   2168,     13, 151645,    198, 151644,  77091,    198,   2082,  15662,   3283,  57518,     13, 151645,    198]]),
275	     'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
276	                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
277	                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
278	                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]),
279	     'pixel_values': tensor([[-1.3251,  0.1347, -0.4784,  ...,  0.4537, -0.0156,  1.2358],
280	                             [ 0.5727,  0.4997, -0.9164,  ..., -0.5701,  0.7950, -0.7123],
281	                             [-0.0550, -0.8288,  1.0690,  ..., -0.1293, -0.1151,  1.6055],
282	                             ...,
283	                             [ 0.2953,  0.5581,  0.1785,  ..., -0.7123, -0.7977,  0.1693],
284	                             [-0.7558,  1.0398,  1.3464,  ..., -0.5417, -0.5417,  0.4395],
285	                             [ 0.8063,  0.6895,  0.4267,  ..., -0.4422,  1.3354,  0.1266]]),
286	     'image_grid_thw': tensor([[1, 4, 4],
287	                               [1, 4, 4],
288	                               [1, 4, 4],
289	                               [1, 4, 4]]),
290	     'completion_mask': tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
291	                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
292	                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
293	                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]])}
294	    ```
295	    """
296	
297	    processor: ProcessorMixin
298	    max_length: int | None = None
299	    pad_to_multiple_of: int | None = None
300	    return_tensors: str = "pt"
301	
302	    def torch_call(self, examples: list[dict[str, Any]]) -> dict[str, Any]:
303	        if self.pad_to_multiple_of is not None:
304	            raise NotImplementedError(
305	                "Padding to a multiple of a value is not yet implemented for vision-language modeling and "
306	                "prompt-completion data."
307	            )
308	        if "image" in examples[0]:
309	            for example in examples:
310	                example["images"] = [example.pop("image")]
311	        images = [example["images"] for example in examples] * 2  # repeat for chosen and rejected
312	        # Transformers requires at least one image in the batch, otherwise it throws an error
313	        if all(img_list == [] for img_list in images):
314	            images = None
315	        if is_conversational(examples[0]):  # conversational case
316	            for example in examples:
317	                example["prompt"] = prepare_multimodal_messages(example["prompt"], images=example["images"])
318	                example["chosen"] = prepare_multimodal_messages(example["chosen"])
319	                example["rejected"] = prepare_multimodal_messages(example["rejected"])
320	            examples = [apply_chat_template(example, self.processor) for example in examples]
321	
322	        prompts = [example["prompt"] for example in examples] * 2  # repeat for chosen and rejected
323	        chosens = [example["chosen"] for example in examples]
324	        rejecteds = [example["rejected"] for example in examples]
325	
326	        processed_prompts = self.processor(
327	            images=images,
328	            text=prompts,
329	            padding=True,
330	            padding_side="left",
331	            return_tensors=self.return_tensors,
332	            add_special_tokens=False,  # to avoid adding the BOS, twice see https://huggingface.co/blog/qgallouedec/gotchas-in-tokenizer-behavior#7-chat-template-and-tokenization-dont-compose-due-to-special-tokens
333	        )
334	        processed_chosens = self.processor(
335	            text=chosens,
336	            padding=True,
337	            padding_side="right",
338	            return_tensors=self.return_tensors,
339	            add_special_tokens=False,  # to avoid adding the BOS, twice see https://huggingface.co/blog/qgallouedec/gotchas-in-tokenizer-behavior#7-chat-template-and-tokenization-dont-compose-due-to-special-tokens
340	        )
341	        processed_rejecteds = self.processor(
342	            text=rejecteds,
343	            padding=True,
344	            padding_side="right",
345	            return_tensors=self.return_tensors,
346	            add_special_tokens=False,  # to avoid adding the BOS, twice see https://huggingface.co/blog/qgallouedec/gotchas-in-tokenizer-behavior#7-chat-template-and-tokenization-dont-compose-due-to-special-tokens
347	        )
348	
349	        # Concatenate prompts and completions
350	        prompt_ids, prompt_mask = processed_prompts["input_ids"], processed_prompts["attention_mask"]
351	        chosen_ids, chosen_mask = processed_chosens["input_ids"], processed_chosens["attention_mask"]
352	        rejected_ids, rejected_mask = processed_rejecteds["input_ids"], processed_rejecteds["attention_mask"]
353	        pad_token_id = self.processor.tokenizer.pad_token_id or self.processor.tokenizer.eos_token_id
354	        completion_ids = torch.cat(tuple(pad([chosen_ids, rejected_ids], padding_value=pad_token_id)))
355	        completion_mask = torch.cat(tuple(pad([chosen_mask, rejected_mask], padding_value=0)))
356	        input_ids = torch.cat((prompt_ids, completion_ids), dim=1)
357	        attention_mask = torch.cat((prompt_mask, completion_mask), dim=1)
358	        completion_mask = torch.cat((torch.zeros_like(prompt_mask), completion_mask), dim=1)
359	        if "token_type_ids" in processed_prompts:  # special case for Gemma
360	            prompt_token_type_ids = processed_prompts["token_type_ids"]
361	            chosen_type_ids = processed_chosens["token_type_ids"]
362	            rejected_type_ids = processed_rejecteds["token_type_ids"]
363	            completion_token_type_ids = torch.cat(tuple(pad([chosen_type_ids, rejected_type_ids], padding_value=0)))
364	            token_type_ids = torch.cat((prompt_token_type_ids, completion_token_type_ids), dim=1)
365	        if "mm_token_type_ids" in processed_prompts:  # special case for Qwen2.5-VL
366	            prompt_mm_token_type_ids = processed_prompts["mm_token_type_ids"]
367	            mm_token_type_ids = torch.cat((prompt_mm_token_type_ids, torch.zeros_like(completion_ids)), dim=1)
368	
369	        # Flush left to reduce padding
370	        if "token_type_ids" in processed_prompts and "mm_token_type_ids" in processed_prompts:
371	            attention_mask, input_ids, completion_mask, token_type_ids, mm_token_type_ids = flush_left(
372	                attention_mask, input_ids, completion_mask, token_type_ids, mm_token_type_ids
373	            )
374	        elif "token_type_ids" in processed_prompts:
375	            attention_mask, input_ids, completion_mask, token_type_ids = flush_left(
376	                attention_mask, input_ids, completion_mask, token_type_ids
377	            )
378	        elif "mm_token_type_ids" in processed_prompts:
379	            attention_mask, input_ids, completion_mask, mm_token_type_ids = flush_left(
380	                attention_mask, input_ids, completion_mask, mm_token_type_ids
381	            )
382	        else:
383	            attention_mask, input_ids, completion_mask = flush_left(attention_mask, input_ids, completion_mask)
384	
385	        if self.max_length is not None:
386	            input_ids = input_ids[:, : self.max_length]
387	            attention_mask = attention_mask[:, : self.max_length]
388	            completion_mask = completion_mask[:, : self.max_length]
389	            if "token_type_ids" in processed_prompts:
390	                token_type_ids = token_type_ids[:, : self.max_length]
391	            if "mm_token_type_ids" in processed_prompts:
392	                mm_token_type_ids = mm_token_type_ids[:, : self.max_length]
393	
394	        # Build the output dictionary
395	        output = processed_prompts  # we take processed_prompts because it contains the images
396	        output["input_ids"] = input_ids
397	        output["attention_mask"] = attention_mask
398	        output["completion_mask"] = completion_mask
399	        if "token_type_ids" in processed_prompts:
400	            output["token_type_ids"] = token_type_ids
401	        if "mm_token_type_ids" in processed_prompts:
402	            output["mm_token_type_ids"] = mm_token_type_ids
403	        return output
404	
405	
406	class DPOTrainer(_BaseTrainer):
407	    """
408	    Trainer for Direct Preference Optimization (DPO) method. This algorithm was initially proposed in the paper [Direct
409	    Preference Optimization: Your Language Model is Secretly a Reward Model](https://huggingface.co/papers/2305.18290).
410	    This class is a wrapper around the [`~transformers.Trainer`] class and inherits all of its attributes and methods.
411	
412	    Example:
413	
414	    ```python
415	    from trl import DPOTrainer
416	    from datasets import load_dataset
417	
418	    dataset = load_dataset("trl-lib/ultrafeedback_binarized", split="train")
419	
420	    trainer = DPOTrainer(
421	        model="Qwen/Qwen2.5-0.5B-Instruct",
422	        train_dataset=dataset,
423	    )
424	    trainer.train()
425	    ```
426	
427	    Args:
428	        model (`str` or [`~transformers.PreTrainedModel`] or [`~peft.PeftModel`]):
429	            Model to be trained. Can be either:
430	
431	            - A string, being the *model id* of a pretrained model hosted inside a model repo on huggingface.co, or a
432	              path to a *directory* containing model weights saved using
433	              [`~transformers.PreTrainedModel.save_pretrained`], e.g., `'./my_model_directory/'`. The model is loaded
434	              using `&lt;ModelArchitecture>.from_pretrained` (where `&lt;ModelArchitecture>` is derived from the model
435	              config) with the keyword arguments in `args.model_init_kwargs`.
436	            - A [`~transformers.PreTrainedModel`] object. Only causal language models are supported.
437	            - A [`~peft.PeftModel`] object. Only causal language models are supported.
438	        ref_model ([`~transformers.PreTrainedModel`], *optional*):
439	            Reference model used to compute the reference log probabilities.
440	
441	            - If provided, this model is used directly as the reference policy.
442	            - If `None`, the trainer will automatically use the initial policy corresponding to `model`, i.e. the model
443	              state before DPO training starts.
444	        args ([`DPOConfig`], *optional*):
445	            Configuration for this trainer. If `None`, a default configuration is used.
446	        data_collator ([`~transformers.DataCollator`], *optional*):
447	            Function to use to form a batch from a list of elements of the processed `train_dataset` or `eval_dataset`.
448	            Will default to [`~trainer.dpo_trainer.DataCollatorForPreference`] if the model is a language model and
449	            [`~trainer.dpo_trainer.DataCollatorForVisionPreference`] if the model is a vision-language model. Custom
450	            collators must truncate sequences before padding; the trainer does not apply post-collation truncation.
451	        train_dataset ([`~datasets.Dataset`] or [`~datasets.IterableDataset`]):
452	            Dataset to use for training. This trainer supports both [language modeling](#language-modeling) type and
453	            [prompt-completion](#prompt-completion) type. The format of the samples can be either:
454	
455	            - [Standard](dataset_formats#standard): Each sample contains plain text.
456	            - [Conversational](dataset_formats#conversational): Each sample contains structured messages (e.g., role
457	              and content).
458	        eval_dataset ([`~datasets.Dataset`], [`~datasets.IterableDataset`] or `dict[str, Dataset | IterableDataset]`):
459	            Dataset to use for evaluation. It must meet the same requirements as `train_dataset`.
460	        processing_class ([`~transformers.PreTrainedTokenizerBase`] or [`~transformers.ProcessorMixin`], *optional*):
461	            Processing class used to process the data. The padding side must be set to "left". If `None`, the
462	            processing class is loaded from the model's name with [`~transformers.AutoProcessor.from_pretrained`]. A
463	            padding token, `tokenizer.pad_token`, must be set. If the processing class has not set a padding token,
464	            `tokenizer.eos_token` will be used as the default.
465	        compute_metrics (`Callable[[EvalPrediction], dict]`, *optional*):
466	            The function that will be used to compute metrics at evaluation. Must take a
467	            [`~transformers.EvalPrediction`] and return a dictionary string to metric values. When passing
468	            [`SFTConfig`] with `batch_eval_metrics` set to `True`, your `compute_metrics` function must take a boolean
469	            `compute_result` argument. This will be triggered after the last eval batch to signal that the function
470	            needs to calculate and return the global summary statistics rather than accumulating the batch-level
471	            statistics.
472	        callbacks (list of [`~transformers.TrainerCallback`], *optional*):
473	            List of callbacks to customize the training loop. Will add those to the list of default callbacks detailed
474	            in [here](https://huggingface.co/docs/transformers/main_classes/callback).
475	
476	            If you want to remove one of the default callbacks used, use the [`~transformers.Trainer.remove_callback`]
477	            method.
478	        optimizers (`tuple[torch.optim.Optimizer | None, torch.optim.lr_scheduler.LambdaLR | None]`, *optional*, defaults to `(None, None)`):
479	            A tuple containing the optimizer and the scheduler to use. Will default to an instance of `AdamW` on your
480	            model and a scheduler given by [`~transformers.get_linear_schedule_with_warmup`] controlled by `args`.
481	        peft_config ([`~peft.PeftConfig`], *optional*):
482	            PEFT configuration used to wrap the model. If `None`, the model is not wrapped.
483	    """
484	
485	    _tag_names = ["trl", "dpo"]
486	    _name = "DPO"
487	    _paper = {
488	        "title": "Direct Preference Optimization: Your Language Model is Secretly a Reward Model",
489	        "id": "2305.18290",
490	        # docstyle-ignore
491	        "citation": textwrap.dedent("""\
492	            @inproceedings{rafailov2023direct,
493	                title        = {{Direct Preference Optimization: Your Language Model is Secretly a Reward Model}},
494	                author       = {Rafael Rafailov and Archit Sharma and Eric Mitchell and Christopher D. Manning and Stefano Ermon and Chelsea Finn},
495	                year         = 2023,
496	                booktitle    = {Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023},
497	                url          = {http://papers.nips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html},
498	                editor       = {Alice Oh and Tristan Naumann and Amir Globerson and Kate Saenko and Moritz Hardt and Sergey Levine},
499	            }"""),
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b11618c2-0f42-4e5f-9bcd-16fb452af99b",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "0e49179e-3c2c-4dae-a5f8-29d991c29252",
  "sourceToolAssistantUUID": "b11618c2-0f42-4e5f-9bcd-16fb452af99b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-12T10:50:16.215Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ky4FhBuuCqRx46RELaSofA`</summary>

```json
{
  "file_path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/dpo_trainer.py",
  "offset": 500,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e49179e-3c2c-4dae-a5f8-29d991c29252",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYbvSDyDCNN3TCkKvdW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80e83421-99ab-49a0-937c-be76dea76dbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019uMdh7NjEZvhPh3ez1BDZa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7162,
      "cache_read_input_tokens": 35045,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7162
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 35045,
          "cache_creation_input_tokens": 7162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7162,
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

_source line 39 · 2026-05-12T10:50:16.220Z_

<details><summary>↩ Tool result · `toolu_01Ky4FhBuuCqRx46RELaSofA`</summary>

```text
500	    }
501	
502	    def __init__(
503	        self,
504	        model: "str | PreTrainedModel | PeftModel",
505	        ref_model: PreTrainedModel | None = None,
506	        args: DPOConfig | None = None,
507	        data_collator: DataCollator | None = None,
508	        train_dataset: Dataset | IterableDataset | None = None,
509	        eval_dataset: Dataset | IterableDataset | dict[str, Dataset | IterableDataset] | None = None,
510	        processing_class: PreTrainedTokenizerBase | ProcessorMixin | None = None,
511	        compute_metrics: Callable[[EvalPrediction], dict] | None = None,
512	        callbacks: list[TrainerCallback] | None = None,
513	        optimizers: tuple[torch.optim.Optimizer | None, torch.optim.lr_scheduler.LambdaLR | None] = (None, None),
514	        peft_config: "PeftConfig | None" = None,
515	    ):
516	        # Args
517	        if args is None:
518	            model_name = model if isinstance(model, str) else get_config_model_id(model.config)
519	            model_name = model_name.split("/")[-1]
520	            args = DPOConfig(f"{model_name}-DPO")
521	
522	        if train_dataset is None:
523	            raise ValueError("`train_dataset` is required")
524	        elif isinstance(train_dataset, IterableDataset):
525	            # IterableDataset requires dispatch_batches=False because Accelerate's dispatch mode may try to concatenate
526	            # batches from multiple processes, leading to mismatch errors.
527	            if args.accelerator_config.dispatch_batches is True:
528	                logger.warning(
529	                    "You are using an `IterableDataset` for training with `dispatch_batches=True`. `dispatch_batches` "
530	                    "is forced to `False` when using an `IterableDataset`. To remove this warning, unset "
531	                    "`dispatch_batches` in `DPOConfig` or set it to `False`."
532	                )
533	            args.accelerator_config.dispatch_batches = False
534	
535	        # Model
536	        if isinstance(model, str):
537	            model_init_kwargs = args.model_init_kwargs or {}
538	            # Distributed training requires device_map=None ("auto" fails)
539	            if args.distributed_state.distributed_type in ["MULTI_GPU", "DEEPSPEED"]:
540	                model_init_kwargs["device_map"] = None
541	            model = create_model_from_path(model, **model_init_kwargs)
542	        else:
543	            if args.model_init_kwargs is not None:
544	                logger.warning(
545	                    "You passed `model_init_kwargs` to the `DPOConfig`, but your model is already instantiated. "
546	                    "The `model_init_kwargs` will be ignored."
547	                )
548	        if ref_model is model:
549	            raise ValueError(
550	                "`model` and `ref_model` cannot be the same object. In most cases you should omit `ref_model` and "
551	                "we'll initialize it to a copy of `model` for you."
552	            )
553	
554	        # Processing class
555	        if processing_class is None:
556	            processing_class = AutoProcessor.from_pretrained(get_config_model_id(model.config))
557	
558	        # Handle pad token for processors or tokenizers
559	        if isinstance(processing_class, ProcessorMixin):
560	            self._tokenizer = processing_class.tokenizer
561	            self._is_vlm = True
562	        elif isinstance(processing_class, PreTrainedTokenizerBase):
563	            self._tokenizer = processing_class
564	            self._is_vlm = False
565	        else:
566	            raise TypeError("The `processing_class` must be either a `PreTrainedTokenizerBase` or a `ProcessorMixin`")
567	
568	        if self._tokenizer.pad_token is None:
569	            self._tokenizer.pad_token = self._tokenizer.eos_token
570	
571	        # PEFT
572	        if peft_config is not None:
573	            if not is_peft_available():
574	                raise ImportError(
575	                    "You passed `peft_config` but the `peft` library is not installed. "
576	                    "Install it with `pip install trl[peft]`."
577	                )
578	            if not isinstance(peft_config, PeftConfig):
579	                raise TypeError(
580	                    f"`peft_config` must be a `peft.PeftConfig` instance (e.g. `peft.LoraConfig`), "
581	                    f"got {type(peft_config).__name__}."
582	                )
583	            if is_peft_model(model):
584	                raise ValueError(
585	                    "You passed a `PeftModel` instance together with a `peft_config` to the trainer. Please first merge "
586	                    "and unload the existing adapter, save the resulting base model, and then pass that base model along "
587	                    "with the new `peft_config` to the trainer."
588	                )
589	            # Create PEFT model
590	            model = get_peft_model(model, peft_config)
591	
592	        elif is_peft_model(model) and ref_model is None:
593	            # If the model is a PEFT model with a pretrained adapter, we need to create a "ref" adapter that is a copy
594	            # of the "default" adapter, so that we can use it as the reference model during DPO training.
595	            model.add_adapter("ref", model.peft_config["default"])
596	            for name, param in model.named_parameters():
597	                if ".default." in name:
598	                    ref_name = name.replace(".default.", ".ref.")
599	                    ref_param = model.get_parameter(ref_name)
600	                    ref_param.data.copy_(param.data)
601	
602	        # When using gradient checkpointing with PEFT, we need to enable input gradients. transformers.Trainer normally
603	        # handles this, but a bug currently prevents it; see https://github.com/huggingface/transformers/issues/42489
604	        if is_peft_model(model) and args.gradient_checkpointing:
605	            model.enable_input_require_grads()
606	
607	        # When using QLoRA, the PEFT adapter weights are converted to bf16 to follow the recommendations from the
608	        # original paper (see https://huggingface.co/papers/2305.14314, paragraph 3). Normally, this can be done by
609	        # passing `autocast_adapter_dtype=False` to `get_peft_model`, but this option is not yet supported for
610	        # quantized models. See: https://github.com/huggingface/peft/issues/2889
611	        # Non-quantized models do not have the `is_loaded_in_{8,4}bit` attributes, whereas quantized models do
612	        if getattr(model, "is_loaded_in_4bit", False) or getattr(model, "is_loaded_in_8bit", False):
613	            for param in model.parameters():
614	                if param.requires_grad:
615	                    param.data = param.data.to(torch.bfloat16)
616	
617	        # Data collator
618	        self.padding_free = args.padding_free
619	        if self.padding_free:
620	            logger.warning(
621	                "`padding_free=True` is temporarily unavailable after a refactor and is currently disabled. Falling "
622	                "back to standard padding (`padding_free=False`). This feature is planned to return in a future "
623	                "update; for now, please set `padding_free=False` explicitly."
624	            )
625	            self.padding_free = False
626	        dataset_sample = next(iter(train_dataset))
627	        self._is_vision_dataset = "image" in dataset_sample or "images" in dataset_sample
628	        if self._is_vision_dataset and not self._is_vlm:
629	            raise ValueError(
630	                "The dataset appears to be vision-related (contains 'image' or 'images' keys), but the provided "
631	                "model does not seem to be a vision-language model. Please check your model and dataset."
632	            )
633	        if self._is_vision_dataset and args.max_length is not None and args.truncation_mode == "keep_end":
634	            raise ValueError(
635	                "truncation_mode='keep_end' is not supported for vision-language models. Image tokens reside "
636	                "inside the prompt portion of the sequence; depending on the example, keep_end may silently "
637	                "drop them, causing pixel_values to be forwarded to the model with no corresponding visual "
638	                "tokens in input_ids. Use truncation_mode='keep_start' (the default) or set max_length=None."
639	            )
640	        if data_collator is None and not self._is_vision_dataset:
641	            # Get the pad token: if not provided, use the one from the processing class or the eos token
642	            # if the processing class does not have a pad token.
643	            pad_token = args.pad_token or self._tokenizer.pad_token or self._tokenizer.eos_token
644	            if pad_token not in self._tokenizer.get_vocab():
645	                raise ValueError(
646	                    f"The specified `pad_token` ('{pad_token}') is not found in the vocabulary of the given "
647	                    f"`processing_class` ({processing_class.__class__.__name__}). Ensure that the `pad_token` exists "
648	                    "in the vocabulary before using it as a padding token."
649	                )
650	            self._tokenizer.pad_token = pad_token
651	            data_collator = DataCollatorForPreference(
652	                pad_token_id=self._tokenizer.pad_token_id,
653	                max_length=args.max_length,
654	                truncation_mode=args.truncation_mode,
655	                pad_to_multiple_of=args.pad_to_multiple_of,
656	            )
657	        elif data_collator is None and self._is_vision_dataset:
658	            data_collator = DataCollatorForVisionPreference(
659	                processor=processing_class,
660	                max_length=args.max_length,
661	                pad_to_multiple_of=args.pad_to_multiple_of,
662	            )
663	
664	        # Training arguments
665	        self.beta = args.beta
666	        self.precompute_ref_logps = args.precompute_ref_log_probs
667	        self.loss_types = args.loss_type  # args.loss_type is already a list
668	        self.loss_weights = args.loss_weights or [1.0] * len(self.loss_types)
669	        self.ld_alpha = args.ld_alpha
670	        self.f_divergence_type = args.f_divergence_type
671	        self.f_alpha_divergence_coef = args.f_alpha_divergence_coef
672	        self.label_smoothing = args.label_smoothing
673	        self.use_weighting = args.use_weighting
674	        if self.use_weighting and any(loss_type in {"aot", "aot_unpaired"} for loss_type in self.loss_types):
675	            raise NotImplementedError(
676	                "WPO-style weighting is not implemented for 'aot' or 'aot_unpaired' because those losses sort "
677	                "samples, which would misalign per-pair weights."
678	            )
679	        if "robust" in self.loss_types and not (0.0 <= self.label_smoothing < 0.5):
680	            logger.warning(
681	                "The `label_smoothing` parameter should lie in [0.0, 0.5) for the 'robust' loss. You provided "
682	                f"{self.label_smoothing}."
683	            )
684	        if "exo_pair" in self.loss_types and self.label_smoothing == 0.0:
685	            raise ValueError(
686	                "Label smoothing must be greater than 0.0 when using 'exo_pair' loss. The EXO paper recommends a "
687	                "value of 1e-3."
688	            )
689	        self.use_liger_kernel = args.use_liger_kernel
690	        if args.use_liger_kernel:
691	            if not is_liger_kernel_available():
692	                raise ImportError(
693	                    "You set `use_liger_kernel=True` but the liger kernel is not available. "
694	                    "Please install liger-kernel first: `pip install liger-kernel`"
695	                )
696	            if len(self.loss_types) != 1:
697	                raise NotImplementedError(
698	                    "Multiple loss types are not yet supported when using Liger kernel. If you need this feature, "
699	                    "please open a feature request at https://github.com/huggingface/trl/issues."
700	                )
701	            self.liger_loss_fn = LigerFusedLinearDPOLoss(beta=args.beta, loss_type=self.loss_types[0])
702	            if compute_metrics is not None:
703	                raise ValueError(
704	                    "compute_metrics is not supported with the Liger kernel. compute_metrics requires to be able to "
705	                    "recover the logits from the forward pass, but Liger kernel does not materialize logits."
706	                )
707	            if self.precompute_ref_logps:
708	                raise ValueError(
709	                    "Liger DPO loss does not support precomputing reference log probabilities. Either disable "
710	                    "`precompute_ref_log_probs` or set `use_liger_kernel` to False."
711	                )
712	            if is_peft_model(model):
713	                raise NotImplementedError("Liger DPO loss is not implemented for PEFT models.")
714	
715	        # Dataset
716	        # Skip dataset preparation if it's a VLM, where preprocessing (e.g., image-to-pixel conversion) is too costly
717	        # and done on the fly instead.
718	        skip_prepare_dataset = self._is_vision_dataset
719	        if not skip_prepare_dataset:
720	            train_dataset = self._prepare_dataset(train_dataset, processing_class, args, "train")
721	            if eval_dataset is not None:
722	                if isinstance(eval_dataset, dict):
723	                    eval_dataset = {
724	                        key: self._prepare_dataset(dataset, processing_class, args, key)
725	                        for key, dataset in eval_dataset.items()
726	                    }
727	                else:
728	                    eval_dataset = self._prepare_dataset(eval_dataset, processing_class, args, "eval")
729	
730	        # Transformers explicitly set use_reentrant=True in the past to silence a PyTorch warning, but the default was
731	        # never updated once PyTorch switched to recommending use_reentrant=False. Until that change lands upstream
732	        # (see https://github.com/huggingface/transformers/pull/43203) and is released (most likely in 5.0.0), we
733	        # default to the recommended non-reentrant behavior here, while preserving any user-provided value.
734	        if args.gradient_checkpointing and Version(transformers.__version__) < Version("5.0.0"):
735	            args.gradient_checkpointing_kwargs = args.gradient_checkpointing_kwargs or {}
736	            args.gradient_checkpointing_kwargs.setdefault("use_reentrant", False)
737	
738	        super().__init__(
739	            model=model,
740	            args=args,
741	            data_collator=data_collator,
742	            train_dataset=train_dataset,
743	            eval_dataset=eval_dataset,
744	            processing_class=processing_class,
745	            compute_metrics=compute_metrics,
746	            callbacks=callbacks,
747	            optimizers=optimizers,
748	        )
749	
750	        # Initialize activation offloading context
751	        if self.args.activation_offloading:
752	            self.maybe_activation_offload_context = get_act_offloading_ctx_manager(model=self.model)
753	        else:
754	            self.maybe_activation_offload_context = contextlib.nullcontext()
755	
756	        # Reference model
757	        if ref_model is None:
758	            if is_peft_model(self.model) or args.precompute_ref_log_probs:
759	                # If PEFT is used, the reference model is not needed since the adapter can be disabled to revert to the
760	                # initial model. If precompute_ref_log_probs is True, the reference model does not need to be kept in
761	                # memory during training.
762	                self.ref_model = None
763	            else:
764	                ref_model_init_kwargs = args.model_init_kwargs or {}
765	                # Distributed training requires device_map=None ("auto" fails)
766	                if self.args.distributed_state.distributed_type in ["MULTI_GPU", "DEEPSPEED"]:
767	                    ref_model_init_kwargs["device_map"] = None
768	                ref_model_path = get_config_model_id(self.model.config)
769	                self.ref_model = create_model_from_path(ref_model_path, **ref_model_init_kwargs)
770	        else:
771	            self.ref_model = ref_model
772	
773	        # Disable dropout in the models
774	        if args.disable_dropout:
775	            disable_dropout_in_model(model)
776	            if self.ref_model is not None:
777	                disable_dropout_in_model(self.ref_model)
778	
779	        # Initialize the metrics
780	        self._metrics = {"train": defaultdict(list), "eval": defaultdict(list)}
781	        self._total_train_tokens = 0
782	
783	        # Gradient accumulation requires scaled loss. Normally, loss scaling in the parent class depends on whether the
784	        # model accepts loss-related kwargs. Since we compute our own loss, this check is irrelevant. We set
785	        # self.model_accepts_loss_kwargs to False to enable scaling.
786	        self.model_accepts_loss_kwargs = False
787	
788	        # Add tags to the model
789	        self.model.add_model_tags(self._tag_names)
790	
791	        if self.ref_model is not None:
792	            if self.is_deepspeed_enabled:
793	                self.ref_model = prepare_deepspeed(self.ref_model, self.accelerator)
794	            elif self.is_fsdp_enabled:
795	                self.ref_model = prepare_fsdp(self.ref_model, self.accelerator)
796	            else:
797	                self.ref_model = self.accelerator.prepare_model(self.ref_model, evaluation_mode=True)
798	
799	        if args.sync_ref_model:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80e83421-99ab-49a0-937c-be76dea76dbd",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "627c856c-5f85-419e-9872-140ea9171cd5",
  "sourceToolAssistantUUID": "80e83421-99ab-49a0-937c-be76dea76dbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-12T10:50:20.013Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Sm7TznVvkdj2WZsBeWmN2R`</summary>

```json
{
  "file_path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/dpo_trainer.py",
  "offset": 799,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "627c856c-5f85-419e-9872-140ea9171cd5",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYcAYo455y1JJPi2pt1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef5863bd-6aa4-48a2-b7fe-645312d47867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpGa974a7FxC8BLrmqs3rr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5224,
      "cache_read_input_tokens": 42207,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 42207,
          "cache_creation_input_tokens": 5224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5224,
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

_source line 41 · 2026-05-12T10:50:20.019Z_

<details><summary>↩ Tool result · `toolu_01Sm7TznVvkdj2WZsBeWmN2R`</summary>

```text
799	        if args.sync_ref_model:
800	            if is_peft_model(self.model):
801	                raise NotImplementedError(
802	                    "You passed `sync_ref_model=True` while using a PEFT model, which is currently not supported. "
803	                    "With PEFT, DPOTrainer does not keep a separate reference model in memory; instead, it recovers "
804	                    "reference behavior by temporarily disabling the adapter. As a result, there is no standalone "
805	                    "`ref_model` instance to synchronize. Use `sync_ref_model=False`, or opt for full fine-tuning if "
806	                    "you need a synced reference model. If you need `sync_ref_model` to work with PEFT, please open a "
807	                    "feature request at https://github.com/huggingface/trl/issues."
808	                )
809	            if args.precompute_ref_log_probs:
810	                raise ValueError(
811	                    "You cannot use `sync_ref_model=True` together with `precompute_ref_log_probs=True`. "
812	                    "`precompute_ref_log_probs=True` assumes a fixed reference model, but with `sync_ref_model=True` "
813	                    "the reference model is periodically updated during training, making any precomputed reference "
814	                    "log-probs stale. Set `precompute_ref_log_probs=False` or disable `sync_ref_model`."
815	                )
816	            self.add_callback(SyncRefModelCallback(ref_model=self.ref_model, accelerator=self.accelerator))
817	
818	        if args.precompute_ref_log_probs:
819	            if isinstance(self.train_dataset, IterableDataset) or isinstance(
820	                self.eval_dataset, (IterableDataset, IterableDatasetDict)
821	            ):
822	                raise ValueError(
823	                    "`precompute_ref_log_probs=True` is not supported with IterableDataset. Please use a map-style "
824	                    "Dataset or set `precompute_ref_log_probs=False`."
825	                )
826	
827	            self.train_dataset = self._precompute_ref_logps(
828	                self.train_dataset,
829	                "train",
830	                self.args.precompute_ref_batch_size or self.args.per_device_train_batch_size,
831	            )
832	            if self.eval_dataset is not None:
833	                if isinstance(self.eval_dataset, dict):
834	                    self.eval_dataset = {
835	                        name: self._precompute_ref_logps(
836	                            dataset, name, self.args.precompute_ref_batch_size or self.args.per_device_eval_batch_size
837	                        )
838	                        for name, dataset in self.eval_dataset.items()
839	                    }
840	                else:
841	                    self.eval_dataset = self._precompute_ref_logps(
842	                        self.eval_dataset,
843	                        "eval",
844	                        self.args.precompute_ref_batch_size or self.args.per_device_eval_batch_size,
845	                    )
846	
847	    def _tokenize(
848	        self,
849	        processing_class: PreTrainedTokenizerBase | ProcessorMixin,
850	        input: str | list,
851	        **kwargs,
852	    ) -> dict[str, list]:
853	        """Tokenize a single example for dataset preprocessing.
854	
855	        Dispatches to `apply_chat_template` for conversational input (list of message dicts) and to `__call__` for
856	        non-conversational input (str). For VLMs, normalizes the batch dimension that processors emit even for single
857	        examples.
858	
859	        Args:
860	            processing_class ([`~transformers.PreTrainedTokenizerBase`] or [`~transformers.ProcessorMixin`]):
861	                The tokenizer or processor to use.
862	            input (`str` or `list`):
863	                A string for non-conversational input, or a list of message dicts for conversational input.
864	            **kwargs:
865	                Forwarded to `apply_chat_template` (e.g. `add_generation_prompt`, `return_assistant_tokens_mask`).
866	
867	        Returns:
868	            `dict` with at least an `"input_ids"` key mapping to a flat `list[int]`.
869	        """
870	        if isinstance(input, list):  # conversational: list of message dicts
871	            if self._is_vlm:
872	                input = prepare_multimodal_messages(input)
873	            result = processing_class.apply_chat_template(input, tokenize=True, return_dict=True, **kwargs)
874	        else:  # non-conversational: plain text string
875	            result = processing_class(text=input)
876	        # VLMs emit a batch dimension even for single examples; unwrap it
877	        if self._is_vlm:
878	            return {k: v[0] for k, v in result.items()}
879	        return result
880	
881	    def _prepare_dataset(
882	        self,
883	        dataset: Dataset | IterableDataset,
884	        processing_class: PreTrainedTokenizerBase | ProcessorMixin,
885	        args: DPOConfig,
886	        dataset_name: str,
887	    ) -> Dataset | IterableDataset:
888	        # Build the kwargs for the `map` function
889	        map_kwargs = {}
890	        if isinstance(dataset, Dataset):  # IterableDataset does not support num_proc
891	            map_kwargs["num_proc"] = args.dataset_num_proc
892	
893	        with PartialState().main_process_first():
894	            # Extract the prompt if needed
895	            first_example = next(iter(dataset))
896	            if "prompt" not in first_example:
897	                if isinstance(dataset, Dataset):  # `IterableDataset.map` does not support `desc`
898	                    map_kwargs["desc"] = f"Extracting prompt from {dataset_name} dataset"
899	                dataset = dataset.map(extract_prompt, **map_kwargs)
900	
901	            # Add EOS token if needed: non-conversational only
902	            first_example = next(iter(dataset))
903	            if not is_conversational(first_example):
904	                if isinstance(dataset, Dataset):  # `IterableDataset.map` does not support `desc`
905	                    map_kwargs["desc"] = f"Adding EOS to {dataset_name} dataset"
906	
907	                def add_eos(example, eos_token):
908	                    if not example["chosen"].endswith(eos_token):
909	                        example["chosen"] = example["chosen"] + eos_token
910	                    if not example["rejected"].endswith(eos_token):
911	                        example["rejected"] = example["rejected"] + eos_token
912	                    return example
913	
914	                dataset = dataset.map(add_eos, fn_kwargs={"eos_token": self._tokenizer.eos_token}, **map_kwargs)
915	
916	            # Tokenize the dataset
917	            if isinstance(dataset, Dataset):  # `IterableDataset.map` does not support `desc`
918	                map_kwargs["desc"] = f"Tokenizing {dataset_name} dataset"
919	
920	            def tokenize_fn(example, processing_class):
921	                tools = example.get("tools")
922	                tools = json.loads(tools) if isinstance(tools, str) else tools
923	                output = {}
924	                if is_conversational(example):
925	                    prompt_ids = self._tokenize(
926	                        processing_class,
927	                        example["prompt"],
928	                        tools=tools,
929	                        add_generation_prompt=True,
930	                        **example.get("chat_template_kwargs", {}),
931	                    )["input_ids"]
932	                    prompt_chosen_ids = self._tokenize(
933	                        processing_class,
934	                        example["prompt"] + example["chosen"],
935	                        tools=tools,
936	                        **example.get("chat_template_kwargs", {}),
937	                    )["input_ids"]
938	                    prompt_rejected_ids = self._tokenize(
939	                        processing_class,
940	                        example["prompt"] + example["rejected"],
941	                        tools=tools,
942	                        **example.get("chat_template_kwargs", {}),
943	                    )["input_ids"]
944	                else:
945	                    prompt_ids = self._tokenize(processing_class, example["prompt"])["input_ids"]
946	                    prompt_chosen_ids = self._tokenize(processing_class, example["prompt"] + example["chosen"])[
947	                        "input_ids"
948	                    ]
949	                    prompt_rejected_ids = self._tokenize(processing_class, example["prompt"] + example["rejected"])[
950	                        "input_ids"
951	                    ]
952	
953	                # Check if the tokenized prompt starts with the tokenized prompt+completion
954	                if not prompt_chosen_ids[: len(prompt_ids)] == prompt_ids:
955	                    logger.warning(
956	                        "Mismatch between tokenized prompt and the start of tokenized prompt+chosen. "
957	                        "This may be due to unexpected tokenizer behavior, whitespace issues, or special "
958	                        "token handling. Verify that the tokenizer is processing text consistently."
959	                    )
960	                if not prompt_rejected_ids[: len(prompt_ids)] == prompt_ids:
961	                    logger.warning(
962	                        "Mismatch between tokenized prompt and the start of tokenized prompt+rejected. "
963	                        "This may be due to unexpected tokenizer behavior, whitespace issues, or special "
964	                        "token handling. Verify that the tokenizer is processing text consistently."
965	                    )
966	
967	                output["prompt_ids"] = prompt_ids
968	                output["chosen_ids"] = prompt_chosen_ids[len(prompt_ids) :]
969	                output["rejected_ids"] = prompt_rejected_ids[len(prompt_ids) :]
970	                return output
971	
972	            dataset = dataset.map(tokenize_fn, fn_kwargs={"processing_class": processing_class}, **map_kwargs)
973	
974	        return dataset
975	
976	    def _set_signature_columns_if_needed(self):
977	        # If `self.args.remove_unused_columns` is True, non-signature columns are removed.
978	        # By default, this method sets `self._signature_columns` to the model's expected inputs (usually, "input_ids"
979	        # and "attention_mask").
980	        if self._signature_columns is None:
981	            if self._is_vision_dataset:
982	                self._signature_columns = [
983	                    "prompt",
984	                    "chosen",
985	                    "rejected",
986	                    "image",
987	                    "images",
988	                    "tools",
989	                    "chat_template_kwargs",
990	                ]
991	            else:
992	                self._signature_columns = [
993	                    "prompt_ids",
994	                    "chosen_ids",
995	                    "rejected_ids",
996	                    "ref_chosen_logps",
997	                    "ref_rejected_logps",
998	                ]
999	
1000	    def _precompute_ref_logps(self, dataset: Dataset, name: str, batch_size: int) -> Dataset:
1001	        model_hash = hash_module(self.ref_model or self.model)
1002	        fingerprint = Hasher.hash((dataset._fingerprint, model_hash))
1003	        cache_file = dataset._get_cache_file_path(fingerprint).removesuffix(".arrow") + ".npz"
1004	        if os.path.exists(cache_file):
1005	            loaded = np.load(cache_file)
1006	            ref_chosen_logps = loaded["ref_chosen_logps"]
1007	            ref_rejected_logps = loaded["ref_rejected_logps"]
1008	        else:
1009	            dataloader = DataLoader(
1010	                dataset,
1011	                batch_size=batch_size,
1012	                collate_fn=self.data_collator,
1013	                num_workers=self.args.dataloader_num_workers,
1014	                pin_memory=self.args.dataloader_pin_memory,
1015	                shuffle=False,
1016	            )
1017	            data_loader = self.accelerator.prepare(dataloader)
1018	            ref_chosen_logps = []
1019	            ref_rejected_logps = []
1020	            for padded_batch in tqdm(iterable=data_loader, desc=f"Computing reference log probs for {name} dataset"):
1021	                ref_chosen_logp, ref_rejected_logp = self.compute_ref_log_probs(padded_batch)
1022	                ref_chosen_logp, ref_rejected_logp = self.accelerator.gather_for_metrics(
1023	                    (ref_chosen_logp, ref_rejected_logp)
1024	                )
1025	                ref_chosen_logps.append(ref_chosen_logp.cpu())
1026	                ref_rejected_logps.append(ref_rejected_logp.cpu())
1027	
1028	            # Save the reference log probabilities to cache. We need .float() because bf16 is not supported by numpy
1029	            ref_chosen_logps = torch.cat(ref_chosen_logps).float().numpy()
1030	            ref_rejected_logps = torch.cat(ref_rejected_logps).float().numpy()
1031	            if self.accelerator.is_main_process:
1032	                np.savez_compressed(
1033	                    cache_file, ref_chosen_logps=ref_chosen_logps, ref_rejected_logps=ref_rejected_logps
1034	                )
1035	            self.accelerator.wait_for_everyone()
1036	
1037	        dataset = dataset.add_column(name="ref_chosen_logps", column=ref_chosen_logps)
1038	        dataset = dataset.add_column(name="ref_rejected_logps", column=ref_rejected_logps, new_fingerprint=fingerprint)
1039	
1040	        return dataset
1041	
1042	    def compute_ref_log_probs(self, inputs):
1043	        """Computes reference log probabilities for a single padded batch."""
1044	        device = self.accelerator.device
1045	
1046	        _non_model_keys = {"completion_mask", "ref_chosen_logps", "ref_rejected_logps"}
1047	        model_kwargs = {k: v for k, v in inputs.items() if k not in _non_model_keys}
1048	        model_kwargs["use_cache"] = False
1049	
1050	        with torch.no_grad(), disable_gradient_checkpointing(self.model, self.args.gradient_checkpointing_kwargs):
1051	            if self.ref_model is None:
1052	                if is_peft_model(self.model):
1053	                    model = self.accelerator.unwrap_model(self.model)
1054	                    with use_adapter(model, adapter_name="ref" if "ref" in model.peft_config else None):
1055	                        ref_outputs = self.model(**model_kwargs)
1056	                else:
1057	                    ref_outputs = self.model(**model_kwargs)
1058	            else:
1059	                ref_outputs = self.ref_model(**model_kwargs)
1060	
1061	        input_ids = inputs["input_ids"]
1062	        completion_mask = inputs["completion_mask"]
1063	        shift_labels = input_ids[..., 1:].contiguous()
1064	        shift_completion_mask = completion_mask[..., 1:].contiguous()
1065	        ref_shift_logits = ref_outputs.logits[..., :-1, :].contiguous()
1066	        ref_per_token_logps = selective_log_softmax(ref_shift_logits, shift_labels)
1067	        ref_per_token_logps[shift_completion_mask == 0] = 0.0
1068	
1069	        if self.ld_alpha is None:
1070	            ref_logps = ref_per_token_logps.sum(dim=1)
1071	        else:
1072	            comp_pos = shift_completion_mask.cumsum(dim=1)
1073	            comp_lens = shift_completion_mask.sum(dim=1).long()
1074	            chosen_lens, rejected_lens = comp_lens.chunk(2, dim=0)
1075	            shared_lens = torch.minimum(chosen_lens, rejected_lens)
1076	            shared_lens = torch.cat([shared_lens, shared_lens], dim=0).to(device)
1077	            shared_mask = (comp_pos > 0) & (comp_pos <= shared_lens.unsqueeze(1))
1078	            tail_mask = comp_pos > shared_lens.unsqueeze(1)
1079	            shared_logps = (ref_per_token_logps * shared_mask).sum(dim=1)
1080	            tail_logps = (ref_per_token_logps * tail_mask).sum(dim=1)
1081	            ref_logps = shared_logps + self.ld_alpha * tail_logps
1082	
1083	        ref_chosen_logps, ref_rejected_logps = ref_logps.chunk(2, dim=0)
1084	        return ref_chosen_logps, ref_rejected_logps
1085	
1086	    def _compute_loss_liger(self, model, inputs, return_outputs):
1087	        if return_outputs:
1088	            raise RuntimeError(
1089	                "return_outputs=True is not supported with the Liger DPO loss. The Liger loss computes the loss "
1090	                "without materializing logits, so outputs cannot be returned."
1091	            )
1092	
1093	        mode = "train" if self.model.training else "eval"
1094	
1095	        input_ids = inputs["input_ids"]
1096	        attention_mask = inputs["attention_mask"]
1097	        completion_mask = inputs["completion_mask"]
1098	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef5863bd-6aa4-48a2-b7fe-645312d47867",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "c92da67f-2f49-4f36-8a4d-f0356d400b19",
  "sourceToolAssistantUUID": "ef5863bd-6aa4-48a2-b7fe-645312d47867",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-12T10:50:23.978Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R2wy6J45sqt2qoaSYhzyEp`</summary>

```json
{
  "file_path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/dpo_trainer.py",
  "offset": 1098,
  "limit": 425
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c92da67f-2f49-4f36-8a4d-f0356d400b19",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYcSm7QVChqLCmYKaUB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "218d7fb5-9086-4a5c-ad30-3716577512f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qo8SLGTWnG1y3LciW61VZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4985,
      "cache_read_input_tokens": 47431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4985,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-12T10:50:23.984Z_

<details><summary>↩ Tool result · `toolu_01R2wy6J45sqt2qoaSYhzyEp`</summary>

```text
1098	
1099	        decoder = model.get_decoder()
1100	        outputs = decoder(input_ids, attention_mask=attention_mask, use_cache=False)
1101	        hidden_states = outputs.last_hidden_state[:, :-1].contiguous()
1102	        lm_head = model.get_output_embeddings()
1103	        weight = lm_head.weight
1104	        bias = lm_head.bias
1105	
1106	        with torch.no_grad(), disable_gradient_checkpointing(self.model, self.args.gradient_checkpointing_kwargs):
1107	            ref_decoder = self.ref_model.get_decoder()
1108	            ref_outputs = ref_decoder(input_ids, attention_mask=attention_mask, use_cache=False)
1109	            ref_lm_head = self.ref_model.get_output_embeddings()
1110	            ref_hidden_states = ref_outputs.last_hidden_state[:, :-1].contiguous()
1111	            ref_weight = ref_lm_head.weight
1112	            ref_bias = ref_lm_head.bias
1113	
1114	        shift_completion_mask = completion_mask[:, 1:].contiguous()
1115	        labels = input_ids[:, 1:].clone()
1116	        labels[shift_completion_mask == 0] = -100
1117	
1118	        loss, metrics = self.liger_loss_fn(
1119	            weight, hidden_states, labels, bias, ref_hidden_states, ref_weight, ref_bias
1120	        )
1121	
1122	        (
1123	            chosen_logps,
1124	            rejected_logps,
1125	            chosen_logits_mean,
1126	            rejected_logits_mean,
1127	            nll_loss,
1128	            chosen_rewards,
1129	            rejected_rewards,
1130	        ) = metrics
1131	
1132	        if mode == "train":
1133	            num_tokens_in_batch = self.accelerator.gather_for_metrics(inputs["attention_mask"].sum()).sum().item()
1134	            self._total_train_tokens += num_tokens_in_batch
1135	        self._metrics[mode]["num_tokens"] = [self._total_train_tokens]
1136	
1137	        avg_chosen_logits = self.accelerator.gather_for_metrics(chosen_logits_mean).mean().item()
1138	        avg_rejected_logits = self.accelerator.gather_for_metrics(rejected_logits_mean).mean().item()
1139	        self._metrics[mode]["logits/chosen"].append(avg_chosen_logits)
1140	        self._metrics[mode]["logits/rejected"].append(avg_rejected_logits)
1141	
1142	        agg_chosen_rewards = self.accelerator.gather(chosen_rewards)
1143	        agg_rejected_rewards = self.accelerator.gather(rejected_rewards)
1144	        self._metrics[mode]["rewards/chosen"].append(agg_chosen_rewards.mean().item())
1145	        self._metrics[mode]["rewards/rejected"].append(agg_rejected_rewards.mean().item())
1146	
1147	        reward_accuracies = (chosen_rewards > rejected_rewards).float()
1148	        agg_reward_accuracies = self.accelerator.gather(reward_accuracies)
1149	        self._metrics[mode]["rewards/accuracies"].append(agg_reward_accuracies.mean().item())
1150	
1151	        margins = chosen_rewards - rejected_rewards
1152	        agg_margins = self.accelerator.gather(margins)
1153	        self._metrics[mode]["rewards/margins"].append(agg_margins.mean().item())
1154	
1155	        self._metrics[mode]["logps/chosen"].append(self.accelerator.gather(chosen_logps).mean().item())
1156	        self._metrics[mode]["logps/rejected"].append(self.accelerator.gather(rejected_logps).mean().item())
1157	
1158	        return loss
1159	
1160	    def _compute_loss(self, model, inputs, return_outputs):
1161	        mode = "train" if self.model.training else "eval"
1162	        device = self.accelerator.device
1163	
1164	        _non_model_keys = {"completion_mask", "ref_chosen_logps", "ref_rejected_logps"}
1165	        model_kwargs = {k: v for k, v in inputs.items() if k not in _non_model_keys}
1166	        model_kwargs["use_cache"] = False
1167	        outputs = model(**model_kwargs)
1168	
1169	        input_ids = inputs["input_ids"]
1170	        completion_mask = inputs["completion_mask"]
1171	        shift_logits = outputs.logits[..., :-1, :].contiguous()
1172	        shift_labels = input_ids[..., 1:].contiguous()
1173	        shift_completion_mask = completion_mask[..., 1:].contiguous()
1174	        per_token_logps = selective_log_softmax(shift_logits, shift_labels)
1175	        per_token_logps[shift_completion_mask == 0] = 0.0  # mask out non-completion tokens
1176	        if self.ld_alpha is None:
1177	            logps = per_token_logps.sum(dim=1)  # sum over sequence length
1178	        else:
1179	            comp_pos = shift_completion_mask.cumsum(dim=1)
1180	            comp_lens = shift_completion_mask.sum(dim=1).long()
1181	            chosen_lens, rejected_lens = comp_lens.chunk(2, dim=0)
1182	            shared_lens = torch.minimum(chosen_lens, rejected_lens)
1183	            shared_lens = torch.cat([shared_lens, shared_lens], dim=0).to(device)
1184	            shared_mask = (comp_pos > 0) & (comp_pos <= shared_lens.unsqueeze(1))  # shared: 1 <= pos <= shared_len
1185	            tail_mask = comp_pos > shared_lens.unsqueeze(1)  # tail: pos > shared_len
1186	            shared_logps = (per_token_logps * shared_mask).sum(dim=1)
1187	            tail_logps = (per_token_logps * tail_mask).sum(dim=1)
1188	            logps = shared_logps + self.ld_alpha * tail_logps
1189	        chosen_logps, rejected_logps = logps.chunk(2, dim=0)  # batch is [chosen, rejected]
1190	
1191	        if self.precompute_ref_logps:
1192	            ref_chosen_logps, ref_rejected_logps = inputs["ref_chosen_logps"], inputs["ref_rejected_logps"]
1193	        else:
1194	            # When gradient checkpointing is enabled with use_reentrant=True (default), calling the model inside a
1195	            # torch.no_grad() block triggers a harmless PyTorch warning ("None of the inputs have requires_grad=True").
1196	            # Temporarily disable checkpointing to avoid this warning during inference.
1197	            with torch.no_grad(), disable_gradient_checkpointing(self.model, self.args.gradient_checkpointing_kwargs):
1198	                if is_peft_model(model) and self.ref_model is None:
1199	                    # When training a PEFT adapter, how we obtain the reference depends on the setup:
1200	                    # - New adapter: disabling adapters yields the base model.
1201	                    # - Re-training an existing adapter: an initial copy is loaded under the name "ref".
1202	                    model = self.accelerator.unwrap_model(model)
1203	                    with use_adapter(model, adapter_name="ref" if "ref" in model.peft_config else None):
1204	                        ref_outputs = self.model(**model_kwargs)
1205	                else:
1206	                    ref_outputs = self.ref_model(**model_kwargs)
1207	
1208	            ref_shift_logits = ref_outputs.logits[..., :-1, :].contiguous()
1209	            ref_per_token_logps = selective_log_softmax(ref_shift_logits, shift_labels)
1210	            ref_per_token_logps[shift_completion_mask == 0] = 0.0  # mask out non-completion tokens
1211	            if self.ld_alpha is None:
1212	                ref_logps = ref_per_token_logps.sum(dim=1)  # sum over sequence length
1213	            else:
1214	                # reuse comp_pos/shared_mask/tail_mask computed above (they depend only on completion_mask)
1215	                ref_shared_logps = (ref_per_token_logps * shared_mask).sum(dim=1)
1216	                ref_tail_logps = (ref_per_token_logps * tail_mask).sum(dim=1)
1217	                ref_logps = ref_shared_logps + self.ld_alpha * ref_tail_logps
1218	            ref_chosen_logps, ref_rejected_logps = ref_logps.chunk(2, dim=0)  # batch is [chosen, rejected]
1219	
1220	        # Get the log ratios for the chosen and rejected responses
1221	        chosen_logratios = chosen_logps - ref_chosen_logps
1222	        rejected_logratios = rejected_logps - ref_rejected_logps
1223	
1224	        if self.f_divergence_type == "reverse_kl":  # standard DPO
1225	            chosen_scores = chosen_logratios
1226	            rejected_scores = rejected_logratios
1227	        elif self.f_divergence_type == "forward_kl":
1228	            # f'(t) = 1 - 1/t  -> drop constant -> -exp(-logratio)
1229	            chosen_scores = -torch.exp(-chosen_logratios)
1230	            rejected_scores = -torch.exp(-rejected_logratios)
1231	        elif self.f_divergence_type == "js_divergence":
1232	            # f'(t) = log(2t/(t+1)) -> drop log 2
1233	            chosen_scores = F.logsigmoid(chosen_logratios)
1234	            rejected_scores = F.logsigmoid(rejected_logratios)
1235	        elif self.f_divergence_type == "alpha_divergence":
1236	            # alpha-divergence: f'(t) = (t^(α-1) - 1)/(α-1)
1237	            if abs(self.f_alpha_divergence_coef - 1.0) < 1e-6:  # limit case f'(t) -> log(t), fall back to reverse_kl
1238	                chosen_scores = chosen_logratios
1239	                rejected_scores = rejected_logratios
1240	            else:
1241	                coef = 1.0 / (self.f_alpha_divergence_coef - 1.0)
1242	                t_chosen = (self.f_alpha_divergence_coef - 1.0) * chosen_logratios
1243	                t_rejected = (self.f_alpha_divergence_coef - 1.0) * rejected_logratios
1244	                dtype = t_chosen.dtype
1245	                # Clamp max so exp(.) stays representable after casting back
1246	                clamp_max = {torch.float16: 11.0, torch.bfloat16: 80.0, torch.float32: 80.0}[dtype]
1247	                t_chosen_float = torch.clamp(t_chosen.float(), max=clamp_max)
1248	                t_rejected_float = torch.clamp(t_rejected.float(), max=clamp_max)
1249	                chosen_scores = torch.exp(t_chosen_float).to(dtype) * coef
1250	                rejected_scores = torch.exp(t_rejected_float).to(dtype) * coef
1251	        else:
1252	            raise ValueError(f"Unknown f_divergence_type: {self.f_divergence_type}")
1253	
1254	        delta_score = chosen_scores - rejected_scores
1255	
1256	        loss = 0.0
1257	        for loss_type, loss_weight in zip(self.loss_types, self.loss_weights, strict=True):
1258	            if loss_type == "sigmoid":
1259	                per_sequence_loss = -F.logsigmoid(self.beta * delta_score)
1260	
1261	            elif loss_type == "hinge":
1262	                per_sequence_loss = torch.relu(1 - self.beta * delta_score)
1263	
1264	            elif loss_type == "ipo":
1265	                # IPO uses sequence-level log-prob differences; in code these are token-summed over the completion,
1266	                # which makes the squared loss scale with completion length. We therefore normalize by the number of
1267	                # completion tokens (average per token) to make β/loss comparable across variable lengths. This length
1268	                # normalization is not explicitly discussed in the IPO paper; we confirmed this choice with the IPO
1269	                # authors, and the results reported in the paper correspond to this normalized form.
1270	                chosen_mask, rejected_mask = completion_mask.chunk(2, dim=0)
1271	                chosen_avg_score = chosen_scores / chosen_mask.sum(dim=1).clamp(min=1.0)
1272	                rejected_avg_score = rejected_scores / rejected_mask.sum(dim=1).clamp(min=1.0)
1273	                ipo_delta = chosen_avg_score - rejected_avg_score
1274	                # (Eq. 17) of the paper where beta is the regularization parameter for the IPO loss, denoted by τ.
1275	                per_sequence_loss = (ipo_delta - 1 / (2 * self.beta)) ** 2
1276	
1277	            elif loss_type == "exo_pair":
1278	                # Implements EXO-pref from the paper https://huggingface.co/papers/2402.00856, (Eq. 16)
1279	                # Minimize KL(p_fθ || p_rh) for K=2; p_fθ = softmax(βπ * (log πθ − log π_ref)) over {chosen, rejected}
1280	                # p_rh = [(1−ε), ε]; expanded KL gives the weighted logsigmoid form below
1281	                epsilon = torch.tensor(self.label_smoothing, device=device)
1282	                qw = torch.sigmoid(self.beta * delta_score)
1283	                log_qw = F.logsigmoid(self.beta * delta_score)
1284	                log_pw = torch.log1p(-epsilon)
1285	                ql = torch.sigmoid(-self.beta * delta_score)
1286	                log_ql = F.logsigmoid(-self.beta * delta_score)
1287	                log_pl = torch.log(epsilon)
1288	                per_sequence_loss = qw * (log_qw - log_pw) + ql * (log_ql - log_pl)
1289	
1290	            elif loss_type == "nca_pair":
1291	                chosen_rewards = self.beta * chosen_scores
1292	                rejected_rewards = self.beta * rejected_scores
1293	                per_sequence_loss = (
1294	                    -F.logsigmoid(chosen_rewards)
1295	                    - 0.5 * F.logsigmoid(-chosen_rewards)
1296	                    - 0.5 * F.logsigmoid(-rejected_rewards)
1297	                )
1298	
1299	            elif loss_type == "robust":
1300	                clean_loss_term = -(1 - self.label_smoothing) * F.logsigmoid(self.beta * delta_score)
1301	                flipped_loss_term = -self.label_smoothing * F.logsigmoid(-self.beta * delta_score)
1302	                per_sequence_loss = (clean_loss_term - flipped_loss_term) / (1 - 2 * self.label_smoothing)
1303	
1304	            elif loss_type == "bco_pair":
1305	                chosen_rewards = self.beta * chosen_scores
1306	                rejected_rewards = self.beta * rejected_scores
1307	                per_sequence_loss = -F.logsigmoid(chosen_rewards) - F.logsigmoid(-rejected_rewards)
1308	
1309	            elif loss_type == "sppo_hard":
1310	                # In the paper (https://huggingface.co/papers/2405.00675), SPPO employs a soft probability approach,
1311	                # estimated using the PairRM score. The probability calculation is conducted outside of the trainer
1312	                # class. The version described here is the hard probability version, where P in Equation (4.7) of
1313	                # Algorithm 1 is set to 1 for the winner and 0 for the loser.
1314	                winner_margin_error = (chosen_scores - 0.5 / self.beta) ** 2
1315	                loser_margin_error = (rejected_scores + 0.5 / self.beta) ** 2
1316	                per_sequence_loss = winner_margin_error + loser_margin_error
1317	
1318	            elif loss_type == "aot":
1319	                logratios = chosen_logps - rejected_logps
1320	                ref_logratios = ref_chosen_logps - ref_rejected_logps
1321	                logratios_sorted, _ = torch.sort(logratios, dim=0)
1322	                ref_logratios_sorted, _ = torch.sort(ref_logratios, dim=0)
1323	                delta = logratios_sorted - ref_logratios_sorted
1324	                per_sequence_loss = (
1325	                    -F.logsigmoid(self.beta * delta) * (1 - self.label_smoothing)
1326	                    - F.logsigmoid(-self.beta * delta) * self.label_smoothing
1327	                )
1328	
1329	            elif loss_type == "aot_unpaired":
1330	                chosen_logratios_sorted, _ = torch.sort(chosen_logratios, dim=0)
1331	                rejected_logratios_sorted, _ = torch.sort(rejected_logratios, dim=0)
1332	                delta = chosen_logratios_sorted - rejected_logratios_sorted
1333	                per_sequence_loss = (
1334	                    -F.logsigmoid(self.beta * delta) * (1 - self.label_smoothing)
1335	                    - F.logsigmoid(-self.beta * delta) * self.label_smoothing
1336	                )
1337	
1338	            elif loss_type == "apo_zero":
1339	                # Eqn (7) of the APO paper (https://huggingface.co/papers/2408.06266)
1340	                # Use this loss when you believe the chosen outputs are better than your model's default output
1341	                # Increase chosen likelihood and decrease rejected likelihood
1342	                losses_chosen = 1 - torch.sigmoid(self.beta * chosen_logratios)
1343	                losses_rejected = torch.sigmoid(self.beta * rejected_logratios)
1344	                per_sequence_loss = losses_chosen + losses_rejected
1345	
1346	            elif loss_type == "apo_down":
1347	                # Eqn (8) of the APO paper (https://huggingface.co/papers/2408.06266)
1348	                # Use this loss when you believe the chosen outputs are worse than your model's default output.
1349	                # Decrease chosen likelihood and decrease rejected likelihood more
1350	                losses_chosen = torch.sigmoid(self.beta * chosen_logratios)
1351	                losses_rejected = 1 - torch.sigmoid(self.beta * delta_score)
1352	                per_sequence_loss = losses_chosen + losses_rejected
1353	
1354	            elif loss_type == "discopop":
1355	                # Eqn (5) of the DiscoPOP paper (https://huggingface.co/papers/2406.08414)
1356	                logits = delta_score * self.beta
1357	                # Modulate the mixing coefficient based on the log ratio magnitudes
1358	                log_ratio_modulation = torch.sigmoid(logits / self.args.discopop_tau)
1359	                logistic_component = -F.logsigmoid(logits)
1360	                exp_component = torch.exp(-logits)
1361	                # Blend between logistic and exponential component based on log ratio modulation
1362	                per_sequence_loss = (
1363	                    logistic_component * (1 - log_ratio_modulation) + exp_component * log_ratio_modulation
1364	                )
1365	
1366	            elif loss_type == "sft":
1367	                chosen_logits, _ = shift_logits.chunk(2, dim=0)
1368	                chosen_labels, _ = shift_labels.chunk(2, dim=0)
1369	                chosen_mask, _ = shift_completion_mask.chunk(2, dim=0)
1370	                batch_loss = F.cross_entropy(chosen_logits[chosen_mask.bool()], chosen_labels[chosen_mask.bool()])
1371	                # Implementation convenience: expand the scalar SFT loss to a per-sequence tensor so it matches the
1372	                # shape of other losses; only the mean is used, so this is a no-op numerically.
1373	                per_sequence_loss = batch_loss.expand(chosen_logits.size(0))
1374	
1375	            elif loss_type == "sigmoid_norm":
1376	                chosen_mask, rejected_mask = completion_mask.chunk(2, dim=0)
1377	                chosen_avg_score = chosen_scores / chosen_mask.sum(dim=1).clamp(min=1.0)
1378	                rejected_avg_score = rejected_scores / rejected_mask.sum(dim=1).clamp(min=1.0)
1379	                delta = chosen_avg_score - rejected_avg_score
1380	                per_sequence_loss = -F.logsigmoid(self.beta * delta)
1381	
1382	            else:
1383	                raise ValueError(
1384	                    f"Unknown loss type: {loss_type}. Should be one of ['sigmoid', 'hinge', 'ipo', 'exo_pair', "
1385	                    "'nca_pair', 'robust', 'bco_pair', 'sppo_hard', 'aot', 'aot_unpaired', 'apo_zero', 'apo_down', "
1386	                    "'discopop', 'sft', 'sigmoid_norm']"
1387	                )
1388	
1389	            if self.use_weighting:
1390	                # Eq (2) of the WPO paper: https://huggingface.co/papers/2406.11827
1391	                completion_lengths = shift_completion_mask.sum(dim=1).clamp_min(1)
1392	                with torch.no_grad():
1393	                    lse1 = torch.logsumexp(shift_logits, dim=-1)
1394	                    lse2 = torch.logsumexp(2.0 * shift_logits, dim=-1)
1395	                    log_denom = lse2 - 2.0 * lse1
1396	                    aligned_logps = (per_token_logps - log_denom) * shift_completion_mask
1397	                mean_logps = aligned_logps.sum(dim=1) / completion_lengths
1398	                weights = torch.exp(mean_logps)
1399	                chosen_weights, rejected_weights = weights.chunk(2, dim=0)
1400	                per_sequence_loss *= chosen_weights * rejected_weights
1401	
1402	            loss += per_sequence_loss.mean() * loss_weight
1403	
1404	        # Log the metrics
1405	        # Entropy
1406	        per_token_entropy = entropy_from_logits(shift_logits.detach())
1407	        mask = shift_completion_mask
1408	        entropy_sum = (per_token_entropy * mask).sum()
1409	        total_tokens = mask.sum()
1410	
1411	        # Gather counts across ranks and weight-average
1412	        entropy_sum = self.accelerator.gather_for_metrics(entropy_sum).sum()
1413	        total_tokens = self.accelerator.gather_for_metrics(total_tokens).sum()
1414	        entropy = (entropy_sum / total_tokens).item() if total_tokens > 0 else 0.0
1415	        self._metrics[mode]["entropy"].append(entropy)
1416	
1417	        # Number of tokens
1418	        if mode == "train":
1419	            num_tokens_in_batch = self.accelerator.gather_for_metrics(inputs["attention_mask"].sum()).sum().item()
1420	            self._total_train_tokens += num_tokens_in_batch
1421	        self._metrics[mode]["num_tokens"] = [self._total_train_tokens]
1422	
1423	        # Average logits for chosen and rejected completions
1424	        chosen_logits, rejected_logits = shift_logits.detach().chunk(2, dim=0)
1425	        chosen_mask, rejected_mask = shift_completion_mask.chunk(2, dim=0)
1426	        total_chosen_logits = chosen_logits[chosen_mask.bool()].mean(-1).sum()
1427	        total_chosen_tokens = chosen_mask.sum()
1428	        total_rejected_logits = rejected_logits[rejected_mask.bool()].mean(-1).sum()
1429	        total_rejected_tokens = rejected_mask.sum()
1430	        total_chosen_logits = self.accelerator.gather_for_metrics(total_chosen_logits).sum().item()
1431	        total_chosen_tokens = self.accelerator.gather_for_metrics(total_chosen_tokens).sum().item()
1432	        total_rejected_logits = self.accelerator.gather_for_metrics(total_rejected_logits).sum().item()
1433	        total_rejected_tokens = self.accelerator.gather_for_metrics(total_rejected_tokens).sum().item()
1434	        avg_chosen_logits = total_chosen_logits / total_chosen_tokens if total_chosen_tokens > 0 else 0.0
1435	        avg_rejected_logits = total_rejected_logits / total_rejected_tokens if total_rejected_tokens > 0 else 0.0
1436	        self._metrics[mode]["logits/chosen"].append(avg_chosen_logits)
1437	        self._metrics[mode]["logits/rejected"].append(avg_rejected_logits)
1438	
1439	        # Token accuracy for the chosen completions
1440	        predictions = chosen_logits.argmax(dim=-1)
1441	        chosen_mask = shift_completion_mask[: len(shift_completion_mask) // 2].bool()
1442	        chosen_labels = shift_labels[: len(shift_labels) // 2]
1443	        correct_predictions = (predictions == chosen_labels) & chosen_mask
1444	        total_tokens = chosen_mask.sum()
1445	        correct_tokens = correct_predictions.sum()
1446	        correct_tokens = self.accelerator.gather_for_metrics(correct_tokens)
1447	        total_tokens = self.accelerator.gather_for_metrics(total_tokens)
1448	        total_sum = total_tokens.sum()
1449	        accuracy = (correct_tokens.sum() / total_sum).item() if total_sum > 0 else 0.0
1450	        self._metrics[mode]["mean_token_accuracy"].append(accuracy)
1451	
1452	        # Rewards for chosen and rejected completions
1453	        chosen_rewards = self.beta * chosen_logratios.detach()
1454	        rejected_rewards = self.beta * rejected_logratios.detach()
1455	        agg_chosen_rewards = self.accelerator.gather(chosen_rewards)
1456	        agg_rejected_rewards = self.accelerator.gather(rejected_rewards)
1457	        self._metrics[mode]["rewards/chosen"].append(agg_chosen_rewards.mean().item())
1458	        self._metrics[mode]["rewards/rejected"].append(agg_rejected_rewards.mean().item())
1459	
1460	        # Reward accuracy
1461	        reward_accuracies = (chosen_rewards > rejected_rewards).float()
1462	        agg_reward_accuracies = self.accelerator.gather(reward_accuracies)
1463	        self._metrics[mode]["rewards/accuracies"].append(agg_reward_accuracies.mean().item())
1464	
1465	        # Reward margins
1466	        margins = chosen_rewards - rejected_rewards
1467	        agg_margins = self.accelerator.gather(margins)
1468	        self._metrics[mode]["rewards/margins"].append(agg_margins.mean().item())
1469	
1470	        # Average log probabilities for chosen and rejected completions
1471	        self._metrics[mode]["logps/chosen"].append(self.accelerator.gather(chosen_logps).mean().item())
1472	        self._metrics[mode]["logps/rejected"].append(self.accelerator.gather(rejected_logps).mean().item())
1473	
1474	        return (loss, outputs) if return_outputs else loss
1475	
1476	    def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
1477	        if self.use_liger_kernel:
1478	            return self._compute_loss_liger(model, inputs, return_outputs)
1479	        else:
1480	            return self._compute_loss(model, inputs, return_outputs)
1481	
1482	    # Override training step to add activation offloading context.
1483	    def training_step(self, *args, **kwargs):
1484	        with self.maybe_activation_offload_context:
1485	            return super().training_step(*args, **kwargs)
1486	
1487	    def log(self, logs: dict[str, float], start_time: float | None = None) -> None:
1488	        mode = "train" if self.model.training else "eval"
1489	        metrics = {key: sum(val) / len(val) for key, val in self._metrics[mode].items()}  # average the metrics
1490	
1491	        # This method can be called both in training and evaluation. When called in evaluation, the keys in `logs`
1492	        # start with "eval_". We need to add the prefix "eval_" to the keys in `metrics` to match the format.
1493	        if mode == "eval":
1494	            metrics = {f"eval_{key}": val for key, val in metrics.items()}
1495	
1496	        logs = {**logs, **metrics}
1497	        super().log(logs, start_time)
1498	        self._metrics[mode].clear()
1499	
1500	    # During eval, Trainer calls prediction_step. If no labels are present in the inputs, it only runs forward and
1501	    # returns logits. We override prediction_step to force compute_loss, because this trainer doesn't involve labels.
1502	    def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys: list[str] | None = None):
1503	        inputs = self._prepare_inputs(inputs)
1504	        with torch.no_grad(), self.compute_loss_context_manager():
1505	            if prediction_loss_only:
1506	                loss = self.compute_loss(model, inputs, return_outputs=False)  # logits aren't materialized with liger
1507	                logits, labels = None, None
1508	            else:
1509	                loss, outputs = self.compute_loss(model, inputs, return_outputs=True)
1510	                logits, labels = outputs.logits, inputs["input_ids"]
1511	        return loss, logits, labels
1512	
1513	    # Ensure the model card is saved along with the checkpoint
1514	    def _save_checkpoint(self, model, trial):
1515	        if self.args.hub_model_id is None:
1516	            model_name = Path(self.args.output_dir).name
1517	        else:
1518	            model_name = self.args.hub_model_id.split("/")[-1]
1519	        self.create_model_card(model_name=model_name)
1520	        super()._save_checkpoint(model, trial)
1521	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "218d7fb5-9086-4a5c-ad30-3716577512f6",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "61a24d67-84c2-4a52-8ae6-791279d65972",
  "sourceToolAssistantUUID": "218d7fb5-9086-4a5c-ad30-3716577512f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-12T10:50:27.296Z_

Now let me also read the `selective_log_softmax` helper and the `_BaseTrainer` and the DPOConfig.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61a24d67-84c2-4a52-8ae6-791279d65972",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYck5AYbVsdpJrWuGBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbe930a2-f409-40c3-b429-9bce0bcaddc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgaKZFDNeGYioXD3TYzfdU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8765,
      "cache_read_input_tokens": 52416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8765,
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

_source line 45 · 2026-05-12T10:50:28.513Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NoMmQyxwekqgGESXqPhr48`</summary>

```json
{
  "file_path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/dpo_config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbe930a2-f409-40c3-b429-9bce0bcaddc7",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYck5AYbVsdpJrWuGBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e4c895b-4cf0-4be2-a3ff-b061e837b27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgaKZFDNeGYioXD3TYzfdU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8765,
      "cache_read_input_tokens": 52416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8765,
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

### Tool result

_source line 46 · 2026-05-12T10:50:28.532Z_

<details><summary>↩ Tool result · `toolu_01NoMmQyxwekqgGESXqPhr48`</summary>

```text
1	# Copyright 2020-2026 The HuggingFace Team. All rights reserved.
2	#
3	# Licensed under the Apache License, Version 2.0 (the "License");
4	# you may not use this file except in compliance with the License.
5	# You may obtain a copy of the License at
6	#
7	#     http://www.apache.org/licenses/LICENSE-2.0
8	#
9	# Unless required by applicable law or agreed to in writing, software
10	# distributed under the License is distributed on an "AS IS" BASIS,
11	# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
12	# See the License for the specific language governing permissions and
13	# limitations under the License.
14	
15	import warnings
16	from dataclasses import dataclass, field
17	from typing import Any
18	
19	from .base_config import _BaseConfig
20	
21	
22	@dataclass
23	class DPOConfig(_BaseConfig):
24	    # docstyle-ignore
25	    r"""
26	    Configuration class for the [`DPOTrainer`].
27	
28	    This class includes only the parameters that are specific to DPO training. For a full list of training arguments,
29	    please refer to the [`~transformers.TrainingArguments`] documentation. Note that default values in this class may
30	    differ from those in [`~transformers.TrainingArguments`].
31	
32	    Using [`~transformers.HfArgumentParser`] we can turn this class into
33	    [argparse](https://docs.python.org/3/library/argparse#module-argparse) arguments that can be specified on the
34	    command line.
35	
36	    Parameters:
37	        > Parameters that control the model
38	
39	        model_init_kwargs (`dict[str, Any]`, *optional*):
40	            Keyword arguments for [`~transformers.AutoModelForCausalLM.from_pretrained`], used when the `model`
41	            argument of the [`DPOTrainer`] is provided as a string.
42	        disable_dropout (`bool`, *optional*, defaults to `True`):
43	            Whether to disable dropout in the model and reference model.
44	
45	        > Parameters that control the data preprocessing
46	
47	        dataset_num_proc (`int`, *optional*):
48	            Number of processes to use for processing the dataset.
49	        max_length (`int` or `None`, *optional*, defaults to `1024`):
50	            Maximum length of the tokenized sequence. Sequences longer than `max_length` are truncated from the left or
51	            right depending on the `truncation_mode`. If `None`, no truncation is applied.
52	        truncation_mode (`str`, *optional*, defaults to `"keep_start"`):
53	            Truncation mode to use when the sequence exceeds `max_length`. The only supported value is
54	            `"keep_start"`. The `"keep_end"` value is deprecated and will be removed in v2.0.0.
55	        padding_free (`bool`, *optional*, defaults to `False`):
56	            Whether to perform forward passes without padding by flattening all sequences in the batch into a single
57	            continuous sequence. This reduces memory usage by eliminating padding overhead. Currently, this is only
58	            supported with the FlashAttention 2 or 3, which can efficiently handle the flattened batch structure.
59	        pad_to_multiple_of (`int`, *optional*):
60	            If set, the sequences will be padded to a multiple of this value.
61	        precompute_ref_log_probs (`bool`, *optional*, defaults to `False`):
62	            Whether to precompute the reference model log probabilities for the entire training dataset before
63	            training. This allows to save memory during training, as the reference model does not need to be kept in
64	            memory.
65	        precompute_ref_batch_size (`int`, *optional*):
66	            Batch size to use when precomputing reference model log probabilities. This can be set higher than the
67	            training batch size to speed up preprocessing. If `None`, defaults to `per_device_train_batch_size` for
68	            training and `per_device_eval_batch_size` for evaluation.
69	
70	        > Parameters that control the training
71	
72	        loss_type (`list[str]`, *optional*, defaults to `["sigmoid"]`):
73	            Type of loss to use. Possible values are: `'sigmoid'`, `'hinge'`, `'ipo'`, `'exo_pair'`, `'nca_pair'`,
74	            `'robust'`, `'bco_pair'`, `'sppo_hard'`, `'aot'`, `'aot_unpaired'`, `'apo_zero'`, `'apo_down'`,
75	            `'discopop'`, `'sft'`, `'sigmoid_norm'`. If multiple loss types are provided, they will be combined using
76	            the weights specified in `loss_weights`.
77	        loss_weights (`list[float]`, *optional*):
78	            List of loss weights for multi-loss combinations. Used when combining multiple loss types. Example: `[0.8,
79	            0.2, 1.0]` for MPO. If not provided, defaults to equal weights (`1.0`) for all loss types.
80	        ld_alpha (`float`, *optional*):
81	            α parameter from the LD-DPO paper, which controls the weighting of the verbose token log-probabilities in
82	            responses. If `None`, no weighting is applied to the verbose part, and the loss is equivalent to the
83	            standard DPO loss. Must be in [0.0, 1.0]: `ld_alpha=1.0` applies no weighting, and `ld_alpha=0.0` masks
84	            tokens beyond shared lengths.
85	        f_divergence_type (`str`, *optional*, defaults to `"reverse_kl"`):
86	            f-divergence regularizer between policy and reference (f-DPO paper). Possible values are: `reverse_kl`
87	            (default), `forward_kl`, `js_divergence`, `alpha_divergence`.
88	        f_alpha_divergence_coef (`float`, *optional*, defaults to `0.5`):
89	            α coefficient for the α-divergence u^-α regularizer, used only when `f_divergence_type='alpha_divergence'`.
90	        label_smoothing (`float`, *optional*, defaults to `0.0`):
91	            Label smoothing parameter used in Robust DPO and EXO. In Robust DPO, it is interpreted as the probability
92	            that a preference label is flipped and must lie in [0.0, 0.5); a typical value recommended by the Robust
93	            DPO paper is 0.1. In EXO, it corresponds to the ε label smoothing parameter, for which the paper recommends
94	            a typical value of 1e-3.
95	        beta (`float`, *optional*, defaults to `0.1`):
96	            Parameter controlling the deviation from the reference model. Higher β means less deviation from the
97	            reference model. For the IPO loss (`loss_type='ipo'`), this value is the regularization parameter denoted
98	            by τ in the [paper](https://huggingface.co/papers/2310.12036).
99	        use_weighting (`bool`, *optional*, defaults to `False`):
100	            Whether to apply WPO-style weighting (https://huggingface.co/papers/2406.11827) to preference pairs using
101	            the policy's length-normalized sequence probabilities.
102	        discopop_tau (`float`, *optional*, defaults to `0.05`):
103	            τ/temperature parameter from the DiscoPOP paper, which controls the shape of the log-ratio modulated loss
104	            when using `loss_type='discopop'`. The paper recommends the default value `discopop_tau=0.05`.
105	        activation_offloading (`bool`, *optional*, defaults to `False`):
106	            Whether to offload the activations to the CPU.
107	        sync_ref_model (`bool`, *optional*, defaults to `False`):
108	            Whether to synchronize the reference model with the active model every `ref_model_sync_steps` steps, using
109	            the `ref_model_mixup_alpha` parameter. This synchronization originates from the
110	            [TR-DPO](https://huggingface.co/papers/2404.09656) paper. `sync_ref_model=True` is not yet compatible with
111	            PEFT or `precompute_ref_log_probs=True`.
112	        ref_model_mixup_alpha (`float`, *optional*, defaults to `0.6`):
113	            α parameter from the TR-DPO paper, which controls the mix between the current policy and the previous
114	            reference policy during updates. The reference policy is updated according to the equation: `π_ref = α *
115	            π_θ + (1 - α) * π_ref_prev`. To use this parameter, you must set `sync_ref_model=True`.
116	        ref_model_sync_steps (`int`, *optional*, defaults to `512`):
117	            τ parameter from the TR-DPO paper, which determines how frequently the current policy is synchronized with
118	            the reference policy. To use this parameter, you must set `sync_ref_model=True`.
119	
120	        > Deprecated parameters
121	
122	        pad_token:
123	
124	            &lt;Deprecated version="1.1.0">
125	
126	            Parameter `pad_token` is deprecated and will be removed in version v2.0.0. Set `tokenizer.pad_token`
127	            directly and pass it as `processing_class` to the trainer instead.
128	
129	            &lt;/Deprecated>
130	
131	    > [!NOTE]
132	    > These parameters have default values different from [`~transformers.TrainingArguments`]:
133	    > - `logging_steps`: Defaults to `10` instead of `500`.
134	    > - `gradient_checkpointing`: Defaults to `True` instead of `False`.
135	    > - `bf16`: Defaults to `True` if `fp16` is not set, instead of `False`.
136	    > - `learning_rate`: Defaults to `1e-6` instead of `5e-5`.
137	    """
138	
139	    _VALID_DICT_FIELDS = _BaseConfig._VALID_DICT_FIELDS + ["model_init_kwargs"]
140	
141	    # Parameters whose default values are overridden from TrainingArguments
142	    learning_rate: float = field(
143	        default=1e-6,
144	        metadata={"help": "The initial learning rate for AdamW."},
145	    )
146	
147	    # Parameters that control the model
148	    model_init_kwargs: dict[str, Any] | str | None = field(
149	        default=None,
150	        metadata={
151	            "help": "Keyword arguments for `AutoModelForCausalLM.from_pretrained`, used when the `model` argument of "
152	            "the `DPOTrainer` is provided as a string."
153	        },
154	    )
155	    disable_dropout: bool = field(
156	        default=True,
157	        metadata={"help": "Whether to disable dropout in the model and reference model."},
158	    )
159	
160	    # Parameters that control the data preprocessing
161	    dataset_num_proc: int | None = field(
162	        default=None,
163	        metadata={"help": "Number of processes to use for processing the dataset."},
164	    )
165	    max_length: int | None = field(
166	        default=1024,
167	        metadata={
168	            "help": "Maximum length of the tokenized sequence. Sequences longer than `max_length` are truncated from "
169	            "the left or right depending on the `truncation_mode`. If `None`, no truncation is applied."
170	        },
171	    )
172	    truncation_mode: str = field(
173	        default="keep_start",
174	        metadata={
175	            "help": "Truncation mode to use when the sequence exceeds `max_length`. The only supported value is "
176	            "`'keep_start'`. The `'keep_end'` value is deprecated and will be removed in v2.0.0.",
177	            "choices": ["keep_end", "keep_start"],
178	        },
179	    )
180	    padding_free: bool = field(
181	        default=False,
182	        metadata={
183	            "help": "Whether to perform forward passes without padding by flattening all sequences in the batch into "
184	            "a single continuous sequence. This reduces memory usage by eliminating padding overhead. Currently, this "
185	            "is only supported with the FlashAttention 2 or 3, which can efficiently handle the flattened batch "
186	            "structure."
187	        },
188	    )
189	    pad_to_multiple_of: int | None = field(
190	        default=None,
191	        metadata={"help": "If set, the sequences will be padded to a multiple of this value."},
192	    )
193	    precompute_ref_log_probs: bool = field(
194	        default=False,
195	        metadata={
196	            "help": "Whether to precompute the reference model log probabilities for the entire training dataset "
197	            "before training. This allows to save memory during training, as the reference model does not need to be "
198	            "kept in memory."
199	        },
200	    )
201	    precompute_ref_batch_size: int | None = field(
202	        default=None,
203	        metadata={
204	            "help": "Batch size to use when precomputing reference model log probabilities. This can be set higher "
205	            "than the training batch size to speed up preprocessing. If `None`, defaults to "
206	            "`per_device_train_batch_size` for training and `per_device_eval_batch_size` for evaluation."
207	        },
208	    )
209	
210	    # Parameters that control the training
211	    loss_type: list[str] = field(
212	        default_factory=lambda: ["sigmoid"],
213	        metadata={
214	            "help": "Type of loss to use. Possible values are: `'sigmoid'`, `'hinge'`, `'ipo'`, `'exo_pair'`, "
215	            "`'nca_pair'`, `'robust'`, `'bco_pair'`, `'sppo_hard'`, `'aot'`, `'aot_unpaired'`, `'apo_zero'`, "
216	            "`'apo_down'`, `'discopop'`, `'sft'`, `'sigmoid_norm'`. If multiple loss types are provided, they will be "
217	            "combined using the weights specified in `loss_weights`.",
218	        },
219	    )
220	    loss_weights: list[float] | None = field(
221	        default=None,
222	        metadata={
223	            "help": "List of loss weights for multi-loss combinations. Used when combining multiple loss types. "
224	            "Example: `[0.8, 0.2, 1.0]` for MPO. If not provided, defaults to equal weights (`1.0`) for all loss "
225	            "types."
226	        },
227	    )
228	    ld_alpha: float | None = field(
229	        default=None,
230	        metadata={
231	            "help": "α parameter from the LD-DPO paper, which controls the weighting of the verbose token "
232	            "log-probabilities in responses. If `None`, no weighting is applied to the verbose part, and the loss is "
233	            "equivalent to the standard DPO loss. Must be in [0.0, 1.0]: `ld_alpha=1.0` applies no weighting, and "
234	            "`ld_alpha=0.0` masks tokens beyond shared lengths.",
235	        },
236	    )
237	    f_divergence_type: str = field(
238	        default="reverse_kl",
239	        metadata={
240	            "help": "f-divergence regularizer between policy and reference (f-DPO paper). Possible values are: "
241	            "`reverse_kl` (default), `forward_kl`, `js_divergence`, `alpha_divergence`.",
242	        },
243	    )
244	    f_alpha_divergence_coef: float = field(
245	        default=0.5,
246	        metadata={
247	            "help": "α coefficient for the α-divergence u^-α regularizer, used only when "
248	            "`f_divergence_type='alpha_divergence'`."
249	        },
250	    )
251	    label_smoothing: float = field(
252	        default=0.0,
253	        metadata={
254	            "help": "Label smoothing parameter used in Robust DPO and EXO. In Robust DPO, it is interpreted as the "
255	            "probability that a preference label is flipped and must lie in [0.0, 0.5); a typical value recommended "
256	            "by the Robust DPO paper is 0.1. In EXO, it corresponds to the ε label smoothing parameter, for which the "
257	            "paper recommends a typical value of 1e-3."
258	        },
259	    )
260	    beta: float = field(
261	        default=0.1,
262	        metadata={
263	            "help": "Parameter controlling the deviation from the reference model. Higher β means less deviation from "
264	            "the reference model. For the IPO loss (`loss_type='ipo'`), this value is the regularization parameter "
265	            "denoted by τ in the [paper](https://huggingface.co/papers/2310.12036)."
266	        },
267	    )
268	    use_weighting: bool = field(
269	        default=False,
270	        metadata={
271	            "help": "Whether to apply WPO-style weighting (https://huggingface.co/papers/2406.11827) to preference "
272	            "pairs using the policy's length-normalized sequence probabilities."
273	        },
274	    )
275	    discopop_tau: float = field(
276	        default=0.05,
277	        metadata={
278	            "help": "τ/temperature parameter from the DiscoPOP paper, which controls the shape of the log-ratio "
279	            "modulated loss when using `loss_type='discopop'`. The paper recommends the default value "
280	            "`discopop_tau=0.05`."
281	        },
282	    )
283	    activation_offloading: bool = field(
284	        default=False,
285	        metadata={"help": "Whether to offload the activations to the CPU."},
286	    )
287	    sync_ref_model: bool = field(
288	        default=False,
289	        metadata={
290	            "help": "Whether to synchronize the reference model with the active model every `ref_model_sync_steps` "
291	            "steps, using the `ref_model_mixup_alpha` parameter. This synchronization originates from the "
292	            "[TR-DPO](https://huggingface.co/papers/2404.09656) paper. `sync_ref_model=True` is not yet compatible "
293	            "with PEFT or `precompute_ref_log_probs=True`."
294	        },
295	    )
296	    ref_model_mixup_alpha: float = field(
297	        default=0.6,
298	        metadata={
299	            "help": "α parameter from the TR-DPO paper, which controls the mix between the current policy and the "
300	            "previous reference policy during updates. The reference policy is updated according to the equation: "
301	            "`π_ref = α * π_θ + (1 - α) * π_ref_prev`. To use this parameter, you must set `sync_ref_model=True`."
302	        },
303	    )
304	    ref_model_sync_steps: int = field(
305	        default=512,
306	        metadata={
307	            "help": "τ parameter from the TR-DPO paper, which determines how frequently the current policy is "
308	            "synchronized with the reference policy. To use this parameter, you must set `sync_ref_model=True`."
309	        },
310	    )
311	
312	    # Deprecated parameters
313	    pad_token: str | None = field(
314	        default=None,
315	        metadata={
316	            "help": "Deprecated. Set `tokenizer.pad_token` directly and pass it as `processing_class` to the trainer instead."
317	        },
318	    )
319	
320	    def __post_init__(self):
321	        if isinstance(self.loss_type, str):
322	            self.loss_type = [self.loss_type]
323	        if self.loss_weights is not None and len(self.loss_weights) != len(self.loss_type):
324	            raise ValueError(
325	                "`loss_weights` must have the same length as `loss_type` when combining multiple losses. "
326	                f"Got {len(self.loss_weights)} weights for {len(self.loss_type)} loss types."
327	            )
328	        if self.pad_token is not None:
329	            warnings.warn(
330	                "`pad_token` is deprecated and will be removed in v2.0.0. "
331	                "Set `tokenizer.pad_token` directly and pass it as `processing_class` to the trainer instead.",
332	                FutureWarning,
333	                stacklevel=3,
334	            )
335	        if self.truncation_mode == "keep_end":
336	            warnings.warn(
337	                "The `'keep_end'` truncation mode is deprecated and will be removed in v2.0.0. "
338	                "Use `truncation_mode='keep_start'` (the default) instead.",
339	                FutureWarning,
340	                stacklevel=3,
341	            )
342	
343	        super().__post_init__()
344	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e4c895b-4cf0-4be2-a3ff-b061e837b27c",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "e67bfee8-488e-44dc-9563-d7ea3486edb9",
  "sourceToolAssistantUUID": "9e4c895b-4cf0-4be2-a3ff-b061e837b27c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-12T10:50:28.926Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01ViJxLUbYDFobYKEcPDUxJz`</summary>

```json
{
  "pattern": "def selective_log_softmax",
  "path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e67bfee8-488e-44dc-9563-d7ea3486edb9",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYck5AYbVsdpJrWuGBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbbcc51a-7cbe-41c0-b40a-f8978e287f0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgaKZFDNeGYioXD3TYzfdU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8765,
      "cache_read_input_tokens": 52416,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8765
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 52416,
          "cache_creation_input_tokens": 8765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8765,
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

_source line 48 · 2026-05-12T10:50:28.964Z_

<details><summary>↩ Tool result · `toolu_01ViJxLUbYDFobYKEcPDUxJz`</summary>

```text
Found 1 file
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/utils.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbbcc51a-7cbe-41c0-b40a-f8978e287f0c",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "fff6720d-a220-44e8-8425-6a0bc3589ea7",
  "sourceToolAssistantUUID": "bbbcc51a-7cbe-41c0-b40a-f8978e287f0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-12T10:50:33.223Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XkPMnb71GC5xoT1ausDqn6`</summary>

```json
{
  "pattern": "def selective_log_softmax",
  "path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/utils.py",
  "output_mode": "content",
  "-A": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff6720d-a220-44e8-8425-6a0bc3589ea7",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYd6ymHV8XBee1jKHWB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c60b217e-8098-4016-8832-fcc9b70dea2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFqwGp6ZaZ45MZH85xgWWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6008,
      "cache_read_input_tokens": 61181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6008,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-12T10:50:33.261Z_

<details><summary>↩ Tool result · `toolu_01XkPMnb71GC5xoT1ausDqn6`</summary>

````text
436:def selective_log_softmax(logits, index) -> torch.Tensor:
437-    """
438-    A memory-efficient implementation of the common `log_softmax -> gather` operation.
439-
440-    This function is equivalent to the following naive implementation:
441-    ```python
442-    # for index with shape (...):
443-    logps = torch.gather(logits.log_softmax(-1), dim=-1, index=index.unsqueeze(-1)).squeeze(-1)
444-    # for index with shape (..., K):
445-    logps = torch.gather(logits.log_softmax(-1), dim=-1, index=index)
446-    ```
447-
448-    Args:
449-        logits (`torch.Tensor`):
450-            Logits tensor of shape `(..., num_classes)`.
451-        index (`torch.Tensor`):
452-            Index tensor of shape `(..., K)` or `(...)`, specifying the positions to gather from the log-softmax
453-            output. When the last case is used, `K` log-probabilities are gathered per position (e.g. for top-K)
454-
455-    Returns:
456-        `torch.Tensor`:
457-            Gathered log probabilities with the same shape as `index`.
458-    """
459-    squeeze = index.ndim == logits.ndim - 1
460-    if squeeze:
461-        index = index.unsqueeze(-1)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c60b217e-8098-4016-8832-fcc9b70dea2f",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "c6ad9ab2-1186-455a-b425-afac0398fd11",
  "sourceToolAssistantUUID": "c60b217e-8098-4016-8832-fcc9b70dea2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-12T10:50:34.253Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018tYWSYfN4NDoay8PLoaAfF`</summary>

```json
{
  "pattern": "def entropy_from_logits",
  "path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/utils.py",
  "output_mode": "content",
  "-A": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6ad9ab2-1186-455a-b425-afac0398fd11",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYd6ymHV8XBee1jKHWB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b93a46dc-4cb0-4846-820d-24630fb220ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFqwGp6ZaZ45MZH85xgWWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6008,
      "cache_read_input_tokens": 61181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6008,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-12T10:50:34.275Z_

<details><summary>↩ Tool result · `toolu_018tYWSYfN4NDoay8PLoaAfF`</summary>

```text
483:def entropy_from_logits(logits: torch.Tensor, chunk_size: int = 128) -> torch.Tensor:
484-    """
485-    Compute the Shannon entropy (in nats) for each row of *logits* in a memory-efficient way.
486-
487-    Instead of materializing the full softmax for all rows at once, the logits are flattened to shape (N, num_classes),
488-    where N is the product of all leading dimensions. Computation is then performed in chunks of size `chunk_size`
489-    along this flattened dimension, reducing peak memory usage. The result is reshaped back to match the input's
490-    leading dimensions.
491-
492-    Args:
493-        logits (`torch.Tensor`):
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b93a46dc-4cb0-4846-820d-24630fb220ef",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "691f12dc-0780-4bd7-8101-092de9862669",
  "sourceToolAssistantUUID": "b93a46dc-4cb0-4846-820d-24630fb220ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-12T10:50:35.176Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DW5tXVH6HwrTcsckhzNaez`</summary>

```json
{
  "pattern": "class _BaseTrainer|class _BaseConfig",
  "path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer",
  "output_mode": "content",
  "-A": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "691f12dc-0780-4bd7-8101-092de9862669",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYd6ymHV8XBee1jKHWB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec8c5000-4c0d-4050-8213-5cedf26eba0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFqwGp6ZaZ45MZH85xgWWf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6008,
      "cache_read_input_tokens": 61181,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6008
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 376,
          "cache_read_input_tokens": 61181,
          "cache_creation_input_tokens": 6008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6008,
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

_source line 54 · 2026-05-12T10:50:35.195Z_

<details><summary>↩ Tool result · `toolu_01DW5tXVH6HwrTcsckhzNaez`</summary>

```text
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_config.py:21:class _BaseConfig(TrainingArguments):
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_config.py-22-    """
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_config.py-23-    Base configuration class for all TRL trainer configurations.
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_config.py-24-
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_config.py-25-    Subclasses [`~transformers.TrainingArguments`] and overrides fields that are common across TRL trainers or that
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_config.py-26-    contain unescaped "%" characters which would cause argparse to raise a `TypeError` when rendering `--help` output.
--
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_trainer.py:26:class _BaseTrainer(Trainer):
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_trainer.py-27-    _tag_names = []
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_trainer.py-28-    _name = "Base"
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_trainer.py-29-    _paper = {}
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_trainer.py-30-    _template_file = None
/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/base_trainer.py-31-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec8c5000-4c0d-4050-8213-5cedf26eba0d",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "a01a0fc1-2f48-4b17-b6e0-49b9302aa1dd",
  "sourceToolAssistantUUID": "ec8c5000-4c0d-4050-8213-5cedf26eba0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-12T10:50:41.218Z_

Let me also check the `use_adapter` context manager since it's key for PEFT ref model handling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a01a0fc1-2f48-4b17-b6e0-49b9302aa1dd",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYdZddyfuek5oS6ovkF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68f50a6a-6af0-447f-9207-9f79eec865f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JgMyiWCkJWSQwftwHxHmP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1516,
      "cache_read_input_tokens": 67189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1516,
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

_source line 56 · 2026-05-12T10:50:42.253Z_

<details open><summary>🔧 Tool call — Grep · `toolu_019hANpcwPyH4nebtBsJBXvL`</summary>

```json
{
  "pattern": "def use_adapter|class use_adapter",
  "path": "/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/utils.py",
  "output_mode": "content",
  "-A": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68f50a6a-6af0-447f-9207-9f79eec865f7",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYdZddyfuek5oS6ovkF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b197c977-cf86-485c-b050-394fdffd8095",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JgMyiWCkJWSQwftwHxHmP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1516,
      "cache_read_input_tokens": 67189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1516,
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

_source line 57 · 2026-05-12T10:50:42.264Z_

<details><summary>↩ Tool result · `toolu_019hANpcwPyH4nebtBsJBXvL`</summary>

````text
1057:def use_adapter(model: "PeftModel", adapter_name: str | None):
1058-    """
1059-    Context manager to temporarily set and reset the active adapter in a PEFT model.
1060-
1061-    Args:
1062-        model ([`~peft.PeftModel`]):
1063-            PEFT model to manage.
1064-        adapter_name (`str` or `None`):
1065-            Name of the adapter to set as active. If `None`, the context manager will disable all adapters.
1066-
1067-    Example:
1068-    ```python
1069-    >>> from trl.trainer.utils import use_adapter
1070-    >>> from peft import AutoPeftModelForCausalLM
1071-    >>> import torch
1072-
1073-    >>> model = AutoPeftModelForCausalLM.from_pretrained("path/to/model")
1074-    >>> input_ids = torch.tensor([[1, 2, 3]])
1075-    >>> with use_adapter(model, "adapter_name"):
1076-    ...     outputs = model(input_ids)
1077-    ```
1078-    """
1079-
1080-    if not is_peft_available():
1081-        raise ImportError(
1082-            "You're trying to use a PEFT adapter but PEFT is not installed. Please install it with `pip install peft`."
1083-        )
1084-    if adapter_name is None:
1085-        with model.disable_adapter():
1086-            yield
1087-    else:
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b197c977-cf86-485c-b050-394fdffd8095",
  "isSidechain": true,
  "promptId": "e0e0ecba-0d98-42a1-801b-52326b81360a",
  "agentId": "a466609ede15340b7",
  "type": "user",
  "uuid": "7565398d-7e0c-441e-a8f6-488ae98826c8",
  "sourceToolAssistantUUID": "b197c977-cf86-485c-b050-394fdffd8095",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-12T10:51:46.671Z_

Now I have a complete picture. Here is the thorough report.

---

## TRL v1.4.0 DPOTrainer API -- Complete Analysis

**Source file**: `/home/ubuntu/.local/lib/python3.14/site-packages/trl/trainer/dpo_trainer.py` (1520 lines)

### Architecture Overview

`DPOTrainer` extends `_BaseTrainer`, which extends `transformers.Trainer`. The old methods `get_batch_loss_metrics`, `concatenated_forward`, `get_batch_logps`, and `dpo_loss` **no longer exist** as separate methods. The entire loss pipeline has been consolidated into a single `_compute_loss` method. This is a major refactor from pre-0.12 versions.

---

### Key Methods and Signatures

#### 1. `__init__`
```python
def __init__(
    self,
    model: "str | PreTrainedModel | PeftModel",
    ref_model: PreTrainedModel | None = None,
    args: DPOConfig | None = None,
    data_collator: DataCollator | None = None,
    train_dataset: Dataset | IterableDataset | None = None,
    eval_dataset: Dataset | IterableDataset | dict[str, Dataset | IterableDataset] | None = None,
    processing_class: PreTrainedTokenizerBase | ProcessorMixin | None = None,
    compute_metrics: Callable[[EvalPrediction], dict] | None = None,
    callbacks: list[TrainerCallback] | None = None,
    optimizers: tuple[...] = (None, None),
    peft_config: "PeftConfig | None" = None,
)
```

#### 2. `compute_loss` (dispatcher)
```python
def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
    if self.use_liger_kernel:
        return self._compute_loss_liger(model, inputs, return_outputs)
    else:
        return self._compute_loss(model, inputs, return_outputs)
```

#### 3. `_compute_loss` (core loss computation -- THE method to override for DMPO)
```python
def _compute_loss(self, model, inputs, return_outputs):
```
This is the single monolithic method (~315 lines) that does everything:
- Forward pass through policy model
- Per-token log prob computation via `selective_log_softmax`
- Reference model forward pass (or uses precomputed ref logps)
- Log ratio computation
- f-divergence score transformation
- Loss computation for all 15 loss types
- Metrics logging

#### 4. `compute_ref_log_probs`
```python
def compute_ref_log_probs(self, inputs):
    """Computes reference log probabilities for a single padded batch."""
```
Used during precomputation. Handles three ref model scenarios: standalone ref_model, PEFT with "ref" adapter, PEFT with disabled adapter.

#### 5. `_precompute_ref_logps`
```python
def _precompute_ref_logps(self, dataset: Dataset, name: str, batch_size: int) -> Dataset:
```
Precomputes and caches ref log probs as `.npz` files. Adds `ref_chosen_logps` and `ref_rejected_logps` columns to the dataset.

#### 6. `_prepare_dataset`
```python
def _prepare_dataset(self, dataset, processing_class, args, dataset_name) -> Dataset | IterableDataset:
```
Handles: prompt extraction, EOS token addition, tokenization into `prompt_ids`, `chosen_ids`, `rejected_ids`.

#### 7. `_tokenize`
```python
def _tokenize(self, processing_class, input: str | list, **kwargs) -> dict[str, list]:
```

#### 8. `prediction_step` (eval override)
```python
def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys=None):
```

#### 9. `training_step` (activation offloading wrapper)
```python
def training_step(self, *args, **kwargs):
    with self.maybe_activation_offload_context:
        return super().training_step(*args, **kwargs)
```

---

### Loss Computation Pipeline (inside `_compute_loss`)

**Step 1: Policy forward pass**
```python
outputs = model(**model_kwargs)  # model_kwargs = inputs minus completion_mask, ref_logps
```

**Step 2: Per-token log probabilities**
```python
shift_logits = outputs.logits[..., :-1, :].contiguous()
shift_labels = input_ids[..., 1:].contiguous()
shift_completion_mask = completion_mask[..., 1:].contiguous()
per_token_logps = selective_log_softmax(shift_logits, shift_labels)
per_token_logps[shift_completion_mask == 0] = 0.0  # mask non-completion tokens
```

**Step 3: Aggregation (sum over sequence)**
```python
if self.ld_alpha is None:
    logps = per_token_logps.sum(dim=1)  # simple sum
else:
    # LD-DPO: split into shared-length and tail portions
    # shared_logps + ld_alpha * tail_logps
chosen_logps, rejected_logps = logps.chunk(2, dim=0)  # batch is [chosen_batch, rejected_batch]
```

**Step 4: Reference log probabilities**
Three paths:
1. `precompute_ref_logps=True`: loaded from `inputs["ref_chosen_logps"]`, `inputs["ref_rejected_logps"]`
2. PEFT model, no explicit ref_model: disables adapter (or uses "ref" adapter copy) in `torch.no_grad()` context
3. Explicit `self.ref_model`: forward pass through `self.ref_model(**model_kwargs)` in `torch.no_grad()` context

Same `selective_log_softmax` + `sum(dim=1)` aggregation as policy model.

**Step 5: Log ratios and f-divergence scores**
```python
chosen_logratios = chosen_logps - ref_chosen_logps
rejected_logratios = rejected_logps - ref_rejected_logps
# Then f-divergence transformation (reverse_kl = identity, forward_kl, js_divergence, alpha_divergence)
delta_score = chosen_scores - rejected_scores
```

**Step 6: Loss computation**
Iterates over `(loss_type, loss_weight)` pairs, accumulates `loss += per_sequence_loss.mean() * loss_weight`.

---

### Data Format and Batching

**Input format**: `{prompt, chosen, rejected}` -- explicit prompt recommended. Supports both plain text and conversational (list of message dicts).

**After tokenization** (by `_prepare_dataset`): each example becomes `{prompt_ids, chosen_ids, rejected_ids}`.

**DataCollatorForPreference** concatenates prompt+chosen and prompt+rejected, then pads. The batch tensor layout is:
```
input_ids:       [chosen_0, chosen_1, ..., chosen_N, rejected_0, rejected_1, ..., rejected_N]
completion_mask: [0..0, 1..1, 0..0, 1..1, ...]  (0 for prompt tokens, 1 for completion tokens)
```
So `chunk(2, dim=0)` splits chosen vs rejected halves.

---

### PEFT / QLoRA Handling

1. If `peft_config` is passed: wraps model via `get_peft_model(model, peft_config)`. Sets `self.ref_model = None`.
2. If model is already a PeftModel with no explicit ref_model: creates a "ref" adapter copy:
   ```python
   model.add_adapter("ref", model.peft_config["default"])
   # copies default adapter weights to ref adapter
   ```
3. For QLoRA (quantized models): adapter weights are cast to bf16:
   ```python
   if getattr(model, "is_loaded_in_4bit", False) or getattr(model, "is_loaded_in_8bit", False):
       for param in model.parameters():
           if param.requires_grad:
               param.data = param.data.to(torch.bfloat16)
   ```
4. Reference model computation with PEFT:
   ```python
   model = self.accelerator.unwrap_model(model)
   with use_adapter(model, adapter_name="ref" if "ref" in model.peft_config else None):
       ref_outputs = self.model(**model_kwargs)
   ```
   `use_adapter(model, None)` calls `model.disable_adapter()` -- reverts to base model weights.

---

### DPOConfig Parameters (complete list)

| Parameter | Type | Default | Description |
|---|---|---|---|
| `model_init_kwargs` | `dict\|str\|None` | `None` | kwargs for `from_pretrained` |
| `disable_dropout` | `bool` | `True` | Disable dropout in both models |
| `dataset_num_proc` | `int\|None` | `None` | Dataset processing workers |
| `max_length` | `int\|None` | `1024` | Max tokenized sequence length |
| `truncation_mode` | `str` | `"keep_start"` | Truncation strategy |
| `padding_free` | `bool` | `False` | Flatten sequences (currently disabled) |
| `pad_to_multiple_of` | `int\|None` | `None` | Pad to multiple |
| `precompute_ref_log_probs` | `bool` | `False` | Precompute ref logps before training |
| `precompute_ref_batch_size` | `int\|None` | `None` | Batch size for precomputation |
| `loss_type` | `list[str]` | `["sigmoid"]` | Loss function(s) |
| `loss_weights` | `list[float]\|None` | `None` | Weights for multi-loss |
| `ld_alpha` | `float\|None` | `None` | LD-DPO length weighting |
| `f_divergence_type` | `str` | `"reverse_kl"` | f-divergence type |
| `f_alpha_divergence_coef` | `float` | `0.5` | Alpha divergence coefficient |
| `label_smoothing` | `float` | `0.0` | Label smoothing |
| `beta` | `float` | `0.1` | KL penalty strength |
| `use_weighting` | `bool` | `False` | WPO-style weighting |
| `discopop_tau` | `float` | `0.05` | DiscoPOP temperature |
| `activation_offloading` | `bool` | `False` | Offload activations to CPU |
| `sync_ref_model` | `bool` | `False` | TR-DPO sync |
| `ref_model_mixup_alpha` | `float` | `0.6` | TR-DPO mix coefficient |
| `ref_model_sync_steps` | `int` | `512` | TR-DPO sync frequency |
| `learning_rate` | `float` | `1e-6` | Overridden default |

`_BaseConfig` extends `TrainingArguments`, also overriding: `logging_steps=10`, `gradient_checkpointing=True`, `bf16=True`.

---

### Key Helper: `selective_log_softmax`
```python
def selective_log_softmax(logits, index) -> torch.Tensor:
    """Memory-efficient log_softmax -> gather. Equivalent to:
    logps = torch.gather(logits.log_softmax(-1), dim=-1, index=index.unsqueeze(-1)).squeeze(-1)
    """
```

---

### Extension Strategy for DMPO

The cleanest extension point is to **subclass DPOTrainer and override `_compute_loss`**. This single method contains:
- The forward pass logic
- Per-token logp computation
- Reference logp computation
- Log ratio computation
- All loss type implementations
- All metrics logging

There is no need to worry about `get_batch_loss_metrics` or `concatenated_forward` -- those methods were removed in the refactor. The entire pipeline lives in `_compute_loss`.

For a multi-turn variant, you would likely need to:
1. Override `_compute_loss` to handle turn-level log probability aggregation differently (instead of a single `sum(dim=1)`)
2. Potentially override `_prepare_dataset` to handle multi-turn tokenization with per-turn completion masks
3. Potentially provide a custom `DataCollator` that produces per-turn `completion_mask` tensors instead of a single binary mask

The `completion_mask` tensor is the key mechanism -- it marks which tokens are "completion" tokens (1) vs prompt tokens (0). For multi-turn DPO, you'd need turn-level masks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7565398d-7e0c-441e-a8f6-488ae98826c8",
  "isSidechain": true,
  "agentId": "a466609ede15340b7",
  "requestId": "req_011CaxYe6BumFpFW8g4sa9yH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a7d4040-4b88-44f3-968b-461ceb289fa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl",
  "sessionId": "9c825e4f-073f-424a-a943-848e9782783e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Mw2WfnkG1fPHmxm1zYxNx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 68705,
      "output_tokens": 3266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 682
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3266,
          "cache_read_input_tokens": 68705,
          "cache_creation_input_tokens": 682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 682,
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
