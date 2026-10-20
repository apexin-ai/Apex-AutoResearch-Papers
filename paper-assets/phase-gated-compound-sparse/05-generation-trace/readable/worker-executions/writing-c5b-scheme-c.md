# writing c5b scheme c

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_writing_c5b_scheme_c_20260514T145226.log`
- **Structured JSON:** [`c01ad0f9cebdbb0240f1.json`](../../sessions/c0/c01ad0f9cebdbb0240f1.json)

## Before a recorded user message

40 recorded events

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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
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
    "mcp__agent-ml-research__list_artifacts",
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
  "uuid": "0e54451c-9bab-4a01-900a-dde0ad6cd9aa",
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
    "resetsAt": 1778911200,
    "rateLimitType": "seven_day",
    "utilization": 0.78,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "9489c54d-8e6e-4ec6-82af-cb6a0d111fdd",
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1"
}
```

---

### Assistant

_source line 4_

I'll read the current design document first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "c285a057-0d09-4c4a-9fc7-b98dbf6a7527",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKeFZp4WjeqDUqQiheVkyq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11904,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11904
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KxSvgjfxp8YNwZnCPW7vho`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__list_artifacts",
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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "420f9804-2aa9-4c98-8736-e894b31f4b71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKeFZp4WjeqDUqQiheVkyq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11904,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11904
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

_source line 6 · 2026-05-14T14:52:37.907Z_

<details><summary>↩ Tool result · `toolu_01KxSvgjfxp8YNwZnCPW7vho`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__list_artifacts"
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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "4b73e333-083f-4947-8b99-b4c0007012e3",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__list_artifacts"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__list_artifacts",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016TZKtdSrRHchYVVY2SWZey`</summary>

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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "ad1f3e67-a6f7-474e-be96-7bfafd453265",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cQ8rqZYsYPDCG5ZT6WsZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1022,
      "cache_read_input_tokens": 23351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1022
      },
      "output_tokens": 73,
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

_source line 8 · 2026-05-14T14:52:40.910Z_

<details><summary>↩ Tool result · `toolu_016TZKtdSrRHchYVVY2SWZey`</summary>

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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "d7ea8ea5-4dc5-4450-aa19-eab604a51866",
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

_source line 9_

The file isn't readable via `read_project_file`. Let me read it directly from the filesystem.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "4ba55837-66d2-45b5-a91a-4693f3a9579e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RD4VsixnpG8yhtGHqnYMV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 24373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01KxSG381s8UnHCKpheg4HL5`</summary>

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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "871fc249-a986-47de-ba9c-6c0ad9a76a6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RD4VsixnpG8yhtGHqnYMV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 24373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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

_source line 11 · 2026-05-14T14:52:44.208Z_

<details><summary>↩ Tool result · `toolu_01KxSG381s8UnHCKpheg4HL5`</summary>

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
38	## 3. Experimental Conditions (per problem, per sparsity level)
39	
40	### 3.1 Condition A — Uniform Baseline (existing data)
41	
42	Standard importance-based compound sparsity at level s, applied uniformly across all phases.
43	
44	This is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.
45	
46	**Per-phase II_uniform(phase, s) from existing data**:
47	- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053
48	- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053
49	
50	### 3.2 Condition B — Oracle Phase-Aware Allocation
51	
52	Phase-dependent sparsity using **true quantile-based phase labels** (from attention sparsity during generation). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.
53	
54	**Allocation rule** (compute-matched):
55	
56	Given target sparsity s and phases with token counts (n_exec, n_reas, n_trans):
57	
58	```
59	s_exec  = s - δ           (reduce sparsity in high-interaction phase)
60	s_reas  = s               (keep reasoning phase unchanged)
61	s_trans = s + δ'           (increase sparsity in low-interaction phase)
62	
63	Compute match constraint:
64	  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s
65	  → δ' = δ × (n_exec / n_trans)
66	```
67	
68	**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').
69	
70	| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |
71	|----------|--------|--------|------------------------------------------|
72	| 0.25 | 0.15 | 0.25 | ~0.35 |
73	| 0.30 | 0.20 | 0.30 | ~0.40 |
74	
75	Note: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.
76	
77	**Implementation**: For each problem:
78	1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)
79	2. Segment into phases (quantile-based, same as existing pipeline)
80	3. For each phase, generate importance-based masks at s_phase
81	4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens
82	5. Compute per-phase II under oracle allocation
83	
84	### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)
85	
86	Phase assignment using **normalized generation position** as a zero-cost proxy:
87	
88	```
89	phase_heuristic(token_pos) =
90	  "execution"  if token_pos / seq_len < 0.33
91	  "reasoning"  if 0.33 ≤ token_pos / seq_len < 0.67
92	  "transition" if token_pos / seq_len ≥ 0.67
93	```
94	
95	Same sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.
96	
97	**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a "thinking → calculating → summarizing" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.
98	
99	**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.
100	
101	---
102	
103	## 4. Evaluation Metrics
104	
105	### 4.1 Primary: II Recovery Percentage
106	
107	For each problem i, sparsity level s, and phase p:
108	
109	```
110	II_uniform(i, s, p)  = II under Condition A
111	II_oracle(i, s, p)   = II under Condition B
112	II_heuristic(i, s, p) = II under Condition C
113	```
114	
115	**Aggregate metric** (per sparsity level):
116	
117	```
118	recovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))
119	recovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))
120	```
121	
122	Where `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.
123	
124	### 4.2 Secondary: Per-Phase II Comparison
125	
126	Compare per-phase II between uniform and oracle:
127	- Execution phase: II should decrease (less sparsity → less compound interaction)
128	- Transition phase: II should stay low (already near zero, even with more sparsity)
129	- Net effect: overall weighted II decreases
130	
131	### 4.3 Gate Criterion
132	
133	```
134	PASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%
135	FAIL otherwise → C5b = "future work"
136	```
137	
138	If heuristic also exceeds 30%, that's a bonus result but not required for the gate.
139	
140	### 4.4 Statistical Test
141	
142	Paired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).
143	
144	---
145	
146	## 5. Implementation Plan
147	
148	### 5.1 Code Changes
149	
150	Create `run_mitigation_pilot.py` extending the existing profiling pipeline:
151	
152	```
153	pacs/profiling/run_mitigation_pilot.py
154	```
155	
156	**Key functions to add**:
157	
158	1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`
159	   - Returns per-phase sparsity levels, compute-matched
160	   - Caps s_trans at 0.50
161	
162	2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`
163	   - Token position ratio → phase assignment
164	   - Returns Phase objects compatible with existing pipeline
165	
166	3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`
167	   - Runs one problem under one condition
168	   - phase_method ∈ {"oracle", "heuristic"}
169	   - Returns per-phase II values and weighted aggregate
170	
171	**Reuse from existing pipeline**:
172	- `load_model_and_tokenizer()` — unchanged
173	- `stratified_sample_math500()` — take first 30
174	- `InteractionIndexCalculator` — core II computation, unchanged
175	- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels
176	- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity
177	- `compute_conditioned_perplexities()` — per-phase PPL computation
178	
179	**New logic** (~150 lines):
180	- Phase-aware sparsity allocation function
181	- Heuristic phase assignment function
182	- Main loop: for each problem × condition, generate phase-specific masks and compute II
183	- Output JSON with per-problem, per-condition II values
184	
185	### 5.2 Data Flow
186	
187	```
188	Input:
189	  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)
190	  - Existing bf16 profiling results for uniform baseline comparison
191	
192	Pipeline (per problem):
193	  1. Generate trace → segment phases (oracle) / assign phases (heuristic)
194	  2. For each phase:
195	     a. Compute phase-specific sparsity level (compute-matched)
196	     b. Generate importance masks at phase-specific level
197	     c. Forward pass with phase masks, extract phase-token PPL
198	     d. Compute phase II
199	  3. Compute weighted aggregate II
200	  4. Compare against uniform baseline II
201	
202	Output:
203	  - mitigation_pilot_results.json:
204	    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}
205	  - Summary statistics + gate evaluation
206	```
207	
208	### 5.3 Compatibility Notes
209	
210	- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.
211	- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.
212	- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.
213	
214	---
215	
216	## 6. GPU & Time Budget
217	
218	| Component | GPU Time | Notes |
219	|-----------|----------|-------|
220	| Model loading | 2 min | DeepSeek 7B bf16, single GPU |
221	| Generation (if needed) | 30 min | 30 problems × ~60s each |
222	| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |
223	| Heuristic condition | 30 min | Same as oracle |
224	| Analysis + bootstrap | 5 min | B=10000 on CPU |
225	| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |
226	
227	**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.
228	
229	**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).
230	
231	**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.
232	
233	---
234	
235	## 7. Expected Outcomes & Contingencies
236	
237	### Scenario A: Oracle recovery > 30% (PASS)
238	
239	- C5b enters paper as "phase-aware allocation recovers X% of compound degradation (oracle upper bound)"
240	- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair
241	- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)
242	
243	### Scenario B: Oracle recovery 10-30% (MARGINAL)
244	
245	- C5b enters Discussion (§6) as "phase-aware allocation shows promising but modest recovery"
246	- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding
247	- Frame full optimization as future work
248	
249	### Scenario C: Oracle recovery < 10% (FAIL)
250	
251	- C5b = future work, one sentence in Discussion
252	- Possible explanations: (1) compound interaction at phase boundaries blurs the effect; (2) head pruning mask is global (can't be phase-specific); (3) KV eviction phase-awareness alone is insufficient
253	- Core claims C1-C6 unaffected — finding stands without mitigation
254	
255	### Risk: Generation trace mismatch
256	
257	If bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.
258	
259	---
260	
261	## 8. Output Artifacts
262	
263	| Artifact | Path | Description |
264	|----------|------|-------------|
265	| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |
266	| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |
267	| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |
268	
269	---
270	
271	## 9. Handoff Checklist for Coding Worker
272	
273	- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)
274	- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1
275	- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection
276	- [ ] Use δ=0.10 for phase-aware allocation, with s_trans capped at 0.50
277	- [ ] Compute-match constraint must hold exactly per-problem (not averaged)
278	- [ ] Output format: JSON with per-problem breakdown + aggregate summary
279	- [ ] Register artifact after completion
280	- [ ] Run on single GPU, ~1.5h total wall time
281	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "296a0797-c0cc-476a-8647-fbc2841c8210",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
      "content": "# C5b Mitigation Pilot — Experiment Design\n\n> Claim: Phase-aware sparsity allocation recovers compound degradation\n> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)\n> Gate: >30% II recovery → full rollout; else → future work\n> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)\n\n---\n\n## 1. Objective & Hypotheses\n\n**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.\n\n**Hypotheses**:\n- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).\n- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.\n\n**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.\n\n---\n\n## 2. Pilot Configuration\n\n| Parameter | Value | Rationale |\n|-----------|-------|-----------|\n| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |\n| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |\n| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |\n| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |\n| Bootstrap | B=10000 | Consistent with bf16 canonical data |\n\n**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.\n\n**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent sparsity using **true quantile-based phase labels** (from attention sparsity during generation). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**Allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|\n| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.\n\n**Implementation**: For each problem:\n1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)\n2. Segment into phases (quantile-based, same as existing pipeline)\n3. For each phase, generate importance-based masks at s_phase\n4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens\n5. Compute per-phase II under oracle allocation\n\n### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy:\n\n```\nphase_heuristic(token_pos) =\n  \"execution\"  if token_pos / seq_len < 0.33\n  \"reasoning\"  if 0.33 ≤ token_pos / seq_len < 0.67\n  \"transition\" if token_pos / seq_len ≥ 0.67\n```\n\nSame sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.\n\n**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a \"thinking → calculating → summarizing\" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.\n\n**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.\n\n---\n\n## 4. Evaluation Metrics\n\n### 4.1 Primary: II Recovery Percentage\n\nFor each problem i, sparsity level s, and phase p:\n\n```\nII_uniform(i, s, p)  = II under Condition A\nII_oracle(i, s, p)   = II under Condition B\nII_heuristic(i, s, p) = II under Condition C\n```\n\n**Aggregate metric** (per sparsity level):\n\n```\nrecovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))\nrecovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))\n```\n\nWhere `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.\n\n### 4.2 Secondary: Per-Phase II Comparison\n\nCompare per-phase II between uniform and oracle:\n- Execution phase: II should decrease (less sparsity → less compound interaction)\n- Transition phase: II should stay low (already near zero, even with more sparsity)\n- Net effect: overall weighted II decreases\n\n### 4.3 Gate Criterion\n\n```\nPASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%\nFAIL otherwise → C5b = \"future work\"\n```\n\nIf heuristic also exceeds 30%, that's a bonus result but not required for the gate.\n\n### 4.4 Statistical Test\n\nPaired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).\n\n---\n\n## 5. Implementation Plan\n\n### 5.1 Code Changes\n\nCreate `run_mitigation_pilot.py` extending the existing profiling pipeline:\n\n```\npacs/profiling/run_mitigation_pilot.py\n```\n\n**Key functions to add**:\n\n1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`\n   - Returns per-phase sparsity levels, compute-matched\n   - Caps s_trans at 0.50\n\n2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`\n   - Token position ratio → phase assignment\n   - Returns Phase objects compatible with existing pipeline\n\n3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`\n   - Runs one problem under one condition\n   - phase_method ∈ {\"oracle\", \"heuristic\"}\n   - Returns per-phase II values and weighted aggregate\n\n**Reuse from existing pipeline**:\n- `load_model_and_tokenizer()` — unchanged\n- `stratified_sample_math500()` — take first 30\n- `InteractionIndexCalculator` — core II computation, unchanged\n- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels\n- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity\n- `compute_conditioned_perplexities()` — per-phase PPL computation\n\n**New logic** (~150 lines):\n- Phase-aware sparsity allocation function\n- Heuristic phase assignment function\n- Main loop: for each problem × condition, generate phase-specific masks and compute II\n- Output JSON with per-problem, per-condition II values\n\n### 5.2 Data Flow\n\n```\nInput:\n  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)\n  - Existing bf16 profiling results for uniform baseline comparison\n\nPipeline (per problem):\n  1. Generate trace → segment phases (oracle) / assign phases (heuristic)\n  2. For each phase:\n     a. Compute phase-specific sparsity level (compute-matched)\n     b. Generate importance masks at phase-specific level\n     c. Forward pass with phase masks, extract phase-token PPL\n     d. Compute phase II\n  3. Compute weighted aggregate II\n  4. Compare against uniform baseline II\n\nOutput:\n  - mitigation_pilot_results.json:\n    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}\n  - Summary statistics + gate evaluation\n```\n\n### 5.3 Compatibility Notes\n\n- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.\n- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.\n- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.\n\n---\n\n## 6. GPU & Time Budget\n\n| Component | GPU Time | Notes |\n|-----------|----------|-------|\n| Model loading | 2 min | DeepSeek 7B bf16, single GPU |\n| Generation (if needed) | 30 min | 30 problems × ~60s each |\n| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |\n| Heuristic condition | 30 min | Same as oracle |\n| Analysis + bootstrap | 5 min | B=10000 on CPU |\n| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |\n\n**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.\n\n**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).\n\n**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.\n\n---\n\n## 7. Expected Outcomes & Contingencies\n\n### Scenario A: Oracle recovery > 30% (PASS)\n\n- C5b enters paper as \"phase-aware allocation recovers X% of compound degradation (oracle upper bound)\"\n- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair\n- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)\n\n### Scenario B: Oracle recovery 10-30% (MARGINAL)\n\n- C5b enters Discussion (§6) as \"phase-aware allocation shows promising but modest recovery\"\n- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding\n- Frame full optimization as future work\n\n### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Possible explanations: (1) compound interaction at phase boundaries blurs the effect; (2) head pruning mask is global (can't be phase-specific); (3) KV eviction phase-awareness alone is insufficient\n- Core claims C1-C6 unaffected — finding stands without mitigation\n\n### Risk: Generation trace mismatch\n\nIf bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.\n\n---\n\n## 8. Output Artifacts\n\n| Artifact | Path | Description |\n|----------|------|-------------|\n| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |\n| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |\n| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |\n\n---\n\n## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] Use δ=0.10 for phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged)\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time\n",
      "numLines": 281,
      "startLine": 1,
      "totalLines": 281
    }
  }
}
````

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I need to update this document to add the Scheme C decision. I need to:

1. Add a new section about Implementation Scheme C
2. Make sure the existing conditions description is consistent with Scheme C

Looking at the document, Scheme C means:
- KV eviction: phase-aware (per-position, varies by phase)
- Head pruning: uniform (global, doesn't vary by phase)

The existing document describes oracle/heuristic conditions that adjust sparsity levels per phase. I need to clarify that these adjustments apply to KV eviction only, while head pruning remains uniform.


I'm deciding where to insert this new section. The most logical placement would be between the pilot configuration and the experimental conditions, so it frames the setup clearly before diving into the specific conditions. I need the next thinking content to rewrite. You've provided the instructions and my current rewritten thinking, but I don't see the "next thinking" that I should be rewriting.

Could you please share the next thinking chunk that needs to be rewritten?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "dd83bfa8-c792-4e2b-b57a-d68874b0c7bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZ3TYhhb8cfkUivn8YVgaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4698,
      "cache_read_input_tokens": 24660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4698
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

Now I'll update the document. I need to:
1. Insert the Scheme C decision section between §2 and §3
2. Add clarifying notes in the conditions to make explicit that phase-aware allocation applies to KV eviction only

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "2bcd5431-c1ee-4db9-90e5-77133de82d07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZ3TYhhb8cfkUivn8YVgaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4698,
      "cache_read_input_tokens": 24660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4698
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

<details open><summary>🔧 Tool call — Edit · `toolu_019G4bAwhRy3Bs14NkoxWduF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "old_string": "---\n\n## 3. Experimental Conditions (per problem, per sparsity level)",
  "new_string": "---\n\n## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)\n\n**Phase-aware KV eviction + uniform head pruning**:\n\n- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.\n- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.\n- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.\n- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.\n\n**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "dc72454e-6c02-41d3-98d4-48d8f2aa4fb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZ3TYhhb8cfkUivn8YVgaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4698,
      "cache_read_input_tokens": 24660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4698
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

_source line 15 · 2026-05-14T14:53:08.669Z_

<details><summary>↩ Tool result · `toolu_019G4bAwhRy3Bs14NkoxWduF`</summary>

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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "8b7cc767-adc7-44d0-8ac7-6a14f70a45aa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
    "oldString": "---\n\n## 3. Experimental Conditions (per problem, per sparsity level)",
    "newString": "---\n\n## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)\n\n**Phase-aware KV eviction + uniform head pruning**:\n\n- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.\n- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.\n- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.\n- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.\n\n**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)",
    "originalFile": "# C5b Mitigation Pilot — Experiment Design\n\n> Claim: Phase-aware sparsity allocation recovers compound degradation\n> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)\n> Gate: >30% II recovery → full rollout; else → future work\n> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)\n\n---\n\n## 1. Objective & Hypotheses\n\n**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.\n\n**Hypotheses**:\n- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).\n- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.\n\n**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.\n\n---\n\n## 2. Pilot Configuration\n\n| Parameter | Value | Rationale |\n|-----------|-------|-----------|\n| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |\n| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |\n| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |\n| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |\n| Bootstrap | B=10000 | Consistent with bf16 canonical data |\n\n**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.\n\n**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent sparsity using **true quantile-based phase labels** (from attention sparsity during generation). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**Allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|\n| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.\n\n**Implementation**: For each problem:\n1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)\n2. Segment into phases (quantile-based, same as existing pipeline)\n3. For each phase, generate importance-based masks at s_phase\n4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens\n5. Compute per-phase II under oracle allocation\n\n### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy:\n\n```\nphase_heuristic(token_pos) =\n  \"execution\"  if token_pos / seq_len < 0.33\n  \"reasoning\"  if 0.33 ≤ token_pos / seq_len < 0.67\n  \"transition\" if token_pos / seq_len ≥ 0.67\n```\n\nSame sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.\n\n**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a \"thinking → calculating → summarizing\" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.\n\n**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.\n\n---\n\n## 4. Evaluation Metrics\n\n### 4.1 Primary: II Recovery Percentage\n\nFor each problem i, sparsity level s, and phase p:\n\n```\nII_uniform(i, s, p)  = II under Condition A\nII_oracle(i, s, p)   = II under Condition B\nII_heuristic(i, s, p) = II under Condition C\n```\n\n**Aggregate metric** (per sparsity level):\n\n```\nrecovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))\nrecovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))\n```\n\nWhere `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.\n\n### 4.2 Secondary: Per-Phase II Comparison\n\nCompare per-phase II between uniform and oracle:\n- Execution phase: II should decrease (less sparsity → less compound interaction)\n- Transition phase: II should stay low (already near zero, even with more sparsity)\n- Net effect: overall weighted II decreases\n\n### 4.3 Gate Criterion\n\n```\nPASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%\nFAIL otherwise → C5b = \"future work\"\n```\n\nIf heuristic also exceeds 30%, that's a bonus result but not required for the gate.\n\n### 4.4 Statistical Test\n\nPaired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).\n\n---\n\n## 5. Implementation Plan\n\n### 5.1 Code Changes\n\nCreate `run_mitigation_pilot.py` extending the existing profiling pipeline:\n\n```\npacs/profiling/run_mitigation_pilot.py\n```\n\n**Key functions to add**:\n\n1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`\n   - Returns per-phase sparsity levels, compute-matched\n   - Caps s_trans at 0.50\n\n2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`\n   - Token position ratio → phase assignment\n   - Returns Phase objects compatible with existing pipeline\n\n3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`\n   - Runs one problem under one condition\n   - phase_method ∈ {\"oracle\", \"heuristic\"}\n   - Returns per-phase II values and weighted aggregate\n\n**Reuse from existing pipeline**:\n- `load_model_and_tokenizer()` — unchanged\n- `stratified_sample_math500()` — take first 30\n- `InteractionIndexCalculator` — core II computation, unchanged\n- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels\n- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity\n- `compute_conditioned_perplexities()` — per-phase PPL computation\n\n**New logic** (~150 lines):\n- Phase-aware sparsity allocation function\n- Heuristic phase assignment function\n- Main loop: for each problem × condition, generate phase-specific masks and compute II\n- Output JSON with per-problem, per-condition II values\n\n### 5.2 Data Flow\n\n```\nInput:\n  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)\n  - Existing bf16 profiling results for uniform baseline comparison\n\nPipeline (per problem):\n  1. Generate trace → segment phases (oracle) / assign phases (heuristic)\n  2. For each phase:\n     a. Compute phase-specific sparsity level (compute-matched)\n     b. Generate importance masks at phase-specific level\n     c. Forward pass with phase masks, extract phase-token PPL\n     d. Compute phase II\n  3. Compute weighted aggregate II\n  4. Compare against uniform baseline II\n\nOutput:\n  - mitigation_pilot_results.json:\n    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}\n  - Summary statistics + gate evaluation\n```\n\n### 5.3 Compatibility Notes\n\n- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.\n- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.\n- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.\n\n---\n\n## 6. GPU & Time Budget\n\n| Component | GPU Time | Notes |\n|-----------|----------|-------|\n| Model loading | 2 min | DeepSeek 7B bf16, single GPU |\n| Generation (if needed) | 30 min | 30 problems × ~60s each |\n| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |\n| Heuristic condition | 30 min | Same as oracle |\n| Analysis + bootstrap | 5 min | B=10000 on CPU |\n| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |\n\n**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.\n\n**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).\n\n**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.\n\n---\n\n## 7. Expected Outcomes & Contingencies\n\n### Scenario A: Oracle recovery > 30% (PASS)\n\n- C5b enters paper as \"phase-aware allocation recovers X% of compound degradation (oracle upper bound)\"\n- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair\n- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)\n\n### Scenario B: Oracle recovery 10-30% (MARGINAL)\n\n- C5b enters Discussion (§6) as \"phase-aware allocation shows promising but modest recovery\"\n- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding\n- Frame full optimization as future work\n\n### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Possible explanations: (1) compound interaction at phase boundaries blurs the effect; (2) head pruning mask is global (can't be phase-specific); (3) KV eviction phase-awareness alone is insufficient\n- Core claims C1-C6 unaffected — finding stands without mitigation\n\n### Risk: Generation trace mismatch\n\nIf bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.\n\n---\n\n## 8. Output Artifacts\n\n| Artifact | Path | Description |\n|----------|------|-------------|\n| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |\n| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |\n| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |\n\n---\n\n## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] Use δ=0.10 for phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged)\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time\n",
    "structuredPatch": [
      {
        "oldStart": 35,
        "oldLines": 6,
        "newStart": 35,
        "newLines": 19,
        "lines": [
          " ",
          " ---",
          " ",
          "+## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)",
          "+",
          "+**Phase-aware KV eviction + uniform head pruning**:",
          "+",
          "+- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.",
          "+- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.",
          "+- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.",
          "+- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.",
          "+",
          "+**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.",
          "+",
          "+---",
          "+",
          " ## 3. Experimental Conditions (per problem, per sparsity level)",
          " ",
          " ### 3.1 Condition A — Uniform Baseline (existing data)"
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

_source line 16_

Now add a clarifying note in Condition B (Oracle) to make explicit that the allocation applies to KV eviction only.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "80fb8a1c-2310-4913-9d62-f2f54af74906",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nGKJXRDfAwEDLPhQW3rMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 29358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1089
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

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01Bb34qpXPPU2SBpEge8F4gK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "old_string": "### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent sparsity using **true quantile-based phase labels** (from attention sparsity during generation). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**Allocation rule** (compute-matched):",
  "new_string": "### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**KV eviction allocation rule** (compute-matched):"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "3f42d298-6580-42d9-a4c1-1a12cfc780c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nGKJXRDfAwEDLPhQW3rMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 29358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1089
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

_source line 18 · 2026-05-14T14:53:16.042Z_

<details><summary>↩ Tool result · `toolu_01Bb34qpXPPU2SBpEge8F4gK`</summary>

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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "6e37489b-fa01-4be1-91b6-b741377cea4c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
    "oldString": "### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent sparsity using **true quantile-based phase labels** (from attention sparsity during generation). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**Allocation rule** (compute-matched):",
    "newString": "### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**KV eviction allocation rule** (compute-matched):",
    "originalFile": "# C5b Mitigation Pilot — Experiment Design\n\n> Claim: Phase-aware sparsity allocation recovers compound degradation\n> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)\n> Gate: >30% II recovery → full rollout; else → future work\n> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)\n\n---\n\n## 1. Objective & Hypotheses\n\n**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.\n\n**Hypotheses**:\n- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).\n- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.\n\n**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.\n\n---\n\n## 2. Pilot Configuration\n\n| Parameter | Value | Rationale |\n|-----------|-------|-----------|\n| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |\n| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |\n| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |\n| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |\n| Bootstrap | B=10000 | Consistent with bf16 canonical data |\n\n**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.\n\n**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.\n\n---\n\n## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)\n\n**Phase-aware KV eviction + uniform head pruning**:\n\n- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.\n- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.\n- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.\n- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.\n\n**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent sparsity using **true quantile-based phase labels** (from attention sparsity during generation). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**Allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|\n| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.\n\n**Implementation**: For each problem:\n1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)\n2. Segment into phases (quantile-based, same as existing pipeline)\n3. For each phase, generate importance-based masks at s_phase\n4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens\n5. Compute per-phase II under oracle allocation\n\n### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy:\n\n```\nphase_heuristic(token_pos) =\n  \"execution\"  if token_pos / seq_len < 0.33\n  \"reasoning\"  if 0.33 ≤ token_pos / seq_len < 0.67\n  \"transition\" if token_pos / seq_len ≥ 0.67\n```\n\nSame sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.\n\n**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a \"thinking → calculating → summarizing\" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.\n\n**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.\n\n---\n\n## 4. Evaluation Metrics\n\n### 4.1 Primary: II Recovery Percentage\n\nFor each problem i, sparsity level s, and phase p:\n\n```\nII_uniform(i, s, p)  = II under Condition A\nII_oracle(i, s, p)   = II under Condition B\nII_heuristic(i, s, p) = II under Condition C\n```\n\n**Aggregate metric** (per sparsity level):\n\n```\nrecovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))\nrecovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))\n```\n\nWhere `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.\n\n### 4.2 Secondary: Per-Phase II Comparison\n\nCompare per-phase II between uniform and oracle:\n- Execution phase: II should decrease (less sparsity → less compound interaction)\n- Transition phase: II should stay low (already near zero, even with more sparsity)\n- Net effect: overall weighted II decreases\n\n### 4.3 Gate Criterion\n\n```\nPASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%\nFAIL otherwise → C5b = \"future work\"\n```\n\nIf heuristic also exceeds 30%, that's a bonus result but not required for the gate.\n\n### 4.4 Statistical Test\n\nPaired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).\n\n---\n\n## 5. Implementation Plan\n\n### 5.1 Code Changes\n\nCreate `run_mitigation_pilot.py` extending the existing profiling pipeline:\n\n```\npacs/profiling/run_mitigation_pilot.py\n```\n\n**Key functions to add**:\n\n1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`\n   - Returns per-phase sparsity levels, compute-matched\n   - Caps s_trans at 0.50\n\n2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`\n   - Token position ratio → phase assignment\n   - Returns Phase objects compatible with existing pipeline\n\n3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`\n   - Runs one problem under one condition\n   - phase_method ∈ {\"oracle\", \"heuristic\"}\n   - Returns per-phase II values and weighted aggregate\n\n**Reuse from existing pipeline**:\n- `load_model_and_tokenizer()` — unchanged\n- `stratified_sample_math500()` — take first 30\n- `InteractionIndexCalculator` — core II computation, unchanged\n- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels\n- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity\n- `compute_conditioned_perplexities()` — per-phase PPL computation\n\n**New logic** (~150 lines):\n- Phase-aware sparsity allocation function\n- Heuristic phase assignment function\n- Main loop: for each problem × condition, generate phase-specific masks and compute II\n- Output JSON with per-problem, per-condition II values\n\n### 5.2 Data Flow\n\n```\nInput:\n  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)\n  - Existing bf16 profiling results for uniform baseline comparison\n\nPipeline (per problem):\n  1. Generate trace → segment phases (oracle) / assign phases (heuristic)\n  2. For each phase:\n     a. Compute phase-specific sparsity level (compute-matched)\n     b. Generate importance masks at phase-specific level\n     c. Forward pass with phase masks, extract phase-token PPL\n     d. Compute phase II\n  3. Compute weighted aggregate II\n  4. Compare against uniform baseline II\n\nOutput:\n  - mitigation_pilot_results.json:\n    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}\n  - Summary statistics + gate evaluation\n```\n\n### 5.3 Compatibility Notes\n\n- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.\n- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.\n- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.\n\n---\n\n## 6. GPU & Time Budget\n\n| Component | GPU Time | Notes |\n|-----------|----------|-------|\n| Model loading | 2 min | DeepSeek 7B bf16, single GPU |\n| Generation (if needed) | 30 min | 30 problems × ~60s each |\n| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |\n| Heuristic condition | 30 min | Same as oracle |\n| Analysis + bootstrap | 5 min | B=10000 on CPU |\n| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |\n\n**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.\n\n**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).\n\n**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.\n\n---\n\n## 7. Expected Outcomes & Contingencies\n\n### Scenario A: Oracle recovery > 30% (PASS)\n\n- C5b enters paper as \"phase-aware allocation recovers X% of compound degradation (oracle upper bound)\"\n- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair\n- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)\n\n### Scenario B: Oracle recovery 10-30% (MARGINAL)\n\n- C5b enters Discussion (§6) as \"phase-aware allocation shows promising but modest recovery\"\n- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding\n- Frame full optimization as future work\n\n### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Possible explanations: (1) compound interaction at phase boundaries blurs the effect; (2) head pruning mask is global (can't be phase-specific); (3) KV eviction phase-awareness alone is insufficient\n- Core claims C1-C6 unaffected — finding stands without mitigation\n\n### Risk: Generation trace mismatch\n\nIf bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.\n\n---\n\n## 8. Output Artifacts\n\n| Artifact | Path | Description |\n|----------|------|-------------|\n| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |\n| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |\n| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |\n\n---\n\n## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] Use δ=0.10 for phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged)\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time\n",
    "structuredPatch": [
      {
        "oldStart": 62,
        "oldLines": 9,
        "newStart": 62,
        "newLines": 9,
        "lines": [
          " ",
          " ### 3.2 Condition B — Oracle Phase-Aware Allocation",
          " ",
          "-Phase-dependent sparsity using **true quantile-based phase labels** (from attention sparsity during generation). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.",
          "+Phase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.",
          " ",
          "-**Allocation rule** (compute-matched):",
          "+**KV eviction allocation rule** (compute-matched):",
          " ",
          " Given target sparsity s and phases with token counts (n_exec, n_reas, n_trans):",
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

### Runtime record

_source line 19_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1778778600,
    "rateLimitType": "five_hour",
    "utilization": 0.9,
    "isUsingOverage": false,
    "surpassedThreshold": 0.9
  },
  "uuid": "7273a0d4-0621-419c-8eff-45b76d874c92",
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_019EuQWZsPhCPXovvon3eo5q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "old_string": "### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy:",
  "new_string": "### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "96ba36cd-3016-4314-8ff0-8e46b1c1d129",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VheRbfYzy7aZDvhRG6sysN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 413,
      "cache_read_input_tokens": 30447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 413
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

_source line 21_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1778778600,
    "rateLimitType": "five_hour",
    "utilization": 0.91,
    "isUsingOverage": false,
    "surpassedThreshold": 0.9
  },
  "uuid": "9e73a0e0-9f8e-46a1-afe6-e131209d68c0",
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1"
}
```

---

### Tool result

_source line 22 · 2026-05-14T14:53:21.242Z_

<details><summary>↩ Tool result · `toolu_019EuQWZsPhCPXovvon3eo5q`</summary>

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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "9eab8c6d-24e9-42f4-9f3e-3a85b2b69e7f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
    "oldString": "### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy:",
    "newString": "### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform.",
    "originalFile": "# C5b Mitigation Pilot — Experiment Design\n\n> Claim: Phase-aware sparsity allocation recovers compound degradation\n> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)\n> Gate: >30% II recovery → full rollout; else → future work\n> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)\n\n---\n\n## 1. Objective & Hypotheses\n\n**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.\n\n**Hypotheses**:\n- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).\n- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.\n\n**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.\n\n---\n\n## 2. Pilot Configuration\n\n| Parameter | Value | Rationale |\n|-----------|-------|-----------|\n| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |\n| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |\n| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |\n| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |\n| Bootstrap | B=10000 | Consistent with bf16 canonical data |\n\n**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.\n\n**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.\n\n---\n\n## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)\n\n**Phase-aware KV eviction + uniform head pruning**:\n\n- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.\n- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.\n- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.\n- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.\n\n**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**KV eviction allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|\n| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.\n\n**Implementation**: For each problem:\n1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)\n2. Segment into phases (quantile-based, same as existing pipeline)\n3. For each phase, generate importance-based masks at s_phase\n4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens\n5. Compute per-phase II under oracle allocation\n\n### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy:\n\n```\nphase_heuristic(token_pos) =\n  \"execution\"  if token_pos / seq_len < 0.33\n  \"reasoning\"  if 0.33 ≤ token_pos / seq_len < 0.67\n  \"transition\" if token_pos / seq_len ≥ 0.67\n```\n\nSame sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.\n\n**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a \"thinking → calculating → summarizing\" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.\n\n**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.\n\n---\n\n## 4. Evaluation Metrics\n\n### 4.1 Primary: II Recovery Percentage\n\nFor each problem i, sparsity level s, and phase p:\n\n```\nII_uniform(i, s, p)  = II under Condition A\nII_oracle(i, s, p)   = II under Condition B\nII_heuristic(i, s, p) = II under Condition C\n```\n\n**Aggregate metric** (per sparsity level):\n\n```\nrecovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))\nrecovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))\n```\n\nWhere `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.\n\n### 4.2 Secondary: Per-Phase II Comparison\n\nCompare per-phase II between uniform and oracle:\n- Execution phase: II should decrease (less sparsity → less compound interaction)\n- Transition phase: II should stay low (already near zero, even with more sparsity)\n- Net effect: overall weighted II decreases\n\n### 4.3 Gate Criterion\n\n```\nPASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%\nFAIL otherwise → C5b = \"future work\"\n```\n\nIf heuristic also exceeds 30%, that's a bonus result but not required for the gate.\n\n### 4.4 Statistical Test\n\nPaired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).\n\n---\n\n## 5. Implementation Plan\n\n### 5.1 Code Changes\n\nCreate `run_mitigation_pilot.py` extending the existing profiling pipeline:\n\n```\npacs/profiling/run_mitigation_pilot.py\n```\n\n**Key functions to add**:\n\n1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`\n   - Returns per-phase sparsity levels, compute-matched\n   - Caps s_trans at 0.50\n\n2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`\n   - Token position ratio → phase assignment\n   - Returns Phase objects compatible with existing pipeline\n\n3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`\n   - Runs one problem under one condition\n   - phase_method ∈ {\"oracle\", \"heuristic\"}\n   - Returns per-phase II values and weighted aggregate\n\n**Reuse from existing pipeline**:\n- `load_model_and_tokenizer()` — unchanged\n- `stratified_sample_math500()` — take first 30\n- `InteractionIndexCalculator` — core II computation, unchanged\n- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels\n- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity\n- `compute_conditioned_perplexities()` — per-phase PPL computation\n\n**New logic** (~150 lines):\n- Phase-aware sparsity allocation function\n- Heuristic phase assignment function\n- Main loop: for each problem × condition, generate phase-specific masks and compute II\n- Output JSON with per-problem, per-condition II values\n\n### 5.2 Data Flow\n\n```\nInput:\n  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)\n  - Existing bf16 profiling results for uniform baseline comparison\n\nPipeline (per problem):\n  1. Generate trace → segment phases (oracle) / assign phases (heuristic)\n  2. For each phase:\n     a. Compute phase-specific sparsity level (compute-matched)\n     b. Generate importance masks at phase-specific level\n     c. Forward pass with phase masks, extract phase-token PPL\n     d. Compute phase II\n  3. Compute weighted aggregate II\n  4. Compare against uniform baseline II\n\nOutput:\n  - mitigation_pilot_results.json:\n    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}\n  - Summary statistics + gate evaluation\n```\n\n### 5.3 Compatibility Notes\n\n- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.\n- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.\n- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.\n\n---\n\n## 6. GPU & Time Budget\n\n| Component | GPU Time | Notes |\n|-----------|----------|-------|\n| Model loading | 2 min | DeepSeek 7B bf16, single GPU |\n| Generation (if needed) | 30 min | 30 problems × ~60s each |\n| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |\n| Heuristic condition | 30 min | Same as oracle |\n| Analysis + bootstrap | 5 min | B=10000 on CPU |\n| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |\n\n**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.\n\n**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).\n\n**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.\n\n---\n\n## 7. Expected Outcomes & Contingencies\n\n### Scenario A: Oracle recovery > 30% (PASS)\n\n- C5b enters paper as \"phase-aware allocation recovers X% of compound degradation (oracle upper bound)\"\n- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair\n- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)\n\n### Scenario B: Oracle recovery 10-30% (MARGINAL)\n\n- C5b enters Discussion (§6) as \"phase-aware allocation shows promising but modest recovery\"\n- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding\n- Frame full optimization as future work\n\n### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Possible explanations: (1) compound interaction at phase boundaries blurs the effect; (2) head pruning mask is global (can't be phase-specific); (3) KV eviction phase-awareness alone is insufficient\n- Core claims C1-C6 unaffected — finding stands without mitigation\n\n### Risk: Generation trace mismatch\n\nIf bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.\n\n---\n\n## 8. Output Artifacts\n\n| Artifact | Path | Description |\n|----------|------|-------------|\n| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |\n| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |\n| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |\n\n---\n\n## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] Use δ=0.10 for phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged)\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time\n",
    "structuredPatch": [
      {
        "oldStart": 96,
        "oldLines": 7,
        "newStart": 96,
        "newLines": 7,
        "lines": [
          " ",
          " ### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)",
          " ",
          "-Phase assignment using **normalized generation position** as a zero-cost proxy:",
          "+Phase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform.",
          " ",
          " ```",
          " phase_heuristic(token_pos) ="
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

_source line 23_

Now update Scenario C in §7 to reflect the Scheme C interpretation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "f4b3709b-1359-4f62-b6f4-8de6985ba2b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpCMnXMatWhvEoaUDRdvci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 30860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_016zV2hhfXxvMjvtmhdrm36Z`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "old_string": "### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Possible explanations: (1) compound interaction at phase boundaries blurs the effect; (2) head pruning mask is global (can't be phase-specific); (3) KV eviction phase-awareness alone is insufficient\n- Core claims C1-C6 unaffected — finding stands without mitigation",
  "new_string": "### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Under Scheme C, this outcome has a clear interpretation: head pruning's fixed structural damage is the dominant source of compound severity, and phase-aware KV eviction alone cannot compensate. This is a meaningful negative result for §7 Discussion (compound interaction is primarily structural, not positional).\n- Core claims C1-C6 unaffected — finding stands without mitigation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "cacb8f7f-8962-474b-ad52-c609d9aab838",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpCMnXMatWhvEoaUDRdvci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 30860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 25 · 2026-05-14T14:53:30.521Z_

<details><summary>↩ Tool result · `toolu_016zV2hhfXxvMjvtmhdrm36Z`</summary>

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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "71b463f2-a902-4146-af93-83ee95a1c4ee",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
    "oldString": "### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Possible explanations: (1) compound interaction at phase boundaries blurs the effect; (2) head pruning mask is global (can't be phase-specific); (3) KV eviction phase-awareness alone is insufficient\n- Core claims C1-C6 unaffected — finding stands without mitigation",
    "newString": "### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Under Scheme C, this outcome has a clear interpretation: head pruning's fixed structural damage is the dominant source of compound severity, and phase-aware KV eviction alone cannot compensate. This is a meaningful negative result for §7 Discussion (compound interaction is primarily structural, not positional).\n- Core claims C1-C6 unaffected — finding stands without mitigation",
    "originalFile": "# C5b Mitigation Pilot — Experiment Design\n\n> Claim: Phase-aware sparsity allocation recovers compound degradation\n> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)\n> Gate: >30% II recovery → full rollout; else → future work\n> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)\n\n---\n\n## 1. Objective & Hypotheses\n\n**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.\n\n**Hypotheses**:\n- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).\n- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.\n\n**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.\n\n---\n\n## 2. Pilot Configuration\n\n| Parameter | Value | Rationale |\n|-----------|-------|-----------|\n| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |\n| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |\n| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |\n| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |\n| Bootstrap | B=10000 | Consistent with bf16 canonical data |\n\n**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.\n\n**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.\n\n---\n\n## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)\n\n**Phase-aware KV eviction + uniform head pruning**:\n\n- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.\n- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.\n- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.\n- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.\n\n**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**KV eviction allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|\n| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.\n\n**Implementation**: For each problem:\n1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)\n2. Segment into phases (quantile-based, same as existing pipeline)\n3. For each phase, generate importance-based masks at s_phase\n4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens\n5. Compute per-phase II under oracle allocation\n\n### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform.\n\n```\nphase_heuristic(token_pos) =\n  \"execution\"  if token_pos / seq_len < 0.33\n  \"reasoning\"  if 0.33 ≤ token_pos / seq_len < 0.67\n  \"transition\" if token_pos / seq_len ≥ 0.67\n```\n\nSame sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.\n\n**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a \"thinking → calculating → summarizing\" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.\n\n**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.\n\n---\n\n## 4. Evaluation Metrics\n\n### 4.1 Primary: II Recovery Percentage\n\nFor each problem i, sparsity level s, and phase p:\n\n```\nII_uniform(i, s, p)  = II under Condition A\nII_oracle(i, s, p)   = II under Condition B\nII_heuristic(i, s, p) = II under Condition C\n```\n\n**Aggregate metric** (per sparsity level):\n\n```\nrecovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))\nrecovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))\n```\n\nWhere `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.\n\n### 4.2 Secondary: Per-Phase II Comparison\n\nCompare per-phase II between uniform and oracle:\n- Execution phase: II should decrease (less sparsity → less compound interaction)\n- Transition phase: II should stay low (already near zero, even with more sparsity)\n- Net effect: overall weighted II decreases\n\n### 4.3 Gate Criterion\n\n```\nPASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%\nFAIL otherwise → C5b = \"future work\"\n```\n\nIf heuristic also exceeds 30%, that's a bonus result but not required for the gate.\n\n### 4.4 Statistical Test\n\nPaired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).\n\n---\n\n## 5. Implementation Plan\n\n### 5.1 Code Changes\n\nCreate `run_mitigation_pilot.py` extending the existing profiling pipeline:\n\n```\npacs/profiling/run_mitigation_pilot.py\n```\n\n**Key functions to add**:\n\n1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`\n   - Returns per-phase sparsity levels, compute-matched\n   - Caps s_trans at 0.50\n\n2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`\n   - Token position ratio → phase assignment\n   - Returns Phase objects compatible with existing pipeline\n\n3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`\n   - Runs one problem under one condition\n   - phase_method ∈ {\"oracle\", \"heuristic\"}\n   - Returns per-phase II values and weighted aggregate\n\n**Reuse from existing pipeline**:\n- `load_model_and_tokenizer()` — unchanged\n- `stratified_sample_math500()` — take first 30\n- `InteractionIndexCalculator` — core II computation, unchanged\n- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels\n- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity\n- `compute_conditioned_perplexities()` — per-phase PPL computation\n\n**New logic** (~150 lines):\n- Phase-aware sparsity allocation function\n- Heuristic phase assignment function\n- Main loop: for each problem × condition, generate phase-specific masks and compute II\n- Output JSON with per-problem, per-condition II values\n\n### 5.2 Data Flow\n\n```\nInput:\n  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)\n  - Existing bf16 profiling results for uniform baseline comparison\n\nPipeline (per problem):\n  1. Generate trace → segment phases (oracle) / assign phases (heuristic)\n  2. For each phase:\n     a. Compute phase-specific sparsity level (compute-matched)\n     b. Generate importance masks at phase-specific level\n     c. Forward pass with phase masks, extract phase-token PPL\n     d. Compute phase II\n  3. Compute weighted aggregate II\n  4. Compare against uniform baseline II\n\nOutput:\n  - mitigation_pilot_results.json:\n    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}\n  - Summary statistics + gate evaluation\n```\n\n### 5.3 Compatibility Notes\n\n- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.\n- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.\n- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.\n\n---\n\n## 6. GPU & Time Budget\n\n| Component | GPU Time | Notes |\n|-----------|----------|-------|\n| Model loading | 2 min | DeepSeek 7B bf16, single GPU |\n| Generation (if needed) | 30 min | 30 problems × ~60s each |\n| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |\n| Heuristic condition | 30 min | Same as oracle |\n| Analysis + bootstrap | 5 min | B=10000 on CPU |\n| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |\n\n**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.\n\n**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).\n\n**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.\n\n---\n\n## 7. Expected Outcomes & Contingencies\n\n### Scenario A: Oracle recovery > 30% (PASS)\n\n- C5b enters paper as \"phase-aware allocation recovers X% of compound degradation (oracle upper bound)\"\n- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair\n- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)\n\n### Scenario B: Oracle recovery 10-30% (MARGINAL)\n\n- C5b enters Discussion (§6) as \"phase-aware allocation shows promising but modest recovery\"\n- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding\n- Frame full optimization as future work\n\n### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Possible explanations: (1) compound interaction at phase boundaries blurs the effect; (2) head pruning mask is global (can't be phase-specific); (3) KV eviction phase-awareness alone is insufficient\n- Core claims C1-C6 unaffected — finding stands without mitigation\n\n### Risk: Generation trace mismatch\n\nIf bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.\n\n---\n\n## 8. Output Artifacts\n\n| Artifact | Path | Description |\n|----------|------|-------------|\n| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |\n| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |\n| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |\n\n---\n\n## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] Use δ=0.10 for phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged)\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time\n",
    "structuredPatch": [
      {
        "oldStart": 262,
        "oldLines": 7,
        "newStart": 262,
        "newLines": 7,
        "lines": [
          " ### Scenario C: Oracle recovery < 10% (FAIL)",
          " ",
          " - C5b = future work, one sentence in Discussion",
          "-- Possible explanations: (1) compound interaction at phase boundaries blurs the effect; (2) head pruning mask is global (can't be phase-specific); (3) KV eviction phase-awareness alone is insufficient",
          "+- Under Scheme C, this outcome has a clear interpretation: head pruning's fixed structural damage is the dominant source of compound severity, and phase-aware KV eviction alone cannot compensate. This is a meaningful negative result for §7 Discussion (compound interaction is primarily structural, not positional).",
          " - Core claims C1-C6 unaffected — finding stands without mitigation",
          " ",
          " ### Risk: Generation trace mismatch"
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

_source line 26_

Let me also update the handoff checklist to reference Scheme C.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "cb96a60b-5eb5-44ec-9f97-b31faa84079c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HmuTgSyxCGprpYpwvGhJn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 435,
      "cache_read_input_tokens": 31271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 435
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01JSE69njG12JygYLeqRNrrd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "old_string": "## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] Use δ=0.10 for phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged)\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time",
  "new_string": "## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] **Scheme C**: Phase-aware δ allocation applies to **KV eviction only**; head pruning stays at uniform rate s for all phases and all conditions\n- [ ] Use δ=0.10 for KV eviction phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged), computed over KV eviction budget only\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "8a5538cc-bbdf-4d05-a627-d8f60e37d6ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HmuTgSyxCGprpYpwvGhJn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 435,
      "cache_read_input_tokens": 31271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 435
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

_source line 28 · 2026-05-14T14:53:37.908Z_

<details><summary>↩ Tool result · `toolu_01JSE69njG12JygYLeqRNrrd`</summary>

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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "462746b3-d125-477e-85fb-1fa39ee26eeb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
    "oldString": "## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] Use δ=0.10 for phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged)\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time",
    "newString": "## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] **Scheme C**: Phase-aware δ allocation applies to **KV eviction only**; head pruning stays at uniform rate s for all phases and all conditions\n- [ ] Use δ=0.10 for KV eviction phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged), computed over KV eviction budget only\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time",
    "originalFile": "# C5b Mitigation Pilot — Experiment Design\n\n> Claim: Phase-aware sparsity allocation recovers compound degradation\n> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)\n> Gate: >30% II recovery → full rollout; else → future work\n> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)\n\n---\n\n## 1. Objective & Hypotheses\n\n**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.\n\n**Hypotheses**:\n- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).\n- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.\n\n**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.\n\n---\n\n## 2. Pilot Configuration\n\n| Parameter | Value | Rationale |\n|-----------|-------|-----------|\n| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |\n| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |\n| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |\n| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |\n| Bootstrap | B=10000 | Consistent with bf16 canonical data |\n\n**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.\n\n**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.\n\n---\n\n## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)\n\n**Phase-aware KV eviction + uniform head pruning**:\n\n- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.\n- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.\n- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.\n- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.\n\n**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**KV eviction allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|\n| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.\n\n**Implementation**: For each problem:\n1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)\n2. Segment into phases (quantile-based, same as existing pipeline)\n3. For each phase, generate importance-based masks at s_phase\n4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens\n5. Compute per-phase II under oracle allocation\n\n### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform.\n\n```\nphase_heuristic(token_pos) =\n  \"execution\"  if token_pos / seq_len < 0.33\n  \"reasoning\"  if 0.33 ≤ token_pos / seq_len < 0.67\n  \"transition\" if token_pos / seq_len ≥ 0.67\n```\n\nSame sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.\n\n**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a \"thinking → calculating → summarizing\" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.\n\n**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.\n\n---\n\n## 4. Evaluation Metrics\n\n### 4.1 Primary: II Recovery Percentage\n\nFor each problem i, sparsity level s, and phase p:\n\n```\nII_uniform(i, s, p)  = II under Condition A\nII_oracle(i, s, p)   = II under Condition B\nII_heuristic(i, s, p) = II under Condition C\n```\n\n**Aggregate metric** (per sparsity level):\n\n```\nrecovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))\nrecovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))\n```\n\nWhere `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.\n\n### 4.2 Secondary: Per-Phase II Comparison\n\nCompare per-phase II between uniform and oracle:\n- Execution phase: II should decrease (less sparsity → less compound interaction)\n- Transition phase: II should stay low (already near zero, even with more sparsity)\n- Net effect: overall weighted II decreases\n\n### 4.3 Gate Criterion\n\n```\nPASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%\nFAIL otherwise → C5b = \"future work\"\n```\n\nIf heuristic also exceeds 30%, that's a bonus result but not required for the gate.\n\n### 4.4 Statistical Test\n\nPaired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).\n\n---\n\n## 5. Implementation Plan\n\n### 5.1 Code Changes\n\nCreate `run_mitigation_pilot.py` extending the existing profiling pipeline:\n\n```\npacs/profiling/run_mitigation_pilot.py\n```\n\n**Key functions to add**:\n\n1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`\n   - Returns per-phase sparsity levels, compute-matched\n   - Caps s_trans at 0.50\n\n2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`\n   - Token position ratio → phase assignment\n   - Returns Phase objects compatible with existing pipeline\n\n3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`\n   - Runs one problem under one condition\n   - phase_method ∈ {\"oracle\", \"heuristic\"}\n   - Returns per-phase II values and weighted aggregate\n\n**Reuse from existing pipeline**:\n- `load_model_and_tokenizer()` — unchanged\n- `stratified_sample_math500()` — take first 30\n- `InteractionIndexCalculator` — core II computation, unchanged\n- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels\n- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity\n- `compute_conditioned_perplexities()` — per-phase PPL computation\n\n**New logic** (~150 lines):\n- Phase-aware sparsity allocation function\n- Heuristic phase assignment function\n- Main loop: for each problem × condition, generate phase-specific masks and compute II\n- Output JSON with per-problem, per-condition II values\n\n### 5.2 Data Flow\n\n```\nInput:\n  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)\n  - Existing bf16 profiling results for uniform baseline comparison\n\nPipeline (per problem):\n  1. Generate trace → segment phases (oracle) / assign phases (heuristic)\n  2. For each phase:\n     a. Compute phase-specific sparsity level (compute-matched)\n     b. Generate importance masks at phase-specific level\n     c. Forward pass with phase masks, extract phase-token PPL\n     d. Compute phase II\n  3. Compute weighted aggregate II\n  4. Compare against uniform baseline II\n\nOutput:\n  - mitigation_pilot_results.json:\n    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}\n  - Summary statistics + gate evaluation\n```\n\n### 5.3 Compatibility Notes\n\n- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.\n- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.\n- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.\n\n---\n\n## 6. GPU & Time Budget\n\n| Component | GPU Time | Notes |\n|-----------|----------|-------|\n| Model loading | 2 min | DeepSeek 7B bf16, single GPU |\n| Generation (if needed) | 30 min | 30 problems × ~60s each |\n| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |\n| Heuristic condition | 30 min | Same as oracle |\n| Analysis + bootstrap | 5 min | B=10000 on CPU |\n| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |\n\n**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.\n\n**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).\n\n**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.\n\n---\n\n## 7. Expected Outcomes & Contingencies\n\n### Scenario A: Oracle recovery > 30% (PASS)\n\n- C5b enters paper as \"phase-aware allocation recovers X% of compound degradation (oracle upper bound)\"\n- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair\n- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)\n\n### Scenario B: Oracle recovery 10-30% (MARGINAL)\n\n- C5b enters Discussion (§6) as \"phase-aware allocation shows promising but modest recovery\"\n- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding\n- Frame full optimization as future work\n\n### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Under Scheme C, this outcome has a clear interpretation: head pruning's fixed structural damage is the dominant source of compound severity, and phase-aware KV eviction alone cannot compensate. This is a meaningful negative result for §7 Discussion (compound interaction is primarily structural, not positional).\n- Core claims C1-C6 unaffected — finding stands without mitigation\n\n### Risk: Generation trace mismatch\n\nIf bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.\n\n---\n\n## 8. Output Artifacts\n\n| Artifact | Path | Description |\n|----------|------|-------------|\n| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |\n| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |\n| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |\n\n---\n\n## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] Use δ=0.10 for phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged)\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time\n",
    "structuredPatch": [
      {
        "oldStart": 286,
        "oldLines": 8,
        "newStart": 286,
        "newLines": 9,
        "lines": [
          " - [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)",
          " - [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1",
          " - [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection",
          "-- [ ] Use δ=0.10 for phase-aware allocation, with s_trans capped at 0.50",
          "-- [ ] Compute-match constraint must hold exactly per-problem (not averaged)",
          "+- [ ] **Scheme C**: Phase-aware δ allocation applies to **KV eviction only**; head pruning stays at uniform rate s for all phases and all conditions",
          "+- [ ] Use δ=0.10 for KV eviction phase-aware allocation, with s_trans capped at 0.50",
          "+- [ ] Compute-match constraint must hold exactly per-problem (not averaged), computed over KV eviction budget only",
          " - [ ] Output format: JSON with per-problem breakdown + aggregate summary",
          " - [ ] Register artifact after completion",
          " - [ ] Run on single GPU, ~1.5h total wall time"
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

_source line 29_

Now verify the final document looks correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "7b50a96b-25ea-4516-a255-305ab2d3f866",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdB3Xr8ziPzknNTc5uMmHo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 31706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 656
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

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01WRRz1uT954tYuovzM35sDR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "offset": 35,
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
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "61db36f1-8e42-4606-af20-03d954e864a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdB3Xr8ziPzknNTc5uMmHo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 31706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 656
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

_source line 31 · 2026-05-14T14:53:40.907Z_

<details><summary>↩ Tool result · `toolu_01WRRz1uT954tYuovzM35sDR`</summary>

````text
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
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "9da32247-131c-4fb4-8a6e-742ef8e213e3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
      "content": "\n---\n\n## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)\n\n**Phase-aware KV eviction + uniform head pruning**:\n\n- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.\n- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.\n- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.\n- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.\n\n**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.\n\n---\n\n## 3. Experimental Conditions (per problem, per sparsity level)\n\n### 3.1 Condition A — Uniform Baseline (existing data)\n\nStandard importance-based compound sparsity at level s, applied uniformly across all phases.\n\nThis is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.\n\n**Per-phase II_uniform(phase, s) from existing data**:\n- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053\n- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053\n\n### 3.2 Condition B — Oracle Phase-Aware Allocation\n\nPhase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.\n\n**KV eviction allocation rule** (compute-matched):\n\nGiven target sparsity s and phases with token counts (n_exec, n_reas, n_trans):\n\n```\ns_exec  = s - δ           (reduce sparsity in high-interaction phase)\ns_reas  = s               (keep reasoning phase unchanged)\ns_trans = s + δ'           (increase sparsity in low-interaction phase)\n\nCompute match constraint:\n  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s\n  → δ' = δ × (n_exec / n_trans)\n```\n\n**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').\n\n| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |\n|----------|--------|--------|------------------------------------------|",
      "numLines": 50,
      "startLine": 35,
      "totalLines": 295
    }
  }
}
````

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1778778600,
    "rateLimitType": "five_hour",
    "utilization": 0.92,
    "isUsingOverage": false,
    "surpassedThreshold": 0.9
  },
  "uuid": "17b8f646-5646-4285-887b-7d0bd44e65b4",
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01KzF5YbhSjPNQJNsDjdKsHS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "offset": 85,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "7859eee0-14dd-4d41-9f6d-b5dda6362de2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P964xqhby2DP9vAAqPC7JW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 32362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1099
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

_source line 34 · 2026-05-14T14:53:43.954Z_

<details><summary>↩ Tool result · `toolu_01KzF5YbhSjPNQJNsDjdKsHS`</summary>

````text
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
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "27531422-dd96-4eaf-9f2b-868245f60a06",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
      "content": "| 0.25 | 0.15 | 0.25 | ~0.35 |\n| 0.30 | 0.20 | 0.30 | ~0.40 |\n\nNote: δ' is computed per-problem based on actual phase token counts to ensure exact compute match. s_trans is capped at 0.50 to avoid degenerate masking.\n\n**Implementation**: For each problem:\n1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)\n2. Segment into phases (quantile-based, same as existing pipeline)\n3. For each phase, generate importance-based masks at s_phase\n4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens\n5. Compute per-phase II under oracle allocation\n\n### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)\n\nPhase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform.\n\n```\nphase_heuristic(token_pos) =\n  \"execution\"  if token_pos / seq_len < 0.33\n  \"reasoning\"  if 0.33 ≤ token_pos / seq_len < 0.67\n  \"transition\" if token_pos / seq_len ≥ 0.67\n```\n\nSame sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.\n",
      "numLines": 25,
      "startLine": 85,
      "totalLines": 295
    }
  }
}
````

</details>

---

### Assistant

_source line 35_

Now save via `save_project_file`. The tool only allows whitelisted files, so I'll write directly since I've already edited the file in place. Let me verify it's saved correctly by checking the Scenario C and checklist sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "36853123-69e2-469a-9ea4-0b52e66e72e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfpDrhCcKMVh4NfHhdfmUi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 33461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
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

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01A94ufr7Dfi6R1eB9euYM7a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
  "offset": 260,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "77becf0f-22ea-4415-b3ae-e79dc63322c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfpDrhCcKMVh4NfHhdfmUi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 33461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
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

_source line 37 · 2026-05-14T14:53:48.455Z_

<details><summary>↩ Tool result · `toolu_01A94ufr7Dfi6R1eB9euYM7a`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "267df1e1-e64b-4da4-b71b-639a7a5e8140",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/c5b_pilot_design.md",
      "content": "- Frame full optimization as future work\n\n### Scenario C: Oracle recovery < 10% (FAIL)\n\n- C5b = future work, one sentence in Discussion\n- Under Scheme C, this outcome has a clear interpretation: head pruning's fixed structural damage is the dominant source of compound severity, and phase-aware KV eviction alone cannot compensate. This is a meaningful negative result for §7 Discussion (compound interaction is primarily structural, not positional).\n- Core claims C1-C6 unaffected — finding stands without mitigation\n\n### Risk: Generation trace mismatch\n\nIf bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.\n\n---\n\n## 8. Output Artifacts\n\n| Artifact | Path | Description |\n|----------|------|-------------|\n| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |\n| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |\n| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |\n\n---\n\n## 9. Handoff Checklist for Coding Worker\n\n- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)\n- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1\n- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection\n- [ ] **Scheme C**: Phase-aware δ allocation applies to **KV eviction only**; head pruning stays at uniform rate s for all phases and all conditions\n- [ ] Use δ=0.10 for KV eviction phase-aware allocation, with s_trans capped at 0.50\n- [ ] Compute-match constraint must hold exactly per-problem (not averaged), computed over KV eviction budget only\n- [ ] Output format: JSON with per-problem breakdown + aggregate summary\n- [ ] Register artifact after completion\n- [ ] Run on single GPU, ~1.5h total wall time\n",
      "numLines": 36,
      "startLine": 260,
      "totalLines": 295
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

文档已更新完成。修改点：

1. **§2.5 新增** — "Implementation Scheme: C (Director Decision 2026-05-14)"，明确 KV eviction phase-aware + head pruning uniform 的方案，含 rationale 和 interpretive value
2. **§3.2 Condition B** — 标题描述改为明确 KV eviction，allocation rule 标注为 KV eviction allocation rule，注明 head pruning 保持 uniform
3. **§3.3 Condition C** — 加注 "only KV eviction sparsity varies by phase; head pruning remains uniform"
4. **§7 Scenario C** — 用 Scheme C 视角重写 FAIL 解释：head pruning 固定损伤是 compound severity 主要来源
5. **§9 Handoff Checklist** — 新增 Scheme C 专项条目，compute-match 约束明确限定为 KV eviction budget

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "uuid": "ca53b443-96da-411b-9ac0-5ff45bf3f7e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsYDA2yxeGdkqd8sS43MFS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 34041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 817
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

### Runtime record

_source line 39_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1778778600,
    "rateLimitType": "five_hour",
    "utilization": 0.93,
    "isUsingOverage": false,
    "surpassedThreshold": 0.9
  },
  "uuid": "82affb2c-d5fe-4359-bd11-3e0498c35c1f",
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1"
}
```

---

### Task result

_source line 40_

文档已更新完成。修改点：

1. **§2.5 新增** — "Implementation Scheme: C (Director Decision 2026-05-14)"，明确 KV eviction phase-aware + head pruning uniform 的方案，含 rationale 和 interpretive value
2. **§3.2 Condition B** — 标题描述改为明确 KV eviction，allocation rule 标注为 KV eviction allocation rule，注明 head pruning 保持 uniform
3. **§3.3 Condition C** — 加注 "only KV eviction sparsity varies by phase; head pruning remains uniform"
4. **§7 Scenario C** — 用 Scheme C 视角重写 FAIL 解释：head pruning 固定损伤是 compound severity 主要来源
5. **§9 Handoff Checklist** — 新增 Scheme C 专项条目，compute-match 约束明确限定为 KV eviction budget

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 80025,
  "duration_api_ms": 80613,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "321a214e-6a89-4dc0-b7d1-909a9c59f6b1",
  "total_cost_usd": 0.40771825,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 23411,
    "cache_read_input_tokens": 337337,
    "output_tokens": 3649,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 23411,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 260,
        "cache_read_input_tokens": 34041,
        "cache_creation_input_tokens": 817,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 817
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1336,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001426,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 3649,
      "cacheReadInputTokens": 337337,
      "cacheCreationInputTokens": 23411,
      "webSearchRequests": 0,
      "costUSD": 0.40629224999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e778f1fb-2894-4a14-8401-cbb596ca3648"
}
```

</details>

---
