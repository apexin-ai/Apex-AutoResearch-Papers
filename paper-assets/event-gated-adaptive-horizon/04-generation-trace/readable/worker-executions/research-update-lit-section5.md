# research update lit section5

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_research_update-lit-section5_20260521T125300.log`
- **Structured JSON:** [`b6a52ec113885ce2be55.json`](../../sessions/b6/b6a52ec113885ce2be55.json)

## Before a recorded user message

24 recorded events

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
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
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
  "uuid": "0c4d1d4b-1762-411f-9e99-198952e7123a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779370800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e0e5a1c5-e5a0-436a-ae0b-3a352ad2730e",
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current literature file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "e066bb53-064e-437c-834d-6cd9ed1701fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6RPQGNQxfJU15iCUZNQvr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11957,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11957
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qa81tizniqV3GACjeiuXEf`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "9c68cf62-fd22-407f-9b3e-184ddf6beb38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6RPQGNQxfJU15iCUZNQvr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11957,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11957
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

_source line 6 · 2026-05-21T12:53:12.517Z_

<details><summary>↩ Tool result · `toolu_01Qa81tizniqV3GACjeiuXEf`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "2ab15c32-d617-49c9-b36d-4f3d7e5e8aff",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current literature file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "b56aa527-a517-461f-9761-86cb094ad066",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuBhpELfxNpmKYco6RVbzK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 23404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 445
      },
      "output_tokens": 55,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AkbuKcPEdZ5uTzjzPRqPVs`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "artifacts/literature/dual_critic_cross_env_literature.md",
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
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "e6a29b41-43ab-4b0e-b803-7386113f84ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuBhpELfxNpmKYco6RVbzK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 23404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 445
      },
      "output_tokens": 55,
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

_source line 9 · 2026-05-21T12:53:16.143Z_

<details><summary>↩ Tool result · `toolu_01AkbuKcPEdZ5uTzjzPRqPVs`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/literature/dual_critic_cross_env_literature.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "e0fa2e8f-13f9-4617-8db2-96a7f4e29e2f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/literature/dual_critic_cross_env_literature.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/literature/dual_critic_cross_env_literature.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

Not in the allowed list. Let me read it directly from the filesystem.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "811a93e7-093c-4863-8f90-e8d5402ae5ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVejSYw1Y1QLiBK8LPHauP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 23849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 323
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01F1uQzxXriMpdoJtUEcN2dG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "558aeb42-34db-4f61-9eae-fcdd458adb98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVejSYw1Y1QLiBK8LPHauP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 23849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 323
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

_source line 12 · 2026-05-21T12:53:19.752Z_

<details><summary>↩ Tool result · `toolu_01F1uQzxXriMpdoJtUEcN2dG`</summary>

````text
1	# Dual-Critic Cross-Environment Effectiveness: Literature Survey
2	
3	**Date:** 2026-05-21
4	**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. Walker: full prevention (NVE≤1.4). Cheetah: partial mitigation (peak NVE 1.8, 40× compression vs baseline NVE 70.64). Key finding: v1 ≈ v2 (critic difference < 0.2), suggesting implicit value regularization rather than pessimistic estimation.
5	
6	---
7	
8	## 1. Environment-Dependent Effectiveness of Bias Correction
9	
10	### 1.1 Turcato et al. 2024 — Bias Preference is Environment-Dependent
11	
12	- **Title:** Exploiting Estimation Bias in Clipped Double Q-Learning for Continuous Control Reinforcement Learning Tasks
13	- **Authors:** Turcato N., Sinigaglia A., Dalla Libera A., Carli R., Susto G.A.
14	- **Year:** 2024
15	- **Venue:** arXiv:2402.09078
16	- **Core finding:** "None of the considered update strategies performs the best among all the considered environments." Specifically:
17	  - **Walker, Ant, Hopper, Humanoid:** TD3's underestimation bias performs best
18	  - **Swimmer, Reacher:** Overestimation bias performs best
19	  - Sufficient condition for overestimation advantage: "noisy regions of the MDP correlate with the high reward"
20	- **Relevance to our finding:** Walker's reward landscape (stand + walk forward, 2 joints) favors underestimation → dual-critic's conservative bias fully prevents CIVO. Cheetah Run's reward landscape (forward speed, 6 joints, more complex coordination) may have regions where underestimation is suboptimal, explaining partial rather than full prevention.
21	
22	### 1.2 Nauman et al. 2024 — Regularization Effectiveness is Task-Dependent (Already in map: nauman2024bitter)
23	
24	- **Title:** Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning
25	- **Authors:** Nauman M., Bortkiewicz M., Miłoś P., Trzcinski T., Ostaszewski M., Cygan M.
26	- **Year:** 2024
27	- **Venue:** ICML 2024
28	- **Core finding:** Tested 60+ off-policy agents with various regularization techniques across 14 tasks. "The effectiveness of a specific regularization setup varies with the task, [though] certain combinations consistently demonstrate robust and superior performance."
29	- **Relevance:** Directly confirms that dual-critic (a form of value regularization) working fully on Walker but partially on Cheetah is a *predicted* consequence of task-dependent regularization effectiveness, not an anomaly.
30	
31	### 1.3 Heess et al. 2015 — Gradient-Through-Dynamics is Task-Dependent (Already in map: heess2015svg)
32	
33	- **Title:** Learning Continuous Control Policies by Stochastic Value Gradients
34	- **Authors:** Heess N., Wayne G., Silver D., Lillicrap T., Erez T., Tassa Y.
35	- **Year:** 2015
36	- **Venue:** NeurIPS
37	- **Core finding:** SVG(0) (no model gradient) works for simple tasks; SVG(1+) needed for complex tasks but SVG(∞) degrades. Simple tasks tolerate aggressive gradient interventions; complex tasks need finer control.
38	- **Relevance:** Walker (simple) tolerates the implicit regularization from dual critics fully; Cheetah (complex) needs more nuanced intervention — consistent with SVG gradient hierarchy.
39	
40	---
41	
42	## 2. The v1 ≈ v2 Phenomenon: Why Two Critics Converge
43	
44	### 2.1 Theoretical Basis — Shared Target Drives Convergence
45	
46	In TD3/SAC dual-critic setups, both critics are trained against `min(Q1_target, Q2_target)`. Since they share identical Bellman targets, gradient descent drives both networks toward the same function. The "independence" that enables pessimism exists only at initialization and early training. Over time, both networks converge because:
47	- Same data distribution (same replay buffer)
48	- Same target values (min of two target networks)
49	- Same loss function (MSE on Bellman residual)
50	
51	**No paper found that specifically studies the "v1 ≈ v2 convergence" phenomenon.** This is a gap in the literature. The closest discussions are:
52	
53	### 2.2 Bhatt et al. 2024 — CrossQ: Implicit Regularization Without Pessimism
54	
55	- **Title:** CrossQ: Batch Normalization in Deep Reinforcement Learning for Greater Sample Efficiency and Simplicity
56	- **Authors:** Bhatt A., et al.
57	- **Year:** 2024 (originally 2019, major revision 2024)
58	- **Venue:** ICLR 2024
59	- **Core finding:** Batch normalization in critic networks achieves state-of-the-art without target networks or ensembles. "High performance may be attributed to implicitly reducing bias as a side effect of design choices." CrossQ drops from 2 critics to 1 with BN and achieves better results.
60	- **Relevance:** Demonstrates that the primary mechanism of twin critics may be *implicit regularization through architectural choices* (shared BN statistics, parameter coupling), not pessimistic estimation. Supports our v1 ≈ v2 finding: the min operation doesn't create pessimism when critics agree; instead, the act of training two networks provides regularization.
61	
62	### 2.3 Lyu et al. 2022 — DARC: Double Actors Provide the Real Benefit
63	
64	- **Title:** Efficient Continuous Control with Double Actors and Regularized Critics
65	- **Authors:** Lyu J., Ma X., Yan J., Li X.
66	- **Year:** 2022
67	- **Venue:** AAAI 2022 (arXiv:2106.03050)
68	- **Core finding:** Double actors (not double critics) are the key to mitigating both over- and underestimation. Critic regularization (not min operation) provides stability.
69	- **Relevance:** Suggests the min-of-two mechanism is not the most important component — the regularization from maintaining multiple estimators is.
70	
71	---
72	
73	## 3. Implicit Regularization Mechanisms in Value Estimation
74	
75	### 3.1 Lyle et al. 2024 — Normalization as Implicit Overestimation Control (Already in map: lyle2024normalization)
76	
77	- **Title:** Normalization and Effective Learning Rates in Reinforcement Learning
78	- **Authors:** Lyle C., et al.
79	- **Year:** 2024
80	- **Venue:** NeurIPS 2024
81	- **Core finding:** Normalization layers combat overestimation but cause effective LR decay via parameter norm growth. Different initializations → different norm growth trajectories → different overestimation damping.
82	- **Relevance:** Dual-critic training introduces additional normalization-like effects through redundant parameterization. The v1 ≈ v2 convergence may itself act as an implicit constraint that damps value growth.
83	
84	### 3.2 Kumar et al. 2022 — DR3: TD Learning Has Implicit Regularization (Already in map: kumar2022dr3)
85	
86	- **Title:** DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization
87	- **Authors:** Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.
88	- **Year:** 2022
89	- **Venue:** ICLR 2022
90	- **Core finding:** Implicit regularization from TD learning favors degenerate feature aliasing. Two critics trained on the same targets undergo similar feature collapse, explaining v1 ≈ v2.
91	- **Relevance:** The convergence of v1 and v2 may be a manifestation of DR3's feature aliasing — both networks learn the same degenerate representation, which incidentally bounds overestimation.
92	
93	### 3.3 Layer Normalization > Explicit Anti-Overestimation (from Nauman et al. 2024)
94	
95	- **Core finding:** "Layer normalisation is more effective in reducing overestimation than techniques specifically designed for mitigating Q-value overestimation in critic networks."
96	- **Relevance:** Network regularization (implicit) can be more powerful than algorithmic pessimism (explicit min-of-two). Our dual-critic may be working primarily through its regularization effect on the shared representation.
97	
98	---
99	
100	## 4. Compounding Error and Critic Architecture in Model-Based RL
101	
102	### 4.1 Palenicek et al. 2025 — Even Oracle Models Show Diminishing Returns (Already in map: palenicek2025diminishing)
103	
104	- **Title:** Diminishing Return of Value Expansion Methods
105	- **Authors:** Palenicek D., et al.
106	- **Year:** 2025
107	- **Venue:** RLC 2025 (arXiv:2412.20537)
108	- **Core finding:** Longer rollout horizons have diminishing returns even with oracle dynamics. The bottleneck is value estimation, not model accuracy.
109	- **Relevance:** Dual-critic's partial effectiveness in Cheetah is consistent with the value estimation bottleneck being harder to resolve in complex environments, even when the critic architecture is improved.
110	
111	### 4.2 Barkley & Fridovich-Keil 2025 — Environment-Dependent MBRL Failures (Already in map: barkley2024stealing; updated version: 2510.01457)
112	
113	- **Title:** A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in Model-Based Policy Optimization
114	- **Authors:** Barkley B., Fridovich-Keil D.
115	- **Year:** 2025
116	- **Venue:** arXiv:2510.01457
117	- **Core finding:** MBPO succeeds on Gym but fails on 7/15 DMC tasks. Root causes: scale mismatch between dynamics and reward targets suppresses reward learning → critic underestimation. Benchmark-specific assumptions get baked into algorithm design.
118	- **Relevance:** Environment-dependent failure of model-based methods is a documented and general phenomenon. Our dual-critic's differential effectiveness across Walker/Cheetah follows the same pattern.
119	
120	### 4.3 Ma et al. 2024 — Policy Gradients Scale Exponentially with Horizon (Already in map: ma2024awm)
121	
122	- **Title:** Do Transformer World Models Give Better Policy Gradients?
123	- **Authors:** Ma M., Ni T., Gehring C., D'Oro P., Bacon P.-L.
124	- **Year:** 2024
125	- **Venue:** ICML 2024
126	- **Core finding:** Policy gradients through standard world models scale exponentially with horizon. Environments differ in how much they rely on long-range credit assignment.
127	- **Relevance:** Cheetah requires deeper temporal credit assignment than Walker. Dual-critic regularization may be insufficient to tame exponentially growing gradient issues in Cheetah's longer credit assignment chain.
128	
129	### 4.4 Chen et al. 2021 — REDQ: Ensemble Size Controls Pessimism (Already in map: chen2021redq)
130	
131	- **Title:** Randomized Ensembled Double Q-Learning
132	- **Authors:** Chen X., Wang C., Zhou Z., Ross K.
133	- **Year:** 2021
134	- **Venue:** ICLR 2021
135	- **Core finding:** Ensemble of N Q-functions with in-target minimization over M < N random subset controls overestimation. Larger M/N → more pessimism. N=2, M=2 (TD3) is the minimum configuration.
136	- **Relevance:** With only 2 critics (TD3-style), the pessimism budget is minimal. If v1 ≈ v2, the effective pessimism is nearly zero. REDQ suggests N > 2 might be needed for Cheetah. Our finding that 2 critics provide regularization rather than pessimism is consistent with REDQ's framework.
137	
138	---
139	
140	## 5. Synthesis: Explaining Prevention vs. Mitigation
141	
142	### Why Full Prevention on Walker
143	
144	1. **Simple reward landscape** (2 joints, stand + walk) → overestimation manifests in a lower-dimensional value function space
145	2. **Dual-critic implicit regularization** (redundant parameterization, shared target convergence) is sufficient to constrain value growth in this simpler space
146	3. **Short credit assignment chain** → regularization doesn't need to propagate through many imagination steps
147	4. **Walker favors underestimation** (Turcato et al. 2024) → even the tiny residual pessimism from min(v1, v2) when v1 ≈ v2 helps
148	
149	### Why Only Mitigation on Cheetah
150	
151	1. **Complex reward landscape** (6 joints, forward speed) → value function has more degrees of freedom for overestimation
152	2. **Implicit regularization from 2 critics is insufficient** for this higher-dimensional problem; need stronger intervention (REDQ-style larger ensembles, or explicit pessimism)
153	3. **Longer credit assignment chain** (Ma et al. 2024) → regularization effect attenuates across more imagination steps
154	4. **v1 ≈ v2 means no effective pessimism** → the 40× compression vs baseline is entirely from regularization, which has limits in complex environments
155	5. **Task-dependent regularization effectiveness** is a general phenomenon (Nauman et al. 2024), not specific to our method
156	
157	### The Implicit Regularization Hypothesis
158	
159	The v1 ≈ v2 finding (< 0.2 difference) is the key evidence. If dual-critic worked via pessimism, we would expect persistent v1 ≠ v2 gaps. Instead, the mechanism appears to be:
160	
161	1. **Redundant parameterization** → training two networks on the same target creates mutual regularization through gradient noise decorrelation
162	2. **Shared target coupling** → the min operation creates a self-consistent training signal that prevents either network from diverging
163	3. **Implicit capacity constraint** → maintaining two networks that must agree constrains the representational capacity available for fitting overestimated values
164	4. **This is analogous to** CrossQ's finding that architectural regularization (BN) outperforms algorithmic pessimism (min-of-two)
165	
166	---
167	
168	## 6. Key Papers for Citation
169	
170	### Must-cite (new, not in literature map)
171	
172	| Paper | Citation Key | Why |
173	|-------|-------------|-----|
174	| Turcato et al. 2024 | turcato2024exploiting | Environment-dependent bias preference — direct explanation for Walker vs Cheetah |
175	| Bhatt et al. 2024 CrossQ | bhatt2024crossq | Implicit regularization > explicit pessimism — supports v1≈v2 mechanism |
176	| Lyu et al. 2022 DARC | lyu2022darc | Double actors + regularized critics — the regularization view of twin networks |
177	
178	### Should-cite (already in literature map)
179	
180	| Paper | Citation Key | Why |
181	|-------|-------------|-----|
182	| Nauman et al. 2024 | nauman2024bitter | Task-dependent regularization effectiveness (60+ agents, 14 tasks) |
183	| Palenicek et al. 2025 | palenicek2025diminishing | Value estimation is the bottleneck, not model quality |
184	| Ma et al. 2024 | ma2024awm | Gradient scaling explains Cheetah's resistance to regularization |
185	| Chen et al. 2021 REDQ | chen2021redq | N=2 is minimal ensemble; larger N may be needed |
186	| Kumar et al. 2022 DR3 | kumar2022dr3 | Feature aliasing explains v1≈v2 convergence |
187	| Lyle et al. 2024 | lyle2024normalization | Normalization as implicit overestimation control |
188	
189	---
190	
191	## 7. Literature Gaps Identified
192	
193	1. **No paper specifically studies the v1 ≈ v2 convergence phenomenon** in dual-critic RL. This is an original observation worth highlighting.
194	2. **No paper applies dual-critic to world-model imagination-based training** (Dreamer family). All dual-critic analysis is in model-free or Dyna-style MBRL.
195	3. **No paper provides a formal theory for when implicit regularization from twin critics is sufficient vs. insufficient** across environments.
196	4. **The implicit regularization interpretation of twin critics** (as opposed to pessimistic estimation) lacks a dedicated theoretical treatment.
197	
198	---
199	
200	## 8. Papers to Add to literature_map.yaml
201	
202	```yaml
203	- paper_id: turcato2024exploiting
204	  title: "Exploiting Estimation Bias in Clipped Double Q-Learning for Continuous Control"
205	  authors: [Turcato N., Sinigaglia A., Dalla Libera A., Carli R., Susto G.A.]
206	  year: 2024
207	  venue: "arXiv:2402.09078"
208	  category: evaluation
209	  role: "Shows bias preference (under- vs over-estimation) is environment-dependent; Walker/Ant favor underestimation, Swimmer/Reacher favor overestimation. Directly explains our dual-critic's differential effectiveness across Walker (full prevention) and Cheetah (partial mitigation)."
210	  relevance_score: 5
211	
212	- paper_id: bhatt2024crossq
213	  title: "CrossQ: Batch Normalization in Deep Reinforcement Learning for Greater Sample Efficiency and Simplicity"
214	  authors: [Bhatt A., et al.]
215	  year: 2024
216	  venue: "ICLR 2024"
217	  category: method-component
218	  role: "Demonstrates that implicit regularization via batch normalization in critics outperforms explicit pessimism (min-of-two); drops from 2 critics to 1 with BN and achieves better results. Supports our v1≈v2 finding: the mechanism is regularization, not pessimism."
219	  relevance_score: 4
220	
221	- paper_id: lyu2022darc
222	  title: "Efficient Continuous Control with Double Actors and Regularized Critics"
223	  authors: [Lyu J., Ma X., Yan J., Li X.]
224	  year: 2022
225	  venue: "AAAI 2022 (arXiv:2106.03050)"
226	  category: method-component
227	  role: "DARC — shows double actors (not double critics) mitigate both over- and underestimation; critic regularization provides stability. Supports the interpretation that min-of-two critics works primarily as regularization."
228	  relevance_score: 3
229	
230	- paper_id: barkley2025forensic
231	  title: "A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in MBPO"
232	  authors: [Barkley B., Fridovich-Keil D.]
233	  year: 2025
234	  venue: "arXiv:2510.01457"
235	  category: evaluation
236	  role: "Extended version of barkley2024stealing. Shows MBPO fails on 7/15 DMC tasks due to scale mismatch between dynamics/reward targets. Environment-dependent MBRL failure is systematic, not anomalous."
237	  relevance_score: 4
238	```
239	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "2be64869-ded4-468b-b3cf-2e0de325b208",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
      "content": "# Dual-Critic Cross-Environment Effectiveness: Literature Survey\n\n**Date:** 2026-05-21\n**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. Walker: full prevention (NVE≤1.4). Cheetah: partial mitigation (peak NVE 1.8, 40× compression vs baseline NVE 70.64). Key finding: v1 ≈ v2 (critic difference < 0.2), suggesting implicit value regularization rather than pessimistic estimation.\n\n---\n\n## 1. Environment-Dependent Effectiveness of Bias Correction\n\n### 1.1 Turcato et al. 2024 — Bias Preference is Environment-Dependent\n\n- **Title:** Exploiting Estimation Bias in Clipped Double Q-Learning for Continuous Control Reinforcement Learning Tasks\n- **Authors:** Turcato N., Sinigaglia A., Dalla Libera A., Carli R., Susto G.A.\n- **Year:** 2024\n- **Venue:** arXiv:2402.09078\n- **Core finding:** \"None of the considered update strategies performs the best among all the considered environments.\" Specifically:\n  - **Walker, Ant, Hopper, Humanoid:** TD3's underestimation bias performs best\n  - **Swimmer, Reacher:** Overestimation bias performs best\n  - Sufficient condition for overestimation advantage: \"noisy regions of the MDP correlate with the high reward\"\n- **Relevance to our finding:** Walker's reward landscape (stand + walk forward, 2 joints) favors underestimation → dual-critic's conservative bias fully prevents CIVO. Cheetah Run's reward landscape (forward speed, 6 joints, more complex coordination) may have regions where underestimation is suboptimal, explaining partial rather than full prevention.\n\n### 1.2 Nauman et al. 2024 — Regularization Effectiveness is Task-Dependent (Already in map: nauman2024bitter)\n\n- **Title:** Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning\n- **Authors:** Nauman M., Bortkiewicz M., Miłoś P., Trzcinski T., Ostaszewski M., Cygan M.\n- **Year:** 2024\n- **Venue:** ICML 2024\n- **Core finding:** Tested 60+ off-policy agents with various regularization techniques across 14 tasks. \"The effectiveness of a specific regularization setup varies with the task, [though] certain combinations consistently demonstrate robust and superior performance.\"\n- **Relevance:** Directly confirms that dual-critic (a form of value regularization) working fully on Walker but partially on Cheetah is a *predicted* consequence of task-dependent regularization effectiveness, not an anomaly.\n\n### 1.3 Heess et al. 2015 — Gradient-Through-Dynamics is Task-Dependent (Already in map: heess2015svg)\n\n- **Title:** Learning Continuous Control Policies by Stochastic Value Gradients\n- **Authors:** Heess N., Wayne G., Silver D., Lillicrap T., Erez T., Tassa Y.\n- **Year:** 2015\n- **Venue:** NeurIPS\n- **Core finding:** SVG(0) (no model gradient) works for simple tasks; SVG(1+) needed for complex tasks but SVG(∞) degrades. Simple tasks tolerate aggressive gradient interventions; complex tasks need finer control.\n- **Relevance:** Walker (simple) tolerates the implicit regularization from dual critics fully; Cheetah (complex) needs more nuanced intervention — consistent with SVG gradient hierarchy.\n\n---\n\n## 2. The v1 ≈ v2 Phenomenon: Why Two Critics Converge\n\n### 2.1 Theoretical Basis — Shared Target Drives Convergence\n\nIn TD3/SAC dual-critic setups, both critics are trained against `min(Q1_target, Q2_target)`. Since they share identical Bellman targets, gradient descent drives both networks toward the same function. The \"independence\" that enables pessimism exists only at initialization and early training. Over time, both networks converge because:\n- Same data distribution (same replay buffer)\n- Same target values (min of two target networks)\n- Same loss function (MSE on Bellman residual)\n\n**No paper found that specifically studies the \"v1 ≈ v2 convergence\" phenomenon.** This is a gap in the literature. The closest discussions are:\n\n### 2.2 Bhatt et al. 2024 — CrossQ: Implicit Regularization Without Pessimism\n\n- **Title:** CrossQ: Batch Normalization in Deep Reinforcement Learning for Greater Sample Efficiency and Simplicity\n- **Authors:** Bhatt A., et al.\n- **Year:** 2024 (originally 2019, major revision 2024)\n- **Venue:** ICLR 2024\n- **Core finding:** Batch normalization in critic networks achieves state-of-the-art without target networks or ensembles. \"High performance may be attributed to implicitly reducing bias as a side effect of design choices.\" CrossQ drops from 2 critics to 1 with BN and achieves better results.\n- **Relevance:** Demonstrates that the primary mechanism of twin critics may be *implicit regularization through architectural choices* (shared BN statistics, parameter coupling), not pessimistic estimation. Supports our v1 ≈ v2 finding: the min operation doesn't create pessimism when critics agree; instead, the act of training two networks provides regularization.\n\n### 2.3 Lyu et al. 2022 — DARC: Double Actors Provide the Real Benefit\n\n- **Title:** Efficient Continuous Control with Double Actors and Regularized Critics\n- **Authors:** Lyu J., Ma X., Yan J., Li X.\n- **Year:** 2022\n- **Venue:** AAAI 2022 (arXiv:2106.03050)\n- **Core finding:** Double actors (not double critics) are the key to mitigating both over- and underestimation. Critic regularization (not min operation) provides stability.\n- **Relevance:** Suggests the min-of-two mechanism is not the most important component — the regularization from maintaining multiple estimators is.\n\n---\n\n## 3. Implicit Regularization Mechanisms in Value Estimation\n\n### 3.1 Lyle et al. 2024 — Normalization as Implicit Overestimation Control (Already in map: lyle2024normalization)\n\n- **Title:** Normalization and Effective Learning Rates in Reinforcement Learning\n- **Authors:** Lyle C., et al.\n- **Year:** 2024\n- **Venue:** NeurIPS 2024\n- **Core finding:** Normalization layers combat overestimation but cause effective LR decay via parameter norm growth. Different initializations → different norm growth trajectories → different overestimation damping.\n- **Relevance:** Dual-critic training introduces additional normalization-like effects through redundant parameterization. The v1 ≈ v2 convergence may itself act as an implicit constraint that damps value growth.\n\n### 3.2 Kumar et al. 2022 — DR3: TD Learning Has Implicit Regularization (Already in map: kumar2022dr3)\n\n- **Title:** DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization\n- **Authors:** Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.\n- **Year:** 2022\n- **Venue:** ICLR 2022\n- **Core finding:** Implicit regularization from TD learning favors degenerate feature aliasing. Two critics trained on the same targets undergo similar feature collapse, explaining v1 ≈ v2.\n- **Relevance:** The convergence of v1 and v2 may be a manifestation of DR3's feature aliasing — both networks learn the same degenerate representation, which incidentally bounds overestimation.\n\n### 3.3 Layer Normalization > Explicit Anti-Overestimation (from Nauman et al. 2024)\n\n- **Core finding:** \"Layer normalisation is more effective in reducing overestimation than techniques specifically designed for mitigating Q-value overestimation in critic networks.\"\n- **Relevance:** Network regularization (implicit) can be more powerful than algorithmic pessimism (explicit min-of-two). Our dual-critic may be working primarily through its regularization effect on the shared representation.\n\n---\n\n## 4. Compounding Error and Critic Architecture in Model-Based RL\n\n### 4.1 Palenicek et al. 2025 — Even Oracle Models Show Diminishing Returns (Already in map: palenicek2025diminishing)\n\n- **Title:** Diminishing Return of Value Expansion Methods\n- **Authors:** Palenicek D., et al.\n- **Year:** 2025\n- **Venue:** RLC 2025 (arXiv:2412.20537)\n- **Core finding:** Longer rollout horizons have diminishing returns even with oracle dynamics. The bottleneck is value estimation, not model accuracy.\n- **Relevance:** Dual-critic's partial effectiveness in Cheetah is consistent with the value estimation bottleneck being harder to resolve in complex environments, even when the critic architecture is improved.\n\n### 4.2 Barkley & Fridovich-Keil 2025 — Environment-Dependent MBRL Failures (Already in map: barkley2024stealing; updated version: 2510.01457)\n\n- **Title:** A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in Model-Based Policy Optimization\n- **Authors:** Barkley B., Fridovich-Keil D.\n- **Year:** 2025\n- **Venue:** arXiv:2510.01457\n- **Core finding:** MBPO succeeds on Gym but fails on 7/15 DMC tasks. Root causes: scale mismatch between dynamics and reward targets suppresses reward learning → critic underestimation. Benchmark-specific assumptions get baked into algorithm design.\n- **Relevance:** Environment-dependent failure of model-based methods is a documented and general phenomenon. Our dual-critic's differential effectiveness across Walker/Cheetah follows the same pattern.\n\n### 4.3 Ma et al. 2024 — Policy Gradients Scale Exponentially with Horizon (Already in map: ma2024awm)\n\n- **Title:** Do Transformer World Models Give Better Policy Gradients?\n- **Authors:** Ma M., Ni T., Gehring C., D'Oro P., Bacon P.-L.\n- **Year:** 2024\n- **Venue:** ICML 2024\n- **Core finding:** Policy gradients through standard world models scale exponentially with horizon. Environments differ in how much they rely on long-range credit assignment.\n- **Relevance:** Cheetah requires deeper temporal credit assignment than Walker. Dual-critic regularization may be insufficient to tame exponentially growing gradient issues in Cheetah's longer credit assignment chain.\n\n### 4.4 Chen et al. 2021 — REDQ: Ensemble Size Controls Pessimism (Already in map: chen2021redq)\n\n- **Title:** Randomized Ensembled Double Q-Learning\n- **Authors:** Chen X., Wang C., Zhou Z., Ross K.\n- **Year:** 2021\n- **Venue:** ICLR 2021\n- **Core finding:** Ensemble of N Q-functions with in-target minimization over M < N random subset controls overestimation. Larger M/N → more pessimism. N=2, M=2 (TD3) is the minimum configuration.\n- **Relevance:** With only 2 critics (TD3-style), the pessimism budget is minimal. If v1 ≈ v2, the effective pessimism is nearly zero. REDQ suggests N > 2 might be needed for Cheetah. Our finding that 2 critics provide regularization rather than pessimism is consistent with REDQ's framework.\n\n---\n\n## 5. Synthesis: Explaining Prevention vs. Mitigation\n\n### Why Full Prevention on Walker\n\n1. **Simple reward landscape** (2 joints, stand + walk) → overestimation manifests in a lower-dimensional value function space\n2. **Dual-critic implicit regularization** (redundant parameterization, shared target convergence) is sufficient to constrain value growth in this simpler space\n3. **Short credit assignment chain** → regularization doesn't need to propagate through many imagination steps\n4. **Walker favors underestimation** (Turcato et al. 2024) → even the tiny residual pessimism from min(v1, v2) when v1 ≈ v2 helps\n\n### Why Only Mitigation on Cheetah\n\n1. **Complex reward landscape** (6 joints, forward speed) → value function has more degrees of freedom for overestimation\n2. **Implicit regularization from 2 critics is insufficient** for this higher-dimensional problem; need stronger intervention (REDQ-style larger ensembles, or explicit pessimism)\n3. **Longer credit assignment chain** (Ma et al. 2024) → regularization effect attenuates across more imagination steps\n4. **v1 ≈ v2 means no effective pessimism** → the 40× compression vs baseline is entirely from regularization, which has limits in complex environments\n5. **Task-dependent regularization effectiveness** is a general phenomenon (Nauman et al. 2024), not specific to our method\n\n### The Implicit Regularization Hypothesis\n\nThe v1 ≈ v2 finding (< 0.2 difference) is the key evidence. If dual-critic worked via pessimism, we would expect persistent v1 ≠ v2 gaps. Instead, the mechanism appears to be:\n\n1. **Redundant parameterization** → training two networks on the same target creates mutual regularization through gradient noise decorrelation\n2. **Shared target coupling** → the min operation creates a self-consistent training signal that prevents either network from diverging\n3. **Implicit capacity constraint** → maintaining two networks that must agree constrains the representational capacity available for fitting overestimated values\n4. **This is analogous to** CrossQ's finding that architectural regularization (BN) outperforms algorithmic pessimism (min-of-two)\n\n---\n\n## 6. Key Papers for Citation\n\n### Must-cite (new, not in literature map)\n\n| Paper | Citation Key | Why |\n|-------|-------------|-----|\n| Turcato et al. 2024 | turcato2024exploiting | Environment-dependent bias preference — direct explanation for Walker vs Cheetah |\n| Bhatt et al. 2024 CrossQ | bhatt2024crossq | Implicit regularization > explicit pessimism — supports v1≈v2 mechanism |\n| Lyu et al. 2022 DARC | lyu2022darc | Double actors + regularized critics — the regularization view of twin networks |\n\n### Should-cite (already in literature map)\n\n| Paper | Citation Key | Why |\n|-------|-------------|-----|\n| Nauman et al. 2024 | nauman2024bitter | Task-dependent regularization effectiveness (60+ agents, 14 tasks) |\n| Palenicek et al. 2025 | palenicek2025diminishing | Value estimation is the bottleneck, not model quality |\n| Ma et al. 2024 | ma2024awm | Gradient scaling explains Cheetah's resistance to regularization |\n| Chen et al. 2021 REDQ | chen2021redq | N=2 is minimal ensemble; larger N may be needed |\n| Kumar et al. 2022 DR3 | kumar2022dr3 | Feature aliasing explains v1≈v2 convergence |\n| Lyle et al. 2024 | lyle2024normalization | Normalization as implicit overestimation control |\n\n---\n\n## 7. Literature Gaps Identified\n\n1. **No paper specifically studies the v1 ≈ v2 convergence phenomenon** in dual-critic RL. This is an original observation worth highlighting.\n2. **No paper applies dual-critic to world-model imagination-based training** (Dreamer family). All dual-critic analysis is in model-free or Dyna-style MBRL.\n3. **No paper provides a formal theory for when implicit regularization from twin critics is sufficient vs. insufficient** across environments.\n4. **The implicit regularization interpretation of twin critics** (as opposed to pessimistic estimation) lacks a dedicated theoretical treatment.\n\n---\n\n## 8. Papers to Add to literature_map.yaml\n\n```yaml\n- paper_id: turcato2024exploiting\n  title: \"Exploiting Estimation Bias in Clipped Double Q-Learning for Continuous Control\"\n  authors: [Turcato N., Sinigaglia A., Dalla Libera A., Carli R., Susto G.A.]\n  year: 2024\n  venue: \"arXiv:2402.09078\"\n  category: evaluation\n  role: \"Shows bias preference (under- vs over-estimation) is environment-dependent; Walker/Ant favor underestimation, Swimmer/Reacher favor overestimation. Directly explains our dual-critic's differential effectiveness across Walker (full prevention) and Cheetah (partial mitigation).\"\n  relevance_score: 5\n\n- paper_id: bhatt2024crossq\n  title: \"CrossQ: Batch Normalization in Deep Reinforcement Learning for Greater Sample Efficiency and Simplicity\"\n  authors: [Bhatt A., et al.]\n  year: 2024\n  venue: \"ICLR 2024\"\n  category: method-component\n  role: \"Demonstrates that implicit regularization via batch normalization in critics outperforms explicit pessimism (min-of-two); drops from 2 critics to 1 with BN and achieves better results. Supports our v1≈v2 finding: the mechanism is regularization, not pessimism.\"\n  relevance_score: 4\n\n- paper_id: lyu2022darc\n  title: \"Efficient Continuous Control with Double Actors and Regularized Critics\"\n  authors: [Lyu J., Ma X., Yan J., Li X.]\n  year: 2022\n  venue: \"AAAI 2022 (arXiv:2106.03050)\"\n  category: method-component\n  role: \"DARC — shows double actors (not double critics) mitigate both over- and underestimation; critic regularization provides stability. Supports the interpretation that min-of-two critics works primarily as regularization.\"\n  relevance_score: 3\n\n- paper_id: barkley2025forensic\n  title: \"A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in MBPO\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2025\n  venue: \"arXiv:2510.01457\"\n  category: evaluation\n  role: \"Extended version of barkley2024stealing. Shows MBPO fails on 7/15 DMC tasks due to scale mismatch between dynamics/reward targets. Environment-dependent MBRL failure is systematic, not anomalous.\"\n  relevance_score: 4\n```\n",
      "numLines": 239,
      "startLine": 1,
      "totalLines": 239
    }
  }
}
````

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full file. I need to update Section 5 (lines 140-165) to reflect the new findings from the 2×2 factorial experiment. The key changes:

1. Title: "Prevention vs. Mitigation" → "Synergistic Prevention"
2. The old narrative was: Walker = full prevention, Cheetah = partial mitigation, and the "Implicit Regularization Hypothesis"
3. The new narrative based on 2×2 factorial:
   - Single + normal (~1.2M): CIVO ✓ (baseline)
   - Single + scaled (~2.9M, exp_033): CIVO ✓ (NVE 4.7) → capacity alone doesn't help
   - Dual + narrow (~1.05M, exp_035): CIVO ✓ (NVE 2.75) → min operation alone doesn't help
   - Dual + scaled (~2.4M, exp_032): CIVO ✗ (NVE < 1.5) → min + capacity together works

The key insight is that neither the min operation nor increased capacity alone prevents the pessimism effect—they only work synergistically, which is why exp_035 shows v1≈v2 with no pessimism suppression despite the narrow architecture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "608edee0-56e2-4f40-84c3-96e7576b4d3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XVqPp2eF5FcGtoZ8ZcztT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5363,
      "cache_read_input_tokens": 24172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5363
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

I have the file. Now I'll update Section 5 and the context header to reflect the 2×2 factorial results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "7dc98c13-e22d-4150-a7b4-9a1793e4460b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XVqPp2eF5FcGtoZ8ZcztT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5363,
      "cache_read_input_tokens": 24172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5363
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

<details open><summary>🔧 Tool call — Edit · `toolu_01M99pGXDX8nomEoQp9dbdcd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
  "old_string": "**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. Walker: full prevention (NVE≤1.4). Cheetah: partial mitigation (peak NVE 1.8, 40× compression vs baseline NVE 70.64). Key finding: v1 ≈ v2 (critic difference < 0.2), suggesting implicit value regularization rather than pessimistic estimation.",
  "new_string": "**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. 2×2 factorial (dual/single × narrow/scaled) reveals that neither the min operation alone nor increased capacity alone prevents CIVO on Walker; only their combination succeeds (exp_032, NVE < 1.5). Key finding: v1 ≈ v2 (critic difference < 0.2), confirming implicit regularization rather than pessimistic estimation — but this regularization requires sufficient critic capacity to be effective."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "bca87fff-09fd-4f43-9b59-e0fc1a2f3d22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XVqPp2eF5FcGtoZ8ZcztT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5363,
      "cache_read_input_tokens": 24172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5363
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

_source line 16 · 2026-05-21T12:53:40.366Z_

<details><summary>↩ Tool result · `toolu_01M99pGXDX8nomEoQp9dbdcd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "f16d9049-5ed0-42d9-947c-30bdb459bd24",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
    "oldString": "**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. Walker: full prevention (NVE≤1.4). Cheetah: partial mitigation (peak NVE 1.8, 40× compression vs baseline NVE 70.64). Key finding: v1 ≈ v2 (critic difference < 0.2), suggesting implicit value regularization rather than pessimistic estimation.",
    "newString": "**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. 2×2 factorial (dual/single × narrow/scaled) reveals that neither the min operation alone nor increased capacity alone prevents CIVO on Walker; only their combination succeeds (exp_032, NVE < 1.5). Key finding: v1 ≈ v2 (critic difference < 0.2), confirming implicit regularization rather than pessimistic estimation — but this regularization requires sufficient critic capacity to be effective.",
    "originalFile": "# Dual-Critic Cross-Environment Effectiveness: Literature Survey\n\n**Date:** 2026-05-21\n**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. Walker: full prevention (NVE≤1.4). Cheetah: partial mitigation (peak NVE 1.8, 40× compression vs baseline NVE 70.64). Key finding: v1 ≈ v2 (critic difference < 0.2), suggesting implicit value regularization rather than pessimistic estimation.\n\n---\n\n## 1. Environment-Dependent Effectiveness of Bias Correction\n\n### 1.1 Turcato et al. 2024 — Bias Preference is Environment-Dependent\n\n- **Title:** Exploiting Estimation Bias in Clipped Double Q-Learning for Continuous Control Reinforcement Learning Tasks\n- **Authors:** Turcato N., Sinigaglia A., Dalla Libera A., Carli R., Susto G.A.\n- **Year:** 2024\n- **Venue:** arXiv:2402.09078\n- **Core finding:** \"None of the considered update strategies performs the best among all the considered environments.\" Specifically:\n  - **Walker, Ant, Hopper, Humanoid:** TD3's underestimation bias performs best\n  - **Swimmer, Reacher:** Overestimation bias performs best\n  - Sufficient condition for overestimation advantage: \"noisy regions of the MDP correlate with the high reward\"\n- **Relevance to our finding:** Walker's reward landscape (stand + walk forward, 2 joints) favors underestimation → dual-critic's conservative bias fully prevents CIVO. Cheetah Run's reward landscape (forward speed, 6 joints, more complex coordination) may have regions where underestimation is suboptimal, explaining partial rather than full prevention.\n\n### 1.2 Nauman et al. 2024 — Regularization Effectiveness is Task-Dependent (Already in map: nauman2024bitter)\n\n- **Title:** Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning\n- **Authors:** Nauman M., Bortkiewicz M., Miłoś P., Trzcinski T., Ostaszewski M., Cygan M.\n- **Year:** 2024\n- **Venue:** ICML 2024\n- **Core finding:** Tested 60+ off-policy agents with various regularization techniques across 14 tasks. \"The effectiveness of a specific regularization setup varies with the task, [though] certain combinations consistently demonstrate robust and superior performance.\"\n- **Relevance:** Directly confirms that dual-critic (a form of value regularization) working fully on Walker but partially on Cheetah is a *predicted* consequence of task-dependent regularization effectiveness, not an anomaly.\n\n### 1.3 Heess et al. 2015 — Gradient-Through-Dynamics is Task-Dependent (Already in map: heess2015svg)\n\n- **Title:** Learning Continuous Control Policies by Stochastic Value Gradients\n- **Authors:** Heess N., Wayne G., Silver D., Lillicrap T., Erez T., Tassa Y.\n- **Year:** 2015\n- **Venue:** NeurIPS\n- **Core finding:** SVG(0) (no model gradient) works for simple tasks; SVG(1+) needed for complex tasks but SVG(∞) degrades. Simple tasks tolerate aggressive gradient interventions; complex tasks need finer control.\n- **Relevance:** Walker (simple) tolerates the implicit regularization from dual critics fully; Cheetah (complex) needs more nuanced intervention — consistent with SVG gradient hierarchy.\n\n---\n\n## 2. The v1 ≈ v2 Phenomenon: Why Two Critics Converge\n\n### 2.1 Theoretical Basis — Shared Target Drives Convergence\n\nIn TD3/SAC dual-critic setups, both critics are trained against `min(Q1_target, Q2_target)`. Since they share identical Bellman targets, gradient descent drives both networks toward the same function. The \"independence\" that enables pessimism exists only at initialization and early training. Over time, both networks converge because:\n- Same data distribution (same replay buffer)\n- Same target values (min of two target networks)\n- Same loss function (MSE on Bellman residual)\n\n**No paper found that specifically studies the \"v1 ≈ v2 convergence\" phenomenon.** This is a gap in the literature. The closest discussions are:\n\n### 2.2 Bhatt et al. 2024 — CrossQ: Implicit Regularization Without Pessimism\n\n- **Title:** CrossQ: Batch Normalization in Deep Reinforcement Learning for Greater Sample Efficiency and Simplicity\n- **Authors:** Bhatt A., et al.\n- **Year:** 2024 (originally 2019, major revision 2024)\n- **Venue:** ICLR 2024\n- **Core finding:** Batch normalization in critic networks achieves state-of-the-art without target networks or ensembles. \"High performance may be attributed to implicitly reducing bias as a side effect of design choices.\" CrossQ drops from 2 critics to 1 with BN and achieves better results.\n- **Relevance:** Demonstrates that the primary mechanism of twin critics may be *implicit regularization through architectural choices* (shared BN statistics, parameter coupling), not pessimistic estimation. Supports our v1 ≈ v2 finding: the min operation doesn't create pessimism when critics agree; instead, the act of training two networks provides regularization.\n\n### 2.3 Lyu et al. 2022 — DARC: Double Actors Provide the Real Benefit\n\n- **Title:** Efficient Continuous Control with Double Actors and Regularized Critics\n- **Authors:** Lyu J., Ma X., Yan J., Li X.\n- **Year:** 2022\n- **Venue:** AAAI 2022 (arXiv:2106.03050)\n- **Core finding:** Double actors (not double critics) are the key to mitigating both over- and underestimation. Critic regularization (not min operation) provides stability.\n- **Relevance:** Suggests the min-of-two mechanism is not the most important component — the regularization from maintaining multiple estimators is.\n\n---\n\n## 3. Implicit Regularization Mechanisms in Value Estimation\n\n### 3.1 Lyle et al. 2024 — Normalization as Implicit Overestimation Control (Already in map: lyle2024normalization)\n\n- **Title:** Normalization and Effective Learning Rates in Reinforcement Learning\n- **Authors:** Lyle C., et al.\n- **Year:** 2024\n- **Venue:** NeurIPS 2024\n- **Core finding:** Normalization layers combat overestimation but cause effective LR decay via parameter norm growth. Different initializations → different norm growth trajectories → different overestimation damping.\n- **Relevance:** Dual-critic training introduces additional normalization-like effects through redundant parameterization. The v1 ≈ v2 convergence may itself act as an implicit constraint that damps value growth.\n\n### 3.2 Kumar et al. 2022 — DR3: TD Learning Has Implicit Regularization (Already in map: kumar2022dr3)\n\n- **Title:** DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization\n- **Authors:** Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.\n- **Year:** 2022\n- **Venue:** ICLR 2022\n- **Core finding:** Implicit regularization from TD learning favors degenerate feature aliasing. Two critics trained on the same targets undergo similar feature collapse, explaining v1 ≈ v2.\n- **Relevance:** The convergence of v1 and v2 may be a manifestation of DR3's feature aliasing — both networks learn the same degenerate representation, which incidentally bounds overestimation.\n\n### 3.3 Layer Normalization > Explicit Anti-Overestimation (from Nauman et al. 2024)\n\n- **Core finding:** \"Layer normalisation is more effective in reducing overestimation than techniques specifically designed for mitigating Q-value overestimation in critic networks.\"\n- **Relevance:** Network regularization (implicit) can be more powerful than algorithmic pessimism (explicit min-of-two). Our dual-critic may be working primarily through its regularization effect on the shared representation.\n\n---\n\n## 4. Compounding Error and Critic Architecture in Model-Based RL\n\n### 4.1 Palenicek et al. 2025 — Even Oracle Models Show Diminishing Returns (Already in map: palenicek2025diminishing)\n\n- **Title:** Diminishing Return of Value Expansion Methods\n- **Authors:** Palenicek D., et al.\n- **Year:** 2025\n- **Venue:** RLC 2025 (arXiv:2412.20537)\n- **Core finding:** Longer rollout horizons have diminishing returns even with oracle dynamics. The bottleneck is value estimation, not model accuracy.\n- **Relevance:** Dual-critic's partial effectiveness in Cheetah is consistent with the value estimation bottleneck being harder to resolve in complex environments, even when the critic architecture is improved.\n\n### 4.2 Barkley & Fridovich-Keil 2025 — Environment-Dependent MBRL Failures (Already in map: barkley2024stealing; updated version: 2510.01457)\n\n- **Title:** A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in Model-Based Policy Optimization\n- **Authors:** Barkley B., Fridovich-Keil D.\n- **Year:** 2025\n- **Venue:** arXiv:2510.01457\n- **Core finding:** MBPO succeeds on Gym but fails on 7/15 DMC tasks. Root causes: scale mismatch between dynamics and reward targets suppresses reward learning → critic underestimation. Benchmark-specific assumptions get baked into algorithm design.\n- **Relevance:** Environment-dependent failure of model-based methods is a documented and general phenomenon. Our dual-critic's differential effectiveness across Walker/Cheetah follows the same pattern.\n\n### 4.3 Ma et al. 2024 — Policy Gradients Scale Exponentially with Horizon (Already in map: ma2024awm)\n\n- **Title:** Do Transformer World Models Give Better Policy Gradients?\n- **Authors:** Ma M., Ni T., Gehring C., D'Oro P., Bacon P.-L.\n- **Year:** 2024\n- **Venue:** ICML 2024\n- **Core finding:** Policy gradients through standard world models scale exponentially with horizon. Environments differ in how much they rely on long-range credit assignment.\n- **Relevance:** Cheetah requires deeper temporal credit assignment than Walker. Dual-critic regularization may be insufficient to tame exponentially growing gradient issues in Cheetah's longer credit assignment chain.\n\n### 4.4 Chen et al. 2021 — REDQ: Ensemble Size Controls Pessimism (Already in map: chen2021redq)\n\n- **Title:** Randomized Ensembled Double Q-Learning\n- **Authors:** Chen X., Wang C., Zhou Z., Ross K.\n- **Year:** 2021\n- **Venue:** ICLR 2021\n- **Core finding:** Ensemble of N Q-functions with in-target minimization over M < N random subset controls overestimation. Larger M/N → more pessimism. N=2, M=2 (TD3) is the minimum configuration.\n- **Relevance:** With only 2 critics (TD3-style), the pessimism budget is minimal. If v1 ≈ v2, the effective pessimism is nearly zero. REDQ suggests N > 2 might be needed for Cheetah. Our finding that 2 critics provide regularization rather than pessimism is consistent with REDQ's framework.\n\n---\n\n## 5. Synthesis: Explaining Prevention vs. Mitigation\n\n### Why Full Prevention on Walker\n\n1. **Simple reward landscape** (2 joints, stand + walk) → overestimation manifests in a lower-dimensional value function space\n2. **Dual-critic implicit regularization** (redundant parameterization, shared target convergence) is sufficient to constrain value growth in this simpler space\n3. **Short credit assignment chain** → regularization doesn't need to propagate through many imagination steps\n4. **Walker favors underestimation** (Turcato et al. 2024) → even the tiny residual pessimism from min(v1, v2) when v1 ≈ v2 helps\n\n### Why Only Mitigation on Cheetah\n\n1. **Complex reward landscape** (6 joints, forward speed) → value function has more degrees of freedom for overestimation\n2. **Implicit regularization from 2 critics is insufficient** for this higher-dimensional problem; need stronger intervention (REDQ-style larger ensembles, or explicit pessimism)\n3. **Longer credit assignment chain** (Ma et al. 2024) → regularization effect attenuates across more imagination steps\n4. **v1 ≈ v2 means no effective pessimism** → the 40× compression vs baseline is entirely from regularization, which has limits in complex environments\n5. **Task-dependent regularization effectiveness** is a general phenomenon (Nauman et al. 2024), not specific to our method\n\n### The Implicit Regularization Hypothesis\n\nThe v1 ≈ v2 finding (< 0.2 difference) is the key evidence. If dual-critic worked via pessimism, we would expect persistent v1 ≠ v2 gaps. Instead, the mechanism appears to be:\n\n1. **Redundant parameterization** → training two networks on the same target creates mutual regularization through gradient noise decorrelation\n2. **Shared target coupling** → the min operation creates a self-consistent training signal that prevents either network from diverging\n3. **Implicit capacity constraint** → maintaining two networks that must agree constrains the representational capacity available for fitting overestimated values\n4. **This is analogous to** CrossQ's finding that architectural regularization (BN) outperforms algorithmic pessimism (min-of-two)\n\n---\n\n## 6. Key Papers for Citation\n\n### Must-cite (new, not in literature map)\n\n| Paper | Citation Key | Why |\n|-------|-------------|-----|\n| Turcato et al. 2024 | turcato2024exploiting | Environment-dependent bias preference — direct explanation for Walker vs Cheetah |\n| Bhatt et al. 2024 CrossQ | bhatt2024crossq | Implicit regularization > explicit pessimism — supports v1≈v2 mechanism |\n| Lyu et al. 2022 DARC | lyu2022darc | Double actors + regularized critics — the regularization view of twin networks |\n\n### Should-cite (already in literature map)\n\n| Paper | Citation Key | Why |\n|-------|-------------|-----|\n| Nauman et al. 2024 | nauman2024bitter | Task-dependent regularization effectiveness (60+ agents, 14 tasks) |\n| Palenicek et al. 2025 | palenicek2025diminishing | Value estimation is the bottleneck, not model quality |\n| Ma et al. 2024 | ma2024awm | Gradient scaling explains Cheetah's resistance to regularization |\n| Chen et al. 2021 REDQ | chen2021redq | N=2 is minimal ensemble; larger N may be needed |\n| Kumar et al. 2022 DR3 | kumar2022dr3 | Feature aliasing explains v1≈v2 convergence |\n| Lyle et al. 2024 | lyle2024normalization | Normalization as implicit overestimation control |\n\n---\n\n## 7. Literature Gaps Identified\n\n1. **No paper specifically studies the v1 ≈ v2 convergence phenomenon** in dual-critic RL. This is an original observation worth highlighting.\n2. **No paper applies dual-critic to world-model imagination-based training** (Dreamer family). All dual-critic analysis is in model-free or Dyna-style MBRL.\n3. **No paper provides a formal theory for when implicit regularization from twin critics is sufficient vs. insufficient** across environments.\n4. **The implicit regularization interpretation of twin critics** (as opposed to pessimistic estimation) lacks a dedicated theoretical treatment.\n\n---\n\n## 8. Papers to Add to literature_map.yaml\n\n```yaml\n- paper_id: turcato2024exploiting\n  title: \"Exploiting Estimation Bias in Clipped Double Q-Learning for Continuous Control\"\n  authors: [Turcato N., Sinigaglia A., Dalla Libera A., Carli R., Susto G.A.]\n  year: 2024\n  venue: \"arXiv:2402.09078\"\n  category: evaluation\n  role: \"Shows bias preference (under- vs over-estimation) is environment-dependent; Walker/Ant favor underestimation, Swimmer/Reacher favor overestimation. Directly explains our dual-critic's differential effectiveness across Walker (full prevention) and Cheetah (partial mitigation).\"\n  relevance_score: 5\n\n- paper_id: bhatt2024crossq\n  title: \"CrossQ: Batch Normalization in Deep Reinforcement Learning for Greater Sample Efficiency and Simplicity\"\n  authors: [Bhatt A., et al.]\n  year: 2024\n  venue: \"ICLR 2024\"\n  category: method-component\n  role: \"Demonstrates that implicit regularization via batch normalization in critics outperforms explicit pessimism (min-of-two); drops from 2 critics to 1 with BN and achieves better results. Supports our v1≈v2 finding: the mechanism is regularization, not pessimism.\"\n  relevance_score: 4\n\n- paper_id: lyu2022darc\n  title: \"Efficient Continuous Control with Double Actors and Regularized Critics\"\n  authors: [Lyu J., Ma X., Yan J., Li X.]\n  year: 2022\n  venue: \"AAAI 2022 (arXiv:2106.03050)\"\n  category: method-component\n  role: \"DARC — shows double actors (not double critics) mitigate both over- and underestimation; critic regularization provides stability. Supports the interpretation that min-of-two critics works primarily as regularization.\"\n  relevance_score: 3\n\n- paper_id: barkley2025forensic\n  title: \"A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in MBPO\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2025\n  venue: \"arXiv:2510.01457\"\n  category: evaluation\n  role: \"Extended version of barkley2024stealing. Shows MBPO fails on 7/15 DMC tasks due to scale mismatch between dynamics/reward targets. Environment-dependent MBRL failure is systematic, not anomalous.\"\n  relevance_score: 4\n```\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " # Dual-Critic Cross-Environment Effectiveness: Literature Survey",
          " ",
          " **Date:** 2026-05-21",
          "-**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. Walker: full prevention (NVE≤1.4). Cheetah: partial mitigation (peak NVE 1.8, 40× compression vs baseline NVE 70.64). Key finding: v1 ≈ v2 (critic difference < 0.2), suggesting implicit value regularization rather than pessimistic estimation.",
          "+**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. 2×2 factorial (dual/single × narrow/scaled) reveals that neither the min operation alone nor increased capacity alone prevents CIVO on Walker; only their combination succeeds (exp_032, NVE < 1.5). Key finding: v1 ≈ v2 (critic difference < 0.2), confirming implicit regularization rather than pessimistic estimation — but this regularization requires sufficient critic capacity to be effective.",
          " ",
          " ---",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 17_

Now update Section 5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "1fd887bf-0049-404d-b774-6b2c890ff111",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuoCJVvuCQnaRDM53TaquQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 29535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
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

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_018YdGkWN2d12qtDvfiZhUCc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
  "old_string": "## 5. Synthesis: Explaining Prevention vs. Mitigation\n\n### Why Full Prevention on Walker\n\n1. **Simple reward landscape** (2 joints, stand + walk) → overestimation manifests in a lower-dimensional value function space\n2. **Dual-critic implicit regularization** (redundant parameterization, shared target convergence) is sufficient to constrain value growth in this simpler space\n3. **Short credit assignment chain** → regularization doesn't need to propagate through many imagination steps\n4. **Walker favors underestimation** (Turcato et al. 2024) → even the tiny residual pessimism from min(v1, v2) when v1 ≈ v2 helps\n\n### Why Only Mitigation on Cheetah\n\n1. **Complex reward landscape** (6 joints, forward speed) → value function has more degrees of freedom for overestimation\n2. **Implicit regularization from 2 critics is insufficient** for this higher-dimensional problem; need stronger intervention (REDQ-style larger ensembles, or explicit pessimism)\n3. **Longer credit assignment chain** (Ma et al. 2024) → regularization effect attenuates across more imagination steps\n4. **v1 ≈ v2 means no effective pessimism** → the 40× compression vs baseline is entirely from regularization, which has limits in complex environments\n5. **Task-dependent regularization effectiveness** is a general phenomenon (Nauman et al. 2024), not specific to our method\n\n### The Implicit Regularization Hypothesis\n\nThe v1 ≈ v2 finding (< 0.2 difference) is the key evidence. If dual-critic worked via pessimism, we would expect persistent v1 ≠ v2 gaps. Instead, the mechanism appears to be:\n\n1. **Redundant parameterization** → training two networks on the same target creates mutual regularization through gradient noise decorrelation\n2. **Shared target coupling** → the min operation creates a self-consistent training signal that prevents either network from diverging\n3. **Implicit capacity constraint** → maintaining two networks that must agree constrains the representational capacity available for fitting overestimated values\n4. **This is analogous to** CrossQ's finding that architectural regularization (BN) outperforms algorithmic pessimism (min-of-two)",
  "new_string": "## 5. Synthesis: Synergistic Prevention\n\n### 2×2 Factorial Evidence\n\nA controlled 2×2 factorial on Walker (dual/single × narrow/scaled) isolates the contributions of the min operation and critic capacity:\n\n| Configuration | Params | CIVO? | NVE | Interpretation |\n|--------------|--------|-------|-----|----------------|\n| Single + normal (baseline) | ~1.2M | ✓ | baseline | Reference |\n| Single + scaled (exp_033) | ~2.9M | ✓ | 4.7 | Capacity alone insufficient |\n| Dual + narrow (exp_035) | ~1.05M | ✓ | 2.75 | Min operation alone insufficient |\n| Dual + scaled (exp_032) | ~2.4M | ✗ | <1.5 | Min + capacity → prevention |\n\nThis overturns the initial \"Walker: full prevention\" characterization. The default dual-critic (2×256, ~1.05M total < baseline 1.18M) does *not* prevent CIVO (NVE 2.75). Prevention requires the combination of dual architecture and scaled capacity.\n\n### Neither Factor Alone Suffices\n\n**Min operation alone is ineffective.** In exp_035 (dual + narrow, 2×256 hidden), v1 ≈ v2 throughout training — the min operation produces no pessimism when critics have limited capacity and converge to the same function. NVE 2.75 represents marginal improvement over baseline, with CIVO still triggered. This confirms the v1 ≈ v2 convergence phenomenon (Section 2): with identical targets, data, and loss, two narrow networks learn the same function.\n\n**Capacity alone is ineffective.** In exp_033 (single + wide, ~2.9M params), the enlarged critic still reaches NVE 4.7 and triggers CIVO. More parameters without structural constraint simply provide more capacity for fitting overestimated values. This rules out a pure \"underfitting\" explanation for CIVO.\n\n### The Synergy: Implicit Regularization Requires Sufficient Capacity\n\nThe key finding is that prevention emerges only from the *interaction* of dual architecture and scaled capacity (exp_032, ~2.4M, NVE < 1.5). We hypothesize the mechanism operates in two stages:\n\n1. **Capacity enables representational diversity.** Scaled critics (≥512 hidden per critic) can maintain distinct value landscapes rather than collapsing to the same function. This is a prerequisite for the min operation to exert any pessimistic pressure.\n\n2. **The min operation constrains the diverse representations.** Given critics with enough capacity to disagree, `min(v1, v2)` selects the conservative estimate, preventing either critic's overestimation from propagating to the actor. The constraint is only meaningful when there is something to constrain.\n\nThis is analogous to CrossQ's batch normalization mechanism (Bhatt et al. 2024): BN regularization is effective only when the network has sufficient capacity for BN statistics to meaningfully decorrelate activations. In undersized networks, BN has little to regularize. Similarly, our dual-critic's implicit regularization — redundant parameterization, shared target coupling, gradient noise decorrelation — requires sufficient per-critic capacity to produce the representational diversity that makes the min operation functional.\n\n### Environment-Dependent Considerations\n\nThe 2×2 factorial was conducted on Walker. Whether the same capacity threshold applies to Cheetah remains an open question. Given Cheetah's more complex reward landscape (6 joints, forward speed optimization) and longer credit assignment chain (Ma et al. 2024), the required capacity for synergistic prevention may be higher:\n\n- **Walker** (2 joints, simple reward): ~1.2M per critic (2×512) suffices for synergy\n- **Cheetah** (6 joints, complex coordination): threshold unknown; task-dependent regularization effectiveness (Nauman et al. 2024; Turcato et al. 2024) suggests it may require larger ensembles (REDQ, N > 2; Chen et al. 2021) or stronger architectural regularization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "e75da5f2-c2f5-4b19-9502-9d65d5166c04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuoCJVvuCQnaRDM53TaquQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 29535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
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

_source line 19 · 2026-05-21T12:54:09.506Z_

<details><summary>↩ Tool result · `toolu_018YdGkWN2d12qtDvfiZhUCc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "8e44195a-feb7-4d64-a760-922b1b302104",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
    "oldString": "## 5. Synthesis: Explaining Prevention vs. Mitigation\n\n### Why Full Prevention on Walker\n\n1. **Simple reward landscape** (2 joints, stand + walk) → overestimation manifests in a lower-dimensional value function space\n2. **Dual-critic implicit regularization** (redundant parameterization, shared target convergence) is sufficient to constrain value growth in this simpler space\n3. **Short credit assignment chain** → regularization doesn't need to propagate through many imagination steps\n4. **Walker favors underestimation** (Turcato et al. 2024) → even the tiny residual pessimism from min(v1, v2) when v1 ≈ v2 helps\n\n### Why Only Mitigation on Cheetah\n\n1. **Complex reward landscape** (6 joints, forward speed) → value function has more degrees of freedom for overestimation\n2. **Implicit regularization from 2 critics is insufficient** for this higher-dimensional problem; need stronger intervention (REDQ-style larger ensembles, or explicit pessimism)\n3. **Longer credit assignment chain** (Ma et al. 2024) → regularization effect attenuates across more imagination steps\n4. **v1 ≈ v2 means no effective pessimism** → the 40× compression vs baseline is entirely from regularization, which has limits in complex environments\n5. **Task-dependent regularization effectiveness** is a general phenomenon (Nauman et al. 2024), not specific to our method\n\n### The Implicit Regularization Hypothesis\n\nThe v1 ≈ v2 finding (< 0.2 difference) is the key evidence. If dual-critic worked via pessimism, we would expect persistent v1 ≠ v2 gaps. Instead, the mechanism appears to be:\n\n1. **Redundant parameterization** → training two networks on the same target creates mutual regularization through gradient noise decorrelation\n2. **Shared target coupling** → the min operation creates a self-consistent training signal that prevents either network from diverging\n3. **Implicit capacity constraint** → maintaining two networks that must agree constrains the representational capacity available for fitting overestimated values\n4. **This is analogous to** CrossQ's finding that architectural regularization (BN) outperforms algorithmic pessimism (min-of-two)",
    "newString": "## 5. Synthesis: Synergistic Prevention\n\n### 2×2 Factorial Evidence\n\nA controlled 2×2 factorial on Walker (dual/single × narrow/scaled) isolates the contributions of the min operation and critic capacity:\n\n| Configuration | Params | CIVO? | NVE | Interpretation |\n|--------------|--------|-------|-----|----------------|\n| Single + normal (baseline) | ~1.2M | ✓ | baseline | Reference |\n| Single + scaled (exp_033) | ~2.9M | ✓ | 4.7 | Capacity alone insufficient |\n| Dual + narrow (exp_035) | ~1.05M | ✓ | 2.75 | Min operation alone insufficient |\n| Dual + scaled (exp_032) | ~2.4M | ✗ | <1.5 | Min + capacity → prevention |\n\nThis overturns the initial \"Walker: full prevention\" characterization. The default dual-critic (2×256, ~1.05M total < baseline 1.18M) does *not* prevent CIVO (NVE 2.75). Prevention requires the combination of dual architecture and scaled capacity.\n\n### Neither Factor Alone Suffices\n\n**Min operation alone is ineffective.** In exp_035 (dual + narrow, 2×256 hidden), v1 ≈ v2 throughout training — the min operation produces no pessimism when critics have limited capacity and converge to the same function. NVE 2.75 represents marginal improvement over baseline, with CIVO still triggered. This confirms the v1 ≈ v2 convergence phenomenon (Section 2): with identical targets, data, and loss, two narrow networks learn the same function.\n\n**Capacity alone is ineffective.** In exp_033 (single + wide, ~2.9M params), the enlarged critic still reaches NVE 4.7 and triggers CIVO. More parameters without structural constraint simply provide more capacity for fitting overestimated values. This rules out a pure \"underfitting\" explanation for CIVO.\n\n### The Synergy: Implicit Regularization Requires Sufficient Capacity\n\nThe key finding is that prevention emerges only from the *interaction* of dual architecture and scaled capacity (exp_032, ~2.4M, NVE < 1.5). We hypothesize the mechanism operates in two stages:\n\n1. **Capacity enables representational diversity.** Scaled critics (≥512 hidden per critic) can maintain distinct value landscapes rather than collapsing to the same function. This is a prerequisite for the min operation to exert any pessimistic pressure.\n\n2. **The min operation constrains the diverse representations.** Given critics with enough capacity to disagree, `min(v1, v2)` selects the conservative estimate, preventing either critic's overestimation from propagating to the actor. The constraint is only meaningful when there is something to constrain.\n\nThis is analogous to CrossQ's batch normalization mechanism (Bhatt et al. 2024): BN regularization is effective only when the network has sufficient capacity for BN statistics to meaningfully decorrelate activations. In undersized networks, BN has little to regularize. Similarly, our dual-critic's implicit regularization — redundant parameterization, shared target coupling, gradient noise decorrelation — requires sufficient per-critic capacity to produce the representational diversity that makes the min operation functional.\n\n### Environment-Dependent Considerations\n\nThe 2×2 factorial was conducted on Walker. Whether the same capacity threshold applies to Cheetah remains an open question. Given Cheetah's more complex reward landscape (6 joints, forward speed optimization) and longer credit assignment chain (Ma et al. 2024), the required capacity for synergistic prevention may be higher:\n\n- **Walker** (2 joints, simple reward): ~1.2M per critic (2×512) suffices for synergy\n- **Cheetah** (6 joints, complex coordination): threshold unknown; task-dependent regularization effectiveness (Nauman et al. 2024; Turcato et al. 2024) suggests it may require larger ensembles (REDQ, N > 2; Chen et al. 2021) or stronger architectural regularization",
    "originalFile": "# Dual-Critic Cross-Environment Effectiveness: Literature Survey\n\n**Date:** 2026-05-21\n**Context:** DreamerV3 + dual-critic (min-of-two, TD3-style) as CIVO intervention. 2×2 factorial (dual/single × narrow/scaled) reveals that neither the min operation alone nor increased capacity alone prevents CIVO on Walker; only their combination succeeds (exp_032, NVE < 1.5). Key finding: v1 ≈ v2 (critic difference < 0.2), confirming implicit regularization rather than pessimistic estimation — but this regularization requires sufficient critic capacity to be effective.\n\n---\n\n## 1. Environment-Dependent Effectiveness of Bias Correction\n\n### 1.1 Turcato et al. 2024 — Bias Preference is Environment-Dependent\n\n- **Title:** Exploiting Estimation Bias in Clipped Double Q-Learning for Continuous Control Reinforcement Learning Tasks\n- **Authors:** Turcato N., Sinigaglia A., Dalla Libera A., Carli R., Susto G.A.\n- **Year:** 2024\n- **Venue:** arXiv:2402.09078\n- **Core finding:** \"None of the considered update strategies performs the best among all the considered environments.\" Specifically:\n  - **Walker, Ant, Hopper, Humanoid:** TD3's underestimation bias performs best\n  - **Swimmer, Reacher:** Overestimation bias performs best\n  - Sufficient condition for overestimation advantage: \"noisy regions of the MDP correlate with the high reward\"\n- **Relevance to our finding:** Walker's reward landscape (stand + walk forward, 2 joints) favors underestimation → dual-critic's conservative bias fully prevents CIVO. Cheetah Run's reward landscape (forward speed, 6 joints, more complex coordination) may have regions where underestimation is suboptimal, explaining partial rather than full prevention.\n\n### 1.2 Nauman et al. 2024 — Regularization Effectiveness is Task-Dependent (Already in map: nauman2024bitter)\n\n- **Title:** Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning\n- **Authors:** Nauman M., Bortkiewicz M., Miłoś P., Trzcinski T., Ostaszewski M., Cygan M.\n- **Year:** 2024\n- **Venue:** ICML 2024\n- **Core finding:** Tested 60+ off-policy agents with various regularization techniques across 14 tasks. \"The effectiveness of a specific regularization setup varies with the task, [though] certain combinations consistently demonstrate robust and superior performance.\"\n- **Relevance:** Directly confirms that dual-critic (a form of value regularization) working fully on Walker but partially on Cheetah is a *predicted* consequence of task-dependent regularization effectiveness, not an anomaly.\n\n### 1.3 Heess et al. 2015 — Gradient-Through-Dynamics is Task-Dependent (Already in map: heess2015svg)\n\n- **Title:** Learning Continuous Control Policies by Stochastic Value Gradients\n- **Authors:** Heess N., Wayne G., Silver D., Lillicrap T., Erez T., Tassa Y.\n- **Year:** 2015\n- **Venue:** NeurIPS\n- **Core finding:** SVG(0) (no model gradient) works for simple tasks; SVG(1+) needed for complex tasks but SVG(∞) degrades. Simple tasks tolerate aggressive gradient interventions; complex tasks need finer control.\n- **Relevance:** Walker (simple) tolerates the implicit regularization from dual critics fully; Cheetah (complex) needs more nuanced intervention — consistent with SVG gradient hierarchy.\n\n---\n\n## 2. The v1 ≈ v2 Phenomenon: Why Two Critics Converge\n\n### 2.1 Theoretical Basis — Shared Target Drives Convergence\n\nIn TD3/SAC dual-critic setups, both critics are trained against `min(Q1_target, Q2_target)`. Since they share identical Bellman targets, gradient descent drives both networks toward the same function. The \"independence\" that enables pessimism exists only at initialization and early training. Over time, both networks converge because:\n- Same data distribution (same replay buffer)\n- Same target values (min of two target networks)\n- Same loss function (MSE on Bellman residual)\n\n**No paper found that specifically studies the \"v1 ≈ v2 convergence\" phenomenon.** This is a gap in the literature. The closest discussions are:\n\n### 2.2 Bhatt et al. 2024 — CrossQ: Implicit Regularization Without Pessimism\n\n- **Title:** CrossQ: Batch Normalization in Deep Reinforcement Learning for Greater Sample Efficiency and Simplicity\n- **Authors:** Bhatt A., et al.\n- **Year:** 2024 (originally 2019, major revision 2024)\n- **Venue:** ICLR 2024\n- **Core finding:** Batch normalization in critic networks achieves state-of-the-art without target networks or ensembles. \"High performance may be attributed to implicitly reducing bias as a side effect of design choices.\" CrossQ drops from 2 critics to 1 with BN and achieves better results.\n- **Relevance:** Demonstrates that the primary mechanism of twin critics may be *implicit regularization through architectural choices* (shared BN statistics, parameter coupling), not pessimistic estimation. Supports our v1 ≈ v2 finding: the min operation doesn't create pessimism when critics agree; instead, the act of training two networks provides regularization.\n\n### 2.3 Lyu et al. 2022 — DARC: Double Actors Provide the Real Benefit\n\n- **Title:** Efficient Continuous Control with Double Actors and Regularized Critics\n- **Authors:** Lyu J., Ma X., Yan J., Li X.\n- **Year:** 2022\n- **Venue:** AAAI 2022 (arXiv:2106.03050)\n- **Core finding:** Double actors (not double critics) are the key to mitigating both over- and underestimation. Critic regularization (not min operation) provides stability.\n- **Relevance:** Suggests the min-of-two mechanism is not the most important component — the regularization from maintaining multiple estimators is.\n\n---\n\n## 3. Implicit Regularization Mechanisms in Value Estimation\n\n### 3.1 Lyle et al. 2024 — Normalization as Implicit Overestimation Control (Already in map: lyle2024normalization)\n\n- **Title:** Normalization and Effective Learning Rates in Reinforcement Learning\n- **Authors:** Lyle C., et al.\n- **Year:** 2024\n- **Venue:** NeurIPS 2024\n- **Core finding:** Normalization layers combat overestimation but cause effective LR decay via parameter norm growth. Different initializations → different norm growth trajectories → different overestimation damping.\n- **Relevance:** Dual-critic training introduces additional normalization-like effects through redundant parameterization. The v1 ≈ v2 convergence may itself act as an implicit constraint that damps value growth.\n\n### 3.2 Kumar et al. 2022 — DR3: TD Learning Has Implicit Regularization (Already in map: kumar2022dr3)\n\n- **Title:** DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization\n- **Authors:** Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.\n- **Year:** 2022\n- **Venue:** ICLR 2022\n- **Core finding:** Implicit regularization from TD learning favors degenerate feature aliasing. Two critics trained on the same targets undergo similar feature collapse, explaining v1 ≈ v2.\n- **Relevance:** The convergence of v1 and v2 may be a manifestation of DR3's feature aliasing — both networks learn the same degenerate representation, which incidentally bounds overestimation.\n\n### 3.3 Layer Normalization > Explicit Anti-Overestimation (from Nauman et al. 2024)\n\n- **Core finding:** \"Layer normalisation is more effective in reducing overestimation than techniques specifically designed for mitigating Q-value overestimation in critic networks.\"\n- **Relevance:** Network regularization (implicit) can be more powerful than algorithmic pessimism (explicit min-of-two). Our dual-critic may be working primarily through its regularization effect on the shared representation.\n\n---\n\n## 4. Compounding Error and Critic Architecture in Model-Based RL\n\n### 4.1 Palenicek et al. 2025 — Even Oracle Models Show Diminishing Returns (Already in map: palenicek2025diminishing)\n\n- **Title:** Diminishing Return of Value Expansion Methods\n- **Authors:** Palenicek D., et al.\n- **Year:** 2025\n- **Venue:** RLC 2025 (arXiv:2412.20537)\n- **Core finding:** Longer rollout horizons have diminishing returns even with oracle dynamics. The bottleneck is value estimation, not model accuracy.\n- **Relevance:** Dual-critic's partial effectiveness in Cheetah is consistent with the value estimation bottleneck being harder to resolve in complex environments, even when the critic architecture is improved.\n\n### 4.2 Barkley & Fridovich-Keil 2025 — Environment-Dependent MBRL Failures (Already in map: barkley2024stealing; updated version: 2510.01457)\n\n- **Title:** A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in Model-Based Policy Optimization\n- **Authors:** Barkley B., Fridovich-Keil D.\n- **Year:** 2025\n- **Venue:** arXiv:2510.01457\n- **Core finding:** MBPO succeeds on Gym but fails on 7/15 DMC tasks. Root causes: scale mismatch between dynamics and reward targets suppresses reward learning → critic underestimation. Benchmark-specific assumptions get baked into algorithm design.\n- **Relevance:** Environment-dependent failure of model-based methods is a documented and general phenomenon. Our dual-critic's differential effectiveness across Walker/Cheetah follows the same pattern.\n\n### 4.3 Ma et al. 2024 — Policy Gradients Scale Exponentially with Horizon (Already in map: ma2024awm)\n\n- **Title:** Do Transformer World Models Give Better Policy Gradients?\n- **Authors:** Ma M., Ni T., Gehring C., D'Oro P., Bacon P.-L.\n- **Year:** 2024\n- **Venue:** ICML 2024\n- **Core finding:** Policy gradients through standard world models scale exponentially with horizon. Environments differ in how much they rely on long-range credit assignment.\n- **Relevance:** Cheetah requires deeper temporal credit assignment than Walker. Dual-critic regularization may be insufficient to tame exponentially growing gradient issues in Cheetah's longer credit assignment chain.\n\n### 4.4 Chen et al. 2021 — REDQ: Ensemble Size Controls Pessimism (Already in map: chen2021redq)\n\n- **Title:** Randomized Ensembled Double Q-Learning\n- **Authors:** Chen X., Wang C., Zhou Z., Ross K.\n- **Year:** 2021\n- **Venue:** ICLR 2021\n- **Core finding:** Ensemble of N Q-functions with in-target minimization over M < N random subset controls overestimation. Larger M/N → more pessimism. N=2, M=2 (TD3) is the minimum configuration.\n- **Relevance:** With only 2 critics (TD3-style), the pessimism budget is minimal. If v1 ≈ v2, the effective pessimism is nearly zero. REDQ suggests N > 2 might be needed for Cheetah. Our finding that 2 critics provide regularization rather than pessimism is consistent with REDQ's framework.\n\n---\n\n## 5. Synthesis: Explaining Prevention vs. Mitigation\n\n### Why Full Prevention on Walker\n\n1. **Simple reward landscape** (2 joints, stand + walk) → overestimation manifests in a lower-dimensional value function space\n2. **Dual-critic implicit regularization** (redundant parameterization, shared target convergence) is sufficient to constrain value growth in this simpler space\n3. **Short credit assignment chain** → regularization doesn't need to propagate through many imagination steps\n4. **Walker favors underestimation** (Turcato et al. 2024) → even the tiny residual pessimism from min(v1, v2) when v1 ≈ v2 helps\n\n### Why Only Mitigation on Cheetah\n\n1. **Complex reward landscape** (6 joints, forward speed) → value function has more degrees of freedom for overestimation\n2. **Implicit regularization from 2 critics is insufficient** for this higher-dimensional problem; need stronger intervention (REDQ-style larger ensembles, or explicit pessimism)\n3. **Longer credit assignment chain** (Ma et al. 2024) → regularization effect attenuates across more imagination steps\n4. **v1 ≈ v2 means no effective pessimism** → the 40× compression vs baseline is entirely from regularization, which has limits in complex environments\n5. **Task-dependent regularization effectiveness** is a general phenomenon (Nauman et al. 2024), not specific to our method\n\n### The Implicit Regularization Hypothesis\n\nThe v1 ≈ v2 finding (< 0.2 difference) is the key evidence. If dual-critic worked via pessimism, we would expect persistent v1 ≠ v2 gaps. Instead, the mechanism appears to be:\n\n1. **Redundant parameterization** → training two networks on the same target creates mutual regularization through gradient noise decorrelation\n2. **Shared target coupling** → the min operation creates a self-consistent training signal that prevents either network from diverging\n3. **Implicit capacity constraint** → maintaining two networks that must agree constrains the representational capacity available for fitting overestimated values\n4. **This is analogous to** CrossQ's finding that architectural regularization (BN) outperforms algorithmic pessimism (min-of-two)\n\n---\n\n## 6. Key Papers for Citation\n\n### Must-cite (new, not in literature map)\n\n| Paper | Citation Key | Why |\n|-------|-------------|-----|\n| Turcato et al. 2024 | turcato2024exploiting | Environment-dependent bias preference — direct explanation for Walker vs Cheetah |\n| Bhatt et al. 2024 CrossQ | bhatt2024crossq | Implicit regularization > explicit pessimism — supports v1≈v2 mechanism |\n| Lyu et al. 2022 DARC | lyu2022darc | Double actors + regularized critics — the regularization view of twin networks |\n\n### Should-cite (already in literature map)\n\n| Paper | Citation Key | Why |\n|-------|-------------|-----|\n| Nauman et al. 2024 | nauman2024bitter | Task-dependent regularization effectiveness (60+ agents, 14 tasks) |\n| Palenicek et al. 2025 | palenicek2025diminishing | Value estimation is the bottleneck, not model quality |\n| Ma et al. 2024 | ma2024awm | Gradient scaling explains Cheetah's resistance to regularization |\n| Chen et al. 2021 REDQ | chen2021redq | N=2 is minimal ensemble; larger N may be needed |\n| Kumar et al. 2022 DR3 | kumar2022dr3 | Feature aliasing explains v1≈v2 convergence |\n| Lyle et al. 2024 | lyle2024normalization | Normalization as implicit overestimation control |\n\n---\n\n## 7. Literature Gaps Identified\n\n1. **No paper specifically studies the v1 ≈ v2 convergence phenomenon** in dual-critic RL. This is an original observation worth highlighting.\n2. **No paper applies dual-critic to world-model imagination-based training** (Dreamer family). All dual-critic analysis is in model-free or Dyna-style MBRL.\n3. **No paper provides a formal theory for when implicit regularization from twin critics is sufficient vs. insufficient** across environments.\n4. **The implicit regularization interpretation of twin critics** (as opposed to pessimistic estimation) lacks a dedicated theoretical treatment.\n\n---\n\n## 8. Papers to Add to literature_map.yaml\n\n```yaml\n- paper_id: turcato2024exploiting\n  title: \"Exploiting Estimation Bias in Clipped Double Q-Learning for Continuous Control\"\n  authors: [Turcato N., Sinigaglia A., Dalla Libera A., Carli R., Susto G.A.]\n  year: 2024\n  venue: \"arXiv:2402.09078\"\n  category: evaluation\n  role: \"Shows bias preference (under- vs over-estimation) is environment-dependent; Walker/Ant favor underestimation, Swimmer/Reacher favor overestimation. Directly explains our dual-critic's differential effectiveness across Walker (full prevention) and Cheetah (partial mitigation).\"\n  relevance_score: 5\n\n- paper_id: bhatt2024crossq\n  title: \"CrossQ: Batch Normalization in Deep Reinforcement Learning for Greater Sample Efficiency and Simplicity\"\n  authors: [Bhatt A., et al.]\n  year: 2024\n  venue: \"ICLR 2024\"\n  category: method-component\n  role: \"Demonstrates that implicit regularization via batch normalization in critics outperforms explicit pessimism (min-of-two); drops from 2 critics to 1 with BN and achieves better results. Supports our v1≈v2 finding: the mechanism is regularization, not pessimism.\"\n  relevance_score: 4\n\n- paper_id: lyu2022darc\n  title: \"Efficient Continuous Control with Double Actors and Regularized Critics\"\n  authors: [Lyu J., Ma X., Yan J., Li X.]\n  year: 2022\n  venue: \"AAAI 2022 (arXiv:2106.03050)\"\n  category: method-component\n  role: \"DARC — shows double actors (not double critics) mitigate both over- and underestimation; critic regularization provides stability. Supports the interpretation that min-of-two critics works primarily as regularization.\"\n  relevance_score: 3\n\n- paper_id: barkley2025forensic\n  title: \"A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in MBPO\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2025\n  venue: \"arXiv:2510.01457\"\n  category: evaluation\n  role: \"Extended version of barkley2024stealing. Shows MBPO fails on 7/15 DMC tasks due to scale mismatch between dynamics/reward targets. Environment-dependent MBRL failure is systematic, not anomalous.\"\n  relevance_score: 4\n```\n",
    "structuredPatch": [
      {
        "oldStart": 137,
        "oldLines": 32,
        "newStart": 137,
        "newLines": 44,
        "lines": [
          " ",
          " ---",
          " ",
          "-## 5. Synthesis: Explaining Prevention vs. Mitigation",
          "+## 5. Synthesis: Synergistic Prevention",
          " ",
          "-### Why Full Prevention on Walker",
          "+### 2×2 Factorial Evidence",
          " ",
          "-1. **Simple reward landscape** (2 joints, stand + walk) → overestimation manifests in a lower-dimensional value function space",
          "-2. **Dual-critic implicit regularization** (redundant parameterization, shared target convergence) is sufficient to constrain value growth in this simpler space",
          "-3. **Short credit assignment chain** → regularization doesn't need to propagate through many imagination steps",
          "-4. **Walker favors underestimation** (Turcato et al. 2024) → even the tiny residual pessimism from min(v1, v2) when v1 ≈ v2 helps",
          "+A controlled 2×2 factorial on Walker (dual/single × narrow/scaled) isolates the contributions of the min operation and critic capacity:",
          " ",
          "-### Why Only Mitigation on Cheetah",
          "+| Configuration | Params | CIVO? | NVE | Interpretation |",
          "+|--------------|--------|-------|-----|----------------|",
          "+| Single + normal (baseline) | ~1.2M | ✓ | baseline | Reference |",
          "+| Single + scaled (exp_033) | ~2.9M | ✓ | 4.7 | Capacity alone insufficient |",
          "+| Dual + narrow (exp_035) | ~1.05M | ✓ | 2.75 | Min operation alone insufficient |",
          "+| Dual + scaled (exp_032) | ~2.4M | ✗ | <1.5 | Min + capacity → prevention |",
          " ",
          "-1. **Complex reward landscape** (6 joints, forward speed) → value function has more degrees of freedom for overestimation",
          "-2. **Implicit regularization from 2 critics is insufficient** for this higher-dimensional problem; need stronger intervention (REDQ-style larger ensembles, or explicit pessimism)",
          "-3. **Longer credit assignment chain** (Ma et al. 2024) → regularization effect attenuates across more imagination steps",
          "-4. **v1 ≈ v2 means no effective pessimism** → the 40× compression vs baseline is entirely from regularization, which has limits in complex environments",
          "-5. **Task-dependent regularization effectiveness** is a general phenomenon (Nauman et al. 2024), not specific to our method",
          "+This overturns the initial \"Walker: full prevention\" characterization. The default dual-critic (2×256, ~1.05M total < baseline 1.18M) does *not* prevent CIVO (NVE 2.75). Prevention requires the combination of dual architecture and scaled capacity.",
          " ",
          "-### The Implicit Regularization Hypothesis",
          "+### Neither Factor Alone Suffices",
          " ",
          "-The v1 ≈ v2 finding (< 0.2 difference) is the key evidence. If dual-critic worked via pessimism, we would expect persistent v1 ≠ v2 gaps. Instead, the mechanism appears to be:",
          "+**Min operation alone is ineffective.** In exp_035 (dual + narrow, 2×256 hidden), v1 ≈ v2 throughout training — the min operation produces no pessimism when critics have limited capacity and converge to the same function. NVE 2.75 represents marginal improvement over baseline, with CIVO still triggered. This confirms the v1 ≈ v2 convergence phenomenon (Section 2): with identical targets, data, and loss, two narrow networks learn the same function.",
          " ",
          "-1. **Redundant parameterization** → training two networks on the same target creates mutual regularization through gradient noise decorrelation",
          "-2. **Shared target coupling** → the min operation creates a self-consistent training signal that prevents either network from diverging",
          "-3. **Implicit capacity constraint** → maintaining two networks that must agree constrains the representational capacity available for fitting overestimated values",
          "-4. **This is analogous to** CrossQ's finding that architectural regularization (BN) outperforms algorithmic pessimism (min-of-two)",
          "+**Capacity alone is ineffective.** In exp_033 (single + wide, ~2.9M params), the enlarged critic still reaches NVE 4.7 and triggers CIVO. More parameters without structural constraint simply provide more capacity for fitting overestimated values. This rules out a pure \"underfitting\" explanation for CIVO.",
          " ",
          "+### The Synergy: Implicit Regularization Requires Sufficient Capacity",
          "+",
          "+The key finding is that prevention emerges only from the *interaction* of dual architecture and scaled capacity (exp_032, ~2.4M, NVE < 1.5). We hypothesize the mechanism operates in two stages:",
          "+",
          "+1. **Capacity enables representational diversity.** Scaled critics (≥512 hidden per critic) can maintain distinct value landscapes rather than collapsing to the same function. This is a prerequisite for the min operation to exert any pessimistic pressure.",
          "+",
          "+2. **The min operation constrains the diverse representations.** Given critics with enough capacity to disagree, `min(v1, v2)` selects the conservative estimate, preventing either critic's overestimation from propagating to the actor. The constraint is only meaningful when there is something to constrain.",
          "+",
          "+This is analogous to CrossQ's batch normalization mechanism (Bhatt et al. 2024): BN regularization is effective only when the network has sufficient capacity for BN statistics to meaningfully decorrelate activations. In undersized networks, BN has little to regularize. Similarly, our dual-critic's implicit regularization — redundant parameterization, shared target coupling, gradient noise decorrelation — requires sufficient per-critic capacity to produce the representational diversity that makes the min operation functional.",
          "+",
          "+### Environment-Dependent Considerations",
          "+",
          "+The 2×2 factorial was conducted on Walker. Whether the same capacity threshold applies to Cheetah remains an open question. Given Cheetah's more complex reward landscape (6 joints, forward speed optimization) and longer credit assignment chain (Ma et al. 2024), the required capacity for synergistic prevention may be higher:",
          "+",
          "+- **Walker** (2 joints, simple reward): ~1.2M per critic (2×512) suffices for synergy",
          "+- **Cheetah** (6 joints, complex coordination): threshold unknown; task-dependent regularization effectiveness (Nauman et al. 2024; Turcato et al. 2024) suggests it may require larger ensembles (REDQ, N > 2; Chen et al. 2021) or stronger architectural regularization",
          "+",
          " ---",
          " ",
          " ## 6. Key Papers for Citation"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---

### Assistant

_source line 20_

Let me verify the updated section reads correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "269a500f-488d-409a-8d5a-9466db98921c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vXBGTw8L9vi6tibKtBAo7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1750,
      "cache_read_input_tokens": 30464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1750
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01MXVi4YHaQDUMk4jbZUYFKa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
  "offset": 139,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "1439121f-038c-4032-b752-07967da7e9d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vXBGTw8L9vi6tibKtBAo7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1750,
      "cache_read_input_tokens": 30464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1750
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

_source line 22 · 2026-05-21T12:54:13.449Z_

<details><summary>↩ Tool result · `toolu_01MXVi4YHaQDUMk4jbZUYFKa`</summary>

```text
139	
140	## 5. Synthesis: Synergistic Prevention
141	
142	### 2×2 Factorial Evidence
143	
144	A controlled 2×2 factorial on Walker (dual/single × narrow/scaled) isolates the contributions of the min operation and critic capacity:
145	
146	| Configuration | Params | CIVO? | NVE | Interpretation |
147	|--------------|--------|-------|-----|----------------|
148	| Single + normal (baseline) | ~1.2M | ✓ | baseline | Reference |
149	| Single + scaled (exp_033) | ~2.9M | ✓ | 4.7 | Capacity alone insufficient |
150	| Dual + narrow (exp_035) | ~1.05M | ✓ | 2.75 | Min operation alone insufficient |
151	| Dual + scaled (exp_032) | ~2.4M | ✗ | <1.5 | Min + capacity → prevention |
152	
153	This overturns the initial "Walker: full prevention" characterization. The default dual-critic (2×256, ~1.05M total < baseline 1.18M) does *not* prevent CIVO (NVE 2.75). Prevention requires the combination of dual architecture and scaled capacity.
154	
155	### Neither Factor Alone Suffices
156	
157	**Min operation alone is ineffective.** In exp_035 (dual + narrow, 2×256 hidden), v1 ≈ v2 throughout training — the min operation produces no pessimism when critics have limited capacity and converge to the same function. NVE 2.75 represents marginal improvement over baseline, with CIVO still triggered. This confirms the v1 ≈ v2 convergence phenomenon (Section 2): with identical targets, data, and loss, two narrow networks learn the same function.
158	
159	**Capacity alone is ineffective.** In exp_033 (single + wide, ~2.9M params), the enlarged critic still reaches NVE 4.7 and triggers CIVO. More parameters without structural constraint simply provide more capacity for fitting overestimated values. This rules out a pure "underfitting" explanation for CIVO.
160	
161	### The Synergy: Implicit Regularization Requires Sufficient Capacity
162	
163	The key finding is that prevention emerges only from the *interaction* of dual architecture and scaled capacity (exp_032, ~2.4M, NVE < 1.5). We hypothesize the mechanism operates in two stages:
164	
165	1. **Capacity enables representational diversity.** Scaled critics (≥512 hidden per critic) can maintain distinct value landscapes rather than collapsing to the same function. This is a prerequisite for the min operation to exert any pessimistic pressure.
166	
167	2. **The min operation constrains the diverse representations.** Given critics with enough capacity to disagree, `min(v1, v2)` selects the conservative estimate, preventing either critic's overestimation from propagating to the actor. The constraint is only meaningful when there is something to constrain.
168	
169	This is analogous to CrossQ's batch normalization mechanism (Bhatt et al. 2024): BN regularization is effective only when the network has sufficient capacity for BN statistics to meaningfully decorrelate activations. In undersized networks, BN has little to regularize. Similarly, our dual-critic's implicit regularization — redundant parameterization, shared target coupling, gradient noise decorrelation — requires sufficient per-critic capacity to produce the representational diversity that makes the min operation functional.
170	
171	### Environment-Dependent Considerations
172	
173	The 2×2 factorial was conducted on Walker. Whether the same capacity threshold applies to Cheetah remains an open question. Given Cheetah's more complex reward landscape (6 joints, forward speed optimization) and longer credit assignment chain (Ma et al. 2024), the required capacity for synergistic prevention may be higher:
174	
175	- **Walker** (2 joints, simple reward): ~1.2M per critic (2×512) suffices for synergy
176	- **Cheetah** (6 joints, complex coordination): threshold unknown; task-dependent regularization effectiveness (Nauman et al. 2024; Turcato et al. 2024) suggests it may require larger ensembles (REDQ, N > 2; Chen et al. 2021) or stronger architectural regularization
177	
178	---
179	
180	## 6. Key Papers for Citation
181	
182	### Must-cite (new, not in literature map)
183	
184	| Paper | Citation Key | Why |
185	|-------|-------------|-----|
186	| Turcato et al. 2024 | turcato2024exploiting | Environment-dependent bias preference — direct explanation for Walker vs Cheetah |
187	| Bhatt et al. 2024 CrossQ | bhatt2024crossq | Implicit regularization > explicit pessimism — supports v1≈v2 mechanism |
188	| Lyu et al. 2022 DARC | lyu2022darc | Double actors + regularized critics — the regularization view of twin networks |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "40ef9283-6bbd-4e2c-9c96-7c9569ac6bdf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature/dual_critic_cross_env_literature.md",
      "content": "\n## 5. Synthesis: Synergistic Prevention\n\n### 2×2 Factorial Evidence\n\nA controlled 2×2 factorial on Walker (dual/single × narrow/scaled) isolates the contributions of the min operation and critic capacity:\n\n| Configuration | Params | CIVO? | NVE | Interpretation |\n|--------------|--------|-------|-----|----------------|\n| Single + normal (baseline) | ~1.2M | ✓ | baseline | Reference |\n| Single + scaled (exp_033) | ~2.9M | ✓ | 4.7 | Capacity alone insufficient |\n| Dual + narrow (exp_035) | ~1.05M | ✓ | 2.75 | Min operation alone insufficient |\n| Dual + scaled (exp_032) | ~2.4M | ✗ | <1.5 | Min + capacity → prevention |\n\nThis overturns the initial \"Walker: full prevention\" characterization. The default dual-critic (2×256, ~1.05M total < baseline 1.18M) does *not* prevent CIVO (NVE 2.75). Prevention requires the combination of dual architecture and scaled capacity.\n\n### Neither Factor Alone Suffices\n\n**Min operation alone is ineffective.** In exp_035 (dual + narrow, 2×256 hidden), v1 ≈ v2 throughout training — the min operation produces no pessimism when critics have limited capacity and converge to the same function. NVE 2.75 represents marginal improvement over baseline, with CIVO still triggered. This confirms the v1 ≈ v2 convergence phenomenon (Section 2): with identical targets, data, and loss, two narrow networks learn the same function.\n\n**Capacity alone is ineffective.** In exp_033 (single + wide, ~2.9M params), the enlarged critic still reaches NVE 4.7 and triggers CIVO. More parameters without structural constraint simply provide more capacity for fitting overestimated values. This rules out a pure \"underfitting\" explanation for CIVO.\n\n### The Synergy: Implicit Regularization Requires Sufficient Capacity\n\nThe key finding is that prevention emerges only from the *interaction* of dual architecture and scaled capacity (exp_032, ~2.4M, NVE < 1.5). We hypothesize the mechanism operates in two stages:\n\n1. **Capacity enables representational diversity.** Scaled critics (≥512 hidden per critic) can maintain distinct value landscapes rather than collapsing to the same function. This is a prerequisite for the min operation to exert any pessimistic pressure.\n\n2. **The min operation constrains the diverse representations.** Given critics with enough capacity to disagree, `min(v1, v2)` selects the conservative estimate, preventing either critic's overestimation from propagating to the actor. The constraint is only meaningful when there is something to constrain.\n\nThis is analogous to CrossQ's batch normalization mechanism (Bhatt et al. 2024): BN regularization is effective only when the network has sufficient capacity for BN statistics to meaningfully decorrelate activations. In undersized networks, BN has little to regularize. Similarly, our dual-critic's implicit regularization — redundant parameterization, shared target coupling, gradient noise decorrelation — requires sufficient per-critic capacity to produce the representational diversity that makes the min operation functional.\n\n### Environment-Dependent Considerations\n\nThe 2×2 factorial was conducted on Walker. Whether the same capacity threshold applies to Cheetah remains an open question. Given Cheetah's more complex reward landscape (6 joints, forward speed optimization) and longer credit assignment chain (Ma et al. 2024), the required capacity for synergistic prevention may be higher:\n\n- **Walker** (2 joints, simple reward): ~1.2M per critic (2×512) suffices for synergy\n- **Cheetah** (6 joints, complex coordination): threshold unknown; task-dependent regularization effectiveness (Nauman et al. 2024; Turcato et al. 2024) suggests it may require larger ensembles (REDQ, N > 2; Chen et al. 2021) or stronger architectural regularization\n\n---\n\n## 6. Key Papers for Citation\n\n### Must-cite (new, not in literature map)\n\n| Paper | Citation Key | Why |\n|-------|-------------|-----|\n| Turcato et al. 2024 | turcato2024exploiting | Environment-dependent bias preference — direct explanation for Walker vs Cheetah |\n| Bhatt et al. 2024 CrossQ | bhatt2024crossq | Implicit regularization > explicit pessimism — supports v1≈v2 mechanism |\n| Lyu et al. 2022 DARC | lyu2022darc | Double actors + regularized critics — the regularization view of twin networks |",
      "numLines": 50,
      "startLine": 139,
      "totalLines": 251
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

Section 5 updated. Changes made:

1. **Context header** (line 4): Updated from "Walker: full prevention" to reflect 2×2 factorial findings — prevention requires min + capacity synergy.

2. **Section 5 title**: "Prevention vs. Mitigation" → "Synergistic Prevention"

3. **New structure with four subsections**:
   - **2×2 Factorial Evidence**: Summary table with all four conditions (baseline, exp_033, exp_035, exp_032) and their NVE/CIVO outcomes
   - **Neither Factor Alone Suffices**: min operation alone → v1≈v2 convergence, no pessimism (exp_035); capacity alone → more room for overestimation (exp_033)
   - **The Synergy**: Two-stage mechanism hypothesis — capacity enables representational diversity, min operation constrains it. CrossQ BN analogy for why regularization needs sufficient capacity.
   - **Environment-Dependent Considerations**: Walker threshold established (~1.2M per critic), Cheetah threshold unknown, with literature pointers for why it may be higher.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "uuid": "ecf0f447-b91a-45ec-91ac-d6b389aea909",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CMzyRnCHgK9GjvcZm2xj8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1517,
      "cache_read_input_tokens": 32214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1517
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

_source line 24_

Section 5 updated. Changes made:

1. **Context header** (line 4): Updated from "Walker: full prevention" to reflect 2×2 factorial findings — prevention requires min + capacity synergy.

2. **Section 5 title**: "Prevention vs. Mitigation" → "Synergistic Prevention"

3. **New structure with four subsections**:
   - **2×2 Factorial Evidence**: Summary table with all four conditions (baseline, exp_033, exp_035, exp_032) and their NVE/CIVO outcomes
   - **Neither Factor Alone Suffices**: min operation alone → v1≈v2 convergence, no pessimism (exp_035); capacity alone → more room for overestimation (exp_033)
   - **The Synergy**: Two-stage mechanism hypothesis — capacity enables representational diversity, min operation constrains it. CrossQ BN analogy for why regularization needs sufficient capacity.
   - **Environment-Dependent Considerations**: Walker threshold established (~1.2M per critic), Cheetah threshold unknown, with literature pointers for why it may be higher.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 71734,
  "duration_api_ms": 73137,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "ac30be3a-883c-4cae-a752-2415d32d4276",
  "total_cost_usd": 0.31063250000000003,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 22284,
    "cache_read_input_tokens": 175085,
    "output_tokens": 3295,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 22284,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 262,
        "cache_read_input_tokens": 32214,
        "cache_creation_input_tokens": 1517,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1517
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1305,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00139,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 3295,
      "cacheReadInputTokens": 175085,
      "cacheCreationInputTokens": 22284,
      "webSearchRequests": 0,
      "costUSD": 0.30924250000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "494bbd82-6566-48b6-ac8b-c944cc1ce6c7"
}
```

</details>

---
