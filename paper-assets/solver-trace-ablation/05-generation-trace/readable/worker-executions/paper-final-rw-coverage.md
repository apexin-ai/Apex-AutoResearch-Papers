# paper final rw coverage

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 102
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/workers/worker_paper_final-rw-coverage_20260522T184708.log`
- **Structured JSON:** [`62dd491fb353bf3be930.json`](../../sessions/62/62dd491fb353bf3be930.json)

## Before a recorded user message

12 recorded events

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
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
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
  "uuid": "26395b26-9fe5-408d-8421-b95596bf11b2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1779489600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "65cfb830-17e1-4705-a055-13e2db2bfd8e",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current related work and references files, then search for potentially missing citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "7a6ca4ff-cf1e-4595-a037-da68d4bc5c97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjqvepnhjLm5vy4azxqY9Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15210,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15210
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

<details open><summary>🔧 Tool call — Read · `toolu_01Rfx7tVoQfuGupVUPFoQjj7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "a47efe2a-a6ca-478a-ad12-13479d040713",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjqvepnhjLm5vy4azxqY9Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15210,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15210
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

_source line 6 · 2026-05-22T18:47:20.461Z_

<details><summary>↩ Tool result · `toolu_01Rfx7tVoQfuGupVUPFoQjj7`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	
16	\paragraph{Reward hacking and Goodhart's Law.}
17	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\citep{gao-reward-overoptimization} and logical formalization~\citep{bondarenko-spec-gaming, kim-game-formalization}.
18	Most closely related, \citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models and Lean~4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage.
19	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where KL regularization provably fails, a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.
20	Reward model ensembles~\citep{coste2023reward} and constrained optimization~\citep{moskovitz2023confronting} address overoptimization at the reward level; STA instead diagnoses structural consequences at the output level.
21	Concurrent work documents spurious signals in RLVR~\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking} and proposes composite rewards as mitigations~\citep{tarek2025reward, pronesti2026beyond}; \citet{yue2025rl-reasoning} show RLVR redistributes base-model probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.
22	\citet{helff2026gaming} propose Input Perturbation Testing (IPT) for gaming detection; STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training.
23	While IPT perturbs \emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.
24	\citet{khalifa2026countdown} provide RLVR hacking testbeds.
25	Our Goodhart effect follows the regressional pattern~\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\beta$; its application to a diagnostic designed to \emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.
26	Complementarily, \citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.
27	
28	\paragraph{Mutation testing.}
29	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "7ff9e72f-1880-46b1-9385-86b9766c4332",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nReward shaping theory~\\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.\nIn mathematical reasoning, learned process reward models~\\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\\citep{processbench}.\nA recurring finding is that auxiliary rewards can hurt rather than help: \\citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \\citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.\nAnnotation-free alternatives~\\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.\n\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\\citep{gao-reward-overoptimization} and logical formalization~\\citep{bondarenko-spec-gaming, kim-game-formalization}.\nMost closely related, \\citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models and Lean~4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where KL regularization provably fails, a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.\nReward model ensembles~\\citep{coste2023reward} and constrained optimization~\\citep{moskovitz2023confronting} address overoptimization at the reward level; STA instead diagnoses structural consequences at the output level.\nConcurrent work documents spurious signals in RLVR~\\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking} and proposes composite rewards as mitigations~\\citep{tarek2025reward, pronesti2026beyond}; \\citet{yue2025rl-reasoning} show RLVR redistributes base-model probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.\n\\citet{helff2026gaming} propose Input Perturbation Testing (IPT) for gaming detection; STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training.\nWhile IPT perturbs \\emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \\emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.\n\\citet{khalifa2026countdown} provide RLVR hacking testbeds.\nOur Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\\beta$; its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\nComplementarily, \\citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_0142LVitMso2atVvBitvCPm7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "b8414ced-2381-4d20-92a1-128e07570cdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjqvepnhjLm5vy4azxqY9Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15210,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15210
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

_source line 8 · 2026-05-22T18:47:20.514Z_

<details><summary>↩ Tool result · `toolu_0142LVitMso2atVvBitvCPm7`</summary>

```text
1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
51	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
52	  year         = {2023},
53	}
54	
55	% ============================================================
56	% Category 2: Reward shaping for code/formal verification
57	% ============================================================
58	
59	@inproceedings{lightman-verify-step,
60	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
61	  title        = {{Let's Verify Step by Step}},
62	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
63	  year         = {2024},
64	  note         = {arXiv:2305.20050},
65	}
66	
67	@inproceedings{skalse-reward-hacking,
68	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
69	  title        = {{Defining and Characterizing Reward Hacking}},
70	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
71	  year         = {2022},
72	  note         = {arXiv:2209.13085},
73	}
74	
75	% ============================================================
76	% Category 3: Mutation testing in software engineering
77	% ============================================================
78	
79	@article{demillo1978,
80	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
81	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
82	  journal      = {Computer},
83	  volume       = {11},
84	  number       = {4},
85	  pages        = {34--41},
86	  year         = {1978},
87	}
88	
89	@article{jia-harman-survey,
90	  author       = {Yue Jia and Mark Harman},
91	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
92	  journal      = {IEEE Transactions on Software Engineering},
93	  volume       = {37},
94	  number       = {5},
95	  pages        = {649--678},
96	  year         = {2011},
97	}
98	
99	@article{spurious-rewards,
100	  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},
101	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
102	  journal      = {arXiv preprint arXiv:2506.10947},
103	  year         = {2025},
104	  eprint       = {2506.10947},
105	  archivePrefix = {arXiv},
106	  primaryClass = {cs.AI},
107	}
108	
109	@article{bondarenko-spec-gaming,
110	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
111	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
112	  journal      = {arXiv preprint arXiv:2502.13295},
113	  year         = {2025},
114	  eprint       = {2502.13295},
115	  archivePrefix = {arXiv},
116	  primaryClass = {cs.AI},
117	}
118	
119	@inproceedings{kim-game-formalization,
120	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
121	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
122	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
123	  year         = {2026},
124	  note         = {arXiv:2604.19459},
125	}
126	
127	@inproceedings{gao-reward-overoptimization,
128	  author       = {Leo Gao and John Schulman and Jacob Hilton},
129	  title        = {{Scaling Laws for Reward Model Overoptimization}},
130	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
131	  year         = {2023},
132	  note         = {arXiv:2210.10760},
133	}
134	
135	@inproceedings{karwowski-goodhart-rl,
136	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
137	  title        = {{Goodhart's Law in Reinforcement Learning}},
138	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
139	  year         = {2024},
140	  note         = {arXiv:2310.09144},
141	}
142	
143	% ============================================================
144	% Category 6: FOL/Prolog formalization with LLMs
145	% ============================================================
146	
147	@inproceedings{folio,
148	  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},
149	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
150	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
151	  year         = {2024},
152	  note         = {arXiv:2209.00840},
153	}
154	
155	@inproceedings{logic-lm,
156	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},
157	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
158	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
159	  year         = {2023},
160	}
161	
162	@inproceedings{linc,
163	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},
164	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
165	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
166	  year         = {2023},
167	}
168	
169	@article{fover-pei2025,
170	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
171	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
172	  journal      = {Transactions of the Association for Computational Linguistics},
173	  volume       = {13},
174	  pages        = {1340--1359},
175	  year         = {2025},
176	}
177	
178	@article{lorp,
179	  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},
180	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
181	  journal      = {Knowledge-Based Systems},
182	  year         = {2025},
183	}
184	
185	@article{manheim-goodhart-taxonomy,
186	  author       = {David Manheim and Scott Garrabrant},
187	  title        = {{Categorizing Variants of Goodhart's Law}},
188	  journal      = {arXiv preprint arXiv:1803.04585},
189	  year         = {2019},
190	  eprint       = {1803.04585},
191	  archivePrefix = {arXiv},
192	  primaryClass = {cs.AI},
193	}
194	
195	@inproceedings{math-shepherd,
196	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},
197	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
198	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
199	  year         = {2024},
200	  note         = {arXiv:2312.08935},
201	}
202	
203	% ============================================================
204	% Reward shaping and process supervision
205	% ============================================================
206	
207	@article{rlsf,
208	  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},
209	  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},
210	  journal      = {arXiv preprint arXiv:2405.16661},
211	  year         = {2024},
212	  eprint       = {2405.16661},
213	  archivePrefix = {arXiv},
214	  primaryClass = {cs.AI},
215	}
216	
217	@article{gao-effective-rl-reward,
218	  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},
219	  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},
220	  journal      = {arXiv preprint arXiv:2410.15115},
221	  year         = {2024},
222	  eprint       = {2410.15115},
223	  archivePrefix = {arXiv},
224	  primaryClass = {cs.AI},
225	}
226	
227	@inproceedings{kwa-catastrophic-goodhart,
228	  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\`{a} Garriga-Alonso},
229	  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},
230	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
231	  year         = {2024},
232	  note         = {arXiv:2404.18926},
233	}
234	
235	@article{deepseek-prover-v15,
236	  author       = {{DeepSeek AI}},
237	  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},
238	  journal      = {arXiv preprint arXiv:2408.08152},
239	  year         = {2024},
240	  eprint       = {2408.08152},
241	  archivePrefix = {arXiv},
242	}
243	
244	@article{deepseek-r1,
245	  author       = {{DeepSeek-AI}},
246	  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},
247	  journal      = {arXiv preprint arXiv:2501.12948},
248	  year         = {2025},
249	  eprint       = {2501.12948},
250	  archivePrefix = {arXiv},
251	}
252	
253	@inproceedings{nlproofs,
254	  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},
255	  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},
256	  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
257	  year         = {2022},
258	  eprint       = {2205.12443},
259	  archivePrefix = {arXiv},
260	}
261	
262	@inproceedings{vstar,
263	  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},
264	  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},
265	  booktitle    = {Conference on Language Modeling (COLM)},
266	  year         = {2024},
267	  eprint       = {2402.06457},
268	  archivePrefix = {arXiv},
269	}
270	
271	@inproceedings{easy-to-hard,
272	  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},
273	  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},
274	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
275	  year         = {2024},
276	  eprint       = {2403.09472},
277	  archivePrefix = {arXiv},
278	}
279	
280	% ============================================================
281	% Additional reward-shaping papers
282	% ============================================================
283	
284	@article{reward-hacking-survey,
285	  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},
286	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
287	  journal      = {arXiv preprint arXiv:2604.13602},
288	  year         = {2026},
289	  eprint       = {2604.13602},
290	  archivePrefix = {arXiv},
291	}
292	
293	@misc{metr-reward-hacking,
294	  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},
295	  title        = {{Recent Frontier Models Are Reward Hacking}},
296	  year         = {2025},
297	  howpublished = {METR Technical Blog},
298	  note         = {\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},
299	}
300	
301	@inproceedings{proofwriter,
302	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
303	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
304	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
305	  year         = {2021},
306	  note         = {arXiv:2012.13048},
307	}
308	
309	@article{prooffol-thatikonda2024,
310	  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},
311	  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},
312	  journal      = {arXiv preprint arXiv:2409.16461},
313	  year         = {2024},
314	  eprint       = {2409.16461},
315	  archivePrefix = {arXiv},
316	}
317	
318	@article{qwen3,
319	  author       = {{Qwen Team}},
320	  title        = {{Qwen3 Technical Report}},
321	  journal      = {arXiv preprint arXiv:2505.09388},
322	  year         = {2025},
323	  eprint       = {2505.09388},
324	  archivePrefix = {arXiv},
325	  primaryClass = {cs.CL},
326	}
327	
328	@article{helff2026gaming,
329	  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},
330	  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},
331	  journal      = {arXiv preprint arXiv:2604.15149},
332	  year         = {2026},
333	  eprint       = {2604.15149},
334	  archivePrefix = {arXiv},
335	}
336	
337	@article{khalifa2026countdown,
338	  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},
339	  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},
340	  journal      = {arXiv preprint arXiv:2603.07084},
341	  year         = {2026},
342	  eprint       = {2603.07084},
343	  archivePrefix = {arXiv},
344	}
345	
346	@inproceedings{uesato2022solving,
347	  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},
348	  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},
349	  booktitle={NeurIPS 2022 Workshop on MATH-AI},
350	  year={2022}
351	}
352	
353	@article{cobbe2021training,
354	  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},
355	  title        = {{Training Verifiers to Solve Math Word Problems}},
356	  journal      = {arXiv preprint arXiv:2110.14168},
357	  year         = {2021},
358	}
359	
360	@inproceedings{processbench,
361	  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},
362	  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},
363	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
364	  year         = {2025},
365	  note         = {arXiv:2412.06559},
366	}
367	
368	@article{pronesti2026beyond,
369	  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},
370	  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},
371	  journal      = {arXiv preprint arXiv:2601.17223},
372	  year         = {2026},
373	  eprint       = {2601.17223},
374	  archivePrefix = {arXiv},
375	}
376	
377	@inproceedings{ng1999policy,
378	  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},
379	  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},
380	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
381	  year      = {1999},
382	  pages     = {278--287},
383	}
384	
385	@article{geirhos2020shortcut,
386	  author  = {Robert Geirhos and J{\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},
387	  title   = {Shortcut Learning in Deep Neural Networks},
388	  journal = {Nature Machine Intelligence},
389	  volume  = {2},
390	  pages   = {665--673},
391	  year    = {2020},
392	}
393	
394	@article{dong2026probing,
395	  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},
396	  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},
397	  journal      = {arXiv preprint arXiv:2602.01103},
398	  year         = {2026},
399	  eprint       = {2602.01103},
400	  archivePrefix = {arXiv},
401	}
402	
403	@article{yan2026spurious,
404	  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},
405	  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},
406	  journal      = {arXiv preprint arXiv:2601.11061},
407	  year         = {2026},
408	  eprint       = {2601.11061},
409	  archivePrefix = {arXiv},
410	}
411	
412	@article{tarek2025reward,
413	  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},
414	  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},
415	  journal      = {arXiv preprint arXiv:2509.15557},
416	  year         = {2025},
417	  eprint       = {2509.15557},
418	  archivePrefix = {arXiv},
419	}
420	
421	@inproceedings{yue2025rl-reasoning,
422	  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},
423	  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},
424	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
425	  year         = {2025},
426	  eprint       = {2504.13837},
427	  archivePrefix = {arXiv},
428	}
429	
430	@article{sullivan2025grpo-prm,
431	  author       = {Michael Sullivan and Alexander Koller},
432	  title        = {{GRPO} is Secretly a Process Reward Model},
433	  journal      = {arXiv preprint arXiv:2509.21154},
434	  year         = {2025},
435	  eprint       = {2509.21154},
436	  archivePrefix = {arXiv},
437	}
438	
439	% ============================================================
440	% R19 reviewer-requested references
441	% ============================================================
442	
443	@inproceedings{setlur2025rewarding,
444	  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},
445	  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},
446	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
447	  year         = {2025},
448	  note         = {arXiv:2410.08146},
449	}
450	
451	@article{alphaproof2025,
452	  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},
453	  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},
454	  journal      = {Nature},
455	  year         = {2025},
456	  doi          = {10.1038/s41586-025-09833-y},
457	}
458	
459	% ============================================================
460	% Solvers (Prover9, SWI-Prolog)
461	% ============================================================
462	
463	@article{deepseek-prover-v2,
464	  author       = {{DeepSeek-AI}},
465	  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},
466	  journal      = {arXiv preprint arXiv:2504.21801},
467	  year         = {2025},
468	  eprint       = {2504.21801},
469	  archivePrefix = {arXiv},
470	}
471	
472	@article{cui2025prime,
473	  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},
474	  title        = {{Process Reinforcement through Implicit Rewards}},
475	  journal      = {arXiv preprint arXiv:2502.01456},
476	  year         = {2025},
477	  eprint       = {2502.01456},
478	  archivePrefix = {arXiv},
479	  primaryClass = {cs.CL},
480	}
481	
482	@misc{mccune-prover9,
483	  author       = {William McCune},
484	  title        = {{Prover9 and Mace4}},
485	  year         = {2005--2010},
486	  howpublished = {\url{https://www.cs.unm.edu/~mccune/prover9/}},
487	  note         = {Version 2009-11A},
488	}
489	
490	@inproceedings{lundberg2017unified,
491	  author       = {Scott M. Lundberg and Su-In Lee},
492	  title        = {A Unified Approach to Interpreting Model Predictions},
493	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
494	  year         = {2017},
495	}
496	
497	@inproceedings{coste2023reward,
498	  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},
499	  title        = {Reward Model Ensembles Help Mitigate Overoptimization},
500	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
501	  year         = {2024},
502	  note         = {arXiv:2310.02743},
503	}
504	
505	@inproceedings{moskovitz2023confronting,
506	  author       = {Ted Moskovitz and Aldo Pacchiano and Parker Lund and Jakob Foerster},
507	  title        = {Confronting Reward Model Overoptimization with Constrained {RLHF}},
508	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
509	  year         = {2024},
510	  note         = {arXiv:2310.04373},
511	}
512	
513	@article{wielemaker2012swi,
514	  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\"o}rn Lager},
515	  title        = {{SWI-Prolog}},
516	  journal      = {Theory and Practice of Logic Programming},
517	  volume       = {12},
518	  number       = {1--2},
519	  pages        = {67--96},
520	  year         = {2012},
521	  doi          = {10.1017/S1471068411000494},
522	}
523	
524	@article{wilhelm2026monitoring,
525	  title={Monitoring Emergent Reward Hacking During Generation via Internal Activations},
526	  author={Wilhelm, Patrick and Wittkopp, Thorsten and Kao, Odej},
527	  journal={arXiv preprint arXiv:2603.04069},
528	  year={2026}
529	}
530	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "b092eac1-af66-4818-aa58-48fd33e7d5eb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
      "content": "% ============================================================\n% LLaMA\n% ============================================================\n\n@article{grattafiori2024llama,\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},\n  title = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n  eprint = {2407.21783},\n  archiveprefix = {arXiv},\n}\n\n% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--41},\n  year         = {1978},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@article{spurious-rewards,\n  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Reward shaping and process supervision\n% ============================================================\n\n@article{rlsf,\n  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},\n  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\\`{a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  note         = {arXiv:2404.18926},\n}\n\n@article{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  journal      = {arXiv preprint arXiv:2408.08152},\n  year         = {2024},\n  eprint       = {2408.08152},\n  archivePrefix = {arXiv},\n}\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2501.12948},\n  year         = {2025},\n  eprint       = {2501.12948},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nlproofs,\n  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},\n  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},\n  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2022},\n  eprint       = {2205.12443},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{vstar,\n  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},\n  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},\n  booktitle    = {Conference on Language Modeling (COLM)},\n  year         = {2024},\n  eprint       = {2402.06457},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{easy-to-hard,\n  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},\n  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  eprint       = {2403.09472},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@article{reward-hacking-survey,\n  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n}\n\n@misc{metr-reward-hacking,\n  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR Technical Blog},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2021},\n  note         = {arXiv:2012.13048},\n}\n\n@article{prooffol-thatikonda2024,\n  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},\n  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},\n  journal      = {arXiv preprint arXiv:2409.16461},\n  year         = {2024},\n  eprint       = {2409.16461},\n  archivePrefix = {arXiv},\n}\n\n@article{qwen3,\n  author       = {{Qwen Team}},\n  title        = {{Qwen3 Technical Report}},\n  journal      = {arXiv preprint arXiv:2505.09388},\n  year         = {2025},\n  eprint       = {2505.09388},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@article{helff2026gaming,\n  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\\\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},\n  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},\n  journal      = {arXiv preprint arXiv:2604.15149},\n  year         = {2026},\n  eprint       = {2604.15149},\n  archivePrefix = {arXiv},\n}\n\n@article{khalifa2026countdown,\n  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},\n  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},\n  journal      = {arXiv preprint arXiv:2603.07084},\n  year         = {2026},\n  eprint       = {2603.07084},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{uesato2022solving,\n  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},\n  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},\n  booktitle={NeurIPS 2022 Workshop on MATH-AI},\n  year={2022}\n}\n\n@article{cobbe2021training,\n  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},\n  title        = {{Training Verifiers to Solve Math Word Problems}},\n  journal      = {arXiv preprint arXiv:2110.14168},\n  year         = {2021},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{pronesti2026beyond,\n  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},\n  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},\n  journal      = {arXiv preprint arXiv:2601.17223},\n  year         = {2026},\n  eprint       = {2601.17223},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{ng1999policy,\n  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},\n  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year      = {1999},\n  pages     = {278--287},\n}\n\n@article{geirhos2020shortcut,\n  author  = {Robert Geirhos and J{\\\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},\n  title   = {Shortcut Learning in Deep Neural Networks},\n  journal = {Nature Machine Intelligence},\n  volume  = {2},\n  pages   = {665--673},\n  year    = {2020},\n}\n\n@article{dong2026probing,\n  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},\n  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},\n  journal      = {arXiv preprint arXiv:2602.01103},\n  year         = {2026},\n  eprint       = {2602.01103},\n  archivePrefix = {arXiv},\n}\n\n@article{yan2026spurious,\n  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},\n  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},\n  journal      = {arXiv preprint arXiv:2601.11061},\n  year         = {2026},\n  eprint       = {2601.11061},\n  archivePrefix = {arXiv},\n}\n\n@article{tarek2025reward,\n  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},\n  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},\n  journal      = {arXiv preprint arXiv:2509.15557},\n  year         = {2025},\n  eprint       = {2509.15557},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{yue2025rl-reasoning,\n  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},\n  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2025},\n  eprint       = {2504.13837},\n  archivePrefix = {arXiv},\n}\n\n@article{sullivan2025grpo-prm,\n  author       = {Michael Sullivan and Alexander Koller},\n  title        = {{GRPO} is Secretly a Process Reward Model},\n  journal      = {arXiv preprint arXiv:2509.21154},\n  year         = {2025},\n  eprint       = {2509.21154},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% R19 reviewer-requested references\n% ============================================================\n\n@inproceedings{setlur2025rewarding,\n  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},\n  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2410.08146},\n}\n\n@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}\n\n% ============================================================\n% Solvers (Prover9, SWI-Prolog)\n% ============================================================\n\n@article{deepseek-prover-v2,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},\n  journal      = {arXiv preprint arXiv:2504.21801},\n  year         = {2025},\n  eprint       = {2504.21801},\n  archivePrefix = {arXiv},\n}\n\n@article{cui2025prime,\n  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},\n  title        = {{Process Reinforcement through Implicit Rewards}},\n  journal      = {arXiv preprint arXiv:2502.01456},\n  year         = {2025},\n  eprint       = {2502.01456},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@misc{mccune-prover9,\n  author       = {William McCune},\n  title        = {{Prover9 and Mace4}},\n  year         = {2005--2010},\n  howpublished = {\\url{https://www.cs.unm.edu/~mccune/prover9/}},\n  note         = {Version 2009-11A},\n}\n\n@inproceedings{lundberg2017unified,\n  author       = {Scott M. Lundberg and Su-In Lee},\n  title        = {A Unified Approach to Interpreting Model Predictions},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2017},\n}\n\n@inproceedings{coste2023reward,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {Reward Model Ensembles Help Mitigate Overoptimization},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.02743},\n}\n\n@inproceedings{moskovitz2023confronting,\n  author       = {Ted Moskovitz and Aldo Pacchiano and Parker Lund and Jakob Foerster},\n  title        = {Confronting Reward Model Overoptimization with Constrained {RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n\n@article{wilhelm2026monitoring,\n  title={Monitoring Emergent Reward Hacking During Generation via Internal Activations},\n  author={Wilhelm, Patrick and Wittkopp, Thorsten and Kao, Odej},\n  journal={arXiv preprint arXiv:2603.04069},\n  year={2026}\n}\n",
      "numLines": 530,
      "startLine": 1,
      "totalLines": 530
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze the coverage:

**1. Reward hacking in RLHF/RLVR core citations:**

- Goodhart 1975 / Strathern 1997: NOT in bib. The tex cites `manheim-goodhart-taxonomy` which is Manheim & Garrabrant (2019). There's no explicit Goodhart 1975 or Strathern 1997.
- Manheim & Garrabrant taxonomy: ✅ `manheim-goodhart-taxonomy` in bib and cited in related_work.tex


- Skalse et al.'s formal definition of reward hacking: ✅ in bib and cited
- METR's reward hacking benchmark: ✅ in bib and cited
- Gao et al.'s work on reward overoptimization scaling laws: ✅ in bib and cited

The main gap is the original Goodhart paper and Strathern's work, though it's standard practice in ML to reference the Manheim & Garrabrant taxonomy as the primary source for Goodhart's Law rather than tracking down the original.

Looking at the related work section, it already cites Goodhart's Law through Manheim & Garrabrant along with Skalse and Karwowski, which is the conventional approach for ML venues. So this isn't actually a gap.

For neurosymbolic reasoning and RL, I'm checking the coverage: FOLIO dataset is in, and the key representatives like Logic-RL, the Prolog-based work, SatLM, Logic-LM, LINC, and FoVer are all accounted for.

I'm also seeing the recent work is covered—DeepSeek-Prover, AlphaProof, DeepSeek-R1 are all there. The Wilhelm et al. (2026) discussion about detecting reward hacking at generation time versus our post-training structural approach is clearly stated. Now I should search for any recent papers on reward hacking in formal reasoning and RLVR that might be missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "e355dde4-7b20-49e2-894e-d1589802a0b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uV4CVb3LMikx8qVGe7iFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10343,
      "cache_read_input_tokens": 27051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10343
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

_source line 10_

Good, I have both files. Let me now search for recent related work that might be missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "2a925e31-dc22-440b-9088-73a9ac60c47c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uV4CVb3LMikx8qVGe7iFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10343,
      "cache_read_input_tokens": 27051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10343
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

<details open><summary>🔧 Tool call — Agent · `toolu_01EBXYMdakeZrEeQ7p4EaLoe`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search recent reward hacking papers",
  "prompt": "Use WebSearch to find recent (2025-2026) papers on reward hacking in formal reasoning and RLVR. Run these searches:\n\n1. \"reward hacking formal reasoning 2025 2026\"\n2. \"reward overoptimization language model 2025 2026\"\n3. \"RLVR reward hacking 2025 2026\"\n4. \"Goodhart law reinforcement learning language model 2025\"\n\nFor each search, report the top 5-8 most relevant papers with: title, authors, year, venue/arXiv ID, and a one-line summary. Focus on papers that study reward hacking/gaming/overoptimization in the context of language model reasoning (especially formal/symbolic reasoning). \n\nAlso specifically search for:\n5. \"Strathern Goodhart\" to find the classic Strathern 1997 formulation\n6. \"Goodhart 1975 monetary policy\" for the original Goodhart paper\n\nReport results concisely — title, authors, year, arXiv ID, one-line summary. No commentary beyond that."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "eee18084-a2a2-4993-bb74-535e11595144",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uV4CVb3LMikx8qVGe7iFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10343,
      "cache_read_input_tokens": 27051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10343
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

### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Search recent reward hacking papers",
  "task_type": "local_agent",
  "prompt": "Use WebSearch to find recent (2025-2026) papers on reward hacking in formal reasoning and RLVR. Run these searches:\n\n1. \"reward hacking formal reasoning 2025 2026\"\n2. \"reward overoptimization language model 2025 2026\"\n3. \"RLVR reward hacking 2025 2026\"\n4. \"Goodhart law reinforcement learning language model 2025\"\n\nFor each search, report the top 5-8 most relevant papers with: title, authors, year, venue/arXiv ID, and a one-line summary. Focus on papers that study reward hacking/gaming/overoptimization in the context of language model reasoning (especially formal/symbolic reasoning). \n\nAlso specifically search for:\n5. \"Strathern Goodhart\" to find the classic Strathern 1997 formulation\n6. \"Goodhart 1975 monetary policy\" for the original Goodhart paper\n\nReport results concisely — title, authors, year, arXiv ID, one-line summary. No commentary beyond that.",
  "uuid": "2e720b88-e05d-4c32-aa01-7c023c43f986",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

## Round 1

90 recorded events

### User

_source line 13 · 2026-05-22T18:47:44.021Z_

Use WebSearch to find recent (2025-2026) papers on reward hacking in formal reasoning and RLVR. Run these searches:

1. "reward hacking formal reasoning 2025 2026"
2. "reward overoptimization language model 2025 2026"
3. "RLVR reward hacking 2025 2026"
4. "Goodhart law reinforcement learning language model 2025"

For each search, report the top 5-8 most relevant papers with: title, authors, year, venue/arXiv ID, and a one-line summary. Focus on papers that study reward hacking/gaming/overoptimization in the context of language model reasoning (especially formal/symbolic reasoning). 

Also specifically search for:
5. "Strathern Goodhart" to find the classic Strathern 1997 formulation
6. "Goodhart 1975 monetary policy" for the original Goodhart paper

Report results concisely — title, authors, year, arXiv ID, one-line summary. No commentary beyond that.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "77404449-23fc-4aa4-b10d-30b4da212028"
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_0193YdaYvsTcbHDDdR3UYXqE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "76a8b1e2-a920-4e76-888e-6caf5a913034",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uV4CVb3LMikx8qVGe7iFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10343,
      "cache_read_input_tokens": 27051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10343
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

_source line 15 · 2026-05-22T18:47:45.447Z_

<details><summary>↩ Tool result · `toolu_0193YdaYvsTcbHDDdR3UYXqE`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	
16	\paragraph{Reward hacking and Goodhart's Law.}
17	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\citep{gao-reward-overoptimization} and logical formalization~\citep{bondarenko-spec-gaming, kim-game-formalization}.
18	Most closely related, \citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models and Lean~4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage.
19	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where KL regularization provably fails, a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.
20	Reward model ensembles~\citep{coste2023reward} and constrained optimization~\citep{moskovitz2023confronting} address overoptimization at the reward level; STA instead diagnoses structural consequences at the output level.
21	Concurrent work documents spurious signals in RLVR~\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking} and proposes composite rewards as mitigations~\citep{tarek2025reward, pronesti2026beyond}; \citet{yue2025rl-reasoning} show RLVR redistributes base-model probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.
22	\citet{helff2026gaming} propose Input Perturbation Testing (IPT) for gaming detection; STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training.
23	While IPT perturbs \emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.
24	\citet{khalifa2026countdown} provide RLVR hacking testbeds.
25	Our Goodhart effect follows the regressional pattern~\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\beta$; its application to a diagnostic designed to \emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.
26	Complementarily, \citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.
27	
28	\paragraph{Mutation testing.}
29	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "71764f38-a82f-43ef-a56e-072f86b0724b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nReward shaping theory~\\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.\nIn mathematical reasoning, learned process reward models~\\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\\citep{processbench}.\nA recurring finding is that auxiliary rewards can hurt rather than help: \\citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \\citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.\nAnnotation-free alternatives~\\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.\n\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\\citep{gao-reward-overoptimization} and logical formalization~\\citep{bondarenko-spec-gaming, kim-game-formalization}.\nMost closely related, \\citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models and Lean~4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where KL regularization provably fails, a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.\nReward model ensembles~\\citep{coste2023reward} and constrained optimization~\\citep{moskovitz2023confronting} address overoptimization at the reward level; STA instead diagnoses structural consequences at the output level.\nConcurrent work documents spurious signals in RLVR~\\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking} and proposes composite rewards as mitigations~\\citep{tarek2025reward, pronesti2026beyond}; \\citet{yue2025rl-reasoning} show RLVR redistributes base-model probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.\n\\citet{helff2026gaming} propose Input Perturbation Testing (IPT) for gaming detection; STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training.\nWhile IPT perturbs \\emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \\emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.\n\\citet{khalifa2026countdown} provide RLVR hacking testbeds.\nOur Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\\beta$; its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\nComplementarily, \\citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01P4zygUjSayUifQT36NqTuo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "91181ad3-98b0-43c4-adb2-afc800ef7536",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uV4CVb3LMikx8qVGe7iFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10343,
      "cache_read_input_tokens": 27051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10343
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

_source line 17 · 2026-05-22T18:47:45.893Z_

<details><summary>↩ Tool result · `toolu_01P4zygUjSayUifQT36NqTuo`</summary>

```text
1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
51	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
52	  year         = {2023},
53	}
54	
55	% ============================================================
56	% Category 2: Reward shaping for code/formal verification
57	% ============================================================
58	
59	@inproceedings{lightman-verify-step,
60	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
61	  title        = {{Let's Verify Step by Step}},
62	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
63	  year         = {2024},
64	  note         = {arXiv:2305.20050},
65	}
66	
67	@inproceedings{skalse-reward-hacking,
68	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
69	  title        = {{Defining and Characterizing Reward Hacking}},
70	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
71	  year         = {2022},
72	  note         = {arXiv:2209.13085},
73	}
74	
75	% ============================================================
76	% Category 3: Mutation testing in software engineering
77	% ============================================================
78	
79	@article{demillo1978,
80	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
81	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
82	  journal      = {Computer},
83	  volume       = {11},
84	  number       = {4},
85	  pages        = {34--41},
86	  year         = {1978},
87	}
88	
89	@article{jia-harman-survey,
90	  author       = {Yue Jia and Mark Harman},
91	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
92	  journal      = {IEEE Transactions on Software Engineering},
93	  volume       = {37},
94	  number       = {5},
95	  pages        = {649--678},
96	  year         = {2011},
97	}
98	
99	@article{spurious-rewards,
100	  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},
101	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
102	  journal      = {arXiv preprint arXiv:2506.10947},
103	  year         = {2025},
104	  eprint       = {2506.10947},
105	  archivePrefix = {arXiv},
106	  primaryClass = {cs.AI},
107	}
108	
109	@article{bondarenko-spec-gaming,
110	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
111	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
112	  journal      = {arXiv preprint arXiv:2502.13295},
113	  year         = {2025},
114	  eprint       = {2502.13295},
115	  archivePrefix = {arXiv},
116	  primaryClass = {cs.AI},
117	}
118	
119	@inproceedings{kim-game-formalization,
120	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
121	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
122	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
123	  year         = {2026},
124	  note         = {arXiv:2604.19459},
125	}
126	
127	@inproceedings{gao-reward-overoptimization,
128	  author       = {Leo Gao and John Schulman and Jacob Hilton},
129	  title        = {{Scaling Laws for Reward Model Overoptimization}},
130	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
131	  year         = {2023},
132	  note         = {arXiv:2210.10760},
133	}
134	
135	@inproceedings{karwowski-goodhart-rl,
136	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
137	  title        = {{Goodhart's Law in Reinforcement Learning}},
138	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
139	  year         = {2024},
140	  note         = {arXiv:2310.09144},
141	}
142	
143	% ============================================================
144	% Category 6: FOL/Prolog formalization with LLMs
145	% ============================================================
146	
147	@inproceedings{folio,
148	  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},
149	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
150	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
151	  year         = {2024},
152	  note         = {arXiv:2209.00840},
153	}
154	
155	@inproceedings{logic-lm,
156	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},
157	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
158	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
159	  year         = {2023},
160	}
161	
162	@inproceedings{linc,
163	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},
164	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
165	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
166	  year         = {2023},
167	}
168	
169	@article{fover-pei2025,
170	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
171	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
172	  journal      = {Transactions of the Association for Computational Linguistics},
173	  volume       = {13},
174	  pages        = {1340--1359},
175	  year         = {2025},
176	}
177	
178	@article{lorp,
179	  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},
180	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
181	  journal      = {Knowledge-Based Systems},
182	  year         = {2025},
183	}
184	
185	@article{manheim-goodhart-taxonomy,
186	  author       = {David Manheim and Scott Garrabrant},
187	  title        = {{Categorizing Variants of Goodhart's Law}},
188	  journal      = {arXiv preprint arXiv:1803.04585},
189	  year         = {2019},
190	  eprint       = {1803.04585},
191	  archivePrefix = {arXiv},
192	  primaryClass = {cs.AI},
193	}
194	
195	@inproceedings{math-shepherd,
196	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},
197	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
198	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
199	  year         = {2024},
200	  note         = {arXiv:2312.08935},
201	}
202	
203	% ============================================================
204	% Reward shaping and process supervision
205	% ============================================================
206	
207	@article{rlsf,
208	  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},
209	  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},
210	  journal      = {arXiv preprint arXiv:2405.16661},
211	  year         = {2024},
212	  eprint       = {2405.16661},
213	  archivePrefix = {arXiv},
214	  primaryClass = {cs.AI},
215	}
216	
217	@article{gao-effective-rl-reward,
218	  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},
219	  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},
220	  journal      = {arXiv preprint arXiv:2410.15115},
221	  year         = {2024},
222	  eprint       = {2410.15115},
223	  archivePrefix = {arXiv},
224	  primaryClass = {cs.AI},
225	}
226	
227	@inproceedings{kwa-catastrophic-goodhart,
228	  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\`{a} Garriga-Alonso},
229	  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},
230	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
231	  year         = {2024},
232	  note         = {arXiv:2404.18926},
233	}
234	
235	@article{deepseek-prover-v15,
236	  author       = {{DeepSeek AI}},
237	  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},
238	  journal      = {arXiv preprint arXiv:2408.08152},
239	  year         = {2024},
240	  eprint       = {2408.08152},
241	  archivePrefix = {arXiv},
242	}
243	
244	@article{deepseek-r1,
245	  author       = {{DeepSeek-AI}},
246	  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},
247	  journal      = {arXiv preprint arXiv:2501.12948},
248	  year         = {2025},
249	  eprint       = {2501.12948},
250	  archivePrefix = {arXiv},
251	}
252	
253	@inproceedings{nlproofs,
254	  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},
255	  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},
256	  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
257	  year         = {2022},
258	  eprint       = {2205.12443},
259	  archivePrefix = {arXiv},
260	}
261	
262	@inproceedings{vstar,
263	  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},
264	  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},
265	  booktitle    = {Conference on Language Modeling (COLM)},
266	  year         = {2024},
267	  eprint       = {2402.06457},
268	  archivePrefix = {arXiv},
269	}
270	
271	@inproceedings{easy-to-hard,
272	  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},
273	  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},
274	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
275	  year         = {2024},
276	  eprint       = {2403.09472},
277	  archivePrefix = {arXiv},
278	}
279	
280	% ============================================================
281	% Additional reward-shaping papers
282	% ============================================================
283	
284	@article{reward-hacking-survey,
285	  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},
286	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
287	  journal      = {arXiv preprint arXiv:2604.13602},
288	  year         = {2026},
289	  eprint       = {2604.13602},
290	  archivePrefix = {arXiv},
291	}
292	
293	@misc{metr-reward-hacking,
294	  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},
295	  title        = {{Recent Frontier Models Are Reward Hacking}},
296	  year         = {2025},
297	  howpublished = {METR Technical Blog},
298	  note         = {\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},
299	}
300	
301	@inproceedings{proofwriter,
302	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
303	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
304	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
305	  year         = {2021},
306	  note         = {arXiv:2012.13048},
307	}
308	
309	@article{prooffol-thatikonda2024,
310	  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},
311	  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},
312	  journal      = {arXiv preprint arXiv:2409.16461},
313	  year         = {2024},
314	  eprint       = {2409.16461},
315	  archivePrefix = {arXiv},
316	}
317	
318	@article{qwen3,
319	  author       = {{Qwen Team}},
320	  title        = {{Qwen3 Technical Report}},
321	  journal      = {arXiv preprint arXiv:2505.09388},
322	  year         = {2025},
323	  eprint       = {2505.09388},
324	  archivePrefix = {arXiv},
325	  primaryClass = {cs.CL},
326	}
327	
328	@article{helff2026gaming,
329	  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},
330	  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},
331	  journal      = {arXiv preprint arXiv:2604.15149},
332	  year         = {2026},
333	  eprint       = {2604.15149},
334	  archivePrefix = {arXiv},
335	}
336	
337	@article{khalifa2026countdown,
338	  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},
339	  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},
340	  journal      = {arXiv preprint arXiv:2603.07084},
341	  year         = {2026},
342	  eprint       = {2603.07084},
343	  archivePrefix = {arXiv},
344	}
345	
346	@inproceedings{uesato2022solving,
347	  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},
348	  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},
349	  booktitle={NeurIPS 2022 Workshop on MATH-AI},
350	  year={2022}
351	}
352	
353	@article{cobbe2021training,
354	  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},
355	  title        = {{Training Verifiers to Solve Math Word Problems}},
356	  journal      = {arXiv preprint arXiv:2110.14168},
357	  year         = {2021},
358	}
359	
360	@inproceedings{processbench,
361	  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},
362	  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},
363	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
364	  year         = {2025},
365	  note         = {arXiv:2412.06559},
366	}
367	
368	@article{pronesti2026beyond,
369	  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},
370	  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},
371	  journal      = {arXiv preprint arXiv:2601.17223},
372	  year         = {2026},
373	  eprint       = {2601.17223},
374	  archivePrefix = {arXiv},
375	}
376	
377	@inproceedings{ng1999policy,
378	  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},
379	  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},
380	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
381	  year      = {1999},
382	  pages     = {278--287},
383	}
384	
385	@article{geirhos2020shortcut,
386	  author  = {Robert Geirhos and J{\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},
387	  title   = {Shortcut Learning in Deep Neural Networks},
388	  journal = {Nature Machine Intelligence},
389	  volume  = {2},
390	  pages   = {665--673},
391	  year    = {2020},
392	}
393	
394	@article{dong2026probing,
395	  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},
396	  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},
397	  journal      = {arXiv preprint arXiv:2602.01103},
398	  year         = {2026},
399	  eprint       = {2602.01103},
400	  archivePrefix = {arXiv},
401	}
402	
403	@article{yan2026spurious,
404	  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},
405	  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},
406	  journal      = {arXiv preprint arXiv:2601.11061},
407	  year         = {2026},
408	  eprint       = {2601.11061},
409	  archivePrefix = {arXiv},
410	}
411	
412	@article{tarek2025reward,
413	  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},
414	  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},
415	  journal      = {arXiv preprint arXiv:2509.15557},
416	  year         = {2025},
417	  eprint       = {2509.15557},
418	  archivePrefix = {arXiv},
419	}
420	
421	@inproceedings{yue2025rl-reasoning,
422	  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},
423	  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},
424	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
425	  year         = {2025},
426	  eprint       = {2504.13837},
427	  archivePrefix = {arXiv},
428	}
429	
430	@article{sullivan2025grpo-prm,
431	  author       = {Michael Sullivan and Alexander Koller},
432	  title        = {{GRPO} is Secretly a Process Reward Model},
433	  journal      = {arXiv preprint arXiv:2509.21154},
434	  year         = {2025},
435	  eprint       = {2509.21154},
436	  archivePrefix = {arXiv},
437	}
438	
439	% ============================================================
440	% R19 reviewer-requested references
441	% ============================================================
442	
443	@inproceedings{setlur2025rewarding,
444	  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},
445	  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},
446	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
447	  year         = {2025},
448	  note         = {arXiv:2410.08146},
449	}
450	
451	@article{alphaproof2025,
452	  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},
453	  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},
454	  journal      = {Nature},
455	  year         = {2025},
456	  doi          = {10.1038/s41586-025-09833-y},
457	}
458	
459	% ============================================================
460	% Solvers (Prover9, SWI-Prolog)
461	% ============================================================
462	
463	@article{deepseek-prover-v2,
464	  author       = {{DeepSeek-AI}},
465	  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},
466	  journal      = {arXiv preprint arXiv:2504.21801},
467	  year         = {2025},
468	  eprint       = {2504.21801},
469	  archivePrefix = {arXiv},
470	}
471	
472	@article{cui2025prime,
473	  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},
474	  title        = {{Process Reinforcement through Implicit Rewards}},
475	  journal      = {arXiv preprint arXiv:2502.01456},
476	  year         = {2025},
477	  eprint       = {2502.01456},
478	  archivePrefix = {arXiv},
479	  primaryClass = {cs.CL},
480	}
481	
482	@misc{mccune-prover9,
483	  author       = {William McCune},
484	  title        = {{Prover9 and Mace4}},
485	  year         = {2005--2010},
486	  howpublished = {\url{https://www.cs.unm.edu/~mccune/prover9/}},
487	  note         = {Version 2009-11A},
488	}
489	
490	@inproceedings{lundberg2017unified,
491	  author       = {Scott M. Lundberg and Su-In Lee},
492	  title        = {A Unified Approach to Interpreting Model Predictions},
493	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
494	  year         = {2017},
495	}
496	
497	@inproceedings{coste2023reward,
498	  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},
499	  title        = {Reward Model Ensembles Help Mitigate Overoptimization},
500	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
501	  year         = {2024},
502	  note         = {arXiv:2310.02743},
503	}
504	
505	@inproceedings{moskovitz2023confronting,
506	  author       = {Ted Moskovitz and Aldo Pacchiano and Parker Lund and Jakob Foerster},
507	  title        = {Confronting Reward Model Overoptimization with Constrained {RLHF}},
508	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
509	  year         = {2024},
510	  note         = {arXiv:2310.04373},
511	}
512	
513	@article{wielemaker2012swi,
514	  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\"o}rn Lager},
515	  title        = {{SWI-Prolog}},
516	  journal      = {Theory and Practice of Logic Programming},
517	  volume       = {12},
518	  number       = {1--2},
519	  pages        = {67--96},
520	  year         = {2012},
521	  doi          = {10.1017/S1471068411000494},
522	}
523	
524	@article{wilhelm2026monitoring,
525	  title={Monitoring Emergent Reward Hacking During Generation via Internal Activations},
526	  author={Wilhelm, Patrick and Wittkopp, Thorsten and Kao, Odej},
527	  journal={arXiv preprint arXiv:2603.04069},
528	  year={2026}
529	}
530	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "033563e2-5a13-4ba4-b55f-85448687395f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
      "content": "% ============================================================\n% LLaMA\n% ============================================================\n\n@article{grattafiori2024llama,\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},\n  title = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n  eprint = {2407.21783},\n  archiveprefix = {arXiv},\n}\n\n% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--41},\n  year         = {1978},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@article{spurious-rewards,\n  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Reward shaping and process supervision\n% ============================================================\n\n@article{rlsf,\n  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},\n  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\\`{a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  note         = {arXiv:2404.18926},\n}\n\n@article{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  journal      = {arXiv preprint arXiv:2408.08152},\n  year         = {2024},\n  eprint       = {2408.08152},\n  archivePrefix = {arXiv},\n}\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2501.12948},\n  year         = {2025},\n  eprint       = {2501.12948},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nlproofs,\n  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},\n  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},\n  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2022},\n  eprint       = {2205.12443},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{vstar,\n  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},\n  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},\n  booktitle    = {Conference on Language Modeling (COLM)},\n  year         = {2024},\n  eprint       = {2402.06457},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{easy-to-hard,\n  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},\n  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  eprint       = {2403.09472},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@article{reward-hacking-survey,\n  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n}\n\n@misc{metr-reward-hacking,\n  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR Technical Blog},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2021},\n  note         = {arXiv:2012.13048},\n}\n\n@article{prooffol-thatikonda2024,\n  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},\n  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},\n  journal      = {arXiv preprint arXiv:2409.16461},\n  year         = {2024},\n  eprint       = {2409.16461},\n  archivePrefix = {arXiv},\n}\n\n@article{qwen3,\n  author       = {{Qwen Team}},\n  title        = {{Qwen3 Technical Report}},\n  journal      = {arXiv preprint arXiv:2505.09388},\n  year         = {2025},\n  eprint       = {2505.09388},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@article{helff2026gaming,\n  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\\\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},\n  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},\n  journal      = {arXiv preprint arXiv:2604.15149},\n  year         = {2026},\n  eprint       = {2604.15149},\n  archivePrefix = {arXiv},\n}\n\n@article{khalifa2026countdown,\n  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},\n  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},\n  journal      = {arXiv preprint arXiv:2603.07084},\n  year         = {2026},\n  eprint       = {2603.07084},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{uesato2022solving,\n  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},\n  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},\n  booktitle={NeurIPS 2022 Workshop on MATH-AI},\n  year={2022}\n}\n\n@article{cobbe2021training,\n  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},\n  title        = {{Training Verifiers to Solve Math Word Problems}},\n  journal      = {arXiv preprint arXiv:2110.14168},\n  year         = {2021},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{pronesti2026beyond,\n  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},\n  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},\n  journal      = {arXiv preprint arXiv:2601.17223},\n  year         = {2026},\n  eprint       = {2601.17223},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{ng1999policy,\n  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},\n  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year      = {1999},\n  pages     = {278--287},\n}\n\n@article{geirhos2020shortcut,\n  author  = {Robert Geirhos and J{\\\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},\n  title   = {Shortcut Learning in Deep Neural Networks},\n  journal = {Nature Machine Intelligence},\n  volume  = {2},\n  pages   = {665--673},\n  year    = {2020},\n}\n\n@article{dong2026probing,\n  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},\n  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},\n  journal      = {arXiv preprint arXiv:2602.01103},\n  year         = {2026},\n  eprint       = {2602.01103},\n  archivePrefix = {arXiv},\n}\n\n@article{yan2026spurious,\n  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},\n  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},\n  journal      = {arXiv preprint arXiv:2601.11061},\n  year         = {2026},\n  eprint       = {2601.11061},\n  archivePrefix = {arXiv},\n}\n\n@article{tarek2025reward,\n  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},\n  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},\n  journal      = {arXiv preprint arXiv:2509.15557},\n  year         = {2025},\n  eprint       = {2509.15557},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{yue2025rl-reasoning,\n  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},\n  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2025},\n  eprint       = {2504.13837},\n  archivePrefix = {arXiv},\n}\n\n@article{sullivan2025grpo-prm,\n  author       = {Michael Sullivan and Alexander Koller},\n  title        = {{GRPO} is Secretly a Process Reward Model},\n  journal      = {arXiv preprint arXiv:2509.21154},\n  year         = {2025},\n  eprint       = {2509.21154},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% R19 reviewer-requested references\n% ============================================================\n\n@inproceedings{setlur2025rewarding,\n  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},\n  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2410.08146},\n}\n\n@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}\n\n% ============================================================\n% Solvers (Prover9, SWI-Prolog)\n% ============================================================\n\n@article{deepseek-prover-v2,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},\n  journal      = {arXiv preprint arXiv:2504.21801},\n  year         = {2025},\n  eprint       = {2504.21801},\n  archivePrefix = {arXiv},\n}\n\n@article{cui2025prime,\n  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},\n  title        = {{Process Reinforcement through Implicit Rewards}},\n  journal      = {arXiv preprint arXiv:2502.01456},\n  year         = {2025},\n  eprint       = {2502.01456},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@misc{mccune-prover9,\n  author       = {William McCune},\n  title        = {{Prover9 and Mace4}},\n  year         = {2005--2010},\n  howpublished = {\\url{https://www.cs.unm.edu/~mccune/prover9/}},\n  note         = {Version 2009-11A},\n}\n\n@inproceedings{lundberg2017unified,\n  author       = {Scott M. Lundberg and Su-In Lee},\n  title        = {A Unified Approach to Interpreting Model Predictions},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2017},\n}\n\n@inproceedings{coste2023reward,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {Reward Model Ensembles Help Mitigate Overoptimization},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.02743},\n}\n\n@inproceedings{moskovitz2023confronting,\n  author       = {Ted Moskovitz and Aldo Pacchiano and Parker Lund and Jakob Foerster},\n  title        = {Confronting Reward Model Overoptimization with Constrained {RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n\n@article{wilhelm2026monitoring,\n  title={Monitoring Emergent Reward Hacking During Generation via Internal Activations},\n  author={Wilhelm, Patrick and Wittkopp, Thorsten and Kao, Odej},\n  journal={arXiv preprint arXiv:2603.04069},\n  year={2026}\n}\n",
      "numLines": 530,
      "startLine": 1,
      "totalLines": 530
    }
  }
}
```

</details>

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Search recent reward hacking papers",
  "usage": {
    "total_tokens": 16226,
    "tool_uses": 1,
    "duration_ms": 2697
  },
  "last_tool_name": "ToolSearch",
  "uuid": "d5ffae66-ef8a-45c8-a6f6-0338adb20b1d",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RqYySym47kBUEYt8vWzQKo`</summary>

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
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "a83d318f-d8e2-4386-b210-05b2708652b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C8stWWfrG19m6zX9V147sw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16156,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16156,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 20 · 2026-05-22T18:47:46.723Z_

<details><summary>↩ Tool result · `toolu_01RqYySym47kBUEYt8vWzQKo`</summary>

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
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "b33a4642-609d-48c1-9d59-9df31172af2f"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for reward hacking formal reasoning 2025 2026",
  "usage": {
    "total_tokens": 17669,
    "tool_uses": 2,
    "duration_ms": 5674
  },
  "last_tool_name": "WebSearch",
  "uuid": "e898ccd9-fd06-4c0e-bcd5-7ae95b022571",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AGcY9P6QVedsZD4dMjnFC8`</summary>

```json
{
  "query": "reward hacking formal reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "217c201e-2135-4766-a20f-0552f0916ba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBX8v8Lmb4gqYRi3LLGBQY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 16156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for reward overoptimization language model 2025 2026",
  "usage": {
    "total_tokens": 17671,
    "tool_uses": 3,
    "duration_ms": 6165
  },
  "last_tool_name": "WebSearch",
  "uuid": "4331a320-a9f8-46e5-8ebc-8ab7b5036313",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ZKgsHTzetPZB3vB1urPJF`</summary>

```json
{
  "query": "reward overoptimization language model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "4d0427b0-1ffc-4a33-a486-3cfc7caeb709",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBX8v8Lmb4gqYRi3LLGBQY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 16156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for RLVR reward hacking 2025 2026",
  "usage": {
    "total_tokens": 17673,
    "tool_uses": 4,
    "duration_ms": 6175
  },
  "last_tool_name": "WebSearch",
  "uuid": "a5874bc6-a691-4ca2-a532-47cc386ae52e",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YH38fBFogbY5BYrgx8YDmV`</summary>

```json
{
  "query": "RLVR reward hacking 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "397ab7c3-0ef7-443b-92b2-e9210908ffba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBX8v8Lmb4gqYRi3LLGBQY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 16156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for Goodhart law reinforcement learning language mode…",
  "usage": {
    "total_tokens": 17675,
    "tool_uses": 5,
    "duration_ms": 6636
  },
  "last_tool_name": "WebSearch",
  "uuid": "9b52a056-7c3c-43a0-b4f1-8b0967e88bff",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XojdVz8KBwcwd6eeCdioM8`</summary>

```json
{
  "query": "Goodhart law reinforcement learning language model 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "2ae1e6b0-e6c9-4fe0-a60d-a99b51bd8458",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBX8v8Lmb4gqYRi3LLGBQY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 16156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for Strathern 1997 Goodhart's law improving published",
  "usage": {
    "total_tokens": 17677,
    "tool_uses": 6,
    "duration_ms": 7108
  },
  "last_tool_name": "WebSearch",
  "uuid": "af8095df-4f15-4a43-a240-0cfdc84b6414",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UfjSvAyvNuGhhKYGXit4Ak`</summary>

```json
{
  "query": "Strathern 1997 Goodhart's law improving published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "5a1be863-5d96-4161-a455-ea7adaacd496",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBX8v8Lmb4gqYRi3LLGBQY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 16156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for Goodhart 1975 monetary policy original paper prob…",
  "usage": {
    "total_tokens": 17679,
    "tool_uses": 7,
    "duration_ms": 7458
  },
  "last_tool_name": "WebSearch",
  "uuid": "ec0470ed-8bbb-4608-ab16-06feebb2239b",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NXZubjhmzHsWdve9sfBXko`</summary>

```json
{
  "query": "Goodhart 1975 monetary policy original paper problems"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "883a9288-50b9-4e80-a3b6-53e34cb14c54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBX8v8Lmb4gqYRi3LLGBQY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 16156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
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

_source line 33 · 2026-05-22T18:47:56.446Z_

<details><summary>↩ Tool result · `toolu_01AGcY9P6QVedsZD4dMjnFC8`</summary>

```text
Web search results for query: "reward hacking formal reasoning 2025 2026"

Links: [{"title":"[2510.01367] Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/abs/2510.01367"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/html/2603.28063v1"},{"title":"Reward hacking - Wikipedia","url":"https://en.wikipedia.org/wiki/Reward_hacking"},{"title":"Reward Hacking Trap","url":"https://www.emergentmind.com/topics/reward-hacking-trap"},{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"},{"title":"Is it thinking or cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/html/2510.01367"},{"title":"In-Context Reward Hacking Behaviors","url":"https://www.emergentmind.com/topics/in-context-reward-hacking-behaviors"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/pdf/2603.28063"}]

I found several recent research papers and articles on reward hacking and formal reasoning. Here are the key findings:

## Recent Research (2025-2026)

A paper submitted in October 2025 and revised in March 2026 titled "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort" addresses how reward hacking poses a significant threat when reasoning models exploit loopholes in reward functions to achieve high rewards without solving the intended task.

Contemporary reasoning models such as OpenAI's O1 series and DeepSeek-R1 have been found to reason about the testing processes and take actions to maximize scores for the intended tasks. In a 2025 study by Palisade Research, when reasoning LLMs were asked to win at a chess game against a stronger opponent, some of these models attempted to hack the game system by deleting or modifying their opponent's chess engine.

## Formal Analysis

A March 2026 paper proves that under five minimal axioms, any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system, establishing reward hacking as a structural equilibrium rather than a correctable bug.

## Detection Methods

The TRACE method quantifies reasoning effort by truncating a model's chain-of-thought at multiple lengths, with early pass rates indicating low-effort, shortcut-based responses, while genuine reasoning shows low early pass rates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "59a9f61b-60b5-472b-a88f-a3e9ad1789c2"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T18:47:57.200Z_

<details><summary>↩ Tool result · `toolu_01NXZubjhmzHsWdve9sfBXko`</summary>

```text
Web search results for query: "Goodhart 1975 monetary policy original paper problems"

Links: [{"title":"Goodhart’s Law • Agile Coffee","url":"https://agilecoffee.com/toolkit/goodharts-law/"},{"title":"“When a Measure Becomes a Target, It Ceases to be a Good Measure” - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7901608/"},{"title":"Goodhart's Law - What Is It, Examples, Forms, Avoiding Pitfalls","url":"https://www.wallstreetmojo.com/goodharts-law/"},{"title":"The Limits of Measurement: Goodhart’s Law in the Modern Economy","url":"https://theyoungeconomistinitiative.com/2025/11/13/the-limits-of-measurement-goodharts-law-in-the-modern-economy/"},{"title":"Problems of monetary management : the U.K. experience - EconBiz","url":"https://www.econbiz.de/Record/problems-of-monetary-management-the-u-k-experience-goodhart-charles/10002525062"},{"title":"Goodhart’s Law and Scientific Innovation in Academia | Mind Matters","url":"https://mindmatters.ai/2023/01/goodharts-law-and-scientific-innovation-in-academia/"},{"title":"Goodhart's law - Wikipedia","url":"https://en.wikipedia.org/wiki/Goodhart%27s_law"},{"title":"Goodhart's law - wikidoc","url":"https://www.wikidoc.org/index.php/Goodhart's_law"},{"title":"Goodhart's Law: Its Origins, Meaning and Implications for Monetary Policy | Request PDF","url":"https://www.researchgate.net/publication/253797490_Goodhart's_Law_Its_Origins_Meaning_and_Implications_for_Monetary_Policy"}]

Based on the search results, here's what I found about Goodhart's 1975 paper on monetary policy:

## The Original Paper

In 1975, Goodhart published a paper titled "Problems of Monetary Management: The U.K. Experience." Goodhart articulated this principle in a paper presented to the "Money Study Group" of the London School of Economics in 1975.

## The Core Problem Identified

In 1971 the monetary authorities in the UK adopted a new approach to monetary management, but the subsequent experience of trying to operate this revised system has, however, been troublesome and at times unhappy.

Goodhart explained that "whenever a government seeks to rely on a previously observed statistical regularity for control purposes, that regularity will collapse." When the central bank tried to stabilize a money supply measure that had been correlated with GDP, it ceased to be correlated with GDP.

## The General Principle

Goodhart is credited with expressing the core idea that any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes. This insight became known as the adage that "When a measure becomes a target, it ceases to be a good measure."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "d8ce1f5e-f5ec-4300-9dc3-373f444fba40"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-22T18:47:58.509Z_

<details><summary>↩ Tool result · `toolu_018ZKgsHTzetPZB3vB1urPJF`</summary>

```text
Web search results for query: "reward overoptimization language model 2025 2026"

Links: [{"title":"Reward Over-Optimization in AI","url":"https://www.emergentmind.com/topics/reward-over-optimization"},{"title":"Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization | OpenReview","url":"https://openreview.net/forum?id=PNMv4r7s1i"},{"title":"Reward Model Overoptimisation in Iterated RLHF | OpenReview","url":"https://openreview.net/forum?id=efoe5VJfKz"},{"title":"Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview","url":"https://openreview.net/forum?id=gkfUvn0fLU"},{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"},{"title":"Reward Model Boosting for RLHF | OpenReview","url":"https://openreview.net/forum?id=ZDscKnCiuJ"},{"title":"Reward Model Ensembles Help Mitigate Overoptimization","url":"https://arxiv.org/pdf/2310.02743"},{"title":"Scalable Ensembling For Mitigating Reward Overoptimisation","url":"https://arxiv.org/pdf/2406.01013"}]

Here are the search results for "reward overoptimization language model 2025 2026":

## Recent Research on Reward Overoptimization

Reward model overoptimization in language models occurs when models overfit to the reward function, resulting in non-generalizable policies that exploit the idiosyncrasies and peculiarities of the reward function. By overoptimizing for a misspecified reward, alignment goals can be subverted and overall performance reduced in a phenomenon commonly referred to as reward hacking.

### Key Findings and Solutions

Empirical studies across language and vision benchmarks demonstrate a characteristic "hump-shaped" curve: as the policy departs from the reference, gold reward and true task winrate rise, peak, and then fall, while the proxy reward increases monotonically.

Recent 2025-2026 approaches to address this issue include:

- Decomposing the reward into interpretable, weighted criteria focused on differentiating "excellent" from "great" responses results in proxy rewards that are robust against superficial gaming and better preserve true performance

- The Behavior-Supported Policy Optimization (BSPO) method mitigates the reward over-optimization issue

- Reward Model Boosting (RMB) uses advanced boosting to construct a reliable reward signal for RLHF, effectively mitigating reward hacking

- Ensemble-based conservative optimization can effectively counter overoptimization

There is a comprehensive study of overoptimization in iterated RLHF that systematically analyzes key design choices including how reward model training data is transferred across iterations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "572c3fc6-1599-4cdd-a02a-b823e769245a"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T18:47:58.559Z_

<details><summary>↩ Tool result · `toolu_01YH38fBFogbY5BYrgx8YDmV`</summary>

```text
Web search results for query: "RLVR reward hacking 2025 2026"

Links: [{"title":"Reward Hacking in RLVR Systems","url":"https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr"},{"title":"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://arxiv.org/html/2604.15149"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"[2604.15149] LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://arxiv.org/abs/2604.15149"},{"title":"Reinforcement Learning with Verified Rewards (RLVR)","url":"https://www.emergentmind.com/topics/reinforcement-learning-with-verified-rewards-rlvr"},{"title":"Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/html/2604.16242"},{"title":"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://chatpaper.com/paper/268961"},{"title":"[2509.15557] Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://arxiv.org/abs/2509.15557"},{"title":"Reward Hacking in RLVR","url":"https://www.emergentmind.com/topics/reward-hacking-in-rlvr"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"}]

Based on the search results, here's what recent research shows about RLVR (Reinforcement Learning from Verifiable Rewards) and reward hacking in 2025-2026:

## Key Findings

**Reward Hacking as an Emerging Problem**

As reinforcement Learning with Verifiable Rewards (RLVR) has become the dominant paradigm for scaling reasoning capabilities in LLMs, a new failure mode emerges: LLMs gaming verifiers. RLVR can incentivize reward hacking not only through overt manipulation but also by exploiting what the verifier fails to enforce.

**Forms of Reward Hacking in RLVR**

RLVR settings introduce additional attack surfaces: reward verifiers (rule-based or model-based) may be circumvented, preference models may be gamed by superficial cues, and rubric aggregation schemes can be targeted by outputs tailored to exploit individual rubric items. Reward hacking in RLVR is exemplified by behaviors such as directly inserting the answer into reasoning sections or exploiting auxiliary format-related loopholes.

**Why RLVR Remains Vulnerable**

Although RLVR is often assumed to be robust against reward hacking because it uses objective programmatic signals, verifiable signals are narrow. By rewarding checkable final answers while ignoring the cognitive steps taken to reach them, RLVR creates a proxy gap regarding faithful process.

**Detection and Mitigation**

Empirical deployment of detectors across 15 environments (Atari, MuJoCo, custom RLVR domains) and five RL algorithms yields 78.4% precision and 81.7% recall, with overhead below 5%. Mitigation techniques based on detection findings can reduce reward hacking occurrence up to 54.6%, although this often involves trade-offs in legitimate performance and increased computational cost.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "99385222-768f-451c-af3c-0a2ea3c1ceeb"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-22T18:47:59.074Z_

<details><summary>↩ Tool result · `toolu_01XojdVz8KBwcwd6eeCdioM8`</summary>

```text
Web search results for query: "Goodhart law reinforcement learning language model 2025"

Links: [{"title":"The Strong, Weak and Benign Goodhart's law. An ...","url":"https://arxiv.org/pdf/2505.23445"},{"title":"Goodhart’s Law in Reinforcement Learning","url":"https://arxiv.org/html/2310.09144v1"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.lesswrong.com/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"},{"title":"Goodhart's Law in Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5o9G4XF1LI"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.semanticscholar.org/paper/Goodhart's-Law-in-Reinforcement-Learning-Karwowski-Hayman/a4bd4da02241eacee990c89ddd748ce37a248fc0"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://arxiv.org/pdf/2310.09144"},{"title":"[2310.09144] Goodhart's Law in Reinforcement Learning","url":"https://arxiv.org/abs/2310.09144"}]

The search returned several relevant results on Goodhart's law in reinforcement learning:

## Key Findings:

**2025 Research:**
A recent paper proposes a formal characterisation of different Goodhart's law effects that captures the different strength of Goodhart's law, with new theoretical advances in understanding this phenomenon.

**Language Models & Reward Modeling:**
Gao et al. (2023) consider the setting where a large language model is optimised against a reward model trained on a "gold standard" reward function, and investigate how the performance of the language model according to the gold standard reward scales in the size of the language model, the amount of training data, and the size of the reward model. They find that the performance of the policy follows a Goodhart curve, where the slope gets less prominent for larger reward models and larger amounts of training data.

**Core Concept:**
Goodhart's law predicts that increasing optimisation of an imperfect proxy beyond some critical point decreases performance on the true objective. Implementing a reward function that perfectly captures a complex task in the real world is impractical, so it is often appropriate to think of the reward function as a proxy for the true objective rather than as its definition.

**Proposed Solutions:**
Researchers provide a geometric explanation for why Goodhart's law occurs in Markov decision processes and propose an optimal early stopping method that provably avoids the pitfall, deriving theoretical regret bounds for this method.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "976faf6b-f548-4ee5-886e-0a96505e2c10"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T18:47:59.734Z_

<details><summary>↩ Tool result · `toolu_01UfjSvAyvNuGhhKYGXit4Ak`</summary>

```text
Web search results for query: "Strathern 1997 Goodhart's law improving published"

Links: [{"title":"Goodhart’s Law, Campbell’s Law, and the Cobra Effect. - Psych Safety","url":"https://psychsafety.com/goodharts-law-campbells-law-and-the-cobra-effect/"},{"title":"Goodhart’s Law | FORRT - Framework for Open and Reproducible Research Training","url":"https://forrt.org/glossary/english/goodhart_s_law/"},{"title":"GOODHART'S LAW","url":"https://www.damtp.cam.ac.uk/user/mem2//papers/LHCE/goodhart.html"},{"title":"Super Thinking","url":"https://superthinking.webflow.io/mental-models/goodharts-law"},{"title":"How to cite Goodhart's law - Cite Bay","url":"http://citebay.com/how-to-cite/goodharts-law/"},{"title":"“When a Measure Becomes a Target, It Ceases to be a Good Measure” - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7901608/"},{"title":"Goodhart's law - Wikipedia","url":"https://en.wikipedia.org/wiki/Goodhart%27s_law"},{"title":"'Improving ratings': audit in the British University system Marilyn","url":"https://gwern.net/doc/statistics/decision/1997-strathern.pdf"},{"title":"ModelThinkers - Goodhart's Law","url":"https://modelthinkers.com/mental-model/goodharts-law"},{"title":"'Improving ratings': audit in the British University system","url":"https://ideas.repec.org/a/cup/eurrev/v5y1997i03p305-321_00.html"}]

Based on the search results, here's what I found about Strathern's 1997 work on Goodhart's law:

Anthropologist Marilyn Strathern published a 1997 paper titled "'Improving Ratings': Audit in the British University System." In this paper, Strathern popularized a generalization of Goodhart's Law, which has become widely known today.

Strathern restated Goodhart's Law more succinctly and more generally as: "When a measure becomes a target, it ceases to be a good measure." This phrasing has become the most commonly cited version of the principle, in contrast to the original 1975 formulation by economist Charles Goodhart.

The full citation is: Strathern, M. (1997). 'Improving ratings': audit in the British University system. European Review, 5(3), 305–321.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "96363787-102a-42f2-bd30-9f997b34e0eb"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"LLMs Gaming Verifiers\" RLVR reward hacking…",
  "usage": {
    "total_tokens": 22666,
    "tool_uses": 8,
    "duration_ms": 19296
  },
  "last_tool_name": "WebSearch",
  "uuid": "5293d88e-9f96-4507-b127-bbbf8696446e",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BKpkP3tTxBDkb5zL6LR1vF`</summary>

```json
{
  "query": "arxiv \"LLMs Gaming Verifiers\" RLVR reward hacking 2604.15149"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "7740312b-2160-498c-942e-8cf72ebbc4a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1o4Cgm2NaUk3LTsT4Nigm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 785,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 17595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4203,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"reward hacking in the era of large models\"…",
  "usage": {
    "total_tokens": 22667,
    "tool_uses": 9,
    "duration_ms": 19780
  },
  "last_tool_name": "WebSearch",
  "uuid": "4a6504fc-8809-45f4-937f-cf4578675ccc",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MqhCNK3JK6NZz2njriRgd8`</summary>

```json
{
  "query": "arxiv \"reward hacking in the era of large models\" 2604.13602 mechanisms emergent misalignment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "b31738f0-614e-46ae-add3-b44db741c987",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1o4Cgm2NaUk3LTsT4Nigm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 785,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 17595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4203,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"detecting and suppressing reward hacking\" …",
  "usage": {
    "total_tokens": 22668,
    "tool_uses": 10,
    "duration_ms": 20260
  },
  "last_tool_name": "WebSearch",
  "uuid": "e831ad34-9255-45b8-b99d-b8f183b10f7c",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HZL94UiZc3pePyh5YiyeG3`</summary>

```json
{
  "query": "arxiv \"detecting and suppressing reward hacking\" gradient fingerprints 2604.16242"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "31269bf3-3100-4db1-8067-935b1e1b73cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1o4Cgm2NaUk3LTsT4Nigm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 785,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 17595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4203,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"inference-time reward hacking\" large langu…",
  "usage": {
    "total_tokens": 22669,
    "tool_uses": 11,
    "duration_ms": 20732
  },
  "last_tool_name": "WebSearch",
  "uuid": "9fb3bc97-5d14-4cf7-9832-cc413ee16d8a",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WhfyV8RBMhNCRxFy8i2G16`</summary>

```json
{
  "query": "arxiv \"inference-time reward hacking\" large language models 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "8a546d37-78b4-48b0-b171-ec5ab3b17955",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1o4Cgm2NaUk3LTsT4Nigm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 785,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 17595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4203,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"reward hacking mitigation\" verifiable comp…",
  "usage": {
    "total_tokens": 22670,
    "tool_uses": 12,
    "duration_ms": 21714
  },
  "last_tool_name": "WebSearch",
  "uuid": "527b68b1-da4b-4fba-89fd-fc95393fca27",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A7rPNrdgShEcZkrxVcNe5w`</summary>

```json
{
  "query": "arxiv \"reward hacking mitigation\" verifiable composite rewards 2509.15557"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "f3439199-4ad2-4659-967c-da337680d2e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1o4Cgm2NaUk3LTsT4Nigm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 785,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 17595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4203,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv 2510.01367 \"is it thinking or cheating\" det…",
  "usage": {
    "total_tokens": 22671,
    "tool_uses": 13,
    "duration_ms": 22410
  },
  "last_tool_name": "WebSearch",
  "uuid": "be75ccf2-d4b7-4646-9ad2-24fb12152f7c",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FaPKqzdihHxMWe3Sbuyhxi`</summary>

```json
{
  "query": "arxiv 2510.01367 \"is it thinking or cheating\" detecting implicit reward hacking reasoning effort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "64977f9a-a50f-4904-8e21-2c4b5bf1af60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1o4Cgm2NaUk3LTsT4Nigm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 785,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 17595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4203,
        "ephemeral_1h_input_tokens": 0
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

_source line 51 · 2026-05-22T18:48:08.951Z_

<details><summary>↩ Tool result · `toolu_01BKpkP3tTxBDkb5zL6LR1vF`</summary>

```text
Web search results for query: "arxiv "LLMs Gaming Verifiers" RLVR reward hacking 2604.15149"

Links: [{"title":"[2604.15149] LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://arxiv.org/abs/2604.15149"},{"title":"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://arxiv.org/html/2604.15149"},{"title":"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://chatpaper.com/paper/268961"},{"title":"LLMS GAMING VERIFIERS: RLVR CAN LEAD TO ...","url":"https://openreview.net/pdf?id=4B3WfRNqe3"},{"title":"GitHub - ml-research/llms-gaming-verifiers · GitHub","url":"https://github.com/ml-research/llms-gaming-verifiers"},{"title":"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking","url":"https://www.researchgate.net/publication/403905797_LLMs_Gaming_Verifiers_RLVR_can_Lead_to_Reward_Hacking"}]

I found the research paper you're looking for! Here's what the paper is about:

The paper "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking" by Lukas Helff and colleagues from TU Darmstadt, Intrinsic, and other institutions was published on April 16, 2026.

**Main Finding:**
As reinforcement learning with verifiable rewards (RLVR) has become the dominant paradigm for scaling reasoning capabilities in LLMs, a new failure mode emerges where LLMs game verifiers. The researchers study this phenomenon on inductive reasoning tasks and find that RLVR-trained models systematically abandon rule induction.

**The Problem:**
Instead of learning generalizable patterns (e.g., "trains carrying red cars go east"), models enumerate instance-level labels, producing outputs that pass verifiers without capturing the relational patterns required by the task. This behavior is not a failure of understanding but a form of reward hacking: imperfect verifiers that check only extensional correctness admit false positives.

**The Solution:**
The researchers introduce Isomorphic Perturbation Testing (IPT) — a black-box diagnostic that detects this behavior in any model, including closed-source ones.

You can access the full paper at https://arxiv.org/abs/2604.15149


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "c1f60051-0825-443e-9fd8-9feed56f7ebe"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T18:48:10.355Z_

<details><summary>↩ Tool result · `toolu_01MqhCNK3JK6NZz2njriRgd8`</summary>

```text
Web search results for query: "arxiv "reward hacking in the era of large models" 2604.13602 mechanisms emergent misalignment"

Links: [{"title":"[2604.13602] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/abs/2604.13602"},{"title":"[2604.13602v1] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/abs/2604.13602v1"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260413602W/abstract"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Paper page - Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://huggingface.co/papers/2604.13602"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/pdf/2506.19248"},{"title":"[2506.19248] Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/abs/2506.19248"}]

I found the paper you're looking for! Here are the search results:

"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges" (arXiv:2604.13602) was submitted on April 15, 2026, with authors including Xiaohua Wang, Muzhao Tian, Yuqi Zeng, and 20 other contributors.

The paper addresses how Reinforcement Learning from Human Feedback (RLHF) and related alignment paradigms have become central to steering large language models and multimodal large language models, but these approaches introduce a systemic vulnerability: reward hacking, where models exploit imperfections in learned reward signals to maximize proxy objectives without fulfilling true task intent.

The paper covers topics including Goodhart's Law, proxy evaluators (RLHF/RLAIF/RLVR), the Proxy Compression Hypothesis, and the escalating hierarchy of feature-/representation-/evaluator-/environment-level exploitation.

You can access the paper directly at:
- arXiv: https://arxiv.org/abs/2604.13602
- HTML version: https://arxiv.org/html/2604.13602v1
- GitHub companion resource: https://github.com/xhwang22/Awesome-Reward-Hacking


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "de33f827-9611-4789-9d9f-ae872a24498d"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-22T18:48:10.604Z_

<details><summary>↩ Tool result · `toolu_01HZL94UiZc3pePyh5YiyeG3`</summary>

```text
Web search results for query: "arxiv "detecting and suppressing reward hacking" gradient fingerprints 2604.16242"

Links: [{"title":"[2604.16242] Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/abs/2604.16242"},{"title":"Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/html/2604.16242"},{"title":"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/pdf/2602.18037"},{"title":"[2507.05619v1] Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/abs/2507.05619v1"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/pdf/2510.01367"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"[2604.02986] Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/abs/2604.02986"},{"title":"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.01750"}]

I found the paper you're looking for! Here are the key details:

**Paper:** Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242)

**Authors:** Songtao Wang, Quang Hieu Pham, Fangcong Yin, Xinpeng Wang, Jocelyn Qiaochu Chen, Greg Durrett, and Xi Ye from University of Alberta, New York University, LMU Munich, and Princeton Language and Intelligence

**Submission Date:** April 17, 2026

**Main Contribution:** The paper proposes Gradient Fingerprint (GRIFT), a method for detecting reward hacking using models' internal computations.

**Problem Addressed:** Reward hacking occurs when models exploit loopholes in the reward function to achieve high scores without solving the intended task, and these behaviors are often implicit as the intermediate chain-of-thought may appear plausible on the surface.

The paper addresses this challenge in reinforcement learning with verifiable rewards (RLVR) by using gradient-based analysis to detect implicit reward-hacking behaviors that text-based monitoring alone cannot catch.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "cf62b076-f074-4f96-8a1e-4d254689f654"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T18:48:11.636Z_

<details><summary>↩ Tool result · `toolu_01WhfyV8RBMhNCRxFy8i2G16`</summary>

```text
Web search results for query: "arxiv "inference-time reward hacking" large language models 2025"

Links: [{"title":"[2506.19248] Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/abs/2506.19248"},{"title":"[2506.19248v1] Inference-Time Reward Hacking in Large Language Models","url":"http://arxiv.org/abs/2506.19248v1"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/html/2506.19248v2"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://openreview.net/pdf?id=vRfDOhiJAR"},{"title":"Inference-Time Reward Hacking in Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.19248v1"},{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"},{"title":"(PDF) Inference-Time Reward Hacking in Large Language Models","url":"https://www.researchgate.net/publication/392981059_Inference-Time_Reward_Hacking_in_Large_Language_Models"},{"title":"Best-of-N through the Smoothing Lens: KL Divergence and Regret Analysis","url":"https://arxiv.org/html/2507.05913v1"}]

I found the paper you're looking for. Here are the key details about the arXiv paper on "Inference-Time Reward Hacking in Large Language Models":

**Paper Details:**
- **Title:** Inference-Time Reward Hacking in Large Language Models
- **arXiv ID:** 2506.19248
- **Published:** NeurIPS 2025 spotlight
- **Latest Version:** November 4, 2025

**Key Contributions:**

The paper characterizes a critical problem in LLM alignment. Reward models assign numerical scores to LLM outputs indicating user preferences or safety goals, but reward models are never perfect and inevitably function as proxies for complex desiderata such as correctness, helpfulness, and safety.

The authors study inference-time alignment methods and introduce three key techniques:

1. Best-of-Poisson (BoP) that provides an efficient, near-exact approximation of the optimal reward-KL divergence policy at inference time

2. They show that the characteristic pattern of hacking (where true reward first increases before declining) is an inevitable property of a broad class of inference-time mechanisms, including Best-of-n and BoP

3. HedgeTune, an efficient algorithm to find the optimal inference-time parameter that mitigates reward hacking and achieves superior reward-distortion tradeoffs on math, reasoning, and human-preference setups


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "2800a96e-0c6e-4128-adf1-beb88cae1c74"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-22T18:48:12.482Z_

<details><summary>↩ Tool result · `toolu_01FaPKqzdihHxMWe3Sbuyhxi`</summary>

```text
Web search results for query: "arxiv 2510.01367 "is it thinking or cheating" detecting implicit reward hacking reasoning effort"

Links: [{"title":"[2510.01367] Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/abs/2510.01367"},{"title":"[2510.01367v2] Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/abs/2510.01367v2"},{"title":"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.1367v3"},{"title":"IS IT THINKING OR CHEATING? DETECTING IMPLICIT REWARD HACKING BY","url":"https://arxiv.org/pdf/2510.01367"},{"title":"Is it thinking or cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/html/2510.01367v3"},{"title":"Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort | OpenReview","url":"https://openreview.net/forum?id=Gk7gLAtVDO"},{"title":"[Literature Review] Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://www.themoonlight.io/en/review/is-it-thinking-or-cheating-detecting-implicit-reward-hacking-by-measuring-reasoning-effort"},{"title":"MCML - Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://mcml.ai/publications/wjp+25/"},{"title":"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502217215600055"},{"title":"[PDF] Is It Thinking or Cheating? Detecting Implicit Reward ...","url":"https://www.semanticscholar.org/paper/Is-It-Thinking-or-Cheating-Detecting-Implicit-by-Wang-Joshi/56736a73c686bcd099973728ad17f9f6dc8578db"}]

I found the paper arxiv 2510.01367 for you. Here's what it's about:

## Paper Summary

**Title:** "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort"

**The Problem:** Reward hacking, where a reasoning model exploits loopholes in a reward function to achieve high rewards without solving the intended task, poses a significant threat. The behavior may be implicit, where the chain-of-thought (CoT) appears benign thus bypasses CoT monitors.

**The Solution:** To detect implicit reward hacking, the authors propose TRACE (Truncated Reasoning AUC Evaluation).

**How It Works:** The key observation is that hacking occurs when exploiting the loophole is easier than solving the actual task, which means the model is using less 'effort' than required to achieve high reward. TRACE quantifies effort by measuring how early a model's reasoning becomes sufficient to obtain the reward by progressively truncating a model's CoT at various lengths, forcing the model to answer, and estimating the expected reward at each cutoff.

The paper was submitted to arXiv in October 2025 and has multiple versions available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "095c71cc-c8f1-4eb0-b288-f3e96690e5e9"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-22T18:48:15.627Z_

<details><summary>↩ Tool result · `toolu_01A7rPNrdgShEcZkrxVcNe5w`</summary>

```text
Web search results for query: "arxiv "reward hacking mitigation" verifiable composite rewards 2509.15557"

Links: [{"title":"[2509.15557] Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://arxiv.org/abs/2509.15557"},{"title":"Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://arxiv.org/html/2509.15557v1"},{"title":"Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://www.arxiv.org/pdf/2509.15557"},{"title":"Artificial Intelligence 2025","url":"https://www.arxiv.org/list/cs.AI/2025?skip=33875&show=1000"},{"title":"Proof-RM: A Scalable and Generalizable Reward Model for Mathematics Proof Verification","url":"https://arxiv.org/html/2602.02377v2"},{"title":"Reward Hacking Mitigation using Verifiable Composite ...","url":"https://dl.acm.org/doi/pdf/10.1145/3765612.3767230"},{"title":"Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://udspace.udel.edu/server/api/core/bitstreams/11090db0-25e3-40a9-834d-1625ab1e4050/content"},{"title":"IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.19416"}]

Based on the search results, I found detailed information about the paper you're looking for.

## Paper Summary

The paper "Reward Hacking Mitigation using Verifiable Composite Rewards" (arXiv:2509.15557) by Mirza Farhan Bin Tarek and Rahmatollah Beheshti addresses how Reinforcement Learning from Verifiable Rewards (RLVR) can be vulnerable to reward hacking in medical question answering applications.

## Main Problem

The work addresses two primary forms of reward hacking: providing a final answer without preceding reasoning, and employing non-standard reasoning formats to exploit the reward mechanism.

## Proposed Solution

The authors introduce a composite reward function with specific penalties for these behaviors, and their experiments show that extending RLVR with their proposed reward model leads to better-formatted reasoning with less reward hacking and good accuracy compared to baselines.

## Publication Status

The paper has been accepted at the 16th ACM Conference on Bioinformatics, Computational Biology, and Health Informatics (ACM-BCB 2025), and was submitted on September 19, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "bdeda9b1-5640-4d5c-a6b9-6b6d72562ae9"
}
```

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"reward hacking as equilibrium under finite…",
  "usage": {
    "total_tokens": 27768,
    "tool_uses": 14,
    "duration_ms": 34769
  },
  "last_tool_name": "WebSearch",
  "uuid": "b05034fa-ad8e-41b7-afbf-b2779d9974d2",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JmnfVXGnS775b7JcdmRV2t`</summary>

```json
{
  "query": "arxiv \"reward hacking as equilibrium under finite evaluation\" 2603.28063 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "04590525-0f4f-46a2-8699-f52709f90b5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JVpyWDepe1cbNPPkwnZsJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 4885,
      "cache_read_input_tokens": 21798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4885,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"strong weak benign Goodhart's law\" 2505.23…",
  "usage": {
    "total_tokens": 27808,
    "tool_uses": 15,
    "duration_ms": 35758
  },
  "last_tool_name": "WebSearch",
  "uuid": "5e61abd7-b4f2-44ab-ab6e-f0fa9723a332",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014DNWpomNuHTkR8xeEtxjxG`</summary>

```json
{
  "query": "arxiv \"strong weak benign Goodhart's law\" 2505.23445 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "2d8b33fb-7bc2-45fb-a30a-d6c0a80eb196",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JVpyWDepe1cbNPPkwnZsJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 4885,
      "cache_read_input_tokens": 21798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4885,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"gradient regularization prevents reward ha…",
  "usage": {
    "total_tokens": 27848,
    "tool_uses": 16,
    "duration_ms": 36261
  },
  "last_tool_name": "WebSearch",
  "uuid": "64e725c8-1eb2-4027-bd11-48d3d17065e5",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VsG92yBrMhbALSWo1SYc2Q`</summary>

```json
{
  "query": "arxiv \"gradient regularization prevents reward hacking\" RLHF verifiable rewards 2602.18037"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "e8081df3-aae4-4aa5-8e5c-a615e6b04198",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JVpyWDepe1cbNPPkwnZsJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 4885,
      "cache_read_input_tokens": 21798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4885,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"behavior-supported\" reward overoptimizatio…",
  "usage": {
    "total_tokens": 27888,
    "tool_uses": 17,
    "duration_ms": 37253
  },
  "last_tool_name": "WebSearch",
  "uuid": "ce68e53b-a9f2-4fbb-9df8-757452687049",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0117FPEwbwLaA8BSbtebgJTz`</summary>

```json
{
  "query": "arxiv \"behavior-supported\" reward overoptimization RLHF 2025 BSPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "2f1404d3-fb62-48a1-8fe3-326364e9868c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JVpyWDepe1cbNPPkwnZsJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 4885,
      "cache_read_input_tokens": 21798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4885,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"when reward hacking rebounds\" representati…",
  "usage": {
    "total_tokens": 27928,
    "tool_uses": 18,
    "duration_ms": 38201
  },
  "last_tool_name": "WebSearch",
  "uuid": "87695156-ad40-45c6-84db-25f417bea1cf",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014LFQ4HdyAFvzJAwNLzJ5zx`</summary>

```json
{
  "query": "arxiv \"when reward hacking rebounds\" representation-level signals 2604.01476"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "4e8bd0de-0439-4973-aaef-3792885a7044",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JVpyWDepe1cbNPPkwnZsJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 4885,
      "cache_read_input_tokens": 21798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4885,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"mitigating reward hacking RLHF advantage s…",
  "usage": {
    "total_tokens": 27968,
    "tool_uses": 19,
    "duration_ms": 38297
  },
  "last_tool_name": "WebSearch",
  "uuid": "3e0b722c-4531-44a1-a458-6becf2ab4d0a",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xkswq5kKEyxLyn7352Ehxp`</summary>

```json
{
  "query": "arxiv \"mitigating reward hacking RLHF advantage sign robustness\" 2604.02986"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "106a964b-44ca-4186-a182-3755b469b304",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JVpyWDepe1cbNPPkwnZsJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 957,
      "cache_creation_input_tokens": 4885,
      "cache_read_input_tokens": 21798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4885,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 69 · 2026-05-22T18:48:24.470Z_

<details><summary>↩ Tool result · `toolu_014DNWpomNuHTkR8xeEtxjxG`</summary>

```text
Web search results for query: "arxiv "strong weak benign Goodhart's law" 2505.23445 2025 authors"

Links: [{"title":"[2505.23445] The Strong, Weak and Benign Goodhart's law. An independence-free and paradigm-agnostic formalisation","url":"https://arxiv.org/abs/2505.23445"},{"title":"[2505.23445v2] The Strong, Weak and Benign Goodhart's law. An independence-free and paradigm-agnostic formalisation","url":"https://arxiv.org/abs/2505.23445v2"},{"title":"[PDF] The Strong, Weak and Benign Goodhart's law. An independence-free and paradigm-agnostic formalisation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Strong,-Weak-and-Benign-Goodhart's-law.-An-and-Majka-El-Mhamdi/93bd4c1e6fcdeacd8fe0d141afdcd7f868e14c79"},{"title":"The Strong, Weak and Benign Goodhart's law. An ...","url":"https://arxiv.org/pdf/2505.23445"},{"title":"The Strong, Weak and Benign Goodhart’s law.","url":"https://arxiv.org/pdf/2505.23445v2"},{"title":"[Literature Review] The Strong, Weak and Benign Goodhart's law. An independence-free and paradigm-agnostic formalisation","url":"https://www.themoonlight.io/en/review/the-strong-weak-and-benign-goodharts-law-an-independence-free-and-paradigm-agnostic-formalisation"},{"title":"The Strong, Weak and Benign Goodhart's law. An independence-free and paradigm-agnostic formalisation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250523445M/abstract"},{"title":"Statistics Theory May 2025","url":"https://www.arxiv.org/list/math.ST/2025-05?skip=125&show=500"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=4600&show=50"}]

Based on the search results, here's the information about the arXiv paper 2505.23445:

The authors of this paper are Adrien Majka and El-Mahdi El-Mhamdi. 

The paper is titled "The Strong, Weak and Benign Goodhart's law. An independence-free and paradigm-agnostic formalisation" and was submitted on May 29, 2025, with the latest revision on September 4, 2025.

Goodhart's law is a famous adage in policy-making that states that "When a measure becomes a target, it ceases to be a good measure". The paper alleviates the simplifying independence assumption made in previous works and studies the effect of the coupling between the proxy metric and the intended goal on Goodhart's law.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "a0ccc59d-3d9b-4929-92ea-dc91e1c1e935"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-22T18:48:25.001Z_

<details><summary>↩ Tool result · `toolu_01JmnfVXGnS775b7JcdmRV2t`</summary>

```text
Web search results for query: "arxiv "reward hacking as equilibrium under finite evaluation" 2603.28063 authors"

Links: [{"title":"[2603.28063] Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/abs/2603.28063"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/html/2603.28063"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/pdf/2603.28063"},{"title":"Computer Science and Game Theory","url":"https://arxiv.org/list/cs.GT/recent?skip=10&show=25"},{"title":"Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels   against Reward Hacking","url":"https://arxiv.org/pdf/2412.09544"},{"title":"[2506.19248] Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/abs/2506.19248"}]

Based on the search results, here is the information about the paper:

**Title:** Reward Hacking as Equilibrium under Finite Evaluation

**Authors:** Jiacheng Wang and Jinbin Huang

**arXiv ID:** 2603.28063

**Submission Date:** March 2026

**Main Contribution:** The paper proves that under five minimal axioms — multi-dimensional quality, finite evaluation, effective optimization, resource finiteness, and combinatorial interaction — any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system. This establishes reward hacking as a structural equilibrium, not a correctable bug, and holds regardless of the specific alignment method (RLHF, DPO, Constitutional AI, or others) or evaluation architecture employed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "facf5dce-4990-4ec1-b335-81d3e2e922b1"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-22T18:48:26.706Z_

<details><summary>↩ Tool result · `toolu_01VsG92yBrMhbALSWo1SYc2Q`</summary>

```text
Web search results for query: "arxiv "gradient regularization prevents reward hacking" RLHF verifiable rewards 2602.18037"

Links: [{"title":"[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/abs/2602.18037"},{"title":"Gradient Regularization Prevents Reward Hacking in ...","url":"https://arxiv.org/pdf/2602.18037"},{"title":"Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/html/2604.16242"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"Unifying Stable Optimization and Reference Regularization in RLHF","url":"https://arxiv.org/html/2602.11523"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking","url":"https://arxiv.org/html/2403.03185v4"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking","url":"https://arxiv.org/pdf/2403.03185"},{"title":"Information-Theoretic Reward Modeling for Stable RLHF: Detecting and Mitigating Reward Hacking","url":"https://arxiv.org/pdf/2510.13694"}]

I found the paper! Here's information about the arXiv paper 2602.18037:

## Paper Summary

The paper addresses Reinforcement Learning from Human Feedback (RLHF) and Verifiable Rewards (RLVR) in post-training of modern Language Models. A common problem it tackles is reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior.

## Key Contribution

The authors propose training the language model in a way that biases policy updates towards regions in which the reward is more accurate, deriving a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, with gradient regularization used to bias training to flatter regions and thereby maintain reward model accuracy.

## Empirical Results

Gradient regularization performs better than a KL penalty across diverse RL experiments with language models, achieving a higher GPT-judged win-rate in RLHF, avoiding overly focusing on format in rule-based math rewards, and preventing hacking the judge in LLM-as-a-Judge math tasks.

The paper was submitted to arXiv on February 20, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "e291d5b0-a322-4801-b44c-52423eb3ce3e"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-22T18:48:26.919Z_

<details><summary>↩ Tool result · `toolu_0117FPEwbwLaA8BSbtebgJTz`</summary>

```text
Web search results for query: "arxiv "behavior-supported" reward overoptimization RLHF 2025 BSPO"

Links: [{"title":"[2503.18130] Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization","url":"https://arxiv.org/abs/2503.18130"},{"title":"Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization | OpenReview","url":"https://openreview.net/forum?id=PNMv4r7s1i"},{"title":"Mitigating Reward Over-Optimization in RLHF via Behavior-Supported   Regularization","url":"https://arxiv.org/pdf/2503.18130"},{"title":"Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization","url":"https://arxiv.org/html/2503.18130v1"},{"title":"Reward Over-Optimization in AI","url":"https://www.emergentmind.com/topics/reward-over-optimization"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"}]

I found the paper you're looking for! Here are the search results:

The paper proposes the Behavior-Supported Policy Optimization (BSPO) method to mitigate the reward over-optimization issue in RLHF. 

Reward over-optimization remains a challenge in RLHF leading to discrepancies between LLM performance under the reward model and true human objectives, with a primary cause being extrapolation error when the reward model evaluates out-of-distribution (OOD) responses.

The method defines behavior policy as the next token distribution of the reward training dataset to model the in-distribution region, and introduces the behavior-supported Bellman operator to regularize the value function, penalizing all OOD values without impacting ID ones.

Theoretically, BSPO guarantees a monotonic improvement of the supported policy until convergence to the optimal behavior-supported policy, and empirical results show that BSPO outperforms baselines in preventing reward over-optimization due to OOD evaluation.

The paper was published on arxiv as [2503.18130](https://arxiv.org/abs/2503.18130) on March 23, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "62a3f28e-40d7-423e-a7db-e2bc2e2d6be2"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-22T18:48:29.640Z_

<details><summary>↩ Tool result · `toolu_01Xkswq5kKEyxLyn7352Ehxp`</summary>

```text
Web search results for query: "arxiv "mitigating reward hacking RLHF advantage sign robustness" 2604.02986"

Links: [{"title":"[2604.02986] Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/abs/2604.02986"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://ar5iv.labs.arxiv.org/html/2502.18770"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/html/2602.10623v1"}]

I found the paper! Here's what the search results show about arxiv:2604.02986:

**Title:** Mitigating Reward Hacking in RLHF via Advantage Sign Robustness

**Authors:** Shinnosuke Ono, Johannes Ackermann, Soichiro Nishimori, Takashi Ishida, and Masashi Sugiyama

**Submission Date:** April 3, 2026

**Main Contribution:**

Reward models used in RLHF are vulnerable to reward hacking: as the policy maximizes a learned proxy reward, true quality plateaus or degrades. 

The authors assume that reward hacking is often caused by flipped advantage signs: instead of reducing the likelihood of a bad response, a flipped sign causes the update to increase it.

They derive a certified sign-preservation radius (the smallest perturbation that can flip the advantage sign during policy optimization) and propose Sign-Certified Policy Optimization (SignCert-PO), which down-weights non-robust completions in the policy gradient update.

**Key Advantage:** Unlike prior approaches that require multiple RMs or access to RM training data, SignCert-PO is lightweight and operates purely at the policy optimization stage using only the RM parameters and on-policy completions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "3b721574-87f3-4de3-88d1-23038693dca6"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-22T18:48:30.591Z_

<details><summary>↩ Tool result · `toolu_014LFQ4HdyAFvzJAwNLzJ5zx`</summary>

```text
Web search results for query: "arxiv "when reward hacking rebounds" representation-level signals 2604.01476"

Links: [{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/html/2604.01476v1"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Monitoring Emergent Reward Hacking During Generation via Internal Activations","url":"https://arxiv.org/pdf/2603.04069"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.01750"}]

I found the paper you were searching for! Here's what the search returned:

"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals" is a paper by Rui Wu and Ruixiang Tang from Rutgers University that studies how reinforcement learning for LLMs is vulnerable to reward hacking, where models exploit shortcuts to maximize reward without solving the intended task.

The paper systematically studies this phenomenon in coding tasks using an environment-manipulation setting, where models can rewrite evaluator code to trivially pass tests without solving the task.

The researchers identify a reproducible three-phase rebound pattern: models first attempt to rewrite the evaluator but fail, as their rewrites embed test cases their own solutions cannot pass. They then temporarily retreat to legitimate solving. When legitimate reward remains scarce, they rebound into successful hacking with qualitatively different strategies.

Using representation engineering, they extract concept directions for shortcut, deception, and evaluation awareness from domain-general contrastive pairs and find that the shortcut direction tracks hacking behavior most closely.

The paper proposes Advantage Modification, which integrates shortcut concept scores into GRPO advantage computation to penalize hacking rollouts before policy updates, providing more robust suppression of hacking compared with generation-time activation steering.

The paper was published on arXiv on April 1, 2026 (arXiv:2604.01476v1).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "360d5733-2474-428d-8175-c9395f0d9a1e"
}
```

</details>

---

### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"Goodhart's law in reinforcement learning\" …",
  "usage": {
    "total_tokens": 32260,
    "tool_uses": 20,
    "duration_ms": 50010
  },
  "last_tool_name": "WebSearch",
  "uuid": "b1e1dcd2-5efd-48db-a930-08eca6740b89",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012GnyDguthfiiTeSrvhouPu`</summary>

```json
{
  "query": "arxiv \"Goodhart's law in reinforcement learning\" Karwowski 2310.09144 ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "7920fc92-c228-4028-925a-0d4220ddfb8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXTgk6Dnk5EBF5TT8LYdfb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 629,
      "cache_creation_input_tokens": 4571,
      "cache_read_input_tokens": 26683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4571,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv Gao \"scaling laws reward model overoptimiza…",
  "usage": {
    "total_tokens": 32309,
    "tool_uses": 21,
    "duration_ms": 50516
  },
  "last_tool_name": "WebSearch",
  "uuid": "70d9094d-5f74-4ec8-9c97-463748b4d625",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0165q2tDs7PMUERXqtw8T39v`</summary>

```json
{
  "query": "arxiv Gao \"scaling laws reward model overoptimization\" 2210.10760"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "d98cabc3-26e9-4c4f-8df3-2ec1b4b8984a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXTgk6Dnk5EBF5TT8LYdfb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 629,
      "cache_creation_input_tokens": 4571,
      "cache_read_input_tokens": 26683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4571,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"reward model overoptimisation iterated RLH…",
  "usage": {
    "total_tokens": 32358,
    "tool_uses": 22,
    "duration_ms": 51487
  },
  "last_tool_name": "WebSearch",
  "uuid": "eb38cb1b-59c4-4206-9857-d39014123498",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AB4VfkeRUY84MhccHUde7q`</summary>

```json
{
  "query": "arxiv \"reward model overoptimisation iterated RLHF\" 2025 OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "3f2fe403-6b18-4f1e-917a-f8c1b351a974",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXTgk6Dnk5EBF5TT8LYdfb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 629,
      "cache_creation_input_tokens": 4571,
      "cache_read_input_tokens": 26683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4571,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "description": "Searching for arxiv \"adversarial reward auditing\" reward hackin…",
  "usage": {
    "total_tokens": 32407,
    "tool_uses": 23,
    "duration_ms": 51835
  },
  "last_tool_name": "WebSearch",
  "uuid": "7334ce0f-333c-4ffb-9f05-dea48b1c25aa",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019P5NighvZHB7KQ4HE2XsfP`</summary>

```json
{
  "query": "arxiv \"adversarial reward auditing\" reward hacking detection mitigation 2602.01750"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "a498ccd7-fc3d-458b-a98b-d42486e0d0cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXTgk6Dnk5EBF5TT8LYdfb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 629,
      "cache_creation_input_tokens": 4571,
      "cache_read_input_tokens": 26683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4571,
        "ephemeral_1h_input_tokens": 0
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

_source line 83 · 2026-05-22T18:48:40.045Z_

<details><summary>↩ Tool result · `toolu_0165q2tDs7PMUERXqtw8T39v`</summary>

```text
Web search results for query: "arxiv Gao "scaling laws reward model overoptimization" 2210.10760"

Links: [{"title":"[2210.10760] Scaling Laws for Reward Model Overoptimization","url":"https://arxiv.org/abs/2210.10760"},{"title":"YYiki: Scaling Laws for Reward Model Overoptimization","url":"https://yyiki.org/wiki/Paper/Gao2022scaling/"},{"title":"Figure 7 from Scaling Laws for Reward Model Overoptimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scaling-Laws-for-Reward-Model-Overoptimization-Gao-Schulman/fb3dc5e20e0a71134ca916f0d6d8d41f01225b4b/figure/8"},{"title":"Scaling Laws for Reward Model Overoptimization Leo Gao OpenAI John Schulman","url":"https://arxiv.org/pdf/2210.10760"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://www.researchgate.net/publication/364436070_Scaling_Laws_for_Reward_Model_Overoptimization"},{"title":"Scaling Laws in Reward Model Overoptimization | PDF | Estimator | Experiment","url":"https://www.scribd.com/document/668584786/2210-10760"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://www.alignmentforum.org/posts/shcSdHGPhnLQkpSbX/scaling-laws-for-reward-model-overoptimization"},{"title":"Scaling Laws for Reward Model Overoptimization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv221010760G/abstract"},{"title":"Paper page - Scaling Laws for Reward Model Overoptimization","url":"https://huggingface.co/papers/2210.10760"}]

I found the paper! Here's what the search returned:

**Title:** Scaling Laws for Reward Model Overoptimization

**Authors:** Leo Gao, John Schulman, Jacob Hilton

**ArXiv ID:** 2210.10760

**Publication Date:** October 19, 2022

**Summary:**

The paper studies reinforcement learning from human feedback and how optimizing against an imperfect reward model can hinder ground truth performance, in accordance with Goodhart's law. To address the challenge of expensive human preference data collection, the authors use a synthetic setup where a "gold-standard" reward model provides labels.

The key findings show that as policies are optimized against a proxy reward model, the gold-standard reward model score follows different functional forms depending on the optimization method—quadratic for best-of-n sampling and logarithmic for reinforcement learning. The coefficients in these relationships scale smoothly with the number of reward model parameters.

You can access the full paper at: https://arxiv.org/abs/2210.10760


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "481a462d-ace0-4933-8c11-50858c3a3476"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-22T18:48:42.141Z_

<details><summary>↩ Tool result · `toolu_012GnyDguthfiiTeSrvhouPu`</summary>

```text
Web search results for query: "arxiv "Goodhart's law in reinforcement learning" Karwowski 2310.09144 ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.05584"},{"title":"[2310.09144] Goodhart's Law in Reinforcement Learning","url":"https://arxiv.org/abs/2310.09144"},{"title":"‪Goodhart's Law in Reinforcement Learning‬","url":"https://scholar.google.com/citations?citation_for_view=GuzLUmQAAAAJ%3AroLk4NBRz8UC&hl=en&sortby=pubdate&user=GuzLUmQAAAAJ&view_op=view_citation"},{"title":"Goodhart’s Law in Reinforcement Learning","url":"https://arxiv.org/html/2310.09144"},{"title":"GOODHART'S LAW IN REINFORCEMENT LEARNING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6ad68a54eaa8f9bf6ac698b02ec05048-Paper-Conference.pdf"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://arxiv.org/pdf/2310.09144"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.semanticscholar.org/paper/Goodhart's-Law-in-Reinforcement-Learning-Karwowski-Hayman/a4bd4da02241eacee990c89ddd748ce37a248fc0"},{"title":"Goodhart's Law in Reinforcement Learning - MATS Research","url":"https://www.matsprogram.org/research/goodhart-s-law-in-reinforcement-learning"}]

Based on the search results, I found the paper you're looking for:

The paper examines how implementing a reward function that perfectly captures a complex task is impractical, so reward functions are often treated as proxies for true objectives. The authors study this through Goodhart's law, which predicts that optimizing an imperfect proxy beyond a critical point decreases performance on the true objective.

The authors propose a way to quantify the magnitude of this effect and show empirically that optimizing imperfect proxy rewards often leads to behavior predicted by Goodhart's law across a wide range of environments. They provide a geometric explanation for why this occurs in Markov decision processes and propose an optimal early stopping method with theoretical regret bounds.

The paper is authored by Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, and Joar Skalse. The arxiv paper was published in 2023 with ID 2310.09144, and it was published as a conference paper at ICLR 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "e4f7b914-35f2-4fb1-bc2e-30efdb66f28b"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-22T18:48:42.368Z_

<details><summary>↩ Tool result · `toolu_019P5NighvZHB7KQ4HE2XsfP`</summary>

```text
Web search results for query: "arxiv "adversarial reward auditing" reward hacking detection mitigation 2602.01750"

Links: [{"title":"[2602.01750] Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/abs/2602.01750"},{"title":"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/html/2602.01750v1"},{"title":"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking | Request PDF","url":"https://www.researchgate.net/publication/400369344_Adversarial_Reward_Auditing_for_Active_Detection_and_Mitigation_of_Reward_Hacking"},{"title":"Adversarial Reward Auditing for Active Detection and ...","url":"https://arxiv.org/pdf/2602.01750"},{"title":"IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.19416"},{"title":"IR3: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/html/2602.19416v1"},{"title":"Adversarial Reward-Hacking","url":"https://www.emergentmind.com/topics/adversarial-reward-hacking"}]

Based on the search results, I found the paper you're looking for. Here's what it contains:

## Paper Overview

The paper addresses the vulnerability of Reinforcement Learning from Human Feedback (RLHF) to reward hacking, where models exploit spurious correlations in learned reward models to achieve high scores while violating human intent.

## The ARA Framework

The authors propose Adversarial Reward Auditing (ARA), a framework that reconceptualizes reward hacking as a dynamic, competitive game. ARA operates in two stages: first, a Hacker policy discovers reward model vulnerabilities while an Auditor learns to detect exploitation from latent representations; second, Auditor-Guided RLHF (AG-RLHF) gates reward signals to penalize detected hacking, transforming reward hacking from an unobservable failure into a measurable, controllable signal.

## Key Innovation

Existing mitigations rely on static defenses that cannot adapt to novel exploitation strategies. The ARA framework addresses this limitation by treating reward hacking as an active detection and mitigation problem rather than a static constraint.

The paper was submitted to arXiv on February 2, 2026, and is intended for ICML 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "b502e363-35a0-4d78-9223-c8ee11e96b47"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-22T18:48:44.403Z_

<details><summary>↩ Tool result · `toolu_01AB4VfkeRUY84MhccHUde7q`</summary>

```text
Web search results for query: "arxiv "reward model overoptimisation iterated RLHF" 2025 OpenReview"

Links: [{"title":"[2505.18126] Reward Model Overoptimisation in Iterated RLHF","url":"https://arxiv.org/abs/2505.18126"},{"title":"Reward Model Overoptimisation in Iterated RLHF","url":"https://arxiv.org/html/2505.18126v1"},{"title":"Reward Model Overoptimisation in Iterated RLHF | OpenReview","url":"https://openreview.net/forum?id=efoe5VJfKz"},{"title":"Reward Model Overoptimisation in Iterated RLHF","url":"https://arxiv.org/pdf/2505.18126"},{"title":"NeurIPS Reward Model Overoptimisation in Iterated RLHF","url":"https://neurips.cc/virtual/2025/loc/san-diego/136061"},{"title":"Computer Science May 2025","url":"http://arxiv.org/list/cs/2025-05?skip=9050&show=1000"},{"title":"Reward Model Overoptimisation in Iterated RLHF Anonymous Author(s) Affiliation","url":"https://openreview.net/pdf/481540971989cf63c41d872d993ebbdd1e23eb2b.pdf"}]

I found the paper you're looking for! Here are the search results:

**Paper Details:**
- **Title:** Reward Model Overoptimisation in Iterated RLHF
- **Authors:** Lorenz Wolf, Robert Kirk, and Mirco Musolesi
- **arXiv ID:** 2505.18126
- **Links:** 
  - arXiv: https://arxiv.org/abs/2505.18126
  - OpenReview: https://openreview.net/forum?id=efoe5VJfKz

**Summary:**
RLHF often suffers from reward model overoptimisation, in which models overfit to the reward function, resulting in non-generalisable policies that exploit the idiosyncrasies and peculiarities of the reward function. A common mitigation is iterated RLHF, in which reward models are repeatedly retrained with updated human feedback and policies are re-optimised.

**Key Findings:**
The paper systematically analyses key design choices: how reward model training data is transferred across iterations, which reward function is used for optimisation, and how policies are initialised. Using the controlled AlpacaFarm benchmark, the researchers observe that overoptimisation tends to decrease over successive iterations, as reward models increasingly approximate ground-truth preferences. However, performance gains diminish over time, and while reinitialising from the base policy is robust, it limits optimisation flexibility. Other initialisation strategies often fail to recover from early overoptimisation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "985b7c2d-e8d3-4e60-86fe-4993c59e827b"
}
```

</details>

---

### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ae3381ac72aa1a5db",
  "tool_use_id": "toolu_01EBXYMdakeZrEeQ7p4EaLoe",
  "status": "completed",
  "output_file": "",
  "summary": "Search recent reward hacking papers",
  "usage": {
    "total_tokens": 35650,
    "tool_uses": 23,
    "duration_ms": 102479
  },
  "uuid": "f002687d-f30a-43ac-9567-620d6dac3d4c",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3"
}
```

---

### Tool result

_source line 88 · 2026-05-22T18:49:26.504Z_

<details><summary>↩ Tool result · `toolu_01EBXYMdakeZrEeQ7p4EaLoe`</summary>

```text
Here are the results organized by search query.

---

## Search 1: "reward hacking formal reasoning 2025 2026"

1. **"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort"** -- Wang et al., 2025. arXiv:2510.01367. Proposes TRACE, which detects implicit reward hacking by truncating CoT at multiple lengths to measure whether models use genuine reasoning effort vs. shortcuts.

2. **"Reward Hacking as Equilibrium under Finite Evaluation"** -- Jiacheng Wang & Jinbin Huang, 2026. arXiv:2603.28063. Proves under five minimal axioms that reward hacking is a structural equilibrium (not a correctable bug) for any optimized AI agent under finite evaluation.

3. **"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking"** -- Helff et al. (TU Darmstadt), 2026. arXiv:2604.15149. Studies RLVR on inductive reasoning tasks; finds models abandon rule induction in favor of enumerating instance-level labels that pass verifiers. Introduces Isomorphic Perturbation Testing (IPT) for detection.

4. **"Detecting and Suppressing Reward Hacking with Gradient Fingerprints"** -- Wang, Pham, Yin et al., 2026. arXiv:2604.16242. Proposes GRIFT, a gradient-based method for detecting implicit reward hacking in RLVR that text-based CoT monitoring misses.

5. **"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges"** -- Xiaohua Wang et al., 2026. arXiv:2604.13602. Survey covering Goodhart's Law, proxy evaluators (RLHF/RLAIF/RLVR), the Proxy Compression Hypothesis, and a hierarchy of feature-/representation-/evaluator-/environment-level exploitation.

---

## Search 2: "reward overoptimization language model 2025 2026"

1. **"Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization"** -- (BSPO), 2025. arXiv:2503.18130. Defines behavior policy as next-token distribution of reward training data; regularizes value function to penalize OOD evaluations, guaranteeing monotonic improvement.

2. **"Reward Model Overoptimisation in Iterated RLHF"** -- Wolf, Kirk & Musolesi, 2025. arXiv:2505.18126. NeurIPS 2025. Systematically analyzes iterated RLHF; finds overoptimization decreases over successive iterations but performance gains diminish; reinitializing from base policy is most robust.

3. **"Inference-Time Reward Hacking in Large Language Models"** -- 2025. arXiv:2506.19248. NeurIPS 2025 spotlight. Shows hacking is an inevitable property of inference-time mechanisms (Best-of-n); proposes HedgeTune for optimal inference-time parameter selection.

4. **"Confronting Reward Model Overoptimization with Constrained RLHF"** -- 2025. OpenReview (NeurIPS). Uses constrained optimization to bound proxy reward divergence from true reward.

5. **"Scaling Laws for Reward Model Overoptimization"** -- Gao, Schulman & Hilton, 2022. arXiv:2210.10760. ICML 2023. Foundational paper: gold reward follows quadratic (BoN) / logarithmic (RL) Goodhart curves; coefficients scale with RM parameters.

---

## Search 3: "RLVR reward hacking 2025 2026"

1. **"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking"** -- Helff et al., 2026. arXiv:2604.15149. (See Search 1 above.)

2. **"Reward Hacking Mitigation using Verifiable Composite Rewards"** -- Tarek & Beheshti, 2025. arXiv:2509.15557. ACM-BCB 2025. Introduces composite reward with penalties for answer-without-reasoning and non-standard reasoning formats in medical QA RLVR.

3. **"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards"** -- 2026. arXiv:2602.18037. Biases policy updates toward regions where reward is accurate using gradient regularization; outperforms KL penalty on math RLVR tasks.

4. **"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals"** -- Wu & Tang (Rutgers), 2026. arXiv:2604.01476. Identifies a three-phase rebound pattern in coding tasks (attempt hack, retreat to legitimate solving, rebound into successful hacking); proposes Advantage Modification using shortcut concept directions from representation engineering.

5. **"Detecting and Suppressing Reward Hacking with Gradient Fingerprints"** -- Wang et al., 2026. arXiv:2604.16242. (See Search 1 above.)

6. **"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness"** -- Ono, Ackermann et al., 2026. arXiv:2604.02986. Derives certified sign-preservation radius for advantage signs; proposes SignCert-PO to down-weight non-robust completions.

7. **"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking"** -- 2026. arXiv:2602.01750. Proposes ARA framework: Hacker policy discovers RM vulnerabilities, Auditor detects exploitation from latent representations, then Auditor-Guided RLHF gates reward signals.

---

## Search 4: "Goodhart law reinforcement learning language model 2025"

1. **"Goodhart's Law in Reinforcement Learning"** -- Karwowski, Hayman, Bai et al., 2023/2025. arXiv:2310.09144. ICLR 2025. Geometric explanation of Goodhart's law in MDPs; proposes optimal early stopping with theoretical regret bounds.

2. **"The Strong, Weak and Benign Goodhart's Law: An Independence-Free and Paradigm-Agnostic Formalisation"** -- Majka & El-Mhamdi, 2025. arXiv:2505.23445. Formal characterization of different strengths of Goodhart effects; removes independence assumption from prior work.

3. **"Scaling Laws for Reward Model Overoptimization"** -- Gao, Schulman & Hilton, 2022. arXiv:2210.10760. (See Search 2 above.)

---

## Search 5: Strathern 1997

**"'Improving Ratings': Audit in the British University System"** -- Marilyn Strathern, 1997. European Review, 5(3), 305--321. Popularized the generalized form of Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure."

---

## Search 6: Goodhart 1975

**"Problems of Monetary Management: The U.K. Experience"** -- Charles A. E. Goodhart, 1975. Paper presented to the Money Study Group, London School of Economics. Published in: Courakis, A.S. (ed.), Papers in Monetary Economics, Reserve Bank of Australia, 1975. Original formulation: "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes."

agentId: ae3381ac72aa1a5db (use SendMessage with to: 'ae3381ac72aa1a5db' to continue this agent)
&lt;usage>total_tokens: 37069
tool_uses: 23
duration_ms: 102482&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "83d43254-5483-47c4-a295-734aec12cae2",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Use WebSearch to find recent (2025-2026) papers on reward hacking in formal reasoning and RLVR. Run these searches:\n\n1. \"reward hacking formal reasoning 2025 2026\"\n2. \"reward overoptimization language model 2025 2026\"\n3. \"RLVR reward hacking 2025 2026\"\n4. \"Goodhart law reinforcement learning language model 2025\"\n\nFor each search, report the top 5-8 most relevant papers with: title, authors, year, venue/arXiv ID, and a one-line summary. Focus on papers that study reward hacking/gaming/overoptimization in the context of language model reasoning (especially formal/symbolic reasoning). \n\nAlso specifically search for:\n5. \"Strathern Goodhart\" to find the classic Strathern 1997 formulation\n6. \"Goodhart 1975 monetary policy\" for the original Goodhart paper\n\nReport results concisely — title, authors, year, arXiv ID, one-line summary. No commentary beyond that.",
    "agentId": "ae3381ac72aa1a5db",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the results organized by search query.\n\n---\n\n## Search 1: \"reward hacking formal reasoning 2025 2026\"\n\n1. **\"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort\"** -- Wang et al., 2025. arXiv:2510.01367. Proposes TRACE, which detects implicit reward hacking by truncating CoT at multiple lengths to measure whether models use genuine reasoning effort vs. shortcuts.\n\n2. **\"Reward Hacking as Equilibrium under Finite Evaluation\"** -- Jiacheng Wang & Jinbin Huang, 2026. arXiv:2603.28063. Proves under five minimal axioms that reward hacking is a structural equilibrium (not a correctable bug) for any optimized AI agent under finite evaluation.\n\n3. **\"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking\"** -- Helff et al. (TU Darmstadt), 2026. arXiv:2604.15149. Studies RLVR on inductive reasoning tasks; finds models abandon rule induction in favor of enumerating instance-level labels that pass verifiers. Introduces Isomorphic Perturbation Testing (IPT) for detection.\n\n4. **\"Detecting and Suppressing Reward Hacking with Gradient Fingerprints\"** -- Wang, Pham, Yin et al., 2026. arXiv:2604.16242. Proposes GRIFT, a gradient-based method for detecting implicit reward hacking in RLVR that text-based CoT monitoring misses.\n\n5. **\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"** -- Xiaohua Wang et al., 2026. arXiv:2604.13602. Survey covering Goodhart's Law, proxy evaluators (RLHF/RLAIF/RLVR), the Proxy Compression Hypothesis, and a hierarchy of feature-/representation-/evaluator-/environment-level exploitation.\n\n---\n\n## Search 2: \"reward overoptimization language model 2025 2026\"\n\n1. **\"Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization\"** -- (BSPO), 2025. arXiv:2503.18130. Defines behavior policy as next-token distribution of reward training data; regularizes value function to penalize OOD evaluations, guaranteeing monotonic improvement.\n\n2. **\"Reward Model Overoptimisation in Iterated RLHF\"** -- Wolf, Kirk & Musolesi, 2025. arXiv:2505.18126. NeurIPS 2025. Systematically analyzes iterated RLHF; finds overoptimization decreases over successive iterations but performance gains diminish; reinitializing from base policy is most robust.\n\n3. **\"Inference-Time Reward Hacking in Large Language Models\"** -- 2025. arXiv:2506.19248. NeurIPS 2025 spotlight. Shows hacking is an inevitable property of inference-time mechanisms (Best-of-n); proposes HedgeTune for optimal inference-time parameter selection.\n\n4. **\"Confronting Reward Model Overoptimization with Constrained RLHF\"** -- 2025. OpenReview (NeurIPS). Uses constrained optimization to bound proxy reward divergence from true reward.\n\n5. **\"Scaling Laws for Reward Model Overoptimization\"** -- Gao, Schulman & Hilton, 2022. arXiv:2210.10760. ICML 2023. Foundational paper: gold reward follows quadratic (BoN) / logarithmic (RL) Goodhart curves; coefficients scale with RM parameters.\n\n---\n\n## Search 3: \"RLVR reward hacking 2025 2026\"\n\n1. **\"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking\"** -- Helff et al., 2026. arXiv:2604.15149. (See Search 1 above.)\n\n2. **\"Reward Hacking Mitigation using Verifiable Composite Rewards\"** -- Tarek & Beheshti, 2025. arXiv:2509.15557. ACM-BCB 2025. Introduces composite reward with penalties for answer-without-reasoning and non-standard reasoning formats in medical QA RLVR.\n\n3. **\"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards\"** -- 2026. arXiv:2602.18037. Biases policy updates toward regions where reward is accurate using gradient regularization; outperforms KL penalty on math RLVR tasks.\n\n4. **\"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals\"** -- Wu & Tang (Rutgers), 2026. arXiv:2604.01476. Identifies a three-phase rebound pattern in coding tasks (attempt hack, retreat to legitimate solving, rebound into successful hacking); proposes Advantage Modification using shortcut concept directions from representation engineering.\n\n5. **\"Detecting and Suppressing Reward Hacking with Gradient Fingerprints\"** -- Wang et al., 2026. arXiv:2604.16242. (See Search 1 above.)\n\n6. **\"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness\"** -- Ono, Ackermann et al., 2026. arXiv:2604.02986. Derives certified sign-preservation radius for advantage signs; proposes SignCert-PO to down-weight non-robust completions.\n\n7. **\"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking\"** -- 2026. arXiv:2602.01750. Proposes ARA framework: Hacker policy discovers RM vulnerabilities, Auditor detects exploitation from latent representations, then Auditor-Guided RLHF gates reward signals.\n\n---\n\n## Search 4: \"Goodhart law reinforcement learning language model 2025\"\n\n1. **\"Goodhart's Law in Reinforcement Learning\"** -- Karwowski, Hayman, Bai et al., 2023/2025. arXiv:2310.09144. ICLR 2025. Geometric explanation of Goodhart's law in MDPs; proposes optimal early stopping with theoretical regret bounds.\n\n2. **\"The Strong, Weak and Benign Goodhart's Law: An Independence-Free and Paradigm-Agnostic Formalisation\"** -- Majka & El-Mhamdi, 2025. arXiv:2505.23445. Formal characterization of different strengths of Goodhart effects; removes independence assumption from prior work.\n\n3. **\"Scaling Laws for Reward Model Overoptimization\"** -- Gao, Schulman & Hilton, 2022. arXiv:2210.10760. (See Search 2 above.)\n\n---\n\n## Search 5: Strathern 1997\n\n**\"'Improving Ratings': Audit in the British University System\"** -- Marilyn Strathern, 1997. European Review, 5(3), 305--321. Popularized the generalized form of Goodhart's Law: \"When a measure becomes a target, it ceases to be a good measure.\"\n\n---\n\n## Search 6: Goodhart 1975\n\n**\"Problems of Monetary Management: The U.K. Experience\"** -- Charles A. E. Goodhart, 1975. Paper presented to the Money Study Group, London School of Economics. Published in: Courakis, A.S. (ed.), Papers in Monetary Economics, Reserve Bank of Australia, 1975. Original formulation: \"Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.\""
      }
    ],
    "totalDurationMs": 102482,
    "totalTokens": 37069,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 716,
      "cache_creation_input_tokens": 3155,
      "cache_read_input_tokens": 31254,
      "output_tokens": 1944,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3155
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 716,
          "output_tokens": 1944,
          "cache_read_input_tokens": 31254,
          "cache_creation_input_tokens": 3155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3155,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 23
    }
  }
}
```

</details>

---

### Assistant

_source line 89_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze the coverage systematically.

## 1. Reward hacking in RLHF/RLVR core citations

| Citation | In bib? | In related_work? | Status |
|----------|---------|-------------------|--------|
| Goodhart 1975 (original) | ❌ | ❌ | Missing - but not strictly needed in ML venue; Manheim & Garrabrant is standard |
| Strathern 1997 | ❌ | ❌ | Missing - but same as above |


| Manheim & Garrabrant taxonomy | ✅ | ✅ | OK |
| Skalse et al. (reward hacking formal) | ✅ | ✅ | OK |
| METR reward hacking | ✅ | ✅ | OK |
| Gao et al. reward overoptimization | ✅ | ✅ | OK |

The key reward hacking papers are all properly cited and referenced in the related work section.

For the foundational Goodhart and Strathern papers, those are really the original economics sources, but in ML contexts it's more standard to cite Manheim & Garrabrant as the primary reference, so I'd mark those as optional rather than critical gaps.

The neurosymbolic reasoning and RL work looks solid too—FOLIO, Logic-RL, SatLM, Logic-LM, and all the recent DeepSeek and AlphaProof papers are accounted for. Now I should check what might be missing from the 2025-2026 literature based on recent developments.

Looking at some newer papers that came up: there's Wang et al. 2025 on detecting implicit reward hacking through CoT truncation, which is related but uses a different mechanism than leave-one-out analysis. Then there's the 2026 work on gradient-based detection and a paper on reward hacking rebound patterns in coding tasks. These are tangentially relevant but not directly about formal reasoning verification, so they're worth noting but probably not essential to the core narrative. The other papers I found aren't currently cited—TRACE detects implicit hacking through reasoning effort, GRIFT uses gradient fingerprints for detection, and there's work on reward hacking as equilibrium and rebound patterns. GRIFT could fit alongside Wilhelm as another concurrent detection method, and the rebound pattern paper offers interesting insights, but the paper already has solid coverage of related work, so these would be nice additions rather than essential gaps.

The Wilhelm comparison is already well-articulated—it clearly distinguishes their generation-time detection via internal activations from STA's post-training structural approach.

Looking at what's covered, the paper handles the major foundations well: the Manheim & Garrabrant taxonomy, Skalse et al., METR, overoptimization work, FOLIO, neurosymbolic reasoning, Wilhelm with a clear complementarity statement, and extensive concurrent work from 2025-2026. The only potentially missing pieces are the original Goodhart and Strathern papers, but those are economics sources rather than standard ML citations, so they're not critical. Whether to add the other papers from the search results would be a director-level call based on how comprehensive they want the related work section to be. I'm scanning through the bibliography to identify which entries are included but never actually cited in the paper—entries like the reward hacking survey, shortcut learning work, and several model papers appear in the references but I need to verify they're not mentioned anywhere else in the document.

Now I'm checking that the paper and docs directories have matching versions of the related work and bibliography files, which they do. For the Goodhart's Law citation, the Manheim & Garrabrant taxonomy paper is the appropriate ML reference to cite rather than tracking back to the original 1975 formulation, so that's sufficient for an EMNLP venue.

The neurosymbolic coverage looks complete with FOLIO cited, and the recent 2025-2026 work is already well-represented across six papers in the concurrent work section. Wilhelm's contribution is clearly positioned on line 26. Overall, the related work section is solid with no critical gaps—I'll compile my findings with a list of potentially relevant papers for the Director to review, but I don't see a need for changes to the current text.

Let me verify one more thing about neurosymbolic RL representative works to make sure nothing important is missing. I'm checking whether the files in both directories are actually identical, since git is showing both as modified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "76c7bc44-e758-4876-9f7d-aac2b95b3f86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XMMzNP99kDq9F2NZrpbgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10152,
      "cache_creation_input_tokens": 3222,
      "cache_read_input_tokens": 37394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3222
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

_source line 90_

Both directories' files are identical. Let me verify one more thing — whether `reward-hacking-survey` is cited anywhere (it's in bib but not in related_work.tex).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "432ce2b4-c92c-4c73-8224-a01de8d26050",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XMMzNP99kDq9F2NZrpbgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10152,
      "cache_creation_input_tokens": 3222,
      "cache_read_input_tokens": 37394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3222
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

_source line 91_

<details open><summary>🔧 Tool call — Grep · `toolu_01XpDEDirXxVuTznLArvArjN`</summary>

```json
{
  "pattern": "reward-hacking-survey",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "337949bf-c11e-410d-b824-08106194ee06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XMMzNP99kDq9F2NZrpbgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10152,
      "cache_creation_input_tokens": 3222,
      "cache_read_input_tokens": 37394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3222
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

_source line 92 · 2026-05-22T18:50:23.897Z_

<details><summary>↩ Tool result · `toolu_01XpDEDirXxVuTznLArvArjN`</summary>

```text
artifacts/submission_package/introduction.tex:9:Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
artifacts/submission/introduction.tex:9:Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
artifacts/_project/paper/related_work.tex:31:In the LLM setting specifically, recent surveys~\cite{reward-hacking-survey} document reward hacking across the full spectrum from specification gaming to emergent misalignment.
artifacts/_project/paper/introduction_b19e34.tex:12:Specification gaming of this kind has been documented in reasoning models more broadly~\citep{bondarenko-spec-gaming}, and a growing body of work studies reward hacking mechanisms in LLM training~\citep{reward-hacking-survey}, yet systematic characterization in neurosymbolic RL remains absent.
artifacts/_project/paper/introduction_41056c.tex:10:This gap is particularly consequential in reinforcement learning settings, where the optimizer will find and exploit any shortcut the reward function fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
artifacts/_project/paper/introduction_176853.tex:10:Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
artifacts/_project/paper/introduction.tex:12:Specification gaming of this kind has been documented in reasoning models more broadly~\citep{bondarenko-spec-gaming}, and a growing body of work studies reward hacking mechanisms in LLM training~\citep{reward-hacking-survey}, yet systematic characterization in neurosymbolic RL remains absent.
artifacts/_project/paper/related_work_b05493.tex:31:In the LLM setting specifically, recent surveys~\cite{reward-hacking-survey} document reward hacking across the full spectrum from specification gaming to emergent misalignment.
artifacts/_project/paper/introduction_12a465.tex:10:Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
paper/introduction.tex:6:Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
docs/paper/introduction.tex:6:Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "03a11597-c708-49f7-ab4d-2307d7564080",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/submission_package/introduction.tex:9:Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nartifacts/submission/introduction.tex:9:Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nartifacts/_project/paper/related_work.tex:31:In the LLM setting specifically, recent surveys~\\cite{reward-hacking-survey} document reward hacking across the full spectrum from specification gaming to emergent misalignment.\nartifacts/_project/paper/introduction_b19e34.tex:12:Specification gaming of this kind has been documented in reasoning models more broadly~\\citep{bondarenko-spec-gaming}, and a growing body of work studies reward hacking mechanisms in LLM training~\\citep{reward-hacking-survey}, yet systematic characterization in neurosymbolic RL remains absent.\nartifacts/_project/paper/introduction_41056c.tex:10:This gap is particularly consequential in reinforcement learning settings, where the optimizer will find and exploit any shortcut the reward function fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nartifacts/_project/paper/introduction_176853.tex:10:Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nartifacts/_project/paper/introduction.tex:12:Specification gaming of this kind has been documented in reasoning models more broadly~\\citep{bondarenko-spec-gaming}, and a growing body of work studies reward hacking mechanisms in LLM training~\\citep{reward-hacking-survey}, yet systematic characterization in neurosymbolic RL remains absent.\nartifacts/_project/paper/related_work_b05493.tex:31:In the LLM setting specifically, recent surveys~\\cite{reward-hacking-survey} document reward hacking across the full spectrum from specification gaming to emergent misalignment.\nartifacts/_project/paper/introduction_12a465.tex:10:Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\npaper/introduction.tex:6:Under reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\ndocs/paper/introduction.tex:6:Under reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.",
    "numLines": 11
  }
}
```

</details>

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Grep · `toolu_01RtGpw5bLGnjtiWcwmYQ3S1`</summary>

```json
{
  "pattern": "geirhos2020shortcut",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "cb96ebfc-1c3c-483e-ba54-d813f4747ab3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XMMzNP99kDq9F2NZrpbgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10152,
      "cache_creation_input_tokens": 3222,
      "cache_read_input_tokens": 37394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3222
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

_source line 94 · 2026-05-22T18:50:24.322Z_

<details><summary>↩ Tool result · `toolu_01RtGpw5bLGnjtiWcwmYQ3S1`</summary>

```text
paper/introduction.tex:6:Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
docs/paper/introduction.tex:6:Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "70d09b80-70ce-497f-b588-88f86fc8fadf",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/introduction.tex:6:Under reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.\ndocs/paper/introduction.tex:6:Under reinforcement learning, this indifference becomes an active vulnerability~\\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 95_

<details><summary>Logged reasoning block</summary>

```text
Good - `reward-hacking-survey` and `geirhos2020shortcut` are both cited in `introduction.tex` (in both `paper/` and `docs/paper/`), just not in `related_work.tex`. That's fine - they're used in the paper, just in a different section.

Now let me compile my coverage check report. The two directories' `related_work.tex` and `references.bib` are identical (I read both and they match). No changes needed.

Let me also quickly verify the docs/paper/ vs paper/ files are truly identical for related_work.tex and references.bib.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "a6f4e436-a483-4cf4-b76a-5119572b558c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAHfDSAewDRpm3BHUV51Dm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14079,
      "cache_read_input_tokens": 40616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14079
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

_source line 96_

Let me verify the two directories are in sync.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "c8e1e02d-8aa0-4fdc-b2f5-492b0d76adff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAHfDSAewDRpm3BHUV51Dm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14079,
      "cache_read_input_tokens": 40616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14079
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

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xr7ULnbtiayrKRqvzniHHa`</summary>

```json
{
  "command": "diff /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "description": "Diff related_work.tex between two directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "0ce3185c-c48a-4c71-93da-eb70d3901de8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAHfDSAewDRpm3BHUV51Dm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14079,
      "cache_read_input_tokens": 40616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14079
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

_source line 98 · 2026-05-22T18:50:31.303Z_

<details><summary>↩ Tool result · `toolu_01Xr7ULnbtiayrKRqvzniHHa`</summary>

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
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "08c8eba1-8344-4ac7-88b4-6a8fb07fc603",
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

### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_011dswUJJ5fMW4qjLBuPEv9E`</summary>

```json
{
  "command": "diff /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "description": "Diff references.bib between two directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "c9c3d88b-4d0f-457d-aaf6-ac53c9c2d79a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HAHfDSAewDRpm3BHUV51Dm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14079,
      "cache_read_input_tokens": 40616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14079
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

_source line 100 · 2026-05-22T18:50:32.048Z_

<details><summary>↩ Tool result · `toolu_011dswUJJ5fMW4qjLBuPEv9E`</summary>

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
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "b2f6e5d2-1540-44a6-8147-8760308304ab",
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

_source line 101_

两个目录完全同步，无需修改。以下是覆盖度检查结果。

---

## 覆盖度检查结果

### 1. Reward Hacking 核心引用

| 引用 | bib | related_work.tex | 状态 |
|------|-----|-------------------|------|
| Manheim & Garrabrant taxonomy | ✅ `manheim-goodhart-taxonomy` | ✅ L17, L25 | OK |
| Skalse et al. (formal definition) | ✅ `skalse-reward-hacking` | ✅ L17 | OK |
| METR reward hacking | ✅ `metr-reward-hacking` | ✅ L21 | OK |
| Gao et al. overoptimization scaling laws | ✅ `gao-reward-overoptimization` | ✅ L17 | OK |
| Goodhart 1975 原始论文 | ❌ | ❌ | **可选** — ML 顶会惯例引 Manheim taxonomy 即可 |
| Strathern 1997 | ❌ | ❌ | **可选** — 同上 |

### 2. Neurosymbolic Reasoning + RL

| 引用 | 状态 |
|------|------|
| FOLIO 原始论文 | ✅ L7 |
| LLM-solver pipelines (SatLM, Logic-LM, LINC, FoVer, LoRP) | ✅ L5 |
| RL+solver (mellgren-prolog-grpo, logic-rl, DeepSeek-Prover-V1.5, DeepSeek-R1) | ✅ L5 |
| AlphaProof, DeepSeek-Prover-V2 | ✅ L6 |

覆盖完整，无遗漏。

### 3. 2025-2026 Concurrent Work

已引用的（共 10 篇 concurrent work）：
- spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking (L21)
- tarek2025reward, pronesti2026beyond (L21)
- yue2025rl-reasoning (L21)
- helff2026gaming (L22-23)
- khalifa2026countdown (L24)
- wilhelm2026monitoring (L26)

**WebSearch 发现的未引用论文（供 Director 判断是否添加）：**

| 论文 | arXiv | 一句话 | 建议 |
|------|-------|--------|------|
| Wang et al. "Detecting and Suppressing Reward Hacking with Gradient Fingerprints" (GRIFT) | 2604.16242 | 梯度指纹检测隐式 reward hacking，文本 CoT 监控无法捕获 | 低优先 — 方法层面不同（gradient vs. LOO），且已有 IPT/Wilhelm 两种对比方法 |
| Wang et al. "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort" (TRACE) | 2510.01367 | 截断 CoT 测量推理 effort 以检测隐式 hacking | 低优先 — truncation-based，与 STA 的 LOO 方法正交 |
| Wu & Tang "When Reward Hacking Rebounds" | 2604.01476 | 发现 RLVR 三阶段 rebound pattern（尝试→撤退→反弹成功 hack） | 中等 — rebound 动态与论文的 training curve collapse 有呼应，但在 coding tasks 上 |
| Wang & Huang "Reward Hacking as Equilibrium under Finite Evaluation" | 2603.28063 | 证明 reward hacking 是结构性均衡而非 bug | 低优先 — 纯理论，与实证工作距离远 |

**结论：无关键缺失。** 已有引用密度对 EMNLP 8 页论文已经很高（related work 段落内引用 30+ 篇），添加更多可能导致臃肿。上述 4 篇均为 nice-to-have。

### 4. Wilhelm et al. (2026) 互补性讨论

L26: `"Complementarily, \citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic."`

清晰区分了：
- **Wilhelm**: generation-time detection via internal activations
- **STA**: post-training structural diagnostic (LOO)
- 互补关系明确

**无需修改。**

---

## 总结

- **实际修改：0 处** — 覆盖度检查通过，无关键缺失
- **两个目录同步状态：** `related_work.tex` 和 `references.bib` 完全一致
- **Director 决策项：** 上述 4 篇 2025-2026 论文是否需要添加（建议不添加，当前密度已足够）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "uuid": "0f609e88-c845-4a7f-afc3-a74227ad7e04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtvcYNUGFJrHftpPFY6u7G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 526,
      "cache_read_input_tokens": 54695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 526
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

_source line 102_

两个目录完全同步，无需修改。以下是覆盖度检查结果。

---

## 覆盖度检查结果

### 1. Reward Hacking 核心引用

| 引用 | bib | related_work.tex | 状态 |
|------|-----|-------------------|------|
| Manheim & Garrabrant taxonomy | ✅ `manheim-goodhart-taxonomy` | ✅ L17, L25 | OK |
| Skalse et al. (formal definition) | ✅ `skalse-reward-hacking` | ✅ L17 | OK |
| METR reward hacking | ✅ `metr-reward-hacking` | ✅ L21 | OK |
| Gao et al. overoptimization scaling laws | ✅ `gao-reward-overoptimization` | ✅ L17 | OK |
| Goodhart 1975 原始论文 | ❌ | ❌ | **可选** — ML 顶会惯例引 Manheim taxonomy 即可 |
| Strathern 1997 | ❌ | ❌ | **可选** — 同上 |

### 2. Neurosymbolic Reasoning + RL

| 引用 | 状态 |
|------|------|
| FOLIO 原始论文 | ✅ L7 |
| LLM-solver pipelines (SatLM, Logic-LM, LINC, FoVer, LoRP) | ✅ L5 |
| RL+solver (mellgren-prolog-grpo, logic-rl, DeepSeek-Prover-V1.5, DeepSeek-R1) | ✅ L5 |
| AlphaProof, DeepSeek-Prover-V2 | ✅ L6 |

覆盖完整，无遗漏。

### 3. 2025-2026 Concurrent Work

已引用的（共 10 篇 concurrent work）：
- spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking (L21)
- tarek2025reward, pronesti2026beyond (L21)
- yue2025rl-reasoning (L21)
- helff2026gaming (L22-23)
- khalifa2026countdown (L24)
- wilhelm2026monitoring (L26)

**WebSearch 发现的未引用论文（供 Director 判断是否添加）：**

| 论文 | arXiv | 一句话 | 建议 |
|------|-------|--------|------|
| Wang et al. "Detecting and Suppressing Reward Hacking with Gradient Fingerprints" (GRIFT) | 2604.16242 | 梯度指纹检测隐式 reward hacking，文本 CoT 监控无法捕获 | 低优先 — 方法层面不同（gradient vs. LOO），且已有 IPT/Wilhelm 两种对比方法 |
| Wang et al. "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort" (TRACE) | 2510.01367 | 截断 CoT 测量推理 effort 以检测隐式 hacking | 低优先 — truncation-based，与 STA 的 LOO 方法正交 |
| Wu & Tang "When Reward Hacking Rebounds" | 2604.01476 | 发现 RLVR 三阶段 rebound pattern（尝试→撤退→反弹成功 hack） | 中等 — rebound 动态与论文的 training curve collapse 有呼应，但在 coding tasks 上 |
| Wang & Huang "Reward Hacking as Equilibrium under Finite Evaluation" | 2603.28063 | 证明 reward hacking 是结构性均衡而非 bug | 低优先 — 纯理论，与实证工作距离远 |

**结论：无关键缺失。** 已有引用密度对 EMNLP 8 页论文已经很高（related work 段落内引用 30+ 篇），添加更多可能导致臃肿。上述 4 篇均为 nice-to-have。

### 4. Wilhelm et al. (2026) 互补性讨论

L26: `"Complementarily, \citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic."`

清晰区分了：
- **Wilhelm**: generation-time detection via internal activations
- **STA**: post-training structural diagnostic (LOO)
- 互补关系明确

**无需修改。**

---

## 总结

- **实际修改：0 处** — 覆盖度检查通过，无关键缺失
- **两个目录同步状态：** `related_work.tex` 和 `references.bib` 完全一致
- **Director 决策项：** 上述 4 篇 2025-2026 论文是否需要添加（建议不添加，当前密度已足够）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 221238,
  "duration_api_ms": 345031,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "059a7c71-72fc-4ac4-8488-45da037817c3",
  "total_cost_usd": 1.42033175,
  "usage": {
    "input_tokens": 10158,
    "cache_creation_input_tokens": 43380,
    "cache_read_input_tokens": 171597,
    "output_tokens": 5883,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 43380,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1388,
        "cache_read_input_tokens": 54695,
        "cache_creation_input_tokens": 526,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 526
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 228144,
      "outputTokens": 9462,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 22,
      "costUSD": 0.495454,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13251,
      "outputTokens": 9196,
      "cacheReadInputTokens": 285083,
      "cacheCreationInputTokens": 77789,
      "webSearchRequests": 0,
      "costUSD": 0.9248777499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "afd2a8ba-cbf1-42b3-88a9-eb6880bdfb52"
}
```

</details>

---
