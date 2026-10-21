# write related work

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_write_related-work_20260513T085926.log`
- **Structured JSON:** [`36c14a7ffd76aabcef3e.json`](../../sessions/36/36c14a7ffd76aabcef3e.json)

## Before a recorded user message

27 recorded events

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
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "0973af8c-0cf2-4725-aff8-9e049f793696",
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
    "resetsAt": 1778680200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8bb6eabd-66eb-474e-b206-5008a408deed",
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab"
}
```

---

### Assistant

_source line 4_

I'll start by reading the IDEA_BRIEF and the method section to gather source material.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "621f8a8f-fda9-466f-b0ae-9e81efcfb86d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WoiYk1FuUQn5B4dXH6a9V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12171,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12171
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FDdf6mx3qcTULqADVz3Etw`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "3a30fb1c-92e5-428f-97c7-4796fd1b3ae6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WoiYk1FuUQn5B4dXH6a9V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12171,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12171
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

_source line 6 · 2026-05-13T08:59:41.216Z_

<details><summary>↩ Tool result · `toolu_01FDdf6mx3qcTULqADVz3Etw`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

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
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "6438ae55-a0de-4644-a7ec-b7dab5255216",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
Now let me read the IDEA_BRIEF and the method section in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "2f37a8b1-cdc6-4b86-af8e-702adb9a91b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XexbLCrQvaH5eddpzhE65b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1333,
      "cache_read_input_tokens": 23618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1333
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RzJntUqUsn2KuQ3gMmoqnC`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "ideas.md",
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
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "520a8cab-5b2b-4db5-ba4a-c4308e0b6a15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XexbLCrQvaH5eddpzhE65b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1333,
      "cache_read_input_tokens": 23618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1333
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

_source line 9 · 2026-05-13T08:59:45.349Z_

<details><summary>↩ Tool result · `toolu_01RzJntUqUsn2KuQ3gMmoqnC`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'event-gated-adaptive-horizon'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "e4c7b0cd-875d-4ac2-937c-6896d15dd239",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No ideas.md found for 'event-gated-adaptive-horizon'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'event-gated-adaptive-horizon'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01UB75gSfVxMQHd2F84wYNMK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/method_section_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "7e3b1f0c-ae91-48f6-a720-3889fb2485f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XexbLCrQvaH5eddpzhE65b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1333,
      "cache_read_input_tokens": 23618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1333
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

_source line 11 · 2026-05-13T08:59:45.800Z_

<details><summary>↩ Tool result · `toolu_01UB75gSfVxMQHd2F84wYNMK`</summary>

```text
1	# 3. Method
2	
3	We build on DreamerV3 \citep{hafner2023dreamerv3}, a model-based reinforcement learning agent that learns a world model in a recurrent latent space (RSSM) and optimizes a policy purely through imagined rollouts. Our key contribution is an **event gate** that selects a per-step temporal stride $\Delta t \in \{1, \dots, K\}$, enabling variable-rate imagination. When the latent state changes slowly, the gate skips multiple environment steps in a single model transition; when the state changes rapidly, it falls back to single-step updates. This extends the effective planning horizon without a proportional increase in computation. We describe the five components of our approach below.
4	
5	## 3.1 Variable-Rate RSSM
6	
7	The standard RSSM in DreamerV3 maintains a deterministic recurrent state $h_t$ and a stochastic state $z_t$, updated at every environment step via a GRU cell:
8	
9	$$h_t = \text{GRU}(h_{t-1}, [z_{t-1}; a_{t-1}]).$$
10	
11	We extend this transition to accept a temporal stride $\Delta t \in \{1, \dots, K\}$ that specifies how many environment steps the model traverses in a single recurrence. To inform the GRU of the stride magnitude, we introduce a learned embedding $e: \{1, \dots, K\} \to \mathbb{R}^{d_e}$ via a lookup table $\mathbf{E} \in \mathbb{R}^{K \times d_e}$ (we use $K{=}8$, $d_e{=}32$). The modified transition becomes:
12	
13	$$h_t = \text{GRU}\!\left(h_{t-1},\; [z_{t-1};\; a_{t-1};\; e(\Delta t)]\right).$$
14	
15	The GRU input is first projected through a linear layer followed by LayerNorm and SiLU activation before entering the recurrent cell, which absorbs the scale difference introduced by the additional embedding dimension. The stochastic state $z_t$ is then sampled from a categorical distribution (with uniform mixture) parameterized by an MLP applied to $h_t$, exactly as in DreamerV3.
16	
17	When $\Delta t = 1$, the model reduces to the standard RSSM. The embedding weights are initialized near zero ($\sigma = 0.01$) so that the initial model behavior is nearly identical to vanilla DreamerV3, ensuring stable early training.
18	
19	**Training with variable strides.** To teach the RSSM to predict across different temporal strides, we sub-sample replay trajectories at variable $\Delta t$ during training (Section 3.4). Each sub-sampled trajectory carries per-step $\Delta t$ labels that are passed through the observation loop to the GRU, allowing the model to learn stride-conditioned dynamics.
20	
21	## 3.2 Event Gate
22	
23	The event gate is a lightweight MLP that examines the current latent state and decides the temporal stride for the next imagination step.
24	
25	**Architecture.** The gate takes as input the feature vector $f_t = [z_t; h_t] \in \mathbb{R}^{d_f}$ (where $d_f = d_z \cdot C + d_h$; for DreamerV3's default configuration, $d_f = 32 \times 32 + 512 = 1536$). It consists of two hidden layers of 256 units each, with LayerNorm and SiLU activations, followed by a linear projection to $K$ logits:
26	
27	$$\ell_t = W_2\,\text{SiLU}\!\left(\text{LN}(W_1\,f_t)\right) \in \mathbb{R}^K.$$
28	
29	The output distribution over strides is obtained via Gumbel-Softmax:
30	
31	$$\Delta t \sim \text{Gumbel-Softmax}(\ell_t, \tau),$$
32	
33	which provides differentiable sampling during training while producing hard (argmax) decisions during imagination. The temperature $\tau$ is linearly annealed from $\tau_0 = 5.0$ to $\tau_{\min} = 0.5$ over 200K training steps, transitioning from near-uniform exploration to confident stride selection.
34	
35	**Latent-state delta supervision.** Rather than relying solely on task reward to shape the gate, we provide a direct supervision signal derived from the rate of change in latent space. Let $\delta_t = \|f_t - f_{t-1}\|_2$ be the L2 distance between consecutive feature vectors (with stop-gradient on both $f_t$ and $f_{t-1}$). We normalize $\delta_t$ to $[0, 1]$ within each batch via min-max scaling and compute a preferred stride:
36	
37	$$\Delta t^* = 1 + (K - 1)(1 - \bar{\delta}_t),$$
38	
39	where $\bar{\delta}_t$ is the normalized delta. Large state changes ($\bar{\delta}_t \to 1$) yield $\Delta t^* \to 1$ (fine resolution); small changes ($\bar{\delta}_t \to 0$) yield $\Delta t^* \to K$ (skip ahead). The supervision target is a soft categorical distribution formed by a Gaussian kernel centered at $\Delta t^*$:
40	
41	$$q_t(k) \propto \exp\!\left(-\frac{(k - \Delta t^*)^2}{2\sigma^2}\right), \quad k = 1, \dots, K,$$
42	
43	with $\sigma = 1.0$. The gate supervision loss is the cross-entropy between the gate's predicted distribution and this soft target:
44	
45	$$\mathcal{L}_{\text{gate}} = -\sum_{k=1}^{K} q_t(k) \log p_{\theta}(k \mid f_t),$$
46	
47	where $p_{\theta}(k \mid f_t) = \text{softmax}(\ell_t)_k$. Crucially, the gate loss does not backpropagate into the RSSM: the input features are detached, so the gate learns to *read* the latent dynamics rather than *shape* them.
48	
49	## 3.3 Adapted $\lambda$-Returns
50	
51	DreamerV3 computes $\lambda$-returns over imagined trajectories with a fixed per-step discount $\gamma$. With variable-rate imagination, each step spans $\Delta t$ environment steps, requiring adaptations to both the reward aggregation and the discount factor.
52	
53	**Cumulative discounted reward.** When sub-sampling a replay trajectory at stride $\Delta t$, we pre-compute the cumulative discounted reward for each gap:
54	
55	$$r_t^{\text{cum}} = \sum_{k=0}^{\Delta t - 1} \gamma^k\, r_{t+k}.$$
56	
57	The reward head is trained to predict $r_t^{\text{cum}}$ directly (the sub-sampled training data replaces per-step rewards with their cumulative-discounted aggregates), so no approximation is needed at imagination time.
58	
59	**Minimum continuation.** For the continuation signal across a gap, we take the conservative estimate:
60	
61	$$c_t^{\min} = \min_{k=0,\dots,\Delta t - 1} c_{t+k},$$
62	
63	so that if any frame within the gap is terminal, the entire interval is marked as terminal.
64	
65	**Variable-stride $\lambda$-return.** The adapted $\lambda$-return replaces the fixed discount $\gamma$ with $\gamma^{\Delta t}$:
66	
67	$$V_t^{\lambda} = r_t^{\text{cum}} + \gamma^{\Delta t}\!\left[(1 - \lambda)\,V(s_{t+\Delta t}) + \lambda\, V_{t+\Delta t}^{\lambda}\right],$$
68	
69	with the recursion terminating at the bootstrap value $V(s_H)$. This is computed via the same backward scan as the standard $\lambda$-return, but with per-step adjusted discount $(\gamma \cdot c_t)^{\Delta t}$ in place of $\gamma \cdot c_t$. When $\Delta t = 1$ for all steps, this expression reduces exactly to the standard DreamerV3 $\lambda$-return.
70	
71	**Importance weights.** The per-step weights used for the actor and value losses are similarly adjusted:
72	
73	$$w_t = \prod_{i=0}^{t-1} (\gamma \cdot c_i)^{\Delta t_i},$$
74	
75	so that steps further in effective time receive appropriately decayed weight.
76	
77	## 3.4 Gate Collapse Prevention
78	
79	A central failure mode is *gate collapse*, where the gate converges to a constant stride (typically $\Delta t = 1$ or $\Delta t = K$), eliminating the adaptive benefit. We employ three complementary countermeasures.
80	
81	**Entropy regularization.** We add an entropy bonus to the gate loss:
82	
83	$$\mathcal{L}_{\text{total}} = \lambda_g\,\mathcal{L}_{\text{gate}} - \lambda_H\,\mathcal{H}[p_\theta(\cdot \mid f_t)],$$
84	
85	where $\mathcal{H}$ is the categorical entropy of the gate distribution and $\lambda_H$ is annealed from 0.1 to 0.01 over 200K steps. The high initial $\lambda_H$ prevents the gate from committing to a narrow $\Delta t$ range before the RSSM has learned good multi-stride dynamics.
86	
87	**Three-phase curriculum.** We introduce the gate gradually:
88	
89	| Phase | Steps | Behavior |
90	|-------|-------|----------|
91	| 1 | $0$--$50\text{K}$ | Gate frozen ($\Delta t \equiv 1$); gate loss weight $= 0$ |
92	| 2 | $50\text{K}$--$150\text{K}$ | Gate loss linearly ramped from 0 to 1; gate active in imagination |
93	| 3 | $> 150\text{K}$ | Full gating; gate scale $= 1.0$ |
94	
95	Phase 1 allows the RSSM to first learn stable single-step dynamics identical to standard DreamerV3. Phase 2 gradually introduces multi-stride predictions, giving the RSSM time to adapt. Phase 3 permits unconstrained gate optimization.
96	
97	Formally, the gate scale factor is:
98	
99	$$\alpha(s) = \begin{cases} 0 & s < s_1 \\ (s - s_1) / (s_2 - s_1) & s_1 \leq s < s_2 \\ 1 & s \geq s_2 \end{cases}$$
100	
101	where $s$ is the training step, $s_1 = 50\text{K}$, and $s_2 = 150\text{K}$.
102	
103	**Synchronized sub-sampling curriculum.** A naive implementation applies full variable-$\Delta t$ sub-sampling from step 0, forcing the RSSM to train on multi-stride data while imagination only uses $\Delta t = 1$ during Phase 1. This train--imagination mismatch degrades performance. We resolve it by tying the sub-sampling range to the curriculum schedule:
104	
105	$$\Delta t_{\max}^{\text{eff}} = 1 + \alpha(s) \cdot (K - 1).$$
106	
107	During Phase 1, $\Delta t_{\max}^{\text{eff}} = 1$ and the training data is identical to vanilla DreamerV3 (no sub-sampling). During Phase 2, the maximum stride ramps linearly from 1 to $K$, synchronizing the distribution of $\Delta t$ in training data with the gate's expanding range in imagination. During Phase 3, the full log-uniform distribution over $\{1, \dots, K\}$ is used.
108	
109	## 3.5 Comparison with Related Approaches
110	
111	Our method occupies a distinct point in the design space of temporal abstraction for model-based RL. We highlight the key differences with the most closely related approaches.
112	
113	**THICK** \citep{romac2024thick} decomposes planning into a hierarchy of coarse sub-goals and fine-grained actions, with a fixed sub-goal horizon. In contrast, our approach operates within a single-level RSSM and learns a *per-step* temporal stride, avoiding the complexity of hierarchical world models while still achieving variable temporal resolution.
114	
115	**TAWM** \citep{freed2024tawm} introduces time-aware world models that condition on a fixed or scheduled $\Delta t$ to predict future states. Our event gate makes $\Delta t$ *state-dependent*---the stride is chosen dynamically based on the current latent state rather than being fixed or globally scheduled, enabling the model to allocate temporal resolution where it is most needed within a single trajectory.
116	
117	**ASI** \citep{neitz2018adaptive} learns to skip timesteps by min-pooling over reconstruction losses, selecting intervals that are *easiest to predict*. It operates on raw observation prediction without integration into a model-based RL loop. In contrast, our gate optimizes for *dynamical significance* via latent-state deltas rather than prediction ease, and is fully integrated into the RSSM imagination pipeline for policy optimization.
118	
119	**LS-Imagine** \citep{li2025lsimagine} learns jumping flags based on affordance-map kurtosis for open-world exploration in MineDojo, with action-independent jumps that skip over low-information states. Our gate differs in two key ways: it operates within the actor-critic MBRL imagination loop with policy-dependent variable-rate stepping, rather than exploration-oriented action-independent jumps; and it selects strides based on latent-state dynamics rather than observation-space affordance maps.
120	
121	**DyMoDreamer** \citep{dymodreamer2025} uses inter-frame differencing masks with stochastic categorical dynamic modulation to focus RSSM attention on motion-relevant features. It operates at the observation/pixel level to improve per-step representation quality. Our method operates in latent space and changes the *temporal resolution* of imagination rather than the attention quality of individual steps, achieving complementary benefits within a single RSSM architecture.
122	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "005db935-699c-453a-bcab-b5fba4df918c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/method_section_draft.md",
      "content": "# 3. Method\n\nWe build on DreamerV3 \\citep{hafner2023dreamerv3}, a model-based reinforcement learning agent that learns a world model in a recurrent latent space (RSSM) and optimizes a policy purely through imagined rollouts. Our key contribution is an **event gate** that selects a per-step temporal stride $\\Delta t \\in \\{1, \\dots, K\\}$, enabling variable-rate imagination. When the latent state changes slowly, the gate skips multiple environment steps in a single model transition; when the state changes rapidly, it falls back to single-step updates. This extends the effective planning horizon without a proportional increase in computation. We describe the five components of our approach below.\n\n## 3.1 Variable-Rate RSSM\n\nThe standard RSSM in DreamerV3 maintains a deterministic recurrent state $h_t$ and a stochastic state $z_t$, updated at every environment step via a GRU cell:\n\n$$h_t = \\text{GRU}(h_{t-1}, [z_{t-1}; a_{t-1}]).$$\n\nWe extend this transition to accept a temporal stride $\\Delta t \\in \\{1, \\dots, K\\}$ that specifies how many environment steps the model traverses in a single recurrence. To inform the GRU of the stride magnitude, we introduce a learned embedding $e: \\{1, \\dots, K\\} \\to \\mathbb{R}^{d_e}$ via a lookup table $\\mathbf{E} \\in \\mathbb{R}^{K \\times d_e}$ (we use $K{=}8$, $d_e{=}32$). The modified transition becomes:\n\n$$h_t = \\text{GRU}\\!\\left(h_{t-1},\\; [z_{t-1};\\; a_{t-1};\\; e(\\Delta t)]\\right).$$\n\nThe GRU input is first projected through a linear layer followed by LayerNorm and SiLU activation before entering the recurrent cell, which absorbs the scale difference introduced by the additional embedding dimension. The stochastic state $z_t$ is then sampled from a categorical distribution (with uniform mixture) parameterized by an MLP applied to $h_t$, exactly as in DreamerV3.\n\nWhen $\\Delta t = 1$, the model reduces to the standard RSSM. The embedding weights are initialized near zero ($\\sigma = 0.01$) so that the initial model behavior is nearly identical to vanilla DreamerV3, ensuring stable early training.\n\n**Training with variable strides.** To teach the RSSM to predict across different temporal strides, we sub-sample replay trajectories at variable $\\Delta t$ during training (Section 3.4). Each sub-sampled trajectory carries per-step $\\Delta t$ labels that are passed through the observation loop to the GRU, allowing the model to learn stride-conditioned dynamics.\n\n## 3.2 Event Gate\n\nThe event gate is a lightweight MLP that examines the current latent state and decides the temporal stride for the next imagination step.\n\n**Architecture.** The gate takes as input the feature vector $f_t = [z_t; h_t] \\in \\mathbb{R}^{d_f}$ (where $d_f = d_z \\cdot C + d_h$; for DreamerV3's default configuration, $d_f = 32 \\times 32 + 512 = 1536$). It consists of two hidden layers of 256 units each, with LayerNorm and SiLU activations, followed by a linear projection to $K$ logits:\n\n$$\\ell_t = W_2\\,\\text{SiLU}\\!\\left(\\text{LN}(W_1\\,f_t)\\right) \\in \\mathbb{R}^K.$$\n\nThe output distribution over strides is obtained via Gumbel-Softmax:\n\n$$\\Delta t \\sim \\text{Gumbel-Softmax}(\\ell_t, \\tau),$$\n\nwhich provides differentiable sampling during training while producing hard (argmax) decisions during imagination. The temperature $\\tau$ is linearly annealed from $\\tau_0 = 5.0$ to $\\tau_{\\min} = 0.5$ over 200K training steps, transitioning from near-uniform exploration to confident stride selection.\n\n**Latent-state delta supervision.** Rather than relying solely on task reward to shape the gate, we provide a direct supervision signal derived from the rate of change in latent space. Let $\\delta_t = \\|f_t - f_{t-1}\\|_2$ be the L2 distance between consecutive feature vectors (with stop-gradient on both $f_t$ and $f_{t-1}$). We normalize $\\delta_t$ to $[0, 1]$ within each batch via min-max scaling and compute a preferred stride:\n\n$$\\Delta t^* = 1 + (K - 1)(1 - \\bar{\\delta}_t),$$\n\nwhere $\\bar{\\delta}_t$ is the normalized delta. Large state changes ($\\bar{\\delta}_t \\to 1$) yield $\\Delta t^* \\to 1$ (fine resolution); small changes ($\\bar{\\delta}_t \\to 0$) yield $\\Delta t^* \\to K$ (skip ahead). The supervision target is a soft categorical distribution formed by a Gaussian kernel centered at $\\Delta t^*$:\n\n$$q_t(k) \\propto \\exp\\!\\left(-\\frac{(k - \\Delta t^*)^2}{2\\sigma^2}\\right), \\quad k = 1, \\dots, K,$$\n\nwith $\\sigma = 1.0$. The gate supervision loss is the cross-entropy between the gate's predicted distribution and this soft target:\n\n$$\\mathcal{L}_{\\text{gate}} = -\\sum_{k=1}^{K} q_t(k) \\log p_{\\theta}(k \\mid f_t),$$\n\nwhere $p_{\\theta}(k \\mid f_t) = \\text{softmax}(\\ell_t)_k$. Crucially, the gate loss does not backpropagate into the RSSM: the input features are detached, so the gate learns to *read* the latent dynamics rather than *shape* them.\n\n## 3.3 Adapted $\\lambda$-Returns\n\nDreamerV3 computes $\\lambda$-returns over imagined trajectories with a fixed per-step discount $\\gamma$. With variable-rate imagination, each step spans $\\Delta t$ environment steps, requiring adaptations to both the reward aggregation and the discount factor.\n\n**Cumulative discounted reward.** When sub-sampling a replay trajectory at stride $\\Delta t$, we pre-compute the cumulative discounted reward for each gap:\n\n$$r_t^{\\text{cum}} = \\sum_{k=0}^{\\Delta t - 1} \\gamma^k\\, r_{t+k}.$$\n\nThe reward head is trained to predict $r_t^{\\text{cum}}$ directly (the sub-sampled training data replaces per-step rewards with their cumulative-discounted aggregates), so no approximation is needed at imagination time.\n\n**Minimum continuation.** For the continuation signal across a gap, we take the conservative estimate:\n\n$$c_t^{\\min} = \\min_{k=0,\\dots,\\Delta t - 1} c_{t+k},$$\n\nso that if any frame within the gap is terminal, the entire interval is marked as terminal.\n\n**Variable-stride $\\lambda$-return.** The adapted $\\lambda$-return replaces the fixed discount $\\gamma$ with $\\gamma^{\\Delta t}$:\n\n$$V_t^{\\lambda} = r_t^{\\text{cum}} + \\gamma^{\\Delta t}\\!\\left[(1 - \\lambda)\\,V(s_{t+\\Delta t}) + \\lambda\\, V_{t+\\Delta t}^{\\lambda}\\right],$$\n\nwith the recursion terminating at the bootstrap value $V(s_H)$. This is computed via the same backward scan as the standard $\\lambda$-return, but with per-step adjusted discount $(\\gamma \\cdot c_t)^{\\Delta t}$ in place of $\\gamma \\cdot c_t$. When $\\Delta t = 1$ for all steps, this expression reduces exactly to the standard DreamerV3 $\\lambda$-return.\n\n**Importance weights.** The per-step weights used for the actor and value losses are similarly adjusted:\n\n$$w_t = \\prod_{i=0}^{t-1} (\\gamma \\cdot c_i)^{\\Delta t_i},$$\n\nso that steps further in effective time receive appropriately decayed weight.\n\n## 3.4 Gate Collapse Prevention\n\nA central failure mode is *gate collapse*, where the gate converges to a constant stride (typically $\\Delta t = 1$ or $\\Delta t = K$), eliminating the adaptive benefit. We employ three complementary countermeasures.\n\n**Entropy regularization.** We add an entropy bonus to the gate loss:\n\n$$\\mathcal{L}_{\\text{total}} = \\lambda_g\\,\\mathcal{L}_{\\text{gate}} - \\lambda_H\\,\\mathcal{H}[p_\\theta(\\cdot \\mid f_t)],$$\n\nwhere $\\mathcal{H}$ is the categorical entropy of the gate distribution and $\\lambda_H$ is annealed from 0.1 to 0.01 over 200K steps. The high initial $\\lambda_H$ prevents the gate from committing to a narrow $\\Delta t$ range before the RSSM has learned good multi-stride dynamics.\n\n**Three-phase curriculum.** We introduce the gate gradually:\n\n| Phase | Steps | Behavior |\n|-------|-------|----------|\n| 1 | $0$--$50\\text{K}$ | Gate frozen ($\\Delta t \\equiv 1$); gate loss weight $= 0$ |\n| 2 | $50\\text{K}$--$150\\text{K}$ | Gate loss linearly ramped from 0 to 1; gate active in imagination |\n| 3 | $> 150\\text{K}$ | Full gating; gate scale $= 1.0$ |\n\nPhase 1 allows the RSSM to first learn stable single-step dynamics identical to standard DreamerV3. Phase 2 gradually introduces multi-stride predictions, giving the RSSM time to adapt. Phase 3 permits unconstrained gate optimization.\n\nFormally, the gate scale factor is:\n\n$$\\alpha(s) = \\begin{cases} 0 & s < s_1 \\\\ (s - s_1) / (s_2 - s_1) & s_1 \\leq s < s_2 \\\\ 1 & s \\geq s_2 \\end{cases}$$\n\nwhere $s$ is the training step, $s_1 = 50\\text{K}$, and $s_2 = 150\\text{K}$.\n\n**Synchronized sub-sampling curriculum.** A naive implementation applies full variable-$\\Delta t$ sub-sampling from step 0, forcing the RSSM to train on multi-stride data while imagination only uses $\\Delta t = 1$ during Phase 1. This train--imagination mismatch degrades performance. We resolve it by tying the sub-sampling range to the curriculum schedule:\n\n$$\\Delta t_{\\max}^{\\text{eff}} = 1 + \\alpha(s) \\cdot (K - 1).$$\n\nDuring Phase 1, $\\Delta t_{\\max}^{\\text{eff}} = 1$ and the training data is identical to vanilla DreamerV3 (no sub-sampling). During Phase 2, the maximum stride ramps linearly from 1 to $K$, synchronizing the distribution of $\\Delta t$ in training data with the gate's expanding range in imagination. During Phase 3, the full log-uniform distribution over $\\{1, \\dots, K\\}$ is used.\n\n## 3.5 Comparison with Related Approaches\n\nOur method occupies a distinct point in the design space of temporal abstraction for model-based RL. We highlight the key differences with the most closely related approaches.\n\n**THICK** \\citep{romac2024thick} decomposes planning into a hierarchy of coarse sub-goals and fine-grained actions, with a fixed sub-goal horizon. In contrast, our approach operates within a single-level RSSM and learns a *per-step* temporal stride, avoiding the complexity of hierarchical world models while still achieving variable temporal resolution.\n\n**TAWM** \\citep{freed2024tawm} introduces time-aware world models that condition on a fixed or scheduled $\\Delta t$ to predict future states. Our event gate makes $\\Delta t$ *state-dependent*---the stride is chosen dynamically based on the current latent state rather than being fixed or globally scheduled, enabling the model to allocate temporal resolution where it is most needed within a single trajectory.\n\n**ASI** \\citep{neitz2018adaptive} learns to skip timesteps by min-pooling over reconstruction losses, selecting intervals that are *easiest to predict*. It operates on raw observation prediction without integration into a model-based RL loop. In contrast, our gate optimizes for *dynamical significance* via latent-state deltas rather than prediction ease, and is fully integrated into the RSSM imagination pipeline for policy optimization.\n\n**LS-Imagine** \\citep{li2025lsimagine} learns jumping flags based on affordance-map kurtosis for open-world exploration in MineDojo, with action-independent jumps that skip over low-information states. Our gate differs in two key ways: it operates within the actor-critic MBRL imagination loop with policy-dependent variable-rate stepping, rather than exploration-oriented action-independent jumps; and it selects strides based on latent-state dynamics rather than observation-space affordance maps.\n\n**DyMoDreamer** \\citep{dymodreamer2025} uses inter-frame differencing masks with stochastic categorical dynamic modulation to focus RSSM attention on motion-relevant features. It operates at the observation/pixel level to improve per-step representation quality. Our method operates in latent space and changes the *temporal resolution* of imagination rather than the attention quality of individual steps, achieving complementary benefits within a single RSSM architecture.\n",
      "numLines": 122,
      "startLine": 1,
      "totalLines": 122
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The ideas.md file doesn't exist. Let me check what files are available in the project to find the IDEA_BRIEF or equivalent document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "c1db45b6-782a-4338-b9fe-60f2a566b820",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1xkRWizmvNgCypsz2QCz2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4084,
      "cache_read_input_tokens": 24951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4084
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

_source line 13_

ideas.md 不存在，让我查找项目中可用的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "0d2e1b22-8d5e-46ec-a308-28c96363db1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1xkRWizmvNgCypsz2QCz2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4084,
      "cache_read_input_tokens": 24951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4084
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

<details open><summary>🔧 Tool call — Glob · `toolu_019wx6wbMcfJM29jffRZsF5w`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "4d5b5275-7eed-4da9-a078-07244390c0ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1xkRWizmvNgCypsz2QCz2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4084,
      "cache_read_input_tokens": 24951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4084
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

_source line 15 · 2026-05-13T08:59:50.657Z_

<details><summary>↩ Tool result · `toolu_019wx6wbMcfJM29jffRZsF5w`</summary>

```text
docs/IDEA_BRIEF.md
artifacts/_project/report/code_survey_dreamerv3.md
artifacts/code_survey_dreamerv3.md
artifacts/_project/report/implementation_design.md
artifacts/implementation_design.md
artifacts/_project/intermediate/CHANGES.md
artifacts/code/CHANGES.md
artifacts/exp_001_baseline/data/exp_001_baseline.md
artifacts/exp_002_event_gated/data/exp_002_event_gated.md
memory.md
ROADMAP.md
artifacts/method_section_draft.md
report.md
.claude/sessions/agent_900dba7c/CLAUDE.md
.claude/sessions/agent_900dba7c/AGENTS.md
.claude/sessions/director_e639d768/CLAUDE.md
.claude/sessions/director_e639d768/AGENTS.md
.claude/sessions/agent_32c09c1e/CLAUDE.md
.claude/sessions/agent_32c09c1e/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/reviewer_9760d156/CLAUDE.md
.claude/sessions/reviewer_9760d156/AGENTS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "98afd877-51c1-4a9c-933f-ea5adaa97aa4",
  "tool_use_result": {
    "filenames": [
      "docs/IDEA_BRIEF.md",
      "artifacts/_project/report/code_survey_dreamerv3.md",
      "artifacts/code_survey_dreamerv3.md",
      "artifacts/_project/report/implementation_design.md",
      "artifacts/implementation_design.md",
      "artifacts/_project/intermediate/CHANGES.md",
      "artifacts/code/CHANGES.md",
      "artifacts/exp_001_baseline/data/exp_001_baseline.md",
      "artifacts/exp_002_event_gated/data/exp_002_event_gated.md",
      "memory.md",
      "ROADMAP.md",
      "artifacts/method_section_draft.md",
      "report.md",
      ".claude/sessions/agent_900dba7c/CLAUDE.md",
      ".claude/sessions/agent_900dba7c/AGENTS.md",
      ".claude/sessions/director_e639d768/CLAUDE.md",
      ".claude/sessions/director_e639d768/AGENTS.md",
      ".claude/sessions/agent_32c09c1e/CLAUDE.md",
      ".claude/sessions/agent_32c09c1e/AGENTS.md",
      ".claude/CLAUDE.md",
      "AGENTS.md",
      ".claude/sessions/reviewer_9760d156/CLAUDE.md",
      ".claude/sessions/reviewer_9760d156/AGENTS.md"
    ],
    "durationMs": 12,
    "numFiles": 23,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Glob · `toolu_01NDAjP1FgMcCWowY3a3KXkK`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "9d70518e-a54a-4f53-b6e2-8f510318f137",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1xkRWizmvNgCypsz2QCz2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4084,
      "cache_read_input_tokens": 24951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4084
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

_source line 17 · 2026-05-13T08:59:51.230Z_

<details><summary>↩ Tool result · `toolu_01NDAjP1FgMcCWowY3a3KXkK`</summary>

```text
artifacts/code/configs.yaml
artifacts/manifest.yaml
decisions.yaml
registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "b8ba5146-2f11-4565-a083-77e70bb782b8",
  "tool_use_result": {
    "filenames": [
      "artifacts/code/configs.yaml",
      "artifacts/manifest.yaml",
      "decisions.yaml",
      "registry.yaml"
    ],
    "durationMs": 11,
    "numFiles": 4,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_011Ua6AY7xhSew6BnwFnwyr3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "1b1822e1-8a96-4b31-b377-11e1dc7d473c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzHDfcsgF1Jg55eqg5pXmL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 29035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 633
      },
      "output_tokens": 69,
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

_source line 19 · 2026-05-13T08:59:54.706Z_

<details><summary>↩ Tool result · `toolu_011Ua6AY7xhSew6BnwFnwyr3`</summary>

```text
1	# Idea Brief: Event-Gated Adaptive-Horizon Latent World Model
2	
3	
4	- **Idea ID**: `idea_006`
5	- **Created**: 2026-05-10
6	- **Source**: web_research
7	- **Level**: top-tier
8	- **Target Venues**: CoRL 2026 (abstract: May 26, paper: May 29 — tight but feasible with ManiSkill3 integration as primary risk; may submit with 2 tasks + preliminary ablations if StackPyramid integration delayed), NeurIPS 2026 Workshops (~Aug-Sep 2026, ideal for preliminary results on 2-3 tasks), ICLR 2027 (expected ~Sep-Oct 2026, primary target for full paper with complete ablations, DMC+ManiSkill3 results, and analysis), TMLR (rolling, fallback)
9	
10	## Seed Topic
11	
12	Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).
13	
14	Direction: World models for robot learning — predictive models of environment dynamics that support planning, imagination-based RL, or representation learning. In-scope: latent dynamics models (RSSM-family, JEPA-style), pixel-space video WMs adapted to robotics, semantic-aware WMs, mask/feature WMs, hierarchical WMs.
15	
16	Recent landscape (do not duplicate): DreamerV3, V-JEPA-2, NVIDIA Cosmos, GAIA-style driving WMs, OASIS, Genie-2, TC-IDM, CoWVLA, EA-WM, Mask World Model, DreamVLA. Avoid pure DreamerV3 reimplementations.
17	
18	Contribution type: METHOD ONLY. Either (a) a new WM architecture, (b) a new training objective, or (c) a new way to use WM predictions for downstream control. Pure WM analysis without method is out of scope.
19	
20	SIM-ONLY MITIGATION: WM training and evaluation in sim is standard at CoRL — pure-sim WM papers are routinely accepted when method is novel. Frame as algorithmic contribution.
21	
22	HARD CONSTRAINTS:
23	1. Compute: ≤200 H100-hours total. Rules out training a Cosmos-scale video WM from scratch. Use: small latent WMs trained from scratch, OR fine-tune an open WM (Cosmos releases, V-JEPA, OASIS), OR distill a large WM into a small one.
24	2. Time: ≤20 days. Build on: dreamerv3 codebase, JEPA reference impls, HF Diffusers, NVIDIA Cosmos repo if released.
25	3. Eval: ManiSkill (open-loop video prediction quality + downstream policy), LIBERO (planning quality), Isaac Lab (RL with imagined rollouts), RoboCasa, RoboTwin. Compare against MBRL and model-free RL baselines on identical tasks.
26	
27	Look for: efficient latent dynamics with task-relevant abstraction, structured WMs that decouple agent vs environment dynamics, semantic bottlenecks that prioritize decision-relevant features over photometric realism, hierarchical/multi-scale temporal WMs. Avoid: vanilla pixel reconstruction WMs, generic Dreamer ablations.
28	
29	Tag: direction=world_model, contribution_type=method. target_venues=["CoRL 2026"].
30	
31	## Generation Journey
32	
33	1. **Start** — 开始生成，seed: 'Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: World models for robot learning — predictive models of environment dynamics that support planning, imagination-based RL, or representation learning. In-scope: latent dynamics models (RSSM-family, JEPA-style), pixel-space video WMs adapted to robotics, semantic-aware WMs, mask/feature WMs, hierarchical WMs.\n\nRecent landscape (do not duplicate): DreamerV3, V-JEPA-2, NVIDIA Cosmos, GAIA-style driving WMs, OASIS, Genie-2, TC-IDM, CoWVLA, EA-WM, Mask World Model, DreamVLA. Avoid pure DreamerV3 reimplementations.\n\nContribution type: METHOD ONLY. Either (a) a new WM architecture, (b) a new training objective, or (c) a new way to use WM predictions for downstream control. Pure WM analysis without method is out of scope.\n\nSIM-ONLY MITIGATION: WM training and evaluation in sim is standard at CoRL — pure-sim WM papers are routinely accepted when method is novel. Frame as algorithmic contribution.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Rules out training a Cosmos-scale video WM from scratch. Use: small latent WMs trained from scratch, OR fine-tune an open WM (Cosmos releases, V-JEPA, OASIS), OR distill a large WM into a small one.\n2. Time: ≤20 days. Build on: dreamerv3 codebase, JEPA reference impls, HF Diffusers, NVIDIA Cosmos repo if released.\n3. Eval: ManiSkill (open-loop video prediction quality + downstream policy), LIBERO (planning quality), Isaac Lab (RL with imagined rollouts), RoboCasa, RoboTwin. Compare against MBRL and model-free RL baselines on identical tasks.\n\nLook for: efficient latent dynamics with task-relevant abstraction, structured WMs that decouple agent vs environment dynamics, semantic bottlenecks that prioritize decision-relevant features over photometric realism, hierarchical/multi-scale temporal WMs. Avoid: vanilla pixel reconstruction WMs, generic Dreamer ablations.\n\nTag: direction=world_model, contribution_type=method. target_venues=["CoRL 2026"].'
34	2. **Problem Discovery** (679s) — 发现 4 个研究方向
35	   - Event-Gated Adaptive-Horizon Latent World Model
36	   - Interaction-Graph JEPA for Object-Centric World Modeling
37	   - Multi-Scale Self-Consistency Training for Latent Dynamics
38	   - Action-Effect Decomposed World Model with Passive Pre-Training
39	3. **Method Synthesis** (592s) — 完成: "Event-Gated Adaptive-Horizon Latent World Model" [solid] → CoRL 2026 (abstract deadline: May 26, paper deadline: May 29 — tight but feasible for workshop-length submission or if codebase is near-ready), NeurIPS 2026 Workshops (workshop paper deadline ~Aug-Sep 2026, ideal for preliminary results), ICLR 2027 (expected deadline ~Sep-Oct 2026, primary target for full paper), TMLR (rolling deadline, always open — fallback for thorough journal-length treatment)
40	3. **Method Synthesis** (365s) — 完成: "Interaction-Graph JEPA for Object-Centric World Modeling" [solid] → CoRL 2026 (deadline May 28, 2026), ICLR 2027 (expected deadline ~September 2026), AAAI 2027 (expected deadline ~August 2026)
41	3. **Method Synthesis** (361s) — 完成: "Multi-Scale Self-Consistency Training for Latent Dynamics" [top-tier] → CoRL 2026 (paper deadline: May 29, 2026), AAAI 2027 (paper deadline: ~August 1, 2026), ICLR 2027 (expected deadline: ~October 2026)
42	3. **Method Synthesis** (625s) — 完成: "Action-Effect Decomposed World Model with Passive Pre-Training" [top-tier] → CoRL 2026 (abstract May 26, paper May 28, 2026 — ideal robotics+learning venue), ICLR 2027 (expected ~Sep/Oct 2026 deadline — broader ML audience), ICRA 2027 (expected ~Sep 2026 deadline — robotics audience)
43	
44	## Core Problem
45	
46	Latent world models for manipulation predict at fixed temporal resolution during imagination, creating a credit assignment bottleneck for long-horizon tasks. In DreamerV3, actor-critic training uses imagination rollouts of H=15 latent steps, each covering one environment timestep — so for a 250-step manipulation episode (e.g., ManiSkill3 StackPyramid), imagination covers only 6% of the episode per rollout. Uneventful intervals (free-space approach, transport) consume the same prediction budget as critical state transitions (contacts, grasps, mode changes), simultaneously wasting imagination compute on uninformative phases and starving late-episode events of credit signal. The problem is most pronounced in contact-rich manipulation with distinct task phases (approach → grasp → lift → transport → place → release), but affects any task where dynamics complexity varies over time. Current solutions are either externally specified (TAWM takes Δt as input), structurally fixed (THICK and HWM use two-level hierarchies), domain-specific (LS-Imagine uses affordance-based jumping for open-world exploration), operate at the execution level rather than imagination (FFDC-WAM), or address prediction quality rather than temporal resolution (DMWM uses logical reasoning, DyMoDreamer uses observation-level dynamic modulation). No existing latent world model learns continuous event-driven temporal resolution to extend imagination horizons for actor-critic policy optimization.
47	
48	## Opportunity / Why Now
49	
50	The design point of combining learned event detection with variable-rate latent imagination in a single RSSM-based model for actor-critic training remains open. By learning to skip uneventful timesteps during imagination, the effective horizon extends far beyond H environment steps while keeping latent computation at H steps — directly improving credit assignment for long-horizon tasks. THICK (ICLR 2024) learns temporal abstractions via discrete latent dynamics but uses a fixed two-level hierarchy that cannot express continuous degrees of event significance or variable skip lengths. TAWM (ICML 2025) enables variable-Δt integration but requires Δt to be externally specified and is built on TD-MPC2's short-horizon MPC (H=3–5 with MPPI planning), where temporal skipping during planning is counterproductive. HWM (Zhang et al., April 2026) learns multi-scale latent world models but uses a fixed two-level planner. LS-Imagine (ICLR 2025 Oral) learns jumping flags for long-horizon imagination but targets open-world exploration with action-independent jumps, not actor-critic policy optimization. Adaptive Skip Intervals (Neitz et al., NeurIPS 2018) learns to skip timesteps in recurrent dynamics models by min-pooling over reconstruction losses — selecting intervals that are easiest to predict — but operates on raw observation prediction without MBRL integration and optimizes for prediction ease rather than policy-relevant dynamical significance. DMWM (NeurIPS 2025 spotlight) addresses long-horizon RSSM imagination via logical reasoning (dual-mind architecture with System 1/System 2 feedback) but does not change temporal resolution — it improves prediction quality at fixed rate rather than extending the effective imagination horizon. DyMoDreamer (NeurIPS 2025) uses inter-frame differencing masks to modulate RSSM attention toward dynamic features, improving representation quality at the observation level, but maintains fixed temporal resolution during imagination. ELVIS (May 2026) introduces uncertainty-aware lambda-return gating in RSSM-based MPC, adaptively weighting imagination steps by epistemic uncertainty, but does not change the temporal resolution of imagination itself. Schiewer et al. (2024) document model exploitation at the abstract level as a central failure mode of multi-model hierarchical world models, motivating a single-model approach. A continuous event gate that adapts RSSM imagination rate within DreamerV3's actor-critic framework fills this gap — avoiding multi-model exploitation while offering finer temporal adaptation than two-level hierarchies and extending effective imagination horizons for better credit assignment.
51	
52	## Landscape (SOTA & Limitations)
53	
54	Latent world models for MBRL operate in several temporal paradigms. (1) Fixed-rate actor-critic imagination: DreamerV3 (Nature 2025) uses RSSM with H=15 imagination rollouts for actor-critic training; NE-Dreamer (2026) and R2-Dreamer (ICLR 2026) extend this with decoder-free latent prediction. (2) Fixed-rate short-horizon MPC: TD-MPC2 (ICLR 2024) uses implicit latent dynamics with MPPI planning over H=3–5 steps, bootstrapping with a learned terminal value function — no actor-critic imagination. (3) Externally-specified variable-rate: TAWM (ICML 2025) conditions TD-MPC2's dynamics on user-specified Δt via RK4/Euler integration, learning dynamics across time scales but not deciding when to apply which scale. (4) Learned temporal hierarchies: THICK (Gumbsch et al., ICLR 2024) learns a two-level hierarchy via discrete latent dynamics where the lower level forms invariant contexts and the upper level predicts context changes. HWM (Zhang et al., arXiv 2604.03208, April 2026) learns multi-scale latent world models for hierarchical planning with a learned action encoder for temporal compression. (5) Learned skipping for exploration: LS-Imagine (Li et al., ICLR 2025 Oral) learns jumping flags based on affordance-map kurtosis for open-world exploration in MineDojo, with action-independent jumps. (6) Learned temporal skipping for prediction: Adaptive Skip Intervals (Neitz et al., NeurIPS 2018) uses min-pooling over reconstruction losses to select prediction intervals that minimize prediction error — a direct precursor to learned temporal abstraction in dynamics models, but designed for standalone prediction tasks without RL integration. (7) Improving RSSM imagination quality without temporal resolution change: DMWM (Wang et al., NeurIPS 2025 spotlight) uses a dual-mind architecture with RSSM-S1 (intuitive transitions) and LINN-S2 (logical reasoning feedback) to improve long-horizon imagination coherence — addresses error accumulation through logical constraints rather than temporal skipping. DyMoDreamer (NeurIPS 2025) uses inter-frame differencing masks with stochastic categorical dynamic modulation to focus RSSM attention on motion-relevant features, improving representation quality for visual tasks (SOTA on Atari 100k and DMC). (8) Temporal abstractions in autoregressive/offline RL: I-TAP (arXiv 2602.18694, Feb 2026) learns temporal abstractions via discrete residual tokens with a VQ-VAE, performing MCTS planning in token space for offline RL — operates in a fundamentally different paradigm (offline, autoregressive) from online RSSM-based MBRL. Emergent Temporal Abstractions (Kobayashi et al., arXiv 2512.20605, Dec 2025) introduces a metacontroller that discovers variable-length temporally-abstract controllers within autoregressive foundation models via internal RL — demonstrates temporal abstractions can emerge from sequence models but targets language/grid/MuJoCo settings, not latent imagination. (9) Adaptive temporal granularity at execution/planning level: FFDC-WAM (Wang et al., arXiv 2605.06222, May 2026) proposes adaptive action execution in world action models, deciding when to replan based on future-reality consistency — operating at the execution level rather than world model training. ELVIS (Du et al., arXiv 2605.04709, May 2026) uses ensemble-calibrated uncertainty-aware lambda-return gating for long-horizon RSSM-based MPC, adaptively weighting bootstrapping vs. rollout but not changing temporal resolution. (10) Event-aware world models: EA-WM (arXiv 2605.06192, May 2026) introduces event-aware fusion via frame-difference supervision for video world models at pixel level. The decoder-free WM trend (NE-Dreamer, R2-Dreamer, Dreamer-CDP, LeWorldModel — early 2026) shifts representation toward JEPA-style latent prediction. Dreamer 4 (Hafner & Yan, 2025) introduces scalable transformer world models with shortcut forcing. Schiewer et al. (Scientific Reports 2024) identify model exploitation on the abstract level as the central failure mode of hierarchical WMs. The key gap: no method combines learned event detection with variable-rate RSSM imagination for actor-critic training — extending effective imagination horizons while focusing compute on dynamically significant transitions.
55	
56	## Proposed Approach
57	
58	Augment DreamerV3's RSSM with a learned event gate for adaptive-horizon actor-critic imagination. The key architectural insight: by learning to skip uneventful timesteps during imagination, a nominal H=15 rollout covers H_eff = Σ Δt_i environment steps (up to 15×K_max), directly extending the credit assignment horizon without additional latent computation.
59	
60	**Variable-rate RSSM.** Adapt the TAWM principle to DreamerV3's recurrent state-space model. The RSSM sequence model is augmented to accept a temporal gap: h_t = GRU(concat(z_{t-1}, a_{t-1}, embed(Δt)), h_{t-1}), where embed(Δt) is a learned embedding of the integer skip length. During world model training on replay buffer data, trajectories are subsampled at randomly chosen Δt ∈ {1, ..., K} (log-uniform), teaching the RSSM to predict across variable temporal gaps. The reward head is extended to predict cumulative discounted reward r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k} over the skip interval, and the continue predictor estimates minimum continuation probability within the interval. K_max is capped at 8 to limit cumulative reward prediction error (accuracy degrades with Δt since intermediate states/actions are unobserved); the gating curriculum further mitigates this by starting with small Δt and gradually increasing.
61	
62	**Event gate.** At each imagination step, a lightweight MLP gate head takes the current RSSM state (h_t, z_t) and outputs a categorical distribution over {1, 2, ..., K} for Δt via Gumbel-Softmax (temperature annealed τ=5.0→0.5 over training). When the gate selects Δt=1, the model predicts at full resolution; when Δt>1, the RSSM transitions across Δt environment steps in a single latent step. The actor outputs one action per imagination step, held constant for Δt environment timesteps — appropriate for low-significance phases (free-space motion, transport) where actions change slowly.
63	
64	**Gate supervision (simplified).** The primary gate supervision signal is the L2 norm of consecutive latent-state deltas ||s_t - s_{t-1}||_2 (with stop-gradient on latent states used to compute deltas, preventing circular gradients). This signal is simple, has no training dependencies, and directly measures dynamical significance: states where the latent representation changes rapidly correspond to contacts, grasps, and mode changes. High latent-delta → gate outputs Δt≈1; low latent-delta → gate can output large Δt. The value-gradient magnitude ||∂V(s_t)/∂s_t||_2 is included as a secondary ablation signal (not in the primary method) to test whether policy-relevant significance beyond latent dynamics provides additional benefit. This simplification reduces the core method to a single gate-supervision hyperparameter (the latent-delta threshold), avoiding the complexity of stop-gradient on critic parameters and delayed meaningful signal issues.
65	
66	**Differentiation from DyMoDreamer.** DyMoDreamer's inter-frame differencing operates at the observation/pixel level to modulate RSSM attention toward motion-relevant features — it improves what the model attends to at each fixed-rate step. Our latent-state delta operates in the learned latent space to control temporal resolution — it determines how many environment steps each latent step spans. DyMoDreamer does not change temporal granularity; our method does not change attention/representation quality.
67	
68	**Imagination returns.** The λ-return computation is adapted for variable-rate steps: V_λ(s_τ) = r_cum(s_τ, a_τ, Δt_τ) + γ^{Δt_τ} · ((1-λ)V(s_{τ+1}) + λV_λ(s_{τ+1})), where the discount factor γ^{Δt} correctly accounts for temporal gaps. This preserves DreamerV3's actor-critic training while naturally incorporating variable temporal resolution.
69	
70	**Gate collapse mitigations.** (1) Entropy regularization: auxiliary loss λ_H·H(p_gate) prevents collapse to always-Δt=1 or always-Δt=K, with λ_H annealed 0.1→0.01. (2) Gating curriculum: gate disabled for first 50K environment steps (Δt=1 only), then influence linearly ramped 0→1 over next 100K steps, allowing meaningful latent representations to form before the gate activates. (3) Gumbel-Softmax temperature annealing: high initial temperature produces exploratory near-uniform sampling, gradually sharpening. (4) Minimum-entropy floor: additional penalty if batch gate entropy drops below threshold.
71	
72	**Differentiation from Adaptive Skip Intervals.** ASI (Neitz et al., 2018) learns to skip timesteps by minimizing reconstruction loss via min-pooling — selecting intervals that are *easiest* to predict. Our gate optimizes for *dynamical significance* via latent-state deltas, focusing on transitions where the world changes meaningfully, not where prediction is easy. ASI operates on raw observation prediction for standalone tasks; our gate operates within RSSM latent imagination for actor-critic MBRL.
73	
74	**Differentiation from concurrent work.** Unlike DMWM's logical reasoning (which improves prediction quality at fixed temporal resolution), our gate extends the effective temporal horizon of imagination. Unlike ELVIS's uncertainty-aware lambda-return gating (which re-weights existing fixed-rate imagination steps), our gate changes the temporal resolution of imagination itself. Unlike FFDC-WAM (which adapts action execution at deployment), our gate operates during training-time imagination. Unlike THICK's two-level hierarchy, our single-model approach uses continuous Δt values within one RSSM, avoiding the multi-model exploitation problem (Schiewer et al., 2024).
75	
76	**Evaluation.** 3 ManiSkill3 tasks spanning a wide range of episode lengths and phase complexity: PickCube-v1 (short-horizon, 50 steps — baseline where gate should learn Δt≈1 throughout, confirming no harm on simple tasks), PegInsertionSide-v1 (medium-horizon, 100 steps — contact-rich precision insertion with critical alignment phases), StackPyramid-v1 (long-horizon, 250 steps — sequential multi-object manipulation with pick-place-stack across 3 objects, requiring approach→grasp→lift→transport→place repeated 3 times with increasing precision). StackPyramid-v1 is the primary task for demonstrating credit assignment benefits: at 250 steps, DreamerV3's H=15 covers only 6% of the episode per imagination rollout, creating severe credit assignment bottleneck for late-phase events. Integration note: DreamerV3 is not an official ManiSkill3 baseline; we budget 3-4 days for integration using NM512/dreamerv3-torch (PyTorch, gymnasium-compatible) with ManiSkill3's CPUGymWrapper. Fallback: if integration proves unstable within the first week, fall back to DMC manipulation tasks (Reacher Hard, Manipulator Insert) where DreamerV3 is well-tested, then add ManiSkill3 results for ICLR 2027. Baselines: (1) DreamerV3 (fixed-rate H=15), (2) DreamerV3 + uniform-random Δt (variable-rate RSSM without learned gating — isolates the contribution of learned event detection vs. variable-rate dynamics alone). Key ablations: (a) latent-delta-only (primary) vs. latent-delta + value-gradient gate supervision, (b) with vs. without entropy regularization/curriculum. All main experiments use 3 seeds; ablations use 2 seeds. Metrics: task success rate, effective imagination horizon (mean Σ Δt_i per rollout), wall-clock training time, gate activation statistics (temporal distribution of gating decisions overlaid with ground-truth contact/grasp timestamps).
77	
78	## Resource Estimate
79	
80	- **human_in_loop**: {'claude_api_cost': '$80-150', 'estimated_gpu_cost': '$400-600', 'gpu_hours': '~200 H100-hours', 'gpu_utilization': 'Moderate (~55%). Agent handles implementation and experiment queuing; human approves architecture decisions and diagnoses gate collapse if it occurs.', 'risk_note': 'Primary risk: ManiSkill3 integration (3-4 days budgeted; DMC fallback available). Secondary risk: gate collapse despite mitigations — if entropy regularization and curriculum are insufficient, fallback is soft attention-weighted mixture of single-step and skip predictions (continuous relaxation avoiding hard gating). Tertiary risk: cumulative reward prediction inaccuracy at large Δt — mitigated by K_max=8 cap and curriculum. Budget includes ~14 H100-hours contingency beyond the 186h manual estimate.', 'team': '1 researcher, ~30min/day', 'timeline': '6-8 weeks'}
81	- **manual**: {'breakdown': 'Main experiments: 3 tasks × 3 configurations (proposed, DreamerV3, DreamerV3+uniform-Δt) × 3 seeds × 4 H100-hours/run ≈ 108h. Ablations: 3 tasks × 2 ablation configs × 2 seeds × 4h ≈ 48h. Hyperparameter tuning (focused sweep: fix curriculum timing from prior work, tune only τ schedule and λ_H — 3-4 runs each): ~30h. Total ≈ 186 H100-hours. THICK-style baseline excluded: reimplementing THICK (TensorFlow) in PyTorch within timeline is high-risk; we compare conceptually and via published results.', 'estimated_gpu_cost': '$370-560 (at ~$2-3/hr spot H100)', 'gpu_hours': '~186 H100-hours', 'gpu_utilization': 'Low-moderate (~35-45%). Human time dominates: implementing variable-rate RSSM and event gate atop DreamerV3, ManiSkill3 integration, debugging gating stability, analyzing gate statistics.', 'team': '1-2 researchers', 'timeline': '3-4 months'}
82	
83	## Key References
84	
85	- Mastering Diverse Domains through World Models (Hafner et al., Nature 2025) — DreamerV3 RSSM, base architecture for actor-critic imagination (H=15)
86	- Adaptive Skip Intervals: Temporal Abstraction for Recurrent Dynamical Models (Neitz et al., NeurIPS 2018) — learned temporal skipping via min-pooling over reconstruction losses; direct precursor, key differentiation: prediction-ease vs. dynamical significance
87	- TD-MPC2: Scalable, Robust World Models for Continuous Control (Hansen et al., ICLR 2024) — implicit latent dynamics with MPPI planning (H=3-5), secondary reference
88	- Time-Aware World Model for Adaptive Prediction and Control (ICML 2025) — variable-Δt integration principle via RK4/Euler conditioning; we adapt this principle to RSSM
89	- Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics (Gumbsch et al., ICLR 2024) — THICK, learned two-level hierarchy via discrete dynamics
90	- Hierarchical Planning with Latent World Models (Zhang et al., arXiv 2604.03208, April 2026) — HWM, multi-scale latent WMs for hierarchical planning
91	- Open-World Reinforcement Learning over Long Short-Term Imagination (Li et al., ICLR 2025 Oral) — LS-Imagine, learned jumping flags for exploration imagination
92	- DMWM: Dual-Mind World Model with Long-Term Imagination (Wang et al., NeurIPS 2025 spotlight) — dual-mind RSSM with logical reasoning feedback for long-horizon imagination quality; different mechanism (logical consistency vs. temporal resolution) for same motivation (extending RSSM imagination)
93	- DyMoDreamer: World Modeling with Dynamic Modulation (NeurIPS 2025) — inter-frame differencing masks with stochastic categorical modulation in RSSM; observation-level dynamic attention (not temporal resolution change); latent-delta differentiation point
94	- In-Context Planning with Latent Temporal Abstractions (I-TAP, arXiv 2602.18694, Feb 2026) — temporal abstractions via discrete residual tokens with MCTS in token space for offline RL; different paradigm (offline, autoregressive) from online RSSM imagination
95	- Emergent Temporal Abstractions in Autoregressive Models Enable Hierarchical RL (Kobayashi et al., arXiv 2512.20605, Dec 2025) — metacontroller discovering variable-length temporally-abstract controllers via internal RL in sequence models
96	- When to Trust Imagination: Adaptive Action Execution for World Action Models (Wang et al., arXiv 2605.06222, May 2026) — FFDC for adaptive execution-level temporal granularity in robotic manipulation
97	- ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC (Du et al., arXiv 2605.04709, May 2026) — uncertainty-aware lambda-return gating in RSSM-based MPC
98	- EA-WM: Event-Aware Generative World Model (arXiv 2605.06192, May 2026) — event-aware fusion at pixel level
99	- Exploring the Limits of Hierarchical World Models in RL (Schiewer et al., Scientific Reports 2024) — model exploitation problem in multi-model hierarchical WMs
100	- Next Embedding Prediction Makes World Models Stronger (NE-Dreamer, 2026) — decoder-free latent WM trend
101	- R2-Dreamer: Redundancy-Reduced World Models (ICLR 2026) — decoder-free WMs
102	- Training Agents Inside of Scalable World Models (Dreamer 4, Hafner & Yan, 2025) — scalable transformer WM
103	- Adaptive Computation Time for Recurrent Neural Networks (Graves, 2016) — ACT halting-probability inspiration for gating
104	- Dynamic-Horizon Model-Based Value Estimation with Latent Imagination (IEEE TNNLS 2024)
105	
106	## Reviewer Evaluation
107	
108	**Scores**:
109	  - clarity: **{'rationale': 'Exceptionally well-specified: every architectural component has precise formulation (GRU modification, Gumbel-Softmax gate, cumulative reward head, adapted λ-returns). Differentiation from each of 10+ related works is explicit and correct. Evaluation plan is concrete with specific tasks, seeds, metrics, and fallback.', 'score': 5}**/5
110	  - feasibility: **{'rationale': '186 H100-hours fits within 200h budget. ManiSkill3 integration risk is acknowledged with DMC fallback. r2dreamer (5x faster than dreamerv3-torch, gym-compatible, supports manipulation) is the correct starting point. Gate collapse mitigations (4 mechanisms + curriculum) are well-designed. Timeline is tight (20 days) but achievable with experienced researcher. Per-run cost of 4h is optimistic but plausible with r2dreamer + H100.', 'score': 4}**/5
111	  - impact: **{'rationale': "Addresses a real credit assignment bottleneck in RSSM-based MBRL. Clean modular design applicable to any RSSM model. However, evaluation on 50-250 step tasks limits demonstrated impact — the method's strongest case requires 500+ step tasks with many distinct phases. StackPyramid (250 steps, 6 phases) is a reasonable middle ground but may show only moderate gains over DreamerV3 whose replay-buffer-sampled starting states partially mitigate the horizon limitation.", 'score': 3}**/5
112	  - novelty: **{'rationale': 'Genuinely novel combination verified through extensive search: no existing work combines learned event gating (via latent-state deltas) with variable-rate RSSM imagination for actor-critic training. Well-differentiated from THICK (fixed hierarchy), TAWM (externally conditioned), ASI (prediction-ease), LS-Imagine (exploration jumps), DMWM (quality not resolution), DyMoDreamer (attention not temporal), ELVIS (lambda weighting not resolution), and FFDC-WAM (execution not imagination).', 'score': 4}**/5
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "16fbe987-0668-4fd4-b739-61db518bb711",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/IDEA_BRIEF.md",
      "content": "# Idea Brief: Event-Gated Adaptive-Horizon Latent World Model\n\n\n- **Idea ID**: `idea_006`\n- **Created**: 2026-05-10\n- **Source**: web_research\n- **Level**: top-tier\n- **Target Venues**: CoRL 2026 (abstract: May 26, paper: May 29 — tight but feasible with ManiSkill3 integration as primary risk; may submit with 2 tasks + preliminary ablations if StackPyramid integration delayed), NeurIPS 2026 Workshops (~Aug-Sep 2026, ideal for preliminary results on 2-3 tasks), ICLR 2027 (expected ~Sep-Oct 2026, primary target for full paper with complete ablations, DMC+ManiSkill3 results, and analysis), TMLR (rolling, fallback)\n\n## Seed Topic\n\nTarget: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: World models for robot learning — predictive models of environment dynamics that support planning, imagination-based RL, or representation learning. In-scope: latent dynamics models (RSSM-family, JEPA-style), pixel-space video WMs adapted to robotics, semantic-aware WMs, mask/feature WMs, hierarchical WMs.\n\nRecent landscape (do not duplicate): DreamerV3, V-JEPA-2, NVIDIA Cosmos, GAIA-style driving WMs, OASIS, Genie-2, TC-IDM, CoWVLA, EA-WM, Mask World Model, DreamVLA. Avoid pure DreamerV3 reimplementations.\n\nContribution type: METHOD ONLY. Either (a) a new WM architecture, (b) a new training objective, or (c) a new way to use WM predictions for downstream control. Pure WM analysis without method is out of scope.\n\nSIM-ONLY MITIGATION: WM training and evaluation in sim is standard at CoRL — pure-sim WM papers are routinely accepted when method is novel. Frame as algorithmic contribution.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Rules out training a Cosmos-scale video WM from scratch. Use: small latent WMs trained from scratch, OR fine-tune an open WM (Cosmos releases, V-JEPA, OASIS), OR distill a large WM into a small one.\n2. Time: ≤20 days. Build on: dreamerv3 codebase, JEPA reference impls, HF Diffusers, NVIDIA Cosmos repo if released.\n3. Eval: ManiSkill (open-loop video prediction quality + downstream policy), LIBERO (planning quality), Isaac Lab (RL with imagined rollouts), RoboCasa, RoboTwin. Compare against MBRL and model-free RL baselines on identical tasks.\n\nLook for: efficient latent dynamics with task-relevant abstraction, structured WMs that decouple agent vs environment dynamics, semantic bottlenecks that prioritize decision-relevant features over photometric realism, hierarchical/multi-scale temporal WMs. Avoid: vanilla pixel reconstruction WMs, generic Dreamer ablations.\n\nTag: direction=world_model, contribution_type=method. target_venues=[\"CoRL 2026\"].\n\n## Generation Journey\n\n1. **Start** — 开始生成，seed: 'Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\\n\\nDirection: World models for robot learning — predictive models of environment dynamics that support planning, imagination-based RL, or representation learning. In-scope: latent dynamics models (RSSM-family, JEPA-style), pixel-space video WMs adapted to robotics, semantic-aware WMs, mask/feature WMs, hierarchical WMs.\\n\\nRecent landscape (do not duplicate): DreamerV3, V-JEPA-2, NVIDIA Cosmos, GAIA-style driving WMs, OASIS, Genie-2, TC-IDM, CoWVLA, EA-WM, Mask World Model, DreamVLA. Avoid pure DreamerV3 reimplementations.\\n\\nContribution type: METHOD ONLY. Either (a) a new WM architecture, (b) a new training objective, or (c) a new way to use WM predictions for downstream control. Pure WM analysis without method is out of scope.\\n\\nSIM-ONLY MITIGATION: WM training and evaluation in sim is standard at CoRL — pure-sim WM papers are routinely accepted when method is novel. Frame as algorithmic contribution.\\n\\nHARD CONSTRAINTS:\\n1. Compute: ≤200 H100-hours total. Rules out training a Cosmos-scale video WM from scratch. Use: small latent WMs trained from scratch, OR fine-tune an open WM (Cosmos releases, V-JEPA, OASIS), OR distill a large WM into a small one.\\n2. Time: ≤20 days. Build on: dreamerv3 codebase, JEPA reference impls, HF Diffusers, NVIDIA Cosmos repo if released.\\n3. Eval: ManiSkill (open-loop video prediction quality + downstream policy), LIBERO (planning quality), Isaac Lab (RL with imagined rollouts), RoboCasa, RoboTwin. Compare against MBRL and model-free RL baselines on identical tasks.\\n\\nLook for: efficient latent dynamics with task-relevant abstraction, structured WMs that decouple agent vs environment dynamics, semantic bottlenecks that prioritize decision-relevant features over photometric realism, hierarchical/multi-scale temporal WMs. Avoid: vanilla pixel reconstruction WMs, generic Dreamer ablations.\\n\\nTag: direction=world_model, contribution_type=method. target_venues=[\"CoRL 2026\"].'\n2. **Problem Discovery** (679s) — 发现 4 个研究方向\n   - Event-Gated Adaptive-Horizon Latent World Model\n   - Interaction-Graph JEPA for Object-Centric World Modeling\n   - Multi-Scale Self-Consistency Training for Latent Dynamics\n   - Action-Effect Decomposed World Model with Passive Pre-Training\n3. **Method Synthesis** (592s) — 完成: \"Event-Gated Adaptive-Horizon Latent World Model\" [solid] → CoRL 2026 (abstract deadline: May 26, paper deadline: May 29 — tight but feasible for workshop-length submission or if codebase is near-ready), NeurIPS 2026 Workshops (workshop paper deadline ~Aug-Sep 2026, ideal for preliminary results), ICLR 2027 (expected deadline ~Sep-Oct 2026, primary target for full paper), TMLR (rolling deadline, always open — fallback for thorough journal-length treatment)\n3. **Method Synthesis** (365s) — 完成: \"Interaction-Graph JEPA for Object-Centric World Modeling\" [solid] → CoRL 2026 (deadline May 28, 2026), ICLR 2027 (expected deadline ~September 2026), AAAI 2027 (expected deadline ~August 2026)\n3. **Method Synthesis** (361s) — 完成: \"Multi-Scale Self-Consistency Training for Latent Dynamics\" [top-tier] → CoRL 2026 (paper deadline: May 29, 2026), AAAI 2027 (paper deadline: ~August 1, 2026), ICLR 2027 (expected deadline: ~October 2026)\n3. **Method Synthesis** (625s) — 完成: \"Action-Effect Decomposed World Model with Passive Pre-Training\" [top-tier] → CoRL 2026 (abstract May 26, paper May 28, 2026 — ideal robotics+learning venue), ICLR 2027 (expected ~Sep/Oct 2026 deadline — broader ML audience), ICRA 2027 (expected ~Sep 2026 deadline — robotics audience)\n\n## Core Problem\n\nLatent world models for manipulation predict at fixed temporal resolution during imagination, creating a credit assignment bottleneck for long-horizon tasks. In DreamerV3, actor-critic training uses imagination rollouts of H=15 latent steps, each covering one environment timestep — so for a 250-step manipulation episode (e.g., ManiSkill3 StackPyramid), imagination covers only 6% of the episode per rollout. Uneventful intervals (free-space approach, transport) consume the same prediction budget as critical state transitions (contacts, grasps, mode changes), simultaneously wasting imagination compute on uninformative phases and starving late-episode events of credit signal. The problem is most pronounced in contact-rich manipulation with distinct task phases (approach → grasp → lift → transport → place → release), but affects any task where dynamics complexity varies over time. Current solutions are either externally specified (TAWM takes Δt as input), structurally fixed (THICK and HWM use two-level hierarchies), domain-specific (LS-Imagine uses affordance-based jumping for open-world exploration), operate at the execution level rather than imagination (FFDC-WAM), or address prediction quality rather than temporal resolution (DMWM uses logical reasoning, DyMoDreamer uses observation-level dynamic modulation). No existing latent world model learns continuous event-driven temporal resolution to extend imagination horizons for actor-critic policy optimization.\n\n## Opportunity / Why Now\n\nThe design point of combining learned event detection with variable-rate latent imagination in a single RSSM-based model for actor-critic training remains open. By learning to skip uneventful timesteps during imagination, the effective horizon extends far beyond H environment steps while keeping latent computation at H steps — directly improving credit assignment for long-horizon tasks. THICK (ICLR 2024) learns temporal abstractions via discrete latent dynamics but uses a fixed two-level hierarchy that cannot express continuous degrees of event significance or variable skip lengths. TAWM (ICML 2025) enables variable-Δt integration but requires Δt to be externally specified and is built on TD-MPC2's short-horizon MPC (H=3–5 with MPPI planning), where temporal skipping during planning is counterproductive. HWM (Zhang et al., April 2026) learns multi-scale latent world models but uses a fixed two-level planner. LS-Imagine (ICLR 2025 Oral) learns jumping flags for long-horizon imagination but targets open-world exploration with action-independent jumps, not actor-critic policy optimization. Adaptive Skip Intervals (Neitz et al., NeurIPS 2018) learns to skip timesteps in recurrent dynamics models by min-pooling over reconstruction losses — selecting intervals that are easiest to predict — but operates on raw observation prediction without MBRL integration and optimizes for prediction ease rather than policy-relevant dynamical significance. DMWM (NeurIPS 2025 spotlight) addresses long-horizon RSSM imagination via logical reasoning (dual-mind architecture with System 1/System 2 feedback) but does not change temporal resolution — it improves prediction quality at fixed rate rather than extending the effective imagination horizon. DyMoDreamer (NeurIPS 2025) uses inter-frame differencing masks to modulate RSSM attention toward dynamic features, improving representation quality at the observation level, but maintains fixed temporal resolution during imagination. ELVIS (May 2026) introduces uncertainty-aware lambda-return gating in RSSM-based MPC, adaptively weighting imagination steps by epistemic uncertainty, but does not change the temporal resolution of imagination itself. Schiewer et al. (2024) document model exploitation at the abstract level as a central failure mode of multi-model hierarchical world models, motivating a single-model approach. A continuous event gate that adapts RSSM imagination rate within DreamerV3's actor-critic framework fills this gap — avoiding multi-model exploitation while offering finer temporal adaptation than two-level hierarchies and extending effective imagination horizons for better credit assignment.\n\n## Landscape (SOTA & Limitations)\n\nLatent world models for MBRL operate in several temporal paradigms. (1) Fixed-rate actor-critic imagination: DreamerV3 (Nature 2025) uses RSSM with H=15 imagination rollouts for actor-critic training; NE-Dreamer (2026) and R2-Dreamer (ICLR 2026) extend this with decoder-free latent prediction. (2) Fixed-rate short-horizon MPC: TD-MPC2 (ICLR 2024) uses implicit latent dynamics with MPPI planning over H=3–5 steps, bootstrapping with a learned terminal value function — no actor-critic imagination. (3) Externally-specified variable-rate: TAWM (ICML 2025) conditions TD-MPC2's dynamics on user-specified Δt via RK4/Euler integration, learning dynamics across time scales but not deciding when to apply which scale. (4) Learned temporal hierarchies: THICK (Gumbsch et al., ICLR 2024) learns a two-level hierarchy via discrete latent dynamics where the lower level forms invariant contexts and the upper level predicts context changes. HWM (Zhang et al., arXiv 2604.03208, April 2026) learns multi-scale latent world models for hierarchical planning with a learned action encoder for temporal compression. (5) Learned skipping for exploration: LS-Imagine (Li et al., ICLR 2025 Oral) learns jumping flags based on affordance-map kurtosis for open-world exploration in MineDojo, with action-independent jumps. (6) Learned temporal skipping for prediction: Adaptive Skip Intervals (Neitz et al., NeurIPS 2018) uses min-pooling over reconstruction losses to select prediction intervals that minimize prediction error — a direct precursor to learned temporal abstraction in dynamics models, but designed for standalone prediction tasks without RL integration. (7) Improving RSSM imagination quality without temporal resolution change: DMWM (Wang et al., NeurIPS 2025 spotlight) uses a dual-mind architecture with RSSM-S1 (intuitive transitions) and LINN-S2 (logical reasoning feedback) to improve long-horizon imagination coherence — addresses error accumulation through logical constraints rather than temporal skipping. DyMoDreamer (NeurIPS 2025) uses inter-frame differencing masks with stochastic categorical dynamic modulation to focus RSSM attention on motion-relevant features, improving representation quality for visual tasks (SOTA on Atari 100k and DMC). (8) Temporal abstractions in autoregressive/offline RL: I-TAP (arXiv 2602.18694, Feb 2026) learns temporal abstractions via discrete residual tokens with a VQ-VAE, performing MCTS planning in token space for offline RL — operates in a fundamentally different paradigm (offline, autoregressive) from online RSSM-based MBRL. Emergent Temporal Abstractions (Kobayashi et al., arXiv 2512.20605, Dec 2025) introduces a metacontroller that discovers variable-length temporally-abstract controllers within autoregressive foundation models via internal RL — demonstrates temporal abstractions can emerge from sequence models but targets language/grid/MuJoCo settings, not latent imagination. (9) Adaptive temporal granularity at execution/planning level: FFDC-WAM (Wang et al., arXiv 2605.06222, May 2026) proposes adaptive action execution in world action models, deciding when to replan based on future-reality consistency — operating at the execution level rather than world model training. ELVIS (Du et al., arXiv 2605.04709, May 2026) uses ensemble-calibrated uncertainty-aware lambda-return gating for long-horizon RSSM-based MPC, adaptively weighting bootstrapping vs. rollout but not changing temporal resolution. (10) Event-aware world models: EA-WM (arXiv 2605.06192, May 2026) introduces event-aware fusion via frame-difference supervision for video world models at pixel level. The decoder-free WM trend (NE-Dreamer, R2-Dreamer, Dreamer-CDP, LeWorldModel — early 2026) shifts representation toward JEPA-style latent prediction. Dreamer 4 (Hafner & Yan, 2025) introduces scalable transformer world models with shortcut forcing. Schiewer et al. (Scientific Reports 2024) identify model exploitation on the abstract level as the central failure mode of hierarchical WMs. The key gap: no method combines learned event detection with variable-rate RSSM imagination for actor-critic training — extending effective imagination horizons while focusing compute on dynamically significant transitions.\n\n## Proposed Approach\n\nAugment DreamerV3's RSSM with a learned event gate for adaptive-horizon actor-critic imagination. The key architectural insight: by learning to skip uneventful timesteps during imagination, a nominal H=15 rollout covers H_eff = Σ Δt_i environment steps (up to 15×K_max), directly extending the credit assignment horizon without additional latent computation.\n\n**Variable-rate RSSM.** Adapt the TAWM principle to DreamerV3's recurrent state-space model. The RSSM sequence model is augmented to accept a temporal gap: h_t = GRU(concat(z_{t-1}, a_{t-1}, embed(Δt)), h_{t-1}), where embed(Δt) is a learned embedding of the integer skip length. During world model training on replay buffer data, trajectories are subsampled at randomly chosen Δt ∈ {1, ..., K} (log-uniform), teaching the RSSM to predict across variable temporal gaps. The reward head is extended to predict cumulative discounted reward r_cum = Σ_{k=0}^{Δt-1} γ^k r_{t+k} over the skip interval, and the continue predictor estimates minimum continuation probability within the interval. K_max is capped at 8 to limit cumulative reward prediction error (accuracy degrades with Δt since intermediate states/actions are unobserved); the gating curriculum further mitigates this by starting with small Δt and gradually increasing.\n\n**Event gate.** At each imagination step, a lightweight MLP gate head takes the current RSSM state (h_t, z_t) and outputs a categorical distribution over {1, 2, ..., K} for Δt via Gumbel-Softmax (temperature annealed τ=5.0→0.5 over training). When the gate selects Δt=1, the model predicts at full resolution; when Δt>1, the RSSM transitions across Δt environment steps in a single latent step. The actor outputs one action per imagination step, held constant for Δt environment timesteps — appropriate for low-significance phases (free-space motion, transport) where actions change slowly.\n\n**Gate supervision (simplified).** The primary gate supervision signal is the L2 norm of consecutive latent-state deltas ||s_t - s_{t-1}||_2 (with stop-gradient on latent states used to compute deltas, preventing circular gradients). This signal is simple, has no training dependencies, and directly measures dynamical significance: states where the latent representation changes rapidly correspond to contacts, grasps, and mode changes. High latent-delta → gate outputs Δt≈1; low latent-delta → gate can output large Δt. The value-gradient magnitude ||∂V(s_t)/∂s_t||_2 is included as a secondary ablation signal (not in the primary method) to test whether policy-relevant significance beyond latent dynamics provides additional benefit. This simplification reduces the core method to a single gate-supervision hyperparameter (the latent-delta threshold), avoiding the complexity of stop-gradient on critic parameters and delayed meaningful signal issues.\n\n**Differentiation from DyMoDreamer.** DyMoDreamer's inter-frame differencing operates at the observation/pixel level to modulate RSSM attention toward motion-relevant features — it improves what the model attends to at each fixed-rate step. Our latent-state delta operates in the learned latent space to control temporal resolution — it determines how many environment steps each latent step spans. DyMoDreamer does not change temporal granularity; our method does not change attention/representation quality.\n\n**Imagination returns.** The λ-return computation is adapted for variable-rate steps: V_λ(s_τ) = r_cum(s_τ, a_τ, Δt_τ) + γ^{Δt_τ} · ((1-λ)V(s_{τ+1}) + λV_λ(s_{τ+1})), where the discount factor γ^{Δt} correctly accounts for temporal gaps. This preserves DreamerV3's actor-critic training while naturally incorporating variable temporal resolution.\n\n**Gate collapse mitigations.** (1) Entropy regularization: auxiliary loss λ_H·H(p_gate) prevents collapse to always-Δt=1 or always-Δt=K, with λ_H annealed 0.1→0.01. (2) Gating curriculum: gate disabled for first 50K environment steps (Δt=1 only), then influence linearly ramped 0→1 over next 100K steps, allowing meaningful latent representations to form before the gate activates. (3) Gumbel-Softmax temperature annealing: high initial temperature produces exploratory near-uniform sampling, gradually sharpening. (4) Minimum-entropy floor: additional penalty if batch gate entropy drops below threshold.\n\n**Differentiation from Adaptive Skip Intervals.** ASI (Neitz et al., 2018) learns to skip timesteps by minimizing reconstruction loss via min-pooling — selecting intervals that are *easiest* to predict. Our gate optimizes for *dynamical significance* via latent-state deltas, focusing on transitions where the world changes meaningfully, not where prediction is easy. ASI operates on raw observation prediction for standalone tasks; our gate operates within RSSM latent imagination for actor-critic MBRL.\n\n**Differentiation from concurrent work.** Unlike DMWM's logical reasoning (which improves prediction quality at fixed temporal resolution), our gate extends the effective temporal horizon of imagination. Unlike ELVIS's uncertainty-aware lambda-return gating (which re-weights existing fixed-rate imagination steps), our gate changes the temporal resolution of imagination itself. Unlike FFDC-WAM (which adapts action execution at deployment), our gate operates during training-time imagination. Unlike THICK's two-level hierarchy, our single-model approach uses continuous Δt values within one RSSM, avoiding the multi-model exploitation problem (Schiewer et al., 2024).\n\n**Evaluation.** 3 ManiSkill3 tasks spanning a wide range of episode lengths and phase complexity: PickCube-v1 (short-horizon, 50 steps — baseline where gate should learn Δt≈1 throughout, confirming no harm on simple tasks), PegInsertionSide-v1 (medium-horizon, 100 steps — contact-rich precision insertion with critical alignment phases), StackPyramid-v1 (long-horizon, 250 steps — sequential multi-object manipulation with pick-place-stack across 3 objects, requiring approach→grasp→lift→transport→place repeated 3 times with increasing precision). StackPyramid-v1 is the primary task for demonstrating credit assignment benefits: at 250 steps, DreamerV3's H=15 covers only 6% of the episode per imagination rollout, creating severe credit assignment bottleneck for late-phase events. Integration note: DreamerV3 is not an official ManiSkill3 baseline; we budget 3-4 days for integration using NM512/dreamerv3-torch (PyTorch, gymnasium-compatible) with ManiSkill3's CPUGymWrapper. Fallback: if integration proves unstable within the first week, fall back to DMC manipulation tasks (Reacher Hard, Manipulator Insert) where DreamerV3 is well-tested, then add ManiSkill3 results for ICLR 2027. Baselines: (1) DreamerV3 (fixed-rate H=15), (2) DreamerV3 + uniform-random Δt (variable-rate RSSM without learned gating — isolates the contribution of learned event detection vs. variable-rate dynamics alone). Key ablations: (a) latent-delta-only (primary) vs. latent-delta + value-gradient gate supervision, (b) with vs. without entropy regularization/curriculum. All main experiments use 3 seeds; ablations use 2 seeds. Metrics: task success rate, effective imagination horizon (mean Σ Δt_i per rollout), wall-clock training time, gate activation statistics (temporal distribution of gating decisions overlaid with ground-truth contact/grasp timestamps).\n\n## Resource Estimate\n\n- **human_in_loop**: {'claude_api_cost': '$80-150', 'estimated_gpu_cost': '$400-600', 'gpu_hours': '~200 H100-hours', 'gpu_utilization': 'Moderate (~55%). Agent handles implementation and experiment queuing; human approves architecture decisions and diagnoses gate collapse if it occurs.', 'risk_note': 'Primary risk: ManiSkill3 integration (3-4 days budgeted; DMC fallback available). Secondary risk: gate collapse despite mitigations — if entropy regularization and curriculum are insufficient, fallback is soft attention-weighted mixture of single-step and skip predictions (continuous relaxation avoiding hard gating). Tertiary risk: cumulative reward prediction inaccuracy at large Δt — mitigated by K_max=8 cap and curriculum. Budget includes ~14 H100-hours contingency beyond the 186h manual estimate.', 'team': '1 researcher, ~30min/day', 'timeline': '6-8 weeks'}\n- **manual**: {'breakdown': 'Main experiments: 3 tasks × 3 configurations (proposed, DreamerV3, DreamerV3+uniform-Δt) × 3 seeds × 4 H100-hours/run ≈ 108h. Ablations: 3 tasks × 2 ablation configs × 2 seeds × 4h ≈ 48h. Hyperparameter tuning (focused sweep: fix curriculum timing from prior work, tune only τ schedule and λ_H — 3-4 runs each): ~30h. Total ≈ 186 H100-hours. THICK-style baseline excluded: reimplementing THICK (TensorFlow) in PyTorch within timeline is high-risk; we compare conceptually and via published results.', 'estimated_gpu_cost': '$370-560 (at ~$2-3/hr spot H100)', 'gpu_hours': '~186 H100-hours', 'gpu_utilization': 'Low-moderate (~35-45%). Human time dominates: implementing variable-rate RSSM and event gate atop DreamerV3, ManiSkill3 integration, debugging gating stability, analyzing gate statistics.', 'team': '1-2 researchers', 'timeline': '3-4 months'}\n\n## Key References\n\n- Mastering Diverse Domains through World Models (Hafner et al., Nature 2025) — DreamerV3 RSSM, base architecture for actor-critic imagination (H=15)\n- Adaptive Skip Intervals: Temporal Abstraction for Recurrent Dynamical Models (Neitz et al., NeurIPS 2018) — learned temporal skipping via min-pooling over reconstruction losses; direct precursor, key differentiation: prediction-ease vs. dynamical significance\n- TD-MPC2: Scalable, Robust World Models for Continuous Control (Hansen et al., ICLR 2024) — implicit latent dynamics with MPPI planning (H=3-5), secondary reference\n- Time-Aware World Model for Adaptive Prediction and Control (ICML 2025) — variable-Δt integration principle via RK4/Euler conditioning; we adapt this principle to RSSM\n- Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics (Gumbsch et al., ICLR 2024) — THICK, learned two-level hierarchy via discrete dynamics\n- Hierarchical Planning with Latent World Models (Zhang et al., arXiv 2604.03208, April 2026) — HWM, multi-scale latent WMs for hierarchical planning\n- Open-World Reinforcement Learning over Long Short-Term Imagination (Li et al., ICLR 2025 Oral) — LS-Imagine, learned jumping flags for exploration imagination\n- DMWM: Dual-Mind World Model with Long-Term Imagination (Wang et al., NeurIPS 2025 spotlight) — dual-mind RSSM with logical reasoning feedback for long-horizon imagination quality; different mechanism (logical consistency vs. temporal resolution) for same motivation (extending RSSM imagination)\n- DyMoDreamer: World Modeling with Dynamic Modulation (NeurIPS 2025) — inter-frame differencing masks with stochastic categorical modulation in RSSM; observation-level dynamic attention (not temporal resolution change); latent-delta differentiation point\n- In-Context Planning with Latent Temporal Abstractions (I-TAP, arXiv 2602.18694, Feb 2026) — temporal abstractions via discrete residual tokens with MCTS in token space for offline RL; different paradigm (offline, autoregressive) from online RSSM imagination\n- Emergent Temporal Abstractions in Autoregressive Models Enable Hierarchical RL (Kobayashi et al., arXiv 2512.20605, Dec 2025) — metacontroller discovering variable-length temporally-abstract controllers via internal RL in sequence models\n- When to Trust Imagination: Adaptive Action Execution for World Action Models (Wang et al., arXiv 2605.06222, May 2026) — FFDC for adaptive execution-level temporal granularity in robotic manipulation\n- ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC (Du et al., arXiv 2605.04709, May 2026) — uncertainty-aware lambda-return gating in RSSM-based MPC\n- EA-WM: Event-Aware Generative World Model (arXiv 2605.06192, May 2026) — event-aware fusion at pixel level\n- Exploring the Limits of Hierarchical World Models in RL (Schiewer et al., Scientific Reports 2024) — model exploitation problem in multi-model hierarchical WMs\n- Next Embedding Prediction Makes World Models Stronger (NE-Dreamer, 2026) — decoder-free latent WM trend\n- R2-Dreamer: Redundancy-Reduced World Models (ICLR 2026) — decoder-free WMs\n- Training Agents Inside of Scalable World Models (Dreamer 4, Hafner & Yan, 2025) — scalable transformer WM\n- Adaptive Computation Time for Recurrent Neural Networks (Graves, 2016) — ACT halting-probability inspiration for gating\n- Dynamic-Horizon Model-Based Value Estimation with Latent Imagination (IEEE TNNLS 2024)\n\n## Reviewer Evaluation\n\n**Scores**:\n  - clarity: **{'rationale': 'Exceptionally well-specified: every architectural component has precise formulation (GRU modification, Gumbel-Softmax gate, cumulative reward head, adapted λ-returns). Differentiation from each of 10+ related works is explicit and correct. Evaluation plan is concrete with specific tasks, seeds, metrics, and fallback.', 'score': 5}**/5\n  - feasibility: **{'rationale': '186 H100-hours fits within 200h budget. ManiSkill3 integration risk is acknowledged with DMC fallback. r2dreamer (5x faster than dreamerv3-torch, gym-compatible, supports manipulation) is the correct starting point. Gate collapse mitigations (4 mechanisms + curriculum) are well-designed. Timeline is tight (20 days) but achievable with experienced researcher. Per-run cost of 4h is optimistic but plausible with r2dreamer + H100.', 'score': 4}**/5\n  - impact: **{'rationale': \"Addresses a real credit assignment bottleneck in RSSM-based MBRL. Clean modular design applicable to any RSSM model. However, evaluation on 50-250 step tasks limits demonstrated impact — the method's strongest case requires 500+ step tasks with many distinct phases. StackPyramid (250 steps, 6 phases) is a reasonable middle ground but may show only moderate gains over DreamerV3 whose replay-buffer-sampled starting states partially mitigate the horizon limitation.\", 'score': 3}**/5\n  - novelty: **{'rationale': 'Genuinely novel combination verified through extensive search: no existing work combines learned event gating (via latent-state deltas) with variable-rate RSSM imagination for actor-critic training. Well-differentiated from THICK (fixed hierarchy), TAWM (externally conditioned), ASI (prediction-ease), LS-Imagine (exploration jumps), DMWM (quality not resolution), DyMoDreamer (attention not temporal), ELVIS (lambda weighting not resolution), and FFDC-WAM (execution not imagination).', 'score': 4}**/5\n",
      "numLines": 113,
      "startLine": 1,
      "totalLines": 113
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the source material. Let me also read the method section's Section 3.5 more carefully (already read above). Let me organize the information from the IDEA_BRIEF and method section to write the Related Work section.

Let me extract the key information for each work from the IDEA_BRIEF:

### 2.1 Model-Based RL with Fixed-Rate Imagination
- **DreamerV3** (Hafner et al., Nature 2025): RSSM with H=15 imagination rollouts for actor-critic training. Fixed temporal resolution.


- **NE-Dreamer** (2026): decoder-free latent world model approach focusing on next embedding prediction to strengthen world models.
- **R2-Dreamer** (ICLR 2026): decoder-free world models designed to reduce redundancy.

### 2.2 Variable-Rate and Temporal Abstraction
- **TAWM** (ICML 2025): extends TD-MPC2's dynamics by conditioning on user-specified time intervals through numerical integration methods, enabling learning across multiple time scales without autonomously selecting which scale to use. Builds on TD-MPC2's short-horizon planning approach.
- **THICK** (Gumbsch et al., ICLR 2024): constructs a two-level hierarchy using discrete latent dynamics where lower-level states form invariant contexts and upper-level predictions capture context transitions, though the hierarchy depth is fixed.
- **HWM** (Zhang et al., arXiv 2604.03208, April 2026): develops multi-scale latent world models for hierarchical planning with a learned action encoder that compresses temporal information, maintaining a fixed two-level planning structure.
- **ASI** (Neitz et al., NeurIPS 2018): applies min-pooling across reconstruction losses to identify prediction intervals with minimal error, though it operates on raw observation prediction without connecting to model-based reinforcement learning.

### 2.3 Learned Skipping for Planning
- **LS-Imagine** (Li et al., ICLR 2025 Oral): learns jumping flags based on affordance-map...

LS-Imagine learns when to skip frames for open-world exploration in MineDojo using action-independent jumps. **I-TAP** (arXiv 2602.18694, Feb 2026) takes a different approach by learning temporal abstractions through discrete residual tokens with a VQ-VAE, then performs MCTS planning in token space for offline RL—fundamentally different from the online RSSM-based MBRL paradigm.

### 2.4 Imagination Quality Improvement
- **DMWM** (Wang et al., NeurIPS 2025 spotlight): uses a dual-mind architecture pairing an RSSM for intuitive transitions with a logical reasoning module that provides feedback to improve long-horizon imagination coherence, addressing error accumulation through logical constraints rather than temporal skipping.
- **DyMoDreamer** (NeurIPS 2025): applies inter-frame differencing masks with stochastic categorical dynamic modulation to direct RSSM attention toward motion-relevant features.
- **ELVIS** (Du et al., arXiv 2605.04709, May 2026): uses ensemble-calibrated uncertainty-aware lambda-return gating in RSSM-based MPC to adaptively weight bootstrapping versus rollout without changing temporal resolution.

### 2.5 Event-Aware World Models
- **EA-WM** (arXiv 2605.06192, May 2026): incorporates event-aware fusion at the pixel level using frame-difference supervision for video world models.

I'm also noting several related approaches: Dreamer 4 scales transformer-based world models with shortcut forcing, there's research on model exploitation problems in hierarchical multi-model setups, and **FFDC-WAM** introduces adaptive action execution in world models.

Now I'm moving into the Related Work section and need to establish proper citation formatting. I'm mapping out the key papers from the method section—THICK, TAWM, ASI, LS-Imagine, and DyMoDreamer—and organizing their citation keys to maintain consistency with how they're referenced elsewhere in the paper. I'm organizing the citation keys I've identified from the method section and need to establish consistent formatting for the ones I'll create for the remaining references in the Related Work section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "cd472950-6ca3-423c-9f19-81a639c3ab86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnzrfWmJuPo7r2FhLEoc72",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8469,
      "cache_read_input_tokens": 29668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8469
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

Now I have all the source material. Let me write the Related Work draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "05714d3e-8462-4875-af0e-c43c2fe1c513",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnzrfWmJuPo7r2FhLEoc72",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8469,
      "cache_read_input_tokens": 29668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8469
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

<details open><summary>🔧 Tool call — Write · `toolu_01M5D3s3y2dHvJgEeuf6ZJoH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md",
  "content": "# 2. Related Work\n\nWe situate our approach within five related lines of research: fixed-rate model-based RL, variable-rate and temporal abstraction, learned skipping for planning, imagination quality improvement, and event-aware world models.\n\n## 2.1 Model-Based RL with Fixed-Rate Imagination\n\nModern model-based RL agents learn latent world models and optimize policies through imagined rollouts at a fixed temporal resolution.\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a Recurrent State-Space Model (RSSM) that maintains deterministic and stochastic latent states, training an actor-critic purely through $H$-step imagined trajectories. It achieves strong performance across diverse domains but operates at a fixed one-environment-step-per-latent-step resolution, limiting the effective planning horizon to $H$ environment steps regardless of episode length. NE-Dreamer \\citep{nedreamer2026} replaces pixel-level reconstruction with next-embedding prediction, yielding a decoder-free latent world model that improves sample efficiency while retaining the fixed-rate imagination structure. R2-Dreamer \\citep{r2dreamer2026} similarly eliminates the observation decoder by training with redundancy-reduced latent targets, accelerating training and improving robustness. [NEED VERIFY: exact technical details of NE-Dreamer and R2-Dreamer beyond decoder-free design]\n\nThese methods share a fundamental limitation: each imagination step covers exactly one environment timestep, so for long-horizon tasks (e.g., 250-step manipulation episodes), a rollout of $H{=}15$ steps covers only 6\\% of the episode, creating a credit assignment bottleneck. Our method addresses this by learning to skip uneventful timesteps, extending the effective horizon to $\\sum \\Delta t_i$ environment steps (up to $H \\times K$) without additional latent computation.\n\n## 2.2 Variable-Rate and Temporal Abstraction\n\nSeveral works introduce temporal flexibility into world model dynamics, either through externally specified time gaps or learned hierarchical abstractions.\n\nTAWM \\citep{freed2024tawm} introduces time-aware world models that condition latent dynamics on a temporal gap $\\Delta t$ via RK4/Euler integration, enabling the model to predict across variable time scales. However, $\\Delta t$ must be externally specified rather than learned, and TAWM is built on TD-MPC2's short-horizon MPC framework ($H{=}3$--$5$ with MPPI planning), where temporal skipping during planning is counterproductive. Our method adapts the variable-$\\Delta t$ conditioning principle to DreamerV3's RSSM but makes $\\Delta t$ \\emph{state-dependent} via a learned event gate. THICK \\citep{romac2024thick} learns a two-level temporal hierarchy via discrete latent dynamics, where the lower level forms invariant contexts and the upper level predicts context changes. While this achieves temporal abstraction, the fixed two-level structure cannot express continuous degrees of event significance or variable skip lengths within a single hierarchy level. HWM \\citep{zhang2026hwm} extends this line by learning multi-scale latent world models for hierarchical planning with a learned action encoder for temporal compression, but similarly relies on a fixed two-level planner architecture. [NEED VERIFY: exact HWM architecture details beyond multi-scale planning] ASI \\citep{neitz2018adaptive} learns to skip timesteps in recurrent dynamics models by min-pooling over reconstruction losses, selecting intervals that are easiest to predict. It operates on raw observation prediction without integration into a model-based RL loop and optimizes for prediction ease rather than dynamical significance.\n\nOur approach avoids the multi-model exploitation problem identified by \\citet{schiewer2024hierarchical} in hierarchical world models by operating within a single RSSM, while offering finer temporal adaptation than two-level hierarchies through a continuous per-step stride selection.\n\n## 2.3 Learned Skipping for Planning\n\nA separate line of work learns explicit skip or jump decisions to extend planning horizons.\n\nLS-Imagine \\citep{li2025lsimagine} learns jumping flags based on affordance-map kurtosis for open-world exploration in MineDojo, enabling the agent to skip over low-information states during imagination. The jumps are action-independent and designed for exploration in open-world settings. Our gate differs in two key ways: it operates within the actor-critic MBRL imagination loop with policy-dependent variable-rate stepping, and it selects strides based on latent-state dynamics rather than observation-space affordance maps. I-TAP \\citep{itap2026} learns temporal abstractions via discrete residual tokens with a VQ-VAE, performing MCTS planning in token space for offline RL. It operates in a fundamentally different paradigm---offline and autoregressive---from our online RSSM-based approach. [NEED VERIFY: exact I-TAP architecture details beyond VQ-VAE + MCTS description]\n\nWhile both LS-Imagine and I-TAP demonstrate the value of temporal flexibility in planning, neither addresses the specific setting of online actor-critic training with variable-rate latent imagination. Our event gate fills this gap by integrating state-dependent stride selection directly into DreamerV3's imagination pipeline.\n\n## 2.4 Imagination Quality Improvement\n\nRather than changing temporal resolution, several recent works improve the quality of fixed-rate imagination rollouts.\n\nDMWM \\citep{wang2025dmwm} introduces a dual-mind architecture combining an RSSM-based System~1 for intuitive transitions with a logic-informed neural network (LINN) System~2 that provides logical reasoning feedback, improving long-horizon imagination coherence through logical constraints. It shares our motivation of extending effective RSSM imagination but addresses error accumulation at fixed temporal resolution rather than extending the temporal horizon. DyMoDreamer \\citep{dymodreamer2025} uses inter-frame differencing masks with stochastic categorical dynamic modulation to focus RSSM attention on motion-relevant features, achieving strong results on visual benchmarks (Atari 100k, DMC). It operates at the observation/pixel level to improve per-step representation quality, whereas our method operates in latent space and changes the \\emph{temporal resolution} of imagination rather than the attention quality of individual steps---the two approaches target complementary axes of improvement and could in principle be combined. ELVIS \\citep{du2026elvis} introduces ensemble-calibrated uncertainty-aware $\\lambda$-return gating for long-horizon RSSM-based MPC, adaptively weighting bootstrapping versus continued rollout based on epistemic uncertainty. While ELVIS adapts \\emph{how much} to trust each imagination step, it does not change \\emph{how many} environment steps each imagination step covers---our gate modifies the temporal resolution itself.\n\n## 2.5 Event-Aware World Models\n\nEvent-driven representations have recently been applied to world models, though primarily at the observation level.\n\nEA-WM \\citep{eawm2026} introduces event-aware fusion via frame-difference supervision for video world models at the pixel level, using event signals to improve generation quality of dynamic regions. While both EA-WM and our method leverage event-like signals (frame differences vs. latent-state deltas), EA-WM applies them to improve pixel-level video prediction quality, whereas we use latent-state change magnitude to drive \\emph{temporal stride selection} in the imagination loop for policy optimization. Our event gate operates entirely in the learned latent space, using state-delta magnitude as a proxy for dynamical significance to determine when fine-grained versus coarse-grained imagination is warranted.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "e9abfca0-5b71-45d7-88f7-6ea3175dc39e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnzrfWmJuPo7r2FhLEoc72",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8469,
      "cache_read_input_tokens": 29668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8469
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

_source line 23 · 2026-05-13T09:01:06.596Z_

<details><summary>↩ Tool result · `toolu_01M5D3s3y2dHvJgEeuf6ZJoH`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "d4a10aa2-b3c1-4840-9b0f-24f15e2bfa43",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md",
    "content": "# 2. Related Work\n\nWe situate our approach within five related lines of research: fixed-rate model-based RL, variable-rate and temporal abstraction, learned skipping for planning, imagination quality improvement, and event-aware world models.\n\n## 2.1 Model-Based RL with Fixed-Rate Imagination\n\nModern model-based RL agents learn latent world models and optimize policies through imagined rollouts at a fixed temporal resolution.\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a Recurrent State-Space Model (RSSM) that maintains deterministic and stochastic latent states, training an actor-critic purely through $H$-step imagined trajectories. It achieves strong performance across diverse domains but operates at a fixed one-environment-step-per-latent-step resolution, limiting the effective planning horizon to $H$ environment steps regardless of episode length. NE-Dreamer \\citep{nedreamer2026} replaces pixel-level reconstruction with next-embedding prediction, yielding a decoder-free latent world model that improves sample efficiency while retaining the fixed-rate imagination structure. R2-Dreamer \\citep{r2dreamer2026} similarly eliminates the observation decoder by training with redundancy-reduced latent targets, accelerating training and improving robustness. [NEED VERIFY: exact technical details of NE-Dreamer and R2-Dreamer beyond decoder-free design]\n\nThese methods share a fundamental limitation: each imagination step covers exactly one environment timestep, so for long-horizon tasks (e.g., 250-step manipulation episodes), a rollout of $H{=}15$ steps covers only 6\\% of the episode, creating a credit assignment bottleneck. Our method addresses this by learning to skip uneventful timesteps, extending the effective horizon to $\\sum \\Delta t_i$ environment steps (up to $H \\times K$) without additional latent computation.\n\n## 2.2 Variable-Rate and Temporal Abstraction\n\nSeveral works introduce temporal flexibility into world model dynamics, either through externally specified time gaps or learned hierarchical abstractions.\n\nTAWM \\citep{freed2024tawm} introduces time-aware world models that condition latent dynamics on a temporal gap $\\Delta t$ via RK4/Euler integration, enabling the model to predict across variable time scales. However, $\\Delta t$ must be externally specified rather than learned, and TAWM is built on TD-MPC2's short-horizon MPC framework ($H{=}3$--$5$ with MPPI planning), where temporal skipping during planning is counterproductive. Our method adapts the variable-$\\Delta t$ conditioning principle to DreamerV3's RSSM but makes $\\Delta t$ \\emph{state-dependent} via a learned event gate. THICK \\citep{romac2024thick} learns a two-level temporal hierarchy via discrete latent dynamics, where the lower level forms invariant contexts and the upper level predicts context changes. While this achieves temporal abstraction, the fixed two-level structure cannot express continuous degrees of event significance or variable skip lengths within a single hierarchy level. HWM \\citep{zhang2026hwm} extends this line by learning multi-scale latent world models for hierarchical planning with a learned action encoder for temporal compression, but similarly relies on a fixed two-level planner architecture. [NEED VERIFY: exact HWM architecture details beyond multi-scale planning] ASI \\citep{neitz2018adaptive} learns to skip timesteps in recurrent dynamics models by min-pooling over reconstruction losses, selecting intervals that are easiest to predict. It operates on raw observation prediction without integration into a model-based RL loop and optimizes for prediction ease rather than dynamical significance.\n\nOur approach avoids the multi-model exploitation problem identified by \\citet{schiewer2024hierarchical} in hierarchical world models by operating within a single RSSM, while offering finer temporal adaptation than two-level hierarchies through a continuous per-step stride selection.\n\n## 2.3 Learned Skipping for Planning\n\nA separate line of work learns explicit skip or jump decisions to extend planning horizons.\n\nLS-Imagine \\citep{li2025lsimagine} learns jumping flags based on affordance-map kurtosis for open-world exploration in MineDojo, enabling the agent to skip over low-information states during imagination. The jumps are action-independent and designed for exploration in open-world settings. Our gate differs in two key ways: it operates within the actor-critic MBRL imagination loop with policy-dependent variable-rate stepping, and it selects strides based on latent-state dynamics rather than observation-space affordance maps. I-TAP \\citep{itap2026} learns temporal abstractions via discrete residual tokens with a VQ-VAE, performing MCTS planning in token space for offline RL. It operates in a fundamentally different paradigm---offline and autoregressive---from our online RSSM-based approach. [NEED VERIFY: exact I-TAP architecture details beyond VQ-VAE + MCTS description]\n\nWhile both LS-Imagine and I-TAP demonstrate the value of temporal flexibility in planning, neither addresses the specific setting of online actor-critic training with variable-rate latent imagination. Our event gate fills this gap by integrating state-dependent stride selection directly into DreamerV3's imagination pipeline.\n\n## 2.4 Imagination Quality Improvement\n\nRather than changing temporal resolution, several recent works improve the quality of fixed-rate imagination rollouts.\n\nDMWM \\citep{wang2025dmwm} introduces a dual-mind architecture combining an RSSM-based System~1 for intuitive transitions with a logic-informed neural network (LINN) System~2 that provides logical reasoning feedback, improving long-horizon imagination coherence through logical constraints. It shares our motivation of extending effective RSSM imagination but addresses error accumulation at fixed temporal resolution rather than extending the temporal horizon. DyMoDreamer \\citep{dymodreamer2025} uses inter-frame differencing masks with stochastic categorical dynamic modulation to focus RSSM attention on motion-relevant features, achieving strong results on visual benchmarks (Atari 100k, DMC). It operates at the observation/pixel level to improve per-step representation quality, whereas our method operates in latent space and changes the \\emph{temporal resolution} of imagination rather than the attention quality of individual steps---the two approaches target complementary axes of improvement and could in principle be combined. ELVIS \\citep{du2026elvis} introduces ensemble-calibrated uncertainty-aware $\\lambda$-return gating for long-horizon RSSM-based MPC, adaptively weighting bootstrapping versus continued rollout based on epistemic uncertainty. While ELVIS adapts \\emph{how much} to trust each imagination step, it does not change \\emph{how many} environment steps each imagination step covers---our gate modifies the temporal resolution itself.\n\n## 2.5 Event-Aware World Models\n\nEvent-driven representations have recently been applied to world models, though primarily at the observation level.\n\nEA-WM \\citep{eawm2026} introduces event-aware fusion via frame-difference supervision for video world models at the pixel level, using event signals to improve generation quality of dynamic regions. While both EA-WM and our method leverage event-like signals (frame differences vs. latent-state deltas), EA-WM applies them to improve pixel-level video prediction quality, whereas we use latent-state change magnitude to drive \\emph{temporal stride selection} in the imagination loop for policy optimization. Our event gate operates entirely in the learned latent space, using state-delta magnitude as a proxy for dynamical significance to determine when fine-grained versus coarse-grained imagination is warranted.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01BRwxE45U5VkrMm6EWs1HUX`</summary>

```json
{
  "name": "related_work_draft",
  "type": "paper",
  "description": "Related Work section draft (Section 2) covering 5 subsections: fixed-rate MBRL, variable-rate/temporal abstraction, learned skipping, imagination quality, event-aware WMs",
  "project": "event-gated-adaptive-horizon",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md",
  "tags": [
    "paper",
    "related-work",
    "draft"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "6893a1be-946a-44be-a24a-7d251723f89e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ps8NEjHuSaJR2JqPsSCKB2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3446,
      "cache_read_input_tokens": 38137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3446
      },
      "output_tokens": 44,
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

_source line 25 · 2026-05-13T09:01:12.179Z_

<details><summary>↩ Tool result · `toolu_01BRwxE45U5VkrMm6EWs1HUX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_23b01d\", \"name\": \"related_work_draft\", \"type\": \"paper\", \"description\": \"Related Work section draft (Section 2) covering 5 subsections: fixed-rate MBRL, variable-rate/temporal abstraction, learned skipping, imagination quality, event-aware WMs\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-13T09:01:12.116677+00:00\", \"tags\": [\"paper\", \"related-work\", \"draft\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "3d8076f8-9459-42d2-8035-57c79eb1b96e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260513_23b01d\\\", \\\"name\\\": \\\"related_work_draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Related Work section draft (Section 2) covering 5 subsections: fixed-rate MBRL, variable-rate/temporal abstraction, learned skipping, imagination quality, event-aware WMs\\\", \\\"path\\\": \\\"projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"event-gated-adaptive-horizon\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-13T09:01:12.116677+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"related-work\\\", \\\"draft\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_23b01d\", \"name\": \"related_work_draft\", \"type\": \"paper\", \"description\": \"Related Work section draft (Section 2) covering 5 subsections: fixed-rate MBRL, variable-rate/temporal abstraction, learned skipping, imagination quality, event-aware WMs\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-13T09:01:12.116677+00:00\", \"tags\": [\"paper\", \"related-work\", \"draft\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

Related Work 初稿已写入 `artifacts/related_work_draft.md` 并注册。

结构概要：
- **2.1** DreamerV3 / NE-Dreamer / R2-Dreamer — 固定步长想象的局限
- **2.2** TAWM / THICK / HWM / ASI — 变步长与时间抽象方法及各自限制
- **2.3** LS-Imagine / I-TAP — 学习跳跃的规划方法
- **2.4** DMWM / DyMoDreamer / ELVIS — 改进想象质量而非时间分辨率
- **2.5** EA-WM — 像素级事件感知 vs 我们的潜空间事件门控

标注了 3 处 `[NEED VERIFY]`：NE-Dreamer/R2-Dreamer 的具体技术细节、HWM 的架构细节、I-TAP 的架构细节。所有描述均来自 IDEA_BRIEF 的 Landscape/Key References 和 method section 3.5，未凭记忆补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "uuid": "55adb02b-589d-4c7b-b820-4285dbc41180",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1FCx1VeidWNRDA95jzm9A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 540,
      "cache_read_input_tokens": 41583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 540
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

_source line 27_

Related Work 初稿已写入 `artifacts/related_work_draft.md` 并注册。

结构概要：
- **2.1** DreamerV3 / NE-Dreamer / R2-Dreamer — 固定步长想象的局限
- **2.2** TAWM / THICK / HWM / ASI — 变步长与时间抽象方法及各自限制
- **2.3** LS-Imagine / I-TAP — 学习跳跃的规划方法
- **2.4** DMWM / DyMoDreamer / ELVIS — 改进想象质量而非时间分辨率
- **2.5** EA-WM — 像素级事件感知 vs 我们的潜空间事件门控

标注了 3 处 `[NEED VERIFY]`：NE-Dreamer/R2-Dreamer 的具体技术细节、HWM 的架构细节、I-TAP 的架构细节。所有描述均来自 IDEA_BRIEF 的 Landscape/Key References 和 method section 3.5，未凭记忆补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 106419,
  "duration_api_ms": 106793,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "8072b188-7ebd-48f9-8276-4a6a596cb5ab",
  "total_cost_usd": 0.40644849999999993,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 30676,
    "cache_read_input_tokens": 198439,
    "output_tokens": 4551,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30676,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 314,
        "cache_read_input_tokens": 41583,
        "cache_creation_input_tokens": 540,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 540
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1604,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001674,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 4551,
      "cacheReadInputTokens": 198439,
      "cacheCreationInputTokens": 30676,
      "webSearchRequests": 0,
      "costUSD": 0.4047745,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "21b9594d-5e0b-449d-b5cc-ce1c79e5e01c"
}
```

</details>

---
