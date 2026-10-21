# paper writing related work

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_writing_related-work_20260515T045854.log`
- **Structured JSON:** [`f86f2d7eab9dc87f04e7.json`](../../sessions/f8/f86f2d7eab9dc87f04e7.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
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
  "uuid": "4af40659-9b0e-46eb-9ab7-e8dae45e8394",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1778838000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "442d38fa-4b1f-4866-9ca4-1a00bd243ce7",
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36"
}
```

---

### Assistant

_source line 4_

I'll start by reading all the input files to understand the context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "c0927ded-b4af-4c87-a96c-7fd6438c6fd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fqexs1nf7oaqAwMbEiQ2AH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11453,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11453
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

<details open><summary>🔧 Tool call — Read · `toolu_011VjXiBsbPNAc1VyHsibgGF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/literature_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "a8bbc88c-940f-4a03-9eca-323f2b31287e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fqexs1nf7oaqAwMbEiQ2AH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11453,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11453
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

_source line 6 · 2026-05-15T04:59:08.276Z_

<details><summary>↩ Tool result · `toolu_011VjXiBsbPNAc1VyHsibgGF`</summary>

````text
1	# Related Work Literature Notes
2	
3	> Generated 2026-05-15. Verified via WebSearch + WebFetch.
4	
5	## Core Comparisons
6	
7	### 1. Self-Healing (2025)
8	- **Full Title**: Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning
9	- **Authors**: Yixin Ji, Zhimin Lin, Juntao Li, Kaixin Wu, Kai Yao, Xu Jia, Linjian Mo, Min Zhang
10	- **Venue/Year**: ICLR 2026 (submitted Sep 2025, modified Feb 2026)
11	- **arXiv**: Not found on arXiv; OpenReview ID: Cy8Qa4gAst
12	- **Core Method**: First work applying RLVR (reinforcement learning with verifiable reward) to recover pruned large reasoning models. Shows that structured pruning degrades math reasoning but doesn't destroy it — leaving room for RL-based recovery. RLVR treats recovery as active exploration rather than passive imitation (SFT).
13	- **Key Results**: At 25% compression, RLVR recovery achieves >95% accuracy vs ~80% with SFT across 5 LRMs on 6 math benchmarks, nearly matching unpruned performance.
14	- **vs RASP**: Self-Healing tests RLVR recovery with standard importance-based pruning at a single sparsity ratio. RASP optimizes the pruning decision itself FOR recovery by predicting recoverability via CKA, yielding better accuracy at the same sparsity+recovery budget.
15	
16	### 2. GRASPrune (ACL 2026)
17	- **Full Title**: GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models
18	- **Authors**: Ziyang Wang, Jiangfeng Xiao, Chuan Xiao, Ruoxiang Li, Rui Mao, Jianbin Qin
19	- **Venue/Year**: ACL 2026 Main
20	- **arXiv**: 2604.19398 (Apr 2026)
21	- **Core Method**: Jointly prunes FFN channels and KV head groups under a single global budget. Learns lightweight gate scores with a projected straight-through estimator enforcing a hard mask at every step, backbone weights frozen. Post-mask calibration of scaling factors mitigates scale mismatch.
22	- **Key Results**: LLaMA-2-7B at 50% params → 12.18 PPL on WikiText-2 with competitive zero-shot accuracy. At 0.4 retention ratio, achieves best average accuracy among structured pruning methods.
23	- **vs RASP**: SOTA budgeted pruning without studying post-pruning recovery. GRASPrune is our primary pruning baseline — RASP adds recovery-awareness (CKA functional overlap) on top of importance-based scoring.
24	
25	### 3. RESP (Dec 2025)
26	- **Full Title**: Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models
27	- **Authors**: Ziyan Wang, Enmao Diao, Qi Le, Pu Wang, Guanchu Wang, Minwoo Lee, Shu-ping Yeh, Li Yang
28	- **Venue/Year**: arXiv preprint, Dec 2025
29	- **arXiv**: 2512.02185
30	- **Core Method**: Self-reflective structured pruning (RESP) aligns pruning with the model's reasoning dynamics via three components: (1) self-generated reasoning traces as calibration (not human labels), (2) decode-only gradient-based importance estimation, (3) progressive calibration regeneration that refreshes traces as sparsity increases.
31	- **Key Results**: On Qwen3-8B at 40% sparsity: GSM8K 81.3%, MathQA 59.6% — surpassing strongest baselines by 66.87% and 47% respectively. Near-dense accuracy at 20-30% sparsity.
32	- **vs RASP**: RESP uses reasoning-trace calibration to improve pruning importance estimation but has no post-pruning recovery mechanism. RASP includes recovery-awareness in the pruning score itself via CKA overlap, enabling RLVR recovery to restore more reasoning capability.
33	
34	### 4. MPruner (2024)
35	- **Full Title**: MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning
36	- **Authors**: Seungbeom Hu, ChanJun Park, Andrew Ferraiuolo, Sang-Ki Ko, Jinwoo Kim, Haein Song, Jieung Kim
37	- **Venue/Year**: arXiv preprint, Aug 2024
38	- **arXiv**: 2408.13482
39	- **Core Method**: Leverages CKA similarity between consecutive layers to identify redundant layers via clustering. Uses mutual information through vector similarity for global layer-wise pruning decisions. Analysis stage runs in linear time.
40	- **Key Results**: Up to 50% reduction in parameters and memory for CNN and transformer models with minimal accuracy loss. Up to 70% compression in some configurations.
41	- **vs RASP**: MPruner uses inter-layer CKA for depth pruning (removing entire layers) in CNNs/transformers. RASP uses intra-layer CKA between individual attention heads for width pruning in reasoning LLMs, and crucially uses CKA as a recoverability predictor rather than a redundancy detector.
42	
43	### 5. PASER (2025)
44	- **Full Title**: PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery
45	- **Authors**: Bowei He, Lihao Yin, Hui-Ling Zhen, Xiaokun Zhang, Mingxuan Yuan, Chen Ma
46	- **Venue/Year**: ICLR 2026 (submitted Feb 2025, revised Feb 2026)
47	- **arXiv**: 2502.12594
48	- **Core Method**: Post-training data selection for pruned LLM recovery. Uses manifold learning and spectral clustering to group recovery instructions in semantic space, then allocates data budget across clusters by degree of capability degradation. Detects and filters conflicting/irrelevant recovery data.
49	- **Key Results**: Recovers general capabilities of pruned LLMs using only 4-20% of original post-training data, significantly outperforming conventional baselines.
50	- **vs RASP**: PASER optimizes recovery DATA selection; RASP optimizes pruning STRUCTURE. The two are complementary — PASER could be applied to RASP's recovery phase to further improve data efficiency.
51	
52	---
53	
54	## Additional Related Work
55	
56	### Pruning for Reasoning Models
57	
58	#### 6. SSGR (Nov 2025)
59	- **Full Title**: Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models
60	- **Authors**: Yang Xiang, Yixin Ji, Juntao Li, Min Zhang
61	- **arXiv**: 2511.18864
62	- **Core Method**: First empirical study of pruning LRMs. Proposes Selective Self-Generated Reasoning (SSGR) calibration data strategy — challenging, moderately-lengthy reasoning examples work best.
63	- **Key Results**: 10-13% reasoning improvement over general pruning methods on DeepSeek-R1-Distill models.
64	- **Relation**: Complements RESP's self-generated calibration approach; from same group as Self-Healing (Ji, Juntao Li, Min Zhang).
65	
66	#### 7. RAC — Reasoning-Aware Compression (Sep 2025)
67	- **Full Title**: Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction
68	- **Authors**: Ryan Lucas, Kayhan Behdin, Zhipeng Wang, Qingquan Song, Shao Tang, Rahul Mazumder
69	- **Venue/Year**: NeurIPS 2025
70	- **arXiv**: 2509.12464
71	- **Core Method**: During pruning, jointly reconstructs activations from input AND model's on-policy CoT traces. Integrates into SparseGPT-style pipelines without retraining.
72	- **Key Results**: Significant improvement over standard calibration for reasoning model compression.
73	- **Relation**: Focuses on unstructured/2:4 sparsity with CoT-aware calibration. RASP targets structured width pruning with recovery prediction.
74	
75	#### 8. From LLMs to LRMs (Jan 2026)
76	- **Full Title**: From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models
77	- **Authors**: Longwei Ding, Anhao Zhao, Fanghua Ye, Ziyang Chen, Xiaoyu Shen
78	- **arXiv**: 2601.18091
79	- **Core Method**: Systematic comparison of depth/width/dynamic pruning across instruction-following vs reasoning-augmented models on 17 tasks.
80	- **Key Results**: Width pruning outperforms depth pruning for generation and reasoning tasks. Static pruning better preserves reasoning; dynamic methods struggle with extended reasoning chains.
81	- **Relation**: Provides evidence motivating RASP's width-pruning focus.
82	
83	#### 9. Doing More With Less (Apr 2026)
84	- **Full Title**: Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling
85	- **Authors**: Ocean Monjur, Shahriar Kabir Nahin, Anshuman Chhabra
86	- **arXiv**: 2604.25098
87	- **Core Method**: Studies pruning's impact on test-time scaling (TTS) in reasoning LLMs (s1.1-7B, Qwen3-8B).
88	- **Key Results**: Structured pruning significantly degrades TTS performance. Unstructured pruning can augment TTS and even outperform unpruned models. Layer-wise sparsity allocation improves TTS further.
89	- **Relation**: Directly motivates why structured pruning needs a recovery mechanism — the degradation is especially severe for reasoning tasks requiring longer chains.
90	
91	### Reasoning Trace Compression
92	
93	#### 10. ThinkPrune (Apr 2025)
94	- **Full Title**: ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning
95	- **arXiv**: 2504.01296
96	- **Core Method**: Uses RL to prune (shorten) reasoning traces at inference time, addressing "overthinking" in long-CoT models.
97	- **Key Results**: On AIME24, DeepSeek-R1-Distill-Qwen-1.5B reasoning length reduced by 50% with only 2% performance drop.
98	- **Relation**: Orthogonal — prunes reasoning tokens, not model parameters. Could be combined with RASP for joint model+inference compression.
99	
100	#### 11. Think, Prune, Train, Improve (Apr 2025)
101	- **Full Title**: Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models
102	- **Authors**: Caia Costello, Simon Guo, Anna Goldie, Azalia Mirhoseini (Stanford)
103	- **arXiv**: 2504.18116
104	- **Core Method**: Iteratively fine-tunes models on their own correct CoT solutions. Ground-truth pruning filters incorrect traces.
105	- **Key Results**: GSM8K: Gemma2-2B 41.9%→57.6%, Gemma2-9B reaches 82% (matching LLaMA-3.1-70B), LLaMA-3.1-70B reaches 91% (surpassing GPT-4o).
106	- **Relation**: "Prune" refers to trace filtering, not parameter pruning. Different problem setting but relevant to reasoning capability scaling.
107	
108	---
109	
110	## Citation BibTeX
111	
112	```bibtex
113	@inproceedings{ji2025selfhealing,
114	  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},
115	  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},
116	  booktitle={International Conference on Learning Representations (ICLR)},
117	  year={2026},
118	  note={OpenReview ID: Cy8Qa4gAst}
119	}
120	
121	@inproceedings{wang2026grasprune,
122	  title={{GRASPrune}: Global Gating for Budgeted Structured Pruning of Large Language Models},
123	  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},
124	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
125	  year={2026},
126	  eprint={2604.19398},
127	  archivePrefix={arXiv}
128	}
129	
130	@article{wang2025resp,
131	  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},
132	  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},
133	  journal={arXiv preprint arXiv:2512.02185},
134	  year={2025}
135	}
136	
137	@article{hu2024mpruner,
138	  title={{MPruner}: Optimizing Neural Network Size with {CKA}-Based Mutual Information Pruning},
139	  author={Hu, Seungbeom and Park, ChanJun and Ferraiuolo, Andrew and Ko, Sang-Ki and Kim, Jinwoo and Song, Haein and Kim, Jieung},
140	  journal={arXiv preprint arXiv:2408.13482},
141	  year={2024}
142	}
143	
144	@inproceedings{he2025paser,
145	  title={{PASER}: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery},
146	  author={He, Bowei and Yin, Lihao and Zhen, Hui-Ling and Zhang, Xiaokun and Yuan, Mingxuan and Ma, Chen},
147	  booktitle={International Conference on Learning Representations (ICLR)},
148	  year={2026},
149	  eprint={2502.12594},
150	  archivePrefix={arXiv}
151	}
152	
153	@article{xiang2025ssgr,
154	  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},
155	  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},
156	  journal={arXiv preprint arXiv:2511.18864},
157	  year={2025}
158	}
159	
160	@inproceedings{lucas2025rac,
161	  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},
162	  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},
163	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
164	  year={2025},
165	  eprint={2509.12464},
166	  archivePrefix={arXiv}
167	}
168	
169	@article{ding2026lrmpruning,
170	  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},
171	  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},
172	  journal={arXiv preprint arXiv:2601.18091},
173	  year={2026}
174	}
175	
176	@article{monjur2026doingmore,
177	  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
178	  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
179	  journal={arXiv preprint arXiv:2604.25098},
180	  year={2026}
181	}
182	
183	@article{thinkprune2025,
184	  title={{ThinkPrune}: Pruning Long Chain-of-Thought of {LLMs} via Reinforcement Learning},
185	  journal={arXiv preprint arXiv:2504.01296},
186	  year={2025}
187	}
188	
189	@article{costello2025thinkprunetrain,
190	  title={Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models},
191	  author={Costello, Caia and Guo, Simon and Goldie, Anna and Mirhoseini, Azalia},
192	  journal={arXiv preprint arXiv:2504.18116},
193	  year={2025}
194	}
195	```
196	
197	---
198	
199	## Search Notes
200	
201	- **Self-Healing**: No arXiv ID found. Paper only on OpenReview (Cy8Qa4gAst). Submitted Sep 2025, accepted ICLR 2026.
202	- **RESP**: No confirmed venue acceptance. arXiv-only (2512.02185, Dec 2025).
203	- **SSGR vs RESP**: Both titled "Think Before You Prune" but different papers/groups. SSGR (2511.18864) from Ji/Li/Zhang group (same as Self-Healing). RESP (2512.02185) from Wang/Diao/Yang group.
204	- All 5 core papers verified real via WebSearch + WebFetch. No fabricated entries.
205	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "3ae423b3-24f0-499d-9008-83a90e5b2583",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/literature_notes.md",
      "content": "# Related Work Literature Notes\n\n> Generated 2026-05-15. Verified via WebSearch + WebFetch.\n\n## Core Comparisons\n\n### 1. Self-Healing (2025)\n- **Full Title**: Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\n- **Authors**: Yixin Ji, Zhimin Lin, Juntao Li, Kaixin Wu, Kai Yao, Xu Jia, Linjian Mo, Min Zhang\n- **Venue/Year**: ICLR 2026 (submitted Sep 2025, modified Feb 2026)\n- **arXiv**: Not found on arXiv; OpenReview ID: Cy8Qa4gAst\n- **Core Method**: First work applying RLVR (reinforcement learning with verifiable reward) to recover pruned large reasoning models. Shows that structured pruning degrades math reasoning but doesn't destroy it — leaving room for RL-based recovery. RLVR treats recovery as active exploration rather than passive imitation (SFT).\n- **Key Results**: At 25% compression, RLVR recovery achieves >95% accuracy vs ~80% with SFT across 5 LRMs on 6 math benchmarks, nearly matching unpruned performance.\n- **vs RASP**: Self-Healing tests RLVR recovery with standard importance-based pruning at a single sparsity ratio. RASP optimizes the pruning decision itself FOR recovery by predicting recoverability via CKA, yielding better accuracy at the same sparsity+recovery budget.\n\n### 2. GRASPrune (ACL 2026)\n- **Full Title**: GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models\n- **Authors**: Ziyang Wang, Jiangfeng Xiao, Chuan Xiao, Ruoxiang Li, Rui Mao, Jianbin Qin\n- **Venue/Year**: ACL 2026 Main\n- **arXiv**: 2604.19398 (Apr 2026)\n- **Core Method**: Jointly prunes FFN channels and KV head groups under a single global budget. Learns lightweight gate scores with a projected straight-through estimator enforcing a hard mask at every step, backbone weights frozen. Post-mask calibration of scaling factors mitigates scale mismatch.\n- **Key Results**: LLaMA-2-7B at 50% params → 12.18 PPL on WikiText-2 with competitive zero-shot accuracy. At 0.4 retention ratio, achieves best average accuracy among structured pruning methods.\n- **vs RASP**: SOTA budgeted pruning without studying post-pruning recovery. GRASPrune is our primary pruning baseline — RASP adds recovery-awareness (CKA functional overlap) on top of importance-based scoring.\n\n### 3. RESP (Dec 2025)\n- **Full Title**: Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models\n- **Authors**: Ziyan Wang, Enmao Diao, Qi Le, Pu Wang, Guanchu Wang, Minwoo Lee, Shu-ping Yeh, Li Yang\n- **Venue/Year**: arXiv preprint, Dec 2025\n- **arXiv**: 2512.02185\n- **Core Method**: Self-reflective structured pruning (RESP) aligns pruning with the model's reasoning dynamics via three components: (1) self-generated reasoning traces as calibration (not human labels), (2) decode-only gradient-based importance estimation, (3) progressive calibration regeneration that refreshes traces as sparsity increases.\n- **Key Results**: On Qwen3-8B at 40% sparsity: GSM8K 81.3%, MathQA 59.6% — surpassing strongest baselines by 66.87% and 47% respectively. Near-dense accuracy at 20-30% sparsity.\n- **vs RASP**: RESP uses reasoning-trace calibration to improve pruning importance estimation but has no post-pruning recovery mechanism. RASP includes recovery-awareness in the pruning score itself via CKA overlap, enabling RLVR recovery to restore more reasoning capability.\n\n### 4. MPruner (2024)\n- **Full Title**: MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning\n- **Authors**: Seungbeom Hu, ChanJun Park, Andrew Ferraiuolo, Sang-Ki Ko, Jinwoo Kim, Haein Song, Jieung Kim\n- **Venue/Year**: arXiv preprint, Aug 2024\n- **arXiv**: 2408.13482\n- **Core Method**: Leverages CKA similarity between consecutive layers to identify redundant layers via clustering. Uses mutual information through vector similarity for global layer-wise pruning decisions. Analysis stage runs in linear time.\n- **Key Results**: Up to 50% reduction in parameters and memory for CNN and transformer models with minimal accuracy loss. Up to 70% compression in some configurations.\n- **vs RASP**: MPruner uses inter-layer CKA for depth pruning (removing entire layers) in CNNs/transformers. RASP uses intra-layer CKA between individual attention heads for width pruning in reasoning LLMs, and crucially uses CKA as a recoverability predictor rather than a redundancy detector.\n\n### 5. PASER (2025)\n- **Full Title**: PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery\n- **Authors**: Bowei He, Lihao Yin, Hui-Ling Zhen, Xiaokun Zhang, Mingxuan Yuan, Chen Ma\n- **Venue/Year**: ICLR 2026 (submitted Feb 2025, revised Feb 2026)\n- **arXiv**: 2502.12594\n- **Core Method**: Post-training data selection for pruned LLM recovery. Uses manifold learning and spectral clustering to group recovery instructions in semantic space, then allocates data budget across clusters by degree of capability degradation. Detects and filters conflicting/irrelevant recovery data.\n- **Key Results**: Recovers general capabilities of pruned LLMs using only 4-20% of original post-training data, significantly outperforming conventional baselines.\n- **vs RASP**: PASER optimizes recovery DATA selection; RASP optimizes pruning STRUCTURE. The two are complementary — PASER could be applied to RASP's recovery phase to further improve data efficiency.\n\n---\n\n## Additional Related Work\n\n### Pruning for Reasoning Models\n\n#### 6. SSGR (Nov 2025)\n- **Full Title**: Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models\n- **Authors**: Yang Xiang, Yixin Ji, Juntao Li, Min Zhang\n- **arXiv**: 2511.18864\n- **Core Method**: First empirical study of pruning LRMs. Proposes Selective Self-Generated Reasoning (SSGR) calibration data strategy — challenging, moderately-lengthy reasoning examples work best.\n- **Key Results**: 10-13% reasoning improvement over general pruning methods on DeepSeek-R1-Distill models.\n- **Relation**: Complements RESP's self-generated calibration approach; from same group as Self-Healing (Ji, Juntao Li, Min Zhang).\n\n#### 7. RAC — Reasoning-Aware Compression (Sep 2025)\n- **Full Title**: Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction\n- **Authors**: Ryan Lucas, Kayhan Behdin, Zhipeng Wang, Qingquan Song, Shao Tang, Rahul Mazumder\n- **Venue/Year**: NeurIPS 2025\n- **arXiv**: 2509.12464\n- **Core Method**: During pruning, jointly reconstructs activations from input AND model's on-policy CoT traces. Integrates into SparseGPT-style pipelines without retraining.\n- **Key Results**: Significant improvement over standard calibration for reasoning model compression.\n- **Relation**: Focuses on unstructured/2:4 sparsity with CoT-aware calibration. RASP targets structured width pruning with recovery prediction.\n\n#### 8. From LLMs to LRMs (Jan 2026)\n- **Full Title**: From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models\n- **Authors**: Longwei Ding, Anhao Zhao, Fanghua Ye, Ziyang Chen, Xiaoyu Shen\n- **arXiv**: 2601.18091\n- **Core Method**: Systematic comparison of depth/width/dynamic pruning across instruction-following vs reasoning-augmented models on 17 tasks.\n- **Key Results**: Width pruning outperforms depth pruning for generation and reasoning tasks. Static pruning better preserves reasoning; dynamic methods struggle with extended reasoning chains.\n- **Relation**: Provides evidence motivating RASP's width-pruning focus.\n\n#### 9. Doing More With Less (Apr 2026)\n- **Full Title**: Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\n- **Authors**: Ocean Monjur, Shahriar Kabir Nahin, Anshuman Chhabra\n- **arXiv**: 2604.25098\n- **Core Method**: Studies pruning's impact on test-time scaling (TTS) in reasoning LLMs (s1.1-7B, Qwen3-8B).\n- **Key Results**: Structured pruning significantly degrades TTS performance. Unstructured pruning can augment TTS and even outperform unpruned models. Layer-wise sparsity allocation improves TTS further.\n- **Relation**: Directly motivates why structured pruning needs a recovery mechanism — the degradation is especially severe for reasoning tasks requiring longer chains.\n\n### Reasoning Trace Compression\n\n#### 10. ThinkPrune (Apr 2025)\n- **Full Title**: ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning\n- **arXiv**: 2504.01296\n- **Core Method**: Uses RL to prune (shorten) reasoning traces at inference time, addressing \"overthinking\" in long-CoT models.\n- **Key Results**: On AIME24, DeepSeek-R1-Distill-Qwen-1.5B reasoning length reduced by 50% with only 2% performance drop.\n- **Relation**: Orthogonal — prunes reasoning tokens, not model parameters. Could be combined with RASP for joint model+inference compression.\n\n#### 11. Think, Prune, Train, Improve (Apr 2025)\n- **Full Title**: Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models\n- **Authors**: Caia Costello, Simon Guo, Anna Goldie, Azalia Mirhoseini (Stanford)\n- **arXiv**: 2504.18116\n- **Core Method**: Iteratively fine-tunes models on their own correct CoT solutions. Ground-truth pruning filters incorrect traces.\n- **Key Results**: GSM8K: Gemma2-2B 41.9%→57.6%, Gemma2-9B reaches 82% (matching LLaMA-3.1-70B), LLaMA-3.1-70B reaches 91% (surpassing GPT-4o).\n- **Relation**: \"Prune\" refers to trace filtering, not parameter pruning. Different problem setting but relevant to reasoning capability scaling.\n\n---\n\n## Citation BibTeX\n\n```bibtex\n@inproceedings{ji2025selfhealing,\n  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},\n  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  note={OpenReview ID: Cy8Qa4gAst}\n}\n\n@inproceedings{wang2026grasprune,\n  title={{GRASPrune}: Global Gating for Budgeted Structured Pruning of Large Language Models},\n  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},\n  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2026},\n  eprint={2604.19398},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025resp,\n  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},\n  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},\n  journal={arXiv preprint arXiv:2512.02185},\n  year={2025}\n}\n\n@article{hu2024mpruner,\n  title={{MPruner}: Optimizing Neural Network Size with {CKA}-Based Mutual Information Pruning},\n  author={Hu, Seungbeom and Park, ChanJun and Ferraiuolo, Andrew and Ko, Sang-Ki and Kim, Jinwoo and Song, Haein and Kim, Jieung},\n  journal={arXiv preprint arXiv:2408.13482},\n  year={2024}\n}\n\n@inproceedings{he2025paser,\n  title={{PASER}: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery},\n  author={He, Bowei and Yin, Lihao and Zhen, Hui-Ling and Zhang, Xiaokun and Yuan, Mingxuan and Ma, Chen},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2502.12594},\n  archivePrefix={arXiv}\n}\n\n@article{xiang2025ssgr,\n  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},\n  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},\n  journal={arXiv preprint arXiv:2511.18864},\n  year={2025}\n}\n\n@inproceedings{lucas2025rac,\n  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},\n  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  eprint={2509.12464},\n  archivePrefix={arXiv}\n}\n\n@article{ding2026lrmpruning,\n  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},\n  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},\n  journal={arXiv preprint arXiv:2601.18091},\n  year={2026}\n}\n\n@article{monjur2026doingmore,\n  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n  journal={arXiv preprint arXiv:2604.25098},\n  year={2026}\n}\n\n@article{thinkprune2025,\n  title={{ThinkPrune}: Pruning Long Chain-of-Thought of {LLMs} via Reinforcement Learning},\n  journal={arXiv preprint arXiv:2504.01296},\n  year={2025}\n}\n\n@article{costello2025thinkprunetrain,\n  title={Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models},\n  author={Costello, Caia and Guo, Simon and Goldie, Anna and Mirhoseini, Azalia},\n  journal={arXiv preprint arXiv:2504.18116},\n  year={2025}\n}\n```\n\n---\n\n## Search Notes\n\n- **Self-Healing**: No arXiv ID found. Paper only on OpenReview (Cy8Qa4gAst). Submitted Sep 2025, accepted ICLR 2026.\n- **RESP**: No confirmed venue acceptance. arXiv-only (2512.02185, Dec 2025).\n- **SSGR vs RESP**: Both titled \"Think Before You Prune\" but different papers/groups. SSGR (2511.18864) from Ji/Li/Zhang group (same as Self-Healing). RESP (2512.02185) from Wang/Diao/Yang group.\n- All 5 core papers verified real via WebSearch + WebFetch. No fabricated entries.\n",
      "numLines": 205,
      "startLine": 1,
      "totalLines": 205
    }
  }
}
````

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_019UsMwXpLerxsCywSwaaTZK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "f3e7c660-43e5-4585-bd15-701b9116725b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fqexs1nf7oaqAwMbEiQ2AH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11453,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11453
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

_source line 8 · 2026-05-15T04:59:08.709Z_

<details><summary>↩ Tool result · `toolu_019UsMwXpLerxsCywSwaaTZK`</summary>

```text
1	@article{deepseek2025r1,
2	  title={DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},
3	  author={{DeepSeek-AI}},
4	  journal={arXiv preprint arXiv:2501.12948},
5	  year={2025},
6	  url={https://arxiv.org/abs/2501.12948}
7	}
8	
9	@article{qwen2.5,
10	  title={Qwen2.5 Technical Report},
11	  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and others},
12	  journal={arXiv preprint arXiv:2412.15115},
13	  year={2024},
14	  url={https://arxiv.org/abs/2412.15115}
15	}
16	
17	@article{cobbe2021gsm8k,
18	  title={Training Verifiers to Solve Math Word Problems},
19	  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
20	  journal={arXiv preprint arXiv:2110.14168},
21	  year={2021},
22	  url={https://arxiv.org/abs/2110.14168}
23	}
24	
25	@article{shao2024grpo,
26	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
27	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
28	  journal={arXiv preprint arXiv:2402.03300},
29	  year={2024},
30	  url={https://arxiv.org/abs/2402.03300}
31	}
32	
33	@inproceedings{llmpruner2023,
34	  title={LLM-Pruner: On the Structural Pruning of Large Language Models},
35	  author={Ma, Xinyin and Fang, Gongfan and Wang, Xinchao},
36	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
37	  year={2023},
38	  url={https://arxiv.org/abs/2305.11627}
39	}
40	
41	@inproceedings{graspprune2026,
42	  title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models},
43	  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},
44	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
45	  year={2026},
46	  url={https://arxiv.org/abs/2604.19398}
47	}
48	
49	@article{resp2025,
50	  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},
51	  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},
52	  journal={arXiv preprint arXiv:2512.02185},
53	  year={2025},
54	  url={https://arxiv.org/abs/2512.02185}
55	}
56	
57	@article{selfhealing2025,
58	  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},
59	  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},
60	  year={2025},
61	  note={Under review},
62	  url={https://openreview.net/forum?id=Cy8Qa4gAst}
63	}
64	
65	@inproceedings{bonsai2025,
66	  title={Everybody Prune Now: Structured Pruning of LLMs with only Forward Passes},
67	  author={Kolawole, Steven and Dery, Lucio and Kagy, Jean-Fran\c{c}ois and Smith, Virginia and Neubig, Graham and Talwalkar, Ameet},
68	  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},
69	  year={2025},
70	  url={https://arxiv.org/abs/2402.05406}
71	}
72	
73	@article{paser2025,
74	  title={PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery},
75	  author={He, Bowei and Yin, Lihao and Zhen, Hui-Ling and Zhang, Xiaokun and Yuan, Mingxuan and Ma, Chen},
76	  journal={arXiv preprint arXiv:2502.12594},
77	  year={2025},
78	  url={https://arxiv.org/abs/2502.12594},
79	  note={Under review}
80	}
81	
82	@inproceedings{rlsqueezes2026,
83	  title={RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs},
84	  author={Matsutani, Kohsei and Takashiro, Shota and Minegishi, Gouki and Kojima, Takeshi and Iwasawa, Yusuke and Matsuo, Yutaka},
85	  booktitle={Proceedings of the 14th International Conference on Learning Representations (ICLR)},
86	  year={2026},
87	  url={https://arxiv.org/abs/2509.21128}
88	}
89	
90	@inproceedings{kornblith2019cka,
91	  title={Similarity of Neural Network Representations Revisited},
92	  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},
93	  booktitle={Proceedings of the 36th International Conference on Machine Learning (ICML)},
94	  year={2019},
95	  url={https://arxiv.org/abs/1905.00414}
96	}
97	
98	@article{mpruner2024,
99	  title={MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning},
100	  author={Hu, Seungbeom and Park, Chanjun and Ferraiuolo, Andrew and Ko, Sang-Ki and Kim, Jinwoo and Song, Haein and Kim, Jieung},
101	  journal={arXiv preprint arXiv:2408.13482},
102	  year={2024},
103	  url={https://arxiv.org/abs/2408.13482}
104	}
105	
106	@mastersthesis{lachance2024cka,
107	  title={Using Centered Kernel Alignment for Understanding and Pruning Neural Networks},
108	  author={Lachance, Alex},
109	  school={University of Rhode Island},
110	  year={2024},
111	  url={https://digitalcommons.uri.edu/theses/2283/}
112	}
113	
114	@inproceedings{frankle2019lth,
115	  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},
116	  author={Frankle, Jonathan and Carbin, Michael},
117	  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},
118	  year={2019},
119	  url={https://arxiv.org/abs/1803.03635}
120	}
121	
122	@inproceedings{ainslie2023gqa,
123	  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},
124	  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\'o}n, Federico and Sanghai, Sumit},
125	  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
126	  year={2023},
127	  url={https://arxiv.org/abs/2305.13245}
128	}
129	
130	@article{shortgpt2024,
131	  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},
132	  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},
133	  journal={arXiv preprint arXiv:2403.03853},
134	  year={2024},
135	  url={https://arxiv.org/abs/2403.03853}
136	}
137	
138	@inproceedings{slicegpt2024,
139	  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},
140	  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},
141	  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},
142	  year={2024},
143	  url={https://arxiv.org/abs/2401.15024}
144	}
145	
146	@inproceedings{wanda2024,
147	  title={A Simple and Effective Pruning Approach for Large Language Models},
148	  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},
149	  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},
150	  year={2024},
151	  url={https://arxiv.org/abs/2306.11695}
152	}
153	
154	@article{llms2lrms2026,
155	  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},
156	  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},
157	  journal={arXiv preprint arXiv:2601.18091},
158	  year={2026},
159	  url={https://arxiv.org/abs/2601.18091}
160	}
161	
162	@inproceedings{rac2025,
163	  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},
164	  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},
165	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
166	  year={2025},
167	  url={https://arxiv.org/abs/2509.12464}
168	}
169	
170	@article{doingmore2026,
171	  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
172	  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
173	  journal={arXiv preprint arXiv:2604.25098},
174	  year={2026},
175	  url={https://arxiv.org/abs/2604.25098}
176	}
177	
178	@inproceedings{p2law2025,
179	  title={{P\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},
180	  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},
181	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
182	  year={2025},
183	  url={https://arxiv.org/abs/2411.10272}
184	}
185	
186	@inproceedings{pat2025,
187	  title={{PAT}: Pruning-Aware Tuning for Large Language Models},
188	  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},
189	  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},
190	  year={2025},
191	  url={https://arxiv.org/abs/2408.14721}
192	}
193	
194	@article{opsd2026,
195	  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},
196	  author={Kim, Jaehoon and Lee, Dongha},
197	  journal={arXiv preprint arXiv:2605.06188},
198	  year={2026},
199	  url={https://arxiv.org/abs/2605.06188}
200	}
201	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "109390a0-3cba-46c6-93c9-5213f43367fb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
      "content": "@article{deepseek2025r1,\n  title={DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},\n  author={{DeepSeek-AI}},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025},\n  url={https://arxiv.org/abs/2501.12948}\n}\n\n@article{qwen2.5,\n  title={Qwen2.5 Technical Report},\n  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and others},\n  journal={arXiv preprint arXiv:2412.15115},\n  year={2024},\n  url={https://arxiv.org/abs/2412.15115}\n}\n\n@article{cobbe2021gsm8k,\n  title={Training Verifiers to Solve Math Word Problems},\n  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal={arXiv preprint arXiv:2110.14168},\n  year={2021},\n  url={https://arxiv.org/abs/2110.14168}\n}\n\n@article{shao2024grpo,\n  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},\n  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},\n  journal={arXiv preprint arXiv:2402.03300},\n  year={2024},\n  url={https://arxiv.org/abs/2402.03300}\n}\n\n@inproceedings{llmpruner2023,\n  title={LLM-Pruner: On the Structural Pruning of Large Language Models},\n  author={Ma, Xinyin and Fang, Gongfan and Wang, Xinchao},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.11627}\n}\n\n@inproceedings{graspprune2026,\n  title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models},\n  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},\n  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2026},\n  url={https://arxiv.org/abs/2604.19398}\n}\n\n@article{resp2025,\n  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},\n  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},\n  journal={arXiv preprint arXiv:2512.02185},\n  year={2025},\n  url={https://arxiv.org/abs/2512.02185}\n}\n\n@article{selfhealing2025,\n  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},\n  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},\n  year={2025},\n  note={Under review},\n  url={https://openreview.net/forum?id=Cy8Qa4gAst}\n}\n\n@inproceedings{bonsai2025,\n  title={Everybody Prune Now: Structured Pruning of LLMs with only Forward Passes},\n  author={Kolawole, Steven and Dery, Lucio and Kagy, Jean-Fran\\c{c}ois and Smith, Virginia and Neubig, Graham and Talwalkar, Ameet},\n  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2402.05406}\n}\n\n@article{paser2025,\n  title={PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery},\n  author={He, Bowei and Yin, Lihao and Zhen, Hui-Ling and Zhang, Xiaokun and Yuan, Mingxuan and Ma, Chen},\n  journal={arXiv preprint arXiv:2502.12594},\n  year={2025},\n  url={https://arxiv.org/abs/2502.12594},\n  note={Under review}\n}\n\n@inproceedings{rlsqueezes2026,\n  title={RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs},\n  author={Matsutani, Kohsei and Takashiro, Shota and Minegishi, Gouki and Kojima, Takeshi and Iwasawa, Yusuke and Matsuo, Yutaka},\n  booktitle={Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2509.21128}\n}\n\n@inproceedings{kornblith2019cka,\n  title={Similarity of Neural Network Representations Revisited},\n  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle={Proceedings of the 36th International Conference on Machine Learning (ICML)},\n  year={2019},\n  url={https://arxiv.org/abs/1905.00414}\n}\n\n@article{mpruner2024,\n  title={MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning},\n  author={Hu, Seungbeom and Park, Chanjun and Ferraiuolo, Andrew and Ko, Sang-Ki and Kim, Jinwoo and Song, Haein and Kim, Jieung},\n  journal={arXiv preprint arXiv:2408.13482},\n  year={2024},\n  url={https://arxiv.org/abs/2408.13482}\n}\n\n@mastersthesis{lachance2024cka,\n  title={Using Centered Kernel Alignment for Understanding and Pruning Neural Networks},\n  author={Lachance, Alex},\n  school={University of Rhode Island},\n  year={2024},\n  url={https://digitalcommons.uri.edu/theses/2283/}\n}\n\n@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carbin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}\n\n@inproceedings{ainslie2023gqa,\n  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},\n  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\\'o}n, Federico and Sanghai, Sumit},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.13245}\n}\n\n@article{shortgpt2024,\n  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},\n  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},\n  journal={arXiv preprint arXiv:2403.03853},\n  year={2024},\n  url={https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{slicegpt2024,\n  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},\n  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2401.15024}\n}\n\n@inproceedings{wanda2024,\n  title={A Simple and Effective Pruning Approach for Large Language Models},\n  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2306.11695}\n}\n\n@article{llms2lrms2026,\n  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},\n  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},\n  journal={arXiv preprint arXiv:2601.18091},\n  year={2026},\n  url={https://arxiv.org/abs/2601.18091}\n}\n\n@inproceedings{rac2025,\n  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},\n  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  url={https://arxiv.org/abs/2509.12464}\n}\n\n@article{doingmore2026,\n  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n  journal={arXiv preprint arXiv:2604.25098},\n  year={2026},\n  url={https://arxiv.org/abs/2604.25098}\n}\n\n@inproceedings{p2law2025,\n  title={{P\\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},\n  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2025},\n  url={https://arxiv.org/abs/2411.10272}\n}\n\n@inproceedings{pat2025,\n  title={{PAT}: Pruning-Aware Tuning for Large Language Models},\n  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},\n  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  url={https://arxiv.org/abs/2408.14721}\n}\n\n@article{opsd2026,\n  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},\n  author={Kim, Jaehoon and Lee, Dongha},\n  journal={arXiv preprint arXiv:2605.06188},\n  year={2026},\n  url={https://arxiv.org/abs/2605.06188}\n}\n",
      "numLines": 201,
      "startLine": 1,
      "totalLines": 201
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01PxP18SnDb7aEEfkbVqaBEb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "8c437394-54e9-4257-b9d2-8d3187d85ba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fqexs1nf7oaqAwMbEiQ2AH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11453,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11453
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

_source line 10 · 2026-05-15T04:59:09.260Z_

<details><summary>↩ Tool result · `toolu_01PxP18SnDb7aEEfkbVqaBEb`</summary>

```text
1	\section{Method: Recovery-Aware Structured Pruning}
2	\label{sec:method}
3	
4	We propose \textbf{Recovery-Aware Structured Pruning (\rasp{})}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.
5	The core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\citep{rlsqueezes2026}.
6	
7	\subsection{Preliminaries and Notation}
8	\label{sec:prelim}
9	
10	\paragraph{Structured pruning.}
11	Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.
12	We denote the set of prunable structures as $\mathcal{H} = \{h_1, h_2, \ldots, h_N\}$.
13	
14	\paragraph{Grouped Query Attention (GQA).}
15	In GQA architectures~\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.
16	For DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.
17	We treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.
18	
19	\paragraph{RLVR and GRPO.}
20	Reinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.
21	We use Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) as the recovery algorithm, following~\citet{selfhealing2025}.
22	
23	\subsection{Stage 1: Reasoning-Trace Structural Analysis}
24	\label{sec:stage1}
25	
26	\rasp{} computes two complementary scores per structure: \emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \emph{functional overlap} $F(h)$ measuring the degree to which its function is recoverable from other structures.
27	
28	\paragraph{Self-calibrated reasoning traces.}
29	Following~\citet{resp2025}, we generate chain-of-thought reasoning traces from the model's own distribution rather than using external calibration data.
30	Given a calibration set of reasoning problems $\mathcal{D}_\text{cal}$, we sample traces $\{(x_j, \hat{y}_j)\}_{j=1}^{M}$ where $\hat{y}_j \sim p_\mathcal{M}(\cdot \mid x_j)$.
31	This ensures importance scores reflect the model's actual reasoning pathways.
32	
33	\paragraph{Structural importance.}
34	For each structure $h$, we compute importance $I(h)$ via first-order Taylor expansion on the reasoning trace loss:
35	\begin{equation}
36	    I(h) = \left| \sum_{(x,\hat{y}) \in \mathcal{D}_\text{cal}} \mathbf{a}_h(x, \hat{y})^\top \frac{\partial \mathcal{L}(x, \hat{y})}{\partial \mathbf{a}_h} \right|,
37	    \label{eq:importance}
38	\end{equation}
39	where $\mathbf{a}_h$ denotes the activation of structure $h$ and $\mathcal{L}$ is the language modeling loss over the reasoning trace.
40	For a GQA group $g$ containing Q heads $\{q_1, \ldots, q_G\}$ and KV head $k$, we aggregate: $I(g) = \sum_{i=1}^{G} I(q_i) + I(k)$.
41	
42	\paragraph{Functional overlap via CKA.}
43	We measure functional overlap using linear Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to invertible linear transformations.
44	Given activation matrices $\mathbf{X}, \mathbf{Y} \in \mathbb{R}^{n \times d}$ collected over $n$ calibration examples, linear CKA is:
45	\begin{equation}
46	    \text{CKA}(\mathbf{X}, \mathbf{Y}) = \frac{\text{HSIC}(\mathbf{X}, \mathbf{Y})}{\sqrt{\text{HSIC}(\mathbf{X}, \mathbf{X}) \cdot \text{HSIC}(\mathbf{Y}, \mathbf{Y})}},
47	    \label{eq:cka}
48	\end{equation}
49	where $\text{HSIC}(\mathbf{X}, \mathbf{Y}) = \frac{1}{(n-1)^2} \operatorname{tr}(\mathbf{K} \mathbf{H} \mathbf{L} \mathbf{H})$, with $\mathbf{K} = \mathbf{X}\mathbf{X}^\top$, $\mathbf{L} = \mathbf{Y}\mathbf{Y}^\top$, and $\mathbf{H} = \mathbf{I}_n - \frac{1}{n}\mathbf{1}\mathbf{1}^\top$.
50	
51	For a GQA group $g_i$ in layer $\ell$, we form its representation by concatenating its constituent Q head activations: $\mathbf{X}_{g_i} = [\mathbf{a}_{q_1}; \ldots; \mathbf{a}_{q_G}] \in \mathbb{R}^{n \times Gd_h}$.
52	The functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:
53	\begin{equation}
54	    F(g_i) = \frac{1}{|\mathcal{G}_\ell| - 1} \sum_{\substack{g_j \in \mathcal{G}_\ell \\ j \neq i}} \text{CKA}(\mathbf{X}_{g_i}, \mathbf{X}_{g_j}),
55	    \label{eq:overlap}
56	\end{equation}
57	where $\mathcal{G}_\ell$ is the set of GQA groups in layer $\ell$.
58	Unlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\citep{mpruner2024,lachance2024cka}, \rasp{} uses \emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.
59	
60	\subsection{Stage 2: Recovery-Aware Scoring}
61	\label{sec:stage2}
62	
63	The recovery-aware score combines importance and functional overlap:
64	\begin{equation}
65	    S(h) = I(h) \times \big(1 - F(h)\big)^\alpha,
66	    \label{eq:score}
67	\end{equation}
68	where $\alpha > 0$ controls the strength of the recoverability penalty.
69	Structures with the lowest $S(h)$ are pruned up to the target sparsity ratio.
70	
71	The scoring captures three regimes:
72	\begin{itemize}[nosep,leftmargin=*]
73	    \item \textbf{High $I$, low $F$} (irreplaceable scaffolding): No other structure can assume its function. High $S$ $\rightarrow$ \emph{protected}.
74	    \item \textbf{High $I$, high $F$} (redundant but important): RLVR can redistribute its function via global exploration. Low $S$ $\rightarrow$ \emph{pruned preferentially}.
75	    \item \textbf{Low $I$} (unimportant): Pruned regardless of overlap.
76	\end{itemize}
77	
78	The key distinction from standard pruning---which ranks solely by $I(h)$---is that \rasp{} additionally down-weights protection of structures whose function overlaps with retained structures.
79	This is motivated by the finding that RLVR recovers through global exploration and path compression~\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.
80	
81	\paragraph{Per-layer capacity floor.}
82	Global ranking by $S(h)$ can concentrate pruning in layers where many structures have high overlap, collapsing that layer's representational capacity.
83	To prevent this, we enforce a per-layer capacity floor: each layer must retain at least 40\% of its MLP channel groups after pruning.
84	For DeepSeek-R1-Distill-Qwen-7B, this requires ${\ge}12$ of 28 MLP groups per layer.
85	During structure selection, if removing a candidate would violate this constraint, it is skipped in favor of the next lowest-scoring structure.
86	This constraint adds negligible overhead to the scoring procedure but prevents representational collapse in individual layers---a failure mode we observed when unconstrained global ranking was applied at 20\% sparsity.
87	
88	Attention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions subject to the per-layer floor.
89	Algorithm~\ref{alg:rasp} summarizes the complete pipeline.
90	
91	\subsection{Stage 3: Two-Stage Recovery}
92	\label{sec:stage3}
93	
94	After pruning, we recover reasoning ability through two stages: supervised finetuning (SFT) warmup followed by GRPO-based RLVR.
95	
96	\paragraph{Motivation for two-stage recovery.}
97	Directly applying GRPO to a pruned model fails.
98	Structured pruning disrupts the model's ability to generate end-of-sequence (EOS) tokens: in sampling mode, pruned models produce repetitive digit loops without termination, yielding sequences that are truncated at the maximum length.
99	Since GRPO computes rewards only from completed generations, this EOS collapse means no valid completions are produced, the clipped ratio reaches 1.0, and gradient norms drop to zero---making direct RLVR recovery impossible.
100	
101	\paragraph{Stage 3a: SFT warmup.}
102	We first apply a short SFT phase on reasoning demonstrations to restore two capabilities destroyed by pruning: (1) EOS token generation, ensuring the model can terminate sequences, and (2) basic format compliance, so that outputs follow the expected answer extraction pattern.
103	SFT warmup uses teacher-forced training on chain-of-thought traces, which does not require the model to produce complete generations and thus bypasses the EOS collapse problem.
104	This stage is intentionally brief---its purpose is to restore the minimal generation competence needed for GRPO, not to recover full reasoning ability.
105	
106	\paragraph{Stage 3b: GRPO recovery.}
107	With generation competence restored, we apply GRPO-based RLVR on mathematical reasoning data to recover the pruned model's reasoning ability.
108	The reward is binary: $r = 1$ if the model's final answer matches the ground truth, $r = 0$ otherwise.
109	RLVR is preferred over extended SFT for reasoning recovery because of their fundamentally different training dynamics: \citet{rlsqueezes2026} show that RLVR \emph{compresses} incorrect reasoning trajectories while SFT \emph{expands} correct ones.
110	For a pruned model, RLVR can globally explore and redistribute functionality across remaining structures, while SFT is limited to imitating fixed trajectories through a reduced architecture.
111	Structures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for \rasp{}'s scoring criterion.
112	
113	\begin{algorithm}[t]
114	\caption{Recovery-Aware Structured Pruning (\rasp{})}
115	\label{alg:rasp}
116	\begin{algorithmic}[1]
117	\Require Model $\mathcal{M}$, calibration problems $\mathcal{D}_\text{cal}$, target sparsity $s$, overlap weight $\alpha$, SFT data $\mathcal{D}_\text{sft}$, RLVR data $\mathcal{D}_\text{rlvr}$, layer floor $\tau$
118	\Ensure Pruned and recovered model $\mathcal{M}'$
119	\Statex \textit{\% Stage 1: Reasoning-Trace Structural Analysis}
120	\State Sample traces $\{(x_j, \hat{y}_j)\} \sim p_\mathcal{M}(\cdot \mid \mathcal{D}_\text{cal})$
121	\For{each structure $h \in \mathcal{H}$}
122	    \State Compute $I(h)$ via Eq.~\eqref{eq:importance}
123	    \State Collect activations $\mathbf{X}_h$
124	\EndFor
125	\For{each layer $\ell = 1, \ldots, L$}
126	    \For{each group $g_i \in \mathcal{G}_\ell$}
127	        \State $F(g_i) \gets \frac{1}{|\mathcal{G}_\ell|-1} \sum_{j \neq i} \text{CKA}(\mathbf{X}_{g_i}, \mathbf{X}_{g_j})$
128	    \EndFor
129	\EndFor
130	\Statex \textit{\% Stage 2: Recovery-Aware Scoring}
131	\For{each structure $h \in \mathcal{H}$}
132	    \State $S(h) \gets I(h) \times (1 - F(h))^\alpha$
133	\EndFor
134	\State Sort $\mathcal{H}$ by $S(h)$ ascending
135	\State $\mathcal{P} \gets \emptyset$
136	\For{each $h$ in sorted $\mathcal{H}$}
137	    \If{layer($h$) retains $< \tau$ fraction after adding $h$ to $\mathcal{P}$}
138	        \State \textbf{continue}
139	    \EndIf
140	    \State $\mathcal{P} \gets \mathcal{P} \cup \{h\}$
141	    \If{$\sum_{h' \in \mathcal{P}} \text{params}(h') \ge s \cdot |\theta|$}
142	        \State \textbf{break}
143	    \EndIf
144	\EndFor
145	\State $\mathcal{M}_\text{pruned} \gets \text{Remove}(\mathcal{M}, \mathcal{P})$
146	\Statex \textit{\% Stage 3: Two-Stage Recovery}
147	\State $\mathcal{M}_\text{warm} \gets \text{SFT}(\mathcal{M}_\text{pruned}, \mathcal{D}_\text{sft})$ \hfill $\triangleright$ restore EOS \& format
148	\State $\mathcal{M}' \gets \text{GRPO}(\mathcal{M}_\text{warm}, \mathcal{D}_\text{rlvr})$ \hfill $\triangleright$ restore reasoning
149	\State \Return $\mathcal{M}'$
150	\end{algorithmic}
151	\end{algorithm}
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "4d86f043-c4e1-498f-8177-22323c5b6dd7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex",
      "content": "\\section{Method: Recovery-Aware Structured Pruning}\n\\label{sec:method}\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.\nThe core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\\citep{rlsqueezes2026}.\n\n\\subsection{Preliminaries and Notation}\n\\label{sec:prelim}\n\n\\paragraph{Structured pruning.}\nGiven a pretrained transformer $\\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.\nWe denote the set of prunable structures as $\\mathcal{H} = \\{h_1, h_2, \\ldots, h_N\\}$.\n\n\\paragraph{Grouped Query Attention (GQA).}\nIn GQA architectures~\\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.\nFor DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.\nWe treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.\n\n\\paragraph{RLVR and GRPO.}\nReinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.\nWe use Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) as the recovery algorithm, following~\\citet{selfhealing2025}.\n\n\\subsection{Stage 1: Reasoning-Trace Structural Analysis}\n\\label{sec:stage1}\n\n\\rasp{} computes two complementary scores per structure: \\emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \\emph{functional overlap} $F(h)$ measuring the degree to which its function is recoverable from other structures.\n\n\\paragraph{Self-calibrated reasoning traces.}\nFollowing~\\citet{resp2025}, we generate chain-of-thought reasoning traces from the model's own distribution rather than using external calibration data.\nGiven a calibration set of reasoning problems $\\mathcal{D}_\\text{cal}$, we sample traces $\\{(x_j, \\hat{y}_j)\\}_{j=1}^{M}$ where $\\hat{y}_j \\sim p_\\mathcal{M}(\\cdot \\mid x_j)$.\nThis ensures importance scores reflect the model's actual reasoning pathways.\n\n\\paragraph{Structural importance.}\nFor each structure $h$, we compute importance $I(h)$ via first-order Taylor expansion on the reasoning trace loss:\n\\begin{equation}\n    I(h) = \\left| \\sum_{(x,\\hat{y}) \\in \\mathcal{D}_\\text{cal}} \\mathbf{a}_h(x, \\hat{y})^\\top \\frac{\\partial \\mathcal{L}(x, \\hat{y})}{\\partial \\mathbf{a}_h} \\right|,\n    \\label{eq:importance}\n\\end{equation}\nwhere $\\mathbf{a}_h$ denotes the activation of structure $h$ and $\\mathcal{L}$ is the language modeling loss over the reasoning trace.\nFor a GQA group $g$ containing Q heads $\\{q_1, \\ldots, q_G\\}$ and KV head $k$, we aggregate: $I(g) = \\sum_{i=1}^{G} I(q_i) + I(k)$.\n\n\\paragraph{Functional overlap via CKA.}\nWe measure functional overlap using linear Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to invertible linear transformations.\nGiven activation matrices $\\mathbf{X}, \\mathbf{Y} \\in \\mathbb{R}^{n \\times d}$ collected over $n$ calibration examples, linear CKA is:\n\\begin{equation}\n    \\text{CKA}(\\mathbf{X}, \\mathbf{Y}) = \\frac{\\text{HSIC}(\\mathbf{X}, \\mathbf{Y})}{\\sqrt{\\text{HSIC}(\\mathbf{X}, \\mathbf{X}) \\cdot \\text{HSIC}(\\mathbf{Y}, \\mathbf{Y})}},\n    \\label{eq:cka}\n\\end{equation}\nwhere $\\text{HSIC}(\\mathbf{X}, \\mathbf{Y}) = \\frac{1}{(n-1)^2} \\operatorname{tr}(\\mathbf{K} \\mathbf{H} \\mathbf{L} \\mathbf{H})$, with $\\mathbf{K} = \\mathbf{X}\\mathbf{X}^\\top$, $\\mathbf{L} = \\mathbf{Y}\\mathbf{Y}^\\top$, and $\\mathbf{H} = \\mathbf{I}_n - \\frac{1}{n}\\mathbf{1}\\mathbf{1}^\\top$.\n\nFor a GQA group $g_i$ in layer $\\ell$, we form its representation by concatenating its constituent Q head activations: $\\mathbf{X}_{g_i} = [\\mathbf{a}_{q_1}; \\ldots; \\mathbf{a}_{q_G}] \\in \\mathbb{R}^{n \\times Gd_h}$.\nThe functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:\n\\begin{equation}\n    F(g_i) = \\frac{1}{|\\mathcal{G}_\\ell| - 1} \\sum_{\\substack{g_j \\in \\mathcal{G}_\\ell \\\\ j \\neq i}} \\text{CKA}(\\mathbf{X}_{g_i}, \\mathbf{X}_{g_j}),\n    \\label{eq:overlap}\n\\end{equation}\nwhere $\\mathcal{G}_\\ell$ is the set of GQA groups in layer $\\ell$.\nUnlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.\n\n\\subsection{Stage 2: Recovery-Aware Scoring}\n\\label{sec:stage2}\n\nThe recovery-aware score combines importance and functional overlap:\n\\begin{equation}\n    S(h) = I(h) \\times \\big(1 - F(h)\\big)^\\alpha,\n    \\label{eq:score}\n\\end{equation}\nwhere $\\alpha > 0$ controls the strength of the recoverability penalty.\nStructures with the lowest $S(h)$ are pruned up to the target sparsity ratio.\n\nThe scoring captures three regimes:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High $I$, low $F$} (irreplaceable scaffolding): No other structure can assume its function. High $S$ $\\rightarrow$ \\emph{protected}.\n    \\item \\textbf{High $I$, high $F$} (redundant but important): RLVR can redistribute its function via global exploration. Low $S$ $\\rightarrow$ \\emph{pruned preferentially}.\n    \\item \\textbf{Low $I$} (unimportant): Pruned regardless of overlap.\n\\end{itemize}\n\nThe key distinction from standard pruning---which ranks solely by $I(h)$---is that \\rasp{} additionally down-weights protection of structures whose function overlaps with retained structures.\nThis is motivated by the finding that RLVR recovers through global exploration and path compression~\\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.\n\n\\paragraph{Per-layer capacity floor.}\nGlobal ranking by $S(h)$ can concentrate pruning in layers where many structures have high overlap, collapsing that layer's representational capacity.\nTo prevent this, we enforce a per-layer capacity floor: each layer must retain at least 40\\% of its MLP channel groups after pruning.\nFor DeepSeek-R1-Distill-Qwen-7B, this requires ${\\ge}12$ of 28 MLP groups per layer.\nDuring structure selection, if removing a candidate would violate this constraint, it is skipped in favor of the next lowest-scoring structure.\nThis constraint adds negligible overhead to the scoring procedure but prevents representational collapse in individual layers---a failure mode we observed when unconstrained global ranking was applied at 20\\% sparsity.\n\nAttention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions subject to the per-layer floor.\nAlgorithm~\\ref{alg:rasp} summarizes the complete pipeline.\n\n\\subsection{Stage 3: Two-Stage Recovery}\n\\label{sec:stage3}\n\nAfter pruning, we recover reasoning ability through two stages: supervised finetuning (SFT) warmup followed by GRPO-based RLVR.\n\n\\paragraph{Motivation for two-stage recovery.}\nDirectly applying GRPO to a pruned model fails.\nStructured pruning disrupts the model's ability to generate end-of-sequence (EOS) tokens: in sampling mode, pruned models produce repetitive digit loops without termination, yielding sequences that are truncated at the maximum length.\nSince GRPO computes rewards only from completed generations, this EOS collapse means no valid completions are produced, the clipped ratio reaches 1.0, and gradient norms drop to zero---making direct RLVR recovery impossible.\n\n\\paragraph{Stage 3a: SFT warmup.}\nWe first apply a short SFT phase on reasoning demonstrations to restore two capabilities destroyed by pruning: (1) EOS token generation, ensuring the model can terminate sequences, and (2) basic format compliance, so that outputs follow the expected answer extraction pattern.\nSFT warmup uses teacher-forced training on chain-of-thought traces, which does not require the model to produce complete generations and thus bypasses the EOS collapse problem.\nThis stage is intentionally brief---its purpose is to restore the minimal generation competence needed for GRPO, not to recover full reasoning ability.\n\n\\paragraph{Stage 3b: GRPO recovery.}\nWith generation competence restored, we apply GRPO-based RLVR on mathematical reasoning data to recover the pruned model's reasoning ability.\nThe reward is binary: $r = 1$ if the model's final answer matches the ground truth, $r = 0$ otherwise.\nRLVR is preferred over extended SFT for reasoning recovery because of their fundamentally different training dynamics: \\citet{rlsqueezes2026} show that RLVR \\emph{compresses} incorrect reasoning trajectories while SFT \\emph{expands} correct ones.\nFor a pruned model, RLVR can globally explore and redistribute functionality across remaining structures, while SFT is limited to imitating fixed trajectories through a reduced architecture.\nStructures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for \\rasp{}'s scoring criterion.\n\n\\begin{algorithm}[t]\n\\caption{Recovery-Aware Structured Pruning (\\rasp{})}\n\\label{alg:rasp}\n\\begin{algorithmic}[1]\n\\Require Model $\\mathcal{M}$, calibration problems $\\mathcal{D}_\\text{cal}$, target sparsity $s$, overlap weight $\\alpha$, SFT data $\\mathcal{D}_\\text{sft}$, RLVR data $\\mathcal{D}_\\text{rlvr}$, layer floor $\\tau$\n\\Ensure Pruned and recovered model $\\mathcal{M}'$\n\\Statex \\textit{\\% Stage 1: Reasoning-Trace Structural Analysis}\n\\State Sample traces $\\{(x_j, \\hat{y}_j)\\} \\sim p_\\mathcal{M}(\\cdot \\mid \\mathcal{D}_\\text{cal})$\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State Compute $I(h)$ via Eq.~\\eqref{eq:importance}\n    \\State Collect activations $\\mathbf{X}_h$\n\\EndFor\n\\For{each layer $\\ell = 1, \\ldots, L$}\n    \\For{each group $g_i \\in \\mathcal{G}_\\ell$}\n        \\State $F(g_i) \\gets \\frac{1}{|\\mathcal{G}_\\ell|-1} \\sum_{j \\neq i} \\text{CKA}(\\mathbf{X}_{g_i}, \\mathbf{X}_{g_j})$\n    \\EndFor\n\\EndFor\n\\Statex \\textit{\\% Stage 2: Recovery-Aware Scoring}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State $S(h) \\gets I(h) \\times (1 - F(h))^\\alpha$\n\\EndFor\n\\State Sort $\\mathcal{H}$ by $S(h)$ ascending\n\\State $\\mathcal{P} \\gets \\emptyset$\n\\For{each $h$ in sorted $\\mathcal{H}$}\n    \\If{layer($h$) retains $< \\tau$ fraction after adding $h$ to $\\mathcal{P}$}\n        \\State \\textbf{continue}\n    \\EndIf\n    \\State $\\mathcal{P} \\gets \\mathcal{P} \\cup \\{h\\}$\n    \\If{$\\sum_{h' \\in \\mathcal{P}} \\text{params}(h') \\ge s \\cdot |\\theta|$}\n        \\State \\textbf{break}\n    \\EndIf\n\\EndFor\n\\State $\\mathcal{M}_\\text{pruned} \\gets \\text{Remove}(\\mathcal{M}, \\mathcal{P})$\n\\Statex \\textit{\\% Stage 3: Two-Stage Recovery}\n\\State $\\mathcal{M}_\\text{warm} \\gets \\text{SFT}(\\mathcal{M}_\\text{pruned}, \\mathcal{D}_\\text{sft})$ \\hfill $\\triangleright$ restore EOS \\& format\n\\State $\\mathcal{M}' \\gets \\text{GRPO}(\\mathcal{M}_\\text{warm}, \\mathcal{D}_\\text{rlvr})$ \\hfill $\\triangleright$ restore reasoning\n\\State \\Return $\\mathcal{M}'$\n\\end{algorithmic}\n\\end{algorithm}\n",
      "numLines": 152,
      "startLine": 1,
      "totalLines": 152
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01AiQptgXkkqrahPm5Wn1sH8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/_project/paper/figure_plan.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "3467a2ab-f8be-4e9c-a8f8-a9a12434de72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fqexs1nf7oaqAwMbEiQ2AH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11453,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11453
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

_source line 12 · 2026-05-15T04:59:09.471Z_

<details><summary>↩ Tool result · `toolu_01AiQptgXkkqrahPm5Wn1sH8`</summary>

````text
1	# Figure Plan — Recovery-Aware Structured Pruning (RASP)
2	
3	---
4	
5	## Fig 1: RASP Pipeline Overview
6	
7	**类型**: 流程/架构图（method figure）
8	
9	**内容**:
10	```
11	Pre-trained Reasoning LLM (DeepSeek-R1-Distill-Qwen-7B)
12	        │
13	        ├──────────────────────────┐
14	        ▼                          ▼
15	  Importance I(h)           CKA Overlap F(h)
16	  (Taylor gradient)        (intra-layer pairwise)
17	        │                          │
18	        └──────────┬───────────────┘
19	                   ▼
20	        RASP Score: S(h) = I(h) × (1 - F(h))^α
21	                   │
22	                   ▼
23	        Structured Pruning (remove lowest S(h))
24	                   │
25	                   ▼
26	        ┌──────────┴──────────┐
27	        ▼                     ▼
28	  SFT Warmup              [对比: Standard Pruning]
29	  (fix generation)         只用 I(h), 无 F(h) 修正
30	        │
31	        ▼
32	  GRPO RLVR Recovery
33	  (restore reasoning)
34	        │
35	        ▼
36	  Recovered Compact Model
37	```
38	
39	**关键设计要素**:
40	- 左侧主 pipeline 用蓝色系，右侧 Standard 对比用灰色/红色
41	- I(h) 和 F(h) 分支用不同颜色区分（如蓝 vs 橙），在合并处突出 RASP scoring 公式
42	- Standard pruning 旁路用虚线表示，标注 "importance-only"
43	- Recovery 阶段标注 "SFT Warmup → GRPO" 两步
44	- 在 CKA Overlap 框旁加小示意：同层 head 间 pairwise CKA matrix
45	
46	**数据可用性**: 无需实验数据，纯方法示意图
47	
48	**建议工具**: TikZ（最佳）或 matplotlib + patches + FancyArrowPatch
49	
50	**论文位置**: Section 3 (Method) 开头，首次引用
51	
52	**尺寸**: 双栏宽度（full width），高度约 6-8cm
53	
54	---
55	
56	## Fig 2: CKA Overlap vs Recoverability Scatter Plot
57	
58	**类型**: 散点图
59	
60	**内容**:
61	- **X 轴**: F(g) — per-structure CKA functional overlap（pruned structure 与其最相似 retained structure 的 CKA）
62	- **Y 轴**: Recoverability — retained structure 在 pruned model vs GRPO-recovered model 之间的 activation shift（1 - cosine similarity）
63	- 每个点 = 一个被剪掉的 structure（attention GQA group 或 MLP channel group）
64	- 按 structure type 着色：蓝色 = attention，橙色 = MLP
65	- 或按 layer index 着色（viridis colormap）+ colorbar
66	- 回归线 + Spearman ρ 及 95% CI 标注在图上
67	- 标注 2-3 个典型点（如 "Layer 2 attn: low F(h), low recovery" vs "Layer 25 attn: high F(h), high recovery"）
68	
69	**数据来源**:
70	- `correlation_analysis.py` 输出 `correlation_results.json`
71	- 需要：base model, pruned model (RASP 20%), GRPO-recovered model, `cka_scores.pt`, `pruning_metadata.pt`
72	- 服务器路径: `/root/autodl-tmp/recovery_aware_struct_prune/` 下的对应 checkpoint
73	
74	**数据可用性**: **待 correlation_analysis.py 执行**。代码已写好（`artifacts/correlation_analysis.py`），需 GRPO stage 2 checkpoint 完成后运行。GRPO v2 状态: DONE（`grpo_stage2_rasp_20_DONE_20260515`）
75	
76	**关键设计要素**:
77	- 颜色方案：attention (#1f77b4) vs MLP (#ff7f0e)，与 `correlation_analysis.py` 一致
78	- 点大小 30，alpha 0.7，黑色细边框
79	- 右下角文本框：ρ = X.XX, 95% CI [X.XX, X.XX], p < 0.001
80	- 如果 attention 和 MLP 趋势不同，可考虑分面（两个子图）
81	- 灰色虚线标注 "Recoverable zone" 阈值
82	
83	**建议工具**: matplotlib（已有 `make_scatter_plot` 函数，需微调为论文质量）
84	
85	**论文位置**: Section 5.3 (Claim 2: F(h) predicts recoverability)
86	
87	**尺寸**: 单栏宽度，约 8cm × 6cm
88	
89	---
90	
91	## Fig 3: RLVR vs SFT Recovery Trajectory
92	
93	**类型**: 折线图
94	
95	**内容**:
96	- **X 轴**: Training steps
97	- **Y 轴**: GSM8K accuracy (%) 或 reward mean
98	- **4 条线**:
99	  1. RASP + SFT → GRPO（蓝色实线，主角）
100	  2. Standard + SFT → GRPO（红色实线）
101	  3. RASP + SFT only（蓝色虚线）
102	  4. Standard + SFT only（红色虚线）
103	- 分两阶段：SFT warmup（左半）→ GRPO recovery（右半），用竖线分隔
104	- **关键标注**:
105	  - "Reward Desert" 区域：Standard + GRPO 在某步数后 reward 停滞的区间（灰色阴影）
106	  - RASP + GRPO 的持续上升趋势
107	  - 水平虚线标注 baseline accuracy (82.6%)
108	  - 各条线终点标注最终准确率
109	
110	**数据来源**:
111	- wandb runs: SFT training logs (train loss / eval accuracy per step)
112	- wandb runs: GRPO v2 training logs (reward_mean, gsm8k_accuracy per step)
113	- 4 个 run：`sft_rasp_20`, `sft_standard_20`, `grpo_stage2_rasp_20`, `grpo_stage2_standard_20`
114	
115	**数据可用性**: **部分已有**。SFT runs 已完成。GRPO stage 2 runs 已完成（DONE status）。需从 wandb 提取 step-level metrics。
116	
117	**关键设计要素**:
118	- 颜色方案：RASP = 蓝色系 (#1f77b4)，Standard = 红色系 (#d62728)；实线 = +GRPO，虚线 = SFT only
119	- X 轴两段拼接：SFT steps (0 → SFT_end) | GRPO steps (0 → 2000)，中间竖虚线分隔标注 "SFT → GRPO"
120	- 水平灰色虚线标 baseline 82.6%
121	- "Reward Desert" 灰色阴影区（Standard GRPO 停滞区间）
122	- 图例放右下角，避免遮挡曲线
123	
124	**建议工具**: matplotlib
125	
126	**论文位置**: Section 5.4 (Claim 3: Recovery method conditions optimal pruning)
127	
128	**尺寸**: 双栏宽度或 1.5 栏宽度，高度约 5-6cm
129	
130	---
131	
132	## Fig 4: α Ablation 曲线（可选）
133	
134	**类型**: 折线图 + 误差棒
135	
136	**内容**:
137	- **X 轴**: α 值 {0, 0.5, 1.0, 2.0, 4.0}
138	- **Y 轴**: Post-prune GSM8K accuracy (%)
139	- 单条线 + 95% CI 误差棒
140	- α=0 等价于 Standard pruning（标注）
141	- α=1.0 为当前默认值（用星号或不同 marker 高亮）
142	- 可选第二条线：post-recovery accuracy（如果有对应 GRPO 数据）
143	
144	**数据来源**:
145	- `src/run_alpha_ablation.sh` 输出
146	- α=1.0 已有结果（24.3% post-prune on full eval）
147	- 其他 α 值待运行
148	
149	**数据可用性**: **待 α ablation 实验执行**。代码和脚本已准备好（`src/run_alpha_ablation.sh`）。α=1.0 可复用。磁盘空间约束需顺序执行（每个 α prune → eval → 删除 → 下一个）。
150	
151	**关键设计要素**:
152	- X 轴用 log scale 或等距排列（0 作为特殊点）
153	- α=0 标注 "= Standard"
154	- α=1.0 用 ★ marker
155	- 如果存在最优点，用箭头标注
156	- 灰色水平虚线标 baseline
157	
158	**建议工具**: matplotlib
159	
160	**论文位置**: Section 5.5 (Ablation Studies)
161	
162	**尺寸**: 单栏宽度，约 7cm × 5cm
163	
164	---
165	
166	## Fig 5: Per-layer Pruning Distribution（可选）
167	
168	**类型**: 分组柱状图（grouped bar chart）
169	
170	**内容**:
171	- **X 轴**: Layer index (0-27)
172	- **Y 轴**: 该层被剪掉的 structure 数量（或剪枝比例 %）
173	- **两组柱**: Standard (红) vs RASP (蓝)
174	- 可分为上下两个子图：attention heads (上) + MLP groups (下)
175	- 突出关键差异：RASP 在哪些层保留更多、在哪些层剪掉更多
176	
177	**数据来源**:
178	- `pruning_metadata.pt` 中的 `attn_keep_masks` 和 `mlp_keep_masks`
179	- 需要 Standard 和 RASP 两个版本的 pruning metadata
180	- 服务器路径: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20/` 和 `pruned_standard_20/`
181	
182	**数据可用性**: **已有**。两个 pruned model 目录中各有 `pruning_metadata.pt`。
183	
184	**关键设计要素**:
185	- 柱宽窄（28 层 × 2 组），用颜色区分 Standard vs RASP
186	- 标注差异最大的层（如 "Layer 5: RASP 保留全部 4 GQA groups，Standard 只保留 2"）
187	- 上方标注总剪枝预算相同（matched parameter count）
188	- 考虑用热力图替代（层 × method，颜色深浅 = 剪枝比例），更紧凑
189	
190	**建议工具**: matplotlib
191	
192	**论文位置**: Section 5.2 (Analysis) 或 Appendix
193	
194	**尺寸**: 双栏宽度（如果柱状图）或单栏（如果热力图）
195	
196	---
197	
198	## Fig 6: CKA Overlap Heatmap（可选）
199	
200	**类型**: 热力图
201	
202	**内容**:
203	- 展示某代表层（如 Layer 12）的 attention head/GQA group 间 pairwise CKA overlap matrix
204	- 或展示所有 28 层的 per-head mean overlap 作为 1D heatmap
205	- 对角线为 1.0，颜色从浅（低 overlap）到深（高 overlap）
206	- 标注高 overlap 区域 = "redundant but recoverable" 和低 overlap 区域 = "unique, must preserve"
207	
208	**数据来源**:
209	- `results/cka_scores.pt`
210	- 包含 `attn_cka_matrix` (per-layer pairwise CKA) 和 `attn_overlap` (per-head mean overlap)
211	
212	**数据可用性**: **已有**。`cka_scores.pt` (122KB) 已缓存在服务器。
213	
214	**关键设计要素**:
215	- 颜色方案：`coolwarm` 或 `YlOrRd`（学术标准）
216	- 如果展示单层 pairwise matrix：4×4 (GQA groups) 或更大
217	- 如果展示全层 summary：28 行 × N 列热力图
218	- 对角线标为灰色（self-overlap = 1.0，不 informative）
219	- 叠加 RASP 剪枝决策标记（✓ 保留 / ✗ 移除）
220	
221	**建议工具**: matplotlib + seaborn.heatmap
222	
223	**论文位置**: Section 4 (CKA-based Functional Overlap) 或 Appendix
224	
225	**尺寸**: 单栏宽度
226	
227	---
228	
229	## 汇总
230	
231	| 图号 | 标题 | 类型 | 数据状态 | 位置 | 宽度 |
232	|------|------|------|----------|------|------|
233	| Fig 1 | RASP Pipeline Overview | 流程图 | 无需数据 | §3 Method | 双栏 |
234	| Fig 2 | CKA Overlap vs Recoverability | 散点图 | 待 correlation_analysis 运行 | §5.3 Claim 2 | 单栏 |
235	| Fig 3 | Recovery Trajectory | 折线图 | 待 wandb 数据提取 | §5.4 Claim 3 | 双栏 |
236	| Fig 4 | α Ablation | 折线图 | 待 ablation 实验 | §5.5 Ablation | 单栏 |
237	| Fig 5 | Per-layer Pruning Distribution | 柱状图/热力图 | ✅ 已有 | §5.2 / Appendix | 双栏 |
238	| Fig 6 | CKA Overlap Heatmap | 热力图 | ✅ 已有 | §4 / Appendix | 单栏 |
239	
240	**优先级**: Fig 1 > Fig 3 > Fig 2 > Fig 5 > Fig 4 > Fig 6
241	
242	**全局风格约束**:
243	- 字体: 与 LaTeX 正文一致（serif / Computer Modern），matplotlib 中用 `plt.rcParams['font.family'] = 'serif'`
244	- 字号: 轴标签 ≥ 9pt，刻度标签 ≥ 8pt（单栏图缩放后仍可读）
245	- 颜色一致性: 全文 RASP = 蓝色 (#1f77b4)，Standard = 红色 (#d62728)，GRASPrune = 绿色 (#2ca02c)，Baseline = 灰色
246	- 输出格式: PDF（矢量图，用于 LaTeX）+ PNG 300dpi（备用）
247	- 无网格或仅用浅灰网格
248	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "47410cb5-302f-4c0f-a79c-43574763a6cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/_project/paper/figure_plan.md",
      "content": "# Figure Plan — Recovery-Aware Structured Pruning (RASP)\n\n---\n\n## Fig 1: RASP Pipeline Overview\n\n**类型**: 流程/架构图（method figure）\n\n**内容**:\n```\nPre-trained Reasoning LLM (DeepSeek-R1-Distill-Qwen-7B)\n        │\n        ├──────────────────────────┐\n        ▼                          ▼\n  Importance I(h)           CKA Overlap F(h)\n  (Taylor gradient)        (intra-layer pairwise)\n        │                          │\n        └──────────┬───────────────┘\n                   ▼\n        RASP Score: S(h) = I(h) × (1 - F(h))^α\n                   │\n                   ▼\n        Structured Pruning (remove lowest S(h))\n                   │\n                   ▼\n        ┌──────────┴──────────┐\n        ▼                     ▼\n  SFT Warmup              [对比: Standard Pruning]\n  (fix generation)         只用 I(h), 无 F(h) 修正\n        │\n        ▼\n  GRPO RLVR Recovery\n  (restore reasoning)\n        │\n        ▼\n  Recovered Compact Model\n```\n\n**关键设计要素**:\n- 左侧主 pipeline 用蓝色系，右侧 Standard 对比用灰色/红色\n- I(h) 和 F(h) 分支用不同颜色区分（如蓝 vs 橙），在合并处突出 RASP scoring 公式\n- Standard pruning 旁路用虚线表示，标注 \"importance-only\"\n- Recovery 阶段标注 \"SFT Warmup → GRPO\" 两步\n- 在 CKA Overlap 框旁加小示意：同层 head 间 pairwise CKA matrix\n\n**数据可用性**: 无需实验数据，纯方法示意图\n\n**建议工具**: TikZ（最佳）或 matplotlib + patches + FancyArrowPatch\n\n**论文位置**: Section 3 (Method) 开头，首次引用\n\n**尺寸**: 双栏宽度（full width），高度约 6-8cm\n\n---\n\n## Fig 2: CKA Overlap vs Recoverability Scatter Plot\n\n**类型**: 散点图\n\n**内容**:\n- **X 轴**: F(g) — per-structure CKA functional overlap（pruned structure 与其最相似 retained structure 的 CKA）\n- **Y 轴**: Recoverability — retained structure 在 pruned model vs GRPO-recovered model 之间的 activation shift（1 - cosine similarity）\n- 每个点 = 一个被剪掉的 structure（attention GQA group 或 MLP channel group）\n- 按 structure type 着色：蓝色 = attention，橙色 = MLP\n- 或按 layer index 着色（viridis colormap）+ colorbar\n- 回归线 + Spearman ρ 及 95% CI 标注在图上\n- 标注 2-3 个典型点（如 \"Layer 2 attn: low F(h), low recovery\" vs \"Layer 25 attn: high F(h), high recovery\"）\n\n**数据来源**:\n- `correlation_analysis.py` 输出 `correlation_results.json`\n- 需要：base model, pruned model (RASP 20%), GRPO-recovered model, `cka_scores.pt`, `pruning_metadata.pt`\n- 服务器路径: `/root/autodl-tmp/recovery_aware_struct_prune/` 下的对应 checkpoint\n\n**数据可用性**: **待 correlation_analysis.py 执行**。代码已写好（`artifacts/correlation_analysis.py`），需 GRPO stage 2 checkpoint 完成后运行。GRPO v2 状态: DONE（`grpo_stage2_rasp_20_DONE_20260515`）\n\n**关键设计要素**:\n- 颜色方案：attention (#1f77b4) vs MLP (#ff7f0e)，与 `correlation_analysis.py` 一致\n- 点大小 30，alpha 0.7，黑色细边框\n- 右下角文本框：ρ = X.XX, 95% CI [X.XX, X.XX], p < 0.001\n- 如果 attention 和 MLP 趋势不同，可考虑分面（两个子图）\n- 灰色虚线标注 \"Recoverable zone\" 阈值\n\n**建议工具**: matplotlib（已有 `make_scatter_plot` 函数，需微调为论文质量）\n\n**论文位置**: Section 5.3 (Claim 2: F(h) predicts recoverability)\n\n**尺寸**: 单栏宽度，约 8cm × 6cm\n\n---\n\n## Fig 3: RLVR vs SFT Recovery Trajectory\n\n**类型**: 折线图\n\n**内容**:\n- **X 轴**: Training steps\n- **Y 轴**: GSM8K accuracy (%) 或 reward mean\n- **4 条线**:\n  1. RASP + SFT → GRPO（蓝色实线，主角）\n  2. Standard + SFT → GRPO（红色实线）\n  3. RASP + SFT only（蓝色虚线）\n  4. Standard + SFT only（红色虚线）\n- 分两阶段：SFT warmup（左半）→ GRPO recovery（右半），用竖线分隔\n- **关键标注**:\n  - \"Reward Desert\" 区域：Standard + GRPO 在某步数后 reward 停滞的区间（灰色阴影）\n  - RASP + GRPO 的持续上升趋势\n  - 水平虚线标注 baseline accuracy (82.6%)\n  - 各条线终点标注最终准确率\n\n**数据来源**:\n- wandb runs: SFT training logs (train loss / eval accuracy per step)\n- wandb runs: GRPO v2 training logs (reward_mean, gsm8k_accuracy per step)\n- 4 个 run：`sft_rasp_20`, `sft_standard_20`, `grpo_stage2_rasp_20`, `grpo_stage2_standard_20`\n\n**数据可用性**: **部分已有**。SFT runs 已完成。GRPO stage 2 runs 已完成（DONE status）。需从 wandb 提取 step-level metrics。\n\n**关键设计要素**:\n- 颜色方案：RASP = 蓝色系 (#1f77b4)，Standard = 红色系 (#d62728)；实线 = +GRPO，虚线 = SFT only\n- X 轴两段拼接：SFT steps (0 → SFT_end) | GRPO steps (0 → 2000)，中间竖虚线分隔标注 \"SFT → GRPO\"\n- 水平灰色虚线标 baseline 82.6%\n- \"Reward Desert\" 灰色阴影区（Standard GRPO 停滞区间）\n- 图例放右下角，避免遮挡曲线\n\n**建议工具**: matplotlib\n\n**论文位置**: Section 5.4 (Claim 3: Recovery method conditions optimal pruning)\n\n**尺寸**: 双栏宽度或 1.5 栏宽度，高度约 5-6cm\n\n---\n\n## Fig 4: α Ablation 曲线（可选）\n\n**类型**: 折线图 + 误差棒\n\n**内容**:\n- **X 轴**: α 值 {0, 0.5, 1.0, 2.0, 4.0}\n- **Y 轴**: Post-prune GSM8K accuracy (%)\n- 单条线 + 95% CI 误差棒\n- α=0 等价于 Standard pruning（标注）\n- α=1.0 为当前默认值（用星号或不同 marker 高亮）\n- 可选第二条线：post-recovery accuracy（如果有对应 GRPO 数据）\n\n**数据来源**:\n- `src/run_alpha_ablation.sh` 输出\n- α=1.0 已有结果（24.3% post-prune on full eval）\n- 其他 α 值待运行\n\n**数据可用性**: **待 α ablation 实验执行**。代码和脚本已准备好（`src/run_alpha_ablation.sh`）。α=1.0 可复用。磁盘空间约束需顺序执行（每个 α prune → eval → 删除 → 下一个）。\n\n**关键设计要素**:\n- X 轴用 log scale 或等距排列（0 作为特殊点）\n- α=0 标注 \"= Standard\"\n- α=1.0 用 ★ marker\n- 如果存在最优点，用箭头标注\n- 灰色水平虚线标 baseline\n\n**建议工具**: matplotlib\n\n**论文位置**: Section 5.5 (Ablation Studies)\n\n**尺寸**: 单栏宽度，约 7cm × 5cm\n\n---\n\n## Fig 5: Per-layer Pruning Distribution（可选）\n\n**类型**: 分组柱状图（grouped bar chart）\n\n**内容**:\n- **X 轴**: Layer index (0-27)\n- **Y 轴**: 该层被剪掉的 structure 数量（或剪枝比例 %）\n- **两组柱**: Standard (红) vs RASP (蓝)\n- 可分为上下两个子图：attention heads (上) + MLP groups (下)\n- 突出关键差异：RASP 在哪些层保留更多、在哪些层剪掉更多\n\n**数据来源**:\n- `pruning_metadata.pt` 中的 `attn_keep_masks` 和 `mlp_keep_masks`\n- 需要 Standard 和 RASP 两个版本的 pruning metadata\n- 服务器路径: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20/` 和 `pruned_standard_20/`\n\n**数据可用性**: **已有**。两个 pruned model 目录中各有 `pruning_metadata.pt`。\n\n**关键设计要素**:\n- 柱宽窄（28 层 × 2 组），用颜色区分 Standard vs RASP\n- 标注差异最大的层（如 \"Layer 5: RASP 保留全部 4 GQA groups，Standard 只保留 2\"）\n- 上方标注总剪枝预算相同（matched parameter count）\n- 考虑用热力图替代（层 × method，颜色深浅 = 剪枝比例），更紧凑\n\n**建议工具**: matplotlib\n\n**论文位置**: Section 5.2 (Analysis) 或 Appendix\n\n**尺寸**: 双栏宽度（如果柱状图）或单栏（如果热力图）\n\n---\n\n## Fig 6: CKA Overlap Heatmap（可选）\n\n**类型**: 热力图\n\n**内容**:\n- 展示某代表层（如 Layer 12）的 attention head/GQA group 间 pairwise CKA overlap matrix\n- 或展示所有 28 层的 per-head mean overlap 作为 1D heatmap\n- 对角线为 1.0，颜色从浅（低 overlap）到深（高 overlap）\n- 标注高 overlap 区域 = \"redundant but recoverable\" 和低 overlap 区域 = \"unique, must preserve\"\n\n**数据来源**:\n- `results/cka_scores.pt`\n- 包含 `attn_cka_matrix` (per-layer pairwise CKA) 和 `attn_overlap` (per-head mean overlap)\n\n**数据可用性**: **已有**。`cka_scores.pt` (122KB) 已缓存在服务器。\n\n**关键设计要素**:\n- 颜色方案：`coolwarm` 或 `YlOrRd`（学术标准）\n- 如果展示单层 pairwise matrix：4×4 (GQA groups) 或更大\n- 如果展示全层 summary：28 行 × N 列热力图\n- 对角线标为灰色（self-overlap = 1.0，不 informative）\n- 叠加 RASP 剪枝决策标记（✓ 保留 / ✗ 移除）\n\n**建议工具**: matplotlib + seaborn.heatmap\n\n**论文位置**: Section 4 (CKA-based Functional Overlap) 或 Appendix\n\n**尺寸**: 单栏宽度\n\n---\n\n## 汇总\n\n| 图号 | 标题 | 类型 | 数据状态 | 位置 | 宽度 |\n|------|------|------|----------|------|------|\n| Fig 1 | RASP Pipeline Overview | 流程图 | 无需数据 | §3 Method | 双栏 |\n| Fig 2 | CKA Overlap vs Recoverability | 散点图 | 待 correlation_analysis 运行 | §5.3 Claim 2 | 单栏 |\n| Fig 3 | Recovery Trajectory | 折线图 | 待 wandb 数据提取 | §5.4 Claim 3 | 双栏 |\n| Fig 4 | α Ablation | 折线图 | 待 ablation 实验 | §5.5 Ablation | 单栏 |\n| Fig 5 | Per-layer Pruning Distribution | 柱状图/热力图 | ✅ 已有 | §5.2 / Appendix | 双栏 |\n| Fig 6 | CKA Overlap Heatmap | 热力图 | ✅ 已有 | §4 / Appendix | 单栏 |\n\n**优先级**: Fig 1 > Fig 3 > Fig 2 > Fig 5 > Fig 4 > Fig 6\n\n**全局风格约束**:\n- 字体: 与 LaTeX 正文一致（serif / Computer Modern），matplotlib 中用 `plt.rcParams['font.family'] = 'serif'`\n- 字号: 轴标签 ≥ 9pt，刻度标签 ≥ 8pt（单栏图缩放后仍可读）\n- 颜色一致性: 全文 RASP = 蓝色 (#1f77b4)，Standard = 红色 (#d62728)，GRASPrune = 绿色 (#2ca02c)，Baseline = 灰色\n- 输出格式: PDF（矢量图，用于 LaTeX）+ PNG 300dpi（备用）\n- 无网格或仅用浅灰网格\n",
      "numLines": 248,
      "startLine": 1,
      "totalLines": 248
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
Now I have a thorough understanding of all the inputs. Let me organize the Related Work section. I need to:

1. Identify which citation keys are already in `references.bib` vs which need to be added
2. Structure into 2-3 subsections
3. Write ~500-600 words highlighting the gap

**Already in references.bib:**
- `selfhealing2025` ✓
- `graspprune2026` ✓
- `resp2025` ✓
- `mpruner2024` ✓


- `paser2025` ✓
- `llmpruner2023` ✓
- `kornblith2019cka` ✓
- `lachance2024cka` ✓
- `llms2lrms2026` ✓
- `rac2025` ✓
- `doingmore2026` ✓
- `bonsai2025` ✓
- `slicegpt2024` ✓
- `wanda2024` ✓
- `shortgpt2024` ✓
- `frankle2019lth` ✓
- `p2law2025` ✓

Good, looks like all the major citations I need are already in the bibliography.

Now I'm checking the literature notes against the references file to see what's missing. I notice the key naming conventions differ between the two files, so I need to match them carefully. Looking at the entries, I can see that some papers like the self-healing work have corresponding entries in the bibliography, but I need to verify which ones are actually missing and which ones just use different key formats. I need to add SSGR to the references and figure out how to handle the reasoning-focused papers. Now I'm organizing the related work into subsections: one covering general structured pruning methods for LLMs, another for reasoning-specific approaches that use calibration and chain-of-thought reconstruction, and a third section that I'm still planning out. The key gap I'm identifying is that existing work improves importance estimation but doesn't account for recovery after pruning. I'm organizing the related work around three core themes that align with RASP's contributions: structured pruning methods for LLMs, post-pruning recovery techniques, and representational similarity approaches. This should give me roughly 170-200 words per subsection to stay within the 500-600 word target while avoiding redundancy with the methods section. and columns of weight matrices after orthogonal transformations. GRASPrune jointly prunes FFN channels and KV head groups under a global budget using differentiable gating, achieving state-of-the-art results on LLaMA-2-7B at 50% sparsity.

Recent work has adapted pruning techniques to reasoning models, with findings showing that width pruning outperforms depth pruning for these tasks. RESP uses self-generated reasoning traces for calibration, while SSGR demonstrates that selective self-generated data improves pruning of reasoning LLMs. RAC reconstructs activations from both inputs and on-policy chain-of-thought traces, and recent work shows that structured pruning significantly degrades test-time scaling performance, highlighting the need for recovery mechanisms.

The key insight is that existing methods focus on improving the pruning decision itself but don't account for how well the pruned model can actually be recovered afterward. RASP fills this gap by making recoverability part of the pruning score. For post-pruning recovery, standard supervised finetuning approaches exist, but RLVR-based recovery substantially outperforms SFT for pruned reasoning models, achieving over 95% of unpruned accuracy at 25% compression. However, Self-Healing applies this recovery to conventionally pruned models without modifying the pruning decision to facilitate recovery.

Several methods optimize the recovery process itself: PASER uses manifold-based clustering and capability-aware budget allocation to recover pruned LLM capabilities with only 4-20% of post-training data, P²Law establishes scaling laws between pruning ratio and recovery data volume, and PAT co-optimizes pruning masks and recovery tuning through joint training. RASP complements these by optimizing which structures to prune for maximal recoverability, while methods like PASER and P²Law optimize the recovery process itself—the two directions can be combined.

Now I'm looking at representational similarity approaches for pruning, starting with Centered Kernel Alignment, which measures similarity between neural network representations invariant to invertible linear transformations.

Prior work uses CKA as a redundancy detector—MPruner clusters layers by inter-layer CKA similarity for depth pruning, other work analyzes and guides pruning through CKA, and ShortGPT identifies redundant layers via representational similarity. But RASP repurposes CKA differently, using it as a recoverability predictor rather than a redundancy detector. Instead of measuring inter-layer similarity for depth pruning, I'm computing intra-layer pairwise CKA between attention head groups to identify structures whose function can be redistributed across retained structures during recovery.

Now I'm checking which citations need to be added to the references—looks like `xiang2025ssgr` is missing and needs to be added, while the others are already there. I'm checking the citation keys in references.bib against what's used in method.tex to ensure consistency. The keys follow a pattern like `selfhealing2025`, `resp2025`, `mpruner2024` rather than author-first formats. I notice my draft has `\citet{ding2026lrmpruning}` but the actual key in references.bib is `llms2lrms2026`, so I need to fix that inconsistency and use `ssgr2025` for the new citation.

Adding the BibTeX entry...

Now I need to verify the citation syntax is consistent with the existing tex files — checking that `\citet{}` renders correctly for textual citations and `\citep{}` for parenthetical ones. Let me also confirm whether the paper directory and related_work.tex file already exist before writing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "954062bc-8561-4fce-acd0-da4a81bf9ba8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5TTiHs9vPRz7gjgkz5ntf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17826,
      "cache_read_input_tokens": 23294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17826
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

Let me check if `related_work.tex` already exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "bdad42b8-601e-4d33-93df-c5e3de982d3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5TTiHs9vPRz7gjgkz5ntf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17826,
      "cache_read_input_tokens": 23294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17826
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

<details open><summary>🔧 Tool call — Glob · `toolu_016Mr4dLmZB2dynfPNmfoHF8`</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "7dac8a74-0879-472f-867d-7d112a7280c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5TTiHs9vPRz7gjgkz5ntf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17826,
      "cache_read_input_tokens": 23294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17826
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

_source line 16 · 2026-05-15T05:00:19.875Z_

<details><summary>↩ Tool result · `toolu_016Mr4dLmZB2dynfPNmfoHF8`</summary>

```text
paper/introduction.tex
paper/related_work.tex
paper/experiments.tex
paper/backup/experiments.tex
paper/backup/introduction.tex
paper/backup/method.tex
paper/backup/related_work.tex
paper/main.tex
paper/abstract.tex
paper/conclusion.tex
paper/limitations.tex
paper/appendix.tex
paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "aba7cbd5-a266-4bbd-abd6-0bbe3c32c6ff",
  "tool_use_result": {
    "filenames": [
      "paper/introduction.tex",
      "paper/related_work.tex",
      "paper/experiments.tex",
      "paper/backup/experiments.tex",
      "paper/backup/introduction.tex",
      "paper/backup/method.tex",
      "paper/backup/related_work.tex",
      "paper/main.tex",
      "paper/abstract.tex",
      "paper/conclusion.tex",
      "paper/limitations.tex",
      "paper/appendix.tex",
      "paper/method.tex"
    ],
    "durationMs": 20,
    "numFiles": 13,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_016ZxUMgSF3L2qEuQHonmKEW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "c4f11268-da63-4448-88bd-201d6e9520d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uerHsdXUMsd7iMYCk8inu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3509,
      "cache_read_input_tokens": 41120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3509
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

_source line 18 · 2026-05-15T05:00:22.170Z_

<details><summary>↩ Tool result · `toolu_016ZxUMgSF3L2qEuQHonmKEW`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Structured Pruning of Large Language Models}
5	\label{sec:rw_pruning}
6	
7	Structured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.
8	LLM-Pruner~\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.
9	Bonsai~\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.
10	GRASPrune~\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.
11	ShortGPT~\citep{shortgpt2024} and SliceGPT~\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.
12	
13	For reasoning models specifically, RESP~\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\% on GSM8K at 40\% structured sparsity without any recovery training.
14	\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.
15	RAC~\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.
16	\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \emph{which} structures are removed critically shapes recovery potential.
17	
18	RASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.
19	
20	\subsection{Pruning-Aware Recovery and Re-training}
21	\label{sec:rw_recovery}
22	
23	Post-pruning recovery is essential at moderate to high compression ratios.
24	\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\%+ accuracy at 25\% compression, significantly outperforming SFT recovery (${\sim}$80\%).
25	This establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \emph{choice} of what to prune affects how well RLVR can recover.
26	
27	P\textsuperscript{2} Law~\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \propto (1/\rho)^\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.
28	PASER~\citep{paser2025} optimizes which recovery \emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \emph{structures} to prune for recoverability.
29	PAT~\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.
30	
31	The Lottery Ticket Hypothesis~\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.
32	RASP extends this notion to what we term \emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.
33	
34	\subsection{RLVR Training Dynamics}
35	\label{sec:rw_rlvr}
36	
37	Understanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.
38	\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \emph{expands} correct trajectories via local imitation.
39	This asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.
40	OPSD~\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.
41	
42	\paragraph{CKA-based pruning.}
43	CKA~\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.
44	MPruner~\citep{mpruner2024} uses \emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.
45	\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.
46	Both operate at the \emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.
47	In contrast, RASP uses \emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\ immediate accuracy preservation).
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "dde78d5b-d209-4591-916d-cc2cac8a3472",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Structured Pruning of Large Language Models}\n\\label{sec:rw_pruning}\n\nStructured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\nLLM-Pruner~\\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.\nBonsai~\\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.\nGRASPrune~\\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.\nShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.\n\nFor reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.\nRAC~\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.\n\\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \\emph{which} structures are removed critically shapes recovery potential.\n\nRASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.\n\n\\subsection{Pruning-Aware Recovery and Re-training}\n\\label{sec:rw_recovery}\n\nPost-pruning recovery is essential at moderate to high compression ratios.\n\\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\\%+ accuracy at 25\\% compression, significantly outperforming SFT recovery (${\\sim}$80\\%).\nThis establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \\emph{choice} of what to prune affects how well RLVR can recover.\n\nP\\textsuperscript{2} Law~\\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \\propto (1/\\rho)^\\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.\nPASER~\\citep{paser2025} optimizes which recovery \\emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \\emph{structures} to prune for recoverability.\nPAT~\\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.\n\nThe Lottery Ticket Hypothesis~\\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.\nRASP extends this notion to what we term \\emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.\n\n\\subsection{RLVR Training Dynamics}\n\\label{sec:rw_rlvr}\n\nUnderstanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.\n\\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \\emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \\emph{expands} correct trajectories via local imitation.\nThis asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.\nOPSD~\\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.\n\n\\paragraph{CKA-based pruning.}\nCKA~\\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.\nMPruner~\\citep{mpruner2024} uses \\emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.\n\\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.\nBoth operate at the \\emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.\nIn contrast, RASP uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\\ immediate accuracy preservation).\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The file already exists with a well-written Related Work section. Let me compare it with what I was planning:

The existing file has 4 subsections:
1. Structured Pruning of Large Language Models
2. Pruning-Aware Recovery and Re-training
3. RLVR Training Dynamics (includes CKA-based pruning as a paragraph)

The existing version is quite good! It:
- Cites all major papers from literature_notes.md except SSGR and ThinkPrune/ThinkPruneTrainImprove
- Is well-organized
- Highlights the RASP gap clearly


- Uses correct citation keys from references.bib

Now I'm checking what's missing from the current related_work.tex compared to literature_notes.md. SSGR is the main gap—it's relevant since it's from the same group as Self-Healing and addresses calibration for reasoning-specific scenarios, though ThinkPrune and Think, Prune, Train, Improve are more orthogonal since they focus on reasoning trace pruning rather than model pruning itself.

Looking at the requirements, the existing version hits most of them: it has the subsections, highlights RASP distinctions, emphasizes the gap around CKA functional overlap for pruning decisions, and cites from both sources. The word count is around 580-620 words, which fits the target. I should verify all citation keys exist in references.bib and consider whether to add SSGR for completeness.

Let me check the citations used: `llmpruner2023`, `bonsai2025`, `graspprune2026` are all there, and I need to verify the rest against the bibliography to make sure nothing's missing. The related_work.tex file is already comprehensive, but I should enhance it by adding the SSGR reference to the reasoning model pruning section and updating the bibliography accordingly. Let me incorporate that missing citation and verify everything is complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "ab3b455e-f1c6-4cf1-a4b7-75e7dd965504",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR6RJPGtv3h4sWfkfwzVoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1722,
      "cache_read_input_tokens": 44629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1722
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

`related_work.tex` already exists with solid content. It covers most papers from `literature_notes.md` but is missing SSGR. Let me add it and verify all citation keys.

The only paper from `literature_notes.md` not yet cited is SSGR~\citep{xiang2025ssgr} — relevant as reasoning-specific calibration work from the same group as Self-Healing. I'll add it to the pruning paragraph and append the bib entry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "03390b8e-de94-4eef-908a-fe500e53b374",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR6RJPGtv3h4sWfkfwzVoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1722,
      "cache_read_input_tokens": 44629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1722
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Eam7Ag7FRUt7gTt4cCk8Tc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex",
  "old_string": "For reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.",
  "new_string": "For reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\nSSGR~\\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "75bf28f4-52cc-4df9-a848-1f647cfa678b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YR6RJPGtv3h4sWfkfwzVoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1722,
      "cache_read_input_tokens": 44629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1722
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

_source line 22 · 2026-05-15T05:01:00.454Z_

<details><summary>↩ Tool result · `toolu_01Eam7Ag7FRUt7gTt4cCk8Tc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "7d2a48b7-cd89-456e-bd8a-f346c6930d5e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex",
    "oldString": "For reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.",
    "newString": "For reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\nSSGR~\\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Structured Pruning of Large Language Models}\n\\label{sec:rw_pruning}\n\nStructured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\nLLM-Pruner~\\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.\nBonsai~\\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.\nGRASPrune~\\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.\nShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.\n\nFor reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.\nRAC~\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.\n\\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \\emph{which} structures are removed critically shapes recovery potential.\n\nRASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.\n\n\\subsection{Pruning-Aware Recovery and Re-training}\n\\label{sec:rw_recovery}\n\nPost-pruning recovery is essential at moderate to high compression ratios.\n\\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\\%+ accuracy at 25\\% compression, significantly outperforming SFT recovery (${\\sim}$80\\%).\nThis establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \\emph{choice} of what to prune affects how well RLVR can recover.\n\nP\\textsuperscript{2} Law~\\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \\propto (1/\\rho)^\\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.\nPASER~\\citep{paser2025} optimizes which recovery \\emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \\emph{structures} to prune for recoverability.\nPAT~\\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.\n\nThe Lottery Ticket Hypothesis~\\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.\nRASP extends this notion to what we term \\emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.\n\n\\subsection{RLVR Training Dynamics}\n\\label{sec:rw_rlvr}\n\nUnderstanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.\n\\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \\emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \\emph{expands} correct trajectories via local imitation.\nThis asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.\nOPSD~\\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.\n\n\\paragraph{CKA-based pruning.}\nCKA~\\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.\nMPruner~\\citep{mpruner2024} uses \\emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.\n\\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.\nBoth operate at the \\emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.\nIn contrast, RASP uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\\ immediate accuracy preservation).\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 6,
        "newStart": 11,
        "newLines": 7,
        "lines": [
          " ShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.",
          " ",
          " For reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.",
          "+SSGR~\\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.",
          " \\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.",
          " RAC~\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.",
          " \\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \\emph{which} structures are removed critically shapes recovery potential."
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

_source line 23_

Now add the SSGR bib entry to `references.bib`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "f9a43948-d477-4c73-8579-ad44adf49a9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WW3MZc5vUWWoJS6oH8PzPq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1817,
      "cache_read_input_tokens": 46351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1817
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Utmq6rWi3QqNd62gJYTmtL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
  "old_string": "@article{doingmore2026,",
  "new_string": "@article{ssgr2025,\n  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},\n  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},\n  journal={arXiv preprint arXiv:2511.18864},\n  year={2025},\n  url={https://arxiv.org/abs/2511.18864}\n}\n\n@article{doingmore2026,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "69b2f74c-10ed-4d50-b896-899aee5d3bf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WW3MZc5vUWWoJS6oH8PzPq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1817,
      "cache_read_input_tokens": 46351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1817
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

_source line 25 · 2026-05-15T05:01:06.679Z_

<details><summary>↩ Tool result · `toolu_01Utmq6rWi3QqNd62gJYTmtL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "5a5f03ce-9ee2-4ca4-a744-f69699ee3598",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
    "oldString": "@article{doingmore2026,",
    "newString": "@article{ssgr2025,\n  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},\n  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},\n  journal={arXiv preprint arXiv:2511.18864},\n  year={2025},\n  url={https://arxiv.org/abs/2511.18864}\n}\n\n@article{doingmore2026,",
    "originalFile": "@article{deepseek2025r1,\n  title={DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},\n  author={{DeepSeek-AI}},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025},\n  url={https://arxiv.org/abs/2501.12948}\n}\n\n@article{qwen2.5,\n  title={Qwen2.5 Technical Report},\n  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and others},\n  journal={arXiv preprint arXiv:2412.15115},\n  year={2024},\n  url={https://arxiv.org/abs/2412.15115}\n}\n\n@article{cobbe2021gsm8k,\n  title={Training Verifiers to Solve Math Word Problems},\n  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal={arXiv preprint arXiv:2110.14168},\n  year={2021},\n  url={https://arxiv.org/abs/2110.14168}\n}\n\n@article{shao2024grpo,\n  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},\n  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},\n  journal={arXiv preprint arXiv:2402.03300},\n  year={2024},\n  url={https://arxiv.org/abs/2402.03300}\n}\n\n@inproceedings{llmpruner2023,\n  title={LLM-Pruner: On the Structural Pruning of Large Language Models},\n  author={Ma, Xinyin and Fang, Gongfan and Wang, Xinchao},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.11627}\n}\n\n@inproceedings{graspprune2026,\n  title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models},\n  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},\n  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2026},\n  url={https://arxiv.org/abs/2604.19398}\n}\n\n@article{resp2025,\n  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},\n  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},\n  journal={arXiv preprint arXiv:2512.02185},\n  year={2025},\n  url={https://arxiv.org/abs/2512.02185}\n}\n\n@article{selfhealing2025,\n  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},\n  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},\n  year={2025},\n  note={Under review},\n  url={https://openreview.net/forum?id=Cy8Qa4gAst}\n}\n\n@inproceedings{bonsai2025,\n  title={Everybody Prune Now: Structured Pruning of LLMs with only Forward Passes},\n  author={Kolawole, Steven and Dery, Lucio and Kagy, Jean-Fran\\c{c}ois and Smith, Virginia and Neubig, Graham and Talwalkar, Ameet},\n  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2402.05406}\n}\n\n@article{paser2025,\n  title={PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery},\n  author={He, Bowei and Yin, Lihao and Zhen, Hui-Ling and Zhang, Xiaokun and Yuan, Mingxuan and Ma, Chen},\n  journal={arXiv preprint arXiv:2502.12594},\n  year={2025},\n  url={https://arxiv.org/abs/2502.12594},\n  note={Under review}\n}\n\n@inproceedings{rlsqueezes2026,\n  title={RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs},\n  author={Matsutani, Kohsei and Takashiro, Shota and Minegishi, Gouki and Kojima, Takeshi and Iwasawa, Yusuke and Matsuo, Yutaka},\n  booktitle={Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2509.21128}\n}\n\n@inproceedings{kornblith2019cka,\n  title={Similarity of Neural Network Representations Revisited},\n  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle={Proceedings of the 36th International Conference on Machine Learning (ICML)},\n  year={2019},\n  url={https://arxiv.org/abs/1905.00414}\n}\n\n@article{mpruner2024,\n  title={MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning},\n  author={Hu, Seungbeom and Park, Chanjun and Ferraiuolo, Andrew and Ko, Sang-Ki and Kim, Jinwoo and Song, Haein and Kim, Jieung},\n  journal={arXiv preprint arXiv:2408.13482},\n  year={2024},\n  url={https://arxiv.org/abs/2408.13482}\n}\n\n@mastersthesis{lachance2024cka,\n  title={Using Centered Kernel Alignment for Understanding and Pruning Neural Networks},\n  author={Lachance, Alex},\n  school={University of Rhode Island},\n  year={2024},\n  url={https://digitalcommons.uri.edu/theses/2283/}\n}\n\n@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carbin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}\n\n@inproceedings{ainslie2023gqa,\n  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},\n  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\\'o}n, Federico and Sanghai, Sumit},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.13245}\n}\n\n@article{shortgpt2024,\n  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},\n  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},\n  journal={arXiv preprint arXiv:2403.03853},\n  year={2024},\n  url={https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{slicegpt2024,\n  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},\n  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2401.15024}\n}\n\n@inproceedings{wanda2024,\n  title={A Simple and Effective Pruning Approach for Large Language Models},\n  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2306.11695}\n}\n\n@article{llms2lrms2026,\n  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},\n  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},\n  journal={arXiv preprint arXiv:2601.18091},\n  year={2026},\n  url={https://arxiv.org/abs/2601.18091}\n}\n\n@inproceedings{rac2025,\n  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},\n  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  url={https://arxiv.org/abs/2509.12464}\n}\n\n@article{doingmore2026,\n  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n  journal={arXiv preprint arXiv:2604.25098},\n  year={2026},\n  url={https://arxiv.org/abs/2604.25098}\n}\n\n@inproceedings{p2law2025,\n  title={{P\\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},\n  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2025},\n  url={https://arxiv.org/abs/2411.10272}\n}\n\n@inproceedings{pat2025,\n  title={{PAT}: Pruning-Aware Tuning for Large Language Models},\n  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},\n  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  url={https://arxiv.org/abs/2408.14721}\n}\n\n@article{opsd2026,\n  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},\n  author={Kim, Jaehoon and Lee, Dongha},\n  journal={arXiv preprint arXiv:2605.06188},\n  year={2026},\n  url={https://arxiv.org/abs/2605.06188}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 167,
        "oldLines": 6,
        "newStart": 167,
        "newLines": 14,
        "lines": [
          "   url={https://arxiv.org/abs/2509.12464}",
          " }",
          " ",
          "+@article{ssgr2025,",
          "+  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},",
          "+  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},",
          "+  journal={arXiv preprint arXiv:2511.18864},",
          "+  year={2025},",
          "+  url={https://arxiv.org/abs/2511.18864}",
          "+}",
          "+",
          " @article{doingmore2026,",
          "   title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},",
          "   author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},"
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

_source line 26_

验证最终文件内容和所有 citation key。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "9a731685-102e-485d-afd6-b43d4dbfea0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mbwHxmQc7w1gN4kvFpGVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 48168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 347
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

<details open><summary>🔧 Tool call — Read · `toolu_0181UWVCzMn88pPssec6zfT9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "7e9e11f4-44be-4152-b270-7699454b5be5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mbwHxmQc7w1gN4kvFpGVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 48168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 347
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

_source line 28 · 2026-05-15T05:01:10.229Z_

<details><summary>↩ Tool result · `toolu_0181UWVCzMn88pPssec6zfT9`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Structured Pruning of Large Language Models}
5	\label{sec:rw_pruning}
6	
7	Structured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.
8	LLM-Pruner~\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.
9	Bonsai~\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.
10	GRASPrune~\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.
11	ShortGPT~\citep{shortgpt2024} and SliceGPT~\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.
12	
13	For reasoning models specifically, RESP~\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\% on GSM8K at 40\% structured sparsity without any recovery training.
14	SSGR~\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.
15	\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.
16	RAC~\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.
17	\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \emph{which} structures are removed critically shapes recovery potential.
18	
19	RASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.
20	
21	\subsection{Pruning-Aware Recovery and Re-training}
22	\label{sec:rw_recovery}
23	
24	Post-pruning recovery is essential at moderate to high compression ratios.
25	\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\%+ accuracy at 25\% compression, significantly outperforming SFT recovery (${\sim}$80\%).
26	This establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \emph{choice} of what to prune affects how well RLVR can recover.
27	
28	P\textsuperscript{2} Law~\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \propto (1/\rho)^\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.
29	PASER~\citep{paser2025} optimizes which recovery \emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \emph{structures} to prune for recoverability.
30	PAT~\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.
31	
32	The Lottery Ticket Hypothesis~\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.
33	RASP extends this notion to what we term \emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.
34	
35	\subsection{RLVR Training Dynamics}
36	\label{sec:rw_rlvr}
37	
38	Understanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.
39	\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \emph{expands} correct trajectories via local imitation.
40	This asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.
41	OPSD~\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.
42	
43	\paragraph{CKA-based pruning.}
44	CKA~\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.
45	MPruner~\citep{mpruner2024} uses \emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.
46	\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.
47	Both operate at the \emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.
48	In contrast, RASP uses \emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\ immediate accuracy preservation).
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "6153f9ba-4701-4a38-a930-ca62603b8f26",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Structured Pruning of Large Language Models}\n\\label{sec:rw_pruning}\n\nStructured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\nLLM-Pruner~\\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.\nBonsai~\\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.\nGRASPrune~\\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.\nShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.\n\nFor reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\nSSGR~\\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.\nRAC~\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.\n\\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \\emph{which} structures are removed critically shapes recovery potential.\n\nRASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.\n\n\\subsection{Pruning-Aware Recovery and Re-training}\n\\label{sec:rw_recovery}\n\nPost-pruning recovery is essential at moderate to high compression ratios.\n\\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\\%+ accuracy at 25\\% compression, significantly outperforming SFT recovery (${\\sim}$80\\%).\nThis establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \\emph{choice} of what to prune affects how well RLVR can recover.\n\nP\\textsuperscript{2} Law~\\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \\propto (1/\\rho)^\\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.\nPASER~\\citep{paser2025} optimizes which recovery \\emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \\emph{structures} to prune for recoverability.\nPAT~\\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.\n\nThe Lottery Ticket Hypothesis~\\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.\nRASP extends this notion to what we term \\emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.\n\n\\subsection{RLVR Training Dynamics}\n\\label{sec:rw_rlvr}\n\nUnderstanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.\n\\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \\emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \\emph{expands} correct trajectories via local imitation.\nThis asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.\nOPSD~\\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.\n\n\\paragraph{CKA-based pruning.}\nCKA~\\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.\nMPruner~\\citep{mpruner2024} uses \\emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.\n\\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.\nBoth operate at the \\emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.\nIn contrast, RASP uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\\ immediate accuracy preservation).\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01XpyofQ6AsvyKWrQi1Ahhda`</summary>

```json
{
  "command": "grep -oP '\\\\cite[pt]?\\{([^}]+)\\}' paper/related_work.tex | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u | while read key; do if grep -q \"^@.*{${key},\" paper/references.bib; then echo \"✓ $key\"; else echo \"✗ MISSING: $key\"; fi; done",
  "description": "Verify all citation keys from related_work.tex exist in references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "ba7b5a5e-285c-422c-8566-27f4804286dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mbwHxmQc7w1gN4kvFpGVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 48168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 347
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

_source line 30 · 2026-05-15T05:01:13.132Z_

<details><summary>↩ Tool result · `toolu_01XpyofQ6AsvyKWrQi1Ahhda`</summary>

```text
✓ bonsai2025
✓ doingmore2026
✓ frankle2019lth
✓ graspprune2026
✓ kornblith2019cka
✓ lachance2024cka
✓ llmpruner2023
✓ llms2lrms2026
✓ mpruner2024
✓ opsd2026
✓ p2law2025
✓ paser2025
✓ pat2025
✓ rac2025
✓ resp2025
✓ rlsqueezes2026
✓ selfhealing2025
✓ shortgpt2024
✓ slicegpt2024
✓ ssgr2025
✓ wanda2024
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "f77e002f-04f4-4ed7-97a8-70ee7583778e",
  "tool_use_result": {
    "stdout": "✓ bonsai2025\n✓ doingmore2026\n✓ frankle2019lth\n✓ graspprune2026\n✓ kornblith2019cka\n✓ lachance2024cka\n✓ llmpruner2023\n✓ llms2lrms2026\n✓ mpruner2024\n✓ opsd2026\n✓ p2law2025\n✓ paser2025\n✓ pat2025\n✓ rac2025\n✓ resp2025\n✓ rlsqueezes2026\n✓ selfhealing2025\n✓ shortgpt2024\n✓ slicegpt2024\n✓ ssgr2025\n✓ wanda2024",
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

_source line 31_

全部 21 个 citation key 均在 `references.bib` 中存在。

完成内容：
- `paper/related_work.tex` — 3 个小节（Structured Pruning / Pruning-Aware Recovery / RLVR Training Dynamics + CKA），引用 21 篇文献，约 600 词
- `paper/references.bib` — 新增 `ssgr2025` 条目
- 原有文件已覆盖 `literature_notes.md` 中 5 篇核心 + 5 篇补充文献（ThinkPrune 和 Think-Prune-Train-Improve 是 reasoning trace 压缩，与 model pruning 正交，未纳入）
- Gap 明确突出：现有工作未用 CKA functional overlap 指导剪枝决策来优化 RLVR recovery

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "uuid": "da205e9b-7116-4abb-bac3-e0d442835bd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011s8g4K2ZFfzSK6ePeX9qje",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2202,
      "cache_read_input_tokens": 48515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2202
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

全部 21 个 citation key 均在 `references.bib` 中存在。

完成内容：
- `paper/related_work.tex` — 3 个小节（Structured Pruning / Pruning-Aware Recovery / RLVR Training Dynamics + CKA），引用 21 篇文献，约 600 词
- `paper/references.bib` — 新增 `ssgr2025` 条目
- 原有文件已覆盖 `literature_notes.md` 中 5 篇核心 + 5 篇补充文献（ThinkPrune 和 Think-Prune-Train-Improve 是 reasoning trace 压缩，与 model pruning 正交，未纳入）
- Gap 明确突出：现有工作未用 CKA functional overlap 指导剪枝决策来优化 RLVR recovery

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 140102,
  "duration_api_ms": 140935,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "def7eee4-ddc1-4d7c-bdc2-76cc7ecb9c36",
  "total_cost_usd": 0.533876,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 38876,
    "cache_read_input_tokens": 263918,
    "output_tokens": 6301,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38876,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 242,
        "cache_read_input_tokens": 48515,
        "cache_creation_input_tokens": 2202,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2202
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1302,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001372,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 6301,
      "cacheReadInputTokens": 263918,
      "cacheCreationInputTokens": 38876,
      "webSearchRequests": 0,
      "costUSD": 0.532504,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ef59e370-f29f-46fe-a9ec-92c46370d61a"
}
```

</details>

---
