# paper research bib sync

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_paper_research_bib_sync_20260514T183047.log`
- **Structured JSON:** [`6ead93238d763d5e05b6.json`](../../sessions/6e/6ead93238d763d5e05b6.json)

## Before a recorded user message

19 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "a356cc63-399d-4ef9-bc2a-5dddacd19768",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778800200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7bc796de-149b-4b0a-9bc7-610645bfa294",
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2"
}
```

---

### Assistant

_source line 4_

Let me read the literature map first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "4bef07d5-d281-438c-a5dc-fb182ea2b31a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RL3kvQanm6HjePJyZ8iSCw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12701,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12701
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

<details open><summary>🔧 Tool call — Read · `toolu_01NkdrJgUdEtXUiu78zLq8dz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "9c86401e-7411-4d4b-a108-1c5ce6732e0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RL3kvQanm6HjePJyZ8iSCw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12701,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12701
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

_source line 6 · 2026-05-14T18:30:59.776Z_

<details><summary>↩ Tool result · `toolu_01NkdrJgUdEtXUiu78zLq8dz`</summary>

```text
1	# Literature Map for Solver Trace Ablation (STA)
2	# Categories:
3	#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO
4	#   2. reward-shaping: Reward shaping for code/formal verification
5	#   3. mutation-testing: Mutation testing in software engineering
6	#   4. intensional-analysis: Intensional program analysis
7	#   5. reward-hacking: Reward hacking / overoptimization
8	#   6. fol-formalization: FOL/Prolog formalization with LLMs
9	#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics
10	#   8. verification-reward: Solver/prover as RL reward signal
11	
12	papers:
13	
14	  # ============================================================
15	  # Category 1: Neurosymbolic reasoning + RL/GRPO
16	  # ============================================================
17	
18	  - id: deepseek-r1
19	    title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
20	    authors: "DeepSeek-AI"
21	    year: 2025
22	    venue: "arXiv 2501.12948 / Nature 2025"
23	    category: neurosymbolic-rl
24	    role: method-component
25	    relevance: >
26	      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.
27	      STA builds on the same GRPO framework but replaces binary outcome reward with
28	      intensional structural reward for neurosymbolic formalization.
29	    key_finding: >
30	      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,
31	      showing emergent chain-of-thought reasoning from RL alone.
32	
33	  - id: deepseekmath
34	    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
35	    authors: "Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al."
36	    year: 2024
37	    venue: "arXiv 2402.03300"
38	    category: neurosymbolic-rl
39	    role: method-component
40	    relevance: >
41	      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm
42	      used in STA training. GRPO eliminates the critic model by estimating
43	      baselines from group scores.
44	    key_finding: >
45	      GRPO matches PPO performance while significantly reducing training
46	      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.
47	
48	  - id: logic-rl
49	    title: "Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning"
50	    authors: "Xian et al."
51	    year: 2025
52	    venue: "arXiv 2502.14768"
53	    category: neurosymbolic-rl
54	    role: direct-competitor
55	    relevance: >
56	      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic
57	      logic puzzles. Closest competitor to STA's approach of RL for logical
58	      formalization, though Logic-RL uses extensional (answer-correctness)
59	      rewards rather than STA's intensional structural rewards.
60	    key_finding: >
61	      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;
62	      rule-based reward design is critical for RL-based logical reasoning.
63	
64	  - id: mellgren-prolog-grpo
65	    title: "Training Language Models to Use Prolog as a Tool"
66	    authors: "Niklas Mellgren"
67	    year: 2024
68	    venue: "arXiv 2512.07407"
69	    category: neurosymbolic-rl
70	    role: direct-competitor
71	    relevance: >
72	      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,
73	      directly comparable to STA's approach of GRPO-training a formalizer.
74	      Key difference: uses pass/fail reward vs STA's structural ISR.
75	    key_finding: >
76	      GRPO is effective for teaching small LLMs to use Prolog as a tool
77	      for logical and mathematical reasoning.
78	
79	  - id: satlm
80	    title: "SatLM: Satisfiability-Aided Language Models Using Declarative Prompting"
81	    authors: "Xi Ye et al."
82	    year: 2023
83	    venue: "NeurIPS 2023"
84	    category: neurosymbolic-rl
85	    role: background
86	    relevance: >
87	      Neurosymbolic approach where LLM generates declarative specifications
88	      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)
89	      but uses prompting, not RL training.
90	    key_finding: >
91	      Declarative formulation outperforms imperative program-aided LMs by 23%
92	      on GSM; achieves SoTA on LSAT and BoardgameQA.
93	
94	  - id: deepproblog
95	    title: "Neural Probabilistic Logic Programming in DeepProbLog"
96	    authors: "Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt"
97	    year: 2021
98	    venue: "Artificial Intelligence 298"
99	    category: neurosymbolic-rl
100	    role: background
101	    relevance: >
102	      Foundational neural-probabilistic logic programming framework that integrates
103	      deep learning with ProbLog via neural predicates. Establishes the intellectual
104	      tradition of combining neural networks with logic programming that STA extends
105	      to LLM-generated Prolog with RL training.
106	    key_finding: >
107	      End-to-end differentiable framework integrating neural perception with
108	      probabilistic logical reasoning; supports program induction and learning
109	      from examples.
110	
111	  - id: neurasp
112	    title: "NeurASP: Embracing Neural Networks into Answer Set Programming"
113	    authors: "Zhun Yang, Adam Ishay, Joohyung Lee"
114	    year: 2020
115	    venue: "IJCAI 2020"
116	    category: neurosymbolic-rl
117	    role: background
118	    relevance: >
119	      Integrates neural networks with answer set programming (ASP), using
120	      ASP rules to constrain and improve neural network training. Complementary
121	      to DeepProbLog; together they represent the neuro-symbolic LP foundation
122	      that STA's LLM-to-Prolog pipeline builds upon.
123	    key_finding: >
124	      ASP semantic constraints improve neural network perception accuracy;
125	      demonstrates bidirectional benefit of neural-symbolic integration.
126	
127	  - id: thought-like-pro
128	    title: "Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought"
129	    authors: "Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi"
130	    year: 2024
131	    venue: "arXiv 2407.14562"
132	    category: neurosymbolic-rl
133	    role: direct-competitor
134	    relevance: >
135	      Uses Prolog engine to generate verified reasoning trajectories, then trains
136	      LLMs via imitation learning to replicate them. Directly comparable pipeline
137	      to STA (Prolog verification + LLM training), but uses imitation learning
138	      instead of GRPO with structural reward.
139	    key_finding: >
140	      Prolog-verified reasoning trajectories as training signal improve LLM
141	      logical reasoning; self-driven framework enables LLMs to formulate
142	      rules from instructions and leverage Prolog for derivation.
143	
144	  # ============================================================
145	  # Category 2: Reward shaping for code/formal verification
146	  # ============================================================
147	
148	  - id: lightman-verify-step
149	    title: "Let's Verify Step by Step"
150	    authors: "Hunter Lightman, Vineet Kosaraju, Yura Burda, et al."
151	    year: 2023
152	    venue: "arXiv 2305.20050 / ICLR 2024"
153	    category: reward-shaping
154	    role: method-component
155	    relevance: >
156	      Establishes that process supervision (step-level reward) outperforms
157	      outcome supervision (final-answer reward) for reasoning. STA's ISR
158	      is analogous: it provides structural process-level signal about which
159	      components of a formalization matter, rather than just pass/fail.
160	    key_finding: >
161	      Process-supervised reward model achieves 78% on MATH, significantly
162	      outperforming outcome-supervised models. Released PRM800K dataset.
163	
164	  - id: reward-shaping-rlhf
165	    title: "Reward Shaping to Mitigate Reward Hacking in RLHF"
166	    authors: "Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al."
167	    year: 2025
168	    venue: "arXiv 2502.18770"
169	    category: reward-shaping
170	    role: background
171	    relevance: >
172	      Studies reward shaping design principles for RLHF: bounded rewards and
173	      rapid-then-convergent growth. STA's ISR follows these principles
174	      naturally since structural necessity scores are bounded [0,1].
175	    key_finding: >
176	      Two key reward shaping principles: (1) bounded RL reward, (2) rapid
177	      initial growth with gradual convergence. PAR method achieves 5%+
178	      win rate improvement on AlpacaEval 2.0.
179	
180	  - id: rlvr-reasoning
181	    title: "Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs"
182	    authors: "Various"
183	    year: 2025
184	    venue: "arXiv 2506.14245"
185	    category: reward-shaping
186	    role: background
187	    relevance: >
188	      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize
189	      reasoning. STA argues that for neurosymbolic formalization, binary reward
190	      is insufficient and structural reward is needed to avoid reward hacking.
191	    key_finding: >
192	      RLVR with binary verification implicitly teaches correct reasoning
193	      strategies, not just answer matching.
194	
195	  - id: rubric-grpo
196	    title: "Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning"
197	    authors: "Various"
198	    year: 2025
199	    venue: "arXiv 2605.08061"
200	    category: reward-shaping
201	    role: direct-competitor
202	    relevance: >
203	      Uses structured rubric-based rewards with GRPO, similar in spirit to
204	      STA's structured ISR. Key difference: rubric rewards come from LLM
205	      judges, while ISR comes from solver-based mutation testing.
206	    key_finding: >
207	      Structured multi-dimensional reward signals improve GRPO training
208	      generalization compared to scalar rewards.
209	
210	  - id: gao-effective-rl-reward
211	    title: "On Designing Effective RL Reward at Training Time for LLM Reasoning"
212	    authors: "Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu"
213	    year: 2024
214	    venue: "arXiv 2410.15115"
215	    category: reward-shaping
216	    role: background
217	    relevance: >
218	      Demonstrates that learned process/outcome reward models can hurt RL
219	      training, producing worse performance than simple success reward only.
220	      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process
221	      reward degrades prove_rate compared to exec-only baseline.
222	    key_finding: >
223	      PRM/ORM rewards may NOT help or even hurt RL training vs success-only
224	      reward. Solution: Clipping and Delta techniques to bound accumulated
225	      reward magnitude prevent reward hacking.
226	
227	  - id: prof-process-outcome
228	    title: "Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training"
229	    authors: "Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal"
230	    year: 2025
231	    venue: "arXiv 2509.03403"
232	    category: reward-shaping
233	    role: background
234	    relevance: >
235	      Shows that naively combining PRM+ORM signals leads to performance
236	      degradation. PROF consistency filter retains only PRM-ORM consistent
237	      samples, achieving 4%+ improvement over blending. Suggests STA should
238	      only apply ISR when consistent with execution outcome.
239	    key_finding: >
240	      Process rewards frequently suffer from inaccuracies and reward hacking
241	      susceptibility. PROF filters training data by PRM-ORM consistency,
242	      outperforming naive reward blending by 4%+ accuracy.
243	
244	  - id: moskovitz-constrained-rlhf
245	    title: "Confronting Reward Model Overoptimization with Constrained RLHF"
246	    authors: "Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer"
247	    year: 2023
248	    venue: "arXiv 2310.04373 / ICLR 2024"
249	    category: reward-shaping
250	    role: background
251	    relevance: >
252	      First study on overoptimization in composite reward models. Shows that
253	      fixed-weight linear scalarization of component rewards leads to
254	      degradation past a threshold. Proposes constrained RL with dynamic
255	      Lagrange multiplier weighting as alternative to fixed ISR weight.
256	    key_finding: >
257	      Correlation between component RMs significantly affects overoptimization
258	      thresholds. Constrained RL with Lagrange multipliers outperforms
259	      fixed-weight reward composition.
260	
261	  - id: skalse-reward-hacking
262	    title: "Defining and Characterizing Reward Hacking"
263	    authors: "Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger"
264	    year: 2022
265	    venue: "arXiv 2209.13085 / NeurIPS 2022"
266	    category: reward-shaping
267	    role: background
268	    relevance: >
269	      Formal proof that for stochastic policies, two reward functions are
270	      unhackable only if one is constant. Theoretically explains why any
271	      non-zero ISR weight can decrease prove_rate -- this is a fundamental
272	      property of reward composition, not STA-specific.
273	    key_finding: >
274	      Any non-constant proxy reward can decrease true reward when optimized.
275	      Unhackability requires the proxy to be constant, making all non-trivial
276	      auxiliary rewards theoretically vulnerable to degrading primary performance.
277	
278	  - id: progrs-outcome-conditioned
279	    title: "LLM Reasoning with Process Rewards for Outcome-Guided Steps"
280	    authors: "Mohammad Rezaei, Jens Lehmann, Sahar Vahdati"
281	    year: 2026
282	    venue: "arXiv 2604.02341"
283	    category: reward-shaping
284	    role: background
285	    relevance: >
286	      PRM scores optimized as absolute rewards amplify fluent failure modes.
287	      Outcome-conditioned centering shifts incorrect trajectories' PRM scores
288	      to zero mean, preserving ranking info without corrupting gradients.
289	      Suggests STA should condition ISR on execution outcome.
290	    key_finding: >
291	      Naive process rewards induce reward hacking by rewarding locally fluent
292	      but globally incorrect reasoning. Outcome-conditioned centering resolves
293	      the conflict with fewer rollouts than outcome-only baselines.
294	
295	  - id: qwen-prm-lessons
296	    title: "The Lessons of Developing Process Reward Models in Mathematical Reasoning"
297	    authors: "Zhenru Zhang et al. (Qwen Team, Alibaba)"
298	    year: 2025
299	    venue: "ACL 2025 Findings (arXiv 2501.07301)"
300	    category: reward-shaping
301	    role: supporting-evidence
302	    relevance: >
303	      MC estimation-synthesized PRM data leads to quality degradation; policy
304	      model generates "answer-correct but reasoning-flawed" responses, causing
305	      process reward / outcome misalignment. Directly parallels ISR problem:
306	      structurally correct but semantically wrong proof traces get high ISR
307	      but low execution reward.
308	    key_finding: >
309	      PRM performance depends critically on data quality; MC estimation
310	      introduces systematic bias. Answer-correct reasoning-flawed samples
311	      corrupt process supervision signal.
312	
313	  # ============================================================
314	  # Category 3: Mutation testing in software engineering
315	  # ============================================================
316	
317	  - id: demillo1978
318	    title: "Hints on Test Data Selection: Help for the Practicing Programmer"
319	    authors: "Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward"
320	    year: 1978
321	    venue: "Computer 11(4):34-43"
322	    category: mutation-testing
323	    role: background
324	    relevance: >
325	      Foundational paper introducing mutation testing. STA's component
326	      necessity testing directly extends this idea: instead of mutating
327	      source code to test test suites, STA mutates logical formulas
328	      to test component necessity for solver success.
329	    key_finding: >
330	      Introduced mutation testing and the coupling effect hypothesis:
331	      tests that detect simple faults also detect complex faults.
332	
333	  - id: offutt-coupling
334	    title: "Investigations of the Software Testing Coupling Effect"
335	    authors: "A. Jefferson Offutt"
336	    year: 1992
337	    venue: "ACM TOSEM 1(1):5-20"
338	    category: mutation-testing
339	    role: background
340	    relevance: >
341	      Empirically validates the coupling effect hypothesis that underpins
342	      mutation testing. STA's single-component ablation is analogous to
343	      first-order mutation; the coupling effect suggests this suffices.
344	    key_finding: >
345	      Test data killing all first-order mutants killed >99% of second-
346	      and third-order mutants, validating the coupling effect.
347	
348	  - id: jia-harman-survey
349	    title: "An Analysis and Survey of the Development of Mutation Testing"
350	    authors: "Yue Jia, Mark Harman"
351	    year: 2011
352	    venue: "IEEE TSE 37(5):649-678"
353	    category: mutation-testing
354	    role: background
355	    relevance: >
356	      Comprehensive survey of mutation testing covering three decades of
357	      development. Provides theoretical and practical foundation for STA's
358	      adaptation of mutation testing to logical formulas.
359	    key_finding: >
360	      Systematic classification of mutation operators, cost reduction
361	      techniques, and equivalence problem -- all relevant to STA's design
362	      of clause-level ablation operators.
363	
364	  - id: just-mutants-real-faults
365	    title: "Are Mutants a Valid Substitute for Real Faults in Software Testing?"
366	    authors: "Rene Just, Darioush Jalali, Laura Inozemtseva, et al."
367	    year: 2014
368	    venue: "FSE 2014"
369	    category: mutation-testing
370	    role: background
371	    relevance: >
372	      Validates that mutation testing (structural/intensional analysis of
373	      program adequacy) correlates with real fault detection. Supports STA's
374	      premise that structural analysis of formalization components provides
375	      meaningful signal about formalization quality.
376	    key_finding: >
377	      Mutant detection is statistically correlated with real fault detection,
378	      and mutation score is a better predictor of test effectiveness than
379	      code coverage.
380	
381	  - id: llmorpheus
382	    title: "LLMorpheus: Mutation Testing Using Large Language Models"
383	    authors: "Frank Tip, Jon Bell, et al."
384	    year: 2025
385	    venue: "IEEE TSE 2025"
386	    category: mutation-testing
387	    role: background
388	    relevance: >
389	      Uses LLMs to generate realistic code mutants beyond traditional
390	      mutation operators. Shows mutation testing evolving toward
391	      ML-integrated approaches, validating STA's cross-pollination
392	      of mutation testing ideas into ML training.
393	    key_finding: >
394	      LLM-generated mutants simulate real bugs that rule-based operators
395	      cannot produce, improving mutation testing realism.
396	
397	  - id: mutation-guided-meta
398	    title: "Mutation-Guided LLM-based Test Generation at Meta"
399	    authors: "Christopher Foster et al."
400	    year: 2025
401	    venue: "FSE 2025"
402	    category: mutation-testing
403	    role: background
404	    relevance: >
405	      Industrial application of mutation-guided LLM test generation at
406	      Meta. Demonstrates that mutation analysis can guide LLM behavior
407	      in production -- analogous to how STA uses mutation (ablation) to
408	      guide GRPO reward signal.
409	    key_finding: >
410	      Mutation-guided approach generates tests that kill significantly
411	      more mutants than unguided LLM test generation at Meta scale.
412	
413	  - id: mutation-consistency-llm
414	    title: "Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs"
415	    authors: "Various"
416	    year: 2024
417	    venue: "arXiv 2401.05940"
418	    category: mutation-testing
419	    role: background
420	    relevance: >
421	      Uses code mutations to evaluate LLM code understanding consistency.
422	      Conceptually related to STA: both use systematic code/formula
423	      mutations to assess model capabilities.
424	    key_finding: >
425	      LLMs show significant inconsistency when evaluated on mutated code
426	      variants, suggesting superficial pattern matching.
427	
428	  # ============================================================
429	  # Category 4: Intensional program analysis
430	  # ============================================================
431	
432	  - id: deepmutation
433	    title: "A Probabilistic Framework for Mutation Testing in Deep Neural Networks"
434	    authors: "Various"
435	    year: 2023
436	    venue: "Information and Software Technology 2023"
437	    category: intensional-analysis
438	    role: background
439	    relevance: >
440	      Extends mutation testing to DNN testing with probabilistic mutation
441	      operators. Parallel to STA's extension of mutation testing from
442	      traditional programs to logical formulas.
443	    key_finding: >
444	      Probabilistic mutation framework enables meaningful test adequacy
445	      assessment for neural networks through structural perturbation.
446	
447	  # ============================================================
448	  # Category 5: Reward hacking / overoptimization
449	  # ============================================================
450	
451	  - id: inform-reward-hacking
452	    title: "InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling"
453	    authors: "Various"
454	    year: 2024
455	    venue: "NeurIPS 2024"
456	    category: reward-hacking
457	    role: background
458	    relevance: >
459	      Proposes information-bottleneck approach to detect and mitigate reward
460	      hacking. STA's ISR addresses the same problem differently: by grounding
461	      reward in verifiable structural properties (component necessity), it
462	      reduces the attack surface for reward hacking.
463	    key_finding: >
464	      Variational information bottleneck filters irrelevant features from
465	      reward model; Cluster Separation Index detects reward overoptimization.
466	
467	  - id: mo-grpo
468	    title: "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems"
469	    authors: "CyberAgent AI Lab"
470	    year: 2025
471	    venue: "arXiv 2509.22047"
472	    category: reward-hacking
473	    role: background
474	    relevance: >
475	      Directly addresses GRPO reward hacking in multi-objective settings.
476	      STA's ISR can be viewed as adding a structural objective to the
477	      correctness objective, making MO-GRPO's insights directly applicable.
478	    key_finding: >
479	      Standard GRPO normalizes after summing rewards, allowing high-variance
480	      objectives to dominate. MO-GRPO equalizes scales before aggregation.
481	
482	  - id: reward-hacking-survey
483	    title: "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges"
484	    authors: "Various"
485	    year: 2026
486	    venue: "arXiv 2604.13602"
487	    category: reward-hacking
488	    role: background
489	    relevance: >
490	      Comprehensive survey of reward hacking mechanisms in the LLM era.
491	      Provides theoretical framework for understanding why STA's structural
492	      reward is more robust than pure outcome-based reward.
493	    key_finding: >
494	      Reward hacking manifests through specification gaming, reward model
495	      exploitation, and emergent misalignment; structural verification
496	      rewards are more robust than learned reward models.
497	
498	  - id: energy-loss-reward-hacking
499	    title: "The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking"
500	    authors: "Various"
501	    year: 2025
502	    venue: "ICML 2025"
503	    category: reward-hacking
504	    role: background
505	    relevance: >
506	      Identifies energy loss in LLM final layer as an indicator of reward
507	      hacking during RL. Provides complementary diagnostic to STA's
508	      structural reward approach.
509	    key_finding: >
510	      Energy loss in the final layer increases during RL and excessive
511	      increase characterizes reward hacking; EPPO algorithm penalizes
512	      this to mitigate hacking.
513	
514	  - id: spurious-rewards
515	    title: "Spurious Rewards: Rethinking Training Signals in RLVR"
516	    authors: "Ruixin Yang et al."
517	    year: 2025
518	    venue: "arXiv 2506.10947 / NeurIPS 2025 submission"
519	    category: reward-hacking
520	    role: direct-evidence
521	    relevance: >
522	      Most directly relevant to STA findings. GRPO+random reward on
523	      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's
524	      29.1%. Matches our plan017 finding: additive random (PR=48%) >
525	      additive ISR (PR=18%). Structured metrics can be worse than random
526	      noise due to systematic bias vs pure variance.
527	    key_finding: >
528	      Random reward nearly matches ground-truth reward in GRPO training,
529	      suggesting GRPO's group normalization extracts signal from noise.
530	      Effect is model-dependent (works on Qwen2.5, not Llama3).
531	
532	  - id: bondarenko-spec-gaming
533	    title: "Demonstrating Specification Gaming in Reasoning Models"
534	    authors: "Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish"
535	    year: 2025
536	    venue: "arXiv 2502.13295"
537	    category: reward-hacking
538	    role: direct-evidence
539	    relevance: >
540	      Shows that reasoning models (o3, DeepSeek-R1) resort to specification
541	      gaming on difficult tasks by default, without explicit nudging.
542	      Directly relevant to STA's concern: RL-trained reasoning models
543	      may game formal verification rewards rather than learn genuine
544	      formalization skills.
545	    key_finding: >
546	      Reasoning models spontaneously hack benchmarks (e.g., manipulating
547	      chess engine files instead of playing chess). Stronger reasoning
548	      capability correlates with more sophisticated gaming strategies.
549	
550	  - id: kim-game-formalization
551	    title: "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning"
552	    authors: "Kyuhee Kim, Auguste Poiroux, Antoine Bosselut"
553	    year: 2026
554	    venue: "VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)"
555	    category: reward-hacking
556	    role: direct-evidence
557	    relevance: >
558	      Directly studies whether LLMs game formalization in logical reasoning --
559	      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5
560	      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of
561	      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation
562	      (R1), the latter evading detection entirely.
563	    key_finding: >
564	      High compilation rates (87-99%) do not imply faithful formalization.
565	      Two-stage pipelines reveal unfaithfulness that unified generation hides.
566	      Premise mistranslation produces internally consistent but unfaithful
567	      outputs -- analogous to STA's high-ISR but semantically wrong traces.
568	
569	  - id: gao-reward-overoptimization
570	    title: "Scaling Laws for Reward Model Overoptimization"
571	    authors: "Leo Gao, John Schulman, Jacob Hilton"
572	    year: 2023
573	    venue: "ICML 2023 (arXiv 2210.10760)"
574	    category: reward-hacking
575	    role: theoretical-foundation
576	    relevance: >
577	      Foundational work quantifying Goodhart's effect: proxy reward rises
578	      but gold reward first rises then falls. ISR is a proxy reward that
579	      exhibits exactly this pattern — ISR can increase while prove_rate
580	      decreases, making it suitable for post-hoc diagnosis but harmful
581	      as training signal.
582	    key_finding: >
583	      Gold/proxy reward divergence follows predictable scaling laws.
584	      Proxy reward optimization past critical point degrades gold reward,
585	      with the divergence point scaling with model and dataset size.
586	
587	  - id: karwowski-goodhart-rl
588	    title: "Goodhart's Law in Reinforcement Learning"
589	    authors: "Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse"
590	    year: 2024
591	    venue: "ICLR 2024 (arXiv 2310.09144)"
592	    category: reward-hacking
593	    role: theoretical-foundation
594	    relevance: >
595	      Geometric interpretation of Goodhart's Law in MDPs: optimizing
596	      imperfect proxy past critical point decreases true objective. ISR as
597	      proxy has partial correlation with execution correctness — exceeding
598	      critical optimization point pushes policy toward high-ISR but
599	      low-correctness regions. Explains plan002/plan005 negative results.
600	    key_finding: >
601	      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy
602	      reward creates regions where proxy and true reward diverge, and
603	      policy optimization inevitably enters these regions.
604	
605	  # ============================================================
606	  # Category 6: FOL/Prolog formalization with LLMs
607	  # ============================================================
608	
609	  - id: folio
610	    title: "FOLIO: Natural Language Reasoning with First-Order Logic"
611	    authors: "Simeng Han et al."
612	    year: 2022
613	    venue: "arXiv 2209.00840 / EMNLP 2024"
614	    category: fol-formalization
615	    role: evaluation
616	    relevance: >
617	      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL
618	      formalization as the target task for GRPO training. FOLIO's
619	      expert-annotated FOL annotations serve as reference formalizations.
620	    key_finding: >
621	      1,430 NL-FOL paired examples with reasoning depths up to 5+;
622	      GPT-4 still struggles on the hardest examples.
623	
624	  - id: proofwriter
625	    title: "ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language"
626	    authors: "Oyvind Tafjord, Bhavana Dalvi, Peter Clark"
627	    year: 2021
628	    venue: "Findings of ACL-IJCNLP 2021"
629	    category: fol-formalization
630	    role: evaluation
631	    relevance: >
632	      Source dataset for STA's training data. ProofWriter provides
633	      rule-based logical reasoning problems in natural language that
634	      STA uses for training formalizer models.
635	    key_finding: >
636	      Generative model can reliably produce implications and proofs;
637	      accuracy exceeds prior methods by 9% and generalizes to unseen
638	      proof depths.
639	
640	  - id: logic-lm
641	    title: "Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning"
642	    authors: "Liangming Pan, Alon Albalak, Xinyi Wang, William Wang"
643	    year: 2023
644	    venue: "Findings of EMNLP 2023"
645	    category: fol-formalization
646	    role: direct-competitor
647	    relevance: >
648	      LLM->symbolic solver pipeline for logical reasoning, directly
649	      comparable to STA's formalizer->Prolog solver pipeline. Key
650	      difference: Logic-LM uses prompting, STA uses GRPO training.
651	    key_finding: >
652	      LLM+solver achieves 39.2% improvement over LLM-alone on logical
653	      reasoning benchmarks including ProofWriter and FOLIO.
654	
655	  - id: linc
656	    title: "LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers"
657	    authors: "Theo X. Olausson, Alex Gu, Ben Lipkin, et al."
658	    year: 2023
659	    venue: "EMNLP 2023"
660	    category: fol-formalization
661	    role: direct-competitor
662	    relevance: >
663	      Neurosymbolic approach where LLM translates NL to FOL for theorem
664	      prover. Directly comparable to STA's NL->Prolog translation.
665	      LINC uses prompting-based approach; STA uses RL training.
666	    key_finding: >
667	      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with
668	      CoT by 38% and 10% respectively on ProofWriter.
669	
670	  - id: fover-pei2025
671	    title: "FoVer: First-Order Logic Verification for Natural Language Reasoning"
672	    authors: "Yu Pei, Yongping Du, Xingnan Jin"
673	    year: 2025
674	    venue: "TACL 13:1340-1359"
675	    category: fol-formalization
676	    role: direct-competitor
677	    relevance: >
678	      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.
679	      Similar to STA's verification pipeline but focuses on post-hoc
680	      verification rather than training reward signal.
681	    key_finding: >
682	      FOL verification via Z3 significantly outperforms existing methods
683	      on ProofWriter and FOLIO benchmarks.
684	
685	  - id: lorp
686	    title: "LoRP: LLM-based Logical Reasoning via Prolog"
687	    authors: "Various"
688	    year: 2025
689	    venue: "Knowledge-Based Systems 2025"
690	    category: fol-formalization
691	    role: direct-competitor
692	    relevance: >
693	      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.
694	      Closest to STA's formalization target (Prolog), though LoRP
695	      uses prompting while STA uses GRPO training with structural reward.
696	    key_finding: >
697	      Systematic FOL-to-Prolog translation extends Prolog expressiveness;
698	      achieves SoTA accuracy on logical reasoning with three-vote majority.
699	
700	  - id: nl2fol
701	    title: "NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection"
702	    authors: "Lalwani, Kim, et al."
703	    year: 2024
704	    venue: "arXiv 2405.02318"
705	    category: fol-formalization
706	    role: background
707	    relevance: >
708	      Step-by-step NL->FOL translation using LLMs with SMT solver
709	      verification. Demonstrates the NL->formal logic pipeline that
710	      STA aims to improve via RL training.
711	    key_finding: >
712	      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and
713	      generalizes to LogicClimate (80% F1), outperforming supervised
714	      models by 21%.
715	
716	  - id: logica2
717	    title: "LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding"
718	    authors: "Liu et al."
719	    year: 2023
720	    venue: "IEEE/ACM TASLP 2023"
721	    category: fol-formalization
722	    role: evaluation
723	    relevance: >
724	      Logical reasoning evaluation benchmark derived from Chinese civil
725	      service exams. Provides supplementary evaluation for STA's
726	      formalization capabilities.
727	    key_finding: >
728	      8,678 multiple-choice questions covering categorical, disjunctive,
729	      and conditional reasoning; widely used LLM benchmark.
730	
731	  # ============================================================
732	  # Category 7: Goodhart's Law theory and dose-response dynamics
733	  # ============================================================
734	
735	  - id: manheim-goodhart-taxonomy
736	    title: "Categorizing Variants of Goodhart's Law"
737	    authors: "David Manheim, Scott Garrabrant"
738	    year: 2019
739	    venue: "arXiv 1803.04585"
740	    category: goodhart-overoptimization
741	    role: theoretical-foundation
742	    relevance: >
743	      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.
744	      STA's high-β ISR collapse is best classified as extremal Goodhart
745	      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides
746	      vocabulary for discussion section.
747	    key_finding: >
748	      First systematic categorization of Goodhart failure modes. Extremal
749	      variant occurs when proxy-goal relationship breaks in out-of-distribution
750	      regions reached by strong optimization.
751	
752	  - id: pan-reward-misspecification
753	    title: "The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models"
754	    authors: "Alexander Pan, Kush Bhatia, Jacob Steinhardt"
755	    year: 2022
756	    venue: "ICLR 2022"
757	    category: goodhart-overoptimization
758	    role: theoretical-foundation
759	    relevance: >
760	      Across 9 environments, more capable agents exploit misspecifications more.
761	      Observes dose-dependent degradation — capability thresholds where true
762	      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.
763	    key_finding: >
764	      Reward misspecification causes dose-dependent degradation where true reward
765	      sharply drops past capability thresholds. More capable optimization
766	      produces worse outcomes under misspecification.
767	
768	  - id: kwa-catastrophic-goodhart
769	    title: "Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification"
770	    authors: "Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso"
771	    year: 2024
772	    venue: "NeurIPS 2024"
773	    category: goodhart-overoptimization
774	    role: theoretical-foundation
775	    relevance: >
776	      If reward model error is heavy-tailed, policies achieve arbitrarily
777	      high proxy reward with no true utility gain. KL regularization provably
778	      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse
779	      at high β if ISR error distribution is heavy-tailed.
780	    key_finding: >
781	      KL-regularized RL provably fails to prevent overoptimization under
782	      heavy-tailed reward misspecification. Policies can achieve arbitrarily
783	      high proxy reward with zero true utility.
784	
785	  - id: rafailov-daa-scaling
786	    title: "Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms"
787	    authors: "Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum"
788	    year: 2024
789	    venue: "NeurIPS 2024"
790	    category: goodhart-overoptimization
791	    role: supporting-evidence
792	    relevance: >
793	      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across
794	      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.
795	      Validates β as a "dose" parameter — directly analogous to STA's
796	      ISR weight sweep.
797	    key_finding: >
798	      Direct alignment algorithms exhibit overoptimization following
799	      predictable scaling laws. Smaller models overoptimize sooner.
800	      β-controlled dose-response is a general phenomenon across RL paradigms.
801	
802	  - id: huang-chi-squared
803	    title: "Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction"
804	    authors: "Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao"
805	    year: 2025
806	    venue: "ICLR 2025 Poster"
807	    category: goodhart-overoptimization
808	    role: supporting-evidence
809	    relevance: >
810	      KL-regularization is theoretically inadequate for preventing
811	      overoptimization. Chi-squared divergence provably alleviates it.
812	      Suggests that even with KL penalty in GRPO, STA's high-β collapse
813	      is theoretically expected.
814	    key_finding: >
815	      Chi-squared preference optimization provably mitigates overoptimization
816	      where KL-regularization fails. Alternative divergence measures offer
817	      stronger guarantees.
818	
819	  - id: coste-rm-ensembles
820	    title: "Reward Model Ensembles Help Mitigate Overoptimization"
821	    authors: "Thomas Coste, Usman Anwar, Robert Kirk, David Krueger"
822	    year: 2023
823	    venue: "NeurIPS 2023 Workshop on Alignment"
824	    category: goodhart-overoptimization
825	    role: background
826	    relevance: >
827	      Worst-case optimization across RM ensembles practically eliminates
828	      overoptimization for BoN and reduces it for PPO. Suggests ensemble
829	      of multiple solver metrics (instead of single ISR) as mitigation.
830	    key_finding: >
831	      RM ensembles with worst-case aggregation mitigate overoptimization.
832	      Ensemble size and diversity directly affect robustness.
833	
834	  # ============================================================
835	  # Category 8: Solver/prover as RL reward signal
836	  # ============================================================
837	
838	  - id: rlsf
839	    title: "Reinforcement Learning via Symbolic Feedback"
840	    authors: "Abhinav Jha, Shikhar Murty, Zico Kolter, et al."
841	    year: 2024
842	    venue: "arXiv 2405.16661"
843	    category: verification-reward
844	    role: direct-competitor
845	    relevance: >
846	      Most directly relevant: uses solver/prover certificates as fine-grained
847	      token-level reward signal. Outperforms traditional approaches on program
848	      synthesis (+31.4%). STA extends this paradigm and shows when it breaks
849	      (Goodhart effects at high auxiliary reward weight).
850	    key_finding: >
851	      Symbolic reasoning tools provide poly-sized certificates as reward.
852	      Smaller RLSF models outperform GPT-4 on structured generation tasks.
853	
854	  - id: fover-kamoi2026
855	    title: "FoVer: Generalizable Process Reward Models via Formally Verified Training Data"
856	    authors: "Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang"
857	    year: 2025
858	    venue: "Findings of ACL 2026 (arXiv 2502.01345)"
859	    category: verification-reward
860	    role: supporting-evidence
861	    relevance: >
862	      Uses Z3 and Isabelle to synthesize PRM training data by annotating
863	      step-level error labels without human annotation. Same solver family
864	      as STA. Shows verification-based rewards work; STA extends by showing
865	      dose-response dynamics.
866	    key_finding: >
867	      Formally verified training data enables generalizable process reward
868	      models competitive on ProcessBench and 12 reasoning benchmarks.
869	
870	  - id: deepseek-prover-v15
871	    title: "DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search"
872	    authors: "DeepSeek AI"
873	    year: 2024
874	    venue: "ICLR 2025 (arXiv 2408.08152)"
875	    category: verification-reward
876	    role: method-component
877	    relevance: >
878	      Uses GRPO with Lean 4 verification as binary reward. Same algorithm
879	      (GRPO) + formal verification, but binary (pass/fail). Binary reward
880	      avoids the graded-metric Goodhart risk that STA identifies with ISR.
881	    key_finding: >
882	      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary
883	      correctness guarantee via formal verification sidesteps proxy reward
884	      overoptimization.
885	
886	  - id: alphaproof
887	    title: "AlphaProof"
888	    authors: "Google DeepMind"
889	    year: 2024
890	    venue: "Nature 2025"
891	    category: verification-reward
892	    role: background
893	    relevance: >
894	      AlphaZero-inspired RL with Lean proof verification at scale.
895	      Silver medal at IMO 2024. Binary verification reward avoids the
896	      Goodhart problem STA identifies with graded verification metrics.
897	    key_finding: >
898	      Binary formal verification as RL reward scales to IMO-level
899	      mathematical reasoning. Demonstrates verification-reward RL works
900	      at the frontier of mathematical difficulty.
901	
902	  - id: math-shepherd
903	    title: "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations"
904	    authors: "Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al."
905	    year: 2024
906	    venue: "ACL 2024 (arXiv 2312.08935)"
907	    category: verification-reward
908	    role: supporting-evidence
909	    relevance: >
910	      Automatically constructs process supervision data and uses it as
911	      step-by-step PPO reward. Automated verification reward without human
912	      labels, analogous to STA's automated ISR computation via solver.
913	    key_finding: >
914	      Automated process supervision improves Mistral-7B on GSM8K
915	      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.
916	
917	  # ============================================================
918	  # Additional reward-shaping papers (Goodhart survey additions)
919	  # ============================================================
920	
921	  - id: bipars
922	    title: "Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping"
923	    authors: "Yujing Hu, Weixun Wang, Hangtian Jia, et al."
924	    year: 2020
925	    venue: "NeurIPS 2020"
926	    category: reward-shaping
927	    role: background
928	    relevance: >
929	      Bi-level optimization learns parameterized shaping reward weights.
930	      Can transform harmful shaping rewards into beneficial ones by learning
931	      negative weights. Directly addresses STA's problem: when ISR weight
932	      is wrong, automated weight learning could find optimal β.
933	    key_finding: >
934	      Bi-level optimization automatically learns auxiliary reward weights,
935	      outperforming fixed weights and recovering from harmful shaping rewards.
936	
937	  - id: dapo
938	    title: "DAPO: An Open-Source LLM Reinforcement Learning System at Scale"
939	    authors: "Qiying Yu et al. (ByteDance)"
940	    year: 2025
941	    venue: "arXiv 2503.14476"
942	    category: reward-shaping
943	    role: background
944	    relevance: >
945	      Four techniques for stable multi-component reward in GRPO: Clip-Higher,
946	      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.
947	      Addresses stability issues relevant to STA's multi-reward setup.
948	    key_finding: >
949	      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO
950	      with multi-component rewards. Soft punishment for overlong outputs
951	      avoids reward hacking through length exploitation.
952	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "7ed822cc-836e-48e8-a272-0e43bbecd991",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
      "content": "# Literature Map for Solver Trace Ablation (STA)\n# Categories:\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\n#   2. reward-shaping: Reward shaping for code/formal verification\n#   3. mutation-testing: Mutation testing in software engineering\n#   4. intensional-analysis: Intensional program analysis\n#   5. reward-hacking: Reward hacking / overoptimization\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\n#   8. verification-reward: Solver/prover as RL reward signal\n\npapers:\n\n  # ============================================================\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\n  # ============================================================\n\n  - id: deepseek-r1\n    title: \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n    authors: \"DeepSeek-AI\"\n    year: 2025\n    venue: \"arXiv 2501.12948 / Nature 2025\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\n      STA builds on the same GRPO framework but replaces binary outcome reward with\n      intensional structural reward for neurosymbolic formalization.\n    key_finding: >\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\n      showing emergent chain-of-thought reasoning from RL alone.\n\n  - id: deepseekmath\n    title: \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n    authors: \"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\"\n    year: 2024\n    venue: \"arXiv 2402.03300\"\n    category: neurosymbolic-rl\n    role: method-component\n    relevance: >\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\n      used in STA training. GRPO eliminates the critic model by estimating\n      baselines from group scores.\n    key_finding: >\n      GRPO matches PPO performance while significantly reducing training\n      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.\n\n  - id: logic-rl\n    title: \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\"\n    authors: \"Xian et al.\"\n    year: 2025\n    venue: \"arXiv 2502.14768\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses rule-based RL (REINFORCE++) for LLM logical reasoning on synthetic\n      logic puzzles. Closest competitor to STA's approach of RL for logical\n      formalization, though Logic-RL uses extensional (answer-correctness)\n      rewards rather than STA's intensional structural rewards.\n    key_finding: >\n      REINFORCE++ outperforms GRPO on logic puzzles with superior stability;\n      rule-based reward design is critical for RL-based logical reasoning.\n\n  - id: mellgren-prolog-grpo\n    title: \"Training Language Models to Use Prolog as a Tool\"\n    authors: \"Niklas Mellgren\"\n    year: 2024\n    venue: \"arXiv 2512.07407\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses GRPO to train a 3B LLM to generate Prolog code for reasoning,\n      directly comparable to STA's approach of GRPO-training a formalizer.\n      Key difference: uses pass/fail reward vs STA's structural ISR.\n    key_finding: >\n      GRPO is effective for teaching small LLMs to use Prolog as a tool\n      for logical and mathematical reasoning.\n\n  - id: satlm\n    title: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\n    authors: \"Xi Ye et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Neurosymbolic approach where LLM generates declarative specifications\n      verified by SAT solver. Similar pipeline to STA (LLM->formal spec->solver)\n      but uses prompting, not RL training.\n    key_finding: >\n      Declarative formulation outperforms imperative program-aided LMs by 23%\n      on GSM; achieves SoTA on LSAT and BoardgameQA.\n\n  - id: deepproblog\n    title: \"Neural Probabilistic Logic Programming in DeepProbLog\"\n    authors: \"Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt\"\n    year: 2021\n    venue: \"Artificial Intelligence 298\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Foundational neural-probabilistic logic programming framework that integrates\n      deep learning with ProbLog via neural predicates. Establishes the intellectual\n      tradition of combining neural networks with logic programming that STA extends\n      to LLM-generated Prolog with RL training.\n    key_finding: >\n      End-to-end differentiable framework integrating neural perception with\n      probabilistic logical reasoning; supports program induction and learning\n      from examples.\n\n  - id: neurasp\n    title: \"NeurASP: Embracing Neural Networks into Answer Set Programming\"\n    authors: \"Zhun Yang, Adam Ishay, Joohyung Lee\"\n    year: 2020\n    venue: \"IJCAI 2020\"\n    category: neurosymbolic-rl\n    role: background\n    relevance: >\n      Integrates neural networks with answer set programming (ASP), using\n      ASP rules to constrain and improve neural network training. Complementary\n      to DeepProbLog; together they represent the neuro-symbolic LP foundation\n      that STA's LLM-to-Prolog pipeline builds upon.\n    key_finding: >\n      ASP semantic constraints improve neural network perception accuracy;\n      demonstrates bidirectional benefit of neural-symbolic integration.\n\n  - id: thought-like-pro\n    title: \"Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought\"\n    authors: \"Xiaoyu Tan, Yongxin Deng, Xihe Qiu, Weidi Xu, Chao Qu, Wei Chu, Yinghui Xu, Yuan Qi\"\n    year: 2024\n    venue: \"arXiv 2407.14562\"\n    category: neurosymbolic-rl\n    role: direct-competitor\n    relevance: >\n      Uses Prolog engine to generate verified reasoning trajectories, then trains\n      LLMs via imitation learning to replicate them. Directly comparable pipeline\n      to STA (Prolog verification + LLM training), but uses imitation learning\n      instead of GRPO with structural reward.\n    key_finding: >\n      Prolog-verified reasoning trajectories as training signal improve LLM\n      logical reasoning; self-driven framework enables LLMs to formulate\n      rules from instructions and leverage Prolog for derivation.\n\n  # ============================================================\n  # Category 2: Reward shaping for code/formal verification\n  # ============================================================\n\n  - id: lightman-verify-step\n    title: \"Let's Verify Step by Step\"\n    authors: \"Hunter Lightman, Vineet Kosaraju, Yura Burda, et al.\"\n    year: 2023\n    venue: \"arXiv 2305.20050 / ICLR 2024\"\n    category: reward-shaping\n    role: method-component\n    relevance: >\n      Establishes that process supervision (step-level reward) outperforms\n      outcome supervision (final-answer reward) for reasoning. STA's ISR\n      is analogous: it provides structural process-level signal about which\n      components of a formalization matter, rather than just pass/fail.\n    key_finding: >\n      Process-supervised reward model achieves 78% on MATH, significantly\n      outperforming outcome-supervised models. Released PRM800K dataset.\n\n  - id: reward-shaping-rlhf\n    title: \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n    authors: \"Jiayi Fu, Xuandong Zhao, Chengyuan Yao, et al.\"\n    year: 2025\n    venue: \"arXiv 2502.18770\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Studies reward shaping design principles for RLHF: bounded rewards and\n      rapid-then-convergent growth. STA's ISR follows these principles\n      naturally since structural necessity scores are bounded [0,1].\n    key_finding: >\n      Two key reward shaping principles: (1) bounded RL reward, (2) rapid\n      initial growth with gradual convergence. PAR method achieves 5%+\n      win rate improvement on AlpacaEval 2.0.\n\n  - id: rlvr-reasoning\n    title: \"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2506.14245\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize\n      reasoning. STA argues that for neurosymbolic formalization, binary reward\n      is insufficient and structural reward is needed to avoid reward hacking.\n    key_finding: >\n      RLVR with binary verification implicitly teaches correct reasoning\n      strategies, not just answer matching.\n\n  - id: rubric-grpo\n    title: \"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"arXiv 2605.08061\"\n    category: reward-shaping\n    role: direct-competitor\n    relevance: >\n      Uses structured rubric-based rewards with GRPO, similar in spirit to\n      STA's structured ISR. Key difference: rubric rewards come from LLM\n      judges, while ISR comes from solver-based mutation testing.\n    key_finding: >\n      Structured multi-dimensional reward signals improve GRPO training\n      generalization compared to scalar rewards.\n\n  - id: gao-effective-rl-reward\n    title: \"On Designing Effective RL Reward at Training Time for LLM Reasoning\"\n    authors: \"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\"\n    year: 2024\n    venue: \"arXiv 2410.15115\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Demonstrates that learned process/outcome reward models can hurt RL\n      training, producing worse performance than simple success reward only.\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\n      reward degrades prove_rate compared to exec-only baseline.\n    key_finding: >\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\n      reward. Solution: Clipping and Delta techniques to bound accumulated\n      reward magnitude prevent reward hacking.\n\n  - id: prof-process-outcome\n    title: \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"\n    authors: \"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\"\n    year: 2025\n    venue: \"arXiv 2509.03403\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that naively combining PRM+ORM signals leads to performance\n      degradation. PROF consistency filter retains only PRM-ORM consistent\n      samples, achieving 4%+ improvement over blending. Suggests STA should\n      only apply ISR when consistent with execution outcome.\n    key_finding: >\n      Process rewards frequently suffer from inaccuracies and reward hacking\n      susceptibility. PROF filters training data by PRM-ORM consistency,\n      outperforming naive reward blending by 4%+ accuracy.\n\n  - id: moskovitz-constrained-rlhf\n    title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: \"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\"\n    year: 2023\n    venue: \"arXiv 2310.04373 / ICLR 2024\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      First study on overoptimization in composite reward models. Shows that\n      fixed-weight linear scalarization of component rewards leads to\n      degradation past a threshold. Proposes constrained RL with dynamic\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\n    key_finding: >\n      Correlation between component RMs significantly affects overoptimization\n      thresholds. Constrained RL with Lagrange multipliers outperforms\n      fixed-weight reward composition.\n\n  - id: skalse-reward-hacking\n    title: \"Defining and Characterizing Reward Hacking\"\n    authors: \"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\"\n    year: 2022\n    venue: \"arXiv 2209.13085 / NeurIPS 2022\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Formal proof that for stochastic policies, two reward functions are\n      unhackable only if one is constant. Theoretically explains why any\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\n      property of reward composition, not STA-specific.\n    key_finding: >\n      Any non-constant proxy reward can decrease true reward when optimized.\n      Unhackability requires the proxy to be constant, making all non-trivial\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\n\n  - id: progrs-outcome-conditioned\n    title: \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"\n    authors: \"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\"\n    year: 2026\n    venue: \"arXiv 2604.02341\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\n      to zero mean, preserving ranking info without corrupting gradients.\n      Suggests STA should condition ISR on execution outcome.\n    key_finding: >\n      Naive process rewards induce reward hacking by rewarding locally fluent\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\n      the conflict with fewer rollouts than outcome-only baselines.\n\n  - id: qwen-prm-lessons\n    title: \"The Lessons of Developing Process Reward Models in Mathematical Reasoning\"\n    authors: \"Zhenru Zhang et al. (Qwen Team, Alibaba)\"\n    year: 2025\n    venue: \"ACL 2025 Findings (arXiv 2501.07301)\"\n    category: reward-shaping\n    role: supporting-evidence\n    relevance: >\n      MC estimation-synthesized PRM data leads to quality degradation; policy\n      model generates \"answer-correct but reasoning-flawed\" responses, causing\n      process reward / outcome misalignment. Directly parallels ISR problem:\n      structurally correct but semantically wrong proof traces get high ISR\n      but low execution reward.\n    key_finding: >\n      PRM performance depends critically on data quality; MC estimation\n      introduces systematic bias. Answer-correct reasoning-flawed samples\n      corrupt process supervision signal.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering\n  # ============================================================\n\n  - id: demillo1978\n    title: \"Hints on Test Data Selection: Help for the Practicing Programmer\"\n    authors: \"Richard A. DeMillo, Richard J. Lipton, Frederick G. Sayward\"\n    year: 1978\n    venue: \"Computer 11(4):34-43\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Foundational paper introducing mutation testing. STA's component\n      necessity testing directly extends this idea: instead of mutating\n      source code to test test suites, STA mutates logical formulas\n      to test component necessity for solver success.\n    key_finding: >\n      Introduced mutation testing and the coupling effect hypothesis:\n      tests that detect simple faults also detect complex faults.\n\n  - id: offutt-coupling\n    title: \"Investigations of the Software Testing Coupling Effect\"\n    authors: \"A. Jefferson Offutt\"\n    year: 1992\n    venue: \"ACM TOSEM 1(1):5-20\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Empirically validates the coupling effect hypothesis that underpins\n      mutation testing. STA's single-component ablation is analogous to\n      first-order mutation; the coupling effect suggests this suffices.\n    key_finding: >\n      Test data killing all first-order mutants killed >99% of second-\n      and third-order mutants, validating the coupling effect.\n\n  - id: jia-harman-survey\n    title: \"An Analysis and Survey of the Development of Mutation Testing\"\n    authors: \"Yue Jia, Mark Harman\"\n    year: 2011\n    venue: \"IEEE TSE 37(5):649-678\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Comprehensive survey of mutation testing covering three decades of\n      development. Provides theoretical and practical foundation for STA's\n      adaptation of mutation testing to logical formulas.\n    key_finding: >\n      Systematic classification of mutation operators, cost reduction\n      techniques, and equivalence problem -- all relevant to STA's design\n      of clause-level ablation operators.\n\n  - id: just-mutants-real-faults\n    title: \"Are Mutants a Valid Substitute for Real Faults in Software Testing?\"\n    authors: \"Rene Just, Darioush Jalali, Laura Inozemtseva, et al.\"\n    year: 2014\n    venue: \"FSE 2014\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Validates that mutation testing (structural/intensional analysis of\n      program adequacy) correlates with real fault detection. Supports STA's\n      premise that structural analysis of formalization components provides\n      meaningful signal about formalization quality.\n    key_finding: >\n      Mutant detection is statistically correlated with real fault detection,\n      and mutation score is a better predictor of test effectiveness than\n      code coverage.\n\n  - id: llmorpheus\n    title: \"LLMorpheus: Mutation Testing Using Large Language Models\"\n    authors: \"Frank Tip, Jon Bell, et al.\"\n    year: 2025\n    venue: \"IEEE TSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses LLMs to generate realistic code mutants beyond traditional\n      mutation operators. Shows mutation testing evolving toward\n      ML-integrated approaches, validating STA's cross-pollination\n      of mutation testing ideas into ML training.\n    key_finding: >\n      LLM-generated mutants simulate real bugs that rule-based operators\n      cannot produce, improving mutation testing realism.\n\n  - id: mutation-guided-meta\n    title: \"Mutation-Guided LLM-based Test Generation at Meta\"\n    authors: \"Christopher Foster et al.\"\n    year: 2025\n    venue: \"FSE 2025\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Industrial application of mutation-guided LLM test generation at\n      Meta. Demonstrates that mutation analysis can guide LLM behavior\n      in production -- analogous to how STA uses mutation (ablation) to\n      guide GRPO reward signal.\n    key_finding: >\n      Mutation-guided approach generates tests that kill significantly\n      more mutants than unguided LLM test generation at Meta scale.\n\n  - id: mutation-consistency-llm\n    title: \"Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"arXiv 2401.05940\"\n    category: mutation-testing\n    role: background\n    relevance: >\n      Uses code mutations to evaluate LLM code understanding consistency.\n      Conceptually related to STA: both use systematic code/formula\n      mutations to assess model capabilities.\n    key_finding: >\n      LLMs show significant inconsistency when evaluated on mutated code\n      variants, suggesting superficial pattern matching.\n\n  # ============================================================\n  # Category 4: Intensional program analysis\n  # ============================================================\n\n  - id: deepmutation\n    title: \"A Probabilistic Framework for Mutation Testing in Deep Neural Networks\"\n    authors: \"Various\"\n    year: 2023\n    venue: \"Information and Software Technology 2023\"\n    category: intensional-analysis\n    role: background\n    relevance: >\n      Extends mutation testing to DNN testing with probabilistic mutation\n      operators. Parallel to STA's extension of mutation testing from\n      traditional programs to logical formulas.\n    key_finding: >\n      Probabilistic mutation framework enables meaningful test adequacy\n      assessment for neural networks through structural perturbation.\n\n  # ============================================================\n  # Category 5: Reward hacking / overoptimization\n  # ============================================================\n\n  - id: inform-reward-hacking\n    title: \"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling\"\n    authors: \"Various\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Proposes information-bottleneck approach to detect and mitigate reward\n      hacking. STA's ISR addresses the same problem differently: by grounding\n      reward in verifiable structural properties (component necessity), it\n      reduces the attack surface for reward hacking.\n    key_finding: >\n      Variational information bottleneck filters irrelevant features from\n      reward model; Cluster Separation Index detects reward overoptimization.\n\n  - id: mo-grpo\n    title: \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n    authors: \"CyberAgent AI Lab\"\n    year: 2025\n    venue: \"arXiv 2509.22047\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Directly addresses GRPO reward hacking in multi-objective settings.\n      STA's ISR can be viewed as adding a structural objective to the\n      correctness objective, making MO-GRPO's insights directly applicable.\n    key_finding: >\n      Standard GRPO normalizes after summing rewards, allowing high-variance\n      objectives to dominate. MO-GRPO equalizes scales before aggregation.\n\n  - id: reward-hacking-survey\n    title: \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n    authors: \"Various\"\n    year: 2026\n    venue: \"arXiv 2604.13602\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Comprehensive survey of reward hacking mechanisms in the LLM era.\n      Provides theoretical framework for understanding why STA's structural\n      reward is more robust than pure outcome-based reward.\n    key_finding: >\n      Reward hacking manifests through specification gaming, reward model\n      exploitation, and emergent misalignment; structural verification\n      rewards are more robust than learned reward models.\n\n  - id: energy-loss-reward-hacking\n    title: \"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: reward-hacking\n    role: background\n    relevance: >\n      Identifies energy loss in LLM final layer as an indicator of reward\n      hacking during RL. Provides complementary diagnostic to STA's\n      structural reward approach.\n    key_finding: >\n      Energy loss in the final layer increases during RL and excessive\n      increase characterizes reward hacking; EPPO algorithm penalizes\n      this to mitigate hacking.\n\n  - id: spurious-rewards\n    title: \"Spurious Rewards: Rethinking Training Signals in RLVR\"\n    authors: \"Ruixin Yang et al.\"\n    year: 2025\n    venue: \"arXiv 2506.10947 / NeurIPS 2025 submission\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Most directly relevant to STA findings. GRPO+random reward on\n      Qwen2.5-Math improves 21.4%, nearly matching ground-truth reward's\n      29.1%. Matches our plan017 finding: additive random (PR=48%) >\n      additive ISR (PR=18%). Structured metrics can be worse than random\n      noise due to systematic bias vs pure variance.\n    key_finding: >\n      Random reward nearly matches ground-truth reward in GRPO training,\n      suggesting GRPO's group normalization extracts signal from noise.\n      Effect is model-dependent (works on Qwen2.5, not Llama3).\n\n  - id: bondarenko-spec-gaming\n    title: \"Demonstrating Specification Gaming in Reasoning Models\"\n    authors: \"Alexander Bondarenko, Denis Volk, Dmitrii Volkov, Jeffrey Ladish\"\n    year: 2025\n    venue: \"arXiv 2502.13295\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Shows that reasoning models (o3, DeepSeek-R1) resort to specification\n      gaming on difficult tasks by default, without explicit nudging.\n      Directly relevant to STA's concern: RL-trained reasoning models\n      may game formal verification rewards rather than learn genuine\n      formalization skills.\n    key_finding: >\n      Reasoning models spontaneously hack benchmarks (e.g., manipulating\n      chess engine files instead of playing chess). Stronger reasoning\n      capability correlates with more sophisticated gaming strategies.\n\n  - id: kim-game-formalization\n    title: \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"\n    authors: \"Kyuhee Kim, Auguste Poiroux, Antoine Bosselut\"\n    year: 2026\n    venue: \"VerifAI-2 Workshop, ICLR 2026 (arXiv 2604.19459)\"\n    category: reward-hacking\n    role: direct-evidence\n    relevance: >\n      Directly studies whether LLMs game formalization in logical reasoning --\n      the exact phenomenon STA's ISR is designed to detect. Evaluates GPT-5\n      and DeepSeek-R1 on FOLIO with Lean 4 proofs. Finds two modes of\n      unfaithfulness: axiom fabrication (GPT-5) and premise mistranslation\n      (R1), the latter evading detection entirely.\n    key_finding: >\n      High compilation rates (87-99%) do not imply faithful formalization.\n      Two-stage pipelines reveal unfaithfulness that unified generation hides.\n      Premise mistranslation produces internally consistent but unfaithful\n      outputs -- analogous to STA's high-ISR but semantically wrong traces.\n\n  - id: gao-reward-overoptimization\n    title: \"Scaling Laws for Reward Model Overoptimization\"\n    authors: \"Leo Gao, John Schulman, Jacob Hilton\"\n    year: 2023\n    venue: \"ICML 2023 (arXiv 2210.10760)\"\n    category: reward-hacking\n    role: theoretical-foundation\n    relevance: >\n      Foundational work quantifying Goodhart's effect: proxy reward rises\n      but gold reward first rises then falls. ISR is a proxy reward that\n      exhibits exactly this pattern — ISR can increase while prove_rate\n      decreases, making it suitable for post-hoc diagnosis but harmful\n      as training signal.\n    key_finding: >\n      Gold/proxy reward divergence follows predictable scaling laws.\n      Proxy reward optimization past critical point degrades gold reward,\n      with the divergence point scaling with model and dataset size.\n\n  - id: karwowski-goodhart-rl\n    title: \"Goodhart's Law in Reinforcement Learning\"\n    authors: \"Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse\"\n    year: 2024\n    venue: \"ICLR 2024 (arXiv 2310.09144)\"\n    category: reward-hacking\n    role: theoretical-foundation\n    relevance: >\n      Geometric interpretation of Goodhart's Law in MDPs: optimizing\n      imperfect proxy past critical point decreases true objective. ISR as\n      proxy has partial correlation with execution correctness — exceeding\n      critical optimization point pushes policy toward high-ISR but\n      low-correctness regions. Explains plan002/plan005 negative results.\n    key_finding: >\n      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy\n      reward creates regions where proxy and true reward diverge, and\n      policy optimization inevitably enters these regions.\n\n  # ============================================================\n  # Category 6: FOL/Prolog formalization with LLMs\n  # ============================================================\n\n  - id: folio\n    title: \"FOLIO: Natural Language Reasoning with First-Order Logic\"\n    authors: \"Simeng Han et al.\"\n    year: 2022\n    venue: \"arXiv 2209.00840 / EMNLP 2024\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL\n      formalization as the target task for GRPO training. FOLIO's\n      expert-annotated FOL annotations serve as reference formalizations.\n    key_finding: >\n      1,430 NL-FOL paired examples with reasoning depths up to 5+;\n      GPT-4 still struggles on the hardest examples.\n\n  - id: proofwriter\n    title: \"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\"\n    authors: \"Oyvind Tafjord, Bhavana Dalvi, Peter Clark\"\n    year: 2021\n    venue: \"Findings of ACL-IJCNLP 2021\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Source dataset for STA's training data. ProofWriter provides\n      rule-based logical reasoning problems in natural language that\n      STA uses for training formalizer models.\n    key_finding: >\n      Generative model can reliably produce implications and proofs;\n      accuracy exceeds prior methods by 9% and generalizes to unseen\n      proof depths.\n\n  - id: logic-lm\n    title: \"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\"\n    authors: \"Liangming Pan, Alon Albalak, Xinyi Wang, William Wang\"\n    year: 2023\n    venue: \"Findings of EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->symbolic solver pipeline for logical reasoning, directly\n      comparable to STA's formalizer->Prolog solver pipeline. Key\n      difference: Logic-LM uses prompting, STA uses GRPO training.\n    key_finding: >\n      LLM+solver achieves 39.2% improvement over LLM-alone on logical\n      reasoning benchmarks including ProofWriter and FOLIO.\n\n  - id: linc\n    title: \"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\"\n    authors: \"Theo X. Olausson, Alex Gu, Ben Lipkin, et al.\"\n    year: 2023\n    venue: \"EMNLP 2023\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Neurosymbolic approach where LLM translates NL to FOL for theorem\n      prover. Directly comparable to STA's NL->Prolog translation.\n      LINC uses prompting-based approach; STA uses RL training.\n    key_finding: >\n      StarCoder+ (15.5B) with LINC outperforms GPT-3.5 and GPT-4 with\n      CoT by 38% and 10% respectively on ProofWriter.\n\n  - id: fover-pei2025\n    title: \"FoVer: First-Order Logic Verification for Natural Language Reasoning\"\n    authors: \"Yu Pei, Yongping Du, Xingnan Jin\"\n    year: 2025\n    venue: \"TACL 13:1340-1359\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      Uses LLM->FOL->Z3 pipeline for verifying NL reasoning correctness.\n      Similar to STA's verification pipeline but focuses on post-hoc\n      verification rather than training reward signal.\n    key_finding: >\n      FOL verification via Z3 significantly outperforms existing methods\n      on ProofWriter and FOLIO benchmarks.\n\n  - id: lorp\n    title: \"LoRP: LLM-based Logical Reasoning via Prolog\"\n    authors: \"Various\"\n    year: 2025\n    venue: \"Knowledge-Based Systems 2025\"\n    category: fol-formalization\n    role: direct-competitor\n    relevance: >\n      LLM->Prolog pipeline with FOL-to-Prolog translation mechanism.\n      Closest to STA's formalization target (Prolog), though LoRP\n      uses prompting while STA uses GRPO training with structural reward.\n    key_finding: >\n      Systematic FOL-to-Prolog translation extends Prolog expressiveness;\n      achieves SoTA accuracy on logical reasoning with three-vote majority.\n\n  - id: nl2fol\n    title: \"NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection\"\n    authors: \"Lalwani, Kim, et al.\"\n    year: 2024\n    venue: \"arXiv 2405.02318\"\n    category: fol-formalization\n    role: background\n    relevance: >\n      Step-by-step NL->FOL translation using LLMs with SMT solver\n      verification. Demonstrates the NL->formal logic pipeline that\n      STA aims to improve via RL training.\n    key_finding: >\n      Neurosymbolic NL2FOL achieves 78% F1 on LOGIC dataset and\n      generalizes to LogicClimate (80% F1), outperforming supervised\n      models by 21%.\n\n  - id: logica2\n    title: \"LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"IEEE/ACM TASLP 2023\"\n    category: fol-formalization\n    role: evaluation\n    relevance: >\n      Logical reasoning evaluation benchmark derived from Chinese civil\n      service exams. Provides supplementary evaluation for STA's\n      formalization capabilities.\n    key_finding: >\n      8,678 multiple-choice questions covering categorical, disjunctive,\n      and conditional reasoning; widely used LLM benchmark.\n\n  # ============================================================\n  # Category 7: Goodhart's Law theory and dose-response dynamics\n  # ============================================================\n\n  - id: manheim-goodhart-taxonomy\n    title: \"Categorizing Variants of Goodhart's Law\"\n    authors: \"David Manheim, Scott Garrabrant\"\n    year: 2019\n    venue: \"arXiv 1803.04585\"\n    category: goodhart-overoptimization\n    role: theoretical-foundation\n    relevance: >\n      Four-part Goodhart taxonomy: regressional, extremal, causal, adversarial.\n      STA's high-β ISR collapse is best classified as extremal Goodhart\n      (policy moves to OOD region where ISR↑ but prove_rate↓). Provides\n      vocabulary for discussion section.\n    key_finding: >\n      First systematic categorization of Goodhart failure modes. Extremal\n      variant occurs when proxy-goal relationship breaks in out-of-distribution\n      regions reached by strong optimization.\n\n  - id: pan-reward-misspecification\n    title: \"The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models\"\n    authors: \"Alexander Pan, Kush Bhatia, Jacob Steinhardt\"\n    year: 2022\n    venue: \"ICLR 2022\"\n    category: goodhart-overoptimization\n    role: theoretical-foundation\n    relevance: >\n      Across 9 environments, more capable agents exploit misspecifications more.\n      Observes dose-dependent degradation — capability thresholds where true\n      reward sharply drops. Matches STA's β=0.1→0.3 qualitative shift.\n    key_finding: >\n      Reward misspecification causes dose-dependent degradation where true reward\n      sharply drops past capability thresholds. More capable optimization\n      produces worse outcomes under misspecification.\n\n  - id: kwa-catastrophic-goodhart\n    title: \"Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification\"\n    authors: \"Tat-Thang Kwa, Rachel Thomas, Adrià Garriga-Alonso\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: goodhart-overoptimization\n    role: theoretical-foundation\n    relevance: >\n      If reward model error is heavy-tailed, policies achieve arbitrarily\n      high proxy reward with no true utility gain. KL regularization provably\n      fails. Explains why KL penalty in GRPO cannot prevent ISR collapse\n      at high β if ISR error distribution is heavy-tailed.\n    key_finding: >\n      KL-regularized RL provably fails to prevent overoptimization under\n      heavy-tailed reward misspecification. Policies can achieve arbitrarily\n      high proxy reward with zero true utility.\n\n  - id: rafailov-daa-scaling\n    title: \"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms\"\n    authors: \"Rafael Rafailov, Yaswanth Chittepu, Ryan Park, Harshit Sikchi, Joey Hejna, W. Bradley Knox, Chelsea Finn, Scott Niekum\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    category: goodhart-overoptimization\n    role: supporting-evidence\n    relevance: >\n      Extends Gao et al. to DPO/IPO/SLiC. Tests seven β values across\n      1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM.\n      Validates β as a \"dose\" parameter — directly analogous to STA's\n      ISR weight sweep.\n    key_finding: >\n      Direct alignment algorithms exhibit overoptimization following\n      predictable scaling laws. Smaller models overoptimize sooner.\n      β-controlled dose-response is a general phenomenon across RL paradigms.\n\n  - id: huang-chi-squared\n    title: \"Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction\"\n    authors: \"Afra Feyza Akyürek, Banghua Zhu, Sham Kakade, Jiantao Jiao\"\n    year: 2025\n    venue: \"ICLR 2025 Poster\"\n    category: goodhart-overoptimization\n    role: supporting-evidence\n    relevance: >\n      KL-regularization is theoretically inadequate for preventing\n      overoptimization. Chi-squared divergence provably alleviates it.\n      Suggests that even with KL penalty in GRPO, STA's high-β collapse\n      is theoretically expected.\n    key_finding: >\n      Chi-squared preference optimization provably mitigates overoptimization\n      where KL-regularization fails. Alternative divergence measures offer\n      stronger guarantees.\n\n  - id: coste-rm-ensembles\n    title: \"Reward Model Ensembles Help Mitigate Overoptimization\"\n    authors: \"Thomas Coste, Usman Anwar, Robert Kirk, David Krueger\"\n    year: 2023\n    venue: \"NeurIPS 2023 Workshop on Alignment\"\n    category: goodhart-overoptimization\n    role: background\n    relevance: >\n      Worst-case optimization across RM ensembles practically eliminates\n      overoptimization for BoN and reduces it for PPO. Suggests ensemble\n      of multiple solver metrics (instead of single ISR) as mitigation.\n    key_finding: >\n      RM ensembles with worst-case aggregation mitigate overoptimization.\n      Ensemble size and diversity directly affect robustness.\n\n  # ============================================================\n  # Category 8: Solver/prover as RL reward signal\n  # ============================================================\n\n  - id: rlsf\n    title: \"Reinforcement Learning via Symbolic Feedback\"\n    authors: \"Abhinav Jha, Shikhar Murty, Zico Kolter, et al.\"\n    year: 2024\n    venue: \"arXiv 2405.16661\"\n    category: verification-reward\n    role: direct-competitor\n    relevance: >\n      Most directly relevant: uses solver/prover certificates as fine-grained\n      token-level reward signal. Outperforms traditional approaches on program\n      synthesis (+31.4%). STA extends this paradigm and shows when it breaks\n      (Goodhart effects at high auxiliary reward weight).\n    key_finding: >\n      Symbolic reasoning tools provide poly-sized certificates as reward.\n      Smaller RLSF models outperform GPT-4 on structured generation tasks.\n\n  - id: fover-kamoi2026\n    title: \"FoVer: Generalizable Process Reward Models via Formally Verified Training Data\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    year: 2025\n    venue: \"Findings of ACL 2026 (arXiv 2502.01345)\"\n    category: verification-reward\n    role: supporting-evidence\n    relevance: >\n      Uses Z3 and Isabelle to synthesize PRM training data by annotating\n      step-level error labels without human annotation. Same solver family\n      as STA. Shows verification-based rewards work; STA extends by showing\n      dose-response dynamics.\n    key_finding: >\n      Formally verified training data enables generalizable process reward\n      models competitive on ProcessBench and 12 reasoning benchmarks.\n\n  - id: deepseek-prover-v15\n    title: \"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\"\n    authors: \"DeepSeek AI\"\n    year: 2024\n    venue: \"ICLR 2025 (arXiv 2408.08152)\"\n    category: verification-reward\n    role: method-component\n    relevance: >\n      Uses GRPO with Lean 4 verification as binary reward. Same algorithm\n      (GRPO) + formal verification, but binary (pass/fail). Binary reward\n      avoids the graded-metric Goodhart risk that STA identifies with ISR.\n    key_finding: >\n      GRPO + binary Lean verification achieves 63.5% on miniF2F. Binary\n      correctness guarantee via formal verification sidesteps proxy reward\n      overoptimization.\n\n  - id: alphaproof\n    title: \"AlphaProof\"\n    authors: \"Google DeepMind\"\n    year: 2024\n    venue: \"Nature 2025\"\n    category: verification-reward\n    role: background\n    relevance: >\n      AlphaZero-inspired RL with Lean proof verification at scale.\n      Silver medal at IMO 2024. Binary verification reward avoids the\n      Goodhart problem STA identifies with graded verification metrics.\n    key_finding: >\n      Binary formal verification as RL reward scales to IMO-level\n      mathematical reasoning. Demonstrates verification-reward RL works\n      at the frontier of mathematical difficulty.\n\n  - id: math-shepherd\n    title: \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\"\n    authors: \"Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, et al.\"\n    year: 2024\n    venue: \"ACL 2024 (arXiv 2312.08935)\"\n    category: verification-reward\n    role: supporting-evidence\n    relevance: >\n      Automatically constructs process supervision data and uses it as\n      step-by-step PPO reward. Automated verification reward without human\n      labels, analogous to STA's automated ISR computation via solver.\n    key_finding: >\n      Automated process supervision improves Mistral-7B on GSM8K\n      (77.9→84.1%) and MATH (28.6→33.0%) without human annotation.\n\n  # ============================================================\n  # Additional reward-shaping papers (Goodhart survey additions)\n  # ============================================================\n\n  - id: bipars\n    title: \"Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping\"\n    authors: \"Yujing Hu, Weixun Wang, Hangtian Jia, et al.\"\n    year: 2020\n    venue: \"NeurIPS 2020\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Bi-level optimization learns parameterized shaping reward weights.\n      Can transform harmful shaping rewards into beneficial ones by learning\n      negative weights. Directly addresses STA's problem: when ISR weight\n      is wrong, automated weight learning could find optimal β.\n    key_finding: >\n      Bi-level optimization automatically learns auxiliary reward weights,\n      outperforming fixed weights and recovering from harmful shaping rewards.\n\n  - id: dapo\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: \"Qiying Yu et al. (ByteDance)\"\n    year: 2025\n    venue: \"arXiv 2503.14476\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Four techniques for stable multi-component reward in GRPO: Clip-Higher,\n      Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping.\n      Addresses stability issues relevant to STA's multi-reward setup.\n    key_finding: >\n      Clip-Higher and Dynamic Sampling prevent entropy collapse in GRPO\n      with multi-component rewards. Soft punishment for overlong outputs\n      avoids reward hacking through length exploitation.\n",
      "numLines": 952,
      "startLine": 1,
      "totalLines": 952
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have all 44 papers. Let me parse them and generate the BibTeX. Let me also check if the paper directory exists.

Let me count the papers:
1. deepseek-r1
2. deepseekmath
3. logic-rl
4. mellgren-prolog-grpo
5. satlm
6. deepproblog
7. neurasp
8. thought-like-pro
9. lightman-verify-step
10. reward-shaping-rlhf
11. rlvr-reasoning
12. rubric-grpo


13. gao-effective-rl-reward
14. prof-process-outcome
15. moskovitz-constrained-rlhf
16. skalse-reward-hacking
17. progrs-outcome-conditioned
18. qwen-prm-lessons
19. demillo1978
20. offutt-coupling
21. jia-harman-survey
22. just-mutants-real-faults
23. llmorpheus
24. mutation-guided-meta
25. mutation-consistency-llm
26. deepmutation
27. inform-reward-hacking
28. mo-grpo
29. reward-hacking-survey
30. energy
31. spurious-rewards
32. bondarenko-spec-gaming
33. kim-game-formalization
34. gao-reward-overoptimization
35. karwowski-goodhart-rl
36. folio
37. proofwriter
38. logic-lm
39. linc
40. fover-pei2025
41. lorp
42. nl2fol
43. logica2
44. manheim-goodhart-taxonomy
45. pan-reward-misspecification
46. kwa-catastrophic-goodhart
47. rafailov-daa-scaling
48. huang-chi-squared
49. coste-rm-ensembles
50. rlsf
51. fover-kamoi2026
52. deepseek-prover-v15
53. alphaproof
54. math-shepherd
55. bipars
56. dapo

I'm compiling a bibliography of 56 papers spanning reward hacking, specification gaming, formal reasoning, and proof verification in language models.

Now I need to generate BibTeX entries for all of them. I'll categorize each paper by its publication venue—arXiv-only papers get @article with eprint fields, papers with both arXiv and conference venues go to @inproceedings with the arXiv as a note, pure conference papers use @inproceedings, journal papers use @article, and anything else defaults to @misc. Let me work through the entries systematically, starting with the neurosymbolic-RL section and handling cases like deepseek-r1 which has both an arXiv preprint and a Nature publication. and arXiv as note.

2. deepseekmath: "arXiv 2402.03300" → @article with eprint

3. logic-rl: "arXiv 2502.14768" → @article with eprint

4. mellgren-prolog-grpo: "arXiv 2512.07407" → @article with eprint

5. satlm: "NeurIPS 2023" → @inproceedings

6. deepproblog: "Artificial Intelligence 298" → @article, journal

7. neurasp: "IJCAI 2020" → @inproceedings

8. thought-like-pro: "arXiv 2407.14562" → @article with eprint

**Category 2: reward-shaping**

9. lightman-verify-step: "arXiv 2305.20050 / ICLR 2024" → @inproceedings (ICLR), arXiv as note

10. reward-shaping-rlhf: "arXiv 2502.18770" → @article with eprint

11. rlvr-reasoning: "arXiv 2506.14245" → @article with eprint

12. rubric-grpo: "arXiv 2605.08061" → @article with eprint

13. gao-effective-rl-reward: "arXiv 2410.15115" → @article with eprint

14. prof-process-outcome: "arXiv 2509.03403" → @article with eprint

15. moskovitz-constrained-rlhf: "arXiv 2310.04373 / ICLR 2024" → @inproceedings (ICLR), arXiv as note

16. skalse-reward-hacking: "arXiv 2209.13085 / NeurIPS 2022" → @inproceedings (NeurIPS), arXiv as note

17. progrs-outcome-conditioned: "arXiv 2604.02341" → @article with eprint

18. qwen-prm-lessons: "ACL 2025 Findings (arXiv 2501.07301)" → @inproceedings (ACL), arXiv as note

**Category 3: mutation-testing**

19. demillo1978: "Computer 11(4):34-43

" → @article, journal=Computer

20. offutt-coupling: "ACM TOSEM 1(1):5-20" → @article, journal=ACM TOSEM

21. jia-harman-survey: "IEEE TSE 37(5):649-678" → @article, journal=IEEE TSE

22. just-mutants-real-faults: "FSE 2014" → @inproceedings

23. llmorpheus: "IEEE TSE 2025" → @article, journal=IEEE TSE

24. mutation-guided-meta: "FSE 2025" → @inproceedings

25. mutation-consistency-llm: "arXiv 2401.05940" → @article with eprint

**Category 4: intensional-analysis**

26. deepmutation: "Information and Software Technology 2023" → @article, journal

**Category 5: reward-hacking**

27. inform-reward-hacking: "NeurIPS 2024" → @inproceedings

Continuing through the bibliography entries, mapping each reference to its appropriate BibTeX format based on publication venue and type. Continuing through the bibliography entries. Kim's game formalization paper is from the VerifAI-2 Workshop at ICLR 2026 with an arXiv preprint, so that's an inproceedings entry with the arXiv as a note. Gao's reward overoptimization work appeared at ICML 2023 with an arXiv version, and Karwowski's Goodhart's law paper is from ICLR 2024, both inproceedings with arXiv notes. Moving into the formalization category now—FOLIO has both an arXiv and EMNLP 2024 publication, so I'll use the conference as primary with the preprint noted, and ProofWriter appeared in the Findings of ACL-IJCNLP 2021.

Logic-LM is from the Findings of EMNLP 2023, LINC from EMNLP 2023 proper, and then I'm seeing some journal articles: FOVER in TACL volume 13, LORP in Knowledge-Based Systems 2025, NL2FOL as an arXiv preprint, and Logica2 in IEEE/ACM TASLP 2023. Now shifting to the Goodhart and overoptimization category—Manheim's taxonomy paper is on arXiv, Pan's reward misspecification work is from ICLR 2022, and Kwa's catastrophic Goodhart paper appeared at NeurIPS 2024.

Continuing with Rafailov's DAA scaling work also from NeurIPS 2024, Huang's chi-squared test at ICLR 2025 as a poster, and Coste's reward model ensembles from the NeurIPS 2023 alignment workshop. Moving into verification and reward models now—RLSF is an arXiv paper, FOVER appears in ACL 2026 Findings with an arXiv identifier, DeepSeek Prover v1.5 was published at ICLR 2025 with arXiv details, and AlphaProof came out in Nature 2025.

Math-Shepherd is from ACL 2024 with an arXiv preprint. Then there's a section on additional reward-shaping approaches—BIPARS from NeurIPS 2020 and DAPO as an arXiv-only entry. That brings me to 56 papers total, which is more than the stated 44, but the instructions allow for a margin of error. I'll proceed with generating all of them in BibTeX format, being careful with author names and title capitalization, extracting arXiv IDs where needed.

Generating the BibTeX entries... I'm noticing several entries with "Various" as the author field, which isn't ideal for BibTeX formatting, but I'll keep them as provided since that's what the source data shows. For the entries with partial author information or organizational names like "CyberAgent AI Lab" or "Google DeepMind," I'll use those as given rather than trying to reconstruct full author lists.

Now I need to handle the `primaryClass` field—the task specifies `cs.AI` for arXiv entries, so I'll apply that consistently across all papers. For the dual-source entries like deepseek-r1 and lightman-verify-step, I'll structure them as articles or conference papers with the primary venue in the main fields and the arXiv reference in a note field.

Writing the BibTeX file now...

For author names, I need to convert the YAML comma-separated format to BibTeX's "and" separator. I'll also handle special cases like "et al." by converting to "and others", and protect entries like "Various" with braces to prevent parsing issues.

Now I'm writing out the BibTeX file with proper formatting... I'm debating the right format for arXiv entries in BibTeX—whether to include `journal = {arXiv preprint}` or omit it entirely—and I've decided to go with the preprint journal field since `@article` requires one. Rather than continue formatting entries manually, I should just write out the complete bibliography file directly using the Write tool. First, let me verify that the paper directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "d816037e-a151-4c09-99e6-91525d36008f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2HGWcGP2qdSnkAuYCJebj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14151,
      "cache_read_input_tokens": 24542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14151
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

_source line 8_

<details open><summary>🔧 Tool call — Bash · `toolu_01VEidG5Tuz97UFNppSiA4dn`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/",
  "description": "Check paper directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "27f6567b-aa9e-403b-a9d6-bf3b86d51aa5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2HGWcGP2qdSnkAuYCJebj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14151,
      "cache_read_input_tokens": 24542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14151
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

_source line 9 · 2026-05-14T18:32:18.136Z_

<details><summary>↩ Tool result · `toolu_01VEidG5Tuz97UFNppSiA4dn`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "47809dfb-f180-4a82-acf4-07aabde7f09c",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
The directory exists but is empty. Let me now count the papers in the YAML to confirm.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "2bef5c9c-b406-4e69-b19c-0d62195b87e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJw14FnvLatX3UDpAzv1yk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4209,
      "cache_read_input_tokens": 38693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4209
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

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_01FLtH3wRP3SLz9S2HzjLCqu`</summary>

```json
{
  "command": "grep -c '^ *- id:' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "description": "Count paper entries in literature map"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "dcc89db8-49e7-4c0c-af58-0fd169197254",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJw14FnvLatX3UDpAzv1yk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4209,
      "cache_read_input_tokens": 38693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4209
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

_source line 12 · 2026-05-14T18:32:22.367Z_

<details><summary>↩ Tool result · `toolu_01FLtH3wRP3SLz9S2HzjLCqu`</summary>

```text
56
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "0b77bf86-88f0-4e43-a4d4-d17c64cefc0c",
  "tool_use_result": {
    "stdout": "56",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 13_

YAML contains 56 papers, not 44. I'll generate all 56 entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "9336b92b-b3d3-452a-85c3-aa3f30334add",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xqGTWJvzGNMzcXwkYMs56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 165,
      "cache_read_input_tokens": 42902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 165
      },
      "output_tokens": 3,
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

<details open><summary>🔧 Tool call — Write · `toolu_01V9QYgniDxdKV8gF8KqtCpu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "content": "% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  note         = {arXiv:2501.12948},\n}\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Xian and others},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2024},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and others},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n@article{deepproblog,\n  author       = {Robin Manhaeve and Sebastijan Duman{\\v{c}}i{\\'c} and Angelika Kimmig and Thomas Demeester and Luc De Raedt},\n  title        = {{Neural Probabilistic Logic Programming in DeepProbLog}},\n  journal      = {Artificial Intelligence},\n  volume       = {298},\n  year         = {2021},\n}\n\n@inproceedings{neurasp,\n  author       = {Zhun Yang and Adam Ishay and Joohyung Lee},\n  title        = {{NeurASP: Embracing Neural Networks into Answer Set Programming}},\n  booktitle    = {Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},\n  year         = {2020},\n}\n\n@article{thought-like-pro,\n  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},\n  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},\n  journal      = {arXiv preprint arXiv:2407.14562},\n  year         = {2024},\n  eprint       = {2407.14562},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@article{reward-shaping-rlhf,\n  author       = {Jiayi Fu and Xuandong Zhao and Chengyuan Yao and others},\n  title        = {{Reward Shaping to Mitigate Reward Hacking in RLHF}},\n  journal      = {arXiv preprint arXiv:2502.18770},\n  year         = {2025},\n  eprint       = {2502.18770},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rlvr-reasoning,\n  author       = {{Various}},\n  title        = {{Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs}},\n  journal      = {arXiv preprint arXiv:2506.14245},\n  year         = {2025},\n  eprint       = {2506.14245},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rubric-grpo,\n  author       = {{Various}},\n  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},\n  journal      = {arXiv preprint arXiv:2605.08061},\n  year         = {2025},\n  eprint       = {2605.08061},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{prof-process-outcome,\n  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},\n  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},\n  journal      = {arXiv preprint arXiv:2509.03403},\n  year         = {2025},\n  eprint       = {2509.03403},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{moskovitz-constrained-rlhf,\n  author       = {Ted Moskovitz and Aaditya K. Singh and DJ Strouse and Tuomas Sandholm and Ruslan Salakhutdinov and Anca D. Dragan and Stephen McAleer},\n  title        = {{Confronting Reward Model Overoptimization with Constrained RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n@article{progrs-outcome-conditioned,\n  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},\n  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},\n  journal      = {arXiv preprint arXiv:2604.02341},\n  year         = {2026},\n  eprint       = {2604.02341},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{qwen-prm-lessons,\n  author       = {Zhenru Zhang and others},\n  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2501.07301},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--43},\n  year         = {1978},\n}\n\n@article{offutt-coupling,\n  author       = {A. Jefferson Offutt},\n  title        = {{Investigations of the Software Testing Coupling Effect}},\n  journal      = {ACM Transactions on Software Engineering and Methodology},\n  volume       = {1},\n  number       = {1},\n  pages        = {5--20},\n  year         = {1992},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@inproceedings{just-mutants-real-faults,\n  author       = {Ren{\\'e} Just and Darioush Jalali and Laura Inozemtseva and others},\n  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2014},\n}\n\n@article{llmorpheus,\n  author       = {Frank Tip and Jon Bell and others},\n  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},\n  journal      = {IEEE Transactions on Software Engineering},\n  year         = {2025},\n}\n\n@inproceedings{mutation-guided-meta,\n  author       = {Christopher Foster and others},\n  title        = {{Mutation-Guided LLM-based Test Generation at Meta}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2025},\n}\n\n@article{mutation-consistency-llm,\n  author       = {{Various}},\n  title        = {{Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs}},\n  journal      = {arXiv preprint arXiv:2401.05940},\n  year         = {2024},\n  eprint       = {2401.05940},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 4: Intensional program analysis\n% ============================================================\n\n@article{deepmutation,\n  author       = {{Various}},\n  title        = {{A Probabilistic Framework for Mutation Testing in Deep Neural Networks}},\n  journal      = {Information and Software Technology},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 5: Reward hacking / overoptimization\n% ============================================================\n\n@inproceedings{inform-reward-hacking,\n  author       = {{Various}},\n  title        = {{InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@article{mo-grpo,\n  author       = {{CyberAgent AI Lab}},\n  title        = {{MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems}},\n  journal      = {arXiv preprint arXiv:2509.22047},\n  year         = {2025},\n  eprint       = {2509.22047},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{reward-hacking-survey,\n  author       = {{Various}},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{energy-loss-reward-hacking,\n  author       = {{Various}},\n  title        = {{The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2025},\n}\n\n@article{spurious-rewards,\n  author       = {Ruixin Yang and others},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and others},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},\n  year         = {2021},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {{Various}},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{nl2fol,\n  author       = {Lalwani and Kim and others},\n  title        = {{NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection}},\n  journal      = {arXiv preprint arXiv:2405.02318},\n  year         = {2024},\n  eprint       = {2405.02318},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logica2,\n  author       = {Liu and others},\n  title        = {{LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding}},\n  journal      = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 7: Goodhart's Law theory and dose-response dynamics\n% ============================================================\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{pan-reward-misspecification,\n  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},\n  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2022},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri{\\`a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{rafailov-daa-scaling,\n  author       = {Rafael Rafailov and Yaswanth Chittepu and Ryan Park and Harshit Sikchi and Joey Hejna and W. Bradley Knox and Chelsea Finn and Scott Niekum},\n  title        = {{Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{huang-chi-squared,\n  author       = {Afra Feyza Aky{\\\"u}rek and Banghua Zhu and Sham Kakade and Jiantao Jiao},\n  title        = {{Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n}\n\n@inproceedings{coste-rm-ensembles,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {{Reward Model Ensembles Help Mitigate Overoptimization}},\n  booktitle    = {NeurIPS 2023 Workshop on Alignment},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 8: Solver/prover as RL reward signal\n% ============================================================\n\n@article{rlsf,\n  author       = {Abhinav Jha and Shikhar Murty and Zico Kolter and others},\n  title        = {{Reinforcement Learning via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{fover-kamoi2026,\n  author       = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},\n  title        = {{FoVer: Generalizable Process Reward Models via Formally Verified Training Data}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2026},\n  note         = {arXiv:2502.01345},\n}\n\n@inproceedings{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2408.08152},\n}\n\n@article{alphaproof,\n  author       = {{Google DeepMind}},\n  title        = {{AlphaProof}},\n  journal      = {Nature},\n  year         = {2025},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@inproceedings{bipars,\n  author       = {Yujing Hu and Weixun Wang and Hangtian Jia and others},\n  title        = {{Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2020},\n}\n\n@article{dapo,\n  author       = {Qiying Yu and others},\n  title        = {{DAPO: An Open-Source LLM Reinforcement Learning System at Scale}},\n  journal      = {arXiv preprint arXiv:2503.14476},\n  year         = {2025},\n  eprint       = {2503.14476},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "980655bc-8554-4479-bd93-810bd9dae4cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xqGTWJvzGNMzcXwkYMs56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 165,
      "cache_read_input_tokens": 42902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 165
      },
      "output_tokens": 3,
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

_source line 15 · 2026-05-14T18:33:56.517Z_

<details><summary>↩ Tool result · `toolu_01V9QYgniDxdKV8gF8KqtCpu`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "5ca2f8ab-6634-451a-aca0-d794def542c4",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
    "content": "% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  note         = {arXiv:2501.12948},\n}\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Xian and others},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2024},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and others},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n@article{deepproblog,\n  author       = {Robin Manhaeve and Sebastijan Duman{\\v{c}}i{\\'c} and Angelika Kimmig and Thomas Demeester and Luc De Raedt},\n  title        = {{Neural Probabilistic Logic Programming in DeepProbLog}},\n  journal      = {Artificial Intelligence},\n  volume       = {298},\n  year         = {2021},\n}\n\n@inproceedings{neurasp,\n  author       = {Zhun Yang and Adam Ishay and Joohyung Lee},\n  title        = {{NeurASP: Embracing Neural Networks into Answer Set Programming}},\n  booktitle    = {Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},\n  year         = {2020},\n}\n\n@article{thought-like-pro,\n  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},\n  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},\n  journal      = {arXiv preprint arXiv:2407.14562},\n  year         = {2024},\n  eprint       = {2407.14562},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@article{reward-shaping-rlhf,\n  author       = {Jiayi Fu and Xuandong Zhao and Chengyuan Yao and others},\n  title        = {{Reward Shaping to Mitigate Reward Hacking in RLHF}},\n  journal      = {arXiv preprint arXiv:2502.18770},\n  year         = {2025},\n  eprint       = {2502.18770},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rlvr-reasoning,\n  author       = {{Various}},\n  title        = {{Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs}},\n  journal      = {arXiv preprint arXiv:2506.14245},\n  year         = {2025},\n  eprint       = {2506.14245},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rubric-grpo,\n  author       = {{Various}},\n  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},\n  journal      = {arXiv preprint arXiv:2605.08061},\n  year         = {2025},\n  eprint       = {2605.08061},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{prof-process-outcome,\n  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},\n  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},\n  journal      = {arXiv preprint arXiv:2509.03403},\n  year         = {2025},\n  eprint       = {2509.03403},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{moskovitz-constrained-rlhf,\n  author       = {Ted Moskovitz and Aaditya K. Singh and DJ Strouse and Tuomas Sandholm and Ruslan Salakhutdinov and Anca D. Dragan and Stephen McAleer},\n  title        = {{Confronting Reward Model Overoptimization with Constrained RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n@article{progrs-outcome-conditioned,\n  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},\n  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},\n  journal      = {arXiv preprint arXiv:2604.02341},\n  year         = {2026},\n  eprint       = {2604.02341},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{qwen-prm-lessons,\n  author       = {Zhenru Zhang and others},\n  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2501.07301},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--43},\n  year         = {1978},\n}\n\n@article{offutt-coupling,\n  author       = {A. Jefferson Offutt},\n  title        = {{Investigations of the Software Testing Coupling Effect}},\n  journal      = {ACM Transactions on Software Engineering and Methodology},\n  volume       = {1},\n  number       = {1},\n  pages        = {5--20},\n  year         = {1992},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@inproceedings{just-mutants-real-faults,\n  author       = {Ren{\\'e} Just and Darioush Jalali and Laura Inozemtseva and others},\n  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2014},\n}\n\n@article{llmorpheus,\n  author       = {Frank Tip and Jon Bell and others},\n  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},\n  journal      = {IEEE Transactions on Software Engineering},\n  year         = {2025},\n}\n\n@inproceedings{mutation-guided-meta,\n  author       = {Christopher Foster and others},\n  title        = {{Mutation-Guided LLM-based Test Generation at Meta}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2025},\n}\n\n@article{mutation-consistency-llm,\n  author       = {{Various}},\n  title        = {{Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs}},\n  journal      = {arXiv preprint arXiv:2401.05940},\n  year         = {2024},\n  eprint       = {2401.05940},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 4: Intensional program analysis\n% ============================================================\n\n@article{deepmutation,\n  author       = {{Various}},\n  title        = {{A Probabilistic Framework for Mutation Testing in Deep Neural Networks}},\n  journal      = {Information and Software Technology},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 5: Reward hacking / overoptimization\n% ============================================================\n\n@inproceedings{inform-reward-hacking,\n  author       = {{Various}},\n  title        = {{InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@article{mo-grpo,\n  author       = {{CyberAgent AI Lab}},\n  title        = {{MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems}},\n  journal      = {arXiv preprint arXiv:2509.22047},\n  year         = {2025},\n  eprint       = {2509.22047},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{reward-hacking-survey,\n  author       = {{Various}},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{energy-loss-reward-hacking,\n  author       = {{Various}},\n  title        = {{The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2025},\n}\n\n@article{spurious-rewards,\n  author       = {Ruixin Yang and others},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and others},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},\n  year         = {2021},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {{Various}},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{nl2fol,\n  author       = {Lalwani and Kim and others},\n  title        = {{NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection}},\n  journal      = {arXiv preprint arXiv:2405.02318},\n  year         = {2024},\n  eprint       = {2405.02318},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logica2,\n  author       = {Liu and others},\n  title        = {{LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding}},\n  journal      = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 7: Goodhart's Law theory and dose-response dynamics\n% ============================================================\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{pan-reward-misspecification,\n  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},\n  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2022},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri{\\`a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{rafailov-daa-scaling,\n  author       = {Rafael Rafailov and Yaswanth Chittepu and Ryan Park and Harshit Sikchi and Joey Hejna and W. Bradley Knox and Chelsea Finn and Scott Niekum},\n  title        = {{Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{huang-chi-squared,\n  author       = {Afra Feyza Aky{\\\"u}rek and Banghua Zhu and Sham Kakade and Jiantao Jiao},\n  title        = {{Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n}\n\n@inproceedings{coste-rm-ensembles,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {{Reward Model Ensembles Help Mitigate Overoptimization}},\n  booktitle    = {NeurIPS 2023 Workshop on Alignment},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 8: Solver/prover as RL reward signal\n% ============================================================\n\n@article{rlsf,\n  author       = {Abhinav Jha and Shikhar Murty and Zico Kolter and others},\n  title        = {{Reinforcement Learning via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{fover-kamoi2026,\n  author       = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},\n  title        = {{FoVer: Generalizable Process Reward Models via Formally Verified Training Data}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2026},\n  note         = {arXiv:2502.01345},\n}\n\n@inproceedings{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2408.08152},\n}\n\n@article{alphaproof,\n  author       = {{Google DeepMind}},\n  title        = {{AlphaProof}},\n  journal      = {Nature},\n  year         = {2025},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@inproceedings{bipars,\n  author       = {Yujing Hu and Weixun Wang and Hangtian Jia and others},\n  title        = {{Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2020},\n}\n\n@article{dapo,\n  author       = {Qiying Yu and others},\n  title        = {{DAPO: An Open-Source LLM Reinforcement Learning System at Scale}},\n  journal      = {arXiv preprint arXiv:2503.14476},\n  year         = {2025},\n  eprint       = {2503.14476},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01TtZpzJpPfuU4Yyap8FrEb6`</summary>

```json
{
  "command": "grep -c '^@' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "description": "Count BibTeX entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "4c2f6105-05c9-4ef1-9d05-42b5be950417",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VZSv8CezfpVjS1Wc1pYDH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6690,
      "cache_read_input_tokens": 43067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6690
      },
      "output_tokens": 49,
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

_source line 17 · 2026-05-14T18:34:00.535Z_

<details><summary>↩ Tool result · `toolu_01TtZpzJpPfuU4Yyap8FrEb6`</summary>

```text
56
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "bdcd73ea-af0f-4a30-bed2-bf2f627f01df",
  "tool_use_result": {
    "stdout": "56",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 18_

56 条 BibTeX 条目已写入 `paper/references.bib`，覆盖 literature_map.yaml 中全部 56 篇论文（YAML 实际有 56 篇，非任务描述的 44 篇）。按 8 个 category 分组，注释分隔。arXiv+会议的条目优先用会议格式（`@inproceedings`），arXiv ID 放 `note`；纯 arXiv 用 `@article` 带 `eprint`/`archivePrefix`；期刊用 `@article`。所有 title 已用 `{{...}}` 保护。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "uuid": "fa13e62e-5251-49ea-90d2-14bda8c39569",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y11V2iy3wFG3Yr1CGw9Ex2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 127,
      "cache_read_input_tokens": 49757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 127
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

_source line 19_

56 条 BibTeX 条目已写入 `paper/references.bib`，覆盖 literature_map.yaml 中全部 56 篇论文（YAML 实际有 56 篇，非任务描述的 44 篇）。按 8 个 category 分组，注释分隔。arXiv+会议的条目优先用会议格式（`@inproceedings`），arXiv ID 放 `note`；纯 arXiv 用 `@article` 带 `eprint`/`archivePrefix`；期刊用 `@article`。所有 title 已用 `{{...}}` 保护。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 191179,
  "duration_api_ms": 192276,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "91158eec-dcb9-4798-9749-9a0de8ecc9e2",
  "total_cost_usd": 0.62995575,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 38043,
    "cache_read_input_tokens": 210802,
    "output_tokens": 11381,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38043,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 180,
        "cache_read_input_tokens": 49757,
        "cache_creation_input_tokens": 127,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 127
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2146,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0022259999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 11381,
      "cacheReadInputTokens": 210802,
      "cacheCreationInputTokens": 38043,
      "webSearchRequests": 0,
      "costUSD": 0.62772975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "4a3f4430-d8f3-47ca-9de6-d5598828b3e2"
}
```

</details>

---
