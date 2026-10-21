# research smolvla official checkpoint

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_research_smolvla_official_checkpoint_20260518T115208.jsonl`
- **Structured JSON:** [`7a63a483b3720a589006.json`](../../sessions/7a/7a63a483b3720a589006.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-18T11:53:56.958540+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T11:53:56.958901+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T11:53:56.959071+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA HuggingFace LIBERO finetuned checkpoint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA HuggingFace LIBERO finetuned checkpoint"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T11:53:56.959249+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co SmolVLA LIBERO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co SmolVLA LIBERO"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T11:53:56.959384+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HuggingFaceVLA SmolVLA LIBERO batch 64"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HuggingFaceVLA SmolVLA LIBERO batch 64"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T11:53:56.959536+00:00_

Web search results for query: "site:huggingface.co SmolVLA LIBERO"

Links: [{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"bicmol/smolvla-libero · Hugging Face","url":"https://huggingface.co/bicmol/smolvla-libero"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"Alkatt/smolvla-libero-100000 · Hugging Face","url":"https://huggingface.co/Alkatt/smolvla-libero-100000"},{"title":"irisWU23/smolVLA_libero · Hugging Face","url":"https://huggingface.co/irisWU23/smolVLA_libero"},{"title":"HuggingFaceVLA/smolvla_libero_ckpts · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts"}]

I found search results for SmolVLA and LIBERO on Hugging Face. Here's what I found:

SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. This policy has been trained and pushed to the Hub using LeRobot.

Regarding SmolVLA's performance on LIBERO, SmolVLA-450M outperforms much larger VLAs and strong baselines such as ACT on simulation (LIBERO, Meta-World) and real-world tasks (SO100, SO101).

Additionally, there's a related resource called Smol-LIBERO, a compact version of the LIBERO benchmark built to make experimentation fast and accessible at just 1.79 GB (compared to ~34 GB for the full LIBERO).

The main model repository is available at: https://h
…[truncated 146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T11:53:56.959712+00:00_

Web search results for query: "SmolVLA HuggingFace LIBERO finetuned checkpoint"

Links: [{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"bicmol/smolvla-libero · Hugging Face","url":"https://huggingface.co/bicmol/smolvla-libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"},{"title":"k1000dai/smolvla_libero_finetune · Hugging Face","url":"https://huggingface.co/k1000dai/smolvla_libero_finetune"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"},{"title":"Alkatt/smolvla-libero-100000 · Hugging Face","url":"https://huggingface.co/Alkatt/smolvla-libero-100000"},{"title":"ezzzeee/my_smolvla · Hugging Face","url":"https://huggingface.co/ezzzeee/my_smolvla"}]

Based on the search results, here's what I found about SmolVLA HuggingFace LIBERO finetuned checkpoints:

## Official SmolVLA LIBERO Checkpoint

SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. The official HuggingFace checkpoint is available at **HuggingFaceVLA/smolvla_libero** on Hugging Face Hub.

## Multiple Finetuned Variants

There are several community-created SmolVLA LIBERO finetuned checkpoints available on Hugging Face Hub:

1. **HuggingFaceVLA/smolvla_libero** - The official checkpoint with 4,446 finetuned steps
2. **bicmol/smolvl
…[truncated 803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T11:53:56.959896+00:00_

Web search results for query: "HuggingFaceVLA SmolVLA LIBERO batch 64"

Links: [{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"The performance of SmolVLA on LIBERO cannot be replicated · Issue #1369 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1369"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"LIBERO Leaderboard - a Hugging Face Space by HuggingFaceVLA","url":"https://huggingface.co/spaces/HuggingFaceVLA/libero-vla-leaderboard"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"Question about the HuggingFaceVLA/smolvla_libero Model Configuration · Issue #2294 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2294"},{"title":"blog/smolvla.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/smolvla.md"},{"title":"HuggingFaceVLA/smolvla_libero_ckpts · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts"}]

Based on the search results, here's what I found about HuggingFaceVLA SmolVLA, LIBERO, and batch 64:

## SmolVLA Overview
SmolVLA is a 450M parameter vision-language-action model designed for affordable and efficient robotics, optimized to run on consumer hardware while maintaining competitive performance. SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on
…[truncated 857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T11:53:56.960080+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co HuggingFaceVLA/smolvla_libero training config batch_size steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co HuggingFaceVLA/smolvla_libero training config batch_size steps"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T11:53:56.960235+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github huggingface lerobot issue 1369 SmolVLA LIBERO replicate performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github huggingface lerobot issue 1369 SmolVLA LIBERO replicate performance"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T11:53:56.960357+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA LIBERO 87.3 success rate batch_size 64 training details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA LIBERO 87.3 success rate batch_size 64 training details"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T11:53:56.960497+00:00_

Web search results for query: "site:huggingface.co HuggingFaceVLA/smolvla_libero training config batch_size steps"

Links: [{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"Meta-World · Hugging Face","url":"https://huggingface.co/docs/lerobot/metaworld"},{"title":"train_config.json · Alkatt/smolvla-libero-100000 at main","url":"https://huggingface.co/Alkatt/smolvla-libero-100000/blob/main/train_config.json"}]

Based on the search results, I found relevant information about the HuggingFaceVLA/smolvla_libero training configuration:

The training command for SmolVLA on LIBERO uses 100,000 steps and a batch size of 4, as shown in the documented training example. 

Additionally, the Physical Intelligence LIBERO base model (pi05_libero) was finetuned for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the HuggingFace LIBERO dataset.

The search results show example training configurations, though the specific original training config for HuggingFaceVLA/smolvla_libero with its exact hyperparameters may be accessible through the model repository files (such as the train_config.json files mentioned in the results).


REMINDER: You MUST include the sources above in your respon
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T11:53:56.960677+00:00_

Web search results for query: "github huggingface lerobot issue 1369 SmolVLA LIBERO replicate performance"

Links: [{"title":"The performance of SmolVLA on LIBERO cannot be replicated · Issue #1369 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1369"},{"title":"Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2354"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2107"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"smolvla can not reproduce results in libero eval using official checkpoints · Issue #3264 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3264"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"}]

Based on the web search results, I found information about GitHub issue #1369 in the Hugging Face LeRobot repository:

Issue #1369, opened on June 23, 2025, reports that a user trained SmolVLA from scratch on the LIBERO dataset but couldn't reproduce its results from the
…[truncated 989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T11:53:56.960865+00:00_

Web search results for query: "SmolVLA LIBERO 87.3 success rate batch_size 64 training details"

Links: [{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA: An Open-Source Vision-Language-Action Model for Modern Robotics","url":"https://smolvla.net/index_en"},{"title":"Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2107"},{"title":"SmolVLA: Compact Vision-Language-Action Model","url":"https://www.emergentmind.com/topics/smolvla"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]","url":"https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"SmolVLA: compact VLA for robot policy | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/smolvla-compact-vla-for-robot-policy-b30604ac23c5"},{"title":"Hugging Face Releases SmolVLA: A Compact Vision-Language-Action Model for Affordable and Efficient Robotics - MarkTechPost","url":"https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/"},{"title":"How can i train and eval SmolVLA in libero? · Issue #2258 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2258"}]

Based on the search results, here's what I found about SmolVLA's 87.3% success rate on LIBERO with
…[truncated 1241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T11:53:56.961146+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com huggingface lerobot issues 3287 training configurations batch size SmolVLA LIBERO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com huggingface lerobot issues 3287 training configurations batch size SmolVLA LIBERO"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T11:53:56.961386+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co HuggingFaceVLA/smolvla_libero_ckpts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co HuggingFaceVLA/smolvla_libero_ckpts"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T11:53:56.961642+00:00_

Web search results for query: "site:huggingface.co HuggingFaceVLA/smolvla_libero_ckpts"

Links: [{"title":"HuggingFaceVLA/smolvla_libero_ckpts · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"HuggingFaceVLA (Hugging Face Vision Language Action Models Research)","url":"https://huggingface.co/HuggingFaceVLA"},{"title":"LIBERO Leaderboard - a Hugging Face Space by HuggingFaceVLA","url":"https://huggingface.co/spaces/HuggingFaceVLA/libero-vla-leaderboard"},{"title":"LIBERO - a HuggingFaceVLA Collection","url":"https://huggingface.co/collections/HuggingFaceVLA/libero"},{"title":"HuggingFaceVLA/libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/libero"},{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"policy_preprocessor.json · HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/blame/main/policy_preprocessor.json"}]

Based on the search results, here's what I found:

The HuggingFaceVLA/smolvla_libero_ckpts model is deprecated and users should use the updated version at https://huggingface.co/HuggingFaceVLA/smolvla_libero instead.

The updated model page shows that SmolVLA is a compact, efficient vision-language-action model that achieves competitive performance at reduced computational costs and can be deployed on consumer-grade hardware. This policy has been trained and pushed to the Hub using LeRobot.

The repository contains 1.22 GB of model weights and configuration files, with
…[truncated 176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T11:53:56.961903+00:00_

Web search results for query: "site:github.com huggingface lerobot issues 3287 training configurations batch size SmolVLA LIBERO"

Links: [{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"},{"title":"Cannot reproduce SmolVLA results on LIBERO benchmark · Issue #2354 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2354"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"Low Success Rate When Training SmolVLA-0.24B on LIBERO · Issue #2107 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2107"},{"title":"smolvla training bugs on 3090 · Issue #1234 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1234"},{"title":"Evaluation of Policies on Libero · Issue #2731 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2731"},{"title":"`smolvla_base training`: `Expected all tensors to be on the same device` · Issue #1377 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1377"},{"title":"smolvla issue · Issue #2790 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2790"},{"title":"Using the latest version of training in libero the loss is as high as 0.05 · Issue #1842 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1842"}]

I found GitHub Issue #3287 from the HuggingFace LeRobot repository. Here's what the search revealed:

The issue is titled "Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LI
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T11:53:56.962158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "huggingface.co HuggingFaceVLA smolvla_libero train_config.json batch_size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "huggingface.co HuggingFaceVLA smolvla_libero train_config.json batch_size"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T11:53:56.962327+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA paper arxiv 2506.01844 LIBERO training batch size 64 100000 steps configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA paper arxiv 2506.01844 LIBERO training batch size 64 100000 steps configuration"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T11:53:56.962478+00:00_

Web search results for query: "huggingface.co HuggingFaceVLA smolvla_libero train_config.json batch_size"

Links: [{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"train_config.json · Alkatt/smolvla-libero-100000 at main","url":"https://huggingface.co/Alkatt/smolvla-libero-100000/blob/main/train_config.json"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"HuggingFaceVLA/smolvla_libero at main","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero/tree/main"},{"title":"HuggingFaceVLA/smolvla_libero · Hugging Face","url":"https://huggingface.co/HuggingFaceVLA/smolvla_libero"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"HuggingFaceVLA/smol-libero · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceVLA/smol-libero"},{"title":"Clarifications on fine-tuning on different envs and embodiments · Issue #2259 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2259"},{"title":"HuggingFaceTB/SmolVLM-Instruct · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct"}]

I found search results related to your query about HuggingFaceVLA's SmolVLA model and LIBERO training. Here are the relevant findings:

The search results show that SmolVLA is a compact, efficient vision-language-action model that has been trained and pushed to the Hub using LeRobot. The HuggingFaceVLA/smolvla_libero repository contains the trained policy.

Regarding batch size configurations, the search results show training examples with different batch sizes:

- A training command example uses `--batch_size=4` for LIBERO training
- Another fine-tuning example uses `--batch_size=32` for custom tasks
- The Physical Intelligence LIBERO base model was fine-tuned with a batch size of 256 on 8 H100 GPUs

Wh
…[truncated 480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T11:53:56.962647+00:00_

Web search results for query: "SmolVLA paper arxiv 2506.01844 LIBERO training batch size 64 100000 steps configuration"

Links: [{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://www.researchgate.net/publication/392370918_SmolVLA_A_Vision-Language-Action_Model_for_Affordable_and_Efficient_Robotics"},{"title":"Alkatt/smolvla-libero-100000 · Hugging Face","url":"https://huggingface.co/Alkatt/smolvla-libero-100000"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"}]

I've found search results related to the SmolVLA paper (arxiv 2506.01844). The search results include information about the paper and its evaluation on LIBERO benchmarks. However, the specific training configuration details you mentioned (batch size 64 and 100000 steps) are not prominently featured in these initial results.

From the search results, I can see:

1. Sm
…[truncated 931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T11:53:56.962827+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA arxiv \"batch size\" \"64\" LIBERO \"100,000\" OR \"100000\" OR \"100k\" steps fine-tuning hyperparameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA arxiv \"batch size\" \"64\" LIBERO \"100,000\" OR \"100000\" OR \"100k\" steps fine-tuning hyperparameters"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T11:53:56.962950+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lerobot docs smolvla LIBERO fine-tuning command batch_size 64 steps 100000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lerobot docs smolvla LIBERO fine-tuning command batch_size 64 steps 100000"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T11:53:56.963099+00:00_

Web search results for query: "SmolVLA arxiv "batch size" "64" LIBERO "100,000" OR "100000" OR "100k" steps fine-tuning hyperparameters"

Links: [{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/smolvla"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"VLA-0-Smol","url":"https://robot-learning-collective.github.io/vla-0-smol"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics [Quick Review]","url":"https://liner.com/review/smolvla-visionlanguageaction-model-for-affordable-and-efficient-robotics"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"SmolVLA - ArXivIQ","url":"https://arxiviq.substack.com/p/smolvla"}]

Perfect! I found the exact information you were looking for. Here are the key findings from the SmolVLA arXiv paper:

For fine-tuning on simulation benchmarks, SmolVLA trains for 100,000 steps with a batch size of 64, while for real-world tasks, it fine-tunes for 200,000 steps.

SmolVLA is evaluated in the LIBERO benchmark, which assesses diverse visuomotor skills across four categories–Spatial, Object, Goal, and 
…[truncated 384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T11:53:56.963319+00:00_

Web search results for query: "lerobot docs smolvla LIBERO fine-tuning command batch_size 64 steps 100000"

Links: [{"title":"SmolVLA · Hugging Face","url":"https://huggingface.co/docs/lerobot/smolvla"},{"title":"lerobot/docs/source/smolvla.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/smolvla.mdx"},{"title":"Inquiry about Training Configurations (Batch Size, LR, Commit Hash) for Replicating SmolVLA on LIBERO Benchmark · Issue #3287 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/3287"},{"title":"fine tune SmolVLA in libero with tensor shape mismatch · Issue #2418 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2418"},{"title":"Train SmolVLA","url":"https://docs.phospho.ai/learn/train-smolvla"},{"title":"SmolVLA fine-tuning | EmbodiFlow","url":"https://io-ai.tech/platform/en/guides/Pipeline/LeRobot/SmolVLA/"},{"title":"Fine Tuning SmolVLA for New Environments (Code included!) | by Xavier O'Keefe | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/fine-tuning-smolvla-for-new-environments-code-included-af266c56d632"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"lerobot/docs/source/peft_training.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/peft_training.mdx"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"}]

Based on the search results, I found relevant documentation about SmolVLA fine-tuning with LeRobot on LIBERO. Here are the key findings:

## SmolVLA Fine-tuning with LIBERO

A basic example fine-tuning command uses `lerobot-train` with parameters like `--policy.path=lerobot/smolvla_base`, `--batch_size=64`, and `--steps=20000`.

For LIBERO-specific fine-tuning, there's a training command that uses `--policy.type=smolvla`, `--dataset.repo_id=HuggingFaceVLA/libero`, `--env.type=libero`, `--env.task=libero_
…[truncated 878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-18T11:53:56.963532+00:00_

## 结果

### 官方 LIBERO finetuned checkpoint: **存在**

| 项目 | 值 |
|---|---|
| **Model ID** | `HuggingFaceVLA/smolvla_libero` |
| **Size** | ~1.22 GB |
| **Base model** | `lerobot/smolvla_base` |
| **论文报告训练配置** | batch_size=64, 100K steps, 只训练 action expert，VLM frozen |
| **论文报告 SR** | Spatial 90%, Object 96%, Goal 92%, Long 71%, **平均 87.3%** |
| **旧版 (deprecated)** | `HuggingFaceVLA/smolvla_libero_ckpts` → 已指向上面的新版 |

### 重要警告：复现问题

社区有多个 issue 报告无法复现 87.3%：
- [#1369](https://github.com/huggingface/lerobot/issues/1369) — 从头训练无法复现
- [#2354](https://github.com/huggingface/lerobot/issues/2354) — 无法复现 benchmark 结果
- [#3264](https://github.com/huggingface/lerobot/issues/3264) — **用官方 checkpoint eval 也无法复现**
- [#3287](https://github.com/huggingface/lerobot/issues/3287) — 询问精确训练配置（batch size, LR, commit hash）

这意味着：
1. 官方 checkpoint 存在且可下载，但用它直接 eval 可能因 lerobot 版本/eval 协议差异拿不到 87.3%
2. 论文的 87.3% 可能依赖特定 lerobot commit 和 eval 设置

### 对我们项目的影响

可以直接下载 `HuggingFaceVLA/smolvla_libero` 做 pruning 实验。即使 eval SR 不到 87.3%，只要比我们 batch_size=4 的 44.8% baseline 显著更高，就足以验证 cliff-edge 在强 baseline 上的存在。关键是要用**同一 eval 流程**对比 pruned vs unpruned，保证内部一致性。

Sources:
- [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)
- [SmolVLA paper (arXiv:2506.01844)](https://arxiv.org/abs/2506.01844)
- [Issue #3287 - Training config inquiry](https://github.com/huggingface/lerobot/issues/3287)
- [Issue #3264 - Cannot reproduce with official checkpoints](https://github.com/huggingface/lerobot/issues/3264)
- [HuggingFaceVLA/smolvla_libero_ckpts (deprecated)](https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts)
- [SmolVLA docs](https://huggingface.co/docs/lerobot/smolvla)
- [LIBERO Leaderboard](https://huggingface.co/spaces/HuggingFaceVLA/libero-vla-leaderboard)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_smolvla_official_checkpoint_20260518T115208"
}
```

</details>

---
