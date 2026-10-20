# Research conversation: Search the web for the paper "Rethinking Visual-Language-Action Model Scaling" by Wang et al., arXiv 2602.09722 (Februar

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ab2ec437f181d01e4.jsonl`
- **Structured JSON:** [`ccc099322a6b3e2cc5e9.json`](../../sessions/cc/ccc099322a6b3e2cc5e9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-13T04:57:46.990Z_

Search the web for the paper "Rethinking Visual-Language-Action Model Scaling" by Wang et al., arXiv 2602.09722 (February 2026). I need to verify:
1. Does this paper actually exist?
2. Did they test visual/sensory dropout during VLA pretraining?
3. What were the exact results (the idea claims 84.5% with dropout vs 85.6% without)?
4. Did they conclude that "natural diversity of the pre-training corpus already serves as an effective regularizer"?
5. Was the dropout uniform random at p=0.2?

Use WebSearch with queries like:
- "Rethinking Visual-Language-Action Model Scaling arXiv 2602.09722"
- "Wang et al 2026 VLA scaling sensory dropout"
- "visual dropout VLA pretraining harmful"

Then use WebFetch to read the actual paper abstract/content if you find it. Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ab2ec437f181d01e4",
  "type": "user",
  "uuid": "4ee12adb-f4fe-483e-95f9-cf20d0d9cfd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T04:57:46.994Z_

```json
{
  "parentUuid": "4ee12adb-f4fe-483e-95f9-cf20d0d9cfd1",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b6624917-3653-4f1f-90ae-7e940b252c11",
  "timestamp": "2026-05-13T04:57:46.994Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T04:57:49.708Z_



I'll search for this paper using multiple queries. Let me first load the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6624917-3653-4f1f-90ae-7e940b252c11",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyY5U197PkebwJRGyNV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6e1d78b-83c4-42d1-8665-3e4f5d164a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012hX1NBJCHaFA6PjZdUATmP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8055,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8055,
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

_source line 4 · 2026-05-13T04:57:49.995Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TbFBCjznHzEBpiKZec5Q8j`</summary>

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
  "parentUuid": "e6e1d78b-83c4-42d1-8665-3e4f5d164a8e",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyY5U197PkebwJRGyNV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d44c36b9-3162-4700-aa80-eea85b4cb869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012hX1NBJCHaFA6PjZdUATmP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8055,
      "cache_read_input_tokens": 0,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8055
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8055,
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

_source line 5 · 2026-05-13T04:57:49.999Z_

<details><summary>↩ Tool result · `toolu_01TbFBCjznHzEBpiKZec5Q8j`</summary>

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
  "parentUuid": "d44c36b9-3162-4700-aa80-eea85b4cb869",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ab2ec437f181d01e4",
  "type": "user",
  "uuid": "a9ab485e-21e6-45f3-a863-52a56f66f14f",
  "sourceToolAssistantUUID": "d44c36b9-3162-4700-aa80-eea85b4cb869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T04:57:58.269Z_



Now let me run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9ab485e-21e6-45f3-a863-52a56f66f14f",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyYJjxjqZocUiGELRPt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4fab6f0-f62a-4bac-ad74-e526731fe5b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtDwNi5angScefd8xSBKKV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-13T04:57:59.445Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HbUfrrYfY4Twniu54Q3sYu`</summary>

```json
{
  "query": "Rethinking Visual-Language-Action Model Scaling arXiv 2602.09722"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4fab6f0-f62a-4bac-ad74-e526731fe5b7",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyYJjxjqZocUiGELRPt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f36c69b3-53df-41e2-b70b-a6978c9ed2b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtDwNi5angScefd8xSBKKV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-13T04:57:59.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NXrehCd537P6iQMdjnataC`</summary>

```json
{
  "query": "Wang et al 2026 VLA scaling sensory dropout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f36c69b3-53df-41e2-b70b-a6978c9ed2b7",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyYJjxjqZocUiGELRPt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2717069e-26de-4b00-9fd5-35f03dc2289a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtDwNi5angScefd8xSBKKV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 9 · 2026-05-13T04:58:00.371Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019PGmPh35qmY42ZPp58uKd5`</summary>

```json
{
  "query": "visual dropout VLA pretraining harmful 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2717069e-26de-4b00-9fd5-35f03dc2289a",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyYJjxjqZocUiGELRPt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ebb40d7-2aeb-4152-8e08-3ba2021e9f78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtDwNi5angScefd8xSBKKV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8055,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 175,
          "cache_read_input_tokens": 8055,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 10 · 2026-05-13T04:58:06.034Z_

<details><summary>↩ Tool result · `toolu_019PGmPh35qmY42ZPp58uKd5`</summary>

```text
Web search results for query: "visual dropout VLA pretraining harmful 2026"

Links: [{"title":"Alignment, Mixture, and Regularization - BeingBeyond","url":"https://research.beingbeyond.com/rethink_vla"},{"title":"Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.15618"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models","url":"https://arxiv.org/html/2604.03956v2"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models [Quick Review]","url":"https://liner.com/review/cotvla-visual-chainofthought-reasoning-for-visionlanguageaction-models"},{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.28740"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse","url":"https://arxiv.org/html/2503.16365v1"},{"title":"GitHub - BeingBeyond/JALA: Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild (CVPR 2026) · GitHub","url":"https://github.com/BeingBeyond/JALA"}]

Based on the search results, I found relevant information about visual dropout in VLA (Vision-Language-Action) pretraining. Here are the key findings:

Stochastic modality dropout does not consistently improve performance, and disabling visual dropout was examined in recent VLA research. More specifically, intuitive strategies, such as sensory dropout and multi-stage fine-tuning, do not consistently improve performance at scale in Vision-Language-Action models.

The research from 2026 suggests that limited benefit is found with stochastic modality dropout, indicating that visual dropout during pretraining is not as beneficial as commonly assumed for VLA models. This finding comes from a systematic study by Wang et al. (2026) that examined core training choices for VLA pretraining across diverse robots.

Additionally, the research challenges broader assumptions about training VLA models, noting that future VLA research must move beyond simple data accumulation and focus on addressing the interference caused by embodiment heterogeneity, suggesting that improvements in VLA training involve more nuanced considerations than traditional regularization techniques like dropout.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ebb40d7-2aeb-4152-8e08-3ba2021e9f78",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ab2ec437f181d01e4",
  "type": "user",
  "uuid": "d73f9511-135b-453b-8431-6195e8d0813d",
  "sourceToolAssistantUUID": "9ebb40d7-2aeb-4152-8e08-3ba2021e9f78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T04:58:07.640Z_

<details><summary>↩ Tool result · `toolu_01HbUfrrYfY4Twniu54Q3sYu`</summary>

```text
Web search results for query: "Rethinking Visual-Language-Action Model Scaling arXiv 2602.09722"

Links: [{"title":"Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization","url":"https://arxiv.org/html/2602.09722"},{"title":"[2602.09722] Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization","url":"https://arxiv.org/abs/2602.09722"},{"title":"Rethinking Visual-Language-Action Model Scaling:","url":"https://arxiv.org/pdf/2602.09722"},{"title":"An Anatomy of Vision-Language-Action Models: From Modules to Milestones and Challenges","url":"https://arxiv.org/html/2512.11362v3"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual-Language-Action+(VLA)+models"},{"title":"[2602.22663] Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline","url":"https://arxiv.org/abs/2602.22663"},{"title":"QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.20309"},{"title":": A Vision-Language-Action Model Bridging Understanding and Generation to Actions","url":"https://arxiv.org/html/2509.06951"},{"title":"Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline","url":"https://arxiv.org/html/2602.22663"},{"title":"[2505.04769] Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/abs/2505.04769"}]

I found the paper! Here's the information about **"Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization"** (arXiv 2602.09722):

## Overview
The paper addresses whether the standard "scale data" recipe translates to robotics, where training data is inherently heterogeneous across embodiments, sensors, and action spaces.

## Research Approach
The authors present a systematic, controlled study of VLA scaling that revisits core training choices for pretraining across diverse robots, using a representative VLA framework that combines a vision-language backbone with flow-matching. To improve the reliability of real-world results, they introduce a Grouped Blind Ensemble protocol that blinds operators to model identity and separates policy execution from outcome judgment, reducing experimenter bias.

## Key Findings
The analysis targets three dimensions of VLA scaling: (1) Physical alignment—showing that a unified end-effector (EEF)-relative action representation is critical for robust cross-embodiment transfer; (2) Embodiment mixture—finding that naively pooling heterogeneous robot datasets often induces negative transfer rather than gains; and (3) Training regularization—observing that intuitive strategies, such as sensory dropout and multi-stage fine-tuning, do not consistently improve performance at scale.

Together, this study challenges some common assumptions about embodied scaling and provides practical guidance for training large-scale VLA policies from diverse robotic data.

The paper was submitted on February 10, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f36c69b3-53df-41e2-b70b-a6978c9ed2b7",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ab2ec437f181d01e4",
  "type": "user",
  "uuid": "1e286842-6754-4536-9783-1bb4cb83a0a8",
  "sourceToolAssistantUUID": "f36c69b3-53df-41e2-b70b-a6978c9ed2b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T04:58:07.692Z_

<details><summary>↩ Tool result · `toolu_01NXrehCd537P6iQMdjnataC`</summary>

```text
Web search results for query: "Wang et al 2026 VLA scaling sensory dropout"

Links: [{"title":"Alignment, Mixture, and Regularization - BeingBeyond","url":"https://research.beingbeyond.com/rethink_vla"},{"title":"VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models","url":"https://arxiv.org/html/2604.03956v2"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/html/2603.22760"},{"title":"[Paper Notes] EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data (arXiv 2026) - Lixin Xu","url":"https://davidlxu.github.io/posts/2026/02/egoscale-paper-notes/"},{"title":"Deciphering neuronal variability across states reveals dynamic sensory encoding | Nature Communications","url":"https://www.nature.com/articles/s41467-025-56733-w"},{"title":"AAAI2026","url":"https://hongsong-wang.github.io/AAAI2026_Abstract/"},{"title":"Multisensory VLA Model Architecture","url":"https://www.emergentmind.com/topics/multisensory-vision-language-action-vla-model-architecture"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision–Language–Action Models via Latent Iterative Reasoning","url":"https://arxiv.org/html/2602.07845"},{"title":"[2509.09372] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model","url":"https://arxiv.org/abs/2509.09372"}]

I found a highly relevant paper! Based on the search results, I can provide you with information about the Wang et al. 2026 paper on VLA scaling:

The paper is titled "Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization" by Wang, Ye and colleagues (arXiv:2602.09722, 2026).

## Key Findings on Sensory Dropout

The study observes that intuitive strategies, such as sensory dropout and multi-stage fine-tuning, do not consistently improve performance at scale. More specifically:

- Stochastic modality dropout does not consistently improve performance.

- Direct end-to-end fine-tuning of the full model reached the best average success (85.8%), indicating that the action expert quickly co-adapts with the VLM backbone.

## Overall Research Focus

The paper presents a systematic, controlled study of VLA scaling that revisits core training choices for pre-training across diverse robots, using a representative VLA framework that combines a vision-language backbone with flow-matching, and ablates key design decisions under matched conditions.

The research challenges common assumptions about scaling Vision-Language-Action models with heterogeneous robotic data and focuses on three key dimensions: physical alignment, embodiment mixture, and training regularization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2717069e-26de-4b00-9fd5-35f03dc2289a",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ab2ec437f181d01e4",
  "type": "user",
  "uuid": "00201d51-cb71-4797-97e1-15f35031d76d",
  "sourceToolAssistantUUID": "2717069e-26de-4b00-9fd5-35f03dc2289a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-13T04:58:13.871Z_

The paper exists. Let me now fetch the actual paper content to verify the specific claims about dropout rates, exact numbers, and the quoted conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00201d51-cb71-4797-97e1-15f35031d76d",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyZbtsA7yhBFiLXVHNq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a2cbfd2-e7ac-4de4-af12-a7291e794ab0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Shhh12WyaTo4dXGaAHncP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1877,
      "cache_read_input_tokens": 9968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1877,
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

_source line 14 · 2026-05-13T04:58:16.910Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018wUWhjLG9aJCXZmbuqLjBf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.09722",
  "prompt": "Extract the full abstract and any details about: (1) sensory/visual dropout experiments, (2) specific success rate numbers with and without dropout, (3) the dropout probability used (was it p=0.2?), (4) any statement about \"natural diversity of the pre-training corpus already serves as an effective regularizer\", (5) author list. Include all exact numbers and quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a2cbfd2-e7ac-4de4-af12-a7291e794ab0",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyZbtsA7yhBFiLXVHNq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0f243fb-fbcb-4fd0-be76-88ba073f70d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Shhh12WyaTo4dXGaAHncP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1877,
      "cache_read_input_tokens": 9968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1877,
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

_source line 15 · 2026-05-13T04:58:19.857Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EjqhV19bC2vCh2CkJpkTN1`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.09722",
  "prompt": "Find and extract all details about: (1) sensory dropout or visual dropout experiments, (2) exact success rate percentages comparing dropout vs no dropout (looking for numbers like 84.5% and 85.6%), (3) the dropout probability p value used (was it p=0.2 or something else?), (4) any quote about \"natural diversity of the pre-training corpus already serves as an effective regularizer\", (5) any table or results showing dropout ablation results. Include all exact numbers, table data, and direct quotes from the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0f243fb-fbcb-4fd0-be76-88ba073f70d1",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyZbtsA7yhBFiLXVHNq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9c27615-9410-41c4-a02f-ba936906dc47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Shhh12WyaTo4dXGaAHncP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1877,
      "cache_read_input_tokens": 9968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1877,
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

_source line 16 · 2026-05-13T04:58:21.371Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NQJU8EJwrfcfueV1wuYvjt`</summary>

```json
{
  "url": "https://research.beingbeyond.com/rethink_vla",
  "prompt": "Find all details about: (1) sensory dropout experiments and results, (2) exact success rate numbers with and without dropout, (3) what dropout probability was used, (4) any statement about natural diversity serving as regularizer, (5) any tables showing dropout ablation results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9c27615-9410-41c4-a02f-ba936906dc47",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyZbtsA7yhBFiLXVHNq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5776e945-1c20-418c-ad7c-8a8776bfd773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Shhh12WyaTo4dXGaAHncP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1877,
      "cache_read_input_tokens": 9968,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 849,
          "output_tokens": 508,
          "cache_read_input_tokens": 9968,
          "cache_creation_input_tokens": 1877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1877,
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

_source line 17 · 2026-05-13T04:58:25.107Z_

<details><summary>↩ Tool result · `toolu_018wUWhjLG9aJCXZmbuqLjBf`</summary>

```text
# Paper Details from arXiv:2602.09722

## Full Abstract
"While Vision-Language-Action (VLA) models show strong promise for generalist robot control, it remains unclear whether -- and under what conditions -- the standard 'scale data' recipe translates to robotics, where training data is inherently heterogeneous across embodiments, sensors, and action spaces. We present a systematic, controlled study of VLA scaling that revisits core training choices for pretraining across diverse robots. Using a representative VLA framework that combines a vision-language backbone with flow-matching, we ablate key design decisions under matched conditions and evaluate in extensive simulation and real-robot experiments. To improve the reliability of real-world results, we introduce a Grouped Blind Ensemble protocol that blinds operators to model identity and separates policy execution from outcome judgment, reducing experimenter bias. Our analysis targets three dimensions of VLA scaling. (1) Physical alignment: we show that a unified end-effector (EEF)-relative action representation is critical for robust cross-embodiment transfer. (2) Embodiment mixture: we find that naively pooling heterogeneous robot datasets often induces negative transfer rather than gains, underscoring the fragility of indiscriminate data scaling. (3) Training regularization: we observe that intuitive strategies, such as sensory dropout and multi-stage fine-tuning, do not consistently improve performance at scale."

## Specific Findings

**(1) & (2) Sensory Dropout & Success Rates:**
The abstract mentions "sensory dropout" as a training regularization strategy but notes it "do not consistently improve performance at scale." The page content provides no specific success rate numbers or dropout probability values.

**(3) Dropout Probability:**
No dropout probability (p=0.2 or otherwise) is specified in the provided content.

**(4) Natural Diversity Quote:**
This statement does not appear in the accessible page content.

**(5) Authors:**
Ye Wang, Sipeng Zheng, Hao Luo, Wanpeng Zhang, Haoqi Yuan, Chaoyi Xu, Haiweng Xu, Yicheng Feng, Mingyang Yu, Zhiyu Kang, Zongqing Lu, Qin Jin
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0f243fb-fbcb-4fd0-be76-88ba073f70d1",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ab2ec437f181d01e4",
  "type": "user",
  "uuid": "d39691d7-bb25-40c1-be6c-83979ced8124",
  "sourceToolAssistantUUID": "f0f243fb-fbcb-4fd0-be76-88ba073f70d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T04:58:25.561Z_

<details><summary>↩ Tool result · `toolu_01EjqhV19bC2vCh2CkJpkTN1`</summary>

```text
# Sensory Dropout and Visual Dropout Experiments

## Dropout Configuration
The paper uses **p=0.2** for both proprioceptive state masking and visual view dropout during pretraining. As stated: "we first mask proprioception by zeroing the input proprioceptive vector with probability p=0.2" and "apply independent dropping of each camera view with p=0.2."

## Table V Results - Ablation Study

Table V presents the key dropout ablation results on LIBERO 5-shot benchmark:

| State Mask | View Mask | Schedule | Avg Success (%) |
|-----------|-----------|----------|-----------------|
| 0.2 | 0.2 | 2-Stage | **84.5%** |
| 0 | 0.2 | 2-Stage | 85.2% |
| 0.5 | 0.2 | 2-Stage | 84.0% |
| 0.2 | 0 | 2-Stage | 85.6% |
| 0.2 | 0.5 | 2-Stage | 84.5% |
| 0.2 | 0.2 | Stage 2 Only | **85.8%** |

## Key Finding on Natural Diversity

The paper states: "the natural diversity of the pre-training corpus already serves as an effective regularizer, making additional noise injection unnecessary, or even harmful."

## Conclusion on Regularization

Disabling visual dropout (p_view=0) improved performance to 85.6% versus the baseline 84.5%, suggesting dropout provides limited benefit at scale.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9c27615-9410-41c4-a02f-ba936906dc47",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ab2ec437f181d01e4",
  "type": "user",
  "uuid": "906da818-8e50-4fad-b2ed-b2070adc3329",
  "sourceToolAssistantUUID": "e9c27615-9410-41c4-a02f-ba936906dc47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T04:58:26.330Z_

<details><summary>↩ Tool result · `toolu_01NQJU8EJwrfcfueV1wuYvjt`</summary>

```text
# Sensory Dropout Experiments & Results

## Dropout Details
The research evaluated sensory dropout through stochastic masking of visual and proprioceptive inputs. Table VI presents the ablation results with specific dropout configurations tested.

## Success Rates
According to Table VI (Training Dynamics and Strategies):
- **With balanced dropout** (state mask 0.2, view mask 0.2): 84.5% average success
- **Without visual dropout** (state mask 0, view mask 0.2): 85.2% average success  
- **No view dropout** (state mask 0.2, view mask 0): **85.6% average success** (highest)

## Key Finding
The authors concluded: *"Stochastic modality dropout does not consistently improve performance. Disabling visual dropout actually achieved higher success (85.6%) than the balanced baseline."*

## Dropout Probability
The document specifies dropout rates of **0.2, 0.5, and 0** for both state and view masking across different experimental conditions, but does not discuss natural diversity as a regularization mechanism.

## Notable Insight
The results suggest that simpler training approaches outperformed regularization strategies, as *"Direct end-to-end fine-tuning of the full model reached the best average success (85.8%)"* without requiring dropout-based regularization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5776e945-1c20-418c-ad7c-8a8776bfd773",
  "isSidechain": true,
  "promptId": "cf0ab368-1b89-47a1-b44c-6f8cb6a5b762",
  "agentId": "ab2ec437f181d01e4",
  "type": "user",
  "uuid": "de2a8438-cfd4-4615-98bf-ef79cc0e1f04",
  "sourceToolAssistantUUID": "5776e945-1c20-418c-ad7c-8a8776bfd773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-13T04:58:50.095Z_

I now have all the details needed. Here is the full report.

---

**The paper does exist.** It is:

**"Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization"**
arXiv: 2602.09722, submitted February 10, 2026.
Authors: Ye Wang, Sipeng Zheng, Hao Luo, Wanpeng Zhang, Haoqi Yuan, Chaoyi Xu, Haiweng Xu, Yicheng Feng, Mingyang Yu, Zhiyu Kang, Zongqing Lu, Qin Jin.

---

**Answers to your five questions:**

**1. Does the paper exist?**
Yes, confirmed on arXiv (2602.09722) and a companion project page at research.beingbeyond.com.

**2. Did they test visual/sensory dropout during VLA pretraining?**
Yes. They ablated both proprioceptive state masking and visual view dropout during pretraining, testing probabilities of 0, 0.2, and 0.5 for each.

**3. What were the exact results?**
From their Table V (LIBERO 5-shot benchmark):

| State Mask | View Mask | Avg Success |
|---|---|---|
| 0.2 | 0.2 | **84.5%** |
| 0 | 0.2 | 85.2% |
| 0.5 | 0.2 | 84.0% |
| 0.2 | 0 | **85.6%** |
| 0.2 | 0.5 | 84.5% |
| 0.2 | 0.2 (Stage 2 only) | 85.8% |

The specific claim you asked about -- **84.5% with dropout vs 85.6% without** -- is correct. The 84.5% is the baseline with both state and view dropout at p=0.2, and 85.6% is achieved when view (visual) dropout is disabled (p_view=0) while keeping state mask at 0.2. Disabling visual dropout *improved* performance.

**4. Did they conclude that "natural diversity of the pre-training corpus already serves as an effective regularizer"?**
Yes, this is a direct quote from the paper. The full statement is: *"the natural diversity of the pre-training corpus already serves as an effective regularizer, making additional noise injection unnecessary, or even harmful."*

**5. Was the dropout uniform random at p=0.2?**
Yes. They describe it as: masking proprioception by zeroing the input proprioceptive vector with probability p=0.2, and independently dropping each camera view with p=0.2. This is uniform random dropout at p=0.2.

---

**Summary:** All five claims you asked about are verified as accurate. The paper exists, the numbers match (84.5% with dropout, 85.6% without), the dropout was uniform random at p=0.2, and the quoted conclusion about natural diversity as a regularizer is a direct quote from the paper.

Sources:
- [arXiv Abstract - 2602.09722](https://arxiv.org/abs/2602.09722)
- [arXiv HTML - 2602.09722](https://arxiv.org/html/2602.09722)
- [BeingBeyond Project Page](https://research.beingbeyond.com/rethink_vla)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de2a8438-cfd4-4615-98bf-ef79cc0e1f04",
  "isSidechain": true,
  "agentId": "ab2ec437f181d01e4",
  "requestId": "req_011CayyayWQgAsSqyy58feUN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee5984a8-b874-4d73-acc3-30751ebf46cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c97a7968-cb28-460a-9fc5-2ece39bd49ab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrHU2cz5EXCfwgAkqRUw8t",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2747,
      "cache_read_input_tokens": 11845,
      "output_tokens": 847,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2747
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 847,
          "cache_read_input_tokens": 11845,
          "cache_creation_input_tokens": 2747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2747,
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
