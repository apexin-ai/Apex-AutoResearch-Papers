# research seed dependent value overestimation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/workers/worker_research_seed-dependent-value-overestimation_20260514T142751.log`
- **Structured JSON:** [`30bf07c80d802d3348a1.json`](../../sessions/30/30bf07c80d802d3348a1.json)

## Before a recorded user message

64 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
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
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "605ad32f-49b0-479a-a3ca-fe39a9315abf",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1778778000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7e06b18c-68d2-4501-bdb4-a5c698a59541",
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for literature related to seed-dependent value overestimation in model-based RL, specifically in the context of DreamerV3 and temporal abstraction experiments. Let me:

1. First read the existing literature_map.yaml to understand the format
2. Then search for papers using WebSearch
3. Append findings to literature_map.yaml

Let me start by reading the existing file and doing web searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "1c8febb7-e763-4624-a698-cebaa4f472a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cPdZCjhJQNvf7nxy1TjNx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11966,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11966
      },
      "output_tokens": 35,
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

_source line 5_

先读取现有 literature_map.yaml，同时启动文献搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "24eab212-5181-4978-871e-12758e64ee18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cPdZCjhJQNvf7nxy1TjNx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11966,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11966
      },
      "output_tokens": 35,
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LGfj5YZiduDQctGAcboEoD`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__append_idea",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "de3cd731-fc56-4477-b14f-26f1a2511c79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cPdZCjhJQNvf7nxy1TjNx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11966,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11966
      },
      "output_tokens": 35,
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

_source line 7 · 2026-05-14T14:28:03.050Z_

<details><summary>↩ Tool result · `toolu_01LGfj5YZiduDQctGAcboEoD`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "cb301371-edbc-48ed-bd3f-c737c203e27c",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__append_idea",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011ohQSdggizbe4syfWJ4bkf`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "2feab53f-bb40-4476-85cd-275cfecbc901",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdHYpqTteoEEutf3McGC2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 23413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1268
      },
      "output_tokens": 71,
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

_source line 9 · 2026-05-14T14:28:06.964Z_

<details><summary>↩ Tool result · `toolu_011ohQSdggizbe4syfWJ4bkf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\", \"content\": \"# Literature Map — event-gated-adaptive-horizon\\n# Last updated: 2026-05-14\\n# Total: 28 papers (5 existing + 23 new)\\n\\n# ============================================================\\n# EXISTING CITATIONS (already in paper.tex)\\n# ============================================================\\n\\n- paper_id: sutton1999options\\n  title: \\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\"\\n  authors: [Sutton R.S., Precup D., Singh S.]\\n  year: 1999\\n  venue: \\\"Artificial Intelligence 112(1-2):181-211\\\"\\n  category: background\\n  role: \\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2020dreamerv1\\n  title: \\\"Dream to Control: Learning Behaviors by Latent Imagination\\\"\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\n  year: 2020\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2023dreamerv3\\n  title: \\\"Mastering Diverse Domains through World Models\\\"\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\n  year: 2023\\n  venue: \\\"arXiv:2301.04104 (Nature 2025)\\\"\\n  category: background\\n  role: \\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\"\\n  relevance_score: 5\\n\\n- paper_id: sharma2017figar\\n  title: \\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\n  year: 2017\\n  venue: \\\"ICLR Workshop\\\"\\n  category: method-component\\n  role: \\\"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\\\"\\n  relevance_score: 4\\n\\n- paper_id: janner2019mbpo\\n  title: \\\"When to Trust Your Model: Model-Based Policy Optimization\\\"\\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\\n  year: 2019\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Multi-step prediction error compounding\\n# ============================================================\\n\\n- paper_id: ke2019learning\\n  title: \\\"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\\\"\\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\\n  year: 2019\\n  venue: ICLR\\n  category: background\\n  role: \\\"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\\\"\\n  relevance_score: 4\\n\\n- paper_id: asadi2019combating\\n  title: \\\"Combating the Compounding-Error Problem with a Multi-step Model\\\"\\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\\n  year: 2019\\n  venue: \\\"arXiv:1905.13320\\\"\\n  category: background\\n  role: \\\"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\\\"\\n  relevance_score: 4\\n\\n- paper_id: venkatraman2015improving\\n  title: \\\"Improving Multi-Step Prediction of Learned Time Series Models\\\"\\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\\n  year: 2015\\n  venue: AAAI\\n  category: background\\n  role: \\\"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\\\"\\n  relevance_score: 3\\n\\n- paper_id: lambert2022investigating\\n  title: \\\"Investigating Compounding Prediction Errors in Learned Dynamics Models\\\"\\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\\n  year: 2022\\n  venue: \\\"arXiv:2203.09637\\\"\\n  category: background\\n  role: \\\"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Model-predictive control with learned dynamics\\n# ============================================================\\n\\n- paper_id: chua2018pets\\n  title: \\\"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\\\"\\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\\\"\\n  relevance_score: 3\\n\\n- paper_id: nagabandi2018neural\\n  title: \\\"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\\\"\\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\\n  year: 2018\\n  venue: ICRA\\n  category: background\\n  role: \\\"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Value overestimation mitigation\\n# ============================================================\\n\\n- paper_id: thrun1993issues\\n  title: \\\"Issues in Using Function Approximation for Reinforcement Learning\\\"\\n  authors: [Thrun S., Schwartz A.]\\n  year: 1993\\n  venue: \\\"Connectionist Models Summer School\\\"\\n  category: background\\n  role: \\\"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\\\"\\n  relevance_score: 4\\n\\n- paper_id: vanhasselt2016double\\n  title: \\\"Deep Reinforcement Learning with Double Q-Learning\\\"\\n  authors: [van Hasselt H., Guez A., Silver D.]\\n  year: 2016\\n  venue: AAAI\\n  category: background\\n  role: \\\"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\\\"\\n  relevance_score: 4\\n\\n- paper_id: fujimoto2018td3\\n  title: \\\"Addressing Function Approximation Error in Actor-Critic Methods\\\"\\n  authors: [Fujimoto S., van Hoof H., Meger D.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\\\"\\n  relevance_score: 4\\n\\n- paper_id: haarnoja2018sac\\n  title: \\\"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\\\"\\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\\\"\\n  relevance_score: 3\\n\\n- paper_id: lee2021sunrise\\n  title: \\\"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\\\"\\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Delusional bias\\n# ============================================================\\n\\n- paper_id: lu2018nondelusional\\n  title: \\\"Non-delusional Q-learning and Value-Iteration\\\"\\n  authors: [Lu T., Schuurmans D., Boutilier C.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Hierarchical RL with learned models\\n# ============================================================\\n\\n- paper_id: hafner2022director\\n  title: \\\"Deep Hierarchical Planning from Pixels\\\"\\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\\n  year: 2022\\n  venue: NeurIPS\\n  category: direct-competitor\\n  role: \\\"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\\\"\\n  relevance_score: 4\\n\\n- paper_id: nachum2018hiro\\n  title: \\\"Data-Efficient Hierarchical Reinforcement Learning\\\"\\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Action repeat / frame skip\\n# ============================================================\\n\\n- paper_id: braylan2015frame\\n  title: \\\"Frame Skip Is a Powerful Parameter for Learning to Play Atari\\\"\\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\\n  year: 2015\\n  venue: \\\"AAAI Workshop on Learning for General Competency in Video Games\\\"\\n  category: background\\n  role: \\\"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\\\"\\n  relevance_score: 3\\n\\n- paper_id: lakshminarayanan2017dynamic\\n  title: \\\"Dynamic Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\\n  year: 2017\\n  venue: AAAI\\n  category: method-component\\n  role: \\\"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\\\"\\n  relevance_score: 4\\n\\n- paper_id: biedenkapp2021temporl\\n  title: \\\"TempoRL: Learning When to Act\\\"\\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: DreamerV2\\n# ============================================================\\n\\n- paper_id: hafner2021dreamerv2\\n  title: \\\"Mastering Atari with Discrete World Models\\\"\\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\\n  year: 2021\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Alternative world model architectures\\n# ============================================================\\n\\n- paper_id: micheli2023iris\\n  title: \\\"Transformers are Sample-Efficient World Models\\\"\\n  authors: [Micheli V., Alonso E., Fleuret F.]\\n  year: 2023\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\\\"\\n  relevance_score: 3\\n\\n- paper_id: robine2023twm\\n  title: \\\"Transformer-based World Models Are Happy With 100k Interactions\\\"\\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\\n  year: 2023\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\\\"\\n  relevance_score: 3\\n\\n- paper_id: chen2022transdreamer\\n  title: \\\"TransDreamer: Reinforcement Learning with Transformer World Models\\\"\\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\\n  year: 2022\\n  venue: \\\"arXiv:2202.09481\\\"\\n  category: direct-competitor\\n  role: \\\"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\\n# ============================================================\\n\\n- paper_id: gumbsch2024thick\\n  title: \\\"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\\\"\\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\\n  year: 2024\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\\\"\\n  relevance_score: 5\\n\\n- paper_id: mattes2024hieros\\n  title: \\\"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\\\"\\n  authors: [Mattes P., Schlosser R., Herbrich R.]\\n  year: 2024\\n  venue: ICML\\n  category: direct-competitor\\n  role: \\\"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\\\"\\n  relevance_score: 5\\n\", \"total_chars\": 13210, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "1b0f99a1-3296-4d59-9aff-447dfd882b9e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map — event-gated-adaptive-horizon\\\\n# Last updated: 2026-05-14\\\\n# Total: 28 papers (5 existing + 23 new)\\\\n\\\\n# ============================================================\\\\n# EXISTING CITATIONS (already in paper.tex)\\\\n# ============================================================\\\\n\\\\n- paper_id: sutton1999options\\\\n  title: \\\\\\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\\\\\"\\\\n  authors: [Sutton R.S., Precup D., Singh S.]\\\\n  year: 1999\\\\n  venue: \\\\\\\"Artificial Intelligence 112(1-2):181-211\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hafner2020dreamerv1\\\\n  title: \\\\\\\"Dream to Control: Learning Behaviors by Latent Imagination\\\\\\\"\\\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\\\n  year: 2020\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: hafner2023dreamerv3\\\\n  title: \\\\\\\"Mastering Diverse Domains through World Models\\\\\\\"\\\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\\\n  year: 2023\\\\n  venue: \\\\\\\"arXiv:2301.04104 (Nature 2025)\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: sharma2017figar\\\\n  title: \\\\\\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\\\n  year: 2017\\\\n  venue: \\\\\\\"ICLR Workshop\\\\\\\"\\\\n  category: method-component\\\\n  role: \\\\\\\"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: janner2019mbpo\\\\n  title: \\\\\\\"When to Trust Your Model: Model-Based Policy Optimization\\\\\\\"\\\\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\\\\n  year: 2019\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Multi-step prediction error compounding\\\\n# ============================================================\\\\n\\\\n- paper_id: ke2019learning\\\\n  title: \\\\\\\"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\\\\\\\"\\\\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\\\\n  year: 2019\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: asadi2019combating\\\\n  title: \\\\\\\"Combating the Compounding-Error Problem with a Multi-step Model\\\\\\\"\\\\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\\\\n  year: 2019\\\\n  venue: \\\\\\\"arXiv:1905.13320\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: venkatraman2015improving\\\\n  title: \\\\\\\"Improving Multi-Step Prediction of Learned Time Series Models\\\\\\\"\\\\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\\\\n  year: 2015\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lambert2022investigating\\\\n  title: \\\\\\\"Investigating Compounding Prediction Errors in Learned Dynamics Models\\\\\\\"\\\\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"arXiv:2203.09637\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Model-predictive control with learned dynamics\\\\n# ============================================================\\\\n\\\\n- paper_id: chua2018pets\\\\n  title: \\\\\\\"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\\\\\\\"\\\\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: nagabandi2018neural\\\\n  title: \\\\\\\"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\\\\\\\"\\\\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\\\\n  year: 2018\\\\n  venue: ICRA\\\\n  category: background\\\\n  role: \\\\\\\"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Value overestimation mitigation\\\\n# ============================================================\\\\n\\\\n- paper_id: thrun1993issues\\\\n  title: \\\\\\\"Issues in Using Function Approximation for Reinforcement Learning\\\\\\\"\\\\n  authors: [Thrun S., Schwartz A.]\\\\n  year: 1993\\\\n  venue: \\\\\\\"Connectionist Models Summer School\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: vanhasselt2016double\\\\n  title: \\\\\\\"Deep Reinforcement Learning with Double Q-Learning\\\\\\\"\\\\n  authors: [van Hasselt H., Guez A., Silver D.]\\\\n  year: 2016\\\\n  venue: AAAI\\\\n  category: background\\\\n  role: \\\\\\\"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: fujimoto2018td3\\\\n  title: \\\\\\\"Addressing Function Approximation Error in Actor-Critic Methods\\\\\\\"\\\\n  authors: [Fujimoto S., van Hoof H., Meger D.]\\\\n  year: 2018\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: haarnoja2018sac\\\\n  title: \\\\\\\"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\\\\\\\"\\\\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\\\\n  year: 2018\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lee2021sunrise\\\\n  title: \\\\\\\"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\\\\n  year: 2021\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Delusional bias\\\\n# ============================================================\\\\n\\\\n- paper_id: lu2018nondelusional\\\\n  title: \\\\\\\"Non-delusional Q-learning and Value-Iteration\\\\\\\"\\\\n  authors: [Lu T., Schuurmans D., Boutilier C.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Hierarchical RL with learned models\\\\n# ============================================================\\\\n\\\\n- paper_id: hafner2022director\\\\n  title: \\\\\\\"Deep Hierarchical Planning from Pixels\\\\\\\"\\\\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\\\\n  year: 2022\\\\n  venue: NeurIPS\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: nachum2018hiro\\\\n  title: \\\\\\\"Data-Efficient Hierarchical Reinforcement Learning\\\\\\\"\\\\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\\\\n  year: 2018\\\\n  venue: NeurIPS\\\\n  category: background\\\\n  role: \\\\\\\"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: Action repeat / frame skip\\\\n# ============================================================\\\\n\\\\n- paper_id: braylan2015frame\\\\n  title: \\\\\\\"Frame Skip Is a Powerful Parameter for Learning to Play Atari\\\\\\\"\\\\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\\\\n  year: 2015\\\\n  venue: \\\\\\\"AAAI Workshop on Learning for General Competency in Video Games\\\\\\\"\\\\n  category: background\\\\n  role: \\\\\\\"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: lakshminarayanan2017dynamic\\\\n  title: \\\\\\\"Dynamic Action Repetition for Deep Reinforcement Learning\\\\\\\"\\\\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\\\\n  year: 2017\\\\n  venue: AAAI\\\\n  category: method-component\\\\n  role: \\\\\\\"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n- paper_id: biedenkapp2021temporl\\\\n  title: \\\\\\\"TempoRL: Learning When to Act\\\\\\\"\\\\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\\\\n  year: 2021\\\\n  venue: ICML\\\\n  category: method-component\\\\n  role: \\\\\\\"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\\\\\\\"\\\\n  relevance_score: 4\\\\n\\\\n# ============================================================\\\\n# NEW: DreamerV2\\\\n# ============================================================\\\\n\\\\n- paper_id: hafner2021dreamerv2\\\\n  title: \\\\\\\"Mastering Atari with Discrete World Models\\\\\\\"\\\\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\\\\n  year: 2021\\\\n  venue: ICLR\\\\n  category: background\\\\n  role: \\\\\\\"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n# ============================================================\\\\n# NEW: Alternative world model architectures\\\\n# ============================================================\\\\n\\\\n- paper_id: micheli2023iris\\\\n  title: \\\\\\\"Transformers are Sample-Efficient World Models\\\\\\\"\\\\n  authors: [Micheli V., Alonso E., Fleuret F.]\\\\n  year: 2023\\\\n  venue: ICLR\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: robine2023twm\\\\n  title: \\\\\\\"Transformer-based World Models Are Happy With 100k Interactions\\\\\\\"\\\\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\\\\n  year: 2023\\\\n  venue: ICLR\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n- paper_id: chen2022transdreamer\\\\n  title: \\\\\\\"TransDreamer: Reinforcement Learning with Transformer World Models\\\\\\\"\\\\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\\\\n  year: 2022\\\\n  venue: \\\\\\\"arXiv:2202.09481\\\\\\\"\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\\\\\\\"\\\\n  relevance_score: 3\\\\n\\\\n# ============================================================\\\\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\\\\n# ============================================================\\\\n\\\\n- paper_id: gumbsch2024thick\\\\n  title: \\\\\\\"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\\\\\\\"\\\\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\\\\n  year: 2024\\\\n  venue: ICLR\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\\n- paper_id: mattes2024hieros\\\\n  title: \\\\\\\"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\\\\\\\"\\\\n  authors: [Mattes P., Schlosser R., Herbrich R.]\\\\n  year: 2024\\\\n  venue: ICML\\\\n  category: direct-competitor\\\\n  role: \\\\\\\"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\\\\\\\"\\\\n  relevance_score: 5\\\\n\\\", \\\"total_chars\\\": 13210, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml\", \"content\": \"# Literature Map — event-gated-adaptive-horizon\\n# Last updated: 2026-05-14\\n# Total: 28 papers (5 existing + 23 new)\\n\\n# ============================================================\\n# EXISTING CITATIONS (already in paper.tex)\\n# ============================================================\\n\\n- paper_id: sutton1999options\\n  title: \\\"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\\\"\\n  authors: [Sutton R.S., Precup D., Singh S.]\\n  year: 1999\\n  venue: \\\"Artificial Intelligence 112(1-2):181-211\\\"\\n  category: background\\n  role: \\\"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2020dreamerv1\\n  title: \\\"Dream to Control: Learning Behaviors by Latent Imagination\\\"\\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\\n  year: 2020\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\\\"\\n  relevance_score: 5\\n\\n- paper_id: hafner2023dreamerv3\\n  title: \\\"Mastering Diverse Domains through World Models\\\"\\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\\n  year: 2023\\n  venue: \\\"arXiv:2301.04104 (Nature 2025)\\\"\\n  category: background\\n  role: \\\"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\\\"\\n  relevance_score: 5\\n\\n- paper_id: sharma2017figar\\n  title: \\\"Fine Grained Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\\n  year: 2017\\n  venue: \\\"ICLR Workshop\\\"\\n  category: method-component\\n  role: \\\"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\\\"\\n  relevance_score: 4\\n\\n- paper_id: janner2019mbpo\\n  title: \\\"When to Trust Your Model: Model-Based Policy Optimization\\\"\\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\\n  year: 2019\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Multi-step prediction error compounding\\n# ============================================================\\n\\n- paper_id: ke2019learning\\n  title: \\\"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\\\"\\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\\n  year: 2019\\n  venue: ICLR\\n  category: background\\n  role: \\\"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\\\"\\n  relevance_score: 4\\n\\n- paper_id: asadi2019combating\\n  title: \\\"Combating the Compounding-Error Problem with a Multi-step Model\\\"\\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\\n  year: 2019\\n  venue: \\\"arXiv:1905.13320\\\"\\n  category: background\\n  role: \\\"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\\\"\\n  relevance_score: 4\\n\\n- paper_id: venkatraman2015improving\\n  title: \\\"Improving Multi-Step Prediction of Learned Time Series Models\\\"\\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\\n  year: 2015\\n  venue: AAAI\\n  category: background\\n  role: \\\"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\\\"\\n  relevance_score: 3\\n\\n- paper_id: lambert2022investigating\\n  title: \\\"Investigating Compounding Prediction Errors in Learned Dynamics Models\\\"\\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\\n  year: 2022\\n  venue: \\\"arXiv:2203.09637\\\"\\n  category: background\\n  role: \\\"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Model-predictive control with learned dynamics\\n# ============================================================\\n\\n- paper_id: chua2018pets\\n  title: \\\"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\\\"\\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\\\"\\n  relevance_score: 3\\n\\n- paper_id: nagabandi2018neural\\n  title: \\\"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\\\"\\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\\n  year: 2018\\n  venue: ICRA\\n  category: background\\n  role: \\\"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Value overestimation mitigation\\n# ============================================================\\n\\n- paper_id: thrun1993issues\\n  title: \\\"Issues in Using Function Approximation for Reinforcement Learning\\\"\\n  authors: [Thrun S., Schwartz A.]\\n  year: 1993\\n  venue: \\\"Connectionist Models Summer School\\\"\\n  category: background\\n  role: \\\"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\\\"\\n  relevance_score: 4\\n\\n- paper_id: vanhasselt2016double\\n  title: \\\"Deep Reinforcement Learning with Double Q-Learning\\\"\\n  authors: [van Hasselt H., Guez A., Silver D.]\\n  year: 2016\\n  venue: AAAI\\n  category: background\\n  role: \\\"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\\\"\\n  relevance_score: 4\\n\\n- paper_id: fujimoto2018td3\\n  title: \\\"Addressing Function Approximation Error in Actor-Critic Methods\\\"\\n  authors: [Fujimoto S., van Hoof H., Meger D.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\\\"\\n  relevance_score: 4\\n\\n- paper_id: haarnoja2018sac\\n  title: \\\"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\\\"\\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\\n  year: 2018\\n  venue: ICML\\n  category: method-component\\n  role: \\\"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\\\"\\n  relevance_score: 3\\n\\n- paper_id: lee2021sunrise\\n  title: \\\"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\\\"\\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Delusional bias\\n# ============================================================\\n\\n- paper_id: lu2018nondelusional\\n  title: \\\"Non-delusional Q-learning and Value-Iteration\\\"\\n  authors: [Lu T., Schuurmans D., Boutilier C.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Hierarchical RL with learned models\\n# ============================================================\\n\\n- paper_id: hafner2022director\\n  title: \\\"Deep Hierarchical Planning from Pixels\\\"\\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\\n  year: 2022\\n  venue: NeurIPS\\n  category: direct-competitor\\n  role: \\\"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\\\"\\n  relevance_score: 4\\n\\n- paper_id: nachum2018hiro\\n  title: \\\"Data-Efficient Hierarchical Reinforcement Learning\\\"\\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\\n  year: 2018\\n  venue: NeurIPS\\n  category: background\\n  role: \\\"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: Action repeat / frame skip\\n# ============================================================\\n\\n- paper_id: braylan2015frame\\n  title: \\\"Frame Skip Is a Powerful Parameter for Learning to Play Atari\\\"\\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\\n  year: 2015\\n  venue: \\\"AAAI Workshop on Learning for General Competency in Video Games\\\"\\n  category: background\\n  role: \\\"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\\\"\\n  relevance_score: 3\\n\\n- paper_id: lakshminarayanan2017dynamic\\n  title: \\\"Dynamic Action Repetition for Deep Reinforcement Learning\\\"\\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\\n  year: 2017\\n  venue: AAAI\\n  category: method-component\\n  role: \\\"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\\\"\\n  relevance_score: 4\\n\\n- paper_id: biedenkapp2021temporl\\n  title: \\\"TempoRL: Learning When to Act\\\"\\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\\n  year: 2021\\n  venue: ICML\\n  category: method-component\\n  role: \\\"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\\\"\\n  relevance_score: 4\\n\\n# ============================================================\\n# NEW: DreamerV2\\n# ============================================================\\n\\n- paper_id: hafner2021dreamerv2\\n  title: \\\"Mastering Atari with Discrete World Models\\\"\\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\\n  year: 2021\\n  venue: ICLR\\n  category: background\\n  role: \\\"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\\\"\\n  relevance_score: 5\\n\\n# ============================================================\\n# NEW: Alternative world model architectures\\n# ============================================================\\n\\n- paper_id: micheli2023iris\\n  title: \\\"Transformers are Sample-Efficient World Models\\\"\\n  authors: [Micheli V., Alonso E., Fleuret F.]\\n  year: 2023\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\\\"\\n  relevance_score: 3\\n\\n- paper_id: robine2023twm\\n  title: \\\"Transformer-based World Models Are Happy With 100k Interactions\\\"\\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\\n  year: 2023\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\\\"\\n  relevance_score: 3\\n\\n- paper_id: chen2022transdreamer\\n  title: \\\"TransDreamer: Reinforcement Learning with Transformer World Models\\\"\\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\\n  year: 2022\\n  venue: \\\"arXiv:2202.09481\\\"\\n  category: direct-competitor\\n  role: \\\"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\\\"\\n  relevance_score: 3\\n\\n# ============================================================\\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\\n# ============================================================\\n\\n- paper_id: gumbsch2024thick\\n  title: \\\"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\\\"\\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\\n  year: 2024\\n  venue: ICLR\\n  category: direct-competitor\\n  role: \\\"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\\\"\\n  relevance_score: 5\\n\\n- paper_id: mattes2024hieros\\n  title: \\\"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\\\"\\n  authors: [Mattes P., Schlosser R., Herbrich R.]\\n  year: 2024\\n  venue: ICML\\n  category: direct-competitor\\n  role: \\\"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\\\"\\n  relevance_score: 5\\n\", \"total_chars\": 13210, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I have the existing literature_map.yaml with 28 papers. Let me search for papers related to the three angles the user wants:

1. Seed/initialization sensitivity in value overestimation
2. Stochastic instability in Dreamer-family training
3. Value overestimation as delayed failure

Let me run the web searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "7cdfca34-5c70-4282-b199-342699e3b068",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN5UPyQogx61i7ZKc6E1rT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4557,
      "cache_read_input_tokens": 24681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4557
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

_source line 11_

现有 28 篇论文。开始 4 组文献搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "503ddb41-60ef-462c-bbed-a670556b350c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN5UPyQogx61i7ZKc6E1rT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4557,
      "cache_read_input_tokens": 24681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4557
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sc9fRbSAt5psbd5Tf8PtQU`</summary>

```json
{
  "query": "\"value overestimation\" \"seed-dependent\" \"model-based reinforcement learning\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "c996609c-fbfe-46ee-966f-ad3d6c117652",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN5UPyQogx61i7ZKc6E1rT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4557,
      "cache_read_input_tokens": 24681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4557
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FkhqqTuSnvT1uKTpSHMi89`</summary>

```json
{
  "query": "\"DreamerV3\" OR \"Dreamer\" \"training instability\" \"seed variance\" reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "b5164219-e048-40de-9e2f-986631303ed7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN5UPyQogx61i7ZKc6E1rT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4557,
      "cache_read_input_tokens": 24681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4557
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WmZQ3YA8BcF4LbjcS55Bpf`</summary>

```json
{
  "query": "\"delusional\" \"critic\" \"model-based\" \"initialization sensitivity\" reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "91da3e3a-c918-4bcb-89e5-8f824333cd86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN5UPyQogx61i7ZKc6E1rT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4557,
      "cache_read_input_tokens": 24681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4557
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RDfMTeunxk7viUuZ9QmaSq`</summary>

```json
{
  "query": "\"imagination\" \"value overestimation\" \"stochastic\" \"failure mode\" model-based RL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "d0a8da24-50a0-4f6f-9989-960ea478825f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN5UPyQogx61i7ZKc6E1rT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4557,
      "cache_read_input_tokens": 24681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4557
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

_source line 16 · 2026-05-14T14:28:17.571Z_

<details><summary>↩ Tool result · `toolu_01Sc9fRbSAt5psbd5Tf8PtQU`</summary>

```text
Web search results for query: ""value overestimation" "seed-dependent" "model-based reinforcement learning""

No links found.

I performed a web search with your exact query, but it did not return any results. This suggests that this specific combination of terms may not appear together in publicly indexed web content, or the topic may be quite specialized or recent.

If you're researching this topic, you might try:
- Searching for fewer terms at once (e.g., just "seed-dependent" and "model-based reinforcement learning")
- Searching for related concepts like "value overestimation" and "reinforcement learning"
- Looking in academic databases like ArXiv, Google Scholar, or conference proceedings (ICML, NeurIPS, etc.)
- Checking recent reinforcement learning papers or blogs that discuss bias and value estimation issues

Would you like me to search with a modified query or help you explore this topic differently?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "f4812487-b5c5-4467-95c2-02263a8016ae",
  "tool_use_result": {
    "query": "\"value overestimation\" \"seed-dependent\" \"model-based reinforcement learning\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NtwnKFEHGMsWiSMnJApX3k",
        "content": []
      },
      "I performed a web search with your exact query, but it did not return any results. This suggests that this specific combination of terms may not appear together in publicly indexed web content, or the topic may be quite specialized or recent.\n\nIf you're researching this topic, you might try:\n- Searching for fewer terms at once (e.g., just \"seed-dependent\" and \"model-based reinforcement learning\")\n- Searching for related concepts like \"value overestimation\" and \"reinforcement learning\"\n- Looking in academic databases like ArXiv, Google Scholar, or conference proceedings (ICML, NeurIPS, etc.)\n- Checking recent reinforcement learning papers or blogs that discuss bias and value estimation issues\n\nWould you like me to search with a modified query or help you explore this topic differently?"
    ],
    "durationSeconds": 4.021120251
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T14:28:21.876Z_

<details><summary>↩ Tool result · `toolu_01WmZQ3YA8BcF4LbjcS55Bpf`</summary>

```text
Web search results for query: ""delusional" "critic" "model-based" "initialization sensitivity" reinforcement learning"

Links: [{"title":"Policy Gradient Algorithms | Lil'Log","url":"https://lilianweng.github.io/posts/2018-04-08-policy-gradient/"},{"title":"ConQUR: Mitigating Delusional Bias in Deep Q-Learning | OpenReview","url":"https://openreview.net/forum?id=ryg8WJSKPr"},{"title":"DeepCritic: Deliberate Critique with Large Language Models","url":"https://arxiv.org/html/2505.00662v1"},{"title":"Shaking the foundations: delusions in sequence models for interaction and control","url":"https://www.academia.edu/80458066/Shaking_the_foundations_delusions_in_sequence_models_for_interaction_and_control"},{"title":"Improving Rationality in the Reasoning Process of ...","url":"https://www.arxiv.org/pdf/2506.22920"},{"title":"Policy-shaped prediction: avoiding distractions in model-based reinforcement learning","url":"https://arxiv.org/html/2412.05766v1"},{"title":"Simulating AI Psychosis, Delusion Reinforcement and ...","url":"https://arxiv.org/pdf/2509.10970"},{"title":"Beyond Hype: The Brutal Truth About Deep Reinforcement Learning | by Aethelios | Medium","url":"https://medium.com/@Aethelios/beyond-hype-the-brutal-truth-about-deep-reinforcement-learning-a9b408ffaf4a"},{"title":"The Psychogenic Machine: Simulating AI Psychosis, Delusion Reinforcement and Harm Enablement in Large Language Models","url":"https://arxiv.org/html/2509.10970v1"},{"title":"Teaching Language Models to Critique via Reinforcement Learning","url":"https://arxiv.org/html/2502.03492v1"}]

I found search results related to your query. Here's what the search returned:

The most relevant result appears to be research on "ConQUR" which developed methods to mitigate delusional bias, described as "a fundamental source of error in approximate Q-learning."

The work develops efficient methods to mitigate delusional bias by training Q-approximators with labels consistent with the underlying greedy policy class, introducing a penalization scheme that encourages Q-labels to remain consistent with the expressible policy class, and proposing a search framework that allows multiple Q-approximators to be generated and tracked.

Regarding initialization sensitivity in reinforcement learning more broadly, research indicates that policy is sensitive to initialization when there are locally optimal actions close to initialization. Additionally, the performance of deep reinforcement learning algorithms is notoriously sensitive to the choice of numerous hyperparameters including learning rates for actor and critic networks, and even minor changes can lead to drastically different performance outcomes.

The search results also contained information about model-based reinforcement learning and critic networks in various contexts, though they don't all directly address the intersection of all four terms in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "1f746053-fae2-40dd-bb6d-9e78242f756b",
  "tool_use_result": {
    "query": "\"delusional\" \"critic\" \"model-based\" \"initialization sensitivity\" reinforcement learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Cqn1Ky5gSq5ZRcWipubNsE",
        "content": [
          {
            "title": "Policy Gradient Algorithms | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2018-04-08-policy-gradient/"
          },
          {
            "title": "ConQUR: Mitigating Delusional Bias in Deep Q-Learning | OpenReview",
            "url": "https://openreview.net/forum?id=ryg8WJSKPr"
          },
          {
            "title": "DeepCritic: Deliberate Critique with Large Language Models",
            "url": "https://arxiv.org/html/2505.00662v1"
          },
          {
            "title": "Shaking the foundations: delusions in sequence models for interaction and control",
            "url": "https://www.academia.edu/80458066/Shaking_the_foundations_delusions_in_sequence_models_for_interaction_and_control"
          },
          {
            "title": "Improving Rationality in the Reasoning Process of ...",
            "url": "https://www.arxiv.org/pdf/2506.22920"
          },
          {
            "title": "Policy-shaped prediction: avoiding distractions in model-based reinforcement learning",
            "url": "https://arxiv.org/html/2412.05766v1"
          },
          {
            "title": "Simulating AI Psychosis, Delusion Reinforcement and ...",
            "url": "https://arxiv.org/pdf/2509.10970"
          },
          {
            "title": "Beyond Hype: The Brutal Truth About Deep Reinforcement Learning | by Aethelios | Medium",
            "url": "https://medium.com/@Aethelios/beyond-hype-the-brutal-truth-about-deep-reinforcement-learning-a9b408ffaf4a"
          },
          {
            "title": "The Psychogenic Machine: Simulating AI Psychosis, Delusion Reinforcement and Harm Enablement in Large Language Models",
            "url": "https://arxiv.org/html/2509.10970v1"
          },
          {
            "title": "Teaching Language Models to Critique via Reinforcement Learning",
            "url": "https://arxiv.org/html/2502.03492v1"
          }
        ]
      },
      "I found search results related to your query. Here's what the search returned:\n\nThe most relevant result appears to be research on \"ConQUR\" which developed methods to mitigate delusional bias, described as \"a fundamental source of error in approximate Q-learning.\"\n\nThe work develops efficient methods to mitigate delusional bias by training Q-approximators with labels consistent with the underlying greedy policy class, introducing a penalization scheme that encourages Q-labels to remain consistent with the expressible policy class, and proposing a search framework that allows multiple Q-approximators to be generated and tracked.\n\nRegarding initialization sensitivity in reinforcement learning more broadly, research indicates that policy is sensitive to initialization when there are locally optimal actions close to initialization. Additionally, the performance of deep reinforcement learning algorithms is notoriously sensitive to the choice of numerous hyperparameters including learning rates for actor and critic networks, and even minor changes can lead to drastically different performance outcomes.\n\nThe search results also contained information about model-based reinforcement learning and critic networks in various contexts, though they don't all directly address the intersection of all four terms in your query."
    ],
    "durationSeconds": 6.886155978000002
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T14:28:22.027Z_

<details><summary>↩ Tool result · `toolu_01FkhqqTuSnvT1uKTpSHMi89`</summary>

```text
Web search results for query: ""DreamerV3" OR "Dreamer" "training instability" "seed variance" reinforcement learning"

Links: [{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://arxiv.org/html/2510.21418v1"},{"title":"Mastering Diverse Control Tasks through World Models","url":"https://danijar.com/project/dreamerv3/"},{"title":"DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"},{"title":"DreamerV3: Model-Based RL Algorithm","url":"https://www.emergentmind.com/topics/dreamerv3-algorithm"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"}]

Based on the search results, I found relevant information about DreamerV3 and training stability:

## DreamerV3 and Training Stability

DreamerV3 employs a "bag of tricks" to stabilize and normalize learning across a wide range of environments. Rather than making significant algorithmic changes from previous versions, the focus has been on robustness mechanisms.

The robustness techniques introduced include observation symlog, KL balance and free bits, 1% unimix for all categoricals, percentile return normalization, symexp twohot loss for the reward head and critic. Additional improvements include Block GRU architecture, RMSNorm normalization, SiLu activation, and adaptive gradient clipping (AGC) with LaProp optimizer.

Robustness techniques based on normalization, balancing and transformations enable stable learning across domains. These mechanisms enable DreamerV3 to operate robustly without the domain-specific norm schedules and KL annealing critical to previous Dreamer variants.

## Seed Variance and Reproducibility

The research demonstrates awareness of seed variance in evaluations. Experiments run 5 seeds for each Dreamer and PPO per benchmark, with curves showing the mean over seeds with one standard deviation shaded. Additionally, some results can be attributed to variance from fewer runs, with research using two seeds compared to five seeds in the DreamerV3 paper.

The comprehensive robustness improvements in DreamerV3 appear to address the need for more stable training across diverse reinforcement learning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "f0c1740d-7f40-4f22-b051-ba63aa78cd39",
  "tool_use_result": {
    "query": "\"DreamerV3\" OR \"Dreamer\" \"training instability\" \"seed variance\" reinforcement learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_015bQ34pTZrDE9rz5Ca1sHqH",
        "content": [
          {
            "title": "DreamerV3: Mastering Diverse Domains through World Models",
            "url": "https://vitalab.github.io/article/2023/01/19/DreamerV3.html"
          },
          {
            "title": "GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub",
            "url": "https://github.com/danijar/dreamerv3"
          },
          {
            "title": "[2301.04104] Mastering Diverse Domains through World Models",
            "url": "https://arxiv.org/abs/2301.04104"
          },
          {
            "title": "Mastering Diverse Domains through World Models",
            "url": "https://arxiv.org/pdf/2301.04104"
          },
          {
            "title": "Mastering diverse control tasks through world models | Nature",
            "url": "https://www.nature.com/articles/s41586-025-08744-2"
          },
          {
            "title": "DreamerV3-XP: Optimizing exploration through uncertainty estimation",
            "url": "https://arxiv.org/html/2510.21418v1"
          },
          {
            "title": "Mastering Diverse Control Tasks through World Models",
            "url": "https://danijar.com/project/dreamerv3/"
          },
          {
            "title": "DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"
          },
          {
            "title": "DreamerV3: Model-Based RL Algorithm",
            "url": "https://www.emergentmind.com/topics/dreamerv3-algorithm"
          },
          {
            "title": "Mastering diverse control tasks through world models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"
          }
        ]
      },
      "Based on the search results, I found relevant information about DreamerV3 and training stability:\n\n## DreamerV3 and Training Stability\n\nDreamerV3 employs a \"bag of tricks\" to stabilize and normalize learning across a wide range of environments. Rather than making significant algorithmic changes from previous versions, the focus has been on robustness mechanisms.\n\nThe robustness techniques introduced include observation symlog, KL balance and free bits, 1% unimix for all categoricals, percentile return normalization, symexp twohot loss for the reward head and critic. Additional improvements include Block GRU architecture, RMSNorm normalization, SiLu activation, and adaptive gradient clipping (AGC) with LaProp optimizer.\n\nRobustness techniques based on normalization, balancing and transformations enable stable learning across domains. These mechanisms enable DreamerV3 to operate robustly without the domain-specific norm schedules and KL annealing critical to previous Dreamer variants.\n\n## Seed Variance and Reproducibility\n\nThe research demonstrates awareness of seed variance in evaluations. Experiments run 5 seeds for each Dreamer and PPO per benchmark, with curves showing the mean over seeds with one standard deviation shaded. Additionally, some results can be attributed to variance from fewer runs, with research using two seeds compared to five seeds in the DreamerV3 paper.\n\nThe comprehensive robustness improvements in DreamerV3 appear to address the need for more stable training across diverse reinforcement learning tasks."
    ],
    "durationSeconds": 7.504867615999999
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T14:28:24.638Z_

<details><summary>↩ Tool result · `toolu_01RDfMTeunxk7viUuZ9QmaSq`</summary>

```text
Web search results for query: ""imagination" "value overestimation" "stochastic" "failure mode" model-based RL"

Links: [{"title":"Week 5: Model-Based Methods - Deep RL Course","url":"https://deeprlcourse.github.io/course_notes/model-based/"},{"title":"Model-Based Value Expansion for Efficient Model-Free RL","url":"https://mugoh.github.io/log/paper-summaries/mve/"},{"title":"Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning","url":"https://proceedings.nips.cc/paper_files/paper/2020/file/661b1e76b95cc50a7a11a85619a67d95-Paper.pdf"},{"title":"Model-Based Reinforcement Learning — DI-engine 0.1.0 documentation","url":"https://opendilab.github.io/DI-engine/02_algo/model_based_rl.html"},{"title":"Model-Based Offline Reinforcement Learning With Uncertainty Estimation and Policy Constraint | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10459064/"},{"title":"GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-model-based-RL"},{"title":"Uncertainty-Aware RWM","url":"https://sites.google.com/view/uncertainty-aware-rwm/home"},{"title":"Model-Based Reinforcement Learning via Imagination with Derived Memory | OpenReview","url":"https://openreview.net/forum?id=jeATherHHGj"},{"title":"Model-Based Reinforcement Learning via Imagination with Derived Memory Yao Mu","url":"https://proceedings.neurips.cc/paper/2021/file/4ebccfb3e317c7789f04f7a558df4537-Paper.pdf"},{"title":"TD3: Overcoming Overestimation in Deep Reinforcement Learning | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/td3-overcoming-overestimation-in-deep-reinforcement-learning-c52d1cc9d69a"}]

I've performed a web search for your query on "imagination," "value overestimation," "stochastic," "failure mode," and model-based RL. Here are the most relevant findings:

## Key Results

**Value Overestimation and Model Exploitation in Model-Based RL:**

Model-based RL faces a key challenge where the policy can exploit inaccuracies in the model, particularly when the model overestimates rewards in regions with sparse coverage due to limited training data.

**Imagination-Based Learning and Failure Modes:**

When uncertainty is not properly constrained, policies can exploit imperfections in learned models and inflate rewards purely in imagination, becoming overconfident in hallucinated rollouts and optimizing toward behaviors that violate real robot dynamics, resulting in unstable walking, unintended collisions, or complete breakdown of locomotion despite high imagined returns.

**Stochastic Error Accumulation:**

Even with a stochastic model, errors can accumulate as predictions are fed back into the model during multi-step rollouts. Errors compound during long autoregressive rollouts, and policies will optimize against hallucinated dynamics unless explicitly informed about what is unreliable.

**Mitigation Strategies:**

Model-based value expansion controls for uncertainty in the model by only allowing imagination to a fixed depth, using learned dynamics in model-free RL algorithms to improve value estimation and reduce sample complexity. Additionally, tracking epistemic uncertainty during imagination and keeping rollouts within regions where learned dynamics remain trustworthy can leverage calibrated uncertainty to steadily increase imagination reward while avoiding exploitation of model errors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "745a4ffc-de06-41f3-9c46-b13011a27c56",
  "tool_use_result": {
    "query": "\"imagination\" \"value overestimation\" \"stochastic\" \"failure mode\" model-based RL",
    "results": [
      {
        "tool_use_id": "srvtoolu_013T745d7Q9hk6ua4Nd7YXPJ",
        "content": [
          {
            "title": "Week 5: Model-Based Methods - Deep RL Course",
            "url": "https://deeprlcourse.github.io/course_notes/model-based/"
          },
          {
            "title": "Model-Based Value Expansion for Efficient Model-Free RL",
            "url": "https://mugoh.github.io/log/paper-summaries/mve/"
          },
          {
            "title": "Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning",
            "url": "https://proceedings.nips.cc/paper_files/paper/2020/file/661b1e76b95cc50a7a11a85619a67d95-Paper.pdf"
          },
          {
            "title": "Model-Based Reinforcement Learning — DI-engine 0.1.0 documentation",
            "url": "https://opendilab.github.io/DI-engine/02_algo/model_based_rl.html"
          },
          {
            "title": "Model-Based Offline Reinforcement Learning With Uncertainty Estimation and Policy Constraint | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/10459064/"
          },
          {
            "title": "GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-model-based-RL"
          },
          {
            "title": "Uncertainty-Aware RWM",
            "url": "https://sites.google.com/view/uncertainty-aware-rwm/home"
          },
          {
            "title": "Model-Based Reinforcement Learning via Imagination with Derived Memory | OpenReview",
            "url": "https://openreview.net/forum?id=jeATherHHGj"
          },
          {
            "title": "Model-Based Reinforcement Learning via Imagination with Derived Memory Yao Mu",
            "url": "https://proceedings.neurips.cc/paper/2021/file/4ebccfb3e317c7789f04f7a558df4537-Paper.pdf"
          },
          {
            "title": "TD3: Overcoming Overestimation in Deep Reinforcement Learning | by Dong-Keon Kim | Medium",
            "url": "https://medium.com/@kdk199604/td3-overcoming-overestimation-in-deep-reinforcement-learning-c52d1cc9d69a"
          }
        ]
      },
      "I've performed a web search for your query on \"imagination,\" \"value overestimation,\" \"stochastic,\" \"failure mode,\" and model-based RL. Here are the most relevant findings:\n\n## Key Results\n\n**Value Overestimation and Model Exploitation in Model-Based RL:**\n\nModel-based RL faces a key challenge where the policy can exploit inaccuracies in the model, particularly when the model overestimates rewards in regions with sparse coverage due to limited training data.\n\n**Imagination-Based Learning and Failure Modes:**\n\nWhen uncertainty is not properly constrained, policies can exploit imperfections in learned models and inflate rewards purely in imagination, becoming overconfident in hallucinated rollouts and optimizing toward behaviors that violate real robot dynamics, resulting in unstable walking, unintended collisions, or complete breakdown of locomotion despite high imagined returns.\n\n**Stochastic Error Accumulation:**\n\nEven with a stochastic model, errors can accumulate as predictions are fed back into the model during multi-step rollouts. Errors compound during long autoregressive rollouts, and policies will optimize against hallucinated dynamics unless explicitly informed about what is unreliable.\n\n**Mitigation Strategies:**\n\nModel-based value expansion controls for uncertainty in the model by only allowing imagination to a fixed depth, using learned dynamics in model-free RL algorithms to improve value estimation and reduce sample complexity. Additionally, tracking epistemic uncertainty during imagination and keeping rollouts within regions where learned dynamics remain trustworthy can leverage calibrated uncertainty to steadily increase imagination reward while avoiding exploitation of model errors."
    ],
    "durationSeconds": 9.060086052000003
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
The first search didn't find anything. Let me do more targeted searches to find specific papers about seed sensitivity in RL training, value overestimation variance, and delayed failure modes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "7802c605-3983-4278-9920-91c73d963132",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDQvNWK34XqvStdLwV7WD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3196,
      "cache_read_input_tokens": 29238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3196
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

_source line 21_

初步搜索没有直接命中 "seed-dependent value overestimation" 的论文。扩大搜索范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "274ff6f3-40d3-4fc0-8368-95ee3b253ab6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDQvNWK34XqvStdLwV7WD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3196,
      "cache_read_input_tokens": 29238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3196
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

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RqyQVAnmnqJXCgkXprbdMn`</summary>

```json
{
  "query": "reinforcement learning \"seed sensitivity\" \"value overestimation\" variance deep RL arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "c0e23f4c-1f2d-4ed5-a1c6-b0e6e553b3a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDQvNWK34XqvStdLwV7WD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3196,
      "cache_read_input_tokens": 29238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3196
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

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Miwk69xNn1yCmsCmk86kLB`</summary>

```json
{
  "query": "\"model-based reinforcement learning\" \"value overestimation\" \"delayed collapse\" OR \"delayed failure\" OR \"progressive\" training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "09d1fc01-15a7-4446-9809-9334a9d024cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDQvNWK34XqvStdLwV7WD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3196,
      "cache_read_input_tokens": 29238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3196
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RHZ911Y6rY3NUnjBKcefKC`</summary>

```json
{
  "query": "Henderson 2018 \"deep reinforcement learning that matters\" seed variance reproducibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "e6126f37-f499-4e64-980c-085e8602e633",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDQvNWK34XqvStdLwV7WD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3196,
      "cache_read_input_tokens": 29238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3196
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CG5zDve15M7vrUkz12vTDi`</summary>

```json
{
  "query": "\"Dreamer\" OR \"world model\" \"high variance\" seeds \"performance collapse\" reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "fbf842e8-f088-4db9-aa20-cc6ad3b0f922",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDQvNWK34XqvStdLwV7WD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3196,
      "cache_read_input_tokens": 29238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3196
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

_source line 26 · 2026-05-14T14:28:38.373Z_

<details><summary>↩ Tool result · `toolu_01Miwk69xNn1yCmsCmk86kLB`</summary>

```text
Web search results for query: ""model-based reinforcement learning" "value overestimation" "delayed collapse" OR "delayed failure" OR "progressive" training"

Links: [{"title":"TD3: Overcoming Overestimation in Deep Reinforcement Learning | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/td3-overcoming-overestimation-in-deep-reinforcement-learning-c52d1cc9d69a"},{"title":"Examinations of Biases by Model Misspecification and Parameter Reliability of Reinforcement Learning Models | Computational Brain & Behavior | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s42113-023-00175-4"},{"title":"Parameter-Free Reduction of the Estimation Bias in Deep Reinforcement Learning for Deterministic Policy Gradients | Neural Processing Letters | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11063-024-11461-y"},{"title":"Model-Based Reinforcement Learning","url":"https://www.emergentmind.com/topics/model-based-reinforcement-learning-rl"},{"title":"[2410.08315] Avoiding mode collapse in diffusion models fine-tuned with reinforcement learning","url":"https://arxiv.org/abs/2410.08315"},{"title":"Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers | OpenReview","url":"https://openreview.net/forum?id=6LORvHYkV3"},{"title":"Model-Based Reinforcement Learning:Theory and Practice – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2019/12/12/mbpo/"},{"title":"Understanding reinforcement learning for model training from scratch | by Rohit Patel | Data Science Collective | Medium","url":"https://medium.com/data-science-collective/understanding-reinforcement-learning-for-model-training-from-scratch-8bffe8d87a07"},{"title":"Predictive representations can link model-based reinforcement learning to model-free mechanisms - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5628940/"},{"title":"Model-Based Reinforcement Learning - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/computer-science/model-based-reinforcement-learning"}]

I've completed the web search for your query. The results cover several relevant topics related to your search terms:

**Key Findings:**

1. **Value Overestimation in Reinforcement Learning**: The Twin Delayed Deep Deterministic Policy Gradient (TD3) algorithm addresses overestimation bias in actor-critic reinforcement learning, particularly in continuous control domains. A significant challenge in temporal difference learning is the accumulation of approximation errors over time—each Q-value estimate depends on the estimated value of the next state, and as training progresses, these small errors compound, leading to high-variance, unstable learning dynamics.

2. **Model-Based RL Challenges**: Safe and robust planning in model-based RL involves incorporating state and action constraints, risk-aware value estimation, and adversarial training to prevent catastrophic failures due to off-model exploitation or compounding estimation errors.

3. **Progressive Training Approaches**: One approach addresses training instability in diffusion models with RL by training them dynamically at each epoch with a tailored RL method, allowing for continual evaluation and step-by-step refinement of model performance.

4. **Estimation Error Dynamics**: Approximate critics overestimate actual Q-values at initial steps, but when the agent starts exploring and encounters varying rewards, the variance of value estimates increases and underestimation bias starts growing.

The search results focus primarily on value overestimation in deep RL and model-based methods, though they don't specifically address papers on "delayed collapse" terminology in the exact context of your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "79ff09ed-d818-4c5d-9811-4b5142f61978",
  "tool_use_result": {
    "query": "\"model-based reinforcement learning\" \"value overestimation\" \"delayed collapse\" OR \"delayed failure\" OR \"progressive\" training",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WKyAfCB98fshMe7Ak3xmbc",
        "content": [
          {
            "title": "TD3: Overcoming Overestimation in Deep Reinforcement Learning | by Dong-Keon Kim | Medium",
            "url": "https://medium.com/@kdk199604/td3-overcoming-overestimation-in-deep-reinforcement-learning-c52d1cc9d69a"
          },
          {
            "title": "Examinations of Biases by Model Misspecification and Parameter Reliability of Reinforcement Learning Models | Computational Brain & Behavior | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s42113-023-00175-4"
          },
          {
            "title": "Parameter-Free Reduction of the Estimation Bias in Deep Reinforcement Learning for Deterministic Policy Gradients | Neural Processing Letters | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11063-024-11461-y"
          },
          {
            "title": "Model-Based Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/model-based-reinforcement-learning-rl"
          },
          {
            "title": "[2410.08315] Avoiding mode collapse in diffusion models fine-tuned with reinforcement learning",
            "url": "https://arxiv.org/abs/2410.08315"
          },
          {
            "title": "Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers | OpenReview",
            "url": "https://openreview.net/forum?id=6LORvHYkV3"
          },
          {
            "title": "Model-Based Reinforcement Learning:Theory and Practice – The Berkeley Artificial Intelligence Research Blog",
            "url": "https://bair.berkeley.edu/blog/2019/12/12/mbpo/"
          },
          {
            "title": "Understanding reinforcement learning for model training from scratch | by Rohit Patel | Data Science Collective | Medium",
            "url": "https://medium.com/data-science-collective/understanding-reinforcement-learning-for-model-training-from-scratch-8bffe8d87a07"
          },
          {
            "title": "Predictive representations can link model-based reinforcement learning to model-free mechanisms - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5628940/"
          },
          {
            "title": "Model-Based Reinforcement Learning - an overview | ScienceDirect Topics",
            "url": "https://www.sciencedirect.com/topics/computer-science/model-based-reinforcement-learning"
          }
        ]
      },
      "I've completed the web search for your query. The results cover several relevant topics related to your search terms:\n\n**Key Findings:**\n\n1. **Value Overestimation in Reinforcement Learning**: The Twin Delayed Deep Deterministic Policy Gradient (TD3) algorithm addresses overestimation bias in actor-critic reinforcement learning, particularly in continuous control domains. A significant challenge in temporal difference learning is the accumulation of approximation errors over time—each Q-value estimate depends on the estimated value of the next state, and as training progresses, these small errors compound, leading to high-variance, unstable learning dynamics.\n\n2. **Model-Based RL Challenges**: Safe and robust planning in model-based RL involves incorporating state and action constraints, risk-aware value estimation, and adversarial training to prevent catastrophic failures due to off-model exploitation or compounding estimation errors.\n\n3. **Progressive Training Approaches**: One approach addresses training instability in diffusion models with RL by training them dynamically at each epoch with a tailored RL method, allowing for continual evaluation and step-by-step refinement of model performance.\n\n4. **Estimation Error Dynamics**: Approximate critics overestimate actual Q-values at initial steps, but when the agent starts exploring and encounters varying rewards, the variance of value estimates increases and underestimation bias starts growing.\n\nThe search results focus primarily on value overestimation in deep RL and model-based methods, though they don't specifically address papers on \"delayed collapse\" terminology in the exact context of your query."
    ],
    "durationSeconds": 7.338716279
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T14:28:38.561Z_

<details><summary>↩ Tool result · `toolu_01RHZ911Y6rY3NUnjBKcefKC`</summary>

```text
Web search results for query: "Henderson 2018 "deep reinforcement learning that matters" seed variance reproducibility"

Links: [{"title":"Deep reinforcement learning that matters | Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence and Thirtieth Innovative Applications of Artificial Intelligence Conference and Eighth AAAI Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/abs/10.5555/3504035.3504427"},{"title":"[1709.06560] Deep Reinforcement Learning that Matters","url":"https://arxiv.org/abs/1709.06560"},{"title":"Deep reinforcement learning that matters - Princeton University","url":"https://collaborate.princeton.edu/en/publications/deep-reinforcement-learning-that-matters/"},{"title":"Deep Reinforcement Learning that Matters (1709.06560v3)","url":"https://www.emergentmind.com/papers/1709.06560"},{"title":"[PDF] Deep Reinforcement Learning that Matters | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Reinforcement-Learning-that-Matters-Henderson-Islam/33690ff21ef1efb576410e656f2e60c89d0307d6"},{"title":"(PDF) Deep Reinforcement Learning That Matters","url":"https://www.researchgate.net/publication/319953023_Deep_Reinforcement_Learning_That_Matters"},{"title":"Deep Reinforcement Learning That Matters | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/11694"},{"title":"Deep Reinforcement Learning that Matters","url":"https://arxiv.org/pdf/1709.06560"},{"title":"Variability of Deep Reinforcement Learning Agents in Atari ...","url":"https://people.cs.umass.edu/~kclary/NeurIPS_Critiquing_Trends_Workshop_2018___Variability_of_Deep_RL.pdf"},{"title":"Reproducibility in Deep RL | Advanced RL","url":"https://apxml.com/courses/advanced-reinforcement-learning/chapter-8-rl-implementation-optimization/reproducibility-deep-rl"}]

Here are the search results for Henderson 2018 "Deep Reinforcement Learning that Matters" regarding seed variance and reproducibility:

## Paper Overview

The paper by Peter Henderson, Riashat Islam, Philip Bachman and colleagues was presented at the 32nd AAAI Conference on Artificial Intelligence in 2018. The work addresses that reproducing results for state-of-the-art deep RL methods is seldom straightforward, and in particular, non-determinism in standard benchmark environments, combined with variance intrinsic to the methods, can make reported results tough to interpret.

## Key Findings on Seed Variance

The paper reveals that random seed variability can lead to substantial differences in results, highlighting the need for multiple trial evaluations. More specifically, statistically different distributions can be attained just from the random seeds with the same exact hyperparameters.

## Main Contributions

The paper illustrates the variability in reported metrics and results when comparing against common baselines and suggests guidelines to make future results in deep RL more reproducible. The recommendations include: consistent reporting of all hyperparameters and implementation details, reporting average performance across multiple trials with different random seeds to mitigate variability, and using statistical methods to evaluate the significance of performance gains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "ffda4e8e-4c9b-47c8-b340-86ad11bde743",
  "tool_use_result": {
    "query": "Henderson 2018 \"deep reinforcement learning that matters\" seed variance reproducibility",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FYTQyN4UjqLgxD28tzfc5j",
        "content": [
          {
            "title": "Deep reinforcement learning that matters | Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence and Thirtieth Innovative Applications of Artificial Intelligence Conference and Eighth AAAI Symposium on Educational Advances in Artificial Intelligence",
            "url": "https://dl.acm.org/doi/abs/10.5555/3504035.3504427"
          },
          {
            "title": "[1709.06560] Deep Reinforcement Learning that Matters",
            "url": "https://arxiv.org/abs/1709.06560"
          },
          {
            "title": "Deep reinforcement learning that matters - Princeton University",
            "url": "https://collaborate.princeton.edu/en/publications/deep-reinforcement-learning-that-matters/"
          },
          {
            "title": "Deep Reinforcement Learning that Matters (1709.06560v3)",
            "url": "https://www.emergentmind.com/papers/1709.06560"
          },
          {
            "title": "[PDF] Deep Reinforcement Learning that Matters | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Deep-Reinforcement-Learning-that-Matters-Henderson-Islam/33690ff21ef1efb576410e656f2e60c89d0307d6"
          },
          {
            "title": "(PDF) Deep Reinforcement Learning That Matters",
            "url": "https://www.researchgate.net/publication/319953023_Deep_Reinforcement_Learning_That_Matters"
          },
          {
            "title": "Deep Reinforcement Learning That Matters | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/11694"
          },
          {
            "title": "Deep Reinforcement Learning that Matters",
            "url": "https://arxiv.org/pdf/1709.06560"
          },
          {
            "title": "Variability of Deep Reinforcement Learning Agents in Atari ...",
            "url": "https://people.cs.umass.edu/~kclary/NeurIPS_Critiquing_Trends_Workshop_2018___Variability_of_Deep_RL.pdf"
          },
          {
            "title": "Reproducibility in Deep RL | Advanced RL",
            "url": "https://apxml.com/courses/advanced-reinforcement-learning/chapter-8-rl-implementation-optimization/reproducibility-deep-rl"
          }
        ]
      },
      "Here are the search results for Henderson 2018 \"Deep Reinforcement Learning that Matters\" regarding seed variance and reproducibility:\n\n## Paper Overview\n\nThe paper by Peter Henderson, Riashat Islam, Philip Bachman and colleagues was presented at the 32nd AAAI Conference on Artificial Intelligence in 2018. The work addresses that reproducing results for state-of-the-art deep RL methods is seldom straightforward, and in particular, non-determinism in standard benchmark environments, combined with variance intrinsic to the methods, can make reported results tough to interpret.\n\n## Key Findings on Seed Variance\n\nThe paper reveals that random seed variability can lead to substantial differences in results, highlighting the need for multiple trial evaluations. More specifically, statistically different distributions can be attained just from the random seeds with the same exact hyperparameters.\n\n## Main Contributions\n\nThe paper illustrates the variability in reported metrics and results when comparing against common baselines and suggests guidelines to make future results in deep RL more reproducible. The recommendations include: consistent reporting of all hyperparameters and implementation details, reporting average performance across multiple trials with different random seeds to mitigate variability, and using statistical methods to evaluate the significance of performance gains."
    ],
    "durationSeconds": 7.063359915000001
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T14:28:39.958Z_

<details><summary>↩ Tool result · `toolu_01RqyQVAnmnqJXCgkXprbdMn`</summary>

```text
Web search results for query: "reinforcement learning "seed sensitivity" "value overestimation" variance deep RL arXiv"

Links: [{"title":"On the Reduction of Variance and Overestimation of Deep Q-Learning","url":"https://arxiv.org/html/1910.05983v2"},{"title":"Dissecting Deep RL with High Update Ratios: Combatting Value Overestimation and Divergence","url":"https://arxiv.org/html/2403.05996v1"},{"title":"A Controlled Study of Double DQN and Dueling DQN Under Cross-Environment Transfer","url":"https://arxiv.org/html/2602.09810"},{"title":"Distributional Soft Actor-Critic with Three Refinements","url":"https://arxiv.org/html/2310.05858.pdf"},{"title":"[1910.06591] SEED RL: Scalable and Efficient Deep-RL with Accelerated Central Inference","url":"https://arxiv.org/abs/1910.06591"},{"title":"[1910.05983] On the Reduction of Variance and Overestimation of Deep Q-Learning","url":"https://arxiv.org/abs/1910.05983"},{"title":"Averaged-DQN: Variance Reduction and Stabilization for ...","url":"https://arxiv.org/pdf/1611.01929"},{"title":"Abstract","url":"https://arxiv.org/html/2510.14503"},{"title":"Deep Reinforcement Learning that Matters","url":"https://arxiv.org/pdf/1709.06560"},{"title":"On the consistency of hyper-parameter selection in value-based deep reinforcement learning","url":"https://arxiv.org/html/2406.17523v1"}]

I found several relevant research papers on arXiv addressing reinforcement learning challenges related to seed sensitivity, value overestimation, and variance in deep RL:

## Key Papers Found:

1. **"On the Reduction of Variance and Overestimation of Deep Q-Learning"** (arXiv:1910.05983) - This paper addresses how many extensions to deep Q-Learning algorithm have been proposed to reduce the variance of the target values and the overestimation phenomena. The authors propose using Dropout techniques on deep Q-Learning algorithm as a way to reduce variance and overestimation.

2. **"Dissecting Deep RL with High Update Ratios: Combatting Value Overestimation and Divergence"** (arXiv:2403.05996) - This work shows that Q-value divergence can arise due to problems inherent to neural network optimization, and this optimization-caused divergence can be mitigated using the unit-ball normalization approach.

3. **"A Controlled Study of Double DQN and Dueling DQN Under Cross-Environment Transfer"** (arXiv:2602.09810) - Statistical analysis across multiple random seeds confirms a significant performance gap under transfer. Standard DQN is known to suffer from overestimation bias and unstable value updates.

4. **"Distributional Soft Actor-Critic with Three Refinements"** (arXiv:2310.05858) - Mathematical analysis has shown that the overestimation bias is inversely proportional to the variance of the value distribution.

5. **"Deep Reinforcement Learning that Matters"** (arXiv:1709.06560) - The sensitivity of RL algorithms to changes in reward scale, environment dynamics, and random seeds can be considerable and varies between algorithms and settings.

6. **"On the consistency of hyper-parameter selection in value-based deep reinforcement learning"** (arXiv:2406.17523) - Deep reinforcement learning approaches are often notoriously sensitive to their hyperparameters and demonstrate brittle convergence properties, particularly true for off-policy approaches that use a replay buffer.

These papers collectively address your query's core themes of seed sensitivity, value overestimation, and variance reduction in deep reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "6410d32a-dd78-4a88-8e7b-275f3dcd9201",
  "tool_use_result": {
    "query": "reinforcement learning \"seed sensitivity\" \"value overestimation\" variance deep RL arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ay7PHcCjSJV7ey1zNK6KpR",
        "content": [
          {
            "title": "On the Reduction of Variance and Overestimation of Deep Q-Learning",
            "url": "https://arxiv.org/html/1910.05983v2"
          },
          {
            "title": "Dissecting Deep RL with High Update Ratios: Combatting Value Overestimation and Divergence",
            "url": "https://arxiv.org/html/2403.05996v1"
          },
          {
            "title": "A Controlled Study of Double DQN and Dueling DQN Under Cross-Environment Transfer",
            "url": "https://arxiv.org/html/2602.09810"
          },
          {
            "title": "Distributional Soft Actor-Critic with Three Refinements",
            "url": "https://arxiv.org/html/2310.05858.pdf"
          },
          {
            "title": "[1910.06591] SEED RL: Scalable and Efficient Deep-RL with Accelerated Central Inference",
            "url": "https://arxiv.org/abs/1910.06591"
          },
          {
            "title": "[1910.05983] On the Reduction of Variance and Overestimation of Deep Q-Learning",
            "url": "https://arxiv.org/abs/1910.05983"
          },
          {
            "title": "Averaged-DQN: Variance Reduction and Stabilization for ...",
            "url": "https://arxiv.org/pdf/1611.01929"
          },
          {
            "title": "Abstract",
            "url": "https://arxiv.org/html/2510.14503"
          },
          {
            "title": "Deep Reinforcement Learning that Matters",
            "url": "https://arxiv.org/pdf/1709.06560"
          },
          {
            "title": "On the consistency of hyper-parameter selection in value-based deep reinforcement learning",
            "url": "https://arxiv.org/html/2406.17523v1"
          }
        ]
      },
      "I found several relevant research papers on arXiv addressing reinforcement learning challenges related to seed sensitivity, value overestimation, and variance in deep RL:\n\n## Key Papers Found:\n\n1. **\"On the Reduction of Variance and Overestimation of Deep Q-Learning\"** (arXiv:1910.05983) - This paper addresses how many extensions to deep Q-Learning algorithm have been proposed to reduce the variance of the target values and the overestimation phenomena. The authors propose using Dropout techniques on deep Q-Learning algorithm as a way to reduce variance and overestimation.\n\n2. **\"Dissecting Deep RL with High Update Ratios: Combatting Value Overestimation and Divergence\"** (arXiv:2403.05996) - This work shows that Q-value divergence can arise due to problems inherent to neural network optimization, and this optimization-caused divergence can be mitigated using the unit-ball normalization approach.\n\n3. **\"A Controlled Study of Double DQN and Dueling DQN Under Cross-Environment Transfer\"** (arXiv:2602.09810) - Statistical analysis across multiple random seeds confirms a significant performance gap under transfer. Standard DQN is known to suffer from overestimation bias and unstable value updates.\n\n4. **\"Distributional Soft Actor-Critic with Three Refinements\"** (arXiv:2310.05858) - Mathematical analysis has shown that the overestimation bias is inversely proportional to the variance of the value distribution.\n\n5. **\"Deep Reinforcement Learning that Matters\"** (arXiv:1709.06560) - The sensitivity of RL algorithms to changes in reward scale, environment dynamics, and random seeds can be considerable and varies between algorithms and settings.\n\n6. **\"On the consistency of hyper-parameter selection in value-based deep reinforcement learning\"** (arXiv:2406.17523) - Deep reinforcement learning approaches are often notoriously sensitive to their hyperparameters and demonstrate brittle convergence properties, particularly true for off-policy approaches that use a replay buffer.\n\nThese papers collectively address your query's core themes of seed sensitivity, value overestimation, and variance reduction in deep reinforcement learning."
    ],
    "durationSeconds": 9.817721482000001
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T14:28:40.464Z_

<details><summary>↩ Tool result · `toolu_01CG5zDve15M7vrUkz12vTDi`</summary>

```text
Web search results for query: ""Dreamer" OR "world model" "high variance" seeds "performance collapse" reinforcement learning"

Links: [{"title":"Introducing Dreamer: Scalable Reinforcement Learning Using World Models","url":"https://research.google/blog/introducing-dreamer-scalable-reinforcement-learning-using-world-models/"},{"title":"learning behaviors","url":"https://arxiv.org/pdf/1912.01603"},{"title":"Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction","url":"https://arxiv.org/html/2603.07083"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"Mastering Diverse Control Tasks through World Models","url":"https://danijar.com/project/dreamerv3/"},{"title":"Reinforcement Learning from Delayed Observations via World Models","url":"https://arxiv.org/pdf/2403.12309"},{"title":"Probabilistic Dreaming for World Models","url":"https://arxiv.org/html/2603.04715"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"}]

I found search results related to Dreamer and world models in reinforcement learning. Here's what the search revealed:

## Overview of Dreamer

Dreamer is an RL agent that learns a world model from images and uses it to learn long-sighted behaviors. Dreamer leverages its world model to efficiently learn behaviors via backpropagation through model predictions.

## Performance and Robustness

Dreamer achieves state-of-the-art performance, data efficiency and computation time on a benchmark of 20 continuous control tasks given raw image inputs. More recently, Dreamer is a general algorithm that outperforms specialized expert algorithms across a wide range of domains while using fixed hyperparameters.

## Addressing Stability

Robustness techniques based on normalization, balancing and transformations enable stable learning across domains. This represents an important development for addressing training instability issues.

## Related Work on Variance

The search results mention work on variance reduction in world model-based RL. For example, one approach learns a more robust policy that leads to 28% lower variance in episode returns. Additionally, sharp performance degradation was observed when introducing latent beam search and high particle counts in some approaches.

The results show that researchers have been actively working on addressing stability and variance issues in world model-based reinforcement learning, though the specific combination of terms you searched for (high variance seeds and performance collapse) appears to be addressed more through robustness techniques than as a named problem in recent publications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "4299521d-26d1-48bb-9e6f-dc06f236f04a",
  "tool_use_result": {
    "query": "\"Dreamer\" OR \"world model\" \"high variance\" seeds \"performance collapse\" reinforcement learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VDub2fdPAUhrSyVPPh5Rqc",
        "content": [
          {
            "title": "Introducing Dreamer: Scalable Reinforcement Learning Using World Models",
            "url": "https://research.google/blog/introducing-dreamer-scalable-reinforcement-learning-using-world-models/"
          },
          {
            "title": "learning behaviors",
            "url": "https://arxiv.org/pdf/1912.01603"
          },
          {
            "title": "Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction",
            "url": "https://arxiv.org/html/2603.07083"
          },
          {
            "title": "Mastering diverse control tasks through world models | Nature",
            "url": "https://www.nature.com/articles/s41586-025-08744-2"
          },
          {
            "title": "Mastering Diverse Control Tasks through World Models",
            "url": "https://danijar.com/project/dreamerv3/"
          },
          {
            "title": "Reinforcement Learning from Delayed Observations via World Models",
            "url": "https://arxiv.org/pdf/2403.12309"
          },
          {
            "title": "Probabilistic Dreaming for World Models",
            "url": "https://arxiv.org/html/2603.04715"
          },
          {
            "title": "[2301.04104] Mastering Diverse Domains through World Models",
            "url": "https://arxiv.org/abs/2301.04104"
          },
          {
            "title": "Mastering Diverse Domains through World Models",
            "url": "https://arxiv.org/pdf/2301.04104"
          },
          {
            "title": "Mastering diverse control tasks through world models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"
          }
        ]
      },
      "I found search results related to Dreamer and world models in reinforcement learning. Here's what the search revealed:\n\n## Overview of Dreamer\n\nDreamer is an RL agent that learns a world model from images and uses it to learn long-sighted behaviors. Dreamer leverages its world model to efficiently learn behaviors via backpropagation through model predictions.\n\n## Performance and Robustness\n\nDreamer achieves state-of-the-art performance, data efficiency and computation time on a benchmark of 20 continuous control tasks given raw image inputs. More recently, Dreamer is a general algorithm that outperforms specialized expert algorithms across a wide range of domains while using fixed hyperparameters.\n\n## Addressing Stability\n\nRobustness techniques based on normalization, balancing and transformations enable stable learning across domains. This represents an important development for addressing training instability issues.\n\n## Related Work on Variance\n\nThe search results mention work on variance reduction in world model-based RL. For example, one approach learns a more robust policy that leads to 28% lower variance in episode returns. Additionally, sharp performance degradation was observed when introducing latent beam search and high particle counts in some approaches.\n\nThe results show that researchers have been actively working on addressing stability and variance issues in world model-based reinforcement learning, though the specific combination of terms you searched for (high variance seeds and performance collapse) appears to be addressed more through robustness techniques than as a named problem in recent publications."
    ],
    "durationSeconds": 8.358306525
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Let me continue searching for more specific papers. The Henderson 2018 paper is very relevant. Let me also search for:
1. The "Dissecting Deep RL with High Update Ratios" paper (value overestimation + divergence)
2. More on value overestimation in MBRL specifically
3. Primacy bias / plasticity loss as a mechanism for delayed failure
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "6b7807c4-b901-4718-9a3f-2aeb471b9e37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tfTsF8CsR4RRsVLDjuLrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4063,
      "cache_read_input_tokens": 32434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4063
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

_source line 31_

找到几个方向。继续深入搜索更具体的论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "2b4f2b9b-ae36-463f-85e0-5f6c87253fa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tfTsF8CsR4RRsVLDjuLrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4063,
      "cache_read_input_tokens": 32434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4063
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015sSD2DXGd8ehwEKvukefWi`</summary>

```json
{
  "query": "arXiv \"Dissecting Deep RL with High Update Ratios\" value overestimation divergence 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "fa27a6d9-74ed-4147-8c6c-4042ae09f598",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tfTsF8CsR4RRsVLDjuLrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4063,
      "cache_read_input_tokens": 32434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4063
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

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JNog1J5F6JrjRv5ue9gwKG`</summary>

```json
{
  "query": "\"primacy bias\" reinforcement learning \"value overestimation\" OR \"performance collapse\" seed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "0026e872-2a17-465b-99bf-a23d2a9e0243",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tfTsF8CsR4RRsVLDjuLrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4063,
      "cache_read_input_tokens": 32434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4063
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

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Axrg5diynCMrsEoPuorZxc`</summary>

```json
{
  "query": "\"Bridging Imagination and Reality\" model-based reinforcement learning value overestimation imagination rollout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "70ac6980-6cd0-4aab-a286-cf765471db02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tfTsF8CsR4RRsVLDjuLrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4063,
      "cache_read_input_tokens": 32434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4063
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

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013oBFd4h1PyZH8gYiy85XUu`</summary>

```json
{
  "query": "arXiv \"model-based reinforcement learning\" \"value divergence\" OR \"Q-value explosion\" imagination training 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "d4abb601-9559-46ca-9318-f27ab26774fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tfTsF8CsR4RRsVLDjuLrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4063,
      "cache_read_input_tokens": 32434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4063
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

_source line 36 · 2026-05-14T14:28:51.438Z_

<details><summary>↩ Tool result · `toolu_015sSD2DXGd8ehwEKvukefWi`</summary>

```text
Web search results for query: "arXiv "Dissecting Deep RL with High Update Ratios" value overestimation divergence 2024"

Links: [{"title":"Dissecting Deep RL with High Update Ratios: Combatting Value Overestimation and Divergence","url":"https://arxiv.org/html/2403.05996v1"},{"title":"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence","url":"https://arxiv.org/html/2403.05996v3"},{"title":"[2403.05996] Dissecting Deep RL with High Update Ratios: Combatting Value Divergence","url":"https://arxiv.org/abs/2403.05996"},{"title":"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence - NASA/ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240305996H/abstract"},{"title":"Dissecting Deep RL with High Update Ratios: Combatting Value Overestimation and Divergence | Semantic Scholar","url":"https://www.semanticscholar.org/paper/0fb2ab32801f9802e06b721a809e98477eca58dd"},{"title":"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning","url":"https://arxiv.org/html/2412.14312v1"},{"title":"RLJ | RLC 2024 Dissecting Deep RL with High Update Ratios:","url":"https://www.seas.upenn.edu/~eeaton/papers/Hussing2024DissectingDeepRL.pdf"},{"title":"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/dissecting-deep-rl-high-update-ratios-combatting"},{"title":"RLJ · Dissecting Deep RL with High Update Ratios: Combatting Value Divergence","url":"https://rlj.cs.umass.edu/2024/papers/Paper125.html"},{"title":"[PDF] Dissecting Deep RL with High Update Ratios: Combatting Value Divergence | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Dissecting-Deep-RL-with-High-Update-Ratios:-Value-Hussing-Voelcker/384b0c06c5dcdb986876868781e67bf1f57469a9"}]

I found the paper successfully! Here's what I discovered:

## Paper Information

The paper is titled **"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence"** by Marcel Hussing, Claas A Voelcker, Igor Gilitschenski, Amir-massoud Farahmand, and Eric Eaton.

**arXiv ID:** 2403.05996

**Publication:** Reinforcement Learning Journal, vol. 2, 2024

## Key Findings

Under large update-to-data ratios, a recent study by Nikishin et al. (2022) suggested the emergence of a primacy bias, in which agents overfit early interactions and downplay later experience, impairing their ability to learn.

The paper's main contribution is that one fundamental challenge is a long-standing acquaintance: value function divergence. Overinflated Q-values are found not only on out-of-distribution but also in-distribution data and can be linked to overestimation on unseen action prediction propelled by optimizer momentum.

## Proposed Solution

The authors employ a simple unit-ball normalization that enables learning under large update ratios, show its efficacy on the widely used dm_control suite, and obtain strong performance on the challenging dog tasks, competitive with model-based approaches.

The work questions previous explanations for learning failures and identifies value divergence as a critical issue to address in deep RL when using high update-to-data ratios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "cd08c03a-9f1f-4608-b812-8ce7138a9f71",
  "tool_use_result": {
    "query": "arXiv \"Dissecting Deep RL with High Update Ratios\" value overestimation divergence 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_016HJtdXtdKoMXxw26i51Swv",
        "content": [
          {
            "title": "Dissecting Deep RL with High Update Ratios: Combatting Value Overestimation and Divergence",
            "url": "https://arxiv.org/html/2403.05996v1"
          },
          {
            "title": "Dissecting Deep RL with High Update Ratios: Combatting Value Divergence",
            "url": "https://arxiv.org/html/2403.05996v3"
          },
          {
            "title": "[2403.05996] Dissecting Deep RL with High Update Ratios: Combatting Value Divergence",
            "url": "https://arxiv.org/abs/2403.05996"
          },
          {
            "title": "Dissecting Deep RL with High Update Ratios: Combatting Value Divergence - NASA/ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240305996H/abstract"
          },
          {
            "title": "Dissecting Deep RL with High Update Ratios: Combatting Value Overestimation and Divergence | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/0fb2ab32801f9802e06b721a809e98477eca58dd"
          },
          {
            "title": "Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning",
            "url": "https://arxiv.org/html/2412.14312v1"
          },
          {
            "title": "RLJ | RLC 2024 Dissecting Deep RL with High Update Ratios:",
            "url": "https://www.seas.upenn.edu/~eeaton/papers/Hussing2024DissectingDeepRL.pdf"
          },
          {
            "title": "Dissecting Deep RL with High Update Ratios: Combatting Value Divergence | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/dissecting-deep-rl-high-update-ratios-combatting"
          },
          {
            "title": "RLJ · Dissecting Deep RL with High Update Ratios: Combatting Value Divergence",
            "url": "https://rlj.cs.umass.edu/2024/papers/Paper125.html"
          },
          {
            "title": "[PDF] Dissecting Deep RL with High Update Ratios: Combatting Value Divergence | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Dissecting-Deep-RL-with-High-Update-Ratios:-Value-Hussing-Voelcker/384b0c06c5dcdb986876868781e67bf1f57469a9"
          }
        ]
      },
      "I found the paper successfully! Here's what I discovered:\n\n## Paper Information\n\nThe paper is titled **\"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\"** by Marcel Hussing, Claas A Voelcker, Igor Gilitschenski, Amir-massoud Farahmand, and Eric Eaton.\n\n**arXiv ID:** 2403.05996\n\n**Publication:** Reinforcement Learning Journal, vol. 2, 2024\n\n## Key Findings\n\nUnder large update-to-data ratios, a recent study by Nikishin et al. (2022) suggested the emergence of a primacy bias, in which agents overfit early interactions and downplay later experience, impairing their ability to learn.\n\nThe paper's main contribution is that one fundamental challenge is a long-standing acquaintance: value function divergence. Overinflated Q-values are found not only on out-of-distribution but also in-distribution data and can be linked to overestimation on unseen action prediction propelled by optimizer momentum.\n\n## Proposed Solution\n\nThe authors employ a simple unit-ball normalization that enables learning under large update ratios, show its efficacy on the widely used dm_control suite, and obtain strong performance on the challenging dog tasks, competitive with model-based approaches.\n\nThe work questions previous explanations for learning failures and identifies value divergence as a critical issue to address in deep RL when using high update-to-data ratios."
    ],
    "durationSeconds": 6.163656325999996
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T14:28:53.171Z_

<details><summary>↩ Tool result · `toolu_01JNog1J5F6JrjRv5ue9gwKG`</summary>

```text
Web search results for query: ""primacy bias" reinforcement learning "value overestimation" OR "performance collapse" seed"

Links: [{"title":"The Primacy Bias in Deep Reinforcement Learning","url":"https://proceedings.mlr.press/v162/nikishin22a/nikishin22a.pdf"},{"title":"[2205.07802] The Primacy Bias in Deep Reinforcement Learning","url":"https://arxiv.org/abs/2205.07802"},{"title":"It's Time to Move On: Primacy Bias and Why It Helps to Forget | ICLR Blogposts 2024","url":"https://iclr-blogposts.github.io/2024/blog/primacy-bias-and-why-it-helps-to-forget/"},{"title":"The Primacy Bias in Deep Reinforcement Learning | Mila","url":"https://mila.quebec/en/article/the-primacy-bias-in-deep-reinforcement-learning"},{"title":"The Primacy Bias in Deep Reinforcement Learning Evgenii Nikishin∗","url":"https://evgenii-nikishin.github.io/data/RL_primacy_bias_RLDM2022.pdf"},{"title":"[2502.00802] Fisher-Guided Selective Forgetting: Mitigating The Primacy Bias in Deep Reinforcement Learning","url":"https://arxiv.org/abs/2502.00802"},{"title":"Eliminating Primacy Bias in Online Reinforcement Learning by Self-Distillation | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10533687/"},{"title":"GitHub - evgenii-nikishin/rl_with_resets: JAX implementation of deep RL agents with resets from the paper \"The Primacy Bias in Deep Reinforcement Learning\"","url":"https://github.com/evgenii-nikishin/rl_with_resets"},{"title":"[2310.15017] Mind the Model, Not the Agent: The Primacy Bias in Model-based RL","url":"https://arxiv.org/abs/2310.15017"},{"title":"It's Time to Move On: Primacy Bias and Why It Helps to Forget | OpenReview","url":"https://openreview.net/forum?id=7ZEwqUyKMC"}]

I've completed the web search for your query. Here are the key findings about primacy bias in reinforcement learning, value overestimation, and performance collapse:

## Overview of Primacy Bias in Deep RL

Primacy bias is a tendency in deep RL algorithms to rely on early interactions and ignore useful evidence encountered later, causing agents to overfit to earlier experiences because of training on progressively growing datasets.

## Connection to Value Overestimation and Collapse

In some failure modes, the critic might severely overestimate action values even with double Q-learning. Temporal-difference learning can be prone to divergence and collapse to a trivial solution, and once in a failure mode, standard RL optimization struggles to recover from it.

## Performance Impact

An agent extremely affected by the primacy bias is unable to learn even after collecting hundreds of thousands of new transitions. Common algorithmic features such as a high replay ratio and long n-step targets amplify the primacy bias.

## Proposed Solution

A simple mechanism tackles the primacy bias by periodically resetting a part of the agent, and this mechanism has been applied to algorithms in both discrete (Atari 100k) and continuous action (DeepMind Control Suite) domains, consistently improving their performance.

The research demonstrates this is a reproducible phenomenon across different random seeds and environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "ca765d27-602f-4f40-8160-4fe72b3c4171",
  "tool_use_result": {
    "query": "\"primacy bias\" reinforcement learning \"value overestimation\" OR \"performance collapse\" seed",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Sx7U3jUBzC2T8xGXEB2Z5g",
        "content": [
          {
            "title": "The Primacy Bias in Deep Reinforcement Learning",
            "url": "https://proceedings.mlr.press/v162/nikishin22a/nikishin22a.pdf"
          },
          {
            "title": "[2205.07802] The Primacy Bias in Deep Reinforcement Learning",
            "url": "https://arxiv.org/abs/2205.07802"
          },
          {
            "title": "It's Time to Move On: Primacy Bias and Why It Helps to Forget | ICLR Blogposts 2024",
            "url": "https://iclr-blogposts.github.io/2024/blog/primacy-bias-and-why-it-helps-to-forget/"
          },
          {
            "title": "The Primacy Bias in Deep Reinforcement Learning | Mila",
            "url": "https://mila.quebec/en/article/the-primacy-bias-in-deep-reinforcement-learning"
          },
          {
            "title": "The Primacy Bias in Deep Reinforcement Learning Evgenii Nikishin∗",
            "url": "https://evgenii-nikishin.github.io/data/RL_primacy_bias_RLDM2022.pdf"
          },
          {
            "title": "[2502.00802] Fisher-Guided Selective Forgetting: Mitigating The Primacy Bias in Deep Reinforcement Learning",
            "url": "https://arxiv.org/abs/2502.00802"
          },
          {
            "title": "Eliminating Primacy Bias in Online Reinforcement Learning by Self-Distillation | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/10533687/"
          },
          {
            "title": "GitHub - evgenii-nikishin/rl_with_resets: JAX implementation of deep RL agents with resets from the paper \"The Primacy Bias in Deep Reinforcement Learning\"",
            "url": "https://github.com/evgenii-nikishin/rl_with_resets"
          },
          {
            "title": "[2310.15017] Mind the Model, Not the Agent: The Primacy Bias in Model-based RL",
            "url": "https://arxiv.org/abs/2310.15017"
          },
          {
            "title": "It's Time to Move On: Primacy Bias and Why It Helps to Forget | OpenReview",
            "url": "https://openreview.net/forum?id=7ZEwqUyKMC"
          }
        ]
      },
      "I've completed the web search for your query. Here are the key findings about primacy bias in reinforcement learning, value overestimation, and performance collapse:\n\n## Overview of Primacy Bias in Deep RL\n\nPrimacy bias is a tendency in deep RL algorithms to rely on early interactions and ignore useful evidence encountered later, causing agents to overfit to earlier experiences because of training on progressively growing datasets.\n\n## Connection to Value Overestimation and Collapse\n\nIn some failure modes, the critic might severely overestimate action values even with double Q-learning. Temporal-difference learning can be prone to divergence and collapse to a trivial solution, and once in a failure mode, standard RL optimization struggles to recover from it.\n\n## Performance Impact\n\nAn agent extremely affected by the primacy bias is unable to learn even after collecting hundreds of thousands of new transitions. Common algorithmic features such as a high replay ratio and long n-step targets amplify the primacy bias.\n\n## Proposed Solution\n\nA simple mechanism tackles the primacy bias by periodically resetting a part of the agent, and this mechanism has been applied to algorithms in both discrete (Atari 100k) and continuous action (DeepMind Control Suite) domains, consistently improving their performance.\n\nThe research demonstrates this is a reproducible phenomenon across different random seeds and environments."
    ],
    "durationSeconds": 7.418407214999999
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T14:28:54.104Z_

<details><summary>↩ Tool result · `toolu_01Axrg5diynCMrsEoPuorZxc`</summary>

```text
Web search results for query: ""Bridging Imagination and Reality" model-based reinforcement learning value overestimation imagination rollout"

Links: [{"title":"[2010.12142] Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning","url":"https://arxiv.org/abs/2010.12142"},{"title":"Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning","url":"https://proceedings.nips.cc/paper_files/paper/2020/file/661b1e76b95cc50a7a11a85619a67d95-Paper.pdf"},{"title":"Review for NeurIPS paper: Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning","url":"https://proceedings.neurips.cc/paper/2020/file/661b1e76b95cc50a7a11a85619a67d95-Review.html"},{"title":"Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning","url":"https://proceedings.neurips.cc/paper/2020/hash/661b1e76b95cc50a7a11a85619a67d95-Abstract.html"},{"title":"[2110.00188] Offline Reinforcement Learning with Reverse Model-based Imagination","url":"https://ar5iv.labs.arxiv.org/html/2110.00188"},{"title":"[PDF] Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Bridging-Imagination-and-Reality-for-Model-Based-Zhu-Zhang/e2cac0f861832a988e52506f1e973a14f90d9647"},{"title":"Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning - DocsLib","url":"https://docslib.org/doc/289105/bridging-imagination-and-reality-for-model-based-deep-reinforcement-learning"},{"title":"Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning","url":"https://papertalk.org/papertalks/8425"},{"title":"Ofﬂine Reinforcement Learning with Reverse Model-based Imagination","url":"https://proceedings.neurips.cc/paper/2021/file/f5e647292cc4e1064968ca62bebe7e47-Paper.pdf"},{"title":"ImagineBench: Evaluating Reinforcement Learning with Large Language Model Rollouts","url":"https://arxiv.org/html/2505.10010v1"}]

Based on the search results, here's what I found about "Bridging Imagination and Reality" in model-based reinforcement learning:

## Overview

"Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning" proposes a novel model-based reinforcement learning algorithm called BIRD (BrIdging Reality and Dream), which maximizes the mutual information between imaginary and real trajectories so that policy improvement learned from imaginary trajectories can be easily generalized to real trajectories.

## The Problem

Sample efficiency is a major challenge for deep reinforcement learning. Model-based reinforcement learning addresses this challenge by performing planning on imaginary trajectories with a learned world model. However, world model learning may suffer from overfitting to training trajectories, and thus model-based value estimation and policy search will be prone to being sucked into an inferior local policy.

## Key Approach

The authors explicitly use a term for model fitting to prioritize maximizing the mutual information between rollouts under the learned model and trajectories obtained from rollouts in the real world. BIRD optimizes the world model to be more real and reinforces the actions whose resulting imaginations not only have large accumulative rewards, but also resemble real trajectories.

## Results

The approach improves sample efficiency of model-based planning and achieves state-of-the-art performance on challenging visual control benchmarks.

The paper was published at NeurIPS 2020 and addresses the critical challenge of value overestimation and domain gap between imagined and real trajectories in model-based RL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "bc4b2000-34ce-4b58-a83b-83195fef3dbd",
  "tool_use_result": {
    "query": "\"Bridging Imagination and Reality\" model-based reinforcement learning value overestimation imagination rollout",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B7TfYpEgCPG7eW4jhHiu9V",
        "content": [
          {
            "title": "[2010.12142] Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning",
            "url": "https://arxiv.org/abs/2010.12142"
          },
          {
            "title": "Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning",
            "url": "https://proceedings.nips.cc/paper_files/paper/2020/file/661b1e76b95cc50a7a11a85619a67d95-Paper.pdf"
          },
          {
            "title": "Review for NeurIPS paper: Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning",
            "url": "https://proceedings.neurips.cc/paper/2020/file/661b1e76b95cc50a7a11a85619a67d95-Review.html"
          },
          {
            "title": "Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning",
            "url": "https://proceedings.neurips.cc/paper/2020/hash/661b1e76b95cc50a7a11a85619a67d95-Abstract.html"
          },
          {
            "title": "[2110.00188] Offline Reinforcement Learning with Reverse Model-based Imagination",
            "url": "https://ar5iv.labs.arxiv.org/html/2110.00188"
          },
          {
            "title": "[PDF] Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Bridging-Imagination-and-Reality-for-Model-Based-Zhu-Zhang/e2cac0f861832a988e52506f1e973a14f90d9647"
          },
          {
            "title": "Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning - DocsLib",
            "url": "https://docslib.org/doc/289105/bridging-imagination-and-reality-for-model-based-deep-reinforcement-learning"
          },
          {
            "title": "Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning",
            "url": "https://papertalk.org/papertalks/8425"
          },
          {
            "title": "Ofﬂine Reinforcement Learning with Reverse Model-based Imagination",
            "url": "https://proceedings.neurips.cc/paper/2021/file/f5e647292cc4e1064968ca62bebe7e47-Paper.pdf"
          },
          {
            "title": "ImagineBench: Evaluating Reinforcement Learning with Large Language Model Rollouts",
            "url": "https://arxiv.org/html/2505.10010v1"
          }
        ]
      },
      "Based on the search results, here's what I found about \"Bridging Imagination and Reality\" in model-based reinforcement learning:\n\n## Overview\n\n\"Bridging Imagination and Reality for Model-Based Deep Reinforcement Learning\" proposes a novel model-based reinforcement learning algorithm called BIRD (BrIdging Reality and Dream), which maximizes the mutual information between imaginary and real trajectories so that policy improvement learned from imaginary trajectories can be easily generalized to real trajectories.\n\n## The Problem\n\nSample efficiency is a major challenge for deep reinforcement learning. Model-based reinforcement learning addresses this challenge by performing planning on imaginary trajectories with a learned world model. However, world model learning may suffer from overfitting to training trajectories, and thus model-based value estimation and policy search will be prone to being sucked into an inferior local policy.\n\n## Key Approach\n\nThe authors explicitly use a term for model fitting to prioritize maximizing the mutual information between rollouts under the learned model and trajectories obtained from rollouts in the real world. BIRD optimizes the world model to be more real and reinforces the actions whose resulting imaginations not only have large accumulative rewards, but also resemble real trajectories.\n\n## Results\n\nThe approach improves sample efficiency of model-based planning and achieves state-of-the-art performance on challenging visual control benchmarks.\n\nThe paper was published at NeurIPS 2020 and addresses the critical challenge of value overestimation and domain gap between imagined and real trajectories in model-based RL."
    ],
    "durationSeconds": 7.410752027000003
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T14:28:54.989Z_

<details><summary>↩ Tool result · `toolu_013oBFd4h1PyZH8gYiy85XUu`</summary>

```text
Web search results for query: "arXiv "model-based reinforcement learning" "value divergence" OR "Q-value explosion" imagination training 2023 2024"

Links: [{"title":"Diffusion-based Reinforcement Learning via Q-weighted Variational...","url":"https://arxiv.org/abs/2405.16173"},{"title":"Understanding Reinforcement Learning for Model Training, ...","url":"https://arxiv.org/pdf/2509.04501"},{"title":"Published in Transactions on Machine Learning Research (11/2024)","url":"https://arxiv.org/pdf/2406.06309"},{"title":"Diffusion-based Reinforcement Learning via Q-weighted Variational Policy Optimization","url":"https://arxiv.org/html/2405.16173v3"},{"title":"Integrating Reinforcement Learning with Visual Generative Models: Foundations and Advances","url":"https://arxiv.org/html/2508.10316v1"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104"},{"title":"Reinforcement Learning from Human Feedback","url":"https://arxiv.org/html/2504.12501v3"},{"title":"𝑄⁢♯: Provably Optimal Distributional RL for LLM Post-Training","url":"https://arxiv.org/html/2502.20548v1"},{"title":"An Invitation to Deep Reinforcement Learning Bernhard Jaeger","url":"https://arxiv.org/pdf/2312.08365"},{"title":"Inverse Reinforcement Learning Meets Large Language ...","url":"https://arxiv.org/pdf/2507.13158"}]

I found several relevant arXiv papers from 2023-2024 related to your search terms. Here are the key findings:

## Model-Based Reinforcement Learning and World Models

DreamerV3 learns a model of the environment and improves its behavior by imagining future scenarios, using robustness techniques based on normalization, balancing, and transformations to enable stable learning across domains. This paper from 2023 directly addresses model-based RL with imagination training.

## Q-Value and Value-Based Approaches

Several papers address value function challenges in RL:

- A 2023 paper on Q-ensemble for offline RL discusses scaling the batch size rather than the ensemble size, touching on value estimation issues.

- While there are existing value-based RL algorithms for LLM post-training (CD and VAS), they have a major issue in that they do not faithfully optimize the KL-constrained RL objective.

## Diffusion Models in RL

Diffusion models have garnered widespread attention in Reinforcement Learning for their powerful expressiveness and multimodality, with research showing they can significantly improve RL algorithm performance in continuous control tasks.

The search results show active research in model-based RL with imagination training and value function issues, though the specific papers directly addressing "value divergence" or "Q-value explosion" weren't prominently featured in these results. You may want to refine your search with more specific paper titles or author names if you're looking for particular works on these failure modes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "64265adc-a974-42af-9adf-9025dbc25c45",
  "tool_use_result": {
    "query": "arXiv \"model-based reinforcement learning\" \"value divergence\" OR \"Q-value explosion\" imagination training 2023 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_012sRadjR1GB1Bm44obfunwv",
        "content": [
          {
            "title": "Diffusion-based Reinforcement Learning via Q-weighted Variational...",
            "url": "https://arxiv.org/abs/2405.16173"
          },
          {
            "title": "Understanding Reinforcement Learning for Model Training, ...",
            "url": "https://arxiv.org/pdf/2509.04501"
          },
          {
            "title": "Published in Transactions on Machine Learning Research (11/2024)",
            "url": "https://arxiv.org/pdf/2406.06309"
          },
          {
            "title": "Diffusion-based Reinforcement Learning via Q-weighted Variational Policy Optimization",
            "url": "https://arxiv.org/html/2405.16173v3"
          },
          {
            "title": "Integrating Reinforcement Learning with Visual Generative Models: Foundations and Advances",
            "url": "https://arxiv.org/html/2508.10316v1"
          },
          {
            "title": "[2301.04104] Mastering Diverse Domains through World Models",
            "url": "https://arxiv.org/abs/2301.04104"
          },
          {
            "title": "Reinforcement Learning from Human Feedback",
            "url": "https://arxiv.org/html/2504.12501v3"
          },
          {
            "title": "𝑄⁢♯: Provably Optimal Distributional RL for LLM Post-Training",
            "url": "https://arxiv.org/html/2502.20548v1"
          },
          {
            "title": "An Invitation to Deep Reinforcement Learning Bernhard Jaeger",
            "url": "https://arxiv.org/pdf/2312.08365"
          },
          {
            "title": "Inverse Reinforcement Learning Meets Large Language ...",
            "url": "https://arxiv.org/pdf/2507.13158"
          }
        ]
      },
      "I found several relevant arXiv papers from 2023-2024 related to your search terms. Here are the key findings:\n\n## Model-Based Reinforcement Learning and World Models\n\nDreamerV3 learns a model of the environment and improves its behavior by imagining future scenarios, using robustness techniques based on normalization, balancing, and transformations to enable stable learning across domains. This paper from 2023 directly addresses model-based RL with imagination training.\n\n## Q-Value and Value-Based Approaches\n\nSeveral papers address value function challenges in RL:\n\n- A 2023 paper on Q-ensemble for offline RL discusses scaling the batch size rather than the ensemble size, touching on value estimation issues.\n\n- While there are existing value-based RL algorithms for LLM post-training (CD and VAS), they have a major issue in that they do not faithfully optimize the KL-constrained RL objective.\n\n## Diffusion Models in RL\n\nDiffusion models have garnered widespread attention in Reinforcement Learning for their powerful expressiveness and multimodality, with research showing they can significantly improve RL algorithm performance in continuous control tasks.\n\nThe search results show active research in model-based RL with imagination training and value function issues, though the specific papers directly addressing \"value divergence\" or \"Q-value explosion\" weren't prominently featured in these results. You may want to refine your search with more specific paper titles or author names if you're looking for particular works on these failure modes."
    ],
    "durationSeconds": 7.417154943000002
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Good, I've found some strong candidates. Let me search for a couple more specific ones:

1. "Mind the Model, Not the Agent: The Primacy Bias in Model-based RL" - this seems very relevant
2. The BIRD paper (Bridging Imagination and Reality)
3. Let me also check for "Stealing That Free Lunch" which appeared in results

Let me get more details on these papers and also look for any papers about seed-dependent failures specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "c0fa8a9b-f5ca-4d45-8933-e0540cda317e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7U9UFrWsNzmgmtrnLnQvr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4150,
      "cache_read_input_tokens": 36497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4150
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

_source line 41_

找到关键线索。再搜几篇高相关的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "cb12f741-de95-4e49-8883-42ffa42fc5c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7U9UFrWsNzmgmtrnLnQvr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4150,
      "cache_read_input_tokens": 36497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4150
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

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QycwWCkf3K8CL6HqPYKNEX`</summary>

```json
{
  "query": "arXiv 2310.15017 \"Mind the Model Not the Agent\" primacy bias model-based RL Dreamer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "fc551af1-535f-4255-917a-f881245efa72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7U9UFrWsNzmgmtrnLnQvr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4150,
      "cache_read_input_tokens": 36497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4150
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

_source line 43_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TAKjMRzveXTGMXnquP4NqJ`</summary>

```json
{
  "query": "\"Stealing That Free Lunch\" Dyna reinforcement learning value overestimation model exploitation 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "ec3d7c20-5837-4fd5-a43b-47a63ed4ba20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7U9UFrWsNzmgmtrnLnQvr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4150,
      "cache_read_input_tokens": 36497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4150
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

_source line 44 · 2026-05-14T14:29:09.760Z_

<details><summary>↩ Tool result · `toolu_01QycwWCkf3K8CL6HqPYKNEX`</summary>

```text
Web search results for query: "arXiv 2310.15017 "Mind the Model Not the Agent" primacy bias model-based RL Dreamer"

Links: [{"title":"[2310.15017] Mind the Model, Not the Agent: The Primacy Bias in Model-based RL","url":"https://arxiv.org/abs/2310.15017"},{"title":"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL","url":"https://arxiv.org/html/2310.15017"},{"title":"[2310.15017] The Primacy Bias in Model-based RL - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2310.15017"},{"title":"IOS Press Ebooks - Mind the Model, Not the Agent: The Primacy Bias in Model-Based RL","url":"https://ebooks.iospress.nl/DOI/10.3233/FAIA240694"},{"title":"The Primacy Bias in Model-based RL","url":"https://arxiv.org/pdf/2310.15017"},{"title":"Mind the Model, Not the Agent: The Primacy Bias in ...","url":"https://www.aimodels.fyi/papers/arxiv/mind-model-not-agent-primacy-bias-model"},{"title":"The Primacy Bias in Model-based RL","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2310.15017"},{"title":"Fisher-Guided Selective Forgetting: Mitigating The Primacy Bias in Deep Reinforcement Learning","url":"https://arxiv.org/html/2502.00802v1"},{"title":"Cognitive Bias in Decision-Making with LLMs","url":"https://arxiv.org/html/2403.00811v2"},{"title":"[2205.07802] The Primacy Bias in Deep Reinforcement Learning","url":"https://arxiv.org/abs/2205.07802"}]

Based on the search results, I found comprehensive information about arXiv paper 2310.15017. Here's what the paper is about:

## Paper Overview

The paper is titled "Mind the Model, Not the Agent: The Primacy Bias in Model-based RL" by Zhongjian Qiao, Jiafei Lyu, and Xiu Li.

## Main Findings

The primacy bias in model-free reinforcement learning (MFRL) refers to the agent's tendency to overfit early data and lose the ability to learn from new data, and can significantly decrease the performance of MFRL algorithms. Previous studies have shown that employing simple techniques, such as resetting the agent's parameters, can substantially alleviate the primacy bias in MFRL.

However, the key contribution of this paper is that the primacy bias in MBRL is more closely related to the primacy bias of the world model instead of the primacy bias of the agent.

## Proposed Solution

Based on this finding, the authors propose "world model resetting," a simple yet effective technique to alleviate the primacy bias in MBRL.

## Experimental Validation

The method is applied to two different MBRL algorithms, MBPO and DreamerV2. The effectiveness of the method is validated on multiple continuous control tasks on MuJoCo and DeepMind Control Suite, as well as discrete control tasks on Atari 100k benchmark, and the results show that world model resetting can significantly alleviate the primacy bias in the model-based setting and improve the algorithm's performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "4eb6c999-bfb9-435e-86e3-4a526f0aa49d",
  "tool_use_result": {
    "query": "arXiv 2310.15017 \"Mind the Model Not the Agent\" primacy bias model-based RL Dreamer",
    "results": [
      {
        "tool_use_id": "srvtoolu_012s1F8Xx8X2RnhJdDVRjb1K",
        "content": [
          {
            "title": "[2310.15017] Mind the Model, Not the Agent: The Primacy Bias in Model-based RL",
            "url": "https://arxiv.org/abs/2310.15017"
          },
          {
            "title": "Mind the Model, Not the Agent: The Primacy Bias in Model-based RL",
            "url": "https://arxiv.org/html/2310.15017"
          },
          {
            "title": "[2310.15017] The Primacy Bias in Model-based RL - ar5iv",
            "url": "https://ar5iv.labs.arxiv.org/html/2310.15017"
          },
          {
            "title": "IOS Press Ebooks - Mind the Model, Not the Agent: The Primacy Bias in Model-Based RL",
            "url": "https://ebooks.iospress.nl/DOI/10.3233/FAIA240694"
          },
          {
            "title": "The Primacy Bias in Model-based RL",
            "url": "https://arxiv.org/pdf/2310.15017"
          },
          {
            "title": "Mind the Model, Not the Agent: The Primacy Bias in ...",
            "url": "https://www.aimodels.fyi/papers/arxiv/mind-model-not-agent-primacy-bias-model"
          },
          {
            "title": "The Primacy Bias in Model-based RL",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2310.15017"
          },
          {
            "title": "Fisher-Guided Selective Forgetting: Mitigating The Primacy Bias in Deep Reinforcement Learning",
            "url": "https://arxiv.org/html/2502.00802v1"
          },
          {
            "title": "Cognitive Bias in Decision-Making with LLMs",
            "url": "https://arxiv.org/html/2403.00811v2"
          },
          {
            "title": "[2205.07802] The Primacy Bias in Deep Reinforcement Learning",
            "url": "https://arxiv.org/abs/2205.07802"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about arXiv paper 2310.15017. Here's what the paper is about:\n\n## Paper Overview\n\nThe paper is titled \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\" by Zhongjian Qiao, Jiafei Lyu, and Xiu Li.\n\n## Main Findings\n\nThe primacy bias in model-free reinforcement learning (MFRL) refers to the agent's tendency to overfit early data and lose the ability to learn from new data, and can significantly decrease the performance of MFRL algorithms. Previous studies have shown that employing simple techniques, such as resetting the agent's parameters, can substantially alleviate the primacy bias in MFRL.\n\nHowever, the key contribution of this paper is that the primacy bias in MBRL is more closely related to the primacy bias of the world model instead of the primacy bias of the agent.\n\n## Proposed Solution\n\nBased on this finding, the authors propose \"world model resetting,\" a simple yet effective technique to alleviate the primacy bias in MBRL.\n\n## Experimental Validation\n\nThe method is applied to two different MBRL algorithms, MBPO and DreamerV2. The effectiveness of the method is validated on multiple continuous control tasks on MuJoCo and DeepMind Control Suite, as well as discrete control tasks on Atari 100k benchmark, and the results show that world model resetting can significantly alleviate the primacy bias in the model-based setting and improve the algorithm's performance."
    ],
    "durationSeconds": 7.090030343999999
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T14:29:10.800Z_

<details><summary>↩ Tool result · `toolu_01TAKjMRzveXTGMXnquP4NqJ`</summary>

```text
Web search results for query: ""Stealing That Free Lunch" Dyna reinforcement learning value overestimation model exploitation 2024 arXiv"

Links: [{"title":"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning","url":"https://arxiv.org/html/2412.14312v1"},{"title":"[2412.14312] Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning","url":"https://arxiv.org/abs/2412.14312"},{"title":"Machine Learning Dec 2024","url":"https://www.arxiv.org/list/cs.LG/2024-12?skip=1100&show=1000"},{"title":"Fixing That Free Lunch: When, Where, and Why Synthetic Data Fails in Model-Based Policy Optimization","url":"https://arxiv.org/html/2510.01457v1"},{"title":"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=Zt05jXhqXx"},{"title":"A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in Model-Based Policy Optimization","url":"https://arxiv.org/html/2510.01457"},{"title":"Machine Learning Dec 2024","url":"https://arxiv.org/list/cs.LG/2024-12?skip=1075&show=250"},{"title":"Computer Science Dec 2024","url":"https://www.arxiv.org/list/cs/2024-12?skip=6550&show=50"}]

I found the paper! Here are the key findings:

## "Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning"

**Authors:** Brett Barkley and David Fridovich-Keil

**Publication:** Accepted to ICML 2025 (arXiv preprint: 2412.14312)

### Main Findings:

The paper investigates Dyna-style off-policy model-based reinforcement learning (DMBRL) algorithms—a family of techniques for generating synthetic state transition data—and identifies a surprising performance gap observed when applying them across different benchmark environments with proprioceptive observations.

While DMBRL algorithms perform well in OpenAI Gym, their performance can drop significantly in DeepMind Control Suite (DMC), even though these settings offer similar tasks and identical physics backends.

### Key Issues Investigated:

The authors analyzed the Gym/DMC performance gap and tried to close it by addressing possible sources of discrepancy including overestimation bias, neural network plasticity, and environment modeling fidelity.

### Critical Result:

Modern techniques designed to address several key issues that arise in these settings do not provide a consistent improvement across all environments, and overall the results show that adding synthetic rollouts to the training process—the backbone of Dyna-style algorithms—significantly degrades performance across most DMC environments.

### Implications:

"Our findings contribute to a deeper understanding of several fundamental challenges in model-based RL and show that, like many optimization fields, there is no free lunch when evaluating performance across diverse benchmarks in RL."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "6f30c9d0-21e6-49b9-9bc9-fbf16c8da9c1",
  "tool_use_result": {
    "query": "\"Stealing That Free Lunch\" Dyna reinforcement learning value overestimation model exploitation 2024 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_016vSw6WQiFCe8qoD2HWzQDB",
        "content": [
          {
            "title": "Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning",
            "url": "https://arxiv.org/html/2412.14312v1"
          },
          {
            "title": "[2412.14312] Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning",
            "url": "https://arxiv.org/abs/2412.14312"
          },
          {
            "title": "Machine Learning Dec 2024",
            "url": "https://www.arxiv.org/list/cs.LG/2024-12?skip=1100&show=1000"
          },
          {
            "title": "Fixing That Free Lunch: When, Where, and Why Synthetic Data Fails in Model-Based Policy Optimization",
            "url": "https://arxiv.org/html/2510.01457v1"
          },
          {
            "title": "Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=Zt05jXhqXx"
          },
          {
            "title": "A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in Model-Based Policy Optimization",
            "url": "https://arxiv.org/html/2510.01457"
          },
          {
            "title": "Machine Learning Dec 2024",
            "url": "https://arxiv.org/list/cs.LG/2024-12?skip=1075&show=250"
          },
          {
            "title": "Computer Science Dec 2024",
            "url": "https://www.arxiv.org/list/cs/2024-12?skip=6550&show=50"
          }
        ]
      },
      "I found the paper! Here are the key findings:\n\n## \"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\"\n\n**Authors:** Brett Barkley and David Fridovich-Keil\n\n**Publication:** Accepted to ICML 2025 (arXiv preprint: 2412.14312)\n\n### Main Findings:\n\nThe paper investigates Dyna-style off-policy model-based reinforcement learning (DMBRL) algorithms—a family of techniques for generating synthetic state transition data—and identifies a surprising performance gap observed when applying them across different benchmark environments with proprioceptive observations.\n\nWhile DMBRL algorithms perform well in OpenAI Gym, their performance can drop significantly in DeepMind Control Suite (DMC), even though these settings offer similar tasks and identical physics backends.\n\n### Key Issues Investigated:\n\nThe authors analyzed the Gym/DMC performance gap and tried to close it by addressing possible sources of discrepancy including overestimation bias, neural network plasticity, and environment modeling fidelity.\n\n### Critical Result:\n\nModern techniques designed to address several key issues that arise in these settings do not provide a consistent improvement across all environments, and overall the results show that adding synthetic rollouts to the training process—the backbone of Dyna-style algorithms—significantly degrades performance across most DMC environments.\n\n### Implications:\n\n\"Our findings contribute to a deeper understanding of several fundamental challenges in model-based RL and show that, like many optimization fields, there is no free lunch when evaluating performance across diverse benchmarks in RL.\""
    ],
    "durationSeconds": 7.366637595000007
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have a strong set of papers. Let me compile the most relevant ones for the user's specific needs:

1. **Henderson et al. 2018** - "Deep Reinforcement Learning that Matters" - AAAI 2018 - Foundational paper on seed variance in deep RL. Directly relevant to angle 1 (seed sensitivity).

2. **Nikishin et al. 2022** - "The Primacy Bias in Deep Reinforcement Learning" - ICML 2022 - Describes how early overfitting leads to delayed performance collapse. Relevant to angle 3 (value overestimation as delayed failure).
   
3. **Qiao et al. 2023** - "Mind the Model, Not the Agent: The Primacy Bias in Model-based RL" - arXiv 2310.15017 / ECAI 2024 - Extends primacy bias to model-based RL and Dreamer specifically, covering both the instability issues and value overestimation angles.

4. **Hussing et al. 2024** - "Dissecting Deep RL with High Update Ratios: Combatting Value Divergence" - RLC 2024 - Directly addresses value divergence and overestimation problems that emerge under high update-to-data ratios.

5. **Barkley & Fridovich-Keil 2024** - "Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning" - ICML 2025 - Demonstrates that synthetic rollouts can actually hurt performance inconsistently across environments, which is crucial for understanding imagination-based training failures.

Now I'm checking the literature map to see which papers are already documented. None of these five papers appear in the existing map, so they're all new additions that would strengthen the coverage.

I should also consider whether the Zhu et al. 2020 paper on imagination-reality gaps is relevant here, though it's less directly connected to the seed-dependent overestimation problem. Now I need to read the current YAML file to match its formatting before adding these entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "b9758bc7-4077-472f-a8b0-68a61414c5b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcdRM559Rj7AbZvrEKzMrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2009,
      "cache_read_input_tokens": 40647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2009
      },
      "output_tokens": 32,
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

_source line 47_

找到了 5 篇高相关论文。现在读取实际文件并追加。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "f1ec81d7-e776-440a-aaa3-92012dc44ff5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcdRM559Rj7AbZvrEKzMrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2009,
      "cache_read_input_tokens": 40647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2009
      },
      "output_tokens": 32,
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

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01SWHKHV62CDx7dF8hP6Tc41`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "046f819b-2da6-4266-b508-be7d55b4da83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcdRM559Rj7AbZvrEKzMrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2009,
      "cache_read_input_tokens": 40647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2009
      },
      "output_tokens": 32,
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

_source line 49 · 2026-05-14T14:29:25.968Z_

<details><summary>↩ Tool result · `toolu_01SWHKHV62CDx7dF8hP6Tc41`</summary>

```text
1	# Literature Map — event-gated-adaptive-horizon
2	# Last updated: 2026-05-14
3	# Total: 28 papers (5 existing + 23 new)
4	
5	# ============================================================
6	# EXISTING CITATIONS (already in paper.tex)
7	# ============================================================
8	
9	- paper_id: sutton1999options
10	  title: "Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning"
11	  authors: [Sutton R.S., Precup D., Singh S.]
12	  year: 1999
13	  venue: "Artificial Intelligence 112(1-2):181-211"
14	  category: background
15	  role: "Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL"
16	  relevance_score: 5
17	
18	- paper_id: hafner2020dreamerv1
19	  title: "Dream to Control: Learning Behaviors by Latent Imagination"
20	  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]
21	  year: 2020
22	  venue: ICLR
23	  category: background
24	  role: "DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm"
25	  relevance_score: 5
26	
27	- paper_id: hafner2023dreamerv3
28	  title: "Mastering Diverse Domains through World Models"
29	  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]
30	  year: 2023
31	  venue: "arXiv:2301.04104 (Nature 2025)"
32	  category: background
33	  role: "DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here"
34	  relevance_score: 5
35	
36	- paper_id: sharma2017figar
37	  title: "Fine Grained Action Repetition for Deep Reinforcement Learning"
38	  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]
39	  year: 2017
40	  venue: "ICLR Workshop"
41	  category: method-component
42	  role: "FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL"
43	  relevance_score: 4
44	
45	- paper_id: janner2019mbpo
46	  title: "When to Trust Your Model: Model-Based Policy Optimization"
47	  authors: [Janner M., Fu J., Zhang M., Levine S.]
48	  year: 2019
49	  venue: NeurIPS
50	  category: background
51	  role: "MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding"
52	  relevance_score: 5
53	
54	# ============================================================
55	# NEW: Multi-step prediction error compounding
56	# ============================================================
57	
58	- paper_id: ke2019learning
59	  title: "Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future"
60	  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]
61	  year: 2019
62	  venue: ICLR
63	  category: background
64	  role: "Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1"
65	  relevance_score: 4
66	
67	- paper_id: asadi2019combating
68	  title: "Combating the Compounding-Error Problem with a Multi-step Model"
69	  authors: [Asadi K., Misra D., Kim S., Littman M.L.]
70	  year: 2019
71	  venue: "arXiv:1905.13320"
72	  category: background
73	  role: "Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error"
74	  relevance_score: 4
75	
76	- paper_id: venkatraman2015improving
77	  title: "Improving Multi-Step Prediction of Learned Time Series Models"
78	  authors: [Venkatraman A., Hebert M., Bagnell J.A.]
79	  year: 2015
80	  venue: AAAI
81	  category: background
82	  role: "Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error"
83	  relevance_score: 3
84	
85	- paper_id: lambert2022investigating
86	  title: "Investigating Compounding Prediction Errors in Learned Dynamics Models"
87	  authors: [Lambert N., Pister K.S.J., Calandra R.]
88	  year: 2022
89	  venue: "arXiv:2203.09637"
90	  category: background
91	  role: "Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead"
92	  relevance_score: 3
93	
94	# ============================================================
95	# NEW: Model-predictive control with learned dynamics
96	# ============================================================
97	
98	- paper_id: chua2018pets
99	  title: "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models"
100	  authors: [Chua K., Calandra R., McAllister R., Levine S.]
101	  year: 2018
102	  venue: NeurIPS
103	  category: background
104	  role: "PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach"
105	  relevance_score: 3
106	
107	- paper_id: nagabandi2018neural
108	  title: "Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning"
109	  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]
110	  year: 2018
111	  venue: ICRA
112	  category: background
113	  role: "Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures"
114	  relevance_score: 3
115	
116	# ============================================================
117	# NEW: Value overestimation mitigation
118	# ============================================================
119	
120	- paper_id: thrun1993issues
121	  title: "Issues in Using Function Approximation for Reinforcement Learning"
122	  authors: [Thrun S., Schwartz A.]
123	  year: 1993
124	  venue: "Connectionist Models Summer School"
125	  category: background
126	  role: "First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning"
127	  relevance_score: 4
128	
129	- paper_id: vanhasselt2016double
130	  title: "Deep Reinforcement Learning with Double Q-Learning"
131	  authors: [van Hasselt H., Guez A., Silver D.]
132	  year: 2016
133	  venue: AAAI
134	  category: background
135	  role: "Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL"
136	  relevance_score: 4
137	
138	- paper_id: fujimoto2018td3
139	  title: "Addressing Function Approximation Error in Actor-Critic Methods"
140	  authors: [Fujimoto S., van Hoof H., Meger D.]
141	  year: 2018
142	  venue: ICML
143	  category: method-component
144	  role: "TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify"
145	  relevance_score: 4
146	
147	- paper_id: haarnoja2018sac
148	  title: "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor"
149	  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]
150	  year: 2018
151	  venue: ICML
152	  category: method-component
153	  role: "SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values"
154	  relevance_score: 3
155	
156	- paper_id: lee2021sunrise
157	  title: "SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning"
158	  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]
159	  year: 2021
160	  venue: ICML
161	  category: method-component
162	  role: "Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism"
163	  relevance_score: 3
164	
165	# ============================================================
166	# NEW: Delusional bias
167	# ============================================================
168	
169	- paper_id: lu2018nondelusional
170	  title: "Non-delusional Q-learning and Value-Iteration"
171	  authors: [Lu T., Schuurmans D., Boutilier C.]
172	  year: 2018
173	  venue: NeurIPS
174	  category: background
175	  role: "Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision"
176	  relevance_score: 5
177	
178	# ============================================================
179	# NEW: Hierarchical RL with learned models
180	# ============================================================
181	
182	- paper_id: hafner2022director
183	  title: "Deep Hierarchical Planning from Pixels"
184	  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]
185	  year: 2022
186	  venue: NeurIPS
187	  category: direct-competitor
188	  role: "Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt"
189	  relevance_score: 4
190	
191	- paper_id: nachum2018hiro
192	  title: "Data-Efficient Hierarchical Reinforcement Learning"
193	  authors: [Nachum O., Gu S., Lee H., Levine S.]
194	  year: 2018
195	  venue: NeurIPS
196	  category: background
197	  role: "HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed"
198	  relevance_score: 3
199	
200	# ============================================================
201	# NEW: Action repeat / frame skip
202	# ============================================================
203	
204	- paper_id: braylan2015frame
205	  title: "Frame Skip Is a Powerful Parameter for Learning to Play Atari"
206	  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]
207	  year: 2015
208	  venue: "AAAI Workshop on Learning for General Competency in Video Games"
209	  category: background
210	  role: "Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice"
211	  relevance_score: 3
212	
213	- paper_id: lakshminarayanan2017dynamic
214	  title: "Dynamic Action Repetition for Deep Reinforcement Learning"
215	  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]
216	  year: 2017
217	  venue: AAAI
218	  category: method-component
219	  role: "Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach"
220	  relevance_score: 4
221	
222	- paper_id: biedenkapp2021temporl
223	  title: "TempoRL: Learning When to Act"
224	  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]
225	  year: 2021
226	  venue: ICML
227	  category: method-component
228	  role: "Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify"
229	  relevance_score: 4
230	
231	# ============================================================
232	# NEW: DreamerV2
233	# ============================================================
234	
235	- paper_id: hafner2021dreamerv2
236	  title: "Mastering Atari with Discrete World Models"
237	  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]
238	  year: 2021
239	  venue: ICLR
240	  category: background
241	  role: "DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system"
242	  relevance_score: 5
243	
244	# ============================================================
245	# NEW: Alternative world model architectures
246	# ============================================================
247	
248	- paper_id: micheli2023iris
249	  title: "Transformers are Sample-Efficient World Models"
250	  authors: [Micheli V., Alonso E., Fleuret F.]
251	  year: 2023
252	  venue: ICLR
253	  category: direct-competitor
254	  role: "IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction"
255	  relevance_score: 3
256	
257	- paper_id: robine2023twm
258	  title: "Transformer-based World Models Are Happy With 100k Interactions"
259	  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]
260	  year: 2023
261	  venue: ICLR
262	  category: direct-competitor
263	  role: "TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap"
264	  relevance_score: 3
265	
266	- paper_id: chen2022transdreamer
267	  title: "TransDreamer: Reinforcement Learning with Transformer World Models"
268	  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]
269	  year: 2022
270	  venue: "arXiv:2202.09481"
271	  category: direct-competitor
272	  role: "Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures"
273	  relevance_score: 3
274	
275	# ============================================================
276	# NEW: 2024-2026 concurrent work on temporal abstraction in world models
277	# ============================================================
278	
279	- paper_id: gumbsch2024thick
280	  title: "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics"
281	  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]
282	  year: 2024
283	  venue: ICLR
284	  category: direct-competitor
285	  role: "THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination"
286	  relevance_score: 5
287	
288	- paper_id: mattes2024hieros
289	  title: "Hieros: Hierarchical Imagination on Structured State Space Sequence World Models"
290	  authors: [Mattes P., Schlosser R., Herbrich R.]
291	  year: 2024
292	  venue: ICML
293	  category: direct-competitor
294	  role: "Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify"
295	  relevance_score: 5
296	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "bcdd9265-ccc4-441a-9c31-30f43a427e2d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
      "content": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 28 papers (5 existing + 23 new)\n\n# ============================================================\n# EXISTING CITATIONS (already in paper.tex)\n# ============================================================\n\n- paper_id: sutton1999options\n  title: \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\"\n  authors: [Sutton R.S., Precup D., Singh S.]\n  year: 1999\n  venue: \"Artificial Intelligence 112(1-2):181-211\"\n  category: background\n  role: \"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\"\n  relevance_score: 5\n\n- paper_id: hafner2020dreamerv1\n  title: \"Dream to Control: Learning Behaviors by Latent Imagination\"\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\n  year: 2020\n  venue: ICLR\n  category: background\n  role: \"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\"\n  relevance_score: 5\n\n- paper_id: hafner2023dreamerv3\n  title: \"Mastering Diverse Domains through World Models\"\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\n  year: 2023\n  venue: \"arXiv:2301.04104 (Nature 2025)\"\n  category: background\n  role: \"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\"\n  relevance_score: 5\n\n- paper_id: sharma2017figar\n  title: \"Fine Grained Action Repetition for Deep Reinforcement Learning\"\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\n  year: 2017\n  venue: \"ICLR Workshop\"\n  category: method-component\n  role: \"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\"\n  relevance_score: 4\n\n- paper_id: janner2019mbpo\n  title: \"When to Trust Your Model: Model-Based Policy Optimization\"\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\n  year: 2019\n  venue: NeurIPS\n  category: background\n  role: \"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Multi-step prediction error compounding\n# ============================================================\n\n- paper_id: ke2019learning\n  title: \"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\"\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\n  year: 2019\n  venue: ICLR\n  category: background\n  role: \"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\"\n  relevance_score: 4\n\n- paper_id: asadi2019combating\n  title: \"Combating the Compounding-Error Problem with a Multi-step Model\"\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\n  year: 2019\n  venue: \"arXiv:1905.13320\"\n  category: background\n  role: \"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\"\n  relevance_score: 4\n\n- paper_id: venkatraman2015improving\n  title: \"Improving Multi-Step Prediction of Learned Time Series Models\"\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\n  year: 2015\n  venue: AAAI\n  category: background\n  role: \"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\"\n  relevance_score: 3\n\n- paper_id: lambert2022investigating\n  title: \"Investigating Compounding Prediction Errors in Learned Dynamics Models\"\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\n  year: 2022\n  venue: \"arXiv:2203.09637\"\n  category: background\n  role: \"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Model-predictive control with learned dynamics\n# ============================================================\n\n- paper_id: chua2018pets\n  title: \"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\"\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\"\n  relevance_score: 3\n\n- paper_id: nagabandi2018neural\n  title: \"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\"\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\n  year: 2018\n  venue: ICRA\n  category: background\n  role: \"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Value overestimation mitigation\n# ============================================================\n\n- paper_id: thrun1993issues\n  title: \"Issues in Using Function Approximation for Reinforcement Learning\"\n  authors: [Thrun S., Schwartz A.]\n  year: 1993\n  venue: \"Connectionist Models Summer School\"\n  category: background\n  role: \"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\"\n  relevance_score: 4\n\n- paper_id: vanhasselt2016double\n  title: \"Deep Reinforcement Learning with Double Q-Learning\"\n  authors: [van Hasselt H., Guez A., Silver D.]\n  year: 2016\n  venue: AAAI\n  category: background\n  role: \"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\"\n  relevance_score: 4\n\n- paper_id: fujimoto2018td3\n  title: \"Addressing Function Approximation Error in Actor-Critic Methods\"\n  authors: [Fujimoto S., van Hoof H., Meger D.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\"\n  relevance_score: 4\n\n- paper_id: haarnoja2018sac\n  title: \"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\"\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\"\n  relevance_score: 3\n\n- paper_id: lee2021sunrise\n  title: \"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\"\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Delusional bias\n# ============================================================\n\n- paper_id: lu2018nondelusional\n  title: \"Non-delusional Q-learning and Value-Iteration\"\n  authors: [Lu T., Schuurmans D., Boutilier C.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Hierarchical RL with learned models\n# ============================================================\n\n- paper_id: hafner2022director\n  title: \"Deep Hierarchical Planning from Pixels\"\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\n  year: 2022\n  venue: NeurIPS\n  category: direct-competitor\n  role: \"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\"\n  relevance_score: 4\n\n- paper_id: nachum2018hiro\n  title: \"Data-Efficient Hierarchical Reinforcement Learning\"\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Action repeat / frame skip\n# ============================================================\n\n- paper_id: braylan2015frame\n  title: \"Frame Skip Is a Powerful Parameter for Learning to Play Atari\"\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\n  year: 2015\n  venue: \"AAAI Workshop on Learning for General Competency in Video Games\"\n  category: background\n  role: \"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\"\n  relevance_score: 3\n\n- paper_id: lakshminarayanan2017dynamic\n  title: \"Dynamic Action Repetition for Deep Reinforcement Learning\"\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\n  year: 2017\n  venue: AAAI\n  category: method-component\n  role: \"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\"\n  relevance_score: 4\n\n- paper_id: biedenkapp2021temporl\n  title: \"TempoRL: Learning When to Act\"\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV2\n# ============================================================\n\n- paper_id: hafner2021dreamerv2\n  title: \"Mastering Atari with Discrete World Models\"\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\n  year: 2021\n  venue: ICLR\n  category: background\n  role: \"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Alternative world model architectures\n# ============================================================\n\n- paper_id: micheli2023iris\n  title: \"Transformers are Sample-Efficient World Models\"\n  authors: [Micheli V., Alonso E., Fleuret F.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\"\n  relevance_score: 3\n\n- paper_id: robine2023twm\n  title: \"Transformer-based World Models Are Happy With 100k Interactions\"\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\"\n  relevance_score: 3\n\n- paper_id: chen2022transdreamer\n  title: \"TransDreamer: Reinforcement Learning with Transformer World Models\"\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\n  year: 2022\n  venue: \"arXiv:2202.09481\"\n  category: direct-competitor\n  role: \"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\n# ============================================================\n\n- paper_id: gumbsch2024thick\n  title: \"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\"\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\n  year: 2024\n  venue: ICLR\n  category: direct-competitor\n  role: \"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\"\n  relevance_score: 5\n\n- paper_id: mattes2024hieros\n  title: \"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\"\n  authors: [Mattes P., Schlosser R., Herbrich R.]\n  year: 2024\n  venue: ICML\n  category: direct-competitor\n  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n",
      "numLines": 296,
      "startLine": 1,
      "totalLines": 296
    }
  }
}
```

</details>

---

### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full file. Let me compile the papers to add. Based on my searches, here are the most relevant papers:

1. **Henderson et al. 2018** - "Deep Reinforcement Learning that Matters" - AAAI 2018
   - Foundational paper on seed variance/reproducibility in deep RL
   - Shows statistically different distributions from just random seeds with same hyperparameters
   - Angle 1: seed sensitivity

2. **Nikishin et al. 2022** - "The Primacy Bias in Deep Reinforcement Learning" - ICML 2022
   - Demonstrates how early training experiences create lasting biases that lead to overfitting and eventual performance collapse
   - Angle 3: delayed failure and initialization sensitivity

3. **Qiao et al. 2023** - "Mind the Model, Not the Agent: The Primacy Bias in Model-based RL" - ECAI 2024
   - Extends primacy bias findings to model-based RL, showing the world model's early training is more critical than agent training
   - Angle 2: Dreamer-family training instability and delayed failure modes

4. **Hussing et al. 2024** - "Dissecting Deep RL with High Update Ratios: Combatting Value Divergence" - RLC 2024
   - High update-to-data ratios cause value overestimation through optimizer momentum effects, with divergence tied to initialization
   - Angle 1 & 3: initialization-dependent divergence and progressive value explosion

5. **Barkley & Fridovich-Keil 2024** - "Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning" - ICML 2025
   - Synthetic rollouts can inconsistently degrade performance across environments, with overestimation bias as a key culprit
   - Angle 2: instability from imagination-based training

Now I'm preparing the YAML entries...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "9d413a37-23a5-49e5-a19c-f2a9f951cd01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01272wnSLnNrCXpECACPpyCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5274,
      "cache_read_input_tokens": 42656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5274
      },
      "output_tokens": 9,
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

_source line 51_

筛选出 5 篇论文，追加到 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "67937390-bc11-4f30-8f8e-e285ff7813a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01272wnSLnNrCXpECACPpyCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5274,
      "cache_read_input_tokens": 42656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5274
      },
      "output_tokens": 9,
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

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01TKSiJAYwHnmCXVmGPxPwwA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
  "old_string": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 28 papers (5 existing + 23 new)",
  "new_string": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 33 papers (5 existing + 28 new)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "169291aa-4448-4c20-bfca-59a80d09508d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01272wnSLnNrCXpECACPpyCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5274,
      "cache_read_input_tokens": 42656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5274
      },
      "output_tokens": 9,
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

_source line 53 · 2026-05-14T14:29:44.023Z_

<details><summary>↩ Tool result · `toolu_01TKSiJAYwHnmCXVmGPxPwwA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "1e2e7d2f-2add-4115-a7cf-5eaba27a7837",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
    "oldString": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 28 papers (5 existing + 23 new)",
    "newString": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 33 papers (5 existing + 28 new)",
    "originalFile": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 28 papers (5 existing + 23 new)\n\n# ============================================================\n# EXISTING CITATIONS (already in paper.tex)\n# ============================================================\n\n- paper_id: sutton1999options\n  title: \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\"\n  authors: [Sutton R.S., Precup D., Singh S.]\n  year: 1999\n  venue: \"Artificial Intelligence 112(1-2):181-211\"\n  category: background\n  role: \"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\"\n  relevance_score: 5\n\n- paper_id: hafner2020dreamerv1\n  title: \"Dream to Control: Learning Behaviors by Latent Imagination\"\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\n  year: 2020\n  venue: ICLR\n  category: background\n  role: \"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\"\n  relevance_score: 5\n\n- paper_id: hafner2023dreamerv3\n  title: \"Mastering Diverse Domains through World Models\"\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\n  year: 2023\n  venue: \"arXiv:2301.04104 (Nature 2025)\"\n  category: background\n  role: \"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\"\n  relevance_score: 5\n\n- paper_id: sharma2017figar\n  title: \"Fine Grained Action Repetition for Deep Reinforcement Learning\"\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\n  year: 2017\n  venue: \"ICLR Workshop\"\n  category: method-component\n  role: \"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\"\n  relevance_score: 4\n\n- paper_id: janner2019mbpo\n  title: \"When to Trust Your Model: Model-Based Policy Optimization\"\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\n  year: 2019\n  venue: NeurIPS\n  category: background\n  role: \"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Multi-step prediction error compounding\n# ============================================================\n\n- paper_id: ke2019learning\n  title: \"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\"\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\n  year: 2019\n  venue: ICLR\n  category: background\n  role: \"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\"\n  relevance_score: 4\n\n- paper_id: asadi2019combating\n  title: \"Combating the Compounding-Error Problem with a Multi-step Model\"\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\n  year: 2019\n  venue: \"arXiv:1905.13320\"\n  category: background\n  role: \"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\"\n  relevance_score: 4\n\n- paper_id: venkatraman2015improving\n  title: \"Improving Multi-Step Prediction of Learned Time Series Models\"\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\n  year: 2015\n  venue: AAAI\n  category: background\n  role: \"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\"\n  relevance_score: 3\n\n- paper_id: lambert2022investigating\n  title: \"Investigating Compounding Prediction Errors in Learned Dynamics Models\"\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\n  year: 2022\n  venue: \"arXiv:2203.09637\"\n  category: background\n  role: \"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Model-predictive control with learned dynamics\n# ============================================================\n\n- paper_id: chua2018pets\n  title: \"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\"\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\"\n  relevance_score: 3\n\n- paper_id: nagabandi2018neural\n  title: \"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\"\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\n  year: 2018\n  venue: ICRA\n  category: background\n  role: \"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Value overestimation mitigation\n# ============================================================\n\n- paper_id: thrun1993issues\n  title: \"Issues in Using Function Approximation for Reinforcement Learning\"\n  authors: [Thrun S., Schwartz A.]\n  year: 1993\n  venue: \"Connectionist Models Summer School\"\n  category: background\n  role: \"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\"\n  relevance_score: 4\n\n- paper_id: vanhasselt2016double\n  title: \"Deep Reinforcement Learning with Double Q-Learning\"\n  authors: [van Hasselt H., Guez A., Silver D.]\n  year: 2016\n  venue: AAAI\n  category: background\n  role: \"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\"\n  relevance_score: 4\n\n- paper_id: fujimoto2018td3\n  title: \"Addressing Function Approximation Error in Actor-Critic Methods\"\n  authors: [Fujimoto S., van Hoof H., Meger D.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\"\n  relevance_score: 4\n\n- paper_id: haarnoja2018sac\n  title: \"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\"\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\"\n  relevance_score: 3\n\n- paper_id: lee2021sunrise\n  title: \"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\"\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Delusional bias\n# ============================================================\n\n- paper_id: lu2018nondelusional\n  title: \"Non-delusional Q-learning and Value-Iteration\"\n  authors: [Lu T., Schuurmans D., Boutilier C.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Hierarchical RL with learned models\n# ============================================================\n\n- paper_id: hafner2022director\n  title: \"Deep Hierarchical Planning from Pixels\"\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\n  year: 2022\n  venue: NeurIPS\n  category: direct-competitor\n  role: \"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\"\n  relevance_score: 4\n\n- paper_id: nachum2018hiro\n  title: \"Data-Efficient Hierarchical Reinforcement Learning\"\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Action repeat / frame skip\n# ============================================================\n\n- paper_id: braylan2015frame\n  title: \"Frame Skip Is a Powerful Parameter for Learning to Play Atari\"\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\n  year: 2015\n  venue: \"AAAI Workshop on Learning for General Competency in Video Games\"\n  category: background\n  role: \"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\"\n  relevance_score: 3\n\n- paper_id: lakshminarayanan2017dynamic\n  title: \"Dynamic Action Repetition for Deep Reinforcement Learning\"\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\n  year: 2017\n  venue: AAAI\n  category: method-component\n  role: \"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\"\n  relevance_score: 4\n\n- paper_id: biedenkapp2021temporl\n  title: \"TempoRL: Learning When to Act\"\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV2\n# ============================================================\n\n- paper_id: hafner2021dreamerv2\n  title: \"Mastering Atari with Discrete World Models\"\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\n  year: 2021\n  venue: ICLR\n  category: background\n  role: \"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Alternative world model architectures\n# ============================================================\n\n- paper_id: micheli2023iris\n  title: \"Transformers are Sample-Efficient World Models\"\n  authors: [Micheli V., Alonso E., Fleuret F.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\"\n  relevance_score: 3\n\n- paper_id: robine2023twm\n  title: \"Transformer-based World Models Are Happy With 100k Interactions\"\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\"\n  relevance_score: 3\n\n- paper_id: chen2022transdreamer\n  title: \"TransDreamer: Reinforcement Learning with Transformer World Models\"\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\n  year: 2022\n  venue: \"arXiv:2202.09481\"\n  category: direct-competitor\n  role: \"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\n# ============================================================\n\n- paper_id: gumbsch2024thick\n  title: \"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\"\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\n  year: 2024\n  venue: ICLR\n  category: direct-competitor\n  role: \"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\"\n  relevance_score: 5\n\n- paper_id: mattes2024hieros\n  title: \"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\"\n  authors: [Mattes P., Schlosser R., Herbrich R.]\n  year: 2024\n  venue: ICML\n  category: direct-competitor\n  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " # Literature Map — event-gated-adaptive-horizon",
          " # Last updated: 2026-05-14",
          "-# Total: 28 papers (5 existing + 23 new)",
          "+# Total: 33 papers (5 existing + 28 new)",
          " ",
          " # ============================================================",
          " # EXISTING CITATIONS (already in paper.tex)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_01NKktyVfpoDttNw4epfWCX2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
  "old_string": "  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5",
  "new_string": "  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Seed-dependent instability & value overestimation in MBRL\n# ============================================================\n\n- paper_id: henderson2018deep\n  title: \"Deep Reinforcement Learning that Matters\"\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\n  year: 2018\n  venue: AAAI\n  category: background\n  role: \"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\"\n  relevance_score: 4\n\n- paper_id: nikishin2022primacy\n  title: \"The Primacy Bias in Deep Reinforcement Learning\"\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\n  year: 2022\n  venue: ICML\n  category: background\n  role: \"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\"\n  relevance_score: 4\n\n- paper_id: qiao2023mind\n  title: \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\"\n  authors: [Qiao Z., Lyu J., Li X.]\n  year: 2023\n  venue: \"arXiv:2310.15017 (ECAI 2024)\"\n  category: evaluation\n  role: \"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\"\n  relevance_score: 5\n\n- paper_id: hussing2024dissecting\n  title: \"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\"\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\n  year: 2024\n  venue: \"Reinforcement Learning Journal (RLC 2024)\"\n  category: evaluation\n  role: \"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\"\n  relevance_score: 4\n\n- paper_id: barkley2024stealing\n  title: \"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2024\n  venue: \"arXiv:2412.14312 (ICML 2025)\"\n  category: evaluation\n  role: \"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\"\n  relevance_score: 3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "df772266-0662-4c82-af35-d110f48e85e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9VRey7YJhb6WWrmH6vZZX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 47930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 827
      },
      "output_tokens": 72,
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

_source line 55 · 2026-05-14T14:30:03.580Z_

<details><summary>↩ Tool result · `toolu_01NKktyVfpoDttNw4epfWCX2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "f010141a-90c2-4453-ac37-4ddc025b16bb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
    "oldString": "  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5",
    "newString": "  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Seed-dependent instability & value overestimation in MBRL\n# ============================================================\n\n- paper_id: henderson2018deep\n  title: \"Deep Reinforcement Learning that Matters\"\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\n  year: 2018\n  venue: AAAI\n  category: background\n  role: \"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\"\n  relevance_score: 4\n\n- paper_id: nikishin2022primacy\n  title: \"The Primacy Bias in Deep Reinforcement Learning\"\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\n  year: 2022\n  venue: ICML\n  category: background\n  role: \"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\"\n  relevance_score: 4\n\n- paper_id: qiao2023mind\n  title: \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\"\n  authors: [Qiao Z., Lyu J., Li X.]\n  year: 2023\n  venue: \"arXiv:2310.15017 (ECAI 2024)\"\n  category: evaluation\n  role: \"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\"\n  relevance_score: 5\n\n- paper_id: hussing2024dissecting\n  title: \"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\"\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\n  year: 2024\n  venue: \"Reinforcement Learning Journal (RLC 2024)\"\n  category: evaluation\n  role: \"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\"\n  relevance_score: 4\n\n- paper_id: barkley2024stealing\n  title: \"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2024\n  venue: \"arXiv:2412.14312 (ICML 2025)\"\n  category: evaluation\n  role: \"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\"\n  relevance_score: 3",
    "originalFile": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-14\n# Total: 33 papers (5 existing + 28 new)\n\n# ============================================================\n# EXISTING CITATIONS (already in paper.tex)\n# ============================================================\n\n- paper_id: sutton1999options\n  title: \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\"\n  authors: [Sutton R.S., Precup D., Singh S.]\n  year: 1999\n  venue: \"Artificial Intelligence 112(1-2):181-211\"\n  category: background\n  role: \"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\"\n  relevance_score: 5\n\n- paper_id: hafner2020dreamerv1\n  title: \"Dream to Control: Learning Behaviors by Latent Imagination\"\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\n  year: 2020\n  venue: ICLR\n  category: background\n  role: \"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\"\n  relevance_score: 5\n\n- paper_id: hafner2023dreamerv3\n  title: \"Mastering Diverse Domains through World Models\"\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\n  year: 2023\n  venue: \"arXiv:2301.04104 (Nature 2025)\"\n  category: background\n  role: \"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\"\n  relevance_score: 5\n\n- paper_id: sharma2017figar\n  title: \"Fine Grained Action Repetition for Deep Reinforcement Learning\"\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\n  year: 2017\n  venue: \"ICLR Workshop\"\n  category: method-component\n  role: \"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\"\n  relevance_score: 4\n\n- paper_id: janner2019mbpo\n  title: \"When to Trust Your Model: Model-Based Policy Optimization\"\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\n  year: 2019\n  venue: NeurIPS\n  category: background\n  role: \"MBPO — formalizes model exploitation in MBRL; our delusional critic is a specific instance of model exploitation tied to temporal embedding\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Multi-step prediction error compounding\n# ============================================================\n\n- paper_id: ke2019learning\n  title: \"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\"\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\n  year: 2019\n  venue: ICLR\n  category: background\n  role: \"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\"\n  relevance_score: 4\n\n- paper_id: asadi2019combating\n  title: \"Combating the Compounding-Error Problem with a Multi-step Model\"\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\n  year: 2019\n  venue: \"arXiv:1905.13320\"\n  category: background\n  role: \"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\"\n  relevance_score: 4\n\n- paper_id: venkatraman2015improving\n  title: \"Improving Multi-Step Prediction of Learned Time Series Models\"\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\n  year: 2015\n  venue: AAAI\n  category: background\n  role: \"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\"\n  relevance_score: 3\n\n- paper_id: lambert2022investigating\n  title: \"Investigating Compounding Prediction Errors in Learned Dynamics Models\"\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\n  year: 2022\n  venue: \"arXiv:2203.09637\"\n  category: background\n  role: \"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Model-predictive control with learned dynamics\n# ============================================================\n\n- paper_id: chua2018pets\n  title: \"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\"\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\"\n  relevance_score: 3\n\n- paper_id: nagabandi2018neural\n  title: \"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\"\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\n  year: 2018\n  venue: ICRA\n  category: background\n  role: \"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Value overestimation mitigation\n# ============================================================\n\n- paper_id: thrun1993issues\n  title: \"Issues in Using Function Approximation for Reinforcement Learning\"\n  authors: [Thrun S., Schwartz A.]\n  year: 1993\n  venue: \"Connectionist Models Summer School\"\n  category: background\n  role: \"First identification of systematic value overestimation from function approximation; our delusional critic extends this to model-based imagination with temporal conditioning\"\n  relevance_score: 4\n\n- paper_id: vanhasselt2016double\n  title: \"Deep Reinforcement Learning with Double Q-Learning\"\n  authors: [van Hasselt H., Guez A., Silver D.]\n  year: 2016\n  venue: AAAI\n  category: background\n  role: \"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\"\n  relevance_score: 4\n\n- paper_id: fujimoto2018td3\n  title: \"Addressing Function Approximation Error in Actor-Critic Methods\"\n  authors: [Fujimoto S., van Hoof H., Meger D.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\"\n  relevance_score: 4\n\n- paper_id: haarnoja2018sac\n  title: \"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\"\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\"\n  relevance_score: 3\n\n- paper_id: lee2021sunrise\n  title: \"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\"\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified delusional critic mechanism\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Delusional bias\n# ============================================================\n\n- paper_id: lu2018nondelusional\n  title: \"Non-delusional Q-learning and Value-Iteration\"\n  authors: [Lu T., Schuurmans D., Boutilier C.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Hierarchical RL with learned models\n# ============================================================\n\n- paper_id: hafner2022director\n  title: \"Deep Hierarchical Planning from Pixels\"\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\n  year: 2022\n  venue: NeurIPS\n  category: direct-competitor\n  role: \"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\"\n  relevance_score: 4\n\n- paper_id: nachum2018hiro\n  title: \"Data-Efficient Hierarchical Reinforcement Learning\"\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Action repeat / frame skip\n# ============================================================\n\n- paper_id: braylan2015frame\n  title: \"Frame Skip Is a Powerful Parameter for Learning to Play Atari\"\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\n  year: 2015\n  venue: \"AAAI Workshop on Learning for General Competency in Video Games\"\n  category: background\n  role: \"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\"\n  relevance_score: 3\n\n- paper_id: lakshminarayanan2017dynamic\n  title: \"Dynamic Action Repetition for Deep Reinforcement Learning\"\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\n  year: 2017\n  venue: AAAI\n  category: method-component\n  role: \"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\"\n  relevance_score: 4\n\n- paper_id: biedenkapp2021temporl\n  title: \"TempoRL: Learning When to Act\"\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV2\n# ============================================================\n\n- paper_id: hafner2021dreamerv2\n  title: \"Mastering Atari with Discrete World Models\"\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\n  year: 2021\n  venue: ICLR\n  category: background\n  role: \"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Alternative world model architectures\n# ============================================================\n\n- paper_id: micheli2023iris\n  title: \"Transformers are Sample-Efficient World Models\"\n  authors: [Micheli V., Alonso E., Fleuret F.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\"\n  relevance_score: 3\n\n- paper_id: robine2023twm\n  title: \"Transformer-based World Models Are Happy With 100k Interactions\"\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\n  year: 2023\n  venue: ICLR\n  category: direct-competitor\n  role: \"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\"\n  relevance_score: 3\n\n- paper_id: chen2022transdreamer\n  title: \"TransDreamer: Reinforcement Learning with Transformer World Models\"\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\n  year: 2022\n  venue: \"arXiv:2202.09481\"\n  category: direct-competitor\n  role: \"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\n# ============================================================\n\n- paper_id: gumbsch2024thick\n  title: \"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\"\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\n  year: 2024\n  venue: ICLR\n  category: direct-competitor\n  role: \"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\"\n  relevance_score: 5\n\n- paper_id: mattes2024hieros\n  title: \"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\"\n  authors: [Mattes P., Schlosser R., Herbrich R.]\n  year: 2024\n  venue: ICML\n  category: direct-competitor\n  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n",
    "structuredPatch": [
      {
        "oldStart": 293,
        "oldLines": 3,
        "newStart": 293,
        "newLines": 52,
        "lines": [
          "   category: direct-competitor",
          "   role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"",
          "   relevance_score: 5",
          "+",
          "+# ============================================================",
          "+# NEW: Seed-dependent instability & value overestimation in MBRL",
          "+# ============================================================",
          "+",
          "+- paper_id: henderson2018deep",
          "+  title: \"Deep Reinforcement Learning that Matters\"",
          "+  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]",
          "+  year: 2018",
          "+  venue: AAAI",
          "+  category: background",
          "+  role: \"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\"",
          "+  relevance_score: 4",
          "+",
          "+- paper_id: nikishin2022primacy",
          "+  title: \"The Primacy Bias in Deep Reinforcement Learning\"",
          "+  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]",
          "+  year: 2022",
          "+  venue: ICML",
          "+  category: background",
          "+  role: \"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\"",
          "+  relevance_score: 4",
          "+",
          "+- paper_id: qiao2023mind",
          "+  title: \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\"",
          "+  authors: [Qiao Z., Lyu J., Li X.]",
          "+  year: 2023",
          "+  venue: \"arXiv:2310.15017 (ECAI 2024)\"",
          "+  category: evaluation",
          "+  role: \"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\"",
          "+  relevance_score: 5",
          "+",
          "+- paper_id: hussing2024dissecting",
          "+  title: \"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\"",
          "+  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]",
          "+  year: 2024",
          "+  venue: \"Reinforcement Learning Journal (RLC 2024)\"",
          "+  category: evaluation",
          "+  role: \"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\"",
          "+  relevance_score: 4",
          "+",
          "+- paper_id: barkley2024stealing",
          "+  title: \"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\"",
          "+  authors: [Barkley B., Fridovich-Keil D.]",
          "+  year: 2024",
          "+  venue: \"arXiv:2412.14312 (ICML 2025)\"",
          "+  category: evaluation",
          "+  role: \"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\"",
          "+  relevance_score: 3"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 56_

现在用 MCP 工具注册更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "9c7317fe-8ef2-44ba-b7b3-93c5c239528f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8LKKMjnaRQxLj69ZM5Xxz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1149,
      "cache_read_input_tokens": 48757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1149
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

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01J57s67bSnXxRkSAQEfBAp4`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "db005ec3-4375-4260-bf07-fa1e44c599a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8LKKMjnaRQxLj69ZM5Xxz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1149,
      "cache_read_input_tokens": 48757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1149
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

### Tool result

_source line 58 · 2026-05-14T14:30:06.914Z_

<details><summary>↩ Tool result · `toolu_01J57s67bSnXxRkSAQEfBAp4`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "f3afbd9b-17d9-4139-b8f8-61cc21b1068e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool only allows writing to memory.md, writing_plan.yaml, paper_framing.md. literature_map.yaml is not in the whitelist. But I already edited the file directly using the Edit tool, so the file is already updated. Let me verify the file was written correctly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "1cf6a3ba-fbc9-4c61-af66-b11d3f3e1199",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSu1WvKEXu9rvK8ptdQWMb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 49906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 378
      },
      "output_tokens": 36,
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

_source line 60_

文件已通过 Edit 工具直接更新。验证一下追加的内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "ee7e37ba-1549-496c-b84a-729638b0e86a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSu1WvKEXu9rvK8ptdQWMb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 49906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 378
      },
      "output_tokens": 36,
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

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_0148U62zkh4d99LvB272mAGS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
  "offset": 290
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "fcffd293-d7a4-4f90-88c5-483c970370f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSu1WvKEXu9rvK8ptdQWMb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 49906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 378
      },
      "output_tokens": 36,
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

_source line 62 · 2026-05-14T14:30:12.103Z_

<details><summary>↩ Tool result · `toolu_0148U62zkh4d99LvB272mAGS`</summary>

```text
290	  authors: [Mattes P., Schlosser R., Herbrich R.]
291	  year: 2024
292	  venue: ICML
293	  category: direct-competitor
294	  role: "Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify"
295	  relevance_score: 5
296	
297	# ============================================================
298	# NEW: Seed-dependent instability & value overestimation in MBRL
299	# ============================================================
300	
301	- paper_id: henderson2018deep
302	  title: "Deep Reinforcement Learning that Matters"
303	  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]
304	  year: 2018
305	  venue: AAAI
306	  category: background
307	  role: "Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config"
308	  relevance_score: 4
309	
310	- paper_id: nikishin2022primacy
311	  title: "The Primacy Bias in Deep Reinforcement Learning"
312	  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]
313	  year: 2022
314	  venue: ICML
315	  category: background
316	  role: "Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent"
317	  relevance_score: 4
318	
319	- paper_id: qiao2023mind
320	  title: "Mind the Model, Not the Agent: The Primacy Bias in Model-based RL"
321	  authors: [Qiao Z., Lyu J., Li X.]
322	  year: 2023
323	  venue: "arXiv:2310.15017 (ECAI 2024)"
324	  category: evaluation
325	  role: "Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't"
326	  relevance_score: 5
327	
328	- paper_id: hussing2024dissecting
329	  title: "Dissecting Deep RL with High Update Ratios: Combatting Value Divergence"
330	  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]
331	  year: 2024
332	  venue: "Reinforcement Learning Journal (RLC 2024)"
333	  category: evaluation
334	  role: "Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization"
335	  relevance_score: 4
336	
337	- paper_id: barkley2024stealing
338	  title: "Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning"
339	  authors: [Barkley B., Fridovich-Keil D.]
340	  year: 2024
341	  venue: "arXiv:2412.14312 (ICML 2025)"
342	  category: evaluation
343	  role: "Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix"
344	  relevance_score: 3
345	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "8b53d1d6-dc3c-4f01-95d0-ce4ebdd0c3b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
      "content": "  authors: [Mattes P., Schlosser R., Herbrich R.]\n  year: 2024\n  venue: ICML\n  category: direct-competitor\n  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Seed-dependent instability & value overestimation in MBRL\n# ============================================================\n\n- paper_id: henderson2018deep\n  title: \"Deep Reinforcement Learning that Matters\"\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\n  year: 2018\n  venue: AAAI\n  category: background\n  role: \"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\"\n  relevance_score: 4\n\n- paper_id: nikishin2022primacy\n  title: \"The Primacy Bias in Deep Reinforcement Learning\"\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\n  year: 2022\n  venue: ICML\n  category: background\n  role: \"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\"\n  relevance_score: 4\n\n- paper_id: qiao2023mind\n  title: \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\"\n  authors: [Qiao Z., Lyu J., Li X.]\n  year: 2023\n  venue: \"arXiv:2310.15017 (ECAI 2024)\"\n  category: evaluation\n  role: \"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\"\n  relevance_score: 5\n\n- paper_id: hussing2024dissecting\n  title: \"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\"\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\n  year: 2024\n  venue: \"Reinforcement Learning Journal (RLC 2024)\"\n  category: evaluation\n  role: \"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our delusional critic where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\"\n  relevance_score: 4\n\n- paper_id: barkley2024stealing\n  title: \"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2024\n  venue: \"arXiv:2412.14312 (ICML 2025)\"\n  category: evaluation\n  role: \"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\"\n  relevance_score: 3\n",
      "numLines": 56,
      "startLine": 290,
      "totalLines": 345
    }
  }
}
```

</details>

---

### Assistant

_source line 63_

已追加 5 篇论文到 `literature_map.yaml`（总数 28→33）。按三个搜索角度的覆盖情况：

**角度 1 — Seed/initialization sensitivity in value overestimation**
- **Henderson et al. 2018** (AAAI): 证明相同超参下不同 seed 产生统计显著的性能分布差异
- **Hussing et al. 2024** (RLC): value divergence 的发生与 optimizer momentum 和初始化相关，onset timing 不固定

**角度 2 — Dreamer-family training instability**
- **Qiao et al. 2023** (ECAI 2024): 直接在 DreamerV2 上验证 primacy bias，发现 world model 的 primacy bias 比 agent 的更关键 — 最高相关度
- **Barkley & Fridovich-Keil 2024** (ICML 2025): synthetic rollout 在不同环境下不一致地降低性能，overestimation 是贡献因素之一

**角度 3 — Value overestimation as delayed failure**
- **Nikishin et al. 2022** (ICML): primacy bias 导致 initially fine → eventually pathological 的渐进退化模式，collapse timing seed-dependent

**Gap 分析**: 搜索确认 "seed-dependent value overestimation in MBRL" 没有被任何论文作为核心主题研究。现有工作分别讨论了 seed variance（Henderson）、delayed collapse via primacy bias（Nikishin, Qiao）、imagination-induced overestimation（Barkley），但没有论文将这三者关联起来解释 "为什么同一配置下某些 seed collapse 而其他 seed 不会"。这是一个 novelty signal — 我们的实验（seed 0 稳定 vs seed 2 borderline collapse）是对这一现象的直接观测。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "uuid": "c3303676-3ca6-4477-9f74-aed24a77ad2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn9nLCLifqhHP6KsTGrMfd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 50284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1296
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

_source line 64_

已追加 5 篇论文到 `literature_map.yaml`（总数 28→33）。按三个搜索角度的覆盖情况：

**角度 1 — Seed/initialization sensitivity in value overestimation**
- **Henderson et al. 2018** (AAAI): 证明相同超参下不同 seed 产生统计显著的性能分布差异
- **Hussing et al. 2024** (RLC): value divergence 的发生与 optimizer momentum 和初始化相关，onset timing 不固定

**角度 2 — Dreamer-family training instability**
- **Qiao et al. 2023** (ECAI 2024): 直接在 DreamerV2 上验证 primacy bias，发现 world model 的 primacy bias 比 agent 的更关键 — 最高相关度
- **Barkley & Fridovich-Keil 2024** (ICML 2025): synthetic rollout 在不同环境下不一致地降低性能，overestimation 是贡献因素之一

**角度 3 — Value overestimation as delayed failure**
- **Nikishin et al. 2022** (ICML): primacy bias 导致 initially fine → eventually pathological 的渐进退化模式，collapse timing seed-dependent

**Gap 分析**: 搜索确认 "seed-dependent value overestimation in MBRL" 没有被任何论文作为核心主题研究。现有工作分别讨论了 seed variance（Henderson）、delayed collapse via primacy bias（Nikishin, Qiao）、imagination-induced overestimation（Barkley），但没有论文将这三者关联起来解释 "为什么同一配置下某些 seed collapse 而其他 seed 不会"。这是一个 novelty signal — 我们的实验（seed 0 稳定 vs seed 2 borderline collapse）是对这一现象的直接观测。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 148550,
  "duration_api_ms": 220685,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "badb957c-2ab9-4fd4-8ac5-45b1099c2811",
  "total_cost_usd": 0.9998642500000001,
  "usage": {
    "input_tokens": 18,
    "cache_creation_input_tokens": 40133,
    "cache_read_input_tokens": 437890,
    "output_tokens": 5134,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40133,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 538,
        "cache_read_input_tokens": 50284,
        "cache_creation_input_tokens": 1296,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1296
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 228053,
      "outputTokens": 6719,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 14,
      "costUSD": 0.401648,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 18,
      "outputTokens": 5134,
      "cacheReadInputTokens": 437890,
      "cacheCreationInputTokens": 40133,
      "webSearchRequests": 0,
      "costUSD": 0.5982162499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7817d2b0-8bf3-46a6-a284-330435608751"
}
```

</details>

---
