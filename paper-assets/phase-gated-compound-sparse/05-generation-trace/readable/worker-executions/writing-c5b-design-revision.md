# writing c5b design revision

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_writing_c5b_design_revision_20260514T145503.log`
- **Structured JSON:** [`6bcd1736ad6575f30a4e.json`](../../sessions/6b/6bcd1736ad6575f30a4e.json)

## Before a recorded user message

25 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
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
  "uuid": "23d127a1-7a28-4d99-883d-bd6c0f14d47f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1778778600,
    "rateLimitType": "five_hour",
    "utilization": 0.95,
    "isUsingOverage": false,
    "surpassedThreshold": 0.9
  },
  "uuid": "f9617aea-486f-4700-9488-385649177fc1",
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "dc8f81ad-6947-40aa-9091-ba83ed25972d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ETcPEnnNFYvpnd6CdjpZd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11976,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11976
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014GEeVr8qp6g9gK5jWojJHs`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "f5a98615-058c-4c4e-9ce7-cf5207d0f20c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ETcPEnnNFYvpnd6CdjpZd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11976,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11976
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

_source line 6 · 2026-05-14T14:55:20.962Z_

<details><summary>↩ Tool result · `toolu_014GEeVr8qp6g9gK5jWojJHs`</summary>

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
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "6ab8b477-2d6e-4f08-ba55-eeb4a36dc0b9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
Let me read the current document first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "38a6f665-7085-454e-a084-c375b46b4748",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jzk7rmjj9Dk89xc8ks32mq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 23423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 709
      },
      "output_tokens": 64,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013pJz1MyyCoWcJWytkL5FyG`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "artifacts/c5b_pilot_design.md",
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
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "61b00179-bb4f-4e3f-a2c1-10ca1ac088c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jzk7rmjj9Dk89xc8ks32mq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 23423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 709
      },
      "output_tokens": 64,
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

_source line 9 · 2026-05-14T14:55:24.080Z_

<details><summary>↩ Tool result · `toolu_013pJz1MyyCoWcJWytkL5FyG`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/c5b_pilot_design.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "cff0df9f-2507-4d82-aa5b-c288e897954c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/c5b_pilot_design.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/c5b_pilot_design.md'\", \"metadata\": {}}"
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
The MCP tool has a whitelist and doesn't support reading/writing arbitrary artifact files. Let me read the file directly from the filesystem.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "7b784f9d-c98b-401c-ab35-a01fd812f19b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158p375T9M4FCse1N1cnM4g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 309,
      "cache_read_input_tokens": 24132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 309
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

File is outside the MCP whitelist. I'll read and edit it directly from the filesystem.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "41b01837-b749-4b07-bcd4-f430e9fa7baa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158p375T9M4FCse1N1cnM4g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 309,
      "cache_read_input_tokens": 24132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 309
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

<details open><summary>🔧 Tool call — Read · `toolu_01VufZWQjdUGk2JEKB2vHmg6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "4817219c-6ca8-4fe2-803c-0de4a74e4ccd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158p375T9M4FCse1N1cnM4g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 309,
      "cache_read_input_tokens": 24132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 309
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

_source line 13 · 2026-05-14T14:55:28.143Z_

<details><summary>↩ Tool result · `toolu_01VufZWQjdUGk2JEKB2vHmg6`</summary>

````text
1	# C5b Mitigation Pilot — Experiment Design
2	
3	> Claim: Phase-aware sparsity allocation recovers compound degradation
4	> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)
5	> Gate: >30% II recovery → full rollout; else → future work
6	> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)
7	
8	---
9	
10	## 1. Objective & Hypotheses
11	
12	**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.
13	
14	**Hypotheses**:
15	- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).
16	- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.
17	
18	**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.
19	
20	---
21	
22	## 2. Pilot Configuration
23	
24	| Parameter | Value | Rationale |
25	|-----------|-------|-----------|
26	| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |
27	| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |
28	| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |
29	| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |
30	| Bootstrap | B=10000 | Consistent with bf16 canonical data |
31	
32	**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.
33	
34	**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.
35	
36	---
37	
38	## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)
39	
40	**Phase-aware KV eviction + uniform head pruning**:
41	
42	- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.
43	- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.
44	- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.
45	- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.
46	
47	**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.
48	
49	---
50	
51	## 3. Experimental Conditions (per problem, per sparsity level)
52	
53	### 3.1 Condition A — Uniform Baseline (existing data)
54	
55	Standard importance-based compound sparsity at level s, applied uniformly across all phases.
56	
57	This is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.
58	
59	**Per-phase II_uniform(phase, s) from existing data**:
60	- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053
61	- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053
62	
63	### 3.2 Condition B — Oracle Phase-Aware Allocation
64	
65	Phase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.
66	
67	**KV eviction allocation rule** (compute-matched):
68	
69	Given target sparsity s and phases with token counts (n_exec, n_reas, n_trans):
70	
71	```
72	s_exec  = s - δ           (reduce sparsity in high-interaction phase)
73	s_reas  = s               (keep reasoning phase unchanged)
74	s_trans = s + δ'           (increase sparsity in low-interaction phase)
75	
76	Compute match constraint:
77	  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s
78	  → δ' = δ × (n_exec / n_trans)
79	```
80	
81	**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').
82	
83	| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |
84	|----------|--------|--------|------------------------------------------|
85	| 0.25 | 0.15 | 0.25 | ~0.35 |
86	| 0.30 | 0.20 | 0.30 | ~0.40 |
87	
88	Note: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.
89	
90	**Implementation**: For each problem:
91	1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)
92	2. Segment into phases (quantile-based, same as existing pipeline)
93	3. For each phase, generate importance-based masks at s_phase
94	4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens
95	5. Compute per-phase II under oracle allocation
96	
97	### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)
98	
99	Phase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform.
100	
101	```
102	phase_heuristic(token_pos) =
103	  "execution"  if token_pos / seq_len < 0.33
104	  "reasoning"  if 0.33 ≤ token_pos / seq_len < 0.67
105	  "transition" if token_pos / seq_len ≥ 0.67
106	```
107	
108	Same sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.
109	
110	**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a "thinking → calculating → summarizing" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.
111	
112	**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.
113	
114	---
115	
116	## 4. Evaluation Metrics
117	
118	### 4.1 Primary: II Recovery Percentage
119	
120	For each problem i, sparsity level s, and phase p:
121	
122	```
123	II_uniform(i, s, p)  = II under Condition A
124	II_oracle(i, s, p)   = II under Condition B
125	II_heuristic(i, s, p) = II under Condition C
126	```
127	
128	**Aggregate metric** (per sparsity level):
129	
130	```
131	recovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))
132	recovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))
133	```
134	
135	Where `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.
136	
137	### 4.2 Secondary: Per-Phase II Comparison
138	
139	Compare per-phase II between uniform and oracle:
140	- Execution phase: II should decrease (less sparsity → less compound interaction)
141	- Transition phase: II should stay low (already near zero, even with more sparsity)
142	- Net effect: overall weighted II decreases
143	
144	### 4.3 Gate Criterion
145	
146	```
147	PASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%
148	FAIL otherwise → C5b = "future work"
149	```
150	
151	If heuristic also exceeds 30%, that's a bonus result but not required for the gate.
152	
153	### 4.4 Statistical Test
154	
155	Paired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).
156	
157	---
158	
159	## 5. Implementation Plan
160	
161	### 5.1 Code Changes
162	
163	Create `run_mitigation_pilot.py` extending the existing profiling pipeline:
164	
165	```
166	pacs/profiling/run_mitigation_pilot.py
167	```
168	
169	**Key functions to add**:
170	
171	1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`
172	   - Returns per-phase sparsity levels, compute-matched
173	   - Caps s_trans at 0.50
174	
175	2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`
176	   - Token position ratio → phase assignment
177	   - Returns Phase objects compatible with existing pipeline
178	
179	3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`
180	   - Runs one problem under one condition
181	   - phase_method ∈ {"oracle", "heuristic"}
182	   - Returns per-phase II values and weighted aggregate
183	
184	**Reuse from existing pipeline**:
185	- `load_model_and_tokenizer()` — unchanged
186	- `stratified_sample_math500()` — take first 30
187	- `InteractionIndexCalculator` — core II computation, unchanged
188	- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels
189	- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity
190	- `compute_conditioned_perplexities()` — per-phase PPL computation
191	
192	**New logic** (~150 lines):
193	- Phase-aware sparsity allocation function
194	- Heuristic phase assignment function
195	- Main loop: for each problem × condition, generate phase-specific masks and compute II
196	- Output JSON with per-problem, per-condition II values
197	
198	### 5.2 Data Flow
199	
200	```
201	Input:
202	  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)
203	  - Existing bf16 profiling results for uniform baseline comparison
204	
205	Pipeline (per problem):
206	  1. Generate trace → segment phases (oracle) / assign phases (heuristic)
207	  2. For each phase:
208	     a. Compute phase-specific sparsity level (compute-matched)
209	     b. Generate importance masks at phase-specific level
210	     c. Forward pass with phase masks, extract phase-token PPL
211	     d. Compute phase II
212	  3. Compute weighted aggregate II
213	  4. Compare against uniform baseline II
214	
215	Output:
216	  - mitigation_pilot_results.json:
217	    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}
218	  - Summary statistics + gate evaluation
219	```
220	
221	### 5.3 Compatibility Notes
222	
223	- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.
224	- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.
225	- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.
226	
227	---
228	
229	## 6. GPU & Time Budget
230	
231	| Component | GPU Time | Notes |
232	|-----------|----------|-------|
233	| Model loading | 2 min | DeepSeek 7B bf16, single GPU |
234	| Generation (if needed) | 30 min | 30 problems × ~60s each |
235	| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |
236	| Heuristic condition | 30 min | Same as oracle |
237	| Analysis + bootstrap | 5 min | B=10000 on CPU |
238	| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |
239	
240	**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.
241	
242	**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).
243	
244	**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.
245	
246	---
247	
248	## 7. Expected Outcomes & Contingencies
249	
250	### Scenario A: Oracle recovery > 30% (PASS)
251	
252	- C5b enters paper as "phase-aware allocation recovers X% of compound degradation (oracle upper bound)"
253	- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair
254	- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)
255	
256	### Scenario B: Oracle recovery 10-30% (MARGINAL)
257	
258	- C5b enters Discussion (§6) as "phase-aware allocation shows promising but modest recovery"
259	- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding
260	- Frame full optimization as future work
261	
262	### Scenario C: Oracle recovery < 10% (FAIL)
263	
264	- C5b = future work, one sentence in Discussion
265	- Under Scheme C, this outcome has a clear interpretation: head pruning's fixed structural damage is the dominant source of compound severity, and phase-aware KV eviction alone cannot compensate. This is a meaningful negative result for §7 Discussion (compound interaction is primarily structural, not positional).
266	- Core claims C1-C6 unaffected — finding stands without mitigation
267	
268	### Risk: Generation trace mismatch
269	
270	If bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.
271	
272	---
273	
274	## 8. Output Artifacts
275	
276	| Artifact | Path | Description |
277	|----------|------|-------------|
278	| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |
279	| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |
280	| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |
281	
282	---
283	
284	## 9. Handoff Checklist for Coding Worker
285	
286	- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)
287	- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1
288	- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection
289	- [ ] **Scheme C**: Phase-aware δ allocation applies to **KV eviction only**; head pruning stays at uniform rate s for all phases and all conditions
290	- [ ] Use δ=0.10 for KV eviction phase-aware allocation, with s_trans capped at 0.50
291	- [ ] Compute-match constraint must hold exactly per-problem (not averaged), computed over KV eviction budget only
292	- [ ] Output format: JSON with per-problem breakdown + aggregate summary
293	- [ ] Register artifact after completion
294	- [ ] Run on single GPU, ~1.5h total wall time
295	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "09604635-2026-4b2d-89d0-91c91ff9feb0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
      "content": "# C5b Mitigation Pilot — Experiment Design\n\n> Claim: Phase-aware sparsity allocation recovers compound degradation\n> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)\n> Gate: >30% II recovery → full rollout; else → future work\n> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)\n\n---\n\n## 1. Objective & Hypotheses\n\n**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.\n\n**Hypotheses**:\n- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).\n- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.\n\n**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.\n\n---\n\n## 2. Pilot Configuration\n\n| Parameter | Value | Rationale |\n|-----------|-------|-----------|\n| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |\n| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |\n| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |\n| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |\n| Bootstrap | B=10000 | Consistent with bf16 canonical data |\n\n**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.\n\n**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.\n\n---\n\n## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)\n\n**Phase-aware KV eviction + uniform head pruning**:\n\n- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.\n- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.\n- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.\n- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.\n\n**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**KV eviction allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|\n| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.\n\n**Implementation**: For each problem:\n1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)\n2. Segment into phases (quantile-based, same as existing pipeline)\n3. For each phase, generate importance-based masks at s_phase\n4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens\n5. Compute per-phase II under oracle allocation\n\n### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform.\n\n```\nphase_heuristic(token_pos) =\n  \"execution\"  if token_pos / seq_len < 0.33\n  \"reasoning\"  if 0.33 ≤ token_pos / seq_len < 0.67\n  \"transition\" if token_pos / seq_len ≥ 0.67\n```\n\nSame sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.\n\n**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a \"thinking → calculating → summarizing\" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.\n\n**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.\n\n---\n\n## 4. Evaluation Metrics\n\n### 4.1 Primary: II Recovery Percentage\n\nFor each problem i, sparsity level s, and phase p:\n\n```\nII_uniform(i, s, p)  = II under Condition A\nII_oracle(i, s, p)   = II under Condition B\nII_heuristic(i, s, p) = II under Condition C\n```\n\n**Aggregate metric** (per sparsity level):\n\n```\nrecovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))\nrecovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))\n```\n\nWhere `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.\n\n### 4.2 Secondary: Per-Phase II Comparison\n\nCompare per-phase II between uniform and oracle:\n- Execution phase: II should decrease (less sparsity → less compound interaction)\n- Transition phase: II should stay low (already near zero, even with more sparsity)\n- Net effect: overall weighted II decreases\n\n### 4.3 Gate Criterion\n\n```\nPASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%\nFAIL otherwise → C5b = \"future work\"\n```\n\nIf heuristic also exceeds 30%, that's a bonus result but not required for the gate.\n\n### 4.4 Statistical Test\n\nPaired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).\n\n---\n\n## 5. Implementation Plan\n\n### 5.1 Code Changes\n\nCreate `run_mitigation_pilot.py` extending the existing profiling pipeline:\n\n```\npacs/profiling/run_mitigation_pilot.py\n```\n\n**Key functions to add**:\n\n1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`\n   - Returns per-phase sparsity levels, compute-matched\n   - Caps s_trans at 0.50\n\n2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`\n   - Token position ratio → phase assignment\n   - Returns Phase objects compatible with existing pipeline\n\n3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`\n   - Runs one problem under one condition\n   - phase_method ∈ {\"oracle\", \"heuristic\"}\n   - Returns per-phase II values and weighted aggregate\n\n**Reuse from existing pipeline**:\n- `load_model_and_tokenizer()` — unchanged\n- `stratified_sample_math500()` — take first 30\n- `InteractionIndexCalculator` — core II computation, unchanged\n- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels\n- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity\n- `compute_conditioned_perplexities()` — per-phase PPL computation\n\n**New logic** (~150 lines):\n- Phase-aware sparsity allocation function\n- Heuristic phase assignment function\n- Main loop: for each problem × condition, generate phase-specific masks and compute II\n- Output JSON with per-problem, per-condition II values\n\n### 5.2 Data Flow\n\n```\nInput:\n  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)\n  - Existing bf16 profiling results for uniform baseline comparison\n\nPipeline (per problem):\n  1. Generate trace → segment phases (oracle) / assign phases (heuristic)\n  2. For each phase:\n     a. Compute phase-specific sparsity level (compute-matched)\n     b. Generate importance masks at phase-specific level\n     c. Forward pass with phase masks, extract phase-token PPL\n     d. Compute phase II\n  3. Compute weighted aggregate II\n  4. Compare against uniform baseline II\n\nOutput:\n  - mitigation_pilot_results.json:\n    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}\n  - Summary statistics + gate evaluation\n```\n\n### 5.3 Compatibility Notes\n\n- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.\n- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.\n- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.\n\n---\n\n## 6. GPU & Time Budget\n\n| Component | GPU Time | Notes |\n|-----------|----------|-------|\n| Model loading | 2 min | DeepSeek 7B bf16, single GPU |\n| Generation (if needed) | 30 min | 30 problems × ~60s each |\n| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |\n| Heuristic condition | 30 min | Same as oracle |\n| Analysis + bootstrap | 5 min | B=10000 on CPU |\n| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |\n\n**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.\n\n**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).\n\n**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.\n\n---\n\n## 7. Expected Outcomes & Contingencies\n\n### Scenario A: Oracle recovery > 30% (PASS)\n\n- C5b enters paper as \"phase-aware allocation recovers X% of compound degradation (oracle upper bound)\"\n- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair\n- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)\n\n### Scenario B: Oracle recovery 10-30% (MARGINAL)\n\n- C5b enters Discussion (§6) as \"phase-aware allocation shows promising but modest recovery\"\n- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding\n- Frame full optimization as future work\n\n### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Under Scheme C, this outcome has a clear interpretation: head pruning's fixed structural damage is the dominant source of compound severity, and phase-aware KV eviction alone cannot compensate. This is a meaningful negative result for §7 Discussion (compound interaction is primarily structural, not positional).\n- Core claims C1-C6 unaffected — finding stands without mitigation\n\n### Risk: Generation trace mismatch\n\nIf bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.\n\n---\n\n## 8. Output Artifacts\n\n| Artifact | Path | Description |\n|----------|------|-------------|\n| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |\n| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |\n| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |\n\n---\n\n## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] **Scheme C**: Phase-aware δ allocation applies to **KV eviction only**; head pruning stays at uniform rate s for all phases and all conditions\n- [ ] Use δ=0.10 for KV eviction phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged), computed over KV eviction budget only\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time\n",
      "numLines": 295,
      "startLine": 1,
      "totalLines": 295
    }
  }
}
````

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full document. Let me plan the two revisions:

**Revision 1: Head pruning remains global uniform**

I need to:
1. In §3.2 and related places, add explicit statement about head pruning remaining uniform
2. Redefine the three conditions clearly
3. Ensure all mentions of oracle/heuristic are limited to KV eviction dimension

Looking at the document:
- §3.1 (Condition A): "Standard importance-based compound sparsity at level s, applied uniformly across all phases." → needs to be clarified as "uniform head pruning + uniform KV eviction"


- §3.2 (Condition B): Already mentions "Phase-dependent **KV eviction** sparsity" and "Head pruning remains at uniform rate s" - this is already somewhat aligned, but needs the explicit statement
- §3.3 (Condition C): Already mentions "only KV eviction sparsity varies by phase; head pruning remains uniform"

The document already has §2.5 describing Scheme C with uniform head pruning, and the three conditions already clarify this distinction. But I need to make it even more explicit with specific wording throughout. Now I'm identifying the exact locations where I should add revision markers and strengthen the language around head pruning uniformity versus phase-dependent KV eviction.

For the first revision, I'll add an explicit statement in §3.2 clarifying that phase-aware modulation applies only to KV eviction while head pruning stays uniform, then redefine the three conditions with the requested format and add a note about code impact.

For the second revision, I need to locate where the δ cap is mentioned and integrate the proportional rescale formula. I can see in §3.2 around line 88 there's a note about δ' being computed per-problem and s_trans being capped at 0.50 - that's where I should add the rescaling logic. I'll plan out the specific edits now, starting with adding a revision note block after the §3 header. I need to be precise about where these edits go. I'm adding a revision note right after the §3 header that clarifies the phase-aware modulation applies only to KV eviction, then redefining the three experimental conditions to make this distinction clear. After that, I'll update the note around line 88 to include the full rescaling logic for the heuristic approach. position-ratio heuristic KV eviction

Code impact: no modification to head mask forward pass needed; only KV eviction logic requires per-phase eviction rate switching. Code volume ~150 lines unchanged.

When δ exceeds the 0.50 cap, I need to rescale the effective delta to preserve the exact compute match. The revised approach computes an effective delta based on the cap, then adjusts both execution and transition phase sparsity accordingly so the total compute still equals the target. For cases where the original delta stays within bounds, I skip the rescale entirely, and if there's no transition phase, that phase gets skipped too. I'm clarifying the cap mechanism — it's actually s_trans that's capped at 0.50, not δ' directly. Since s_trans = s + δ', when this sum exceeds 0.50, we need to apply the cap to keep the transition phase sparsity bounded. When δ' exceeds 0.50, I cap it at that value, which means the execution phase sparsity becomes s - 0.50 × (n_trans / n_exec) and the transition phase uses s + 0.50. Let me verify this preserves the total compute: the terms rearrange to n_exec × s + n_reas × s + n_trans × s, which equals the original N_total × s, so the math checks out.

But I'm noticing the original document says "s_trans is capped at 0.50" directly, not the delta. If s = 0.25 and I cap δ' at 0.50, then s_trans = 0.75, which seems inconsistent with capping s_trans itself at 0.50. Re-reading the task description and the original line 88, I think the intent is to cap the actual sparsity value s_trans at 0.50 to prevent degenerate masking, not just the delta component.

The task specifies that when δ' exceeds 0.50, I should set δ_effective using cap = 0.50, then apply s_trans = s + cap and s_exec = s - δ_effective. For s = 0.25, this gives s_trans = 0.75, which the task explicitly requires even though it seems high. Let me verify this interpretation against the formula structure once more. I'm realizing the original doc caps s_trans at 0.50 total, but the revision caps δ' at 0.50 instead—a different approach using proportional rescaling. The task wants me to follow the revision exactly, so I'll stop second-guessing and just implement the specified changes. I need to insert the revision block into §3 and replace the Note line with the full rescale section, then finalize both edits. I'm checking whether the hypotheses in §1 need updating to specify KV eviction, but the task says to keep other parts unchanged except for the revision markers. The Scheme C section already makes it clear that we're talking about KV eviction, so I'll focus on adding the explicit statement in §3 and leave §1 as is. Now I'll make the two main edits cleanly — inserting the revision block after the §3 header to clarify that phase-aware modulation applies only to KV eviction while head pruning stays uniform. δ' is computed per-problem based on actual phase token counts to ensure exact compute match. When the raw δ' exceeds 0.50, I'm rescaling it proportionally so the compute-match constraint holds exactly—capping the effective δ at 0.50 and then adjusting the execution phase sparsity downward while keeping the transition phase adjustment at the cap.

I'm verifying this maintains the total compute by expanding the weighted sum across all phases and confirming it simplifies back to the baseline. I also need to handle edge cases: when δ doesn't exceed the cap, use the original formula; when there's no transition phase, fall back to uniform allocation; and ensure δ_effective stays non-negative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "5ab3f8c2-a467-4cfc-8d6c-c925c0469778",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4fzBbvNpjRbbqhyaaKRdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5182,
      "cache_read_input_tokens": 24441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5182
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

_source line 15_

Now I have the full document. I'll make both revisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "aaa70033-cb96-43e2-8397-fc1355ca5f86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4fzBbvNpjRbbqhyaaKRdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5182,
      "cache_read_input_tokens": 24441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5182
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

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_013k2mdi6BddHknEP6fPFTxp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "old_string": "## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)",
  "new_string": "## 3. Experimental Conditions (per problem, per sparsity level)\n\n> **Revision (Director 2026-05-14)**: Phase-aware modulation applies to KV eviction only; head pruning remains uniform across phases. Three-condition redefinition:\n> - (1) **Uniform baseline** = uniform head pruning + uniform KV eviction\n> - (2) **Oracle** = uniform head pruning + oracle phase-aware KV eviction (uses true phase labels to modulate KV eviction rate)\n> - (3) **Heuristic** = uniform head pruning + token-position-ratio heuristic KV eviction\n>\n> Code impact: no modification to head mask forward pass; only KV eviction logic requires per-phase eviction rate switching. ~150 lines unchanged.\n\n### 3.1 Condition A — Uniform Baseline (existing data)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "9e3e1b03-6ba5-4027-9a13-9437b15f6778",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4fzBbvNpjRbbqhyaaKRdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5182,
      "cache_read_input_tokens": 24441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5182
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

_source line 17 · 2026-05-14T14:56:44.744Z_

<details><summary>↩ Tool result · `toolu_013k2mdi6BddHknEP6fPFTxp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "9ffb067b-5033-4abc-a298-599ce088384e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
    "oldString": "## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)",
    "newString": "## 3. Experimental Conditions (per problem, per sparsity level)\n\n> **Revision (Director 2026-05-14)**: Phase-aware modulation applies to KV eviction only; head pruning remains uniform across phases. Three-condition redefinition:\n> - (1) **Uniform baseline** = uniform head pruning + uniform KV eviction\n> - (2) **Oracle** = uniform head pruning + oracle phase-aware KV eviction (uses true phase labels to modulate KV eviction rate)\n> - (3) **Heuristic** = uniform head pruning + token-position-ratio heuristic KV eviction\n>\n> Code impact: no modification to head mask forward pass; only KV eviction logic requires per-phase eviction rate switching. ~150 lines unchanged.\n\n### 3.1 Condition A — Uniform Baseline (existing data)",
    "originalFile": "# C5b Mitigation Pilot — Experiment Design\n\n> Claim: Phase-aware sparsity allocation recovers compound degradation\n> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)\n> Gate: >30% II recovery → full rollout; else → future work\n> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)\n\n---\n\n## 1. Objective & Hypotheses\n\n**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.\n\n**Hypotheses**:\n- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).\n- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.\n\n**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.\n\n---\n\n## 2. Pilot Configuration\n\n| Parameter | Value | Rationale |\n|-----------|-------|-----------|\n| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |\n| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |\n| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |\n| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |\n| Bootstrap | B=10000 | Consistent with bf16 canonical data |\n\n**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.\n\n**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.\n\n---\n\n## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)\n\n**Phase-aware KV eviction + uniform head pruning**:\n\n- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.\n- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.\n- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.\n- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.\n\n**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**KV eviction allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|\n| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.\n\n**Implementation**: For each problem:\n1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)\n2. Segment into phases (quantile-based, same as existing pipeline)\n3. For each phase, generate importance-based masks at s_phase\n4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens\n5. Compute per-phase II under oracle allocation\n\n### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform.\n\n```\nphase_heuristic(token_pos) =\n  \"execution\"  if token_pos / seq_len < 0.33\n  \"reasoning\"  if 0.33 ≤ token_pos / seq_len < 0.67\n  \"transition\" if token_pos / seq_len ≥ 0.67\n```\n\nSame sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.\n\n**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a \"thinking → calculating → summarizing\" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.\n\n**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.\n\n---\n\n## 4. Evaluation Metrics\n\n### 4.1 Primary: II Recovery Percentage\n\nFor each problem i, sparsity level s, and phase p:\n\n```\nII_uniform(i, s, p)  = II under Condition A\nII_oracle(i, s, p)   = II under Condition B\nII_heuristic(i, s, p) = II under Condition C\n```\n\n**Aggregate metric** (per sparsity level):\n\n```\nrecovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))\nrecovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))\n```\n\nWhere `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.\n\n### 4.2 Secondary: Per-Phase II Comparison\n\nCompare per-phase II between uniform and oracle:\n- Execution phase: II should decrease (less sparsity → less compound interaction)\n- Transition phase: II should stay low (already near zero, even with more sparsity)\n- Net effect: overall weighted II decreases\n\n### 4.3 Gate Criterion\n\n```\nPASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%\nFAIL otherwise → C5b = \"future work\"\n```\n\nIf heuristic also exceeds 30%, that's a bonus result but not required for the gate.\n\n### 4.4 Statistical Test\n\nPaired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).\n\n---\n\n## 5. Implementation Plan\n\n### 5.1 Code Changes\n\nCreate `run_mitigation_pilot.py` extending the existing profiling pipeline:\n\n```\npacs/profiling/run_mitigation_pilot.py\n```\n\n**Key functions to add**:\n\n1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`\n   - Returns per-phase sparsity levels, compute-matched\n   - Caps s_trans at 0.50\n\n2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`\n   - Token position ratio → phase assignment\n   - Returns Phase objects compatible with existing pipeline\n\n3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`\n   - Runs one problem under one condition\n   - phase_method ∈ {\"oracle\", \"heuristic\"}\n   - Returns per-phase II values and weighted aggregate\n\n**Reuse from existing pipeline**:\n- `load_model_and_tokenizer()` — unchanged\n- `stratified_sample_math500()` — take first 30\n- `InteractionIndexCalculator` — core II computation, unchanged\n- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels\n- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity\n- `compute_conditioned_perplexities()` — per-phase PPL computation\n\n**New logic** (~150 lines):\n- Phase-aware sparsity allocation function\n- Heuristic phase assignment function\n- Main loop: for each problem × condition, generate phase-specific masks and compute II\n- Output JSON with per-problem, per-condition II values\n\n### 5.2 Data Flow\n\n```\nInput:\n  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)\n  - Existing bf16 profiling results for uniform baseline comparison\n\nPipeline (per problem):\n  1. Generate trace → segment phases (oracle) / assign phases (heuristic)\n  2. For each phase:\n     a. Compute phase-specific sparsity level (compute-matched)\n     b. Generate importance masks at phase-specific level\n     c. Forward pass with phase masks, extract phase-token PPL\n     d. Compute phase II\n  3. Compute weighted aggregate II\n  4. Compare against uniform baseline II\n\nOutput:\n  - mitigation_pilot_results.json:\n    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}\n  - Summary statistics + gate evaluation\n```\n\n### 5.3 Compatibility Notes\n\n- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.\n- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.\n- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.\n\n---\n\n## 6. GPU & Time Budget\n\n| Component | GPU Time | Notes |\n|-----------|----------|-------|\n| Model loading | 2 min | DeepSeek 7B bf16, single GPU |\n| Generation (if needed) | 30 min | 30 problems × ~60s each |\n| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |\n| Heuristic condition | 30 min | Same as oracle |\n| Analysis + bootstrap | 5 min | B=10000 on CPU |\n| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |\n\n**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.\n\n**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).\n\n**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.\n\n---\n\n## 7. Expected Outcomes & Contingencies\n\n### Scenario A: Oracle recovery > 30% (PASS)\n\n- C5b enters paper as \"phase-aware allocation recovers X% of compound degradation (oracle upper bound)\"\n- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair\n- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)\n\n### Scenario B: Oracle recovery 10-30% (MARGINAL)\n\n- C5b enters Discussion (§6) as \"phase-aware allocation shows promising but modest recovery\"\n- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding\n- Frame full optimization as future work\n\n### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Under Scheme C, this outcome has a clear interpretation: head pruning's fixed structural damage is the dominant source of compound severity, and phase-aware KV eviction alone cannot compensate. This is a meaningful negative result for §7 Discussion (compound interaction is primarily structural, not positional).\n- Core claims C1-C6 unaffected — finding stands without mitigation\n\n### Risk: Generation trace mismatch\n\nIf bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.\n\n---\n\n## 8. Output Artifacts\n\n| Artifact | Path | Description |\n|----------|------|-------------|\n| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |\n| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |\n| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |\n\n---\n\n## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] **Scheme C**: Phase-aware δ allocation applies to **KV eviction only**; head pruning stays at uniform rate s for all phases and all conditions\n- [ ] Use δ=0.10 for KV eviction phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged), computed over KV eviction budget only\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time\n",
    "structuredPatch": [
      {
        "oldStart": 50,
        "oldLines": 6,
        "newStart": 50,
        "newLines": 13,
        "lines": [
          " ",
          " ## 3. Experimental Conditions (per problem, per sparsity level)",
          " ",
          "+> **Revision (Director 2026-05-14)**: Phase-aware modulation applies to KV eviction only; head pruning remains uniform across phases. Three-condition redefinition:",
          "+> - (1) **Uniform baseline** = uniform head pruning + uniform KV eviction",
          "+> - (2) **Oracle** = uniform head pruning + oracle phase-aware KV eviction (uses true phase labels to modulate KV eviction rate)",
          "+> - (3) **Heuristic** = uniform head pruning + token-position-ratio heuristic KV eviction",
          "+>",
          "+> Code impact: no modification to head mask forward pass; only KV eviction logic requires per-phase eviction rate switching. ~150 lines unchanged.",
          "+",
          " ### 3.1 Condition A — Uniform Baseline (existing data)",
          " ",
          " Standard importance-based compound sparsity at level s, applied uniformly across all phases."
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

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01YYeoqGKCUBFibPyLLJm6Ch`</summary>

````json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "old_string": "Note: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.",
  "new_string": "Note: δ' is computed per-problem based on actual phase token counts to ensure exact compute match.\n\n> **Revision (Director 2026-05-14)**: δ cap triggers proportional rescale to maintain exact compute match.\n>\n> Original: δ' = δ × (n_exec / n_trans), cap δ' at 0.50. Problem: after cap, compute-match constraint no longer holds exactly.\n>\n> Revised rescale rule — when δ × (n_exec / n_trans) > 0.50:\n> ```\n> cap = 0.50\n> δ_effective = cap × (n_trans / n_exec)\n> s_exec  = s - δ_effective          (execution phase KV eviction sparsity)\n> s_reas  = s                        (reasoning phase unchanged)\n> s_trans = s + cap                  (transition phase KV eviction sparsity)\n>\n> Verify: n_exec×(s - δ_effective) + n_reas×s + n_trans×(s + cap)\n>       = N_total×s - n_exec×δ_effective + n_trans×cap\n>       = N_total×s - n_exec×(cap×n_trans/n_exec) + n_trans×cap\n>       = N_total×s                  (exact match)\n> ```\n>\n> Boundary conditions:\n> - δ × (n_exec / n_trans) ≤ 0.50 → use original formula, no rescale needed\n> - n_trans = 0 → skip phase-aware allocation, fall back to uniform\n> - δ_effective ≥ 0 always holds when both n_exec, n_trans > 0"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "a8362c51-9f25-4d1b-a954-f6dbccc138a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015g3ZhmL3zVAcRLKvFLfHUa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4756,
      "cache_read_input_tokens": 29623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4756
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

### Runtime record

_source line 19_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1778778600,
    "rateLimitType": "five_hour",
    "utilization": 0.96,
    "isUsingOverage": false,
    "surpassedThreshold": 0.9
  },
  "uuid": "a4b4aee1-e7b9-452f-9962-b73752dfa813",
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc"
}
```

---

### Tool result

_source line 20 · 2026-05-14T14:56:51.428Z_

<details><summary>↩ Tool result · `toolu_01YYeoqGKCUBFibPyLLJm6Ch`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "dd86bf7c-97d9-42f0-80e7-993cf47e0e2b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
    "oldString": "Note: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.",
    "newString": "Note: δ' is computed per-problem based on actual phase token counts to ensure exact compute match.\n\n> **Revision (Director 2026-05-14)**: δ cap triggers proportional rescale to maintain exact compute match.\n>\n> Original: δ' = δ × (n_exec / n_trans), cap δ' at 0.50. Problem: after cap, compute-match constraint no longer holds exactly.\n>\n> Revised rescale rule — when δ × (n_exec / n_trans) > 0.50:\n> ```\n> cap = 0.50\n> δ_effective = cap × (n_trans / n_exec)\n> s_exec  = s - δ_effective          (execution phase KV eviction sparsity)\n> s_reas  = s                        (reasoning phase unchanged)\n> s_trans = s + cap                  (transition phase KV eviction sparsity)\n>\n> Verify: n_exec×(s - δ_effective) + n_reas×s + n_trans×(s + cap)\n>       = N_total×s - n_exec×δ_effective + n_trans×cap\n>       = N_total×s - n_exec×(cap×n_trans/n_exec) + n_trans×cap\n>       = N_total×s                  (exact match)\n> ```\n>\n> Boundary conditions:\n> - δ × (n_exec / n_trans) ≤ 0.50 → use original formula, no rescale needed\n> - n_trans = 0 → skip phase-aware allocation, fall back to uniform\n> - δ_effective ≥ 0 always holds when both n_exec, n_trans > 0",
    "originalFile": "# C5b Mitigation Pilot — Experiment Design\n\n> Claim: Phase-aware sparsity allocation recovers compound degradation\n> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)\n> Gate: >30% II recovery → full rollout; else → future work\n> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)\n\n---\n\n## 1. Objective & Hypotheses\n\n**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.\n\n**Hypotheses**:\n- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).\n- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.\n\n**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.\n\n---\n\n## 2. Pilot Configuration\n\n| Parameter | Value | Rationale |\n|-----------|-------|-----------|\n| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |\n| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |\n| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |\n| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |\n| Bootstrap | B=10000 | Consistent with bf16 canonical data |\n\n**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.\n\n**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.\n\n---\n\n## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)\n\n**Phase-aware KV eviction + uniform head pruning**:\n\n- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.\n- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.\n- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.\n- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.\n\n**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n> **Revision (Director 2026-05-14)**: Phase-aware modulation applies to KV eviction only; head pruning remains uniform across phases. Three-condition redefinition:\n> - (1) **Uniform baseline** = uniform head pruning + uniform KV eviction\n> - (2) **Oracle** = uniform head pruning + oracle phase-aware KV eviction (uses true phase labels to modulate KV eviction rate)\n> - (3) **Heuristic** = uniform head pruning + token-position-ratio heuristic KV eviction\n>\n> Code impact: no modification to head mask forward pass; only KV eviction logic requires per-phase eviction rate switching. ~150 lines unchanged.\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**KV eviction allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|\n| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.\n\n**Implementation**: For each problem:\n1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)\n2. Segment into phases (quantile-based, same as existing pipeline)\n3. For each phase, generate importance-based masks at s_phase\n4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens\n5. Compute per-phase II under oracle allocation\n\n### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform.\n\n```\nphase_heuristic(token_pos) =\n  \"execution\"  if token_pos / seq_len < 0.33\n  \"reasoning\"  if 0.33 ≤ token_pos / seq_len < 0.67\n  \"transition\" if token_pos / seq_len ≥ 0.67\n```\n\nSame sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.\n\n**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a \"thinking → calculating → summarizing\" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.\n\n**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.\n\n---\n\n## 4. Evaluation Metrics\n\n### 4.1 Primary: II Recovery Percentage\n\nFor each problem i, sparsity level s, and phase p:\n\n```\nII_uniform(i, s, p)  = II under Condition A\nII_oracle(i, s, p)   = II under Condition B\nII_heuristic(i, s, p) = II under Condition C\n```\n\n**Aggregate metric** (per sparsity level):\n\n```\nrecovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))\nrecovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))\n```\n\nWhere `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.\n\n### 4.2 Secondary: Per-Phase II Comparison\n\nCompare per-phase II between uniform and oracle:\n- Execution phase: II should decrease (less sparsity → less compound interaction)\n- Transition phase: II should stay low (already near zero, even with more sparsity)\n- Net effect: overall weighted II decreases\n\n### 4.3 Gate Criterion\n\n```\nPASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%\nFAIL otherwise → C5b = \"future work\"\n```\n\nIf heuristic also exceeds 30%, that's a bonus result but not required for the gate.\n\n### 4.4 Statistical Test\n\nPaired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).\n\n---\n\n## 5. Implementation Plan\n\n### 5.1 Code Changes\n\nCreate `run_mitigation_pilot.py` extending the existing profiling pipeline:\n\n```\npacs/profiling/run_mitigation_pilot.py\n```\n\n**Key functions to add**:\n\n1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`\n   - Returns per-phase sparsity levels, compute-matched\n   - Caps s_trans at 0.50\n\n2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`\n   - Token position ratio → phase assignment\n   - Returns Phase objects compatible with existing pipeline\n\n3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`\n   - Runs one problem under one condition\n   - phase_method ∈ {\"oracle\", \"heuristic\"}\n   - Returns per-phase II values and weighted aggregate\n\n**Reuse from existing pipeline**:\n- `load_model_and_tokenizer()` — unchanged\n- `stratified_sample_math500()` — take first 30\n- `InteractionIndexCalculator` — core II computation, unchanged\n- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels\n- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity\n- `compute_conditioned_perplexities()` — per-phase PPL computation\n\n**New logic** (~150 lines):\n- Phase-aware sparsity allocation function\n- Heuristic phase assignment function\n- Main loop: for each problem × condition, generate phase-specific masks and compute II\n- Output JSON with per-problem, per-condition II values\n\n### 5.2 Data Flow\n\n```\nInput:\n  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)\n  - Existing bf16 profiling results for uniform baseline comparison\n\nPipeline (per problem):\n  1. Generate trace → segment phases (oracle) / assign phases (heuristic)\n  2. For each phase:\n     a. Compute phase-specific sparsity level (compute-matched)\n     b. Generate importance masks at phase-specific level\n     c. Forward pass with phase masks, extract phase-token PPL\n     d. Compute phase II\n  3. Compute weighted aggregate II\n  4. Compare against uniform baseline II\n\nOutput:\n  - mitigation_pilot_results.json:\n    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}\n  - Summary statistics + gate evaluation\n```\n\n### 5.3 Compatibility Notes\n\n- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.\n- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.\n- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.\n\n---\n\n## 6. GPU & Time Budget\n\n| Component | GPU Time | Notes |\n|-----------|----------|-------|\n| Model loading | 2 min | DeepSeek 7B bf16, single GPU |\n| Generation (if needed) | 30 min | 30 problems × ~60s each |\n| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |\n| Heuristic condition | 30 min | Same as oracle |\n| Analysis + bootstrap | 5 min | B=10000 on CPU |\n| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |\n\n**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.\n\n**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).\n\n**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.\n\n---\n\n## 7. Expected Outcomes & Contingencies\n\n### Scenario A: Oracle recovery > 30% (PASS)\n\n- C5b enters paper as \"phase-aware allocation recovers X% of compound degradation (oracle upper bound)\"\n- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair\n- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)\n\n### Scenario B: Oracle recovery 10-30% (MARGINAL)\n\n- C5b enters Discussion (§6) as \"phase-aware allocation shows promising but modest recovery\"\n- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding\n- Frame full optimization as future work\n\n### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Under Scheme C, this outcome has a clear interpretation: head pruning's fixed structural damage is the dominant source of compound severity, and phase-aware KV eviction alone cannot compensate. This is a meaningful negative result for §7 Discussion (compound interaction is primarily structural, not positional).\n- Core claims C1-C6 unaffected — finding stands without mitigation\n\n### Risk: Generation trace mismatch\n\nIf bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.\n\n---\n\n## 8. Output Artifacts\n\n| Artifact | Path | Description |\n|----------|------|-------------|\n| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |\n| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |\n| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |\n\n---\n\n## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] **Scheme C**: Phase-aware δ allocation applies to **KV eviction only**; head pruning stays at uniform rate s for all phases and all conditions\n- [ ] Use δ=0.10 for KV eviction phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged), computed over KV eviction budget only\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time\n",
    "structuredPatch": [
      {
        "oldStart": 92,
        "oldLines": 8,
        "newStart": 92,
        "newLines": 31,
        "lines": [
          " | 0.25 | 0.15 | 0.25 | ~0.35 |",
          " | 0.30 | 0.20 | 0.30 | ~0.40 |",
          " ",
          "-Note: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.",
          "+Note: δ' is computed per-problem based on actual phase token counts to ensure exact compute match.",
          " ",
          "+> **Revision (Director 2026-05-14)**: δ cap triggers proportional rescale to maintain exact compute match.",
          "+>",
          "+> Original: δ' = δ × (n_exec / n_trans), cap δ' at 0.50. Problem: after cap, compute-match constraint no longer holds exactly.",
          "+>",
          "+> Revised rescale rule — when δ × (n_exec / n_trans) > 0.50:",
          "+> ```",
          "+> cap = 0.50",
          "+> δ_effective = cap × (n_trans / n_exec)",
          "+> s_exec  = s - δ_effective          (execution phase KV eviction sparsity)",
          "+> s_reas  = s                        (reasoning phase unchanged)",
          "+> s_trans = s + cap                  (transition phase KV eviction sparsity)",
          "+>",
          "+> Verify: n_exec×(s - δ_effective) + n_reas×s + n_trans×(s + cap)",
          "+>       = N_total×s - n_exec×δ_effective + n_trans×cap",
          "+>       = N_total×s - n_exec×(cap×n_trans/n_exec) + n_trans×cap",
          "+>       = N_total×s                  (exact match)",
          "+> ```",
          "+>",
          "+> Boundary conditions:",
          "+> - δ × (n_exec / n_trans) ≤ 0.50 → use original formula, no rescale needed",
          "+> - n_trans = 0 → skip phase-aware allocation, fall back to uniform",
          "+> - δ_effective ≥ 0 always holds when both n_exec, n_trans > 0",
          "+",
          " **Implementation**: For each problem:",
          " 1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)",
          " 2. Segment into phases (quantile-based, same as existing pipeline)"
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

_source line 21_

验证最终文档。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "3a933b89-4b00-4eb7-a90a-046b72487c58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Am8vnWa6GvakRtDsw2G5ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 34379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 668
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01KyKJCaKmfeY6bNDpjmY4tW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "offset": 50,
  "limit": 70
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "0d97035c-5558-4f7c-99ee-aee6dc140734",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Am8vnWa6GvakRtDsw2G5ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 34379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 668
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

_source line 23 · 2026-05-14T14:56:54.445Z_

<details><summary>↩ Tool result · `toolu_01KyKJCaKmfeY6bNDpjmY4tW`</summary>

````text
50	
51	## 3. Experimental Conditions (per problem, per sparsity level)
52	
53	> **Revision (Director 2026-05-14)**: Phase-aware modulation applies to KV eviction only; head pruning remains uniform across phases. Three-condition redefinition:
54	> - (1) **Uniform baseline** = uniform head pruning + uniform KV eviction
55	> - (2) **Oracle** = uniform head pruning + oracle phase-aware KV eviction (uses true phase labels to modulate KV eviction rate)
56	> - (3) **Heuristic** = uniform head pruning + token-position-ratio heuristic KV eviction
57	>
58	> Code impact: no modification to head mask forward pass; only KV eviction logic requires per-phase eviction rate switching. ~150 lines unchanged.
59	
60	### 3.1 Condition A — Uniform Baseline (existing data)
61	
62	Standard importance-based compound sparsity at level s, applied uniformly across all phases.
63	
64	This is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.
65	
66	**Per-phase II_uniform(phase, s) from existing data**:
67	- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053
68	- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053
69	
70	### 3.2 Condition B — Oracle Phase-Aware Allocation
71	
72	Phase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.
73	
74	**KV eviction allocation rule** (compute-matched):
75	
76	Given target sparsity s and phases with token counts (n_exec, n_reas, n_trans):
77	
78	```
79	s_exec  = s - δ           (reduce sparsity in high-interaction phase)
80	s_reas  = s               (keep reasoning phase unchanged)
81	s_trans = s + δ'           (increase sparsity in low-interaction phase)
82	
83	Compute match constraint:
84	  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s
85	  → δ' = δ × (n_exec / n_trans)
86	```
87	
88	**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').
89	
90	| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |
91	|----------|--------|--------|------------------------------------------|
92	| 0.25 | 0.15 | 0.25 | ~0.35 |
93	| 0.30 | 0.20 | 0.30 | ~0.40 |
94	
95	Note: δ' is computed per-problem based on actual phase token counts to ensure exact compute match.
96	
97	> **Revision (Director 2026-05-14)**: δ cap triggers proportional rescale to maintain exact compute match.
98	>
99	> Original: δ' = δ × (n_exec / n_trans), cap δ' at 0.50. Problem: after cap, compute-match constraint no longer holds exactly.
100	>
101	> Revised rescale rule — when δ × (n_exec / n_trans) > 0.50:
102	> ```
103	> cap = 0.50
104	> δ_effective = cap × (n_trans / n_exec)
105	> s_exec  = s - δ_effective          (execution phase KV eviction sparsity)
106	> s_reas  = s                        (reasoning phase unchanged)
107	> s_trans = s + cap                  (transition phase KV eviction sparsity)
108	>
109	> Verify: n_exec×(s - δ_effective) + n_reas×s + n_trans×(s + cap)
110	>       = N_total×s - n_exec×δ_effective + n_trans×cap
111	>       = N_total×s - n_exec×(cap×n_trans/n_exec) + n_trans×cap
112	>       = N_total×s                  (exact match)
113	> ```
114	>
115	> Boundary conditions:
116	> - δ × (n_exec / n_trans) ≤ 0.50 → use original formula, no rescale needed
117	> - n_trans = 0 → skip phase-aware allocation, fall back to uniform
118	> - δ_effective ≥ 0 always holds when both n_exec, n_trans > 0
119	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "1b2a862d-78cc-4155-9ca0-fd2fd6272213",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
      "content": "\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n> **Revision (Director 2026-05-14)**: Phase-aware modulation applies to KV eviction only; head pruning remains uniform across phases. Three-condition redefinition:\n> - (1) **Uniform baseline** = uniform head pruning + uniform KV eviction\n> - (2) **Oracle** = uniform head pruning + oracle phase-aware KV eviction (uses true phase labels to modulate KV eviction rate)\n> - (3) **Heuristic** = uniform head pruning + token-position-ratio heuristic KV eviction\n>\n> Code impact: no modification to head mask forward pass; only KV eviction logic requires per-phase eviction rate switching. ~150 lines unchanged.\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**KV eviction allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|\n| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match.\n\n> **Revision (Director 2026-05-14)**: δ cap triggers proportional rescale to maintain exact compute match.\n>\n> Original: δ' = δ × (n_exec / n_trans), cap δ' at 0.50. Problem: after cap, compute-match constraint no longer holds exactly.\n>\n> Revised rescale rule — when δ × (n_exec / n_trans) > 0.50:\n> ```\n> cap = 0.50\n> δ_effective = cap × (n_trans / n_exec)\n> s_exec  = s - δ_effective          (execution phase KV eviction sparsity)\n> s_reas  = s                        (reasoning phase unchanged)\n> s_trans = s + cap                  (transition phase KV eviction sparsity)\n>\n> Verify: n_exec×(s - δ_effective) + n_reas×s + n_trans×(s + cap)\n>       = N_total×s - n_exec×δ_effective + n_trans×cap\n>       = N_total×s - n_exec×(cap×n_trans/n_exec) + n_trans×cap\n>       = N_total×s                  (exact match)\n> ```\n>\n> Boundary conditions:\n> - δ × (n_exec / n_trans) ≤ 0.50 → use original formula, no rescale needed\n> - n_trans = 0 → skip phase-aware allocation, fall back to uniform\n> - δ_effective ≥ 0 always holds when both n_exec, n_trans > 0\n",
      "numLines": 70,
      "startLine": 50,
      "totalLines": 325
    }
  }
}
````

</details>

---

### Assistant

_source line 24_

两项修订已写入 `c5b_pilot_design.md`：

1. **§3 头部**：添加 Revision 块，明确 phase-aware modulation 仅适用于 KV eviction，head pruning 保持 uniform；三条件重新定义为 (1) uniform+uniform, (2) uniform+oracle KV, (3) uniform+heuristic KV；标注代码影响不变。

2. **§3.2 δ cap 处**：原 "s_trans capped at 0.50" 替换为 proportional rescale 公式——cap 触发时反求 δ_effective = cap × (n_trans / n_exec)，确保总 compute 精确匹配。含验证推导和三项边界条件。

文档其余部分（含 Scheme C 段落）未改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "uuid": "a41dd3e0-79c6-40eb-85ad-198b1a686072",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDKEsLuzSEkNhpDGMFmZJe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1582,
      "cache_read_input_tokens": 35047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1582
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

_source line 25_

两项修订已写入 `c5b_pilot_design.md`：

1. **§3 头部**：添加 Revision 块，明确 phase-aware modulation 仅适用于 KV eviction，head pruning 保持 uniform；三条件重新定义为 (1) uniform+uniform, (2) uniform+oracle KV, (3) uniform+heuristic KV；标注代码影响不变。

2. **§3.2 δ cap 处**：原 "s_trans capped at 0.50" 替换为 proportional rescale 公式——cap 触发时反求 δ_effective = cap × (n_trans / n_exec)，确保总 compute 精确匹配。含验证推导和三项边界条件。

文档其余部分（含 Scheme C 段落）未改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 103771,
  "duration_api_ms": 104822,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "40f97d6c-ab98-4c0f-a8ce-1b9207c24fbc",
  "total_cost_usd": 0.40206450000000005,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 25182,
    "cache_read_input_tokens": 182492,
    "output_tokens": 6075,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25182,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 230,
        "cache_read_input_tokens": 35047,
        "cache_creation_input_tokens": 1582,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1582
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1421,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001501,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 6075,
      "cacheReadInputTokens": 182492,
      "cacheCreationInputTokens": 25182,
      "webSearchRequests": 0,
      "costUSD": 0.4005635000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "81e5102b-a296-4f0f-93ac-84595662f5b3"
}
```

</details>

---
