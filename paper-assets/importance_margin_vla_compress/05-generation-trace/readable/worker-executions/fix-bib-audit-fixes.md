# fix bib audit fixes

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 116
- **Recorded user turns:** 1
- **Tool calls:** 38
- **Original source:** `logs/workers/worker_fix_bib_audit_fixes_20260528T171451.log`
- **Structured JSON:** [`116b2e79cc1110ddb1bf.json`](../../sessions/11/116b2e79cc1110ddb1bf.json)

## Before a recorded user message

30 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
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
  "uuid": "bee85c2a-b935-46f4-9624-8118894cd09f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1780003800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "712c81d7-a3ac-4765-b039-fbe4ac89d326",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Assistant

_source line 4_

Looking at the bib file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "25c5b14f-5f7a-4599-93b0-2fc0a46ba2b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYDM6BEw5csbSvDMpEQ6wK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12398,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12398
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

<details open><summary>🔧 Tool call — Glob · `toolu_01JYNDvZnmXaHsG6hQEQAAw3`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "4c7e4b75-79aa-4323-8a9c-913222759012",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYDM6BEw5csbSvDMpEQ6wK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12398,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12398
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

_source line 6 · 2026-05-28T17:15:01.027Z_

<details><summary>↩ Tool result · reported error · `toolu_01JYNDvZnmXaHsG6hQEQAAw3`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "ae6f1a3f-cc9b-45f3-95e6-689e0c398df1",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01Y37J6iEDcQEXRSDh6aP1JW`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "0709150a-9fae-44aa-8d99-ba6292d33a01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mRqVKis6Rp8PRDjPUtGfJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 227,
      "cache_read_input_tokens": 24243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 227
      },
      "output_tokens": 66,
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

_source line 8 · 2026-05-28T17:15:03.938Z_

<details><summary>↩ Tool result · `toolu_01Y37J6iEDcQEXRSDh6aP1JW`</summary>

```text
artifacts/corl_template/corl_2026_template_submission/example.bib
artifacts/corl_template/__MACOSX/corl_2026_template_submission/._example.bib
artifacts/_project/paper/new_references_8papers.bib
artifacts/new_references_8papers.bib
artifacts/missing_citations_4papers.bib
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "24edb12c-5756-4ae5-8b64-3c36d1e39620",
  "tool_use_result": {
    "filenames": [
      "artifacts/corl_template/corl_2026_template_submission/example.bib",
      "artifacts/corl_template/__MACOSX/corl_2026_template_submission/._example.bib",
      "artifacts/_project/paper/new_references_8papers.bib",
      "artifacts/new_references_8papers.bib",
      "artifacts/missing_citations_4papers.bib",
      "docs/paper/references.bib"
    ],
    "durationMs": 73,
    "numFiles": 6,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01M34Wu79N8Cg7Z2DBJzDCfW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "67693080-84f9-4b8f-924b-e03e57f8141b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RmPWTRwXTD9h8uWLQare9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 213,
      "cache_read_input_tokens": 24470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 213
      },
      "output_tokens": 71,
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

_source line 10 · 2026-05-28T17:15:06.440Z_

<details><summary>↩ Tool result · `toolu_01M34Wu79N8Cg7Z2DBJzDCfW`</summary>

```text
1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% Attention Analysis
8	% ============================================================
9	
10	@inproceedings{abnar2020quantifying,
11	  title={Quantifying Attention Flow in Transformers},
12	  author={Abnar, Samira and Zuidema, Willem},
13	  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
14	  pages={4190--4197},
15	  year={2020},
16	}
17	
18	% ============================================================
19	% VLA Token Compression (concurrent work)
20	% ============================================================
21	
22	@article{gao2025compressorvla,
23	  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
24	  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
25	  journal={arXiv preprint arXiv:2511.18950},
26	  year={2025},
27	  eprint={2511.18950},
28	  archivePrefix={arXiv}
29	}
30	
31	@article{wang2025specprunevla,
32	  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
33	  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
34	  journal={arXiv preprint arXiv:2509.05614},
35	  year={2025},
36	  eprint={2509.05614},
37	  archivePrefix={arXiv}
38	}
39	
40	@inproceedings{jiang2026lightvla,
41	  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
42	  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
43	  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
44	  year={2026},
45	  eprint={2509.12594},
46	  archivePrefix={arXiv}
47	}
48	
49	@inproceedings{feng2026seewhatmatters,
50	  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},
51	  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},
52	  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},
53	  year={2026},
54	  eprint={2605.11817},
55	  archivePrefix={arXiv}
56	}
57	
58	@inproceedings{zhang2025sparsevlm,
59	  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},
60	  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},
61	  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},
62	  year={2025},
63	  eprint={2410.04417},
64	  archivePrefix={arXiv}
65	}
66	
67	@inproceedings{khaki2025sparsevila,
68	  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},
69	  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},
70	  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
71	  year={2025},
72	  eprint={2510.17777},
73	  archivePrefix={arXiv}
74	}
75	
76	@article{jabbour2025dontrun,
77	  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},
78	  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},
79	  journal={arXiv preprint arXiv:2510.08464},
80	  year={2025},
81	  eprint={2510.08464},
82	  archivePrefix={arXiv}
83	}
84	
85	@inproceedings{li2024roboflamingo,
86	  title={Vision-Language Foundation Models as Effective Robot Imitators},
87	  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},
88	  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
89	  year={2024},
90	  eprint={2311.01378},
91	  archivePrefix={arXiv}
92	}
93	
94	% ============================================================
95	% VLA Models
96	% ============================================================
97	
98	@article{shukor2025smolvla,
99	  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},
100	  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},
101	  journal={arXiv preprint arXiv:2506.01844},
102	  year={2025}
103	}
104	
105	@inproceedings{kim2024openvla,
106	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
107	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},
108	  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},
109	  year={2024}
110	}
111	
112	@inproceedings{brohan2023rt2,
113	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
114	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},
115	  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},
116	  year={2023}
117	}
118	
119	
120	@article{black2024pi0,
121	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
122	  author={Black, Kevin and Brown, Noah and Driess, Danny and others},
123	  journal={arXiv preprint arXiv:2410.24164},
124	  year={2024}
125	}
126	
127	@article{black2025pi05,
128	  title={$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},
129	  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},
130	  journal={arXiv preprint arXiv:2504.16054},
131	  year={2025},
132	  eprint={2504.16054},
133	  archivePrefix={arXiv}
134	}
135	
136	@inproceedings{ghosh2024octo,
137	  title={Octo: An Open-Source Generalist Robot Policy},
138	  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},
139	  booktitle={Robotics: Science and Systems (RSS)},
140	  year={2024}
141	}
142	
143	@inproceedings{brohan2023rt1,
144	  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},
145	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},
146	  booktitle={Robotics: Science and Systems (RSS)},
147	  year={2023}
148	}
149	
150	
151	% ============================================================
152	% VLM/LLM Token Efficiency
153	% ============================================================
154	
155	@inproceedings{chen2024fastv,
156	  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},
157	  author={Chen, Liang and others},
158	  booktitle={European Conference on Computer Vision (ECCV)},
159	  year={2024},
160	  note={Oral presentation}
161	}
162	
163	
164	@inproceedings{xu2025vlacache,
165	  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},
166	  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},
167	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
168	  year={2025}
169	}
170	
171	@article{cheng2026vlaiap,
172	  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},
173	  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},
174	  journal={arXiv preprint arXiv:2603.22991},
175	  year={2026}
176	}
177	
178	% ============================================================
179	% ViT Token Pruning/Merging
180	% ============================================================
181	
182	@inproceedings{rao2021dynamicvit,
183	  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},
184	  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},
185	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
186	  year={2021}
187	}
188	
189	@inproceedings{bolya2023tome,
190	  title={Token Merging: Your {ViT} But Faster},
191	  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},
192	  booktitle={International Conference on Learning Representations (ICLR)},
193	  year={2023}
194	}
195	
196	@inproceedings{liang2022evit,
197	  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},
198	  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},
199	  booktitle={International Conference on Learning Representations (ICLR)},
200	  year={2022}
201	}
202	
203	% ============================================================
204	% Closed-Loop Evaluation
205	% ============================================================
206	
207	@inproceedings{liu2023libero,
208	  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
209	  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
210	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
211	  year={2023}
212	}
213	
214	
215	% ============================================================
216	% Negative Results & Evaluation Pitfalls
217	% ============================================================
218	
219	
220	% ============================================================
221	% VLA Token Efficiency (new additions)
222	% ============================================================
223	
224	@article{yang2025efficientvla,
225	  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},
226	  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},
227	  journal={arXiv preprint arXiv:2506.10100},
228	  year={2025}
229	}
230	
231	@article{liu2025vlapruner,
232	  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},
233	  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},
234	  journal={arXiv preprint arXiv:2511.16449},
235	  year={2025}
236	}
237	
238	@inproceedings{shang2024prumerge,
239	  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},
240	  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},
241	  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},
242	  year={2025}
243	}
244	
245	% ============================================================
246	% Vision Connectors
247	% ============================================================
248	
249	@inproceedings{alayrac2022flamingo,
250	  title={Flamingo: a Visual Language Model for Few-Shot Learning},
251	  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},
252	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
253	  year={2022}
254	}
255	
256	@inproceedings{liu2023llava,
257	  title={Visual Instruction Tuning},
258	  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},
259	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
260	  year={2023}
261	}
262	
263	@inproceedings{shi2016subpixel,
264	  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},
265	  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},
266	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
267	  year={2016}
268	}
269	
270	@article{chen2024internvl,
271	  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},
272	  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},
273	  journal={arXiv preprint arXiv:2404.16821},
274	  year={2024}
275	}
276	
277	% ============================================================
278	% Background / Architecture
279	% ============================================================
280	
281	@inproceedings{li2023blip2,
282	  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},
283	  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},
284	  booktitle={International Conference on Machine Learning (ICML)},
285	  year={2023}
286	}
287	
288	@inproceedings{jaegle2021perceiver,
289	  title={Perceiver: General Perception with Iterative Attention},
290	  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},
291	  booktitle={International Conference on Machine Learning (ICML)},
292	  year={2021}
293	}
294	
295	@article{oquab2023dinov2,
296	  title={{DINOv2}: Learning Robust Visual Features without Supervision},
297	  author={Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Theo and others},
298	  journal={Transactions on Machine Learning Research},
299	  year={2024}
300	}
301	
302	@inproceedings{zhai2023siglip,
303	  title={Sigmoid Loss for Language Image Pre-Training},
304	  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},
305	  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},
306	  year={2023}
307	}
308	
309	@article{yang2024qwen2,
310	  title={Qwen2 Technical Report},
311	  author={Yang, An and others},
312	  journal={arXiv preprint arXiv:2407.10671},
313	  year={2024}
314	}
315	
316	@inproceedings{lipman2023flow,
317	  title={Flow Matching for Generative Modeling},
318	  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},
319	  booktitle={International Conference on Learning Representations (ICLR)},
320	  year={2023}
321	}
322	
323	% ============================================================
324	% Additional references (Round 3 reviewer request)
325	% ============================================================
326	
327	% ============================================================
328	% Additional VLA / VLM references
329	% ============================================================
330	
331	@article{li2024cogact,
332	  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},
333	  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},
334	  journal={arXiv preprint arXiv:2411.19650},
335	  year={2024},
336	  eprint={2411.19650},
337	  archivePrefix={arXiv}
338	}
339	
340	@article{kim2025openoft,
341	  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},
342	  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},
343	  journal={arXiv preprint arXiv:2502.19645},
344	  year={2025},
345	  eprint={2502.19645},
346	  archivePrefix={arXiv}
347	}
348	
349	@article{li2024tokenpacker,
350	  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},
351	  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},
352	  journal={arXiv preprint arXiv:2407.02392},
353	  year={2024},
354	  eprint={2407.02392},
355	  archivePrefix={arXiv}
356	}
357	
358	@inproceedings{zheng2025xvla,
359	  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},
360	  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},
361	  booktitle={International Conference on Learning Representations (ICLR)},
362	  year={2026},
363	  eprint={2510.10274},
364	  archivePrefix={arXiv}
365	}
366	
367	@article{wen2024tinyvla,
368	  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},
369	  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},
370	  journal={arXiv preprint arXiv:2409.12514},
371	  year={2024},
372	  eprint={2409.12514},
373	  archivePrefix={arXiv}
374	}
375	
376	@inproceedings{lewis2020bart,
377	  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},
378	  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},
379	  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},
380	  year={2020}
381	}
382	
383	% ============================================================
384	% New additions for expanded Related Work
385	% ============================================================
386	
387	@inproceedings{ryoo2021tokenlearner,
388	  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},
389	  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},
390	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
391	  year={2021},
392	  eprint={2106.11297},
393	  archivePrefix={arXiv}
394	}
395	
396	@inproceedings{yin2022avit,
397	  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},
398	  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},
399	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
400	  year={2022},
401	  eprint={2112.07658},
402	  archivePrefix={arXiv}
403	}
404	
405	@inproceedings{meng2022adavit,
406	  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},
407	  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},
408	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
409	  year={2022},
410	  eprint={2111.15668},
411	  archivePrefix={arXiv}
412	}
413	
414	@inproceedings{chen2023sparsevit,
415	  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},
416	  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},
417	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
418	  year={2023},
419	  eprint={2303.17605},
420	  archivePrefix={arXiv}
421	}
422	
423	@inproceedings{ye2025fitprune,
424	  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},
425	  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},
426	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
427	  year={2025},
428	  eprint={2409.10197},
429	  archivePrefix={arXiv}
430	}
431	
432	@inproceedings{shi2024crossget,
433	  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},
434	  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},
435	  booktitle={International Conference on Machine Learning (ICML)},
436	  year={2024},
437	  eprint={2305.17455},
438	  archivePrefix={arXiv}
439	}
440	
441	@article{zhang2024fastervlm,
442	  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},
443	  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},
444	  journal={arXiv preprint arXiv:2412.01818},
445	  year={2024},
446	  eprint={2412.01818},
447	  archivePrefix={arXiv}
448	}
449	
450	@inproceedings{liu2024llava15,
451	  title={Improved Baselines with Visual Instruction Tuning},
452	  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},
453	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
454	  year={2024},
455	  eprint={2310.03744},
456	  archivePrefix={arXiv}
457	}
458	
459	@article{chen2024internvl25,
460	  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},
461	  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},
462	  journal={arXiv preprint arXiv:2412.05271},
463	  year={2024},
464	  eprint={2412.05271},
465	  archivePrefix={arXiv}
466	}
467	
468	@article{gao2024miniinternvl,
469	  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\% Parameters and 90\% Performance},
470	  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},
471	  journal={arXiv preprint arXiv:2410.16261},
472	  year={2024},
473	  eprint={2410.16261},
474	  archivePrefix={arXiv}
475	}
476	
477	% ============================================================
478	% Synced from literature_map.yaml (missing entries)
479	% ============================================================
480	
481	% --- VLA Models ---
482	
483	@inproceedings{zitkovich2023rt2,
484	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
485	  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},
486	  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},
487	  year={2023},
488	  eprint={2307.15818},
489	  archivePrefix={arXiv}
490	}
491	
492	@inproceedings{openxembodiment2024,
493	  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},
494	  author={{Open X-Embodiment Collaboration}},
495	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
496	  year={2024},
497	  eprint={2310.08864},
498	  archivePrefix={arXiv}
499	}
500	
501	% --- VLM/LLM Token Efficiency ---
502	
503	@inproceedings{zhang2023h2o,
504	  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
505	  author={Zhang, Zhenyu and others},
506	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
507	  year={2023},
508	  eprint={2306.14048},
509	  archivePrefix={arXiv}
510	}
511	
512	@inproceedings{xiao2024streamingllm,
513	  title={Efficient Streaming Language Models with Attention Sinks},
514	  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},
515	  booktitle={International Conference on Learning Representations (ICLR)},
516	  year={2024},
517	  eprint={2309.17453},
518	  archivePrefix={arXiv}
519	}
520	
521	
522	% --- Closed-Loop Evaluation ---
523	
524	@article{mees2022calvin,
525	  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},
526	  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},
527	  journal={IEEE Robotics and Automation Letters},
528	  year={2022},
529	  eprint={2112.03227},
530	  archivePrefix={arXiv}
531	}
532	
533	@inproceedings{chi2023diffusionpolicy,
534	  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
535	  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
536	  booktitle={Robotics: Science and Systems (RSS)},
537	  year={2023},
538	  eprint={2303.04137},
539	  archivePrefix={arXiv}
540	}
541	
542	% --- Negative Results & Evaluation Pitfalls ---
543	
544	@inproceedings{zeng2023transformers_tsf,
545	  title={Are Transformers Effective for Time Series Forecasting?},
546	  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},
547	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
548	  year={2023},
549	  eprint={2205.13504},
550	  archivePrefix={arXiv}
551	}
552	
553	@inproceedings{bouthillier2024negative,
554	  title={Position: Embracing Negative Results in Machine Learning},
555	  author={Bouthillier, Xavier and others},
556	  booktitle={International Conference on Machine Learning (ICML)},
557	  year={2024},
558	  eprint={2406.03980},
559	  archivePrefix={arXiv}
560	}
561	
562	% --- Vision Connectors & Token Compression ---
563	
564	@article{oquab2024dinov2,
565	  title={{DINOv2}: Learning Robust Visual Features without Supervision},
566	  author={Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Theo and others},
567	  journal={Transactions on Machine Learning Research},
568	  year={2024},
569	  eprint={2304.07193},
570	  archivePrefix={arXiv}
571	}
572	
573	@article{su2024roformer,
574	  title={{RoFormer}: Enhanced Transformer with Rotary Position Embedding},
575	  author={Su, Jianlin and Ahmed, Murtadha and Lu, Yu and Pan, Shengfeng and Bo, Wen and Liu, Yunfeng},
576	  journal={Neurocomputing},
577	  volume={568},
578	  pages={127063},
579	  year={2024},
580	  publisher={Elsevier}
581	}
582	
583	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "41475f69-57ee-4d04-94be-921f6d0d8cb4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
      "content": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% Attention Analysis\n% ============================================================\n\n@inproceedings{abnar2020quantifying,\n  title={Quantifying Attention Flow in Transformers},\n  author={Abnar, Samira and Zuidema, Willem},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={4190--4197},\n  year={2020},\n}\n\n% ============================================================\n% VLA Token Compression (concurrent work)\n% ============================================================\n\n@article{gao2025compressorvla,\n  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},\n  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},\n  journal={arXiv preprint arXiv:2511.18950},\n  year={2025},\n  eprint={2511.18950},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025specprunevla,\n  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},\n  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},\n  journal={arXiv preprint arXiv:2509.05614},\n  year={2025},\n  eprint={2509.05614},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{jiang2026lightvla,\n  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},\n  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},\n  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2026},\n  eprint={2509.12594},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{feng2026seewhatmatters,\n  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},\n  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},\n  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},\n  year={2026},\n  eprint={2605.11817},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zhang2025sparsevlm,\n  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},\n  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},\n  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},\n  year={2025},\n  eprint={2410.04417},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{khaki2025sparsevila,\n  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},\n  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025},\n  eprint={2510.17777},\n  archivePrefix={arXiv}\n}\n\n@article{jabbour2025dontrun,\n  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},\n  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},\n  journal={arXiv preprint arXiv:2510.08464},\n  year={2025},\n  eprint={2510.08464},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{li2024roboflamingo,\n  title={Vision-Language Foundation Models as Effective Robot Imitators},\n  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2311.01378},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt1,\n  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}\n\n\n@inproceedings{xu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cheng2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n\n% ============================================================\n% VLA Token Efficiency (new additions)\n% ============================================================\n\n@article{yang2025efficientvla,\n  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},\n  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},\n  journal={arXiv preprint arXiv:2506.10100},\n  year={2025}\n}\n\n@article{liu2025vlapruner,\n  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},\n  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},\n  journal={arXiv preprint arXiv:2511.16449},\n  year={2025}\n}\n\n@inproceedings{shang2024prumerge,\n  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},\n  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025}\n}\n\n% ============================================================\n% Vision Connectors\n% ============================================================\n\n@inproceedings{alayrac2022flamingo,\n  title={Flamingo: a Visual Language Model for Few-Shot Learning},\n  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2022}\n}\n\n@inproceedings{liu2023llava,\n  title={Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{shi2016subpixel,\n  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},\n  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2016}\n}\n\n@article{chen2024internvl,\n  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},\n  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2404.16821},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{li2023blip2,\n  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},\n  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@inproceedings{jaegle2021perceiver,\n  title={Perceiver: General Perception with Iterative Attention},\n  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2021}\n}\n\n@article{oquab2023dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ============================================================\n% Additional references (Round 3 reviewer request)\n% ============================================================\n\n% ============================================================\n% Additional VLA / VLM references\n% ============================================================\n\n@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2510.10274},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{lewis2020bart,\n  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},\n  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},\n  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2020}\n}\n\n% ============================================================\n% New additions for expanded Related Work\n% ============================================================\n\n@inproceedings{ryoo2021tokenlearner,\n  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},\n  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021},\n  eprint={2106.11297},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{yin2022avit,\n  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},\n  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2112.07658},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{meng2022adavit,\n  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},\n  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2111.15668},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chen2023sparsevit,\n  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},\n  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2023},\n  eprint={2303.17605},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ye2025fitprune,\n  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},\n  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  eprint={2409.10197},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{shi2024crossget,\n  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},\n  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2305.17455},\n  archivePrefix={arXiv}\n}\n\n@article{zhang2024fastervlm,\n  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},\n  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},\n  journal={arXiv preprint arXiv:2412.01818},\n  year={2024},\n  eprint={2412.01818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{liu2024llava15,\n  title={Improved Baselines with Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2024},\n  eprint={2310.03744},\n  archivePrefix={arXiv}\n}\n\n@article{chen2024internvl25,\n  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},\n  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2412.05271},\n  year={2024},\n  eprint={2412.05271},\n  archivePrefix={arXiv}\n}\n\n@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% Synced from literature_map.yaml (missing entries)\n% ============================================================\n\n% --- VLA Models ---\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023},\n  eprint={2307.15818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024},\n  eprint={2310.08864},\n  archivePrefix={arXiv}\n}\n\n% --- VLM/LLM Token Efficiency ---\n\n@inproceedings{zhang2023h2o,\n  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  eprint={2306.14048},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2309.17453},\n  archivePrefix={arXiv}\n}\n\n\n% --- Closed-Loop Evaluation ---\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022},\n  eprint={2112.03227},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023},\n  eprint={2303.04137},\n  archivePrefix={arXiv}\n}\n\n% --- Negative Results & Evaluation Pitfalls ---\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2023},\n  eprint={2205.13504},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2406.03980},\n  archivePrefix={arXiv}\n}\n\n% --- Vision Connectors & Token Compression ---\n\n@article{oquab2024dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024},\n  eprint={2304.07193},\n  archivePrefix={arXiv}\n}\n\n@article{su2024roformer,\n  title={{RoFormer}: Enhanced Transformer with Rotary Position Embedding},\n  author={Su, Jianlin and Ahmed, Murtadha and Lu, Yu and Pan, Shengfeng and Bo, Wen and Liu, Yunfeng},\n  journal={Neurocomputing},\n  volume={568},\n  pages={127063},\n  year={2024},\n  publisher={Elsevier}\n}\n\n",
      "numLines": 583,
      "startLine": 1,
      "totalLines": 583
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full bib file. Let me identify the three items to fix:

1. **`zheng2025xvla`** (line 358-365): Author "Zheng, Yifu" should be "Zheng, Jinliang"
2. **`chen2024fastv`** (line 155-161): Only has "Chen, Liang and others" — need to find full author list
3. **`black2025pi05`** (line 127-134): Still marked as arXiv preprint, needs CoRL 2025 format


I need to look up the complete author information for the FastV paper and verify the CoRL 2025 publication details for the pi0.5 entry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "82b79fe6-4494-48a4-814b-b067948fe5f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RaivW2viSmBAm6mDLs1s3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9435,
      "cache_read_input_tokens": 24683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9435
      },
      "output_tokens": 9,
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

_source line 12_

Found the bib file. Now searching for the missing information for items 2 and 3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "bf29d22c-98da-48c1-a312-0b149a3a2e3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RaivW2viSmBAm6mDLs1s3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9435,
      "cache_read_input_tokens": 24683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9435
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HDTZeiw7xpDrmZjesUwucP`</summary>

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
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "efa737f0-6b97-454f-8d32-60b2e143e9a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RaivW2viSmBAm6mDLs1s3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9435,
      "cache_read_input_tokens": 24683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9435
      },
      "output_tokens": 9,
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

_source line 14 · 2026-05-28T17:15:14.079Z_

<details><summary>↩ Tool result · `toolu_01HDTZeiw7xpDrmZjesUwucP`</summary>

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
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "034386aa-1603-4fec-a876-cccccf37df11",
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

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the FastV paper authors and the pi0.5 CoRL 2025 publication details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "2a337273-81e8-466e-9d89-aad0bc319c47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013g7BRASJmz3LUETJiD3zE4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 34118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 796
      },
      "output_tokens": 58,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0113dkhYw8TsQyHrxKe9mVW2`</summary>

```json
{
  "query": "FastV \"An Image is Worth 1/2 Tokens After Layer 2\" ECCV 2024 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "87a66ed4-0f2d-46be-b527-13078905b2dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013g7BRASJmz3LUETJiD3zE4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 34118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 796
      },
      "output_tokens": 58,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LmG2bhKg1kNz37VJmsXS6K`</summary>

```json
{
  "query": "pi0.5 \"pi_{0.5}\" black 2025 CoRL PMLR 305 proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "0deeadc2-6fb7-4292-87e4-a34d9954e311",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013g7BRASJmz3LUETJiD3zE4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 34118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 796
      },
      "output_tokens": 58,
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

_source line 18 · 2026-05-28T17:15:23.710Z_

<details><summary>↩ Tool result · `toolu_01LmG2bhKg1kNz37VJmsXS6K`</summary>

```text
Web search results for query: "pi0.5 "pi_{0.5}" black 2025 CoRL PMLR 305 proceedings"

Links: [{"title":"GitHub - mlresearch/v305: Proceedings of CoRL 2025 · GitHub","url":"https://github.com/mlresearch/v305"},{"title":"CoRL 2025 - Awards","url":"https://2025.corl.org/program/awards"},{"title":"CoRL 2025 Survey - Speaker Deck","url":"https://speakerdeck.com/harukiabe/corl-2025-survey"},{"title":"GitHub - UT-Austin-RPL/openreview-to-pmlr: Making PMLR Proceedings from CoRL OpenReview Data · GitHub","url":"https://github.com/UT-Austin-RPL/openreview-to-pmlr"},{"title":"CoRL Papers Published in Proceedings of Machine Learning - News/Research - Berkeley Center for New Media","url":"https://bcnm.berkeley.edu/news-research/5515/corl-papers-published-in-proceedings-of-machine-learning"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/pdf/2512.06951"},{"title":"Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies","url":"https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"},{"title":"Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and associated with a particular workshop or conference. Volumes are published online on the PMLR web site. The Series Editors are Neil D. Lawrence and Mark Reid.","url":"https://proceedings.mlr.press/"},{"title":"Journal and Conference Papers","url":"http://rl.cs.rutgers.edu/publications.html"}]

Based on the search results, I found relevant information about your query:

Pi 0.5 is "a Vision-Language-Action Model with Open-World Generalization" with Kevin Black as one of the lead authors. This work was published as Volume 305 by the Proceedings of Machine Learning Research (PMLR) on October 7, 2025, which corresponds to the CoRL 2025 proceedings.

The paper appears to be a significant contribution to robot learning, as π0.5 is mentioned as a notable example of Vision-Language-Action models in recent CoRL research trends.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "236af28b-3767-4020-8edf-24a6bd418738",
  "tool_use_result": {
    "query": "pi0.5 \"pi_{0.5}\" black 2025 CoRL PMLR 305 proceedings",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CnsN4k6E6tKv3EBYLtSe28",
        "content": [
          {
            "title": "GitHub - mlresearch/v305: Proceedings of CoRL 2025 · GitHub",
            "url": "https://github.com/mlresearch/v305"
          },
          {
            "title": "CoRL 2025 - Awards",
            "url": "https://2025.corl.org/program/awards"
          },
          {
            "title": "CoRL 2025 Survey - Speaker Deck",
            "url": "https://speakerdeck.com/harukiabe/corl-2025-survey"
          },
          {
            "title": "GitHub - UT-Austin-RPL/openreview-to-pmlr: Making PMLR Proceedings from CoRL OpenReview Data · GitHub",
            "url": "https://github.com/UT-Austin-RPL/openreview-to-pmlr"
          },
          {
            "title": "CoRL Papers Published in Proceedings of Machine Learning - News/Research - Berkeley Center for New Media",
            "url": "https://bcnm.berkeley.edu/news-research/5515/corl-papers-published-in-proceedings-of-machine-learning"
          },
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/pdf/2512.06951"
          },
          {
            "title": "Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies",
            "url": "https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"
          },
          {
            "title": "Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and associated with a particular workshop or conference. Volumes are published online on the PMLR web site. The Series Editors are Neil D. Lawrence and Mark Reid.",
            "url": "https://proceedings.mlr.press/"
          },
          {
            "title": "Journal and Conference Papers",
            "url": "http://rl.cs.rutgers.edu/publications.html"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query:\n\nPi 0.5 is \"a Vision-Language-Action Model with Open-World Generalization\" with Kevin Black as one of the lead authors. This work was published as Volume 305 by the Proceedings of Machine Learning Research (PMLR) on October 7, 2025, which corresponds to the CoRL 2025 proceedings.\n\nThe paper appears to be a significant contribution to robot learning, as π0.5 is mentioned as a notable example of Vision-Language-Action models in recent CoRL research trends."
    ],
    "durationSeconds": 4.797269358999998
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T17:15:24.015Z_

<details><summary>↩ Tool result · `toolu_0113dkhYw8TsQyHrxKe9mVW2`</summary>

```text
Web search results for query: "FastV "An Image is Worth 1/2 Tokens After Layer 2" ECCV 2024 full author list"

Links: [{"title":"GitHub - MachineLearningSystem/24ECCV-FastV: [ECCV 2024] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/MachineLearningSystem/24ECCV-FastV"},{"title":"GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/pkunlp-icler/FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Computer Vision – ECCV 2024","url":"https://dl.acm.org/doi/10.1007/978-3-031-73004-7_2"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764"},{"title":"GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/chenllliang/FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference","url":"https://arxiv.org/html/2403.06764v3"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference   Acceleration for Large Vision-Language Models","url":"https://arxiv.org/pdf/2403.06764"},{"title":"[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"}]

Based on the search results, I found the full author list for the FastV paper. The authors are: Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, and Baobao Chang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "b4e435f1-62ae-41c7-8652-b06cd49eba37",
  "tool_use_result": {
    "query": "FastV \"An Image is Worth 1/2 Tokens After Layer 2\" ECCV 2024 full author list",
    "results": [
      {
        "tool_use_id": "srvtoolu_012bCBChFVXohAyTe82HLqDz",
        "content": [
          {
            "title": "GitHub - MachineLearningSystem/24ECCV-FastV: [ECCV 2024] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub",
            "url": "https://github.com/MachineLearningSystem/24ECCV-FastV"
          },
          {
            "title": "GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub",
            "url": "https://github.com/pkunlp-icler/FastV"
          },
          {
            "title": "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Computer Vision – ECCV 2024",
            "url": "https://dl.acm.org/doi/10.1007/978-3-031-73004-7_2"
          },
          {
            "title": "[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models",
            "url": "https://arxiv.org/abs/2403.06764"
          },
          {
            "title": "GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub",
            "url": "https://github.com/chenllliang/FastV"
          },
          {
            "title": "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference",
            "url": "https://arxiv.org/html/2403.06764v3"
          },
          {
            "title": "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference   Acceleration for Large Vision-Language Models",
            "url": "https://arxiv.org/pdf/2403.06764"
          },
          {
            "title": "[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"
          }
        ]
      },
      "Based on the search results, I found the full author list for the FastV paper. The authors are: Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, and Baobao Chang."
    ],
    "durationSeconds": 5.945481693999998
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Let me get more specific details about the pi0.5 paper in CoRL 2025 proceedings - I need the exact pages, volume number, etc.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "1394eac4-67dc-47c5-8864-75b1384e33b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S38rKeGLxVBmXw7Rp7T4dU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 693,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 34914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 940
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013nUu4ZwTtcUzQme2y6AruQ`</summary>

```json
{
  "query": "site:proceedings.mlr.press \"pi_{0.5}\" OR \"pi0.5\" v305"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "2735af15-bbae-4433-bf14-2f9412fbfb04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S38rKeGLxVBmXw7Rp7T4dU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 693,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 34914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 940
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FGmABZzkNLjkKu5gfGKCDb`</summary>

```json
{
  "query": "arxiv 2403.06764 FastV authors \"Liang Chen\" \"Haozhe Zhao\" \"Tianyu Liu\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "0476c397-5699-41dc-8fa8-e7c3a0bc6ca1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S38rKeGLxVBmXw7Rp7T4dU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 693,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 34914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 940
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

_source line 23 · 2026-05-28T17:15:32.734Z_

<details><summary>↩ Tool result · `toolu_01FGmABZzkNLjkKu5gfGKCDb`</summary>

```text
Web search results for query: "arxiv 2403.06764 FastV authors "Liang Chen" "Haozhe Zhao" "Tianyu Liu""

Links: [{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/html/2403.06764v1"},{"title":"Paper page - An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://huggingface.co/papers/2403.06764"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"http://export.arxiv.org/abs/2403.06764"},{"title":"GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/chenllliang/FastV"},{"title":"GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/pkunlp-icler/FastV"},{"title":"FastV: Plug-and-Play LVLM Inference Acceleration","url":"https://www.emergentmind.com/papers/2403.06764"},{"title":"[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference","url":"https://arxiv.org/html/2403.06764v3"}]

Based on the search results, I found the paper arxiv:2403.06764 titled "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models."

The authors are Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, and Baobao Chang.

FastV is a versatile plug-and-play method designed to optimize computational efficiency by learning adaptive attention patterns in early layers and pruning visual tokens in subsequent ones. The method can dramatically reduce computational costs (e.g., a 45% reduction in FLOPs for LLaVA-1.5-13B) without sacrificing performance in a wide range of image and video understanding tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "0f9c7912-8778-4852-831d-d1806c40373a",
  "tool_use_result": {
    "query": "arxiv 2403.06764 FastV authors \"Liang Chen\" \"Haozhe Zhao\" \"Tianyu Liu\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NFTZT4fRuPyCtcMJANmKi3",
        "content": [
          {
            "title": "[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models",
            "url": "https://arxiv.org/abs/2403.06764"
          },
          {
            "title": "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models",
            "url": "https://arxiv.org/html/2403.06764v1"
          },
          {
            "title": "Paper page - An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models",
            "url": "https://huggingface.co/papers/2403.06764"
          },
          {
            "title": "[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models",
            "url": "http://export.arxiv.org/abs/2403.06764"
          },
          {
            "title": "GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub",
            "url": "https://github.com/chenllliang/FastV"
          },
          {
            "title": "GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub",
            "url": "https://github.com/pkunlp-icler/FastV"
          },
          {
            "title": "FastV: Plug-and-Play LVLM Inference Acceleration",
            "url": "https://www.emergentmind.com/papers/2403.06764"
          },
          {
            "title": "[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"
          },
          {
            "title": "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference",
            "url": "https://arxiv.org/html/2403.06764v3"
          }
        ]
      },
      "Based on the search results, I found the paper arxiv:2403.06764 titled \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models.\"\n\nThe authors are Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, and Baobao Chang.\n\nFastV is a versatile plug-and-play method designed to optimize computational efficiency by learning adaptive attention patterns in early layers and pruning visual tokens in subsequent ones. The method can dramatically reduce computational costs (e.g., a 45% reduction in FLOPs for LLaVA-1.5-13B) without sacrificing performance in a wide range of image and video understanding tasks."
    ],
    "durationSeconds": 4.239082326000004
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T17:15:34.025Z_

<details><summary>↩ Tool result · `toolu_013nUu4ZwTtcUzQme2y6AruQ`</summary>

```text
Web search results for query: "site:proceedings.mlr.press "pi_{0.5}" OR "pi0.5" v305"

Links: [{"title":"$\\pi_0.5$: a Vision-Language-Action Model with Open-World Generalization","url":"https://proceedings.mlr.press/v305/black25a.html"},{"title":"Sample-Efficient Online Control Policy Learning with Real-Time Recursive Model Updates","url":"https://proceedings.mlr.press/v305/zhang25d.html"},{"title":"Learning Long-Context Diffusion Policies via Past-Token Prediction","url":"https://proceedings.mlr.press/v305/villasevil25a.html"},{"title":"Meta-Optimization and Program Search using Language Models for Task and Motion Planning","url":"https://proceedings.mlr.press/v305/shcherba25a.html"},{"title":"About | Proceedings of Machine Learning Research - mlr.press","url":"https://proceedings.mlr.press/about/"},{"title":"A mixture representation of \\pi with applications in Markov chain Monte   Carlo and perfect sampling","url":"https://arxiv.org/pdf/math/0407120"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 9th Conference on Robot Learning Held in Seoul, Korea on 27-30 September 2025 Published as Volume 305 by the Proceedings of Machine Learning Research on 07 October 2025. Volume Edited by: Joseph Lim Shuran Song Hae-Won Park Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v305/"},{"title":"Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and associated with a particular workshop or conference. Volumes are published online on the PMLR web site. The Series Editors are Neil D. Lawrence and Mark Reid.","url":"https://proceedings.mlr.press/"}]

The search was successful! I found the paper you were looking for:

**π₀.₅: a Vision-Language-Action Model with Open-World Generalization** was published in Proceedings of The 9th Conference on Robot Learning, PMLR 305:17-40, 2025.

The model uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. π₀.₅ is based on π₀ and uses co-training on heterogeneous tasks to enable broad generalization.

The full paper is available at: https://proceedings.mlr.press/v305/black25a.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "b300905f-6852-4781-acee-e5ae7889e45e",
  "tool_use_result": {
    "query": "site:proceedings.mlr.press \"pi_{0.5}\" OR \"pi0.5\" v305",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CwfahQ3hnZWPqe7xqovPZF",
        "content": [
          {
            "title": "$\\pi_0.5$: a Vision-Language-Action Model with Open-World Generalization",
            "url": "https://proceedings.mlr.press/v305/black25a.html"
          },
          {
            "title": "Sample-Efficient Online Control Policy Learning with Real-Time Recursive Model Updates",
            "url": "https://proceedings.mlr.press/v305/zhang25d.html"
          },
          {
            "title": "Learning Long-Context Diffusion Policies via Past-Token Prediction",
            "url": "https://proceedings.mlr.press/v305/villasevil25a.html"
          },
          {
            "title": "Meta-Optimization and Program Search using Language Models for Task and Motion Planning",
            "url": "https://proceedings.mlr.press/v305/shcherba25a.html"
          },
          {
            "title": "About | Proceedings of Machine Learning Research - mlr.press",
            "url": "https://proceedings.mlr.press/about/"
          },
          {
            "title": "A mixture representation of \\pi with applications in Markov chain Monte   Carlo and perfect sampling",
            "url": "https://arxiv.org/pdf/math/0407120"
          },
          {
            "title": "Proceedings of Machine Learning Research | Proceedings of The 9th Conference on Robot Learning Held in Seoul, Korea on 27-30 September 2025 Published as Volume 305 by the Proceedings of Machine Learning Research on 07 October 2025. Volume Edited by: Joseph Lim Shuran Song Hae-Won Park Series Editors: Neil D. Lawrence",
            "url": "https://proceedings.mlr.press/v305/"
          },
          {
            "title": "Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and associated with a particular workshop or conference. Volumes are published online on the PMLR web site. The Series Editors are Neil D. Lawrence and Mark Reid.",
            "url": "https://proceedings.mlr.press/"
          }
        ]
      },
      "The search was successful! I found the paper you were looking for:\n\n**π₀.₅: a Vision-Language-Action Model with Open-World Generalization** was published in Proceedings of The 9th Conference on Robot Learning, PMLR 305:17-40, 2025.\n\nThe model uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. π₀.₅ is based on π₀ and uses co-training on heterogeneous tasks to enable broad generalization.\n\nThe full paper is available at: https://proceedings.mlr.press/v305/black25a.html"
    ],
    "durationSeconds": 6.018717355999994
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I have:

1. **`zheng2025xvla`**: Change "Zheng, Yifu" to "Zheng, Jinliang"
2. **`chen2024fastv`**: Full author list: Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, Baobao Chang
3. **`black2025pi05`**: Published at CoRL 2025, PMLR 305, pages 17-40. URL: https://proceedings.mlr.press/v305/black25a.html


4. I've confirmed the page range for pi0.5 is 17-40 from PMLR 305. Now I need to check which .tex files cite which bib entries to identify any orphan entries, then make the three edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "e16d91d6-b44b-4329-9fc3-c7bebeb71a0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9KrcBaB8UNnS6Dr2S4m4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 1679,
      "cache_read_input_tokens": 35854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1679
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

_source line 26_

Got all the information needed. Now let me also find orphan entries by checking which bib keys are cited in the tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "c6c1522e-7fe9-4e5a-bcc2-529c7c6ca6e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9KrcBaB8UNnS6Dr2S4m4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 1679,
      "cache_read_input_tokens": 35854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1679
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

_source line 27_

<details open><summary>🔧 Tool call — Glob · `toolu_01Xi6ycPj7FikQpyLtsXjKvB`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "2442a84c-ff80-4d44-bbdc-033814d49bc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9KrcBaB8UNnS6Dr2S4m4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 1679,
      "cache_read_input_tokens": 35854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1679
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

_source line 28 · 2026-05-28T17:15:44.908Z_

<details><summary>↩ Tool result · `toolu_01Xi6ycPj7FikQpyLtsXjKvB`</summary>

```text
docs/paper/sections/analysis.tex
docs/paper/sections/background.tex
docs/paper/sections/experimental_setup.tex
docs/paper/sections/results_draft.tex
docs/paper/sections/analysis_draft.tex
docs/paper/experiments_deprecated.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work_draft.tex
docs/paper/sections/introduction.tex
docs/paper/background.tex
docs/paper/results_v2.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/discussion.tex
docs/paper/analysis.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/appendix.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/main.tex
docs/paper/experiments.tex
docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "32b28dac-bf6f-45fa-ae96-4738e58bd119",
  "tool_use_result": {
    "filenames": [
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/background.tex",
      "docs/paper/sections/experimental_setup.tex",
      "docs/paper/sections/results_draft.tex",
      "docs/paper/sections/analysis_draft.tex",
      "docs/paper/experiments_deprecated.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/sections/related_work_draft.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/background.tex",
      "docs/paper/results_v2.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/results.tex",
      "docs/paper/discussion.tex",
      "docs/paper/analysis.tex",
      "docs/paper/introduction.tex",
      "docs/paper/related_work.tex",
      "docs/paper/abstract.tex",
      "docs/paper/appendix.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/limitations.tex",
      "docs/paper/main.tex",
      "docs/paper/experiments.tex",
      "docs/paper/method.tex"
    ],
    "durationMs": 9,
    "numFiles": 24,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Agent · `toolu_015B9d2e5a4oUdbnmPjscqUY`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find all cited bib keys in tex",
  "prompt": "I need to find ALL citation keys referenced in .tex files under /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/. \n\nSearch for all occurrences of \\cite{...}, \\citep{...}, \\citet{...}, and similar citation commands across all .tex files. Extract just the citation keys (the text inside the braces). Note that a single \\cite command can contain multiple comma-separated keys like \\cite{key1,key2}.\n\nReport a deduplicated sorted list of all citation keys found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "c12b4914-c7fd-4ecf-9443-885a44a57d3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYPS3ZLbuiQCdsxRPdUHGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1527,
      "cache_read_input_tokens": 37533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1527
      },
      "output_tokens": 52,
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
  "subtype": "task_started",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Find all cited bib keys in tex",
  "task_type": "local_agent",
  "prompt": "I need to find ALL citation keys referenced in .tex files under /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/. \n\nSearch for all occurrences of \\cite{...}, \\citep{...}, \\citet{...}, and similar citation commands across all .tex files. Extract just the citation keys (the text inside the braces). Note that a single \\cite command can contain multiple comma-separated keys like \\cite{key1,key2}.\n\nReport a deduplicated sorted list of all citation keys found.",
  "uuid": "2706c40a-e4e3-493b-b65a-1cb17e13ed7c",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

## Round 1

86 recorded events

### User

_source line 31 · 2026-05-28T17:15:50.783Z_

I need to find ALL citation keys referenced in .tex files under /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/. 

Search for all occurrences of \cite{...}, \citep{...}, \citet{...}, and similar citation commands across all .tex files. Extract just the citation keys (the text inside the braces). Note that a single \cite command can contain multiple comma-separated keys like \cite{key1,key2}.

Report a deduplicated sorted list of all citation keys found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "247194c5-5f37-4866-83af-c6409e562695"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Finding /home/ubuntu/.agent-ml-research-be-idea-gen-0515-…",
  "usage": {
    "total_tokens": 17912,
    "tool_uses": 1,
    "duration_ms": 5827
  },
  "last_tool_name": "Glob",
  "uuid": "319fa79a-c5ec-4cac-a66a-0514fda280b5",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Glob · `toolu_01BC12kbXkKZ8qgnqGci9xzX`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "698781e5-c36b-414c-8421-4fce56175cbe",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01U2QiW8a72H8NLzP4Mx8btf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17895,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17895,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 34 · 2026-05-28T17:15:56.634Z_

<details><summary>↩ Tool result · `toolu_01BC12kbXkKZ8qgnqGci9xzX`</summary>

```text
docs/paper/sections/analysis.tex
docs/paper/sections/background.tex
docs/paper/sections/experimental_setup.tex
docs/paper/sections/results_draft.tex
docs/paper/sections/analysis_draft.tex
docs/paper/experiments_deprecated.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work_draft.tex
docs/paper/sections/introduction.tex
docs/paper/background.tex
docs/paper/results_v2.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/discussion.tex
docs/paper/analysis.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/appendix.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/main.tex
docs/paper/experiments.tex
docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "3cebf464-d1f3-45bb-8c98-dc6ffee9fc6a"
}
```

</details>

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Searching for \\\\cite[tp]*\\{[^}]+\\}",
  "usage": {
    "total_tokens": 19099,
    "tool_uses": 2,
    "duration_ms": 8714
  },
  "last_tool_name": "Grep",
  "uuid": "85372e7a-9dbe-48ee-8846-e2fba3de9ad9",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Grep · `toolu_01MpHFdJF6cp3R1cC4oympNJ`</summary>

```json
{
  "pattern": "\\\\cite[tp]*\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "f297abd6-b224-4c9d-8ae7-70f8c17803d3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015J6tEBhFYTCikp7nBUtcDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 17895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1183,
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

_source line 37 · 2026-05-28T17:15:59.525Z_

<details><summary>↩ Tool result · `toolu_01MpHFdJF6cp3R1cC4oympNJ`</summary>

```text
&lt;persisted-output>
Output too large (20.7KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5fcbbc8f-a94c-480e-bf9e-7ce4eca56009/tool-results/toolu_01MpHFdJF6cp3R1cC4oympNJ.txt

Preview (first 2KB):
docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
docs/paper/related_work.tex:8:[Omitted long matching line]
docs/paper/related_work.tex:11:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
docs/paper/experiments.tex:7:We evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\times$ 50 episodes each).
docs/paper/experiments.tex:9:[Omitted long matching line]
docs/paper/results_v2.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
docs/paper/results_v2.tex:9:[Omitted long matching line]
docs/paper/results_v2.tex:11:[Omitted long matching line]
docs/paper/results_v2.tex:16:[Omitted long matching line]
docs/paper/results_v2.tex:22:$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "23405996-dd92-4395-9df2-ced2d756f24e"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading ~/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5fcbbc8f-a94c-480e-bf9e-7ce4eca56009/tool-results/toolu_01MpHFdJF6cp3R1cC4oympNJ.txt",
  "usage": {
    "total_tokens": 20028,
    "tool_uses": 3,
    "duration_ms": 10860
  },
  "last_tool_name": "Read",
  "uuid": "b6f4a166-38f0-4f63-8a81-84cfcd13a741",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01Cm9Pyd4o2Qo3cajFvweffH`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5fcbbc8f-a94c-480e-bf9e-7ce4eca56009/tool-results/toolu_01MpHFdJF6cp3R1cC4oympNJ.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "8f25ff8a-e89d-46f3-a052-8eba2b9cd447",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CEEmvaKCJmNWdo4xp3P6qt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 924,
      "cache_read_input_tokens": 19078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 924,
        "ephemeral_1h_input_tokens": 0
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

_source line 40 · 2026-05-28T17:16:01.649Z_

<details><summary>↩ Tool result · `toolu_01Cm9Pyd4o2Qo3cajFvweffH`</summary>

```text
1	docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
2	docs/paper/related_work.tex:8:[Omitted long matching line]
3	docs/paper/related_work.tex:11:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
4	docs/paper/experiments.tex:7:We evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\times$ 50 episodes each).
5	docs/paper/experiments.tex:9:[Omitted long matching line]
6	docs/paper/results_v2.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
7	docs/paper/results_v2.tex:9:[Omitted long matching line]
8	docs/paper/results_v2.tex:11:[Omitted long matching line]
9	docs/paper/results_v2.tex:16:[Omitted long matching line]
10	docs/paper/results_v2.tex:22:$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
11	docs/paper/results_v2.tex:23:$\pi_0.5$~\cite{black2025pi05} & Linear proj ($\times\!\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\%, R$=$69.4\% ($\Delta{=}$+36pp) & Uniformly critical \\
12	docs/paper/results_v2.tex:24:X-VLA~\cite{zheng2025xvla} & Linear proj$^\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\pm}0.4$, $k{=}0.85$: $67.8$ & Threshold-graded \\
13	docs/paper/results_v2.tex:25:OpenVLA~\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\% SR ($-$49\%) & Smooth graded \\
14	docs/paper/results_v2.tex:26:OFT~\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \approx 0.215$; Ent.\ $0.667 \approx 0.661$$^\S$ & Smooth graded \\
15	docs/paper/results_v2.tex:27:CogACT~\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\% SR under 78\% prune$^\|$ & Smooth graded \\
16	docs/paper/results_v2.tex:28:SmolVLA~\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\% SR & Catastrophic cliff \\
17	docs/paper/results_v2.tex:45:OFT~\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, determines token importance structure. EfficientVLA~\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\cite{li2024cogact} (MLP projector) retains 74.2\% SR under 78\% pruning.
18	docs/paper/sections/analysis.tex:21:DynamicViT~\cite{rao2021dynamicvit} and ToMe~\cite{bolya2023tome} exploit this concentration: tokens that receive low attention contribute little to the classification decision and can be safely removed.
19	docs/paper/sections/analysis.tex:24:We extract attention weights from the LLM backbone (Qwen2-0.5B~\cite{yang2024qwen2}) over all vision tokens across three LIBERO tasks.
20	docs/paper/sections/analysis.tex:31:SigLIP~\cite{zhai2023siglip} encodes images using non-overlapping spatial patches without a \texttt{[CLS]} aggregation token.
21	docs/paper/sections/analysis.tex:123:In ViT classification, attention concentrates on a small subset of discriminative patches~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}.
22	docs/paper/sections/analysis.tex:129:SigLIP~\cite{zhai2023siglip} encodes each non-overlapping spatial patch as a separate token with no \texttt{[CLS]} aggregation, so the VLA's LLM backbone must attend to all patches to reconstruct spatial relationships between the robot end-effector, target objects, and obstacles.
23	docs/paper/sections/related_work_draft.tex:6:[Omitted long matching line]
24	docs/paper/sections/related_work_draft.tex:8:[Omitted long matching line]
25	docs/paper/sections/related_work_draft.tex:12:[Omitted long matching line]
26	docs/paper/sections/related_work_draft.tex:14:[Omitted long matching line]
27	docs/paper/sections/related_work_draft.tex:20:[Omitted long matching line]
28	docs/paper/sections/related_work_draft.tex:22:[Omitted long matching line]
29	docs/paper/sections/related_work_draft.tex:24:[Omitted long matching line]
30	docs/paper/sections/related_work_draft.tex:28:[Omitted long matching line]
31	docs/paper/sections/experiments.tex:17:DynamicViT~\cite{rao2021dynamicvit} removes 30\%--50\% of tokens with less than 0.5\% accuracy loss on ImageNet, and Token Merging (ToMe)~\cite{bolya2023tome} merges up to 40\% of tokens while retaining over 99\% of classification accuracy.
32	docs/paper/sections/experiments.tex:18:EViT~\cite{liang2022evit} similarly discards 50\% of inattentive tokens with negligible degradation.
33	docs/paper/sections/experiments.tex:19:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\cite{xu2025vlacache,cheng2026vlaiap}.
34	docs/paper/sections/experiments.tex:20:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\cite{liu2023libero}.
35	docs/paper/sections/experiments.tex:66:Token merging (following ToMe~\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.
36	docs/paper/sections/experiments.tex:73:\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\% accuracy on classification benchmarks even at aggressive retention ratios~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}
37	docs/paper/sections/results_draft.tex:4:We evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\% confidence intervals.
38	docs/paper/sections/results_draft.tex:9:[Omitted long matching line]
39	docs/paper/sections/results_draft.tex:12:[Omitted long matching line]
40	docs/paper/sections/results_draft.tex:59:OpenVLA~\cite{kim2024openvla} uses a two-layer MLP projector to map vision encoder outputs (from DINOv2 and SigLIP~\cite{zhai2023siglip}) into the Llama-2 language model's embedding space. Unlike pixel-shuffle, the MLP projector processes each patch token independently through a shared linear transformation. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence.
41	docs/paper/sections/background.tex:6:This section describes the two components of our experimental setup: the SmolVLA architecture~\cite{shukor2025smolvla}, in which we study vision token reduction, and the LIBERO benchmark~\cite{liu2023libero}, on which we evaluate closed-loop performance.
42	docs/paper/sections/background.tex:12:SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a modality connector, a language model backbone, and an action head.
43	docs/paper/sections/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
44	docs/paper/sections/background.tex:41:The Qwen2-0.5B language model~\cite{yang2024qwen2} serves as the central reasoning module.
45	docs/paper/sections/background.tex:47:SmolVLA generates actions through conditional flow matching~\cite{lipman2023flow} rather than autoregressive token prediction.
46	docs/paper/sections/background.tex:54:This architecture shares its high-level structure with larger VLA systems such as OpenVLA~\cite{kim2024openvla} and $\pi_0$~\cite{black2024pi0}, making SmolVLA a representative testbed for studying vision token efficiency in VLA policies.
47	docs/paper/sections/background.tex:59:We evaluate on the LIBERO benchmark~\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.
48	docs/paper/sections/experimental_setup.tex:33:  \item \textbf{Token merge}: following the bipartite matching strategy of ToMe~\cite{bolya2023tome}, each pruned token is merged with its nearest retained neighbor by averaging their embeddings. Sequence length and total information content are both preserved.
49	docs/paper/sections/introduction.tex:7:DynamicViT~\cite{rao2021dynamicvit} removes 66\% of patch tokens with less than 0.5\% accuracy loss on ImageNet classification.
50	docs/paper/sections/introduction.tex:8:Token Merging (ToMe)~\cite{bolya2023tome} merges 40\% of tokens while retaining over 99\% of classification accuracy.
51	docs/paper/sections/introduction.tex:9:EViT~\cite{liang2022evit} discards 50\% of inattentive tokens with negligible degradation.
52	docs/paper/sections/introduction.tex:12:Vision-Language-Action (VLA) models~\cite{brohan2023rt2,kim2024openvla,black2024pi0,shukor2025smolvla} use the same ViT encoders as their visual front-ends, producing hundreds of patch tokens that dominate the input sequence to the language model backbone.
53	docs/paper/sections/introduction.tex:17:Current VLA models such as RT-2~\cite{brohan2023rt2} and $\pi_0$~\cite{black2024pi0} use large vision encoders that produce 256 or more tokens per image.
54	docs/paper/sections/introduction.tex:20:SmolVLA~\cite{shukor2025smolvla}, a compact 451.5M-parameter VLA, produces 256 vision tokens from two cameras (128 per view), and these tokens constitute the majority of the LLM backbone's input sequence.
55	docs/paper/sections/introduction.tex:23:FastV~\cite{chen2024fastv} identifies and prunes inattentive visual tokens in VLM inference, achieving 2$\times$ speedup with minimal quality loss on VLM benchmarks.
56	docs/paper/sections/introduction.tex:24:VLA-Cache~\cite{xu2025vlacache} caches vision tokens across timesteps to reduce redundant computation in temporal sequences.
57	docs/paper/sections/introduction.tex:25:VLA-IAP~\cite{cheng2026vlaiap} proposes importance-aware pruning for VLA inference acceleration.
58	docs/paper/sections/introduction.tex:30:Existing evaluations of VLM token reduction rely on offline metrics such as action loss, perplexity, or next-token prediction accuracy~\cite{chen2024fastv,cheng2026vlaiap}.
59	docs/paper/sections/introduction.tex:38:Using SmolVLA on the LIBERO benchmark~\cite{liu2023libero}, we test six pruning configurations spanning three axes: scoring function (a trained Attention-Conditioned Importance Scorer versus random selection), retention ratio ($k \in \{0.5, 0.7, 0.9\}$), and mechanism (zero-masking, true removal, and token merging).
60	docs/paper/sections/introduction.tex:50:This uniformity arises because SigLIP~\cite{zhai2023siglip} encodes non-overlapping spatial patches without a \texttt{[CLS]} aggregation token; each token carries unique, irreplaceable spatial information about the scene.
61	docs/paper/sections/introduction.tex:59:We believe this negative result~\cite{karl2024negative,zeng2023transformers_tsf} carries important implications for the VLA efficiency community: future work on VLA compression should seek alternatives to naive token removal, such as training-time distillation into fewer tokens or architectural modifications that build in spatial redundancy.
62	docs/paper/method.tex:9:\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
63	docs/paper/method.tex:11:\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft} shares the same connector (512 tokens; CV$\,{=}\,$0.219).
64	docs/paper/method.tex:13:\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).
65	docs/paper/method.tex:15:We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
66	docs/paper/background.tex:6:This section describes the architectures and benchmark used in our study: SmolVLA~\cite{shukor2025smolvla} and OpenVLA~\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\cite{liu2023libero} on which we evaluate closed-loop performance.
67	docs/paper/background.tex:12:SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.
68	docs/paper/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
69	docs/paper/background.tex:36:The Qwen2-0.5B language model~\cite{yang2024qwen2} serves as the central reasoning module.
70	docs/paper/background.tex:41:SmolVLA generates actions through conditional flow matching~\cite{lipman2023flow} rather than autoregressive token prediction.
71	docs/paper/background.tex:49:OpenVLA~\cite{kim2024openvla} is a 7B-parameter VLA built on the Llama-2 backbone. Its vision pipeline differs from SmolVLA in two respects that are directly relevant to compressibility.
72	docs/paper/background.tex:52:OpenVLA uses a dual encoder combining DINOv2~\cite{oquab2023dinov2} and SigLIP~\cite{zhai2023siglip}. The two encoders produce complementary representations (self-supervised spatial features and language-aligned features) that are concatenated per patch position.
73	docs/paper/background.tex:63:We evaluate on the LIBERO benchmark~\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.
74	docs/paper/appendix.tex:90:[Omitted long matching line]
75	docs/paper/appendix.tex:93:[Omitted long matching line]
76	docs/paper/appendix.tex:137:[Omitted long matching line]
77	docs/paper/appendix.tex:747:X-VLA's 12-layer BART encoder~\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\,pp), confirming it as an architectural property.
78	docs/paper/appendix.tex:749:MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\% SR under 78\% pruning).
79	docs/paper/appendix.tex:867:Table~\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\_last), mean attention across all decoder layers (attn\_mean), and attention rollout~\cite{abnar2020quantifying}.
80	docs/paper/experimental_setup.tex:9:[Omitted long matching line]
81	docs/paper/experimental_setup.tex:11:We evaluate on LIBERO~\cite{liu2023libero} (Object: 10 tasks $\times$ 50 episodes = 500 total; Spatial and Goal for cross-suite validation). Closed-loop success rate (SR) with Wilson 95\% CIs is the primary metric; multi-seed results report mean $\pm$ std. Baselines: SmolVLA 44.8\%, OpenVLA 74.0\%, X-VLA 99.2\%, $\pi_0.5$ 98.2\%.
82	docs/paper/introduction.tex:14:[Omitted long matching line]
83	docs/paper/introduction.tex:16:Yet current VLAs employ fundamentally different vision connectors---linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure.
84	docs/paper/results.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
85	docs/paper/results.tex:9:[Omitted long matching line]
86	docs/paper/results.tex:11:[Omitted long matching line]
87	docs/paper/results.tex:16:[Omitted long matching line]
88	docs/paper/results.tex:22:$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
89	docs/paper/results.tex:23:$\pi_0.5$~\cite{black2025pi05} & Linear proj ($\times\!\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\%, R$=$69.4\% ($\Delta{=}$+36pp) & Uniformly critical \\
90	docs/paper/results.tex:24:X-VLA~\cite{zheng2025xvla} & Linear + BART (12L)$^\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\pm}0.4$, $k{=}0.85$: $67.9{\pm}0.3$ & Threshold-graded \\
91	docs/paper/results.tex:25:OpenVLA~\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\% SR ($-$49\%) & Smooth graded \\
92	docs/paper/results.tex:26:OFT~\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \approx 0.215$; Ent.\ $0.667 \approx 0.661$$^\S$ & Smooth graded \\
93	docs/paper/results.tex:27:CogACT~\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\% SR under 78\% prune$^\|$ & Smooth graded \\
94	docs/paper/results.tex:28:SmolVLA~\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\% SR & Catastrophic cliff \\
95	docs/paper/results.tex:45:OFT~\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\cite{li2024cogact} (MLP projector) retains 74.2\% SR under 78\% pruning.
96	docs/paper/experiments_deprecated.tex:6:DynamicViT~\cite{rao2021dynamicvit} removes 30\%--50\% of tokens with less than 0.5\% accuracy loss on ImageNet, and Token Merging (ToMe)~\cite{bolya2023tome} merges up to 40\% of tokens while retaining over 99\% of classification accuracy.
97	docs/paper/experiments_deprecated.tex:7:EViT~\cite{liang2022evit} similarly discards 50\% of inattentive tokens with negligible degradation.
98	docs/paper/experiments_deprecated.tex:8:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\cite{xu2025vlacache,cheng2026vlaiap}.
99	docs/paper/experiments_deprecated.tex:9:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\cite{liu2023libero}.
100	docs/paper/experiments_deprecated.tex:55:Token merging (following ToMe~\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.
101	docs/paper/experiments_deprecated.tex:62:\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\% accuracy on classification benchmarks even at aggressive retention ratios~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "8e569033-9e98-4c25-b9f9-1d8b93e48e65"
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
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Running find /home/ubuntu/.agent-ml-research-be-idea-gen-…",
  "usage": {
    "total_tokens": 27166,
    "tool_uses": 4,
    "duration_ms": 14280
  },
  "last_tool_name": "Bash",
  "uuid": "23d187e5-e804-4cbc-81a2-7284143a4006",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01CJd3S8ZfsnwKEhPihAu6tp`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper -name \"*.tex\" -type f | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "084cc339-8528-4fc0-a8fa-bc6033fac2f1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017EE1eGaNLGozRAmeKgjcAh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7135,
      "cache_read_input_tokens": 20002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7135,
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

_source line 43 · 2026-05-28T17:16:05.236Z_

<details><summary>↩ Tool result · `toolu_01CJd3S8ZfsnwKEhPihAu6tp`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments_deprecated.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis_draft.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experimental_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/related_work_draft.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/results_draft.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "8240c874-3860-4e82-93a2-f943e9e31c13"
}
```

</details>

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 28322,
    "tool_uses": 5,
    "duration_ms": 16582
  },
  "last_tool_name": "Read",
  "uuid": "9dfd504e-b3e2-4db7-992f-17c77e4dd0f9",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01865Het634KEynNxizXZ6aT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "7c861575-f7af-4fe4-83d7-6ed64aeed984",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MKVGtU9Bs62KqQvTEsaYS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 27137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1154,
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

_source line 46 · 2026-05-28T17:16:07.371Z_

<details><summary>↩ Tool result · `toolu_01865Het634KEynNxizXZ6aT`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	\usepackage{wrapfig}
13	
14	% Tighten float spacing for page limit
15	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
16	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{8pt plus 2pt minus 4pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{0pt}
20	
21	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{abstract}
27	
28	\keywords{vision-language-action models, token pruning, robot learning}
29	
30	\input{introduction}
31	
32	\input{related_work}
33	
34	\input{method}
35	
36	\input{experiments}
37	
38	\input{conclusion}
39	
40	\input{limitations}
41	
42	\bibliography{references}
43	
44	\input{appendix}
45	
46	\end{document}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "f3d6d612-5e1f-4c4b-b236-bd5182ff95a0"
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
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/related_work.tex",
  "usage": {
    "total_tokens": 28323,
    "tool_uses": 6,
    "duration_ms": 16694
  },
  "last_tool_name": "Read",
  "uuid": "06827c23-0336-41c6-b8b6-ae675a1619ac",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01PzNWfg4Wyf2ff5QRjQmaZ8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "6d260f7c-d30c-470e-b6f7-8449d835cd3d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MKVGtU9Bs62KqQvTEsaYS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 27137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1154,
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

_source line 49 · 2026-05-28T17:16:07.484Z_

<details><summary>↩ Tool result · `toolu_01PzNWfg4Wyf2ff5QRjQmaZ8`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using attention signals. VLA-specific methods have emerged: VLA-IAP~\cite{cheng2026vlaiap}, VLA-Cache~\cite{xu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, VLA-Pruner~\cite{liu2025vlapruner}, LightVLA~\cite{jiang2026lightvla}, and Compressor-VLA~\cite{gao2025compressorvla}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.
9	
10	\paragraph{Vision connectors.}
11	LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "63243344-0749-4d15-9ccc-a1a23da48878"
}
```

</details>

---

### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 28324,
    "tool_uses": 7,
    "duration_ms": 16976
  },
  "last_tool_name": "Read",
  "uuid": "1c682112-f54c-4d83-bb4c-42296a9b1438",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01LHt2JGikHEqnHpb1aL88ig`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "4a0db49a-d67c-4040-ad84-87014d683ff2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MKVGtU9Bs62KqQvTEsaYS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 27137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1154,
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

_source line 52 · 2026-05-28T17:16:07.769Z_

<details><summary>↩ Tool result · `toolu_01LHt2JGikHEqnHpb1aL88ig`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_hero_overview.pdf}
7	\caption{Overview of VLA token compressibility.
8	\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.
9	\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.
10	\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy.}
11	\label{fig:teaser}
12	\end{figure*}
13	
14	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to near-zero (${\leq}$6.6\%). Apply the same reduction to $\pi_{0.5}$ and it retains 98.2\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a ViT encoder feeding tokens through a connector into a language model backbone; the critical difference is the connector architecture. Token pruning is well-established for ViTs~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and extends to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture, implicitly assuming pruning transfers across designs.
15	
16	Yet current VLAs employ fundamentally different vision connectors---linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure.
17	
18	We present an empirical study of VLA token compressibility, identifying the vision-language connector as the primary determinant of pruning robustness (Figure~\ref{fig:teaser}). Token-independent connectors degrade gracefully; entangling connectors produce catastrophic failures amplified by task complexity ($20{\times}$ from Object to Goal). The coefficient of variation (CV) of post-connector token L2 norms captures this on a continuous spectrum (0.038 to 0.314). Under sufficient compression, scoring effectiveness becomes connector-dependent: L2 norm aids $\pi_{0.5}$ (up to $+$46.9\,pp on Long at $k{=}0.9$; $+$35.2\,pp on Goal at $k{=}0.85$) but reverses at aggressive ratios ($-$36\,pp at $k{=}0.5$); on X-VLA it is anti-informative ($-$8 to $-$27\,pp), while attention recovers near-baseline performance. For pixel-shuffle connectors where all pruning fails, Vision Token Re-encoder (VTR, ${\sim}$5\% extra parameters) recovers over 60\% SR at 75\% compression.
19	
20	Our contributions are:
21	\begin{itemize}[nosep]
22	    \item A compressibility analysis across five VLA architectures (450M--7B) on four LIBERO suites, identifying connector architecture as the primary determinant of pruning robustness.
23	    \item CV of token L2 norms as a single-pass diagnostic for connector compressibility type (uniform, graded, catastrophic), validated on four closed-loop architectures.
24	    \item A zero-mask ablation proving position disruption---not information loss---drives $\pi_{0.5}$'s 89\,pp failure gap. VTR recovers a pixel-shuffle VLA from 0\% to over 60\% at 75\% compression.
25	\end{itemize}
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "74b6536c-ac82-4f9a-b0b2-69e6235b1447"
}
```

</details>

---

### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 30783,
    "tool_uses": 8,
    "duration_ms": 19961
  },
  "last_tool_name": "Read",
  "uuid": "1702ca20-bf7d-44f1-b386-45d86476de07",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01JYKYdMEr64H2CVgzThg33b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "7339119b-20ab-46f1-9f2b-34760d578739",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019hnKabXoxGddZwUmKof18P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 28291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2454,
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

_source line 55 · 2026-05-28T17:16:10.751Z_

<details><summary>↩ Tool result · `toolu_01JYKYdMEr64H2CVgzThg33b`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft} shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
20	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}
21	\label{fig:architecture}
22	\end{figure*}
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\caption{VLA models evaluated. Coupling indicates independent vs.\ cross-token processing. $N$ = vision tokens input to the LLM. $^\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}
28	\label{tab:model_properties}
29	\begin{tabular}{lrlcrll}
30	\toprule
31	Model & Params & Connector & $N$ & CV & Coupling & Eval \\
32	\midrule
33	$\pi_{0.5}$ & 4B & Linear ($\times\!\sqrt{d}$) & 768 & 0.055 & Indep.\ & Closed-loop \\
34	X-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\
35	OpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\ & Closed-loop \\
36	SmolVLA & 450M & Pixel-shuffle $4{\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\
37	\midrule
38	$\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\ & Offline \\
39	OFT$^\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\ & Offline \\
40	\bottomrule
41	\end{tabular}
42	\end{table}
43	
44	\subsection{Pruning Protocol}
45	\label{sec:pruning_protocol}
46	
47	We apply post-connector token pruning at retention ratio $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$, retaining $\lfloor k \cdot N \rfloor$ tokens. Two strategies bracket expected performance: \textbf{L2 norm selection} retains the top-$k$ fraction by L2 norm, and \textbf{random subsampling} selects $\lfloor k \cdot N \rfloor$ tokens uniformly at random. The \emph{importance margin} at ratio $k$ is $\text{SR}_{\text{L2}}(k) - \text{SR}_{\text{Random}}(k)$; a positive margin indicates token importance structure is informative. Both strategies physically remove unselected tokens and re-index position IDs. We prune post-connector to isolate the connector's effect on token information structure.
48	
49	\subsection{Compressibility Diagnostic: Importance CV}
50	\label{sec:cv_diagnostic}
51	
52	We quantify post-connector token heterogeneity via the coefficient of variation (CV) of L2 norms:
53	\begin{equation}
54	\text{CV} = \frac{\sigma\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}{\mu\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}
55	\label{eq:cv}
56	\end{equation}
57	CV is a single-pass diagnostic requiring one forward pass with no downstream evaluation. It captures a continuous spectrum from $\pi_{0}$ (CV$\,{=}\,$0.038, near-uniform norms) to SmolVLA (CV$\,{=}\,$0.314, high heterogeneity). Low-CV models have near-uniform tokens where \emph{which} tokens are removed matters more than \emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy.
58	
59	\subsection{Vision Token Re-encoder (VTR)}
60	\label{sec:vtr}
61	
62	Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding: a cross-attention module (${\sim}$22M parameters, ${\sim}$5\% of SmolVLA) uses $M$ learned queries to attend over all $N$ source tokens. The compression ratio is controlled by $M \in \{16, 32, 64, 96, 128\}$; $M{=}N$ serves as a passthrough control.
63	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "46840858-bad7-422f-8e88-0cac7d79cf44"
}
```

</details>

---

### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/background.tex",
  "usage": {
    "total_tokens": 30785,
    "tool_uses": 9,
    "duration_ms": 20077
  },
  "last_tool_name": "Read",
  "uuid": "4269e902-9d5f-47fc-9fce-20c844a0a6fa",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01UW1EdKU5Y1xLAjwiNnhn3o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "cdf2612a-7ab9-41d5-aa45-d14ed2d708b1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019hnKabXoxGddZwUmKof18P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 28291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2454,
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

_source line 58 · 2026-05-28T17:16:10.866Z_

<details><summary>↩ Tool result · `toolu_01UW1EdKU5Y1xLAjwiNnhn3o`</summary>

```text
1	% background.tex -- Section 2: Background
2	
3	\section{Background}
4	\label{sec:background}
5	
6	This section describes the architectures and benchmark used in our study: SmolVLA~\cite{shukor2025smolvla} and OpenVLA~\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\cite{liu2023libero} on which we evaluate closed-loop performance.
7	
8	\subsection{SmolVLA Architecture}
9	\label{sec:smolvla_arch}
10	
11	Vision-Language-Action (VLA) models cast robotic control as conditional generation: given a camera observation and a language instruction, the model predicts a continuous action.
12	SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.
13	Figure~\ref{fig:architecture} contrasts the vision pipelines of SmolVLA and OpenVLA, highlighting the connector designs that determine compressibility.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
18	\caption{Vision connector comparison. \textbf{Left}: SmolVLA applies $4{\times}4$ pixel-shuffle to fold 1024 SigLIP patches into 64 tokens per camera (128 total), creating dense, spatially entangled representations. \textbf{Right}: OpenVLA uses an MLP projector that maps each patch independently, producing 256 tokens with per-token independence. We hypothesize that this architectural difference is the primary factor governing token compressibility: pixel-shuffle tokens resist any form of deletion, while independently projected tokens allow graded pruning.}
19	\label{fig:architecture}
20	\end{figure}
21	
22	\paragraph{Vision encoder.}
23	SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
24	SigLIP divides each camera image into non-overlapping spatial patches on a $32 \times 32$ grid, producing 1024 patch tokens per image.
25	SigLIP does not include a \texttt{[CLS]} aggregation token; there is no single summary representation that pools information across patches.
26	
27	\paragraph{Pixel-shuffle vision connector.}
28	Before reaching the language model, the 1024 SigLIP patches pass through a pixel-shuffle connector that applies $4 \times 4$ spatial folding. Each $4 \times 4$ block of spatially adjacent patches is collapsed into a single token by channel concatenation, compressing 1024 patches into 64 tokens per camera image ($16\times$ reduction). An MLP then projects these 64 tokens into the Qwen2-0.5B embedding space. The pixel-shuffle operation is fixed and non-learned; it creates dense tokens where each encodes the full semantic content of 16 contiguous patches. This design choice is central to the cliff-edge phenomenon we report: the spatial folding creates inter-token dependencies that make every token indispensable.
29	
30	\paragraph{Dual-camera input.}
31	SmolVLA receives images from two cameras: a wrist-mounted camera and an overhead camera.
32	Each camera image produces 64 vision tokens after pixel-shuffle, yielding 128 vision tokens total that enter the language model.
33	The two viewpoints are complementary: the wrist camera captures fine-grained end-effector interactions, while the overhead camera provides a global spatial layout of objects on the workspace.
34	
35	\paragraph{LLM backbone.}
36	The Qwen2-0.5B language model~\cite{yang2024qwen2} serves as the central reasoning module.
37	It receives a concatenated input sequence of 128 projected vision tokens and the tokenized language instruction.
38	Self-attention across this full sequence allows the model to ground language in visual context and to integrate information across both camera views.
39	
40	\paragraph{Flow matching action head.}
41	SmolVLA generates actions through conditional flow matching~\cite{lipman2023flow} rather than autoregressive token prediction.
42	The action head maps the LLM's output representation to a continuous 7-DoF action vector: three position coordinates, three rotation angles, and one gripper open/close value.
43	Flow matching learns a vector field that transports a noise distribution to the target action distribution, conditioned on the LLM output.
44	Any corruption of the vision token input propagates through the full LLM computation into the predicted action.
45	
46	\subsection{OpenVLA Architecture}
47	\label{sec:openvla_arch}
48	
49	OpenVLA~\cite{kim2024openvla} is a 7B-parameter VLA built on the Llama-2 backbone. Its vision pipeline differs from SmolVLA in two respects that are directly relevant to compressibility.
50	
51	\paragraph{Vision encoder.}
52	OpenVLA uses a dual encoder combining DINOv2~\cite{oquab2023dinov2} and SigLIP~\cite{zhai2023siglip}. The two encoders produce complementary representations (self-supervised spatial features and language-aligned features) that are concatenated per patch position.
53	
54	\paragraph{MLP projector.}
55	Unlike SmolVLA's pixel-shuffle connector, OpenVLA maps vision encoder outputs to the language model through a three-layer MLP projector (GELU activations) that processes each patch token independently. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence. The projector produces 256 vision tokens that maintain a one-to-one correspondence with spatial patch locations.
56	
57	\paragraph{Architectural contrast.}
58	The key difference for compressibility is the connector design. SmolVLA's pixel-shuffle folds 16 patches into each token, creating dense, entangled representations where removing one token eliminates a $4 \times 4$ spatial region. OpenVLA's MLP projector preserves patch-level granularity, so removing one token discards approximately $1/256$ of the visual field. Model scale (0.5B vs.\ 7B) is a confound that we discuss in Section~\ref{sec:discussion}.
59	
60	\subsection{LIBERO Benchmark}
61	\label{sec:libero_bench}
62	
63	We evaluate on the LIBERO benchmark~\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.
64	LIBERO provides standardized task definitions, initial state distributions, and evaluation protocols for reproducible comparison of manipulation policies.
65	We use three of its four suites, each testing a distinct aspect of policy competence.
66	LIBERO-Object presents ten tasks focused on object manipulation; the policy must identify and interact with specific objects from visually similar alternatives.
67	LIBERO-Spatial presents ten tasks focused on spatial reasoning, where the policy must place objects correctly or navigate relative to reference locations.
68	LIBERO-Goal presents ten tasks with varied goal conditions applied to a shared environment layout; these tasks test whether the policy can condition its behavior on the language instruction.
69	
70	Each suite contains 10 tasks, and we run 50 evaluation episodes per task, yielding 500 episodes per suite per experimental condition.
71	The evaluation metric is closed-loop Success Rate (SR): a binary indicator per episode that equals 1 only if the robot completes the full task within the time limit.
72	SR is measured through closed-loop execution, where the policy observes the current state, predicts an action, the simulator advances, and the policy re-observes the updated state at every timestep.
73	This closed-loop evaluation is critical because errors at any single step can cascade through subsequent observations and actions.
74	A policy that produces even one qualitatively wrong action (for example, opening the gripper when it should close) will likely fail the entire episode.
75	
76	The three LIBERO suites span a range of baseline difficulty levels: SmolVLA achieves 44.8\% SR on Object, 51.8\% on Spatial, and 63.0\% on Goal in bypass mode (full vision tokens, no pruning).
77	These baseline numbers are not state-of-the-art; SmolVLA is a compact model designed for efficiency research.
78	The relevant comparison is not the absolute success rate but the change under token reduction: any viable pruning strategy must approximately preserve these baselines rather than collapse to 0\%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "3ee0987e-a4a7-4b97-be8e-7fc8c20674b7"
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
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/results.tex",
  "usage": {
    "total_tokens": 30787,
    "tool_uses": 10,
    "duration_ms": 20251
  },
  "last_tool_name": "Read",
  "uuid": "2733600d-3833-41b3-b9f9-4a98cdba39c4",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01DPFjTNTE3bbZHsXFQ4uZTx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "7681e3da-b60e-4e1f-9ea0-e90f7d3530fb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019hnKabXoxGddZwUmKof18P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2454,
      "cache_read_input_tokens": 28291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2454,
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

_source line 61 · 2026-05-28T17:16:11.040Z_

<details><summary>↩ Tool result · `toolu_01DPFjTNTE3bbZHsXFQ4uZTx`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, is strongly associated with pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A pairwise comparison between $\pi_0$ and OpenVLA (both consuming 256 SigLIP-based~\cite{zhai2023siglip} tokens but differing in connector, backbone, and encoder fusion) yields a 63\,pp gap at $k{=}0.1$; this gap is consistent with the monotonic CV-degradation pattern across all seven models (Section~\ref{sec:linear_results}).
10	
11	The four classes differ qualitatively in their failure mode. Uniformly critical models ($\pi_0$, $\pi_0.5$~\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.
12	
13	\begin{table*}[t]
14	\centering
15	\small
16	\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\dagger\pi_0$: offline metrics only, no closed-loop evaluation; the 63\,pp gap vs.\ OpenVLA at $k{=}0.1$ mixes offline loss with closed-loop SR. $^\ddagger$X-VLA uses a linear projection followed by a 12-layer BART encoder; the effective pipeline is not purely linear. $^\S$OFT reports attention entropy and CV only (no pruning evaluation); both metrics match OpenVLA, consistent with the connector being associated with token importance structure. $^\|$CogACT: literature result from EfficientVLA~\cite{yang2025efficientvla}, not our evaluation.}
17	\label{tab:taxonomy}
18	\begin{tabular}{llcrcll}
19	\toprule
20	Model & Connector & Params & Tokens & CV & Representative Result & Class \\
21	\midrule
22	$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
23	$\pi_0.5$~\cite{black2025pi05} & Linear proj ($\times\!\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\%, R$=$69.4\% ($\Delta{=}$+36pp) & Uniformly critical \\
24	X-VLA~\cite{zheng2025xvla} & Linear + BART (12L)$^\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\pm}0.4$, $k{=}0.85$: $67.9{\pm}0.3$ & Threshold-graded \\
25	OpenVLA~\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\% SR ($-$49\%) & Smooth graded \\
26	OFT~\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \approx 0.215$; Ent.\ $0.667 \approx 0.661$$^\S$ & Smooth graded \\
27	CogACT~\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\% SR under 78\% prune$^\|$ & Smooth graded \\
28	SmolVLA~\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\% SR & Catastrophic cliff \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	
33	\subsection{Pixel-Shuffle: Catastrophic Cliff-Edge}
34	\label{sec:smolvla_results}
35	
36	The SmolVLA baseline (bypass mode, all 128 vision tokens) achieves 44.8\% SR (224/500, CI [40.5\%, 49.2\%]).\footnote{The official SmolVLA result is 87.3\% SR with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch due to compute constraints.} Every pruning configuration produces 0\% SR across seven configurations varying scoring (learned ACIS vs.\ random), retention ratio ($k \in \{0.50, 0.70, 0.90, 0.95\}$), and mechanism (zero-masking, true removal, token merging). The cliff persists regardless of checkpoint quality: the official SmolVLA HF checkpoint (57.2\%--59.2\% SR across two evaluation protocols; Appendix~\ref{app:smolvla_ablation}) also collapses to 0\% under random $k{=}0.95$ (5\% removal), L2 norm $k{=}0.9$ (10\% removal), and L2 norm $k{=}0.5$ (Table~\ref{tab:smolvla_ablation}). The failure is architectural, not a training artifact.
37	
38	The pattern generalizes across LIBERO suites: Spatial 0.6\%, Goal 0\%. Pixel-shuffle folds each $4{\times}4$ patch block into a single token by channel concatenation; removing one token eliminates an entire $4{\times}4$ receptive field. The resulting spatial entanglement means even 5\% removal ($k{=}0.95$, losing 6 of 128 tokens) destroys task-critical visual information. Full ablation results appear in Table~\ref{tab:smolvla_ablation}, Appendix~\ref{app:smolvla_ablation}.
39	
40	\subsection{MLP Projector: Smooth Graded Degradation}
41	\label{sec:openvla_results}
42	
43	Under random token removal, OpenVLA degrades gracefully across all retention ratios: 74.0\% (baseline) $\rightarrow$ 69.4\% at $k{=}0.95$ ($-4.6$\,pp) $\rightarrow$ 62.0\% at $k{=}0.90$ $\rightarrow$ 49.0\% at $k{=}0.70$ $\rightarrow$ 37.4\% at $k{=}0.50$ $\rightarrow$ 20.6\% at $k{=}0.30$ (Figure~\ref{fig:degradation_curve}; full results with CIs in Table~\ref{tab:openvla_full}, Appendix).\footnote{A second random seed confirms the graded pattern: 62.2\% at $k{=}0.9$ ($+$0.2\,pp), 44.4\% at $k{=}0.7$ ($-$4.6\,pp), 35.6\% at $k{=}0.5$ ($-$1.8\,pp). All within 5\,pp of the primary seed. Per-seed details in Table~\ref{tab:openvla_multiseed}, Appendix~\ref{app:openvla_multiseed}.} At $k{=}0.30$, two tasks reach 0\% SR, but eight retain non-zero performance: degradation is graded, not cliff-edge. Random token removal provides a conservative lower bound on architectural resilience; learned scoring methods would likely yield better retention.
44	
45	OFT~\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\cite{li2024cogact} (MLP projector) retains 74.2\% SR under 78\% pruning.
46	
47	To control for scoring method in cross-architecture comparisons, we evaluate L2 norm-based selection on OpenVLA. At moderate-to-aggressive retention ($k \leq 0.7$), L2 performs within 2--6\,pp of random removal\footnote{OpenVLA random results use seed$\,{=}\,$7; L2 norm results use seed$\,{=}\,$42. Same-seed (seed42) gaps: 5.4\,pp at $k{=}0.7$, 3.6\,pp at $k{=}0.3$ (21.4\% random vs.\ 25.0\% L2); same-seed at $k{=}0.5$: 35.8\% random vs.\ 39.2\% L2 (gap 3.4\,pp).} (Table~\ref{tab:openvla_l2_vs_random}, Appendix~\ref{app:l2_vs_random}). At $k{=}0.9$, L2 outperforms random by 8.6\,pp (70.6\% vs.\ 62.0\%, reproducible across two random seeds), consistent with the weak but non-zero importance gradient predicted by CV$\,{=}\,$0.215: the signal is exploitable only when few tokens are removed.
48	
49	\subsection{Linear Projection: From Uniformly Critical to Threshold-Graded}
50	\label{sec:linear_results}
51	
52	Three models share a linear projection connector yet exhibit qualitatively different pruning responses. The divergence traces to what happens \emph{after} the projection: nothing ($\pi_0$), a learned scaling ($\pi_0.5$), or a full 12-layer encoder (X-VLA).
53	
54	\paragraph{$\pi_0$ (3.3B, 256 tokens, pure linear).} Offline normalized L1 action loss at $k{=}0.1$ is 0.976, a 2.4\% \emph{improvement} over the unpruned baseline.\footnote{Offline action loss measures single-step prediction quality; closed-loop evaluation may reveal additional degradation.} CV$\,{=}\,$0.038 indicates near-uniform token norms. Near-uniform L2 norms (CV$\,{=}\,$0.038) suggest that no token subset carries disproportionate information, so random removal approximates uniform spatial downsampling and the model compensates.
55	
56	\paragraph{$\pi_0.5$ (4B, 768 tokens, linear $\times\!\sqrt{d}$).} The baseline achieves 98.2\% SR. This model reveals that low CV does not imply tokens are dispensable; it implies uniform criticality. The response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\% SR ($-$28.8\,pp), while L2 norm-based removal at the same ratio collapses to 33.4\% ($-$64.8\,pp). The gap of 36\,pp is the largest method-dependent effect at $k{=}0.5$ in our study.
57	
58	At $k \leq 0.7$, random removal degrades monotonically (77.2\%, 69.4\%, 36.4\% at $k{=}0.7, 0.5, 0.3$; seed43 within 1\,pp). At higher retention, a task-specific random cliff emerges on LIBERO-Object: SR drops from 69.4\% ($k{=}0.95$) to 5.0\% ($k{=}0.85$) before recovering to 77.2\% ($k{=}0.7$), a 72\,pp swing; the same $k{=}0.85$ on LIBERO-Spatial retains 58.4\% (Appendix~\ref{app:pi05_crosssuite}). L2 norm selection produces a V-shaped curve: 55.0\% at $k{=}0.7$, 33.4\% at $k{=}0.5$ (the valley), 51.0\% at $k{=}0.3$, confirmed across two seeds ($\sigma = 0.1$\,pp at the valley).\footnote{V-shape valley at $k{=}0.5$: 33.4\% (seed42) vs.\ 33.6\% (seed43), $\sigma{=}0.1$\,pp. V-depth: 17.6\,pp (seed42), 21.8\,pp (seed43). Full multi-seed table in Appendix~\ref{app:pi05_multiseed}.} The non-monotonic L2 pattern arises because norm ranking in a low-CV distribution selects spatially clustered tokens (slight norm variations correlate with image regions), and the resulting loss of spatial coverage peaks at intermediate budgets.
59	
60	This result demonstrates that models showing offline pruning tolerance can exhibit severe closed-loop degradation. Low-CV tokens are uniformly critical, not uniformly dispensable. L2 norm-based selection systematically concentrates on spatially correlated tokens and loses coverage; random selection preserves the uniform spatial distribution that these architectures require.
61	
62	\paragraph{X-VLA (880M, 50 tokens, linear + 12-layer BART).} The 99.2\% baseline is maintained at $k{=}0.95$ ($99.1 \pm 0.2$\%, 3 seeds) and $k{=}0.9$ ($97.8 \pm 0.4$\%) under L2 norm-based removal. A sharp cliff appears at $k{=}0.85$ ($67.9 \pm 0.3$\%, $-$31\,pp, 3 seeds), with non-monotonic recovery at $k{=}0.80$ ($89.0 \pm 0.7$\%, 3 seeds) before degradation resumes: $58.6 \pm 0.4$\% at $k{=}0.7$, $43.4 \pm 0.8$\% at $k{=}0.5$, $22.0 \pm 0.9$\% at $k{=}0.3$, $4.7 \pm 0.6$\% at $k{=}0.2$, and near-zero at $k{=}0.1$. The cliff at $k{=}0.85$ (retaining 42 of 50 BART-encoded tokens) is reproducible across seeds (std $\leq$ 1.6\,pp). The non-monotonic dip is task-specific: four tasks lose $\sim$50\,pp each while six remain unaffected (Table~\ref{tab:xvla_cliff_pertask}, Appendix~\ref{app:xvla_cliff}). Under random removal, X-VLA exhibits a plateau: $65.1 \pm 0.1$\% at $k{=}0.7$ and $64.0 \pm 1.6$\% at $k{=}0.3$ (3 seeds each), confirming that L2 norm-based selection ($22.0 \pm 0.9$\% at $k{=}0.3$) is far more destructive than random for this intermediate-CV architecture.
63	
64	That this threshold appears under importance-based removal (the more favorable test) while OpenVLA degrades smoothly under random removal (the harder test) strengthens the architecture-dependent conclusion. The $\pi_0$--OpenVLA comparison (both consuming 256 SigLIP-based tokens, differing in connector, backbone, and encoder fusion) produces a 63\,pp gap at $k{=}0.1$, consistent with the connector-associated pattern observed across all seven models. This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation.
65	
66	\subsection{VTR: Re-Encoding Overcomes Cliff-Edge}
67	\label{sec:smart_compress_results}
68	
69	To test whether learned re-encoding can overcome the pixel-shuffle cliff-edge, we insert a 22.2M-parameter cross-attention module (Vision Token Re-encoder, VTR) between the vision connector and the LLM backbone (details in Appendix~\ref{app:smart_compress_details}). VTR compresses 128 input tokens to $M$ output tokens. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\% SR ($p > 0.9$ vs.\ the 44.8\% baseline); the gain is architectural, not from additional optimization steps.\footnote{The extended baseline also collapses to 0\% SR under pruning ($k{=}0.50$, random, true removal). Additional training does not mitigate the pixel-shuffle vulnerability.}
70	
71	\begin{table}[t]
72	\centering
73	\small
74	\caption{VTR re-encoding vs.\ deletion on SmolVLA (LIBERO-Object). The M-curve is relatively stable: $M{=}16$ (87.5\% compression) matches $M{=}128$ (no compression) within 1.1\,pp. A parameter-matched MLP adapter achieves comparable SR ($p = 0.15$ vs.\ cross-attention). $^\ddagger$Mean $\pm$ std over 3 seeds (500 episodes each). Other rows: single seed with Wilson 95\% CI.}
75	\label{tab:smart_compress}
76	\begin{tabular}{lccrr}
77	\toprule
78	Method & $M$ & Red. & SR (\%) & Seeds \\
79	\midrule
80	\textit{Baseline} & 128 & 0\% & 44.8 & 1 \\
81	\textit{Ext.\ training} & -- & -- & 45.0 & 1 \\
82	\textit{Hard pruning} & -- & 50--90\% & 0.0 & mult. \\
83	\midrule
84	Cross-attn$^\ddagger$ & 16 & 87.5\% & 56.9$\pm$1.3 & 55.8/58.4/56.5 \\
85	Cross-attn$^\ddagger$ & 32 & 75\% & 60.1$\pm$1.3 & 61.6/59.2/59.6 \\
86	Cross-attn$^\ddagger$ & 64 & 50\% & \textbf{62.0}$\pm$2.3 & 61.6/60.0/64.4 \\
87	Cross-attn$^\ddagger$ & 96 & 25\% & 54.5$\pm$3.2 & 52.6/58.2/52.8 \\
88	Cross-attn$^\ddagger$ & 128 & 0\% & 58.0$\pm$3.5 & 59.8/54.0/60.2 \\
89	MLP adapter$^\ddagger$ & 32 & 75\% & 63.4$\pm$2.6 & 65.2/64.6/60.4 \\
90	\midrule
91	\multicolumn{5}{l}{\textit{Official checkpoint (59.2\% baseline)}} \\
92	Cross-attn & 32 & 75\% & 53.4 & 1 \\
93	\bottomrule
94	\end{tabular}
95	\end{table}
96	
97	The M-curve is relatively stable (Table~\ref{tab:smart_compress}): $M{=}16$ (56.9\%, 87.5\% compression) performs within 1.1\,pp of $M{=}128$ (58.0\%, no compression). A parameter-matched MLP adapter achieves 63.4\% $\pm$ 2.6 at $M{=}32$ ($p = 0.15$ vs.\ cross-attention; Figure~\ref{fig:compression_curve}). Cross-suite evaluation confirms generalization: 53.2\% on LIBERO-Spatial and 56.4\% on LIBERO-Goal where hard pruning yields 0\% (Appendix~\ref{app:smart_compress_full}). VTR applied to OpenVLA yields 0\% SR even in passthrough mode: it is a targeted remedy for pixel-shuffle entanglement.
98	
99	\subsection{CV Correlates with Optimal Pruning Strategy}
100	\label{sec:scaling_law}
101	
102	Token importance CV correlates with both pruning tolerance and optimal strategy. Comparing L2 norm-based and random removal across three models, the gap $\Delta$(R$-$L2) decreases monotonically with CV at both $k{=}0.5$ and $k{=}0.7$ (full data in Table~\ref{tab:scaling_law}, Appendix~\ref{app:cv_scaling_table}). At $k{=}0.5$: $+$36.0\,pp ($\pi_0.5$, CV$\,{=}\,$0.055) $\rightarrow$ $+$26.9\,pp (X-VLA, CV$\,{=}\,$0.151) $\rightarrow$ $-$1.8\,pp (OpenVLA, CV$\,{=}\,$0.215). At $k{=}0.7$: $+$22.2\,pp $\rightarrow$ $+$6.5\,pp $\rightarrow$ $-$5.4\,pp. The monotonic ordering holds across a 2$\times$ change in token budget, indicating CV captures a structural property of the connector. Below CV $\approx 0.15$, L2 ranking captures spatial artifacts rather than importance; above it, importance-based scoring becomes beneficial (reversal at $k{=}0.3$; Appendix~\ref{app:cv_strategy_interaction}).
103	
104	\begin{figure}[t]
105	\centering
106	\begin{subfigure}[b]{0.48\linewidth}
107	\includegraphics[width=\linewidth]{figures/paper/fig_degradation_curve.pdf}
108	\caption{Token pruning across connector classes.}
109	\label{fig:degradation_curve}
110	\end{subfigure}
111	\hfill
112	\begin{subfigure}[b]{0.48\linewidth}
113	\includegraphics[width=\linewidth]{figures/paper/fig_compression_curve.pdf}
114	\caption{VTR M-curve and CV-strategy interaction.}
115	\label{fig:compression_curve}
116	\end{subfigure}
117	\caption{Token reduction on LIBERO-Object. (a)~Pruning: linear ($\pi_0$) uniformly critical, linear+encoder (X-VLA) threshold-graded, MLP (OpenVLA) smooth, pixel-shuffle (SmolVLA) collapses. (b)~VTR: $M{=}16 \approx M{=}128$ where deletion yields 0\%; CV-gap monotonic.}
118	\label{fig:results_combined}
119	\end{figure}
120	
121	\enlargethispage{2\baselineskip}
122	\subsection{Cross-Suite Generalization}
123	\label{sec:cross_suite}
124	
125	The cliff zone exhibits a suite $\times$ method interaction: at $k \in [0.85, 0.95]$, Object tasks collapse under random removal while Spatial tasks degrade gracefully (Figure~\ref{fig:crosssuite}, Table~\ref{tab:pi05_crosssuite}). L2 norm maintains a near-baseline plateau on both suites ($\leq 2.4$\,pp at $k \geq 0.85$). CV$\,{=}\,$0.055 correctly predicts this plateau on both suites despite qualitatively different cliff profiles, confirming CV as a model-level diagnostic. Token importance heatmaps reveal a center-high, edge-low spatial pattern (Figure~\ref{fig:token_heatmap}, Appendix~\ref{app:token_heatmap}), formalized by a hypergeometric model $H(N{=}768,\, C{=}91,\, T{=}6)$: cliff onset at $k{=}0.96$ (10\% collapse probability) narrows to $k{=}0.90$ (90\%), RMSE${=}$0.025 (Appendix~\ref{app:cliff_model}). The model captures onset sharpness at high retention but does not generalize to moderate retention ($k \leq 0.7$), where compensatory mechanisms may emerge (\S\ref{sec:analysis}). The cross-suite difference is driven by Object's concentrated criticality ($C{=}91$) versus Spatial's distributed pattern ($C \approx 5$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "cfab877b-d66f-43fa-bd28-067ef18c9add"
}
```

</details>

---

### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/appendix.tex",
  "usage": {
    "total_tokens": 41775,
    "tool_uses": 11,
    "duration_ms": 23256
  },
  "last_tool_name": "Read",
  "uuid": "6bd9e5d2-002c-4b14-86bc-5670d0c46cc0",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_01MZJcrTTvrfJRJibZKyq9xN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "3d310835-d498-4305-9c37-ebcd87d3d9bf",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TWY1PoMtib55fNuD9t159T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 10986,
      "cache_read_input_tokens": 30745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10986,
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

_source line 64 · 2026-05-28T17:16:14.340Z_

<details><summary>↩ Tool result · `toolu_01MZJcrTTvrfJRJibZKyq9xN`</summary>

```text
1	\appendix
2	
3	\section{Full Pruning Results}
4	\label{app:full_results}
5	
6	Table~\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\ref{tab:main_results} for space.
7	
8	\begin{table*}[ht]
9	\centering
10	\footnotesize
11	\caption{Full closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \textsuperscript{$\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}
12	\label{tab:full_results}
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{llccccc}
15	\toprule
16	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
17	\midrule
18	\multirow{4}{*}{$\pi_{0.5}$}
19	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\
20	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\
21	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\
22	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\
23	\midrule
24	\multirow{4}{*}{X-VLA}
25	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\
26	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\
27	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\
28	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\
29	\midrule
30	\multirow{4}{*}{OpenVLA}
31	& Object  & \textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\textsuperscript{$\dagger$} & -- / -- & 39.2 / 35.8 \\
32	& Goal    & \textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
33	& Spatial & \textbf{80.0} & -- / -- & 75.0 / 79.8 / 80.4\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
34	& Long    & \textbf{52.8} & -- / -- & 43.6 / 46.8 / 44.0\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
35	\midrule
36	\multirow{4}{*}{SmolVLA}
37	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
38	& Spatial & \textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
39	& Goal    & \textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
40	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
41	\bottomrule
42	\end{tabular}
43	\end{table*}
44	
45	
46	\section{Extended Discussion}
47	\label{app:extended_discussion}
48	\label{app:discussion}
49	
50	\paragraph{Re-encoding and CV diagnostics.}
51	Both cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels, differentiating X-VLA's threshold-graded behavior (CV$\,{=}\,$0.151) from $\pi_0$'s uniformly critical profile (CV$\,{=}\,$0.038); the interaction reverses at $k{=}0.3$ (Appendices~\ref{app:cv_strategy_interaction},~\ref{app:cv_extended}).
52	
53	\paragraph{Task complexity compresses the importance margin.}
54	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector. OpenVLA illustrates the full pattern across LIBERO's complexity gradient (Figure~\ref{fig:openvla_sweep}).
55	
56	On single-step Object, L2 leads at moderate pruning ($+$7.8\,pp at $k{=}0.9$), but the three methods exhibit staggered cliffs---L2 earliest ($k{=}0.9{\to}0.85$, $-$15.4\,pp), random next, attention latest---each defining a distinct effective compression window before converging at $k{=}0.5$ ($<$4.8\,pp spread). As task complexity increases, the scoring hierarchy inverts. On Goal, random pruning at $k{=}0.9$ \emph{exceeds} the unpruned baseline ($+$4.8\,pp; cross-seed confirmed), suggesting OpenVLA's 256 vision tokens are over-provisioned for goal-conditioned tasks---random removal acts as implicit regularization. On Long, the inversion is complete: at $k{=}0.7$, Random (38.8\%) $>$ L2 (31.2\%) $>$ Attention (24.0\%), with attention degrading $2.5{\times}$ faster than random. The mechanism is consistent: multi-step tasks distribute critical information across tokens with heterogeneous norm profiles; L2 and attention both cluster on locally salient tokens, sacrificing the spatial diversity that compositional reasoning requires.
57	
58	\begin{figure}[ht]
59	\centering
60	\includegraphics[width=\linewidth]{figures/paper/fig_openvla_sweep.pdf}
61	\caption{OpenVLA scoring method comparison across four LIBERO suites. On Object, L2 leads at $k{=}0.9$ ($+$7.8\,pp) but the margin flips at $k{=}0.85$ ($-$5.2\,pp, Random wins). Goal degrades smoothly with three-method convergence at $k{=}0.7$. On Long, the ranking inverts with compression. No single scoring method dominates across suites or retention ratios.}
62	\label{fig:openvla_sweep}
63	\end{figure}
64	
65	This is a concrete manifestation of the two-axis framework (Section~\ref{sec:two_axis}): Axis~1 (connector architecture) determines \emph{whether} pruning is viable; Axis~2 (task complexity) determines \emph{which} scoring method succeeds. CV remains a valid connector diagnostic, but the optimal scoring strategy requires knowledge of both axes.
66	
67	\paragraph{Position encoding mediates the V-shape recovery.}
68	The monotonic L2 curve versus the non-monotonic random curve on $\pi_{0.5}$ Long (Figure~\ref{fig:cliff_highlight}) reflects an interaction between token selection strategy and positional encoding. L2 norm scoring preserves spatial locality: retained tokens form near-contiguous clusters in the ViT grid, producing continuous position shifts after re-indexing that Gemma's RoPE accommodates smoothly---hence monotonic degradation (86.8\% $\to$ 51.7\% from $k{=}0.95$ to $k{=}0.5$). Random selection creates scattered gaps that produce position aliasing after re-indexing. At $k{\approx}0.9$, the aliasing is maximally destructive: a small number of randomly placed gaps create highly irregular inter-token spacing, collapsing SR to 33.6\%. Per-task analysis reveals this aggregate is driven by specific tasks with position-sensitive spatial reasoning: Task~4 (``put mugs on plates'') drops from 80\% at $k{=}0.7$ to 12\% at $k{=}0.85$, contributing disproportionately to the V-shape minimum. At $k{=}0.7$, enough tokens are removed that the surviving positions become approximately uniform again, and SR recovers to 64.6\%---exceeding the $k{=}0.9$ level by ${\sim}2{\times}$. The zero-mask ablation (Section~\ref{sec:zeromask}) provides causal confirmation: zeroing token content while preserving positions yields 98.0\% SR, while physically removing the same tokens collapses to 9.0\%. Position encoding, not information content, is the binding constraint---and scoring method determines whether that constraint is violated.
69	
70	\paragraph{Per-task reversal within L2-dominant regimes.} The Long $k{=}0.85$ aggregate ($+$33.2\,pp for L2) masks extreme per-task heterogeneity (per-task $\sigma{=}$21.5\,pp). L2 outperforms random on 9 of 10 tasks ($+$16 to $+$52\,pp), but on Task~6---a dual-object spatial-relation task (``place white mug on plate \emph{and} chocolate pudding to the right of plate'')---L2 collapses to 8\% while random achieves 52\% ($-$44\,pp reversal). L2 scoring systematically undervalues tokens encoding spatial relationships, which carry low norms but are critical for relational reasoning. This per-task sign flip within an architecture where L2 dominates overall reinforces that no single scoring method is universally safe: task semantics, not just connector architecture or suite-level statistics, determine optimal strategy.
71	
72	\begin{figure}[ht]
73	\centering
74	\includegraphics[width=0.85\linewidth]{figures/paper/fig_scoring_crossover.pdf}
75	\caption{Scoring method comparison at $k{=}0.9$ across three models and four LIBERO suites. Cell color encodes SR as a fraction of unpruned baseline; blue bars mark the best method per condition; dashed borders indicate method-indifferent cells ($\Delta{<}3.5$\,pp). $\pi_{0.5}$'s linear connector strongly favors L2 selection, while X-VLA's BART encoder is largely method-indifferent. SmolVLA collapses to 0\% regardless of method. Compact 2$\times$2 summary in Appendix Table~\ref{tab:scoring_crossover_summary}.}
76	\label{fig:scoring_crossover}
77	\end{figure}
78	
79	\begin{figure}[ht]
80	\centering
81	\includegraphics[width=0.85\linewidth]{figures/paper/fig_margin_profile.pdf}
82	\caption{Importance margin (L2 $-$ Random SR) on $\pi_{0.5}$ Long across retention ratios (multi-seed mean $\pm$ s.d.; $n{=}5$). The margin peaks sharply at $k{=}0.9$ (46.9\,pp) where random pruning is maximally destructive, then declines asymmetrically: one step above the peak ($k{=}0.95$: 25.6\,pp) versus four steps below before crossing zero at $k{\approx}0.71$. At $k{=}0.5$, L2 and Random converge ($|\Delta|{\approx}1.3$\,pp), indicating that scoring method choice matters only in the moderate-pruning window.}
83	\label{fig:margin_profile}
84	\end{figure}
85	
86	\paragraph{Limitations (extended).}
87	All closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\pi_{0}$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\% official, 44.8\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.
88	
89	\paragraph{Non-monotonicity as structural property.}
90	X-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\% (L2) and 54.0\% (random), while $k{=}0.9$ recovers to 70.2\% under L2 selection (Table~\ref{tab:main_results}). The 0.2\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.
91	
92	\paragraph{$\pi_{0.5}$ random subsampling anomaly and RoPE amplification.}
93	Random selection on $\pi_{0.5}$ Object collapses from 74.0\% at $k{=}0.95$ to 9.0\% at $k{=}0.9$, then recovers to 74.0\% at $k{=}0.7$ (Table~\ref{tab:main_results}). The re-indexing step of our pruning protocol (Section~\ref{sec:pruning_protocol}) contributes to this non-monotonicity. $\pi_{0.5}$'s linear connector preserves a one-to-one mapping between spatial patches and token positions; when random removal shifts surviving tokens to new positions, the backbone's Rotary Position Embeddings (RoPE)~\cite{su2024roformer} encode spatial content at unfamiliar positions, amplifying disruption of learned attention patterns. X-VLA's BART encoder, which redistributes spatial information via cross-attention and lacks RoPE, provides a partial control. At $k{=}0.85$, single-step suites degrade smoothly (Spatial~68.2\%, Object~65.0\%, Goal~60.4\%), but Long drops to 35.0\%, below its $k{=}0.5$ performance of 61.6\% (Table~\ref{tab:xvla_k085_crosssuite}). Random re-indexing thus induces non-monotonic behavior for complex tasks even without RoPE, but RoPE amplifies the reversal: $\pi_{0.5}$ Object drops to 5.6\% at $k{=}0.85$ versus 69.4\% at $k{=}0.5$ ($-$63.8\,pp), more than double X-VLA Long's $-$26.6\,pp. The V-shaped recovery at $k \leq 0.7$ remains unexplained.
94	
95	\begin{table}[ht]
96	\centering
97	\small
98	\caption{Random pruning at $k{=}0.85$: X-VLA (BART encoder) vs.\ $\pi_{0.5}$ (linear connector). X-VLA degrades smoothly on single-step suites (60--68\%) but drops to 35.0\% on Long (below $k{=}0.5$); $\pi_{0.5}$ exhibits a severe disruption peak on Object.}
99	\label{tab:xvla_k085_crosssuite}
100	\begin{tabular}{lcccc}
101	\toprule
102	Suite & X-VLA SR (\%) & $\Delta$ & $\pi_{0.5}$ SR (\%) & $\Delta$ \\
103	\midrule
104	Object & 65.0 & $-$34.2 & 3.6--5.6\textsuperscript{$\dagger$} & $-$93 to $-$95 \\
105	Goal & 60.4 & $-$38.0 & 52.4 & $-$44.0 \\
106	Spatial & 68.2 & $-$24.8 & --- & --- \\
107	Long & 35.0 & $-$59.0 & --- & --- \\
108	\bottomrule
109	\multicolumn{5}{l}{\footnotesize\textsuperscript{$\dagger$}Two seeds: seed42$\,{=}\,$5.6\% (post-fix), seed43$\,{=}\,$3.6\%. $\Delta$ from respective baselines.}
110	\end{tabular}
111	\end{table}
112	
113	\paragraph{Small-$N$ interactions.}
114	X-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.6\,pp on Goal and $-$47.0\,pp on Long (L2 norm selection). Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.
115	
116	\paragraph{Design implications.}
117	Practitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.
118	
119	
120	\section{Cross-Suite Task Complexity Analysis}
121	\label{app:cross_suite_extended}
122	
123	LIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.
124	
125	$\pi_{0.5}$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\% (matching the baseline), Spatial retains 97.8\% (within noise of the 97.2\% baseline), and Goal drops to 89.4\% ($-$7.0\,pp from 96.4\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\% token removal.
126	
127	X-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 97.6\% ($-$1.6\,pp from the 99.2\% baseline), while Goal drops to 70.2\% ($-$28.2\,pp from 98.4\% baseline). Under random pruning at the same ratio, Object loses just 1.4\,pp (97.8\%) while Goal loses 27.8\,pp (70.6\%), a $20{\times}$ amplification. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\% to 47.0\% (L2) and 48.2\% (random), a 47.0\,pp loss with only 1.2\,pp method gap, while Object at the same ratio loses only 0.2\,pp.
128	
129	Token-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\pi_{0.5}$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.
130	
131	
132	\section{Pruning Protocol Details}
133	\label{app:pruning_details}
134	
135	Both pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.
136	
137	Model-specific retention ratios reflect each architecture's token count and expected sensitivity. $\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\pi_{0.5}$ uses $k \in \{0.3, 0.5, 0.7\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \in \{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \in \{0.3, 0.5, 0.7, 0.9, 0.95\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\ random), retention ratio ($k \in \{0.5, 0.7, 0.9, 0.95\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\cite{bolya2023tome}).
138	
139	The $\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\ three-layer MLP), backbone (PaliGemma vs.\ Llama-2), and encoder fusion strategy (single SigLIP vs.\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.
140	
141	
142	\section{SmolVLA Pruning Ablation}
143	\label{app:smolvla_ablation}
144	
145	\begin{table}[ht]
146	\centering
147	\small
148	\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\% SR. Two independent evaluations of the official HF checkpoint (59.2\% and 57.2\% baseline, within CI) confirm the cliff-edge across scoring methods.}
149	\label{tab:smolvla_ablation}
150	\begin{tabular}{llccrr}
151	\toprule
152	Scoring & $k$ & Mechanism & SR (\%) & Episodes & Wilson 95\% CI \\
153	\midrule
154	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\
155	\midrule
156	ACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
157	ACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
158	ACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
159	Random & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
160	Random & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
161	ACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\
162	ACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\
163	\midrule
164	\multicolumn{6}{l}{\textit{Official checkpoint, eval protocol A (59.2\% baseline)}} \\
165	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\
166	Random & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\
167	\midrule
168	\multicolumn{6}{l}{\textit{Official checkpoint, eval protocol B (57.2\% baseline)}} \\
169	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 57.2 & 500 & [52.9, 61.4] \\
170	Random & 0.95 & True removal & 0.0 & 500 & [0, 0.76] \\
171	L2 norm & 0.90 & True removal & 0.0 & 500 & [0, 0.76] \\
172	L2 norm & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\
173	\bottomrule
174	\end{tabular}
175	\end{table}
176	
177	
178	\section{Per-Task Breakdown Tables}
179	\label{app:per_task}
180	
181	\subsection{SmolVLA Baseline Per-Task Results}
182	
183	Table~\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\ref{tab:smolvla_ablation}) produce 0\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\% already reported.
184	
185	\begin{table}[ht]
186	\centering
187	\small
188	\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\%.}
189	\label{tab:smolvla_baseline_pertask}
190	\begin{tabular}{lc}
191	\toprule
192	Task & SR (\%) \\
193	\midrule
194	alphabet\_soup & 22 \\
195	bbq\_sauce & 60 \\
196	butter & 42 \\
197	chocolate\_pudding & 38 \\
198	cream\_cheese & 58 \\
199	ketchup & 26 \\
200	milk & 62 \\
201	orange\_juice & 38 \\
202	salad\_dressing & 50 \\
203	tomato\_sauce & 52 \\
204	\midrule
205	\textbf{Overall} & \textbf{44.8} \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	\subsection{Official SmolVLA Checkpoint Per-Task Results}
211	
212	Table~\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\_libero). Under 50\% random token removal, all tasks produce 0\% SR, identical to the fine-tuned checkpoint results.
213	
214	\begin{table}[ht]
215	\centering
216	\small
217	\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\%. Under 50\% random pruning, all tasks collapse to 0\%. An independent evaluation (protocol B) yields 57.2\% baseline with identical cliff-edge (Table~\ref{tab:smolvla_ablation}).}
218	\label{tab:smolvla_official_pertask}
219	\begin{tabular}{lcc}
220	\toprule
221	Task & Baseline SR (\%) & $k{=}0.5$ SR (\%) \\
222	\midrule
223	alphabet\_soup & 64 & 0 \\
224	bbq\_sauce & 38 & 0 \\
225	butter & 78 & 0 \\
226	chocolate\_pudding & 90 & 0 \\
227	cream\_cheese & 40 & 0 \\
228	ketchup & 60 & 0 \\
229	milk & 52 & 0 \\
230	orange\_juice & 80 & 0 \\
231	salad\_dressing & 44 & 0 \\
232	tomato\_sauce & 46 & 0 \\
233	\midrule
234	\textbf{Overall} & \textbf{59.2} & \textbf{0.0} \\
235	\bottomrule
236	\end{tabular}
237	\end{table}
238	
239	\subsection{OpenVLA Per-Task Results Under Pruning}
240	
241	\begin{table}[ht]
242	\centering
243	\small
244	\caption{OpenVLA per-task success rates (\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\%. Tasks requiring fine-grained discrimination (butter, cream\_cheese) degrade earliest; visually distinctive targets (orange\_juice, salad\_dressing) are most resilient.}
245	\label{tab:openvla_pertask}
246	\begin{tabular}{lccccc}
247	\toprule
248	Task & $k{=}0.95$ & $k{=}0.90$ & $k{=}0.70$ & $k{=}0.50$ & $k{=}0.30$ \\
249	\midrule
250	alphabet\_soup & 76 & 70 & 74 & 60 & 14 \\
251	bbq\_sauce & 38 & 28 & 46 & 44 & 30 \\
252	butter & 84 & 76 & 10 & 2 & 0 \\
253	chocolate\_pudding & 54 & 56 & 32 & 40 & 10 \\
254	cream\_cheese & 84 & 78 & 18 & 8 & 0 \\
255	ketchup & 82 & 70 & 68 & 50 & 30 \\
256	milk & 46 & 42 & 40 & 24 & 8 \\
257	orange\_juice & 74 & 60 & 76 & 72 & 42 \\
258	salad\_dressing & 64 & 54 & 64 & 36 & 64 \\
259	tomato\_sauce & 92 & 86 & 62 & 38 & 8 \\
260	\midrule
261	\textbf{Overall} & \textbf{69.4} & \textbf{62.0} & \textbf{49.0} & \textbf{37.4} & \textbf{20.6} \\
262	\bottomrule
263	\end{tabular}
264	\end{table}
265	
266	\subsection{OpenVLA Full Degradation Curve}
267	
268	\begin{table}[ht]
269	\centering
270	\small
271	\caption{OpenVLA success rates on LIBERO-Object under random token removal at six retention ratios (50 episodes per task, 500 total per ratio). Baseline SR: 74.0\%. All confidence intervals are Wilson 95\%.}
272	\label{tab:openvla_full}
273	\begin{tabular}{ccrr}
274	\toprule
275	$k$ & Tokens Retained & SR (\%) & Wilson 95\% CI \\
276	\midrule
277	1.00 (baseline) & 256 & 74.0 & [69.9, 77.7] \\
278	0.95 & 243 & 69.4 & [65.2, 73.3] \\
279	0.90 & 230 & 62.0 & [57.7, 66.2] \\
280	0.70 & 179 & 49.0 & [44.6, 53.4] \\
281	0.50 & 128 & 37.4 & [33.3, 41.7] \\
282	0.30 & 77 & 20.6 & [17.2, 24.4] \\
283	\bottomrule
284	\end{tabular}
285	\end{table}
286	
287	\subsection{$\pi_{0.5}$ LIBERO-Long Five-Seed Results}
288	\label{app:pi05_long_multiseed}
289	
290	\begin{table}[ht]
291	\centering
292	\small
293	\caption{$\pi_{0.5}$ LIBERO-Long success rates (\%) across five seeds (500 episodes each). All values are means over seeds 42--46 with sample standard deviation (ddof$\,{=}\,$1). The importance margin (L2$-$Random) peaks at $k{=}0.9$ (46.9\,pp) and crosses zero near $k{\approx}0.71$. Maximum per-seed range is 5.8\,pp (L2, $k{=}0.75$).}
294	\label{tab:pi05_long_multiseed}
295	\begin{tabular}{cccc}
296	\toprule
297	$k$ & L2 Norm (\%) & Random (\%) & Attention (\%) \\
298	\midrule
299	0.95 & $86.8 \pm 0.8$ & $61.2 \pm 0.7$ & $77.3 \pm 1.2$ \\
300	0.90 & $80.4 \pm 0.5$ & $33.6 \pm 1.2$ & $64.2 \pm 1.0$ \\
301	0.85 & $78.1 \pm 1.0$ & $44.9 \pm 1.3$ & $50.8 \pm 1.3$ \\
302	0.75 & $70.6 \pm 2.7$ & $63.0 \pm 1.7$ & $51.4 \pm 1.2$ \\
303	0.70 & $63.2 \pm 1.5$ & $64.6 \pm 1.8$ & $53.0 \pm 1.1$ \\
304	0.50 & $51.7 \pm 1.5$ & $50.4 \pm 0.6$ & $49.4 \pm 1.5$ \\
305	\bottomrule
306	\end{tabular}
307	\end{table}
308	
309	\subsection{$\pi_{0.5}$ L2 Norm Multi-Seed Consistency}
310	\label{app:pi05_multiseed}
311	
312	\begin{table}[ht]
313	\centering
314	\small
315	\caption{$\pi_{0.5}$ L2 norm-based removal across two seeds (500 episodes each). The V-shaped curve is reproduced with near-identical valleys ($\sigma{=}0.1$\,pp at $k{=}0.5$). V-depth: 17.6\,pp (seed42), 21.8\,pp (seed43).}
316	\label{tab:pi05_l2_multiseed}
317	\begin{tabular}{ccccc}
318	\toprule
319	$k$ & Seed 42 (\%) & Seed 43 (\%) & Mean $\pm$ Std & $\Delta$ (pp) \\
320	\midrule
321	0.70 & 55.0 & 57.8 & $56.4 \pm 2.0$ & $+$2.8 \\
322	0.50 & 33.4 & 33.6 & $33.5 \pm 0.1$ & $+$0.2 \\
323	0.30 & 51.0 & 55.4 & $53.2 \pm 3.1$ & $+$4.4 \\
324	\bottomrule
325	\end{tabular}
326	\end{table}
327	
328	\subsection{$\pi_{0.5}$ Cross-Suite Comparison}
329	\label{app:pi05_crosssuite}
330	
331	\begin{table}[ht]
332	\centering
333	\small
334	\caption{$\pi_{0.5}$ pruning across LIBERO-Object (baseline 98.2\%) and LIBERO-Spatial (baseline 97.2\%), seed\,42, 500 episodes each. Object random exhibits a deep cliff at $k \in [0.85, 0.925]$ absent on Spatial; L2 norm maintains a plateau across suites at high retention ($\leq 2.4$\,pp difference at $k \geq 0.85$).}
335	\label{tab:pi05_crosssuite}
336	\begin{tabular}{ccccc}
337	\toprule
338	\multirow{2}{*}{$k$} & \multicolumn{2}{c}{LIBERO-Object (\%)} & \multicolumn{2}{c}{LIBERO-Spatial (\%)} \\
339	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
340	 & L2 Norm & Random & L2 Norm & Random \\
341	\midrule
342	1.00 & 98.2 & 98.2 & 97.2 & 97.2 \\
343	0.95 & 98.2 & 74.0 & 97.8 & 76.4 \\
344	0.925 & 99.2 & 27.6 & 97.0 & 60.4 \\
345	0.90 & 98.2 & 9.0 & 95.0 & 54.6 \\
346	0.85 & 98.0 & 5.6 & 90.4 & 58.4 \\
347	0.70 & 55.0 & 74.0 & 67.0 & 74.4 \\
348	0.50 & 33.4 & 69.4 & 55.6 & 71.6 \\
349	0.30 & 51.0 & 36.4 & 57.2 & 49.6 \\
350	\bottomrule
351	\end{tabular}
352	\end{table}
353	
354	\begin{figure}[ht]
355	\centering
356	\includegraphics[width=0.85\linewidth]{figures/paper/fig_crosssuite.pdf}
357	\caption{$\pi_{0.5}$ cross-suite pruning profiles. Object random (green solid) exhibits a deep cliff at $k \in [0.85, 0.925]$ with 68\,pp recovery, absent on Spatial (blue solid). L2 norm (dashed) maintains a plateau on both suites through the cliff zone.}
358	\label{fig:crosssuite}
359	\end{figure}
360	
361	The random cliff at $k \in [0.85, 0.925]$ is task-specific: Object collapses from 74.0\% ($k{=}0.95$) to 5.6\% ($k{=}0.85$), whereas Spatial retains 58.4\% at $k{=}0.85$ ($\Delta{=}53$\,pp between suites). Spatial random also exhibits mild non-monotonicity ($k{=}0.925$: 60.4\% $>$ $k{=}0.9$: 54.6\%, $\Delta{=}5.8$\,pp), but this is an order of magnitude smaller than Object's 68\,pp V-dip. The cliff pattern suggests Object manipulation concentrates critical information in specific token subsets whose removal is catastrophic at narrow retention bands; Spatial tasks distribute critical information more uniformly, tolerating moderate random removal without catastrophic failure.
362	
363	L2 norm selection is consistent across suites at high retention ($k \geq 0.85$): Object and Spatial differ by $\leq 2.4$\,pp (Table~\ref{tab:pi05_crosssuite}). At $k \leq 0.7$, both suites exhibit the L2 V-shape (Object valley: 33.4\% at $k{=}0.5$; Spatial valley: 55.6\% at $k{=}0.5$), with Spatial maintaining higher absolute SR throughout. The method preference (random $>$ L2 at $k{=}0.5$; L2 $>$ random at $k{=}0.3$) is consistent across the two suites tested, suggesting the CV-strategy interaction may extend beyond a single task distribution.
364	
365	\subsection{Token Importance Spatial Distribution}
366	\label{app:token_heatmap}
367	
368	\begin{figure}[ht]
369	\centering
370	\includegraphics[width=0.85\linewidth]{figures/paper/fig_token_heatmap.pdf}
371	\caption{$\pi_{0.5}$ token importance spatial distribution (16$\times$16 grid, averaged over timesteps). Left: LIBERO-Object shows a pronounced center-high, edge-low pattern (center rows 7--9: norm $\sim$265--267; edge rows 0, 14--15: norm $\sim$235--236; CV${=}$0.066). Right: LIBERO-Spatial exhibits a flatter distribution (center-edge gap 14.67 vs.\ 21.87; CV${=}$0.059). The 33\% center-edge gap difference quantitatively explains Object's sharp cliff versus Spatial's graceful degradation under random removal.}
372	\label{fig:token_heatmap}
373	\end{figure}
374	
375	Token importance heatmaps reveal that $\pi_{0.5}$'s 768 vision tokens (reshaped to a 16$\times$16 spatial grid after the $\sqrt{d}$-scaled linear projection) exhibit a center-high, edge-low L2 norm pattern. At $k{=}0.9$ (26 tokens removed), L2 norm-based selection discards predominantly edge tokens: 50\% of removed tokens fall in the outermost ring despite edge positions comprising only 23\% of the grid. This spatial concentration is consistent with the center tokens encoding the robot arm and target object, while edge tokens capture less task-relevant background.
376	
377	Random removal at the same ratio samples deletions uniformly across the spatial grid, creating a combinatorial probability of simultaneously removing multiple high-importance center tokens. As more tokens are removed ($k{=}0.925 \to 0.85$), this probability increases sharply, consistent with the observed cliff onset. The asymmetry explains why L2 norm selection maintains a near-baseline plateau through the cliff zone: it preferentially preserves the high-importance center region that random removal disrupts by chance.
378	
379	\subsection{Hypergeometric Cliff Model}
380	\label{app:cliff_model}
381	
382	\begin{figure}[ht]
383	\centering
384	\includegraphics[width=0.85\linewidth]{figures/paper/fig_cliff_model.pdf}
385	\caption{Hypergeometric cliff model for $\pi_{0.5}$ Object random pruning. (a)~Model-predicted collapse probability (dashed) vs.\ observed success rate (solid) across the cliff zone $k \in [0.85, 0.95]$; RMSE${=}$0.025. (b)~$P(\text{collapse})$ curves for Object ($C{=}91$, concentrated) and Spatial ($C \approx 5$, distributed), illustrating why Object exhibits a sharp phase transition absent on Spatial.}
386	\label{fig:cliff_model}
387	\end{figure}
388	
389	The random cliff on $\pi_{0.5}$ Object (Section~\ref{app:cross_suite_extended}) can be modeled as a hypergeometric sampling problem. Among $N{=}768$ vision tokens, $C{=}106$ are critical. $C$ and $T$ are jointly fit by minimizing RMSE against three cliff-zone data points ($k \in \{0.9, 0.925, 0.95\}$; all post-fix confirmed). When $\lfloor N(1{-}k) \rfloor$ tokens are removed uniformly at random, the number of critical tokens removed follows a hypergeometric distribution $\mathrm{Hypergeometric}(N, C, \lfloor N(1{-}k) \rfloor)$. We define performance collapse as removing $\geq T{=}7$ critical tokens simultaneously; the fit yields $C{=}106$, $T{=}7$ with RMSE${=}$0.018. The fitted $C{=}106$ (13.8\% of tokens) is broadly consistent with the top-importance center region identified in the token heatmap (Figure~\ref{fig:token_heatmap}), providing post-hoc interpretability: the ``critical tokens'' correspond to spatially concentrated, high-norm positions encoding the robot arm and target object.
390	
391	The model predicts three characteristic retention ratios: $k{=}0.960$ where $P(\text{collapse}){=}10\%$ (cliff onset), $k{=}0.937$ where $P(\text{collapse}){=}50\%$ (midpoint), and $k{=}0.904$ where $P(\text{collapse}){=}90\%$ (near-complete collapse). The cliff width $\Delta k \approx 0.056$ between 10\% and 90\% collapse probability matches the observed transition from 74.0\% SR ($k{=}0.95$) to 9.0\% SR ($k{=}0.90$). At $k{=}0.85$ the model predicts near-certain collapse ($P{>}0.999$), consistent with the observed 5.6\% SR. The model captures the cliff onset and sharpness but does not explain the V-shape recovery at $k \leq 0.7$, where success rate rebounds to 74.0\%. The recovery lies outside the model's scope (which assumes monotonic collapse probability). We hypothesize that at aggressive pruning the model transitions to a qualitatively different computation regime, potentially relying on coarser spatial features that survive uniform subsampling, but this remains untested.
392	
393	The cross-suite difference emerges naturally from the critical token count. Object manipulation concentrates critical information in $C{=}106$ tokens (13.8\% of the grid), creating a steep increase in $P(\text{collapse} \geq T)$ over a narrow $k$ range. Spatial tasks distribute critical information across approximately $C \approx 5$ tokens, making the probability of simultaneously removing $\geq T$ critical tokens negligible at all tested retention ratios, consistent with Spatial's graceful degradation (58.4\% at $k{=}0.85$ vs.\ Object's 5.6\%).
394	
395	\subsection{OpenVLA Multi-Seed Consistency}
396	\label{app:openvla_multiseed}
397	
398	\begin{table}[ht]
399	\centering
400	\small
401	\caption{OpenVLA success rates (\%) on LIBERO-Object under random token removal across two seeds (500 episodes each). All values are within 5\,pp, confirming the graded degradation curve is reproducible. Main text (Table~\ref{tab:main_results}) uses seed 42 for both L2 and random.}
402	\label{tab:openvla_multiseed}
403	\begin{tabular}{cccc}
404	\toprule
405	$k$ & Seed 7 (\%) & Seed 43 (\%) & $\Delta$ (pp) \\
406	\midrule
407	0.90 & 62.0 & 62.2 & $+$0.2 \\
408	0.70 & 49.0 & 44.4 & $-$4.6 \\
409	0.50 & 37.4 & 35.6 & $-$1.8 \\
410	\bottomrule
411	\end{tabular}
412	\end{table}
413	
414	\subsection{L2 Norm vs.\ Random Scoring on OpenVLA}
415	\label{app:l2_vs_random}
416	
417	\begin{table}[ht]
418	\centering
419	\small
420	\caption{OpenVLA cross-seed comparison on LIBERO-Object (500 episodes per configuration). L2 uses seed$\,{=}\,$42; random uses seed$\,{=}\,$7. Main text (Table~\ref{tab:main_results}) reports seed-42 random where available ($k{=}0.9$: 62.8\%, $k{=}0.5$: 35.8\%). Same-seed (seed42) random at $k{=}0.3$ yields 21.4\% (L2 outperforms by 3.6\,pp); same-seed at $k{=}0.7$ yields 44.4\% (L2 outperforms by 5.4\,pp). $\Delta$ is defined as L2$-$Random (positive indicates L2 advantage).}
421	\label{tab:openvla_l2_vs_random}
422	\begin{tabular}{cccc}
423	\toprule
424	$k$ & L2 Norm SR (\%) & Random SR (\%) & $\Delta$ (pp) \\
425	\midrule
426	0.95 & 70.6 & 69.4 & $+$1.2 \\
427	0.90 & 70.6 & 62.0 & $+$8.6 \\
428	0.70 & 49.8 & 49.0 & $+$0.8 \\
429	0.50 & 39.2 & 37.4 & $+$1.8 \\
430	0.30 & 25.0 & 20.6 & $+$4.4 \\
431	\bottomrule
432	\end{tabular}
433	\end{table}
434	
435	\subsection{X-VLA Cliff Localization: Per-Task Analysis}
436	\label{app:xvla_cliff}
437	
438	\begin{table}[ht]
439	\centering
440	\small
441	\caption{X-VLA per-task success rates (\%) at $k{=}0.80$ (40 of 50 tokens) and $k{=}0.85$ (42 of 50 tokens) on LIBERO-Object. Per-task breakdown is mean of 2 seeds (50 episodes per task per seed, 100 total); overall values are confirmed across 3 seeds ($89.0 \pm 0.7$\% at $k{=}0.80$, $67.9 \pm 0.3$\% at $k{=}0.85$). Despite retaining \emph{fewer} tokens, $k{=}0.80$ outperforms $k{=}0.85$ by 21.1\,pp overall. Four tasks (\textbf{bold}) suffer catastrophic interference ($\Delta \leq -50$\,pp) from two additional low-importance tokens (L2 rank 41--42 of 50) at $k{=}0.85$; the remaining six are unaffected ($|\Delta| \leq 10$\,pp). Cross-seed variance is $\leq 4$\,pp per task.}
442	\label{tab:xvla_cliff_pertask}
443	\begin{tabular}{lccr}
444	\toprule
445	Task & $k{=}0.80$ (\%) & $k{=}0.85$ (\%) & $\Delta$ (pp) \\
446	\midrule
447	alphabet\_soup & 100.0 & 100.0 & 0 \\
448	bbq\_sauce & 85.0 & 87.0 & $+$2 \\
449	\textbf{butter} & \textbf{57.0} & \textbf{0.0} & $\boldsymbol{-57}$ \\
450	\textbf{chocolate\_pudding} & \textbf{88.0} & \textbf{35.0} & $\boldsymbol{-53}$ \\
451	\textbf{cream\_cheese} & \textbf{98.0} & \textbf{45.0} & $\boldsymbol{-53}$ \\
452	\textbf{ketchup} & \textbf{79.0} & \textbf{27.0} & $\boldsymbol{-52}$ \\
453	milk & 85.0 & 95.0 & $+$10 \\
454	orange\_juice & 96.0 & 98.0 & $+$2 \\
455	salad\_dressing & 100.0 & 100.0 & 0 \\
456	tomato\_sauce & 98.0 & 91.0 & $-$7 \\
457	\midrule
458	\textbf{Overall} & \textbf{89.0} & \textbf{67.9} & $\boldsymbol{-21.1}$ \\
459	\bottomrule
460	\end{tabular}
461	\end{table}
462	
463	The non-monotonic pattern is reproducible across both seeds: the same four tasks (butter, chocolate\_pudding, cream\_cheese, ketchup) exhibit catastrophic drops at $k{=}0.85$, while the remaining six maintain or improve performance. This task-specific sensitivity is consistent with the BART encoder creating entangled dependencies among marginal tokens: at $k{=}0.85$, two additional low-importance tokens (L2 rank 41--42) introduce interference that selectively disrupts tasks requiring fine-grained spatial discrimination. The four affected tasks all involve small, visually similar grocery items, while the robust tasks (alphabet\_soup, salad\_dressing) feature distinctive objects or high-contrast targets.
464	
465	\subsection{VTR Per-Task Comparison}
466	
467	\begin{table}[ht]
468	\centering
469	\small
470	\caption{VTR per-task success rates on LIBERO-Object for $M \in \{32, 64, 128\}$ (seed 42; 3-seed means are reported in Table~\ref{tab:vtr_results}). All three achieve similar overall SR (59.8\%--61.6\%), but individual task performance varies substantially across configurations, with per-task differences up to 30 percentage points.}
471	\label{tab:smart_compress_pertask}
472	\begin{tabular}{lcccc}
473	\toprule
474	Task & $M{=}32$ (\%) & $M{=}64$ (\%) & $M{=}128$ (\%) \\
475	\midrule
476	alphabet\_soup & 68 & 74 & 62 \\
477	bbq\_sauce & 46 & 56 & 34 \\
478	butter & 82 & 84 & 82 \\
479	chocolate\_pudding & 90 & 74 & 82 \\
480	cream\_cheese & 64 & 38 & 58 \\
481	ketchup & 66 & 64 & 62 \\
482	milk & 76 & 62 & 56 \\
483	orange\_juice & 28 & 46 & 58 \\
484	salad\_dressing & 60 & 64 & 54 \\
485	tomato\_sauce & 36 & 54 & 50 \\
486	\midrule
487	\textbf{Overall} & \textbf{61.6} & \textbf{61.6} & \textbf{59.8} \\
488	\bottomrule
489	\end{tabular}
490	\end{table}
491	
492	\subsection{VTR Multi-Seed Results}
493	
494	\begin{table}[ht]
495	\centering
496	\small
497	\caption{VTR success rates across three seeds on LIBERO-Object (500 episodes each). Mean $\pm$ std reported.}
498	\label{tab:multi_seed}
499	\begin{tabular}{lccccr}
500	\toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "301cd81e-a0d6-459a-bb4b-cc4fcf623618"
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
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/experiments.tex",
  "usage": {
    "total_tokens": 41776,
    "tool_uses": 12,
    "duration_ms": 23743
  },
  "last_tool_name": "Read",
  "uuid": "7445fb63-f7c5-4ab5-9b65-e177b52335d0",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01Wtnapx8YedE6qtzqWCj7SJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "665f9a96-1822-4166-af0e-80be8a0006b9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TWY1PoMtib55fNuD9t159T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 10986,
      "cache_read_input_tokens": 30745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10986,
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

_source line 67 · 2026-05-28T17:16:14.531Z_

<details><summary>↩ Tool result · `toolu_01Wtnapx8YedE6qtzqWCj7SJ`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\times$ 50 episodes each).
8	
9	Four models are evaluated in closed-loop control: $\pi_{0.5}$~\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$, 128 tokens, CV$\,{=}\,$0.314). Two additional models ($\pi_{0}$~\cite{black2024pi0}, OFT~\cite{kim2025openoft}) are analyzed via offline metrics only. Table~\ref{tab:model_properties} summarizes all six architectures. We prune at $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$, reporting mean success rate (SR) over 500 episodes.
10	
11	\subsection{Two-Axis Framework Overview}
12	\label{sec:two_axis}
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
17	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
18	\label{fig:pruning_overview}
19	\end{figure}
20	
21	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
22	
23	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. L2 maintains ${\geq}$98.0\% through $k{=}0.85$, while random at $k{=}0.9$ collapses to 9.0\%---an 89\,pp method gap from identical removal fractions.
24	
25	\textbf{X-VLA (BART encoder, CV$\,{=}\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\,pp, yet the same model drops 27.4\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.
26	
27	\textbf{OpenVLA (MLP, CV$\,{=}\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\ref{tab:full_results}; Section~\ref{sec:analysis}).
28	
29	\textbf{SmolVLA (pixel-shuffle, CV$\,{=}\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\leq}$6.6\% across all suites and methods---a catastrophic cliff detailed below.
30	
31	\begin{table*}[t]
32	\centering
33	\small
34	\caption{Closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\leq}$6.6\% across all conditions. $\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\ref{tab:full_results}.}
35	\label{tab:main_results}
36	\begin{tabular}{llcccc}
37	\toprule
38	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
39	\midrule
40	\multirow{4}{*}{$\pi_{0.5}$}
41	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 33.4 / 69.4 \\
42	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\
43	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\
44	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\
45	\midrule
46	\multirow{4}{*}{X-VLA}
47	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\
48	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\
49	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\
50	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\
51	\midrule
52	\multirow{4}{*}{SmolVLA}
53	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
54	& Spatial & \textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
55	& Goal    & \textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
56	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
57	\bottomrule
58	\end{tabular}
59	\end{table*}
60	
61	\subsection{Pixel-Shuffle Entanglement}
62	\label{sec:pixel_shuffle}
63	
64	\begin{figure*}[t]
65	\centering
66	\begin{subfigure}[t]{0.495\textwidth}
67	\centering
68	\includegraphics[width=\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
69	\label{fig:pixel_shuffle}
70	\end{subfigure}
71	\hfill
72	\begin{subfigure}[t]{0.495\textwidth}
73	\centering
74	\includegraphics[width=\linewidth]{figures/paper/fig_method_gap.pdf}
75	\label{fig:method_gap}
76	\end{subfigure}
77	\caption{Token entanglement and scoring sensitivity. \textbf{(a)}~Pixel-shuffle $4{\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \textbf{(b)}~Method gap $|\text{SR(L2)} - \text{SR(Random)}|$ at $k{=}0.95$: $\pi_{0.5}$'s Object gap (24.2\,pp) exceeds X-VLA's maximum (1.4\,pp) by $17{\times}$ (single seed except $\pi_{0.5}$ Long, $n{=}5$).}
78	\label{fig:entanglement_scoring}
79	\end{figure*}
80	
81	SmolVLA's pixel-shuffle $4{\times}4$ folding concatenates 16 patches per token (Figure~\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\leq}$6.6\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.
82	
83	\subsection{Position Disruption vs.\ Information Loss}
84	\label{sec:zeromask}
85	
86	$\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\% on Object despite removing only 10\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\% SR while hard pruning collapses to 9.0\%. The 89\,pp gap is entirely attributable to position disruption---$\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.
87	
88	\subsection{Scoring Method Sensitivity and CV Diagnostic}
89	\label{sec:cv_sensitivity}
90	
91	CV predicts where scoring method choice becomes critical (Figure~\ref{fig:method_gap}). $\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\,pp, exceeding X-VLA's maximum (1.4\,pp) by $17{\times}$. At $k{=}0.5$, $\Delta$(R$-$L2) on Object is $+$36.0\,pp ($\pi_{0.5}$), $+$27.2\,pp (X-VLA), confirming random preserves spatial diversity while L2 clusters correlated tokens.
92	
93	\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\geq}$92.8\% while L2 falls 8--27\,pp below random; on $\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\,pp). On Long, attention cliffs $-$26.5\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\ref{fig:cliff_highlight}).
94	
95	\textbf{Disruption peak.} Random pruning on $\pi_{0.5}$ is \emph{more} destructive at intermediate than aggressive ratios. On Long at $k{=}0.9$, the margin peaks at 46.9\,pp (L2 80.4\% vs.\ Random 33.6\%; Figure~\ref{fig:cliff_highlight}); at $k{=}0.5$ all methods converge within ${\sim}$2\,pp (Appendix Figure~\ref{fig:margin_profile}). The V-shaped random recovery arises from position aliasing under scattered removal (Section~\ref{sec:analysis}).
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=0.75\linewidth]{figures/paper/fig_cliff_highlight.pdf}
100	\caption{Scoring method determines cliff behavior on $\pi_{0.5}$ Long (five-seed mean $\pm$ s.d.\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\,pp gap vs.\ L2) and recovery at $k{\leq}0.7$.}
101	\label{fig:cliff_highlight}
102	\end{figure}
103	
104	\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\pi_{0.5}$ at $k{=}0.85$: Object $+$93\,pp $>$ Goal $+$35.2\,pp $>$ Long $+$33.2\,pp, as multi-step tasks distribute critical information across heterogeneous norm profiles.
105	
106	\subsection{VTR Recovery}
107	\label{sec:vtr_recovery}
108	
109	VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\sim}$22M parameters, ${\sim}$5\% of SmolVLA), recovering from 0.0\% to over 60\% SR at 75\% compression ($M{=}32$: 60.1 $\pm$ 1.3\%, 3 seeds; Table~\ref{tab:vtr_main}). A parameter-matched MLP adapter achieves 63.4 $\pm$ 2.6\% ($p{=}0.15$), confirming the gain stems from re-encoding, not cross-attention. Cross-suite: Spatial 53.2\%, Goal 56.4\%, both from 0.0\%.
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\%; VTR recovers ${\geq}$57\% at up to 87.5\% compression.}
115	\label{tab:vtr_main}
116	\begin{tabular}{lccr}
117	\toprule
118	Configuration & $M$ & Compress.\ & SR (\%) \\
119	\midrule
120	\textit{Baseline (unpruned)} & 128 & 0\% & 44.8 \\
121	\textit{Hard pruning (any)} & -- & 5--50\% & 0.0 \\
122	\midrule
123	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
124	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
125	MLP adapter & 32 & 75\% & 63.4 $\pm$ 2.6 \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	\textbf{Efficiency.}\label{sec:efficiency} For $\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\sim}$16\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\% compression with ${\leq}$1.1\,pp below passthrough.
131	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "2ad9c16d-fd81-4474-8960-47243028d5f7"
}
```

</details>

---

### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/analysis.tex",
  "usage": {
    "total_tokens": 41777,
    "tool_uses": 13,
    "duration_ms": 24026
  },
  "last_tool_name": "Read",
  "uuid": "8f3a1e76-fcb0-462a-9c0f-b8be6ff28300",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01PSr4usC8dYPAHww8WDrJx4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "f180473f-fab8-41e0-9b47-bf478704ee77",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TWY1PoMtib55fNuD9t159T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 10986,
      "cache_read_input_tokens": 30745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10986,
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

_source line 70 · 2026-05-28T17:16:14.814Z_

<details><summary>↩ Tool result · `toolu_01PSr4usC8dYPAHww8WDrJx4`</summary>

```text
1	\section{Discussion}
2	\label{sec:analysis}
3	
4	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector. On OpenVLA, L2 leads on single-step Object ($+$7.8\,pp at $k{=}0.9$) but the hierarchy inverts on multi-step Long, where Random outperforms both L2 and attention at $k{=}0.7$ (Appendix~\ref{app:extended_discussion}). The monotonic L2 curve versus the non-monotonic random curve on $\pi_{0.5}$ Long (Figure~\ref{fig:cliff_highlight}) reflects position encoding sensitivity: L2 preserves spatial locality after re-indexing, while random creates scattered gaps that maximally disrupt RoPE at $k{\approx}0.9$ before recovering at $k{\leq}0.7$ as surviving positions become approximately uniform (Appendix~\ref{app:extended_discussion}).
5	
6	\paragraph{Limitations.}
7	All evaluations use LIBERO simulation; we provide no sim-to-real evidence. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing causal isolation. The CV--SR correlation relies on four closed-loop models, too few for a general law. VTR is validated on SmolVLA only. Most conditions use a single seed; $\pi_{0.5}$ Long uses five-seed means ($n{=}5$, sample s.d.\ ${\leq}$2.7\,pp; Appendix~\ref{app:pi05_long_multiseed}); cross-seed validation on other models shows $\Delta \leq 5.8$\,pp (Appendix~\ref{app:pi05_multiseed},~\ref{app:openvla_multiseed}). Extended discussion in Appendix~\ref{app:extended_discussion}.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "3302a607-9f5f-498e-a7be-82c1d510913a"
}
```

</details>

---

### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/conclusion.tex",
  "usage": {
    "total_tokens": 62468,
    "tool_uses": 14,
    "duration_ms": 26911
  },
  "last_tool_name": "Read",
  "uuid": "821b1544-b065-4dea-8771-c7961b8b16c6",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01AWiHjmRL8mJWrFJDswVFdF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "676666e2-3ed5-484c-9fdc-dd1b5c274bd7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TsnyzUHweXJLmnDc7KR1ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 20683,
      "cache_read_input_tokens": 41731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20683,
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

_source line 73 · 2026-05-28T17:16:17.705Z_

<details><summary>↩ Tool result · `toolu_01AWiHjmRL8mJWrFJDswVFdF`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	\label{sec:analysis}
4	
5	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector---L2 leads on $\pi_{0.5}$ Object but inverts on Long; on X-VLA, attention recovers near-baseline while L2 is anti-informative (Appendix~\ref{app:extended_discussion}). The V-shaped random recovery on $\pi_{0.5}$ Long reflects position encoding sensitivity: scattered gaps maximally disrupt RoPE at $k{\approx}0.9$, recovering as surviving positions become approximately uniform.
6	
7	Connector architecture is the primary factor governing VLA token compressibility. Token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity ($20{\times}$ from Object to Goal). CV partitions models in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and $k$-dependent. Where all deletion fails, VTR recovers over 60\% SR at 75\% compression. Real-robot validation and adaptive per-task pruning schedules remain open.
8	
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "da2fa2fe-b140-4b98-b74a-3d08fc962ac7"
}
```

</details>

---

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/abstract.tex",
  "usage": {
    "total_tokens": 62472,
    "tool_uses": 15,
    "duration_ms": 27017
  },
  "last_tool_name": "Read",
  "uuid": "6bf454ab-6365-4f07-9818-4563c0167488",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_011TqBoGRnPcbfLntjpZc5kQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "7a7e41ff-3eba-4350-932b-d9a835c4d0d9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TsnyzUHweXJLmnDc7KR1ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 20683,
      "cache_read_input_tokens": 41731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20683,
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

_source line 76 · 2026-05-28T17:16:17.805Z_

<details><summary>↩ Tool result · `toolu_011TqBoGRnPcbfLntjpZc5kQ`</summary>

```text
1	\begin{abstract}
2	Vision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\pi_{0.5}$ preserves 98\% task success while SmolVLA collapses to 0\%---why?
3	
4	We identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\,{=}\,$0.038 (near-immune linear projection) to CV$\,{=}\,$0.314 (catastrophic pixel-shuffle collapse). Across five VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.
5	
6	Importance-based selection is not universally beneficial---it can be actively harmful. L2 norm selection preserves 98\% success on $\pi_{0.5}$ where random yields 5\% (93\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\,pp. No scoring method is universally safe: task complexity amplifies connector-dependent patterns ($20{\times}$ from Object to Goal). A zero-mask ablation isolates the mechanism: zeroing 10\% of tokens preserves 98.0\% SR while physical removal collapses to 9.0\%---the 89\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion fails, a lightweight re-encoding module (${\sim}$5\% extra parameters) recovers $>$60\% success at 75\% compression.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "3dfd0434-e14c-4224-9025-33aeae379e2b"
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
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Reading docs/paper/sections/related_work_draft.tex",
  "usage": {
    "total_tokens": 62476,
    "tool_uses": 16,
    "duration_ms": 27223
  },
  "last_tool_name": "Read",
  "uuid": "cb43c65d-bacc-40dc-af13-ff6535146925",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_01Qb8ERmQpq1oTjNEGgMXR8g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/related_work_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "187e71f2-54cf-4ec4-b4f0-c4be6856cfc8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TsnyzUHweXJLmnDc7KR1ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 20683,
      "cache_read_input_tokens": 41731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20683,
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

_source line 79 · 2026-05-28T17:16:18.012Z_

<details><summary>↩ Tool result · `toolu_01Qb8ERmQpq1oTjNEGgMXR8g`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Vision-Language-Action Models}
5	
6	Recent advances in foundation models have enabled a new class of robotic policies that map visual observations and language instructions directly to actions. RT-2~\cite{brohan2023rt2} first demonstrated that fine-tuning large vision-language models on robot demonstrations transfers web-scale semantic knowledge to robotic control; it tokenizes actions as text and trains jointly on internet and robot data. Octo~\cite{ghosh2024octo} introduced a modular transformer backbone trained on 800k trajectories from the Open X-Embodiment dataset, with flexible adaptation to new observation spaces and embodiments. OpenVLA~\cite{kim2024openvla} scaled this paradigm to 7B parameters with a fused SigLIP-DinoV2 visual encoder and an MLP projector that maps visual embeddings into the Llama~2 input space; it outperforms RT-2-X (55B) by 16.5\% in absolute success rate with 7$\times$ fewer parameters. SmolVLA~\cite{shukor2025smolvla} pursued the opposite end of the efficiency spectrum: a 450M-parameter model that combines aggressive pixel shuffle compression (64 visual tokens per frame) with a flow-matching action expert, and matches or exceeds larger VLAs on both simulation and real-world benchmarks. $\pi_0$~\cite{black2024pi0} and $\pi_{0.5}$~\cite{physicalintelligence2025pi05} built on PaLiGemma with a separate action expert connected via cross-attention and produce smooth 50Hz action trajectories through flow matching.
7	
8	A critical but underexplored dimension across these models is the \emph{vision connector}: the module that bridges the visual encoder and the language/action backbone. OpenVLA and LLaVA~\cite{liu2023llava} use per-patch MLP projectors that preserve the spatial independence of each visual token. SmolVLA and InternVL~\cite{chen2024internvl} employ pixel shuffle (space-to-depth) connectors that fold spatial neighborhoods into channel dimensions before projection, creating tokens whose information content spans multiple spatial locations. BLIP-2~\cite{li2023blip2} introduced the Q-Former, a learned cross-attention bottleneck with fixed-size query vectors, while Flamingo~\cite{alayrac2022flamingo} proposed the Perceiver Resampler for a similar purpose. These architectural choices determine how visual information is distributed across tokens, yet no prior work has systematically studied how connector type affects the compressibility of the resulting token sequences in the context of action generation.
9	
10	\subsection{Token Efficiency in Vision-Language Models}
11	
12	Reducing the computational cost of visual tokens has been extensively studied in the vision transformer and VLM literature. DynamicViT~\cite{rao2021dynamicvit} introduced learnable prediction modules that progressively prune tokens at multiple transformer layers and reduce FLOPs by 30\% with less than 0.5\% accuracy loss. Token Merging (ToMe)~\cite{bolya2023tome} takes a complementary approach, bipartite-matching similar tokens and merging them rather than discarding, which preserves foreground information that pruning-based methods may lose. EViT~\cite{liang2022evit} reorganizes tokens by fusing inattentive patches into a single representative token, guided by class token attention. FastV~\cite{chen2024fastv} extended these ideas to multimodal LLMs and showed that 50\% of visual tokens can be pruned after shallow layers with negligible performance loss on image and video understanding tasks.
13	
14	In the VLA setting, several concurrent works have adapted token pruning for robotic control. VLA-IAP~\cite{cheng2026vlaiap} proposed an interaction-aligned pruning strategy that preserves structurally critical manipulation regions through a geometric prior and retains 97.8\% success rate on OpenVLA with 1.25$\times$ speedup. VLA-Pruner~\cite{liu2025vlapruner} introduced dual-level importance scoring that combines semantic prefill attention with action decode attention estimated via temporal smoothing. VLA-Cache~\cite{xu2025vlacache} exploits temporal coherence between consecutive frames to reuse KV-cache entries for unchanged visual tokens. At the LLM level, H$_2$O~\cite{zhang2023h2o} identified ``heavy hitter'' tokens that dominate attention scores and proposed a KV-cache eviction policy that retains only these high-utility entries.
15	
16	A common limitation of these methods is that they were developed and evaluated on a single architecture (typically OpenVLA or a standard VLM with MLP projection). Whether the same pruning strategies transfer across architectures with fundamentally different vision connectors remains untested. Our work fills this gap by showing that connector choice determines whether token pruning produces graceful degradation or catastrophic failure.
17	
18	\subsection{Vision Connectors and Information Density}
19	
20	The vision connector governs how spatial information from the visual encoder is reorganized before entering the language model, and this reorganization has direct consequences for per-token information density. MLP projectors, as used in LLaVA~\cite{liu2023llava} and OpenVLA~\cite{kim2024openvla}, apply independent linear transformations to each patch embedding. Because each output token corresponds to exactly one spatial location, removing a token discards information from that location alone, and the remaining tokens retain their original semantics. This locality property makes MLP-projected tokens amenable to importance-based pruning: low-attention tokens can be dropped with bounded information loss.
21	
22	Pixel shuffle connectors, adopted by SmolVLA~\cite{shukor2025smolvla} and InternVL~\cite{chen2024internvl}, operate differently. The space-to-depth rearrangement groups $k \times k$ spatial neighborhoods and concatenates their features along the channel dimension before a linear projection. The resulting tokens each encode a mixture of $k^2$ original patch representations. This creates two related problems for token pruning. First, tokens are no longer spatially independent: dropping one token removes information from multiple spatial positions, and the lost information cannot be recovered from neighboring tokens because they encode \emph{different} spatial neighborhoods. Second, the information content per token is higher and more uniformly distributed, so the assumption that some tokens carry negligible information (the basis for attention-based pruning) breaks down. We refer to this phenomenon as \emph{token entanglement} and show empirically that it produces a cliff-edge failure mode: even modest pruning ratios cause complete task failure (0\% success rate) on SmolVLA, in contrast to the graded degradation observed on OpenVLA.
23	
24	Learned compression modules such as the Q-Former~\cite{li2023blip2} and Perceiver Resampler~\cite{alayrac2022flamingo} represent a third paradigm. These modules use a fixed set of learnable queries that cross-attend to the full set of visual features, and produce a compact representation trained end-to-end to preserve task-relevant information. Unlike pixel shuffle, the compression is adaptive: the cross-attention weights determine which spatial regions contribute to each output token based on learned relevance rather than fixed spatial grouping. This adaptivity makes learned compression a natural candidate for addressing the token entanglement problem in pixel shuffle architectures.
25	
26	\subsection{Learned Token Compression}
27	
28	Cross-attention-based compression was introduced in the vision-language literature to reduce the number of visual tokens entering the language model. The Q-Former in BLIP-2~\cite{li2023blip2} uses 32 learnable queries in a 12-layer transformer that cross-attends to frozen image encoder outputs; it acts as an information bottleneck trained in two stages, first for vision-language representation learning and then for generative pre-training. The Perceiver Resampler in Flamingo~\cite{alayrac2022flamingo} serves a similar function: it maps variable-length spatio-temporal visual features to a fixed number of output tokens that condition the language model through gated cross-attention layers.
29	
30	These architectures were designed to bridge modality gaps in VLMs, not to address the specific challenges of compressing entangled token representations in VLA models. Our Smart Compress module draws on the same cross-attention mechanism but applies it to a different problem: recovering compressibility in architectures where post-connector tokens resist importance-based pruning. By training a small set of queries to cross-attend to the pixel-shuffle output, the module learns to disentangle the spatial information that was mixed during the space-to-depth rearrangement and yields tokens that can be pruned without catastrophic failure. This positions learned compression not as an alternative to token pruning, but as a prerequisite for making pruning viable on entangled architectures.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "06c4330e-baa3-4af4-9678-788a10a856e6"
}
```

</details>

---

### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Running cd /home/ubuntu/.agent-ml-research-be-idea-gen-05…",
  "usage": {
    "total_tokens": 65849,
    "tool_uses": 17,
    "duration_ms": 30692
  },
  "last_tool_name": "Bash",
  "uuid": "5c253950-0334-4d8d-b077-4aba64977617",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_01U1P3DpqVrDgnaWzJCAdXEb`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -exec grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" {} \\; | sed 's/.*\\\\cite[tp]*{\\([^}]*\\)}.*/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "1ed6177c-1863-49f4-b88a-9cc056c197df",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VP35i4U7EsCPRfTLX6DiGu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 3371,
      "cache_read_input_tokens": 62414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3371,
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

_source line 82 · 2026-05-28T17:16:21.589Z_

<details><summary>↩ Tool result · `toolu_01U1P3DpqVrDgnaWzJCAdXEb`</summary>

```text
abnar2020quantifying
alayrac2022flamingo
black2024pi0
black2025pi05
bolya2023tome
brohan2023rt2
chen2024fastv
chen2024internvl
cheng2026vlaiap
gao2025compressorvla
karl2024negative
kim2024openvla
kim2025openoft
lewis2020bart
li2024cogact
liang2022evit
lipman2023flow
liu2023libero
liu2025vlapruner
physicalintelligence2025pi05
rao2021dynamicvit
shi2016subpixel
shukor2025smolvla
su2024roformer
xu2025vlacache
yang2024qwen2
yang2025efficientvla
zeng2023transformers_tsf
zhai2023siglip
zhang2023h2o
zheng2025xvla
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "d914e577-70fe-4a0c-bc02-186286caa7e0"
}
```

</details>

---

### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Running cd /home/ubuntu/.agent-ml-research-be-idea-gen-05…",
  "usage": {
    "total_tokens": 66283,
    "tool_uses": 18,
    "duration_ms": 33637
  },
  "last_tool_name": "Bash",
  "uuid": "0c439566-24e9-44b5-94aa-e9191bf4fee5",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_014ZLwffECM2HdTdv5FeaVn3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -exec grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" {} \\; | grep -o \"\\\\\\\\cite[tp]*{[^}]*}\" | sed 's/.*{\\([^}]*\\)}/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort | uniq -c | sort -rn"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "d4fec6af-4074-4493-98f1-8f1fedfc086e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AMT2Ts33bfAfuxoeuixHQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 433,
      "cache_read_input_tokens": 65785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 433,
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

_source line 85 · 2026-05-28T17:16:24.524Z_

<details><summary>↩ Tool result · `toolu_014ZLwffECM2HdTdv5FeaVn3`</summary>

```text
     15 shukor2025smolvla
     15 bolya2023tome
     13 liu2023libero
     13 kim2024openvla
     10 zhai2023siglip
     10 rao2021dynamicvit
     10 black2024pi0
      9 liang2022evit
      7 yang2025efficientvla
      7 kim2025openoft
      7 cheng2026vlaiap
      7 black2025pi05
      6 zheng2025xvla
      6 xu2025vlacache
      6 li2024cogact
      4 li2023blip2
      4 lewis2020bart
      4 chen2024fastv
      3 yang2024qwen2
      3 liu2025vlapruner
      3 liu2023llava
      3 brohan2023rt2
      3 alayrac2022flamingo
      2 oquab2023dinov2
      2 lipman2023flow
      2 chen2024internvl
      1 zhang2023h2o
      1 zeng2023transformers_tsf
      1 yin2022avit
      1 su2024roformer
      1 shi2016subpixel
      1 shang2024prumerge
      1 physicalintelligence2025pi05
      1 karl2024negative
      1 jiang2026lightvla
      1 ghosh2024octo
      1 gao2025compressorvla
      1 abnar2020quantifying
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "229ab344-85f3-4e61-bcf2-0b10c7dff626"
}
```

</details>

---

### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Running cd /home/ubuntu/.agent-ml-research-be-idea-gen-05…",
  "usage": {
    "total_tokens": 66912,
    "tool_uses": 19,
    "duration_ms": 35959
  },
  "last_tool_name": "Bash",
  "uuid": "a5876022-1eb4-41d4-af7b-998437eef7a0",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01PcepY2bhwMsrH73s8GXPqt`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -exec grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" {} \\; | sed 's/.*\\\\cite[tp]*{\\([^}]*\\)}.*/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "da706c92-9c91-4253-b46c-3e6ed774706e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014wauwj2XmM9hGsL73PCNv9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 66218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 627,
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

_source line 88 · 2026-05-28T17:16:26.841Z_

<details><summary>↩ Tool result · `toolu_01PcepY2bhwMsrH73s8GXPqt`</summary>

```text
abnar2020quantifying
alayrac2022flamingo
black2024pi0
black2025pi05
bolya2023tome
brohan2023rt2
chen2024fastv
chen2024internvl
cheng2026vlaiap
gao2025compressorvla
karl2024negative
kim2024openvla
kim2025openoft
lewis2020bart
li2024cogact
liang2022evit
lipman2023flow
liu2023libero
liu2025vlapruner
physicalintelligence2025pi05
rao2021dynamicvit
shi2016subpixel
shukor2025smolvla
su2024roformer
xu2025vlacache
yang2024qwen2
yang2025efficientvla
zeng2023transformers_tsf
zhai2023siglip
zhang2023h2o
zheng2025xvla
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "33462e99-d0ea-4a1f-b4c0-5efa9cfd946d"
}
```

</details>

---

### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Running cd /home/ubuntu/.agent-ml-research-be-idea-gen-05…",
  "usage": {
    "total_tokens": 67353,
    "tool_uses": 20,
    "duration_ms": 38239
  },
  "last_tool_name": "Bash",
  "uuid": "7c441ea4-ef8b-47f1-bf4e-2dc0f78d8fcc",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_01UW5RWUAREZBANgGMfSMcBi`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -print0 | xargs -0 grep -h \"\\\\\\\\cite[tp]*{[^}]*}\" | sed 's/.*\\\\cite[tp]*{\\([^}]*\\)}.*/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | grep -v '^$' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "b82e2de8-caac-4466-99a1-3fdf220f8a52",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Gr4bdS6n8swqifDrEZEiom",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 439,
      "cache_read_input_tokens": 66845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 439,
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

_source line 91 · 2026-05-28T17:16:29.112Z_

<details><summary>↩ Tool result · `toolu_01UW5RWUAREZBANgGMfSMcBi`</summary>

```text
abnar2020quantifying
alayrac2022flamingo
black2024pi0
black2025pi05
bolya2023tome
brohan2023rt2
chen2024fastv
chen2024internvl
cheng2026vlaiap
gao2025compressorvla
karl2024negative
kim2024openvla
kim2025openoft
lewis2020bart
li2024cogact
liang2022evit
lipman2023flow
liu2023libero
liu2025vlapruner
physicalintelligence2025pi05
rao2021dynamicvit
shi2016subpixel
shukor2025smolvla
su2024roformer
xu2025vlacache
yang2024qwen2
yang2025efficientvla
zeng2023transformers_tsf
zhai2023siglip
zhang2023h2o
zheng2025xvla
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "a7824fb6-3ed5-4f6a-b056-d1ae9b898036"
}
```

</details>

---

### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Running cd /home/ubuntu/.agent-ml-research-be-idea-gen-05…",
  "usage": {
    "total_tokens": 67807,
    "tool_uses": 21,
    "duration_ms": 40994
  },
  "last_tool_name": "Bash",
  "uuid": "b41351a2-6c70-411a-88db-f2d52449cd5a",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01ECmMsu4rfEw1TjTfAuZp2g`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && grep -rh \"oquab2023dinov2\\|yin2022avit\\|shang2024prumerge\\|jiang2026lightvla\\|ghosh2024octo\\|li2023blip2\\|liu2023llava\" . --include=\"*.tex\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "b2214ef7-4708-4f32-8e54-fc41dcc3c215",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WLWz4NPWQBo3hiWhbALwgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 67284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 442,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 94 · 2026-05-28T17:16:31.844Z_

<details><summary>↩ Tool result · `toolu_01ECmMsu4rfEw1TjTfAuZp2g`</summary>

```text
\textbf{Linear projection.} $\pi_0$~\cite{black2024pi0} (3.3B, 256 tokens) maps SigLIP~\cite{zhai2023siglip} patches through a single linear layer; $\pi_0.5$~\cite{black2025pi05} (4B, 768 tokens from three cameras) adds a learned $\times\!\sqrt{d}$ scaling; X-VLA~\cite{zheng2025xvla} (880M, 50 tokens) augments its linear projection with a 12-layer BART encoder~\cite{lewis2020bart} that introduces cross-token mixing. \textbf{MLP projector.} OpenVLA~\cite{kim2024openvla} (7B, 256 tokens) fuses DINOv2~\cite{oquab2023dinov2} and SigLIP through a three-layer MLP; OFT~\cite{kim2025openoft} shares this connector (entropy comparison only); CogACT~\cite{li2024cogact} retains 74.2\% SR under 78\% pruning per EfficientVLA~\cite{yang2025efficientvla} (literature corroboration, not our evaluation). \textbf{Spatial folding.} SmolVLA~\cite{shukor2025smolvla} (450M, 128 tokens) applies pixel-shuffle ($4{\times}4$ folding) so each token encodes 16 contiguous patches.
OpenVLA uses a dual encoder combining DINOv2~\cite{oquab2023dinov2} and SigLIP~\cite{zhai2023siglip}. The two encoders produce complementary representations (self-supervised spatial features and language-aligned features) that are concatenated per patch position.
Recent advances in foundation models have enabled a new class of robotic policies that map visual observations and language instructions directly to actions. RT-2~\cite{brohan2023rt2} first demonstrated that fine-tuning large vision-language models on robot demonstrations transfers web-scale semantic knowledge to robotic control; it tokenizes actions as text and trains jointly on internet and robot data. Octo~\cite{ghosh2024octo} introduced a modular transformer backbone trained on 800k trajectories from the Open X-Embodiment dataset, with flexible adaptation to new observation spaces and embodiments. OpenVLA~\cite{kim2024openvla} scaled this paradigm to 7B parameters with a fused SigLIP-DinoV2 visual encoder and an MLP projector that maps visual embeddings into the Llama~2 input space; it outperforms RT-2-X (55B) by 16.5\% in absolute success rate with 7$\times$ fewer parameters. SmolVLA~\cite{shukor2025smolvla} pursued the opposite end of the efficiency spectrum: a 450M-parameter model that combines aggressive pixel shuffle compression (64 visual tokens per frame) with a flow-matching action expert, and matches or exceeds larger VLAs on both simulation and real-world benchmarks. $\pi_0$~\cite{black2024pi0} and $\pi_{0.5}$~\cite{physicalintelligence2025pi05} built on PaLiGemma with a separate action expert connected via cross-attention and produce smooth 50Hz action trajectories through flow matching.
A critical but underexplored dimension across these models is the \emph{vision connector}: the module that bridges the visual encoder and the language/action backbone. OpenVLA and LLaVA~\cite{liu2023llava} use per-patch MLP projectors that preserve the spatial independence of each visual token. SmolVLA and InternVL~\cite{chen2024internvl} employ pixel shuffle (space-to-depth) connectors that fold spatial neighborhoods into channel dimensions before projection, creating tokens whose information content spans multiple spatial locations. BLIP-2~\cite{li2023blip2} introduced the Q-Former, a learned cross-attention bottleneck with fixed-size query vectors, while Flamingo~\cite{alayrac2022flamingo} proposed the Perceiver Resampler for a similar purpose. These architectural choices determine how visual information is distributed across tokens, yet no prior work has systematically studied how connector type affects the compressibility of the resulting token sequences in the context of action generation.
The vision connector governs how spatial information from the visual encoder is reorganized before entering the language model, and this reorganization has direct consequences for per-token information density. MLP projectors, as used in LLaVA~\cite{liu2023llava} and OpenVLA~\cite{kim2024openvla}, apply independent linear transformations to each patch embedding. Because each output token corresponds to exactly one spatial location, removing a token discards information from that location alone, and the remaining tokens retain their original semantics. This locality property makes MLP-projected tokens amenable to importance-based pruning: low-attention tokens can be dropped with bounded information loss.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "f787dd73-a4c7-42b1-b300-27441043f9e0"
}
```

</details>

---

### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "description": "Running cd /home/ubuntu/.agent-ml-research-be-idea-gen-05…",
  "usage": {
    "total_tokens": 69295,
    "tool_uses": 22,
    "duration_ms": 44651
  },
  "last_tool_name": "Bash",
  "uuid": "b0b01697-291a-4575-a567-0152db2dabd2",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Bash · `toolu_01YJ4XDDjAydfwN91Zf7SLwu`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && find . -name \"*.tex\" -type f -print0 | xargs -0 grep -oh \"\\\\\\\\cite[tp]*{[^}]*}\" | sed 's/\\\\cite[tp]*{\\([^}]*\\)}/\\1/g' | tr ',' '\\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | grep -v '^$' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "282eece0-2048-4c4f-b16e-b650af8cb003",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016sajWNYknnQ8w9mZxoT8TR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1487,
      "cache_read_input_tokens": 67726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1487,
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

_source line 97 · 2026-05-28T17:16:35.514Z_

<details><summary>↩ Tool result · `toolu_01YJ4XDDjAydfwN91Zf7SLwu`</summary>

```text
abnar2020quantifying
alayrac2022flamingo
black2024pi0
black2025pi05
bolya2023tome
brohan2023rt2
chen2024fastv
chen2024internvl
cheng2026vlaiap
gao2025compressorvla
ghosh2024octo
jiang2026lightvla
karl2024negative
kim2024openvla
kim2025openoft
lewis2020bart
li2023blip2
li2024cogact
liang2022evit
lipman2023flow
liu2023libero
liu2023llava
liu2025vlapruner
oquab2023dinov2
physicalintelligence2025pi05
rao2021dynamicvit
shang2024prumerge
shi2016subpixel
shukor2025smolvla
su2024roformer
xu2025vlacache
yang2024qwen2
yang2025efficientvla
yin2022avit
zeng2023transformers_tsf
zhai2023siglip
zhang2023h2o
zheng2025xvla
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "8db296ce-8fa0-49e6-b775-ce7e31afaf79"
}
```

</details>

---

### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a4e94d8fce91be5af",
  "tool_use_id": "toolu_015B9d2e5a4oUdbnmPjscqUY",
  "status": "completed",
  "output_file": "",
  "summary": "Find all cited bib keys in tex",
  "usage": {
    "total_tokens": 69792,
    "tool_uses": 22,
    "duration_ms": 48851
  },
  "uuid": "6cbddcf6-c2dc-4107-83bc-743e18eac09d",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009"
}
```

---

### Tool result

_source line 99 · 2026-05-28T17:16:39.637Z_

<details><summary>↩ Tool result · `toolu_015B9d2e5a4oUdbnmPjscqUY`</summary>

```text
Perfect! Now I have the complete deduplicated list. Let me format it nicely:

Based on my comprehensive search of all .tex files in `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/`, here is the complete deduplicated sorted list of all citation keys referenced:

1. abnar2020quantifying
2. alayrac2022flamingo
3. black2024pi0
4. black2025pi05
5. bolya2023tome
6. brohan2023rt2
7. chen2024fastv
8. chen2024internvl
9. cheng2026vlaiap
10. gao2025compressorvla
11. ghosh2024octo
12. jiang2026lightvla
13. karl2024negative
14. kim2024openvla
15. kim2025openoft
16. lewis2020bart
17. li2023blip2
18. li2024cogact
19. liang2022evit
20. lipman2023flow
21. liu2023libero
22. liu2023llava
23. liu2025vlapruner
24. oquab2023dinov2
25. physicalintelligence2025pi05
26. rao2021dynamicvit
27. shang2024prumerge
28. shi2016subpixel
29. shukor2025smolvla
30. su2024roformer
31. xu2025vlacache
32. yang2024qwen2
33. yang2025efficientvla
34. yin2022avit
35. zeng2023transformers_tsf
36. zhai2023siglip
37. zhang2023h2o
38. zheng2025xvla

**Total: 38 unique citation keys**

The most frequently cited works are:
- shukor2025smolvla (15 occurrences)
- bolya2023tome (15 occurrences)
- liu2023libero (13 occurrences)
- kim2024openvla (13 occurrences)
- zhai2023siglip (10 occurrences)
- rao2021dynamicvit (10 occurrences)
- black2024pi0 (10 occurrences)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "5d8e98fe-d1e0-4219-8b09-39c56147d052",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to find ALL citation keys referenced in .tex files under /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/. \n\nSearch for all occurrences of \\cite{...}, \\citep{...}, \\citet{...}, and similar citation commands across all .tex files. Extract just the citation keys (the text inside the braces). Note that a single \\cite command can contain multiple comma-separated keys like \\cite{key1,key2}.\n\nReport a deduplicated sorted list of all citation keys found.",
    "agentId": "a4e94d8fce91be5af",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have the complete deduplicated list. Let me format it nicely:\n\nBased on my comprehensive search of all .tex files in `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/`, here is the complete deduplicated sorted list of all citation keys referenced:\n\n1. abnar2020quantifying\n2. alayrac2022flamingo\n3. black2024pi0\n4. black2025pi05\n5. bolya2023tome\n6. brohan2023rt2\n7. chen2024fastv\n8. chen2024internvl\n9. cheng2026vlaiap\n10. gao2025compressorvla\n11. ghosh2024octo\n12. jiang2026lightvla\n13. karl2024negative\n14. kim2024openvla\n15. kim2025openoft\n16. lewis2020bart\n17. li2023blip2\n18. li2024cogact\n19. liang2022evit\n20. lipman2023flow\n21. liu2023libero\n22. liu2023llava\n23. liu2025vlapruner\n24. oquab2023dinov2\n25. physicalintelligence2025pi05\n26. rao2021dynamicvit\n27. shang2024prumerge\n28. shi2016subpixel\n29. shukor2025smolvla\n30. su2024roformer\n31. xu2025vlacache\n32. yang2024qwen2\n33. yang2025efficientvla\n34. yin2022avit\n35. zeng2023transformers_tsf\n36. zhai2023siglip\n37. zhang2023h2o\n38. zheng2025xvla\n\n**Total: 38 unique citation keys**\n\nThe most frequently cited works are:\n- shukor2025smolvla (15 occurrences)\n- bolya2023tome (15 occurrences)\n- liu2023libero (13 occurrences)\n- kim2024openvla (13 occurrences)\n- zhai2023siglip (10 occurrences)\n- rao2021dynamicvit (10 occurrences)\n- black2024pi0 (10 occurrences)"
      }
    ],
    "totalDurationMs": 48854,
    "totalTokens": 70279,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 69213,
      "output_tokens": 568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 496
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 568,
          "cache_read_input_tokens": 69213,
          "cache_creation_input_tokens": 496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 496,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 13,
      "searchCount": 2,
      "bashCount": 7,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 100_

<details><summary>Logged reasoning block</summary>

```text
Now I have the list of 38 cited keys. Let me extract all bib entry keys from the references.bib file to find orphans.

Bib entries in references.bib:
1. abnar2020quantifying
2. gao2025compressorvla
3. wang2025specprunevla
4. jiang2026lightvla
5. feng2026seewhatmatters
6. zhang2025sparsevlm
7. khaki2025sparsevila
8. jabbour2025dontrun
9. li2024roboflamingo


10. shukor2025smolvla
11. kim2024openvla
12. brohan2023rt2
13. black2024pi0
14. black2025pi05
15. ghosh2024octo
16. brohan2023rt1
17. chen2024fastv
18. xu2025vlacache
19. cheng2026vlaiap
20. rao2021dynamicvit
21. bolya2023tome
22. liang2022evit
23. liu2023libero
24. yang2025efficientvla
25. liu2025vlapruner
26. shang2024prumerge
27. alayrac2022flamingo
28. liu

2023llava
29. shi2016subpixel
30. chen2024internvl
31. li2023blip2
32. jaegle2021perceiver
33. oquab2023dinov2
34. zhai2023siglip
35. yang2024qwen2
36. lipman2023flow
37. li2024cogact
38. kim2025openoft
39. li2024tokenpacker
40. zheng2025xvla
41. wen2024tinyvla
42. lewis2020bart
43. ryoo2021tokenlearner
44. yin2022avit
45. meng2022adavit
46. chen2023sparsevit
47. ye2025fitprune
48. shi2024crossget
49. zhang2024fastervlm
50. liu

Continuing through the bibliography with entries 51-62, including updated versions of InternVL and DINOv2, along with papers on efficient language models, streaming attention mechanisms, and robotic learning policies, bringing the total to 62 references with 38 cited keys across the document.

I notice there's a discrepancy where `karl2024negative` and `physicalintelligence2025pi05` are referenced in the text but missing from the bibliography file.

Beyond that, there are quite a few entries sitting in the bib file that aren't actually cited anywhere in the document—things like `wang2025specprunevla`, `feng2026seewhatmatters`, `zhang2025sparsevlm`, and several others related to vision language models, robotics, and vision transformers. That's a separate cleanup issue to address.

Let me recount the orphan entries more systematically. I have 62 total entries in the bibliography, and when I check which ones are actually cited in the text, I'm finding that only 36 of them are referenced. So that leaves 26 orphan entries that need to be either removed or integrated into the document. Continuing through the bibliography, I've verified entries 26 through 36, and I'm noticing that two cited keys—karl2024negative and physicalintelligence2025pi05—don't appear in the bibliography file, which means I have 36 cited entries against 62 total bibliography entries, leaving 26 orphaned references.

Now I'm going through the bibliography systematically to identify which entries aren't cited anywhere. I'm checking each one against my citation list, and so far I've found wang2025specprunevla, feng2026seewhatmatters, and zhang2025sparsevlm as orphans, with more to verify as I continue down the list. Continuing through the citation status of the remaining papers in the list, marking which ones are referenced in the work and which are orphaned entries. I'm compiling the complete list of orphaned references—26 papers that weren't cited in the main text, ranging from vision-language model pruning techniques to robotic learning frameworks and foundational transformer architectures.

The count is 26 rather than the 36 mentioned in the task, so I'll report what I've actually found. Now I need to make three specific corrections: updating the author name in zheng2025xvla, completing the author list for chen2024fastv, and reformatting black2025pi05 to match the CoRL 2025 proceedings format with the PMLR volume 305 details and proper editor attribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "5b4639a1-c4a9-4daf-9961-6a0db6a91493",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tm8Ze6zRieWP8WweUDyZdg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 39060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 809
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

_source line 101_

Now I have all the information. Let me apply the three fixes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "53288bed-1aa5-4347-b3e5-4a2b5b4c384a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tm8Ze6zRieWP8WweUDyZdg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 39060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 809
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

_source line 102_

<details open><summary>🔧 Tool call — Edit · `toolu_0167bouwXKXEuTAvtk6HBh3H`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "old_string": "  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},",
  "new_string": "  author={Zheng, Jinliang and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "704387ef-e8c9-4ed2-8ed1-c714ec2303bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tm8Ze6zRieWP8WweUDyZdg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 39060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 809
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

_source line 103 · 2026-05-28T17:17:24.511Z_

<details><summary>↩ Tool result · `toolu_0167bouwXKXEuTAvtk6HBh3H`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "415e39c5-145a-4f77-9701-942637ecc292",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "oldString": "  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},",
    "newString": "  author={Zheng, Jinliang and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},",
    "originalFile": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% Attention Analysis\n% ============================================================\n\n@inproceedings{abnar2020quantifying,\n  title={Quantifying Attention Flow in Transformers},\n  author={Abnar, Samira and Zuidema, Willem},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={4190--4197},\n  year={2020},\n}\n\n% ============================================================\n% VLA Token Compression (concurrent work)\n% ============================================================\n\n@article{gao2025compressorvla,\n  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},\n  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},\n  journal={arXiv preprint arXiv:2511.18950},\n  year={2025},\n  eprint={2511.18950},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025specprunevla,\n  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},\n  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},\n  journal={arXiv preprint arXiv:2509.05614},\n  year={2025},\n  eprint={2509.05614},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{jiang2026lightvla,\n  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},\n  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},\n  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2026},\n  eprint={2509.12594},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{feng2026seewhatmatters,\n  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},\n  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},\n  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},\n  year={2026},\n  eprint={2605.11817},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zhang2025sparsevlm,\n  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},\n  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},\n  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},\n  year={2025},\n  eprint={2410.04417},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{khaki2025sparsevila,\n  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},\n  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025},\n  eprint={2510.17777},\n  archivePrefix={arXiv}\n}\n\n@article{jabbour2025dontrun,\n  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},\n  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},\n  journal={arXiv preprint arXiv:2510.08464},\n  year={2025},\n  eprint={2510.08464},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{li2024roboflamingo,\n  title={Vision-Language Foundation Models as Effective Robot Imitators},\n  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2311.01378},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt1,\n  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}\n\n\n@inproceedings{xu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cheng2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n\n% ============================================================\n% VLA Token Efficiency (new additions)\n% ============================================================\n\n@article{yang2025efficientvla,\n  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},\n  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},\n  journal={arXiv preprint arXiv:2506.10100},\n  year={2025}\n}\n\n@article{liu2025vlapruner,\n  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},\n  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},\n  journal={arXiv preprint arXiv:2511.16449},\n  year={2025}\n}\n\n@inproceedings{shang2024prumerge,\n  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},\n  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025}\n}\n\n% ============================================================\n% Vision Connectors\n% ============================================================\n\n@inproceedings{alayrac2022flamingo,\n  title={Flamingo: a Visual Language Model for Few-Shot Learning},\n  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2022}\n}\n\n@inproceedings{liu2023llava,\n  title={Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{shi2016subpixel,\n  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},\n  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2016}\n}\n\n@article{chen2024internvl,\n  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},\n  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2404.16821},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{li2023blip2,\n  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},\n  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@inproceedings{jaegle2021perceiver,\n  title={Perceiver: General Perception with Iterative Attention},\n  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2021}\n}\n\n@article{oquab2023dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ============================================================\n% Additional references (Round 3 reviewer request)\n% ============================================================\n\n% ============================================================\n% Additional VLA / VLM references\n% ============================================================\n\n@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2510.10274},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{lewis2020bart,\n  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},\n  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},\n  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2020}\n}\n\n% ============================================================\n% New additions for expanded Related Work\n% ============================================================\n\n@inproceedings{ryoo2021tokenlearner,\n  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},\n  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021},\n  eprint={2106.11297},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{yin2022avit,\n  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},\n  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2112.07658},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{meng2022adavit,\n  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},\n  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2111.15668},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chen2023sparsevit,\n  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},\n  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2023},\n  eprint={2303.17605},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ye2025fitprune,\n  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},\n  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  eprint={2409.10197},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{shi2024crossget,\n  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},\n  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2305.17455},\n  archivePrefix={arXiv}\n}\n\n@article{zhang2024fastervlm,\n  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},\n  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},\n  journal={arXiv preprint arXiv:2412.01818},\n  year={2024},\n  eprint={2412.01818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{liu2024llava15,\n  title={Improved Baselines with Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2024},\n  eprint={2310.03744},\n  archivePrefix={arXiv}\n}\n\n@article{chen2024internvl25,\n  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},\n  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2412.05271},\n  year={2024},\n  eprint={2412.05271},\n  archivePrefix={arXiv}\n}\n\n@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% Synced from literature_map.yaml (missing entries)\n% ============================================================\n\n% --- VLA Models ---\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023},\n  eprint={2307.15818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024},\n  eprint={2310.08864},\n  archivePrefix={arXiv}\n}\n\n% --- VLM/LLM Token Efficiency ---\n\n@inproceedings{zhang2023h2o,\n  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  eprint={2306.14048},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2309.17453},\n  archivePrefix={arXiv}\n}\n\n\n% --- Closed-Loop Evaluation ---\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022},\n  eprint={2112.03227},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023},\n  eprint={2303.04137},\n  archivePrefix={arXiv}\n}\n\n% --- Negative Results & Evaluation Pitfalls ---\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2023},\n  eprint={2205.13504},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2406.03980},\n  archivePrefix={arXiv}\n}\n\n% --- Vision Connectors & Token Compression ---\n\n@article{oquab2024dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024},\n  eprint={2304.07193},\n  archivePrefix={arXiv}\n}\n\n@article{su2024roformer,\n  title={{RoFormer}: Enhanced Transformer with Rotary Position Embedding},\n  author={Su, Jianlin and Ahmed, Murtadha and Lu, Yu and Pan, Shengfeng and Bo, Wen and Liu, Yunfeng},\n  journal={Neurocomputing},\n  volume={568},\n  pages={127063},\n  year={2024},\n  publisher={Elsevier}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 357,
        "oldLines": 7,
        "newStart": 357,
        "newLines": 7,
        "lines": [
          " ",
          " @inproceedings{zheng2025xvla,",
          "   title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},",
          "-  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},",
          "+  author={Zheng, Jinliang and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},",
          "   booktitle={International Conference on Learning Representations (ICLR)},",
          "   year={2026},",
          "   eprint={2510.10274},"
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

_source line 104_

<details open><summary>🔧 Tool call — Edit · `toolu_01F3cEdGtgXSKoVaitevypoy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "old_string": "@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}",
  "new_string": "@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  eprint={2403.06764},\n  archivePrefix={arXiv},\n  note={Oral presentation}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "4af3b6ff-7073-496a-8861-2e49c4309ce0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tm8Ze6zRieWP8WweUDyZdg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 39060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 809
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

_source line 105 · 2026-05-28T17:17:27.860Z_

<details><summary>↩ Tool result · `toolu_01F3cEdGtgXSKoVaitevypoy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "c86d5b1c-e0eb-47cc-a9f1-b5a5c233be9d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "oldString": "@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}",
    "newString": "@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  eprint={2403.06764},\n  archivePrefix={arXiv},\n  note={Oral presentation}\n}",
    "originalFile": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% Attention Analysis\n% ============================================================\n\n@inproceedings{abnar2020quantifying,\n  title={Quantifying Attention Flow in Transformers},\n  author={Abnar, Samira and Zuidema, Willem},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={4190--4197},\n  year={2020},\n}\n\n% ============================================================\n% VLA Token Compression (concurrent work)\n% ============================================================\n\n@article{gao2025compressorvla,\n  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},\n  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},\n  journal={arXiv preprint arXiv:2511.18950},\n  year={2025},\n  eprint={2511.18950},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025specprunevla,\n  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},\n  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},\n  journal={arXiv preprint arXiv:2509.05614},\n  year={2025},\n  eprint={2509.05614},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{jiang2026lightvla,\n  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},\n  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},\n  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2026},\n  eprint={2509.12594},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{feng2026seewhatmatters,\n  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},\n  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},\n  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},\n  year={2026},\n  eprint={2605.11817},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zhang2025sparsevlm,\n  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},\n  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},\n  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},\n  year={2025},\n  eprint={2410.04417},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{khaki2025sparsevila,\n  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},\n  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025},\n  eprint={2510.17777},\n  archivePrefix={arXiv}\n}\n\n@article{jabbour2025dontrun,\n  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},\n  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},\n  journal={arXiv preprint arXiv:2510.08464},\n  year={2025},\n  eprint={2510.08464},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{li2024roboflamingo,\n  title={Vision-Language Foundation Models as Effective Robot Imitators},\n  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2311.01378},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt1,\n  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}\n\n\n@inproceedings{xu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cheng2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n\n% ============================================================\n% VLA Token Efficiency (new additions)\n% ============================================================\n\n@article{yang2025efficientvla,\n  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},\n  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},\n  journal={arXiv preprint arXiv:2506.10100},\n  year={2025}\n}\n\n@article{liu2025vlapruner,\n  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},\n  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},\n  journal={arXiv preprint arXiv:2511.16449},\n  year={2025}\n}\n\n@inproceedings{shang2024prumerge,\n  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},\n  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025}\n}\n\n% ============================================================\n% Vision Connectors\n% ============================================================\n\n@inproceedings{alayrac2022flamingo,\n  title={Flamingo: a Visual Language Model for Few-Shot Learning},\n  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2022}\n}\n\n@inproceedings{liu2023llava,\n  title={Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{shi2016subpixel,\n  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},\n  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2016}\n}\n\n@article{chen2024internvl,\n  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},\n  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2404.16821},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{li2023blip2,\n  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},\n  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@inproceedings{jaegle2021perceiver,\n  title={Perceiver: General Perception with Iterative Attention},\n  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2021}\n}\n\n@article{oquab2023dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ============================================================\n% Additional references (Round 3 reviewer request)\n% ============================================================\n\n% ============================================================\n% Additional VLA / VLM references\n% ============================================================\n\n@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Jinliang and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2510.10274},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{lewis2020bart,\n  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},\n  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},\n  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2020}\n}\n\n% ============================================================\n% New additions for expanded Related Work\n% ============================================================\n\n@inproceedings{ryoo2021tokenlearner,\n  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},\n  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021},\n  eprint={2106.11297},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{yin2022avit,\n  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},\n  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2112.07658},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{meng2022adavit,\n  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},\n  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2111.15668},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chen2023sparsevit,\n  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},\n  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2023},\n  eprint={2303.17605},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ye2025fitprune,\n  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},\n  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  eprint={2409.10197},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{shi2024crossget,\n  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},\n  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2305.17455},\n  archivePrefix={arXiv}\n}\n\n@article{zhang2024fastervlm,\n  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},\n  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},\n  journal={arXiv preprint arXiv:2412.01818},\n  year={2024},\n  eprint={2412.01818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{liu2024llava15,\n  title={Improved Baselines with Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2024},\n  eprint={2310.03744},\n  archivePrefix={arXiv}\n}\n\n@article{chen2024internvl25,\n  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},\n  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2412.05271},\n  year={2024},\n  eprint={2412.05271},\n  archivePrefix={arXiv}\n}\n\n@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% Synced from literature_map.yaml (missing entries)\n% ============================================================\n\n% --- VLA Models ---\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023},\n  eprint={2307.15818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024},\n  eprint={2310.08864},\n  archivePrefix={arXiv}\n}\n\n% --- VLM/LLM Token Efficiency ---\n\n@inproceedings{zhang2023h2o,\n  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  eprint={2306.14048},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2309.17453},\n  archivePrefix={arXiv}\n}\n\n\n% --- Closed-Loop Evaluation ---\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022},\n  eprint={2112.03227},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023},\n  eprint={2303.04137},\n  archivePrefix={arXiv}\n}\n\n% --- Negative Results & Evaluation Pitfalls ---\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2023},\n  eprint={2205.13504},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2406.03980},\n  archivePrefix={arXiv}\n}\n\n% --- Vision Connectors & Token Compression ---\n\n@article{oquab2024dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024},\n  eprint={2304.07193},\n  archivePrefix={arXiv}\n}\n\n@article{su2024roformer,\n  title={{RoFormer}: Enhanced Transformer with Rotary Position Embedding},\n  author={Su, Jianlin and Ahmed, Murtadha and Lu, Yu and Pan, Shengfeng and Bo, Wen and Liu, Yunfeng},\n  journal={Neurocomputing},\n  volume={568},\n  pages={127063},\n  year={2024},\n  publisher={Elsevier}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 154,
        "oldLines": 9,
        "newStart": 154,
        "newLines": 11,
        "lines": [
          " ",
          " @inproceedings{chen2024fastv,",
          "   title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},",
          "-  author={Chen, Liang and others},",
          "+  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},",
          "   booktitle={European Conference on Computer Vision (ECCV)},",
          "   year={2024},",
          "+  eprint={2403.06764},",
          "+  archivePrefix={arXiv},",
          "   note={Oral presentation}",
          " }",
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

_source line 106_

<details open><summary>🔧 Tool call — Edit · `toolu_01FN2bbxoHvGDG6uUQxSbr2e`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "old_string": "@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}",
  "new_string": "@inproceedings{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},\n  series={Proceedings of Machine Learning Research},\n  volume={305},\n  pages={17--40},\n  year={2025},\n  publisher={PMLR},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "197fc6bb-415a-4f48-bb4b-764d32c48a65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tm8Ze6zRieWP8WweUDyZdg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 39060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 809
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

_source line 107 · 2026-05-28T17:17:31.543Z_

<details><summary>↩ Tool result · `toolu_01FN2bbxoHvGDG6uUQxSbr2e`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "7255037a-5426-4448-a8af-7e1ac0265377",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "oldString": "@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}",
    "newString": "@inproceedings{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},\n  series={Proceedings of Machine Learning Research},\n  volume={305},\n  pages={17--40},\n  year={2025},\n  publisher={PMLR},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}",
    "originalFile": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% Attention Analysis\n% ============================================================\n\n@inproceedings{abnar2020quantifying,\n  title={Quantifying Attention Flow in Transformers},\n  author={Abnar, Samira and Zuidema, Willem},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={4190--4197},\n  year={2020},\n}\n\n% ============================================================\n% VLA Token Compression (concurrent work)\n% ============================================================\n\n@article{gao2025compressorvla,\n  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},\n  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},\n  journal={arXiv preprint arXiv:2511.18950},\n  year={2025},\n  eprint={2511.18950},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025specprunevla,\n  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},\n  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},\n  journal={arXiv preprint arXiv:2509.05614},\n  year={2025},\n  eprint={2509.05614},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{jiang2026lightvla,\n  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},\n  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},\n  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2026},\n  eprint={2509.12594},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{feng2026seewhatmatters,\n  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},\n  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},\n  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},\n  year={2026},\n  eprint={2605.11817},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zhang2025sparsevlm,\n  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},\n  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},\n  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},\n  year={2025},\n  eprint={2410.04417},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{khaki2025sparsevila,\n  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},\n  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025},\n  eprint={2510.17777},\n  archivePrefix={arXiv}\n}\n\n@article{jabbour2025dontrun,\n  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},\n  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},\n  journal={arXiv preprint arXiv:2510.08464},\n  year={2025},\n  eprint={2510.08464},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{li2024roboflamingo,\n  title={Vision-Language Foundation Models as Effective Robot Imitators},\n  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2311.01378},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt1,\n  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  eprint={2403.06764},\n  archivePrefix={arXiv},\n  note={Oral presentation}\n}\n\n\n@inproceedings{xu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cheng2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n\n% ============================================================\n% VLA Token Efficiency (new additions)\n% ============================================================\n\n@article{yang2025efficientvla,\n  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},\n  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},\n  journal={arXiv preprint arXiv:2506.10100},\n  year={2025}\n}\n\n@article{liu2025vlapruner,\n  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},\n  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},\n  journal={arXiv preprint arXiv:2511.16449},\n  year={2025}\n}\n\n@inproceedings{shang2024prumerge,\n  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},\n  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025}\n}\n\n% ============================================================\n% Vision Connectors\n% ============================================================\n\n@inproceedings{alayrac2022flamingo,\n  title={Flamingo: a Visual Language Model for Few-Shot Learning},\n  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2022}\n}\n\n@inproceedings{liu2023llava,\n  title={Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{shi2016subpixel,\n  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},\n  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2016}\n}\n\n@article{chen2024internvl,\n  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},\n  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2404.16821},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{li2023blip2,\n  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},\n  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@inproceedings{jaegle2021perceiver,\n  title={Perceiver: General Perception with Iterative Attention},\n  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2021}\n}\n\n@article{oquab2023dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ============================================================\n% Additional references (Round 3 reviewer request)\n% ============================================================\n\n% ============================================================\n% Additional VLA / VLM references\n% ============================================================\n\n@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Jinliang and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2510.10274},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{lewis2020bart,\n  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},\n  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},\n  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2020}\n}\n\n% ============================================================\n% New additions for expanded Related Work\n% ============================================================\n\n@inproceedings{ryoo2021tokenlearner,\n  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},\n  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021},\n  eprint={2106.11297},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{yin2022avit,\n  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},\n  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2112.07658},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{meng2022adavit,\n  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},\n  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2111.15668},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chen2023sparsevit,\n  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},\n  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2023},\n  eprint={2303.17605},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ye2025fitprune,\n  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},\n  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  eprint={2409.10197},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{shi2024crossget,\n  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},\n  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2305.17455},\n  archivePrefix={arXiv}\n}\n\n@article{zhang2024fastervlm,\n  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},\n  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},\n  journal={arXiv preprint arXiv:2412.01818},\n  year={2024},\n  eprint={2412.01818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{liu2024llava15,\n  title={Improved Baselines with Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2024},\n  eprint={2310.03744},\n  archivePrefix={arXiv}\n}\n\n@article{chen2024internvl25,\n  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},\n  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2412.05271},\n  year={2024},\n  eprint={2412.05271},\n  archivePrefix={arXiv}\n}\n\n@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% Synced from literature_map.yaml (missing entries)\n% ============================================================\n\n% --- VLA Models ---\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023},\n  eprint={2307.15818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024},\n  eprint={2310.08864},\n  archivePrefix={arXiv}\n}\n\n% --- VLM/LLM Token Efficiency ---\n\n@inproceedings{zhang2023h2o,\n  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  eprint={2306.14048},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2309.17453},\n  archivePrefix={arXiv}\n}\n\n\n% --- Closed-Loop Evaluation ---\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022},\n  eprint={2112.03227},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023},\n  eprint={2303.04137},\n  archivePrefix={arXiv}\n}\n\n% --- Negative Results & Evaluation Pitfalls ---\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2023},\n  eprint={2205.13504},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2406.03980},\n  archivePrefix={arXiv}\n}\n\n% --- Vision Connectors & Token Compression ---\n\n@article{oquab2024dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024},\n  eprint={2304.07193},\n  archivePrefix={arXiv}\n}\n\n@article{su2024roformer,\n  title={{RoFormer}: Enhanced Transformer with Rotary Position Embedding},\n  author={Su, Jianlin and Ahmed, Murtadha and Lu, Yu and Pan, Shengfeng and Bo, Wen and Liu, Yunfeng},\n  journal={Neurocomputing},\n  volume={568},\n  pages={127063},\n  year={2024},\n  publisher={Elsevier}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 124,
        "oldLines": 11,
        "newStart": 124,
        "newLines": 15,
        "lines": [
          "   year={2024}",
          " }",
          " ",
          "-@article{black2025pi05,",
          "+@inproceedings{black2025pi05,",
          "   title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},",
          "   author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},",
          "-  journal={arXiv preprint arXiv:2504.16054},",
          "+  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},",
          "+  series={Proceedings of Machine Learning Research},",
          "+  volume={305},",
          "+  pages={17--40},",
          "   year={2025},",
          "+  publisher={PMLR},",
          "   eprint={2504.16054},",
          "   archivePrefix={arXiv}",
          " }"
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

_source line 108_

验证修改结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "08ec7e95-dfee-45d7-abb3-f2b9aef7638a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsAUH95SE1SvMzRM5vrDF7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4648,
      "cache_read_input_tokens": 39869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4648
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

_source line 109_

<details open><summary>🔧 Tool call — Read · `toolu_019PYMNcGhmi6gEPGwT2FeUU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "offset": 126,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "ba17f2fa-337b-4b30-9b66-b1dfdcbcfebd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsAUH95SE1SvMzRM5vrDF7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4648,
      "cache_read_input_tokens": 39869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4648
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

_source line 110 · 2026-05-28T17:17:35.287Z_

<details><summary>↩ Tool result · `toolu_019PYMNcGhmi6gEPGwT2FeUU`</summary>

```text
126	
127	@inproceedings{black2025pi05,
128	  title={$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},
129	  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},
130	  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},
131	  series={Proceedings of Machine Learning Research},
132	  volume={305},
133	  pages={17--40},
134	  year={2025},
135	  publisher={PMLR},
136	  eprint={2504.16054},
137	  archivePrefix={arXiv}
138	}
139	
140	@inproceedings{ghosh2024octo,
141	  title={Octo: An Open-Source Generalist Robot Policy},
142	  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},
143	  booktitle={Robotics: Science and Systems (RSS)},
144	  year={2024}
145	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "b6b3bdd8-461a-40c4-9d2a-9ba7763ee646",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
      "content": "\n@inproceedings{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},\n  series={Proceedings of Machine Learning Research},\n  volume={305},\n  pages={17--40},\n  year={2025},\n  publisher={PMLR},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}",
      "numLines": 20,
      "startLine": 126,
      "totalLines": 589
    }
  }
}
```

</details>

---

### Tool call

_source line 111_

<details open><summary>🔧 Tool call — Read · `toolu_019MC1szV5wt2dkpAJegr4VF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "offset": 154,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "b495a5a6-5237-48aa-8609-56609406f556",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsAUH95SE1SvMzRM5vrDF7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4648,
      "cache_read_input_tokens": 39869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4648
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

_source line 112 · 2026-05-28T17:17:36.225Z_

<details><summary>↩ Tool result · `toolu_019MC1szV5wt2dkpAJegr4VF`</summary>

```text
154	
155	% ============================================================
156	% VLM/LLM Token Efficiency
157	% ============================================================
158	
159	@inproceedings{chen2024fastv,
160	  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},
161	  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},
162	  booktitle={European Conference on Computer Vision (ECCV)},
163	  year={2024},
164	  eprint={2403.06764},
165	  archivePrefix={arXiv},
166	  note={Oral presentation}
167	}
168	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "419969cc-4358-46db-a5ab-9177930eeb33",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
      "content": "\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  eprint={2403.06764},\n  archivePrefix={arXiv},\n  note={Oral presentation}\n}\n",
      "numLines": 15,
      "startLine": 154,
      "totalLines": 589
    }
  }
}
```

</details>

---

### Tool call

_source line 113_

<details open><summary>🔧 Tool call — Read · `toolu_01FgRGBoUUGWRR1BE44E3kq4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "offset": 358,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "ec2dc91a-b4fc-4aa3-a75c-2d80c764474a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsAUH95SE1SvMzRM5vrDF7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4648,
      "cache_read_input_tokens": 39869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4648
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

_source line 114 · 2026-05-28T17:17:36.742Z_

<details><summary>↩ Tool result · `toolu_01FgRGBoUUGWRR1BE44E3kq4`</summary>

```text
358	  journal={arXiv preprint arXiv:2407.02392},
359	  year={2024},
360	  eprint={2407.02392},
361	  archivePrefix={arXiv}
362	}
363	
364	@inproceedings{zheng2025xvla,
365	  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},
366	  author={Zheng, Jinliang and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},
367	  booktitle={International Conference on Learning Representations (ICLR)},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "7afff065-5501-48ce-95a3-50878c2eed53",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
      "content": "  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Jinliang and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},\n  booktitle={International Conference on Learning Representations (ICLR)},",
      "numLines": 10,
      "startLine": 358,
      "totalLines": 589
    }
  }
}
```

</details>

---

### Assistant

_source line 115_

三项修改均已生效。

## 改动摘要

### Critical — 已修复
1. **`zheng2025xvla`** (line 366): 第一作者 `Zheng, Yifu` → `Zheng, Jinliang`

### Warning — 已修复
2. **`chen2024fastv`** (line 159-167): 作者列表从 `Chen, Liang and others` 补全为 7 位完整作者：Chen, Liang; Zhao, Haozhe; Liu, Tianyu; Bai, Shuai; Lin, Junyang; Zhou, Chang; Chang, Baobao。同时补充了 eprint 字段。

3. **`black2025pi05`** (line 127-138): 从 `@article`(arXiv preprint）转为 `@inproceedings`（CoRL 2025 正式发表），新增 `booktitle`, `series=PMLR`, `volume=305`, `pages=17--40`, `publisher=PMLR`。

### Orphan 条目（26 条，保留未删除）

以下 bib key 在 `references.bib` 中定义但未被任何 `.tex` 文件引用：

`wang2025specprunevla`, `feng2026seewhatmatters`, `zhang2025sparsevlm`, `khaki2025sparsevila`, `jabbour2025dontrun`, `li2024roboflamingo`, `brohan2023rt1`, `jaegle2021perceiver`, `li2024tokenpacker`, `wen2024tinyvla`, `ryoo2021tokenlearner`, `meng2022adavit`, `chen2023sparsevit`, `ye2025fitprune`, `shi2024crossget`, `zhang2024fastervlm`, `liu2024llava15`, `chen2024internvl25`, `gao2024miniinternvl`, `zitkovich2023rt2`, `openxembodiment2024`, `xiao2024streamingllm`, `mees2022calvin`, `chi2023diffusionpolicy`, `bouthillier2024negative`, `oquab2024dinov2`

另外，tex 中引用了 `karl2024negative` 和 `physicalintelligence2025pi05` 两个 key，但 bib 中不存在对应条目——这属于 missing citation，非本次任务范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "uuid": "eea6a05c-5dbb-4899-9162-9aff89bffdc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Do66urH2UKFLVsj4Mk63yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1212,
      "cache_read_input_tokens": 44517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1212
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

_source line 116_

三项修改均已生效。

## 改动摘要

### Critical — 已修复
1. **`zheng2025xvla`** (line 366): 第一作者 `Zheng, Yifu` → `Zheng, Jinliang`

### Warning — 已修复
2. **`chen2024fastv`** (line 159-167): 作者列表从 `Chen, Liang and others` 补全为 7 位完整作者：Chen, Liang; Zhao, Haozhe; Liu, Tianyu; Bai, Shuai; Lin, Junyang; Zhou, Chang; Chang, Baobao。同时补充了 eprint 字段。

3. **`black2025pi05`** (line 127-138): 从 `@article`(arXiv preprint）转为 `@inproceedings`（CoRL 2025 正式发表），新增 `booktitle`, `series=PMLR`, `volume=305`, `pages=17--40`, `publisher=PMLR`。

### Orphan 条目（26 条，保留未删除）

以下 bib key 在 `references.bib` 中定义但未被任何 `.tex` 文件引用：

`wang2025specprunevla`, `feng2026seewhatmatters`, `zhang2025sparsevlm`, `khaki2025sparsevila`, `jabbour2025dontrun`, `li2024roboflamingo`, `brohan2023rt1`, `jaegle2021perceiver`, `li2024tokenpacker`, `wen2024tinyvla`, `ryoo2021tokenlearner`, `meng2022adavit`, `chen2023sparsevit`, `ye2025fitprune`, `shi2024crossget`, `zhang2024fastervlm`, `liu2024llava15`, `chen2024internvl25`, `gao2024miniinternvl`, `zitkovich2023rt2`, `openxembodiment2024`, `xiao2024streamingllm`, `mees2022calvin`, `chi2023diffusionpolicy`, `bouthillier2024negative`, `oquab2024dinov2`

另外，tex 中引用了 `karl2024negative` 和 `physicalintelligence2025pi05` 两个 key，但 bib 中不存在对应条目——这属于 missing citation，非本次任务范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 170020,
  "duration_api_ms": 180988,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "5fcbbc8f-a94c-480e-bf9e-7ce4eca56009",
  "total_cost_usd": 0.82984865,
  "usage": {
    "input_tokens": 1582,
    "cache_creation_input_tokens": 33884,
    "cache_read_input_tokens": 351106,
    "output_tokens": 6960,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33884,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 638,
        "cache_read_input_tokens": 44517,
        "cache_creation_input_tokens": 1212,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1212
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 46668,
      "outputTokens": 4354,
      "cacheReadInputTokens": 650364,
      "cacheCreationInputTokens": 69709,
      "webSearchRequests": 4,
      "costUSD": 0.26061065,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1582,
      "outputTokens": 6960,
      "cacheReadInputTokens": 351106,
      "cacheCreationInputTokens": 33884,
      "webSearchRequests": 0,
      "costUSD": 0.5692380000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6ddb2f3c-0599-4d35-bdfd-bc4a0728e8a7"
}
```

</details>

---
