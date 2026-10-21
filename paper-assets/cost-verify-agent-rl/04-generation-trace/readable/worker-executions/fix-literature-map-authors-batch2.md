# fix literature map authors batch2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_fix_literature-map-authors-batch2_20260516T001844.log`
- **Structured JSON:** [`85962d0d3aef766d1233.json`](../../sessions/85/85962d0d3aef766d1233.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
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
  "uuid": "1c3c95a3-1951-422b-ba43-a50361d35ee0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/memory/"
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
    "resetsAt": 1778906400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0d46a5de-b959-46c6-a0b4-eb08708f3c66",
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me first read the file to understand its current state, then search for the author information for each paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "482d08f6-058d-4667-ab25-40fb31f4d974",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dc9wUY8mnPJZjqr7GfVwPF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11534,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11534
      },
      "output_tokens": 29,
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

Let me read the file and search for the three papers' authors in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "9c3e7d26-354e-4890-9506-ffbd73e8b9cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dc9wUY8mnPJZjqr7GfVwPF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11534,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11534
      },
      "output_tokens": 29,
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

<details open><summary>🔧 Tool call — Read · `toolu_016bW3vhuT4YFqNnhGi8kU23`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "c1d2cb43-7c52-4737-a58c-3312e5679d74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dc9wUY8mnPJZjqr7GfVwPF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11534,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11534
      },
      "output_tokens": 29,
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

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HoLBMFz5zX5dw3jxMLRpW4`</summary>

```json
{
  "query": "select:WebSearch",
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
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "78134472-2917-4d6f-9c33-d903725e7c25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dc9wUY8mnPJZjqr7GfVwPF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11534,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11534
      },
      "output_tokens": 29,
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

_source line 8 · 2026-05-16T00:18:58.007Z_

<details><summary>↩ Tool result · `toolu_01HoLBMFz5zX5dw3jxMLRpW4`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "1cac2c7c-905d-42c6-8fb8-368c078ba616",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T00:18:58.105Z_

<details><summary>↩ Tool result · `toolu_016bW3vhuT4YFqNnhGi8kU23`</summary>

```text
1	# B-IAVR Literature Map
2	# Updated: 2026-05-16
3	# Categories: direct-competitor, method-component, background, evaluation
4	# Roles: predecessor, competitor, baseline, evaluation, background
5	
6	papers:
7	
8	  # ============================================================
9	  # Direction 1: Self-Verification / Self-Correction in LLM Agents
10	  # ============================================================
11	
12	  - id: kamoi2024self-correction-survey
13	    title: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"
14	    authors: "Kamoi et al."
15	    venue: "arXiv"
16	    year: 2024
17	    arxiv_id: "2406.01297"
18	    category: background
19	    role: background
20	    relevance_note: >
21	      Foundational survey establishing that pure intrinsic self-correction is unreliable.
22	      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.
23	
24	  - id: tie2025correctbench
25	    title: "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs"
26	    authors: "Tie et al."
27	    venue: "NeurIPS 2025 Datasets & Benchmarks"
28	    year: 2025
29	    arxiv_id: "2510.16062"
30	    category: background
31	    role: background
32	    relevance_note: >
33	      Benchmark showing self-correction has diminishing returns when applied uniformly.
34	      Supports B-IAVR's selective verification design over blanket correction.
35	
36	  - id: self-verification-dilemma-2026
37	    title: "Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning"
38	    authors: "Long et al."
39	    venue: "arXiv"
40	    year: 2026
41	    arxiv_id: "2602.03485"
42	    category: background
43	    role: background
44	    relevance_note: >
45	      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.
46	      Directly supports B-IAVR's core thesis that verification should be selective.
47	      Their experience-pool approach is complementary to B-IAVR's action-change signal.
48	
49	  - id: zhang2025incentivize-self-verify
50	    title: "Incentivizing LLMs to Self-Verify Their Answers"
51	    authors: "Zhang et al."
52	    venue: "arXiv"
53	    year: 2025
54	    arxiv_id: "2506.01369"
55	    category: background
56	    role: background
57	    relevance_note: >
58	      Unifies answer generation and verification via single RL training process.
59	      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.
60	
61	  - id: mar2025
62	    title: "MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs"
63	    authors: "Ozer et al."
64	    venue: "arXiv"
65	    year: 2025
66	    arxiv_id: "2512.20845"
67	    category: background
68	    role: background
69	    relevance_note: >
70	      Multi-agent self-correction with diverse critic personas.
71	      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.
72	
73	  - id: ssr2025
74	    title: "SSR: Socratic Self-Refine for Large Language Model Reasoning"
75	    authors: "Shi et al."
76	    venue: "arXiv"
77	    year: 2025
78	    arxiv_id: "2511.10621"
79	    category: background
80	    role: background
81	    relevance_note: >
82	      Structured Socratic questioning for self-refinement.
83	      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.
84	
85	  - id: verifiagent2025
86	    title: "VerifiAgent: a Unified Verification Agent in Language Model Reasoning"
87	    authors: "Han et al."
88	    venue: "EMNLP 2025 Findings"
89	    year: 2025
90	    arxiv_id: "2504.00406"
91	    category: background
92	    role: background
93	    relevance_note: >
94	      Unified verification agent with meta-verification + tool-based adaptive verification.
95	      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).
96	      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.
97	
98	  # ============================================================
99	  # Direction 2: Agent RL Training
100	  # ============================================================
101	
102	  - id: feng2025gigpo
103	    title: "GiGPO: Group-in-Group Policy Optimization for LLM Agent Training"
104	    authors: "Feng et al."
105	    venue: "NeurIPS 2025"
106	    year: 2025
107	    arxiv_id: "2505.10978"
108	    category: method-component
109	    role: predecessor
110	    relevance_note: >
111	      Core training algorithm for B-IAVR. Nested group structure provides step-level credit
112	      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.
113	
114	  - id: selfguide2026
115	    title: "Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)"
116	    authors: "Wang et al."
117	    venue: "arXiv"
118	    year: 2026
119	    arxiv_id: "2604.03098"
120	    category: method-component
121	    role: predecessor
122	    relevance_note: >
123	      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.
124	      The self-guidance signal is the foundation for action-change detection triggering verification.
125	      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.
126	
127	  - id: spear2025
128	    title: "Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"
129	    authors: "Qin et al."
130	    venue: "ICLR 2026"
131	    year: 2025
132	    arxiv_id: "2509.22601"
133	    category: method-component
134	    role: background
135	    relevance_note: >
136	      Curriculum-based self-imitation for sparse-reward agent tasks.
137	      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.
138	
139	  - id: wei2025webagent-r1
140	    title: "WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL"
141	    authors: "Wei et al."
142	    venue: "EMNLP 2025"
143	    year: 2025
144	    arxiv_id: "2505.16421"
145	    category: background
146	    role: background
147	    relevance_note: >
148	      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.
149	      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.
150	
151	  - id: dapo2025
152	    title: "DAPO: An Open-Source LLM Reinforcement Learning System at Scale"
153	    authors: "Yu et al."
154	    venue: "arXiv"
155	    year: 2025
156	    arxiv_id: "2503.14476"
157	    category: method-component
158	    role: background
159	    relevance_note: >
160	      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).
161	      Applicable to B-IAVR's RL training to prevent entropy collapse.
162	
163	  - id: digiRL2024
164	    title: "DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL"
165	    authors: "Bai et al."
166	    venue: "NeurIPS 2024"
167	    year: 2024
168	    arxiv_id: "2406.11896"
169	    category: background
170	    role: background
171	    relevance_note: >
172	      Online RL for device control agents. Demonstrates online RL viability for interactive agents.
173	      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.
174	
175	  - id: li2025sorl
176	    title: "SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training"
177	    authors: "Li et al."
178	    venue: "arXiv"
179	    year: 2025
180	    arxiv_id: "2511.20718"
181	    category: method-component
182	    role: background
183	    relevance_note: >
184	      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.
185	      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.
186	
187	  - id: agentic-rl-survey-2025
188	    title: "The Landscape of Agentic Reinforcement Learning for LLMs: A Survey"
189	    authors: "Zhang et al."
190	    venue: "TMLR 2026"
191	    year: 2025
192	    arxiv_id: "2509.02547"
193	    category: background
194	    role: background
195	    relevance_note: >
196	      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents
197	      to make meta-decisions (when to verify) via RL within the POMDP framework.
198	
199	  - id: skillmaster2026
200	    title: "SkillMaster: Toward Autonomous Skill Mastery in LLM Agents"
201	    authors: "Yang et al."
202	    venue: "arXiv"
203	    year: 2026
204	    arxiv_id: "2605.08693"
205	    category: method-component
206	    role: background
207	    relevance_note: >
208	      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.
209	      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's
210	      separation of action and verification advantages.
211	
212	  - id: t2po2026
213	    title: "T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL"
214	    authors: "Wang et al."
215	    venue: "ICML 2026 Spotlight"
216	    year: 2026
217	    arxiv_id: "2605.02178"
218	    category: method-component
219	    role: background
220	    relevance_note: >
221	      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.
222	      Triggers thinking intervention when marginal uncertainty change drops below threshold.
223	      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs
224	      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.
225	
226	  - id: gvpo2026
227	    title: "GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents"
228	    authors: "Dai et al."
229	    venue: "ICLR 2026"
230	    year: 2026
231	    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV
232	    category: method-component
233	    role: background
234	    relevance_note: >
235	      Advantage shaping with outcome-verifiable + process-verifiable signals.
236	      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level
237	      verification signals. Different focus: uses verification for credit assignment during
238	      training; B-IAVR learns when to invoke verification at deployment.
239	
240	  - id: agentv-rl2026
241	    title: "AgentV-RL: Scaling Reward Modeling with Agentic Verifier"
242	    authors: "Zhang et al."
243	    venue: "arXiv"
244	    year: 2026
245	    arxiv_id: "2604.16004"
246	    category: method-component
247	    role: background
248	    relevance_note: >
249	      Bidirectional forward/backward agentic verifier for reward modeling in RL.
250	      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;
251	      B-IAVR addresses verification timing in agent deployment. Complementary.
252	
253	  - id: pa-moe2026
254	    title: "PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning"
255	    authors: "Li et al."
256	    venue: "arXiv"
257	    year: 2026
258	    arxiv_id: "2602.17038"
259	    category: evaluation
260	    role: baseline
261	    relevance_note: >
262	      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.
263	      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).
264	      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.
265	      Orthogonal architecture innovation; important baseline to cite.
266	
267	  - id: sdar2026
268	    title: "SDAR: Self-Distilled Agentic Reinforcement Learning"
269	    authors: "ZJU-REAL"
270	    venue: "arXiv"
271	    year: 2026
272	    arxiv_id: "2605.15155"
273	    category: method-component
274	    role: background
275	    relevance_note: >
276	      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.
277	      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.
278	      Complementary: SDAR improves RL training; B-IAVR learns verification policy.
279	
280	  - id: hcapo2026
281	    title: "HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents"
282	    authors: "Tan et al."
283	    venue: "arXiv"
284	    year: 2026
285	    arxiv_id: "2603.08754"
286	    category: method-component
287	    role: background
288	    relevance_note: >
289	      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +
290	      multi-scale advantage for critical decision states.
291	      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).
292	      Could improve B-IAVR's reward signal for verification decision steps.
293	
294	  - id: act2026
295	    title: "ACT: Agentic Critical Training"
296	    authors: "Unknown"
297	    venue: "arXiv"
298	    year: 2026
299	    arxiv_id: "2603.08706"
300	    category: method-component
301	    role: background
302	    relevance_note: >
303	      [NEW-0516] Trains agents to judge action quality via critical comparison reward.
304	      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;
305	      B-IAVR decides when to reflect.
306	
307	  - id: rwml2026
308	    title: "RWML: Reinforcement World Model Learning for LLM-based Agents"
309	    authors: "Yu et al."
310	    venue: "arXiv"
311	    year: 2026
312	    arxiv_id: "2602.05842"
313	    category: method-component
314	    role: background
315	    relevance_note: >
316	      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.
317	      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.
318	      Orthogonal: improves internal world model; B-IAVR adds selective verification.
319	
320	  - id: skill0-2026
321	    title: "SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization"
322	    authors: "ZJU-REAL"
323	    venue: "arXiv"
324	    year: 2026
325	    arxiv_id: "2604.02268"
326	    category: method-component
327	    role: background
328	    relevance_note: >
329	      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.
330	      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.
331	      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.
332	
333	  - id: fission-grpo2026
334	    title: "Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors"
335	    authors: "Zhang et al."
336	    venue: "arXiv"
337	    year: 2026
338	    arxiv_id: "2601.15625"
339	    category: method-component
340	    role: background
341	    relevance_note: >
342	      [NEW-0516] Fissions failed trajectories into recovery training instances.
343	      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.
344	      Related: error recovery after failure vs B-IAVR's proactive verification.
345	
346	  - id: selfbudgeter2026
347	    title: "SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning"
348	    authors: "Li et al."
349	    venue: "ICLR 2026 (under review)"
350	    year: 2025
351	    arxiv_id: "2505.11274"
352	    category: background
353	    role: background
354	    relevance_note: >
355	      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.
356	      Parallel concept: SelfBudgeter allocates computation budget;
357	      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.
358	
359	  - id: cove2026
360	    title: "CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification"
361	    authors: "Chen et al."
362	    venue: "arXiv"
363	    year: 2026
364	    arxiv_id: "2603.01940"
365	    category: background
366	    role: background
367	    relevance_note: >
368	      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.
369	      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.
370	
371	  # ============================================================
372	  # Direction 3: Selective Verification / Adaptive Computation
373	  # ============================================================
374	
375	  - id: wan2025derailer-rerailer
376	    title: "Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning"
377	    authors: "Wan et al."
378	    venue: "ACL 2025 Findings"
379	    year: 2025
380	    arxiv_id: "2408.13940"
381	    category: direct-competitor
382	    role: competitor
383	    relevance_note: >
384	      Most directly related competitor. Both do selective verification with binary trigger.
385	      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).
386	      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.
387	      8-11% accuracy gain, 2-3x efficiency over uniform verification.
388	
389	  - id: sherlock2025
390	    title: "Sherlock: Reliable and Efficient Agentic Workflow Execution"
391	    authors: "Microsoft"
392	    venue: "arXiv"
393	    year: 2025
394	    arxiv_id: "2511.00330"
395	    category: direct-competitor
396	    role: competitor
397	    relevance_note: >
398	      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.
399	      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).
400	      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.
401	
402	  - id: singhi2025when-to-verify
403	    title: "When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning"
404	    authors: "Singhi et al."
405	    venue: "arXiv"
406	    year: 2025
407	    arxiv_id: "2504.01005"
408	    category: background
409	    role: background
410	    relevance_note: >
411	      Derives inference scaling laws for solve-vs-verify tradeoff.
412	      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.
413	      B-IAVR learns this allocation via RL rather than analytically.
414	
415	  - id: yang2026ares
416	    title: "ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents"
417	    authors: "Yang et al."
418	    venue: "arXiv"
419	    year: 2026
420	    arxiv_id: "2603.07915"
421	    category: direct-competitor
422	    role: competitor
423	    relevance_note: >
424	      Closest competitor in agent domain. Both train learned per-step compute allocation.
425	      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;
426	      B-IAVR trains binary verify/not-verify via RL with action-change signal.
427	      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change
428	      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data
429	      to bootstrap the router, B-IAVR learns from environment interaction alone.
430	      Reduces reasoning tokens by up to 52.7%.
431	
432	  - id: tu2025autothink
433	    title: "Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL"
434	    authors: "Tu et al."
435	    venue: "NeurIPS 2025"
436	    year: 2025
437	    arxiv_id: "2505.10832"
438	    category: direct-competitor
439	    role: competitor
440	    relevance_note: >
441	      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.
442	      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.
443	      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.
444	
445	  - id: du2025thinkless
446	    title: "Thinkless: LLM Learns When to Think"
447	    authors: "Fang et al."
448	    venue: "NeurIPS 2025"
449	    year: 2025
450	    arxiv_id: "2505.13379"
451	    category: direct-competitor
452	    role: competitor
453	    relevance_note: >
454	      RL-trained control token to decide when to invoke extended thinking.
455	      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.
456	
457	  - id: wang2025efficient-agents
458	    title: "Efficient Agents: Building Effective Agents While Reducing Cost"
459	    authors: "Wang et al."
460	    venue: "arXiv"
461	    year: 2025
462	    arxiv_id: "2508.02694"
463	    category: background
464	    role: background
465	    relevance_note: >
466	      First systematic study of agent efficiency-effectiveness tradeoff.
467	      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.
468	      Retains 96.7% performance with 28.4% cost-of-pass improvement.
469	
470	  - id: venktesh2025trust-but-verify
471	    title: "Trust but Verify! A Survey on Verification Design for Test-time Scaling"
472	    authors: "Venktesh et al."
473	    venue: "arXiv"
474	    year: 2025
475	    arxiv_id: "2508.16665"
476	    category: background
477	    role: background
478	    relevance_note: >
479	      Survey of verification approaches for test-time compute scaling.
480	      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.
481	
482	  - id: agent-omit2026
483	    title: "Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL"
484	    authors: "Ning et al."
485	    venue: "ICML 2026"
486	    year: 2026
487	    arxiv_id: "2602.04284"
488	    category: direct-competitor
489	    role: competitor
490	    relevance_note: >
491	      RL-trained policy for adaptive omission of redundant thoughts and observations.
492	      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.
493	      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts
494	      (omits unnecessary context); B-IAVR selectively adds (verification steps).
495	      Opposite but complementary approaches to cost-efficiency. Potentially combinable.
496	
497	  - id: ava2026
498	    title: "Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints"
499	    authors: "Patel"
500	    venue: "TMLR 2026"
501	    year: 2026
502	    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF
503	    category: direct-competitor
504	    role: competitor
505	    relevance_note: >
506	      Dynamic compute allocation across search, sampling, and verification under budget.
507	      Uses calibrated uncertainty + value-of-information for selective verification cascades.
508	      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.
509	      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;
510	      single-turn reasoning vs multi-turn agent trajectories.
511	
512	  - id: cast2026
513	    title: "CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use"
514	    authors: "Pang et al."
515	    venue: "arXiv"
516	    year: 2026
517	    arxiv_id: "2605.15041"
518	    category: background
519	    role: background
520	    relevance_note: >
521	      Historical execution cases calibrate reasoning depth for tool use.
522	      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.
523	      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.
524	
525	  - id: marginal-token-allocators2026
526	    title: "Agentic AI Systems Should Be Designed as Marginal Token Allocators"
527	    authors: "Zhu"
528	    venue: "arXiv"
529	    year: 2026
530	    arxiv_id: "2605.01214"
531	    category: background
532	    role: background
533	    relevance_note: >
534	      Position paper framing agent cost-efficiency as marginal token allocation economics.
535	      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing
536	      that verification decisions should reflect marginal cost-benefit analysis.
537	
538	  - id: argos2025
539	    title: "Argos: Multimodal RL with Adaptive Verifier for AI Agents"
540	    authors: "Tan et al."
541	    venue: "arXiv (revised April 2026)"
542	    year: 2025
543	    arxiv_id: "2512.03438"
544	    category: background
545	    role: background
546	    relevance_note: >
547	      Agentic verifier that adaptively selects scoring functions for multimodal RL training.
548	      Different domain (multimodal/robotics). The adaptive verifier selection concept is
549	      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.
550	
551	  # ============================================================
552	  # Direction 4: ALFWorld / Interactive Environment Benchmarks
553	  # ============================================================
554	
555	  - id: kim2025reflact
556	    title: "ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection"
557	    authors: "Kim et al."
558	    venue: "EMNLP 2025"
559	    year: 2025
560	    arxiv_id: "2505.15182"
561	    category: evaluation
562	    role: baseline
563	    relevance_note: >
564	      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.
565	      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.
566	
567	  - id: choudhury2025agentprm
568	    title: "Process Reward Models for LLM Agents: Practical Framework and Directions"
569	    authors: "Choudhury"
570	    venue: "arXiv"
571	    year: 2025
572	    arxiv_id: "2502.10325"
573	    category: evaluation
574	    role: baseline
575	    relevance_note: >
576	      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.
577	      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.
578	
579	  - id: xi2025agentprm
580	    title: "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress"
581	    authors: "Xi et al."
582	    venue: "ACM Web Conference 2026"
583	    year: 2025
584	    arxiv_id: "2511.08325"
585	    category: evaluation
586	    role: baseline
587	    relevance_note: >
588	      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable
589	      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.
590	      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.
591	
592	  - id: xiang2024retrospex
593	    title: "Retrospex: Language Agent Meets Offline RL Critic"
594	    authors: "Xiang et al."
595	    venue: "EMNLP 2024"
596	    year: 2024
597	    arxiv_id: "2505.11807"
598	    category: background
599	    role: background
600	    relevance_note: >
601	      Offline RL Critic augments LLM agent action selection via dynamic rescoring.
602	      Similar architecture could inform B-IAVR's verification value estimation.
603	
604	  - id: cfgm2025
605	    title: "CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning"
606	    authors: "Yang et al."
607	    venue: "EMNLP 2025"
608	    year: 2025
609	    arxiv_id: "2508.15305"
610	    category: background
611	    role: background
612	    relevance_note: >
613	      Memory-augmented agent planning with episodic grounding.
614	      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.
615	
616	  - id: respact2024
617	    title: "ReSpAct: Harmonizing Reasoning, Speaking, and Acting"
618	    authors: "Dongre et al."
619	    venue: "arXiv"
620	    year: 2024
621	    arxiv_id: "2411.00927"
622	    category: evaluation
623	    role: baseline
624	    relevance_note: >
625	      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.
626	      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.
627	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "77869eca-f7cc-4015-8520-ff2a432e2b87",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
      "content": "# B-IAVR Literature Map\n# Updated: 2026-05-16\n# Categories: direct-competitor, method-component, background, evaluation\n# Roles: predecessor, competitor, baseline, evaluation, background\n\npapers:\n\n  # ============================================================\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\n  # ============================================================\n\n  - id: kamoi2024self-correction-survey\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Kamoi et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2406.01297\"\n    category: background\n    role: background\n    relevance_note: >\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\n\n  - id: tie2025correctbench\n    title: \"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\"\n    authors: \"Tie et al.\"\n    venue: \"NeurIPS 2025 Datasets & Benchmarks\"\n    year: 2025\n    arxiv_id: \"2510.16062\"\n    category: background\n    role: background\n    relevance_note: >\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\n      Supports B-IAVR's selective verification design over blanket correction.\n\n  - id: self-verification-dilemma-2026\n    title: \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\"\n    authors: \"Long et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.03485\"\n    category: background\n    role: background\n    relevance_note: >\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\n      Directly supports B-IAVR's core thesis that verification should be selective.\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\n\n  - id: zhang2025incentivize-self-verify\n    title: \"Incentivizing LLMs to Self-Verify Their Answers\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2506.01369\"\n    category: background\n    role: background\n    relevance_note: >\n      Unifies answer generation and verification via single RL training process.\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\n\n  - id: mar2025\n    title: \"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\"\n    authors: \"Ozer et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.20845\"\n    category: background\n    role: background\n    relevance_note: >\n      Multi-agent self-correction with diverse critic personas.\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\n\n  - id: ssr2025\n    title: \"SSR: Socratic Self-Refine for Large Language Model Reasoning\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.10621\"\n    category: background\n    role: background\n    relevance_note: >\n      Structured Socratic questioning for self-refinement.\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\n\n  - id: verifiagent2025\n    title: \"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\"\n    authors: \"Han et al.\"\n    venue: \"EMNLP 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2504.00406\"\n    category: background\n    role: background\n    relevance_note: >\n      Unified verification agent with meta-verification + tool-based adaptive verification.\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\n\n  # ============================================================\n  # Direction 2: Agent RL Training\n  # ============================================================\n\n  - id: feng2025gigpo\n    title: \"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\"\n    authors: \"Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10978\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\n\n  - id: selfguide2026\n    title: \"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.03098\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\n      The self-guidance signal is the foundation for action-change detection triggering verification.\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\n\n  - id: spear2025\n    title: \"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"\n    authors: \"Qin et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.22601\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Curriculum-based self-imitation for sparse-reward agent tasks.\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\n\n  - id: wei2025webagent-r1\n    title: \"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\"\n    authors: \"Wei et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.16421\"\n    category: background\n    role: background\n    relevance_note: >\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\n\n  - id: dapo2025\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2503.14476\"\n    category: method-component\n    role: background\n    relevance_note: >\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\n\n  - id: digiRL2024\n    title: \"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\"\n    authors: \"Bai et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv_id: \"2406.11896\"\n    category: background\n    role: background\n    relevance_note: >\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\n\n  - id: li2025sorl\n    title: \"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.20718\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\n\n  - id: agentic-rl-survey-2025\n    title: \"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\"\n    authors: \"Zhang et al.\"\n    venue: \"TMLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.02547\"\n    category: background\n    role: background\n    relevance_note: >\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\n\n  - id: skillmaster2026\n    title: \"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.08693\"\n    category: method-component\n    role: background\n    relevance_note: >\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\n      separation of action and verification advantages.\n\n  - id: t2po2026\n    title: \"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\"\n    authors: \"Wang et al.\"\n    venue: \"ICML 2026 Spotlight\"\n    year: 2026\n    arxiv_id: \"2605.02178\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\n\n  - id: gvpo2026\n    title: \"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\"\n    authors: \"Dai et al.\"\n    venue: \"ICLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\n    category: method-component\n    role: background\n    relevance_note: >\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\n      verification signals. Different focus: uses verification for credit assignment during\n      training; B-IAVR learns when to invoke verification at deployment.\n\n  - id: agentv-rl2026\n    title: \"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.16004\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\n      B-IAVR addresses verification timing in agent deployment. Complementary.\n\n  - id: pa-moe2026\n    title: \"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.17038\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\n      Orthogonal architecture innovation; important baseline to cite.\n\n  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"ZJU-REAL\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15155\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\n\n  - id: hcapo2026\n    title: \"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08754\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\n      multi-scale advantage for critical decision states.\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\n      Could improve B-IAVR's reward signal for verification decision steps.\n\n  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Unknown\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08706\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\n      B-IAVR decides when to reflect.\n\n  - id: rwml2026\n    title: \"RWML: Reinforcement World Model Learning for LLM-based Agents\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.05842\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\n\n  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"ZJU-REAL\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.02268\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\n\n  - id: fission-grpo2026\n    title: \"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2601.15625\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\n      Related: error recovery after failure vs B-IAVR's proactive verification.\n\n  - id: selfbudgeter2026\n    title: \"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\"\n    authors: \"Li et al.\"\n    venue: \"ICLR 2026 (under review)\"\n    year: 2025\n    arxiv_id: \"2505.11274\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\n      Parallel concept: SelfBudgeter allocates computation budget;\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\n\n  - id: cove2026\n    title: \"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.01940\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\n\n  # ============================================================\n  # Direction 3: Selective Verification / Adaptive Computation\n  # ============================================================\n\n  - id: wan2025derailer-rerailer\n    title: \"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\"\n    authors: \"Wan et al.\"\n    venue: \"ACL 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2408.13940\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Most directly related competitor. Both do selective verification with binary trigger.\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\n\n  - id: sherlock2025\n    title: \"Sherlock: Reliable and Efficient Agentic Workflow Execution\"\n    authors: \"Microsoft\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.00330\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\n\n  - id: singhi2025when-to-verify\n    title: \"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\"\n    authors: \"Singhi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2504.01005\"\n    category: background\n    role: background\n    relevance_note: >\n      Derives inference scaling laws for solve-vs-verify tradeoff.\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\n      B-IAVR learns this allocation via RL rather than analytically.\n\n  - id: yang2026ares\n    title: \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.07915\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\n      Reduces reasoning tokens by up to 52.7%.\n\n  - id: tu2025autothink\n    title: \"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\"\n    authors: \"Tu et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10832\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\n\n  - id: du2025thinkless\n    title: \"Thinkless: LLM Learns When to Think\"\n    authors: \"Fang et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.13379\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained control token to decide when to invoke extended thinking.\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\n\n  - id: wang2025efficient-agents\n    title: \"Efficient Agents: Building Effective Agents While Reducing Cost\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.02694\"\n    category: background\n    role: background\n    relevance_note: >\n      First systematic study of agent efficiency-effectiveness tradeoff.\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\n\n  - id: venktesh2025trust-but-verify\n    title: \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\"\n    authors: \"Venktesh et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.16665\"\n    category: background\n    role: background\n    relevance_note: >\n      Survey of verification approaches for test-time compute scaling.\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\n\n  - id: agent-omit2026\n    title: \"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\"\n    authors: \"Ning et al.\"\n    venue: \"ICML 2026\"\n    year: 2026\n    arxiv_id: \"2602.04284\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\n\n  - id: ava2026\n    title: \"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\"\n    authors: \"Patel\"\n    venue: \"TMLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Dynamic compute allocation across search, sampling, and verification under budget.\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\n      single-turn reasoning vs multi-turn agent trajectories.\n\n  - id: cast2026\n    title: \"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\"\n    authors: \"Pang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15041\"\n    category: background\n    role: background\n    relevance_note: >\n      Historical execution cases calibrate reasoning depth for tool use.\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\n\n  - id: marginal-token-allocators2026\n    title: \"Agentic AI Systems Should Be Designed as Marginal Token Allocators\"\n    authors: \"Zhu\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.01214\"\n    category: background\n    role: background\n    relevance_note: >\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\n      that verification decisions should reflect marginal cost-benefit analysis.\n\n  - id: argos2025\n    title: \"Argos: Multimodal RL with Adaptive Verifier for AI Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv (revised April 2026)\"\n    year: 2025\n    arxiv_id: \"2512.03438\"\n    category: background\n    role: background\n    relevance_note: >\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\n\n  # ============================================================\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\n  # ============================================================\n\n  - id: kim2025reflact\n    title: \"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\"\n    authors: \"Kim et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.15182\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\n\n  - id: choudhury2025agentprm\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2502.10325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\n\n  - id: xi2025agentprm\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Xi et al.\"\n    venue: \"ACM Web Conference 2026\"\n    year: 2025\n    arxiv_id: \"2511.08325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\n\n  - id: xiang2024retrospex\n    title: \"Retrospex: Language Agent Meets Offline RL Critic\"\n    authors: \"Xiang et al.\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    arxiv_id: \"2505.11807\"\n    category: background\n    role: background\n    relevance_note: >\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\n      Similar architecture could inform B-IAVR's verification value estimation.\n\n  - id: cfgm2025\n    title: \"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\"\n    authors: \"Yang et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2508.15305\"\n    category: background\n    role: background\n    relevance_note: >\n      Memory-augmented agent planning with episodic grounding.\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\n\n  - id: respact2024\n    title: \"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\"\n    authors: \"Dongre et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2411.00927\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\n",
      "numLines": 627,
      "startLine": 1,
      "totalLines": 627
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
Now let me search for the authors of all three papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "582c3ecb-d189-4757-a67d-e4ce7b5ed920",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jJCZbFwJixyjsU4cHD7iR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9944,
      "cache_read_input_tokens": 23375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9944
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U3wrAzMNGR5eqJuXeK4Mhw`</summary>

```json
{
  "query": "arXiv 2605.15155 SDAR Self-Distilled Agentic Reinforcement Learning authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "9f478884-5b02-409d-8318-b3a54822afd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jJCZbFwJixyjsU4cHD7iR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9944,
      "cache_read_input_tokens": 23375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9944
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LkYTNx3qMW9BTdVY7rfbAi`</summary>

```json
{
  "query": "arXiv 2604.02268 SKILL0 In-Context Agentic Reinforcement Learning authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "89fa2d09-85db-4736-8e1d-01d5e8668db6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jJCZbFwJixyjsU4cHD7iR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9944,
      "cache_read_input_tokens": 23375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9944
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NuDzjiCbrJw2c72hQsiSv9`</summary>

```json
{
  "query": "arXiv 2603.08706 ACT Agentic Critical Training authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "3e5042fe-00dd-490f-b25a-79d49f8971d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jJCZbFwJixyjsU4cHD7iR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9944,
      "cache_read_input_tokens": 23375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9944
      },
      "output_tokens": 21,
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

_source line 14 · 2026-05-16T00:19:06.438Z_

<details><summary>↩ Tool result · `toolu_01U3wrAzMNGR5eqJuXeK4Mhw`</summary>

```text
Web search results for query: "arXiv 2605.15155 SDAR Self-Distilled Agentic Reinforcement Learning authors"

Links: [{"title":"[2605.15155] Self-Distilled Agentic Reinforcement Learning","url":"https://arxiv.org/abs/2605.15155"},{"title":"Paper page - Self-Distilled Agentic Reinforcement Learning","url":"https://huggingface.co/papers/2605.15155"},{"title":"Self-Distilled Agentic Reinforcement Learning","url":"https://arxiv.org/html/2605.15155"},{"title":"GitHub - ZJU-REAL/SDAR: Official code for \"Self-Distilled Agentic Reinforcement Learning\" · GitHub","url":"https://github.com/ZJU-REAL/SDAR"},{"title":"Explore | alphaXiv","url":"https://www.alphaxiv.org/?categories=%5B%22computer-science%22%5D"},{"title":"SDPO: Reinforcement Learning via Self-Distillation","url":"https://self-distillation.github.io/SDPO"},{"title":"[2604.10029] Self-Distilled Reinforcement Learning for Co-Evolving Agentic Recommender Systems","url":"https://arxiv.org/abs/2604.10029"},{"title":"Ola Lindeberg's Post","url":"https://www.linkedin.com/posts/olalindeberg_amazed-by-how-much-llms-can-benefit-causal-activity-7392092905173303296-tMU3"},{"title":"Reinforcement Learning via Self-Distillation","url":"https://podcasts.apple.com/us/podcast/reinforcement-learning-via-self-distillation/id1835878324?i=1000748567886&l=zh-Hans-CN"},{"title":"Reinforcement Learning via Self-Distillation","url":"https://arxiv.org/html/2601.20802"}]

Based on the search results, the authors of the arXiv paper 2605.15155 "Self-Distilled Agentic Reinforcement Learning" (SDAR) are: Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, and Yongliang Shen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "bafea8ff-f568-44c5-8d10-b8f52d1555e9",
  "tool_use_result": {
    "query": "arXiv 2605.15155 SDAR Self-Distilled Agentic Reinforcement Learning authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KWMZ8k63ZoKmqUwSDsHo32",
        "content": [
          {
            "title": "[2605.15155] Self-Distilled Agentic Reinforcement Learning",
            "url": "https://arxiv.org/abs/2605.15155"
          },
          {
            "title": "Paper page - Self-Distilled Agentic Reinforcement Learning",
            "url": "https://huggingface.co/papers/2605.15155"
          },
          {
            "title": "Self-Distilled Agentic Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.15155"
          },
          {
            "title": "GitHub - ZJU-REAL/SDAR: Official code for \"Self-Distilled Agentic Reinforcement Learning\" · GitHub",
            "url": "https://github.com/ZJU-REAL/SDAR"
          },
          {
            "title": "Explore | alphaXiv",
            "url": "https://www.alphaxiv.org/?categories=%5B%22computer-science%22%5D"
          },
          {
            "title": "SDPO: Reinforcement Learning via Self-Distillation",
            "url": "https://self-distillation.github.io/SDPO"
          },
          {
            "title": "[2604.10029] Self-Distilled Reinforcement Learning for Co-Evolving Agentic Recommender Systems",
            "url": "https://arxiv.org/abs/2604.10029"
          },
          {
            "title": "Ola Lindeberg's Post",
            "url": "https://www.linkedin.com/posts/olalindeberg_amazed-by-how-much-llms-can-benefit-causal-activity-7392092905173303296-tMU3"
          },
          {
            "title": "Reinforcement Learning via Self-Distillation",
            "url": "https://podcasts.apple.com/us/podcast/reinforcement-learning-via-self-distillation/id1835878324?i=1000748567886&l=zh-Hans-CN"
          },
          {
            "title": "Reinforcement Learning via Self-Distillation",
            "url": "https://arxiv.org/html/2601.20802"
          }
        ]
      },
      "Based on the search results, the authors of the arXiv paper 2605.15155 \"Self-Distilled Agentic Reinforcement Learning\" (SDAR) are: Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, and Yongliang Shen."
    ],
    "durationSeconds": 3.9747007389999998
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T00:19:07.147Z_

<details><summary>↩ Tool result · `toolu_01NuDzjiCbrJw2c72hQsiSv9`</summary>

```text
Web search results for query: "arXiv 2603.08706 ACT Agentic Critical Training authors"

Links: [{"title":"[2603.08706] Agentic Critical Training","url":"https://arxiv.org/abs/2603.08706"},{"title":"Agentic Critical Training","url":"https://arxiv.org/pdf/2603.08706"},{"title":"[2603.08706v1] Agentic Critical Training","url":"https://arxiv.org/abs/2603.08706v1"},{"title":"Agentic Critical Training","url":"https://attention-is-all-i-need.github.io/ACT/"},{"title":"[2603.03205v1] Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use","url":"https://arxiv.org/abs/2603.03205v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.04746v1"},{"title":"[2603.03205] Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use","url":"https://arxiv.org/abs/2603.03205"},{"title":"[2603.18197] Access Controlled Website Interaction for Agentic AI with Delegated Critical Tasks","url":"https://arxiv.org/abs/2603.18197"},{"title":"Responsible Agentic Reasoning and AI Agents: A Critical Survey","url":"https://www.techrxiv.org/users/574774/articles/1329333/master/file/data/Responsible_reasoning_survey%20(5)/Responsible_reasoning_survey%20(5).pdf"},{"title":"[2603.15914] The Agentic Researcher: A Practical Guide to AI-Assisted Research in Mathematics and Machine Learning","url":"https://arxiv.org/abs/2603.15914"}]

Based on the search results, the authors of arXiv paper 2603.08706 "Agentic Critical Training" are Weize Liu, Minghui Liu, Sy-Tuyen Ho, Souradip Chakraborty, Xiyao Wang, and Furong Huang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "b75bb36a-fc1c-4cea-8d7b-c1ea72bdb2a6",
  "tool_use_result": {
    "query": "arXiv 2603.08706 ACT Agentic Critical Training authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BEdGqEhaezipwobAK4U2tM",
        "content": [
          {
            "title": "[2603.08706] Agentic Critical Training",
            "url": "https://arxiv.org/abs/2603.08706"
          },
          {
            "title": "Agentic Critical Training",
            "url": "https://arxiv.org/pdf/2603.08706"
          },
          {
            "title": "[2603.08706v1] Agentic Critical Training",
            "url": "https://arxiv.org/abs/2603.08706v1"
          },
          {
            "title": "Agentic Critical Training",
            "url": "https://attention-is-all-i-need.github.io/ACT/"
          },
          {
            "title": "[2603.03205v1] Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use",
            "url": "https://arxiv.org/abs/2603.03205v1"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.04746v1"
          },
          {
            "title": "[2603.03205] Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use",
            "url": "https://arxiv.org/abs/2603.03205"
          },
          {
            "title": "[2603.18197] Access Controlled Website Interaction for Agentic AI with Delegated Critical Tasks",
            "url": "https://arxiv.org/abs/2603.18197"
          },
          {
            "title": "Responsible Agentic Reasoning and AI Agents: A Critical Survey",
            "url": "https://www.techrxiv.org/users/574774/articles/1329333/master/file/data/Responsible_reasoning_survey%20(5)/Responsible_reasoning_survey%20(5).pdf"
          },
          {
            "title": "[2603.15914] The Agentic Researcher: A Practical Guide to AI-Assisted Research in Mathematics and Machine Learning",
            "url": "https://arxiv.org/abs/2603.15914"
          }
        ]
      },
      "Based on the search results, the authors of arXiv paper 2603.08706 \"Agentic Critical Training\" are Weize Liu, Minghui Liu, Sy-Tuyen Ho, Souradip Chakraborty, Xiyao Wang, and Furong Huang."
    ],
    "durationSeconds": 3.2212884560000004
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T00:19:07.919Z_

<details><summary>↩ Tool result · `toolu_01LkYTNx3qMW9BTdVY7rfbAi`</summary>

```text
Web search results for query: "arXiv 2604.02268 SKILL0 In-Context Agentic Reinforcement Learning authors"

Links: [{"title":"[2604.02268] SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization","url":"https://arxiv.org/abs/2604.02268"},{"title":"Skill0: In-Context Agentic Reinforcement Learning for Skill Internalization","url":"https://arxiv.org/html/2604.02268v1"},{"title":"(PDF) SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization","url":"https://www.researchgate.net/publication/403467632_SKILL0_In-Context_Agentic_Reinforcement_Learning_for_Skill_Internalization"},{"title":"GitHub - ZJU-REAL/SkillZero: Official code for \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\" · GitHub","url":"https://github.com/ZJU-REAL/SkillZero"},{"title":"Paper page - SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization","url":"https://huggingface.co/papers/2604.02268"},{"title":"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization | alphaXiv","url":"https://www.alphaxiv.org/resources/2604.02268"},{"title":"[Paper Note] SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization, Zhengxi Lu+, arXiv'26, 2026.04 · AkihikoWatanabe/paper_notes@5ea6144","url":"https://github.com/AkihikoWatanabe/paper_notes/actions/runs/24027506673"},{"title":"alphaXiv on X: \"“SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization” Most agent systems use skills like cheat sheets. It retrieves them at runtime, pastes them into the prompt, and hopes the model follows them. This paper suggests why not train the model with those https://t.co/aig1e8d3ZJ\" / X","url":"https://x.com/askalphaxiv/status/2041420021788705207"},{"title":"Rethinking Agentic Reinforcement Learning In Large Language Models","url":"https://arxiv.org/html/2604.27859v1"},{"title":"A Brief Overview: Agentic Reinforcement Learning In Large Language Models","url":"https://arxiv.org/html/2604.27859"}]

Based on the search results, the authors of arXiv 2604.02268 "SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization" are Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Chengcheng Han, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, and Yongliang Shen.

The paper was submitted on April 2, 2026, and the authors are affiliated with Zhejiang University, Meituan, and Tsinghua University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "ae649215-44b5-4343-9963-45e3a30f4010",
  "tool_use_result": {
    "query": "arXiv 2604.02268 SKILL0 In-Context Agentic Reinforcement Learning authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FnyoTn2Y3dnJEyA7rLFiTb",
        "content": [
          {
            "title": "[2604.02268] SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization",
            "url": "https://arxiv.org/abs/2604.02268"
          },
          {
            "title": "Skill0: In-Context Agentic Reinforcement Learning for Skill Internalization",
            "url": "https://arxiv.org/html/2604.02268v1"
          },
          {
            "title": "(PDF) SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization",
            "url": "https://www.researchgate.net/publication/403467632_SKILL0_In-Context_Agentic_Reinforcement_Learning_for_Skill_Internalization"
          },
          {
            "title": "GitHub - ZJU-REAL/SkillZero: Official code for \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\" · GitHub",
            "url": "https://github.com/ZJU-REAL/SkillZero"
          },
          {
            "title": "Paper page - SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization",
            "url": "https://huggingface.co/papers/2604.02268"
          },
          {
            "title": "SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2604.02268"
          },
          {
            "title": "[Paper Note] SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization, Zhengxi Lu+, arXiv'26, 2026.04 · AkihikoWatanabe/paper_notes@5ea6144",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/actions/runs/24027506673"
          },
          {
            "title": "alphaXiv on X: \"“SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization” Most agent systems use skills like cheat sheets. It retrieves them at runtime, pastes them into the prompt, and hopes the model follows them. This paper suggests why not train the model with those https://t.co/aig1e8d3ZJ\" / X",
            "url": "https://x.com/askalphaxiv/status/2041420021788705207"
          },
          {
            "title": "Rethinking Agentic Reinforcement Learning In Large Language Models",
            "url": "https://arxiv.org/html/2604.27859v1"
          },
          {
            "title": "A Brief Overview: Agentic Reinforcement Learning In Large Language Models",
            "url": "https://arxiv.org/html/2604.27859"
          }
        ]
      },
      "Based on the search results, the authors of arXiv 2604.02268 \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\" are Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Chengcheng Han, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, and Yongliang Shen.\n\nThe paper was submitted on April 2, 2026, and the authors are affiliated with Zhejiang University, Meituan, and Tsinghua University."
    ],
    "durationSeconds": 4.103308103000002
  }
}
```

</details>

---

### Assistant

_source line 17_

三篇论文作者已确认，执行修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "a66aada1-85ef-4234-afc5-eb7d1330169c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLm1qhnMn687MECngTBhS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 594,
      "cache_creation_input_tokens": 1749,
      "cache_read_input_tokens": 33319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1749
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

<details open><summary>🔧 Tool call — Edit · `toolu_01XrsJwxsAFRDkYvrbb3e4Fp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"ZJU-REAL\"",
  "new_string": "  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"Lu et al.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "f82ef6b2-f3b6-4088-9857-a737f5499a6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLm1qhnMn687MECngTBhS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 594,
      "cache_creation_input_tokens": 1749,
      "cache_read_input_tokens": 33319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1749
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

_source line 19 · 2026-05-16T00:19:13.403Z_

<details><summary>↩ Tool result · `toolu_01XrsJwxsAFRDkYvrbb3e4Fp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "f3571cda-1578-4a2f-909e-d88505094f61",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"ZJU-REAL\"",
    "newString": "  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"Lu et al.\"",
    "originalFile": "# B-IAVR Literature Map\n# Updated: 2026-05-16\n# Categories: direct-competitor, method-component, background, evaluation\n# Roles: predecessor, competitor, baseline, evaluation, background\n\npapers:\n\n  # ============================================================\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\n  # ============================================================\n\n  - id: kamoi2024self-correction-survey\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Kamoi et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2406.01297\"\n    category: background\n    role: background\n    relevance_note: >\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\n\n  - id: tie2025correctbench\n    title: \"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\"\n    authors: \"Tie et al.\"\n    venue: \"NeurIPS 2025 Datasets & Benchmarks\"\n    year: 2025\n    arxiv_id: \"2510.16062\"\n    category: background\n    role: background\n    relevance_note: >\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\n      Supports B-IAVR's selective verification design over blanket correction.\n\n  - id: self-verification-dilemma-2026\n    title: \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\"\n    authors: \"Long et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.03485\"\n    category: background\n    role: background\n    relevance_note: >\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\n      Directly supports B-IAVR's core thesis that verification should be selective.\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\n\n  - id: zhang2025incentivize-self-verify\n    title: \"Incentivizing LLMs to Self-Verify Their Answers\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2506.01369\"\n    category: background\n    role: background\n    relevance_note: >\n      Unifies answer generation and verification via single RL training process.\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\n\n  - id: mar2025\n    title: \"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\"\n    authors: \"Ozer et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.20845\"\n    category: background\n    role: background\n    relevance_note: >\n      Multi-agent self-correction with diverse critic personas.\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\n\n  - id: ssr2025\n    title: \"SSR: Socratic Self-Refine for Large Language Model Reasoning\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.10621\"\n    category: background\n    role: background\n    relevance_note: >\n      Structured Socratic questioning for self-refinement.\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\n\n  - id: verifiagent2025\n    title: \"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\"\n    authors: \"Han et al.\"\n    venue: \"EMNLP 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2504.00406\"\n    category: background\n    role: background\n    relevance_note: >\n      Unified verification agent with meta-verification + tool-based adaptive verification.\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\n\n  # ============================================================\n  # Direction 2: Agent RL Training\n  # ============================================================\n\n  - id: feng2025gigpo\n    title: \"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\"\n    authors: \"Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10978\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\n\n  - id: selfguide2026\n    title: \"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.03098\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\n      The self-guidance signal is the foundation for action-change detection triggering verification.\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\n\n  - id: spear2025\n    title: \"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"\n    authors: \"Qin et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.22601\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Curriculum-based self-imitation for sparse-reward agent tasks.\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\n\n  - id: wei2025webagent-r1\n    title: \"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\"\n    authors: \"Wei et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.16421\"\n    category: background\n    role: background\n    relevance_note: >\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\n\n  - id: dapo2025\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2503.14476\"\n    category: method-component\n    role: background\n    relevance_note: >\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\n\n  - id: digiRL2024\n    title: \"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\"\n    authors: \"Bai et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv_id: \"2406.11896\"\n    category: background\n    role: background\n    relevance_note: >\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\n\n  - id: li2025sorl\n    title: \"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.20718\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\n\n  - id: agentic-rl-survey-2025\n    title: \"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\"\n    authors: \"Zhang et al.\"\n    venue: \"TMLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.02547\"\n    category: background\n    role: background\n    relevance_note: >\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\n\n  - id: skillmaster2026\n    title: \"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.08693\"\n    category: method-component\n    role: background\n    relevance_note: >\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\n      separation of action and verification advantages.\n\n  - id: t2po2026\n    title: \"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\"\n    authors: \"Wang et al.\"\n    venue: \"ICML 2026 Spotlight\"\n    year: 2026\n    arxiv_id: \"2605.02178\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\n\n  - id: gvpo2026\n    title: \"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\"\n    authors: \"Dai et al.\"\n    venue: \"ICLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\n    category: method-component\n    role: background\n    relevance_note: >\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\n      verification signals. Different focus: uses verification for credit assignment during\n      training; B-IAVR learns when to invoke verification at deployment.\n\n  - id: agentv-rl2026\n    title: \"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.16004\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\n      B-IAVR addresses verification timing in agent deployment. Complementary.\n\n  - id: pa-moe2026\n    title: \"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.17038\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\n      Orthogonal architecture innovation; important baseline to cite.\n\n  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"ZJU-REAL\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15155\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\n\n  - id: hcapo2026\n    title: \"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08754\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\n      multi-scale advantage for critical decision states.\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\n      Could improve B-IAVR's reward signal for verification decision steps.\n\n  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Unknown\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08706\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\n      B-IAVR decides when to reflect.\n\n  - id: rwml2026\n    title: \"RWML: Reinforcement World Model Learning for LLM-based Agents\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.05842\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\n\n  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"ZJU-REAL\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.02268\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\n\n  - id: fission-grpo2026\n    title: \"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2601.15625\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\n      Related: error recovery after failure vs B-IAVR's proactive verification.\n\n  - id: selfbudgeter2026\n    title: \"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\"\n    authors: \"Li et al.\"\n    venue: \"ICLR 2026 (under review)\"\n    year: 2025\n    arxiv_id: \"2505.11274\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\n      Parallel concept: SelfBudgeter allocates computation budget;\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\n\n  - id: cove2026\n    title: \"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.01940\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\n\n  # ============================================================\n  # Direction 3: Selective Verification / Adaptive Computation\n  # ============================================================\n\n  - id: wan2025derailer-rerailer\n    title: \"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\"\n    authors: \"Wan et al.\"\n    venue: \"ACL 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2408.13940\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Most directly related competitor. Both do selective verification with binary trigger.\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\n\n  - id: sherlock2025\n    title: \"Sherlock: Reliable and Efficient Agentic Workflow Execution\"\n    authors: \"Microsoft\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.00330\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\n\n  - id: singhi2025when-to-verify\n    title: \"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\"\n    authors: \"Singhi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2504.01005\"\n    category: background\n    role: background\n    relevance_note: >\n      Derives inference scaling laws for solve-vs-verify tradeoff.\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\n      B-IAVR learns this allocation via RL rather than analytically.\n\n  - id: yang2026ares\n    title: \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.07915\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\n      Reduces reasoning tokens by up to 52.7%.\n\n  - id: tu2025autothink\n    title: \"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\"\n    authors: \"Tu et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10832\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\n\n  - id: du2025thinkless\n    title: \"Thinkless: LLM Learns When to Think\"\n    authors: \"Fang et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.13379\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained control token to decide when to invoke extended thinking.\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\n\n  - id: wang2025efficient-agents\n    title: \"Efficient Agents: Building Effective Agents While Reducing Cost\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.02694\"\n    category: background\n    role: background\n    relevance_note: >\n      First systematic study of agent efficiency-effectiveness tradeoff.\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\n\n  - id: venktesh2025trust-but-verify\n    title: \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\"\n    authors: \"Venktesh et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.16665\"\n    category: background\n    role: background\n    relevance_note: >\n      Survey of verification approaches for test-time compute scaling.\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\n\n  - id: agent-omit2026\n    title: \"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\"\n    authors: \"Ning et al.\"\n    venue: \"ICML 2026\"\n    year: 2026\n    arxiv_id: \"2602.04284\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\n\n  - id: ava2026\n    title: \"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\"\n    authors: \"Patel\"\n    venue: \"TMLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Dynamic compute allocation across search, sampling, and verification under budget.\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\n      single-turn reasoning vs multi-turn agent trajectories.\n\n  - id: cast2026\n    title: \"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\"\n    authors: \"Pang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15041\"\n    category: background\n    role: background\n    relevance_note: >\n      Historical execution cases calibrate reasoning depth for tool use.\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\n\n  - id: marginal-token-allocators2026\n    title: \"Agentic AI Systems Should Be Designed as Marginal Token Allocators\"\n    authors: \"Zhu\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.01214\"\n    category: background\n    role: background\n    relevance_note: >\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\n      that verification decisions should reflect marginal cost-benefit analysis.\n\n  - id: argos2025\n    title: \"Argos: Multimodal RL with Adaptive Verifier for AI Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv (revised April 2026)\"\n    year: 2025\n    arxiv_id: \"2512.03438\"\n    category: background\n    role: background\n    relevance_note: >\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\n\n  # ============================================================\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\n  # ============================================================\n\n  - id: kim2025reflact\n    title: \"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\"\n    authors: \"Kim et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.15182\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\n\n  - id: choudhury2025agentprm\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2502.10325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\n\n  - id: xi2025agentprm\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Xi et al.\"\n    venue: \"ACM Web Conference 2026\"\n    year: 2025\n    arxiv_id: \"2511.08325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\n\n  - id: xiang2024retrospex\n    title: \"Retrospex: Language Agent Meets Offline RL Critic\"\n    authors: \"Xiang et al.\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    arxiv_id: \"2505.11807\"\n    category: background\n    role: background\n    relevance_note: >\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\n      Similar architecture could inform B-IAVR's verification value estimation.\n\n  - id: cfgm2025\n    title: \"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\"\n    authors: \"Yang et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2508.15305\"\n    category: background\n    role: background\n    relevance_note: >\n      Memory-augmented agent planning with episodic grounding.\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\n\n  - id: respact2024\n    title: \"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\"\n    authors: \"Dongre et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2411.00927\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\n",
    "structuredPatch": [
      {
        "oldStart": 266,
        "oldLines": 7,
        "newStart": 266,
        "newLines": 7,
        "lines": [
          " ",
          "   - id: sdar2026",
          "     title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"",
          "-    authors: \"ZJU-REAL\"",
          "+    authors: \"Lu et al.\"",
          "     venue: \"arXiv\"",
          "     year: 2026",
          "     arxiv_id: \"2605.15155\""
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

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01XmRe7u2GQc9whPYhH9tNNW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"ZJU-REAL\"",
  "new_string": "  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"Lu et al.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "5f0005bf-3d22-456a-b289-9711908f6f62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLm1qhnMn687MECngTBhS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 594,
      "cache_creation_input_tokens": 1749,
      "cache_read_input_tokens": 33319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1749
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

_source line 21 · 2026-05-16T00:19:14.787Z_

<details><summary>↩ Tool result · `toolu_01XmRe7u2GQc9whPYhH9tNNW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "7f88108e-dbdb-4f2a-9ee5-2a3293b29830",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"ZJU-REAL\"",
    "newString": "  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"Lu et al.\"",
    "originalFile": "# B-IAVR Literature Map\n# Updated: 2026-05-16\n# Categories: direct-competitor, method-component, background, evaluation\n# Roles: predecessor, competitor, baseline, evaluation, background\n\npapers:\n\n  # ============================================================\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\n  # ============================================================\n\n  - id: kamoi2024self-correction-survey\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Kamoi et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2406.01297\"\n    category: background\n    role: background\n    relevance_note: >\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\n\n  - id: tie2025correctbench\n    title: \"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\"\n    authors: \"Tie et al.\"\n    venue: \"NeurIPS 2025 Datasets & Benchmarks\"\n    year: 2025\n    arxiv_id: \"2510.16062\"\n    category: background\n    role: background\n    relevance_note: >\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\n      Supports B-IAVR's selective verification design over blanket correction.\n\n  - id: self-verification-dilemma-2026\n    title: \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\"\n    authors: \"Long et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.03485\"\n    category: background\n    role: background\n    relevance_note: >\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\n      Directly supports B-IAVR's core thesis that verification should be selective.\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\n\n  - id: zhang2025incentivize-self-verify\n    title: \"Incentivizing LLMs to Self-Verify Their Answers\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2506.01369\"\n    category: background\n    role: background\n    relevance_note: >\n      Unifies answer generation and verification via single RL training process.\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\n\n  - id: mar2025\n    title: \"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\"\n    authors: \"Ozer et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.20845\"\n    category: background\n    role: background\n    relevance_note: >\n      Multi-agent self-correction with diverse critic personas.\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\n\n  - id: ssr2025\n    title: \"SSR: Socratic Self-Refine for Large Language Model Reasoning\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.10621\"\n    category: background\n    role: background\n    relevance_note: >\n      Structured Socratic questioning for self-refinement.\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\n\n  - id: verifiagent2025\n    title: \"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\"\n    authors: \"Han et al.\"\n    venue: \"EMNLP 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2504.00406\"\n    category: background\n    role: background\n    relevance_note: >\n      Unified verification agent with meta-verification + tool-based adaptive verification.\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\n\n  # ============================================================\n  # Direction 2: Agent RL Training\n  # ============================================================\n\n  - id: feng2025gigpo\n    title: \"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\"\n    authors: \"Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10978\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\n\n  - id: selfguide2026\n    title: \"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.03098\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\n      The self-guidance signal is the foundation for action-change detection triggering verification.\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\n\n  - id: spear2025\n    title: \"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"\n    authors: \"Qin et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.22601\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Curriculum-based self-imitation for sparse-reward agent tasks.\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\n\n  - id: wei2025webagent-r1\n    title: \"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\"\n    authors: \"Wei et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.16421\"\n    category: background\n    role: background\n    relevance_note: >\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\n\n  - id: dapo2025\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2503.14476\"\n    category: method-component\n    role: background\n    relevance_note: >\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\n\n  - id: digiRL2024\n    title: \"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\"\n    authors: \"Bai et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv_id: \"2406.11896\"\n    category: background\n    role: background\n    relevance_note: >\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\n\n  - id: li2025sorl\n    title: \"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.20718\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\n\n  - id: agentic-rl-survey-2025\n    title: \"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\"\n    authors: \"Zhang et al.\"\n    venue: \"TMLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.02547\"\n    category: background\n    role: background\n    relevance_note: >\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\n\n  - id: skillmaster2026\n    title: \"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.08693\"\n    category: method-component\n    role: background\n    relevance_note: >\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\n      separation of action and verification advantages.\n\n  - id: t2po2026\n    title: \"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\"\n    authors: \"Wang et al.\"\n    venue: \"ICML 2026 Spotlight\"\n    year: 2026\n    arxiv_id: \"2605.02178\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\n\n  - id: gvpo2026\n    title: \"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\"\n    authors: \"Dai et al.\"\n    venue: \"ICLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\n    category: method-component\n    role: background\n    relevance_note: >\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\n      verification signals. Different focus: uses verification for credit assignment during\n      training; B-IAVR learns when to invoke verification at deployment.\n\n  - id: agentv-rl2026\n    title: \"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.16004\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\n      B-IAVR addresses verification timing in agent deployment. Complementary.\n\n  - id: pa-moe2026\n    title: \"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.17038\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\n      Orthogonal architecture innovation; important baseline to cite.\n\n  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15155\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\n\n  - id: hcapo2026\n    title: \"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08754\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\n      multi-scale advantage for critical decision states.\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\n      Could improve B-IAVR's reward signal for verification decision steps.\n\n  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Unknown\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08706\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\n      B-IAVR decides when to reflect.\n\n  - id: rwml2026\n    title: \"RWML: Reinforcement World Model Learning for LLM-based Agents\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.05842\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\n\n  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"ZJU-REAL\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.02268\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\n\n  - id: fission-grpo2026\n    title: \"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2601.15625\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\n      Related: error recovery after failure vs B-IAVR's proactive verification.\n\n  - id: selfbudgeter2026\n    title: \"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\"\n    authors: \"Li et al.\"\n    venue: \"ICLR 2026 (under review)\"\n    year: 2025\n    arxiv_id: \"2505.11274\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\n      Parallel concept: SelfBudgeter allocates computation budget;\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\n\n  - id: cove2026\n    title: \"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.01940\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\n\n  # ============================================================\n  # Direction 3: Selective Verification / Adaptive Computation\n  # ============================================================\n\n  - id: wan2025derailer-rerailer\n    title: \"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\"\n    authors: \"Wan et al.\"\n    venue: \"ACL 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2408.13940\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Most directly related competitor. Both do selective verification with binary trigger.\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\n\n  - id: sherlock2025\n    title: \"Sherlock: Reliable and Efficient Agentic Workflow Execution\"\n    authors: \"Microsoft\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.00330\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\n\n  - id: singhi2025when-to-verify\n    title: \"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\"\n    authors: \"Singhi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2504.01005\"\n    category: background\n    role: background\n    relevance_note: >\n      Derives inference scaling laws for solve-vs-verify tradeoff.\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\n      B-IAVR learns this allocation via RL rather than analytically.\n\n  - id: yang2026ares\n    title: \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.07915\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\n      Reduces reasoning tokens by up to 52.7%.\n\n  - id: tu2025autothink\n    title: \"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\"\n    authors: \"Tu et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10832\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\n\n  - id: du2025thinkless\n    title: \"Thinkless: LLM Learns When to Think\"\n    authors: \"Fang et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.13379\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained control token to decide when to invoke extended thinking.\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\n\n  - id: wang2025efficient-agents\n    title: \"Efficient Agents: Building Effective Agents While Reducing Cost\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.02694\"\n    category: background\n    role: background\n    relevance_note: >\n      First systematic study of agent efficiency-effectiveness tradeoff.\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\n\n  - id: venktesh2025trust-but-verify\n    title: \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\"\n    authors: \"Venktesh et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.16665\"\n    category: background\n    role: background\n    relevance_note: >\n      Survey of verification approaches for test-time compute scaling.\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\n\n  - id: agent-omit2026\n    title: \"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\"\n    authors: \"Ning et al.\"\n    venue: \"ICML 2026\"\n    year: 2026\n    arxiv_id: \"2602.04284\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\n\n  - id: ava2026\n    title: \"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\"\n    authors: \"Patel\"\n    venue: \"TMLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Dynamic compute allocation across search, sampling, and verification under budget.\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\n      single-turn reasoning vs multi-turn agent trajectories.\n\n  - id: cast2026\n    title: \"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\"\n    authors: \"Pang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15041\"\n    category: background\n    role: background\n    relevance_note: >\n      Historical execution cases calibrate reasoning depth for tool use.\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\n\n  - id: marginal-token-allocators2026\n    title: \"Agentic AI Systems Should Be Designed as Marginal Token Allocators\"\n    authors: \"Zhu\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.01214\"\n    category: background\n    role: background\n    relevance_note: >\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\n      that verification decisions should reflect marginal cost-benefit analysis.\n\n  - id: argos2025\n    title: \"Argos: Multimodal RL with Adaptive Verifier for AI Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv (revised April 2026)\"\n    year: 2025\n    arxiv_id: \"2512.03438\"\n    category: background\n    role: background\n    relevance_note: >\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\n\n  # ============================================================\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\n  # ============================================================\n\n  - id: kim2025reflact\n    title: \"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\"\n    authors: \"Kim et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.15182\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\n\n  - id: choudhury2025agentprm\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2502.10325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\n\n  - id: xi2025agentprm\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Xi et al.\"\n    venue: \"ACM Web Conference 2026\"\n    year: 2025\n    arxiv_id: \"2511.08325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\n\n  - id: xiang2024retrospex\n    title: \"Retrospex: Language Agent Meets Offline RL Critic\"\n    authors: \"Xiang et al.\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    arxiv_id: \"2505.11807\"\n    category: background\n    role: background\n    relevance_note: >\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\n      Similar architecture could inform B-IAVR's verification value estimation.\n\n  - id: cfgm2025\n    title: \"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\"\n    authors: \"Yang et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2508.15305\"\n    category: background\n    role: background\n    relevance_note: >\n      Memory-augmented agent planning with episodic grounding.\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\n\n  - id: respact2024\n    title: \"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\"\n    authors: \"Dongre et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2411.00927\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\n",
    "structuredPatch": [
      {
        "oldStart": 319,
        "oldLines": 7,
        "newStart": 319,
        "newLines": 7,
        "lines": [
          " ",
          "   - id: skill0-2026",
          "     title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"",
          "-    authors: \"ZJU-REAL\"",
          "+    authors: \"Lu et al.\"",
          "     venue: \"arXiv\"",
          "     year: 2026",
          "     arxiv_id: \"2604.02268\""
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01S8uQexjTa4WzqXMJ9eV98Q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Unknown\"",
  "new_string": "  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Liu et al.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "4531c9fe-3db9-4ecb-ad8d-994b7eb7dd9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLm1qhnMn687MECngTBhS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 594,
      "cache_creation_input_tokens": 1749,
      "cache_read_input_tokens": 33319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1749
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

_source line 23 · 2026-05-16T00:19:16.006Z_

<details><summary>↩ Tool result · `toolu_01S8uQexjTa4WzqXMJ9eV98Q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "cbe7b787-dcd1-4992-b3cf-aebca08651db",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml",
    "oldString": "  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Unknown\"",
    "newString": "  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Liu et al.\"",
    "originalFile": "# B-IAVR Literature Map\n# Updated: 2026-05-16\n# Categories: direct-competitor, method-component, background, evaluation\n# Roles: predecessor, competitor, baseline, evaluation, background\n\npapers:\n\n  # ============================================================\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\n  # ============================================================\n\n  - id: kamoi2024self-correction-survey\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Kamoi et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2406.01297\"\n    category: background\n    role: background\n    relevance_note: >\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\n\n  - id: tie2025correctbench\n    title: \"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\"\n    authors: \"Tie et al.\"\n    venue: \"NeurIPS 2025 Datasets & Benchmarks\"\n    year: 2025\n    arxiv_id: \"2510.16062\"\n    category: background\n    role: background\n    relevance_note: >\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\n      Supports B-IAVR's selective verification design over blanket correction.\n\n  - id: self-verification-dilemma-2026\n    title: \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\"\n    authors: \"Long et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.03485\"\n    category: background\n    role: background\n    relevance_note: >\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\n      Directly supports B-IAVR's core thesis that verification should be selective.\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\n\n  - id: zhang2025incentivize-self-verify\n    title: \"Incentivizing LLMs to Self-Verify Their Answers\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2506.01369\"\n    category: background\n    role: background\n    relevance_note: >\n      Unifies answer generation and verification via single RL training process.\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\n\n  - id: mar2025\n    title: \"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\"\n    authors: \"Ozer et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2512.20845\"\n    category: background\n    role: background\n    relevance_note: >\n      Multi-agent self-correction with diverse critic personas.\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\n\n  - id: ssr2025\n    title: \"SSR: Socratic Self-Refine for Large Language Model Reasoning\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.10621\"\n    category: background\n    role: background\n    relevance_note: >\n      Structured Socratic questioning for self-refinement.\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\n\n  - id: verifiagent2025\n    title: \"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\"\n    authors: \"Han et al.\"\n    venue: \"EMNLP 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2504.00406\"\n    category: background\n    role: background\n    relevance_note: >\n      Unified verification agent with meta-verification + tool-based adaptive verification.\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\n\n  # ============================================================\n  # Direction 2: Agent RL Training\n  # ============================================================\n\n  - id: feng2025gigpo\n    title: \"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\"\n    authors: \"Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10978\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\n\n  - id: selfguide2026\n    title: \"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.03098\"\n    category: method-component\n    role: predecessor\n    relevance_note: >\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\n      The self-guidance signal is the foundation for action-change detection triggering verification.\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\n\n  - id: spear2025\n    title: \"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"\n    authors: \"Qin et al.\"\n    venue: \"ICLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.22601\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Curriculum-based self-imitation for sparse-reward agent tasks.\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\n\n  - id: wei2025webagent-r1\n    title: \"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\"\n    authors: \"Wei et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.16421\"\n    category: background\n    role: background\n    relevance_note: >\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\n\n  - id: dapo2025\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2503.14476\"\n    category: method-component\n    role: background\n    relevance_note: >\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\n\n  - id: digiRL2024\n    title: \"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\"\n    authors: \"Bai et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    arxiv_id: \"2406.11896\"\n    category: background\n    role: background\n    relevance_note: >\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\n\n  - id: li2025sorl\n    title: \"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.20718\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\n\n  - id: agentic-rl-survey-2025\n    title: \"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\"\n    authors: \"Zhang et al.\"\n    venue: \"TMLR 2026\"\n    year: 2025\n    arxiv_id: \"2509.02547\"\n    category: background\n    role: background\n    relevance_note: >\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\n\n  - id: skillmaster2026\n    title: \"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.08693\"\n    category: method-component\n    role: background\n    relevance_note: >\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\n      separation of action and verification advantages.\n\n  - id: t2po2026\n    title: \"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\"\n    authors: \"Wang et al.\"\n    venue: \"ICML 2026 Spotlight\"\n    year: 2026\n    arxiv_id: \"2605.02178\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\n\n  - id: gvpo2026\n    title: \"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\"\n    authors: \"Dai et al.\"\n    venue: \"ICLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\n    category: method-component\n    role: background\n    relevance_note: >\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\n      verification signals. Different focus: uses verification for credit assignment during\n      training; B-IAVR learns when to invoke verification at deployment.\n\n  - id: agentv-rl2026\n    title: \"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.16004\"\n    category: method-component\n    role: background\n    relevance_note: >\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\n      B-IAVR addresses verification timing in agent deployment. Complementary.\n\n  - id: pa-moe2026\n    title: \"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\"\n    authors: \"Li et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.17038\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\n      Orthogonal architecture innovation; important baseline to cite.\n\n  - id: sdar2026\n    title: \"SDAR: Self-Distilled Agentic Reinforcement Learning\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15155\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\n\n  - id: hcapo2026\n    title: \"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08754\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\n      multi-scale advantage for critical decision states.\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\n      Could improve B-IAVR's reward signal for verification decision steps.\n\n  - id: act2026\n    title: \"ACT: Agentic Critical Training\"\n    authors: \"Unknown\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.08706\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\n      B-IAVR decides when to reflect.\n\n  - id: rwml2026\n    title: \"RWML: Reinforcement World Model Learning for LLM-based Agents\"\n    authors: \"Yu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2602.05842\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\n\n  - id: skill0-2026\n    title: \"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\"\n    authors: \"Lu et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2604.02268\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\n\n  - id: fission-grpo2026\n    title: \"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2601.15625\"\n    category: method-component\n    role: background\n    relevance_note: >\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\n      Related: error recovery after failure vs B-IAVR's proactive verification.\n\n  - id: selfbudgeter2026\n    title: \"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\"\n    authors: \"Li et al.\"\n    venue: \"ICLR 2026 (under review)\"\n    year: 2025\n    arxiv_id: \"2505.11274\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\n      Parallel concept: SelfBudgeter allocates computation budget;\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\n\n  - id: cove2026\n    title: \"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\"\n    authors: \"Chen et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.01940\"\n    category: background\n    role: background\n    relevance_note: >\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\n\n  # ============================================================\n  # Direction 3: Selective Verification / Adaptive Computation\n  # ============================================================\n\n  - id: wan2025derailer-rerailer\n    title: \"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\"\n    authors: \"Wan et al.\"\n    venue: \"ACL 2025 Findings\"\n    year: 2025\n    arxiv_id: \"2408.13940\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Most directly related competitor. Both do selective verification with binary trigger.\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\n\n  - id: sherlock2025\n    title: \"Sherlock: Reliable and Efficient Agentic Workflow Execution\"\n    authors: \"Microsoft\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2511.00330\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\n\n  - id: singhi2025when-to-verify\n    title: \"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\"\n    authors: \"Singhi et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2504.01005\"\n    category: background\n    role: background\n    relevance_note: >\n      Derives inference scaling laws for solve-vs-verify tradeoff.\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\n      B-IAVR learns this allocation via RL rather than analytically.\n\n  - id: yang2026ares\n    title: \"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2603.07915\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\n      Reduces reasoning tokens by up to 52.7%.\n\n  - id: tu2025autothink\n    title: \"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\"\n    authors: \"Tu et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.10832\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\n\n  - id: du2025thinkless\n    title: \"Thinkless: LLM Learns When to Think\"\n    authors: \"Fang et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    arxiv_id: \"2505.13379\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained control token to decide when to invoke extended thinking.\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\n\n  - id: wang2025efficient-agents\n    title: \"Efficient Agents: Building Effective Agents While Reducing Cost\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.02694\"\n    category: background\n    role: background\n    relevance_note: >\n      First systematic study of agent efficiency-effectiveness tradeoff.\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\n\n  - id: venktesh2025trust-but-verify\n    title: \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\"\n    authors: \"Venktesh et al.\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2508.16665\"\n    category: background\n    role: background\n    relevance_note: >\n      Survey of verification approaches for test-time compute scaling.\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\n\n  - id: agent-omit2026\n    title: \"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\"\n    authors: \"Ning et al.\"\n    venue: \"ICML 2026\"\n    year: 2026\n    arxiv_id: \"2602.04284\"\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\n\n  - id: ava2026\n    title: \"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\"\n    authors: \"Patel\"\n    venue: \"TMLR 2026\"\n    year: 2026\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\n    category: direct-competitor\n    role: competitor\n    relevance_note: >\n      Dynamic compute allocation across search, sampling, and verification under budget.\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\n      single-turn reasoning vs multi-turn agent trajectories.\n\n  - id: cast2026\n    title: \"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\"\n    authors: \"Pang et al.\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.15041\"\n    category: background\n    role: background\n    relevance_note: >\n      Historical execution cases calibrate reasoning depth for tool use.\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\n\n  - id: marginal-token-allocators2026\n    title: \"Agentic AI Systems Should Be Designed as Marginal Token Allocators\"\n    authors: \"Zhu\"\n    venue: \"arXiv\"\n    year: 2026\n    arxiv_id: \"2605.01214\"\n    category: background\n    role: background\n    relevance_note: >\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\n      that verification decisions should reflect marginal cost-benefit analysis.\n\n  - id: argos2025\n    title: \"Argos: Multimodal RL with Adaptive Verifier for AI Agents\"\n    authors: \"Tan et al.\"\n    venue: \"arXiv (revised April 2026)\"\n    year: 2025\n    arxiv_id: \"2512.03438\"\n    category: background\n    role: background\n    relevance_note: >\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\n\n  # ============================================================\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\n  # ============================================================\n\n  - id: kim2025reflact\n    title: \"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\"\n    authors: \"Kim et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2505.15182\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\n\n  - id: choudhury2025agentprm\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    venue: \"arXiv\"\n    year: 2025\n    arxiv_id: \"2502.10325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\n\n  - id: xi2025agentprm\n    title: \"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\"\n    authors: \"Xi et al.\"\n    venue: \"ACM Web Conference 2026\"\n    year: 2025\n    arxiv_id: \"2511.08325\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\n\n  - id: xiang2024retrospex\n    title: \"Retrospex: Language Agent Meets Offline RL Critic\"\n    authors: \"Xiang et al.\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    arxiv_id: \"2505.11807\"\n    category: background\n    role: background\n    relevance_note: >\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\n      Similar architecture could inform B-IAVR's verification value estimation.\n\n  - id: cfgm2025\n    title: \"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\"\n    authors: \"Yang et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    arxiv_id: \"2508.15305\"\n    category: background\n    role: background\n    relevance_note: >\n      Memory-augmented agent planning with episodic grounding.\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\n\n  - id: respact2024\n    title: \"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\"\n    authors: \"Dongre et al.\"\n    venue: \"arXiv\"\n    year: 2024\n    arxiv_id: \"2411.00927\"\n    category: evaluation\n    role: baseline\n    relevance_note: >\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\n",
    "structuredPatch": [
      {
        "oldStart": 293,
        "oldLines": 7,
        "newStart": 293,
        "newLines": 7,
        "lines": [
          " ",
          "   - id: act2026",
          "     title: \"ACT: Agentic Critical Training\"",
          "-    authors: \"Unknown\"",
          "+    authors: \"Liu et al.\"",
          "     venue: \"arXiv\"",
          "     year: 2026",
          "     arxiv_id: \"2603.08706\""
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

_source line 24_

修改完成：

| 条目 | 修正前 | 修正后 | 首作者全名 |
|------|--------|--------|-----------|
| `sdar2026` | `"ZJU-REAL"` | `"Lu et al."` | Zhengxi Lu |
| `skill0-2026` | `"ZJU-REAL"` | `"Lu et al."` | Zhengxi Lu |
| `act2026` | `"Unknown"` | `"Liu et al."` | Weize Liu |

注：sdar2026 和 skill0-2026 均为 ZJU-REAL 实验室同一第一作者 Zhengxi Lu 的工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "uuid": "94450f23-742c-4cee-93c6-f4fe29f8d3da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4aFRKou4qZP7xxjkAYiFy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1553,
      "cache_read_input_tokens": 35068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1553
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

修改完成：

| 条目 | 修正前 | 修正后 | 首作者全名 |
|------|--------|--------|-----------|
| `sdar2026` | `"ZJU-REAL"` | `"Lu et al."` | Zhengxi Lu |
| `skill0-2026` | `"ZJU-REAL"` | `"Lu et al."` | Zhengxi Lu |
| `act2026` | `"Unknown"` | `"Liu et al."` | Weize Liu |

注：sdar2026 和 skill0-2026 均为 ZJU-REAL 实验室同一第一作者 Zhengxi Lu 的工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 26367,
  "duration_api_ms": 34603,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "59100853-7e2d-41ce-bbd6-d96f6d583cfa",
  "total_cost_usd": 0.32214149999999997,
  "usage": {
    "input_tokens": 600,
    "cache_creation_input_tokens": 24780,
    "cache_read_input_tokens": 103603,
    "output_tokens": 1200,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24780,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 187,
        "cache_read_input_tokens": 35068,
        "cache_creation_input_tokens": 1553,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1553
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 49480,
      "outputTokens": 597,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 3,
      "costUSD": 0.08246500000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 600,
      "outputTokens": 1200,
      "cacheReadInputTokens": 103603,
      "cacheCreationInputTokens": 24780,
      "webSearchRequests": 0,
      "costUSD": 0.23967650000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7618a23e-00a3-43f5-ade5-71e27ef98f1a"
}
```

</details>

---
