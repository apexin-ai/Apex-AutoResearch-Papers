# research itpr deep read

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_research_itpr-deep-read_20260513T090907.log`
- **Structured JSON:** [`5bf90b6cb182365c301c.json`](../../sessions/5b/5bf90b6cb182365c301c.json)

## Before a recorded user message

32 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "9ac64b00-0ed6-4b6a-9d10-9aedaa867af3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
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
    "resetsAt": 1778664000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "61a9670f-3657-4238-8bef-05c7976a8d55",
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622"
}
```

---

### Assistant

_source line 4_

I'll fetch the ITP-R paper and extract the required information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "b632c2c1-56b0-4248-a7e4-dbb581508ea6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Myeuit9C1hVkQCYkc8zTZu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11486,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11486
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Vno86iwfRwmH8SdEsYmHkY`</summary>

```json
{
  "query": "select:WebFetch,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "514f942f-f01d-4208-a70a-82b1ad7ffa1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Myeuit9C1hVkQCYkc8zTZu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11486,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11486
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

_source line 6 · 2026-05-13T09:09:20.869Z_

<details><summary>↩ Tool result · `toolu_01Vno86iwfRwmH8SdEsYmHkY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "fc81e02f-8984-4323-9fc5-5b6be00a09a4",
  "tool_use_result": {
    "matches": [
      "WebFetch",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:WebFetch,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the ITP-R paper from arXiv. I'll use the HTML version for better text extraction, and also fetch the PDF abstract page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "2febbc6b-c466-4a1b-a161-9781f3a688fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A7q676LBkfxVYzmheb8KP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 23327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 31,
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

Let me fetch the paper content from arXiv. I'll grab both the abstract page and the HTML version for full text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "bba68fdd-5741-4f0b-8f2f-49b4756b2719",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A7q676LBkfxVYzmheb8KP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 23327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 31,
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RTGRK8psPYCVtRMpgqXoxh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.08955",
  "prompt": "Extract the full title, authors, and complete abstract of this paper. Also extract any metadata like submission date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "c5491b10-d220-49ec-ac0a-7fa7134121ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A7q676LBkfxVYzmheb8KP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 23327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 31,
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

_source line 10 · 2026-05-13T09:09:30.348Z_

<details><summary>↩ Tool result · `toolu_01RTGRK8psPYCVtRMpgqXoxh`</summary>

```text
# Paper Information

**Full Title:** Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models

**Authors:** Youwei Liu, Jian Wang, Hanlin Wang, Beichen Guo, Wenjie Li

**Submission Date:** January 13, 2026 (v1); March 16, 2026 (v2)

**arXiv Identifier:** 2601.08955

## Abstract Summary

The paper proposes a framework enabling agents to learn through forward-looking simulation using world models. The approach involves an agent's policy generating multi-step "imagined" trajectories by interacting with a learned world model. A key innovation is an adaptive mechanism that adjusts how far into the future the agent plans based on task requirements and current progress. These simulated trajectories reveal insights about future outcomes and potential obstacles, which combine with present observations to guide policy development. The researchers demonstrate both versions without reinforcement learning and with RL-based variants. Testing across multiple benchmarks shows the method substantially surpasses comparable approaches, with analysis confirming that adaptive lookahead meaningfully strengthens agent reasoning capabilities.

**Subject Areas:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

**License:** CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "a0667931-d8c7-48f4-af7c-059182f71bbe",
  "tool_use_result": {
    "bytes": 47432,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Information\n\n**Full Title:** Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\n\n**Authors:** Youwei Liu, Jian Wang, Hanlin Wang, Beichen Guo, Wenjie Li\n\n**Submission Date:** January 13, 2026 (v1); March 16, 2026 (v2)\n\n**arXiv Identifier:** 2601.08955\n\n## Abstract Summary\n\nThe paper proposes a framework enabling agents to learn through forward-looking simulation using world models. The approach involves an agent's policy generating multi-step \"imagined\" trajectories by interacting with a learned world model. A key innovation is an adaptive mechanism that adjusts how far into the future the agent plans based on task requirements and current progress. These simulated trajectories reveal insights about future outcomes and potential obstacles, which combine with present observations to guide policy development. The researchers demonstrate both versions without reinforcement learning and with RL-based variants. Testing across multiple benchmarks shows the method substantially surpasses comparable approaches, with analysis confirming that adaptive lookahead meaningfully strengthens agent reasoning capabilities.\n\n**Subject Areas:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)\n\n**License:** CC BY 4.0",
    "durationMs": 4660,
    "url": "https://arxiv.org/abs/2601.08955"
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QUjEWvhSiiKMNEQsUSRk6z`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.08955",
  "prompt": "Extract ALL content from this paper. I need:\n\n1. COMPLETE experimental results for ScienceWorld: all scores (seen/unseen variations, continuous score, success rate), per-task type scores if available, all baseline comparisons with their exact scores, and experimental setup details (episodes, max steps, variations).\n\n2. COMPLETE experimental results for ALFWorld: total scores, per-subtask scores, all baseline comparisons.\n\n3. K-head predictor / Gating mechanism details: architecture, how it works, gating distribution (what proportion of steps route to world model vs direct LLM reasoning), differences across task types.\n\n4. World Model details: how it's trained, input/output format, relationship with the environment (learned approximation vs real environment).\n\n5. Ablation study results: performance drops when removing world model or gating, world model quality analysis and prediction accuracy.\n\n6. Training cost: GPU hours, training duration, model sizes, training data amounts.\n\n7. Any analysis of when/where the world model is accurate vs inaccurate.\n\nPlease be as detailed and precise as possible, including all numerical values from tables and figures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "a2f77210-bc40-4e71-b5e8-202aafed8b4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016A7q676LBkfxVYzmheb8KP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 23327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 31,
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

_source line 12 · 2026-05-13T09:09:56.069Z_

<details><summary>↩ Tool result · `toolu_01QUjEWvhSiiKMNEQsUSRk6z`</summary>

```text
# Comprehensive Extraction: ITP Paper Results & Details

## 1. SCIENCEWORLD EXPERIMENTAL RESULTS

**Success Rates by Backbone Model:**

| Backbone | Method | Seen (%) | Unseen (%) |
|----------|--------|----------|-----------|
| Qwen2.5-7B | CoT | 3.09 | 4.63 |
| Qwen2.5-7B | ReAct | 8.24 | 9.93 |
| Qwen2.5-7B | RAP | 10.30 | 16.55 |
| Qwen2.5-7B | ITP_I | 16.49 | 17.88 |
| Qwen2.5-7B | SFT | 55.67 | 49.00 |
| Qwen2.5-7B | WKM | 54.12 | 56.29 |
| Qwen2.5-7B | IWM | 60.82 | 57.61 |
| Qwen2.5-7B | **ITP_R** | **62.58** | **58.94** |
| Qwen3-8B | CoT | 2.44 | 1.99 |
| Qwen3-8B | ReAct | 9.79 | 8.61 |
| Qwen3-8B | RAP | 15.46 | 27.14 |
| Qwen3-8B | ITP_I | 20.61 | 19.86 |
| Qwen3-8B | SFT | 56.70 | 49.67 |
| Qwen3-8B | WKM | 60.31 | 47.68 |
| Qwen3-8B | IWM | 59.27 | 54.30 |
| Qwen3-8B | **ITP_R** | **61.85** | **56.95** |
| Llama-3.1-8B | CoT | 3.09 | 3.31 |
| Llama-3.1-8B | ReAct | 9.27 | 13.24 |
| Llama-3.1-8B | RAP | 11.34 | 17.21 |
| Llama-3.1-8B | ITP_I | 19.58 | 19.20 |
| Llama-3.1-8B | SFT | 57.21 | 50.33 |
| Llama-3.1-8B | WKM | 61.34 | 54.96 |
| Llama-3.1-8B | IWM | 57.56 | 56.29 |
| Llama-3.1-8B | **ITP_R** | **63.91** | **57.61** |

**Dataset Scale:** Training: 1,483 episodes | Test-Seen: 194 | Test-Unseen: 151

## 2. ALFWORLD EXPERIMENTAL RESULTS

**Success Rates Across Tasks (Qwen3-8B shown):**

| Method | PICK | CLEAN | HEAT | COOL | LOOK | PICK2 | Overall |
|--------|------|-------|------|------|------|-------|---------|
| CoT | 14.29 | 14.81 | 12.50 | 12.00 | 15.38 | 12.50 | 13.57 |
| ReAct | 25.71 | 22.22 | 12.50 | 12.00 | 7.69 | 25.00 | 19.29 |
| RAP | 42.86 | 37.04 | 37.50 | 16.00 | 15.38 | 4.17 | 28.57 |
| ITP_I | 82.86 | 25.93 | 12.50 | 16.00 | 23.08 | 54.17 | 41.43 |
| SFT | 71.43 | 70.37 | 68.75 | 72.00 | 69.23 | 70.83 | 70.71 |
| WKM | 80.00 | 77.78 | 81.25 | 80.00 | 76.92 | 79.17 | 79.29 |
| IWM | 85.71 | 85.19 | 87.50 | 84.00 | 46.15 | 87.50 | 82.14 |
| **ITP_R** | **97.14** | **88.88** | **93.75** | **88.00** | **76.92** | **79.17** | **88.57** |

**Dataset Scale:** Training: 3,119 | Test: 140

## 3. K-HEAD PREDICTOR / GATING MECHANISM

**Architecture & Function:**
The K-head is described as "a lightweight K-head predictor P_θ(K_t|s_t), which is a linear layer built on top of a backbone LLM" that predicts distributions over imagination horizons {0,1,...,K_max}.

**Training Process (Three Stages):**

1. **Pseudo-Labeling:** K~_t = argmax_{0≤k≤K_max}[log p_θ0(a*_t|s_t,τ̂^(k)_t) - λ_K k]
2. **Warm-Up Training:** Joint optimization of policy and K-head predictor via supervised learning on pseudo-labels
3. **Online Optimization:** Actor-Critic (A2C) with objective: L_A2C(θ) = L_act(θ) + α L_value(θ) + β L_ent(θ)

**Gating Distribution Analysis:**
Figure 6(b) shows "longer-horizon tasks induce larger lookahead steps." Specifically for ALFWorld: "success rate peaks at k=3," indicating optimal allocation varies by task. No explicit percentage breakdown provided for routing proportions.

**K_max Values by Benchmark:**
- ALFWorld: 5
- ScienceWorld: 8
- WebShop: 7
- StableToolBench: 3

## 4. WORLD MODEL DETAILS

**Training Objective:**
"L_WM(φ) = -E_{(s',s,a)∼D_WM}[log p_φ(s'|s,a)]" where D_WM = D_exp ∪ D_roll

**Input/Output Format:**
"Each training instance is formatted as a dialogue-style causal-LM example, where the input contains the task instruction, current observation, optional inventory or tool feedback, and action, and the target is the next observation."

**Training Details:**
- Objective: "NLL / CE on p_φ(s_{t+1}|s_t,a_t)"
- Training epochs/steps: 3 epochs / 3,450 steps
- Wall-clock time: 8.69 hours
- Validation loss: 0.052 (best) / 0.055 (final)
- Rollout collection: 9.5 GPU-hours on 1×A100

**Relationship to Environment:**
Learned approximation: "An LLM-based world model ℳ_φ that approximates the environment dynamics p_φ(s'|s,a)"

## 5. ABLATION STUDY RESULTS

**ITPR_R Performance Drop Without Online Reinforced Training:**
- ALFWorld: 88.57% → 71.42% (drop: **17.15 percentage points**)
- ScienceWorld: 59.70% → 46.00% (drop: **13.70 percentage points**)

**Analysis:** "Removing RT substantially degrades performance... confirming that online reinforced training is a core component rather than a minor training detail."

**World Model Quality (Fact-F1 Metric):**
Figure 6(a) demonstrates inverse relationship: "Fact-F1 degrades as the horizon increases due to compounding errors." Success rate follows bell curve peaking at k=3, showing "trade-off between foresight and prediction accuracy."

## 6. TRAINING COST ANALYSIS

**World Model Training (Qwen3-8B):**
- Time: 8.69 hours
- GPU-hours: 13.27 (2×A100)
- Throughput: 0.11 steps/s; 1.764 samples/s
- Effective batch size: 16
- Rollout collection: 9.5 GPU-hours

**ITPR_R Training (Stage-wise):**
- Stage 1 (Pseudo-Labeling): 6.63 hours / 13.27 GPU-hours
- Stage 2 (Warm-Up): 6.38 hours / 12.77 GPU-hours
- Stage 3 (Online Optimization): 4.78 hours / 9.57 GPU-hours
- **Total: 17.80 hours / 35.60 GPU-hours**

**Inference Deployment:**
- Decision latency p50: 14.2 seconds per step
- Policy time: 5.1 seconds
- Imagination time: 7.8 seconds
- Peak GPU VRAM (policy): 31.0/38.4 GB allocated/reserved

## 7. WORLD MODEL ACCURACY ANALYSIS

**Where Accurate vs. Inaccurate:**

**Accurate:** Short horizons (k=1-3) where "Fact-F1" metric remains stable. Figure 6(a) shows success maximized at k=3.

**Inaccurate:** Longer horizons show "compounding errors," with "Fact-F1 [that] degrades as the horizon increases." By k=8, prediction reliability drops significantly.

**Task-Specific Patterns:**
- ScienceWorld (longer tasks): favors k=8 maximum
- ALFWorld (shorter tasks): optimal at k=3-5
- StableToolBench: k=3 maximum (shortest tasks)

**Compute-Matched Analysis:**
ITP outperforms no-world-model baselines by +5.01 points (ITP_I) and +10.43 points (ITP_R), confirming gains "come not from extra compute alone, but from state-conditioned adaptive lookahead over imagined future states."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "0399dc16-e055-4211-b3cd-b4012ef427b5",
  "tool_use_result": {
    "bytes": 367208,
    "code": 200,
    "codeText": "OK",
    "result": "# Comprehensive Extraction: ITP Paper Results & Details\n\n## 1. SCIENCEWORLD EXPERIMENTAL RESULTS\n\n**Success Rates by Backbone Model:**\n\n| Backbone | Method | Seen (%) | Unseen (%) |\n|----------|--------|----------|-----------|\n| Qwen2.5-7B | CoT | 3.09 | 4.63 |\n| Qwen2.5-7B | ReAct | 8.24 | 9.93 |\n| Qwen2.5-7B | RAP | 10.30 | 16.55 |\n| Qwen2.5-7B | ITP_I | 16.49 | 17.88 |\n| Qwen2.5-7B | SFT | 55.67 | 49.00 |\n| Qwen2.5-7B | WKM | 54.12 | 56.29 |\n| Qwen2.5-7B | IWM | 60.82 | 57.61 |\n| Qwen2.5-7B | **ITP_R** | **62.58** | **58.94** |\n| Qwen3-8B | CoT | 2.44 | 1.99 |\n| Qwen3-8B | ReAct | 9.79 | 8.61 |\n| Qwen3-8B | RAP | 15.46 | 27.14 |\n| Qwen3-8B | ITP_I | 20.61 | 19.86 |\n| Qwen3-8B | SFT | 56.70 | 49.67 |\n| Qwen3-8B | WKM | 60.31 | 47.68 |\n| Qwen3-8B | IWM | 59.27 | 54.30 |\n| Qwen3-8B | **ITP_R** | **61.85** | **56.95** |\n| Llama-3.1-8B | CoT | 3.09 | 3.31 |\n| Llama-3.1-8B | ReAct | 9.27 | 13.24 |\n| Llama-3.1-8B | RAP | 11.34 | 17.21 |\n| Llama-3.1-8B | ITP_I | 19.58 | 19.20 |\n| Llama-3.1-8B | SFT | 57.21 | 50.33 |\n| Llama-3.1-8B | WKM | 61.34 | 54.96 |\n| Llama-3.1-8B | IWM | 57.56 | 56.29 |\n| Llama-3.1-8B | **ITP_R** | **63.91** | **57.61** |\n\n**Dataset Scale:** Training: 1,483 episodes | Test-Seen: 194 | Test-Unseen: 151\n\n## 2. ALFWORLD EXPERIMENTAL RESULTS\n\n**Success Rates Across Tasks (Qwen3-8B shown):**\n\n| Method | PICK | CLEAN | HEAT | COOL | LOOK | PICK2 | Overall |\n|--------|------|-------|------|------|------|-------|---------|\n| CoT | 14.29 | 14.81 | 12.50 | 12.00 | 15.38 | 12.50 | 13.57 |\n| ReAct | 25.71 | 22.22 | 12.50 | 12.00 | 7.69 | 25.00 | 19.29 |\n| RAP | 42.86 | 37.04 | 37.50 | 16.00 | 15.38 | 4.17 | 28.57 |\n| ITP_I | 82.86 | 25.93 | 12.50 | 16.00 | 23.08 | 54.17 | 41.43 |\n| SFT | 71.43 | 70.37 | 68.75 | 72.00 | 69.23 | 70.83 | 70.71 |\n| WKM | 80.00 | 77.78 | 81.25 | 80.00 | 76.92 | 79.17 | 79.29 |\n| IWM | 85.71 | 85.19 | 87.50 | 84.00 | 46.15 | 87.50 | 82.14 |\n| **ITP_R** | **97.14** | **88.88** | **93.75** | **88.00** | **76.92** | **79.17** | **88.57** |\n\n**Dataset Scale:** Training: 3,119 | Test: 140\n\n## 3. K-HEAD PREDICTOR / GATING MECHANISM\n\n**Architecture & Function:**\nThe K-head is described as \"a lightweight K-head predictor P_θ(K_t|s_t), which is a linear layer built on top of a backbone LLM\" that predicts distributions over imagination horizons {0,1,...,K_max}.\n\n**Training Process (Three Stages):**\n\n1. **Pseudo-Labeling:** K~_t = argmax_{0≤k≤K_max}[log p_θ0(a*_t|s_t,τ̂^(k)_t) - λ_K k]\n2. **Warm-Up Training:** Joint optimization of policy and K-head predictor via supervised learning on pseudo-labels\n3. **Online Optimization:** Actor-Critic (A2C) with objective: L_A2C(θ) = L_act(θ) + α L_value(θ) + β L_ent(θ)\n\n**Gating Distribution Analysis:**\nFigure 6(b) shows \"longer-horizon tasks induce larger lookahead steps.\" Specifically for ALFWorld: \"success rate peaks at k=3,\" indicating optimal allocation varies by task. No explicit percentage breakdown provided for routing proportions.\n\n**K_max Values by Benchmark:**\n- ALFWorld: 5\n- ScienceWorld: 8\n- WebShop: 7\n- StableToolBench: 3\n\n## 4. WORLD MODEL DETAILS\n\n**Training Objective:**\n\"L_WM(φ) = -E_{(s',s,a)∼D_WM}[log p_φ(s'|s,a)]\" where D_WM = D_exp ∪ D_roll\n\n**Input/Output Format:**\n\"Each training instance is formatted as a dialogue-style causal-LM example, where the input contains the task instruction, current observation, optional inventory or tool feedback, and action, and the target is the next observation.\"\n\n**Training Details:**\n- Objective: \"NLL / CE on p_φ(s_{t+1}|s_t,a_t)\"\n- Training epochs/steps: 3 epochs / 3,450 steps\n- Wall-clock time: 8.69 hours\n- Validation loss: 0.052 (best) / 0.055 (final)\n- Rollout collection: 9.5 GPU-hours on 1×A100\n\n**Relationship to Environment:**\nLearned approximation: \"An LLM-based world model ℳ_φ that approximates the environment dynamics p_φ(s'|s,a)\"\n\n## 5. ABLATION STUDY RESULTS\n\n**ITPR_R Performance Drop Without Online Reinforced Training:**\n- ALFWorld: 88.57% → 71.42% (drop: **17.15 percentage points**)\n- ScienceWorld: 59.70% → 46.00% (drop: **13.70 percentage points**)\n\n**Analysis:** \"Removing RT substantially degrades performance... confirming that online reinforced training is a core component rather than a minor training detail.\"\n\n**World Model Quality (Fact-F1 Metric):**\nFigure 6(a) demonstrates inverse relationship: \"Fact-F1 degrades as the horizon increases due to compounding errors.\" Success rate follows bell curve peaking at k=3, showing \"trade-off between foresight and prediction accuracy.\"\n\n## 6. TRAINING COST ANALYSIS\n\n**World Model Training (Qwen3-8B):**\n- Time: 8.69 hours\n- GPU-hours: 13.27 (2×A100)\n- Throughput: 0.11 steps/s; 1.764 samples/s\n- Effective batch size: 16\n- Rollout collection: 9.5 GPU-hours\n\n**ITPR_R Training (Stage-wise):**\n- Stage 1 (Pseudo-Labeling): 6.63 hours / 13.27 GPU-hours\n- Stage 2 (Warm-Up): 6.38 hours / 12.77 GPU-hours\n- Stage 3 (Online Optimization): 4.78 hours / 9.57 GPU-hours\n- **Total: 17.80 hours / 35.60 GPU-hours**\n\n**Inference Deployment:**\n- Decision latency p50: 14.2 seconds per step\n- Policy time: 5.1 seconds\n- Imagination time: 7.8 seconds\n- Peak GPU VRAM (policy): 31.0/38.4 GB allocated/reserved\n\n## 7. WORLD MODEL ACCURACY ANALYSIS\n\n**Where Accurate vs. Inaccurate:**\n\n**Accurate:** Short horizons (k=1-3) where \"Fact-F1\" metric remains stable. Figure 6(a) shows success maximized at k=3.\n\n**Inaccurate:** Longer horizons show \"compounding errors,\" with \"Fact-F1 [that] degrades as the horizon increases.\" By k=8, prediction reliability drops significantly.\n\n**Task-Specific Patterns:**\n- ScienceWorld (longer tasks): favors k=8 maximum\n- ALFWorld (shorter tasks): optimal at k=3-5\n- StableToolBench: k=3 maximum (shortest tasks)\n\n**Compute-Matched Analysis:**\nITP outperforms no-world-model baselines by +5.01 points (ITP_I) and +10.43 points (ITP_R), confirming gains \"come not from extra compute alone, but from state-conditioned adaptive lookahead over imagined future states.\"",
    "durationMs": 24959,
    "url": "https://arxiv.org/html/2601.08955"
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
I got good data from the HTML version. Let me also try to get some more details that might be missing - particularly the continuous scores for ScienceWorld (the tables above only show success rates), more details on the world model architecture, and the per-task ScienceWorld results.

Let me fetch more specific sections of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "bc7c8cb3-2c1c-434e-814b-7a9cb827281d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PwuVHKPc8VF7xad14SycW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3449,
      "cache_read_input_tokens": 24510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3449
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

_source line 14_

Good extraction. Let me get additional details - continuous scores for ScienceWorld and per-task breakdowns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "44dbcafb-7e88-4c4a-b5a6-ac267ca12a98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PwuVHKPc8VF7xad14SycW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3449,
      "cache_read_input_tokens": 24510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3449
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WzJefnJC6H68x8bFfhtBB8`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.08955",
  "prompt": "I need the following specific details that may have been missed:\n\n1. ScienceWorld CONTINUOUS SCORES (not just success rates) - there should be a separate table or scores showing continuous/partial credit scores for seen and unseen variations. Look for any table with \"continuous\" or \"score\" columns distinct from success rate.\n\n2. Per-task type breakdown for ScienceWorld - are there scores broken down by the 30 task types (like boil, melt, freeze, change-state, etc.)? If so, extract ALL of them.\n\n3. The exact architecture of the K-head predictor - is it just a single linear layer on top of the LLM's hidden states? What's the input dimension? How is it trained jointly?\n\n4. WebShop and StableToolBench results - extract complete tables for these benchmarks too.\n\n5. What is IWM baseline? How does it differ from ITP_R?\n\n6. What is the max_steps setting for ScienceWorld experiments? How many steps does the agent typically take?\n\n7. The exact RL algorithm used in Stage 3 - A2C details, reward function, discount factor.\n\n8. Figure descriptions - describe what Figures 5, 6, 7 show in detail.\n\n9. Any discussion of failure cases or limitations.\n\n10. The paper's own comparison to or discussion of using real simulators vs learned world models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "375effbb-7d9b-44cb-84df-b10b1667f11b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PwuVHKPc8VF7xad14SycW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3449,
      "cache_read_input_tokens": 24510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3449
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

_source line 16 · 2026-05-13T09:10:17.278Z_

<details><summary>↩ Tool result · `toolu_01WzJefnJC6H68x8bFfhtBB8`</summary>

```text
# Analysis of "Imagine-then-Plan" Paper

## Key Findings

### 1. **ScienceWorld Continuous Scores**
The paper does not provide separate continuous/partial credit scoring tables. Table 1 reports only success rates (percentage of tasks solved) for seen and unseen test splits.

### 2. **Per-Task Type Breakdown**
No breakdown by the 30 ScienceWorld task types is provided in the main paper or appendices. Results are aggregated across task categories.

### 3. **K-Head Predictor Architecture**
The paper describes it as "a lightweight K-head predictor" implemented as "a linear layer built on top of a backbone LLM that predicts distributions over imagination horizons." Specific input dimensions and layer details are not disclosed.

### 4. **WebShop and StableToolBench Results**
- **WebShop** (Table 1): Shows seen/unseen test performance metrics across backbone models
- **StableToolBench** (Table 2): Reports solvable pass rate (SoPR) and solvable win rate (SoWR) metrics with Qwen3-8B

### 5. **IWM Baseline Definition**
"IWM augments imitation learning with an implicit world-modeling objective to encourage the policy to internalize environment dynamics" (from baseline descriptions).

### 6. **ScienceWorld Max Steps**
Appendix C.5 indicates Kmax=8 for ScienceWorld, suggesting typical trajectories around 15 steps based on comparative task length discussions.

### 7. **Stage 3 RL Algorithm**
Uses "Advantage Actor-Critic (A2C)" with discount factor γ=0.99, lookahead penalty λK=0.2, step cost λstep=0.01, and entropy coefficient β=0.01.

### 8. **Figure Details**
- **Figure 5**: Success rates across different world-model backbones (Qwen, Llama, DeepSeek)
- **Figure 6**: Fact-F1 reliability degradation vs. lookahead horizon; learned K distributions correlate with task complexity
- **Figure 7**: Training data scale visualization across benchmarks

### 9. **Failure Cases/Limitations**
The Limitations section acknowledges: evaluation focuses on text-based environments rather than multimodal/robotic settings; world models introduce inference overhead despite higher success rates on complex tasks.

### 10. **Learned vs. Real Simulators**
No explicit comparison to real simulators is provided. The approach treats textual LLM predictions as environment dynamics proxies without comparison to ground-truth simulator alternatives.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "f49ef54d-b2cc-470b-b1a2-ee8c31e66616",
  "tool_use_result": {
    "bytes": 367208,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of \"Imagine-then-Plan\" Paper\n\n## Key Findings\n\n### 1. **ScienceWorld Continuous Scores**\nThe paper does not provide separate continuous/partial credit scoring tables. Table 1 reports only success rates (percentage of tasks solved) for seen and unseen test splits.\n\n### 2. **Per-Task Type Breakdown**\nNo breakdown by the 30 ScienceWorld task types is provided in the main paper or appendices. Results are aggregated across task categories.\n\n### 3. **K-Head Predictor Architecture**\nThe paper describes it as \"a lightweight K-head predictor\" implemented as \"a linear layer built on top of a backbone LLM that predicts distributions over imagination horizons.\" Specific input dimensions and layer details are not disclosed.\n\n### 4. **WebShop and StableToolBench Results**\n- **WebShop** (Table 1): Shows seen/unseen test performance metrics across backbone models\n- **StableToolBench** (Table 2): Reports solvable pass rate (SoPR) and solvable win rate (SoWR) metrics with Qwen3-8B\n\n### 5. **IWM Baseline Definition**\n\"IWM augments imitation learning with an implicit world-modeling objective to encourage the policy to internalize environment dynamics\" (from baseline descriptions).\n\n### 6. **ScienceWorld Max Steps**\nAppendix C.5 indicates Kmax=8 for ScienceWorld, suggesting typical trajectories around 15 steps based on comparative task length discussions.\n\n### 7. **Stage 3 RL Algorithm**\nUses \"Advantage Actor-Critic (A2C)\" with discount factor γ=0.99, lookahead penalty λK=0.2, step cost λstep=0.01, and entropy coefficient β=0.01.\n\n### 8. **Figure Details**\n- **Figure 5**: Success rates across different world-model backbones (Qwen, Llama, DeepSeek)\n- **Figure 6**: Fact-F1 reliability degradation vs. lookahead horizon; learned K distributions correlate with task complexity\n- **Figure 7**: Training data scale visualization across benchmarks\n\n### 9. **Failure Cases/Limitations**\nThe Limitations section acknowledges: evaluation focuses on text-based environments rather than multimodal/robotic settings; world models introduce inference overhead despite higher success rates on complex tasks.\n\n### 10. **Learned vs. Real Simulators**\nNo explicit comparison to real simulators is provided. The approach treats textual LLM predictions as environment dynamics proxies without comparison to ground-truth simulator alternatives.",
    "durationMs": 7898,
    "url": "https://arxiv.org/html/2601.08955"
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Let me also get the WebShop and StableToolBench numbers more precisely, and check for any more details on the world model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "c5dd35f2-c4d1-472d-a9ee-474e859decc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5N6S4jPXj8ugBWosddEPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 27959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1126
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

_source line 18_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CbDJ6mFyLkppAUKU3FaF7u`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.08955",
  "prompt": "Extract the COMPLETE Table 1 and Table 2 from this paper with ALL numbers. I need every single cell value.\n\nFor Table 1, it should cover multiple benchmarks (ScienceWorld, ALFWorld, WebShop) across multiple backbone models (Qwen2.5-7B, Qwen3-8B, Llama-3.1-8B) and multiple methods (CoT, ReAct, RAP, ITP_I, SFT, WKM, IWM, ITP_R).\n\nFor Table 2, it should cover StableToolBench results.\n\nAlso extract any other tables in the paper (ablation tables, world model quality tables, training cost tables).\n\nPlease reproduce the tables exactly as they appear, preserving all numerical values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "52a91056-9a5c-40be-88bd-bd89864a1f2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5N6S4jPXj8ugBWosddEPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 27959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1126
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

_source line 19 · 2026-05-13T09:10:44.459Z_

<details><summary>↩ Tool result · `toolu_01CbDJ6mFyLkppAUKU3FaF7u`</summary>

```text
# Tables from "Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"

## Table 1: Task Success Rates (%) Across Benchmarks

| Type | Method | ALFWorld ||||||| ScienceWorld ||| WebShop |
|------|--------|PICK|CLEAN|HEAT|COOL|LOOK|PICK2|Overall|Seen|Unseen|Total|
| **Qwen2.5-7B** |
| Prompting | CoT | 17.14 | 18.52 | 18.75 | 16.00 | 15.38 | 0.00 | 14.29 | 3.09 | 4.63 | 5.10 |
| | ReAct | 20.00 | 22.22 | 18.75 | 20.00 | 23.08 | 0.00 | 17.14 | 8.24 | 9.93 | 15.28 |
| | RAP | 40.00 | 33.33 | 6.25 | 32.00 | 15.38 | 20.83 | 27.86 | 10.30 | 16.55 | 11.28 |
| | **ITP_I (Ours)** | **65.71** | **25.93** | **25.00** | **24.00** | **30.77** | **25.00** | **35.71** | **16.49** | **17.88** | **20.10** |
| Training | SFT | 85.71 | 66.67 | 56.25 | 68.00 | 38.46 | 66.67 | 67.86 | 55.67 | 49.00 | 51.60 |
| | WKM | 77.14 | 77.78 | 75.00 | 76.00 | 76.92 | 75.00 | 76.43 | 54.12 | 56.29 | 58.80 |
| | IWM | 90.60 | 85.20 | 88.20 | 84.20 | 42.90 | 76.90 | 82.80 | 60.82 | 57.61 | 56.20 |
| | **ITP_R (Ours)** | **94.29** | **88.89** | **87.50** | **53.84** | **76.00** | **91.67** | **85.07** | **62.58** | **58.94** | **60.20** |

| Type | Method | ALFWorld ||||||| ScienceWorld ||| WebShop |
|------|--------|PICK|CLEAN|HEAT|COOL|LOOK|PICK2|Overall|Seen|Unseen|Total|
| **Qwen3-8B** |
| Prompting | CoT | 14.29 | 14.81 | 12.50 | 12.00 | 15.38 | 12.50 | 13.57 | 2.44 | 1.99 | 6.32 |
| | ReAct | 25.71 | 22.22 | 12.50 | 12.00 | 7.69 | 25.00 | 19.29 | 9.79 | 8.61 | 18.62 |
| | RAP | 42.86 | 37.04 | 37.50 | 16.00 | 15.38 | 4.17 | 28.57 | 15.46 | 27.14 | 12.40 |
| | **ITP_I (Ours)** | **82.86** | **25.93** | **12.50** | **16.00** | **23.08** | **54.17** | **41.43** | **20.61** | **19.86** | **25.25** |
| Training | SFT | 71.43 | 70.37 | 68.75 | 72.00 | 69.23 | 70.83 | 70.71 | 56.70 | 49.67 | 52.30 |
| | WKM | 80.00 | 77.78 | 81.25 | 80.00 | 76.92 | 79.17 | 79.29 | 60.31 | 47.68 | 61.15 |
| | IWM | 85.71 | 85.19 | 87.50 | 84.00 | 46.15 | 87.50 | 82.14 | 59.27 | 54.30 | 57.30 |
| | **ITP_R (Ours)** | **97.14** | **88.88** | **93.75** | **88.00** | **76.92** | **79.17** | **88.57** | **61.85** | **56.95** | **68.10** |

| Type | Method | ALFWorld ||||||| ScienceWorld ||| WebShop |
|------|--------|PICK|CLEAN|HEAT|COOL|LOOK|PICK2|Overall|Seen|Unseen|Total|
| **Llama-3.1-8B-Instruct** |
| Prompting | CoT | 17.14 | 14.81 | 18.75 | 16.00 | 15.38 | 8.33 | 15.00 | 3.09 | 3.31 | 8.20 |
| | ReAct | 22.86 | 22.22 | 6.25 | 24.00 | 23.08 | 25.00 | 21.43 | 9.27 | 13.24 | 19.32 |
| | RAP | 25.71 | 25.93 | 6.25 | 32.00 | 7.69 | 25.00 | 22.86 | 11.34 | 17.21 | 16.05 |
| | **ITP_I (Ours)** | **57.14** | **37.04** | **31.25** | **28.00** | **23.08** | **33.33** | **37.86** | **19.58** | **19.20** | **24.30** |
| Training | SFT | 85.71 | 85.20 | 82.40 | 89.50 | 85.70 | 53.80 | 79.28 | 57.21 | 50.33 | 47.30 |
| | WKM | 85.71 | 85.19 | 75.00 | 80.00 | 38.46 | 79.17 | 77.86 | 61.34 | 54.96 | 65.58 |
| | IWM | 87.50 | 88.90 | 82.40 | 94.70 | 85.90 | 84.60 | 85.90 | 57.56 | 56.29 | 58.60 |
| | **ITP_R (Ours)** | **88.57** | **92.59** | **93.75** | **92.00** | **46.15** | **91.67** | **87.14** | **63.91** | **57.61** | **67.50** |

## Table 2: StableToolBench Results (Qwen3-8B)

| Type | Method | SoPR (%) | SoWR (%) |
|------|--------|----------|----------|
| Prompting | ReAct | 26 | 22 |
| | RAP | 28 | 26 |
| | **ITP_I (Ours)** | **35 (+7)** | **28 (+2)** |
| Training | SFT | 42 | 36 |
| | IWM | 44 | 36 |
| | **ITP_R (Ours)** | **68 (+24)** | **54 (+18)** |

## Additional Tables

**Table 3: Dataset Statistics**

| Domain | Task Description | Dataset Statistics |
|--------|------------------|-------------------|
| ALFWorld | "Household, text-based embodied tasks" | Six task families; Train: 3,119; Test: 140 |
| ScienceWorld | "Elementary science curriculum in interactive text environment" | 30 subtasks; Train: 1,483; Test-Seen: 194; Test-Unseen: 151 |
| WebShop | "Goal-driven web shopping in text-based browsing environment" | Train: 1,824; Test: 210 |
| StableToolBench | "Multi-turn tool-use tasks with executable tool interactions" | Train: 1,972; Test: 169 |

**Table 6: World-Model Training Diagnostics (Qwen3-8B)**

| Item | Value |
|------|-------|
| Objective | NLL / CE on p_φ(s_{t+1}\|s_t,a_t) |
| Training epochs / steps | 3 epochs / 3,450 steps |
| Wall-clock time | 8.69 h |
| Throughput | 0.11 steps/s; 1.764 samples/s |
| Best / final validation loss | 0.052 / 0.055 |
| Effective batch size | 16 |
| Max sequence length | 2048 |
| Optimizer | AdamW + cosine decay |
| Precision / hardware | bf16 on 2×A100 GPUs |
| Rollout collection cost | 9.5 GPU-hours |

**Table 8: ITPR Training Cost (Stage-wise)**

| Stage | Wall-clock | GPU-hours |
|-------|-----------|-----------|
| I: Lookahead Pseudo-Labeling | 6.63 h | 13.27 |
| II: Warm-Up Training | 6.38 h | 12.77 |
| III: Online Optimization | 4.78 h | 9.57 |
| **Total** | **17.80 h** | **35.60** |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "b0a35528-0cc4-460e-9261-94066e5971b2",
  "tool_use_result": {
    "bytes": 367208,
    "code": 200,
    "codeText": "OK",
    "result": "# Tables from \"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\"\n\n## Table 1: Task Success Rates (%) Across Benchmarks\n\n| Type | Method | ALFWorld ||||||| ScienceWorld ||| WebShop |\n|------|--------|PICK|CLEAN|HEAT|COOL|LOOK|PICK2|Overall|Seen|Unseen|Total|\n| **Qwen2.5-7B** |\n| Prompting | CoT | 17.14 | 18.52 | 18.75 | 16.00 | 15.38 | 0.00 | 14.29 | 3.09 | 4.63 | 5.10 |\n| | ReAct | 20.00 | 22.22 | 18.75 | 20.00 | 23.08 | 0.00 | 17.14 | 8.24 | 9.93 | 15.28 |\n| | RAP | 40.00 | 33.33 | 6.25 | 32.00 | 15.38 | 20.83 | 27.86 | 10.30 | 16.55 | 11.28 |\n| | **ITP_I (Ours)** | **65.71** | **25.93** | **25.00** | **24.00** | **30.77** | **25.00** | **35.71** | **16.49** | **17.88** | **20.10** |\n| Training | SFT | 85.71 | 66.67 | 56.25 | 68.00 | 38.46 | 66.67 | 67.86 | 55.67 | 49.00 | 51.60 |\n| | WKM | 77.14 | 77.78 | 75.00 | 76.00 | 76.92 | 75.00 | 76.43 | 54.12 | 56.29 | 58.80 |\n| | IWM | 90.60 | 85.20 | 88.20 | 84.20 | 42.90 | 76.90 | 82.80 | 60.82 | 57.61 | 56.20 |\n| | **ITP_R (Ours)** | **94.29** | **88.89** | **87.50** | **53.84** | **76.00** | **91.67** | **85.07** | **62.58** | **58.94** | **60.20** |\n\n| Type | Method | ALFWorld ||||||| ScienceWorld ||| WebShop |\n|------|--------|PICK|CLEAN|HEAT|COOL|LOOK|PICK2|Overall|Seen|Unseen|Total|\n| **Qwen3-8B** |\n| Prompting | CoT | 14.29 | 14.81 | 12.50 | 12.00 | 15.38 | 12.50 | 13.57 | 2.44 | 1.99 | 6.32 |\n| | ReAct | 25.71 | 22.22 | 12.50 | 12.00 | 7.69 | 25.00 | 19.29 | 9.79 | 8.61 | 18.62 |\n| | RAP | 42.86 | 37.04 | 37.50 | 16.00 | 15.38 | 4.17 | 28.57 | 15.46 | 27.14 | 12.40 |\n| | **ITP_I (Ours)** | **82.86** | **25.93** | **12.50** | **16.00** | **23.08** | **54.17** | **41.43** | **20.61** | **19.86** | **25.25** |\n| Training | SFT | 71.43 | 70.37 | 68.75 | 72.00 | 69.23 | 70.83 | 70.71 | 56.70 | 49.67 | 52.30 |\n| | WKM | 80.00 | 77.78 | 81.25 | 80.00 | 76.92 | 79.17 | 79.29 | 60.31 | 47.68 | 61.15 |\n| | IWM | 85.71 | 85.19 | 87.50 | 84.00 | 46.15 | 87.50 | 82.14 | 59.27 | 54.30 | 57.30 |\n| | **ITP_R (Ours)** | **97.14** | **88.88** | **93.75** | **88.00** | **76.92** | **79.17** | **88.57** | **61.85** | **56.95** | **68.10** |\n\n| Type | Method | ALFWorld ||||||| ScienceWorld ||| WebShop |\n|------|--------|PICK|CLEAN|HEAT|COOL|LOOK|PICK2|Overall|Seen|Unseen|Total|\n| **Llama-3.1-8B-Instruct** |\n| Prompting | CoT | 17.14 | 14.81 | 18.75 | 16.00 | 15.38 | 8.33 | 15.00 | 3.09 | 3.31 | 8.20 |\n| | ReAct | 22.86 | 22.22 | 6.25 | 24.00 | 23.08 | 25.00 | 21.43 | 9.27 | 13.24 | 19.32 |\n| | RAP | 25.71 | 25.93 | 6.25 | 32.00 | 7.69 | 25.00 | 22.86 | 11.34 | 17.21 | 16.05 |\n| | **ITP_I (Ours)** | **57.14** | **37.04** | **31.25** | **28.00** | **23.08** | **33.33** | **37.86** | **19.58** | **19.20** | **24.30** |\n| Training | SFT | 85.71 | 85.20 | 82.40 | 89.50 | 85.70 | 53.80 | 79.28 | 57.21 | 50.33 | 47.30 |\n| | WKM | 85.71 | 85.19 | 75.00 | 80.00 | 38.46 | 79.17 | 77.86 | 61.34 | 54.96 | 65.58 |\n| | IWM | 87.50 | 88.90 | 82.40 | 94.70 | 85.90 | 84.60 | 85.90 | 57.56 | 56.29 | 58.60 |\n| | **ITP_R (Ours)** | **88.57** | **92.59** | **93.75** | **92.00** | **46.15** | **91.67** | **87.14** | **63.91** | **57.61** | **67.50** |\n\n## Table 2: StableToolBench Results (Qwen3-8B)\n\n| Type | Method | SoPR (%) | SoWR (%) |\n|------|--------|----------|----------|\n| Prompting | ReAct | 26 | 22 |\n| | RAP | 28 | 26 |\n| | **ITP_I (Ours)** | **35 (+7)** | **28 (+2)** |\n| Training | SFT | 42 | 36 |\n| | IWM | 44 | 36 |\n| | **ITP_R (Ours)** | **68 (+24)** | **54 (+18)** |\n\n## Additional Tables\n\n**Table 3: Dataset Statistics**\n\n| Domain | Task Description | Dataset Statistics |\n|--------|------------------|-------------------|\n| ALFWorld | \"Household, text-based embodied tasks\" | Six task families; Train: 3,119; Test: 140 |\n| ScienceWorld | \"Elementary science curriculum in interactive text environment\" | 30 subtasks; Train: 1,483; Test-Seen: 194; Test-Unseen: 151 |\n| WebShop | \"Goal-driven web shopping in text-based browsing environment\" | Train: 1,824; Test: 210 |\n| StableToolBench | \"Multi-turn tool-use tasks with executable tool interactions\" | Train: 1,972; Test: 169 |\n\n**Table 6: World-Model Training Diagnostics (Qwen3-8B)**\n\n| Item | Value |\n|------|-------|\n| Objective | NLL / CE on p_φ(s_{t+1}\\|s_t,a_t) |\n| Training epochs / steps | 3 epochs / 3,450 steps |\n| Wall-clock time | 8.69 h |\n| Throughput | 0.11 steps/s; 1.764 samples/s |\n| Best / final validation loss | 0.052 / 0.055 |\n| Effective batch size | 16 |\n| Max sequence length | 2048 |\n| Optimizer | AdamW + cosine decay |\n| Precision / hardware | bf16 on 2×A100 GPUs |\n| Rollout collection cost | 9.5 GPU-hours |\n\n**Table 8: ITPR Training Cost (Stage-wise)**\n\n| Stage | Wall-clock | GPU-hours |\n|-------|-----------|-----------|\n| I: Lookahead Pseudo-Labeling | 6.63 h | 13.27 |\n| II: Warm-Up Training | 6.38 h | 12.77 |\n| III: Online Optimization | 4.78 h | 9.57 |\n| **Total** | **17.80 h** | **35.60** |",
    "durationMs": 20684,
    "url": "https://arxiv.org/html/2601.08955"
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive set of data from the paper. Let me also check for some more details about the RL algorithm and comparison with real simulators.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "ed24a652-c403-4402-9efb-cfcb0383e243",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019642Gfgvmr9pmEpJbgpNnA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 29085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xe4ukZAaPtEpG5mGYQUKae`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.08955",
  "prompt": "Extract these specific details:\n\n1. The EXACT reward function used in Stage 3 (Online Optimization / A2C). What signal does the agent receive? Is it task completion? Intermediate rewards?\n\n2. What is IWM exactly? Full name and method description. How does it differ from ITP_R specifically?\n\n3. What is WKM? Full name and method description.\n\n4. How does the world model generate rollouts? Does it auto-regressively predict multiple steps? Or one step at a time with the policy choosing actions?\n\n5. The \"imagination\" process: when the agent is at state s_t, how exactly does it use the world model? Does it simulate k steps ahead? What does it do with the imagined trajectory?\n\n6. How is K (the lookahead horizon) chosen at test time? Is it predicted by the K-head or fixed?\n\n7. Any mention of \"simulator\", \"simulation\", \"real environment\", \"ground truth\" in the context of comparing learned world models to actual environment simulators.\n\n8. The exact training data collection process - how are the expert trajectories obtained?\n\n9. The backbone LLM used for the world model - is it the same as the policy model or different?\n\n10. Any hyperparameters table - learning rates, batch sizes, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "41ef50fb-7a90-4fe9-8ebf-cf5bcadc4dc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019642Gfgvmr9pmEpJbgpNnA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 29085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

_source line 22 · 2026-05-13T09:11:05.944Z_

<details><summary>↩ Tool result · `toolu_01Xe4ukZAaPtEpG5mGYQUKae`</summary>

```text
# Analysis of "Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"

## 1. Reward Function (Stage 3)

The exact reward function is:
> "r_{t+1} = r_env − λ_K K_t − λ_step"

This combines environment rewards with penalties for lookahead depth and step redundancy. The agent receives task completion signals from the environment, minus computational costs.

## 2. IWM (Implicit World Model)

IWM is described as a baseline method that "augments imitation learning with an implicit world-modeling objective to encourage the policy to internalize environment dynamics." It differs from ITP_R in that IWM internalizes dynamics implicitly within the policy, whereas ITP_R explicitly uses a separate world model for lookahead planning.

## 3. WKM (World Knowledge Model)

WKM is a baseline that "trains a parametric world knowledge model that provides global task priors and local dynamic state knowledge to guide planning." Unlike ITP's adaptive lookahead, WKM provides static guidance without dynamic horizon adjustment.

## 4. World Model Rollout Generation

The world model generates rollouts auto-regressively. At each imagination step:
> "ŝ_{t+i+1} ∼ M_φ(·|ŝ_{t+i}, â_{t+i})"

The policy selects imagined actions, and the world model predicts next states sequentially, creating a multi-step trajectory.

## 5. Imagination Process

When at state s_t with lookahead horizon K_t, the agent:
> "interacts with M_φ for K_t steps within a 'mental sandbox'"

This produces imagined trajectory τ̂_t^(K_t). The agent then "reflects on the imagined trajectory to assess progress toward the goal and identify potential conflicts."

## 6. Lookahead Horizon Selection at Test Time

For ITP_I (training-free): The agent "analyzes the instruction and state s_t to choose an imagination horizon K_t ∈ {0,1,...,K_max}."

For ITP_R: The learned K-head predictor estimates: "K_t ∼ P_θ(K_t|s_t)"

## 7. Learned vs. Real Environment Comparison

The paper does not compare learned world models against actual environment simulators. It evaluates on four text-based benchmarks (ALFWorld, ScienceWorld, WebShop, StableToolBench) where the world model learns from expert trajectories, without mentioning ground-truth simulator access.

## 8. Training Data Collection

Expert trajectories come from benchmarks themselves. The agent then performs rollouts: "we ask the agent to perform rollouts in the environment, obtaining the rollout trajectories D_roll." Both D_exp and D_roll are combined for world model training.

## 9. World Model Backbone

The world model uses the same backbone as specified per experiment. The paper states: "we use Qwen3-8B to train the world model" (as default), but evaluates across "Qwen2.5-7B, Qwen3-8B, and Llama-3.1-8B." Different backbones tested for world model choice.

## 10. Hyperparameters

Table 9 provides comprehensive settings: learning rate 2×10⁻⁵ (warm-up), RL learning rate 5×10⁻⁶, batch size 1 with 16 gradient accumulation steps, λ_K=0.2, λ_step=0.01, K_max values vary by benchmark (3-8 steps).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "2ec6e5a0-376b-400e-ad2a-92b14220e92a",
  "tool_use_result": {
    "bytes": 367208,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of \"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\"\n\n## 1. Reward Function (Stage 3)\n\nThe exact reward function is:\n> \"r_{t+1} = r_env − λ_K K_t − λ_step\"\n\nThis combines environment rewards with penalties for lookahead depth and step redundancy. The agent receives task completion signals from the environment, minus computational costs.\n\n## 2. IWM (Implicit World Model)\n\nIWM is described as a baseline method that \"augments imitation learning with an implicit world-modeling objective to encourage the policy to internalize environment dynamics.\" It differs from ITP_R in that IWM internalizes dynamics implicitly within the policy, whereas ITP_R explicitly uses a separate world model for lookahead planning.\n\n## 3. WKM (World Knowledge Model)\n\nWKM is a baseline that \"trains a parametric world knowledge model that provides global task priors and local dynamic state knowledge to guide planning.\" Unlike ITP's adaptive lookahead, WKM provides static guidance without dynamic horizon adjustment.\n\n## 4. World Model Rollout Generation\n\nThe world model generates rollouts auto-regressively. At each imagination step:\n> \"ŝ_{t+i+1} ∼ M_φ(·|ŝ_{t+i}, â_{t+i})\"\n\nThe policy selects imagined actions, and the world model predicts next states sequentially, creating a multi-step trajectory.\n\n## 5. Imagination Process\n\nWhen at state s_t with lookahead horizon K_t, the agent:\n> \"interacts with M_φ for K_t steps within a 'mental sandbox'\"\n\nThis produces imagined trajectory τ̂_t^(K_t). The agent then \"reflects on the imagined trajectory to assess progress toward the goal and identify potential conflicts.\"\n\n## 6. Lookahead Horizon Selection at Test Time\n\nFor ITP_I (training-free): The agent \"analyzes the instruction and state s_t to choose an imagination horizon K_t ∈ {0,1,...,K_max}.\"\n\nFor ITP_R: The learned K-head predictor estimates: \"K_t ∼ P_θ(K_t|s_t)\"\n\n## 7. Learned vs. Real Environment Comparison\n\nThe paper does not compare learned world models against actual environment simulators. It evaluates on four text-based benchmarks (ALFWorld, ScienceWorld, WebShop, StableToolBench) where the world model learns from expert trajectories, without mentioning ground-truth simulator access.\n\n## 8. Training Data Collection\n\nExpert trajectories come from benchmarks themselves. The agent then performs rollouts: \"we ask the agent to perform rollouts in the environment, obtaining the rollout trajectories D_roll.\" Both D_exp and D_roll are combined for world model training.\n\n## 9. World Model Backbone\n\nThe world model uses the same backbone as specified per experiment. The paper states: \"we use Qwen3-8B to train the world model\" (as default), but evaluates across \"Qwen2.5-7B, Qwen3-8B, and Llama-3.1-8B.\" Different backbones tested for world model choice.\n\n## 10. Hyperparameters\n\nTable 9 provides comprehensive settings: learning rate 2×10⁻⁵ (warm-up), RL learning rate 5×10⁻⁶, batch size 1 with 16 gradient accumulation steps, λ_K=0.2, λ_step=0.01, K_max values vary by benchmark (3-8 steps).",
    "durationMs": 10703,
    "url": "https://arxiv.org/html/2601.08955"
  }
}
```

</details>

---

### Assistant

_source line 23_

Now I have all the information needed. Let me write the literature note to the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "ce6f66a8-c55d-4b6c-88ca-96444584910a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUPM1oaMLg2uK2tyDhqAU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 32021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1294
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

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Fk9oRRtN7TDKetLq3LFKzn`</summary>

```json
{
  "server": "autodl-simgate",
  "command": "mkdir -p /root/autodl-tmp/simgate-modular-routing/notes",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "61aafcf5-7673-4c49-8070-80271c6a2b82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUPM1oaMLg2uK2tyDhqAU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 32021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1294
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

_source line 25 · 2026-05-13T09:11:12.162Z_

<details><summary>↩ Tool result · `toolu_01Fk9oRRtN7TDKetLq3LFKzn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "0c8a7e52-54f9-4aa9-bc41-b3fc40dd8132",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.77}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Y5THMEMc9j9UeYn8BY4wBd`</summary>

```json
{
  "server": "autodl-simgate",
  "command": "cat > /root/autodl-tmp/simgate-modular-routing/notes/literature_itpr.md << 'HEREDOC'\n# ITP-R (Imagine-then-Plan with Reinforced Training)\n\n**Paper**: arXiv 2601.08955 (v2: 2026-03-16)\n**Authors**: Youwei Liu, Jian Wang, Hanlin Wang, Beichen Guo, Wenjie Li\n**Title**: Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\n\n---\n\n## 1. 核心方法\n\n### 总体框架\n- Agent 在每步决策时，用 learned world model 进行 K 步前瞻（\"mental sandbox\"）\n- K-head predictor 自适应选择前瞻步数 K_t ∈ {0, 1, ..., K_max}\n- K=0 表示不使用 world model，直接由 policy LLM 决策\n- 前瞻产生的 imagined trajectory 用于 reflect + plan，然后选择 real action\n\n### 两个变体\n- **ITP_I** (Inference-only): 不训练，用 prompting 让 LLM 自行选择 K 和做 imagination\n- **ITP_R** (Reinforced): 三阶段训练，含 K-head predictor + A2C online optimization\n\n---\n\n## 2. World Model\n\n### 架构\n- LLM-based world model M_φ，与 policy 用相同 backbone（如 Qwen3-8B）\n- 目标函数: NLL/CE on p_φ(s_{t+1} | s_t, a_t)\n- 输入格式: dialogue-style causal-LM，input = (task instruction, current observation, inventory/tool feedback, action)，target = next observation\n- **本质是 learned approximation，不是真实环境**\n\n### Rollout 生成\n- 自回归多步展开: ŝ_{t+i+1} ~ M_φ(·|ŝ_{t+i}, â_{t+i})\n- Policy 在 imagined state 上选 action，world model 预测 next state，迭代 K 步\n\n### 训练细节 (Qwen3-8B)\n| 项目 | 值 |\n|------|-----|\n| 训练数据 | D_exp (expert) ∪ D_roll (rollout) |\n| Epochs / Steps | 3 / 3,450 |\n| Wall-clock | 8.69 h |\n| Hardware | 2×A100, bf16 |\n| Best val loss | 0.052 |\n| Batch size | 16 (effective) |\n| Max seq length | 2048 |\n| Optimizer | AdamW + cosine decay |\n| Rollout 收集成本 | 9.5 GPU-hours |\n\n### World Model 质量\n- **Fact-F1 随 horizon 增加而下降**（compounding errors）\n- Success rate 在 k=3 左右 peak（ALFWorld），说明存在 foresight vs accuracy 的 trade-off\n- 没有给出具体的 per-task prediction accuracy 数字\n\n---\n\n## 3. K-head Predictor / Gating 机制\n\n### 架构\n- \"A linear layer built on top of the backbone LLM\"\n- 输入: policy LLM 的 hidden states（at state s_t）\n- 输出: distribution over {0, 1, ..., K_max}\n- 轻量级，与 policy 共享 backbone\n\n### K_max 设置\n| Benchmark | K_max |\n|-----------|-------|\n| ALFWorld | 5 |\n| ScienceWorld | 8 |\n| WebShop | 7 |\n| StableToolBench | 3 |\n\n### Gating 分布\n- \"Longer-horizon tasks induce larger lookahead steps\" (Figure 6b)\n- **没有给出 K=0 的具体比例**（即没报告多少 % 的 step 跳过 world model）\n- ALFWorld success rate peak at k=3\n- ScienceWorld 允许更长的 lookahead (K_max=8)\n\n### 训练过程（三阶段）\n1. **Pseudo-Labeling**: K̃_t = argmax_{0≤k≤K_max} [log p_θ0(a*_t | s_t, τ̂^(k)_t) - λ_K · k]\n   - 对每个 step 尝试所有 k 值，选使 policy 最优且 k 最小的\n2. **Warm-Up**: 用 pseudo-labels 联合训练 policy + K-head (SFT)\n3. **Online Optimization**: A2C，reward = r_env - λ_K · K_t - λ_step\n\n---\n\n## 4. 训练成本\n\n### ITP_R 总训练成本 (Qwen3-8B, 2×A100)\n| Stage | Wall-clock | GPU-hours |\n|-------|-----------|-----------|\n| World Model 训练 | 8.69 h | ~17.4 |\n| World Model Rollout 收集 | - | 9.5 |\n| Stage I: Pseudo-Labeling | 6.63 h | 13.27 |\n| Stage II: Warm-Up | 6.38 h | 12.77 |\n| Stage III: Online Optimization | 4.78 h | 9.57 |\n| **ITP_R 三阶段合计** | **17.80 h** | **35.60** |\n| **含 WM 训练总计** | **~26.5 h** | **~62.5** |\n\n### 推理延迟\n- Decision latency p50: 14.2s per step\n- Policy time: 5.1s\n- Imagination time: 7.8s\n- Peak VRAM: 31.0 / 38.4 GB (allocated/reserved)\n\n### 超参数\n- Learning rate (warm-up): 2e-5\n- Learning rate (RL): 5e-6\n- Batch size: 1, gradient accumulation: 16\n- λ_K = 0.2, λ_step = 0.01\n- Discount γ = 0.99, entropy coeff β = 0.01\n\n---\n\n## 5. ScienceWorld 实验结果\n\n### 实验设置\n- 30 subtasks, Train: 1,483 episodes, Test-Seen: 194, Test-Unseen: 151\n- K_max = 8\n- 指标: Success Rate (%), 无 continuous score 报告\n- **没有 per-task type 分数分解**\n\n### Success Rate (%)\n\n| Backbone | Method | Type | Seen | Unseen |\n|----------|--------|------|------|--------|\n| Qwen2.5-7B | CoT | Prompt | 3.09 | 4.63 |\n| | ReAct | Prompt | 8.24 | 9.93 |\n| | RAP | Prompt | 10.30 | 16.55 |\n| | ITP_I | Prompt | 16.49 | 17.88 |\n| | SFT | Train | 55.67 | 49.00 |\n| | WKM | Train | 54.12 | 56.29 |\n| | IWM | Train | 60.82 | 57.61 |\n| | **ITP_R** | **Train** | **62.58** | **58.94** |\n| Qwen3-8B | CoT | Prompt | 2.44 | 1.99 |\n| | ReAct | Prompt | 9.79 | 8.61 |\n| | RAP | Prompt | 15.46 | 27.14 |\n| | ITP_I | Prompt | 20.61 | 19.86 |\n| | SFT | Train | 56.70 | 49.67 |\n| | WKM | Train | 60.31 | 47.68 |\n| | IWM | Train | 59.27 | 54.30 |\n| | **ITP_R** | **Train** | **61.85** | **56.95** |\n| Llama-3.1-8B | CoT | Prompt | 3.09 | 3.31 |\n| | ReAct | Prompt | 9.27 | 13.24 |\n| | RAP | Prompt | 11.34 | 17.21 |\n| | ITP_I | Prompt | 19.58 | 19.20 |\n| | SFT | Train | 57.21 | 50.33 |\n| | WKM | Train | 61.34 | 54.96 |\n| | IWM | Train | 57.56 | 56.29 |\n| | **ITP_R** | **Train** | **63.91** | **57.61** |\n\n### 关键观察\n- ITP_R 在 Seen 上一致最优 (61.85-63.91%)\n- Unseen 上 ITP_R 最优或接近最优 (56.95-58.94%)\n- ITP_R vs SFT: +5~7% (Seen), +7~10% (Unseen)\n- ITP_R vs IWM: +1.8~6.3% (Seen), +1.3~1.3% (Unseen)\n- Prompting 方法远弱于 Training 方法 (3-27% vs 47-64%)\n\n---\n\n## 6. ALFWorld 实验结果\n\n### 实验设置\n- 6 task families: PICK, CLEAN, HEAT, COOL, LOOK, PICK2\n- Train: 3,119, Test: 140\n- K_max = 5\n\n### Success Rate (%) — Qwen3-8B (最强配置)\n\n| Method | PICK | CLEAN | HEAT | COOL | LOOK | PICK2 | Overall |\n|--------|------|-------|------|------|------|-------|---------|\n| CoT | 14.29 | 14.81 | 12.50 | 12.00 | 15.38 | 12.50 | 13.57 |\n| ReAct | 25.71 | 22.22 | 12.50 | 12.00 | 7.69 | 25.00 | 19.29 |\n| RAP | 42.86 | 37.04 | 37.50 | 16.00 | 15.38 | 4.17 | 28.57 |\n| ITP_I | 82.86 | 25.93 | 12.50 | 16.00 | 23.08 | 54.17 | 41.43 |\n| SFT | 71.43 | 70.37 | 68.75 | 72.00 | 69.23 | 70.83 | 70.71 |\n| WKM | 80.00 | 77.78 | 81.25 | 80.00 | 76.92 | 79.17 | 79.29 |\n| IWM | 85.71 | 85.19 | 87.50 | 84.00 | 46.15 | 87.50 | 82.14 |\n| **ITP_R** | **97.14** | **88.88** | **93.75** | **88.00** | **76.92** | **79.17** | **88.57** |\n\n### 关键观察\n- ITP_R overall 88.57% (Qwen3-8B), 远超 IWM 82.14%\n- PICK subtask 最强: 97.14%\n- LOOK subtask 最弱: 76.92% (与 WKM 持平)\n\n---\n\n## 7. WebShop 实验结果\n\n### 实验设置\n- Train: 1,824, Test: 210\n- K_max = 7\n\n### Total Score (%)\n\n| Method | Qwen2.5-7B | Qwen3-8B | Llama-3.1-8B |\n|--------|-----------|----------|--------------|\n| CoT | 5.10 | 6.32 | 8.20 |\n| ReAct | 15.28 | 18.62 | 19.32 |\n| RAP | 11.28 | 12.40 | 16.05 |\n| ITP_I | 20.10 | 25.25 | 24.30 |\n| SFT | 51.60 | 52.30 | 47.30 |\n| WKM | 58.80 | 61.15 | 65.58 |\n| IWM | 56.20 | 57.30 | 58.60 |\n| **ITP_R** | **60.20** | **68.10** | **67.50** |\n\n---\n\n## 8. StableToolBench 实验结果\n\n### Qwen3-8B Only\n\n| Method | SoPR (%) | SoWR (%) |\n|--------|----------|----------|\n| ReAct | 26 | 22 |\n| RAP | 28 | 26 |\n| ITP_I | 35 (+7) | 28 (+2) |\n| SFT | 42 | 36 |\n| IWM | 44 | 36 |\n| **ITP_R** | **68 (+24)** | **54 (+18)** |\n\n---\n\n## 9. 消融实验\n\n### 去掉 Online Reinforced Training (Stage 3)\n| Benchmark | ITP_R | w/o RT | Drop |\n|-----------|-------|--------|------|\n| ALFWorld | 88.57% | 71.42% | -17.15 pp |\n| ScienceWorld | 59.70% | 46.00% | -13.70 pp |\n\n### Compute-Matched 对比\n- ITP_I vs no-WM baseline: +5.01 pp\n- ITP_R vs no-WM baseline: +10.43 pp\n- 结论: \"gains come not from extra compute alone, but from state-conditioned adaptive lookahead\"\n\n### World Model 质量 vs Agent 性能\n- Fact-F1 随 horizon k 增加而单调下降（compounding errors）\n- Agent success rate 在 k=3 左右 peak，然后下降\n- 说明 world model 不准时，更长的 imagination 反而有害\n\n---\n\n## 10. Baselines 说明\n\n| Method | 类型 | 描述 |\n|--------|------|------|\n| CoT | Prompting | Chain-of-Thought |\n| ReAct | Prompting | Reasoning + Acting |\n| RAP | Prompting | Reasoning via Planning (with world model prompting) |\n| ITP_I | Prompting | 本文 inference-only 变体 |\n| SFT | Training | 标准 supervised fine-tuning on expert trajectories |\n| WKM | Training | World Knowledge Model — 训练 parametric world knowledge model 提供 global task priors + local state knowledge |\n| IWM | Training | Implicit World Model — 用 implicit world-modeling objective 增强 imitation learning，让 policy 内化环境动态 |\n| ITP_R | Training | 本文 reinforced 变体 |\n\n---\n\n## 11. 与 SimGate 的关键对比点\n\n### World Model: Learned vs Real Simulator\n- **ITP-R**: Learned LLM-based world model，存在 compounding errors（Fact-F1 随 horizon 下降）\n- **SimGate**: 用真实 ScienceWorld simulator 的 action-replay fork，zero approximation error\n- **关键优势**: SimGate 的 simulator rollout 完全精确，不受 horizon 限制；ITP-R 的 imagination 在 k>3 后质量下降\n- **潜在劣势**: SimGate 需要 simulator 可 fork（不是所有环境都支持），ITP-R 的 learned WM 更通用\n\n### Gating / Routing 机制\n- **ITP-R**: K-head predictor 选择 lookahead 步数 K ∈ {0,...,K_max}，K=0 = 不用 WM\n- **SimGate**: Binary routing — 每步决定是否 fork simulator 做 exploration\n- **异同**: \n  - 都是 per-step adaptive decision\n  - ITP-R 的 K 控制 imagination depth，SimGate 的 routing 控制是否用 simulator\n  - ITP-R 没报告 K=0 的比例，无法直接对比 \"跳过 WM\" 的频率\n  - ITP-R 的 gating 是 soft（选深度），SimGate 是 hard（用/不用）\n\n### 性能参考点 (ScienceWorld)\n- ITP-R best: Seen 63.91%, Unseen 57.61% (Llama-3.1-8B)\n- 注意: ITP-R 只报告了 success rate，没有 continuous score\n- SimGate 需要在相同 split、相同 metric 下对比\n\n### 训练成本\n- ITP-R: ~62.5 GPU-hours (2×A100) 含 WM 训练\n- 推理时每步 14.2s（其中 imagination 占 7.8s）\n- SimGate 的 simulator fork 推理成本取决于 fork 频率和 simulator 速度\n\n### 论文未讨论的点\n- **没有对比 learned WM vs real simulator** — 这是 SimGate 可以贡献的新视角\n- **没有 per-task-type 分析** — SimGate 可以分析哪些 task type 更需要 simulator\n- **没有 continuous score** — 如果 SimGate 报告 continuous score，需注意不可直接对比\nHEREDOC",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "66675aae-e41b-4b36-ac21-f7e545556ae0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016u7DJxAAem5cp6s9S8vP5E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 33315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 314
      },
      "output_tokens": 65,
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

_source line 27 · 2026-05-13T09:12:37.330Z_

<details><summary>↩ Tool result · `toolu_01Y5THMEMc9j9UeYn8BY4wBd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "8f86d7ea-e764-46ca-8cc8-2f9ce7b4cc79",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.76}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

验证文件已写入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "5a627e58-d95c-42f8-a146-e928ceeb5cb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcVw2DLEU4pqExRagrWamC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4933,
      "cache_read_input_tokens": 33629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4933
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

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NdYz1jFuEb1z2XJPKVVTPP`</summary>

```json
{
  "server": "autodl-simgate",
  "command": "wc -l /root/autodl-tmp/simgate-modular-routing/notes/literature_itpr.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "8eed4282-a272-4ac1-b248-3f10931ef2e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcVw2DLEU4pqExRagrWamC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4933,
      "cache_read_input_tokens": 33629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4933
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

_source line 30 · 2026-05-13T09:12:43.711Z_

<details><summary>↩ Tool result · `toolu_01NdYz1jFuEb1z2XJPKVVTPP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"287 /root/autodl-tmp/simgate-modular-routing/notes/literature_itpr.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.03}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "27e97bd9-1bd3-4694-abcc-df840a0adddd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"287 /root/autodl-tmp/simgate-modular-routing/notes/literature_itpr.md\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.03}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"287 /root/autodl-tmp/simgate-modular-routing/notes/literature_itpr.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.03}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

文件已写入 `/root/autodl-tmp/simgate-modular-routing/notes/literature_itpr.md`（287 行）。

关键发现：

**性能**: ITP-R 在 ScienceWorld 上 best success rate 为 Seen 63.91% / Unseen 57.61%（Llama-3.1-8B）。只报告了 success rate，无 continuous score，无 per-task breakdown。

**World Model 核心弱点**: Learned LLM-based WM 存在 compounding errors — Fact-F1 随 horizon 单调下降，agent success 在 k≈3 后也开始下降。这是 SimGate 用真实 simulator 的最大优势切入点：zero approximation error，不受 horizon 限制。

**Gating 机制**: K-head predictor（线性层）预测 K ∈ {0,...,K_max}，控制 imagination 深度。与 SimGate 的 binary routing 不同 — ITP-R 是选"看多远"，SimGate 是选"用不用 simulator"。论文没报告 K=0（跳过 WM）的比例。

**训练成本**: ~62.5 A100 GPU-hours，推理每步 14.2s（imagination 占 7.8s）。

**最关键的对比缺口**: ITP-R 论文完全没有对比 learned WM vs real simulator，这正是 SimGate 的贡献空间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "uuid": "b51e2715-a42e-480e-8baa-b42b09f5e5f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhME5emvTjYuhK93JRYcBh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 38562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 239
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

_source line 32_

文件已写入 `/root/autodl-tmp/simgate-modular-routing/notes/literature_itpr.md`（287 行）。

关键发现：

**性能**: ITP-R 在 ScienceWorld 上 best success rate 为 Seen 63.91% / Unseen 57.61%（Llama-3.1-8B）。只报告了 success rate，无 continuous score，无 per-task breakdown。

**World Model 核心弱点**: Learned LLM-based WM 存在 compounding errors — Fact-F1 随 horizon 单调下降，agent success 在 k≈3 后也开始下降。这是 SimGate 用真实 simulator 的最大优势切入点：zero approximation error，不受 horizon 限制。

**Gating 机制**: K-head predictor（线性层）预测 K ∈ {0,...,K_max}，控制 imagination 深度。与 SimGate 的 binary routing 不同 — ITP-R 是选"看多远"，SimGate 是选"用不用 simulator"。论文没报告 K=0（跳过 WM）的比例。

**训练成本**: ~62.5 A100 GPU-hours，推理每步 14.2s（imagination 占 7.8s）。

**最关键的对比缺口**: ITP-R 论文完全没有对比 learned WM vs real simulator，这正是 SimGate 的贡献空间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 215888,
  "duration_api_ms": 216707,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "72784097-3c32-4fe7-b534-4f989b07c622",
  "total_cost_usd": 0.6493435,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 26960,
    "cache_read_input_tokens": 254249,
    "output_tokens": 7387,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26960,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 409,
        "cache_read_input_tokens": 38562,
        "cache_creation_input_tokens": 239,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 239
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 133854,
      "outputTokens": 7025,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.168979,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 7387,
      "cacheReadInputTokens": 254249,
      "cacheCreationInputTokens": 26960,
      "webSearchRequests": 0,
      "costUSD": 0.4803645000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9a2faf15-9822-47e0-9a3a-df63e0dbf1de"
}
```

</details>

---
