# paper text fixes r24

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 2
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_paper_text-fixes-r24_20260522T030823.log`
- **Structured JSON:** [`e71c071a99862345f694.json`](../../sessions/e7/e71c071a99862345f694.json)

## Before a recorded user message

21 recorded events

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
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
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
  "uuid": "94545d8f-8d05-4264-a165-875c97368b20",
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
    "resetsAt": 1779435000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "99cc15fc-82aa-4a9b-8629-4fb8bbc39ebe",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant files to understand the current state before making any changes. I'll read all the files I need in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "e032e3e9-7c1c-405a-b2b9-3ff5bae29834",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb2TP2Y1ERPa76QLjfxCyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15199
      },
      "output_tokens": 25,
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

I'll read all the relevant files first, then make the changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "d923884f-272b-4008-9425-6b330f9ceeeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb2TP2Y1ERPa76QLjfxCyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15199
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — Read · `toolu_01RK9xMZAfZow4zyQH39BL6k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "ee7c4919-4191-4b1b-ab18-138aaef7b022",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb2TP2Y1ERPa76QLjfxCyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15199
      },
      "output_tokens": 25,
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

_source line 7 · 2026-05-22T03:08:37.074Z_

<details><summary>↩ Tool result · `toolu_01RK9xMZAfZow4zyQH39BL6k`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: the mode breakdown reveals ${\geq}87\%$ structural hacking under exec-only GRPO while PR rises (ISR collapses $214\times$ for seed~42, partially amplified by premise-count inflation), while SFT results are consistent with GRPO-specific degradation (\S\ref{sec:diagnostic}).
5	Cross-logic replication in Prolog confirms the phenomenon generalizes beyond FOL (\S\ref{sec:crosslogic}).
6	Repurposed as a reward, ISR produces a seed-dependent compositional Goodhart effect: on FOLIO, 3 of 5 seeds shift hacking from CE to TS ($p{<}10^{-15}$) without reducing prevalence ($p{=}0.182$), while 2 retain ${\sim}55\%$ non-hacking; deconfounding collapses the apparent ISR advantage to $1.06\times$; on ProofFOL, preliminary evidence ($p{=}0.10$) suggests beneficial instability (\S\ref{sec:goodhart}).
7	The central finding is ISR's observer/optimizer asymmetry: the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward, with outcomes depending on whether the dataset's hacking geometry satisfies the metric.
8	
9	For practitioners in similar settings (\S\ref{sec:limitations}): evaluate with ISR and component count jointly (not PR alone), report multi-seed results, and use ISR for post-hoc diagnosis only---any dose induces gaming or collapse when optimized (Appendix~\ref{app:practical-guidelines}).
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "74ab9e83-47fb-45dd-8e70-679ea7712397",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation: the mode breakdown reveals ${\\geq}87\\%$ structural hacking under exec-only GRPO while PR rises (ISR collapses $214\\times$ for seed~42, partially amplified by premise-count inflation), while SFT results are consistent with GRPO-specific degradation (\\S\\ref{sec:diagnostic}).\nCross-logic replication in Prolog confirms the phenomenon generalizes beyond FOL (\\S\\ref{sec:crosslogic}).\nRepurposed as a reward, ISR produces a seed-dependent compositional Goodhart effect: on FOLIO, 3 of 5 seeds shift hacking from CE to TS ($p{<}10^{-15}$) without reducing prevalence ($p{=}0.182$), while 2 retain ${\\sim}55\\%$ non-hacking; deconfounding collapses the apparent ISR advantage to $1.06\\times$; on ProofFOL, preliminary evidence ($p{=}0.10$) suggests beneficial instability (\\S\\ref{sec:goodhart}).\nThe central finding is ISR's observer/optimizer asymmetry: the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward, with outcomes depending on whether the dataset's hacking geometry satisfies the metric.\n\nFor practitioners in similar settings (\\S\\ref{sec:limitations}): evaluate with ISR and component count jointly (not PR alone), report multi-seed results, and use ISR for post-hoc diagnosis only---any dose induces gaming or collapse when optimized (Appendix~\\ref{app:practical-guidelines}).\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01WxVHMoWz8p3WyefNo4toYy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "4329ef77-2d31-4143-aeda-a323b415356e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb2TP2Y1ERPa76QLjfxCyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15199
      },
      "output_tokens": 25,
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

_source line 9 · 2026-05-22T03:08:37.576Z_

<details><summary>↩ Tool result · `toolu_01WxVHMoWz8p3WyefNo4toYy`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); RLVR gains from random or incorrect rewards have been shown to be Qwen-specific~\citep{spurious-rewards}, so the structural degeneration patterns we document may not transfer identically to other model families.
5	Cross-dataset evidence (ProofFOL, Prolog) supports generality, but LLaMA-3.2-3B achieves only $\text{PR}{\approx}15\%$ after SFT warmstart with GRPO unable to amplify beyond this baseline (Appendix~\ref{app:llama-coldstart}), establishing a capability threshold below which STA's degeneration analysis is uninformative (the model cannot hack what it cannot prove).
6	Three seeds demonstrate qualitative divergence but limit statistical power ($N{=}3$ independent replications); all pooled statistics treat within-seed samples as independent, and the ProofFOL genuine-rate advantage ($p{=}0.10$) is an observation, not a confirmed effect.
7	At our scale (500 training / 100 evaluation examples), non-hacking rates of ${\sim}5\%$ correspond to ${\sim}5$ samples, limiting mode-level precision.
8	ISR quantifies syntactic component necessity, not semantic faithfulness ($\rho{=}{-}0.049$ with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	Intermediate checkpoints (100--900 steps) were not retained; trajectory analyses rely on saved evaluation outputs at recorded steps.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "7a0bf327-5398-4387-b871-e7edbfcbe52c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B); RLVR gains from random or incorrect rewards have been shown to be Qwen-specific~\\citep{spurious-rewards}, so the structural degeneration patterns we document may not transfer identically to other model families.\nCross-dataset evidence (ProofFOL, Prolog) supports generality, but LLaMA-3.2-3B achieves only $\\text{PR}{\\approx}15\\%$ after SFT warmstart with GRPO unable to amplify beyond this baseline (Appendix~\\ref{app:llama-coldstart}), establishing a capability threshold below which STA's degeneration analysis is uninformative (the model cannot hack what it cannot prove).\nThree seeds demonstrate qualitative divergence but limit statistical power ($N{=}3$ independent replications); all pooled statistics treat within-seed samples as independent, and the ProofFOL genuine-rate advantage ($p{=}0.10$) is an observation, not a confirmed effect.\nAt our scale (500 training / 100 evaluation examples), non-hacking rates of ${\\sim}5\\%$ correspond to ${\\sim}5$ samples, limiting mode-level precision.\nISR quantifies syntactic component necessity, not semantic faithfulness ($\\rho{=}{-}0.049$ with NLI accuracy; Appendix~\\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.\nIntermediate checkpoints (100--900 steps) were not retained; trajectory analyses rely on saved evaluation outputs at recorded steps.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01Tot76iaA6Ukq6oBVaLRHXw`</summary>

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
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "2c862691-88f6-4a22-abba-e827376e41ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb2TP2Y1ERPa76QLjfxCyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15199
      },
      "output_tokens": 25,
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

_source line 11 · 2026-05-22T03:08:38.561Z_

<details><summary>↩ Tool result · `toolu_01Tot76iaA6Ukq6oBVaLRHXw`</summary>

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
463	@misc{mccune-prover9,
464	  author       = {William McCune},
465	  title        = {{Prover9 and Mace4}},
466	  year         = {2005--2010},
467	  howpublished = {\url{https://www.cs.unm.edu/~mccune/prover9/}},
468	  note         = {Version 2009-11A},
469	}
470	
471	@article{wielemaker2012swi,
472	  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\"o}rn Lager},
473	  title        = {{SWI-Prolog}},
474	  journal      = {Theory and Practice of Logic Programming},
475	  volume       = {12},
476	  number       = {1--2},
477	  pages        = {67--96},
478	  year         = {2012},
479	  doi          = {10.1017/S1471068411000494},
480	}
481	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "40404d15-e3d4-4fc7-a674-2846458db83e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
      "content": "% ============================================================\n% LLaMA\n% ============================================================\n\n@article{grattafiori2024llama,\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},\n  title = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n  eprint = {2407.21783},\n  archiveprefix = {arXiv},\n}\n\n% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--41},\n  year         = {1978},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@article{spurious-rewards,\n  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Reward shaping and process supervision\n% ============================================================\n\n@article{rlsf,\n  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},\n  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\\`{a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  note         = {arXiv:2404.18926},\n}\n\n@article{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  journal      = {arXiv preprint arXiv:2408.08152},\n  year         = {2024},\n  eprint       = {2408.08152},\n  archivePrefix = {arXiv},\n}\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2501.12948},\n  year         = {2025},\n  eprint       = {2501.12948},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nlproofs,\n  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},\n  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},\n  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2022},\n  eprint       = {2205.12443},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{vstar,\n  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},\n  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},\n  booktitle    = {Conference on Language Modeling (COLM)},\n  year         = {2024},\n  eprint       = {2402.06457},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{easy-to-hard,\n  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},\n  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  eprint       = {2403.09472},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@article{reward-hacking-survey,\n  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n}\n\n@misc{metr-reward-hacking,\n  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR Technical Blog},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2021},\n  note         = {arXiv:2012.13048},\n}\n\n@article{prooffol-thatikonda2024,\n  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},\n  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},\n  journal      = {arXiv preprint arXiv:2409.16461},\n  year         = {2024},\n  eprint       = {2409.16461},\n  archivePrefix = {arXiv},\n}\n\n@article{qwen3,\n  author       = {{Qwen Team}},\n  title        = {{Qwen3 Technical Report}},\n  journal      = {arXiv preprint arXiv:2505.09388},\n  year         = {2025},\n  eprint       = {2505.09388},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@article{helff2026gaming,\n  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\\\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},\n  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},\n  journal      = {arXiv preprint arXiv:2604.15149},\n  year         = {2026},\n  eprint       = {2604.15149},\n  archivePrefix = {arXiv},\n}\n\n@article{khalifa2026countdown,\n  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},\n  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},\n  journal      = {arXiv preprint arXiv:2603.07084},\n  year         = {2026},\n  eprint       = {2603.07084},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{uesato2022solving,\n  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},\n  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},\n  booktitle={NeurIPS 2022 Workshop on MATH-AI},\n  year={2022}\n}\n\n@article{cobbe2021training,\n  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},\n  title        = {{Training Verifiers to Solve Math Word Problems}},\n  journal      = {arXiv preprint arXiv:2110.14168},\n  year         = {2021},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{pronesti2026beyond,\n  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},\n  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},\n  journal      = {arXiv preprint arXiv:2601.17223},\n  year         = {2026},\n  eprint       = {2601.17223},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{ng1999policy,\n  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},\n  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year      = {1999},\n  pages     = {278--287},\n}\n\n@article{geirhos2020shortcut,\n  author  = {Robert Geirhos and J{\\\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},\n  title   = {Shortcut Learning in Deep Neural Networks},\n  journal = {Nature Machine Intelligence},\n  volume  = {2},\n  pages   = {665--673},\n  year    = {2020},\n}\n\n@article{dong2026probing,\n  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},\n  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},\n  journal      = {arXiv preprint arXiv:2602.01103},\n  year         = {2026},\n  eprint       = {2602.01103},\n  archivePrefix = {arXiv},\n}\n\n@article{yan2026spurious,\n  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},\n  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},\n  journal      = {arXiv preprint arXiv:2601.11061},\n  year         = {2026},\n  eprint       = {2601.11061},\n  archivePrefix = {arXiv},\n}\n\n@article{tarek2025reward,\n  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},\n  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},\n  journal      = {arXiv preprint arXiv:2509.15557},\n  year         = {2025},\n  eprint       = {2509.15557},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{yue2025rl-reasoning,\n  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},\n  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2025},\n  eprint       = {2504.13837},\n  archivePrefix = {arXiv},\n}\n\n@article{sullivan2025grpo-prm,\n  author       = {Michael Sullivan and Alexander Koller},\n  title        = {{GRPO} is Secretly a Process Reward Model},\n  journal      = {arXiv preprint arXiv:2509.21154},\n  year         = {2025},\n  eprint       = {2509.21154},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% R19 reviewer-requested references\n% ============================================================\n\n@inproceedings{setlur2025rewarding,\n  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},\n  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2410.08146},\n}\n\n@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}\n\n% ============================================================\n% Solvers (Prover9, SWI-Prolog)\n% ============================================================\n\n@misc{mccune-prover9,\n  author       = {William McCune},\n  title        = {{Prover9 and Mace4}},\n  year         = {2005--2010},\n  howpublished = {\\url{https://www.cs.unm.edu/~mccune/prover9/}},\n  note         = {Version 2009-11A},\n}\n\n@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n",
      "numLines": 481,
      "startLine": 1,
      "totalLines": 481
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01ACoLbLJxm2WpiWVuaiFvJF`</summary>

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
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "cd736175-fbb3-435a-ac57-139306784af4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb2TP2Y1ERPa76QLjfxCyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15199
      },
      "output_tokens": 25,
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

_source line 13 · 2026-05-22T03:08:39.044Z_

<details><summary>↩ Tool result · `toolu_01ACoLbLJxm2WpiWVuaiFvJF`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
11	Learned PRMs~\citep{lightman-verify-step, math-shepherd} and verifier-guided search~\citep{nlproofs, vstar} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; \citet{easy-to-hard} show that verifiers trained on easy tasks can generalize to hard ones, though structural gaming remains unaddressed.
12	\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\beta$-dependent Goodhart transitions.
13	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly equivalent to a Monte-Carlo PRM, offering a mechanism for why component-level gaming emerges under GRPO specifically.
15	
16	\paragraph{Reward hacking and Goodhart's Law.}
17	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
18	\citet{kim-game-formalization} document inference-time gaming in logical formalization on FOLIO using frontier models with Lean~4.
19	Our work is complementary: training-time (vs.\ inference), component necessity (vs.\ faithfulness), medium-model/Prover9 (vs.\ frontier/Lean~4); combining STA with inference-time faithfulness detection would provide complete gaming coverage.
20	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.
21	Recent work further documents spurious reward signals in RLVR~\citep{spurious-rewards, yan2026spurious}, training instability via objective-level hacking~\citep{dong2026probing}, reward hacking in frontier models~\citep{metr-reward-hacking}, and proposes verifiable composite or process rewards to mitigate outcome-only limitations~\citep{tarek2025reward, pronesti2026beyond}.
22	\citet{yue2025rl-reasoning} show RLVR redistributes probability mass over base-model capabilities rather than eliciting new reasoning patterns, consistent with our finding that GRPO-trained models exploit existing shortcuts rather than learning genuine derivation.
23	\citet{helff2026gaming} propose Input Perturbation Testing (IPT), which perturbs verifier inputs to detect gaming; STA shares the perturbation intuition but operates at the component level (LOO ablation on solver premises vs.\ token-level perturbation on verifier prompts) and targets neurosymbolic settings where gaming \emph{emerges during training}.
24	\citet{khalifa2026countdown} provide RLVR hacking testbeds.
25	The Goodhart effect follows standard taxonomy~\citep{manheim-goodhart-taxonomy}: regressional on FOLIO (tautologies satisfy the LOO metric), extremal at high $\beta$. Its application to a structural diagnostic designed to \emph{detect} gaming is, to our knowledge, novel; the dataset-dependent asymmetry (the same metric gamed on one dataset, beneficial on another) is a non-trivial empirical finding not predicted by the taxonomy alone.
26	
27	\paragraph{Mutation testing.}
28	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "d81532cd-a434-48ff-900e-25d6f11e8cfe",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nReward shaping theory~\\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\\citep{uesato2022solving}.\nLearned PRMs~\\citep{lightman-verify-step, math-shepherd} and verifier-guided search~\\citep{nlproofs, vstar} provide step-level feedback but suffer from reward-model noise and distribution shift~\\citep{processbench}; \\citet{easy-to-hard} show that verifiers trained on easy tasks can generalize to hard ones, though structural gaming remains unaddressed.\n\\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \\citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\\beta$-dependent Goodhart transitions.\nSymbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\n\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly equivalent to a Monte-Carlo PRM, offering a mechanism for why component-level gaming emerges under GRPO specifically.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.\n\\citet{kim-game-formalization} document inference-time gaming in logical formalization on FOLIO using frontier models with Lean~4.\nOur work is complementary: training-time (vs.\\ inference), component necessity (vs.\\ faithfulness), medium-model/Prover9 (vs.\\ frontier/Lean~4); combining STA with inference-time faithfulness detection would provide complete gaming coverage.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.\nRecent work further documents spurious reward signals in RLVR~\\citep{spurious-rewards, yan2026spurious}, training instability via objective-level hacking~\\citep{dong2026probing}, reward hacking in frontier models~\\citep{metr-reward-hacking}, and proposes verifiable composite or process rewards to mitigate outcome-only limitations~\\citep{tarek2025reward, pronesti2026beyond}.\n\\citet{yue2025rl-reasoning} show RLVR redistributes probability mass over base-model capabilities rather than eliciting new reasoning patterns, consistent with our finding that GRPO-trained models exploit existing shortcuts rather than learning genuine derivation.\n\\citet{helff2026gaming} propose Input Perturbation Testing (IPT), which perturbs verifier inputs to detect gaming; STA shares the perturbation intuition but operates at the component level (LOO ablation on solver premises vs.\\ token-level perturbation on verifier prompts) and targets neurosymbolic settings where gaming \\emph{emerges during training}.\n\\citet{khalifa2026countdown} provide RLVR hacking testbeds.\nThe Goodhart effect follows standard taxonomy~\\citep{manheim-goodhart-taxonomy}: regressional on FOLIO (tautologies satisfy the LOO metric), extremal at high $\\beta$. Its application to a structural diagnostic designed to \\emph{detect} gaming is, to our knowledge, novel; the dataset-dependent asymmetry (the same metric gamed on one dataset, beneficial on another) is a non-trivial empirical finding not predicted by the taxonomy alone.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01CFqdnMuDvqah84hGqU8uoN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "7893cf28-e1c0-4ad5-a23a-47469f785fa2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb2TP2Y1ERPa76QLjfxCyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15199
      },
      "output_tokens": 25,
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

_source line 15 · 2026-05-22T03:08:39.721Z_

<details><summary>↩ Tool result · `toolu_01CFqdnMuDvqah84hGqU8uoN`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems, yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut (an instance of shortcut learning~\citep{geirhos2020shortcut} in the neurosymbolic setting) is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on component necessity.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for component necessity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}, leave-one-out (LOO) ablation on solver inputs, to quantify component necessity.
16	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
17	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution is the empirical discovery that the same LOO structure making ISR informative as a diagnostic also makes it vulnerable to gaming as a reward, a compositional Goodhart effect on structural metrics.
18	ISR captures component necessity rather than semantic faithfulness (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
19	
20	\begin{figure}[t]
21	\centering
22	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
23	\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\text{ISR}{\approx}0$, confirming structural degeneration (\S\ref{sec:diagnostic}); the ${\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\beta{=}0.1$ seeds rise toward $\text{ISR}{\approx}1$ via TS gaming (Goodhart effect, \S\ref{sec:goodhart}); random remains low.}
24	\label{fig:training-isr-curves}
25	\end{figure}
26	
27	\paragraph{ISR as diagnostic.}
28	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR (Figure~\ref{fig:training-isr-curves}): for seed~42, $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (partially amplified by component-count inflation; mode breakdown confirms 87\% CE at 500 steps, independent of the ISR scalar; all 3 seeds: ${\leq}7\%$ non-hacking by 1000 steps) while PR rises $32\%{\to}96\%$.
29	Three seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different mode (conclusion embedding, repetition collapse, and tautological collapse), yet all reach ${\geq}93\%$ structural hacking by 1000 steps.
30	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (upper bound; 3-seed pooled, 1000 steps), consistent with GRPO-specific degradation rather than data or capacity limitations.
31	
32	\paragraph{Goodhart effects.}
33	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR produces a seed-dependent compositional Goodhart effect~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
34	On FOLIO, this instantiates \emph{regressional} Goodhart~\citep{manheim-goodhart-taxonomy}: $P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR rewards the shortcut; at $\beta{=}0.1$, 3 of 5 seeds shift hacking composition from CE to TS ($p{<}10^{-15}$) without reducing prevalence ($p{=}0.182$), while 2 of 5 seeds retain ${\sim}55\%$ genuine reasoning; the sole apparent ISR advantage reduces to $1.06\times$ after controlling for premise count.
35	At $\beta{\geq}0.2$, \emph{extremal} Goodhart dominates ($\text{PR}{=}66{\pm}42\%$ ISR, $54{\pm}35\%$ random at $\beta{=}0.3$).
36	On ProofFOL, hacking yields $\text{ISR}{=}0.0$, so ISR correctly penalizes shortcuts, associated with beneficial instability (76.8\% vs.\ 17.4\% genuine under a coarser binary classifier, $p{=}0.10$).
37	ISR's asymmetry is the central finding: \emph{reliable as observer, dataset-dependent as optimizer.}
38	
39	\paragraph{Contributions.}
40	In this case study (Qwen3-4B, 6 reward conditions, 3--5 seeds, 2 logic types, 2 dataset families, up to 1000 steps), we contribute: (\textbf{C1}) STA as a diagnostic framework (ISR metric, eight-mode hacking taxonomy, and cross-domain evaluation protocol) revealing structural collapse invisible to PR (${\leq}7\%$ non-hacking, 3 seeds, 1000 steps; 99.5\% in seed~42), with an SFT control consistent with GRPO-specific degradation (\S\ref{sec:diagnostic}); (\textbf{C2}) a seed-dependent compositional Goodhart effect on ISR-as-reward: in 3 of 5 seeds, significant composition shift CE$\to$TS ($p{<}10^{-15}$) without prevalence reduction ($p{=}0.182$); 2 of 5 seeds retain ${\sim}55\%$ genuine reasoning, showing the effect is stochastic; apparent ISR advantage collapses to $1.06\times$ after deconfounding; shuffled-ISR control rules out distributional shape (\S\ref{sec:goodhart}), with cross-domain evidence: confirmed in Prolog (3/3 seeds 0\% non-hacking) and exploratory in ProofFOL ($p{=}0.10$), showing dataset-dependent outcomes (\S\ref{sec:crossdomain}).
41	These are cautionary results from a Qwen3-4B case study, replicated across dataset families, relevant to any work treating a structural proxy as a training signal (generalization scope discussed in \S\ref{sec:limitations}).
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "589aab4b-efa7-4d39-a964-3d08585c9482",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on first-order logic problems, yet 87\\% of its proved outputs embed the conclusion verbatim among the premises.\nThe solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.\nThis structural shortcut (an instance of shortcut learning~\\citep{geirhos2020shortcut} in the neurosymbolic setting) is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.\n\n\\paragraph{The execution-only blind spot.}\nProve rate, the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on component necessity.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line of work documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for component necessity in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic applying \\emph{component necessity testing}, leave-one-out (LOO) ablation on solver inputs, to quantify component necessity.\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is the empirical discovery that the same LOO structure making ISR informative as a diagnostic also makes it vulnerable to gaming as a reward, a compositional Goodhart effect on structural metrics.\nISR captures component necessity rather than semantic faithfulness (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\\text{ISR}{\\approx}0$, confirming structural degeneration (\\S\\ref{sec:diagnostic}); the ${\\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\\beta{=}0.1$ seeds rise toward $\\text{ISR}{\\approx}1$ via TS gaming (Goodhart effect, \\S\\ref{sec:goodhart}); random remains low.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR (Figure~\\ref{fig:training-isr-curves}): for seed~42, $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (partially amplified by component-count inflation; mode breakdown confirms 87\\% CE at 500 steps, independent of the ISR scalar; all 3 seeds: ${\\leq}7\\%$ non-hacking by 1000 steps) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode (conclusion embedding, repetition collapse, and tautological collapse), yet all reach ${\\geq}93\\%$ structural hacking by 1000 steps.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (upper bound; 3-seed pooled, 1000 steps), consistent with GRPO-specific degradation rather than data or capacity limitations.\n\n\\paragraph{Goodhart effects.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR produces a seed-dependent compositional Goodhart effect~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.\nOn FOLIO, this instantiates \\emph{regressional} Goodhart~\\citep{manheim-goodhart-taxonomy}: $P{\\to}P$ tautologies yield $\\text{ISR}{\\geq}0.5$, so ISR rewards the shortcut; at $\\beta{=}0.1$, 3 of 5 seeds shift hacking composition from CE to TS ($p{<}10^{-15}$) without reducing prevalence ($p{=}0.182$), while 2 of 5 seeds retain ${\\sim}55\\%$ genuine reasoning; the sole apparent ISR advantage reduces to $1.06\\times$ after controlling for premise count.\nAt $\\beta{\\geq}0.2$, \\emph{extremal} Goodhart dominates ($\\text{PR}{=}66{\\pm}42\\%$ ISR, $54{\\pm}35\\%$ random at $\\beta{=}0.3$).\nOn ProofFOL, hacking yields $\\text{ISR}{=}0.0$, so ISR correctly penalizes shortcuts, associated with beneficial instability (76.8\\% vs.\\ 17.4\\% genuine under a coarser binary classifier, $p{=}0.10$).\nISR's asymmetry is the central finding: \\emph{reliable as observer, dataset-dependent as optimizer.}\n\n\\paragraph{Contributions.}\nIn this case study (Qwen3-4B, 6 reward conditions, 3--5 seeds, 2 logic types, 2 dataset families, up to 1000 steps), we contribute: (\\textbf{C1}) STA as a diagnostic framework (ISR metric, eight-mode hacking taxonomy, and cross-domain evaluation protocol) revealing structural collapse invisible to PR (${\\leq}7\\%$ non-hacking, 3 seeds, 1000 steps; 99.5\\% in seed~42), with an SFT control consistent with GRPO-specific degradation (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) a seed-dependent compositional Goodhart effect on ISR-as-reward: in 3 of 5 seeds, significant composition shift CE$\\to$TS ($p{<}10^{-15}$) without prevalence reduction ($p{=}0.182$); 2 of 5 seeds retain ${\\sim}55\\%$ genuine reasoning, showing the effect is stochastic; apparent ISR advantage collapses to $1.06\\times$ after deconfounding; shuffled-ISR control rules out distributional shape (\\S\\ref{sec:goodhart}), with cross-domain evidence: confirmed in Prolog (3/3 seeds 0\\% non-hacking) and exploratory in ProofFOL ($p{=}0.10$), showing dataset-dependent outcomes (\\S\\ref{sec:crossdomain}).\nThese are cautionary results from a Qwen3-4B case study, replicated across dataset families, relevant to any work treating a structural proxy as a training signal (generalization scope discussed in \\S\\ref{sec:limitations}).\n",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 42
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_018BGsxUWRbuRy7YWETV34vw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "9c6f72ea-3c1e-4e50-91df-4d898afee77c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb2TP2Y1ERPa76QLjfxCyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15199
      },
      "output_tokens": 25,
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

_source line 17 · 2026-05-22T03:08:39.738Z_

<details><summary>↩ Tool result · `toolu_018BGsxUWRbuRy7YWETV34vw`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).
13	
14	\paragraph{Statistical considerations.}
15	With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.
16	Pooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.
17	At $N{=}3$, seed-level tests achieve 80\% power only for very large effects ($d{\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.
18	ProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory.
19	
20	\subsection{ISR as Diagnostic}
21	\label{sec:diagnostic}
22	
23	\textbf{Collapse trajectory.}
24	Figure~\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.
25	PR rises $32\%\to93\%\to96\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\text{ISR}^*$ tells the opposite story, $0.642\to0.132\to0.003$ (214$\times$ collapse; component count inflates $2.8\times$ over the same interval, amplifying the ratio; the mode breakdown below provides count-independent evidence). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
26	By 500 steps, 87.1\% of proved samples embed the conclusion (CE), confirming structural degeneration independent of the ISR scalar.
27	An $O(1)$ binary variant testing only collective premise necessity returns $\text{ISR}{=}1.0$ for all 402 proved samples, confirming that per-component LOO testing is essential for detecting the collapse (Appendix~\ref{app:o1-ablation}).
28	
29	\textbf{Cross-seed instability.}
30	Three seeds diverge radically ($\text{PR}\,\sigma{=}47$\,pp) into conclusion embedding (s42, CE$=$87\%), repetition collapse (s43), and tautological collapse (s44, TS$=$100\%), all converging to ${\leq}7\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2
31	
32	\textbf{SFT baseline.}
33	SFT on gold formalizations reaches $92.3\%$ non-hacking ($\text{PR}{=}13\%$, 3-seed pooled; $\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$).
34	SFT serves as a pre-RL reference (not a PR-matched control; its low PR reflects minimal optimization pressure, so hacking-rate differences are confounded with PR level): the base model has zero FOL capability ($\text{PR}{=}0\%$) and SFT's $8\%$ hacking confirms these modes are absent before RL.
35	Supplementary evidence comes from the 100-step comparison (seed~42, $n{=}32$ proved): at $\text{PR}{=}32\%$, hacking already reaches $31\%$ ($9$ TS $+$ $1$ CE / $32$ proved) vs.\ SFT's $8\%$ at comparable PR, consistent with hacking as an RL optimization product rather than a mechanical consequence of prove-rate level (Appendix~\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
36	
37	\subsection{Goodhart Effects on ISR-as-Reward}
38	\label{sec:goodhart}
39	
40	We reverse ISR's role from observer to reward: $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with matched random control ($u\sim\mathcal{U}(0,1)$).
41	We define the \emph{compositional Goodhart effect} as: optimization against a structural proxy shifts the composition of failure modes without reducing their aggregate prevalence---a regressional pattern in \citeauthor{manheim-goodhart-taxonomy}'s taxonomy (the proxy correlates with quality but admits satisfying shortcuts; at $\beta{\geq}0.2$, extremal Goodhart dominates instead) where the proxy's attack surface redirects rather than eliminates gaming.
42	Here (seed-dependent; 3 of 5 seeds): (1)~hacking composition shifts from CE to TS (supplementary CMH $p{<}10^{-15}$), (2)~overall prevalence is unchanged ($p{=}0.182$); 2 of 5 seeds retain ${\sim}55\%$ non-hacking (Table~\ref{tab:hacking-taxonomy}).
43	Deconfounding collapses the apparent $3.2\times$ ISR advantage to $1.06\times$ after controlling for premise count.
44	
45	\paragraph{Multiplicative coupling.}
46	The reward $r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ couples signals; exec-only's $0\%$ non-hacking, the qualitative TS shift ($0\%{\to}71\%$), and an additive variant's PR collapse (Appendix~\ref{app:setup}) constrain this confound.
47	A shuffled-ISR control (random permutation preserving ISR's distribution but breaking the sample-level semantic link) yields $\text{PR}{=}15.3{\pm}0.6\%$ with $87.0\%$ non-hacking ($N{=}46$, 3-seed pooled), comparable to SFT, ruling out distributional shape as the Goodhart driver.
48	
49	\begin{table*}[t]
50	\centering
51	\small
52	\begin{tabular}{lcccccc}
53	\toprule
54	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
55	\midrule
56	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
57	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
58	\midrule
59	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (PG corrected)
60	ISR (3-seed) & 0.1 & 77{\scriptsize$\pm$14} & $1.06\times^\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
61	ISR (5-seed) & 0.1 & 70{\scriptsize$\pm$19} & (0.63)$^\ddagger$ & 54 & 18 & 23 \\ %% registry: plan002-additive-b01-s42--s46 (pooled)
62	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
63	Shuffled-ISR & 0.1 & 15{\scriptsize$\pm$1} & 0.559{\scriptsize$\pm$.02} & 7 & 7 & \textbf{87} \\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)
64	\midrule
65	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
66	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)
67	\bottomrule
68	\end{tabular}
69	\caption{Goodhart landscape across reward conditions. 3-seed rows: TS/CE/non-hacking percentage (N-H) pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\times$ is the premise-count-matched value relative to random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random TS driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\S\ref{sec:goodhart}), not an independent reward condition. ISR $\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\sim}55\%$ non-hacking each; Appendix~\ref{app:detailed-results}).}
70	\label{tab:goodhart-landscape}
71	\end{table*}
72	
73	\textbf{Low-dose ISR ($\beta{=}0.1$): per-seed consistent gaming.}
74	ISR reward increases TS rates in all three initial seeds (s42--44) relative to matched random: $70.6\%$ ($163/231$) vs.\ $13.7\%$ ($36/262$) pooled (supplementary CMH: $\text{OR}_{\text{CMH}}{=}2.46$, $p{=}5.6{\times}10^{-16}$; $N{=}3$ seed-level units, sample-level $p$ reflects within-seed effect; Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
75	Random TS is seed-dependent ($38.3\%$ in s43 vs.\ $0\%$ in s42/s44); ISR amplifies TS ($2/3$ seeds at $97$--$100\%$; Table~\ref{tab:fol-detailed}; 5-seed extension below).
76	TS (a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction; \S\ref{sec:taxonomy-method}) is the canonical Goodhart move: the model satisfies the LOO definition directly.
77	Total conclusion embedding ($\text{CE}+\text{TS}$) is $68$--$100\%$ across both conditions; the composition differs: CE dominates under random ($71\%$), TS under ISR. ISR converts CE into TS rather than reducing total embedding (Figure~\ref{fig:hacking-composition}).
78	Random yields higher PR ($87{\pm}8\%$ vs.\ $77{\pm}14\%$): noise disrupts convergence toward a single collapse trajectory.
79	
80	\textbf{Premise-count confound.}
81	The sole non-TS ISR seed (s42) shows raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ random ($0.131$), a premise-minimization artifact ($n{=}5.58$ vs.\ $8.46$); matched comparison gives $1.06\times$ (Appendix~\ref{app:detailed-results}). %% D051 premise-count-matched analysis
82	After reclassifying PG and TS false negatives, non-hacking rates ($6.1\%$ ISR vs.\ $9.5\%$ random) are not significant ($p{=}0.182$; Appendix~\ref{app:h8}). %% D095 FINAL Fisher test
83	The key asymmetry is compositional: ISR amplifies TS convergence ($2/3$ seeds ${\geq}97\%$), while random remains seed-dependent and CE-dominated.
84	
85	\textbf{Higher doses and temporal dynamics.}
86	ISR $\beta{=}0.1$ non-hacking is transient: seed~42 drops $17.3\%{\to}2.2\%$ by 1000 steps as TS escalates to $96.7\%$ (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
87	At higher doses ($\beta{\geq}0.2$), TS becomes universal ($0\%$ non-hacking at $\beta{=}0.2$); $\beta{=}0.3$ destabilizes both ISR ($\text{PR}{=}66{\pm}42\%$) and random ($54{\pm}35\%$), with ISR producing multi-modal failure~\citep{gao-reward-overoptimization} and random converging to CE ($91\%$; Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
88	
89	\textbf{Bimodal seed-dependence (5-seed extension).}
90	Two additional seeds (s45, s46; Appendix~\ref{app:detailed-results}) under the same ISR $\beta{=}0.1$ condition yield ${\sim}55\%$ non-hacking---qualitatively different from the 3-seed average of $6\%$.
91	This bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \S\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46
92	
93	\subsection{Cross-Domain and Cross-Dataset Evidence}
94	\label{sec:crossdomain}
95	\label{sec:crosslogic}
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
100	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
101	\label{fig:prolog-comparison}
102	\end{figure}
103	
104	\textbf{Prolog: universal Goodhart.}
105	We replicate the FOL pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}).
106	Exec-only seeds show $\text{ISR}^*{\approx}0$ via redundant ground-fact coding (2/3 seeds); ISR flags this mode as it flags FOL's conclusion embedding.
107	Under ISR-as-reward, 3/3 seeds reach 0\% non-hacking through distinct mechanisms: clean TS (s42), uppercase pseudo-Prolog bypassing text-match classifiers (s43, all 38 proved at $n_{\text{necessary}}{=}1$), and query-as-fact gaming (s44, 95/97 at $n_{\text{necessary}}{=}1$; Table~\ref{tab:prolog-detailed}).
108	Prolog's simpler semantics broadens the gaming basin, eliminating the non-hacking residual entirely.
109	
110	\textbf{ProofFOL exec-only: cross-dataset evidence for structural degeneration, with differing mode distributions.}
111	Two converged seeds ($\text{ISR}^*{<}0.07$) show ${\leq}1.4\%$ genuine; s42 exhibits 100\% TS (absent from all FOLIO exec-only seeds), showing hacking-mode repertoire is dataset-specific ($\text{ISR}^*{<}0.12$ across all seeds, far below baseline $0.31$).
112	
113	\textbf{ProofFOL ISR ($\beta{=}0.1$): beneficial instability (exploratory).}
114	ISR seeds average 76.8\% genuine versus 17.4\% exec-only ($p{=}0.10$, $N{=}3$; Table~\ref{tab:prooffol-detailed}), but ISR prove rates ($0.35$--$0.49$) remain far below exec-only (${\sim}1.0$), so this may reflect insufficient training; ProofFOL ``genuine'' excludes only TS/CE (coarser than FOLIO's eight-mode residual).
115	
116	\textbf{Mechanism.}
117	The dataset-dependent outcome follows from hacking geometry: on FOLIO, $P{\to}P$ produces 2-component formalizations where both are LOO-necessary ($\text{ISR}{\geq}0.5$, regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL, hacking embeds conclusions among many premises ($\bar{n}{=}18.2$), making most individually redundant ($\text{ISR}{\approx}0$).
118	ISR-as-reward thus inherits the dataset's hacking topology: it rewards shortcuts only when the shortcut geometry satisfies the LOO criterion.
119	
120	\subsection{Hacking Taxonomy}
121	\label{sec:taxonomy}
122	
123	\begin{figure}[t]
124	\centering
125	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
126	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}
127	\label{fig:hacking-composition}
128	\end{figure}
129	
130	\begin{table}[t]
131	\centering
132	\small
133	\resizebox{\columnwidth}{!}{%
134	\begin{tabular}{lccccc}
135	\toprule
136	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
137	\midrule
138	CE embed       & 87 & 18 & 71 & 7 & 0$^\sharp$ \\
139	TS duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
140	PG prem-subset & 6  & 5  & 8   & 0 & --- \\
141	Tautological   & --- & --- & --- & --- & s42 \\
142	Repetition     & s43 & --- & --- & --- & --- \\
143	Contradiction  & 1k & --- & --- & --- & --- \\
144	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
145	Query-as-fact  & --- & --- & --- & --- & s44 \\
146	\midrule
147	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
148	\bottomrule
149	\end{tabular}}
150	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
151	\label{tab:hacking-taxonomy}
152	\end{table}
153	
154	Three modes account for ${>}90\%$ of hacking (Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}): \textbf{CE} (conclusion embedding), \textbf{TS} (conclusion duplication, ISR-amplified), and \textbf{PG} (premise-subset gaming; audited for s42 only). \emph{Reward formulation determines composition but not prevalence}: all GRPO conditions show ${\geq}80\%$ hacking; only SFT achieves $92.3\%$ non-hacking.
155	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "d18c3cbd-ef09-41d3-91f5-6f0420b165b5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse; component count inflates $2.8\\times$ over the same interval, amplifying the ratio; the mode breakdown below provides count-independent evidence). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (CE), confirming structural degeneration independent of the ISR scalar.\nAn $O(1)$ binary variant testing only collective premise necessity returns $\\text{ISR}{=}1.0$ for all 402 proved samples, confirming that per-component LOO testing is essential for detecting the collapse (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge radically ($\\text{PR}\\,\\sigma{=}47$\\,pp) into conclusion embedding (s42, CE$=$87\\%), repetition collapse (s43), and tautological collapse (s44, TS$=$100\\%), all converging to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $92.3\\%$ non-hacking ($\\text{PR}{=}13\\%$, 3-seed pooled; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$).\nSFT serves as a pre-RL reference (not a PR-matched control; its low PR reflects minimal optimization pressure, so hacking-rate differences are confounded with PR level): the base model has zero FOL capability ($\\text{PR}{=}0\\%$) and SFT's $8\\%$ hacking confirms these modes are absent before RL.\nSupplementary evidence comes from the 100-step comparison (seed~42, $n{=}32$ proved): at $\\text{PR}{=}32\\%$, hacking already reaches $31\\%$ ($9$ TS $+$ $1$ CE / $32$ proved) vs.\\ SFT's $8\\%$ at comparable PR, consistent with hacking as an RL optimization product rather than a mechanical consequence of prove-rate level (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nWe define the \\emph{compositional Goodhart effect} as: optimization against a structural proxy shifts the composition of failure modes without reducing their aggregate prevalence---a regressional pattern in \\citeauthor{manheim-goodhart-taxonomy}'s taxonomy (the proxy correlates with quality but admits satisfying shortcuts; at $\\beta{\\geq}0.2$, extremal Goodhart dominates instead) where the proxy's attack surface redirects rather than eliminates gaming.\nHere (seed-dependent; 3 of 5 seeds): (1)~hacking composition shifts from CE to TS (supplementary CMH $p{<}10^{-15}$), (2)~overall prevalence is unchanged ($p{=}0.182$); 2 of 5 seeds retain ${\\sim}55\\%$ non-hacking (Table~\\ref{tab:hacking-taxonomy}).\nDeconfounding collapses the apparent $3.2\\times$ ISR advantage to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe reward $r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ couples signals; exec-only's $0\\%$ non-hacking, the qualitative TS shift ($0\\%{\\to}71\\%$), and an additive variant's PR collapse (Appendix~\\ref{app:setup}) constrain this confound.\nA shuffled-ISR control (random permutation preserving ISR's distribution but breaking the sample-level semantic link) yields $\\text{PR}{=}15.3{\\pm}0.6\\%$ with $87.0\\%$ non-hacking ($N{=}46$, 3-seed pooled), comparable to SFT, ruling out distributional shape as the Goodhart driver.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows: TS/CE/non-hacking percentage (N-H) pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): per-seed consistent gaming.}\nISR reward increases TS rates in all three initial seeds (s42--44) relative to matched random: $70.6\\%$ ($163/231$) vs.\\ $13.7\\%$ ($36/262$) pooled (supplementary CMH: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{=}5.6{\\times}10^{-16}$; $N{=}3$ seed-level units, sample-level $p$ reflects within-seed effect; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nRandom TS is seed-dependent ($38.3\\%$ in s43 vs.\\ $0\\%$ in s42/s44); ISR amplifies TS ($2/3$ seeds at $97$--$100\\%$; Table~\\ref{tab:fol-detailed}; 5-seed extension below).\nTS (a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction; \\S\\ref{sec:taxonomy-method}) is the canonical Goodhart move: the model satisfies the LOO definition directly.\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) is $68$--$100\\%$ across both conditions; the composition differs: CE dominates under random ($71\\%$), TS under ISR. ISR converts CE into TS rather than reducing total embedding (Figure~\\ref{fig:hacking-composition}).\nRandom yields higher PR ($87{\\pm}8\\%$ vs.\\ $77{\\pm}14\\%$): noise disrupts convergence toward a single collapse trajectory.\n\n\\textbf{Premise-count confound.}\nThe sole non-TS ISR seed (s42) shows raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ random ($0.131$), a premise-minimization artifact ($n{=}5.58$ vs.\\ $8.46$); matched comparison gives $1.06\\times$ (Appendix~\\ref{app:detailed-results}). %% D051 premise-count-matched analysis\nAfter reclassifying PG and TS false negatives, non-hacking rates ($6.1\\%$ ISR vs.\\ $9.5\\%$ random) are not significant ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D095 FINAL Fisher test\nThe key asymmetry is compositional: ISR amplifies TS convergence ($2/3$ seeds ${\\geq}97\\%$), while random remains seed-dependent and CE-dominated.\n\n\\textbf{Higher doses and temporal dynamics.}\nISR $\\beta{=}0.1$ non-hacking is transient: seed~42 drops $17.3\\%{\\to}2.2\\%$ by 1000 steps as TS escalates to $96.7\\%$ (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nAt higher doses ($\\beta{\\geq}0.2$), TS becomes universal ($0\\%$ non-hacking at $\\beta{=}0.2$); $\\beta{=}0.3$ destabilizes both ISR ($\\text{PR}{=}66{\\pm}42\\%$) and random ($54{\\pm}35\\%$), with ISR producing multi-modal failure~\\citep{gao-reward-overoptimization} and random converging to CE ($91\\%$; Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking---qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nWe replicate the FOL pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}).\nExec-only seeds show $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding (2/3 seeds); ISR flags this mode as it flags FOL's conclusion embedding.\nUnder ISR-as-reward, 3/3 seeds reach 0\\% non-hacking through distinct mechanisms: clean TS (s42), uppercase pseudo-Prolog bypassing text-match classifiers (s43, all 38 proved at $n_{\\text{necessary}}{=}1$), and query-as-fact gaming (s44, 95/97 at $n_{\\text{necessary}}{=}1$; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the non-hacking residual entirely.\n\n\\textbf{ProofFOL exec-only: cross-dataset evidence for structural degeneration, with differing mode distributions.}\nTwo converged seeds ($\\text{ISR}^*{<}0.07$) show ${\\leq}1.4\\%$ genuine; s42 exhibits 100\\% TS (absent from all FOLIO exec-only seeds), showing hacking-mode repertoire is dataset-specific ($\\text{ISR}^*{<}0.12$ across all seeds, far below baseline $0.31$).\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): beneficial instability (exploratory).}\nISR seeds average 76.8\\% genuine versus 17.4\\% exec-only ($p{=}0.10$, $N{=}3$; Table~\\ref{tab:prooffol-detailed}), but ISR prove rates ($0.35$--$0.49$) remain far below exec-only (${\\sim}1.0$), so this may reflect insufficient training; ProofFOL ``genuine'' excludes only TS/CE (coarser than FOLIO's eight-mode residual).\n\n\\textbf{Mechanism.}\nThe dataset-dependent outcome follows from hacking geometry: on FOLIO, $P{\\to}P$ produces 2-component formalizations where both are LOO-necessary ($\\text{ISR}{\\geq}0.5$, regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, hacking embeds conclusions among many premises ($\\bar{n}{=}18.2$), making most individually redundant ($\\text{ISR}{\\approx}0$).\nISR-as-reward thus inherits the dataset's hacking topology: it rewards shortcuts only when the shortcut geometry satisfies the LOO criterion.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for ${>}90\\%$ of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): \\textbf{CE} (conclusion embedding), \\textbf{TS} (conclusion duplication, ISR-amplified), and \\textbf{PG} (premise-subset gaming; audited for s42 only). \\emph{Reward formulation determines composition but not prevalence}: all GRPO conditions show ${\\geq}80\\%$ hacking; only SFT achieves $92.3\\%$ non-hacking.\n",
      "numLines": 155,
      "startLine": 1,
      "totalLines": 155
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the files read. Let me also search for the two references (DeepSeek-Prover-V2 and PRIME) to get accurate bibliographic information.

Let me now plan all four modifications:

1. **W3 Reproducibility statement**: Add to `limitations.tex` at the end, since conclusion.tex ends with a practical recommendation. Limitations is the better place since it's the standard location for reproducibility statements.

2. **Missing references**: Need to web search for DeepSeek-Prover-V2 and PRIME, add to references.bib, cite in related_work.tex.


3. **Introduction 99.5% fix**: I'm locating the exact text on line 40 that mentions the 99.5% figure in seed 42 to understand the context and make the necessary correction. I'm checking the exact LaTeX formatting for the metrics—specifically whether the 99.5% value needs math mode delimiters and how to restructure the phrasing to clarify that ISR degrades significantly in seed 42 while maintaining the technical precision of the original numbers. Looking at the Table 2 caption, I can see "1k" appears as a cell value in the Contradiction row under the Exec column. The user wants me to clarify what "1k" means—it likely refers to observations at 1000 steps—so I should add an explanation to the caption.

Now I need to verify this is indeed Table 2 and then search for the references to make the necessary updates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "b233003b-c01b-4766-b906-95b5fa162165",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012izb1CX8kF8K8eQHhsW4E9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19568,
      "cache_read_input_tokens": 27040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19568
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

_source line 19_

I'll search for both references and start making edits in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "bf9f5080-4e8d-4e5c-8795-e5ce1bde3868",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012izb1CX8kF8K8eQHhsW4E9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19568,
      "cache_read_input_tokens": 27040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19568
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

_source line 20_

<details open><summary>🔧 Tool call — Agent · `toolu_014iJ6JuMnCxaqQTHur7h1wd`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search for DeepSeek-Prover-V2 paper",
  "prompt": "Search the web for \"DeepSeek-Prover-V2 arXiv 2501.14333\" to find the exact title and author list. I need: full title, complete author list, arXiv ID, and year. Report concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "1f340d04-db9a-4de2-8e59-1ae1d2951c96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012izb1CX8kF8K8eQHhsW4E9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19568,
      "cache_read_input_tokens": 27040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19568
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

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a62211cc337f8589c",
  "tool_use_id": "toolu_014iJ6JuMnCxaqQTHur7h1wd",
  "description": "Search for DeepSeek-Prover-V2 paper",
  "task_type": "local_agent",
  "prompt": "Search the web for \"DeepSeek-Prover-V2 arXiv 2501.14333\" to find the exact title and author list. I need: full title, complete author list, arXiv ID, and year. Report concisely.",
  "uuid": "099e0820-5bba-475b-867d-26dca4107adc",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90"
}
```

---

## Round 1

3 recorded events

### User

_source line 22 · 2026-05-22T03:09:07.385Z_

Search the web for "DeepSeek-Prover-V2 arXiv 2501.14333" to find the exact title and author list. I need: full title, complete author list, arXiv ID, and year. Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014iJ6JuMnCxaqQTHur7h1wd",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "7b8599ef-809c-43ae-a372-150a2ab0e61f"
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Agent · `toolu_01G2yKTuE2jXQ9nWu7MvMs3A`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search for PRIME paper",
  "prompt": "Search the web for \"PRIME process reward implicit\" OR \"PRIME Cui 2025 arXiv\" to find the paper by Cui et al. about PRIME (process reward / implicit reward). I need: exact title, complete author list, arXiv ID, and year. Report concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "a4b66a9b-4160-4580-a3a8-ae01c70e8a36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012izb1CX8kF8K8eQHhsW4E9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19568,
      "cache_read_input_tokens": 27040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19568
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

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a1ea263c60d7f443a",
  "tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "description": "Search for PRIME paper",
  "task_type": "local_agent",
  "prompt": "Search the web for \"PRIME process reward implicit\" OR \"PRIME Cui 2025 arXiv\" to find the paper by Cui et al. about PRIME (process reward / implicit reward). I need: exact title, complete author list, arXiv ID, and year. Report concisely.",
  "uuid": "fe4cf0cd-303d-46b7-9a5e-645a37c0881e",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90"
}
```

---

## Round 2

34 recorded events

### User

_source line 25 · 2026-05-22T03:09:08.623Z_

Search the web for "PRIME process reward implicit" OR "PRIME Cui 2025 arXiv" to find the paper by Cui et al. about PRIME (process reward / implicit reward). I need: exact title, complete author list, arXiv ID, and year. Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "93a41da4-fd96-4062-8f33-98095d3afcb5"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a62211cc337f8589c",
  "tool_use_id": "toolu_014iJ6JuMnCxaqQTHur7h1wd",
  "description": "Searching for DeepSeek-Prover-V2 arXiv 2501.14333",
  "usage": {
    "total_tokens": 15460,
    "tool_uses": 1,
    "duration_ms": 1406
  },
  "last_tool_name": "WebSearch",
  "uuid": "eb74433f-7eee-4162-8ff5-34103287d918",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P15qNiqi2DxvutvqREs5h7`</summary>

```json
{
  "query": "DeepSeek-Prover-V2 arXiv 2501.14333"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_014iJ6JuMnCxaqQTHur7h1wd",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "33d8f950-34a6-43da-b69a-6487aa771309",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DUEYMTzu6cY7yEEue84StF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15449,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1ea263c60d7f443a",
  "tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "description": "Searching for PRIME process reward implicit Cui 2025 arXiv",
  "usage": {
    "total_tokens": 15469,
    "tool_uses": 1,
    "duration_ms": 1364
  },
  "last_tool_name": "WebSearch",
  "uuid": "5d588437-0967-4ea4-9e76-22fe185b42bd",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014zFXN77AX6CN49LnqLmw2G`</summary>

```json
{
  "query": "PRIME process reward implicit Cui 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "b0c5f7da-ab95-4231-8837-997c99be6555",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HELzZUvdT6PLn8Zc7bYkvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 14966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 492,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1ea263c60d7f443a",
  "tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "description": "Searching for PRIME Cui 2025 process reward arXiv",
  "usage": {
    "total_tokens": 15473,
    "tool_uses": 2,
    "duration_ms": 1399
  },
  "last_tool_name": "WebSearch",
  "uuid": "f024be96-be54-406b-b962-6eedf407be24",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CwF9ybzyVhPkLmaGErX34Y`</summary>

```json
{
  "query": "PRIME Cui 2025 process reward arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "6cfd4ff0-805a-42c5-a61b-7fb41af05391",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HELzZUvdT6PLn8Zc7bYkvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 14966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 492,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 32 · 2026-05-22T03:09:15.990Z_

<details><summary>↩ Tool result · `toolu_01P15qNiqi2DxvutvqREs5h7`</summary>

```text
Web search results for query: "DeepSeek-Prover-V2 arXiv 2501.14333"

Links: [{"title":"DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition","url":"https://arxiv.org/html/2504.21801v1"},{"title":"[2504.21801] DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition","url":"https://arxiv.org/abs/2504.21801"},{"title":"GitHub - deepseek-ai/DeepSeek-Prover-V2 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Prover-V2"},{"title":"DeepSeek Prover V2 download | SourceForge.net","url":"https://sourceforge.net/projects/deepseek-prover-v2.mirror/"},{"title":"DeepSeek-Prover-V2: Advancing Formal Mathematical ...","url":"https://arxiv.org/pdf/2504.21801"},{"title":"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search","url":"https://arxiv.org/html/2408.08152v1"},{"title":"[PDF] DeepSeek-Prover: Advancing Theorem Proving in LLMs through Large-Scale Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepSeek-Prover:-Advancing-Theorem-Proving-in-LLMs-Xin-Guo/3648515cc35b517cdf60331cc4870e24616f9939"}]

Based on the search results, DeepSeek-Prover-V2 is an open-source large language model designed for formal theorem proving in Lean 4, with initialization data collected through a recursive theorem proving pipeline powered by DeepSeek-V3.

**Key Features:**

The cold-start training procedure begins by prompting DeepSeek-V3 to decompose complex problems into a series of subgoals. The proofs of resolved subgoals are synthesized into a chain-of-thought process, combined with DeepSeek-V3's step-by-step reasoning, to create an initial cold start for reinforcement learning.

**Performance:**

The resulting model, DeepSeek-Prover-V2-671B, achieves state-of-the-art performance in neural theorem proving, reaching 88.9% pass ratio on the MiniF2F-test and solving 49 out of 658 problems from PutnamBench. On 15 selected AIME problems, the model successfully solves 6 of them. In comparison, DeepSeek-V3 solves 8 of these problems using majority voting, highlighting that the gap between formal and informal mathematical reasoning in large language models is substantially narrowing.

Note: The search results show the paper is indexed as arXiv 2504.21801, not 2501.14333. The 2501.14333 number appears to be associated with the original DeepSeek-Prover paper from an earlier version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014iJ6JuMnCxaqQTHur7h1wd",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "27957e03-4622-48d0-a5d9-ed7cad044b17"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-22T03:09:16.168Z_

<details><summary>↩ Tool result · `toolu_014zFXN77AX6CN49LnqLmw2G`</summary>

```text
Web search results for query: "PRIME process reward implicit Cui 2025 arXiv"

Links: [{"title":"[PDF] Process Reinforcement through Implicit Rewards | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Process-Reinforcement-through-Implicit-Rewards-Cui-Yuan/e23379a9752f57732d311f7a97af2c69af6fae7b"},{"title":"[2502.01456] Process Reinforcement through Implicit Rewards","url":"https://arxiv.org/abs/2502.01456"},{"title":"[2502.01456v1] Process Reinforcement through Implicit Rewards","url":"https://arxiv.org/abs/2502.01456v1"},{"title":"GitHub - PRIME-RL/PRIME: Scalable RL solution for advanced reasoning of language models · GitHub","url":"https://github.com/PRIME-RL/PRIME"},{"title":"Process Reinforcement through Implicit Rewards","url":"https://arxiv.org/html/2502.01456v2"},{"title":"Paper page - Process Reinforcement through Implicit Rewards","url":"https://huggingface.co/papers/2502.01456"},{"title":"Agentic Reinforcement Learning with Implicit Step Rewards","url":"https://arxiv.org/html/2509.19199v3"},{"title":"Preprint PROCESS REINFORCEMENT THROUGH IMPLICIT RE- WARDS","url":"https://arxiv.org/pdf/2502.01456"}]

I found the research paper you're looking for. Here's what I found about the PRIME paper by Cui et al. from 2025:

PRIME (Process Reinforcement through IMplicit rEwards) enables online PRM updates using only policy rollouts and outcome labels through implicit process rewards, combining well with various advantage functions and forgoing the dedicated reward model training phase that existing approaches require.

The key insight of PRIME is to apply implicit process rewards, which are derivable from the Implicit PRM that is trained with only outcome labels, and this property enables updating the PRMs online to avoid reward hacking.

The paper was released on arXiv on February 4, 2025, with the arXiv identifier being 2502.01456. The paper introduces PRIME and Eurus-2, trained from a base model to surpass Qwen2.5-Math-Instruct using only 1/10 of the data.

The open-source implementation is available on GitHub, and you can access the full paper at arxiv.org/abs/2502.01456.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "3e4a8fb3-dcc6-4323-8629-bb643c4204ba"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a62211cc337f8589c",
  "tool_use_id": "toolu_014iJ6JuMnCxaqQTHur7h1wd",
  "status": "completed",
  "output_file": "",
  "summary": "Search for DeepSeek-Prover-V2 paper",
  "usage": {
    "total_tokens": 17206,
    "tool_uses": 1,
    "duration_ms": 12627
  },
  "uuid": "189a75d6-3039-425a-8dca-10d65b7b71b2",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90"
}
```

---

### Tool result

_source line 35 · 2026-05-22T03:09:20.014Z_

<details><summary>↩ Tool result · `toolu_014iJ6JuMnCxaqQTHur7h1wd`</summary>

```text
I found the information about the DeepSeek-Prover paper, but there's an important note: the arXiv ID you mentioned (2501.14333) does not match the search results. The current DeepSeek-Prover-V2 paper is indexed as **arXiv 2504.21801**, which is from 2025 (April 2025 based on the ID).

Here's what I found:

**Full Title:** DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition

**arXiv ID:** 2504.21801

**Year:** 2025

**Note on Author List:** The search results provide the title and abstract but don't display the complete author list in the summaries. To get the full author list, you would need to visit the arXiv page directly at https://arxiv.org/abs/2504.21801.

The arXiv ID 2501.14333 you provided may refer to a different paper or an earlier version. If you specifically need information about a paper with that ID, please let me know and I can search for it separately.

Sources:
- [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/abs/2504.21801)
- [DeepSeek-Prover-V2 GitHub Repository](https://github.com/deepseek-ai/DeepSeek-Prover-V2)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "ca51eede-212e-4370-9394-be12826bf04b",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search the web for \"DeepSeek-Prover-V2 arXiv 2501.14333\" to find the exact title and author list. I need: full title, complete author list, arXiv ID, and year. Report concisely.",
    "agentId": "a62211cc337f8589c",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "I found the information about the DeepSeek-Prover paper, but there's an important note: the arXiv ID you mentioned (2501.14333) does not match the search results. The current DeepSeek-Prover-V2 paper is indexed as **arXiv 2504.21801**, which is from 2025 (April 2025 based on the ID).\n\nHere's what I found:\n\n**Full Title:** DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition\n\n**arXiv ID:** 2504.21801\n\n**Year:** 2025\n\n**Note on Author List:** The search results provide the title and abstract but don't display the complete author list in the summaries. To get the full author list, you would need to visit the arXiv page directly at https://arxiv.org/abs/2504.21801.\n\nThe arXiv ID 2501.14333 you provided may refer to a different paper or an earlier version. If you specifically need information about a paper with that ID, please let me know and I can search for it separately.\n\nSources:\n- [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/abs/2504.21801)\n- [DeepSeek-Prover-V2 GitHub Repository](https://github.com/deepseek-ai/DeepSeek-Prover-V2)"
      }
    ],
    "totalDurationMs": 12629,
    "totalTokens": 17563,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1743,
      "cache_read_input_tokens": 15449,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1743
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 366,
          "cache_read_input_tokens": 15449,
          "cache_creation_input_tokens": 1743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1743,
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
      "otherToolCount": 1
    }
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T03:09:21.554Z_

<details><summary>↩ Tool result · `toolu_01CwF9ybzyVhPkLmaGErX34Y`</summary>

```text
Web search results for query: "PRIME Cui 2025 process reward arXiv"

Links: [{"title":"GitHub - PRIME-RL/PRIME: Scalable RL solution for advanced reasoning of language models · GitHub","url":"https://github.com/PRIME-RL/PRIME"},{"title":"PRIME-RL/Eurus-2-7B-PRIME-Zero · Hugging Face","url":"https://huggingface.co/PRIME-RL/Eurus-2-7B-PRIME-Zero"},{"title":"[2502.01456] Process Reinforcement through Implicit Rewards","url":"https://arxiv.org/abs/2502.01456"},{"title":"[2502.01456v1] Process Reinforcement through Implicit Rewards","url":"https://arxiv.org/abs/2502.01456v1"},{"title":"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization","url":"https://arxiv.org/html/2508.00222v3"},{"title":"Process Reinforcement through Implicit Rewards","url":"https://arxiv.org/html/2502.01456v1"},{"title":"Agentic Reinforcement Learning with Implicit Step Rewards","url":"https://arxiv.org/html/2509.19199v3"},{"title":"Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning","url":"https://arxiv.org/html/2510.10649v1"},{"title":"Preprint PROCESS REINFORCEMENT THROUGH IMPLICIT RE- WARDS","url":"https://arxiv.org/pdf/2502.01456"}]

Based on the search results, I found information about the PRIME paper by Cui et al. 2025:

PRIME (Process Reinforcement through IMplicit REwards) is an open-source solution for online RL with process rewards, designed to advance reasoning abilities of language models beyond imitation or distillation.

The paper is titled "Process Reinforcement through Implicit Rewards" and addresses dense process rewards as a more effective alternative to sparse outcome-level rewards in inference-time scaling of large language models.

The key challenge PRIME addresses is the difficulty of training process reward models (PRMs) online, where collecting high-quality process labels is prohibitively expensive. PRIME combines well with various advantage functions and forgoes the dedicated reward model training phase that existing approaches require, substantially reducing the development overhead.

Starting from Qwen2.5-Math-7B-Base, PRIME achieves a 15.1% average improvement across several key reasoning benchmarks over the SFT model. The resulting model, Eurus-2-7B-PRIME, surpasses Qwen2.5-Math-7B-Instruct on seven reasoning benchmarks with 10% of its training data.

The paper was published on arXiv with ID 2502.01456 in February 2025, and the associated code and models are available on GitHub and Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "321edd8c-03ad-4c29-ad35-84bf9cea9a61"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1ea263c60d7f443a",
  "tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "description": "Fetching https://arxiv.org/abs/2502.01456",
  "usage": {
    "total_tokens": 17874,
    "tool_uses": 3,
    "duration_ms": 14919
  },
  "last_tool_name": "WebFetch",
  "uuid": "69d65aa1-87ce-424c-b208-97969c8df41c",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XXjYVQZTrtCjBZ3fPyRVew`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.01456",
  "prompt": "Extract the exact title, complete author list, and arXiv ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "6aa48c6f-7ed6-44e2-8964-ba68a6b57a8f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GJK1KeGm8E2Lvcuk1ezGAL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2395,
      "cache_read_input_tokens": 15458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2395,
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

_source line 39 · 2026-05-22T03:09:27.323Z_

<details><summary>↩ Tool result · `toolu_01XXjYVQZTrtCjBZ3fPyRVew`</summary>

```text
# Paper Information

**Title:** "Process Reinforcement through Implicit Rewards"

**arXiv ID:** 2502.01456

**Complete Author List:**
Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Yuchen Zhang, Jiacheng Chen, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, Jiarui Yuan, Huayu Chen, Kaiyan Zhang, Xingtai Lv, Shuo Wang, Yuan Yao, Xu Han, Hao Peng, Yu Cheng, Zhiyuan Liu, Maosong Sun, Bowen Zhou, Ning Ding
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "37533f62-261b-4440-9582-cbbdecd2d2a0"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a1ea263c60d7f443a",
  "tool_use_id": "toolu_01G2yKTuE2jXQ9nWu7MvMs3A",
  "status": "completed",
  "output_file": "",
  "summary": "Search for PRIME paper",
  "usage": {
    "total_tokens": 18180,
    "tool_uses": 3,
    "duration_ms": 21352
  },
  "uuid": "77078458-e797-4298-983f-baed01c64517",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90"
}
```

---

### Tool result

_source line 41 · 2026-05-22T03:09:29.976Z_

<details><summary>↩ Tool result · `toolu_01G2yKTuE2jXQ9nWu7MvMs3A`</summary>

```text
**Paper Found:**

**Title:** Process Reinforcement through Implicit Rewards

**Authors:** Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Yuchen Zhang, Jiacheng Chen, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, Jiarui Yuan, Huayu Chen, Kaiyan Zhang, Xingtai Lv, Shuo Wang, Yuan Yao, Xu Han, Hao Peng, Yu Cheng, Zhiyuan Liu, Maosong Sun, Bowen Zhou, Ning Ding

**arXiv ID:** 2502.01456

**Year:** 2025

Sources:
- [arXiv: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)
- [Semantic Scholar](https://www.semanticscholar.org/paper/Process-Reinforcement-through-Implicit-Rewards-Cui-Yuan/e23379a9752f57732d311f7a97af2c69af6fae7b)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "a637d19c-7ccb-46e3-bdfa-ba3ba4963ffb",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search the web for \"PRIME process reward implicit\" OR \"PRIME Cui 2025 arXiv\" to find the paper by Cui et al. about PRIME (process reward / implicit reward). I need: exact title, complete author list, arXiv ID, and year. Report concisely.",
    "agentId": "a1ea263c60d7f443a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "**Paper Found:**\n\n**Title:** Process Reinforcement through Implicit Rewards\n\n**Authors:** Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Yuchen Zhang, Jiacheng Chen, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, Jiarui Yuan, Huayu Chen, Kaiyan Zhang, Xingtai Lv, Shuo Wang, Yuan Yao, Xu Han, Hao Peng, Yu Cheng, Zhiyuan Liu, Maosong Sun, Bowen Zhou, Ning Ding\n\n**arXiv ID:** 2502.01456\n\n**Year:** 2025\n\nSources:\n- [arXiv: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)\n- [Semantic Scholar](https://www.semanticscholar.org/paper/Process-Reinforcement-through-Implicit-Rewards-Cui-Yuan/e23379a9752f57732d311f7a97af2c69af6fae7b)"
      }
    ],
    "totalDurationMs": 21353,
    "totalTokens": 18449,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 306,
      "cache_read_input_tokens": 17853,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 306
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 284,
          "cache_read_input_tokens": 17853,
          "cache_creation_input_tokens": 306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 306,
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
      "otherToolCount": 3
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the reference info. Let me also verify the DeepSeek-Prover-V2 arXiv ID. The user said 2501.14333 but the search found 2504.21801. Let me do a quick web search to confirm. Actually, let me just use the correct one found by the search (2504.21801). The user's ID might have been wrong.

Now let me also check for DeepSeek-Prover-V2's author list since the search didn't return it. Given it's by DeepSeek AI, I can use `{DeepSeek AI}` as the author, consistent with how deepseek-r1 is cited in the existing bib.


Now I'll make the four modifications: adding the reproducibility statement to limitations.tex, updating the bibliography and citations in related_work.tex, fixing the 99.5% reference in the introduction, and updating Table 2's caption. Looking at the existing bibliography entries, I notice deepseek-r1 uses `{DeepSeek-AI}` while deepseek-prover-v15 uses `{DeepSeek AI}`, so I'll go with `{DeepSeek-AI}` for consistency with the more recent entry.

The user mentioned arXiv 2501.14333, but my search found 2504.21801 from April 2025—these might be different versions. I'll proceed with the ID from the search results since that's what I confirmed, though there's a discrepancy worth noting. Let me start making these edits now. I need to complete the PRIME bibliography entry first, then move through the modifications in order—starting with the limitations section, fixing the introduction line, updating the table caption, and finally handling the bibliography and citation updates in the related work section. I'm checking what the 99.5% degradation in seed 42 refers to—it's specifically about ISR performance, so I need to clarify that in the introduction. For the Table 2 caption, I should add an explanation about what the "1k" checkpoint means in the Contradiction row, since that's when the contradiction was first observed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "9831e7a4-4150-4f6b-b415-07a3ee413559",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdDybpRZFMa2KsMd2xmh6u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 46608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2394
      },
      "output_tokens": 22,
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

_source line 43_

DeepSeek-Prover-V2 arXiv ID is 2504.21801 (not 2501.14333 as suggested). PRIME is 2502.01456. Now making all four edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "40b38524-7b52-4746-9ddf-06375f6eccd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdDybpRZFMa2KsMd2xmh6u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 46608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2394
      },
      "output_tokens": 22,
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

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01LHdzoUMQkBLeWa35WJNBBY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex",
  "old_string": "Intermediate checkpoints (100--900 steps) were not retained; trajectory analyses rely on saved evaluation outputs at recorded steps.",
  "new_string": "Intermediate checkpoints (100--900 steps) were not retained; trajectory analyses rely on saved evaluation outputs at recorded steps.\nCode, evaluation scripts, the ProofFOL dataset, and final model checkpoints will be released upon acceptance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "7fba02a3-a9ad-460e-8e26-651a6ff101d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdDybpRZFMa2KsMd2xmh6u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 46608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2394
      },
      "output_tokens": 22,
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

_source line 45 · 2026-05-22T03:10:01.735Z_

<details><summary>↩ Tool result · `toolu_01LHdzoUMQkBLeWa35WJNBBY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "82f7e792-17a8-45a1-bac6-a63ea93f7834",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex",
    "oldString": "Intermediate checkpoints (100--900 steps) were not retained; trajectory analyses rely on saved evaluation outputs at recorded steps.",
    "newString": "Intermediate checkpoints (100--900 steps) were not retained; trajectory analyses rely on saved evaluation outputs at recorded steps.\nCode, evaluation scripts, the ProofFOL dataset, and final model checkpoints will be released upon acceptance.",
    "originalFile": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B); RLVR gains from random or incorrect rewards have been shown to be Qwen-specific~\\citep{spurious-rewards}, so the structural degeneration patterns we document may not transfer identically to other model families.\nCross-dataset evidence (ProofFOL, Prolog) supports generality, but LLaMA-3.2-3B achieves only $\\text{PR}{\\approx}15\\%$ after SFT warmstart with GRPO unable to amplify beyond this baseline (Appendix~\\ref{app:llama-coldstart}), establishing a capability threshold below which STA's degeneration analysis is uninformative (the model cannot hack what it cannot prove).\nThree seeds demonstrate qualitative divergence but limit statistical power ($N{=}3$ independent replications); all pooled statistics treat within-seed samples as independent, and the ProofFOL genuine-rate advantage ($p{=}0.10$) is an observation, not a confirmed effect.\nAt our scale (500 training / 100 evaluation examples), non-hacking rates of ${\\sim}5\\%$ correspond to ${\\sim}5$ samples, limiting mode-level precision.\nISR quantifies syntactic component necessity, not semantic faithfulness ($\\rho{=}{-}0.049$ with NLI accuracy; Appendix~\\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.\nIntermediate checkpoints (100--900 steps) were not retained; trajectory analyses rely on saved evaluation outputs at recorded steps.\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 3,
        "newStart": 7,
        "newLines": 4,
        "lines": [
          " At our scale (500 training / 100 evaluation examples), non-hacking rates of ${\\sim}5\\%$ correspond to ${\\sim}5$ samples, limiting mode-level precision.",
          " ISR quantifies syntactic component necessity, not semantic faithfulness ($\\rho{=}{-}0.049$ with NLI accuracy; Appendix~\\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.",
          " Intermediate checkpoints (100--900 steps) were not retained; trajectory analyses rely on saved evaluation outputs at recorded steps.",
          "+Code, evaluation scripts, the ProofFOL dataset, and final model checkpoints will be released upon acceptance."
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

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_01FeH19WipTx5ZoyL7jMwNRw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
  "old_string": "${\\leq}7\\%$ non-hacking, 3 seeds, 1000 steps; 99.5\\% in seed~42)",
  "new_string": "${\\leq}7\\%$ non-hacking across 3 seeds at 1000 steps; ISR degrades 99.5\\% in seed~42)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "44d77d06-0c23-4aec-8765-5d16fe0d919b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdDybpRZFMa2KsMd2xmh6u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 46608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2394
      },
      "output_tokens": 22,
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

_source line 47 · 2026-05-22T03:10:02.972Z_

<details><summary>↩ Tool result · `toolu_01FeH19WipTx5ZoyL7jMwNRw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "c1b7ef43-972b-44be-8a7c-c25bba27e7b7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex",
    "oldString": "${\\leq}7\\%$ non-hacking, 3 seeds, 1000 steps; 99.5\\% in seed~42)",
    "newString": "${\\leq}7\\%$ non-hacking across 3 seeds at 1000 steps; ISR degrades 99.5\\% in seed~42)",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on first-order logic problems, yet 87\\% of its proved outputs embed the conclusion verbatim among the premises.\nThe solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.\nThis structural shortcut (an instance of shortcut learning~\\citep{geirhos2020shortcut} in the neurosymbolic setting) is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.\n\n\\paragraph{The execution-only blind spot.}\nProve rate, the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on component necessity.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line of work documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for component necessity in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic applying \\emph{component necessity testing}, leave-one-out (LOO) ablation on solver inputs, to quantify component necessity.\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution is the empirical discovery that the same LOO structure making ISR informative as a diagnostic also makes it vulnerable to gaming as a reward, a compositional Goodhart effect on structural metrics.\nISR captures component necessity rather than semantic faithfulness (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{ISR training trajectories across reward conditions (proved samples only, rolling $w{=}20$). Exec-only collapses to $\\text{ISR}{\\approx}0$, confirming structural degeneration (\\S\\ref{sec:diagnostic}); the ${\\sim}0.5$ plateau is an $n{=}2$ artifact. ISR $\\beta{=}0.1$ seeds rise toward $\\text{ISR}{\\approx}1$ via TS gaming (Goodhart effect, \\S\\ref{sec:goodhart}); random remains low.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR (Figure~\\ref{fig:training-isr-curves}): for seed~42, $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (partially amplified by component-count inflation; mode breakdown confirms 87\\% CE at 500 steps, independent of the ISR scalar; all 3 seeds: ${\\leq}7\\%$ non-hacking by 1000 steps) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode (conclusion embedding, repetition collapse, and tautological collapse), yet all reach ${\\geq}93\\%$ structural hacking by 1000 steps.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (upper bound; 3-seed pooled, 1000 steps), consistent with GRPO-specific degradation rather than data or capacity limitations.\n\n\\paragraph{Goodhart effects.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR produces a seed-dependent compositional Goodhart effect~\\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.\nOn FOLIO, this instantiates \\emph{regressional} Goodhart~\\citep{manheim-goodhart-taxonomy}: $P{\\to}P$ tautologies yield $\\text{ISR}{\\geq}0.5$, so ISR rewards the shortcut; at $\\beta{=}0.1$, 3 of 5 seeds shift hacking composition from CE to TS ($p{<}10^{-15}$) without reducing prevalence ($p{=}0.182$), while 2 of 5 seeds retain ${\\sim}55\\%$ genuine reasoning; the sole apparent ISR advantage reduces to $1.06\\times$ after controlling for premise count.\nAt $\\beta{\\geq}0.2$, \\emph{extremal} Goodhart dominates ($\\text{PR}{=}66{\\pm}42\\%$ ISR, $54{\\pm}35\\%$ random at $\\beta{=}0.3$).\nOn ProofFOL, hacking yields $\\text{ISR}{=}0.0$, so ISR correctly penalizes shortcuts, associated with beneficial instability (76.8\\% vs.\\ 17.4\\% genuine under a coarser binary classifier, $p{=}0.10$).\nISR's asymmetry is the central finding: \\emph{reliable as observer, dataset-dependent as optimizer.}\n\n\\paragraph{Contributions.}\nIn this case study (Qwen3-4B, 6 reward conditions, 3--5 seeds, 2 logic types, 2 dataset families, up to 1000 steps), we contribute: (\\textbf{C1}) STA as a diagnostic framework (ISR metric, eight-mode hacking taxonomy, and cross-domain evaluation protocol) revealing structural collapse invisible to PR (${\\leq}7\\%$ non-hacking, 3 seeds, 1000 steps; 99.5\\% in seed~42), with an SFT control consistent with GRPO-specific degradation (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) a seed-dependent compositional Goodhart effect on ISR-as-reward: in 3 of 5 seeds, significant composition shift CE$\\to$TS ($p{<}10^{-15}$) without prevalence reduction ($p{=}0.182$); 2 of 5 seeds retain ${\\sim}55\\%$ genuine reasoning, showing the effect is stochastic; apparent ISR advantage collapses to $1.06\\times$ after deconfounding; shuffled-ISR control rules out distributional shape (\\S\\ref{sec:goodhart}), with cross-domain evidence: confirmed in Prolog (3/3 seeds 0\\% non-hacking) and exploratory in ProofFOL ($p{=}0.10$), showing dataset-dependent outcomes (\\S\\ref{sec:crossdomain}).\nThese are cautionary results from a Qwen3-4B case study, replicated across dataset families, relevant to any work treating a structural proxy as a training signal (generalization scope discussed in \\S\\ref{sec:limitations}).\n",
    "structuredPatch": [
      {
        "oldStart": 37,
        "oldLines": 5,
        "newStart": 37,
        "newLines": 5,
        "lines": [
          " ISR's asymmetry is the central finding: \\emph{reliable as observer, dataset-dependent as optimizer.}",
          " ",
          " \\paragraph{Contributions.}",
          "-In this case study (Qwen3-4B, 6 reward conditions, 3--5 seeds, 2 logic types, 2 dataset families, up to 1000 steps), we contribute: (\\textbf{C1}) STA as a diagnostic framework (ISR metric, eight-mode hacking taxonomy, and cross-domain evaluation protocol) revealing structural collapse invisible to PR (${\\leq}7\\%$ non-hacking, 3 seeds, 1000 steps; 99.5\\% in seed~42), with an SFT control consistent with GRPO-specific degradation (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) a seed-dependent compositional Goodhart effect on ISR-as-reward: in 3 of 5 seeds, significant composition shift CE$\\to$TS ($p{<}10^{-15}$) without prevalence reduction ($p{=}0.182$); 2 of 5 seeds retain ${\\sim}55\\%$ genuine reasoning, showing the effect is stochastic; apparent ISR advantage collapses to $1.06\\times$ after deconfounding; shuffled-ISR control rules out distributional shape (\\S\\ref{sec:goodhart}), with cross-domain evidence: confirmed in Prolog (3/3 seeds 0\\% non-hacking) and exploratory in ProofFOL ($p{=}0.10$), showing dataset-dependent outcomes (\\S\\ref{sec:crossdomain}).",
          "+In this case study (Qwen3-4B, 6 reward conditions, 3--5 seeds, 2 logic types, 2 dataset families, up to 1000 steps), we contribute: (\\textbf{C1}) STA as a diagnostic framework (ISR metric, eight-mode hacking taxonomy, and cross-domain evaluation protocol) revealing structural collapse invisible to PR (${\\leq}7\\%$ non-hacking across 3 seeds at 1000 steps; ISR degrades 99.5\\% in seed~42), with an SFT control consistent with GRPO-specific degradation (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) a seed-dependent compositional Goodhart effect on ISR-as-reward: in 3 of 5 seeds, significant composition shift CE$\\to$TS ($p{<}10^{-15}$) without prevalence reduction ($p{=}0.182$); 2 of 5 seeds retain ${\\sim}55\\%$ genuine reasoning, showing the effect is stochastic; apparent ISR advantage collapses to $1.06\\times$ after deconfounding; shuffled-ISR control rules out distributional shape (\\S\\ref{sec:goodhart}), with cross-domain evidence: confirmed in Prolog (3/3 seeds 0\\% non-hacking) and exploratory in ProofFOL ($p{=}0.10$), showing dataset-dependent outcomes (\\S\\ref{sec:crossdomain}).",
          " These are cautionary results from a Qwen3-4B case study, replicated across dataset families, relevant to any work treating a structural proxy as a training signal (generalization scope discussed in \\S\\ref{sec:limitations})."
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01DoyjBL69N7smpDYEDN3vYD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "old_string": "$^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}",
  "new_string": "$^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "34d7f996-5964-43fe-9799-97d978212609",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdDybpRZFMa2KsMd2xmh6u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 46608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2394
      },
      "output_tokens": 22,
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

_source line 49 · 2026-05-22T03:10:05.034Z_

<details><summary>↩ Tool result · `toolu_01DoyjBL69N7smpDYEDN3vYD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "eef97332-48bd-4e4a-8ea4-ee7e8eb0666b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "oldString": "$^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}",
    "newString": "$^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse; component count inflates $2.8\\times$ over the same interval, amplifying the ratio; the mode breakdown below provides count-independent evidence). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (CE), confirming structural degeneration independent of the ISR scalar.\nAn $O(1)$ binary variant testing only collective premise necessity returns $\\text{ISR}{=}1.0$ for all 402 proved samples, confirming that per-component LOO testing is essential for detecting the collapse (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge radically ($\\text{PR}\\,\\sigma{=}47$\\,pp) into conclusion embedding (s42, CE$=$87\\%), repetition collapse (s43), and tautological collapse (s44, TS$=$100\\%), all converging to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $92.3\\%$ non-hacking ($\\text{PR}{=}13\\%$, 3-seed pooled; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$).\nSFT serves as a pre-RL reference (not a PR-matched control; its low PR reflects minimal optimization pressure, so hacking-rate differences are confounded with PR level): the base model has zero FOL capability ($\\text{PR}{=}0\\%$) and SFT's $8\\%$ hacking confirms these modes are absent before RL.\nSupplementary evidence comes from the 100-step comparison (seed~42, $n{=}32$ proved): at $\\text{PR}{=}32\\%$, hacking already reaches $31\\%$ ($9$ TS $+$ $1$ CE / $32$ proved) vs.\\ SFT's $8\\%$ at comparable PR, consistent with hacking as an RL optimization product rather than a mechanical consequence of prove-rate level (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nWe define the \\emph{compositional Goodhart effect} as: optimization against a structural proxy shifts the composition of failure modes without reducing their aggregate prevalence---a regressional pattern in \\citeauthor{manheim-goodhart-taxonomy}'s taxonomy (the proxy correlates with quality but admits satisfying shortcuts; at $\\beta{\\geq}0.2$, extremal Goodhart dominates instead) where the proxy's attack surface redirects rather than eliminates gaming.\nHere (seed-dependent; 3 of 5 seeds): (1)~hacking composition shifts from CE to TS (supplementary CMH $p{<}10^{-15}$), (2)~overall prevalence is unchanged ($p{=}0.182$); 2 of 5 seeds retain ${\\sim}55\\%$ non-hacking (Table~\\ref{tab:hacking-taxonomy}).\nDeconfounding collapses the apparent $3.2\\times$ ISR advantage to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe reward $r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ couples signals; exec-only's $0\\%$ non-hacking, the qualitative TS shift ($0\\%{\\to}71\\%$), and an additive variant's PR collapse (Appendix~\\ref{app:setup}) constrain this confound.\nA shuffled-ISR control (random permutation preserving ISR's distribution but breaking the sample-level semantic link) yields $\\text{PR}{=}15.3{\\pm}0.6\\%$ with $87.0\\%$ non-hacking ($N{=}46$, 3-seed pooled), comparable to SFT, ruling out distributional shape as the Goodhart driver.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows: TS/CE/non-hacking percentage (N-H) pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): per-seed consistent gaming.}\nISR reward increases TS rates in all three initial seeds (s42--44) relative to matched random: $70.6\\%$ ($163/231$) vs.\\ $13.7\\%$ ($36/262$) pooled (supplementary CMH: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{=}5.6{\\times}10^{-16}$; $N{=}3$ seed-level units, sample-level $p$ reflects within-seed effect; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nRandom TS is seed-dependent ($38.3\\%$ in s43 vs.\\ $0\\%$ in s42/s44); ISR amplifies TS ($2/3$ seeds at $97$--$100\\%$; Table~\\ref{tab:fol-detailed}; 5-seed extension below).\nTS (a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction; \\S\\ref{sec:taxonomy-method}) is the canonical Goodhart move: the model satisfies the LOO definition directly.\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) is $68$--$100\\%$ across both conditions; the composition differs: CE dominates under random ($71\\%$), TS under ISR. ISR converts CE into TS rather than reducing total embedding (Figure~\\ref{fig:hacking-composition}).\nRandom yields higher PR ($87{\\pm}8\\%$ vs.\\ $77{\\pm}14\\%$): noise disrupts convergence toward a single collapse trajectory.\n\n\\textbf{Premise-count confound.}\nThe sole non-TS ISR seed (s42) shows raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ random ($0.131$), a premise-minimization artifact ($n{=}5.58$ vs.\\ $8.46$); matched comparison gives $1.06\\times$ (Appendix~\\ref{app:detailed-results}). %% D051 premise-count-matched analysis\nAfter reclassifying PG and TS false negatives, non-hacking rates ($6.1\\%$ ISR vs.\\ $9.5\\%$ random) are not significant ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D095 FINAL Fisher test\nThe key asymmetry is compositional: ISR amplifies TS convergence ($2/3$ seeds ${\\geq}97\\%$), while random remains seed-dependent and CE-dominated.\n\n\\textbf{Higher doses and temporal dynamics.}\nISR $\\beta{=}0.1$ non-hacking is transient: seed~42 drops $17.3\\%{\\to}2.2\\%$ by 1000 steps as TS escalates to $96.7\\%$ (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nAt higher doses ($\\beta{\\geq}0.2$), TS becomes universal ($0\\%$ non-hacking at $\\beta{=}0.2$); $\\beta{=}0.3$ destabilizes both ISR ($\\text{PR}{=}66{\\pm}42\\%$) and random ($54{\\pm}35\\%$), with ISR producing multi-modal failure~\\citep{gao-reward-overoptimization} and random converging to CE ($91\\%$; Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking---qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nWe replicate the FOL pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}).\nExec-only seeds show $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding (2/3 seeds); ISR flags this mode as it flags FOL's conclusion embedding.\nUnder ISR-as-reward, 3/3 seeds reach 0\\% non-hacking through distinct mechanisms: clean TS (s42), uppercase pseudo-Prolog bypassing text-match classifiers (s43, all 38 proved at $n_{\\text{necessary}}{=}1$), and query-as-fact gaming (s44, 95/97 at $n_{\\text{necessary}}{=}1$; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the non-hacking residual entirely.\n\n\\textbf{ProofFOL exec-only: cross-dataset evidence for structural degeneration, with differing mode distributions.}\nTwo converged seeds ($\\text{ISR}^*{<}0.07$) show ${\\leq}1.4\\%$ genuine; s42 exhibits 100\\% TS (absent from all FOLIO exec-only seeds), showing hacking-mode repertoire is dataset-specific ($\\text{ISR}^*{<}0.12$ across all seeds, far below baseline $0.31$).\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): beneficial instability (exploratory).}\nISR seeds average 76.8\\% genuine versus 17.4\\% exec-only ($p{=}0.10$, $N{=}3$; Table~\\ref{tab:prooffol-detailed}), but ISR prove rates ($0.35$--$0.49$) remain far below exec-only (${\\sim}1.0$), so this may reflect insufficient training; ProofFOL ``genuine'' excludes only TS/CE (coarser than FOLIO's eight-mode residual).\n\n\\textbf{Mechanism.}\nThe dataset-dependent outcome follows from hacking geometry: on FOLIO, $P{\\to}P$ produces 2-component formalizations where both are LOO-necessary ($\\text{ISR}{\\geq}0.5$, regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, hacking embeds conclusions among many premises ($\\bar{n}{=}18.2$), making most individually redundant ($\\text{ISR}{\\approx}0$).\nISR-as-reward thus inherits the dataset's hacking topology: it rewards shortcuts only when the shortcut geometry satisfies the LOO criterion.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for ${>}90\\%$ of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): \\textbf{CE} (conclusion embedding), \\textbf{TS} (conclusion duplication, ISR-amplified), and \\textbf{PG} (premise-subset gaming; audited for s42 only). \\emph{Reward formulation determines composition but not prevalence}: all GRPO conditions show ${\\geq}80\\%$ hacking; only SFT achieves $92.3\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 147,
        "oldLines": 7,
        "newStart": 147,
        "newLines": 7,
        "lines": [
          " \\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\",
          " \\bottomrule",
          " \\end{tabular}}",
          "-\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}",
          "+\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}",
          " \\label{tab:hacking-taxonomy}",
          " \\end{table}",
          " "
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01JEPnkbtGu2SFRfyQswXRew`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
  "old_string": "@misc{mccune-prover9,",
  "new_string": "@article{deepseek-prover-v2,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},\n  journal      = {arXiv preprint arXiv:2504.21801},\n  year         = {2025},\n  eprint       = {2504.21801},\n  archivePrefix = {arXiv},\n}\n\n@article{cui2025prime,\n  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},\n  title        = {{Process Reinforcement through Implicit Rewards}},\n  journal      = {arXiv preprint arXiv:2502.01456},\n  year         = {2025},\n  eprint       = {2502.01456},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@misc{mccune-prover9,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "241e3cfe-e23f-482a-8e74-f432ee206d2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdDybpRZFMa2KsMd2xmh6u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 46608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2394
      },
      "output_tokens": 22,
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

_source line 51 · 2026-05-22T03:10:09.405Z_

<details><summary>↩ Tool result · `toolu_01JEPnkbtGu2SFRfyQswXRew`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "df421dc0-6b84-42f7-a0ae-f1690549f8b1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
    "oldString": "@misc{mccune-prover9,",
    "newString": "@article{deepseek-prover-v2,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},\n  journal      = {arXiv preprint arXiv:2504.21801},\n  year         = {2025},\n  eprint       = {2504.21801},\n  archivePrefix = {arXiv},\n}\n\n@article{cui2025prime,\n  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},\n  title        = {{Process Reinforcement through Implicit Rewards}},\n  journal      = {arXiv preprint arXiv:2502.01456},\n  year         = {2025},\n  eprint       = {2502.01456},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@misc{mccune-prover9,",
    "originalFile": "% ============================================================\n% LLaMA\n% ============================================================\n\n@article{grattafiori2024llama,\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},\n  title = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n  eprint = {2407.21783},\n  archiveprefix = {arXiv},\n}\n\n% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--41},\n  year         = {1978},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@article{spurious-rewards,\n  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Reward shaping and process supervision\n% ============================================================\n\n@article{rlsf,\n  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},\n  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\\`{a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  note         = {arXiv:2404.18926},\n}\n\n@article{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  journal      = {arXiv preprint arXiv:2408.08152},\n  year         = {2024},\n  eprint       = {2408.08152},\n  archivePrefix = {arXiv},\n}\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2501.12948},\n  year         = {2025},\n  eprint       = {2501.12948},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nlproofs,\n  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},\n  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},\n  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2022},\n  eprint       = {2205.12443},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{vstar,\n  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},\n  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},\n  booktitle    = {Conference on Language Modeling (COLM)},\n  year         = {2024},\n  eprint       = {2402.06457},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{easy-to-hard,\n  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},\n  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  eprint       = {2403.09472},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@article{reward-hacking-survey,\n  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n}\n\n@misc{metr-reward-hacking,\n  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR Technical Blog},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2021},\n  note         = {arXiv:2012.13048},\n}\n\n@article{prooffol-thatikonda2024,\n  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},\n  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},\n  journal      = {arXiv preprint arXiv:2409.16461},\n  year         = {2024},\n  eprint       = {2409.16461},\n  archivePrefix = {arXiv},\n}\n\n@article{qwen3,\n  author       = {{Qwen Team}},\n  title        = {{Qwen3 Technical Report}},\n  journal      = {arXiv preprint arXiv:2505.09388},\n  year         = {2025},\n  eprint       = {2505.09388},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@article{helff2026gaming,\n  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\\\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},\n  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},\n  journal      = {arXiv preprint arXiv:2604.15149},\n  year         = {2026},\n  eprint       = {2604.15149},\n  archivePrefix = {arXiv},\n}\n\n@article{khalifa2026countdown,\n  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},\n  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},\n  journal      = {arXiv preprint arXiv:2603.07084},\n  year         = {2026},\n  eprint       = {2603.07084},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{uesato2022solving,\n  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},\n  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},\n  booktitle={NeurIPS 2022 Workshop on MATH-AI},\n  year={2022}\n}\n\n@article{cobbe2021training,\n  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},\n  title        = {{Training Verifiers to Solve Math Word Problems}},\n  journal      = {arXiv preprint arXiv:2110.14168},\n  year         = {2021},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{pronesti2026beyond,\n  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},\n  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},\n  journal      = {arXiv preprint arXiv:2601.17223},\n  year         = {2026},\n  eprint       = {2601.17223},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{ng1999policy,\n  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},\n  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year      = {1999},\n  pages     = {278--287},\n}\n\n@article{geirhos2020shortcut,\n  author  = {Robert Geirhos and J{\\\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},\n  title   = {Shortcut Learning in Deep Neural Networks},\n  journal = {Nature Machine Intelligence},\n  volume  = {2},\n  pages   = {665--673},\n  year    = {2020},\n}\n\n@article{dong2026probing,\n  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},\n  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},\n  journal      = {arXiv preprint arXiv:2602.01103},\n  year         = {2026},\n  eprint       = {2602.01103},\n  archivePrefix = {arXiv},\n}\n\n@article{yan2026spurious,\n  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},\n  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},\n  journal      = {arXiv preprint arXiv:2601.11061},\n  year         = {2026},\n  eprint       = {2601.11061},\n  archivePrefix = {arXiv},\n}\n\n@article{tarek2025reward,\n  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},\n  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},\n  journal      = {arXiv preprint arXiv:2509.15557},\n  year         = {2025},\n  eprint       = {2509.15557},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{yue2025rl-reasoning,\n  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},\n  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2025},\n  eprint       = {2504.13837},\n  archivePrefix = {arXiv},\n}\n\n@article{sullivan2025grpo-prm,\n  author       = {Michael Sullivan and Alexander Koller},\n  title        = {{GRPO} is Secretly a Process Reward Model},\n  journal      = {arXiv preprint arXiv:2509.21154},\n  year         = {2025},\n  eprint       = {2509.21154},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% R19 reviewer-requested references\n% ============================================================\n\n@inproceedings{setlur2025rewarding,\n  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},\n  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2410.08146},\n}\n\n@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}\n\n% ============================================================\n% Solvers (Prover9, SWI-Prolog)\n% ============================================================\n\n@misc{mccune-prover9,\n  author       = {William McCune},\n  title        = {{Prover9 and Mace4}},\n  year         = {2005--2010},\n  howpublished = {\\url{https://www.cs.unm.edu/~mccune/prover9/}},\n  note         = {Version 2009-11A},\n}\n\n@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n",
    "structuredPatch": [
      {
        "oldStart": 460,
        "oldLines": 6,
        "newStart": 460,
        "newLines": 25,
        "lines": [
          " % Solvers (Prover9, SWI-Prolog)",
          " % ============================================================",
          " ",
          "+@article{deepseek-prover-v2,",
          "+  author       = {{DeepSeek-AI}},",
          "+  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},",
          "+  journal      = {arXiv preprint arXiv:2504.21801},",
          "+  year         = {2025},",
          "+  eprint       = {2504.21801},",
          "+  archivePrefix = {arXiv},",
          "+}",
          "+",
          "+@article{cui2025prime,",
          "+  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},",
          "+  title        = {{Process Reinforcement through Implicit Rewards}},",
          "+  journal      = {arXiv preprint arXiv:2502.01456},",
          "+  year         = {2025},",
          "+  eprint       = {2502.01456},",
          "+  archivePrefix = {arXiv},",
          "+  primaryClass = {cs.CL},",
          "+}",
          "+",
          " @misc{mccune-prover9,",
          "   author       = {William McCune},",
          "   title        = {{Prover9 and Mace4}},"
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

_source line 52_

Now adding citations in related_work.tex — DeepSeek-Prover-V2 in the neurosymbolic paragraph, PRIME in the process rewards paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "0069e0e1-b06f-4581-adcd-0da9aa81bc3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfVgjXnv4K3YJTCdTJpuAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2984,
      "cache_read_input_tokens": 49002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2984
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

_source line 53_

<details open><summary>🔧 Tool call — Edit · `toolu_01U6M8tFiah6xxTLxBenAwUF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
  "old_string": "AlphaProof~\\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.",
  "new_string": "AlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4, achieving state-of-the-art results on competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these theorem-proving settings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "b371651e-13e4-44f4-b61a-6bc9a4704f55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfVgjXnv4K3YJTCdTJpuAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2984,
      "cache_read_input_tokens": 49002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2984
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

_source line 54 · 2026-05-22T03:10:15.998Z_

<details><summary>↩ Tool result · `toolu_01U6M8tFiah6xxTLxBenAwUF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "c7846260-9425-45ec-97dc-ebed327db93d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
    "oldString": "AlphaProof~\\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.",
    "newString": "AlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4, achieving state-of-the-art results on competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these theorem-proving settings.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nReward shaping theory~\\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\\citep{uesato2022solving}.\nLearned PRMs~\\citep{lightman-verify-step, math-shepherd} and verifier-guided search~\\citep{nlproofs, vstar} provide step-level feedback but suffer from reward-model noise and distribution shift~\\citep{processbench}; \\citet{easy-to-hard} show that verifiers trained on easy tasks can generalize to hard ones, though structural gaming remains unaddressed.\n\\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \\citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\\beta$-dependent Goodhart transitions.\nSymbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\n\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly equivalent to a Monte-Carlo PRM, offering a mechanism for why component-level gaming emerges under GRPO specifically.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.\n\\citet{kim-game-formalization} document inference-time gaming in logical formalization on FOLIO using frontier models with Lean~4.\nOur work is complementary: training-time (vs.\\ inference), component necessity (vs.\\ faithfulness), medium-model/Prover9 (vs.\\ frontier/Lean~4); combining STA with inference-time faithfulness detection would provide complete gaming coverage.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.\nRecent work further documents spurious reward signals in RLVR~\\citep{spurious-rewards, yan2026spurious}, training instability via objective-level hacking~\\citep{dong2026probing}, reward hacking in frontier models~\\citep{metr-reward-hacking}, and proposes verifiable composite or process rewards to mitigate outcome-only limitations~\\citep{tarek2025reward, pronesti2026beyond}.\n\\citet{yue2025rl-reasoning} show RLVR redistributes probability mass over base-model capabilities rather than eliciting new reasoning patterns, consistent with our finding that GRPO-trained models exploit existing shortcuts rather than learning genuine derivation.\n\\citet{helff2026gaming} propose Input Perturbation Testing (IPT), which perturbs verifier inputs to detect gaming; STA shares the perturbation intuition but operates at the component level (LOO ablation on solver premises vs.\\ token-level perturbation on verifier prompts) and targets neurosymbolic settings where gaming \\emph{emerges during training}.\n\\citet{khalifa2026countdown} provide RLVR hacking testbeds.\nThe Goodhart effect follows standard taxonomy~\\citep{manheim-goodhart-taxonomy}: regressional on FOLIO (tautologies satisfy the LOO metric), extremal at high $\\beta$. Its application to a structural diagnostic designed to \\emph{detect} gaming is, to our knowledge, novel; the dataset-dependent asymmetry (the same metric gamed on one dataset, beneficial on another) is a non-trivial empirical finding not predicted by the taxonomy alone.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Neurosymbolic reasoning.}",
          " LLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.",
          "-AlphaProof~\\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.",
          "+AlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4, achieving state-of-the-art results on competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these theorem-proving settings.",
          " We use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.",
          " ",
          " \\paragraph{Process rewards and reward shaping.}"
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

_source line 55_

<details open><summary>🔧 Tool call — Edit · `toolu_019mRnU2rpEJCUmn5Dv6d91Q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
  "old_string": "\\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \\citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\\beta$-dependent Goodhart transitions.",
  "new_string": "\\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \\citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\\beta$-dependent Goodhart transitions.\n\\citet{cui2025prime} derive implicit process rewards from outcome-level signals without step-level annotation, showing that reward density can be improved cheaply; ISR similarly requires no annotation but operates at the component level, and our results show that even annotation-free structural rewards are susceptible to Goodhart effects."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "379f3f14-6e10-47d2-9e08-e7795223b026",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfVgjXnv4K3YJTCdTJpuAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2984,
      "cache_read_input_tokens": 49002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2984
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

_source line 56 · 2026-05-22T03:10:22.468Z_

<details><summary>↩ Tool result · `toolu_019mRnU2rpEJCUmn5Dv6d91Q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "88de5b6f-b2a7-407f-bba1-b80b15af55a2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
    "oldString": "\\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \\citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\\beta$-dependent Goodhart transitions.",
    "newString": "\\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \\citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\\beta$-dependent Goodhart transitions.\n\\citet{cui2025prime} derive implicit process rewards from outcome-level signals without step-level annotation, showing that reward density can be improved cheaply; ISR similarly requires no annotation but operates at the component level, and our results show that even annotation-free structural rewards are susceptible to Goodhart effects.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4, achieving state-of-the-art results on competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these theorem-proving settings.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nReward shaping theory~\\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\\citep{uesato2022solving}.\nLearned PRMs~\\citep{lightman-verify-step, math-shepherd} and verifier-guided search~\\citep{nlproofs, vstar} provide step-level feedback but suffer from reward-model noise and distribution shift~\\citep{processbench}; \\citet{easy-to-hard} show that verifiers trained on easy tasks can generalize to hard ones, though structural gaming remains unaddressed.\n\\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \\citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\\beta$-dependent Goodhart transitions.\nSymbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\n\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly equivalent to a Monte-Carlo PRM, offering a mechanism for why component-level gaming emerges under GRPO specifically.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.\n\\citet{kim-game-formalization} document inference-time gaming in logical formalization on FOLIO using frontier models with Lean~4.\nOur work is complementary: training-time (vs.\\ inference), component necessity (vs.\\ faithfulness), medium-model/Prover9 (vs.\\ frontier/Lean~4); combining STA with inference-time faithfulness detection would provide complete gaming coverage.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.\nRecent work further documents spurious reward signals in RLVR~\\citep{spurious-rewards, yan2026spurious}, training instability via objective-level hacking~\\citep{dong2026probing}, reward hacking in frontier models~\\citep{metr-reward-hacking}, and proposes verifiable composite or process rewards to mitigate outcome-only limitations~\\citep{tarek2025reward, pronesti2026beyond}.\n\\citet{yue2025rl-reasoning} show RLVR redistributes probability mass over base-model capabilities rather than eliciting new reasoning patterns, consistent with our finding that GRPO-trained models exploit existing shortcuts rather than learning genuine derivation.\n\\citet{helff2026gaming} propose Input Perturbation Testing (IPT), which perturbs verifier inputs to detect gaming; STA shares the perturbation intuition but operates at the component level (LOO ablation on solver premises vs.\\ token-level perturbation on verifier prompts) and targets neurosymbolic settings where gaming \\emph{emerges during training}.\n\\citet{khalifa2026countdown} provide RLVR hacking testbeds.\nThe Goodhart effect follows standard taxonomy~\\citep{manheim-goodhart-taxonomy}: regressional on FOLIO (tautologies satisfy the LOO metric), extremal at high $\\beta$. Its application to a structural diagnostic designed to \\emph{detect} gaming is, to our knowledge, novel; the dataset-dependent asymmetry (the same metric gamed on one dataset, beneficial on another) is a non-trivial empirical finding not predicted by the taxonomy alone.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 6,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " Reward shaping theory~\\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\\citep{uesato2022solving}.",
          " Learned PRMs~\\citep{lightman-verify-step, math-shepherd} and verifier-guided search~\\citep{nlproofs, vstar} provide step-level feedback but suffer from reward-model noise and distribution shift~\\citep{processbench}; \\citet{easy-to-hard} show that verifiers trained on easy tasks can generalize to hard ones, though structural gaming remains unaddressed.",
          " \\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \\citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\\beta$-dependent Goodhart transitions.",
          "+\\citet{cui2025prime} derive implicit process rewards from outcome-level signals without step-level annotation, showing that reward density can be improved cheaply; ISR similarly requires no annotation but operates at the component level, and our results show that even annotation-free structural rewards are susceptible to Goodhart effects.",
          " Symbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.",
          " \\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly equivalent to a Monte-Carlo PRM, offering a mechanism for why component-level gaming emerges under GRPO specifically.",
          " "
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

_source line 57_

All four modifications complete:

1. **Reproducibility statement** — added release sentence at end of `limitations.tex`
2. **Missing references** — added `deepseek-prover-v2` and `cui2025prime` to `references.bib`; cited DeepSeek-Prover-V2 in neurosymbolic paragraph and PRIME in process rewards paragraph of `related_work.tex`
3. **Introduction 99.5% fix** — changed comma-separated list to "across 3 seeds at 1000 steps; ISR degrades 99.5\%" for clarity
4. **Table 2 caption** — added "`1k` denotes a mode observed only at the 1000-step checkpoint"

Note: DeepSeek-Prover-V2's correct arXiv ID is **2504.21801** (not 2501.14333 as initially suggested).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "uuid": "de997c34-d85e-4f30-922f-2a94d6e3b2af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvwhhFDgrkByQrAbJedZrM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 51986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 851
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

_source line 58_

All four modifications complete:

1. **Reproducibility statement** — added release sentence at end of `limitations.tex`
2. **Missing references** — added `deepseek-prover-v2` and `cui2025prime` to `references.bib`; cited DeepSeek-Prover-V2 in neurosymbolic paragraph and PRIME in process rewards paragraph of `related_work.tex`
3. **Introduction 99.5% fix** — changed comma-separated list to "across 3 seeds at 1000 steps; ISR degrades 99.5\%" for clarity
4. **Table 2 caption** — added "`1k` denotes a mode observed only at the 1000-step checkpoint"

Note: DeepSeek-Prover-V2's correct arXiv ID is **2504.21801** (not 2501.14333 as initially suggested).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 114405,
  "duration_api_ms": 134078,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "a03d9e33-cd52-4545-a7a0-012e3f1f1d90",
  "total_cost_usd": 0.6031313500000001,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 40996,
    "cache_read_input_tokens": 186477,
    "output_tokens": 5649,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40996,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 216,
        "cache_read_input_tokens": 51986,
        "cache_creation_input_tokens": 851,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 851
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 38314,
      "outputTokens": 2447,
      "cacheReadInputTokens": 63726,
      "cacheCreationInputTokens": 20385,
      "webSearchRequests": 3,
      "costUSD": 0.11240284999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 5649,
      "cacheReadInputTokens": 186477,
      "cacheCreationInputTokens": 40996,
      "webSearchRequests": 0,
      "costUSD": 0.4907284999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b62678f3-fc8f-4f61-a9bf-1e4aee9c27ba"
}
```

</details>

---
