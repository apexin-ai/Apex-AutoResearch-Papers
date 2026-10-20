# paper research bib quality fix r2

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 72
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_paper_research_bib-quality-fix-r2_20260515T035006.log`
- **Structured JSON:** [`41dcdc9ac0a34379850e.json`](../../sessions/41/41dcdc9ac0a34379850e.json)

## Before a recorded user message

72 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
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
  "uuid": "08a2d723-73d2-4921-bbcb-a183a4383703",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/memory/"
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
    "resetsAt": 1778826600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3f013ae0-643b-4ac5-a482-4fb684df341a",
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the bib file and then doing the WebSearches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "3bb6b0c3-047c-4632-af6a-7fbf09cd8847",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rGKxAQurTAM5vTV1TwHG7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13123
      },
      "output_tokens": 27,
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

Reading the bib file and searching for the 3 missing author entries plus verifying Reflexion authors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "4f074408-ba21-4dca-abc5-28fede6c7d1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rGKxAQurTAM5vTV1TwHG7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13123
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — Read · `toolu_011xMtG7AheQrgH64fYUgkVk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "e355ce7a-923b-4437-bcf7-320702c44700",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rGKxAQurTAM5vTV1TwHG7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13123
      },
      "output_tokens": 27,
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

_source line 7 · 2026-05-15T03:50:18.607Z_

<details><summary>↩ Tool result · `toolu_011xMtG7AheQrgH64fYUgkVk`</summary>

```text
1	@article{rolnick2017robust,
2	  title={Deep Learning is Robust to Massive Label Noise},
3	  author={{Rolnick} and {Veit} and {Belongie} and {Shavit}},
4	  year={2017},
5	  journal={arXiv preprint arXiv:1705.10694},
6	  url={https://arxiv.org/abs/1705.10694}
7	}
8	
9	@inproceedings{yuan2024early_stopping,
10	  title={Early Stopping Against Label Noise Without Validation Data},
11	  author={{Yuan} and {Feng} and {Liu}},
12	  year={2024},
13	  booktitle={International Conference on Learning Representations}
14	}
15	
16	@inproceedings{dohmatob2025collapse,
17	  title={Strong Model Collapse},
18	  author={{Dohmatob} and {Feng} and {Subramonian} and {Kempe}},
19	  year={2025},
20	  booktitle={International Conference on Learning Representations}
21	}
22	
23	@article{beyond_clean_data2024,
24	  title={Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance},
25	  author={{Various Authors}},
26	  year={2024},
27	  journal={ScienceDirect}
28	}
29	
30	@article{wang2024learning_from_failure,
31	  title={Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents},
32	  author={{Wang} and {Li} and {Han} and {Zhang} and {Baldwin}},
33	  year={2024},
34	  journal={arXiv preprint arXiv:2402.11651},
35	  url={https://arxiv.org/abs/2402.11651}
36	}
37	
38	@inproceedings{song2024eto,
39	  title={Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents},
40	  author={{Song} and {Yin} and {Yue} and {Huang} and {Li} and {Lin}},
41	  year={2024},
42	  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}
43	}
44	
45	@article{paladin2025,
46	  title={{PALADIN}: Self-Correcting Language Model Agents to Cure Tool-Failure Cases},
47	  author={{Vuddanti} and {Shah} and Others},
48	  year={2025},
49	  journal={arXiv preprint arXiv:2509.25238},
50	  url={https://arxiv.org/abs/2509.25238}
51	}
52	
53	@article{agentHER2025,
54	  title={{AgentHER}: Hindsight Experience Replay for LLM Agent Trajectory Relabeling},
55	  author={{Various Authors}},
56	  year={2025},
57	  journal={arXiv preprint arXiv:2603.21357},
58	  url={https://arxiv.org/abs/2603.21357}
59	}
60	
61	@inproceedings{dong2024composition,
62	  title={How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition},
63	  author={{Dong} and {Yuan} and Others},
64	  year={2024},
65	  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}
66	}
67	
68	@inproceedings{ye2025mixing_laws,
69	  title={Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance},
70	  author={{Ye} and Others},
71	  year={2025},
72	  booktitle={International Conference on Learning Representations}
73	}
74	
75	@inproceedings{li2025mixing_optimization,
76	  title={Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models},
77	  author={{Li} and Others},
78	  year={2025},
79	  booktitle={Proceedings of the International Conference on Machine Learning}
80	}
81	
82	@article{seddik2024synthetic_bound,
83	  title={How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse},
84	  author={{Seddik} and Others},
85	  year={2024},
86	  journal={arXiv preprint arXiv:2404.05090},
87	  url={https://arxiv.org/abs/2404.05090}
88	}
89	
90	@inproceedings{curriculum_robust2021,
91	  title={Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction},
92	  author={{Zhou} and {Wang} and {Bilmes}},
93	  year={2021},
94	  booktitle={International Conference on Learning Representations}
95	}
96	
97	@article{agentprm2025,
98	  title={Process Reward Models for LLM Agents: Practical Framework and Directions},
99	  author={{Choudhury}},
100	  year={2025},
101	  journal={arXiv preprint arXiv:2502.10325},
102	  url={https://arxiv.org/abs/2502.10325}
103	}
104	
105	@inproceedings{wkm2024alfworld,
106	  title={Agent Planning with World Knowledge Model},
107	  author={{Various Authors}},
108	  year={2024},
109	  booktitle={Advances in Neural Information Processing Systems}
110	}
111	
112	@inproceedings{arpit2017memorization,
113	  title={A Closer Look at Memorization in Deep Networks},
114	  author={{Arpit} and {Jastrz\k{e}bski} and {Ballas} and {Krueger} and {Bengio} and {Kanwal} and {Maharaj} and {Fischer} and {Courville} and {Bengio} and {Lacoste-Julien}},
115	  year={2017},
116	  booktitle={Proceedings of the International Conference on Machine Learning}
117	}
118	
119	@inproceedings{liu2020early_learning_reg,
120	  title={Early-Learning Regularization Prevents Memorization of Noisy Labels},
121	  author={{Liu} and {Niles-Weed} and {Razavian} and {Fernandez-Granda}},
122	  year={2020},
123	  booktitle={Advances in Neural Information Processing Systems}
124	}
125	
126	@inproceedings{zhou2023lima,
127	  title={{LIMA}: Less Is More for Alignment},
128	  author={{Zhou} and {Liu} and {Xu} and {Iyer} and {Sun} and {Mao} and {Ma} and {Efrat} and {Yu} and {Yu} and {Zhang} and {Ghosh} and {Lewis} and {Zettlemoyer} and {Levy}},
129	  year={2023},
130	  booktitle={Advances in Neural Information Processing Systems}
131	}
132	
133	@article{luo2023catastrophic_forgetting,
134	  title={An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning},
135	  author={{Luo} and {Yang} and {Meng} and {Li} and {Zhou} and {Zhang}},
136	  year={2023},
137	  journal={arXiv preprint arXiv:2308.08747},
138	  url={https://arxiv.org/abs/2308.08747}
139	}
140	
141	@inproceedings{longpre2020augmentation,
142	  title={How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?},
143	  author={{Longpre} and {Wang} and {DuBois}},
144	  year={2020},
145	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020}
146	}
147	
148	@inproceedings{mccoy2020seeds,
149	  title={{BERTs} of a feather do not generalize together: Large variability in generalization across models with similar test set performance},
150	  author={{McCoy} and {Min} and {Linzen}},
151	  year={2020},
152	  booktitle={Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP}
153	}
154	
155	@inproceedings{mosbach2021stability,
156	  title={On the Stability of Fine-tuning {BERT}: Misconceptions, Explanations, and Strong Baselines},
157	  author={{Mosbach} and {Andriushchenko} and {Klakow}},
158	  year={2021},
159	  booktitle={International Conference on Learning Representations}
160	}
161	
162	@article{damour2022underspecification,
163	  title={Underspecification Presents Challenges for Credibility in Modern Machine Learning},
164	  author={{D'Amour} and {Heller} and {Moldovan} and {Adlam} and {Alipanahi} and {Beutel} and {Chen} and {Deaton} and {Eisenstein} and {Hoffman} and Others},
165	  year={2022},
166	  journal={Journal of Machine Learning Research},
167	  volume={23},
168	  number={226}
169	}
170	
171	@inproceedings{shridhar2021alfworld,
172	  title={{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},
173	  author={{Shridhar} and {Yuan} and {C\^{o}t\'{e}} and {Bisk} and {Trischler} and {Hausknecht}},
174	  year={2021},
175	  booktitle={International Conference on Learning Representations},
176	  url={https://arxiv.org/abs/2010.03768}
177	}
178	
179	@inproceedings{yao2023react,
180	  title={{ReAct}: Synergizing Reasoning and Acting in Language Models},
181	  author={{Yao} and {Zhao} and {Yu} and {Du} and {Shafran} and {Narasimhan} and {Cao}},
182	  year={2023},
183	  booktitle={International Conference on Learning Representations},
184	  url={https://arxiv.org/abs/2210.03629}
185	}
186	
187	@inproceedings{shinn2023reflexion,
188	  title={Reflexion: Language Agents with Verbal Reinforcement Learning},
189	  author={{Shinn} and {Cassano} and {Berman} and {Gopinath} and {Narasimhan} and {Yao}},
190	  year={2023},
191	  booktitle={Advances in Neural Information Processing Systems},
192	  url={https://arxiv.org/abs/2303.11366}
193	}
194	
195	@inproceedings{kim2025coex,
196	  title={{CoEx} -- Co-evolving World-model and Exploration},
197	  author={{Kim} and {Hwang}},
198	  year={2025},
199	  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
200	  url={https://arxiv.org/abs/2507.22281}
201	}
202	
203	@article{eef2025,
204	  title={Exploring Expert Failures Improves LLM Agent Tuning},
205	  author={{Lan} and {Bai} and {Cheng} and {Wang} and Others},
206	  year={2025},
207	  journal={arXiv preprint arXiv:2504.13145},
208	  url={https://arxiv.org/abs/2504.13145}
209	}
210	
211	@article{agentdebug2025,
212	  title={Where LLM Agents Fail and How They can Learn From Failures},
213	  author={{Zhu} and {Liu} and {Li} and {Tian} and Others},
214	  year={2025},
215	  journal={arXiv preprint arXiv:2509.25370},
216	  url={https://arxiv.org/abs/2509.25370}
217	}
218	
219	@inproceedings{bengio2009curriculum,
220	  title={Curriculum Learning},
221	  author={{Bengio} and {Louradour} and {Collobert} and {Weston}},
222	  year={2009},
223	  booktitle={Proceedings of the International Conference on Machine Learning}
224	}
225	
226	@inproceedings{madry2018adversarial,
227	  title={Towards Deep Learning Models Resistant to Adversarial Attacks},
228	  author={{Madry} and {Makelov} and {Schmidt} and {Tsipras} and {Vladu}},
229	  year={2018},
230	  booktitle={International Conference on Learning Representations}
231	}
232	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "9b80e78a-2e8b-4528-8ad4-de3975a325e9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/references.bib",
      "content": "@article{rolnick2017robust,\n  title={Deep Learning is Robust to Massive Label Noise},\n  author={{Rolnick} and {Veit} and {Belongie} and {Shavit}},\n  year={2017},\n  journal={arXiv preprint arXiv:1705.10694},\n  url={https://arxiv.org/abs/1705.10694}\n}\n\n@inproceedings{yuan2024early_stopping,\n  title={Early Stopping Against Label Noise Without Validation Data},\n  author={{Yuan} and {Feng} and {Liu}},\n  year={2024},\n  booktitle={International Conference on Learning Representations}\n}\n\n@inproceedings{dohmatob2025collapse,\n  title={Strong Model Collapse},\n  author={{Dohmatob} and {Feng} and {Subramonian} and {Kempe}},\n  year={2025},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{beyond_clean_data2024,\n  title={Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance},\n  author={{Various Authors}},\n  year={2024},\n  journal={ScienceDirect}\n}\n\n@article{wang2024learning_from_failure,\n  title={Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents},\n  author={{Wang} and {Li} and {Han} and {Zhang} and {Baldwin}},\n  year={2024},\n  journal={arXiv preprint arXiv:2402.11651},\n  url={https://arxiv.org/abs/2402.11651}\n}\n\n@inproceedings{song2024eto,\n  title={Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents},\n  author={{Song} and {Yin} and {Yue} and {Huang} and {Li} and {Lin}},\n  year={2024},\n  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}\n}\n\n@article{paladin2025,\n  title={{PALADIN}: Self-Correcting Language Model Agents to Cure Tool-Failure Cases},\n  author={{Vuddanti} and {Shah} and Others},\n  year={2025},\n  journal={arXiv preprint arXiv:2509.25238},\n  url={https://arxiv.org/abs/2509.25238}\n}\n\n@article{agentHER2025,\n  title={{AgentHER}: Hindsight Experience Replay for LLM Agent Trajectory Relabeling},\n  author={{Various Authors}},\n  year={2025},\n  journal={arXiv preprint arXiv:2603.21357},\n  url={https://arxiv.org/abs/2603.21357}\n}\n\n@inproceedings{dong2024composition,\n  title={How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition},\n  author={{Dong} and {Yuan} and Others},\n  year={2024},\n  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}\n}\n\n@inproceedings{ye2025mixing_laws,\n  title={Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance},\n  author={{Ye} and Others},\n  year={2025},\n  booktitle={International Conference on Learning Representations}\n}\n\n@inproceedings{li2025mixing_optimization,\n  title={Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models},\n  author={{Li} and Others},\n  year={2025},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@article{seddik2024synthetic_bound,\n  title={How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse},\n  author={{Seddik} and Others},\n  year={2024},\n  journal={arXiv preprint arXiv:2404.05090},\n  url={https://arxiv.org/abs/2404.05090}\n}\n\n@inproceedings{curriculum_robust2021,\n  title={Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction},\n  author={{Zhou} and {Wang} and {Bilmes}},\n  year={2021},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{agentprm2025,\n  title={Process Reward Models for LLM Agents: Practical Framework and Directions},\n  author={{Choudhury}},\n  year={2025},\n  journal={arXiv preprint arXiv:2502.10325},\n  url={https://arxiv.org/abs/2502.10325}\n}\n\n@inproceedings{wkm2024alfworld,\n  title={Agent Planning with World Knowledge Model},\n  author={{Various Authors}},\n  year={2024},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@inproceedings{arpit2017memorization,\n  title={A Closer Look at Memorization in Deep Networks},\n  author={{Arpit} and {Jastrz\\k{e}bski} and {Ballas} and {Krueger} and {Bengio} and {Kanwal} and {Maharaj} and {Fischer} and {Courville} and {Bengio} and {Lacoste-Julien}},\n  year={2017},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@inproceedings{liu2020early_learning_reg,\n  title={Early-Learning Regularization Prevents Memorization of Noisy Labels},\n  author={{Liu} and {Niles-Weed} and {Razavian} and {Fernandez-Granda}},\n  year={2020},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@inproceedings{zhou2023lima,\n  title={{LIMA}: Less Is More for Alignment},\n  author={{Zhou} and {Liu} and {Xu} and {Iyer} and {Sun} and {Mao} and {Ma} and {Efrat} and {Yu} and {Yu} and {Zhang} and {Ghosh} and {Lewis} and {Zettlemoyer} and {Levy}},\n  year={2023},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@article{luo2023catastrophic_forgetting,\n  title={An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning},\n  author={{Luo} and {Yang} and {Meng} and {Li} and {Zhou} and {Zhang}},\n  year={2023},\n  journal={arXiv preprint arXiv:2308.08747},\n  url={https://arxiv.org/abs/2308.08747}\n}\n\n@inproceedings{longpre2020augmentation,\n  title={How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?},\n  author={{Longpre} and {Wang} and {DuBois}},\n  year={2020},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020}\n}\n\n@inproceedings{mccoy2020seeds,\n  title={{BERTs} of a feather do not generalize together: Large variability in generalization across models with similar test set performance},\n  author={{McCoy} and {Min} and {Linzen}},\n  year={2020},\n  booktitle={Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP}\n}\n\n@inproceedings{mosbach2021stability,\n  title={On the Stability of Fine-tuning {BERT}: Misconceptions, Explanations, and Strong Baselines},\n  author={{Mosbach} and {Andriushchenko} and {Klakow}},\n  year={2021},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{damour2022underspecification,\n  title={Underspecification Presents Challenges for Credibility in Modern Machine Learning},\n  author={{D'Amour} and {Heller} and {Moldovan} and {Adlam} and {Alipanahi} and {Beutel} and {Chen} and {Deaton} and {Eisenstein} and {Hoffman} and Others},\n  year={2022},\n  journal={Journal of Machine Learning Research},\n  volume={23},\n  number={226}\n}\n\n@inproceedings{shridhar2021alfworld,\n  title={{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},\n  author={{Shridhar} and {Yuan} and {C\\^{o}t\\'{e}} and {Bisk} and {Trischler} and {Hausknecht}},\n  year={2021},\n  booktitle={International Conference on Learning Representations},\n  url={https://arxiv.org/abs/2010.03768}\n}\n\n@inproceedings{yao2023react,\n  title={{ReAct}: Synergizing Reasoning and Acting in Language Models},\n  author={{Yao} and {Zhao} and {Yu} and {Du} and {Shafran} and {Narasimhan} and {Cao}},\n  year={2023},\n  booktitle={International Conference on Learning Representations},\n  url={https://arxiv.org/abs/2210.03629}\n}\n\n@inproceedings{shinn2023reflexion,\n  title={Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author={{Shinn} and {Cassano} and {Berman} and {Gopinath} and {Narasimhan} and {Yao}},\n  year={2023},\n  booktitle={Advances in Neural Information Processing Systems},\n  url={https://arxiv.org/abs/2303.11366}\n}\n\n@inproceedings{kim2025coex,\n  title={{CoEx} -- Co-evolving World-model and Exploration},\n  author={{Kim} and {Hwang}},\n  year={2025},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},\n  url={https://arxiv.org/abs/2507.22281}\n}\n\n@article{eef2025,\n  title={Exploring Expert Failures Improves LLM Agent Tuning},\n  author={{Lan} and {Bai} and {Cheng} and {Wang} and Others},\n  year={2025},\n  journal={arXiv preprint arXiv:2504.13145},\n  url={https://arxiv.org/abs/2504.13145}\n}\n\n@article{agentdebug2025,\n  title={Where LLM Agents Fail and How They can Learn From Failures},\n  author={{Zhu} and {Liu} and {Li} and {Tian} and Others},\n  year={2025},\n  journal={arXiv preprint arXiv:2509.25370},\n  url={https://arxiv.org/abs/2509.25370}\n}\n\n@inproceedings{bengio2009curriculum,\n  title={Curriculum Learning},\n  author={{Bengio} and {Louradour} and {Collobert} and {Weston}},\n  year={2009},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@inproceedings{madry2018adversarial,\n  title={Towards Deep Learning Models Resistant to Adversarial Attacks},\n  author={{Madry} and {Makelov} and {Schmidt} and {Tsipras} and {Vladu}},\n  year={2018},\n  booktitle={International Conference on Learning Representations}\n}\n",
      "numLines": 232,
      "startLine": 1,
      "totalLines": 232
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AkEjQREeD4vcr5H5zMFqjy`</summary>

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
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "223aa918-0a1d-4fc8-a57e-2089daf816f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rGKxAQurTAM5vTV1TwHG7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13123,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13123
      },
      "output_tokens": 27,
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

_source line 9 · 2026-05-15T03:50:18.868Z_

<details><summary>↩ Tool result · `toolu_01AkEjQREeD4vcr5H5zMFqjy`</summary>

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
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "30c0457b-c369-4e27-b3f3-8847d51c2757",
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

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the 4 WebSearches in parallel for the 3 Various Authors entries and the Reflexion author verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "dd21b385-91c0-4f53-8455-866ea33710e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKyTs5HgBkaUFEF7Limv6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4241,
      "cache_read_input_tokens": 24964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4241
      },
      "output_tokens": 17,
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

Running 4 WebSearches in parallel to fill in the missing authors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "8c753978-4399-4524-8f78-d71d4d304804",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKyTs5HgBkaUFEF7Limv6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4241,
      "cache_read_input_tokens": 24964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4241
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TBuR9unPauNrXQGGGmQ5Dn`</summary>

```json
{
  "query": "Beyond Clean Data Exploring Effects Label Noise Object Detection Performance 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "de917c06-3b8c-49b0-9cdf-60da11625f10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKyTs5HgBkaUFEF7Limv6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4241,
      "cache_read_input_tokens": 24964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4241
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LXkr8zSrMz985tGbWFwEcE`</summary>

```json
{
  "query": "AgentHER Hindsight Experience Replay LLM Agent Trajectory Relabeling arXiv 2603.21357 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "b6092e2b-ae2b-4c55-9c39-2e3753963b44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKyTs5HgBkaUFEF7Limv6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4241,
      "cache_read_input_tokens": 24964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4241
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_014A4LsrUnypiLgEBdH7R9Qv`</summary>

```json
{
  "query": "Agent Planning with World Knowledge Model NeurIPS 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "38bf6d44-1a84-4d4f-958b-34bd64654309",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKyTs5HgBkaUFEF7Limv6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4241,
      "cache_read_input_tokens": 24964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4241
      },
      "output_tokens": 17,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UmFEphqG2PWk3ThdQ9umYn`</summary>

```json
{
  "query": "Reflexion Language Agents Verbal Reinforcement Learning arXiv 2303.11366 authors Shinn Cassano"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "cff13363-0024-4cb8-a074-93e4f5f061d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKyTs5HgBkaUFEF7Limv6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4241,
      "cache_read_input_tokens": 24964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4241
      },
      "output_tokens": 17,
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

_source line 16 · 2026-05-15T03:50:27.893Z_

<details><summary>↩ Tool result · `toolu_01TBuR9unPauNrXQGGGmQ5Dn`</summary>

```text
Web search results for query: "Beyond Clean Data Exploring Effects Label Noise Object Detection Performance 2024 authors"

Links: [{"title":"Beyond clean data: Exploring the effects of label noise on object detection performance - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095070512401178X"},{"title":"Beyond clean data: Exploring the effects of label noise on object detection performance | Request PDF","url":"https://www.researchgate.net/publication/384538905_Beyond_clean_data_Exploring_the_effects_of_label_noise_on_object_detection_performance"},{"title":"Beyond clean data: : Exploring the effects of label noise on ...","url":"https://dl.acm.org/doi/10.1016/j.knosys.2024.112544"},{"title":"Exploring the effects of label noise on object detection performance","url":"https://dl.acm.org/doi/abs/10.1016/j.knosys.2024.112544"},{"title":"Effect of Label Noise on Robustness of Deep Neural Network Object Detectors | Request PDF","url":"https://www.researchgate.net/publication/354111821_Effect_of_Label_Noise_on_Robustness_of_Deep_Neural_Network_Object_Detectors"},{"title":"Deep learning with noisy labels: exploring techniques and ...","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7484266/"},{"title":"ProtoSimi: label correction for fine-grained visual categorization | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-023-06313-0"},{"title":"Benchmarking Label Noise in Instance Segmentation: Spatial Noise Matters","url":"https://arxiv.org/html/2406.10891v2"},{"title":"Identifying and Mitigating Label Noise in Deep Learning for Image Classification | MDPI","url":"https://www.mdpi.com/2227-7080/13/4/132"},{"title":"Impact of Noisy Labels on Dental Deep Learning—Calculus Detection on Bitewing Radiographs - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10179289/"}]

Based on the search results, I found the paper you're looking for:

**"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance"** (2024)

The authors are:
- Agostinho Freire
- Leandro H. de S. Silva
- João V.R. de Andrade
- Bruno J. T. Fernandes

The paper analyzes the influence of noisy labels using three renowned object detection frameworks: YOLOv5, Faster R-CNN, and YOLOv8, alongside established datasets: MS COCO, VOC, and ExDARK, with additional experiments using the UVM dataset for domain-specific tasks in dense object scenarios.

The paper was published in October 2024 in the journal Knowledge-Based Systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "05b0c7e3-74a1-48fc-91d6-90c0de60fc3b",
  "tool_use_result": {
    "query": "Beyond Clean Data Exploring Effects Label Noise Object Detection Performance 2024 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_016FgttkraqFTBkSiMT99YMj",
        "content": [
          {
            "title": "Beyond clean data: Exploring the effects of label noise on object detection performance - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S095070512401178X"
          },
          {
            "title": "Beyond clean data: Exploring the effects of label noise on object detection performance | Request PDF",
            "url": "https://www.researchgate.net/publication/384538905_Beyond_clean_data_Exploring_the_effects_of_label_noise_on_object_detection_performance"
          },
          {
            "title": "Beyond clean data: : Exploring the effects of label noise on ...",
            "url": "https://dl.acm.org/doi/10.1016/j.knosys.2024.112544"
          },
          {
            "title": "Exploring the effects of label noise on object detection performance",
            "url": "https://dl.acm.org/doi/abs/10.1016/j.knosys.2024.112544"
          },
          {
            "title": "Effect of Label Noise on Robustness of Deep Neural Network Object Detectors | Request PDF",
            "url": "https://www.researchgate.net/publication/354111821_Effect_of_Label_Noise_on_Robustness_of_Deep_Neural_Network_Object_Detectors"
          },
          {
            "title": "Deep learning with noisy labels: exploring techniques and ...",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7484266/"
          },
          {
            "title": "ProtoSimi: label correction for fine-grained visual categorization | Machine Learning | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10994-023-06313-0"
          },
          {
            "title": "Benchmarking Label Noise in Instance Segmentation: Spatial Noise Matters",
            "url": "https://arxiv.org/html/2406.10891v2"
          },
          {
            "title": "Identifying and Mitigating Label Noise in Deep Learning for Image Classification | MDPI",
            "url": "https://www.mdpi.com/2227-7080/13/4/132"
          },
          {
            "title": "Impact of Noisy Labels on Dental Deep Learning—Calculus Detection on Bitewing Radiographs - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10179289/"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**\"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"** (2024)\n\nThe authors are:\n- Agostinho Freire\n- Leandro H. de S. Silva\n- João V.R. de Andrade\n- Bruno J. T. Fernandes\n\nThe paper analyzes the influence of noisy labels using three renowned object detection frameworks: YOLOv5, Faster R-CNN, and YOLOv8, alongside established datasets: MS COCO, VOC, and ExDARK, with additional experiments using the UVM dataset for domain-specific tasks in dense object scenarios.\n\nThe paper was published in October 2024 in the journal Knowledge-Based Systems."
    ],
    "durationSeconds": 4.428461831999999
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T03:50:28.858Z_

<details><summary>↩ Tool result · `toolu_014A4LsrUnypiLgEBdH7R9Qv`</summary>

```text
Web search results for query: "Agent Planning with World Knowledge Model NeurIPS 2024 authors"

Links: [{"title":"GitHub - zjunlp/WKM: [NeurIPS 2024] Agent Planning with World Knowledge Model · GitHub","url":"https://github.com/zjunlp/WKM"},{"title":"Agent Planning with World Knowledge Model","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf"},{"title":"Agent Planning with World Knowledge Model","url":"https://neurips.cc/media/neurips-2024/Slides/93977.pdf"},{"title":"[2405.14205] Agent Planning with World Knowledge Model","url":"https://arxiv.org/abs/2405.14205"},{"title":"Agent Planning with World Knowledge Model","url":"https://knowledge-nlp.github.io/acl2024/papers/20_agent_planning_with_world_know.pdf"},{"title":"Agent planning with world knowledge model | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3741562"},{"title":"Agent Planning with World Knowledge Model | OpenReview","url":"https://openreview.net/forum?id=j6kJSS9O6I"},{"title":"NeurIPS Poster Agent Planning with World Knowledge Model","url":"https://neurips.cc/virtual/2024/poster/93977"},{"title":"Agent Planning with World Knowledge Model | Request PDF","url":"https://www.researchgate.net/publication/397201478_Agent_Planning_with_World_Knowledge_Model"},{"title":"Agent Planning with World Knowledge Model","url":"https://papers.nips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf"}]

Based on the search results, I found the authors of the "Agent Planning with World Knowledge Model" paper from NeurIPS 2024:

The authors are: Shuofei Qiao, Runnan Fang, Ningyu Zhang, Yuqi Zhu, Xiang Chen, Shumin Deng, Yong Jiang, Pengjun Xie, Fei Huang, and Huajun Chen.

The paper was presented at the 38th Conference on Neural Information Processing Systems (NeurIPS 2024), and introduces a parametric World Knowledge Model (WKM) to facilitate agent planning by imitating humans' mental world knowledge model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "eb568d7c-ecb0-41ec-bf44-897c201e57a2",
  "tool_use_result": {
    "query": "Agent Planning with World Knowledge Model NeurIPS 2024 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N7r6dkz5eP7gNpoLRhiYHP",
        "content": [
          {
            "title": "GitHub - zjunlp/WKM: [NeurIPS 2024] Agent Planning with World Knowledge Model · GitHub",
            "url": "https://github.com/zjunlp/WKM"
          },
          {
            "title": "Agent Planning with World Knowledge Model",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf"
          },
          {
            "title": "Agent Planning with World Knowledge Model",
            "url": "https://neurips.cc/media/neurips-2024/Slides/93977.pdf"
          },
          {
            "title": "[2405.14205] Agent Planning with World Knowledge Model",
            "url": "https://arxiv.org/abs/2405.14205"
          },
          {
            "title": "Agent Planning with World Knowledge Model",
            "url": "https://knowledge-nlp.github.io/acl2024/papers/20_agent_planning_with_world_know.pdf"
          },
          {
            "title": "Agent planning with world knowledge model | Proceedings of the 38th International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3737916.3741562"
          },
          {
            "title": "Agent Planning with World Knowledge Model | OpenReview",
            "url": "https://openreview.net/forum?id=j6kJSS9O6I"
          },
          {
            "title": "NeurIPS Poster Agent Planning with World Knowledge Model",
            "url": "https://neurips.cc/virtual/2024/poster/93977"
          },
          {
            "title": "Agent Planning with World Knowledge Model | Request PDF",
            "url": "https://www.researchgate.net/publication/397201478_Agent_Planning_with_World_Knowledge_Model"
          },
          {
            "title": "Agent Planning with World Knowledge Model",
            "url": "https://papers.nips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, I found the authors of the \"Agent Planning with World Knowledge Model\" paper from NeurIPS 2024:\n\nThe authors are: Shuofei Qiao, Runnan Fang, Ningyu Zhang, Yuqi Zhu, Xiang Chen, Shumin Deng, Yong Jiang, Pengjun Xie, Fei Huang, and Huajun Chen.\n\nThe paper was presented at the 38th Conference on Neural Information Processing Systems (NeurIPS 2024), and introduces a parametric World Knowledge Model (WKM) to facilitate agent planning by imitating humans' mental world knowledge model."
    ],
    "durationSeconds": 3.9730459969999994
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T03:50:30.191Z_

<details><summary>↩ Tool result · `toolu_01LXkr8zSrMz985tGbWFwEcE`</summary>

```text
Web search results for query: "AgentHER Hindsight Experience Replay LLM Agent Trajectory Relabeling arXiv 2603.21357 authors"

Links: [{"title":"[2603.21357] AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling","url":"https://arxiv.org/abs/2603.21357"},{"title":"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling","url":"https://arxiv.org/html/2603.21357"},{"title":"Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting","url":"https://arxiv.org/html/2510.10304v1"},{"title":"[2510.10304] Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting","url":"https://arxiv.org/abs/2510.10304"},{"title":"Hindsight Experience Replay | Request PDF","url":"https://www.researchgate.net/publication/318224066_Hindsight_Experience_Replay"},{"title":"Spinning Straw into Gold: Relabeling LLM Agent Trajectories in Hindsight for Successful Demonstrations | OpenReview","url":"https://openreview.net/forum?id=QNfmqMSR7r"},{"title":"Sample-Efficient Online Learning in LM Agents via ...","url":"https://arxiv.org/pdf/2510.10304"},{"title":"HER — Stable Baselines3 2.9.0a2 documentation","url":"https://stable-baselines3.readthedocs.io/en/master/modules/her.html"},{"title":"[2306.16061] MRHER: Model-based Relay Hindsight Experience Replay for Sequential Object Manipulation Tasks with Sparse Rewards","url":"https://arxiv.org/abs/2306.16061"},{"title":"[PDF] Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sample-Efficient-Online-Learning-in-LM-Agents-via-Hu-Durme/980544498065af165ad7bb34c9a1a46cbdccce57"}]

Based on the search results, I found the paper you were looking for. AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling (arXiv:2603.21357) is authored by Liang Ding from Alibaba Group.

The paper presents a framework that recovers lost training signals by adapting the Hindsight Experience Replay (HER) principle to natural-language agent trajectories for offline data augmentation. It realizes this through a four-stage pipeline: failure classification, outcome extraction, LLM-guided prompt relabeling with confidence gating, and data packaging.

The key contribution is that a trajectory that fails goal A is often a correct demonstration for some achievable alternative goal B. On WebArena and ToolBench benchmarks, AgentHER improves over success-only SFT by +7.1-11.7 percentage points across four model families (GPT-4o, Qwen2.5-72B/7B, LLaMA-3.1-8B).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "3230afcc-bce3-4ade-9ad3-264248275a6a",
  "tool_use_result": {
    "query": "AgentHER Hindsight Experience Replay LLM Agent Trajectory Relabeling arXiv 2603.21357 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_015AnEWsiRX95w9U2XAwTrwW",
        "content": [
          {
            "title": "[2603.21357] AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling",
            "url": "https://arxiv.org/abs/2603.21357"
          },
          {
            "title": "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling",
            "url": "https://arxiv.org/html/2603.21357"
          },
          {
            "title": "Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting",
            "url": "https://arxiv.org/html/2510.10304v1"
          },
          {
            "title": "[2510.10304] Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting",
            "url": "https://arxiv.org/abs/2510.10304"
          },
          {
            "title": "Hindsight Experience Replay | Request PDF",
            "url": "https://www.researchgate.net/publication/318224066_Hindsight_Experience_Replay"
          },
          {
            "title": "Spinning Straw into Gold: Relabeling LLM Agent Trajectories in Hindsight for Successful Demonstrations | OpenReview",
            "url": "https://openreview.net/forum?id=QNfmqMSR7r"
          },
          {
            "title": "Sample-Efficient Online Learning in LM Agents via ...",
            "url": "https://arxiv.org/pdf/2510.10304"
          },
          {
            "title": "HER — Stable Baselines3 2.9.0a2 documentation",
            "url": "https://stable-baselines3.readthedocs.io/en/master/modules/her.html"
          },
          {
            "title": "[2306.16061] MRHER: Model-based Relay Hindsight Experience Replay for Sequential Object Manipulation Tasks with Sparse Rewards",
            "url": "https://arxiv.org/abs/2306.16061"
          },
          {
            "title": "[PDF] Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Sample-Efficient-Online-Learning-in-LM-Agents-via-Hu-Durme/980544498065af165ad7bb34c9a1a46cbdccce57"
          }
        ]
      },
      "Based on the search results, I found the paper you were looking for. AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling (arXiv:2603.21357) is authored by Liang Ding from Alibaba Group.\n\nThe paper presents a framework that recovers lost training signals by adapting the Hindsight Experience Replay (HER) principle to natural-language agent trajectories for offline data augmentation. It realizes this through a four-stage pipeline: failure classification, outcome extraction, LLM-guided prompt relabeling with confidence gating, and data packaging.\n\nThe key contribution is that a trajectory that fails goal A is often a correct demonstration for some achievable alternative goal B. On WebArena and ToolBench benchmarks, AgentHER improves over success-only SFT by +7.1-11.7 percentage points across four model families (GPT-4o, Qwen2.5-72B/7B, LLaMA-3.1-8B)."
    ],
    "durationSeconds": 6.233432255999999
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T03:50:30.467Z_

<details><summary>↩ Tool result · `toolu_01UmFEphqG2PWk3ThdQ9umYn`</summary>

```text
Web search results for query: "Reflexion Language Agents Verbal Reinforcement Learning arXiv 2303.11366 authors Shinn Cassano"

Links: [{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://arxiv.org/pdf/2303.11366"},{"title":"Reflexion: language agents with verbal reinforcement learning | OpenReview","url":"https://openreview.net/forum?id=vAElhFcKW6"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning. Continue this conversation at https://readfm.vercel.app?gist=d54ea52a1875f82cf2221ec6ca253c07 · GitHub","url":"https://gist.github.com/m0o0scar/d54ea52a1875f82cf2221ec6ca253c07"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2303.11366v4"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/html/2303.11366"},{"title":"Building a Self-Correcting AI: A Deep Dive into the Reflexion Agent with LangChain and LangGraph | by Vi Q. Ha | Medium","url":"https://medium.com/@vi.ha.engr/building-a-self-correcting-ai-a-deep-dive-into-the-reflexion-agent-with-langchain-and-langgraph-ae2b1ddb8c3b"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://www.emergentmind.com/papers/2303.11366"},{"title":"[2303.11366v3] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366v3"}]

I found the paper you were looking for. Here are the key details:

**Paper:** Reflexion: Language Agents with Verbal Reinforcement Learning

**Authors:** Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao

**ArXiv ID:** 2303.11366

**Main Contribution:** Reflexion is a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials.

**Problem Addressed:** It remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning.

The paper proposes an innovative approach where environmental feedback is converted into verbal feedback in the form of a textual summary, which is then added as additional context for the LLM agent in the next episode. This self-reflective feedback acts as a 'semantic' gradient signal by providing the agent with a concrete direction to improve upon.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "c7af240a-d9f6-4eed-a47f-533a66570cd4",
  "tool_use_result": {
    "query": "Reflexion Language Agents Verbal Reinforcement Learning arXiv 2303.11366 authors Shinn Cassano",
    "results": [
      {
        "tool_use_id": "srvtoolu_01McAVhDLkfCdT5HKEsinzHi",
        "content": [
          {
            "title": "[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://arxiv.org/abs/2303.11366"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn",
            "url": "https://arxiv.org/pdf/2303.11366"
          },
          {
            "title": "Reflexion: language agents with verbal reinforcement learning | OpenReview",
            "url": "https://openreview.net/forum?id=vAElhFcKW6"
          },
          {
            "title": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub",
            "url": "https://github.com/noahshinn/reflexion"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning. Continue this conversation at https://readfm.vercel.app?gist=d54ea52a1875f82cf2221ec6ca253c07 · GitHub",
            "url": "https://gist.github.com/m0o0scar/d54ea52a1875f82cf2221ec6ca253c07"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2303.11366v4"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://arxiv.org/html/2303.11366"
          },
          {
            "title": "Building a Self-Correcting AI: A Deep Dive into the Reflexion Agent with LangChain and LangGraph | by Vi Q. Ha | Medium",
            "url": "https://medium.com/@vi.ha.engr/building-a-self-correcting-ai-a-deep-dive-into-the-reflexion-agent-with-langchain-and-langgraph-ae2b1ddb8c3b"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://www.emergentmind.com/papers/2303.11366"
          },
          {
            "title": "[2303.11366v3] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://arxiv.org/abs/2303.11366v3"
          }
        ]
      },
      "I found the paper you were looking for. Here are the key details:\n\n**Paper:** Reflexion: Language Agents with Verbal Reinforcement Learning\n\n**Authors:** Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao\n\n**ArXiv ID:** 2303.11366\n\n**Main Contribution:** Reflexion is a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials.\n\n**Problem Addressed:** It remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning.\n\nThe paper proposes an innovative approach where environmental feedback is converted into verbal feedback in the form of a textual summary, which is then added as additional context for the LLM agent in the next episode. This self-reflective feedback acts as a 'semantic' gradient signal by providing the agent with a concrete direction to improve upon."
    ],
    "durationSeconds": 5.452069797999998
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Let me gather the search results:

1. **beyond_clean_data2024**: Authors are Agostinho Freire, Leandro H. de S. Silva, João V.R. de Andrade, Bruno J. T. Fernandes. Published in Knowledge-Based Systems (not ScienceDirect).

2. **agentHER2025**: Author is Liang Ding from Alibaba Group. The search result only mentions Liang Ding. Let me search for more complete author list.


3. **wkm2024alfworld**: The authors include Shuofei Qiao, Runnan Fang, Ningyu Zhang, Yuqi Zhu, Xiang Chen, Shumin Deng, Yong Jiang, Pengjun Xie, Fei Huang, and Huajun Chen. 4. **shinn2023reflexion**: The actual author list includes Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao—so Berman is indeed listed as an author.

Wait, I need to check the task instructions again. The task notes that Berman shouldn't be in the author list according to the known data, but the WebSearch results from arXiv clearly show Berman as one of the authors. So the original task note was incorrect—Berman is actually part of the author list.

For the other papers, I'm realizing I only need to fix the capitalization of "and Others" to "and others" rather than searching for complete author lists. Let me focus on that correction instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "68788115-f6c4-4e7b-b2ef-038449ab468d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012g4CyKTbcGzbEYNWGxnadr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3540,
      "cache_read_input_tokens": 29205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3540
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

AgentHER search only returned "Liang Ding" — need more detail. Let me search specifically for the full author list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "bc59e513-2be5-4a2b-8b72-654b60378205",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012g4CyKTbcGzbEYNWGxnadr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3540,
      "cache_read_input_tokens": 29205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3540
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_014UG971GuNsRQTG2wWDDwev`</summary>

```json
{
  "query": "arxiv 2603.21357 AgentHER authors full list Liang Ding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "891dd49f-374c-4f96-969f-69afbc423204",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012g4CyKTbcGzbEYNWGxnadr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3540,
      "cache_read_input_tokens": 29205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3540
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

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0182Da2ddfc38oG9QhfG8wjU`</summary>

```json
{
  "query": "PALADIN Self-Correcting Language Model Agents Cure Tool-Failure arXiv 2509.25238 authors Vuddanti Shah"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "d7cb2686-a087-4a04-8b2a-1caeea3e26a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012g4CyKTbcGzbEYNWGxnadr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3540,
      "cache_read_input_tokens": 29205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3540
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DNTuiaR3t6fVUdNJ17nBtE`</summary>

```json
{
  "query": "\"Exploring Expert Failures Improves LLM Agent Tuning\" arXiv 2504.13145 authors Li-Cheng Lan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "822a9cfa-b0e1-414d-8feb-a61b6e59cbf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012g4CyKTbcGzbEYNWGxnadr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3540,
      "cache_read_input_tokens": 29205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3540
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MJtfMqsWg19ahYKf8BqG54`</summary>

```json
{
  "query": "\"Where LLM Agents Fail\" arXiv 2509.25370 authors Zhu Liu Li Tian agentdebug"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "4a93af05-3619-4f66-b898-681147614d3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012g4CyKTbcGzbEYNWGxnadr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3540,
      "cache_read_input_tokens": 29205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3540
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

_source line 26 · 2026-05-15T03:50:54.545Z_

<details><summary>↩ Tool result · `toolu_014UG971GuNsRQTG2wWDDwev`</summary>

```text
Web search results for query: "arxiv 2603.21357 AgentHER authors full list Liang Ding"

Links: [{"title":"[2603.21357] AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling","url":"https://arxiv.org/abs/2603.21357"},{"title":"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling","url":"https://arxiv.org/html/2603.21357"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=543&show=2000"},{"title":"[2603.04951] Retrieval-Augmented Generation with Covariate Time Series","url":"https://arxiv.org/abs/2603.04951"},{"title":"[2603.23822] How Vulnerable Are Edge LLMs?","url":"https://arxiv.org/abs/2603.23822"},{"title":"GitHub - WooooDyy/LLM-Agent-Paper-List: The paper list of the 86-page SCIS cover paper \"The Rise and Potential of Large Language Model Based Agents: A Survey\" by Zhiheng Xi et al. · GitHub","url":"https://github.com/WooooDyy/LLM-Agent-Paper-List"},{"title":"Towards a Science of Scaling Agent Systems (Google ...","url":"https://www.facebook.com/groups/DeepNetGroup/posts/2681070338952498/"},{"title":"my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily","url":"https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"},{"title":"[2603.21362] AdaRubric: Task-Adaptive Rubrics for LLM Agent Evaluation","url":"https://arxiv.org/abs/2603.21362"},{"title":"A Survey of Self-Evolving Agents What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence","url":"https://arxiv.org/html/2507.21046v4"}]

Based on the search results, I found information about the ArXiv paper 2603.21357 "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling."

The paper is authored by Liang Ding from Alibaba Group. However, the search results indicate that Liang Ding appears to be the sole author listed on this paper, at least in the available metadata shown in the search results.

If you need the complete list of all authors for this paper, I recommend visiting the full paper directly on ArXiv at https://arxiv.org/abs/2603.21357 or the HTML version at https://arxiv.org/html/2603.21357, where the complete author information should be displayed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "f82d9f96-a29f-46bb-aab6-89f4c0f8b7a1",
  "tool_use_result": {
    "query": "arxiv 2603.21357 AgentHER authors full list Liang Ding",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LDbapXdxNYFYLuRF5rjTzs",
        "content": [
          {
            "title": "[2603.21357] AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling",
            "url": "https://arxiv.org/abs/2603.21357"
          },
          {
            "title": "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling",
            "url": "https://arxiv.org/html/2603.21357"
          },
          {
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/recent?skip=543&show=2000"
          },
          {
            "title": "[2603.04951] Retrieval-Augmented Generation with Covariate Time Series",
            "url": "https://arxiv.org/abs/2603.04951"
          },
          {
            "title": "[2603.23822] How Vulnerable Are Edge LLMs?",
            "url": "https://arxiv.org/abs/2603.23822"
          },
          {
            "title": "GitHub - WooooDyy/LLM-Agent-Paper-List: The paper list of the 86-page SCIS cover paper \"The Rise and Potential of Large Language Model Based Agents: A Survey\" by Zhiheng Xi et al. · GitHub",
            "url": "https://github.com/WooooDyy/LLM-Agent-Paper-List"
          },
          {
            "title": "Towards a Science of Scaling Agent Systems (Google ...",
            "url": "https://www.facebook.com/groups/DeepNetGroup/posts/2681070338952498/"
          },
          {
            "title": "my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily",
            "url": "https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"
          },
          {
            "title": "[2603.21362] AdaRubric: Task-Adaptive Rubrics for LLM Agent Evaluation",
            "url": "https://arxiv.org/abs/2603.21362"
          },
          {
            "title": "A Survey of Self-Evolving Agents What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence",
            "url": "https://arxiv.org/html/2507.21046v4"
          }
        ]
      },
      "Based on the search results, I found information about the ArXiv paper 2603.21357 \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling.\"\n\nThe paper is authored by Liang Ding from Alibaba Group. However, the search results indicate that Liang Ding appears to be the sole author listed on this paper, at least in the available metadata shown in the search results.\n\nIf you need the complete list of all authors for this paper, I recommend visiting the full paper directly on ArXiv at https://arxiv.org/abs/2603.21357 or the HTML version at https://arxiv.org/html/2603.21357, where the complete author information should be displayed."
    ],
    "durationSeconds": 4.495045556000004
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T03:50:58.058Z_

<details><summary>↩ Tool result · `toolu_0182Da2ddfc38oG9QhfG8wjU`</summary>

```text
Web search results for query: "PALADIN Self-Correcting Language Model Agents Cure Tool-Failure arXiv 2509.25238 authors Vuddanti Shah"

Links: [{"title":"[2509.25238] PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://arxiv.org/abs/2509.25238"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://arxiv.org/html/2509.25238v1"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure ...","url":"https://arxiv.org/pdf/2509.25238"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases | alphaXiv","url":"https://www.alphaxiv.org/abs/2509.25238"},{"title":"[PDF] PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases | Semantic Scholar","url":"https://www.semanticscholar.org/paper/PALADIN:-Self-Correcting-Language-Model-Agents-to-Vuddanti-Shah/9ae73fb066a4d577bce84c42ec285a05f0b24c46"},{"title":"(PDF) PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://www.researchgate.net/publication/396048240_PALADIN_Self-Correcting_Language_Model_Agents_to_Cure_Tool-Failure_Cases"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases - haebom","url":"https://slashpage.com/haebom/daily_arxiv?lang=en&tl=en&post=7916x82r8wqjj24kpyg3"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure ...","url":"https://www.aimodels.fyi/papers/arxiv/paladin-self-correcting-language-model-agents-cure"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure ...","url":"https://openreview.net/pdf/8cf404c11b619f3ff8809308181318756620f971.pdf"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://openreview.net/pdf?id=NVTtoO297p"}]

Based on the search results, here's what I found about the PALADIN paper:

## Overview

PALADIN is a generalizable framework for equipping language agents with robust failure recovery capabilities. It was published as a conference paper at ICLR 2026 and submitted to arXiv on September 25, 2025.

## Authors

The authors are Sri Vatsa Vuddanti, Aarav Shah, Satwik Kumar Chittiprolu, Tony Song, Sunishchal Dev, Kevin Zhu, and Maheep Chaudhary.

## Problem and Solution

Tool-augmented language agents frequently fail in real-world deployment due to tool malfunctions--timeouts, API exceptions, or inconsistent outputs--triggering cascading reasoning errors and task abandonment. Existing agent training pipelines optimize only for success trajectories, failing to expose models to the tool failures that dominate real-world usage.

PALADIN trains on 50,000+ recovery-annotated trajectories constructed via systematic failure injection and expert demonstrations on an enhanced ToolBench dataset. Training uses LoRA-based fine-tuning to retain base capabilities while injecting recovery competence.

## Inference Mechanism

At inference, PALADIN detects execution-time errors and retrieves the most similar case from a curated bank of 55+ failure exemplars aligned with ToolScan's taxonomy, then executes the corresponding recovery action.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "302cba34-a59a-46f6-b9e4-e9d4010a5886",
  "tool_use_result": {
    "query": "PALADIN Self-Correcting Language Model Agents Cure Tool-Failure arXiv 2509.25238 authors Vuddanti Shah",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PtcN6dQ9BGauuWumhT3GD3",
        "content": [
          {
            "title": "[2509.25238] PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases",
            "url": "https://arxiv.org/abs/2509.25238"
          },
          {
            "title": "PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases",
            "url": "https://arxiv.org/html/2509.25238v1"
          },
          {
            "title": "PALADIN: Self-Correcting Language Model Agents to Cure ...",
            "url": "https://arxiv.org/pdf/2509.25238"
          },
          {
            "title": "PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2509.25238"
          },
          {
            "title": "[PDF] PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/PALADIN:-Self-Correcting-Language-Model-Agents-to-Vuddanti-Shah/9ae73fb066a4d577bce84c42ec285a05f0b24c46"
          },
          {
            "title": "(PDF) PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases",
            "url": "https://www.researchgate.net/publication/396048240_PALADIN_Self-Correcting_Language_Model_Agents_to_Cure_Tool-Failure_Cases"
          },
          {
            "title": "PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases - haebom",
            "url": "https://slashpage.com/haebom/daily_arxiv?lang=en&tl=en&post=7916x82r8wqjj24kpyg3"
          },
          {
            "title": "PALADIN: Self-Correcting Language Model Agents to Cure ...",
            "url": "https://www.aimodels.fyi/papers/arxiv/paladin-self-correcting-language-model-agents-cure"
          },
          {
            "title": "PALADIN: Self-Correcting Language Model Agents to Cure ...",
            "url": "https://openreview.net/pdf/8cf404c11b619f3ff8809308181318756620f971.pdf"
          },
          {
            "title": "PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases",
            "url": "https://openreview.net/pdf?id=NVTtoO297p"
          }
        ]
      },
      "Based on the search results, here's what I found about the PALADIN paper:\n\n## Overview\n\nPALADIN is a generalizable framework for equipping language agents with robust failure recovery capabilities. It was published as a conference paper at ICLR 2026 and submitted to arXiv on September 25, 2025.\n\n## Authors\n\nThe authors are Sri Vatsa Vuddanti, Aarav Shah, Satwik Kumar Chittiprolu, Tony Song, Sunishchal Dev, Kevin Zhu, and Maheep Chaudhary.\n\n## Problem and Solution\n\nTool-augmented language agents frequently fail in real-world deployment due to tool malfunctions--timeouts, API exceptions, or inconsistent outputs--triggering cascading reasoning errors and task abandonment. Existing agent training pipelines optimize only for success trajectories, failing to expose models to the tool failures that dominate real-world usage.\n\nPALADIN trains on 50,000+ recovery-annotated trajectories constructed via systematic failure injection and expert demonstrations on an enhanced ToolBench dataset. Training uses LoRA-based fine-tuning to retain base capabilities while injecting recovery competence.\n\n## Inference Mechanism\n\nAt inference, PALADIN detects execution-time errors and retrieves the most similar case from a curated bank of 55+ failure exemplars aligned with ToolScan's taxonomy, then executes the corresponding recovery action."
    ],
    "durationSeconds": 7.0728586
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T03:50:58.798Z_

<details><summary>↩ Tool result · `toolu_01DNTuiaR3t6fVUdNJ17nBtE`</summary>

```text
Web search results for query: ""Exploring Expert Failures Improves LLM Agent Tuning" arXiv 2504.13145 authors Li-Cheng Lan"

Links: [{"title":"[2504.13145] Exploring Expert Failures Improves LLM Agent Tuning","url":"https://arxiv.org/abs/2504.13145"},{"title":"[2504.13145v1] Exploring Expert Failures Improves LLM Agent Tuning","url":"http://arxiv.org/abs/2504.13145v1"},{"title":"Paper page - Exploring Expert Failures Improves LLM Agent Tuning","url":"https://huggingface.co/papers/2504.13145"},{"title":"Exploring Expert Failures Improves LLM Agent Tuning","url":"https://www.alphaxiv.org/overview/2504.13145v1"},{"title":"Exploring Expert Failures Improves LLM Agent Tuning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/exploring-expert-failures-improves-llm-agent-tuning"},{"title":"[Literature Review] Exploring Expert Failures Improves LLM Agent Tuning","url":"https://www.themoonlight.io/en/review/exploring-expert-failures-improves-llm-agent-tuning"},{"title":"arXiv:2504.13145v2 [cs.AI] 18 Apr 2025","url":"https://arxiv.org/pdf/2504.13145"},{"title":"Exploring Expert Failures Improves LLM Agent Tuning | OpenReview","url":"https://openreview.net/forum?id=4fh0Z9nwjx"},{"title":"Exploring Expert Failures Improves LLM Agent Tuning | Read Paper on Bytez","url":"https://bytez.com/docs/arxiv/2504.13145/paper"},{"title":"Exploring Expert Failures - LLM Agent tuning #openai - YouTube","url":"https://www.youtube.com/watch?v=5bCje470-2E"}]

I found the paper! Here's what I found about "Exploring Expert Failures Improves LLM Agent Tuning" (arXiv 2504.13145):

**Paper Information:**
The paper is authored by Li-Cheng Lan, Andrew Bai, Minhao Cheng, Cho-Jui Hsieh, and Tianyi Zhou, submitted on April 17, 2025.

**Overview:**
The paper addresses how Large Language Models (LLMs) have shown tremendous potential as agents, excelling at tasks that require multiple rounds of reasoning and interactions.

**Problem Statement:**
Rejection Sampling Fine-Tuning (RFT) is an effective method for finetuning LLMs as agents that first imitates expert-generated successful trajectories and further improves agentic skills through iterative fine-tuning on successful, self-generated trajectories. However, since the expert (e.g., GPT-4) succeeds primarily on simpler subtasks and RFT inherently favors simpler scenarios, many complex subtasks remain unsolved and persistently out-of-distribution (OOD).

**Key Contribution:**
The paper introduces a novel approach called Exploring Expert Failures (EEF) to enhance the fine-tuning of Large Language Models (LLMs) for agent tasks. The core idea behind EEF is to leverage information from expert trajectories that resulted in failure, with the hypothesis that they contain valuable guidance, such as plans and key actions, that can improve exploration efficiency and the acquisition of critical skills.

You can access the full paper at https://arxiv.org/abs/2504.13145.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "481feced-849b-40fb-af6d-e4f640d9745a",
  "tool_use_result": {
    "query": "\"Exploring Expert Failures Improves LLM Agent Tuning\" arXiv 2504.13145 authors Li-Cheng Lan",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H2JV9W74LgA33eg2UWehY7",
        "content": [
          {
            "title": "[2504.13145] Exploring Expert Failures Improves LLM Agent Tuning",
            "url": "https://arxiv.org/abs/2504.13145"
          },
          {
            "title": "[2504.13145v1] Exploring Expert Failures Improves LLM Agent Tuning",
            "url": "http://arxiv.org/abs/2504.13145v1"
          },
          {
            "title": "Paper page - Exploring Expert Failures Improves LLM Agent Tuning",
            "url": "https://huggingface.co/papers/2504.13145"
          },
          {
            "title": "Exploring Expert Failures Improves LLM Agent Tuning",
            "url": "https://www.alphaxiv.org/overview/2504.13145v1"
          },
          {
            "title": "Exploring Expert Failures Improves LLM Agent Tuning | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/exploring-expert-failures-improves-llm-agent-tuning"
          },
          {
            "title": "[Literature Review] Exploring Expert Failures Improves LLM Agent Tuning",
            "url": "https://www.themoonlight.io/en/review/exploring-expert-failures-improves-llm-agent-tuning"
          },
          {
            "title": "arXiv:2504.13145v2 [cs.AI] 18 Apr 2025",
            "url": "https://arxiv.org/pdf/2504.13145"
          },
          {
            "title": "Exploring Expert Failures Improves LLM Agent Tuning | OpenReview",
            "url": "https://openreview.net/forum?id=4fh0Z9nwjx"
          },
          {
            "title": "Exploring Expert Failures Improves LLM Agent Tuning | Read Paper on Bytez",
            "url": "https://bytez.com/docs/arxiv/2504.13145/paper"
          },
          {
            "title": "Exploring Expert Failures - LLM Agent tuning #openai - YouTube",
            "url": "https://www.youtube.com/watch?v=5bCje470-2E"
          }
        ]
      },
      "I found the paper! Here's what I found about \"Exploring Expert Failures Improves LLM Agent Tuning\" (arXiv 2504.13145):\n\n**Paper Information:**\nThe paper is authored by Li-Cheng Lan, Andrew Bai, Minhao Cheng, Cho-Jui Hsieh, and Tianyi Zhou, submitted on April 17, 2025.\n\n**Overview:**\nThe paper addresses how Large Language Models (LLMs) have shown tremendous potential as agents, excelling at tasks that require multiple rounds of reasoning and interactions.\n\n**Problem Statement:**\nRejection Sampling Fine-Tuning (RFT) is an effective method for finetuning LLMs as agents that first imitates expert-generated successful trajectories and further improves agentic skills through iterative fine-tuning on successful, self-generated trajectories. However, since the expert (e.g., GPT-4) succeeds primarily on simpler subtasks and RFT inherently favors simpler scenarios, many complex subtasks remain unsolved and persistently out-of-distribution (OOD).\n\n**Key Contribution:**\nThe paper introduces a novel approach called Exploring Expert Failures (EEF) to enhance the fine-tuning of Large Language Models (LLMs) for agent tasks. The core idea behind EEF is to leverage information from expert trajectories that resulted in failure, with the hypothesis that they contain valuable guidance, such as plans and key actions, that can improve exploration efficiency and the acquisition of critical skills.\n\nYou can access the full paper at https://arxiv.org/abs/2504.13145."
    ],
    "durationSeconds": 6.2125914259999995
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T03:51:01.878Z_

<details><summary>↩ Tool result · `toolu_01MJtfMqsWg19ahYKf8BqG54`</summary>

```text
Web search results for query: ""Where LLM Agents Fail" arXiv 2509.25370 authors Zhu Liu Li Tian agentdebug"

Links: [{"title":"[2509.25370] Where LLM Agents Fail and How They can Learn From Failures","url":"https://arxiv.org/abs/2509.25370"},{"title":"WHERE LLM AGENTS FAIL AND HOW THEY CAN LEARN FROM FAILURES","url":"https://arxiv.org/pdf/2509.25370"},{"title":"Paper page - Where LLM Agents Fail and How They can Learn From Failures","url":"https://huggingface.co/papers/2509.25370"},{"title":"Where LLM Agents Fail and How They can Learn From Failures | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.25370v1"},{"title":"Where LLM Agents Fail and How They can Learn From Failures - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250925370Z/abstract"},{"title":"[Literature Review] Where LLM Agents Fail and How They can Learn From Failures","url":"https://www.themoonlight.io/en/review/where-llm-agents-fail-and-how-they-can-learn-from-failures"},{"title":"Where LLM Agents Fail and How They can Learn From ...","url":"https://www.researchgate.net/publication/396048725_Where_LLM_Agents_Fail_and_How_They_can_Learn_From_Failures"},{"title":"AgenTracer: Failure Attribution in LLM Systems","url":"https://www.emergentmind.com/papers/2509.03312"},{"title":"A System-Level Taxonomy for Reliable AI Applications","url":"https://arxiv.org/pdf/2511.19933"}]

I found the paper! Here's the information about the arXiv paper 2509.25370:

## Paper Details

**Title:** Where LLM Agents Fail and How They can Learn From Failures

**ArXiv ID:** 2509.25370

**Submission Date:** September 29, 2025

**Authors:** Kunlun Zhu, Zijia Liu, Bingxuan Li, Muxin Tian, Yingxuan Yang, Jiaxun Zhang, Pengrui Han, Qipeng Xie, Fuyang Cui, Weijia Zhang, Xiaoteng Ma, Xiaodong Yu, Gowtham Ramesh, Jialian Wu, Zicheng Liu, Pan Lu, James Zou, Jiaxuan You

## Key Contributions

The paper addresses three main contributions:

1. **AgentErrorTaxonomy:** A modular classification of failure modes spanning memory, reflection, planning, action, and system-level operations

2. **AgentErrorBench:** The first dataset of systematically annotated failure trajectories from ALFWorld, GAIA, and WebShop, grounding error analysis in real-world agent rollouts

3. **AgentDebug:** A debugging framework that isolates root-cause failures and provides corrective feedback, enabling agents to recover and iteratively improve

## Results

AgentDebug achieves 24% higher all-correct accuracy and 17% higher step accuracy compared to the strongest baseline, and yields up to 26% relative improvements in task success across ALFWorld, GAIA, and WebShop.

The code and data are available on GitHub at https://github.com/ulab-uiuc/AgentDebug.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "65c9571e-29b6-4ac5-a114-a9c298b5b43e",
  "tool_use_result": {
    "query": "\"Where LLM Agents Fail\" arXiv 2509.25370 authors Zhu Liu Li Tian agentdebug",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R29WKFyW89fSjVh2gPcyn7",
        "content": [
          {
            "title": "[2509.25370] Where LLM Agents Fail and How They can Learn From Failures",
            "url": "https://arxiv.org/abs/2509.25370"
          },
          {
            "title": "WHERE LLM AGENTS FAIL AND HOW THEY CAN LEARN FROM FAILURES",
            "url": "https://arxiv.org/pdf/2509.25370"
          },
          {
            "title": "Paper page - Where LLM Agents Fail and How They can Learn From Failures",
            "url": "https://huggingface.co/papers/2509.25370"
          },
          {
            "title": "Where LLM Agents Fail and How They can Learn From Failures | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2509.25370v1"
          },
          {
            "title": "Where LLM Agents Fail and How They can Learn From Failures - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250925370Z/abstract"
          },
          {
            "title": "[Literature Review] Where LLM Agents Fail and How They can Learn From Failures",
            "url": "https://www.themoonlight.io/en/review/where-llm-agents-fail-and-how-they-can-learn-from-failures"
          },
          {
            "title": "Where LLM Agents Fail and How They can Learn From ...",
            "url": "https://www.researchgate.net/publication/396048725_Where_LLM_Agents_Fail_and_How_They_can_Learn_From_Failures"
          },
          {
            "title": "AgenTracer: Failure Attribution in LLM Systems",
            "url": "https://www.emergentmind.com/papers/2509.03312"
          },
          {
            "title": "A System-Level Taxonomy for Reliable AI Applications",
            "url": "https://arxiv.org/pdf/2511.19933"
          }
        ]
      },
      "I found the paper! Here's the information about the arXiv paper 2509.25370:\n\n## Paper Details\n\n**Title:** Where LLM Agents Fail and How They can Learn From Failures\n\n**ArXiv ID:** 2509.25370\n\n**Submission Date:** September 29, 2025\n\n**Authors:** Kunlun Zhu, Zijia Liu, Bingxuan Li, Muxin Tian, Yingxuan Yang, Jiaxun Zhang, Pengrui Han, Qipeng Xie, Fuyang Cui, Weijia Zhang, Xiaoteng Ma, Xiaodong Yu, Gowtham Ramesh, Jialian Wu, Zicheng Liu, Pan Lu, James Zou, Jiaxuan You\n\n## Key Contributions\n\nThe paper addresses three main contributions:\n\n1. **AgentErrorTaxonomy:** A modular classification of failure modes spanning memory, reflection, planning, action, and system-level operations\n\n2. **AgentErrorBench:** The first dataset of systematically annotated failure trajectories from ALFWorld, GAIA, and WebShop, grounding error analysis in real-world agent rollouts\n\n3. **AgentDebug:** A debugging framework that isolates root-cause failures and provides corrective feedback, enabling agents to recover and iteratively improve\n\n## Results\n\nAgentDebug achieves 24% higher all-correct accuracy and 17% higher step accuracy compared to the strongest baseline, and yields up to 26% relative improvements in task success across ALFWorld, GAIA, and WebShop.\n\nThe code and data are available on GitHub at https://github.com/ulab-uiuc/AgentDebug."
    ],
    "durationSeconds": 8.865698411000006
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also check the AgentHER authors more carefully. The search didn't give me a full list beyond "Liang Ding". Let me try one more search or use WebFetch to get the actual arXiv page.

Actually, let me try fetching the arXiv page directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "99837a72-9012-4fa7-8e7d-69aa9b789d83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WmZCgtbnoydUaVXPoGFT4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4885,
      "cache_read_input_tokens": 32745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4885
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

_source line 31_

Need the full AgentHER author list. Let me fetch the arXiv page directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "53460575-7573-4584-956e-25b6922ce4f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WmZCgtbnoydUaVXPoGFT4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4885,
      "cache_read_input_tokens": 32745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4885
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

_source line 32_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XCkRhxDCr5Zn4xUDU25rPW`</summary>

```json
{
  "query": "select:WebFetch",
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
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "edb3a1ac-acd0-4e8b-9dd6-b69a3596fbfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WmZCgtbnoydUaVXPoGFT4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4885,
      "cache_read_input_tokens": 32745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4885
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

_source line 33 · 2026-05-15T03:51:06.751Z_

<details><summary>↩ Tool result · `toolu_01XCkRhxDCr5Zn4xUDU25rPW`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
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
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "77633fad-4389-4677-830a-995497b7e8e1",
  "tool_use_result": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WH6z9jKTdYkoS4cawxP8eD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.21357",
  "prompt": "List ALL authors of this paper exactly as shown on the page. Return just the author names, comma separated."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "162eee9c-adfb-41d1-9a47-2087ab128dd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6mEg3szZwTCGfbLXvU7PG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 37630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 706
      },
      "output_tokens": 63,
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

_source line 35 · 2026-05-15T03:51:11.673Z_

<details><summary>↩ Tool result · `toolu_01WH6z9jKTdYkoS4cawxP8eD`</summary>

```text
Based on the arXiv page content provided, the author listed for this paper is:

**Liang Ding**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "0255f58e-87a4-4899-ad23-159335fb158a",
  "tool_use_result": {
    "bytes": 47040,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the arXiv page content provided, the author listed for this paper is:\n\n**Liang Ding**",
    "durationMs": 1488,
    "url": "https://arxiv.org/abs/2603.21357"
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
So AgentHER has a single author: Liang Ding. The task said the audit report mentioned "Liang Ding et al." but it seems like it's just Liang Ding.

Let me also check the "beyond_clean_data2024" paper more carefully. The search said the journal is "Knowledge-Based Systems", and the authors are Agostinho Freire, Leandro H. de S. Silva, João V.R. de Andrade, Bruno J. T. Fernandes. Let me verify this is the correct paper by checking ScienceDirect.


The ISSN prefix in the ScienceDirect link confirms this is Knowledge-Based Systems, so I have the right journal and author names. I'll move forward with this information and check the literature_map.yaml next.

Now I'm going through each entry to identify what needs updating, starting with the author name formatting across several papers. I'm working through the BibTeX author name formatting conventions, particularly for Brazilian names with particles like "de". The standard approach is to place the particle with the last name, so names like "Leandro H. de S. Silva" should be formatted as `{de S. Silva, L. H.}` to follow the existing style in this file. I need to get the exact author names from the paper itself rather than guessing at the formatting, especially with the Portuguese naming conventions and particles like "de" that need proper BibTeX handling.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "acc3633e-f9ef-4d08-8041-735cf9f8fed3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcFrzgykg5X7MVAHjG25vh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 38336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
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

_source line 37_

Let me also verify the exact author names for the beyond_clean_data paper, and read the literature_map.yaml.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "65b7abb9-b850-4b19-9eb4-c9c7a390bfca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcFrzgykg5X7MVAHjG25vh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 38336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
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

_source line 38_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WUWfhjLhcSXdc5YnvJdDU5`</summary>

```json
{
  "url": "https://www.sciencedirect.com/science/article/abs/pii/S095070512401178X",
  "prompt": "List ALL author names exactly as shown on the page, comma separated. Also confirm the journal name."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "9961c682-8ba7-4603-b73b-7b9900813b8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcFrzgykg5X7MVAHjG25vh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 38336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
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

_source line 39 · 2026-05-15T03:51:42.260Z_

<details><summary>↩ Tool result · reported error · `toolu_01WUWfhjLhcSXdc5YnvJdDU5`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "19f15bf8-20e2-44e5-8f72-913cb5bdeaad",
  "tool_use_result": "Error: Request failed with status code 403"
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01TJjnqnz7ptUmFz6wzpiheW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "df9ace9e-18c2-4e0b-a226-5b0fadfe8de6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcFrzgykg5X7MVAHjG25vh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 38336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
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

_source line 41 · 2026-05-15T03:51:43.781Z_

<details><summary>↩ Tool result · `toolu_01TJjnqnz7ptUmFz6wzpiheW`</summary>

```text
1	# Literature Map: Dose-Response / Threshold Effects in Data Augmentation
2	# Updated: 2026-05-15
3	
4	entries:
5	  # === Category: dose-response / threshold ===
6	
7	  - id: rolnick2017robust
8	    title: "Deep Learning is Robust to Massive Label Noise"
9	    authors: "Rolnick, Veit, Belongie, Shavit"
10	    year: 2017
11	    venue: arXiv 1705.10694
12	    category: dose-response
13	    role: background
14	    key_finding: "DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin."
15	    relevance: "Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance."
16	
17	  - id: yuan2024early_stopping
18	    title: "Early Stopping Against Label Noise Without Validation Data"
19	    authors: "Yuan, Feng, Liu"
20	    year: 2024
21	    venue: ICLR 2024
22	    category: dose-response
23	    role: background
24	    key_finding: "Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training."
25	    relevance: "Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime."
26	
27	  - id: dohmatob2025collapse
28	    title: "Strong Model Collapse"
29	    authors: "Dohmatob, Feng, Subramonian, Kempe"
30	    year: 2025
31	    venue: ICLR 2025
32	    category: threshold
33	    role: background
34	    key_finding: "Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent)."
35	    relevance: "Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation."
36	
37	  - id: beyond_clean_data2024
38	    title: "Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance"
39	    authors: "Various"
40	    year: 2024
41	    venue: ScienceDirect
42	    category: dose-response
43	    role: background
44	    key_finding: "Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds."
45	    relevance: "Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior."
46	
47	  # === Category: error-injection / failure augmentation ===
48	
49	  - id: wang2024learning_from_failure
50	    title: "Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents"
51	    authors: "Wang, Li, Han, Zhang, Baldwin"
52	    year: 2024
53	    venue: arXiv 2402.11651
54	    category: error-injection
55	    role: evaluation
56	    key_finding: "Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured."
57	    relevance: "Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window."
58	
59	  - id: song2024eto
60	    title: "Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents"
61	    authors: "Song, Yin, Yue, Huang, Li, Lin"
62	    year: 2024
63	    venue: ACL 2024
64	    category: error-injection
65	    role: evaluation
66	    key_finding: "Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT."
67	    relevance: "Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures."
68	
69	  - id: paladin2025
70	    title: "PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases"
71	    authors: "Vuddanti, Shah et al."
72	    year: 2025
73	    venue: arXiv 2509.25238
74	    category: error-injection
75	    role: evaluation
76	    key_finding: "Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval."
77	    relevance: "Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories."
78	
79	  - id: agentHER2025
80	    title: "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling"
81	    authors: "Various"
82	    year: 2025
83	    venue: arXiv 2603.21357
84	    category: error-injection
85	    role: evaluation
86	    key_finding: "Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B."
87	    relevance: "Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach."
88	
89	  # === Category: data-mixing ===
90	
91	  - id: dong2024composition
92	    title: "How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition"
93	    authors: "Dong, Yuan et al."
94	    year: 2024
95	    venue: ACL 2024
96	    category: data-mixing
97	    role: background
98	    key_finding: "Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts."
99	    relevance: "Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven."
100	
101	  - id: ye2025mixing_laws
102	    title: "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance"
103	    authors: "Ye et al."
104	    year: 2025
105	    venue: ICLR 2025
106	    category: data-mixing
107	    role: background
108	    key_finding: "Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting."
109	    relevance: "Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing."
110	
111	  - id: li2025mixing_optimization
112	    title: "Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models"
113	    authors: "Li et al."
114	    year: 2025
115	    venue: ICML 2025
116	    category: data-mixing
117	    role: background
118	    key_finding: "SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale."
119	    relevance: "Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific."
120	
121	  - id: seddik2024synthetic_bound
122	    title: "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse"
123	    authors: "Seddik et al."
124	    year: 2024
125	    venue: arXiv 2404.05090
126	    category: data-mixing
127	    role: background
128	    key_finding: "Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high."
129	    relevance: "Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions."
130	
131	  # === Category: curriculum / quality threshold ===
132	
133	  - id: curriculum_robust2021
134	    title: "Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction"
135	    authors: "Zhou, Wang, Bilmes"
136	    year: 2021
137	    venue: ICLR 2021
138	    category: curriculum
139	    role: background
140	    key_finding: "Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively."
141	    relevance: "Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity."
142	
143	  - id: agentprm2025
144	    title: "Process Reward Models for LLM Agents: Practical Framework and Directions"
145	    authors: "Choudhury"
146	    year: 2025
147	    venue: arXiv 2502.10325
148	    category: curriculum
149	    role: evaluation
150	    key_finding: "Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone."
151	    relevance: "ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search."
152	
153	  - id: wkm2024alfworld
154	    title: "Agent Planning with World Knowledge Model"
155	    authors: "Various"
156	    year: 2024
157	    venue: NeurIPS 2024
158	    category: curriculum
159	    role: evaluation
160	    key_finding: "World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting."
161	    relevance: "ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation."
162	
163	  # === Category: training-dynamics / memorization ===
164	
165	  - id: arpit2017memorization
166	    title: "A Closer Look at Memorization in Deep Networks"
167	    authors: "Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien"
168	    year: 2017
169	    venue: ICML 2017
170	    category: training-dynamics
171	    role: background
172	    key_finding: "DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient."
173	    relevance: "Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization."
174	
175	  - id: liu2020early_learning_reg
176	    title: "Early-Learning Regularization Prevents Memorization of Noisy Labels"
177	    authors: "Liu, Niles-Weed, Razavian, Fernandez-Granda"
178	    year: 2020
179	    venue: NeurIPS 2020
180	    category: training-dynamics
181	    role: background
182	    key_finding: "Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window."
183	    relevance: "Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap."
184	
185	  - id: zhou2023lima
186	    title: "LIMA: Less Is More for Alignment"
187	    authors: "Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy"
188	    year: 2023
189	    venue: NeurIPS 2023
190	    category: training-dynamics
191	    role: background
192	    key_finding: "Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices."
193	    relevance: "Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability."
194	
195	  - id: luo2023catastrophic_forgetting
196	    title: "An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning"
197	    authors: "Luo, Yang, Meng, Li, Zhou, Zhang"
198	    year: 2023
199	    venue: arXiv 2308.08747
200	    category: training-dynamics
201	    role: background
202	    key_finding: "SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions."
203	    relevance: "Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability."
204	
205	  - id: longpre2020augmentation
206	    title: "How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?"
207	    authors: "Longpre, Wang, DuBois"
208	    year: 2020
209	    venue: Findings of EMNLP 2020
210	    category: training-dynamics
211	    role: background
212	    key_finding: "Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift."
213	    relevance: "Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning."
214	
215	  # === Category: training-instability ===
216	
217	  - id: mccoy2020seeds
218	    title: "BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance"
219	    authors: "McCoy, Min, Linzen"
220	    year: 2020
221	    venue: "BlackboxNLP Workshop at EMNLP 2020"
222	    category: training-instability
223	    role: background
224	    key_finding: "Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization."
225	    relevance: "与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity"
226	
227	  - id: mosbach2021stability
228	    title: "On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines"
229	    authors: "Mosbach, Andriushchenko, Klakow"
230	    year: 2021
231	    venue: "ICLR 2021"
232	    category: training-instability
233	    role: background
234	    key_finding: "BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。"
235	    relevance: "fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training"
236	
237	  - id: damour2022underspecification
238	    title: "Underspecification Presents Challenges for Credibility in Modern Machine Learning"
239	    authors: "D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al."
240	    year: 2022
241	    venue: "Journal of Machine Learning Research, Vol. 23, No. 226"
242	    category: training-instability
243	    role: background
244	    key_finding: "ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。"
245	    relevance: "我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现"
246	
247	  # === Category: alfworld-methods ===
248	
249	  - id: shridhar2021alfworld
250	    title: "ALFWorld: Aligning Text and Embodied Environments for Interactive Learning"
251	    authors: "Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht"
252	    year: 2021
253	    venue: "ICLR 2021"
254	    arxiv: "2010.03768"
255	    category: alfworld-methods
256	    role: evaluation
257	    key_finding: "Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding."
258	    relevance: "我们的实验环境；134 tasks across 6 task types benchmark"
259	
260	  - id: yao2023react
261	    title: "ReAct: Synergizing Reasoning and Acting in Language Models"
262	    authors: "Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao"
263	    year: 2023
264	    venue: "ICLR 2023"
265	    arxiv: "2210.03629"
266	    category: alfworld-methods
267	    role: evaluation
268	    key_finding: "Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial)."
269	    relevance: "我们使用的 prompting paradigm（ReAct format）"
270	
271	  - id: shinn2023reflexion
272	    title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
273	    authors: "Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao"
274	    year: 2023
275	    venue: "NeurIPS 2023"
276	    arxiv: "2303.11366"
277	    category: alfworld-methods
278	    role: evaluation
279	    key_finding: "Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates."
280	    relevance: "Inference-time reflection 成功 where training-time injection 失败——对比 key point"
281	
282	  - id: kim2025coex
283	    title: "CoEx -- Co-evolving World-model and Exploration"
284	    authors: "Kim, Hwang"
285	    year: 2025
286	    venue: "Findings of EMNLP 2025"
287	    arxiv: "2507.22281"
288	    category: alfworld-methods
289	    role: evaluation
290	    key_finding: "Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld."
291	    relevance: "ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法"
292	
293	  # === Category: error-injection (补充) ===
294	
295	  - id: eef2025
296	    title: "Exploring Expert Failures Improves LLM Agent Tuning"
297	    authors: "Lan, Bai, Cheng, Wang et al."
298	    year: 2025
299	    venue: "arXiv 2504.13145"
300	    category: error-injection
301	    role: evaluation
302	    key_finding: "从失败 expert trajectories 中提取有益 actions（plans、key actions），用于引导 agent exploration，WebShop SOTA 0.81，SciWorld 81/100。"
303	    relevance: "从失败中提取正向信号（非注入负信号），成功 on WebShop。与我们的直接注入形成对比——方向相反的 failure utilization。"
304	
305	  - id: agentdebug2025
306	    title: "Where LLM Agents Fail and How They can Learn From Failures"
307	    authors: "Zhu, Liu, Li, Tian et al."
308	    year: 2025
309	    venue: "arXiv 2509.25370"
310	    category: error-injection
311	    role: evaluation
312	    key_finding: "5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。"
313	    relevance: "ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。"
314	
315	  # === Category: data-mixing / curriculum (补充) ===
316	
317	  - id: bengio2009curriculum
318	    title: "Curriculum Learning"
319	    authors: "Bengio, Louradour, Collobert, Weston"
320	    year: 2009
321	    venue: "ICML 2009"
322	    category: curriculum
323	    role: background
324	    key_finding: "按难度递增顺序呈现训练样本可加速收敛并改善非凸优化的局部最优质量；curriculum 本质是一种 continuation method。"
325	    relevance: "Curriculum learning 中 difficult example proportion 的 threshold 概念与我们的 dose-response 阈值平行——训练数据中困难/噪声样本超过阈值后性能崩溃"
326	
327	  - id: madry2018adversarial
328	    title: "Towards Deep Learning Models Resistant to Adversarial Attacks"
329	    authors: "Madry, Makelov, Schmidt, Tsipras, Vladu"
330	    year: 2018
331	    venue: "ICLR 2018"
332	    category: data-mixing
333	    role: background
334	    key_finding: "基于 PGD 的 adversarial training 通过 robust optimization 框架显著提升对抗鲁棒性，但以 clean accuracy 下降为代价。"
335	    relevance: "Adversarial training 的 accuracy-robustness tradeoff 是 dose-response 型——增加 adversarial perturbation 强度提升鲁棒性但降低 clean accuracy，与我们的 injection ratio vs clean eval tradeoff 结构相似"
336	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "f5b608c3-0244-44e8-870c-1fc42f7d1f1f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
      "content": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Various\"\n    year: 2024\n    venue: ScienceDirect\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n\n  # === Category: alfworld-methods ===\n\n  - id: shridhar2021alfworld\n    title: \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\"\n    authors: \"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    arxiv: \"2010.03768\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\"\n    relevance: \"我们的实验环境；134 tasks across 6 task types benchmark\"\n\n  - id: yao2023react\n    title: \"ReAct: Synergizing Reasoning and Acting in Language Models\"\n    authors: \"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.03629\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\"\n    relevance: \"我们使用的 prompting paradigm（ReAct format）\"\n\n  - id: shinn2023reflexion\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2303.11366\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\"\n    relevance: \"Inference-time reflection 成功 where training-time injection 失败——对比 key point\"\n\n  - id: kim2025coex\n    title: \"CoEx -- Co-evolving World-model and Exploration\"\n    authors: \"Kim, Hwang\"\n    year: 2025\n    venue: \"Findings of EMNLP 2025\"\n    arxiv: \"2507.22281\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\"\n    relevance: \"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\"\n\n  # === Category: error-injection (补充) ===\n\n  - id: eef2025\n    title: \"Exploring Expert Failures Improves LLM Agent Tuning\"\n    authors: \"Lan, Bai, Cheng, Wang et al.\"\n    year: 2025\n    venue: \"arXiv 2504.13145\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"从失败 expert trajectories 中提取有益 actions（plans、key actions），用于引导 agent exploration，WebShop SOTA 0.81，SciWorld 81/100。\"\n    relevance: \"从失败中提取正向信号（非注入负信号），成功 on WebShop。与我们的直接注入形成对比——方向相反的 failure utilization。\"\n\n  - id: agentdebug2025\n    title: \"Where LLM Agents Fail and How They can Learn From Failures\"\n    authors: \"Zhu, Liu, Li, Tian et al.\"\n    year: 2025\n    venue: \"arXiv 2509.25370\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。\"\n    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"\n\n  # === Category: data-mixing / curriculum (补充) ===\n\n  - id: bengio2009curriculum\n    title: \"Curriculum Learning\"\n    authors: \"Bengio, Louradour, Collobert, Weston\"\n    year: 2009\n    venue: \"ICML 2009\"\n    category: curriculum\n    role: background\n    key_finding: \"按难度递增顺序呈现训练样本可加速收敛并改善非凸优化的局部最优质量；curriculum 本质是一种 continuation method。\"\n    relevance: \"Curriculum learning 中 difficult example proportion 的 threshold 概念与我们的 dose-response 阈值平行——训练数据中困难/噪声样本超过阈值后性能崩溃\"\n\n  - id: madry2018adversarial\n    title: \"Towards Deep Learning Models Resistant to Adversarial Attacks\"\n    authors: \"Madry, Makelov, Schmidt, Tsipras, Vladu\"\n    year: 2018\n    venue: \"ICLR 2018\"\n    category: data-mixing\n    role: background\n    key_finding: \"基于 PGD 的 adversarial training 通过 robust optimization 框架显著提升对抗鲁棒性，但以 clean accuracy 下降为代价。\"\n    relevance: \"Adversarial training 的 accuracy-robustness tradeoff 是 dose-response 型——增加 adversarial perturbation 强度提升鲁棒性但降低 clean accuracy，与我们的 injection ratio vs clean eval tradeoff 结构相似\"\n",
      "numLines": 336,
      "startLine": 1,
      "totalLines": 336
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
OK so the ScienceDirect page is blocked. Let me try fetching from dl.acm.org or researchgate to confirm the authors.

Actually, from the search results, I already have:
- Authors: Agostinho Freire, Leandro H. de S. Silva, João V.R. de Andrade, Bruno J. T. Fernandes
- Journal: Knowledge-Based Systems (from the DOI `10.1016/j.knosys.2024.112544`, knosys = Knowledge-Based Systems)


Now I'll go through the references.bib file and make the necessary formatting updates to standardize the author names with initials. Continuing with the author corrections—I'm expanding the PALADIN entry to include all seven authors instead of the abbreviated version, and I notice the search results are giving me more complete information than what was initially in the file. I'm realizing the task is really about two things: fixing the lowercase "others" for existing entries, and adding first name initials across the board. For PALADIN with 7 authors, I'll list them all since that's manageable and other entries in the dataset have even more. Now I'm working through the remaining entries—agentHER2025 needs to be corrected to just the lead author with initials, and dong2024composition needs both the casing fix and the initials added to the authors.

For ye2025mixing_laws and li2025mixing_optimization, I need to verify whether I'm listing all authors or using "and others"—the task description for li2025mixing lists three specific names, so I should include all three rather than truncating with "and others." are the only ones provided, I should format them as individual authors rather than using "and others." For seddik2024, I have a partial list from the task but it might be incomplete, so I'll need to decide whether to include "and others" or search for the full author list. Given the time constraint, I'll go with what's explicitly provided and use lowercase "and others" where the original entry indicated additional authors beyond what's listed. I need to be more systematic about this. Let me go through each entry and identify what changes are needed—adding first name initials where they're missing, and updating "Others" to "others" with the full author lists where provided. I'll start working through them one by one, beginning with the entries I'm most confident about. Continuing through the remaining entries, I need to handle several more papers where author information is either incomplete or requires verification. Some entries like agentHER2025 and wkm2024alfworld need their author lists filled in, while others like arpit2017memorization present additional complexity I'll need to work through. Continuing through the bibliography entries with more author citations for papers on catastrophic forgetting, data augmentation, and linguistic phenomena. Continuing through the bibliography entries with more author citations for recent papers on reasoning and reflection techniques in language models. I'm noticing a discrepancy in the eef2025 entry — the bibliography lists "Wang" as the fourth author, but the search results show it should be "Cho-Jui Hsieh," with Tianyi Zhou as the fifth. I need to correct this. Now I'm checking the agentdebug2025 entry, which has a much longer author list from the search. I'm noticing a discrepancy between the task's author list and what the WebSearch actually returned. The task lists different first names than what came back from the search results, so I should trust the WebSearch data as authoritative. For the first paper, I'll format it as `{Zhu, K.} and {Liu, Z.} and {Li, B.} and {Tian, M.} and others` based on the actual search results showing Kunlun, Zijia, Bingxuan, and Muxin as the first four authors. Now I need to check the paladin2025 entry similarly—the search found 7 authors total, so I should verify how many to list before adding "and others." I'm finishing up the author list for paladin2025 with Chaudhary and the remaining co-authors. For wkm2024alfworld, I found 10 authors total, so I'm listing the first five with "others" to keep it concise. For beyond_clean_data2024, there are just 4 authors, so I'll include all of them. For Côté, I need to add the first initial M.-A. to get the full author format. Kim's entry should be formatted as Minsoo Kim and Seung-won Hwang. Now I'm going through and verifying a few more uncertain entries before I make all the edits to the bibliography file. Now I'm confirming the exact author names and formatting for those entries—Stanisław Jastrzębski becomes `{Jastrz\k{e}bski, S.}` and R. Thomas McCoy should be `{McCoy, R. T.}`. Let me search for the complete author lists for li2025 and seddik2024 to fill in the remaining gaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "f04d36c7-3191-477e-b5f0-5257e986c055",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VK4UGyUuKGiPenH4JC1K1n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7726,
      "cache_read_input_tokens": 38481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7726
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

_source line 43_

Now let me verify a few uncertain author lists before making edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "c1d75627-bea7-4752-b3a0-e6624462001b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VK4UGyUuKGiPenH4JC1K1n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7726,
      "cache_read_input_tokens": 38481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7726
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

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TjRzwv44yNK8d3veP7CTFJ`</summary>

```json
{
  "query": "\"Data Mixing Optimization for Supervised Fine-Tuning\" ICML 2025 authors Yuan Li Zhengzhong Liu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "48302a1f-e81b-4732-9958-c191e7a0b696",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VK4UGyUuKGiPenH4JC1K1n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7726,
      "cache_read_input_tokens": 38481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7726
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

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013GboguV7d3sTVgLyobLSp6`</summary>

```json
{
  "query": "\"How Bad is Training on Synthetic Data\" arXiv 2404.05090 Seddik authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "633bfbff-d4e8-4377-9479-54d45970e608",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VK4UGyUuKGiPenH4JC1K1n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7726,
      "cache_read_input_tokens": 38481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7726
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

_source line 46 · 2026-05-15T03:53:26.420Z_

<details><summary>↩ Tool result · `toolu_013GboguV7d3sTVgLyobLSp6`</summary>

```text
Web search results for query: ""How Bad is Training on Synthetic Data" arXiv 2404.05090 Seddik authors full list"

Links: [{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis","url":"https://arxiv.org/pdf/2404.05090"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | alphaXiv","url":"https://www.alphaxiv.org/resources/2404.05090v1"},{"title":"[PDF] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240405090E/abstract"},{"title":"arXiv:2410.04840v2 [cs.LG] 8 Oct 2024","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory","url":"https://arxiv.org/html/2410.08942"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/how-bad-is-training-synthetic-data-statistical"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"}]

Based on the search results, here is the full list of authors for the arXiv paper 2404.05090 "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse":

Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah

More specifically, the author affiliations are:

Mohamed El Amine Seddik (Technology Innovation Institute Abu Dhabi, UAE), Suei-Wen Chen (NYU Abu Dhabi), Soufiane Hayou (Simons Institute Berkeley, USA), Pierre Youssef (NYU Abu Dhabi), and Merouane Debbah (Khalifa University of Science and Technology Abu Dhabi, UAE)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "45a4988e-452f-4ff7-882b-375e72be495f",
  "tool_use_result": {
    "query": "\"How Bad is Training on Synthetic Data\" arXiv 2404.05090 Seddik authors full list",
    "results": [
      {
        "tool_use_id": "srvtoolu_019HNKz7Tv8q4sr7UFr6Jx25",
        "content": [
          {
            "title": "[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse",
            "url": "https://arxiv.org/abs/2404.05090"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse",
            "url": "https://arxiv.org/html/2404.05090v1"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical Analysis",
            "url": "https://arxiv.org/pdf/2404.05090"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2404.05090v1"
          },
          {
            "title": "[PDF] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240405090E/abstract"
          },
          {
            "title": "arXiv:2410.04840v2 [cs.LG] 8 Oct 2024",
            "url": "https://arxiv.org/pdf/2410.04840"
          },
          {
            "title": "Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory",
            "url": "https://arxiv.org/html/2410.08942"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/how-bad-is-training-synthetic-data-statistical"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, here is the full list of authors for the arXiv paper 2404.05090 \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\":\n\nMohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah\n\nMore specifically, the author affiliations are:\n\nMohamed El Amine Seddik (Technology Innovation Institute Abu Dhabi, UAE), Suei-Wen Chen (NYU Abu Dhabi), Soufiane Hayou (Simons Institute Berkeley, USA), Pierre Youssef (NYU Abu Dhabi), and Merouane Debbah (Khalifa University of Science and Technology Abu Dhabi, UAE)"
    ],
    "durationSeconds": 4.392136900000012
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T03:53:28.022Z_

<details><summary>↩ Tool result · `toolu_01TjRzwv44yNK8d3veP7CTFJ`</summary>

```text
Web search results for query: ""Data Mixing Optimization for Supervised Fine-Tuning" ICML 2025 authors Yuan Li Zhengzhong Liu"

Links: [{"title":"ICML Poster Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models","url":"https://icml.cc/virtual/2025/poster/46652"},{"title":"[2508.11953] Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models","url":"https://arxiv.org/abs/2508.11953"},{"title":"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models","url":"https://arxiv.org/html/2508.11953v1"},{"title":"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=19kqoNoc2N"},{"title":"dblp: Zhengzhong Liu 0001","url":"https://dblp.org/pid/166/0352.html"},{"title":"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models","url":"https://openreview.net/pdf?id=19kqoNoc2N"},{"title":"(PDF) Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models","url":"https://www.researchgate.net/publication/394540604_Data_Mixing_Optimization_for_Supervised_Fine-Tuning_of_Large_Language_Models"},{"title":"Published as a conference paper at ICLR 2026 DATAPROPHET:","url":"https://arxiv.org/pdf/2603.19688"},{"title":"Data Mixing Optimization for Supervised Fine-Tuning of ...","url":"https://bytez.com/docs/icml/46652/references?_c=eyJ2IjoxLCJyZWxhdGVkIjpbImNvZGUiLCJyZWZlcmVuY2VzIiwiY29uZmVyZW5jZSJdfQ%3D%3D"},{"title":"DATA MIXING LAWS: OPTIMIZING DATA MIXTURES BY ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf"}]

I found comprehensive information about the paper. Here's what I found:

## Paper Details

"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models" is an ICML 2025 poster by Yuan Li, Zhengzhong Liu, and Eric Xing.

## Overview

Optimizing data mixtures for supervised fine-tuning (SFT) of large language models (LLMs) is critical for developing general-purpose models, yet this area remains underexplored.

## Methodology

The paper frames data mixing as an optimization problem and introduces a novel method designed to minimize validation loss by parametrizing the loss through modeling effective data transferred and leveraging scaling laws for fine-tuning. By experimenting with various small-scale data mixtures, they fit these parameters and derive the optimal weights.

## Results

Models trained with their optimized weights perform on par with those using optimal weights determined via grid search, with per-domain loss only 0.66% higher than the best domain loss.

## Key Contributions

The paper provides both mathematical proofs and empirical results demonstrating that their algorithm achieves excellent overall and individual performance across all domains.

The paper is available on multiple platforms including OpenReview and arXiv (arxiv:2508.11953).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "6e6fa5de-2581-40c0-996c-58aa107982f7",
  "tool_use_result": {
    "query": "\"Data Mixing Optimization for Supervised Fine-Tuning\" ICML 2025 authors Yuan Li Zhengzhong Liu",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JwRd65EdfDAMHbhqo9FafN",
        "content": [
          {
            "title": "ICML Poster Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models",
            "url": "https://icml.cc/virtual/2025/poster/46652"
          },
          {
            "title": "[2508.11953] Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models",
            "url": "https://arxiv.org/abs/2508.11953"
          },
          {
            "title": "Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models",
            "url": "https://arxiv.org/html/2508.11953v1"
          },
          {
            "title": "Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=19kqoNoc2N"
          },
          {
            "title": "dblp: Zhengzhong Liu 0001",
            "url": "https://dblp.org/pid/166/0352.html"
          },
          {
            "title": "Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models",
            "url": "https://openreview.net/pdf?id=19kqoNoc2N"
          },
          {
            "title": "(PDF) Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models",
            "url": "https://www.researchgate.net/publication/394540604_Data_Mixing_Optimization_for_Supervised_Fine-Tuning_of_Large_Language_Models"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 DATAPROPHET:",
            "url": "https://arxiv.org/pdf/2603.19688"
          },
          {
            "title": "Data Mixing Optimization for Supervised Fine-Tuning of ...",
            "url": "https://bytez.com/docs/icml/46652/references?_c=eyJ2IjoxLCJyZWxhdGVkIjpbImNvZGUiLCJyZWZlcmVuY2VzIiwiY29uZmVyZW5jZSJdfQ%3D%3D"
          },
          {
            "title": "DATA MIXING LAWS: OPTIMIZING DATA MIXTURES BY ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf"
          }
        ]
      },
      "I found comprehensive information about the paper. Here's what I found:\n\n## Paper Details\n\n\"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\" is an ICML 2025 poster by Yuan Li, Zhengzhong Liu, and Eric Xing.\n\n## Overview\n\nOptimizing data mixtures for supervised fine-tuning (SFT) of large language models (LLMs) is critical for developing general-purpose models, yet this area remains underexplored.\n\n## Methodology\n\nThe paper frames data mixing as an optimization problem and introduces a novel method designed to minimize validation loss by parametrizing the loss through modeling effective data transferred and leveraging scaling laws for fine-tuning. By experimenting with various small-scale data mixtures, they fit these parameters and derive the optimal weights.\n\n## Results\n\nModels trained with their optimized weights perform on par with those using optimal weights determined via grid search, with per-domain loss only 0.66% higher than the best domain loss.\n\n## Key Contributions\n\nThe paper provides both mathematical proofs and empirical results demonstrating that their algorithm achieves excellent overall and individual performance across all domains.\n\nThe paper is available on multiple platforms including OpenReview and arXiv (arxiv:2508.11953)."
    ],
    "durationSeconds": 6.595840369000013
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need:

- li2025mixing_optimization: Yuan Li, Zhengzhong Liu, Eric Xing (3 authors total, confirmed)
- seddik2024: Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah (5 authors)

Now let me compile the complete corrected file. I'll rewrite the entire bib file since there are changes in almost every entry.

Let me finalize all the author strings:


1. rolnick2017: Rolnick, Veit, Belongie, and Shavit
2. yuan2024early_stopping: Yuan, Feng, and Liu
3. dohmatob2025collapse: Dohmatob, Feng, Subramonian, and Kempe
4. beyond_clean_data2024: Freire and...

Continuing with the author list for the Knowledge-Based Systems journal paper, then moving through several more references including Wang et al. on learning from failure, Song et al.'s work on ETO, Vuddanti and colleagues' Paladin paper, and Ding's AgentHER contribution. Finishing up the author list for Choudhury's work, then moving through the remaining papers. For the alfworld paper with 10 authors, I'm listing the first five and adding "others" to keep it concise. The memorization paper has a full author list of 11 people that I'm including in full, and I'm starting on Liu's early learning paper. Continuing through the bibliography entries with more author citations for papers on augmentation strategies, seed selection, model stability, and underspecification in machine learning. Checking the author details for kim2025coex — Kim, M. and Hwang, S. looks correct based on the task description. For eef2025, I'm verifying the five authors (Lan, Bai, Cheng, Hsieh, Zhou) and need to confirm the current bibliography entry matches what the search returned. and {Weston, J.}` for the Bengio entry, then moving on to the Madry paper with its five authors. Now I'm second-guessing the formatting for Hwang's name — "Seung-won" could be abbreviated as just `S.` or `S.-w.` depending on whether we treat it as a compound given name. Looking at the pattern in other entries, a single initial should work fine here. I'm going back and forth on the convention here—Korean names don't always get the hyphenated initial treatment in Western citations, but since I'm already using that pattern for other hyphenated names in this file, I'll stick with `S.-w.` for consistency. Now I need to rewrite the entire file with all these corrections applied.

Let me also verify the author initials from the task description: Alexander D'Amour becomes A., Matthew D. Hoffman stays as M. D., and for Mohamed El Amine Seddik, I'll use M. E. A. for the full first name. I've got the list of all the other authors mapped out correctly too.

Now I'm working through the remaining author names from the other papers. For the beyond_clean_data2024 paper, I need to handle the Portuguese naming conventions carefully—the particles like "de S." and "de" are part of the family name in BibTeX format, so those stay grouped with the surname. For Paladin, I'm converting the full first names to initials: Sri Vatsa becomes S. V., and Aarav becomes A.

I also need to fix the eef2025 paper's author list—it currently has Wang listed as one of the five authors, but that's incorrect. The actual authors are Li-Cheng Lan, Andrew Bai, Minhao Cheng, Cho-Jui Hsieh, and Tianyi Zhou, so I need to replace that entry with the correct names and initials.

For the Seddik entry, I'm noticing the "Chen" refers to Suei-Wen Chen, which should be formatted as S.-W. to match the hyphenated name convention I'm seeing across the bibliography. I'm also catching some inconsistency in how these compound names are capitalized—Chinese and East Asian names tend to capitalize both parts (L.-C., C.-J.), while Korean names sometimes use lowercase for the second part. Let me standardize this across the entries.

I'll go with S.-W. for both Suei-Wen and Seung-won to keep everything consistent in BibTeX format, since initials are typically all capitals. Now I need to write out the complete file and update the literature_map.yaml for those three entries that had "Various" listed as authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "ed67555b-46be-4fc6-b392-e8378365821f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Lk4R4V8nQZ43NJDPjcxFZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 805,
      "cache_creation_input_tokens": 6711,
      "cache_read_input_tokens": 46207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6711
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

_source line 49_

All data collected. Now I have all the author information. Let me rewrite the bib file with all corrections applied.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "67b31796-8ac3-4af2-a001-bb18d99294a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Lk4R4V8nQZ43NJDPjcxFZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 805,
      "cache_creation_input_tokens": 6711,
      "cache_read_input_tokens": 46207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6711
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

_source line 50_

<details open><summary>🔧 Tool call — Write · `toolu_016bVtuGQs94uAc34ubixPVn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/references.bib",
  "content": "@article{rolnick2017robust,\n  title={Deep Learning is Robust to Massive Label Noise},\n  author={{Rolnick, D.} and {Veit, A.} and {Belongie, S.} and {Shavit, N.}},\n  year={2017},\n  journal={arXiv preprint arXiv:1705.10694},\n  url={https://arxiv.org/abs/1705.10694}\n}\n\n@inproceedings{yuan2024early_stopping,\n  title={Early Stopping Against Label Noise Without Validation Data},\n  author={{Yuan, S.} and {Feng, L.} and {Liu, T.}},\n  year={2024},\n  booktitle={International Conference on Learning Representations}\n}\n\n@inproceedings{dohmatob2025collapse,\n  title={Strong Model Collapse},\n  author={{Dohmatob, E.} and {Feng, Y.} and {Subramonian, A.} and {Kempe, J.}},\n  year={2025},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{beyond_clean_data2024,\n  title={Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance},\n  author={{Freire, A.} and {de S. Silva, L. H.} and {de Andrade, J. V. R.} and {Fernandes, B. J. T.}},\n  year={2024},\n  journal={Knowledge-Based Systems}\n}\n\n@article{wang2024learning_from_failure,\n  title={Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents},\n  author={{Wang, R.} and {Li, H.} and {Han, X.} and {Zhang, Y.} and {Baldwin, T.}},\n  year={2024},\n  journal={arXiv preprint arXiv:2402.11651},\n  url={https://arxiv.org/abs/2402.11651}\n}\n\n@inproceedings{song2024eto,\n  title={Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents},\n  author={{Song, Y.} and {Yin, D.} and {Yue, X.} and {Huang, J.} and {Li, S.} and {Lin, B. Y.}},\n  year={2024},\n  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}\n}\n\n@article{paladin2025,\n  title={{PALADIN}: Self-Correcting Language Model Agents to Cure Tool-Failure Cases},\n  author={{Vuddanti, S. V.} and {Shah, A.} and {Chittiprolu, S. K.} and {Song, T.} and {Dev, S.} and {Zhu, K.} and {Chaudhary, M.}},\n  year={2025},\n  journal={arXiv preprint arXiv:2509.25238},\n  url={https://arxiv.org/abs/2509.25238}\n}\n\n@article{agentHER2025,\n  title={{AgentHER}: Hindsight Experience Replay for LLM Agent Trajectory Relabeling},\n  author={{Ding, L.}},\n  year={2025},\n  journal={arXiv preprint arXiv:2603.21357},\n  url={https://arxiv.org/abs/2603.21357}\n}\n\n@inproceedings{dong2024composition,\n  title={How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition},\n  author={{Dong, G.} and {Yuan, H.} and others},\n  year={2024},\n  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}\n}\n\n@inproceedings{ye2025mixing_laws,\n  title={Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance},\n  author={{Ye, J.} and others},\n  year={2025},\n  booktitle={International Conference on Learning Representations}\n}\n\n@inproceedings{li2025mixing_optimization,\n  title={Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models},\n  author={{Li, Y.} and {Liu, Z.} and {Xing, E.}},\n  year={2025},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@article{seddik2024synthetic_bound,\n  title={How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse},\n  author={{Seddik, M. E. A.} and {Chen, S.-W.} and {Hayou, S.} and {Youssef, P.} and {Debbah, M.}},\n  year={2024},\n  journal={arXiv preprint arXiv:2404.05090},\n  url={https://arxiv.org/abs/2404.05090}\n}\n\n@inproceedings{curriculum_robust2021,\n  title={Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction},\n  author={{Zhou, T.} and {Wang, S.} and {Bilmes, J.}},\n  year={2021},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{agentprm2025,\n  title={Process Reward Models for LLM Agents: Practical Framework and Directions},\n  author={{Choudhury, S.}},\n  year={2025},\n  journal={arXiv preprint arXiv:2502.10325},\n  url={https://arxiv.org/abs/2502.10325}\n}\n\n@inproceedings{wkm2024alfworld,\n  title={Agent Planning with World Knowledge Model},\n  author={{Qiao, S.} and {Fang, R.} and {Zhang, N.} and {Zhu, Y.} and {Chen, X.} and others},\n  year={2024},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@inproceedings{arpit2017memorization,\n  title={A Closer Look at Memorization in Deep Networks},\n  author={{Arpit, D.} and {Jastrz\\k{e}bski, S.} and {Ballas, N.} and {Krueger, D.} and {Bengio, E.} and {Kanwal, M. S.} and {Maharaj, T.} and {Fischer, A.} and {Courville, A.} and {Bengio, Y.} and {Lacoste-Julien, S.}},\n  year={2017},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@inproceedings{liu2020early_learning_reg,\n  title={Early-Learning Regularization Prevents Memorization of Noisy Labels},\n  author={{Liu, S.} and {Niles-Weed, J.} and {Razavian, N.} and {Fernandez-Granda, C.}},\n  year={2020},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@inproceedings{zhou2023lima,\n  title={{LIMA}: Less Is More for Alignment},\n  author={{Zhou, C.} and {Liu, P.} and {Xu, P.} and {Iyer, S.} and {Sun, J.} and {Mao, Y.} and {Ma, X.} and {Efrat, A.} and {Yu, P.} and {Yu, L.} and {Zhang, S.} and {Ghosh, G.} and {Lewis, M.} and {Zettlemoyer, L.} and {Levy, O.}},\n  year={2023},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@article{luo2023catastrophic_forgetting,\n  title={An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning},\n  author={{Luo, Y.} and {Yang, Z.} and {Meng, F.} and {Li, Y.} and {Zhou, J.} and {Zhang, Y.}},\n  year={2023},\n  journal={arXiv preprint arXiv:2308.08747},\n  url={https://arxiv.org/abs/2308.08747}\n}\n\n@inproceedings{longpre2020augmentation,\n  title={How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?},\n  author={{Longpre, S.} and {Wang, Y.} and {DuBois, C.}},\n  year={2020},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020}\n}\n\n@inproceedings{mccoy2020seeds,\n  title={{BERTs} of a feather do not generalize together: Large variability in generalization across models with similar test set performance},\n  author={{McCoy, R. T.} and {Min, J.} and {Linzen, T.}},\n  year={2020},\n  booktitle={Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP}\n}\n\n@inproceedings{mosbach2021stability,\n  title={On the Stability of Fine-tuning {BERT}: Misconceptions, Explanations, and Strong Baselines},\n  author={{Mosbach, M.} and {Andriushchenko, M.} and {Klakow, D.}},\n  year={2021},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{damour2022underspecification,\n  title={Underspecification Presents Challenges for Credibility in Modern Machine Learning},\n  author={{D'Amour, A.} and {Heller, K.} and {Moldovan, D.} and {Adlam, B.} and {Alipanahi, B.} and {Beutel, A.} and {Chen, C.} and {Deaton, J.} and {Eisenstein, J.} and {Hoffman, M. D.} and others},\n  year={2022},\n  journal={Journal of Machine Learning Research},\n  volume={23},\n  number={226}\n}\n\n@inproceedings{shridhar2021alfworld,\n  title={{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},\n  author={{Shridhar, M.} and {Yuan, X.} and {C\\^{o}t\\'{e}, M.-A.} and {Bisk, Y.} and {Trischler, A.} and {Hausknecht, M.}},\n  year={2021},\n  booktitle={International Conference on Learning Representations},\n  url={https://arxiv.org/abs/2010.03768}\n}\n\n@inproceedings{yao2023react,\n  title={{ReAct}: Synergizing Reasoning and Acting in Language Models},\n  author={{Yao, S.} and {Zhao, J.} and {Yu, D.} and {Du, N.} and {Shafran, I.} and {Narasimhan, K.} and {Cao, Y.}},\n  year={2023},\n  booktitle={International Conference on Learning Representations},\n  url={https://arxiv.org/abs/2210.03629}\n}\n\n@inproceedings{shinn2023reflexion,\n  title={Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author={{Shinn, N.} and {Cassano, F.} and {Berman, E.} and {Gopinath, A.} and {Narasimhan, K.} and {Yao, S.}},\n  year={2023},\n  booktitle={Advances in Neural Information Processing Systems},\n  url={https://arxiv.org/abs/2303.11366}\n}\n\n@inproceedings{kim2025coex,\n  title={{CoEx} -- Co-evolving World-model and Exploration},\n  author={{Kim, M.} and {Hwang, S.-W.}},\n  year={2025},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},\n  url={https://arxiv.org/abs/2507.22281}\n}\n\n@article{eef2025,\n  title={Exploring Expert Failures Improves LLM Agent Tuning},\n  author={{Lan, L.-C.} and {Bai, A.} and {Cheng, M.} and {Hsieh, C.-J.} and {Zhou, T.}},\n  year={2025},\n  journal={arXiv preprint arXiv:2504.13145},\n  url={https://arxiv.org/abs/2504.13145}\n}\n\n@article{agentdebug2025,\n  title={Where LLM Agents Fail and How They can Learn From Failures},\n  author={{Zhu, K.} and {Liu, Z.} and {Li, B.} and {Tian, M.} and others},\n  year={2025},\n  journal={arXiv preprint arXiv:2509.25370},\n  url={https://arxiv.org/abs/2509.25370}\n}\n\n@inproceedings{bengio2009curriculum,\n  title={Curriculum Learning},\n  author={{Bengio, Y.} and {Louradour, J.} and {Collobert, R.} and {Weston, J.}},\n  year={2009},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@inproceedings{madry2018adversarial,\n  title={Towards Deep Learning Models Resistant to Adversarial Attacks},\n  author={{Madry, A.} and {Makelov, A.} and {Schmidt, L.} and {Tsipras, D.} and {Vladu, A.}},\n  year={2018},\n  booktitle={International Conference on Learning Representations}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "ff9869f9-16c9-4c8e-b892-9d0bc7b6de8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Lk4R4V8nQZ43NJDPjcxFZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 805,
      "cache_creation_input_tokens": 6711,
      "cache_read_input_tokens": 46207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6711
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

_source line 51 · 2026-05-15T03:55:12.957Z_

<details><summary>↩ Tool result · `toolu_016bVtuGQs94uAc34ubixPVn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "d89bf5e7-14d3-4075-92a2-2131477c5a69",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/references.bib",
    "content": "@article{rolnick2017robust,\n  title={Deep Learning is Robust to Massive Label Noise},\n  author={{Rolnick, D.} and {Veit, A.} and {Belongie, S.} and {Shavit, N.}},\n  year={2017},\n  journal={arXiv preprint arXiv:1705.10694},\n  url={https://arxiv.org/abs/1705.10694}\n}\n\n@inproceedings{yuan2024early_stopping,\n  title={Early Stopping Against Label Noise Without Validation Data},\n  author={{Yuan, S.} and {Feng, L.} and {Liu, T.}},\n  year={2024},\n  booktitle={International Conference on Learning Representations}\n}\n\n@inproceedings{dohmatob2025collapse,\n  title={Strong Model Collapse},\n  author={{Dohmatob, E.} and {Feng, Y.} and {Subramonian, A.} and {Kempe, J.}},\n  year={2025},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{beyond_clean_data2024,\n  title={Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance},\n  author={{Freire, A.} and {de S. Silva, L. H.} and {de Andrade, J. V. R.} and {Fernandes, B. J. T.}},\n  year={2024},\n  journal={Knowledge-Based Systems}\n}\n\n@article{wang2024learning_from_failure,\n  title={Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents},\n  author={{Wang, R.} and {Li, H.} and {Han, X.} and {Zhang, Y.} and {Baldwin, T.}},\n  year={2024},\n  journal={arXiv preprint arXiv:2402.11651},\n  url={https://arxiv.org/abs/2402.11651}\n}\n\n@inproceedings{song2024eto,\n  title={Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents},\n  author={{Song, Y.} and {Yin, D.} and {Yue, X.} and {Huang, J.} and {Li, S.} and {Lin, B. Y.}},\n  year={2024},\n  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}\n}\n\n@article{paladin2025,\n  title={{PALADIN}: Self-Correcting Language Model Agents to Cure Tool-Failure Cases},\n  author={{Vuddanti, S. V.} and {Shah, A.} and {Chittiprolu, S. K.} and {Song, T.} and {Dev, S.} and {Zhu, K.} and {Chaudhary, M.}},\n  year={2025},\n  journal={arXiv preprint arXiv:2509.25238},\n  url={https://arxiv.org/abs/2509.25238}\n}\n\n@article{agentHER2025,\n  title={{AgentHER}: Hindsight Experience Replay for LLM Agent Trajectory Relabeling},\n  author={{Ding, L.}},\n  year={2025},\n  journal={arXiv preprint arXiv:2603.21357},\n  url={https://arxiv.org/abs/2603.21357}\n}\n\n@inproceedings{dong2024composition,\n  title={How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition},\n  author={{Dong, G.} and {Yuan, H.} and others},\n  year={2024},\n  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}\n}\n\n@inproceedings{ye2025mixing_laws,\n  title={Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance},\n  author={{Ye, J.} and others},\n  year={2025},\n  booktitle={International Conference on Learning Representations}\n}\n\n@inproceedings{li2025mixing_optimization,\n  title={Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models},\n  author={{Li, Y.} and {Liu, Z.} and {Xing, E.}},\n  year={2025},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@article{seddik2024synthetic_bound,\n  title={How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse},\n  author={{Seddik, M. E. A.} and {Chen, S.-W.} and {Hayou, S.} and {Youssef, P.} and {Debbah, M.}},\n  year={2024},\n  journal={arXiv preprint arXiv:2404.05090},\n  url={https://arxiv.org/abs/2404.05090}\n}\n\n@inproceedings{curriculum_robust2021,\n  title={Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction},\n  author={{Zhou, T.} and {Wang, S.} and {Bilmes, J.}},\n  year={2021},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{agentprm2025,\n  title={Process Reward Models for LLM Agents: Practical Framework and Directions},\n  author={{Choudhury, S.}},\n  year={2025},\n  journal={arXiv preprint arXiv:2502.10325},\n  url={https://arxiv.org/abs/2502.10325}\n}\n\n@inproceedings{wkm2024alfworld,\n  title={Agent Planning with World Knowledge Model},\n  author={{Qiao, S.} and {Fang, R.} and {Zhang, N.} and {Zhu, Y.} and {Chen, X.} and others},\n  year={2024},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@inproceedings{arpit2017memorization,\n  title={A Closer Look at Memorization in Deep Networks},\n  author={{Arpit, D.} and {Jastrz\\k{e}bski, S.} and {Ballas, N.} and {Krueger, D.} and {Bengio, E.} and {Kanwal, M. S.} and {Maharaj, T.} and {Fischer, A.} and {Courville, A.} and {Bengio, Y.} and {Lacoste-Julien, S.}},\n  year={2017},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@inproceedings{liu2020early_learning_reg,\n  title={Early-Learning Regularization Prevents Memorization of Noisy Labels},\n  author={{Liu, S.} and {Niles-Weed, J.} and {Razavian, N.} and {Fernandez-Granda, C.}},\n  year={2020},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@inproceedings{zhou2023lima,\n  title={{LIMA}: Less Is More for Alignment},\n  author={{Zhou, C.} and {Liu, P.} and {Xu, P.} and {Iyer, S.} and {Sun, J.} and {Mao, Y.} and {Ma, X.} and {Efrat, A.} and {Yu, P.} and {Yu, L.} and {Zhang, S.} and {Ghosh, G.} and {Lewis, M.} and {Zettlemoyer, L.} and {Levy, O.}},\n  year={2023},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@article{luo2023catastrophic_forgetting,\n  title={An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning},\n  author={{Luo, Y.} and {Yang, Z.} and {Meng, F.} and {Li, Y.} and {Zhou, J.} and {Zhang, Y.}},\n  year={2023},\n  journal={arXiv preprint arXiv:2308.08747},\n  url={https://arxiv.org/abs/2308.08747}\n}\n\n@inproceedings{longpre2020augmentation,\n  title={How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?},\n  author={{Longpre, S.} and {Wang, Y.} and {DuBois, C.}},\n  year={2020},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020}\n}\n\n@inproceedings{mccoy2020seeds,\n  title={{BERTs} of a feather do not generalize together: Large variability in generalization across models with similar test set performance},\n  author={{McCoy, R. T.} and {Min, J.} and {Linzen, T.}},\n  year={2020},\n  booktitle={Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP}\n}\n\n@inproceedings{mosbach2021stability,\n  title={On the Stability of Fine-tuning {BERT}: Misconceptions, Explanations, and Strong Baselines},\n  author={{Mosbach, M.} and {Andriushchenko, M.} and {Klakow, D.}},\n  year={2021},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{damour2022underspecification,\n  title={Underspecification Presents Challenges for Credibility in Modern Machine Learning},\n  author={{D'Amour, A.} and {Heller, K.} and {Moldovan, D.} and {Adlam, B.} and {Alipanahi, B.} and {Beutel, A.} and {Chen, C.} and {Deaton, J.} and {Eisenstein, J.} and {Hoffman, M. D.} and others},\n  year={2022},\n  journal={Journal of Machine Learning Research},\n  volume={23},\n  number={226}\n}\n\n@inproceedings{shridhar2021alfworld,\n  title={{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},\n  author={{Shridhar, M.} and {Yuan, X.} and {C\\^{o}t\\'{e}, M.-A.} and {Bisk, Y.} and {Trischler, A.} and {Hausknecht, M.}},\n  year={2021},\n  booktitle={International Conference on Learning Representations},\n  url={https://arxiv.org/abs/2010.03768}\n}\n\n@inproceedings{yao2023react,\n  title={{ReAct}: Synergizing Reasoning and Acting in Language Models},\n  author={{Yao, S.} and {Zhao, J.} and {Yu, D.} and {Du, N.} and {Shafran, I.} and {Narasimhan, K.} and {Cao, Y.}},\n  year={2023},\n  booktitle={International Conference on Learning Representations},\n  url={https://arxiv.org/abs/2210.03629}\n}\n\n@inproceedings{shinn2023reflexion,\n  title={Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author={{Shinn, N.} and {Cassano, F.} and {Berman, E.} and {Gopinath, A.} and {Narasimhan, K.} and {Yao, S.}},\n  year={2023},\n  booktitle={Advances in Neural Information Processing Systems},\n  url={https://arxiv.org/abs/2303.11366}\n}\n\n@inproceedings{kim2025coex,\n  title={{CoEx} -- Co-evolving World-model and Exploration},\n  author={{Kim, M.} and {Hwang, S.-W.}},\n  year={2025},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},\n  url={https://arxiv.org/abs/2507.22281}\n}\n\n@article{eef2025,\n  title={Exploring Expert Failures Improves LLM Agent Tuning},\n  author={{Lan, L.-C.} and {Bai, A.} and {Cheng, M.} and {Hsieh, C.-J.} and {Zhou, T.}},\n  year={2025},\n  journal={arXiv preprint arXiv:2504.13145},\n  url={https://arxiv.org/abs/2504.13145}\n}\n\n@article{agentdebug2025,\n  title={Where LLM Agents Fail and How They can Learn From Failures},\n  author={{Zhu, K.} and {Liu, Z.} and {Li, B.} and {Tian, M.} and others},\n  year={2025},\n  journal={arXiv preprint arXiv:2509.25370},\n  url={https://arxiv.org/abs/2509.25370}\n}\n\n@inproceedings{bengio2009curriculum,\n  title={Curriculum Learning},\n  author={{Bengio, Y.} and {Louradour, J.} and {Collobert, R.} and {Weston, J.}},\n  year={2009},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@inproceedings{madry2018adversarial,\n  title={Towards Deep Learning Models Resistant to Adversarial Attacks},\n  author={{Madry, A.} and {Makelov, A.} and {Schmidt, L.} and {Tsipras, D.} and {Vladu, A.}},\n  year={2018},\n  booktitle={International Conference on Learning Representations}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " @article{rolnick2017robust,",
          "   title={Deep Learning is Robust to Massive Label Noise},",
          "-  author={{Rolnick} and {Veit} and {Belongie} and {Shavit}},",
          "+  author={{Rolnick, D.} and {Veit, A.} and {Belongie, S.} and {Shavit, N.}},",
          "   year={2017},",
          "   journal={arXiv preprint arXiv:1705.10694},",
          "   url={https://arxiv.org/abs/1705.10694}"
        ]
      },
      {
        "oldStart": 8,
        "oldLines": 28,
        "newStart": 8,
        "newLines": 28,
        "lines": [
          " ",
          " @inproceedings{yuan2024early_stopping,",
          "   title={Early Stopping Against Label Noise Without Validation Data},",
          "-  author={{Yuan} and {Feng} and {Liu}},",
          "+  author={{Yuan, S.} and {Feng, L.} and {Liu, T.}},",
          "   year={2024},",
          "   booktitle={International Conference on Learning Representations}",
          " }",
          " ",
          " @inproceedings{dohmatob2025collapse,",
          "   title={Strong Model Collapse},",
          "-  author={{Dohmatob} and {Feng} and {Subramonian} and {Kempe}},",
          "+  author={{Dohmatob, E.} and {Feng, Y.} and {Subramonian, A.} and {Kempe, J.}},",
          "   year={2025},",
          "   booktitle={International Conference on Learning Representations}",
          " }",
          " ",
          " @article{beyond_clean_data2024,",
          "   title={Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance},",
          "-  author={{Various Authors}},",
          "+  author={{Freire, A.} and {de S. Silva, L. H.} and {de Andrade, J. V. R.} and {Fernandes, B. J. T.}},",
          "   year={2024},",
          "-  journal={ScienceDirect}",
          "+  journal={Knowledge-Based Systems}",
          " }",
          " ",
          " @article{wang2024learning_from_failure,",
          "   title={Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents},",
          "-  author={{Wang} and {Li} and {Han} and {Zhang} and {Baldwin}},",
          "+  author={{Wang, R.} and {Li, H.} and {Han, X.} and {Zhang, Y.} and {Baldwin, T.}},",
          "   year={2024},",
          "   journal={arXiv preprint arXiv:2402.11651},",
          "   url={https://arxiv.org/abs/2402.11651}"
        ]
      },
      {
        "oldStart": 37,
        "oldLines": 14,
        "newStart": 37,
        "newLines": 14,
        "lines": [
          " ",
          " @inproceedings{song2024eto,",
          "   title={Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents},",
          "-  author={{Song} and {Yin} and {Yue} and {Huang} and {Li} and {Lin}},",
          "+  author={{Song, Y.} and {Yin, D.} and {Yue, X.} and {Huang, J.} and {Li, S.} and {Lin, B. Y.}},",
          "   year={2024},",
          "   booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}",
          " }",
          " ",
          " @article{paladin2025,",
          "   title={{PALADIN}: Self-Correcting Language Model Agents to Cure Tool-Failure Cases},",
          "-  author={{Vuddanti} and {Shah} and Others},",
          "+  author={{Vuddanti, S. V.} and {Shah, A.} and {Chittiprolu, S. K.} and {Song, T.} and {Dev, S.} and {Zhu, K.} and {Chaudhary, M.}},",
          "   year={2025},",
          "   journal={arXiv preprint arXiv:2509.25238},",
          "   url={https://arxiv.org/abs/2509.25238}"
        ]
      },
      {
        "oldStart": 52,
        "oldLines": 7,
        "newStart": 52,
        "newLines": 7,
        "lines": [
          " ",
          " @article{agentHER2025,",
          "   title={{AgentHER}: Hindsight Experience Replay for LLM Agent Trajectory Relabeling},",
          "-  author={{Various Authors}},",
          "+  author={{Ding, L.}},",
          "   year={2025},",
          "   journal={arXiv preprint arXiv:2603.21357},",
          "   url={https://arxiv.org/abs/2603.21357}"
        ]
      },
      {
        "oldStart": 60,
        "oldLines": 28,
        "newStart": 60,
        "newLines": 28,
        "lines": [
          " ",
          " @inproceedings{dong2024composition,",
          "   title={How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition},",
          "-  author={{Dong} and {Yuan} and Others},",
          "+  author={{Dong, G.} and {Yuan, H.} and others},",
          "   year={2024},",
          "   booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}",
          " }",
          " ",
          " @inproceedings{ye2025mixing_laws,",
          "   title={Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance},",
          "-  author={{Ye} and Others},",
          "+  author={{Ye, J.} and others},",
          "   year={2025},",
          "   booktitle={International Conference on Learning Representations}",
          " }",
          " ",
          " @inproceedings{li2025mixing_optimization,",
          "   title={Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models},",
          "-  author={{Li} and Others},",
          "+  author={{Li, Y.} and {Liu, Z.} and {Xing, E.}},",
          "   year={2025},",
          "   booktitle={Proceedings of the International Conference on Machine Learning}",
          " }",
          " ",
          " @article{seddik2024synthetic_bound,",
          "   title={How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse},",
          "-  author={{Seddik} and Others},",
          "+  author={{Seddik, M. E. A.} and {Chen, S.-W.} and {Hayou, S.} and {Youssef, P.} and {Debbah, M.}},",
          "   year={2024},",
          "   journal={arXiv preprint arXiv:2404.05090},",
          "   url={https://arxiv.org/abs/2404.05090}"
        ]
      },
      {
        "oldStart": 89,
        "oldLines": 14,
        "newStart": 89,
        "newLines": 14,
        "lines": [
          " ",
          " @inproceedings{curriculum_robust2021,",
          "   title={Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction},",
          "-  author={{Zhou} and {Wang} and {Bilmes}},",
          "+  author={{Zhou, T.} and {Wang, S.} and {Bilmes, J.}},",
          "   year={2021},",
          "   booktitle={International Conference on Learning Representations}",
          " }",
          " ",
          " @article{agentprm2025,",
          "   title={Process Reward Models for LLM Agents: Practical Framework and Directions},",
          "-  author={{Choudhury}},",
          "+  author={{Choudhury, S.}},",
          "   year={2025},",
          "   journal={arXiv preprint arXiv:2502.10325},",
          "   url={https://arxiv.org/abs/2502.10325}"
        ]
      },
      {
        "oldStart": 104,
        "oldLines": 35,
        "newStart": 104,
        "newLines": 35,
        "lines": [
          " ",
          " @inproceedings{wkm2024alfworld,",
          "   title={Agent Planning with World Knowledge Model},",
          "-  author={{Various Authors}},",
          "+  author={{Qiao, S.} and {Fang, R.} and {Zhang, N.} and {Zhu, Y.} and {Chen, X.} and others},",
          "   year={2024},",
          "   booktitle={Advances in Neural Information Processing Systems}",
          " }",
          " ",
          " @inproceedings{arpit2017memorization,",
          "   title={A Closer Look at Memorization in Deep Networks},",
          "-  author={{Arpit} and {Jastrz\\k{e}bski} and {Ballas} and {Krueger} and {Bengio} and {Kanwal} and {Maharaj} and {Fischer} and {Courville} and {Bengio} and {Lacoste-Julien}},",
          "+  author={{Arpit, D.} and {Jastrz\\k{e}bski, S.} and {Ballas, N.} and {Krueger, D.} and {Bengio, E.} and {Kanwal, M. S.} and {Maharaj, T.} and {Fischer, A.} and {Courville, A.} and {Bengio, Y.} and {Lacoste-Julien, S.}},",
          "   year={2017},",
          "   booktitle={Proceedings of the International Conference on Machine Learning}",
          " }",
          " ",
          " @inproceedings{liu2020early_learning_reg,",
          "   title={Early-Learning Regularization Prevents Memorization of Noisy Labels},",
          "-  author={{Liu} and {Niles-Weed} and {Razavian} and {Fernandez-Granda}},",
          "+  author={{Liu, S.} and {Niles-Weed, J.} and {Razavian, N.} and {Fernandez-Granda, C.}},",
          "   year={2020},",
          "   booktitle={Advances in Neural Information Processing Systems}",
          " }",
          " ",
          " @inproceedings{zhou2023lima,",
          "   title={{LIMA}: Less Is More for Alignment},",
          "-  author={{Zhou} and {Liu} and {Xu} and {Iyer} and {Sun} and {Mao} and {Ma} and {Efrat} and {Yu} and {Yu} and {Zhang} and {Ghosh} and {Lewis} and {Zettlemoyer} and {Levy}},",
          "+  author={{Zhou, C.} and {Liu, P.} and {Xu, P.} and {Iyer, S.} and {Sun, J.} and {Mao, Y.} and {Ma, X.} and {Efrat, A.} and {Yu, P.} and {Yu, L.} and {Zhang, S.} and {Ghosh, G.} and {Lewis, M.} and {Zettlemoyer, L.} and {Levy, O.}},",
          "   year={2023},",
          "   booktitle={Advances in Neural Information Processing Systems}",
          " }",
          " ",
          " @article{luo2023catastrophic_forgetting,",
          "   title={An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning},",
          "-  author={{Luo} and {Yang} and {Meng} and {Li} and {Zhou} and {Zhang}},",
          "+  author={{Luo, Y.} and {Yang, Z.} and {Meng, F.} and {Li, Y.} and {Zhou, J.} and {Zhang, Y.}},",
          "   year={2023},",
          "   journal={arXiv preprint arXiv:2308.08747},",
          "   url={https://arxiv.org/abs/2308.08747}"
        ]
      },
      {
        "oldStart": 140,
        "oldLines": 28,
        "newStart": 140,
        "newLines": 28,
        "lines": [
          " ",
          " @inproceedings{longpre2020augmentation,",
          "   title={How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?},",
          "-  author={{Longpre} and {Wang} and {DuBois}},",
          "+  author={{Longpre, S.} and {Wang, Y.} and {DuBois, C.}},",
          "   year={2020},",
          "   booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020}",
          " }",
          " ",
          " @inproceedings{mccoy2020seeds,",
          "   title={{BERTs} of a feather do not generalize together: Large variability in generalization across models with similar test set performance},",
          "-  author={{McCoy} and {Min} and {Linzen}},",
          "+  author={{McCoy, R. T.} and {Min, J.} and {Linzen, T.}},",
          "   year={2020},",
          "   booktitle={Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP}",
          " }",
          " ",
          " @inproceedings{mosbach2021stability,",
          "   title={On the Stability of Fine-tuning {BERT}: Misconceptions, Explanations, and Strong Baselines},",
          "-  author={{Mosbach} and {Andriushchenko} and {Klakow}},",
          "+  author={{Mosbach, M.} and {Andriushchenko, M.} and {Klakow, D.}},",
          "   year={2021},",
          "   booktitle={International Conference on Learning Representations}",
          " }",
          " ",
          " @article{damour2022underspecification,",
          "   title={Underspecification Presents Challenges for Credibility in Modern Machine Learning},",
          "-  author={{D'Amour} and {Heller} and {Moldovan} and {Adlam} and {Alipanahi} and {Beutel} and {Chen} and {Deaton} and {Eisenstein} and {Hoffman} and Others},",
          "+  author={{D'Amour, A.} and {Heller, K.} and {Moldovan, D.} and {Adlam, B.} and {Alipanahi, B.} and {Beutel, A.} and {Chen, C.} and {Deaton, J.} and {Eisenstein, J.} and {Hoffman, M. D.} and others},",
          "   year={2022},",
          "   journal={Journal of Machine Learning Research},",
          "   volume={23},"
        ]
      },
      {
        "oldStart": 170,
        "oldLines": 7,
        "newStart": 170,
        "newLines": 7,
        "lines": [
          " ",
          " @inproceedings{shridhar2021alfworld,",
          "   title={{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},",
          "-  author={{Shridhar} and {Yuan} and {C\\^{o}t\\'{e}} and {Bisk} and {Trischler} and {Hausknecht}},",
          "+  author={{Shridhar, M.} and {Yuan, X.} and {C\\^{o}t\\'{e}, M.-A.} and {Bisk, Y.} and {Trischler, A.} and {Hausknecht, M.}},",
          "   year={2021},",
          "   booktitle={International Conference on Learning Representations},",
          "   url={https://arxiv.org/abs/2010.03768}"
        ]
      },
      {
        "oldStart": 178,
        "oldLines": 7,
        "newStart": 178,
        "newLines": 7,
        "lines": [
          " ",
          " @inproceedings{yao2023react,",
          "   title={{ReAct}: Synergizing Reasoning and Acting in Language Models},",
          "-  author={{Yao} and {Zhao} and {Yu} and {Du} and {Shafran} and {Narasimhan} and {Cao}},",
          "+  author={{Yao, S.} and {Zhao, J.} and {Yu, D.} and {Du, N.} and {Shafran, I.} and {Narasimhan, K.} and {Cao, Y.}},",
          "   year={2023},",
          "   booktitle={International Conference on Learning Representations},",
          "   url={https://arxiv.org/abs/2210.03629}"
        ]
      },
      {
        "oldStart": 186,
        "oldLines": 7,
        "newStart": 186,
        "newLines": 7,
        "lines": [
          " ",
          " @inproceedings{shinn2023reflexion,",
          "   title={Reflexion: Language Agents with Verbal Reinforcement Learning},",
          "-  author={{Shinn} and {Cassano} and {Berman} and {Gopinath} and {Narasimhan} and {Yao}},",
          "+  author={{Shinn, N.} and {Cassano, F.} and {Berman, E.} and {Gopinath, A.} and {Narasimhan, K.} and {Yao, S.}},",
          "   year={2023},",
          "   booktitle={Advances in Neural Information Processing Systems},",
          "   url={https://arxiv.org/abs/2303.11366}"
        ]
      },
      {
        "oldStart": 194,
        "oldLines": 7,
        "newStart": 194,
        "newLines": 7,
        "lines": [
          " ",
          " @inproceedings{kim2025coex,",
          "   title={{CoEx} -- Co-evolving World-model and Exploration},",
          "-  author={{Kim} and {Hwang}},",
          "+  author={{Kim, M.} and {Hwang, S.-W.}},",
          "   year={2025},",
          "   booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},",
          "   url={https://arxiv.org/abs/2507.22281}"
        ]
      },
      {
        "oldStart": 202,
        "oldLines": 7,
        "newStart": 202,
        "newLines": 7,
        "lines": [
          " ",
          " @article{eef2025,",
          "   title={Exploring Expert Failures Improves LLM Agent Tuning},",
          "-  author={{Lan} and {Bai} and {Cheng} and {Wang} and Others},",
          "+  author={{Lan, L.-C.} and {Bai, A.} and {Cheng, M.} and {Hsieh, C.-J.} and {Zhou, T.}},",
          "   year={2025},",
          "   journal={arXiv preprint arXiv:2504.13145},",
          "   url={https://arxiv.org/abs/2504.13145}"
        ]
      },
      {
        "oldStart": 210,
        "oldLines": 7,
        "newStart": 210,
        "newLines": 7,
        "lines": [
          " ",
          " @article{agentdebug2025,",
          "   title={Where LLM Agents Fail and How They can Learn From Failures},",
          "-  author={{Zhu} and {Liu} and {Li} and {Tian} and Others},",
          "+  author={{Zhu, K.} and {Liu, Z.} and {Li, B.} and {Tian, M.} and others},",
          "   year={2025},",
          "   journal={arXiv preprint arXiv:2509.25370},",
          "   url={https://arxiv.org/abs/2509.25370}"
        ]
      },
      {
        "oldStart": 218,
        "oldLines": 14,
        "newStart": 218,
        "newLines": 14,
        "lines": [
          " ",
          " @inproceedings{bengio2009curriculum,",
          "   title={Curriculum Learning},",
          "-  author={{Bengio} and {Louradour} and {Collobert} and {Weston}},",
          "+  author={{Bengio, Y.} and {Louradour, J.} and {Collobert, R.} and {Weston, J.}},",
          "   year={2009},",
          "   booktitle={Proceedings of the International Conference on Machine Learning}",
          " }",
          " ",
          " @inproceedings{madry2018adversarial,",
          "   title={Towards Deep Learning Models Resistant to Adversarial Attacks},",
          "-  author={{Madry} and {Makelov} and {Schmidt} and {Tsipras} and {Vladu}},",
          "+  author={{Madry, A.} and {Makelov, A.} and {Schmidt, L.} and {Tsipras, D.} and {Vladu, A.}},",
          "   year={2018},",
          "   booktitle={International Conference on Learning Representations}",
          " }"
        ]
      }
    ],
    "originalFile": "@article{rolnick2017robust,\n  title={Deep Learning is Robust to Massive Label Noise},\n  author={{Rolnick} and {Veit} and {Belongie} and {Shavit}},\n  year={2017},\n  journal={arXiv preprint arXiv:1705.10694},\n  url={https://arxiv.org/abs/1705.10694}\n}\n\n@inproceedings{yuan2024early_stopping,\n  title={Early Stopping Against Label Noise Without Validation Data},\n  author={{Yuan} and {Feng} and {Liu}},\n  year={2024},\n  booktitle={International Conference on Learning Representations}\n}\n\n@inproceedings{dohmatob2025collapse,\n  title={Strong Model Collapse},\n  author={{Dohmatob} and {Feng} and {Subramonian} and {Kempe}},\n  year={2025},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{beyond_clean_data2024,\n  title={Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance},\n  author={{Various Authors}},\n  year={2024},\n  journal={ScienceDirect}\n}\n\n@article{wang2024learning_from_failure,\n  title={Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents},\n  author={{Wang} and {Li} and {Han} and {Zhang} and {Baldwin}},\n  year={2024},\n  journal={arXiv preprint arXiv:2402.11651},\n  url={https://arxiv.org/abs/2402.11651}\n}\n\n@inproceedings{song2024eto,\n  title={Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents},\n  author={{Song} and {Yin} and {Yue} and {Huang} and {Li} and {Lin}},\n  year={2024},\n  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}\n}\n\n@article{paladin2025,\n  title={{PALADIN}: Self-Correcting Language Model Agents to Cure Tool-Failure Cases},\n  author={{Vuddanti} and {Shah} and Others},\n  year={2025},\n  journal={arXiv preprint arXiv:2509.25238},\n  url={https://arxiv.org/abs/2509.25238}\n}\n\n@article{agentHER2025,\n  title={{AgentHER}: Hindsight Experience Replay for LLM Agent Trajectory Relabeling},\n  author={{Various Authors}},\n  year={2025},\n  journal={arXiv preprint arXiv:2603.21357},\n  url={https://arxiv.org/abs/2603.21357}\n}\n\n@inproceedings{dong2024composition,\n  title={How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition},\n  author={{Dong} and {Yuan} and Others},\n  year={2024},\n  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}\n}\n\n@inproceedings{ye2025mixing_laws,\n  title={Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance},\n  author={{Ye} and Others},\n  year={2025},\n  booktitle={International Conference on Learning Representations}\n}\n\n@inproceedings{li2025mixing_optimization,\n  title={Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models},\n  author={{Li} and Others},\n  year={2025},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@article{seddik2024synthetic_bound,\n  title={How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse},\n  author={{Seddik} and Others},\n  year={2024},\n  journal={arXiv preprint arXiv:2404.05090},\n  url={https://arxiv.org/abs/2404.05090}\n}\n\n@inproceedings{curriculum_robust2021,\n  title={Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction},\n  author={{Zhou} and {Wang} and {Bilmes}},\n  year={2021},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{agentprm2025,\n  title={Process Reward Models for LLM Agents: Practical Framework and Directions},\n  author={{Choudhury}},\n  year={2025},\n  journal={arXiv preprint arXiv:2502.10325},\n  url={https://arxiv.org/abs/2502.10325}\n}\n\n@inproceedings{wkm2024alfworld,\n  title={Agent Planning with World Knowledge Model},\n  author={{Various Authors}},\n  year={2024},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@inproceedings{arpit2017memorization,\n  title={A Closer Look at Memorization in Deep Networks},\n  author={{Arpit} and {Jastrz\\k{e}bski} and {Ballas} and {Krueger} and {Bengio} and {Kanwal} and {Maharaj} and {Fischer} and {Courville} and {Bengio} and {Lacoste-Julien}},\n  year={2017},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@inproceedings{liu2020early_learning_reg,\n  title={Early-Learning Regularization Prevents Memorization of Noisy Labels},\n  author={{Liu} and {Niles-Weed} and {Razavian} and {Fernandez-Granda}},\n  year={2020},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@inproceedings{zhou2023lima,\n  title={{LIMA}: Less Is More for Alignment},\n  author={{Zhou} and {Liu} and {Xu} and {Iyer} and {Sun} and {Mao} and {Ma} and {Efrat} and {Yu} and {Yu} and {Zhang} and {Ghosh} and {Lewis} and {Zettlemoyer} and {Levy}},\n  year={2023},\n  booktitle={Advances in Neural Information Processing Systems}\n}\n\n@article{luo2023catastrophic_forgetting,\n  title={An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning},\n  author={{Luo} and {Yang} and {Meng} and {Li} and {Zhou} and {Zhang}},\n  year={2023},\n  journal={arXiv preprint arXiv:2308.08747},\n  url={https://arxiv.org/abs/2308.08747}\n}\n\n@inproceedings{longpre2020augmentation,\n  title={How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?},\n  author={{Longpre} and {Wang} and {DuBois}},\n  year={2020},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020}\n}\n\n@inproceedings{mccoy2020seeds,\n  title={{BERTs} of a feather do not generalize together: Large variability in generalization across models with similar test set performance},\n  author={{McCoy} and {Min} and {Linzen}},\n  year={2020},\n  booktitle={Proceedings of the Third BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP}\n}\n\n@inproceedings{mosbach2021stability,\n  title={On the Stability of Fine-tuning {BERT}: Misconceptions, Explanations, and Strong Baselines},\n  author={{Mosbach} and {Andriushchenko} and {Klakow}},\n  year={2021},\n  booktitle={International Conference on Learning Representations}\n}\n\n@article{damour2022underspecification,\n  title={Underspecification Presents Challenges for Credibility in Modern Machine Learning},\n  author={{D'Amour} and {Heller} and {Moldovan} and {Adlam} and {Alipanahi} and {Beutel} and {Chen} and {Deaton} and {Eisenstein} and {Hoffman} and Others},\n  year={2022},\n  journal={Journal of Machine Learning Research},\n  volume={23},\n  number={226}\n}\n\n@inproceedings{shridhar2021alfworld,\n  title={{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},\n  author={{Shridhar} and {Yuan} and {C\\^{o}t\\'{e}} and {Bisk} and {Trischler} and {Hausknecht}},\n  year={2021},\n  booktitle={International Conference on Learning Representations},\n  url={https://arxiv.org/abs/2010.03768}\n}\n\n@inproceedings{yao2023react,\n  title={{ReAct}: Synergizing Reasoning and Acting in Language Models},\n  author={{Yao} and {Zhao} and {Yu} and {Du} and {Shafran} and {Narasimhan} and {Cao}},\n  year={2023},\n  booktitle={International Conference on Learning Representations},\n  url={https://arxiv.org/abs/2210.03629}\n}\n\n@inproceedings{shinn2023reflexion,\n  title={Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author={{Shinn} and {Cassano} and {Berman} and {Gopinath} and {Narasimhan} and {Yao}},\n  year={2023},\n  booktitle={Advances in Neural Information Processing Systems},\n  url={https://arxiv.org/abs/2303.11366}\n}\n\n@inproceedings{kim2025coex,\n  title={{CoEx} -- Co-evolving World-model and Exploration},\n  author={{Kim} and {Hwang}},\n  year={2025},\n  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},\n  url={https://arxiv.org/abs/2507.22281}\n}\n\n@article{eef2025,\n  title={Exploring Expert Failures Improves LLM Agent Tuning},\n  author={{Lan} and {Bai} and {Cheng} and {Wang} and Others},\n  year={2025},\n  journal={arXiv preprint arXiv:2504.13145},\n  url={https://arxiv.org/abs/2504.13145}\n}\n\n@article{agentdebug2025,\n  title={Where LLM Agents Fail and How They can Learn From Failures},\n  author={{Zhu} and {Liu} and {Li} and {Tian} and Others},\n  year={2025},\n  journal={arXiv preprint arXiv:2509.25370},\n  url={https://arxiv.org/abs/2509.25370}\n}\n\n@inproceedings{bengio2009curriculum,\n  title={Curriculum Learning},\n  author={{Bengio} and {Louradour} and {Collobert} and {Weston}},\n  year={2009},\n  booktitle={Proceedings of the International Conference on Machine Learning}\n}\n\n@inproceedings{madry2018adversarial,\n  title={Towards Deep Learning Models Resistant to Adversarial Attacks},\n  author={{Madry} and {Makelov} and {Schmidt} and {Tsipras} and {Vladu}},\n  year={2018},\n  booktitle={International Conference on Learning Representations}\n}\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
Now I need to update the literature_map.yaml for the 3 entries that had "Various" as authors. Let me update:
1. beyond_clean_data2024 (line 39): "Various" → "Freire, de S. Silva, de Andrade, Fernandes"
2. agentHER2025 (line 81): "Various" → "Ding"
3. wkm2024alfworld (line 155): "Various" → "Qiao, Fang, Zhang, Zhu, Chen et al."


I also need to fix the venue for beyond_clean_data2024 from "ScienceDirect" to "Knowledge-Based Systems", and correct the author lists for eef2025 and agentdebug2025 to use the proper full names instead of the abbreviated "et al." format.

For paladin2025, I'm checking whether to expand "Vuddanti, Shah et al." to the full author list or keep it abbreviated.  Since there are seven authors total, the current abbreviated form with "et al." is already accurate and appropriate, so I'll leave it as is. Now I need to update the literature_map.yaml file with the correction for eef2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "bce1fd89-6879-492c-8b3d-b4425198ba4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrkdTyQ3z2S8La9yvqAYEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8482,
      "cache_read_input_tokens": 52918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8482
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

_source line 53_

Now updating the literature_map.yaml for the corrected entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "e192166a-c7a1-4ed8-b70a-9d8569659823",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrkdTyQ3z2S8La9yvqAYEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8482,
      "cache_read_input_tokens": 52918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8482
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

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_01FfNSrTeD4YZR6Cf1LJDLxC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
  "old_string": "    authors: \"Various\"\n    year: 2024\n    venue: ScienceDirect",
  "new_string": "    authors: \"Freire, de S. Silva, de Andrade, Fernandes\"\n    year: 2024\n    venue: Knowledge-Based Systems"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "a5a707be-e9d8-42d5-8576-056e407202d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrkdTyQ3z2S8La9yvqAYEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8482,
      "cache_read_input_tokens": 52918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8482
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

_source line 55 · 2026-05-15T03:55:26.582Z_

<details><summary>↩ Tool result · `toolu_01FfNSrTeD4YZR6Cf1LJDLxC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "3b9ad969-30b4-4291-aa13-467f185e27bd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
    "oldString": "    authors: \"Various\"\n    year: 2024\n    venue: ScienceDirect",
    "newString": "    authors: \"Freire, de S. Silva, de Andrade, Fernandes\"\n    year: 2024\n    venue: Knowledge-Based Systems",
    "originalFile": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Various\"\n    year: 2024\n    venue: ScienceDirect\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n\n  # === Category: alfworld-methods ===\n\n  - id: shridhar2021alfworld\n    title: \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\"\n    authors: \"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    arxiv: \"2010.03768\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\"\n    relevance: \"我们的实验环境；134 tasks across 6 task types benchmark\"\n\n  - id: yao2023react\n    title: \"ReAct: Synergizing Reasoning and Acting in Language Models\"\n    authors: \"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.03629\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\"\n    relevance: \"我们使用的 prompting paradigm（ReAct format）\"\n\n  - id: shinn2023reflexion\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2303.11366\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\"\n    relevance: \"Inference-time reflection 成功 where training-time injection 失败——对比 key point\"\n\n  - id: kim2025coex\n    title: \"CoEx -- Co-evolving World-model and Exploration\"\n    authors: \"Kim, Hwang\"\n    year: 2025\n    venue: \"Findings of EMNLP 2025\"\n    arxiv: \"2507.22281\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\"\n    relevance: \"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\"\n\n  # === Category: error-injection (补充) ===\n\n  - id: eef2025\n    title: \"Exploring Expert Failures Improves LLM Agent Tuning\"\n    authors: \"Lan, Bai, Cheng, Wang et al.\"\n    year: 2025\n    venue: \"arXiv 2504.13145\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"从失败 expert trajectories 中提取有益 actions（plans、key actions），用于引导 agent exploration，WebShop SOTA 0.81，SciWorld 81/100。\"\n    relevance: \"从失败中提取正向信号（非注入负信号），成功 on WebShop。与我们的直接注入形成对比——方向相反的 failure utilization。\"\n\n  - id: agentdebug2025\n    title: \"Where LLM Agents Fail and How They can Learn From Failures\"\n    authors: \"Zhu, Liu, Li, Tian et al.\"\n    year: 2025\n    venue: \"arXiv 2509.25370\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。\"\n    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"\n\n  # === Category: data-mixing / curriculum (补充) ===\n\n  - id: bengio2009curriculum\n    title: \"Curriculum Learning\"\n    authors: \"Bengio, Louradour, Collobert, Weston\"\n    year: 2009\n    venue: \"ICML 2009\"\n    category: curriculum\n    role: background\n    key_finding: \"按难度递增顺序呈现训练样本可加速收敛并改善非凸优化的局部最优质量；curriculum 本质是一种 continuation method。\"\n    relevance: \"Curriculum learning 中 difficult example proportion 的 threshold 概念与我们的 dose-response 阈值平行——训练数据中困难/噪声样本超过阈值后性能崩溃\"\n\n  - id: madry2018adversarial\n    title: \"Towards Deep Learning Models Resistant to Adversarial Attacks\"\n    authors: \"Madry, Makelov, Schmidt, Tsipras, Vladu\"\n    year: 2018\n    venue: \"ICLR 2018\"\n    category: data-mixing\n    role: background\n    key_finding: \"基于 PGD 的 adversarial training 通过 robust optimization 框架显著提升对抗鲁棒性，但以 clean accuracy 下降为代价。\"\n    relevance: \"Adversarial training 的 accuracy-robustness tradeoff 是 dose-response 型——增加 adversarial perturbation 强度提升鲁棒性但降低 clean accuracy，与我们的 injection ratio vs clean eval tradeoff 结构相似\"\n",
    "structuredPatch": [
      {
        "oldStart": 36,
        "oldLines": 9,
        "newStart": 36,
        "newLines": 9,
        "lines": [
          " ",
          "   - id: beyond_clean_data2024",
          "     title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"",
          "-    authors: \"Various\"",
          "+    authors: \"Freire, de S. Silva, de Andrade, Fernandes\"",
          "     year: 2024",
          "-    venue: ScienceDirect",
          "+    venue: Knowledge-Based Systems",
          "     category: dose-response",
          "     role: background",
          "     key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\""
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

_source line 56_

<details open><summary>🔧 Tool call — Edit · `toolu_01TTBHVjJm5DtWm7mHcpbQkg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
  "old_string": "  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"",
  "new_string": "  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Ding\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "dd97c8c3-0349-4fa7-879d-b873b4be8031",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrkdTyQ3z2S8La9yvqAYEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8482,
      "cache_read_input_tokens": 52918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8482
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

_source line 57 · 2026-05-15T03:55:28.303Z_

<details><summary>↩ Tool result · `toolu_01TTBHVjJm5DtWm7mHcpbQkg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "bd7cadf1-b577-453f-b659-175b9384d66f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
    "oldString": "  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"",
    "newString": "  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Ding\"",
    "originalFile": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Freire, de S. Silva, de Andrade, Fernandes\"\n    year: 2024\n    venue: Knowledge-Based Systems\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Various\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n\n  # === Category: alfworld-methods ===\n\n  - id: shridhar2021alfworld\n    title: \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\"\n    authors: \"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    arxiv: \"2010.03768\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\"\n    relevance: \"我们的实验环境；134 tasks across 6 task types benchmark\"\n\n  - id: yao2023react\n    title: \"ReAct: Synergizing Reasoning and Acting in Language Models\"\n    authors: \"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.03629\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\"\n    relevance: \"我们使用的 prompting paradigm（ReAct format）\"\n\n  - id: shinn2023reflexion\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2303.11366\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\"\n    relevance: \"Inference-time reflection 成功 where training-time injection 失败——对比 key point\"\n\n  - id: kim2025coex\n    title: \"CoEx -- Co-evolving World-model and Exploration\"\n    authors: \"Kim, Hwang\"\n    year: 2025\n    venue: \"Findings of EMNLP 2025\"\n    arxiv: \"2507.22281\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\"\n    relevance: \"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\"\n\n  # === Category: error-injection (补充) ===\n\n  - id: eef2025\n    title: \"Exploring Expert Failures Improves LLM Agent Tuning\"\n    authors: \"Lan, Bai, Cheng, Wang et al.\"\n    year: 2025\n    venue: \"arXiv 2504.13145\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"从失败 expert trajectories 中提取有益 actions（plans、key actions），用于引导 agent exploration，WebShop SOTA 0.81，SciWorld 81/100。\"\n    relevance: \"从失败中提取正向信号（非注入负信号），成功 on WebShop。与我们的直接注入形成对比——方向相反的 failure utilization。\"\n\n  - id: agentdebug2025\n    title: \"Where LLM Agents Fail and How They can Learn From Failures\"\n    authors: \"Zhu, Liu, Li, Tian et al.\"\n    year: 2025\n    venue: \"arXiv 2509.25370\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。\"\n    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"\n\n  # === Category: data-mixing / curriculum (补充) ===\n\n  - id: bengio2009curriculum\n    title: \"Curriculum Learning\"\n    authors: \"Bengio, Louradour, Collobert, Weston\"\n    year: 2009\n    venue: \"ICML 2009\"\n    category: curriculum\n    role: background\n    key_finding: \"按难度递增顺序呈现训练样本可加速收敛并改善非凸优化的局部最优质量；curriculum 本质是一种 continuation method。\"\n    relevance: \"Curriculum learning 中 difficult example proportion 的 threshold 概念与我们的 dose-response 阈值平行——训练数据中困难/噪声样本超过阈值后性能崩溃\"\n\n  - id: madry2018adversarial\n    title: \"Towards Deep Learning Models Resistant to Adversarial Attacks\"\n    authors: \"Madry, Makelov, Schmidt, Tsipras, Vladu\"\n    year: 2018\n    venue: \"ICLR 2018\"\n    category: data-mixing\n    role: background\n    key_finding: \"基于 PGD 的 adversarial training 通过 robust optimization 框架显著提升对抗鲁棒性，但以 clean accuracy 下降为代价。\"\n    relevance: \"Adversarial training 的 accuracy-robustness tradeoff 是 dose-response 型——增加 adversarial perturbation 强度提升鲁棒性但降低 clean accuracy，与我们的 injection ratio vs clean eval tradeoff 结构相似\"\n",
    "structuredPatch": [
      {
        "oldStart": 78,
        "oldLines": 7,
        "newStart": 78,
        "newLines": 7,
        "lines": [
          " ",
          "   - id: agentHER2025",
          "     title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"",
          "-    authors: \"Various\"",
          "+    authors: \"Ding\"",
          "     year: 2025",
          "     venue: arXiv 2603.21357",
          "     category: error-injection"
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

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_01Fcis9rBF3Yc2oKMQExPnjH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
  "old_string": "  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"",
  "new_string": "  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Qiao, Fang, Zhang, Zhu, Chen et al.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "ab9d7b31-9f6c-4fbd-9ece-17f0579894e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrkdTyQ3z2S8La9yvqAYEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8482,
      "cache_read_input_tokens": 52918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8482
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

_source line 59 · 2026-05-15T03:55:30.188Z_

<details><summary>↩ Tool result · `toolu_01Fcis9rBF3Yc2oKMQExPnjH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "c0784e8c-8cd5-41bd-897b-f9c92603a639",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
    "oldString": "  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"",
    "newString": "  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Qiao, Fang, Zhang, Zhu, Chen et al.\"",
    "originalFile": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Freire, de S. Silva, de Andrade, Fernandes\"\n    year: 2024\n    venue: Knowledge-Based Systems\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Ding\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Various\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n\n  # === Category: alfworld-methods ===\n\n  - id: shridhar2021alfworld\n    title: \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\"\n    authors: \"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    arxiv: \"2010.03768\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\"\n    relevance: \"我们的实验环境；134 tasks across 6 task types benchmark\"\n\n  - id: yao2023react\n    title: \"ReAct: Synergizing Reasoning and Acting in Language Models\"\n    authors: \"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.03629\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\"\n    relevance: \"我们使用的 prompting paradigm（ReAct format）\"\n\n  - id: shinn2023reflexion\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2303.11366\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\"\n    relevance: \"Inference-time reflection 成功 where training-time injection 失败——对比 key point\"\n\n  - id: kim2025coex\n    title: \"CoEx -- Co-evolving World-model and Exploration\"\n    authors: \"Kim, Hwang\"\n    year: 2025\n    venue: \"Findings of EMNLP 2025\"\n    arxiv: \"2507.22281\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\"\n    relevance: \"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\"\n\n  # === Category: error-injection (补充) ===\n\n  - id: eef2025\n    title: \"Exploring Expert Failures Improves LLM Agent Tuning\"\n    authors: \"Lan, Bai, Cheng, Wang et al.\"\n    year: 2025\n    venue: \"arXiv 2504.13145\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"从失败 expert trajectories 中提取有益 actions（plans、key actions），用于引导 agent exploration，WebShop SOTA 0.81，SciWorld 81/100。\"\n    relevance: \"从失败中提取正向信号（非注入负信号），成功 on WebShop。与我们的直接注入形成对比——方向相反的 failure utilization。\"\n\n  - id: agentdebug2025\n    title: \"Where LLM Agents Fail and How They can Learn From Failures\"\n    authors: \"Zhu, Liu, Li, Tian et al.\"\n    year: 2025\n    venue: \"arXiv 2509.25370\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。\"\n    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"\n\n  # === Category: data-mixing / curriculum (补充) ===\n\n  - id: bengio2009curriculum\n    title: \"Curriculum Learning\"\n    authors: \"Bengio, Louradour, Collobert, Weston\"\n    year: 2009\n    venue: \"ICML 2009\"\n    category: curriculum\n    role: background\n    key_finding: \"按难度递增顺序呈现训练样本可加速收敛并改善非凸优化的局部最优质量；curriculum 本质是一种 continuation method。\"\n    relevance: \"Curriculum learning 中 difficult example proportion 的 threshold 概念与我们的 dose-response 阈值平行——训练数据中困难/噪声样本超过阈值后性能崩溃\"\n\n  - id: madry2018adversarial\n    title: \"Towards Deep Learning Models Resistant to Adversarial Attacks\"\n    authors: \"Madry, Makelov, Schmidt, Tsipras, Vladu\"\n    year: 2018\n    venue: \"ICLR 2018\"\n    category: data-mixing\n    role: background\n    key_finding: \"基于 PGD 的 adversarial training 通过 robust optimization 框架显著提升对抗鲁棒性，但以 clean accuracy 下降为代价。\"\n    relevance: \"Adversarial training 的 accuracy-robustness tradeoff 是 dose-response 型——增加 adversarial perturbation 强度提升鲁棒性但降低 clean accuracy，与我们的 injection ratio vs clean eval tradeoff 结构相似\"\n",
    "structuredPatch": [
      {
        "oldStart": 152,
        "oldLines": 7,
        "newStart": 152,
        "newLines": 7,
        "lines": [
          " ",
          "   - id: wkm2024alfworld",
          "     title: \"Agent Planning with World Knowledge Model\"",
          "-    authors: \"Various\"",
          "+    authors: \"Qiao, Fang, Zhang, Zhu, Chen et al.\"",
          "     year: 2024",
          "     venue: NeurIPS 2024",
          "     category: curriculum"
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

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_01XSTM3fgkcFRf4G5BvfcN42`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
  "old_string": "    authors: \"Lan, Bai, Cheng, Wang et al.\"",
  "new_string": "    authors: \"Lan, Bai, Cheng, Hsieh, Zhou\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "cc99ba69-2a14-4576-b7bd-3aa349e6cce5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrkdTyQ3z2S8La9yvqAYEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8482,
      "cache_read_input_tokens": 52918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8482
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

_source line 61 · 2026-05-15T03:55:30.845Z_

<details><summary>↩ Tool result · `toolu_01XSTM3fgkcFRf4G5BvfcN42`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "cba6895b-90fc-4735-8c68-7f4802baa552",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
    "oldString": "    authors: \"Lan, Bai, Cheng, Wang et al.\"",
    "newString": "    authors: \"Lan, Bai, Cheng, Hsieh, Zhou\"",
    "originalFile": "# Literature Map: Dose-Response / Threshold Effects in Data Augmentation\n# Updated: 2026-05-15\n\nentries:\n  # === Category: dose-response / threshold ===\n\n  - id: rolnick2017robust\n    title: \"Deep Learning is Robust to Massive Label Noise\"\n    authors: \"Rolnick, Veit, Belongie, Shavit\"\n    year: 2017\n    venue: arXiv 1705.10694\n    category: dose-response\n    role: background\n    key_finding: \"DNNs maintain >90% accuracy on MNIST even when correct labels are diluted 100:1, as long as correct label remains most likely by a small margin.\"\n    relevance: \"Contrasts with our finding: image classification is robust to extreme noise, while embodied planning shows sharp degradation at 25%. Task complexity mediates noise tolerance.\"\n\n  - id: yuan2024early_stopping\n    title: \"Early Stopping Against Label Noise Without Validation Data\"\n    authors: \"Yuan, Feng, Liu\"\n    year: 2024\n    venue: ICLR 2024\n    category: dose-response\n    role: background\n    key_finding: \"Identifies phase transition where DNNs shift from fitting clean to fitting mislabeled examples. Proposes Label Wave to detect this transition during training.\"\n    relevance: \"Supports existence of phase transition in learning dynamics. Our 10-25% threshold may correspond to such a transition point in the SFT regime.\"\n\n  - id: dohmatob2025collapse\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Feng, Subramonian, Kempe\"\n    year: 2025\n    venue: ICLR 2025\n    category: threshold\n    role: background\n    key_finding: \"Even 0.1% synthetic data can cause model collapse in supervised regression. Past interpolation threshold, larger models become more robust (double-descent).\"\n    relevance: \"Demonstrates extreme sensitivity to data quality in certain regimes. Our 10-25% threshold is analogous—small quality shifts cause nonlinear degradation.\"\n\n  - id: beyond_clean_data2024\n    title: \"Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance\"\n    authors: \"Freire, de S. Silva, de Andrade, Fernandes\"\n    year: 2024\n    venue: Knowledge-Based Systems\n    category: dose-response\n    role: background\n    key_finding: \"Systematically varies noise levels in training and validation for object detection, mapping convergence limits and degradation thresholds.\"\n    relevance: \"Methodologically similar—varies noise proportion to find degradation curves. Shows task-specific threshold behavior.\"\n\n  # === Category: error-injection / failure augmentation ===\n\n  - id: wang2024learning_from_failure\n    title: \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\"\n    authors: \"Wang, Li, Han, Zhang, Baldwin\"\n    year: 2024\n    venue: arXiv 2402.11651\n    category: error-injection\n    role: evaluation\n    key_finding: \"Failed trajectories provide valuable signal for LLM agents via contrastive learning. Negative examples improve math, QA, strategic tasks when properly structured.\"\n    relevance: \"Directly related—injects negative trajectories into agent SFT. Key difference: they use contrastive framing, not raw mixing. Our work shows raw mixing has narrow safe window.\"\n\n  - id: song2024eto\n    title: \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\"\n    authors: \"Song, Yin, Yue, Huang, Li, Lin\"\n    year: 2024\n    venue: ACL 2024\n    category: error-injection\n    role: evaluation\n    key_finding: \"Iteratively collects failure trajectories, uses DPO-style contrastive learning on success-failure pairs. +8% WebShop, +9.5% ScienceWorld vs SFT.\"\n    relevance: \"Uses failure trajectories via preference optimization (DPO), not direct SFT mixing. Avoids our threshold problem by never training directly on failures.\"\n\n  - id: paladin2025\n    title: \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\"\n    authors: \"Vuddanti, Shah et al.\"\n    year: 2025\n    venue: arXiv 2509.25238\n    category: error-injection\n    role: evaluation\n    key_finding: \"Trains on 50K+ recovery-annotated failure trajectories via LoRA. +57pp recovery rate vs vanilla (32.76%→89.68%), +13.6pp vs CRITIC baseline. Taxonomy of 7 error classes. Includes inference-time retrieval.\"\n    relevance: \"Most similar to our approach (taxonomy-guided error injection). Key difference: they pair failures with recovery demos; we inject standalone error trajectories.\"\n\n  - id: agentHER2025\n    title: \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\"\n    authors: \"Ding\"\n    year: 2025\n    venue: arXiv 2603.21357\n    category: error-injection\n    role: evaluation\n    key_finding: \"Converts failed trajectories to valid training data by relabeling—failure for task A becomes success for task B.\"\n    relevance: \"Avoids noise problem by redefining failure as success for different goals. Contrasts with our direct injection approach.\"\n\n  # === Category: data-mixing ===\n\n  - id: dong2024composition\n    title: \"How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition\"\n    authors: \"Dong, Yuan et al.\"\n    year: 2024\n    venue: ACL 2024\n    category: data-mixing\n    role: background\n    key_finding: \"Data amount per domain matters more than ratio. Low-data mixing enables cross-domain transfer; high-data mixing causes ability conflicts.\"\n    relevance: \"Documents ability-conflict at high data amounts—analogous to our threshold. Ratio secondary to amount suggests our threshold may be absolute-count driven.\"\n\n  - id: ye2025mixing_laws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye et al.\"\n    year: 2025\n    venue: ICLR 2025\n    category: data-mixing\n    role: background\n    key_finding: \"Discovers quantitative scaling laws L=f(r) for mixture proportions. Accurately predicts critical proportion avoiding catastrophic forgetting.\"\n    relevance: \"Their 'critical proportion for catastrophic forgetting' is conceptually identical to our threshold—both mark a phase transition in mixing.\"\n\n  - id: li2025mixing_optimization\n    title: \"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models\"\n    authors: \"Li et al.\"\n    year: 2025\n    venue: ICML 2025\n    category: data-mixing\n    role: background\n    key_finding: \"SFT mixing as optimization with scaling-law parameterization. Optimal weights depend on model size and data scale.\"\n    relevance: \"Optimal mixing is model-size dependent—our 7B model may have different threshold than larger models. Finding is scale-specific.\"\n\n  - id: seddik2024synthetic_bound\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik et al.\"\n    year: 2024\n    venue: arXiv 2404.05090\n    category: data-mixing\n    role: background\n    key_finding: \"Theoretical upper bounds on low-quality data proportion before collapse. Real data proportion must remain high.\"\n    relevance: \"Theoretical grounding for hard thresholds in quality mixing. Our empirical 10-25% window is consistent with their predictions.\"\n\n  # === Category: curriculum / quality threshold ===\n\n  - id: curriculum_robust2021\n    title: \"Robust Curriculum Learning: from Clean Label Detection to Noisy Label Self-Correction\"\n    authors: \"Zhou, Wang, Bilmes\"\n    year: 2021\n    venue: ICLR 2021\n    category: curriculum\n    role: background\n    key_finding: \"Networks learn simple patterns first, then overfit noisy labels. Loss-based curriculum selection is unstable; errors accumulate multiplicatively.\"\n    relevance: \"Explains WHY threshold exists: once noisy proportion exceeds implicit curriculum capacity, errors accumulate. Our 25% may exceed model's capacity.\"\n\n  - id: agentprm2025\n    title: \"Process Reward Models for LLM Agents: Practical Framework and Directions\"\n    authors: \"Choudhury\"\n    year: 2025\n    venue: arXiv 2502.10325\n    category: curriculum\n    role: evaluation\n    key_finding: \"Best-of-N with process reward model achieves 91.0% on ALFWorld (N=16, base policy 88.1%). Shows reward-guided search outperforms SFT alone.\"\n    relevance: \"ALFWorld SOTA reference. Our 65.3% SFT-only baseline is reasonable given AgentPRM uses test-time search.\"\n\n  - id: wkm2024alfworld\n    title: \"Agent Planning with World Knowledge Model\"\n    authors: \"Qiao, Fang, Zhang, Zhu, Chen et al.\"\n    year: 2024\n    venue: NeurIPS 2024\n    category: curriculum\n    role: evaluation\n    key_finding: \"World knowledge models reduce hallucinatory actions in ALFWorld. SFT on expert trajectories prone to overfitting.\"\n    relevance: \"ALFWorld baseline showing SFT quality sensitivity. Hallucination increase from poor training data parallels our error-injection degradation.\"\n\n  # === Category: training-dynamics / memorization ===\n\n  - id: arpit2017memorization\n    title: \"A Closer Look at Memorization in Deep Networks\"\n    authors: \"Arpit, Jastrzębski, Ballas, Krueger, Bengio, Kanwal, Maharaj, Fischer, Courville, Bengio, Lacoste-Julien\"\n    year: 2017\n    venue: ICML 2017\n    category: training-dynamics\n    role: background\n    key_finding: \"DNNs first learn clean patterns (early learning phase), then memorize noise. Training loss/accuracy improve on noisy data but generalization degrades. Dataset-independent capacity concepts are insufficient.\"\n    relevance: \"Directly explains our '50% injection → lowest train loss but worst eval' paradox. Higher injection = more noisy samples to memorize, better train metrics but worse generalization.\"\n\n  - id: liu2020early_learning_reg\n    title: \"Early-Learning Regularization Prevents Memorization of Noisy Labels\"\n    authors: \"Liu, Niles-Weed, Razavian, Fernandez-Granda\"\n    year: 2020\n    venue: NeurIPS 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Formalizes early learning phenomenon: models predict true labels for mislabeled examples early in training, then memorize wrong labels. ELR regularization exploits this window.\"\n    relevance: \"Our error-injected samples may be correctly handled early in training but memorized later, degrading clean-data generalization. Explains why more epochs could worsen the gap.\"\n\n  - id: zhou2023lima\n    title: \"LIMA: Less Is More for Alignment\"\n    authors: \"Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy\"\n    year: 2023\n    venue: NeurIPS 2023\n    category: training-dynamics\n    role: background\n    key_finding: \"Superficial Alignment Hypothesis: LLM knowledge/capability comes from pretraining; SFT only teaches output style/format. Limited SFT data suffices.\"\n    relevance: \"Explains why lower SFT loss ≠ better downstream capability. Error injection improves surface-level fitting (lower loss) but doesn't enhance—and may damage—pretrained planning capability.\"\n\n  - id: luo2023catastrophic_forgetting\n    title: \"An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning\"\n    authors: \"Luo, Yang, Meng, Li, Zhou, Zhang\"\n    year: 2023\n    venue: arXiv 2308.08747\n    category: training-dynamics\n    role: background\n    key_finding: \"SFT is off-policy learning prone to overfit training distribution and forget pretraining knowledge. Forgetting severity increases with divergence between fine-tuning and pretraining distributions.\"\n    relevance: \"Error injection increases distributional gap from pretraining data, accelerating catastrophic forgetting. 50% injection → maximal divergence → most forgetting of planning capability.\"\n\n  - id: longpre2020augmentation\n    title: \"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?\"\n    authors: \"Longpre, Wang, DuBois\"\n    year: 2020\n    venue: Findings of EMNLP 2020\n    category: training-dynamics\n    role: background\n    key_finding: \"Data augmentation provides minimal benefit for pretrained transformers; pretrained representations already capture augmentation diversity. Augmentation can hurt when it introduces distribution shift.\"\n    relevance: \"Pretrained LLMs may already have robust representations; error injection adds noise without new information, explaining why augmentation-style injection fails for embodied planning.\"\n\n  # === Category: training-instability ===\n\n  - id: mccoy2020seeds\n    title: \"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance\"\n    authors: \"McCoy, Min, Linzen\"\n    year: 2020\n    venue: \"BlackboxNLP Workshop at EMNLP 2020\"\n    category: training-instability\n    role: background\n    key_finding: \"Fine-tuning 100 BERT instances on MNLI yields near-identical dev accuracy (83.6-84.8%) but wildly different syntactic generalization (0-66.2% on HANS), demonstrating extreme seed-dependent generalization.\"\n    relevance: \"与我们方差梯度发现的关系：error injection 放大了 McCoy 描述的 seed sensitivity\"\n\n  - id: mosbach2021stability\n    title: \"On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines\"\n    authors: \"Mosbach, Andriushchenko, Klakow\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    category: training-instability\n    role: background\n    key_finding: \"BERT fine-tuning instability的根因是vanishing gradients导致的优化困难，而非此前假设的catastrophic forgetting或数据集过小。\"\n    relevance: \"fine-tuning 不稳定性的基础文献，我们的 TaxEI 方差梯度扩展了这一发现到 error-augmented agent training\"\n\n  - id: damour2022underspecification\n    title: \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\"\n    authors: \"D'Amour, Heller, Moldovan, Adlam, Alipanahi, Beutel, Chen, Deaton, Eisenstein, Hoffman et al.\"\n    year: 2022\n    venue: \"Journal of Machine Learning Research, Vol. 23, No. 226\"\n    category: training-instability\n    role: background\n    key_finding: \"ML pipeline underspecification导致测试性能相当的模型在部署域行为截然不同，涵盖CV、NLP、医学等多领域实证。\"\n    relevance: \"我们的 3 seeds 中 2 个 match vanilla + 1 个 collapse 是 underspecification 的典型表现\"\n\n  # === Category: alfworld-methods ===\n\n  - id: shridhar2021alfworld\n    title: \"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\"\n    authors: \"Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht\"\n    year: 2021\n    venue: \"ICLR 2021\"\n    arxiv: \"2010.03768\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Aligns TextWorld text-based environment with ALFRED embodied benchmark, enabling abstract policy learning that transfers to visual grounding.\"\n    relevance: \"我们的实验环境；134 tasks across 6 task types benchmark\"\n\n  - id: yao2023react\n    title: \"ReAct: Synergizing Reasoning and Acting in Language Models\"\n    authors: \"Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv: \"2210.03629\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Interleaved reasoning traces and actions enable LLMs to ground decisions, achieving 75% on ALFWorld (single-trial).\"\n    relevance: \"我们使用的 prompting paradigm（ReAct format）\"\n\n  - id: shinn2023reflexion\n    title: \"Reflexion: Language Agents with Verbal Reinforcement Learning\"\n    authors: \"Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv: \"2303.11366\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Verbal self-reflection in episodic memory achieves 97% on ALFWorld (12 trials, 130/134 tasks solved) without weight updates.\"\n    relevance: \"Inference-time reflection 成功 where training-time injection 失败——对比 key point\"\n\n  - id: kim2025coex\n    title: \"CoEx -- Co-evolving World-model and Exploration\"\n    authors: \"Kim, Hwang\"\n    year: 2025\n    venue: \"Findings of EMNLP 2025\"\n    arxiv: \"2507.22281\"\n    category: alfworld-methods\n    role: evaluation\n    key_finding: \"Hierarchical state abstraction with dynamically updated neurosymbolic world model achieves 93.28% on ALFWorld.\"\n    relevance: \"ALFWorld SOTA 参考；co-evolving world model 对比我们的 static SFT 方法\"\n\n  # === Category: error-injection (补充) ===\n\n  - id: eef2025\n    title: \"Exploring Expert Failures Improves LLM Agent Tuning\"\n    authors: \"Lan, Bai, Cheng, Wang et al.\"\n    year: 2025\n    venue: \"arXiv 2504.13145\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"从失败 expert trajectories 中提取有益 actions（plans、key actions），用于引导 agent exploration，WebShop SOTA 0.81，SciWorld 81/100。\"\n    relevance: \"从失败中提取正向信号（非注入负信号），成功 on WebShop。与我们的直接注入形成对比——方向相反的 failure utilization。\"\n\n  - id: agentdebug2025\n    title: \"Where LLM Agents Fail and How They can Learn From Failures\"\n    authors: \"Zhu, Liu, Li, Tian et al.\"\n    year: 2025\n    venue: \"arXiv 2509.25370\"\n    category: error-injection\n    role: evaluation\n    key_finding: \"5-dimension AgentErrorTaxonomy（memory, reflection, planning, action, system-level）+ AgentErrorBench 标注数据集 + AgentDebug 纠错框架，跨 ALFWorld/GAIA/WebShop 提升 24% all-correct accuracy。\"\n    relevance: \"ALFWorld 的另一个 error taxonomy（5维 vs 我们的 4 operator）。对比点：不同 taxonomy 设计选择。\"\n\n  # === Category: data-mixing / curriculum (补充) ===\n\n  - id: bengio2009curriculum\n    title: \"Curriculum Learning\"\n    authors: \"Bengio, Louradour, Collobert, Weston\"\n    year: 2009\n    venue: \"ICML 2009\"\n    category: curriculum\n    role: background\n    key_finding: \"按难度递增顺序呈现训练样本可加速收敛并改善非凸优化的局部最优质量；curriculum 本质是一种 continuation method。\"\n    relevance: \"Curriculum learning 中 difficult example proportion 的 threshold 概念与我们的 dose-response 阈值平行——训练数据中困难/噪声样本超过阈值后性能崩溃\"\n\n  - id: madry2018adversarial\n    title: \"Towards Deep Learning Models Resistant to Adversarial Attacks\"\n    authors: \"Madry, Makelov, Schmidt, Tsipras, Vladu\"\n    year: 2018\n    venue: \"ICLR 2018\"\n    category: data-mixing\n    role: background\n    key_finding: \"基于 PGD 的 adversarial training 通过 robust optimization 框架显著提升对抗鲁棒性，但以 clean accuracy 下降为代价。\"\n    relevance: \"Adversarial training 的 accuracy-robustness tradeoff 是 dose-response 型——增加 adversarial perturbation 强度提升鲁棒性但降低 clean accuracy，与我们的 injection ratio vs clean eval tradeoff 结构相似\"\n",
    "structuredPatch": [
      {
        "oldStart": 294,
        "oldLines": 7,
        "newStart": 294,
        "newLines": 7,
        "lines": [
          " ",
          "   - id: eef2025",
          "     title: \"Exploring Expert Failures Improves LLM Agent Tuning\"",
          "-    authors: \"Lan, Bai, Cheng, Wang et al.\"",
          "+    authors: \"Lan, Bai, Cheng, Hsieh, Zhou\"",
          "     year: 2025",
          "     venue: \"arXiv 2504.13145\"",
          "     category: error-injection"
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

_source line 62_

Now running final verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "8e1493e8-23f8-4ebb-a4f8-feb3975ce25c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqWrsSMDe5dVV3dfbBt1Bh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1639,
      "cache_read_input_tokens": 61400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1639
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

_source line 63_

<details open><summary>🔧 Tool call — Grep · `toolu_01D28EmGN1E76LBec76G6BeM`</summary>

```json
{
  "pattern": "Various Authors",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/references.bib",
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
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "e9a334ca-8504-4278-ae45-0b26de808bc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqWrsSMDe5dVV3dfbBt1Bh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1639,
      "cache_read_input_tokens": 61400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1639
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

_source line 64 · 2026-05-15T03:55:34.063Z_

<details><summary>↩ Tool result · `toolu_01D28EmGN1E76LBec76G6BeM`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "0b5acdef-6ac6-4fb7-98a6-72e443f4ba1d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Grep · `toolu_01GsSbCs39pnMgD2ruJtyw9o`</summary>

```json
{
  "pattern": "and Others",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/references.bib",
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
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "d1c56fba-5e11-432e-8231-112547c06b82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqWrsSMDe5dVV3dfbBt1Bh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1639,
      "cache_read_input_tokens": 61400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1639
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

_source line 66 · 2026-05-15T03:55:35.000Z_

<details><summary>↩ Tool result · `toolu_01GsSbCs39pnMgD2ruJtyw9o`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "46699ff3-5c95-4a87-862d-732602382a4e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Grep · `toolu_01XXTqzV2poGNXUh3QUivuAE`</summary>

```json
{
  "pattern": "\\{[A-Z][a-z]+\\} and",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/paper/references.bib",
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
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "fbec1255-b1f4-42fa-9825-82a03b3e5df1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqWrsSMDe5dVV3dfbBt1Bh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1639,
      "cache_read_input_tokens": 61400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1639
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

_source line 68 · 2026-05-15T03:55:35.956Z_

<details><summary>↩ Tool result · `toolu_01XXTqzV2poGNXUh3QUivuAE`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "bb497c2d-ae88-4bd3-a212-c00a727c33c4",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Grep · `toolu_01Rfujmhu4RjPDgQmLZoCffW`</summary>

```json
{
  "pattern": "Various",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/literature_map.yaml",
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
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "a18914a0-a1ef-467d-a4c9-292a1a9a2da9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqWrsSMDe5dVV3dfbBt1Bh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1639,
      "cache_read_input_tokens": 61400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1639
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

_source line 70 · 2026-05-15T03:55:36.690Z_

<details><summary>↩ Tool result · `toolu_01Rfujmhu4RjPDgQmLZoCffW`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "8ad0e586-7ea6-45fb-adb8-0a11e908e2aa",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 71_

全部验证通过：

- `Various Authors` — 0 匹配
- `and Others`（大写）— 0 匹配
- 无 first name initial 的 `{Lastname}` 格式 — 0 匹配
- literature_map.yaml 中 `Various` — 0 匹配

修改摘要：

**references.bib**（3 类问题全部修复）：
1. 3 条 `{Various Authors}` 替换为 WebSearch 验证的真实作者：
   - `beyond_clean_data2024` → Freire, de S. Silva, de Andrade, Fernandes；journal 改为 `Knowledge-Based Systems`
   - `agentHER2025` → Ding, L.（单一作者，已确认）
   - `wkm2024alfworld` → Qiao, Fang, Zhang, Zhu, Chen + others（NeurIPS 2024，10 位作者）
2. 9 处 `and Others` 全部改为 `and others`（小写）
3. 所有 31 个条目的作者补全了 first name initial（格式 `{Lastname, F.}`）
4. `eef2025` 修正了错误作者 Wang → 实际为 Hsieh, C.-J. 和 Zhou, T.
5. `shinn2023reflexion` 保留 Berman — WebSearch 确认 Edward Berman 确为作者

**literature_map.yaml** 同步更新了 4 处：beyond_clean_data2024（authors + venue）、agentHER2025、wkm2024alfworld、eef2025。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "uuid": "0e74cc81-10e3-4ec9-857f-ae5da2283de6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yb9HSx3yZ6sqD5TyZwuCb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 63039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 685
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

_source line 72_

全部验证通过：

- `Various Authors` — 0 匹配
- `and Others`（大写）— 0 匹配
- 无 first name initial 的 `{Lastname}` 格式 — 0 匹配
- literature_map.yaml 中 `Various` — 0 匹配

修改摘要：

**references.bib**（3 类问题全部修复）：
1. 3 条 `{Various Authors}` 替换为 WebSearch 验证的真实作者：
   - `beyond_clean_data2024` → Freire, de S. Silva, de Andrade, Fernandes；journal 改为 `Knowledge-Based Systems`
   - `agentHER2025` → Ding, L.（单一作者，已确认）
   - `wkm2024alfworld` → Qiao, Fang, Zhang, Zhu, Chen + others（NeurIPS 2024，10 位作者）
2. 9 处 `and Others` 全部改为 `and others`（小写）
3. 所有 31 个条目的作者补全了 first name initial（格式 `{Lastname, F.}`）
4. `eef2025` 修正了错误作者 Wang → 实际为 Hsieh, C.-J. 和 Zhou, T.
5. `shinn2023reflexion` 保留 Berman — WebSearch 确认 Edward Berman 确为作者

**literature_map.yaml** 同步更新了 4 处：beyond_clean_data2024（authors + venue）、agentHER2025、wkm2024alfworld、eef2025。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 332989,
  "duration_api_ms": 372000,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "b1aaec26-7648-4997-b1ec-e4ac9d2c1193",
  "total_cost_usd": 1.29823175,
  "usage": {
    "input_tokens": 821,
    "cache_creation_input_tokens": 51883,
    "cache_read_input_tokens": 436766,
    "output_tokens": 18966,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 51883,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 447,
        "cache_read_input_tokens": 63039,
        "cache_creation_input_tokens": 685,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 685
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 157625,
      "outputTokens": 3940,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 10,
      "costUSD": 0.277325,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 821,
      "outputTokens": 18966,
      "cacheReadInputTokens": 436766,
      "cacheCreationInputTokens": 51883,
      "webSearchRequests": 0,
      "costUSD": 1.02090675,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ad0b23d5-39f1-42e7-81bc-9fbda4033943"
}
```

</details>

---
