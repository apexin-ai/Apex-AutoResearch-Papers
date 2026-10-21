# research grids mechanism analysis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_research_grids_mechanism_analysis_20260519T034002.log`
- **Structured JSON:** [`84c91ba7f05f1a188cd1.json`](../../sessions/84/84c91ba7f05f1a188cd1.json)

## Before a recorded user message

28 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "ae0a4619-7493-43b2-80fe-9015cfa4f21f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779179400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9aaccacf-2c12-448e-923f-0802841d38c6",
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8"
}
```

---

### Assistant

_source line 4_

I'll search for the paper and analyze it in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "08e99c29-d680-4a74-a71c-00fb1cee9f44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7wiPUkK5xFww9nyNLgKDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12921,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12921
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CPRbWEPXnfRyGnTUGxfhcR`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "d0d27794-5a1a-4326-8765-496ec48faf77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S7wiPUkK5xFww9nyNLgKDK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12921,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12921
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T03:40:15.125Z_

<details><summary>↩ Tool result · `toolu_01CPRbWEPXnfRyGnTUGxfhcR`</summary>

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "f087c6a8-35d0-48be-afc9-727f184bba5d",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the paper and then fetch its content to analyze it in detail.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "5aadc2a1-dbe5-4c90-bc76-b7d92e6e4afc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4P6bVcvdheah8kade8rZp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 24762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 8_

Starting the search. Let me fetch the paper from multiple angles in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "173e1357-ce2e-44dd-8c95-69a21b3222ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4P6bVcvdheah8kade8rZp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 24762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017LGuJ8kd1zJTnxxgYywLS7`</summary>

```json
{
  "query": "See What Matters Differentiable Grid Sample Pruning VLA arXiv 2605.11817"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "0351ef09-ab20-4ac7-b3e6-a27064e6f7e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4P6bVcvdheah8kade8rZp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 24762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015W9mh8GnqR8Fz1f7Z1byc9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.11817",
  "prompt": "Extract the full abstract, list of authors, and any information about the paper's contributions. Also note if it mentions pixel shuffle, space-to-depth, token entanglement, architecture-dependent compression, SmolVLA, or cross-architecture comparison."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "ba431816-eb9b-467c-b628-6acb9863ab9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4P6bVcvdheah8kade8rZp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 24762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HaAmTQLpkbcXSWNiPeZGyJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.11817",
  "prompt": "Extract the FULL text of the following sections as completely as possible:\n1. Introduction (complete text)\n2. Method/Approach section (complete text)\n3. Any section discussing WHY token pruning fails or WHY grid-based methods are better\n4. Any mention of: pixel shuffle, space-to-depth, token entanglement, spatial mixing, cliff-edge, catastrophic failure, architecture-dependent, connector type, MLP projection, cross-attention\n5. Any experiments on SmolVLA - what benchmarks were used (LIBERO? real robot?), did they observe 0% success rate with pruning?\n6. Related Work section - how do they position against prior token compression methods?\n\nBe as thorough and complete as possible. Include exact quotes where relevant."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "2e7a0b12-96af-4165-b557-ccf837af571e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4P6bVcvdheah8kade8rZp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 24762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1113
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:40:25.397Z_

<details><summary>↩ Tool result · `toolu_017LGuJ8kd1zJTnxxgYywLS7`</summary>

```text
Web search results for query: "See What Matters Differentiable Grid Sample Pruning VLA arXiv 2605.11817"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"}]

Based on the search results, I found information about the paper you're looking for:

"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA.

Vision-Language-Action (VLA) models have shown remarkable promise in robotics manipulation, yet their high computational cost hinders real-time deployment. Existing token pruning methods suffer from a fundamental trade-off where aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation.

By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression.

The paper was featured as an ICML 2026 poster presentation, indicating it's a recent contribution to the field of efficient vision-language-action models for robotics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "48f51b81-cfac-4e2c-a371-b3fa93724ed0",
  "tool_use_result": {
    "query": "See What Matters Differentiable Grid Sample Pruning VLA arXiv 2605.11817",
    "results": [
      {
        "tool_use_id": "srvtoolu_015ED1UXraHX9T7tEMxUvtCV",
        "content": [
          {
            "title": "ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model",
            "url": "https://icml.cc/virtual/2026/poster/65010"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/pdf/2509.12594"
          },
          {
            "title": "[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/abs/2509.12594"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/pdf/2511.16449"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\n\"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA.\n\nVision-Language-Action (VLA) models have shown remarkable promise in robotics manipulation, yet their high computational cost hinders real-time deployment. Existing token pruning methods suffer from a fundamental trade-off where aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation.\n\nBy adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression.\n\nThe paper was featured as an ICML 2026 poster presentation, indicating it's a recent contribution to the field of efficient vision-language-action models for robotics."
    ],
    "durationSeconds": 5.6223403450000005
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T03:40:30.774Z_

<details><summary>↩ Tool result · `toolu_015W9mh8GnqR8Fz1f7Z1byc9`</summary>

```text
# Paper Summary

**Title:** See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model

**ArXiv ID:** 2605.11817

## Authors
Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu

## Abstract
The paper addresses computational efficiency in Vision-Language-Action models for robotics. The researchers propose that "breaking this trade-off requires rethinking compression as a geometry-aware, continuous token resampling in the vision encoder." They introduce GridS (Differentiable Grid Sampler), which "performs task-aware, continuous resampling of visual tokens" while preserving spatial information critical for manipulation tasks like contact points.

## Key Contributions
- A plug-and-play module enabling adaptive, salient coordinate prediction with differentiable interpolation
- Achieves "76% reduction in FLOPs with no degradation in the success rate"
- Uses "fewer than 10% original visual tokens" while maintaining performance
- Validation on LIBERO benchmark and real robotic platforms

## Notable Omissions
The abstract and provided content **do not mention**: pixel shuffle, space-to-depth, token entanglement, architecture-dependent compression, SmolVLA, or cross-architecture comparisons.

Code is available on GitHub at the provided URL.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "9abda152-25f2-4ba0-bdad-ddd6484c4379",
  "tool_use_result": {
    "bytes": 47509,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\n\n**ArXiv ID:** 2605.11817\n\n## Authors\nYixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu\n\n## Abstract\nThe paper addresses computational efficiency in Vision-Language-Action models for robotics. The researchers propose that \"breaking this trade-off requires rethinking compression as a geometry-aware, continuous token resampling in the vision encoder.\" They introduce GridS (Differentiable Grid Sampler), which \"performs task-aware, continuous resampling of visual tokens\" while preserving spatial information critical for manipulation tasks like contact points.\n\n## Key Contributions\n- A plug-and-play module enabling adaptive, salient coordinate prediction with differentiable interpolation\n- Achieves \"76% reduction in FLOPs with no degradation in the success rate\"\n- Uses \"fewer than 10% original visual tokens\" while maintaining performance\n- Validation on LIBERO benchmark and real robotic platforms\n\n## Notable Omissions\nThe abstract and provided content **do not mention**: pixel shuffle, space-to-depth, token entanglement, architecture-dependent compression, SmolVLA, or cross-architecture comparisons.\n\nCode is available on GitHub at the provided URL.",
    "durationMs": 9515,
    "url": "https://arxiv.org/abs/2605.11817"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:40:57.100Z_

<details><summary>↩ Tool result · `toolu_01HaAmTQLpkbcXSWNiPeZGyJ`</summary>

```text
# Analysis of "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

## 1. Introduction (Complete Text)

Vision-Language-Action models (VLAs) integrate semantic reasoning and low-level control into unified architectures, showing strong generalization across manipulation tasks. However, VLAs incur high computational costs due to the massive token volume of the vision encoder. Standard images are projected into 256 tokens in vision encoders, creating a severe bottleneck for subsequent Transformer blocks where computational complexity scales quadratically with input sequence length.

Recent research has investigated visual token pruning through two approaches: semantic pruning (prioritizing salient object bodies while neglecting geometrically critical regions like edges or contact points) and dynamic token pruning (retaining variable token counts per image using training-free, non-differentiable strategies). Both types remain constrained by reliance on discrete selection over fixed grids, introducing quantization errors that lose fine-grained spatial fidelity essential for robotic interaction, where sub-patch precision matters.

The authors propose Differentiable Grid Sampler (GridS), which reformulates VLA token compression from discrete patch-dropping into geometry-aware continuous resampling. GridS dynamically predicts task-driven spatial coordinates and queries the continuous feature map via differentiable bilinear interpolation, achieving drastic compression (fewer than 10% original visual tokens) while preserving essential spatial information. Results demonstrate 76% FLOPs reduction with no success rate degradation, and 28.6% accuracy gain in out-of-distribution scenarios.

## 2. Method/Approach Section (Complete Text)

### 3.1 Efficiency Bottleneck in Standard VLAs

Standard VLA architectures employ frozen Vision Transformers (e.g., SigLIP or DINOv2) encoding input images into dense feature grids. An input image I∈ℝ³×HR×WR is patchified and encoded into T_dense∈ℝH×W×C, where H×W represents patch numbers (DINOv2 generates 16×16=256 tokens). While comprehensive, this dense representation introduces significant redundancy. Since downstream Transformer complexity scales as O(N²), processing hundreds of tokens with most representing non-informative background noise incurs prohibitive computational costs, necessitating a pruning mechanism that discards irrelevant regions while preserving fine-grained details essential for manipulation.

### 3.2 The GridS Pipeline

GridS is a plug-and-play module designed to compress dense features into compact active tokens, divided into two stages: (1) Global Coordinate Prediction, and (2) Grid Sampling with Geometry Injection.

**Global Coordinate Prediction:** Effective active grid sampling requires understanding scene global semantic structure. Rather than processing local patches in isolation, the entire feature map T_dense is aggregated via global average pooling to obtain context vector z∈ℝC. A lightweight MLP then predicts K sets of continuous, normalized coordinates P∈[0,1]K×2 as P=σ(MLP(z)), where σ is the Sigmoid function ensuring coordinates remain within image bounds, with K≪(H×W) representing target active tokens.

**Grid Sampling with Geometry Injection:** Predicted grid points sample from dense tokens (via differentiable bilinear sampling) generating sparse tokens F_spa∈ℝK×C, disrupting original spatial structure. A Coordinate Encoder maps predicted coordinates P into position embeddings E_pos∈ℝK×C, which are added to sampled features forming final Visual Sparse Tokens (T_spa), concatenated with language and action tokens for downstream Transformer.

### 3.3 Differentiable Bilinear Sampling

GridS's core innovation lies in feature extraction from predicted coordinates. Unlike discrete selection strategies suffering quantization errors, it employs Differentiable Bilinear Sampling. Let P(x,y) be a predicted continuous coordinate in feature map space. The sampled token value is weighted interpolation of its four nearest neighbors on the original grid.

Let the top-left neighbor be P₁=(x_i,y_i)=(⌊x⌋,⌊y⌋), with offsets Δx=x-x_i and Δy=y-y_i. Interpolation weights ω_i for four neighbors {P₁,P₂,P₃,P₄} are:

ω₁=(1−Δx)(1−Δy)
ω₂=Δx(1−Δy)
ω₃=(1−Δx)Δy
ω₄=Δx·Δy

The final sampled feature is: F_sampled(x,y)=∑k=1⁴ ωk⋅Pk

This mechanism extracts sub-patch features. For instance, if a grasp point lies on an edge shared by two patches, GridS samples the boundary by assigning balanced weights to neighbors, whereas discrete selection would force choosing just one side.

**Differentiability and Gradient Flow:** The bilinear formulation is fully differentiable with respect to coordinates (x,y), enabling adaptive pruning driven by data. Since weights ω_k are linear functions of x and y, gradients flow back from task loss ℒ to the coordinate predictor: ∂ℒ/∂x=∑k=1⁴(∂ℒ/∂F_sampled)⋅Pk⋅(∂ωk/∂x). This implies the MLP coordinate generator is actively trained by downstream tasks to move sampling points toward regions minimizing action prediction error.

### 3.4 Training Objectives and Joint Optimization

Existing token pruning methods apply post-training (described as training-free). Rather than an advantage, this "training-free" property represents a forced compromise due to non-differentiable designs, inevitably degrading downstream performance. GridS integrates directly between vision encoder and transformer, jointly optimized with VLA policy during standard fine-tuning. It trains end-to-end using only primary task loss—without auxiliary supervision or ground-truth attention maps—seamlessly compatible with diverse paradigms (auto-regressive and flow-matching models). Since downstream fine-tuning is already a prerequisite for VLAs, GridS introduces no extra pipeline steps. By heavily compressing visual tokens early in forward pass, it significantly reduces computational footprint and accelerates training.

## 3. Why Token Pruning Fails / Why GridS is Better

The paper identifies fundamental flaws in existing approaches:

**Limitation of Semantic Pruning:** "These methods often prioritize salient object bodies while neglecting geometrically critical but semantically subtle regions, e.g. edges or contact points."

**Limitation of Dynamic Token Pruning:** "These methods adopt training-free strategies that are inherently non-differentiable, functioning as static heuristics derived from pre-existing policies. Consequently, they fail to align with specific application requirements, leading to varying degrees of degradation in task success rates."

**Fundamental Grid Constraint:** "Both types of methods are constrained by their reliance on discrete selection over a fixed grid. However, robotic interaction often requires sub-patch precision (as Fig. 2 (a), a grasp point is located between two patches). Restricting the model to select coarse patches introduces inherent quantization errors and leads to a loss of fine-grained spatial fidelity."

**Trade-off Resolution:** The paper argues that "breaking this performance-efficiency trade-off requires rethinking compression as a geometry-aware, continuous token resampling in the vision encoder."

Evidence of failure: Table 1 shows FastV achieves -1.5% accuracy degradation and SparseVLM achieves -4.6% degradation compared to baseline π₀, while GridS achieves +1.6% improvement.

## 4. Search for Specified Technical Terms

**None of these terms appear in the provided document:**
- pixel shuffle
- space-to-depth
- token entanglement
- spatial mixing
- cliff-edge
- catastrophic failure
- architecture-dependent
- connector type
- cross-attention (mentioned once in context of "SparseVLM leverages training-free cross-modal attention" but not as a GridS component)

## 5. SmolVLA Experiments

**Benchmarks used with SmolVLA:**
- Real-world experiments on SO100 robot arm
- Three tasks: Pick & Place (83 episodes), Transfer Pen (74 episodes), Stack Cubes (75 episodes)
- 21 distinct out-of-distribution scenarios

**Real-world Results (Figure 5c):**
- Pick & Place: Baseline 47.6%, GridS 71.4%
- Transfer Pen: Baseline 54.1%, GridS 70.3%
- Stack Cubes: Baseline 7.6%, GridS 60.0%

The most dramatic observation: "In the challenging Stack Cubes task, GridS achieves a 60.0% success rate compared to the baseline's ∼7.6%, yielding a substantial +52.4% improvement."

Regarding near-zero baseline performance: The paper doesn't explicitly state 0% success rate with token pruning on SmolVLA, but demonstrates severe baseline struggles (7.6% on Stack Cubes), where "the baseline completely fails in the OOD settings."

## 6. Related Work Section Positioning

**Against Semantic Pruning Methods:**
"SparseVLM leverages training-free cross-modal attention to prune tokens, yet this semantic-driven selection inherently biases the model toward salient objects while neglecting geometrically critical but semantically subtle regions."

**Against Dynamic Token Pruning:**
"VLA-Cache exploits temporal redundancy by caching visual features across timesteps, but its reliance on discrete update thresholds over a fixed grid often fails to capture fine-grained geometric deformations during dynamic interaction. EfficientVLA employs a learnable policy to dynamically drop background patches, but the resulting ragged tensors severely degrade hardware throughput due to inefficient memory coalescing."

**Summary of Prior Limitations:**
"These approaches are collectively constrained by their reliance on discrete selection over a fixed grid, introducing inevitable quantization errors that sacrifice the sub-patch spatial fidelity essential for precision control."

**GridS's Positioning:**
Unlike post-training methods, GridS is "jointly optimized with the VLA policy during standard fine-tuning," operates "end-to-end using only the primary task loss," and leverages continuous, differentiable sampling rather than discrete patch dropping.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "e43dc603-6e7f-4fa0-8b51-8704f79fca19",
  "tool_use_result": {
    "bytes": 432339,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\"\n\n## 1. Introduction (Complete Text)\n\nVision-Language-Action models (VLAs) integrate semantic reasoning and low-level control into unified architectures, showing strong generalization across manipulation tasks. However, VLAs incur high computational costs due to the massive token volume of the vision encoder. Standard images are projected into 256 tokens in vision encoders, creating a severe bottleneck for subsequent Transformer blocks where computational complexity scales quadratically with input sequence length.\n\nRecent research has investigated visual token pruning through two approaches: semantic pruning (prioritizing salient object bodies while neglecting geometrically critical regions like edges or contact points) and dynamic token pruning (retaining variable token counts per image using training-free, non-differentiable strategies). Both types remain constrained by reliance on discrete selection over fixed grids, introducing quantization errors that lose fine-grained spatial fidelity essential for robotic interaction, where sub-patch precision matters.\n\nThe authors propose Differentiable Grid Sampler (GridS), which reformulates VLA token compression from discrete patch-dropping into geometry-aware continuous resampling. GridS dynamically predicts task-driven spatial coordinates and queries the continuous feature map via differentiable bilinear interpolation, achieving drastic compression (fewer than 10% original visual tokens) while preserving essential spatial information. Results demonstrate 76% FLOPs reduction with no success rate degradation, and 28.6% accuracy gain in out-of-distribution scenarios.\n\n## 2. Method/Approach Section (Complete Text)\n\n### 3.1 Efficiency Bottleneck in Standard VLAs\n\nStandard VLA architectures employ frozen Vision Transformers (e.g., SigLIP or DINOv2) encoding input images into dense feature grids. An input image I∈ℝ³×HR×WR is patchified and encoded into T_dense∈ℝH×W×C, where H×W represents patch numbers (DINOv2 generates 16×16=256 tokens). While comprehensive, this dense representation introduces significant redundancy. Since downstream Transformer complexity scales as O(N²), processing hundreds of tokens with most representing non-informative background noise incurs prohibitive computational costs, necessitating a pruning mechanism that discards irrelevant regions while preserving fine-grained details essential for manipulation.\n\n### 3.2 The GridS Pipeline\n\nGridS is a plug-and-play module designed to compress dense features into compact active tokens, divided into two stages: (1) Global Coordinate Prediction, and (2) Grid Sampling with Geometry Injection.\n\n**Global Coordinate Prediction:** Effective active grid sampling requires understanding scene global semantic structure. Rather than processing local patches in isolation, the entire feature map T_dense is aggregated via global average pooling to obtain context vector z∈ℝC. A lightweight MLP then predicts K sets of continuous, normalized coordinates P∈[0,1]K×2 as P=σ(MLP(z)), where σ is the Sigmoid function ensuring coordinates remain within image bounds, with K≪(H×W) representing target active tokens.\n\n**Grid Sampling with Geometry Injection:** Predicted grid points sample from dense tokens (via differentiable bilinear sampling) generating sparse tokens F_spa∈ℝK×C, disrupting original spatial structure. A Coordinate Encoder maps predicted coordinates P into position embeddings E_pos∈ℝK×C, which are added to sampled features forming final Visual Sparse Tokens (T_spa), concatenated with language and action tokens for downstream Transformer.\n\n### 3.3 Differentiable Bilinear Sampling\n\nGridS's core innovation lies in feature extraction from predicted coordinates. Unlike discrete selection strategies suffering quantization errors, it employs Differentiable Bilinear Sampling. Let P(x,y) be a predicted continuous coordinate in feature map space. The sampled token value is weighted interpolation of its four nearest neighbors on the original grid.\n\nLet the top-left neighbor be P₁=(x_i,y_i)=(⌊x⌋,⌊y⌋), with offsets Δx=x-x_i and Δy=y-y_i. Interpolation weights ω_i for four neighbors {P₁,P₂,P₃,P₄} are:\n\nω₁=(1−Δx)(1−Δy)\nω₂=Δx(1−Δy)\nω₃=(1−Δx)Δy\nω₄=Δx·Δy\n\nThe final sampled feature is: F_sampled(x,y)=∑k=1⁴ ωk⋅Pk\n\nThis mechanism extracts sub-patch features. For instance, if a grasp point lies on an edge shared by two patches, GridS samples the boundary by assigning balanced weights to neighbors, whereas discrete selection would force choosing just one side.\n\n**Differentiability and Gradient Flow:** The bilinear formulation is fully differentiable with respect to coordinates (x,y), enabling adaptive pruning driven by data. Since weights ω_k are linear functions of x and y, gradients flow back from task loss ℒ to the coordinate predictor: ∂ℒ/∂x=∑k=1⁴(∂ℒ/∂F_sampled)⋅Pk⋅(∂ωk/∂x). This implies the MLP coordinate generator is actively trained by downstream tasks to move sampling points toward regions minimizing action prediction error.\n\n### 3.4 Training Objectives and Joint Optimization\n\nExisting token pruning methods apply post-training (described as training-free). Rather than an advantage, this \"training-free\" property represents a forced compromise due to non-differentiable designs, inevitably degrading downstream performance. GridS integrates directly between vision encoder and transformer, jointly optimized with VLA policy during standard fine-tuning. It trains end-to-end using only primary task loss—without auxiliary supervision or ground-truth attention maps—seamlessly compatible with diverse paradigms (auto-regressive and flow-matching models). Since downstream fine-tuning is already a prerequisite for VLAs, GridS introduces no extra pipeline steps. By heavily compressing visual tokens early in forward pass, it significantly reduces computational footprint and accelerates training.\n\n## 3. Why Token Pruning Fails / Why GridS is Better\n\nThe paper identifies fundamental flaws in existing approaches:\n\n**Limitation of Semantic Pruning:** \"These methods often prioritize salient object bodies while neglecting geometrically critical but semantically subtle regions, e.g. edges or contact points.\"\n\n**Limitation of Dynamic Token Pruning:** \"These methods adopt training-free strategies that are inherently non-differentiable, functioning as static heuristics derived from pre-existing policies. Consequently, they fail to align with specific application requirements, leading to varying degrees of degradation in task success rates.\"\n\n**Fundamental Grid Constraint:** \"Both types of methods are constrained by their reliance on discrete selection over a fixed grid. However, robotic interaction often requires sub-patch precision (as Fig. 2 (a), a grasp point is located between two patches). Restricting the model to select coarse patches introduces inherent quantization errors and leads to a loss of fine-grained spatial fidelity.\"\n\n**Trade-off Resolution:** The paper argues that \"breaking this performance-efficiency trade-off requires rethinking compression as a geometry-aware, continuous token resampling in the vision encoder.\"\n\nEvidence of failure: Table 1 shows FastV achieves -1.5% accuracy degradation and SparseVLM achieves -4.6% degradation compared to baseline π₀, while GridS achieves +1.6% improvement.\n\n## 4. Search for Specified Technical Terms\n\n**None of these terms appear in the provided document:**\n- pixel shuffle\n- space-to-depth\n- token entanglement\n- spatial mixing\n- cliff-edge\n- catastrophic failure\n- architecture-dependent\n- connector type\n- cross-attention (mentioned once in context of \"SparseVLM leverages training-free cross-modal attention\" but not as a GridS component)\n\n## 5. SmolVLA Experiments\n\n**Benchmarks used with SmolVLA:**\n- Real-world experiments on SO100 robot arm\n- Three tasks: Pick & Place (83 episodes), Transfer Pen (74 episodes), Stack Cubes (75 episodes)\n- 21 distinct out-of-distribution scenarios\n\n**Real-world Results (Figure 5c):**\n- Pick & Place: Baseline 47.6%, GridS 71.4%\n- Transfer Pen: Baseline 54.1%, GridS 70.3%\n- Stack Cubes: Baseline 7.6%, GridS 60.0%\n\nThe most dramatic observation: \"In the challenging Stack Cubes task, GridS achieves a 60.0% success rate compared to the baseline's ∼7.6%, yielding a substantial +52.4% improvement.\"\n\nRegarding near-zero baseline performance: The paper doesn't explicitly state 0% success rate with token pruning on SmolVLA, but demonstrates severe baseline struggles (7.6% on Stack Cubes), where \"the baseline completely fails in the OOD settings.\"\n\n## 6. Related Work Section Positioning\n\n**Against Semantic Pruning Methods:**\n\"SparseVLM leverages training-free cross-modal attention to prune tokens, yet this semantic-driven selection inherently biases the model toward salient objects while neglecting geometrically critical but semantically subtle regions.\"\n\n**Against Dynamic Token Pruning:**\n\"VLA-Cache exploits temporal redundancy by caching visual features across timesteps, but its reliance on discrete update thresholds over a fixed grid often fails to capture fine-grained geometric deformations during dynamic interaction. EfficientVLA employs a learnable policy to dynamically drop background patches, but the resulting ragged tensors severely degrade hardware throughput due to inefficient memory coalescing.\"\n\n**Summary of Prior Limitations:**\n\"These approaches are collectively constrained by their reliance on discrete selection over a fixed grid, introducing inevitable quantization errors that sacrifice the sub-patch spatial fidelity essential for precision control.\"\n\n**GridS's Positioning:**\nUnlike post-training methods, GridS is \"jointly optimized with the VLA policy during standard fine-tuning,\" operates \"end-to-end using only the primary task loss,\" and leverages continuous, differentiable sampling rather than discrete patch dropping.",
    "durationMs": 32353,
    "url": "https://arxiv.org/html/2605.11817"
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Excellent, I now have a very thorough picture of the paper. Let me also check if there's any supplementary material or additional sections that might mention pixel-shuffle or architecture-specific analysis. Let me fetch more details about the experiments section, especially any ablation or analysis that might touch on architecture differences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "c6b93cc2-8a5d-4c31-86ff-725c4b3e9ba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yt2y9azwJdMhd4vp1GLbN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3899,
      "cache_read_input_tokens": 25875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3899
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 16_

Got rich content. Let me dig deeper into whether they have any architecture-specific analysis or mention of connector types.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "00160488-1661-42fb-a627-4c6b1ed0066f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yt2y9azwJdMhd4vp1GLbN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3899,
      "cache_read_input_tokens": 25875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3899
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Sj3hhwMWeJEMmUJ1wqogK1`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.11817",
  "prompt": "I need to find specific details NOT covered in my first pass. Please extract:\n\n1. The EXPERIMENTS section completely - especially:\n   - Which VLA models were tested? (OpenVLA? π₀? SmolVLA? others?)\n   - For EACH model, what vision connector does it use? Do they mention MLP projection vs pixel-shuffle vs any other connector?\n   - Table 1 and Table 2 full content - what are the exact numbers for each method on each model?\n   - Any ablation studies\n\n2. Any ANALYSIS or DISCUSSION section:\n   - Do they analyze WHY their method works differently on different architectures?\n   - Do they discuss architectural differences between the VLA models they test on?\n   - Any mention of how the vision connector design affects compression results?\n\n3. The APPENDIX or supplementary material:\n   - Any additional analysis of failure modes\n   - Any discussion of when/why pruning completely fails\n\n4. Search specifically for these terms anywhere in the full paper:\n   - \"pixel\" (any context)\n   - \"shuffle\" \n   - \"entangle\"\n   - \"connector\"\n   - \"projection\"\n   - \"architecture\" (in context of comparing different model architectures)\n   - \"cliff\"\n   - \"catastroph\"\n   - \"collapse\"\n   - \"0%\" or \"zero percent\"\n\nPlease be exhaustive - check every section including appendix."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "0b0fd255-0067-4644-b7b8-5c2c094451c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yt2y9azwJdMhd4vp1GLbN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3899,
      "cache_read_input_tokens": 25875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3899
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T03:41:20.766Z_

<details><summary>↩ Tool result · `toolu_01Sj3hhwMWeJEMmUJ1wqogK1`</summary>

```text
# Analysis of GridS Paper: VLA Models, Vision Connectors, and Experimental Details

## VLA Models Tested

The paper evaluates GridS across **three distinct VLA architectures**:

1. **π₀** (flow-matching) - Black et al., 2024
2. **π₀.₅** (flow-matching) - Intelligence et al., 2025
3. **SmolVLA** (auto-regressive) - Shukor et al., 2025

## Vision Connector Architecture

**Critical Finding**: The paper provides **no explicit description** of vision connector designs across these models. There is no mention of:
- MLP projection layers between vision encoder and transformer
- Pixel-shuffle operations
- Specific connector architecture comparisons
- How different models handle vision-to-language token bridging

The paper states: "Standard VLA architectures typically employ a frozen Vision Transformer (e.g., SigLIP or DINOv2) to encode visual observations" but does not detail downstream connection mechanisms.

## Experimental Results Summary

**Table 1 (LIBERO - π₀ baseline: 256 tokens, 216.01 GFLOPs)**
- π₀ + GridS16: 51.65 GFLOPs, +1.6% average success rate
- π₀ + GridS4: 43.61 GFLOPs, +1.1% success rate

**Table 1 (LIBERO - π₀.₅ baseline: 256 tokens, 249.76 GFLOPs)**
- π₀.₅ + GridS16: 83.84 GFLOPs, +1.0% success rate
- π₀.₅ + GridS4: 75.73 GFLOPs, no change (0.0%)

**Table 2 (ALOHA - π₀)**
- Baseline 256 tokens → GridS 16 tokens maintains 87.0% success rate

## Architectural Analysis Gaps

The paper **does not analyze** why performance varies between π₀, π₀.₅, and SmolVLA architecturally. No discussion addresses:
- Why flow-matching vs. auto-regressive models respond differently
- Connector design impact on compression tolerance
- Architectural differences affecting pruning sensitivity

## Ablation Studies

**Table 3 (Real-world Stack Cubes task)**
Shows inverted U-shaped curve with **catastrophic failure at K=4** (0.0% success rate) and K=8 revealing "severe positional bias." At K=32, performance drops to 19.0%, suggesting excessive tokens introduce harmful noise rather than enabling flexibility.

## Critical Terminology Searches

**No results found** for: "pixel," "shuffle," "entangle," "connector," "projection" (in architectural context), "cliff," "collapse," or "0%."

The phrase "catastrophic" appears only in: "catastrophic failure is avoided" in discussion of gradient flow properties.

## Why GridS Works: Stated Mechanisms

The paper attributes success to:
1. **Information Retention filtering** (Section 4.4): Reducing spatial redundancy from off-diagonal dense correlations to diagonal-dominant sparse structure
2. **Regularization effect**: "Excessive tokens introduce irrelevant background noise" rather than representing genuine information loss

No architectural comparison explains differential performance across model types.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "615b3f8c-ffe6-4712-8bfd-13741e28a0a6",
  "tool_use_result": {
    "bytes": 432339,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of GridS Paper: VLA Models, Vision Connectors, and Experimental Details\n\n## VLA Models Tested\n\nThe paper evaluates GridS across **three distinct VLA architectures**:\n\n1. **π₀** (flow-matching) - Black et al., 2024\n2. **π₀.₅** (flow-matching) - Intelligence et al., 2025\n3. **SmolVLA** (auto-regressive) - Shukor et al., 2025\n\n## Vision Connector Architecture\n\n**Critical Finding**: The paper provides **no explicit description** of vision connector designs across these models. There is no mention of:\n- MLP projection layers between vision encoder and transformer\n- Pixel-shuffle operations\n- Specific connector architecture comparisons\n- How different models handle vision-to-language token bridging\n\nThe paper states: \"Standard VLA architectures typically employ a frozen Vision Transformer (e.g., SigLIP or DINOv2) to encode visual observations\" but does not detail downstream connection mechanisms.\n\n## Experimental Results Summary\n\n**Table 1 (LIBERO - π₀ baseline: 256 tokens, 216.01 GFLOPs)**\n- π₀ + GridS16: 51.65 GFLOPs, +1.6% average success rate\n- π₀ + GridS4: 43.61 GFLOPs, +1.1% success rate\n\n**Table 1 (LIBERO - π₀.₅ baseline: 256 tokens, 249.76 GFLOPs)**\n- π₀.₅ + GridS16: 83.84 GFLOPs, +1.0% success rate\n- π₀.₅ + GridS4: 75.73 GFLOPs, no change (0.0%)\n\n**Table 2 (ALOHA - π₀)**\n- Baseline 256 tokens → GridS 16 tokens maintains 87.0% success rate\n\n## Architectural Analysis Gaps\n\nThe paper **does not analyze** why performance varies between π₀, π₀.₅, and SmolVLA architecturally. No discussion addresses:\n- Why flow-matching vs. auto-regressive models respond differently\n- Connector design impact on compression tolerance\n- Architectural differences affecting pruning sensitivity\n\n## Ablation Studies\n\n**Table 3 (Real-world Stack Cubes task)**\nShows inverted U-shaped curve with **catastrophic failure at K=4** (0.0% success rate) and K=8 revealing \"severe positional bias.\" At K=32, performance drops to 19.0%, suggesting excessive tokens introduce harmful noise rather than enabling flexibility.\n\n## Critical Terminology Searches\n\n**No results found** for: \"pixel,\" \"shuffle,\" \"entangle,\" \"connector,\" \"projection\" (in architectural context), \"cliff,\" \"collapse,\" or \"0%.\"\n\nThe phrase \"catastrophic\" appears only in: \"catastrophic failure is avoided\" in discussion of gradient flow properties.\n\n## Why GridS Works: Stated Mechanisms\n\nThe paper attributes success to:\n1. **Information Retention filtering** (Section 4.4): Reducing spatial redundancy from off-diagonal dense correlations to diagonal-dominant sparse structure\n2. **Regularization effect**: \"Excessive tokens introduce irrelevant background noise\" rather than representing genuine information loss\n\nNo architectural comparison explains differential performance across model types.",
    "durationMs": 10522,
    "url": "https://arxiv.org/html/2605.11817"
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very comprehensive picture. Let me also check the ablation table more carefully - it mentions K=4 gives 0.0% success rate on SmolVLA real-world. Let me get more details on this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "b4ad27c8-9d86-4d36-9821-a17d2fbeee5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZCViGY56bkfMfqmKtsYB2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 29774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1307
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 20_

Found a critical detail — their ablation shows 0% SR at K=4. Let me get more specifics on that finding and whether they analyze it architecturally.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "51808f7f-3003-4806-83a5-479ecc2cd11f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZCViGY56bkfMfqmKtsYB2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 29774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1307
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QSvYVHNq7K8H6yJKd92Zrq`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.11817",
  "prompt": "I need to find very specific details about:\n\n1. Table 3 and the ablation on number of tokens K. Extract the COMPLETE table with all numbers. They mention K=4 gives 0.0% success rate - what is the full context? Do they explain WHY K=4 fails completely? Is this on SmolVLA specifically?\n\n2. Section 4.4 or any \"Analysis\" section - extract the COMPLETE text. Especially the \"Information Retention filtering\" analysis and the \"diagonal-dominant sparse structure\" discussion.\n\n3. Any visualization or figure that shows attention patterns, token distributions, or spatial analysis. What do Figures 1-6 show?\n\n4. Do they compare GridS performance ACROSS different VLA architectures (π₀ vs π₀.₅ vs SmolVLA) and discuss WHY results differ? Or do they just report numbers without cross-architecture analysis?\n\n5. The exact text around any mention of \"catastrophic\" - full paragraph context.\n\n6. Do they ever discuss or test discrete token DELETION (as opposed to their grid sampling)? Do they test what happens when you simply remove tokens from the sequence?\n\n7. Any comparison with FastV, SparseVLM, VLA-Cache, EfficientVLA - what exact results do these baselines achieve? Do any of them show 0% or near-0% success rates on any model?\n\nExtract complete text for all relevant paragraphs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "e7a17e34-e42a-4340-8abc-971f98039715",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZCViGY56bkfMfqmKtsYB2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 29774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1307
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T03:41:50.483Z_

<details><summary>↩ Tool result · `toolu_01QSvYVHNq7K8H6yJKd92Zrq`</summary>

```text
# Detailed Analysis of GridS Paper

## 1. Table 3 - Complete Token Ablation Results

**Full Table 3 Data (Real-world Stack Cubes task on SO100 robot):**

| Method | Visual Tokens | Success Rate (%) | OOD SR (%) |
|--------|---------------|------------------|-----------|
| GridS | 4 | 0.0 | 0.0 |
| GridS | 8 | 28.5 | 19.1 |
| GridS | 16 | 61.9 | 38.1 |
| GridS | 32 | 19.0 | 0.0 |
| Baseline | 64 | 9.5 | 0.0 |

**Why K=4 Fails Completely:**

The paper states: "At extreme sparsity (K=4), the policy fails completely, indicating an information bottleneck where the representation lacks the geometric resolution required for precise alignment."

The authors identify this as occurring on **SmolVLA specifically** in real-world conditions. They note an "inverted U-shaped trend" where K=16 represents optimal compression, but below that threshold, "the representation lacks the geometric resolution required for precise alignment."

They also observe that "reducing the budget to K=8 causes the policy to suffer from severe positional bias, where successful manipulation is restricted exclusively to objects initialized on the left side due to insufficient spatial coverage."

## 2. Section 4.4 - Why GridS Works (Complete Analysis)

**Full Section 4.4 Text:**

"GridS adaptively samples global contextual cues using a learnable MLP and bilinear interpolation. Fig. 7 (right) illustrates the resulting reduction in spatial redundancy: while original feature maps display dense off-diagonal correlations, GridS yields a clean, diagonal-dominant structure, confirming that the bilinear sampling transforms redundant inputs into a compact, orthogonal token set.

We visualize the corresponding semantic coverage via Information Retention maps (Fig. 7 left). A more detailed calculation method for retention map can be found in the appendix I. In visually simple environments like standard ALOHA, the model easily covers the clean scene, achieving near-uniform retention (0.9994). However, retention scores naturally drop in LIBERO (0.9709) and noisy Real-World scenarios (0.8610). While a strictly uniform map represents the theoretical ideal of zero information loss, preserving all visual input actually degrades performance in cluttered domains. To achieve high success rates in complex environments, the policy must discard irrelevant distractors. Therefore, the low-retention areas are not a flaw; they correctly reflect GridS actively filtering out background noise to concentrate its capacity on critical dynamic geometries. This inherent spatial regularization explains why GridS yields massive out-of-distribution (OOD) improvements over full-token baselines."

## 3. Visualization Content Summary

**Figure 1:** Shows motivation comparing standard VLA (256 tokens, 100% compute) vs. GridS (16 tokens, 6.25% compute) with real-world performance gains (+28.6% OOD success rate, 2.3s latency reduction).

**Figure 2:** Contrasts discrete patch selection (with quantization errors when grasp points fall between patches) versus differentiable continuous coordinate sampling via bilinear interpolation.

**Figure 7:** Displays Information Retention Maps showing spatial coverage (left panel) and Token Self-Similarity matrices (right panel), demonstrating GridS converts "dense off-diagonal correlations" into "clean, diagonal-dominant structure."

## 4. Cross-Architecture Comparative Analysis

The paper reports results across three architectures but **does not provide systematic cross-architecture analysis** explaining performance differences:

- **π₀ with GridS₁₆:** 76% FLOP reduction, +1.6% average success rate
- **π₀.₅ with GridS₁₆:** 66% FLOP reduction, +1.0% average success rate  
- **SmolVLA with GridS:** 1.23× inference speedup, +22.2% real-world success rate

The authors note task-specific sensitivities but attribute this to "overfitting tendencies associated with the LIBERO dataset" rather than architecture-specific factors.

## 5. "Catastrophic" References

The paper does **not use the word "catastrophic."** The strongest failure mode language appears in Table 1 context, where baseline pruning methods show "4.6%" degradation (SparseVLM on π₀).

## 6. Discrete Token Deletion Testing

The paper **does not explicitly test discrete token removal** as a standalone baseline. However, they critique existing methods: "FastV, SparseVLM...discretely dropping patches...destroys spatial continuity, degrading π₀ success rates by 1.5% and 4.6%."

They distinguish their approach as "continuous token resampling" versus "passive discrete patch-dropping."

## 7. Baseline Comparison Results

**Baseline Performance on π₀ (LIBERO average success rate):**

- OpenVLA: 76.5%
- π₀ baseline: 94.4%
- π₀ + FastV: 92.9% (−1.5%)
- π₀ + SparseVLM: 89.8% (−4.6%)
- π₀ + VLA-Cache: 93.8% (−0.6%)
- π₀ + GridS₁₆: 96.0% (+1.6%)
- π₀ + GridS₄: 95.5% (+1.1%)

**None report 0% failure rates on LIBERO**, but SmolVLA achieves 0% only at K=4 on real-world Stack Cubes (Table 3), context-dependent on specific task and compression level.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "a1b09ee6-3143-48a7-917d-07c163fe3e79",
  "tool_use_result": {
    "bytes": 432339,
    "code": 200,
    "codeText": "OK",
    "result": "# Detailed Analysis of GridS Paper\n\n## 1. Table 3 - Complete Token Ablation Results\n\n**Full Table 3 Data (Real-world Stack Cubes task on SO100 robot):**\n\n| Method | Visual Tokens | Success Rate (%) | OOD SR (%) |\n|--------|---------------|------------------|-----------|\n| GridS | 4 | 0.0 | 0.0 |\n| GridS | 8 | 28.5 | 19.1 |\n| GridS | 16 | 61.9 | 38.1 |\n| GridS | 32 | 19.0 | 0.0 |\n| Baseline | 64 | 9.5 | 0.0 |\n\n**Why K=4 Fails Completely:**\n\nThe paper states: \"At extreme sparsity (K=4), the policy fails completely, indicating an information bottleneck where the representation lacks the geometric resolution required for precise alignment.\"\n\nThe authors identify this as occurring on **SmolVLA specifically** in real-world conditions. They note an \"inverted U-shaped trend\" where K=16 represents optimal compression, but below that threshold, \"the representation lacks the geometric resolution required for precise alignment.\"\n\nThey also observe that \"reducing the budget to K=8 causes the policy to suffer from severe positional bias, where successful manipulation is restricted exclusively to objects initialized on the left side due to insufficient spatial coverage.\"\n\n## 2. Section 4.4 - Why GridS Works (Complete Analysis)\n\n**Full Section 4.4 Text:**\n\n\"GridS adaptively samples global contextual cues using a learnable MLP and bilinear interpolation. Fig. 7 (right) illustrates the resulting reduction in spatial redundancy: while original feature maps display dense off-diagonal correlations, GridS yields a clean, diagonal-dominant structure, confirming that the bilinear sampling transforms redundant inputs into a compact, orthogonal token set.\n\nWe visualize the corresponding semantic coverage via Information Retention maps (Fig. 7 left). A more detailed calculation method for retention map can be found in the appendix I. In visually simple environments like standard ALOHA, the model easily covers the clean scene, achieving near-uniform retention (0.9994). However, retention scores naturally drop in LIBERO (0.9709) and noisy Real-World scenarios (0.8610). While a strictly uniform map represents the theoretical ideal of zero information loss, preserving all visual input actually degrades performance in cluttered domains. To achieve high success rates in complex environments, the policy must discard irrelevant distractors. Therefore, the low-retention areas are not a flaw; they correctly reflect GridS actively filtering out background noise to concentrate its capacity on critical dynamic geometries. This inherent spatial regularization explains why GridS yields massive out-of-distribution (OOD) improvements over full-token baselines.\"\n\n## 3. Visualization Content Summary\n\n**Figure 1:** Shows motivation comparing standard VLA (256 tokens, 100% compute) vs. GridS (16 tokens, 6.25% compute) with real-world performance gains (+28.6% OOD success rate, 2.3s latency reduction).\n\n**Figure 2:** Contrasts discrete patch selection (with quantization errors when grasp points fall between patches) versus differentiable continuous coordinate sampling via bilinear interpolation.\n\n**Figure 7:** Displays Information Retention Maps showing spatial coverage (left panel) and Token Self-Similarity matrices (right panel), demonstrating GridS converts \"dense off-diagonal correlations\" into \"clean, diagonal-dominant structure.\"\n\n## 4. Cross-Architecture Comparative Analysis\n\nThe paper reports results across three architectures but **does not provide systematic cross-architecture analysis** explaining performance differences:\n\n- **π₀ with GridS₁₆:** 76% FLOP reduction, +1.6% average success rate\n- **π₀.₅ with GridS₁₆:** 66% FLOP reduction, +1.0% average success rate  \n- **SmolVLA with GridS:** 1.23× inference speedup, +22.2% real-world success rate\n\nThe authors note task-specific sensitivities but attribute this to \"overfitting tendencies associated with the LIBERO dataset\" rather than architecture-specific factors.\n\n## 5. \"Catastrophic\" References\n\nThe paper does **not use the word \"catastrophic.\"** The strongest failure mode language appears in Table 1 context, where baseline pruning methods show \"4.6%\" degradation (SparseVLM on π₀).\n\n## 6. Discrete Token Deletion Testing\n\nThe paper **does not explicitly test discrete token removal** as a standalone baseline. However, they critique existing methods: \"FastV, SparseVLM...discretely dropping patches...destroys spatial continuity, degrading π₀ success rates by 1.5% and 4.6%.\"\n\nThey distinguish their approach as \"continuous token resampling\" versus \"passive discrete patch-dropping.\"\n\n## 7. Baseline Comparison Results\n\n**Baseline Performance on π₀ (LIBERO average success rate):**\n\n- OpenVLA: 76.5%\n- π₀ baseline: 94.4%\n- π₀ + FastV: 92.9% (−1.5%)\n- π₀ + SparseVLM: 89.8% (−4.6%)\n- π₀ + VLA-Cache: 93.8% (−0.6%)\n- π₀ + GridS₁₆: 96.0% (+1.6%)\n- π₀ + GridS₄: 95.5% (+1.1%)\n\n**None report 0% failure rates on LIBERO**, but SmolVLA achieves 0% only at K=4 on real-world Stack Cubes (Table 3), context-dependent on specific task and compression level.",
    "durationMs": 17399,
    "url": "https://arxiv.org/html/2605.11817"
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very comprehensive picture. Let me also check if the paper tests any pruning baselines on SmolVLA specifically (not just π₀). This is crucial - do they test FastV/SparseVLM on SmolVLA?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "19a88091-67f6-4d2b-9f0a-1ee8f90b4679",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4CNDB9jnFknh6oR1ak73E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 31081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2000
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 24_

One more check — I need to verify whether they tested pruning baselines on SmolVLA specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "179a817a-330e-4a73-b8cf-a6066bca9993",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4CNDB9jnFknh6oR1ak73E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 31081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2000
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MAYswncQRag2MBNbhWRJLU`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.11817",
  "prompt": "I need to know specifically:\n\n1. Were the pruning baselines (FastV, SparseVLM, VLA-Cache, EfficientVLA) tested ONLY on π₀/π₀.₅, or also on SmolVLA? Did they run any token pruning baseline on SmolVLA?\n\n2. SmolVLA uses what vision encoder and what connector? Does the paper specify SmolVLA's architecture details (e.g., does it use pixel-shuffle, MLP, or another connector type)?\n\n3. Is there any mention of OpenVLA in the experiments? OpenVLA uses a pixel-shuffle connector - do they test on it or mention it?\n\n4. The paper's Related Work - do they cite or mention \"token entanglement\", \"importance margin\", or any work that analyzes WHY certain architectures are harder to compress?\n\n5. In the conclusion or discussion - do they mention limitations related to architecture-specific effects? Do they suggest future work on understanding architecture-dependent compression?\n\n6. Is there any appendix content about failure analysis, architecture comparison, or connector design?\n\nExtract exact quotes for all findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "f1cdc193-f1a1-44a3-bc8c-35ac82237204",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4CNDB9jnFknh6oR1ak73E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 31081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2000
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T03:42:11.622Z_

<details><summary>↩ Tool result · `toolu_01MAYswncQRag2MBNbhWRJLU`</summary>

```text
# Analysis of GridS Paper: Architecture-Specific Compression Questions

## 1. Pruning Baseline Testing Scope

**Finding:** Pruning baselines were tested **only on π₀/π₀.₅**, not on SmolVLA.

**Evidence:** Table 1 shows FastV, SparseVLM, and VLA-Cache exclusively compared against π₀ baseline. SmolVLA appears only as a separate baseline row without any pruning method applied to it. The paper states: "We select π₀ (Black et al., 2024) and π₀.₅ (Intelligence et al., 2025), two flow-matching method as our baseline models" for LIBERO experiments, then separately notes SmolVLA is used for real-world experiments without pruning baselines.

---

## 2. SmolVLA Architecture Details

**Finding:** The paper provides **minimal architectural specifics** for SmolVLA.

**Evidence:** SmolVLA is described only as "an auto-regressive model" in the introduction. No vision encoder type, connector mechanism, or architectural details are specified in the main text. The paper cites "SmolVLA (Shukor et al., 2025): a vision-language-action model for affordable and efficient robotics" but does not elaborate on internal design.

---

## 3. OpenVLA Mentions

**Finding:** OpenVLA is **cited in related work and baseline comparisons** but NOT tested with GridS.

**Evidence:** Table 1 includes OpenVLA and "OpenVLA-OFT" as baseline rows without GridS applied. The paper references "OpenVLA (Kim et al., 2025b)" and notes it uses "frozen Vision Transformer (e.g., SigLIP...or DINOv2)" but GridS is never evaluated on OpenVLA architecture.

---

## 4. Architecture-Dependent Compression Analysis

**Finding:** The paper does **not cite work on token entanglement, importance margin, or architecture-dependent compression difficulty**.

Related Work (Section 2) discusses: semantic pruning, dynamic token pruning, and "continuous and deformable sampling"—but no citations to theoretical work explaining why certain connectors resist compression.

---

## 5. Limitations Discussion on Architecture Effects

**Finding:** Appendix J (Limitations) does **not mention architecture-specific constraints**.

**Key quote from Appendix J scope:** The appendix is referenced but content truncated in provided text. However, the main conclusion states: "By significantly reducing deployment costs, GridS establishes a new pruning paradigm" without acknowledging potential architecture-dependent limitations.

---

## 6. Failure Analysis and Architecture Comparison

**Finding:** No systematic failure analysis or connector-type comparison provided.

**Evidence:** Section 4.3.1 (Token Count) notes task-specific sensitivity: "Spatial shows a 1.2% decline on π₀.₅ at K=4" and "Long performance drops in the sparsest setting (K=4)," but this is attributed to "geometric ambiguity" rather than architecture-specific factors. No analysis of how connector design (pixel-shuffle vs. MLP) affects compression.

---

## Summary

The paper does **not investigate whether compression difficulty varies by connector architecture**. Testing was confined to flow-matching models (π₀/π₀.₅) with one auto-regressive baseline (SmolVLA), leaving architectural generalization unaddressed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "53924893-8998-4a83-81ec-c5bc416b2942",
  "tool_use_result": {
    "bytes": 432339,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of GridS Paper: Architecture-Specific Compression Questions\n\n## 1. Pruning Baseline Testing Scope\n\n**Finding:** Pruning baselines were tested **only on π₀/π₀.₅**, not on SmolVLA.\n\n**Evidence:** Table 1 shows FastV, SparseVLM, and VLA-Cache exclusively compared against π₀ baseline. SmolVLA appears only as a separate baseline row without any pruning method applied to it. The paper states: \"We select π₀ (Black et al., 2024) and π₀.₅ (Intelligence et al., 2025), two flow-matching method as our baseline models\" for LIBERO experiments, then separately notes SmolVLA is used for real-world experiments without pruning baselines.\n\n---\n\n## 2. SmolVLA Architecture Details\n\n**Finding:** The paper provides **minimal architectural specifics** for SmolVLA.\n\n**Evidence:** SmolVLA is described only as \"an auto-regressive model\" in the introduction. No vision encoder type, connector mechanism, or architectural details are specified in the main text. The paper cites \"SmolVLA (Shukor et al., 2025): a vision-language-action model for affordable and efficient robotics\" but does not elaborate on internal design.\n\n---\n\n## 3. OpenVLA Mentions\n\n**Finding:** OpenVLA is **cited in related work and baseline comparisons** but NOT tested with GridS.\n\n**Evidence:** Table 1 includes OpenVLA and \"OpenVLA-OFT\" as baseline rows without GridS applied. The paper references \"OpenVLA (Kim et al., 2025b)\" and notes it uses \"frozen Vision Transformer (e.g., SigLIP...or DINOv2)\" but GridS is never evaluated on OpenVLA architecture.\n\n---\n\n## 4. Architecture-Dependent Compression Analysis\n\n**Finding:** The paper does **not cite work on token entanglement, importance margin, or architecture-dependent compression difficulty**.\n\nRelated Work (Section 2) discusses: semantic pruning, dynamic token pruning, and \"continuous and deformable sampling\"—but no citations to theoretical work explaining why certain connectors resist compression.\n\n---\n\n## 5. Limitations Discussion on Architecture Effects\n\n**Finding:** Appendix J (Limitations) does **not mention architecture-specific constraints**.\n\n**Key quote from Appendix J scope:** The appendix is referenced but content truncated in provided text. However, the main conclusion states: \"By significantly reducing deployment costs, GridS establishes a new pruning paradigm\" without acknowledging potential architecture-dependent limitations.\n\n---\n\n## 6. Failure Analysis and Architecture Comparison\n\n**Finding:** No systematic failure analysis or connector-type comparison provided.\n\n**Evidence:** Section 4.3.1 (Token Count) notes task-specific sensitivity: \"Spatial shows a 1.2% decline on π₀.₅ at K=4\" and \"Long performance drops in the sparsest setting (K=4),\" but this is attributed to \"geometric ambiguity\" rather than architecture-specific factors. No analysis of how connector design (pixel-shuffle vs. MLP) affects compression.\n\n---\n\n## Summary\n\nThe paper does **not investigate whether compression difficulty varies by connector architecture**. Testing was confined to flow-matching models (π₀/π₀.₅) with one auto-regressive baseline (SmolVLA), leaving architectural generalization unaddressed.",
    "durationMs": 10436,
    "url": "https://arxiv.org/html/2605.11817"
  }
}
```

</details>

---

### Assistant

_source line 27_

Now I have a complete picture. Here's the analysis:

---

## 关键判断

### Q1: 是否分析了 pixel-shuffle entanglement 机制？
**否** — 论文全文不包含 "pixel shuffle"、"space-to-depth"、"token entanglement"、"spatial mixing"、"cliff-edge" 中的任何一个术语。他们完全没有讨论 vision connector 的设计如何影响 token compression 的可行性。他们对 token pruning 失败的解释是：

- discrete selection 导致 quantization error（丢失 sub-patch precision）
- semantic pruning 忽略 geometrically critical regions（如 contact points）
- training-free 方法无法 align with task requirements

这些都是**通用层面**的批评，不涉及任何 architecture-specific 的机制分析。

### Q2: 是否做了 cross-architecture 对比？
**否** — 他们在三个 VLA 上做了实验（π₀、π₀.₅、SmolVLA），但：
- Pruning baselines（FastV、SparseVLM、VLA-Cache）**只在 π₀/π₀.₅ 上测试**，未在 SmolVLA 上跑
- 没有分析为什么不同架构对 compression 的响应不同
- 没有提及 connector type（MLP vs pixel-shuffle vs cross-attention）的区别
- SmolVLA 的架构细节（connector 类型）在论文中未说明

### Q3: SmolVLA 实验深度
- SmolVLA **仅用于真实机器人实验**（SO100 robot arm，3个任务），**没有 LIBERO 仿真**
- 他们观察到 SmolVLA baseline 在 Stack Cubes 上只有 7.6% SR（接近失败），GridS 提升到 60%
- K=4 时 GridS 本身也是 0% SR，但他们将此归因为 "information bottleneck"（geometric resolution 不足），**没有分析是否与 SmolVLA 的 connector 设计有关**
- 关键遗漏：他们没有在 SmolVLA 上测试任何 discrete pruning baseline，所以没有 "token deletion → 0% SR" 的直接证据

### Q4: Motivation 叙事类型
**通用优化** — 他们的叙事是：
> "所有现有 pruning 方法都受限于 discrete selection over a fixed grid，导致 quantization errors 和 spatial fidelity loss。我们提出 continuous resampling 替代 discrete dropping。"

这是一个 **method-level** 的改进论述（continuous > discrete），不是 architecture-level 的诊断。他们没有说 "某些架构下 pruning 完全失败"，而是说 "pruning 在所有情况下都有 quantization error，我们的方法更好"。

---

## 对我们 Claim 2 独特性的影响

**无实质影响。** 具体原因：

1. **机制分析完全不重叠**：GridS 论文不涉及 pixel-shuffle connector 如何制造 token entanglement，不分析 architecture-dependent compressibility，不解释为什么 discrete deletion 在某些架构上 cliff-edge 到 0%
2. **他们的 "为什么 pruning 不好" 停留在 quantization error 层面**，我们的分析深入到 connector-induced spatial entanglement 层面——这是不同抽象层次的解释
3. **他们没有做 cross-architecture 对比实验**：没有在同一 benchmark 上比较不同 connector 类型对 pruning 的容忍度差异
4. **SmolVLA 上的 0% SR 是他们自己的 GridS 在 K=4 时的结果**，不是 discrete pruning 的结果——他们甚至没在 SmolVLA 上跑 discrete pruning baseline

### 一个需要注意的点
他们的 K=4 → 0% 结果表明即使是 continuous resampling，在极端压缩下也会崩溃。但他们的解释（"information bottleneck, insufficient geometric resolution"）与我们的解释（"pixel-shuffle entanglement 导致 token 间不可分离"）完全不同。

---

## 建议的 Related Work positioning 策略

GridS 应作为 **concurrent work** 引用，定位为：

> "GridS (Feng et al., 2026) proposes continuous grid resampling as an alternative to discrete token pruning, achieving strong compression on π₀ and SmolVLA. However, their analysis focuses on the discrete-vs-continuous sampling paradigm without examining **why** certain VLA architectures exhibit fundamentally different compression behaviors. Our work is complementary: we diagnose the architectural root cause (pixel-shuffle-induced token entanglement) that makes discrete pruning catastrophically fail on specific connector designs, providing the theoretical foundation for **when** alternative compression strategies like GridS become necessary."

核心差异化：
- **GridS 回答 "how to compress better"**（continuous > discrete）
- **我们回答 "why compression fails on certain architectures"**（pixel-shuffle entanglement 诊断）+ "how to predict compressibility"（importance margin）

Sources:
- [ICML 2026 Poster - See What Matters](https://icml.cc/virtual/2026/poster/65010)
- [arXiv:2605.11817](https://arxiv.org/abs/2605.11817)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "uuid": "ccce0c25-bc86-4b48-be72-1cb0fe9bae52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9YVqDkDbmaYfqJAVf2fz1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1229,
      "cache_read_input_tokens": 33081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1229
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 28_

Now I have a complete picture. Here's the analysis:

---

## 关键判断

### Q1: 是否分析了 pixel-shuffle entanglement 机制？
**否** — 论文全文不包含 "pixel shuffle"、"space-to-depth"、"token entanglement"、"spatial mixing"、"cliff-edge" 中的任何一个术语。他们完全没有讨论 vision connector 的设计如何影响 token compression 的可行性。他们对 token pruning 失败的解释是：

- discrete selection 导致 quantization error（丢失 sub-patch precision）
- semantic pruning 忽略 geometrically critical regions（如 contact points）
- training-free 方法无法 align with task requirements

这些都是**通用层面**的批评，不涉及任何 architecture-specific 的机制分析。

### Q2: 是否做了 cross-architecture 对比？
**否** — 他们在三个 VLA 上做了实验（π₀、π₀.₅、SmolVLA），但：
- Pruning baselines（FastV、SparseVLM、VLA-Cache）**只在 π₀/π₀.₅ 上测试**，未在 SmolVLA 上跑
- 没有分析为什么不同架构对 compression 的响应不同
- 没有提及 connector type（MLP vs pixel-shuffle vs cross-attention）的区别
- SmolVLA 的架构细节（connector 类型）在论文中未说明

### Q3: SmolVLA 实验深度
- SmolVLA **仅用于真实机器人实验**（SO100 robot arm，3个任务），**没有 LIBERO 仿真**
- 他们观察到 SmolVLA baseline 在 Stack Cubes 上只有 7.6% SR（接近失败），GridS 提升到 60%
- K=4 时 GridS 本身也是 0% SR，但他们将此归因为 "information bottleneck"（geometric resolution 不足），**没有分析是否与 SmolVLA 的 connector 设计有关**
- 关键遗漏：他们没有在 SmolVLA 上测试任何 discrete pruning baseline，所以没有 "token deletion → 0% SR" 的直接证据

### Q4: Motivation 叙事类型
**通用优化** — 他们的叙事是：
> "所有现有 pruning 方法都受限于 discrete selection over a fixed grid，导致 quantization errors 和 spatial fidelity loss。我们提出 continuous resampling 替代 discrete dropping。"

这是一个 **method-level** 的改进论述（continuous > discrete），不是 architecture-level 的诊断。他们没有说 "某些架构下 pruning 完全失败"，而是说 "pruning 在所有情况下都有 quantization error，我们的方法更好"。

---

## 对我们 Claim 2 独特性的影响

**无实质影响。** 具体原因：

1. **机制分析完全不重叠**：GridS 论文不涉及 pixel-shuffle connector 如何制造 token entanglement，不分析 architecture-dependent compressibility，不解释为什么 discrete deletion 在某些架构上 cliff-edge 到 0%
2. **他们的 "为什么 pruning 不好" 停留在 quantization error 层面**，我们的分析深入到 connector-induced spatial entanglement 层面——这是不同抽象层次的解释
3. **他们没有做 cross-architecture 对比实验**：没有在同一 benchmark 上比较不同 connector 类型对 pruning 的容忍度差异
4. **SmolVLA 上的 0% SR 是他们自己的 GridS 在 K=4 时的结果**，不是 discrete pruning 的结果——他们甚至没在 SmolVLA 上跑 discrete pruning baseline

### 一个需要注意的点
他们的 K=4 → 0% 结果表明即使是 continuous resampling，在极端压缩下也会崩溃。但他们的解释（"information bottleneck, insufficient geometric resolution"）与我们的解释（"pixel-shuffle entanglement 导致 token 间不可分离"）完全不同。

---

## 建议的 Related Work positioning 策略

GridS 应作为 **concurrent work** 引用，定位为：

> "GridS (Feng et al., 2026) proposes continuous grid resampling as an alternative to discrete token pruning, achieving strong compression on π₀ and SmolVLA. However, their analysis focuses on the discrete-vs-continuous sampling paradigm without examining **why** certain VLA architectures exhibit fundamentally different compression behaviors. Our work is complementary: we diagnose the architectural root cause (pixel-shuffle-induced token entanglement) that makes discrete pruning catastrophically fail on specific connector designs, providing the theoretical foundation for **when** alternative compression strategies like GridS become necessary."

核心差异化：
- **GridS 回答 "how to compress better"**（continuous > discrete）
- **我们回答 "why compression fails on certain architectures"**（pixel-shuffle entanglement 诊断）+ "how to predict compressibility"（importance margin）

Sources:
- [ICML 2026 Poster - See What Matters](https://icml.cc/virtual/2026/poster/65010)
- [arXiv:2605.11817](https://arxiv.org/abs/2605.11817)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 156040,
  "duration_api_ms": 170434,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "ea2de7c9-a04a-48db-8b45-d955923997c8",
  "total_cost_usd": 0.48901025000000004,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 22469,
    "cache_read_input_tokens": 156414,
    "output_tokens": 3522,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 22469,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1512,
        "cache_read_input_tokens": 33081,
        "cache_creation_input_tokens": 1229,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1229
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 141687,
      "outputTokens": 6117,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 1,
      "costUSD": 0.182272,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 3522,
      "cacheReadInputTokens": 156414,
      "cacheCreationInputTokens": 22469,
      "webSearchRequests": 0,
      "costUSD": 0.30673825000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3e9712df-cea4-4bfe-a863-94ed959251b6"
}
```

</details>

---
