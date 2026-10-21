# fix bib critical 3items urgent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_fix_bib_critical_3items_urgent_20260528T172544.log`
- **Structured JSON:** [`35116d5a773b05ce52be.json`](../../sessions/35/35116d5a773b05ce52be.json)

## Before a recorded user message

23 recorded events

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
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
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
  "uuid": "24ddd788-7f14-41d6-889c-5100a908db59",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1780004400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0123847f-3b23-44bd-949d-729d9a919a46",
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to fix 3 issues in a bib file. Let me start by reading the bib file and doing web searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "bb8eeb6b-77dd-43ae-a422-fcfe83a141a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jwm3LQ7nP9j5iXmupKiPNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12693,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12693
      },
      "output_tokens": 36,
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

先读取 bib 文件并同时搜索三篇论文的准确信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "b4519658-a95e-4221-8fe8-cfb0487266e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jwm3LQ7nP9j5iXmupKiPNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12693,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12693
      },
      "output_tokens": 36,
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

<details open><summary>🔧 Tool call — Read · `toolu_01KvLUskMTzFDRyto3VJE9ix`</summary>

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
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "6fe81fe1-5d02-487f-9934-96272c916210",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jwm3LQ7nP9j5iXmupKiPNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12693,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12693
      },
      "output_tokens": 36,
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

_source line 7 · 2026-05-28T17:26:01.182Z_

<details><summary>↩ Tool result · `toolu_01KvLUskMTzFDRyto3VJE9ix`</summary>

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
146	
147	@inproceedings{brohan2023rt1,
148	  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},
149	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},
150	  booktitle={Robotics: Science and Systems (RSS)},
151	  year={2023}
152	}
153	
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
169	
170	@inproceedings{xu2025vlacache,
171	  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},
172	  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},
173	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
174	  year={2025}
175	}
176	
177	@article{cheng2026vlaiap,
178	  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},
179	  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},
180	  journal={arXiv preprint arXiv:2603.22991},
181	  year={2026}
182	}
183	
184	% ============================================================
185	% ViT Token Pruning/Merging
186	% ============================================================
187	
188	@inproceedings{rao2021dynamicvit,
189	  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},
190	  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},
191	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
192	  year={2021}
193	}
194	
195	@inproceedings{bolya2023tome,
196	  title={Token Merging: Your {ViT} But Faster},
197	  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},
198	  booktitle={International Conference on Learning Representations (ICLR)},
199	  year={2023}
200	}
201	
202	@inproceedings{liang2022evit,
203	  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},
204	  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},
205	  booktitle={International Conference on Learning Representations (ICLR)},
206	  year={2022}
207	}
208	
209	% ============================================================
210	% Closed-Loop Evaluation
211	% ============================================================
212	
213	@inproceedings{liu2023libero,
214	  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
215	  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
216	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
217	  year={2023}
218	}
219	
220	
221	% ============================================================
222	% Negative Results & Evaluation Pitfalls
223	% ============================================================
224	
225	
226	% ============================================================
227	% VLA Token Efficiency (new additions)
228	% ============================================================
229	
230	@article{yang2025efficientvla,
231	  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},
232	  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},
233	  journal={arXiv preprint arXiv:2506.10100},
234	  year={2025}
235	}
236	
237	@article{liu2025vlapruner,
238	  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},
239	  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},
240	  journal={arXiv preprint arXiv:2511.16449},
241	  year={2025}
242	}
243	
244	@inproceedings{shang2024prumerge,
245	  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},
246	  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},
247	  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},
248	  year={2025}
249	}
250	
251	% ============================================================
252	% Vision Connectors
253	% ============================================================
254	
255	@inproceedings{alayrac2022flamingo,
256	  title={Flamingo: a Visual Language Model for Few-Shot Learning},
257	  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},
258	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
259	  year={2022}
260	}
261	
262	@inproceedings{liu2023llava,
263	  title={Visual Instruction Tuning},
264	  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},
265	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
266	  year={2023}
267	}
268	
269	@inproceedings{shi2016subpixel,
270	  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},
271	  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},
272	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
273	  year={2016}
274	}
275	
276	@article{chen2024internvl,
277	  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},
278	  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},
279	  journal={arXiv preprint arXiv:2404.16821},
280	  year={2024}
281	}
282	
283	% ============================================================
284	% Background / Architecture
285	% ============================================================
286	
287	@inproceedings{li2023blip2,
288	  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},
289	  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},
290	  booktitle={International Conference on Machine Learning (ICML)},
291	  year={2023}
292	}
293	
294	@inproceedings{jaegle2021perceiver,
295	  title={Perceiver: General Perception with Iterative Attention},
296	  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},
297	  booktitle={International Conference on Machine Learning (ICML)},
298	  year={2021}
299	}
300	
301	@article{oquab2023dinov2,
302	  title={{DINOv2}: Learning Robust Visual Features without Supervision},
303	  author={Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Theo and others},
304	  journal={Transactions on Machine Learning Research},
305	  year={2024}
306	}
307	
308	@inproceedings{zhai2023siglip,
309	  title={Sigmoid Loss for Language Image Pre-Training},
310	  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},
311	  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},
312	  year={2023}
313	}
314	
315	@article{yang2024qwen2,
316	  title={Qwen2 Technical Report},
317	  author={Yang, An and others},
318	  journal={arXiv preprint arXiv:2407.10671},
319	  year={2024}
320	}
321	
322	@inproceedings{lipman2023flow,
323	  title={Flow Matching for Generative Modeling},
324	  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},
325	  booktitle={International Conference on Learning Representations (ICLR)},
326	  year={2023}
327	}
328	
329	% ============================================================
330	% Additional references (Round 3 reviewer request)
331	% ============================================================
332	
333	% ============================================================
334	% Additional VLA / VLM references
335	% ============================================================
336	
337	@article{li2024cogact,
338	  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},
339	  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},
340	  journal={arXiv preprint arXiv:2411.19650},
341	  year={2024},
342	  eprint={2411.19650},
343	  archivePrefix={arXiv}
344	}
345	
346	@article{kim2025openoft,
347	  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},
348	  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},
349	  journal={arXiv preprint arXiv:2502.19645},
350	  year={2025},
351	  eprint={2502.19645},
352	  archivePrefix={arXiv}
353	}
354	
355	@article{li2024tokenpacker,
356	  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},
357	  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},
358	  journal={arXiv preprint arXiv:2407.02392},
359	  year={2024},
360	  eprint={2407.02392},
361	  archivePrefix={arXiv}
362	}
363	
364	@inproceedings{zheng2025xvla,
365	  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},
366	  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and others},
367	  booktitle={International Conference on Learning Representations (ICLR)},
368	  year={2026},
369	  eprint={2510.10274},
370	  archivePrefix={arXiv}
371	}
372	
373	@article{wen2024tinyvla,
374	  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},
375	  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},
376	  journal={arXiv preprint arXiv:2409.12514},
377	  year={2024},
378	  eprint={2409.12514},
379	  archivePrefix={arXiv}
380	}
381	
382	@inproceedings{lewis2020bart,
383	  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},
384	  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},
385	  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},
386	  year={2020}
387	}
388	
389	% ============================================================
390	% New additions for expanded Related Work
391	% ============================================================
392	
393	@inproceedings{ryoo2021tokenlearner,
394	  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},
395	  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},
396	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
397	  year={2021},
398	  eprint={2106.11297},
399	  archivePrefix={arXiv}
400	}
401	
402	@inproceedings{yin2022avit,
403	  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},
404	  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},
405	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
406	  year={2022},
407	  eprint={2112.07658},
408	  archivePrefix={arXiv}
409	}
410	
411	@inproceedings{meng2022adavit,
412	  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},
413	  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},
414	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
415	  year={2022},
416	  eprint={2111.15668},
417	  archivePrefix={arXiv}
418	}
419	
420	@inproceedings{chen2023sparsevit,
421	  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},
422	  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},
423	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
424	  year={2023},
425	  eprint={2303.17605},
426	  archivePrefix={arXiv}
427	}
428	
429	@inproceedings{ye2025fitprune,
430	  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},
431	  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},
432	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
433	  year={2025},
434	  eprint={2409.10197},
435	  archivePrefix={arXiv}
436	}
437	
438	@inproceedings{shi2024crossget,
439	  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},
440	  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},
441	  booktitle={International Conference on Machine Learning (ICML)},
442	  year={2024},
443	  eprint={2305.17455},
444	  archivePrefix={arXiv}
445	}
446	
447	@article{zhang2024fastervlm,
448	  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},
449	  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},
450	  journal={arXiv preprint arXiv:2412.01818},
451	  year={2024},
452	  eprint={2412.01818},
453	  archivePrefix={arXiv}
454	}
455	
456	@inproceedings{liu2024llava15,
457	  title={Improved Baselines with Visual Instruction Tuning},
458	  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},
459	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
460	  year={2024},
461	  eprint={2310.03744},
462	  archivePrefix={arXiv}
463	}
464	
465	@article{chen2024internvl25,
466	  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},
467	  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},
468	  journal={arXiv preprint arXiv:2412.05271},
469	  year={2024},
470	  eprint={2412.05271},
471	  archivePrefix={arXiv}
472	}
473	
474	@article{gao2024miniinternvl,
475	  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\% Parameters and 90\% Performance},
476	  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},
477	  journal={arXiv preprint arXiv:2410.16261},
478	  year={2024},
479	  eprint={2410.16261},
480	  archivePrefix={arXiv}
481	}
482	
483	% ============================================================
484	% Synced from literature_map.yaml (missing entries)
485	% ============================================================
486	
487	% --- VLA Models ---
488	
489	@inproceedings{zitkovich2023rt2,
490	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
491	  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},
492	  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},
493	  year={2023},
494	  eprint={2307.15818},
495	  archivePrefix={arXiv}
496	}
497	
498	@inproceedings{openxembodiment2024,
499	  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},
500	  author={{Open X-Embodiment Collaboration}},
501	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
502	  year={2024},
503	  eprint={2310.08864},
504	  archivePrefix={arXiv}
505	}
506	
507	% --- VLM/LLM Token Efficiency ---
508	
509	@inproceedings{zhang2023h2o,
510	  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
511	  author={Zhang, Zhenyu and others},
512	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
513	  year={2023},
514	  eprint={2306.14048},
515	  archivePrefix={arXiv}
516	}
517	
518	@inproceedings{xiao2024streamingllm,
519	  title={Efficient Streaming Language Models with Attention Sinks},
520	  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},
521	  booktitle={International Conference on Learning Representations (ICLR)},
522	  year={2024},
523	  eprint={2309.17453},
524	  archivePrefix={arXiv}
525	}
526	
527	
528	% --- Closed-Loop Evaluation ---
529	
530	@article{mees2022calvin,
531	  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},
532	  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},
533	  journal={IEEE Robotics and Automation Letters},
534	  year={2022},
535	  eprint={2112.03227},
536	  archivePrefix={arXiv}
537	}
538	
539	@inproceedings{chi2023diffusionpolicy,
540	  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
541	  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
542	  booktitle={Robotics: Science and Systems (RSS)},
543	  year={2023},
544	  eprint={2303.04137},
545	  archivePrefix={arXiv}
546	}
547	
548	% --- Negative Results & Evaluation Pitfalls ---
549	
550	@inproceedings{zeng2023transformers_tsf,
551	  title={Are Transformers Effective for Time Series Forecasting?},
552	  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},
553	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
554	  year={2023},
555	  eprint={2205.13504},
556	  archivePrefix={arXiv}
557	}
558	
559	@inproceedings{bouthillier2024negative,
560	  title={Position: Embracing Negative Results in Machine Learning},
561	  author={Bouthillier, Xavier and others},
562	  booktitle={International Conference on Machine Learning (ICML)},
563	  year={2024},
564	  eprint={2406.03980},
565	  archivePrefix={arXiv}
566	}
567	
568	% --- Vision Connectors & Token Compression ---
569	
570	@article{oquab2024dinov2,
571	  title={{DINOv2}: Learning Robust Visual Features without Supervision},
572	  author={Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Theo and others},
573	  journal={Transactions on Machine Learning Research},
574	  year={2024},
575	  eprint={2304.07193},
576	  archivePrefix={arXiv}
577	}
578	
579	@article{su2024roformer,
580	  title={{RoFormer}: Enhanced Transformer with Rotary Position Embedding},
581	  author={Su, Jianlin and Ahmed, Murtadha and Lu, Yu and Pan, Shengfeng and Bo, Wen and Liu, Yunfeng},
582	  journal={Neurocomputing},
583	  volume={568},
584	  pages={127063},
585	  year={2024},
586	  publisher={Elsevier}
587	}
588	
589	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "7321a8fb-3587-46b3-a178-9247b7a68f11",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
      "content": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% Attention Analysis\n% ============================================================\n\n@inproceedings{abnar2020quantifying,\n  title={Quantifying Attention Flow in Transformers},\n  author={Abnar, Samira and Zuidema, Willem},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={4190--4197},\n  year={2020},\n}\n\n% ============================================================\n% VLA Token Compression (concurrent work)\n% ============================================================\n\n@article{gao2025compressorvla,\n  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},\n  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},\n  journal={arXiv preprint arXiv:2511.18950},\n  year={2025},\n  eprint={2511.18950},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025specprunevla,\n  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},\n  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},\n  journal={arXiv preprint arXiv:2509.05614},\n  year={2025},\n  eprint={2509.05614},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{jiang2026lightvla,\n  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},\n  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},\n  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2026},\n  eprint={2509.12594},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{feng2026seewhatmatters,\n  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},\n  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},\n  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},\n  year={2026},\n  eprint={2605.11817},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zhang2025sparsevlm,\n  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},\n  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},\n  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},\n  year={2025},\n  eprint={2410.04417},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{khaki2025sparsevila,\n  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},\n  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025},\n  eprint={2510.17777},\n  archivePrefix={arXiv}\n}\n\n@article{jabbour2025dontrun,\n  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},\n  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},\n  journal={arXiv preprint arXiv:2510.08464},\n  year={2025},\n  eprint={2510.08464},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{li2024roboflamingo,\n  title={Vision-Language Foundation Models as Effective Robot Imitators},\n  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2311.01378},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@inproceedings{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},\n  series={Proceedings of Machine Learning Research},\n  volume={305},\n  pages={17--40},\n  year={2025},\n  publisher={PMLR},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt1,\n  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  eprint={2403.06764},\n  archivePrefix={arXiv},\n  note={Oral presentation}\n}\n\n\n@inproceedings{xu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cheng2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n\n% ============================================================\n% VLA Token Efficiency (new additions)\n% ============================================================\n\n@article{yang2025efficientvla,\n  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},\n  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},\n  journal={arXiv preprint arXiv:2506.10100},\n  year={2025}\n}\n\n@article{liu2025vlapruner,\n  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},\n  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},\n  journal={arXiv preprint arXiv:2511.16449},\n  year={2025}\n}\n\n@inproceedings{shang2024prumerge,\n  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},\n  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025}\n}\n\n% ============================================================\n% Vision Connectors\n% ============================================================\n\n@inproceedings{alayrac2022flamingo,\n  title={Flamingo: a Visual Language Model for Few-Shot Learning},\n  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2022}\n}\n\n@inproceedings{liu2023llava,\n  title={Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{shi2016subpixel,\n  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},\n  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2016}\n}\n\n@article{chen2024internvl,\n  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},\n  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2404.16821},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{li2023blip2,\n  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},\n  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@inproceedings{jaegle2021perceiver,\n  title={Perceiver: General Perception with Iterative Attention},\n  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2021}\n}\n\n@article{oquab2023dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ============================================================\n% Additional references (Round 3 reviewer request)\n% ============================================================\n\n% ============================================================\n% Additional VLA / VLM references\n% ============================================================\n\n@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and others},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2510.10274},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{lewis2020bart,\n  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},\n  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},\n  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2020}\n}\n\n% ============================================================\n% New additions for expanded Related Work\n% ============================================================\n\n@inproceedings{ryoo2021tokenlearner,\n  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},\n  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021},\n  eprint={2106.11297},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{yin2022avit,\n  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},\n  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2112.07658},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{meng2022adavit,\n  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},\n  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2111.15668},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chen2023sparsevit,\n  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},\n  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2023},\n  eprint={2303.17605},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ye2025fitprune,\n  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},\n  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  eprint={2409.10197},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{shi2024crossget,\n  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},\n  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2305.17455},\n  archivePrefix={arXiv}\n}\n\n@article{zhang2024fastervlm,\n  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},\n  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},\n  journal={arXiv preprint arXiv:2412.01818},\n  year={2024},\n  eprint={2412.01818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{liu2024llava15,\n  title={Improved Baselines with Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2024},\n  eprint={2310.03744},\n  archivePrefix={arXiv}\n}\n\n@article{chen2024internvl25,\n  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},\n  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2412.05271},\n  year={2024},\n  eprint={2412.05271},\n  archivePrefix={arXiv}\n}\n\n@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% Synced from literature_map.yaml (missing entries)\n% ============================================================\n\n% --- VLA Models ---\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023},\n  eprint={2307.15818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024},\n  eprint={2310.08864},\n  archivePrefix={arXiv}\n}\n\n% --- VLM/LLM Token Efficiency ---\n\n@inproceedings{zhang2023h2o,\n  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  eprint={2306.14048},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2309.17453},\n  archivePrefix={arXiv}\n}\n\n\n% --- Closed-Loop Evaluation ---\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022},\n  eprint={2112.03227},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023},\n  eprint={2303.04137},\n  archivePrefix={arXiv}\n}\n\n% --- Negative Results & Evaluation Pitfalls ---\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2023},\n  eprint={2205.13504},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2406.03980},\n  archivePrefix={arXiv}\n}\n\n% --- Vision Connectors & Token Compression ---\n\n@article{oquab2024dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024},\n  eprint={2304.07193},\n  archivePrefix={arXiv}\n}\n\n@article{su2024roformer,\n  title={{RoFormer}: Enhanced Transformer with Rotary Position Embedding},\n  author={Su, Jianlin and Ahmed, Murtadha and Lu, Yu and Pan, Shengfeng and Bo, Wen and Liu, Yunfeng},\n  journal={Neurocomputing},\n  volume={568},\n  pages={127063},\n  year={2024},\n  publisher={Elsevier}\n}\n\n",
      "numLines": 589,
      "startLine": 1,
      "totalLines": 589
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016cdh8hcKUFqFFtyhPuHRTX`</summary>

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
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "a57c18d5-9e10-4780-abdb-f7f61f16d687",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jwm3LQ7nP9j5iXmupKiPNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12693,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12693
      },
      "output_tokens": 36,
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

_source line 9 · 2026-05-28T17:26:01.567Z_

<details><summary>↩ Tool result · `toolu_016cdh8hcKUFqFFtyhPuHRTX`</summary>

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
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "370d1623-1c7a-4333-aad9-5305a089d25a",
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
Good, I've read the bib file and have WebSearch available. Let me now analyze what needs to be fixed:

1. `zheng2025xvla` (line 364-371) - First author is "Zheng, Jinliang" which actually looks correct already. Wait, the user says current first author is "Zheng, Yifu" but looking at the file, it says "Zheng, Jinliang". Let me re-read... The entry at line 366 says `author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and others}`. 

The first author appears to already be "Zheng, Jinliang", which contradicts what the user mentioned, so either the file was already corrected or the user has outdated information. I should still verify the complete author list through web searches to be thorough.

2. `chen2024fastv` (line 159-167) - Currently has full authors: "Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao". That's 7 authors, not "Chen, Liang and others", so this one also needs checking.

3. `black2025pi05` (line 127-138) - The user says it's an arXiv preprint format, but it's already formatted as `@inproceedings` with CoRL venue, PMLR v305, and pages, so this also appears to be already done.

Let me look more carefully at the actual content. For item 1, line 366 shows the first author as Jinliang, not Yifu as the user indicated. For item 2, line 162 shows the full author list starting with Chen, Liang. It seems like either the file has been recently updated or the user's information is outdated.

I should still run web searches to verify the accuracy of what's currently in the file and make any necessary corrections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "4a48780a-860b-44d9-9609-d2a3b1ec225e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTxhQtYkaq6k96v6WD2Tza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10235,
      "cache_read_input_tokens": 24538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10235
      },
      "output_tokens": 20,
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

读完 bib 文件，发现当前状态与用户描述有出入。让我搜索验证每项的准确性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "79b422bf-388a-408b-b755-f9d97b9021ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTxhQtYkaq6k96v6WD2Tza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10235,
      "cache_read_input_tokens": 24538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10235
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EYSgNKvkDhHZNen5zrWgS8`</summary>

```json
{
  "query": "arXiv 2510.10274 X-VLA authors complete list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "89a9b116-5487-41dc-ad50-ba730b28195d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTxhQtYkaq6k96v6WD2Tza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10235,
      "cache_read_input_tokens": 24538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10235
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0125qJiNGqKvUPwwSPudHdvc`</summary>

```json
{
  "query": "FastV ECCV 2024 \"An Image is Worth 1/2 Tokens\" authors Chen Liang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "2f1ccc28-a1d7-4f70-a3e3-2938c9eefbec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTxhQtYkaq6k96v6WD2Tza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10235,
      "cache_read_input_tokens": 24538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10235
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DMQAY8EY2WDBeuCpxSBDmU`</summary>

```json
{
  "query": "pi0.5 CoRL 2025 PMLR v305 \"Conference on Robot Learning\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "180b767c-e6bf-4c19-ab27-86f0f75a3609",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTxhQtYkaq6k96v6WD2Tza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10235,
      "cache_read_input_tokens": 24538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10235
      },
      "output_tokens": 20,
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

_source line 15 · 2026-05-28T17:26:34.974Z_

<details><summary>↩ Tool result · `toolu_01EYSgNKvkDhHZNen5zrWgS8`</summary>

```text
Web search results for query: "arXiv 2510.10274 X-VLA authors complete list"

Links: [{"title":"[2510.10274] X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/abs/2510.10274"},{"title":"(PDF) X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://www.researchgate.net/publication/396462440_X-VLA_Soft-Prompted_Transformer_as_Scalable_Cross-Embodiment_Vision-Language-Action_Model"},{"title":"2025-10-14 X-VLA: Soft-Prompted Transformer as Scalable","url":"https://arxiv.org/pdf/2510.10274"},{"title":"2toINF/X-VLA-SoftFold · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-SoftFold"},{"title":"2toINF/X-VLA-Pt · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-Pt"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.10274"},{"title":"RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.06710v2"},{"title":"X-VLA","url":"https://thu-air-dream.github.io/X-VLA/"}]

Based on the search results, the complete list of authors for arXiv paper 2510.10274 (X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model) is: Jinliang Zheng, Jianxiong Li, Zhihao Wang, Dongxiu Liu, Xirui Kang, Yuchun Feng, Yinan Zheng, Jiayin Zou, Yilun Chen, Jia Zeng, Ya-Qin Zhang, Jiangmiao Pang, Jingjing Liu, Tai Wang, and Xianyuan Zhan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "c115712f-3dac-4c4f-b53d-5df7ec093137",
  "tool_use_result": {
    "query": "arXiv 2510.10274 X-VLA authors complete list",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NuozYUmQEqADsRgLqENHKs",
        "content": [
          {
            "title": "[2510.10274] X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model",
            "url": "https://arxiv.org/abs/2510.10274"
          },
          {
            "title": "(PDF) X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model",
            "url": "https://www.researchgate.net/publication/396462440_X-VLA_Soft-Prompted_Transformer_as_Scalable_Cross-Embodiment_Vision-Language-Action_Model"
          },
          {
            "title": "2025-10-14 X-VLA: Soft-Prompted Transformer as Scalable",
            "url": "https://arxiv.org/pdf/2510.10274"
          },
          {
            "title": "2toINF/X-VLA-SoftFold · Hugging Face",
            "url": "https://huggingface.co/2toINF/X-VLA-SoftFold"
          },
          {
            "title": "2toINF/X-VLA-Pt · Hugging Face",
            "url": "https://huggingface.co/2toINF/X-VLA-Pt"
          },
          {
            "title": "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2510.10274"
          },
          {
            "title": "RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.06710v2"
          },
          {
            "title": "X-VLA",
            "url": "https://thu-air-dream.github.io/X-VLA/"
          }
        ]
      },
      "Based on the search results, the complete list of authors for arXiv paper 2510.10274 (X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model) is: Jinliang Zheng, Jianxiong Li, Zhihao Wang, Dongxiu Liu, Xirui Kang, Yuchun Feng, Yinan Zheng, Jiayin Zou, Yilun Chen, Jia Zeng, Ya-Qin Zhang, Jiangmiao Pang, Jingjing Liu, Tai Wang, and Xianyuan Zhan."
    ],
    "durationSeconds": 4.953150306999996
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T17:26:35.858Z_

<details><summary>↩ Tool result · `toolu_0125qJiNGqKvUPwwSPudHdvc`</summary>

```text
Web search results for query: "FastV ECCV 2024 "An Image is Worth 1/2 Tokens" authors Chen Liang"

Links: [{"title":"GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/pkunlp-icler/FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Computer Vision – ECCV 2024","url":"https://dl.acm.org/doi/10.1007/978-3-031-73004-7_2"},{"title":"GitHub - MachineLearningSystem/24ECCV-FastV: [ECCV 2024] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/MachineLearningSystem/24ECCV-FastV"},{"title":"GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/chenllliang/FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-73004-7_2"},{"title":"[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference","url":"https://arxiv.org/html/2403.06764v3"},{"title":"ECCV Poster An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://eccv.ecva.net/virtual/2024/poster/2009"}]

I found comprehensive information about this paper. Here are the search results:

FastV ("An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models") was authored by Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, and others, and the paper was selected as an Oral Presentation at ECCV 2024.

FastV is a versatile plug-and-play method designed to optimize computational efficiency by learning adaptive attention patterns in early layers and pruning visual tokens in subsequent ones. The method demonstrates the ability to dramatically reduce computational costs (e.g., a 45% reduction in FLOPs for LLaVA-1.5-13B) without sacrificing performance in a wide range of image and video understanding tasks.

You can find the paper on arXiv (2403.06764), GitHub repositories, and the official ECCV 2024 proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "8f395860-b753-42c4-98b9-aefb6ff894bf",
  "tool_use_result": {
    "query": "FastV ECCV 2024 \"An Image is Worth 1/2 Tokens\" authors Chen Liang",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C2bq53QdGRAjjMU7uCHnwF",
        "content": [
          {
            "title": "GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub",
            "url": "https://github.com/pkunlp-icler/FastV"
          },
          {
            "title": "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Computer Vision – ECCV 2024",
            "url": "https://dl.acm.org/doi/10.1007/978-3-031-73004-7_2"
          },
          {
            "title": "GitHub - MachineLearningSystem/24ECCV-FastV: [ECCV 2024] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub",
            "url": "https://github.com/MachineLearningSystem/24ECCV-FastV"
          },
          {
            "title": "GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub",
            "url": "https://github.com/chenllliang/FastV"
          },
          {
            "title": "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-73004-7_2"
          },
          {
            "title": "[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"
          },
          {
            "title": "[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models",
            "url": "https://arxiv.org/abs/2403.06764"
          },
          {
            "title": "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference",
            "url": "https://arxiv.org/html/2403.06764v3"
          },
          {
            "title": "ECCV Poster An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models",
            "url": "https://eccv.ecva.net/virtual/2024/poster/2009"
          }
        ]
      },
      "I found comprehensive information about this paper. Here are the search results:\n\nFastV (\"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\") was authored by Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, and others, and the paper was selected as an Oral Presentation at ECCV 2024.\n\nFastV is a versatile plug-and-play method designed to optimize computational efficiency by learning adaptive attention patterns in early layers and pruning visual tokens in subsequent ones. The method demonstrates the ability to dramatically reduce computational costs (e.g., a 45% reduction in FLOPs for LLaVA-1.5-13B) without sacrificing performance in a wide range of image and video understanding tasks.\n\nYou can find the paper on arXiv (2403.06764), GitHub repositories, and the official ECCV 2024 proceedings."
    ],
    "durationSeconds": 4.888129618999999
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T17:26:38.876Z_

<details><summary>↩ Tool result · `toolu_01DMQAY8EY2WDBeuCpxSBDmU`</summary>

```text
Web search results for query: "pi0.5 CoRL 2025 PMLR v305 "Conference on Robot Learning""

Links: [{"title":"CoRL 2025","url":"https://2025.corl.org/"},{"title":"CORL 2025 - YouTube","url":"https://www.youtube.com/watch?v=Use5M-nfFlI"},{"title":"Learning a Unified Policy for Position and Force Control in Legged Loco-Manipulation","url":"https://proceedings.mlr.press/v305/zhi25a.html"},{"title":"CoRL 2025 Survey - Speaker Deck","url":"https://speakerdeck.com/harukiabe/corl-2025-survey"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 9th Conference on Robot Learning Held in Seoul, Korea on 27-30 September 2025 Published as Volume 305 by the Proceedings of Machine Learning Research on 07 October 2025. Volume Edited by: Joseph Lim Shuran Song Hae-Won Park Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v305/"},{"title":"Publications · Robot Learning Lab","url":"https://robotlearning.cs.washington.edu/publications/"},{"title":"Conference on Robot Learning (CoRL)","url":"https://dblp.org/db/conf/corl/index.html"},{"title":"Two papers accepted at Conference on Robot Learning (CoRL) 2025 | SLMC | School of Informatics","url":"https://informatics.ed.ac.uk/slmc/two-papers-accepted-at-conference-on-robot-learning-corl-2025"}]

I found relevant information about your search. Here are the results:

The Proceedings of The 9th Conference on Robot Learning was held in Seoul, Korea on 27-30 September 2025 and published as Volume 305 by the Proceedings of Machine Learning Research on 07 October 2025.

Regarding pi0.5 specifically, π0.5 is mentioned as an example of a robot foundation model that "learns diverse skills with a single policy." It was developed by Black et al.

The Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning.

The search results show that PMLR Volume 305 contains numerous papers from CoRL 2025, and pi0.5 is referenced as a notable contribution in the context of robot foundation models presented at the conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "bedf3d34-63ba-432d-be50-bf21f74e5bcd",
  "tool_use_result": {
    "query": "pi0.5 CoRL 2025 PMLR v305 \"Conference on Robot Learning\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_019w8b4EvhzWTGfHQQorFV4E",
        "content": [
          {
            "title": "CoRL 2025",
            "url": "https://2025.corl.org/"
          },
          {
            "title": "CORL 2025 - YouTube",
            "url": "https://www.youtube.com/watch?v=Use5M-nfFlI"
          },
          {
            "title": "Learning a Unified Policy for Position and Force Control in Legged Loco-Manipulation",
            "url": "https://proceedings.mlr.press/v305/zhi25a.html"
          },
          {
            "title": "CoRL 2025 Survey - Speaker Deck",
            "url": "https://speakerdeck.com/harukiabe/corl-2025-survey"
          },
          {
            "title": "Proceedings of Machine Learning Research | Proceedings of The 9th Conference on Robot Learning Held in Seoul, Korea on 27-30 September 2025 Published as Volume 305 by the Proceedings of Machine Learning Research on 07 October 2025. Volume Edited by: Joseph Lim Shuran Song Hae-Won Park Series Editors: Neil D. Lawrence",
            "url": "https://proceedings.mlr.press/v305/"
          },
          {
            "title": "Publications · Robot Learning Lab",
            "url": "https://robotlearning.cs.washington.edu/publications/"
          },
          {
            "title": "Conference on Robot Learning (CoRL)",
            "url": "https://dblp.org/db/conf/corl/index.html"
          },
          {
            "title": "Two papers accepted at Conference on Robot Learning (CoRL) 2025 | SLMC | School of Informatics",
            "url": "https://informatics.ed.ac.uk/slmc/two-papers-accepted-at-conference-on-robot-learning-corl-2025"
          }
        ]
      },
      "I found relevant information about your search. Here are the results:\n\nThe Proceedings of The 9th Conference on Robot Learning was held in Seoul, Korea on 27-30 September 2025 and published as Volume 305 by the Proceedings of Machine Learning Research on 07 October 2025.\n\nRegarding pi0.5 specifically, π0.5 is mentioned as an example of a robot foundation model that \"learns diverse skills with a single policy.\" It was developed by Black et al.\n\nThe Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning.\n\nThe search results show that PMLR Volume 305 contains numerous papers from CoRL 2025, and pi0.5 is referenced as a notable contribution in the context of robot foundation models presented at the conference."
    ],
    "durationSeconds": 7.450192979
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

````text
Now let me analyze the current state vs what needs to be fixed:

**Item 1: `zheng2025xvla`**
Current (line 364-371):
```bibtex
@inproceedings{zheng2025xvla,
  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},
  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and others},


```

The first author is already "Zheng, Jinliang" (correct). But the author list uses "and others" - need to expand with the complete list.

Complete author list from search: Jinliang Zheng, Jianxiong Li, Zhihao Wang, Dongxiu Liu, Xirui Kang, Yuchun Feng, Yinan Zheng, Jiayin Zou, Y

Completing the bibtex entry...

I need to fill in the full author list for the first entry - there are 15 authors total, so I'll write them all out in the BibTeX format rather than using "and others."

Now looking at the second entry, which appears to be a conference paper on vision-language model optimization. The title and author list are visible but the booktitle field is cut off mid-entry. I'm verifying the author list against the ECCV proceedings and arXiv page to confirm all seven authors are correctly included in the bibliography entry.

Now moving to the next item - checking the bibtex entry for the vision-language-action model paper, which currently lists Kevin Black and others but appears to be cut off mid-entry. Now I'm replacing the "and others" placeholder with the full author list from the paper - that's fifteen authors total, ending with Xianyuan Zhan.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "2de1ac79-f253-42fd-b463-af4d75d82ad9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PeSw1tHaKptHN24MUSwoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 34773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3465
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

当前 bib 文件状态与用户描述有出入——2/3 项已修复。逐项检查：

**Item 2 (`chen2024fastv`)**: 已有完整 7 位作者列表，无需修改。
**Item 3 (`black2025pi05`)**: 已是 `@inproceedings`，含 CoRL 2025 / PMLR v305 信息，无需修改。
**Item 1 (`zheng2025xvla`)**: 第一作者已正确为 Jinliang，但作者列表仍用 `and others`，需展开为完整 15 位作者。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "23078a55-12f1-42d6-be12-aef8a66f378e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PeSw1tHaKptHN24MUSwoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 34773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3465
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Jhf9pzevqiFWMQgbDfDyNf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "old_string": "  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and others},",
  "new_string": "  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and Kang, Xirui and Feng, Yuchun and Zheng, Yinan and Zou, Jiayin and Chen, Yilun and Zeng, Jia and Zhang, Ya-Qin and Pang, Jiangmiao and Liu, Jingjing and Wang, Tai and Zhan, Xianyuan},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "177cb208-5870-41f7-af50-9c7d7995b7db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PeSw1tHaKptHN24MUSwoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 34773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3465
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

_source line 21 · 2026-05-28T17:27:21.714Z_

<details><summary>↩ Tool result · `toolu_01Jhf9pzevqiFWMQgbDfDyNf`</summary>

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
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "05b9c2f9-19e3-4093-a5ca-8519f671544f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "oldString": "  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and others},",
    "newString": "  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and Kang, Xirui and Feng, Yuchun and Zheng, Yinan and Zou, Jiayin and Chen, Yilun and Zeng, Jia and Zhang, Ya-Qin and Pang, Jiangmiao and Liu, Jingjing and Wang, Tai and Zhan, Xianyuan},",
    "originalFile": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% Attention Analysis\n% ============================================================\n\n@inproceedings{abnar2020quantifying,\n  title={Quantifying Attention Flow in Transformers},\n  author={Abnar, Samira and Zuidema, Willem},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={4190--4197},\n  year={2020},\n}\n\n% ============================================================\n% VLA Token Compression (concurrent work)\n% ============================================================\n\n@article{gao2025compressorvla,\n  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},\n  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},\n  journal={arXiv preprint arXiv:2511.18950},\n  year={2025},\n  eprint={2511.18950},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025specprunevla,\n  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},\n  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},\n  journal={arXiv preprint arXiv:2509.05614},\n  year={2025},\n  eprint={2509.05614},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{jiang2026lightvla,\n  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},\n  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},\n  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2026},\n  eprint={2509.12594},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{feng2026seewhatmatters,\n  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},\n  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},\n  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},\n  year={2026},\n  eprint={2605.11817},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zhang2025sparsevlm,\n  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},\n  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},\n  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},\n  year={2025},\n  eprint={2410.04417},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{khaki2025sparsevila,\n  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},\n  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025},\n  eprint={2510.17777},\n  archivePrefix={arXiv}\n}\n\n@article{jabbour2025dontrun,\n  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},\n  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},\n  journal={arXiv preprint arXiv:2510.08464},\n  year={2025},\n  eprint={2510.08464},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{li2024roboflamingo,\n  title={Vision-Language Foundation Models as Effective Robot Imitators},\n  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2311.01378},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@inproceedings{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},\n  series={Proceedings of Machine Learning Research},\n  volume={305},\n  pages={17--40},\n  year={2025},\n  publisher={PMLR},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt1,\n  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  eprint={2403.06764},\n  archivePrefix={arXiv},\n  note={Oral presentation}\n}\n\n\n@inproceedings{xu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cheng2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n\n% ============================================================\n% VLA Token Efficiency (new additions)\n% ============================================================\n\n@article{yang2025efficientvla,\n  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},\n  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},\n  journal={arXiv preprint arXiv:2506.10100},\n  year={2025}\n}\n\n@article{liu2025vlapruner,\n  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},\n  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},\n  journal={arXiv preprint arXiv:2511.16449},\n  year={2025}\n}\n\n@inproceedings{shang2024prumerge,\n  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},\n  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025}\n}\n\n% ============================================================\n% Vision Connectors\n% ============================================================\n\n@inproceedings{alayrac2022flamingo,\n  title={Flamingo: a Visual Language Model for Few-Shot Learning},\n  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2022}\n}\n\n@inproceedings{liu2023llava,\n  title={Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{shi2016subpixel,\n  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},\n  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2016}\n}\n\n@article{chen2024internvl,\n  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},\n  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2404.16821},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{li2023blip2,\n  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},\n  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@inproceedings{jaegle2021perceiver,\n  title={Perceiver: General Perception with Iterative Attention},\n  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2021}\n}\n\n@article{oquab2023dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ============================================================\n% Additional references (Round 3 reviewer request)\n% ============================================================\n\n% ============================================================\n% Additional VLA / VLM references\n% ============================================================\n\n@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and others},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2510.10274},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{lewis2020bart,\n  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},\n  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},\n  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2020}\n}\n\n% ============================================================\n% New additions for expanded Related Work\n% ============================================================\n\n@inproceedings{ryoo2021tokenlearner,\n  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},\n  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021},\n  eprint={2106.11297},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{yin2022avit,\n  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},\n  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2112.07658},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{meng2022adavit,\n  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},\n  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2111.15668},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chen2023sparsevit,\n  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},\n  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2023},\n  eprint={2303.17605},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ye2025fitprune,\n  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},\n  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  eprint={2409.10197},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{shi2024crossget,\n  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},\n  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2305.17455},\n  archivePrefix={arXiv}\n}\n\n@article{zhang2024fastervlm,\n  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},\n  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},\n  journal={arXiv preprint arXiv:2412.01818},\n  year={2024},\n  eprint={2412.01818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{liu2024llava15,\n  title={Improved Baselines with Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2024},\n  eprint={2310.03744},\n  archivePrefix={arXiv}\n}\n\n@article{chen2024internvl25,\n  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},\n  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2412.05271},\n  year={2024},\n  eprint={2412.05271},\n  archivePrefix={arXiv}\n}\n\n@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% Synced from literature_map.yaml (missing entries)\n% ============================================================\n\n% --- VLA Models ---\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023},\n  eprint={2307.15818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024},\n  eprint={2310.08864},\n  archivePrefix={arXiv}\n}\n\n% --- VLM/LLM Token Efficiency ---\n\n@inproceedings{zhang2023h2o,\n  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  eprint={2306.14048},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2309.17453},\n  archivePrefix={arXiv}\n}\n\n\n% --- Closed-Loop Evaluation ---\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022},\n  eprint={2112.03227},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023},\n  eprint={2303.04137},\n  archivePrefix={arXiv}\n}\n\n% --- Negative Results & Evaluation Pitfalls ---\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2023},\n  eprint={2205.13504},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2406.03980},\n  archivePrefix={arXiv}\n}\n\n% --- Vision Connectors & Token Compression ---\n\n@article{oquab2024dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024},\n  eprint={2304.07193},\n  archivePrefix={arXiv}\n}\n\n@article{su2024roformer,\n  title={{RoFormer}: Enhanced Transformer with Rotary Position Embedding},\n  author={Su, Jianlin and Ahmed, Murtadha and Lu, Yu and Pan, Shengfeng and Bo, Wen and Liu, Yunfeng},\n  journal={Neurocomputing},\n  volume={568},\n  pages={127063},\n  year={2024},\n  publisher={Elsevier}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 363,
        "oldLines": 7,
        "newStart": 363,
        "newLines": 7,
        "lines": [
          " ",
          " @inproceedings{zheng2025xvla,",
          "   title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},",
          "-  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and others},",
          "+  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and Kang, Xirui and Feng, Yuchun and Zheng, Yinan and Zou, Jiayin and Chen, Yilun and Zeng, Jia and Zhang, Ya-Qin and Pang, Jiangmiao and Liu, Jingjing and Wang, Tai and Zhan, Xianyuan},",
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

### Assistant

_source line 22_

修改完成。汇总：

### 1. `zheng2025xvla` — 已修复
- **修改前**: `author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and others}`
- **修改后**: 展开为完整 15 位作者：`Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and Kang, Xirui and Feng, Yuchun and Zheng, Yinan and Zou, Jiayin and Chen, Yilun and Zeng, Jia and Zhang, Ya-Qin and Pang, Jiangmiao and Liu, Jingjing and Wang, Tai and Zhan, Xianyuan`
- 第一作者已是 Jinliang（正确），venue 已是 ICLR 2026（正确）

### 2. `chen2024fastv` — 无需修改
- 当前已有完整 7 位作者：Chen, Liang / Zhao, Haozhe / Liu, Tianyu / Bai, Shuai / Lin, Junyang / Zhou, Chang / Chang, Baobao
- venue 已标注 ECCV + Oral presentation

### 3. `black2025pi05` — 无需修改
- 当前已是 `@inproceedings`，含 `booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)}`、`series={Proceedings of Machine Learning Research}`、`volume={305}`、`pages={17--40}`、`publisher={PMLR}`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "uuid": "79b6f090-7eee-42ed-a11e-2e2d7a1cfb64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017qkXT56qhR1Cb9jyv7nSbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2326,
      "cache_read_input_tokens": 38238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2326
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

_source line 23_

修改完成。汇总：

### 1. `zheng2025xvla` — 已修复
- **修改前**: `author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and others}`
- **修改后**: 展开为完整 15 位作者：`Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and Kang, Xirui and Feng, Yuchun and Zheng, Yinan and Zou, Jiayin and Chen, Yilun and Zeng, Jia and Zhang, Ya-Qin and Pang, Jiangmiao and Liu, Jingjing and Wang, Tai and Zhan, Xianyuan`
- 第一作者已是 Jinliang（正确），venue 已是 ICLR 2026（正确）

### 2. `chen2024fastv` — 无需修改
- 当前已有完整 7 位作者：Chen, Liang / Zhao, Haozhe / Liu, Tianyu / Bai, Shuai / Lin, Junyang / Zhou, Chang / Chang, Baobao
- venue 已标注 ECCV + Oral presentation

### 3. `black2025pi05` — 无需修改
- 当前已是 `@inproceedings`，含 `booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)}`、`series={Proceedings of Machine Learning Research}`、`volume={305}`、`pages={17--40}`、`publisher={PMLR}`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 93405,
  "duration_api_ms": 104538,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "17746824-1f4f-4a4a-ba8e-bab859b091cd",
  "total_cost_usd": 0.40607575,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 28719,
    "cache_read_input_tokens": 109394,
    "output_tokens": 4075,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28719,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 435,
        "cache_read_input_tokens": 38238,
        "cache_creation_input_tokens": 2326,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2326
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 35475,
      "outputTokens": 899,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 3,
      "costUSD": 0.06997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 4075,
      "cacheReadInputTokens": 109394,
      "cacheCreationInputTokens": 28719,
      "webSearchRequests": 0,
      "costUSD": 0.33610575,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1c5b73fb-4301-4049-8bff-715444cd9efa"
}
```

</details>

---
