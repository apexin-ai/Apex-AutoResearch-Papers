# audit ref verify worker B

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 207
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_audit_ref_verify_worker_B_20260529T062918.log`
- **Structured JSON:** [`ffd8f90c3749f068f5b8.json`](../../sessions/ff/ffd8f90c3749f068f5b8.json)

## Before a recorded user message

207 recorded events

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
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
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
    "Write"
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
  "uuid": "6a1e2c06-500d-4cb9-bc00-a1ff43bd85c7",
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
    "resetsAt": 1780041000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1d952363-e94d-4d61-976e-7c517b4a6f1b",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### Assistant

_source line 4_

I'll start by reading the bib file and all tex files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "31022dd5-745c-4bd5-91b9-10736c5bd21b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fi3Bs98qhmP5hbuXUoVoPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12927,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12927
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

<details open><summary>🔧 Tool call — Read · `toolu_012Z4282AW5yzB5ewW8QbeUF`</summary>

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
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "5c5ded20-d345-47e5-b711-da94f54d5c9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fi3Bs98qhmP5hbuXUoVoPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12927,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12927
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

_source line 6 · 2026-05-29T06:29:34.155Z_

<details><summary>↩ Tool result · `toolu_012Z4282AW5yzB5ewW8QbeUF`</summary>

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
366	  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and Kang, Xirui and Feng, Yuchun and Zheng, Yinan and Zou, Jiayin and Chen, Yilun and Zeng, Jia and Zhang, Ya-Qin and Pang, Jiangmiao and Liu, Jingjing and Wang, Tai and Zhan, Xianyuan},
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
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "b127cd51-943b-4fcb-8a22-29b079c44e60",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
      "content": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% Attention Analysis\n% ============================================================\n\n@inproceedings{abnar2020quantifying,\n  title={Quantifying Attention Flow in Transformers},\n  author={Abnar, Samira and Zuidema, Willem},\n  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n  pages={4190--4197},\n  year={2020},\n}\n\n% ============================================================\n% VLA Token Compression (concurrent work)\n% ============================================================\n\n@article{gao2025compressorvla,\n  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},\n  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},\n  journal={arXiv preprint arXiv:2511.18950},\n  year={2025},\n  eprint={2511.18950},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025specprunevla,\n  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},\n  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},\n  journal={arXiv preprint arXiv:2509.05614},\n  year={2025},\n  eprint={2509.05614},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{jiang2026lightvla,\n  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},\n  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},\n  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2026},\n  eprint={2509.12594},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{feng2026seewhatmatters,\n  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},\n  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},\n  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},\n  year={2026},\n  eprint={2605.11817},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zhang2025sparsevlm,\n  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},\n  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},\n  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},\n  year={2025},\n  eprint={2410.04417},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{khaki2025sparsevila,\n  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},\n  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025},\n  eprint={2510.17777},\n  archivePrefix={arXiv}\n}\n\n@article{jabbour2025dontrun,\n  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},\n  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},\n  journal={arXiv preprint arXiv:2510.08464},\n  year={2025},\n  eprint={2510.08464},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{li2024roboflamingo,\n  title={Vision-Language Foundation Models as Effective Robot Imitators},\n  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2311.01378},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@inproceedings{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  booktitle={Proceedings of The 9th Conference on Robot Learning (CoRL)},\n  series={Proceedings of Machine Learning Research},\n  volume={305},\n  pages={17--40},\n  year={2025},\n  publisher={PMLR},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt1,\n  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and Zhao, Haozhe and Liu, Tianyu and Bai, Shuai and Lin, Junyang and Zhou, Chang and Chang, Baobao},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  eprint={2403.06764},\n  archivePrefix={arXiv},\n  note={Oral presentation}\n}\n\n\n@inproceedings{xu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cheng2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n\n% ============================================================\n% VLA Token Efficiency (new additions)\n% ============================================================\n\n@article{yang2025efficientvla,\n  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},\n  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},\n  journal={arXiv preprint arXiv:2506.10100},\n  year={2025}\n}\n\n@article{liu2025vlapruner,\n  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},\n  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},\n  journal={arXiv preprint arXiv:2511.16449},\n  year={2025}\n}\n\n@inproceedings{shang2024prumerge,\n  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},\n  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025}\n}\n\n% ============================================================\n% Vision Connectors\n% ============================================================\n\n@inproceedings{alayrac2022flamingo,\n  title={Flamingo: a Visual Language Model for Few-Shot Learning},\n  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2022}\n}\n\n@inproceedings{liu2023llava,\n  title={Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{shi2016subpixel,\n  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},\n  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2016}\n}\n\n@article{chen2024internvl,\n  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},\n  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2404.16821},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{li2023blip2,\n  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},\n  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@inproceedings{jaegle2021perceiver,\n  title={Perceiver: General Perception with Iterative Attention},\n  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2021}\n}\n\n@article{oquab2023dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ============================================================\n% Additional references (Round 3 reviewer request)\n% ============================================================\n\n% ============================================================\n% Additional VLA / VLM references\n% ============================================================\n\n@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Jinliang and Li, Jianxiong and Wang, Zhihao and Liu, Dongxiu and Kang, Xirui and Feng, Yuchun and Zheng, Yinan and Zou, Jiayin and Chen, Yilun and Zeng, Jia and Zhang, Ya-Qin and Pang, Jiangmiao and Liu, Jingjing and Wang, Tai and Zhan, Xianyuan},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2510.10274},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{lewis2020bart,\n  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},\n  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},\n  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2020}\n}\n\n% ============================================================\n% New additions for expanded Related Work\n% ============================================================\n\n@inproceedings{ryoo2021tokenlearner,\n  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},\n  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021},\n  eprint={2106.11297},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{yin2022avit,\n  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},\n  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2112.07658},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{meng2022adavit,\n  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},\n  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2111.15668},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chen2023sparsevit,\n  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},\n  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2023},\n  eprint={2303.17605},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ye2025fitprune,\n  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},\n  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  eprint={2409.10197},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{shi2024crossget,\n  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},\n  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2305.17455},\n  archivePrefix={arXiv}\n}\n\n@article{zhang2024fastervlm,\n  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},\n  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},\n  journal={arXiv preprint arXiv:2412.01818},\n  year={2024},\n  eprint={2412.01818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{liu2024llava15,\n  title={Improved Baselines with Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2024},\n  eprint={2310.03744},\n  archivePrefix={arXiv}\n}\n\n@article{chen2024internvl25,\n  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},\n  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2412.05271},\n  year={2024},\n  eprint={2412.05271},\n  archivePrefix={arXiv}\n}\n\n@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% Synced from literature_map.yaml (missing entries)\n% ============================================================\n\n% --- VLA Models ---\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023},\n  eprint={2307.15818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024},\n  eprint={2310.08864},\n  archivePrefix={arXiv}\n}\n\n% --- VLM/LLM Token Efficiency ---\n\n@inproceedings{zhang2023h2o,\n  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  eprint={2306.14048},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2309.17453},\n  archivePrefix={arXiv}\n}\n\n\n% --- Closed-Loop Evaluation ---\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022},\n  eprint={2112.03227},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023},\n  eprint={2303.04137},\n  archivePrefix={arXiv}\n}\n\n% --- Negative Results & Evaluation Pitfalls ---\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2023},\n  eprint={2205.13504},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2406.03980},\n  archivePrefix={arXiv}\n}\n\n% --- Vision Connectors & Token Compression ---\n\n@article{oquab2024dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024},\n  eprint={2304.07193},\n  archivePrefix={arXiv}\n}\n\n@article{su2024roformer,\n  title={{RoFormer}: Enhanced Transformer with Rotary Position Embedding},\n  author={Su, Jianlin and Ahmed, Murtadha and Lu, Yu and Pan, Shengfeng and Bo, Wen and Liu, Yunfeng},\n  journal={Neurocomputing},\n  volume={568},\n  pages={127063},\n  year={2024},\n  publisher={Elsevier}\n}\n\n",
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

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01J6zU8CxikqCt3EueGbUftb`</summary>

```json
{
  "pattern": "*.tex",
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
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "93216603-ffbe-4ca6-9573-29d568fabcd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fi3Bs98qhmP5hbuXUoVoPn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12927,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12927
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

_source line 8 · 2026-05-29T06:29:34.538Z_

<details><summary>↩ Tool result · `toolu_01J6zU8CxikqCt3EueGbUftb`</summary>

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
docs/paper/experimental_setup.tex
docs/paper/discussion.tex
docs/paper/analysis.tex
docs/paper/background.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/results.tex
docs/paper/results_v2.tex
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/experiments.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "5f10659e-9968-4217-b4a8-85722e4aadaf",
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
      "docs/paper/experimental_setup.tex",
      "docs/paper/discussion.tex",
      "docs/paper/analysis.tex",
      "docs/paper/background.tex",
      "docs/paper/main.tex",
      "docs/paper/related_work.tex",
      "docs/paper/introduction.tex",
      "docs/paper/abstract.tex",
      "docs/paper/results.tex",
      "docs/paper/results_v2.tex",
      "docs/paper/appendix.tex",
      "docs/paper/method.tex",
      "docs/paper/experiments.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/limitations.tex"
    ],
    "durationMs": 22,
    "numFiles": 24,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read all the tex files to extract citations. Let me read the main tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "68ac64c9-eded-4fea-8e6e-6d032cec28c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

Now reading all tex files to extract citation usage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "89941c64-945a-4078-ad3f-f9abf08415fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

<details open><summary>🔧 Tool call — Read · `toolu_011wq4kV1evMXy1Kro7BZM1h`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "82e78308-8e32-49f1-b049-2b7a6a15e36f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 12 · 2026-05-29T06:29:40.240Z_

<details><summary>↩ Tool result · `toolu_011wq4kV1evMXy1Kro7BZM1h`</summary>

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
15	\setlength{\textfloatsep}{6pt plus 2pt minus 4pt}
16	\setlength{\floatsep}{6pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{6pt plus 2pt minus 4pt}
18	\setlength{\abovecaptionskip}{3pt}
19	\setlength{\belowcaptionskip}{0pt}
20	\setlength{\abovedisplayskip}{6pt plus 2pt minus 4pt}
21	\setlength{\belowdisplayskip}{6pt plus 2pt minus 4pt}
22	
23	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	
30	\keywords{vision-language-action models, token pruning, robot learning}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{experiments}
39	
40	\input{conclusion}
41	
42	\input{limitations}
43	
44	\bibliography{references}
45	
46	\input{appendix}
47	
48	\end{document}
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "1587e252-e3c5-48ae-b52f-16e7b7076afc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
      "content": "\\documentclass{article}\n\n\\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.\n% \\usepackage[final]{corl_2026} % Uncomment for camera-ready.\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage{wrapfig}\n\n% Tighten float spacing for page limit\n\\setlength{\\textfloatsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\floatsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{3pt}\n\\setlength{\\belowcaptionskip}{0pt}\n\\setlength{\\abovedisplayskip}{6pt plus 2pt minus 4pt}\n\\setlength{\\belowdisplayskip}{6pt plus 2pt minus 4pt}\n\n\\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\\\Vision Connectors and VLA Token Compressibility}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\keywords{vision-language-action models, token pruning, robot learning}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01ND7k2LFR83sDqNauFwEs7Z`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "209bcb0e-8b21-47d3-aff6-73aa5f09bbb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 14 · 2026-05-29T06:29:40.716Z_

<details><summary>↩ Tool result · `toolu_01ND7k2LFR83sDqNauFwEs7Z`</summary>

```text
1	\begin{abstract}
2	Deploying Vision-Language-Action (VLA) models for real-time control requires compressing their vision token sequences, yet identical pruning applied to different architectures produces wildly divergent outcomes---from unscathed performance to total collapse. We trace this divergence to the vision-language connector, the module bridging the visual encoder and language backbone. Across six VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, a single forward-pass diagnostic---the coefficient of variation (CV) of post-connector token norms---predicts pruning tolerance without any task evaluation. Low-CV connectors permit aggressive pruning; high-CV connectors collapse when even a few tokens are removed. No scoring method is universally safe: the advantage of importance-based over random selection follows an inverted-U curve that peaks at moderate compression and reverses at aggressive ratios, with task complexity amplifying connector-dependent patterns. A zero-mask ablation reveals that position disruption, not information loss, is the binding constraint. For architectures where all deletion fails, a lightweight re-encoder (${\sim}$5\% extra parameters) recovers baseline performance at 75\% compression.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "2eed79ee-7ebb-4aff-8c00-4a762c404e28",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nDeploying Vision-Language-Action (VLA) models for real-time control requires compressing their vision token sequences, yet identical pruning applied to different architectures produces wildly divergent outcomes---from unscathed performance to total collapse. We trace this divergence to the vision-language connector, the module bridging the visual encoder and language backbone. Across six VLA architectures (450\\,M--7\\,B parameters) and four LIBERO manipulation suites, a single forward-pass diagnostic---the coefficient of variation (CV) of post-connector token norms---predicts pruning tolerance without any task evaluation. Low-CV connectors permit aggressive pruning; high-CV connectors collapse when even a few tokens are removed. No scoring method is universally safe: the advantage of importance-based over random selection follows an inverted-U curve that peaks at moderate compression and reverses at aggressive ratios, with task complexity amplifying connector-dependent patterns. A zero-mask ablation reveals that position disruption, not information loss, is the binding constraint. For architectures where all deletion fails, a lightweight re-encoder (${\\sim}$5\\% extra parameters) recovers baseline performance at 75\\% compression.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01WqS9HfJ6ypyFotUQfHZH5G`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "539ae532-9c4a-4b89-ae13-9c33eec1035e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 16 · 2026-05-29T06:29:41.197Z_

<details><summary>↩ Tool result · `toolu_01WqS9HfJ6ypyFotUQfHZH5G`</summary>

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
14	Vision-Language-Action (VLA) models process robot observations as hundreds of vision tokens, creating a computational bottleneck for real-time control. Token pruning---removing low-importance tokens before the language backbone---is well-established for vision transformers~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and has been applied to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}. Yet each method validates on a single architecture, implicitly assuming that pruning transfers across designs.
15	
16	This assumption is unsafe. Current VLAs employ fundamentally different vision connectors---linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Whether a pruning strategy validated on one connector type will transfer to another is unknown; deploying it blindly risks silent degradation or complete failure.
17	
18	We present the first cross-architecture study of VLA token compressibility, evaluating six architectures (450M--7B) across four LIBERO manipulation suites (Figure~\ref{fig:teaser}). The vision-language connector emerges as the strongest predictor of pruning robustness: token-independent connectors degrade gracefully, while token-entangling connectors exhibit catastrophic cliffs that task complexity amplifies. No scoring method is universally safe---importance-based selection can dramatically outperform or underperform random pruning depending on the connector, following an inverted-U importance margin that reverses at aggressive compression ratios. A zero-mask ablation isolates the mechanism: position disruption, not information loss, drives failure.
19	
20	Our contributions: (1)~the first cross-architecture VLA compressibility analysis, revealing connector type as the dominant factor governing pruning tolerance; (2)~the coefficient of variation (CV) of post-connector token norms as a zero-cost, single-pass diagnostic predicting both pruning tolerance and scoring method sensitivity; (3)~mechanistic evidence that position disruption drives failure in position-sensitive architectures, plus a lightweight Vision Token Re-encoder (VTR, ${\sim}$5\% extra parameters) recovering baseline performance at 75\% compression for architectures where all deletion fails.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "ffca1656-aa03-4d4f-8903-3d182b1611ec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_hero_overview.pdf}\n\\caption{Overview of VLA token compressibility.\n\\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.\n\\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.\n\\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy.}\n\\label{fig:teaser}\n\\end{figure*}\n\nVision-Language-Action (VLA) models process robot observations as hundreds of vision tokens, creating a computational bottleneck for real-time control. Token pruning---removing low-importance tokens before the language backbone---is well-established for vision transformers~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and has been applied to VLAs~\\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}. Yet each method validates on a single architecture, implicitly assuming that pruning transfers across designs.\n\nThis assumption is unsafe. Current VLAs employ fundamentally different vision connectors---linear projections~\\cite{black2024pi0}, MLP projectors~\\cite{kim2024openvla}, pixel-shuffle folding~\\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Whether a pruning strategy validated on one connector type will transfer to another is unknown; deploying it blindly risks silent degradation or complete failure.\n\nWe present the first cross-architecture study of VLA token compressibility, evaluating six architectures (450M--7B) across four LIBERO manipulation suites (Figure~\\ref{fig:teaser}). The vision-language connector emerges as the strongest predictor of pruning robustness: token-independent connectors degrade gracefully, while token-entangling connectors exhibit catastrophic cliffs that task complexity amplifies. No scoring method is universally safe---importance-based selection can dramatically outperform or underperform random pruning depending on the connector, following an inverted-U importance margin that reverses at aggressive compression ratios. A zero-mask ablation isolates the mechanism: position disruption, not information loss, drives failure.\n\nOur contributions: (1)~the first cross-architecture VLA compressibility analysis, revealing connector type as the dominant factor governing pruning tolerance; (2)~the coefficient of variation (CV) of post-connector token norms as a zero-cost, single-pass diagnostic predicting both pruning tolerance and scoring method sensitivity; (3)~mechanistic evidence that position disruption drives failure in position-sensitive architectures, plus a lightweight Vision Token Re-encoder (VTR, ${\\sim}$5\\% extra parameters) recovering baseline performance at 75\\% compression for architectures where all deletion fails.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01J9prdaMdWAeHSTaYYkRADV`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "e3514bac-64ea-43dd-bba9-7c0021748e54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 18 · 2026-05-29T06:29:41.610Z_

<details><summary>↩ Tool result · `toolu_01J9prdaMdWAeHSTaYYkRADV`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, Token Merging~\cite{bolya2023tome}, and CrossGET~\cite{shi2024crossget} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv}, PruMerge~\cite{shang2024prumerge}, SparseVLM~\cite{zhang2025sparsevlm}, SparseVILA~\cite{khaki2025sparsevila}, and FitPrune~\cite{ye2025fitprune} reduce vision tokens in VLMs using attention or importance signals. VLA-specific methods have emerged: VLA-IAP~\cite{cheng2026vlaiap}, VLA-Cache~\cite{xu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, VLA-Pruner~\cite{liu2025vlapruner}, LightVLA~\cite{jiang2026lightvla}, Compressor-VLA~\cite{gao2025compressorvla}, SpecPrune-VLA~\cite{wang2025specprunevla}, and See What Matters~\cite{feng2026seewhatmatters}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.
9	
10	\paragraph{Concurrent work.}
11	Jabbour et al.~\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.
12	
13	\paragraph{Vision connectors.}
14	LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "1a764674-985a-4678-9b17-309a16af1002",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{ViT token pruning.}\nDynamicViT~\\cite{rao2021dynamicvit}, EViT~\\cite{liang2022evit}, A-ViT~\\cite{yin2022avit}, Token Merging~\\cite{bolya2023tome}, and CrossGET~\\cite{shi2024crossget} remove 50--66\\% of tokens with under 0.5\\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.\n\n\\paragraph{Token efficiency in VLMs and VLAs.}\nFastV~\\cite{chen2024fastv}, PruMerge~\\cite{shang2024prumerge}, SparseVLM~\\cite{zhang2025sparsevlm}, SparseVILA~\\cite{khaki2025sparsevila}, and FitPrune~\\cite{ye2025fitprune} reduce vision tokens in VLMs using attention or importance signals. VLA-specific methods have emerged: VLA-IAP~\\cite{cheng2026vlaiap}, VLA-Cache~\\cite{xu2025vlacache}, EfficientVLA~\\cite{yang2025efficientvla}, VLA-Pruner~\\cite{liu2025vlapruner}, LightVLA~\\cite{jiang2026lightvla}, Compressor-VLA~\\cite{gao2025compressorvla}, SpecPrune-VLA~\\cite{wang2025specprunevla}, and See What Matters~\\cite{feng2026seewhatmatters}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.\n\n\\paragraph{Concurrent work.}\nJabbour et al.~\\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.\n\n\\paragraph{Vision connectors.}\nLLaVA~\\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_017nzzpFwQzkDBuLTZVAxSHm`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "b18750db-9abc-42b2-ac46-fa724885eed5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 20 · 2026-05-29T06:29:42.628Z_

<details><summary>↩ Tool result · `toolu_017nzzpFwQzkDBuLTZVAxSHm`</summary>

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
12	SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 450M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.
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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "c84a5b39-ee9a-40c4-bff7-b01db7d3f83a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex",
      "content": "% background.tex -- Section 2: Background\n\n\\section{Background}\n\\label{sec:background}\n\nThis section describes the architectures and benchmark used in our study: SmolVLA~\\cite{shukor2025smolvla} and OpenVLA~\\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\\cite{liu2023libero} on which we evaluate closed-loop performance.\n\n\\subsection{SmolVLA Architecture}\n\\label{sec:smolvla_arch}\n\nVision-Language-Action (VLA) models cast robotic control as conditional generation: given a camera observation and a language instruction, the model predicts a continuous action.\nSmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 450M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.\nFigure~\\ref{fig:architecture} contrasts the vision pipelines of SmolVLA and OpenVLA, highlighting the connector designs that determine compressibility.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_architecture.pdf}\n\\caption{Vision connector comparison. \\textbf{Left}: SmolVLA applies $4{\\times}4$ pixel-shuffle to fold 1024 SigLIP patches into 64 tokens per camera (128 total), creating dense, spatially entangled representations. \\textbf{Right}: OpenVLA uses an MLP projector that maps each patch independently, producing 256 tokens with per-token independence. We hypothesize that this architectural difference is the primary factor governing token compressibility: pixel-shuffle tokens resist any form of deletion, while independently projected tokens allow graded pruning.}\n\\label{fig:architecture}\n\\end{figure}\n\n\\paragraph{Vision encoder.}\nSmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\nSigLIP divides each camera image into non-overlapping spatial patches on a $32 \\times 32$ grid, producing 1024 patch tokens per image.\nSigLIP does not include a \\texttt{[CLS]} aggregation token; there is no single summary representation that pools information across patches.\n\n\\paragraph{Pixel-shuffle vision connector.}\nBefore reaching the language model, the 1024 SigLIP patches pass through a pixel-shuffle connector that applies $4 \\times 4$ spatial folding. Each $4 \\times 4$ block of spatially adjacent patches is collapsed into a single token by channel concatenation, compressing 1024 patches into 64 tokens per camera image ($16\\times$ reduction). An MLP then projects these 64 tokens into the Qwen2-0.5B embedding space. The pixel-shuffle operation is fixed and non-learned; it creates dense tokens where each encodes the full semantic content of 16 contiguous patches. This design choice is central to the cliff-edge phenomenon we report: the spatial folding creates inter-token dependencies that make every token indispensable.\n\n\\paragraph{Dual-camera input.}\nSmolVLA receives images from two cameras: a wrist-mounted camera and an overhead camera.\nEach camera image produces 64 vision tokens after pixel-shuffle, yielding 128 vision tokens total that enter the language model.\nThe two viewpoints are complementary: the wrist camera captures fine-grained end-effector interactions, while the overhead camera provides a global spatial layout of objects on the workspace.\n\n\\paragraph{LLM backbone.}\nThe Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\nIt receives a concatenated input sequence of 128 projected vision tokens and the tokenized language instruction.\nSelf-attention across this full sequence allows the model to ground language in visual context and to integrate information across both camera views.\n\n\\paragraph{Flow matching action head.}\nSmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\nThe action head maps the LLM's output representation to a continuous 7-DoF action vector: three position coordinates, three rotation angles, and one gripper open/close value.\nFlow matching learns a vector field that transports a noise distribution to the target action distribution, conditioned on the LLM output.\nAny corruption of the vision token input propagates through the full LLM computation into the predicted action.\n\n\\subsection{OpenVLA Architecture}\n\\label{sec:openvla_arch}\n\nOpenVLA~\\cite{kim2024openvla} is a 7B-parameter VLA built on the Llama-2 backbone. Its vision pipeline differs from SmolVLA in two respects that are directly relevant to compressibility.\n\n\\paragraph{Vision encoder.}\nOpenVLA uses a dual encoder combining DINOv2~\\cite{oquab2023dinov2} and SigLIP~\\cite{zhai2023siglip}. The two encoders produce complementary representations (self-supervised spatial features and language-aligned features) that are concatenated per patch position.\n\n\\paragraph{MLP projector.}\nUnlike SmolVLA's pixel-shuffle connector, OpenVLA maps vision encoder outputs to the language model through a three-layer MLP projector (GELU activations) that processes each patch token independently. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence. The projector produces 256 vision tokens that maintain a one-to-one correspondence with spatial patch locations.\n\n\\paragraph{Architectural contrast.}\nThe key difference for compressibility is the connector design. SmolVLA's pixel-shuffle folds 16 patches into each token, creating dense, entangled representations where removing one token eliminates a $4 \\times 4$ spatial region. OpenVLA's MLP projector preserves patch-level granularity, so removing one token discards approximately $1/256$ of the visual field. Model scale (0.5B vs.\\ 7B) is a confound that we discuss in Section~\\ref{sec:discussion}.\n\n\\subsection{LIBERO Benchmark}\n\\label{sec:libero_bench}\n\nWe evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\nLIBERO provides standardized task definitions, initial state distributions, and evaluation protocols for reproducible comparison of manipulation policies.\nWe use three of its four suites, each testing a distinct aspect of policy competence.\nLIBERO-Object presents ten tasks focused on object manipulation; the policy must identify and interact with specific objects from visually similar alternatives.\nLIBERO-Spatial presents ten tasks focused on spatial reasoning, where the policy must place objects correctly or navigate relative to reference locations.\nLIBERO-Goal presents ten tasks with varied goal conditions applied to a shared environment layout; these tasks test whether the policy can condition its behavior on the language instruction.\n\nEach suite contains 10 tasks, and we run 50 evaluation episodes per task, yielding 500 episodes per suite per experimental condition.\nThe evaluation metric is closed-loop Success Rate (SR): a binary indicator per episode that equals 1 only if the robot completes the full task within the time limit.\nSR is measured through closed-loop execution, where the policy observes the current state, predicts an action, the simulator advances, and the policy re-observes the updated state at every timestep.\nThis closed-loop evaluation is critical because errors at any single step can cascade through subsequent observations and actions.\nA policy that produces even one qualitatively wrong action (for example, opening the gripper when it should close) will likely fail the entire episode.\n\nThe three LIBERO suites span a range of baseline difficulty levels: SmolVLA achieves 44.8\\% SR on Object, 51.8\\% on Spatial, and 63.0\\% on Goal in bypass mode (full vision tokens, no pruning).\nThese baseline numbers are not state-of-the-art; SmolVLA is a compact model designed for efficiency research.\nThe relevant comparison is not the absolute success rate but the change under token reduction: any viable pruning strategy must approximately preserve these baselines rather than collapse to 0\\%.",
      "numLines": 78,
      "startLine": 1,
      "totalLines": 78
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01DaVT3hZV4N82YciiXdvAVP`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "19d14c42-4b82-4831-ba44-9f8d952f55d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 22 · 2026-05-29T06:29:43.100Z_

<details><summary>↩ Tool result · `toolu_01DaVT3hZV4N82YciiXdvAVP`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). To preview each connector's compressibility, we report the coefficient of variation (CV) of post-connector token L2 norms---the ratio of standard deviation to mean across all vision tokens from a single forward pass (formally defined in Section~\ref{sec:cv_diagnostic}). \textbf{Linear projection} applies a per-patch matrix multiplication ($\pi_{0}$~\cite{black2024pi0}, $\pi_{0.5}$~\cite{black2025pi05}; CV$\,{<}\,$0.06). \textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\cite{kim2024openvla}, OFT~\cite{kim2025openoft}; CV$\,{\approx}\,$0.22). \textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\cite{zheng2025xvla} uses a 12-layer BART encoder~\cite{lewis2020bart} (CV$\,{=}\,$0.151); SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 patches per token (CV$\,{=}\,$0.314). We classify coupling as \emph{independent} (one patch per output) or \emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
8	
9	\begin{figure*}[t]
10	\centering
11	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
12	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Independent connectors yield low CV; entangling connectors create cross-token dependencies and higher CV.}
13	\label{fig:architecture}
14	\end{figure*}
15	
16	\subsection{Pruning Protocol}
17	\label{sec:pruning_protocol}
18	
19	Given $N$ post-connector tokens $\{t_1, \ldots, t_N\}$ with $t_i \in \mathbb{R}^d$, token pruning retains $\lfloor k \cdot N \rfloor$ tokens for $k \in (0, 1]$ and physically removes the rest. Crucially, we \emph{re-index} the remaining positions contiguously (i.e., the $j$-th retained token receives position ID $j$) rather than preserving original position IDs. This choice isolates two confounded effects: information loss from removing tokens and position disruption from re-indexing. We prune between the connector output and LLM input to isolate the connector's effect on token information structure; the vision encoder and LLM weights remain frozen throughout.
20	
21	\paragraph{Importance scoring functions.}
22	A scoring function $s\colon \mathbb{R}^d \to \mathbb{R}$ assigns each token an importance score; the top-$\lfloor kN \rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies that require only the connector output, not LLM internals.
23	
24	\textbf{L2-norm scoring} uses activation magnitude $s_{\text{L2}}(t_i) = \|t_i\|_2$ as a proxy for information density. For each image, we compute the L2 norm of every post-connector token, rank tokens in descending order, and retain the top-$\lfloor kN \rfloor$. L2 scoring introduces spatial bias: nearby patches share similar visual content and produce correlated norms, so aggressive pruning can concentrate retained tokens in a single spatial region at the expense of scene coverage (Section~\ref{sec:cv_sensitivity}).
25	
26	\textbf{Random subsampling} draws $\lfloor kN \rfloor$ tokens uniformly without replacement ($s_{\text{rand}}(t_i) \sim \mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. To control sampling variance, we report results over multiple seeds (Section~\ref{sec:exp_setup}).
27	
28	We also evaluate \textbf{attention-based scoring} on selected conditions: for each vision token, we sum the attention weights it receives from all action-query tokens across all LLM layers, yielding an importance score that reflects the LLM's actual usage pattern. Results appear in Appendix~\ref{app:attention_scoring}; we focus on L2 and random in the main text because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.
29	
30	The \emph{importance margin} $\Delta(k) = \text{SR}_{\text{L2}}(k) - \text{SR}_{\text{Random}}(k)$ quantifies exploitable importance structure at each retention ratio. A positive margin means the token importance landscape is informative---L2 norm successfully identifies dispensable tokens. A negative margin indicates L2 selection is actively harmful, clustering spatially correlated tokens while discarding critical spatial coverage. The sign and magnitude of $\Delta$ vary systematically with connector CV and $k$ (Section~\ref{sec:cv_sensitivity}).
31	
32	\paragraph{Retention ratios and evaluation.}
33	We evaluate $k \in \{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\}$, spanning extreme compression to conservative trimming. For each model--suite--method--$k$ combination, we run all 50 evaluation episodes per task (10 tasks $\times$ 50 episodes $=$ 500 total) and report mean success rate (SR). Multi-seed conditions ($\pi_{0.5}$ Long: $n{=}5$ seeds; VTR: $n{=}3$) report mean $\pm$ sample standard deviation. This range identifies \emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\approx}0.85$, MLP without a sharp cliff (Appendix~\ref{app:pruning_details}).
34	
35	\begin{table}[t]
36	\centering
37	\small
38	\caption{VLA models evaluated. Coupling indicates independent vs.\ cross-token processing. $N$ = vision tokens input to the LLM. $^\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}
39	\label{tab:model_properties}
40	\begin{tabular}{lrlcrll}
41	\toprule
42	Model & Params & Connector & $N$ & CV & Coupling & Eval \\
43	\midrule
44	$\pi_{0.5}$ & 4B & Linear ($\times\!\sqrt{d}$) & 768 & 0.055 & Indep.\ & Closed-loop \\
45	X-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\
46	OpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\ & Closed-loop \\
47	SmolVLA & 450M & Pixel-shuffle $4{\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\
48	\midrule
49	$\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\ & Offline \\
50	OFT$^\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\ & Offline \\
51	\bottomrule
52	\end{tabular}
53	\end{table}
54	
55	\subsection{Compressibility Diagnostic: Importance CV}
56	\label{sec:cv_diagnostic}
57	
58	We seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:
59	\begin{equation}
60	\text{CV} = \frac{\sigma\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}{\mu\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}
61	\label{eq:cv}
62	\end{equation}
63	where $\sigma$ and $\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.
64	
65	\paragraph{The CV spectrum.}
66	CV captures a continuous ordering across six models and three connector families (Table~\ref{tab:model_properties}). Linear projections yield the lowest values ($\pi_{0}$: 0.038 (offline), $\pi_{0.5}$: 0.055), followed by X-VLA's BART encoder (0.151), the MLP projectors of OpenVLA and OFT (0.215, 0.219), and SmolVLA's pixel-shuffle at the high end (0.314). The progression reflects increasing cross-token entanglement: linear projections produce near-uniform norms (CV$\,{<}\,$0.06), MLP nonlinearities amplify variance (CV$\,{\approx}\,$0.22), and pixel-shuffle creates maximal entanglement.
67	
68	\paragraph{CV as pruning tolerance predictor.}
69	High CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\,{<}\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\,{>}\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\Delta$ increases monotonically with CV across three closed-loop models (Section~\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\ref{app:attention_entropy}).
70	
71	\subsection{Vision Token Re-encoder (VTR)}
72	\label{sec:vtr}
73	
74	Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.
75	
76	\paragraph{Architecture.}
77	VTR inserts a 2-layer cross-attention module (12 heads) between the connector output and the LLM input. $M$ learned queries attend over all $N$ source tokens, producing $M$ compressed tokens ($M \in \{16, 32, 64, 96, 128\}$). The module adds ${\sim}$22M parameters ($<$5\% of SmolVLA) and is trained end-to-end (Appendix~\ref{app:smart_compress_details}).
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "7b7f039b-7e95-49fa-a768-dc05337a8c36",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). To preview each connector's compressibility, we report the coefficient of variation (CV) of post-connector token L2 norms---the ratio of standard deviation to mean across all vision tokens from a single forward pass (formally defined in Section~\\ref{sec:cv_diagnostic}). \\textbf{Linear projection} applies a per-patch matrix multiplication ($\\pi_{0}$~\\cite{black2024pi0}, $\\pi_{0.5}$~\\cite{black2025pi05}; CV$\\,{<}\\,$0.06). \\textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\\cite{kim2024openvla}, OFT~\\cite{kim2025openoft}; CV$\\,{\\approx}\\,$0.22). \\textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\\cite{zheng2025xvla} uses a 12-layer BART encoder~\\cite{lewis2020bart} (CV$\\,{=}\\,$0.151); SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 patches per token (CV$\\,{=}\\,$0.314). We classify coupling as \\emph{independent} (one patch per output) or \\emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Independent connectors yield low CV; entangling connectors create cross-token dependencies and higher CV.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning retains $\\lfloor k \\cdot N \\rfloor$ tokens for $k \\in (0, 1]$ and physically removes the rest. Crucially, we \\emph{re-index} the remaining positions contiguously (i.e., the $j$-th retained token receives position ID $j$) rather than preserving original position IDs. This choice isolates two confounded effects: information loss from removing tokens and position disruption from re-indexing. We prune between the connector output and LLM input to isolate the connector's effect on token information structure; the vision encoder and LLM weights remain frozen throughout.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies that require only the connector output, not LLM internals.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. For each image, we compute the L2 norm of every post-connector token, rank tokens in descending order, and retain the top-$\\lfloor kN \\rfloor$. L2 scoring introduces spatial bias: nearby patches share similar visual content and produce correlated norms, so aggressive pruning can concentrate retained tokens in a single spatial region at the expense of scene coverage (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly without replacement ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. To control sampling variance, we report results over multiple seeds (Section~\\ref{sec:exp_setup}).\n\nWe also evaluate \\textbf{attention-based scoring} on selected conditions: for each vision token, we sum the attention weights it receives from all action-query tokens across all LLM layers, yielding an importance score that reflects the LLM's actual usage pattern. Results appear in Appendix~\\ref{app:attention_scoring}; we focus on L2 and random in the main text because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure at each retention ratio. A positive margin means the token importance landscape is informative---L2 norm successfully identifies dispensable tokens. A negative margin indicates L2 selection is actively harmful, clustering spatially correlated tokens while discarding critical spatial coverage. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Retention ratios and evaluation.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. For each model--suite--method--$k$ combination, we run all 50 evaluation episodes per task (10 tasks $\\times$ 50 episodes $=$ 500 total) and report mean success rate (SR). Multi-seed conditions ($\\pi_{0.5}$ Long: $n{=}5$ seeds; VTR: $n{=}3$) report mean $\\pm$ sample standard deviation. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}). Linear projections yield the lowest values ($\\pi_{0}$: 0.038 (offline), $\\pi_{0.5}$: 0.055), followed by X-VLA's BART encoder (0.151), the MLP projectors of OpenVLA and OFT (0.215, 0.219), and SmolVLA's pixel-shuffle at the high end (0.314). The progression reflects increasing cross-token entanglement: linear projections produce near-uniform norms (CV$\\,{<}\\,$0.06), MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22), and pixel-shuffle creates maximal entanglement.\n\n\\paragraph{CV as pruning tolerance predictor.}\nHigh CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy}).\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module (12 heads) between the connector output and the LLM input. $M$ learned queries attend over all $N$ source tokens, producing $M$ compressed tokens ($M \\in \\{16, 32, 64, 96, 128\\}$). The module adds ${\\sim}$22M parameters ($<$5\\% of SmolVLA) and is trained end-to-end (Appendix~\\ref{app:smart_compress_details}).\n",
      "numLines": 78,
      "startLine": 1,
      "totalLines": 78
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_014j77NLTxyEtDYw9bGVupYZ`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "5b9b9e17-17ca-40bd-a345-229575b9187f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 24 · 2026-05-29T06:29:43.585Z_

<details><summary>↩ Tool result · `toolu_014j77NLTxyEtDYw9bGVupYZ`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).
8	
9	\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\ref{tab:model_properties}): $\pi_{0.5}$~\cite{black2025pi05}, X-VLA~\cite{zheng2025xvla}, OpenVLA~\cite{kim2024openvla}, and SmolVLA~\cite{shukor2025smolvla}. Two additional models ($\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.
10	
11	\paragraph{Protocol.} We prune at $k \in \{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\}$ and report mean SR over 500 episodes. Multi-seed results ($\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\pm$ s.d.\ with per-seed breakdowns in the appendix.
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
16	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
17	\label{fig:pruning_overview}
18	\end{figure}
19	
20	\subsection{Two-Axis Framework Overview}
21	\label{sec:two_axis}
22	
23	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
24	
25	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\geq}$98.0\% through $k{=}0.85$ (Appendix Table~\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\%, an 89\,pp (percentage points) method gap from identical removal fractions.
26	
27	\textbf{X-VLA (BART encoder, CV$\,{=}\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 1.4\,pp, yet the same model drops 28.2\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.
28	
29	\textbf{OpenVLA (MLP, CV$\,{=}\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\ref{tab:full_results}; Section~\ref{sec:analysis}).
30	
31	\textbf{SmolVLA (pixel-shuffle, CV$\,{=}\,$0.314).} Removing 7 of 128 tokens ($k{=}0.95$) collapses SR to ${\leq}$6.6\% across all suites and methods, a catastrophic cliff detailed in Section~\ref{sec:pixel_shuffle}.
32	
33	\begin{table*}[t]
34	\centering
35	\small
36	\caption{Closed-loop SR (\%) on LIBERO under L2 norm (L2) and random (R) pruning. $\pi_{0.5}$ Long: five-seed mean ($n{=}5$). Full results including OpenVLA in Appendix Table~\ref{tab:full_results}.}
37	\label{tab:main_results}
38	\begin{tabular}{llcccc}
39	\toprule
40	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
41	\midrule
42	\multirow{4}{*}{$\pi_{0.5}$}
43	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 33.4 / 69.4 \\
44	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\
45	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\
46	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\
47	\midrule
48	\multirow{4}{*}{X-VLA}
49	& Object  & \textbf{99.2} & 99.0 / 98.8 & 99.2 / 97.8 & 43.4 / 70.6 \\
50	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\
51	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\
52	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\
53	\midrule
54	\multirow{4}{*}{SmolVLA}
55	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
56	& Spatial & \textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
57	& Goal    & \textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
58	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
59	\bottomrule
60	\end{tabular}
61	\end{table*}
62	
63	\begin{figure*}[t]
64	\centering
65	\begin{subfigure}[t]{0.49\textwidth}
66	\centering
67	\includegraphics[width=\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
68	\caption{}
69	\label{fig:pixel_shuffle}
70	\end{subfigure}\hfill%
71	\begin{subfigure}[t]{0.49\textwidth}
72	\centering
73	\includegraphics[width=\linewidth]{figures/paper/fig_method_gap.pdf}
74	\caption{}
75	\label{fig:method_gap}
76	\end{subfigure}
77	\caption{(a)~Pixel-shuffle $4{\times}4$ entanglement: each 16-patch block forms one token; removing any eliminates a non-overlapping receptive field with no redundancy. (b)~Method gap $|\text{SR(L2)} - \text{SR(Random)}|$ at $k{=}0.95$: $\pi_{0.5}$'s Object gap (24.2\,pp) exceeds X-VLA's maximum (1.4\,pp) by $17{\times}$ (single seed except $\pi_{0.5}$ Long, $n{=}5$).}
78	\label{fig:entanglement_and_gap}
79	\end{figure*}
80	
81	\subsection{Pixel-Shuffle Entanglement}
82	\label{sec:pixel_shuffle}
83	
84	SmolVLA's pixel-shuffle $4{\times}4$ folding concatenates 16 patches per token (Figure~\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\leq}$6.6\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\ref{app:smolvla_ablation}). Notably, X-VLA's BART encoder is also entangling, yet far more robust: its 12-layer self-attention redistributes information across tokens, creating inter-token redundancy that buffers against removal. Pixel-shuffle performs a fixed deterministic fold with no learned information sharing---each output token's receptive field is disjoint, leaving zero redundancy for pruning to exploit.
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=0.75\linewidth]{figures/paper/fig_cliff_highlight.pdf}
89	\caption{Scoring method cliff behavior on $\pi_{0.5}$ Long ($n{=}5$, mean $\pm$ s.d.). L2 degrades monotonically; attention cliffs at $k{=}0.85$; random V-shapes with collapse at $k{=}0.9$.}
90	\label{fig:cliff_highlight}
91	\end{figure}
92	
93	\subsection{Position Disruption vs.\ Information Loss}
94	\label{sec:zeromask}
95	
96	$\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\% on Object despite removing only 10\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\% SR while hard pruning collapses to 9.0\%. On $\pi_{0.5}$, the 89\,pp gap is entirely attributable to position disruption: its linear connector tolerates complete signal destruction but not index shifts. This ablation targets $\pi_{0.5}$ because its Rotary Position Embedding (RoPE)-based position encoding is most susceptible to re-indexing; other connectors use different positional mechanisms.
97	
98	This has practical implications: for position-sensitive architectures, any compression that alters the sequence length will disrupt positional encodings. Strategies for such models must either preserve the original length (e.g., zero-masking) or include position-aware mechanisms that compensate for index shifts.
99	
100	\subsection{Scoring Method Sensitivity and CV Diagnostic}
101	\label{sec:cv_sensitivity}
102	
103	CV predicts where scoring method choice becomes critical (Figure~\ref{fig:method_gap}). $\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\,pp, exceeding X-VLA's maximum (1.4\,pp) by $17{\times}$. At $k{=}0.5$, the importance margin on Object is $\Delta{=}{-}36.0$\,pp ($\pi_{0.5}$) and ${-}27.2$\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.
104	
105	\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\geq}$92.8\% while L2 falls 8--27\,pp below random; on $\pi_{0.5}$, attention is catastrophically harmful on Object ($-$31.6\,pp). On Long, attention cliffs $-$26.5\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\ref{fig:cliff_highlight}).
106	
107	\textbf{Inverted-U importance margin.} On $\pi_{0.5}$ Long, $\Delta$ peaks at $k{=}0.9$ ($+$46.8\,pp), diminishes at $k{=}0.95$ ($+$25.6\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\,pp) where both are inadequate. Near $k{\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\ref{fig:cliff_highlight}; Appendix Figure~\ref{fig:margin_profile}).
108	
109	\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\pi_{0.5}$ at $k{=}0.85$: Object $\Delta{=}+$92.4\,pp $>$ Goal $+$35.2\,pp $>$ Long $+$33.2\,pp (Appendix Table~\ref{tab:full_results}).
110	
111	\subsection{VTR Recovery}
112	\label{sec:vtr_recovery}
113	
114	\begin{table}[t]
115	\centering
116	\small
117	\caption{VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0\%; VTR exceeds the unpruned baseline at up to 87.5\% compression. Baseline (44.8\%) is our Low-Rank Adaptation (LoRA) reproduction; official checkpoint achieves 59.2\% (Table~\ref{tab:main_results}).}
118	\label{tab:vtr_main}
119	\begin{tabular}{lccr}
120	\toprule
121	Configuration & $M$ & Compress.\ & SR (\%) \\
122	\midrule
123	\textit{Baseline (unpruned)} & 128 & 0\% & 44.8 \\
124	\textit{Hard pruning (any)} & -- & 5--50\% & 0.0 \\
125	\midrule
126	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
127	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
128	MLP adapter & 32 & 75\% & 63.4 $\pm$ 2.6 \\
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\sim}$22M parameters, $<$5\% of SmolVLA). At 75\% compression, VTR achieves 60.1 $\pm$ 1.3\% SR ($M{=}32$, $n{=}3$; Table~\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\%) by 15.3\,pp. An extended training control rules out additional optimization as the source ($p > 0.9$; Appendix~\ref{app:smart_compress_details}). A parameter-matched MLP adapter achieves 63.4 $\pm$ 2.6\% ($p{=}0.15$), indicating the benefit stems from re-encoding rather than the specific cross-attention mechanism. This suggests the key ingredient is providing a learnable interface between the entangled connector output and the LLM input, allowing the model to reconstruct a compressed representation that respects the LLM's positional expectations.
134	
135	Performance scales gracefully with compression: reducing $M$ from 32 to 16 (87.5\% compression) costs only 3.2\,pp, while still exceeding the unpruned baseline by 12.1\,pp. Cross-suite generalization confirms the learned compression transfers: Spatial recovers to 53.2\% and Goal to 56.4\%, both from 0.0\% under hard pruning, without suite-specific training. For $\pi_{0.5}$, $k{=}0.9$ with L2 scoring cuts attention FLOPs by ${\sim}$16\% while preserving full SR, requiring no additional parameters.
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "d20897fa-2e58-4876-bd72-ec7d9b0afd3f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean SR over 500 episodes. Multi-seed results ($\\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\\pm$ s.d.\\ with per-seed breakdowns in the appendix.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp (percentage points) method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 1.4\\,pp, yet the same model drops 28.2\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 7 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop SR (\\%) on LIBERO under L2 norm (L2) and random (R) pruning. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 99.2 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.49\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\n\\label{fig:pixel_shuffle}\n\\end{subfigure}\\hfill%\n\\begin{subfigure}[t]{0.49\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\n\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{(a)~Pixel-shuffle $4{\\times}4$ entanglement: each 16-patch block forms one token; removing any eliminates a non-overlapping receptive field with no redundancy. (b)~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_and_gap}\n\\end{figure*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\\ref{app:smolvla_ablation}). Notably, X-VLA's BART encoder is also entangling, yet far more robust: its 12-layer self-attention redistributes information across tokens, creating inter-token redundancy that buffers against removal. Pixel-shuffle performs a fixed deterministic fold with no learned information sharing---each output token's receptive field is disjoint, leaving zero redundancy for pruning to exploit.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method cliff behavior on $\\pi_{0.5}$ Long ($n{=}5$, mean $\\pm$ s.d.). L2 degrades monotonically; attention cliffs at $k{=}0.85$; random V-shapes with collapse at $k{=}0.9$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. On $\\pi_{0.5}$, the 89\\,pp gap is entirely attributable to position disruption: its linear connector tolerates complete signal destruction but not index shifts. This ablation targets $\\pi_{0.5}$ because its Rotary Position Embedding (RoPE)-based position encoding is most susceptible to re-indexing; other connectors use different positional mechanisms.\n\nThis has practical implications: for position-sensitive architectures, any compression that alters the sequence length will disrupt positional encodings. Strategies for such models must either preserve the original length (e.g., zero-masking) or include position-aware mechanisms that compensate for index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$31.6\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.8\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$92.4\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results}).\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0\\%; VTR exceeds the unpruned baseline at up to 87.5\\% compression. Baseline (44.8\\%) is our Low-Rank Adaptation (LoRA) reproduction; official checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}).}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, $<$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, $n{=}3$; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control rules out additional optimization as the source ($p > 0.9$; Appendix~\\ref{app:smart_compress_details}). A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), indicating the benefit stems from re-encoding rather than the specific cross-attention mechanism. This suggests the key ingredient is providing a learnable interface between the entangled connector output and the LLM input, allowing the model to reconstruct a compressed representation that respects the LLM's positional expectations.\n\nPerformance scales gracefully with compression: reducing $M$ from 32 to 16 (87.5\\% compression) costs only 3.2\\,pp, while still exceeding the unpruned baseline by 12.1\\,pp. Cross-suite generalization confirms the learned compression transfers: Spatial recovers to 53.2\\% and Goal to 56.4\\%, both from 0.0\\% under hard pruning, without suite-specific training. For $\\pi_{0.5}$, $k{=}0.9$ with L2 scoring cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR, requiring no additional parameters.\n",
      "numLines": 136,
      "startLine": 1,
      "totalLines": 136
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01NL1hpWBTUcCCXYA7GLReeY`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "a1a23690-af53-4f64-b502-a71435ff2d4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 26 · 2026-05-29T06:29:44.056Z_

<details><summary>↩ Tool result · `toolu_01NL1hpWBTUcCCXYA7GLReeY`</summary>

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
38	The pattern generalizes across LIBERO suites: Spatial 0.6\%, Goal 0\%. Pixel-shuffle folds each $4{\times}4$ patch block into a single token by channel concatenation; removing one token eliminates an entire $4{\times}4$ receptive field. The resulting spatial entanglement means even 5\% removal ($k{=}0.95$, losing 7 of 128 tokens) destroys task-critical visual information. Full ablation results appear in Table~\ref{tab:smolvla_ablation}, Appendix~\ref{app:smolvla_ablation}.
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
125	The cliff zone exhibits a suite $\times$ method interaction: at $k \in [0.85, 0.95]$, Object tasks collapse under random removal while Spatial tasks degrade gracefully (Figure~\ref{fig:crosssuite}, Table~\ref{tab:pi05_crosssuite}). L2 norm maintains a near-baseline plateau on both suites ($\leq 2.4$\,pp at $k \geq 0.85$). CV$\,{=}\,$0.055 correctly predicts this plateau on both suites despite qualitatively different cliff profiles, confirming CV as a model-level diagnostic. Token importance heatmaps reveal a center-high, edge-low spatial pattern (Figure~\ref{fig:token_heatmap}, Appendix~\ref{app:token_heatmap}), formalized by a hypergeometric model $H(N{=}768,\, C{=}106,\, T{=}7)$: cliff onset at $k{=}0.96$ (10\% collapse probability) narrows to $k{=}0.90$ (90\%), RMSE${=}$0.018 (Appendix~\ref{app:cliff_model}). The model captures onset sharpness at high retention but does not generalize to moderate retention ($k \leq 0.7$), where compensatory mechanisms may emerge (\S\ref{sec:analysis}). The cross-suite difference is driven by Object's concentrated criticality ($C{=}106$) versus Spatial's distributed pattern ($C \approx 5$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "a28ecdf2-488a-49ae-8411-b92b0b5049d0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\n\n\\subsection{Taxonomy Overview}\n\\label{sec:taxonomy_overview}\n\nTable~\\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, is strongly associated with pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\\sim$0.15, smooth graded at $\\sim$0.22, and catastrophic cliff at $>$0.3. A pairwise comparison between $\\pi_0$ and OpenVLA (both consuming 256 SigLIP-based~\\cite{zhai2023siglip} tokens but differing in connector, backbone, and encoder fusion) yields a 63\\,pp gap at $k{=}0.1$; this gap is consistent with the monotonic CV-degradation pattern across all seven models (Section~\\ref{sec:linear_results}).\n\nThe four classes differ qualitatively in their failure mode. Uniformly critical models ($\\pi_0$, $\\pi_0.5$~\\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\\dagger\\pi_0$: offline metrics only, no closed-loop evaluation; the 63\\,pp gap vs.\\ OpenVLA at $k{=}0.1$ mixes offline loss with closed-loop SR. $^\\ddagger$X-VLA uses a linear projection followed by a 12-layer BART encoder; the effective pipeline is not purely linear. $^\\S$OFT reports attention entropy and CV only (no pruning evaluation); both metrics match OpenVLA, consistent with the connector being associated with token importance structure. $^\\|$CogACT: literature result from EfficientVLA~\\cite{yang2025efficientvla}, not our evaluation.}\n\\label{tab:taxonomy}\n\\begin{tabular}{llcrcll}\n\\toprule\nModel & Connector & Params & Tokens & CV & Representative Result & Class \\\\\n\\midrule\n$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\n$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\nX-VLA~\\cite{zheng2025xvla} & Linear + BART (12L)$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.9{\\pm}0.3$ & Threshold-graded \\\\\nOpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\nOFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\nCogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\nSmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle: Catastrophic Cliff-Edge}\n\\label{sec:smolvla_results}\n\nThe SmolVLA baseline (bypass mode, all 128 vision tokens) achieves 44.8\\% SR (224/500, CI [40.5\\%, 49.2\\%]).\\footnote{The official SmolVLA result is 87.3\\% SR with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch due to compute constraints.} Every pruning configuration produces 0\\% SR across seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.50, 0.70, 0.90, 0.95\\}$), and mechanism (zero-masking, true removal, token merging). The cliff persists regardless of checkpoint quality: the official SmolVLA HF checkpoint (57.2\\%--59.2\\% SR across two evaluation protocols; Appendix~\\ref{app:smolvla_ablation}) also collapses to 0\\% under random $k{=}0.95$ (5\\% removal), L2 norm $k{=}0.9$ (10\\% removal), and L2 norm $k{=}0.5$ (Table~\\ref{tab:smolvla_ablation}). The failure is architectural, not a training artifact.\n\nThe pattern generalizes across LIBERO suites: Spatial 0.6\\%, Goal 0\\%. Pixel-shuffle folds each $4{\\times}4$ patch block into a single token by channel concatenation; removing one token eliminates an entire $4{\\times}4$ receptive field. The resulting spatial entanglement means even 5\\% removal ($k{=}0.95$, losing 7 of 128 tokens) destroys task-critical visual information. Full ablation results appear in Table~\\ref{tab:smolvla_ablation}, Appendix~\\ref{app:smolvla_ablation}.\n\n\\subsection{MLP Projector: Smooth Graded Degradation}\n\\label{sec:openvla_results}\n\nUnder random token removal, OpenVLA degrades gracefully across all retention ratios: 74.0\\% (baseline) $\\rightarrow$ 69.4\\% at $k{=}0.95$ ($-4.6$\\,pp) $\\rightarrow$ 62.0\\% at $k{=}0.90$ $\\rightarrow$ 49.0\\% at $k{=}0.70$ $\\rightarrow$ 37.4\\% at $k{=}0.50$ $\\rightarrow$ 20.6\\% at $k{=}0.30$ (Figure~\\ref{fig:degradation_curve}; full results with CIs in Table~\\ref{tab:openvla_full}, Appendix).\\footnote{A second random seed confirms the graded pattern: 62.2\\% at $k{=}0.9$ ($+$0.2\\,pp), 44.4\\% at $k{=}0.7$ ($-$4.6\\,pp), 35.6\\% at $k{=}0.5$ ($-$1.8\\,pp). All within 5\\,pp of the primary seed. Per-seed details in Table~\\ref{tab:openvla_multiseed}, Appendix~\\ref{app:openvla_multiseed}.} At $k{=}0.30$, two tasks reach 0\\% SR, but eight retain non-zero performance: degradation is graded, not cliff-edge. Random token removal provides a conservative lower bound on architectural resilience; learned scoring methods would likely yield better retention.\n\nOFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\n\nTo control for scoring method in cross-architecture comparisons, we evaluate L2 norm-based selection on OpenVLA. At moderate-to-aggressive retention ($k \\leq 0.7$), L2 performs within 2--6\\,pp of random removal\\footnote{OpenVLA random results use seed$\\,{=}\\,$7; L2 norm results use seed$\\,{=}\\,$42. Same-seed (seed42) gaps: 5.4\\,pp at $k{=}0.7$, 3.6\\,pp at $k{=}0.3$ (21.4\\% random vs.\\ 25.0\\% L2); same-seed at $k{=}0.5$: 35.8\\% random vs.\\ 39.2\\% L2 (gap 3.4\\,pp).} (Table~\\ref{tab:openvla_l2_vs_random}, Appendix~\\ref{app:l2_vs_random}). At $k{=}0.9$, L2 outperforms random by 8.6\\,pp (70.6\\% vs.\\ 62.0\\%, reproducible across two random seeds), consistent with the weak but non-zero importance gradient predicted by CV$\\,{=}\\,$0.215: the signal is exploitable only when few tokens are removed.\n\n\\subsection{Linear Projection: From Uniformly Critical to Threshold-Graded}\n\\label{sec:linear_results}\n\nThree models share a linear projection connector yet exhibit qualitatively different pruning responses. The divergence traces to what happens \\emph{after} the projection: nothing ($\\pi_0$), a learned scaling ($\\pi_0.5$), or a full 12-layer encoder (X-VLA).\n\n\\paragraph{$\\pi_0$ (3.3B, 256 tokens, pure linear).} Offline normalized L1 action loss at $k{=}0.1$ is 0.976, a 2.4\\% \\emph{improvement} over the unpruned baseline.\\footnote{Offline action loss measures single-step prediction quality; closed-loop evaluation may reveal additional degradation.} CV$\\,{=}\\,$0.038 indicates near-uniform token norms. Near-uniform L2 norms (CV$\\,{=}\\,$0.038) suggest that no token subset carries disproportionate information, so random removal approximates uniform spatial downsampling and the model compensates.\n\n\\paragraph{$\\pi_0.5$ (4B, 768 tokens, linear $\\times\\!\\sqrt{d}$).} The baseline achieves 98.2\\% SR. This model reveals that low CV does not imply tokens are dispensable; it implies uniform criticality. The response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\\% SR ($-$28.8\\,pp), while L2 norm-based removal at the same ratio collapses to 33.4\\% ($-$64.8\\,pp). The gap of 36\\,pp is the largest method-dependent effect at $k{=}0.5$ in our study.\n\nAt $k \\leq 0.7$, random removal degrades monotonically (77.2\\%, 69.4\\%, 36.4\\% at $k{=}0.7, 0.5, 0.3$; seed43 within 1\\,pp). At higher retention, a task-specific random cliff emerges on LIBERO-Object: SR drops from 69.4\\% ($k{=}0.95$) to 5.0\\% ($k{=}0.85$) before recovering to 77.2\\% ($k{=}0.7$), a 72\\,pp swing; the same $k{=}0.85$ on LIBERO-Spatial retains 58.4\\% (Appendix~\\ref{app:pi05_crosssuite}). L2 norm selection produces a V-shaped curve: 55.0\\% at $k{=}0.7$, 33.4\\% at $k{=}0.5$ (the valley), 51.0\\% at $k{=}0.3$, confirmed across two seeds ($\\sigma = 0.1$\\,pp at the valley).\\footnote{V-shape valley at $k{=}0.5$: 33.4\\% (seed42) vs.\\ 33.6\\% (seed43), $\\sigma{=}0.1$\\,pp. V-depth: 17.6\\,pp (seed42), 21.8\\,pp (seed43). Full multi-seed table in Appendix~\\ref{app:pi05_multiseed}.} The non-monotonic L2 pattern arises because norm ranking in a low-CV distribution selects spatially clustered tokens (slight norm variations correlate with image regions), and the resulting loss of spatial coverage peaks at intermediate budgets.\n\nThis result demonstrates that models showing offline pruning tolerance can exhibit severe closed-loop degradation. Low-CV tokens are uniformly critical, not uniformly dispensable. L2 norm-based selection systematically concentrates on spatially correlated tokens and loses coverage; random selection preserves the uniform spatial distribution that these architectures require.\n\n\\paragraph{X-VLA (880M, 50 tokens, linear + 12-layer BART).} The 99.2\\% baseline is maintained at $k{=}0.95$ ($99.1 \\pm 0.2$\\%, 3 seeds) and $k{=}0.9$ ($97.8 \\pm 0.4$\\%) under L2 norm-based removal. A sharp cliff appears at $k{=}0.85$ ($67.9 \\pm 0.3$\\%, $-$31\\,pp, 3 seeds), with non-monotonic recovery at $k{=}0.80$ ($89.0 \\pm 0.7$\\%, 3 seeds) before degradation resumes: $58.6 \\pm 0.4$\\% at $k{=}0.7$, $43.4 \\pm 0.8$\\% at $k{=}0.5$, $22.0 \\pm 0.9$\\% at $k{=}0.3$, $4.7 \\pm 0.6$\\% at $k{=}0.2$, and near-zero at $k{=}0.1$. The cliff at $k{=}0.85$ (retaining 42 of 50 BART-encoded tokens) is reproducible across seeds (std $\\leq$ 1.6\\,pp). The non-monotonic dip is task-specific: four tasks lose $\\sim$50\\,pp each while six remain unaffected (Table~\\ref{tab:xvla_cliff_pertask}, Appendix~\\ref{app:xvla_cliff}). Under random removal, X-VLA exhibits a plateau: $65.1 \\pm 0.1$\\% at $k{=}0.7$ and $64.0 \\pm 1.6$\\% at $k{=}0.3$ (3 seeds each), confirming that L2 norm-based selection ($22.0 \\pm 0.9$\\% at $k{=}0.3$) is far more destructive than random for this intermediate-CV architecture.\n\nThat this threshold appears under importance-based removal (the more favorable test) while OpenVLA degrades smoothly under random removal (the harder test) strengthens the architecture-dependent conclusion. The $\\pi_0$--OpenVLA comparison (both consuming 256 SigLIP-based tokens, differing in connector, backbone, and encoder fusion) produces a 63\\,pp gap at $k{=}0.1$, consistent with the connector-associated pattern observed across all seven models. This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation.\n\n\\subsection{VTR: Re-Encoding Overcomes Cliff-Edge}\n\\label{sec:smart_compress_results}\n\nTo test whether learned re-encoding can overcome the pixel-shuffle cliff-edge, we insert a 22.2M-parameter cross-attention module (Vision Token Re-encoder, VTR) between the vision connector and the LLM backbone (details in Appendix~\\ref{app:smart_compress_details}). VTR compresses 128 input tokens to $M$ output tokens. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR ($p > 0.9$ vs.\\ the 44.8\\% baseline); the gain is architectural, not from additional optimization steps.\\footnote{The extended baseline also collapses to 0\\% SR under pruning ($k{=}0.50$, random, true removal). Additional training does not mitigate the pixel-shuffle vulnerability.}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding vs.\\ deletion on SmolVLA (LIBERO-Object). The M-curve is relatively stable: $M{=}16$ (87.5\\% compression) matches $M{=}128$ (no compression) within 1.1\\,pp. A parameter-matched MLP adapter achieves comparable SR ($p = 0.15$ vs.\\ cross-attention). $^\\ddagger$Mean $\\pm$ std over 3 seeds (500 episodes each). Other rows: single seed with Wilson 95\\% CI.}\n\\label{tab:smart_compress}\n\\begin{tabular}{lccrr}\n\\toprule\nMethod & $M$ & Red. & SR (\\%) & Seeds \\\\\n\\midrule\n\\textit{Baseline} & 128 & 0\\% & 44.8 & 1 \\\\\n\\textit{Ext.\\ training} & -- & -- & 45.0 & 1 \\\\\n\\textit{Hard pruning} & -- & 50--90\\% & 0.0 & mult. \\\\\n\\midrule\nCross-attn$^\\ddagger$ & 16 & 87.5\\% & 56.9$\\pm$1.3 & 55.8/58.4/56.5 \\\\\nCross-attn$^\\ddagger$ & 32 & 75\\% & 60.1$\\pm$1.3 & 61.6/59.2/59.6 \\\\\nCross-attn$^\\ddagger$ & 64 & 50\\% & \\textbf{62.0}$\\pm$2.3 & 61.6/60.0/64.4 \\\\\nCross-attn$^\\ddagger$ & 96 & 25\\% & 54.5$\\pm$3.2 & 52.6/58.2/52.8 \\\\\nCross-attn$^\\ddagger$ & 128 & 0\\% & 58.0$\\pm$3.5 & 59.8/54.0/60.2 \\\\\nMLP adapter$^\\ddagger$ & 32 & 75\\% & 63.4$\\pm$2.6 & 65.2/64.6/60.4 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Official checkpoint (59.2\\% baseline)}} \\\\\nCross-attn & 32 & 75\\% & 53.4 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe M-curve is relatively stable (Table~\\ref{tab:smart_compress}): $M{=}16$ (56.9\\%, 87.5\\% compression) performs within 1.1\\,pp of $M{=}128$ (58.0\\%, no compression). A parameter-matched MLP adapter achieves 63.4\\% $\\pm$ 2.6 at $M{=}32$ ($p = 0.15$ vs.\\ cross-attention; Figure~\\ref{fig:compression_curve}). Cross-suite evaluation confirms generalization: 53.2\\% on LIBERO-Spatial and 56.4\\% on LIBERO-Goal where hard pruning yields 0\\% (Appendix~\\ref{app:smart_compress_full}). VTR applied to OpenVLA yields 0\\% SR even in passthrough mode: it is a targeted remedy for pixel-shuffle entanglement.\n\n\\subsection{CV Correlates with Optimal Pruning Strategy}\n\\label{sec:scaling_law}\n\nToken importance CV correlates with both pruning tolerance and optimal strategy. Comparing L2 norm-based and random removal across three models, the gap $\\Delta$(R$-$L2) decreases monotonically with CV at both $k{=}0.5$ and $k{=}0.7$ (full data in Table~\\ref{tab:scaling_law}, Appendix~\\ref{app:cv_scaling_table}). At $k{=}0.5$: $+$36.0\\,pp ($\\pi_0.5$, CV$\\,{=}\\,$0.055) $\\rightarrow$ $+$26.9\\,pp (X-VLA, CV$\\,{=}\\,$0.151) $\\rightarrow$ $-$1.8\\,pp (OpenVLA, CV$\\,{=}\\,$0.215). At $k{=}0.7$: $+$22.2\\,pp $\\rightarrow$ $+$6.5\\,pp $\\rightarrow$ $-$5.4\\,pp. The monotonic ordering holds across a 2$\\times$ change in token budget, indicating CV captures a structural property of the connector. Below CV $\\approx 0.15$, L2 ranking captures spatial artifacts rather than importance; above it, importance-based scoring becomes beneficial (reversal at $k{=}0.3$; Appendix~\\ref{app:cv_strategy_interaction}).\n\n\\begin{figure}[t]\n\\centering\n\\begin{subfigure}[b]{0.48\\linewidth}\n\\includegraphics[width=\\linewidth]{figures/paper/fig_degradation_curve.pdf}\n\\caption{Token pruning across connector classes.}\n\\label{fig:degradation_curve}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[b]{0.48\\linewidth}\n\\includegraphics[width=\\linewidth]{figures/paper/fig_compression_curve.pdf}\n\\caption{VTR M-curve and CV-strategy interaction.}\n\\label{fig:compression_curve}\n\\end{subfigure}\n\\caption{Token reduction on LIBERO-Object. (a)~Pruning: linear ($\\pi_0$) uniformly critical, linear+encoder (X-VLA) threshold-graded, MLP (OpenVLA) smooth, pixel-shuffle (SmolVLA) collapses. (b)~VTR: $M{=}16 \\approx M{=}128$ where deletion yields 0\\%; CV-gap monotonic.}\n\\label{fig:results_combined}\n\\end{figure}\n\n\\enlargethispage{2\\baselineskip}\n\\subsection{Cross-Suite Generalization}\n\\label{sec:cross_suite}\n\nThe cliff zone exhibits a suite $\\times$ method interaction: at $k \\in [0.85, 0.95]$, Object tasks collapse under random removal while Spatial tasks degrade gracefully (Figure~\\ref{fig:crosssuite}, Table~\\ref{tab:pi05_crosssuite}). L2 norm maintains a near-baseline plateau on both suites ($\\leq 2.4$\\,pp at $k \\geq 0.85$). CV$\\,{=}\\,$0.055 correctly predicts this plateau on both suites despite qualitatively different cliff profiles, confirming CV as a model-level diagnostic. Token importance heatmaps reveal a center-high, edge-low spatial pattern (Figure~\\ref{fig:token_heatmap}, Appendix~\\ref{app:token_heatmap}), formalized by a hypergeometric model $H(N{=}768,\\, C{=}106,\\, T{=}7)$: cliff onset at $k{=}0.96$ (10\\% collapse probability) narrows to $k{=}0.90$ (90\\%), RMSE${=}$0.018 (Appendix~\\ref{app:cliff_model}). The model captures onset sharpness at high retention but does not generalize to moderate retention ($k \\leq 0.7$), where compensatory mechanisms may emerge (\\S\\ref{sec:analysis}). The cross-suite difference is driven by Object's concentrated criticality ($C{=}106$) versus Spatial's distributed pattern ($C \\approx 5$).",
      "numLines": 125,
      "startLine": 1,
      "totalLines": 125
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_016Xp1xbh8mA85N3KEKFsAur`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "c228942a-67ba-4381-931e-508637924019",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 28 · 2026-05-29T06:29:45.067Z_

<details><summary>↩ Tool result · `toolu_016Xp1xbh8mA85N3KEKFsAur`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, determines pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A controlled comparison between $\pi_0$ and OpenVLA (both using 256 SigLIP~\cite{zhai2023siglip} tokens, differing only in connector) yields a 63\,pp gap at $k{=}0.1$, isolating the pipeline as causal (Section~\ref{sec:linear_results}).
10	
11	The four classes differ qualitatively in their failure mode. Uniformly critical models ($\pi_0$, $\pi_0.5$~\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.
12	
13	\begin{table*}[t]
14	\centering
15	\small
16	\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\dagger\pi_0$ reports offline normalized L1 action loss (pending closed-loop evaluation). $^\ddagger$X-VLA uses a linear projection followed by a 12-layer BART encoder; the effective pipeline is not purely linear. $^\S$OFT reports attention entropy and CV only (no pruning evaluation); both metrics match OpenVLA, which confirms the connector determines token importance structure. $^\|$CogACT result from EfficientVLA~\cite{yang2025efficientvla} (literature corroboration, not our evaluation).}
17	\label{tab:taxonomy}
18	\begin{tabular}{llcrcll}
19	\toprule
20	Model & Connector & Params & Tokens & CV & Representative Result & Class \\
21	\midrule
22	$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
23	$\pi_0.5$~\cite{black2025pi05} & Linear proj ($\times\!\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\%, R$=$69.4\% ($\Delta{=}$+36pp) & Uniformly critical \\
24	X-VLA~\cite{zheng2025xvla} & Linear proj$^\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\pm}0.4$, $k{=}0.85$: $67.8$ & Threshold-graded \\
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
36	The SmolVLA baseline (bypass mode, all 128 vision tokens) achieves 44.8\% SR (224/500, CI [40.5\%, 49.2\%]).\footnote{The official SmolVLA result is 87.3\% SR with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch due to compute constraints.} Every pruning configuration produces 0\% SR across seven configurations varying scoring (learned ACIS vs.\ random), retention ratio ($k \in \{0.50, 0.70, 0.90, 0.95\}$), and mechanism (zero-masking, true removal, token merging). The official SmolVLA checkpoint (59.2\% SR) exhibits identical failure; the cliff-edge is architectural, not a training artifact.
37	
38	The pattern generalizes across LIBERO suites: Spatial 0.6\%, Goal 0\%. Pixel-shuffle folds each $4{\times}4$ patch block into a single token by channel concatenation; removing one token eliminates an entire $4{\times}4$ receptive field. The resulting spatial entanglement means even 5\% removal ($k{=}0.95$, losing 7 of 128 tokens) destroys task-critical visual information. Full ablation results appear in Table~\ref{tab:smolvla_ablation}, Appendix~\ref{app:smolvla_ablation}.
39	
40	\subsection{MLP Projector: Smooth Graded Degradation}
41	\label{sec:openvla_results}
42	
43	Under random token removal, OpenVLA degrades gracefully across all retention ratios: 74.0\% (baseline) $\rightarrow$ 69.4\% at $k{=}0.95$ ($-4.6$\,pp) $\rightarrow$ 62.0\% at $k{=}0.90$ $\rightarrow$ 49.0\% at $k{=}0.70$ $\rightarrow$ 37.4\% at $k{=}0.50$ $\rightarrow$ 20.6\% at $k{=}0.30$ (Figure~\ref{fig:degradation_curve}; full results with CIs in Table~\ref{tab:openvla_full}, Appendix).\footnote{A second random seed confirms the graded pattern: 62.2\% at $k{=}0.9$ ($+$0.2\,pp), 52.6\% at $k{=}0.7$ ($+$3.6\,pp), 35.6\% at $k{=}0.5$ ($-$1.8\,pp). All within 4\,pp of the primary seed. Per-seed details in Table~\ref{tab:openvla_multiseed}, Appendix~\ref{app:openvla_multiseed}.} At $k{=}0.30$, two tasks reach 0\% SR, but eight retain non-zero performance: degradation is graded, not cliff-edge. Random token removal provides a conservative lower bound on architectural resilience; learned scoring methods would likely yield better retention.
44	
45	OFT~\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, determines token importance structure. EfficientVLA~\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\cite{li2024cogact} (MLP projector) retains 74.2\% SR under 78\% pruning.
46	
47	To control for scoring method in cross-architecture comparisons, we evaluate L2 norm-based selection on OpenVLA. At moderate-to-aggressive retention ($k \leq 0.7$), L2 performs within 2--4\,pp of random removal (Table~\ref{tab:openvla_l2_vs_random}, Appendix~\ref{app:l2_vs_random}). At $k{=}0.9$, L2 outperforms random by 8.5\,pp (70.6\% vs.\ 62.0\%, reproducible across two random seeds), consistent with the weak but non-zero importance gradient predicted by CV$\,{=}\,$0.215: the signal is exploitable only when few tokens are removed.
48	
49	\subsection{Linear Projection: From Uniformly Critical to Threshold-Graded}
50	\label{sec:linear_results}
51	
52	Three models share a linear projection connector yet exhibit qualitatively different pruning responses. The divergence traces to what happens \emph{after} the projection: nothing ($\pi_0$), a learned scaling ($\pi_0.5$), or a full 12-layer encoder (X-VLA).
53	
54	\paragraph{$\pi_0$ (3.3B, 256 tokens, pure linear).} Offline normalized L1 action loss at $k{=}0.1$ is 0.976, a 2.4\% \emph{improvement} over the unpruned baseline.\footnote{Offline action loss measures single-step prediction quality; closed-loop evaluation may reveal additional degradation.} CV$\,{=}\,$0.038 indicates near-uniform token norms. Because all tokens carry equal weight, removing 90\% at random preserves spatial coverage and the model compensates.
55	
56	\paragraph{$\pi_0.5$ (4B, 768 tokens, linear $\times\!\sqrt{d}$).} The baseline achieves 98.2\% SR. This model reveals that low CV does not imply pruning immunity; it implies uniform criticality. The response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\% SR ($-$28.8\,pp), while L2 norm-based removal at the same ratio collapses to 33.4\% ($-$64.8\,pp). The gap of 36\,pp is the largest method-dependent effect in our study.
57	
58	Random removal produces monotonic degradation: 77.2\% at $k{=}0.7$, 69.4\% at $k{=}0.5$, 36.4\% at $k{=}0.3$. L2 norm selection instead produces a V-shaped curve: 55.0\% at $k{=}0.7$, 33.4\% at $k{=}0.5$ (the valley), 51.0\% at $k{=}0.3$. The non-monotonic L2 pattern arises because norm ranking in a low-CV distribution selects spatially clustered tokens (slight norm variations correlate with image regions), and the resulting loss of spatial coverage peaks at intermediate budgets. A second random seed (seed43) confirms the random result: 68.4\% at $k{=}0.5$ ($\Delta{=}$1.0\,pp from seed42).
59	
60	This result falsifies the ``immune'' assumption from the $\pi_0$ offline evaluation. Low-CV tokens are uniformly critical, not uniformly dispensable. L2 norm-based selection systematically concentrates on spatially correlated tokens and loses coverage; random selection preserves the uniform spatial distribution that these architectures require.
61	
62	\paragraph{X-VLA (880M, 50 tokens, linear + 12-layer BART).} The 99.2\% baseline is maintained at $k{=}0.95$ ($99.1 \pm 0.2$\%, 3 seeds) and $k{=}0.9$ ($97.8 \pm 0.4$\%) under L2 norm-based removal. A sharp cliff appears at $k{=}0.85$ (67.8\%, $-$30\,pp, 2 seeds), with non-monotonic recovery at $k{=}0.80$ (88.6\%) before degradation resumes: $57.2 \pm 1.6$\% at $k{=}0.7$, $43.4 \pm 0.8$\% at $k{=}0.5$, $22.3 \pm 1.1$\% at $k{=}0.3$, $4.7 \pm 0.6$\% at $k{=}0.2$, and near-zero at $k{=}0.1$. The cliff at $k{=}0.85$ (retaining 42 of 50 BART-encoded tokens) is reproducible across seeds (std $\leq$ 1.6\,pp). The non-monotonic dip is task-specific: four tasks lose $\sim$50\,pp each while six remain unaffected (Table~\ref{tab:xvla_cliff_pertask}, Appendix~\ref{app:xvla_cliff}).
63	
64	That this threshold appears under importance-based removal (the more favorable test) while OpenVLA degrades smoothly under random removal (the harder test) strengthens the architecture-dependent conclusion. The $\pi_0$--OpenVLA controlled comparison (same 256 SigLIP tokens, same encoder lineage, differing only in connector) produces a 63\,pp gap at $k{=}0.1$, isolating the connector pipeline as the causal factor.
65	
66	\subsection{VTR: Re-Encoding Overcomes Cliff-Edge}
67	\label{sec:smart_compress_results}
68	
69	To test whether learned re-encoding can overcome the pixel-shuffle cliff-edge, we insert a 22.2M-parameter cross-attention module (Vision Token Re-encoder, VTR) between the vision connector and the LLM backbone (details in Appendix~\ref{app:smart_compress_details}). VTR compresses 128 input tokens to $M$ output tokens. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\% SR ($p > 0.9$ vs.\ the 44.8\% baseline); the gain is architectural, not from additional optimization steps.\footnote{The extended baseline also collapses to 0\% SR under pruning ($k{=}0.50$, random, true removal). Additional training does not mitigate the pixel-shuffle vulnerability.}
70	
71	\begin{table}[t]
72	\centering
73	\small
74	\caption{VTR re-encoding vs.\ deletion on SmolVLA (LIBERO-Object). The M-curve is flat: $M{=}16$ (87.5\% compression) matches $M{=}128$ (no compression) within 1.1\,pp. A parameter-matched MLP adapter achieves comparable SR ($p = 0.15$ vs.\ cross-attention). $^\ddagger$Mean $\pm$ std over 3 seeds (500 episodes each). Other rows: single seed with Wilson 95\% CI.}
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
97	The M-curve is flat (Table~\ref{tab:smart_compress}): $M{=}16$ (56.9\%, 87.5\% compression) performs within 1.1\,pp of $M{=}128$ (58.0\%, no compression), and all five $M$ values cluster within 5\,pp. A parameter-matched MLP adapter (22.14M parameters) achieves 63.4\% $\pm$ 2.6 at $M{=}32$ ($p = 0.15$ vs.\ cross-attention); re-encoding itself, not the attention mechanism, is the operative factor (Figure~\ref{fig:compression_curve}). Cross-suite evaluation confirms generalization: 53.2\% on LIBERO-Spatial and 56.4\% on LIBERO-Goal where hard pruning yields 0\% (Appendix~\ref{app:smart_compress_full}). VTR applied to OpenVLA yields 0\% SR even in passthrough mode ($M{=}128$): it is a targeted remedy for pixel-shuffle entanglement, not a universal compression module.
98	
99	\subsection{CV Predicts Optimal Pruning Strategy}
100	\label{sec:scaling_law}
101	
102	The preceding sections establish that connector architecture determines pruning tolerance. A natural follow-up: can a single diagnostic predict not only \emph{how much} pruning a model tolerates, but also \emph{which} pruning strategy to use? Token importance CV provides exactly this dual prediction. Table~\ref{tab:scaling_law} compares L2 norm-based and random removal at two retention ratios ($k{=}0.5$ and $k{=}0.7$) across three models with measured CV.
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\caption{L2 norm vs.\ random removal at two retention ratios. The gap $\Delta$(R$-$L2) scales monotonically with CV at both $k{=}0.5$ and $k{=}0.7$: low-CV models require random selection (uniform importance $\rightarrow$ L2 degenerates to spatial clustering), while high-CV models tolerate either strategy. The monotonic ordering holds across retention ratios despite a 2$\times$ change in token budget.}
108	\label{tab:scaling_law}
109	\begin{tabular}{lccccc}
110	\toprule
111	Model & CV & Tokens & L2 SR (\%) & Random SR (\%) & $\Delta$(R$-$L2) \\
112	\midrule
113	\multicolumn{6}{l}{\textit{$k{=}0.5$ (50\% retention)}} \\
114	$\pi_0.5$ & 0.055 & 768 & 33.4 & \textbf{69.4} & $+$36.0 \\
115	X-VLA & 0.151 & 50 & 43.4$\pm$0.8 & \textbf{70.3}$\pm$0.9 & $+$26.9 \\
116	OpenVLA & 0.215 & 256 & 39.2 & 35.8 & $-$3.4 \\
117	\midrule
118	\multicolumn{6}{l}{\textit{$k{=}0.7$ (70\% retention)}} \\
119	$\pi_0.5$ & 0.055 & 768 & 55.0 & \textbf{77.2} & $+$22.2 \\
120	X-VLA & 0.151 & 50 & 57.2$\pm$1.6 & \textbf{64.2} & $+$7.0 \\
121	OpenVLA & 0.215 & 256 & \multicolumn{3}{c}{\textit{pending}} \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	The gap decreases monotonically as CV increases at both retention ratios. At $k{=}0.5$: $+$36.0\,pp ($\pi_0.5$, CV$\,{=}\,$0.055) $\rightarrow$ $+$26.9\,pp (X-VLA, CV$\,{=}\,$0.151) $\rightarrow$ $-$3.4\,pp (OpenVLA, CV$\,{=}\,$0.215). At $k{=}0.7$: $+$22.2\,pp $\rightarrow$ $+$7.0\,pp $\rightarrow$ pending. The monotonic ordering holds across a 2$\times$ change in absolute token budget, strengthening the claim that CV captures a structural property of the connector rather than a coincidence at a single operating point.
127	
128	The mechanism is intuitive. When tokens have near-uniform L2 norms (low CV), norm ranking captures spatial artifacts rather than genuine importance differences. L2 norm-based selection then clusters on correlated patches and loses spatial coverage, while random selection preserves the uniform distribution these models depend on. As CV rises, a genuine importance gradient emerges that L2 norm ranking can exploit; the random-vs-L2 advantage vanishes and eventually reverses.
129	
130	CV therefore serves as a dual predictor. First, it predicts tolerance class: low CV signals uniform criticality (sensitive to method choice but potentially robust under the right strategy), moderate CV signals a threshold or graded response, and high CV signals extreme fragility (catastrophic cliff). Second, it predicts optimal strategy: models below CV $\approx 0.15$ should use coverage-preserving methods (random or spatially uniform selection), while models above this threshold can benefit from importance-based scoring.
131	
132	At extreme compression ($k{=}0.3$), the interaction partially reverses for $\pi_0.5$: L2 norm achieves 51.0\% vs.\ random 36.4\% ($\Delta{=}-$14.6\,pp favoring L2). The optimal strategy also depends on the absolute token budget; when very few tokens remain, even spatially clustered high-norm tokens provide more signal than a sparse random sample. Full analysis of this interaction appears in Appendix~\ref{app:cv_strategy_interaction}.
133	
134	\begin{figure}[t]
135	\centering
136	\begin{subfigure}[b]{0.48\linewidth}
137	\includegraphics[width=\linewidth]{figures/paper/fig_degradation_curve.pdf}
138	\caption{Token pruning across connector classes.}
139	\label{fig:degradation_curve}
140	\end{subfigure}
141	\hfill
142	\begin{subfigure}[b]{0.48\linewidth}
143	\includegraphics[width=\linewidth]{figures/paper/fig_compression_curve.pdf}
144	\caption{VTR M-curve and CV-strategy interaction.}
145	\label{fig:compression_curve}
146	\end{subfigure}
147	\caption{Architecture-dependent response to token reduction on LIBERO-Object. (a)~Pruning across pipeline types: pure linear ($\pi_0$) is uniformly critical, linear+encoder (X-VLA) is threshold-graded (onset at $k{=}0.85$), MLP (OpenVLA) degrades smoothly, pixel-shuffle (SmolVLA) collapses. (b)~VTR re-encoding achieves near-lossless compression ($M{=}16 \approx M{=}128$) where deletion yields 0\%; CV predicts the L2-vs-random gap monotonically.}
148	\label{fig:results_combined}
149	\end{figure}
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "6a835eee-1c58-491a-bcef-89c6beadb956",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\n\n\\subsection{Taxonomy Overview}\n\\label{sec:taxonomy_overview}\n\nTable~\\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, determines pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\\sim$0.15, smooth graded at $\\sim$0.22, and catastrophic cliff at $>$0.3. A controlled comparison between $\\pi_0$ and OpenVLA (both using 256 SigLIP~\\cite{zhai2023siglip} tokens, differing only in connector) yields a 63\\,pp gap at $k{=}0.1$, isolating the pipeline as causal (Section~\\ref{sec:linear_results}).\n\nThe four classes differ qualitatively in their failure mode. Uniformly critical models ($\\pi_0$, $\\pi_0.5$~\\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\\dagger\\pi_0$ reports offline normalized L1 action loss (pending closed-loop evaluation). $^\\ddagger$X-VLA uses a linear projection followed by a 12-layer BART encoder; the effective pipeline is not purely linear. $^\\S$OFT reports attention entropy and CV only (no pruning evaluation); both metrics match OpenVLA, which confirms the connector determines token importance structure. $^\\|$CogACT result from EfficientVLA~\\cite{yang2025efficientvla} (literature corroboration, not our evaluation).}\n\\label{tab:taxonomy}\n\\begin{tabular}{llcrcll}\n\\toprule\nModel & Connector & Params & Tokens & CV & Representative Result & Class \\\\\n\\midrule\n$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\n$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\nX-VLA~\\cite{zheng2025xvla} & Linear proj$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.8$ & Threshold-graded \\\\\nOpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\nOFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\nCogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\nSmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle: Catastrophic Cliff-Edge}\n\\label{sec:smolvla_results}\n\nThe SmolVLA baseline (bypass mode, all 128 vision tokens) achieves 44.8\\% SR (224/500, CI [40.5\\%, 49.2\\%]).\\footnote{The official SmolVLA result is 87.3\\% SR with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch due to compute constraints.} Every pruning configuration produces 0\\% SR across seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.50, 0.70, 0.90, 0.95\\}$), and mechanism (zero-masking, true removal, token merging). The official SmolVLA checkpoint (59.2\\% SR) exhibits identical failure; the cliff-edge is architectural, not a training artifact.\n\nThe pattern generalizes across LIBERO suites: Spatial 0.6\\%, Goal 0\\%. Pixel-shuffle folds each $4{\\times}4$ patch block into a single token by channel concatenation; removing one token eliminates an entire $4{\\times}4$ receptive field. The resulting spatial entanglement means even 5\\% removal ($k{=}0.95$, losing 7 of 128 tokens) destroys task-critical visual information. Full ablation results appear in Table~\\ref{tab:smolvla_ablation}, Appendix~\\ref{app:smolvla_ablation}.\n\n\\subsection{MLP Projector: Smooth Graded Degradation}\n\\label{sec:openvla_results}\n\nUnder random token removal, OpenVLA degrades gracefully across all retention ratios: 74.0\\% (baseline) $\\rightarrow$ 69.4\\% at $k{=}0.95$ ($-4.6$\\,pp) $\\rightarrow$ 62.0\\% at $k{=}0.90$ $\\rightarrow$ 49.0\\% at $k{=}0.70$ $\\rightarrow$ 37.4\\% at $k{=}0.50$ $\\rightarrow$ 20.6\\% at $k{=}0.30$ (Figure~\\ref{fig:degradation_curve}; full results with CIs in Table~\\ref{tab:openvla_full}, Appendix).\\footnote{A second random seed confirms the graded pattern: 62.2\\% at $k{=}0.9$ ($+$0.2\\,pp), 52.6\\% at $k{=}0.7$ ($+$3.6\\,pp), 35.6\\% at $k{=}0.5$ ($-$1.8\\,pp). All within 4\\,pp of the primary seed. Per-seed details in Table~\\ref{tab:openvla_multiseed}, Appendix~\\ref{app:openvla_multiseed}.} At $k{=}0.30$, two tasks reach 0\\% SR, but eight retain non-zero performance: degradation is graded, not cliff-edge. Random token removal provides a conservative lower bound on architectural resilience; learned scoring methods would likely yield better retention.\n\nOFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, determines token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\n\nTo control for scoring method in cross-architecture comparisons, we evaluate L2 norm-based selection on OpenVLA. At moderate-to-aggressive retention ($k \\leq 0.7$), L2 performs within 2--4\\,pp of random removal (Table~\\ref{tab:openvla_l2_vs_random}, Appendix~\\ref{app:l2_vs_random}). At $k{=}0.9$, L2 outperforms random by 8.5\\,pp (70.6\\% vs.\\ 62.0\\%, reproducible across two random seeds), consistent with the weak but non-zero importance gradient predicted by CV$\\,{=}\\,$0.215: the signal is exploitable only when few tokens are removed.\n\n\\subsection{Linear Projection: From Uniformly Critical to Threshold-Graded}\n\\label{sec:linear_results}\n\nThree models share a linear projection connector yet exhibit qualitatively different pruning responses. The divergence traces to what happens \\emph{after} the projection: nothing ($\\pi_0$), a learned scaling ($\\pi_0.5$), or a full 12-layer encoder (X-VLA).\n\n\\paragraph{$\\pi_0$ (3.3B, 256 tokens, pure linear).} Offline normalized L1 action loss at $k{=}0.1$ is 0.976, a 2.4\\% \\emph{improvement} over the unpruned baseline.\\footnote{Offline action loss measures single-step prediction quality; closed-loop evaluation may reveal additional degradation.} CV$\\,{=}\\,$0.038 indicates near-uniform token norms. Because all tokens carry equal weight, removing 90\\% at random preserves spatial coverage and the model compensates.\n\n\\paragraph{$\\pi_0.5$ (4B, 768 tokens, linear $\\times\\!\\sqrt{d}$).} The baseline achieves 98.2\\% SR. This model reveals that low CV does not imply pruning immunity; it implies uniform criticality. The response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\\% SR ($-$28.8\\,pp), while L2 norm-based removal at the same ratio collapses to 33.4\\% ($-$64.8\\,pp). The gap of 36\\,pp is the largest method-dependent effect in our study.\n\nRandom removal produces monotonic degradation: 77.2\\% at $k{=}0.7$, 69.4\\% at $k{=}0.5$, 36.4\\% at $k{=}0.3$. L2 norm selection instead produces a V-shaped curve: 55.0\\% at $k{=}0.7$, 33.4\\% at $k{=}0.5$ (the valley), 51.0\\% at $k{=}0.3$. The non-monotonic L2 pattern arises because norm ranking in a low-CV distribution selects spatially clustered tokens (slight norm variations correlate with image regions), and the resulting loss of spatial coverage peaks at intermediate budgets. A second random seed (seed43) confirms the random result: 68.4\\% at $k{=}0.5$ ($\\Delta{=}$1.0\\,pp from seed42).\n\nThis result falsifies the ``immune'' assumption from the $\\pi_0$ offline evaluation. Low-CV tokens are uniformly critical, not uniformly dispensable. L2 norm-based selection systematically concentrates on spatially correlated tokens and loses coverage; random selection preserves the uniform spatial distribution that these architectures require.\n\n\\paragraph{X-VLA (880M, 50 tokens, linear + 12-layer BART).} The 99.2\\% baseline is maintained at $k{=}0.95$ ($99.1 \\pm 0.2$\\%, 3 seeds) and $k{=}0.9$ ($97.8 \\pm 0.4$\\%) under L2 norm-based removal. A sharp cliff appears at $k{=}0.85$ (67.8\\%, $-$30\\,pp, 2 seeds), with non-monotonic recovery at $k{=}0.80$ (88.6\\%) before degradation resumes: $57.2 \\pm 1.6$\\% at $k{=}0.7$, $43.4 \\pm 0.8$\\% at $k{=}0.5$, $22.3 \\pm 1.1$\\% at $k{=}0.3$, $4.7 \\pm 0.6$\\% at $k{=}0.2$, and near-zero at $k{=}0.1$. The cliff at $k{=}0.85$ (retaining 42 of 50 BART-encoded tokens) is reproducible across seeds (std $\\leq$ 1.6\\,pp). The non-monotonic dip is task-specific: four tasks lose $\\sim$50\\,pp each while six remain unaffected (Table~\\ref{tab:xvla_cliff_pertask}, Appendix~\\ref{app:xvla_cliff}).\n\nThat this threshold appears under importance-based removal (the more favorable test) while OpenVLA degrades smoothly under random removal (the harder test) strengthens the architecture-dependent conclusion. The $\\pi_0$--OpenVLA controlled comparison (same 256 SigLIP tokens, same encoder lineage, differing only in connector) produces a 63\\,pp gap at $k{=}0.1$, isolating the connector pipeline as the causal factor.\n\n\\subsection{VTR: Re-Encoding Overcomes Cliff-Edge}\n\\label{sec:smart_compress_results}\n\nTo test whether learned re-encoding can overcome the pixel-shuffle cliff-edge, we insert a 22.2M-parameter cross-attention module (Vision Token Re-encoder, VTR) between the vision connector and the LLM backbone (details in Appendix~\\ref{app:smart_compress_details}). VTR compresses 128 input tokens to $M$ output tokens. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR ($p > 0.9$ vs.\\ the 44.8\\% baseline); the gain is architectural, not from additional optimization steps.\\footnote{The extended baseline also collapses to 0\\% SR under pruning ($k{=}0.50$, random, true removal). Additional training does not mitigate the pixel-shuffle vulnerability.}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding vs.\\ deletion on SmolVLA (LIBERO-Object). The M-curve is flat: $M{=}16$ (87.5\\% compression) matches $M{=}128$ (no compression) within 1.1\\,pp. A parameter-matched MLP adapter achieves comparable SR ($p = 0.15$ vs.\\ cross-attention). $^\\ddagger$Mean $\\pm$ std over 3 seeds (500 episodes each). Other rows: single seed with Wilson 95\\% CI.}\n\\label{tab:smart_compress}\n\\begin{tabular}{lccrr}\n\\toprule\nMethod & $M$ & Red. & SR (\\%) & Seeds \\\\\n\\midrule\n\\textit{Baseline} & 128 & 0\\% & 44.8 & 1 \\\\\n\\textit{Ext.\\ training} & -- & -- & 45.0 & 1 \\\\\n\\textit{Hard pruning} & -- & 50--90\\% & 0.0 & mult. \\\\\n\\midrule\nCross-attn$^\\ddagger$ & 16 & 87.5\\% & 56.9$\\pm$1.3 & 55.8/58.4/56.5 \\\\\nCross-attn$^\\ddagger$ & 32 & 75\\% & 60.1$\\pm$1.3 & 61.6/59.2/59.6 \\\\\nCross-attn$^\\ddagger$ & 64 & 50\\% & \\textbf{62.0}$\\pm$2.3 & 61.6/60.0/64.4 \\\\\nCross-attn$^\\ddagger$ & 96 & 25\\% & 54.5$\\pm$3.2 & 52.6/58.2/52.8 \\\\\nCross-attn$^\\ddagger$ & 128 & 0\\% & 58.0$\\pm$3.5 & 59.8/54.0/60.2 \\\\\nMLP adapter$^\\ddagger$ & 32 & 75\\% & 63.4$\\pm$2.6 & 65.2/64.6/60.4 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Official checkpoint (59.2\\% baseline)}} \\\\\nCross-attn & 32 & 75\\% & 53.4 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe M-curve is flat (Table~\\ref{tab:smart_compress}): $M{=}16$ (56.9\\%, 87.5\\% compression) performs within 1.1\\,pp of $M{=}128$ (58.0\\%, no compression), and all five $M$ values cluster within 5\\,pp. A parameter-matched MLP adapter (22.14M parameters) achieves 63.4\\% $\\pm$ 2.6 at $M{=}32$ ($p = 0.15$ vs.\\ cross-attention); re-encoding itself, not the attention mechanism, is the operative factor (Figure~\\ref{fig:compression_curve}). Cross-suite evaluation confirms generalization: 53.2\\% on LIBERO-Spatial and 56.4\\% on LIBERO-Goal where hard pruning yields 0\\% (Appendix~\\ref{app:smart_compress_full}). VTR applied to OpenVLA yields 0\\% SR even in passthrough mode ($M{=}128$): it is a targeted remedy for pixel-shuffle entanglement, not a universal compression module.\n\n\\subsection{CV Predicts Optimal Pruning Strategy}\n\\label{sec:scaling_law}\n\nThe preceding sections establish that connector architecture determines pruning tolerance. A natural follow-up: can a single diagnostic predict not only \\emph{how much} pruning a model tolerates, but also \\emph{which} pruning strategy to use? Token importance CV provides exactly this dual prediction. Table~\\ref{tab:scaling_law} compares L2 norm-based and random removal at two retention ratios ($k{=}0.5$ and $k{=}0.7$) across three models with measured CV.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{L2 norm vs.\\ random removal at two retention ratios. The gap $\\Delta$(R$-$L2) scales monotonically with CV at both $k{=}0.5$ and $k{=}0.7$: low-CV models require random selection (uniform importance $\\rightarrow$ L2 degenerates to spatial clustering), while high-CV models tolerate either strategy. The monotonic ordering holds across retention ratios despite a 2$\\times$ change in token budget.}\n\\label{tab:scaling_law}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & CV & Tokens & L2 SR (\\%) & Random SR (\\%) & $\\Delta$(R$-$L2) \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$k{=}0.5$ (50\\% retention)}} \\\\\n$\\pi_0.5$ & 0.055 & 768 & 33.4 & \\textbf{69.4} & $+$36.0 \\\\\nX-VLA & 0.151 & 50 & 43.4$\\pm$0.8 & \\textbf{70.3}$\\pm$0.9 & $+$26.9 \\\\\nOpenVLA & 0.215 & 256 & 39.2 & 35.8 & $-$3.4 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$k{=}0.7$ (70\\% retention)}} \\\\\n$\\pi_0.5$ & 0.055 & 768 & 55.0 & \\textbf{77.2} & $+$22.2 \\\\\nX-VLA & 0.151 & 50 & 57.2$\\pm$1.6 & \\textbf{64.2} & $+$7.0 \\\\\nOpenVLA & 0.215 & 256 & \\multicolumn{3}{c}{\\textit{pending}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gap decreases monotonically as CV increases at both retention ratios. At $k{=}0.5$: $+$36.0\\,pp ($\\pi_0.5$, CV$\\,{=}\\,$0.055) $\\rightarrow$ $+$26.9\\,pp (X-VLA, CV$\\,{=}\\,$0.151) $\\rightarrow$ $-$3.4\\,pp (OpenVLA, CV$\\,{=}\\,$0.215). At $k{=}0.7$: $+$22.2\\,pp $\\rightarrow$ $+$7.0\\,pp $\\rightarrow$ pending. The monotonic ordering holds across a 2$\\times$ change in absolute token budget, strengthening the claim that CV captures a structural property of the connector rather than a coincidence at a single operating point.\n\nThe mechanism is intuitive. When tokens have near-uniform L2 norms (low CV), norm ranking captures spatial artifacts rather than genuine importance differences. L2 norm-based selection then clusters on correlated patches and loses spatial coverage, while random selection preserves the uniform distribution these models depend on. As CV rises, a genuine importance gradient emerges that L2 norm ranking can exploit; the random-vs-L2 advantage vanishes and eventually reverses.\n\nCV therefore serves as a dual predictor. First, it predicts tolerance class: low CV signals uniform criticality (sensitive to method choice but potentially robust under the right strategy), moderate CV signals a threshold or graded response, and high CV signals extreme fragility (catastrophic cliff). Second, it predicts optimal strategy: models below CV $\\approx 0.15$ should use coverage-preserving methods (random or spatially uniform selection), while models above this threshold can benefit from importance-based scoring.\n\nAt extreme compression ($k{=}0.3$), the interaction partially reverses for $\\pi_0.5$: L2 norm achieves 51.0\\% vs.\\ random 36.4\\% ($\\Delta{=}-$14.6\\,pp favoring L2). The optimal strategy also depends on the absolute token budget; when very few tokens remain, even spatially clustered high-norm tokens provide more signal than a sparse random sample. Full analysis of this interaction appears in Appendix~\\ref{app:cv_strategy_interaction}.\n\n\\begin{figure}[t]\n\\centering\n\\begin{subfigure}[b]{0.48\\linewidth}\n\\includegraphics[width=\\linewidth]{figures/paper/fig_degradation_curve.pdf}\n\\caption{Token pruning across connector classes.}\n\\label{fig:degradation_curve}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[b]{0.48\\linewidth}\n\\includegraphics[width=\\linewidth]{figures/paper/fig_compression_curve.pdf}\n\\caption{VTR M-curve and CV-strategy interaction.}\n\\label{fig:compression_curve}\n\\end{subfigure}\n\\caption{Architecture-dependent response to token reduction on LIBERO-Object. (a)~Pruning across pipeline types: pure linear ($\\pi_0$) is uniformly critical, linear+encoder (X-VLA) is threshold-graded (onset at $k{=}0.85$), MLP (OpenVLA) degrades smoothly, pixel-shuffle (SmolVLA) collapses. (b)~VTR re-encoding achieves near-lossless compression ($M{=}16 \\approx M{=}128$) where deletion yields 0\\%; CV predicts the L2-vs-random gap monotonically.}\n\\label{fig:results_combined}\n\\end{figure}\n",
      "numLines": 150,
      "startLine": 1,
      "totalLines": 150
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_019nmGVpc1ec2z71LfK5GXZj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "4241df9e-09e5-4e38-826c-2adc6ec4303e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 30 · 2026-05-29T06:29:45.546Z_

<details><summary>↩ Tool result · `toolu_019nmGVpc1ec2z71LfK5GXZj`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "1e5e0218-4a4d-4ca1-9b67-d54b3442eaa8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
      "content": "\\section{Discussion}\n\\label{sec:analysis}\n\nCV predicts connector-level compressibility, but task complexity determines \\emph{which} scoring method succeeds within a given connector. On OpenVLA, L2 leads on single-step Object ($+$7.8\\,pp at $k{=}0.9$) but the hierarchy inverts on multi-step Long, where Random outperforms both L2 and attention at $k{=}0.7$ (Appendix~\\ref{app:extended_discussion}). The monotonic L2 curve versus the non-monotonic random curve on $\\pi_{0.5}$ Long (Figure~\\ref{fig:cliff_highlight}) reflects position encoding sensitivity: L2 preserves spatial locality after re-indexing, while random creates scattered gaps that maximally disrupt RoPE at $k{\\approx}0.9$ before recovering at $k{\\leq}0.7$ as surviving positions become approximately uniform (Appendix~\\ref{app:extended_discussion}).\n\n\\paragraph{Limitations.}\nAll evaluations use LIBERO simulation; we provide no sim-to-real evidence. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing causal isolation. The CV--SR correlation relies on four closed-loop models, too few for a general law. VTR is validated on SmolVLA only. Most conditions use a single seed; $\\pi_{0.5}$ Long uses five-seed means ($n{=}5$, sample s.d.\\ ${\\leq}$2.7\\,pp; Appendix~\\ref{app:pi05_long_multiseed}); cross-seed validation on other models shows $\\Delta \\leq 5.8$\\,pp (Appendix~\\ref{app:pi05_multiseed},~\\ref{app:openvla_multiseed}). Extended discussion in Appendix~\\ref{app:extended_discussion}.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01EuPeKCHEjKG3yB5272w7jo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "400b378e-9860-4497-8e91-fa9f46faa37a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 32 · 2026-05-29T06:29:45.936Z_

<details><summary>↩ Tool result · `toolu_01EuPeKCHEjKG3yB5272w7jo`</summary>

```text
1	% Discussion section moved to Appendix (§\ref{app:discussion}) for space.
2	% Three-sentence limitations retained at end of Experiments section.
3	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "c431c328-fc01-4c93-ad3a-653d1f01d1a3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex",
      "content": "% Discussion section moved to Appendix (§\\ref{app:discussion}) for space.\n% Three-sentence limitations retained at end of Experiments section.\n",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01VfKs4nepiSjRj4ZJ7rsoA4`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "45f787d2-ec25-4b63-923e-994c0b382942",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 34 · 2026-05-29T06:29:46.416Z_

<details><summary>↩ Tool result · `toolu_01VfKs4nepiSjRj4ZJ7rsoA4`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	\label{sec:analysis}
4	
5	We set out to understand why identical token pruning produces dramatically different outcomes across VLA architectures. The vision-language connector emerges as the strongest predictor: its coefficient of variation (CV), computable from a single forward pass, partitions architectures into compressibility regimes. Token-independent connectors degrade gracefully while entangling connectors exhibit catastrophic cliffs amplified by task complexity (Appendix~\ref{app:extended_discussion}). No scoring method is universally safe---the importance margin follows an inverted-U curve that reverses at aggressive ratios---and position disruption, not information loss, is the binding constraint. For connectors where all deletion fails, VTR recovers baseline performance at 75\% compression. Practitioners should compute CV before deploying any pruning strategy to identify the appropriate compression regime for their architecture.
6	
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "30f10220-1171-4bf8-a5f9-316773e3ac1c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\\label{sec:analysis}\n\nWe set out to understand why identical token pruning produces dramatically different outcomes across VLA architectures. The vision-language connector emerges as the strongest predictor: its coefficient of variation (CV), computable from a single forward pass, partitions architectures into compressibility regimes. Token-independent connectors degrade gracefully while entangling connectors exhibit catastrophic cliffs amplified by task complexity (Appendix~\\ref{app:extended_discussion}). No scoring method is universally safe---the importance margin follows an inverted-U curve that reverses at aggressive ratios---and position disruption, not information loss, is the binding constraint. For connectors where all deletion fails, VTR recovers baseline performance at 75\\% compression. Practitioners should compute CV before deploying any pruning strategy to identify the appropriate compression regime for their architecture.\n\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01WmMUTneR3UYHPhK3EqNJPz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "1aa25466-2143-4f4e-b633-1e73e59c3239",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 36 · 2026-05-29T06:29:46.941Z_

<details><summary>↩ Tool result · `toolu_01WmMUTneR3UYHPhK3EqNJPz`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	All evaluations use LIBERO simulation; real-robot validation with sensor noise and contact dynamics would further strengthen applicability. Most conditions use a single evaluation seed ($\pi_{0.5}$ Long: $n{=}5$, s.d.\ ${\leq}$2.7\,pp); additional seeds on other models would tighten confidence intervals. VTR is validated on SmolVLA; extending to other entangling connectors is a natural next step.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "78365031-c655-4c66-8f26-16c48e818407",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nAll evaluations use LIBERO simulation; real-robot validation with sensor noise and contact dynamics would further strengthen applicability. Most conditions use a single evaluation seed ($\\pi_{0.5}$ Long: $n{=}5$, s.d.\\ ${\\leq}$2.7\\,pp); additional seeds on other models would tighten confidence intervals. VTR is validated on SmolVLA; extending to other entangling connectors is a natural next step.\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01Fi7scxhtT93yi2gpSGmCfB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "984c1e1a-d0af-41bb-bac6-69dbacb59e6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERswK1bgVPZYxy5jnpM1Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10013,
      "cache_read_input_tokens": 24772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10013
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

_source line 38 · 2026-05-29T06:29:47.729Z_

<details><summary>↩ Tool result · reported error · `toolu_01Fi7scxhtT93yi2gpSGmCfB`</summary>

```text
File content (27358 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "3dc553ad-a150-448e-b9da-4887aae5d8da",
  "tool_use_result": "Error: File content (27358 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
The appendix is too large to read at once. Let me read it in parts. Let me also grep for all cite commands across the tex files to make sure I capture all citations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "e1ee7e09-8384-473a-96ca-429977be8389",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwNJBq9WHUDkqQdHDfjsq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50663,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 50663
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

_source line 40_

Let me get all citations from the tex files and read the appendix in sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "e265ae45-6a41-415b-b157-f7e0b293416f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwNJBq9WHUDkqQdHDfjsq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50663,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 50663
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

_source line 41_

<details open><summary>🔧 Tool call — Grep · `toolu_01F8KqJcAmocH9xZuS1tuny4`</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "0dd3106b-3803-4a47-a65a-66e799c2bc68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwNJBq9WHUDkqQdHDfjsq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50663,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 50663
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

_source line 42 · 2026-05-29T06:29:54.403Z_

<details><summary>↩ Tool result · `toolu_01F8KqJcAmocH9xZuS1tuny4`</summary>

```text
&lt;persisted-output>
Output too large (19.8KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tool-results/toolu_01F8KqJcAmocH9xZuS1tuny4.txt

Preview (first 2KB):
docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, Token Merging~\cite{bolya2023tome}, and CrossGET~\cite{shi2024crossget} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
docs/paper/related_work.tex:8:[Omitted long matching line]
docs/paper/related_work.tex:11:Jabbour et al.~\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.
docs/paper/related_work.tex:14:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.
docs/paper/experiments.tex:7:\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).
docs/paper/experiments.tex:9:\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\ref{tab:model_properties}): $\pi_{0.5}$~\cite{black2025pi05}, X-VLA~\cite{zheng2025xvla}, OpenVLA~\cite{kim2024openvla}, and SmolVLA~\cite{shukor2025smolvla}. Two additional models ($\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "d4445de8-9fc1-41bf-a2a5-2c99b7d5c6b7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:5:DynamicViT~\\cite{rao2021dynamicvit}, EViT~\\cite{liang2022evit}, A-ViT~\\cite{yin2022avit}, Token Merging~\\cite{bolya2023tome}, and CrossGET~\\cite{shi2024crossget} remove 50--66\\% of tokens with under 0.5\\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.\ndocs/paper/related_work.tex:8:[Omitted long matching line]\ndocs/paper/related_work.tex:11:Jabbour et al.~\\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.\ndocs/paper/related_work.tex:14:LLaVA~\\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.\ndocs/paper/experiments.tex:7:\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\ndocs/paper/experiments.tex:9:\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\ndocs/paper/results_v2.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\ndocs/paper/results_v2.tex:9:[Omitted long matching line]\ndocs/paper/results_v2.tex:11:[Omitted long matching line]\ndocs/paper/results_v2.tex:16:[Omitted long matching line]\ndocs/paper/results_v2.tex:22:$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\ndocs/paper/results_v2.tex:23:$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\ndocs/paper/results_v2.tex:24:X-VLA~\\cite{zheng2025xvla} & Linear proj$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.8$ & Threshold-graded \\\\\ndocs/paper/results_v2.tex:25:OpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\ndocs/paper/results_v2.tex:26:OFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\ndocs/paper/results_v2.tex:27:CogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\ndocs/paper/results_v2.tex:28:SmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\ndocs/paper/results_v2.tex:45:OFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, determines token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\ndocs/paper/sections/analysis.tex:21:DynamicViT~\\cite{rao2021dynamicvit} and ToMe~\\cite{bolya2023tome} exploit this concentration: tokens that receive low attention contribute little to the classification decision and can be safely removed.\ndocs/paper/sections/analysis.tex:24:We extract attention weights from the LLM backbone (Qwen2-0.5B~\\cite{yang2024qwen2}) over all vision tokens across three LIBERO tasks.\ndocs/paper/sections/analysis.tex:31:SigLIP~\\cite{zhai2023siglip} encodes images using non-overlapping spatial patches without a \\texttt{[CLS]} aggregation token.\ndocs/paper/sections/analysis.tex:123:In ViT classification, attention concentrates on a small subset of discriminative patches~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}.\ndocs/paper/sections/analysis.tex:129:SigLIP~\\cite{zhai2023siglip} encodes each non-overlapping spatial patch as a separate token with no \\texttt{[CLS]} aggregation, so the VLA's LLM backbone must attend to all patches to reconstruct spatial relationships between the robot end-effector, target objects, and obstacles.\ndocs/paper/sections/related_work_draft.tex:6:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:8:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:12:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:14:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:20:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:22:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:24:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:28:[Omitted long matching line]\ndocs/paper/sections/experiments.tex:17:DynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/sections/experiments.tex:18:EViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/sections/experiments.tex:19:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{xu2025vlacache,cheng2026vlaiap}.\ndocs/paper/sections/experiments.tex:20:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\ndocs/paper/sections/experiments.tex:66:Token merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\ndocs/paper/sections/experiments.tex:73:\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}\ndocs/paper/sections/results_draft.tex:4:We evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\\% confidence intervals.\ndocs/paper/sections/results_draft.tex:9:[Omitted long matching line]\ndocs/paper/sections/results_draft.tex:12:[Omitted long matching line]\ndocs/paper/sections/results_draft.tex:59:OpenVLA~\\cite{kim2024openvla} uses a two-layer MLP projector to map vision encoder outputs (from DINOv2 and SigLIP~\\cite{zhai2023siglip}) into the Llama-2 language model's embedding space. Unlike pixel-shuffle, the MLP projector processes each patch token independently through a shared linear transformation. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence.\ndocs/paper/appendix.tex:91:[Omitted long matching line]\ndocs/paper/appendix.tex:94:[Omitted long matching line]\ndocs/paper/appendix.tex:138:[Omitted long matching line]\ndocs/paper/appendix.tex:748:X-VLA's 12-layer BART encoder~\\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\\,pp), confirming it as an architectural property.\ndocs/paper/appendix.tex:750:MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\\% SR under 78\\% pruning).\ndocs/paper/appendix.tex:878:Table~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.\ndocs/paper/experimental_setup.tex:9:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:11:We evaluate on LIBERO~\\cite{liu2023libero} (Object: 10 tasks $\\times$ 50 episodes = 500 total; Spatial and Goal for cross-suite validation). Closed-loop success rate (SR) with Wilson 95\\% CIs is the primary metric; multi-seed results report mean $\\pm$ std. Baselines: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%.\ndocs/paper/introduction.tex:14:[Omitted long matching line]\ndocs/paper/introduction.tex:16:[Omitted long matching line]\ndocs/paper/results.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\ndocs/paper/results.tex:9:[Omitted long matching line]\ndocs/paper/results.tex:11:[Omitted long matching line]\ndocs/paper/results.tex:16:[Omitted long matching line]\ndocs/paper/results.tex:22:$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\ndocs/paper/results.tex:23:$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\ndocs/paper/results.tex:24:X-VLA~\\cite{zheng2025xvla} & Linear + BART (12L)$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.9{\\pm}0.3$ & Threshold-graded \\\\\ndocs/paper/results.tex:25:OpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\ndocs/paper/results.tex:26:OFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\ndocs/paper/results.tex:27:CogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\ndocs/paper/results.tex:28:SmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\ndocs/paper/results.tex:45:OFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\ndocs/paper/sections/background.tex:6:This section describes the two components of our experimental setup: the SmolVLA architecture~\\cite{shukor2025smolvla}, in which we study vision token reduction, and the LIBERO benchmark~\\cite{liu2023libero}, on which we evaluate closed-loop performance.\ndocs/paper/sections/background.tex:12:SmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a modality connector, a language model backbone, and an action head.\ndocs/paper/sections/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\ndocs/paper/sections/background.tex:41:The Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\ndocs/paper/sections/background.tex:47:SmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\ndocs/paper/sections/background.tex:54:This architecture shares its high-level structure with larger VLA systems such as OpenVLA~\\cite{kim2024openvla} and $\\pi_0$~\\cite{black2024pi0}, making SmolVLA a representative testbed for studying vision token efficiency in VLA policies.\ndocs/paper/sections/background.tex:59:We evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\ndocs/paper/sections/experimental_setup.tex:33:  \\item \\textbf{Token merge}: following the bipartite matching strategy of ToMe~\\cite{bolya2023tome}, each pruned token is merged with its nearest retained neighbor by averaging their embeddings. Sequence length and total information content are both preserved.\ndocs/paper/sections/introduction.tex:7:DynamicViT~\\cite{rao2021dynamicvit} removes 66\\% of patch tokens with less than 0.5\\% accuracy loss on ImageNet classification.\ndocs/paper/sections/introduction.tex:8:Token Merging (ToMe)~\\cite{bolya2023tome} merges 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/sections/introduction.tex:9:EViT~\\cite{liang2022evit} discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/sections/introduction.tex:12:Vision-Language-Action (VLA) models~\\cite{brohan2023rt2,kim2024openvla,black2024pi0,shukor2025smolvla} use the same ViT encoders as their visual front-ends, producing hundreds of patch tokens that dominate the input sequence to the language model backbone.\ndocs/paper/sections/introduction.tex:17:Current VLA models such as RT-2~\\cite{brohan2023rt2} and $\\pi_0$~\\cite{black2024pi0} use large vision encoders that produce 256 or more tokens per image.\ndocs/paper/sections/introduction.tex:20:SmolVLA~\\cite{shukor2025smolvla}, a compact 451.5M-parameter VLA, produces 256 vision tokens from two cameras (128 per view), and these tokens constitute the majority of the LLM backbone's input sequence.\ndocs/paper/sections/introduction.tex:23:FastV~\\cite{chen2024fastv} identifies and prunes inattentive visual tokens in VLM inference, achieving 2$\\times$ speedup with minimal quality loss on VLM benchmarks.\ndocs/paper/sections/introduction.tex:24:VLA-Cache~\\cite{xu2025vlacache} caches vision tokens across timesteps to reduce redundant computation in temporal sequences.\ndocs/paper/sections/introduction.tex:25:VLA-IAP~\\cite{cheng2026vlaiap} proposes importance-aware pruning for VLA inference acceleration.\ndocs/paper/sections/introduction.tex:30:Existing evaluations of VLM token reduction rely on offline metrics such as action loss, perplexity, or next-token prediction accuracy~\\cite{chen2024fastv,cheng2026vlaiap}.\ndocs/paper/sections/introduction.tex:38:Using SmolVLA on the LIBERO benchmark~\\cite{liu2023libero}, we test six pruning configurations spanning three axes: scoring function (a trained Attention-Conditioned Importance Scorer versus random selection), retention ratio ($k \\in \\{0.5, 0.7, 0.9\\}$), and mechanism (zero-masking, true removal, and token merging).\ndocs/paper/sections/introduction.tex:50:This uniformity arises because SigLIP~\\cite{zhai2023siglip} encodes non-overlapping spatial patches without a \\texttt{[CLS]} aggregation token; each token carries unique, irreplaceable spatial information about the scene.\ndocs/paper/sections/introduction.tex:59:We believe this negative result~\\cite{karl2024negative,zeng2023transformers_tsf} carries important implications for the VLA efficiency community: future work on VLA compression should seek alternatives to naive token removal, such as training-time distillation into fewer tokens or architectural modifications that build in spatial redundancy.\ndocs/paper/method.tex:7:[Omitted long matching line]\ndocs/paper/background.tex:6:This section describes the architectures and benchmark used in our study: SmolVLA~\\cite{shukor2025smolvla} and OpenVLA~\\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\\cite{liu2023libero} on which we evaluate closed-loop performance.\ndocs/paper/background.tex:12:SmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 450M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.\ndocs/paper/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\ndocs/paper/background.tex:36:The Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\ndocs/paper/background.tex:41:SmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\ndocs/paper/background.tex:49:OpenVLA~\\cite{kim2024openvla} is a 7B-parameter VLA built on the Llama-2 backbone. Its vision pipeline differs from SmolVLA in two respects that are directly relevant to compressibility.\ndocs/paper/background.tex:52:OpenVLA uses a dual encoder combining DINOv2~\\cite{oquab2023dinov2} and SigLIP~\\cite{zhai2023siglip}. The two encoders produce complementary representations (self-supervised spatial features and language-aligned features) that are concatenated per patch position.\ndocs/paper/background.tex:63:We evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\ndocs/paper/experiments_deprecated.tex:6:DynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/experiments_deprecated.tex:7:EViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/experiments_deprecated.tex:8:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{xu2025vlacache,cheng2026vlaiap}.\ndocs/paper/experiments_deprecated.tex:9:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\ndocs/paper/experiments_deprecated.tex:55:Token merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\ndocs/paper/experiments_deprecated.tex:62:\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}",
    "numLines": 99
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01PYv3Xf4Q8YcUkXUzjTPUPv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "5778bdf9-c359-4d6f-82be-b4cc4f58203b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwNJBq9WHUDkqQdHDfjsq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50663,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 50663
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

_source line 44 · 2026-05-29T06:29:54.855Z_

<details><summary>↩ Tool result · `toolu_01PYv3Xf4Q8YcUkXUzjTPUPv`</summary>

```text
1	\clearpage
2	\appendix
3	
4	\section{Full Pruning Results}
5	\label{app:full_results}
6	
7	Table~\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\ref{tab:main_results} for space.
8	
9	\begin{table*}[ht]
10	\centering
11	\footnotesize
12	\caption{Available closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \textsuperscript{$\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}
13	\label{tab:full_results}
14	\setlength{\tabcolsep}{4pt}
15	\begin{tabular}{llccccc}
16	\toprule
17	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
18	\midrule
19	\multirow{4}{*}{$\pi_{0.5}$}
20	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\
21	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\
22	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\
23	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\
24	\midrule
25	\multirow{4}{*}{X-VLA}
26	& Object  & \textbf{99.2} & 99.0 / 98.8 & 99.2 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\
27	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\
28	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\
29	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\
30	\midrule
31	\multirow{4}{*}{OpenVLA}
32	& Object  & \textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\textsuperscript{$\dagger$} & -- / -- & 39.2 / 35.8 \\
33	& Goal    & \textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
34	& Spatial & \textbf{80.0} & -- / -- & 75.0 / 79.8 / 80.4\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
35	& Long    & \textbf{52.8} & -- / -- & 43.6 / 46.8 / 44.0\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
36	\midrule
37	\multirow{4}{*}{SmolVLA}
38	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
39	& Spatial & \textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
40	& Goal    & \textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
41	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
42	\bottomrule
43	\end{tabular}
44	\end{table*}
45	
46	
47	\section{Extended Discussion}
48	\label{app:extended_discussion}
49	\label{app:discussion}
50	
51	\paragraph{Re-encoding and CV diagnostics.}
52	Both cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels, differentiating X-VLA's threshold-graded behavior (CV$\,{=}\,$0.151) from $\pi_0$'s uniformly critical profile (CV$\,{=}\,$0.038); the interaction reverses at $k{=}0.3$ (Appendices~\ref{app:cv_strategy_interaction},~\ref{app:cv_extended}).
53	
54	\paragraph{Task complexity compresses the importance margin.}
55	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector. OpenVLA illustrates the full pattern across LIBERO's complexity gradient (Figure~\ref{fig:openvla_sweep}).
56	
57	On single-step Object, L2 leads at moderate pruning ($+$7.8\,pp at $k{=}0.9$), but the three methods exhibit staggered cliffs---L2 earliest ($k{=}0.9{\to}0.85$, $-$15.4\,pp), random next, attention latest---each defining a distinct effective compression window before converging at $k{=}0.5$ ($<$4.8\,pp spread). As task complexity increases, the scoring hierarchy inverts. On Goal, random pruning at $k{=}0.9$ \emph{exceeds} the unpruned baseline ($+$4.8\,pp; cross-seed confirmed), suggesting OpenVLA's 256 vision tokens are over-provisioned for goal-conditioned tasks---random removal acts as implicit regularization. On Long, the inversion is complete: at $k{=}0.7$, Random (38.8\%) $>$ L2 (31.2\%) $>$ Attention (24.0\%), with attention degrading $2.5{\times}$ faster than random. The mechanism is consistent: multi-step tasks distribute critical information across tokens with heterogeneous norm profiles; L2 and attention both cluster on locally salient tokens, sacrificing the spatial diversity that compositional reasoning requires.
58	
59	\begin{figure}[ht]
60	\centering
61	\includegraphics[width=\linewidth]{figures/paper/fig_openvla_sweep.pdf}
62	\caption{OpenVLA scoring method comparison across four LIBERO suites. On Object, L2 leads at $k{=}0.9$ ($+$7.8\,pp) but the margin flips at $k{=}0.85$ ($-$5.2\,pp, Random wins). Goal degrades smoothly with three-method convergence at $k{=}0.7$. On Long, the ranking inverts with compression. No single scoring method dominates across suites or retention ratios.}
63	\label{fig:openvla_sweep}
64	\end{figure}
65	
66	This is a concrete manifestation of the two-axis framework (Section~\ref{sec:two_axis}): Axis~1 (connector architecture) determines \emph{whether} pruning is viable; Axis~2 (task complexity) determines \emph{which} scoring method succeeds. CV remains a valid connector diagnostic, but the optimal scoring strategy requires knowledge of both axes.
67	
68	\paragraph{Position encoding mediates the V-shape recovery.}
69	The monotonic L2 curve versus the non-monotonic random curve on $\pi_{0.5}$ Long (Figure~\ref{fig:cliff_highlight}) reflects an interaction between token selection strategy and positional encoding. L2 norm scoring preserves spatial locality: retained tokens form near-contiguous clusters in the ViT grid, producing continuous position shifts after re-indexing that Gemma's RoPE accommodates smoothly---hence monotonic degradation (86.8\% $\to$ 51.7\% from $k{=}0.95$ to $k{=}0.5$). Random selection creates scattered gaps that produce position aliasing after re-indexing. At $k{\approx}0.9$, the aliasing is maximally destructive: a small number of randomly placed gaps create highly irregular inter-token spacing, collapsing SR to 33.6\%. Per-task analysis reveals this aggregate is driven by specific tasks with position-sensitive spatial reasoning: Task~4 (``put mugs on plates'') drops from 80\% at $k{=}0.7$ to 12\% at $k{=}0.85$, contributing disproportionately to the V-shape minimum. At $k{=}0.7$, enough tokens are removed that the surviving positions become approximately uniform again, and SR recovers to 64.6\%---exceeding the $k{=}0.9$ level by ${\sim}2{\times}$. The zero-mask ablation (Section~\ref{sec:zeromask}) provides causal confirmation: zeroing token content while preserving positions yields 98.0\% SR, while physically removing the same tokens collapses to 9.0\%. Position encoding, not information content, is the binding constraint---and scoring method determines whether that constraint is violated.
70	
71	\paragraph{Per-task reversal within L2-dominant regimes.} The Long $k{=}0.85$ aggregate ($+$33.2\,pp for L2) masks extreme per-task heterogeneity (per-task $\sigma{=}$21.5\,pp). L2 outperforms random on 9 of 10 tasks ($+$16 to $+$52\,pp), but on Task~6---a dual-object spatial-relation task (``place white mug on plate \emph{and} chocolate pudding to the right of plate'')---L2 collapses to 8\% while random achieves 52\% ($-$44\,pp reversal). L2 scoring systematically undervalues tokens encoding spatial relationships, which carry low norms but are critical for relational reasoning. This per-task sign flip within an architecture where L2 dominates overall reinforces that no single scoring method is universally safe: task semantics, not just connector architecture or suite-level statistics, determine optimal strategy.
72	
73	\begin{figure}[ht]
74	\centering
75	\includegraphics[width=0.85\linewidth]{figures/paper/fig_scoring_crossover.pdf}
76	\caption{Scoring method comparison at $k{=}0.9$ across three models and four LIBERO suites. Cell color encodes SR as a fraction of unpruned baseline; blue bars mark the best method per condition; dashed borders indicate method-indifferent cells ($\Delta{<}3.5$\,pp). $\pi_{0.5}$'s linear connector strongly favors L2 selection, while X-VLA's BART encoder is largely method-indifferent. SmolVLA collapses to 0\% regardless of method. Compact 2$\times$2 summary in Appendix Table~\ref{tab:scoring_crossover_summary}.}
77	\label{fig:scoring_crossover}
78	\end{figure}
79	
80	\begin{figure}[ht]
81	\centering
82	\includegraphics[width=0.85\linewidth]{figures/paper/fig_margin_profile.pdf}
83	\caption{Importance margin (L2 $-$ Random SR) on $\pi_{0.5}$ Long across retention ratios (multi-seed mean $\pm$ s.d.; $n{=}5$). The margin peaks sharply at $k{=}0.9$ (46.8\,pp) where random pruning is maximally destructive, then declines asymmetrically: one step above the peak ($k{=}0.95$: 25.6\,pp) versus four steps below before crossing zero at $k{\approx}0.71$. At $k{=}0.5$, L2 and Random converge ($|\Delta|{\approx}1.3$\,pp), indicating that scoring method choice matters only in the moderate-pruning window.}
84	\label{fig:margin_profile}
85	\end{figure}
86	
87	\paragraph{Limitations (extended).}
88	All closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\pi_{0}$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\% official, 44.8\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.
89	
90	\paragraph{Non-monotonicity as structural property.}
91	X-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\% (L2) and 54.0\% (random), while $k{=}0.9$ recovers to 70.2\% under L2 selection (Table~\ref{tab:main_results}). The 0.2\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.
92	
93	\paragraph{$\pi_{0.5}$ random subsampling anomaly and RoPE amplification.}
94	Random selection on $\pi_{0.5}$ Object collapses from 74.0\% at $k{=}0.95$ to 9.0\% at $k{=}0.9$, then recovers to 74.0\% at $k{=}0.7$ (Table~\ref{tab:main_results}). The re-indexing step of our pruning protocol (Section~\ref{sec:pruning_protocol}) contributes to this non-monotonicity. $\pi_{0.5}$'s linear connector preserves a one-to-one mapping between spatial patches and token positions; when random removal shifts surviving tokens to new positions, the backbone's Rotary Position Embeddings (RoPE)~\cite{su2024roformer} encode spatial content at unfamiliar positions, amplifying disruption of learned attention patterns. X-VLA's BART encoder, which redistributes spatial information via cross-attention and lacks RoPE, provides a partial control. At $k{=}0.85$, single-step suites degrade smoothly (Spatial~68.2\%, Object~65.0\%, Goal~60.4\%), but Long drops to 35.0\%, below its $k{=}0.5$ performance of 61.6\% (Table~\ref{tab:xvla_k085_crosssuite}). Random re-indexing thus induces non-monotonic behavior for complex tasks even without RoPE, but RoPE amplifies the reversal: $\pi_{0.5}$ Object drops to 5.6\% at $k{=}0.85$ versus 69.4\% at $k{=}0.5$ ($-$63.8\,pp), more than double X-VLA Long's $-$26.6\,pp. The V-shaped recovery at $k \leq 0.7$ remains unexplained.
95	
96	\begin{table}[ht]
97	\centering
98	\small
99	\caption{Random pruning at $k{=}0.85$: X-VLA (BART encoder) vs.\ $\pi_{0.5}$ (linear connector). X-VLA degrades smoothly on single-step suites (60--68\%) but drops to 35.0\% on Long (below $k{=}0.5$); $\pi_{0.5}$ exhibits a severe disruption peak on Object.}
100	\label{tab:xvla_k085_crosssuite}
101	\begin{tabular}{lcccc}
102	\toprule
103	Suite & X-VLA SR (\%) & $\Delta$ & $\pi_{0.5}$ SR (\%) & $\Delta$ \\
104	\midrule
105	Object & 65.0 & $-$34.2 & 3.6--5.6\textsuperscript{$\dagger$} & $-$93 to $-$95 \\
106	Goal & 60.4 & $-$38.0 & 52.4 & $-$44.0 \\
107	Spatial & 68.2 & $-$24.8 & --- & --- \\
108	Long & 35.0 & $-$59.0 & --- & --- \\
109	\bottomrule
110	\multicolumn{5}{l}{\footnotesize\textsuperscript{$\dagger$}Two seeds: seed42$\,{=}\,$5.6\% (post-fix), seed43$\,{=}\,$3.6\%. $\Delta$ from respective baselines.}
111	\end{tabular}
112	\end{table}
113	
114	\paragraph{Small-$N$ interactions.}
115	X-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.6\,pp on Goal and $-$47.0\,pp on Long (L2 norm selection). Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.
116	
117	\paragraph{Design implications.}
118	Practitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.
119	
120	
121	\section{Cross-Suite Task Complexity Analysis}
122	\label{app:cross_suite_extended}
123	
124	LIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.
125	
126	$\pi_{0.5}$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\% (matching the baseline), Spatial retains 97.8\% (within noise of the 97.2\% baseline), and Goal drops to 89.4\% ($-$7.0\,pp from 96.4\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\% token removal.
127	
128	X-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 99.2\% (matching the 99.2\% baseline), while Goal drops to 70.2\% ($-$28.2\,pp from 98.4\% baseline). Under random pruning at the same ratio, Object loses just 1.4\,pp (97.8\%) while Goal loses 27.8\,pp (70.6\%), a $20{\times}$ amplification. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\% to 47.0\% (L2) and 48.2\% (random), a 47.0\,pp loss with only 1.2\,pp method gap, while Object at the same ratio loses only 0.2\,pp.
129	
130	Token-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\pi_{0.5}$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.
131	
132	
133	\section{Pruning Protocol Details}
134	\label{app:pruning_details}
135	
136	Both pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.
137	
138	Model-specific retention ratios reflect each architecture's token count and expected sensitivity. $\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\pi_{0.5}$ uses $k \in \{0.3, 0.5, 0.7\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \in \{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \in \{0.3, 0.5, 0.7, 0.9, 0.95\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\ random), retention ratio ($k \in \{0.5, 0.7, 0.9, 0.95\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\cite{bolya2023tome}).
139	
140	The $\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\ three-layer MLP), backbone (PaliGemma vs.\ Llama-2), and encoder fusion strategy (single SigLIP vs.\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.
141	
142	
143	\section{SmolVLA Pruning Ablation}
144	\label{app:smolvla_ablation}
145	
146	\begin{table}[ht]
147	\centering
148	\small
149	\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\% SR. Two independent evaluations of the official HF checkpoint (59.2\% and 57.2\% baseline, within CI) confirm the cliff-edge across scoring methods.}
150	\label{tab:smolvla_ablation}
151	\begin{tabular}{llccrr}
152	\toprule
153	Scoring & $k$ & Mechanism & SR (\%) & Episodes & Wilson 95\% CI \\
154	\midrule
155	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\
156	\midrule
157	ACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
158	ACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
159	ACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
160	Random & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
161	Random & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
162	ACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\
163	ACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\
164	\midrule
165	\multicolumn{6}{l}{\textit{Official checkpoint, eval protocol A (59.2\% baseline)}} \\
166	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\
167	Random & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\
168	\midrule
169	\multicolumn{6}{l}{\textit{Official checkpoint, eval protocol B (57.2\% baseline)}} \\
170	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 57.2 & 500 & [52.9, 61.4] \\
171	Random & 0.95 & True removal & 0.0 & 500 & [0, 0.76] \\
172	L2 norm & 0.90 & True removal & 0.0 & 500 & [0, 0.76] \\
173	L2 norm & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\
174	\bottomrule
175	\end{tabular}
176	\end{table}
177	
178	
179	\section{Per-Task Breakdown Tables}
180	\label{app:per_task}
181	
182	\subsection{SmolVLA Baseline Per-Task Results}
183	
184	Table~\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\ref{tab:smolvla_ablation}) produce 0\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\% already reported.
185	
186	\begin{table}[ht]
187	\centering
188	\small
189	\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\%.}
190	\label{tab:smolvla_baseline_pertask}
191	\begin{tabular}{lc}
192	\toprule
193	Task & SR (\%) \\
194	\midrule
195	alphabet\_soup & 22 \\
196	bbq\_sauce & 60 \\
197	butter & 42 \\
198	chocolate\_pudding & 38 \\
199	cream\_cheese & 58 \\
200	ketchup & 26 \\
201	milk & 62 \\
202	orange\_juice & 38 \\
203	salad\_dressing & 50 \\
204	tomato\_sauce & 52 \\
205	\midrule
206	\textbf{Overall} & \textbf{44.8} \\
207	\bottomrule
208	\end{tabular}
209	\end{table}
210	
211	\subsection{Official SmolVLA Checkpoint Per-Task Results}
212	
213	Table~\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\_libero). Under 50\% random token removal, all tasks produce 0\% SR, identical to the fine-tuned checkpoint results.
214	
215	\begin{table}[ht]
216	\centering
217	\small
218	\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\%. Under 50\% random pruning, all tasks collapse to 0\%. An independent evaluation (protocol B) yields 57.2\% baseline with identical cliff-edge (Table~\ref{tab:smolvla_ablation}).}
219	\label{tab:smolvla_official_pertask}
220	\begin{tabular}{lcc}
221	\toprule
222	Task & Baseline SR (\%) & $k{=}0.5$ SR (\%) \\
223	\midrule
224	alphabet\_soup & 64 & 0 \\
225	bbq\_sauce & 38 & 0 \\
226	butter & 78 & 0 \\
227	chocolate\_pudding & 90 & 0 \\
228	cream\_cheese & 40 & 0 \\
229	ketchup & 60 & 0 \\
230	milk & 52 & 0 \\
231	orange\_juice & 80 & 0 \\
232	salad\_dressing & 44 & 0 \\
233	tomato\_sauce & 46 & 0 \\
234	\midrule
235	\textbf{Overall} & \textbf{59.2} & \textbf{0.0} \\
236	\bottomrule
237	\end{tabular}
238	\end{table}
239	
240	\subsection{OpenVLA Per-Task Results Under Pruning}
241	
242	\begin{table}[ht]
243	\centering
244	\small
245	\caption{OpenVLA per-task success rates (\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\%. Tasks requiring fine-grained discrimination (butter, cream\_cheese) degrade earliest; visually distinctive targets (orange\_juice, salad\_dressing) are most resilient.}
246	\label{tab:openvla_pertask}
247	\begin{tabular}{lccccc}
248	\toprule
249	Task & $k{=}0.95$ & $k{=}0.90$ & $k{=}0.70$ & $k{=}0.50$ & $k{=}0.30$ \\
250	\midrule
251	alphabet\_soup & 76 & 70 & 74 & 60 & 14 \\
252	bbq\_sauce & 38 & 28 & 46 & 44 & 30 \\
253	butter & 84 & 76 & 10 & 2 & 0 \\
254	chocolate\_pudding & 54 & 56 & 32 & 40 & 10 \\
255	cream\_cheese & 84 & 78 & 18 & 8 & 0 \\
256	ketchup & 82 & 70 & 68 & 50 & 30 \\
257	milk & 46 & 42 & 40 & 24 & 8 \\
258	orange\_juice & 74 & 60 & 76 & 72 & 42 \\
259	salad\_dressing & 64 & 54 & 64 & 36 & 64 \\
260	tomato\_sauce & 92 & 86 & 62 & 38 & 8 \\
261	\midrule
262	\textbf{Overall} & \textbf{69.4} & \textbf{62.0} & \textbf{49.0} & \textbf{37.4} & \textbf{20.6} \\
263	\bottomrule
264	\end{tabular}
265	\end{table}
266	
267	\subsection{OpenVLA Full Degradation Curve}
268	
269	\begin{table}[ht]
270	\centering
271	\small
272	\caption{OpenVLA success rates on LIBERO-Object under random token removal at six retention ratios (50 episodes per task, 500 total per ratio). Baseline SR: 74.0\%. All confidence intervals are Wilson 95\%.}
273	\label{tab:openvla_full}
274	\begin{tabular}{ccrr}
275	\toprule
276	$k$ & Tokens Retained & SR (\%) & Wilson 95\% CI \\
277	\midrule
278	1.00 (baseline) & 256 & 74.0 & [69.9, 77.7] \\
279	0.95 & 243 & 69.4 & [65.2, 73.3] \\
280	0.90 & 230 & 62.0 & [57.7, 66.2] \\
281	0.70 & 179 & 49.0 & [44.6, 53.4] \\
282	0.50 & 128 & 37.4 & [33.3, 41.7] \\
283	0.30 & 77 & 20.6 & [17.2, 24.4] \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	\subsection{$\pi_{0.5}$ LIBERO-Long Five-Seed Results}
289	\label{app:pi05_long_multiseed}
290	
291	\begin{table}[ht]
292	\centering
293	\small
294	\caption{$\pi_{0.5}$ LIBERO-Long success rates (\%) across five seeds (500 episodes each). All values are means over seeds 42--46 with sample standard deviation (ddof$\,{=}\,$1). The importance margin (L2$-$Random) peaks at $k{=}0.9$ (46.8\,pp) and crosses zero near $k{\approx}0.71$. Maximum per-seed range is 5.8\,pp (L2, $k{=}0.75$).}
295	\label{tab:pi05_long_multiseed}
296	\begin{tabular}{cccc}
297	\toprule
298	$k$ & L2 Norm (\%) & Random (\%) & Attention (\%) \\
299	\midrule
300	0.95 & $86.8 \pm 0.8$ & $61.2 \pm 0.7$ & $77.3 \pm 1.2$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "01cf7aae-1e37-420b-a3b6-1c9122226f39",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
      "content": "\\clearpage\n\\appendix\n\n\\section{Full Pruning Results}\n\\label{app:full_results}\n\nTable~\\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\\ref{tab:main_results} for space.\n\n\\begin{table*}[ht]\n\\centering\n\\footnotesize\n\\caption{Available closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \\textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \\textsuperscript{$\\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}\n\\label{tab:full_results}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 99.2 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{OpenVLA}\n& Object  & \\textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\\textsuperscript{$\\dagger$} & -- / -- & 39.2 / 35.8 \\\\\n& Goal    & \\textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n& Spatial & \\textbf{80.0} & -- / -- & 75.0 / 79.8 / 80.4\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n& Long    & \\textbf{52.8} & -- / -- & 43.6 / 46.8 / 44.0\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Extended Discussion}\n\\label{app:extended_discussion}\n\\label{app:discussion}\n\n\\paragraph{Re-encoding and CV diagnostics.}\nBoth cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \\approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels, differentiating X-VLA's threshold-graded behavior (CV$\\,{=}\\,$0.151) from $\\pi_0$'s uniformly critical profile (CV$\\,{=}\\,$0.038); the interaction reverses at $k{=}0.3$ (Appendices~\\ref{app:cv_strategy_interaction},~\\ref{app:cv_extended}).\n\n\\paragraph{Task complexity compresses the importance margin.}\nCV predicts connector-level compressibility, but task complexity determines \\emph{which} scoring method succeeds within a given connector. OpenVLA illustrates the full pattern across LIBERO's complexity gradient (Figure~\\ref{fig:openvla_sweep}).\n\nOn single-step Object, L2 leads at moderate pruning ($+$7.8\\,pp at $k{=}0.9$), but the three methods exhibit staggered cliffs---L2 earliest ($k{=}0.9{\\to}0.85$, $-$15.4\\,pp), random next, attention latest---each defining a distinct effective compression window before converging at $k{=}0.5$ ($<$4.8\\,pp spread). As task complexity increases, the scoring hierarchy inverts. On Goal, random pruning at $k{=}0.9$ \\emph{exceeds} the unpruned baseline ($+$4.8\\,pp; cross-seed confirmed), suggesting OpenVLA's 256 vision tokens are over-provisioned for goal-conditioned tasks---random removal acts as implicit regularization. On Long, the inversion is complete: at $k{=}0.7$, Random (38.8\\%) $>$ L2 (31.2\\%) $>$ Attention (24.0\\%), with attention degrading $2.5{\\times}$ faster than random. The mechanism is consistent: multi-step tasks distribute critical information across tokens with heterogeneous norm profiles; L2 and attention both cluster on locally salient tokens, sacrificing the spatial diversity that compositional reasoning requires.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_openvla_sweep.pdf}\n\\caption{OpenVLA scoring method comparison across four LIBERO suites. On Object, L2 leads at $k{=}0.9$ ($+$7.8\\,pp) but the margin flips at $k{=}0.85$ ($-$5.2\\,pp, Random wins). Goal degrades smoothly with three-method convergence at $k{=}0.7$. On Long, the ranking inverts with compression. No single scoring method dominates across suites or retention ratios.}\n\\label{fig:openvla_sweep}\n\\end{figure}\n\nThis is a concrete manifestation of the two-axis framework (Section~\\ref{sec:two_axis}): Axis~1 (connector architecture) determines \\emph{whether} pruning is viable; Axis~2 (task complexity) determines \\emph{which} scoring method succeeds. CV remains a valid connector diagnostic, but the optimal scoring strategy requires knowledge of both axes.\n\n\\paragraph{Position encoding mediates the V-shape recovery.}\nThe monotonic L2 curve versus the non-monotonic random curve on $\\pi_{0.5}$ Long (Figure~\\ref{fig:cliff_highlight}) reflects an interaction between token selection strategy and positional encoding. L2 norm scoring preserves spatial locality: retained tokens form near-contiguous clusters in the ViT grid, producing continuous position shifts after re-indexing that Gemma's RoPE accommodates smoothly---hence monotonic degradation (86.8\\% $\\to$ 51.7\\% from $k{=}0.95$ to $k{=}0.5$). Random selection creates scattered gaps that produce position aliasing after re-indexing. At $k{\\approx}0.9$, the aliasing is maximally destructive: a small number of randomly placed gaps create highly irregular inter-token spacing, collapsing SR to 33.6\\%. Per-task analysis reveals this aggregate is driven by specific tasks with position-sensitive spatial reasoning: Task~4 (``put mugs on plates'') drops from 80\\% at $k{=}0.7$ to 12\\% at $k{=}0.85$, contributing disproportionately to the V-shape minimum. At $k{=}0.7$, enough tokens are removed that the surviving positions become approximately uniform again, and SR recovers to 64.6\\%---exceeding the $k{=}0.9$ level by ${\\sim}2{\\times}$. The zero-mask ablation (Section~\\ref{sec:zeromask}) provides causal confirmation: zeroing token content while preserving positions yields 98.0\\% SR, while physically removing the same tokens collapses to 9.0\\%. Position encoding, not information content, is the binding constraint---and scoring method determines whether that constraint is violated.\n\n\\paragraph{Per-task reversal within L2-dominant regimes.} The Long $k{=}0.85$ aggregate ($+$33.2\\,pp for L2) masks extreme per-task heterogeneity (per-task $\\sigma{=}$21.5\\,pp). L2 outperforms random on 9 of 10 tasks ($+$16 to $+$52\\,pp), but on Task~6---a dual-object spatial-relation task (``place white mug on plate \\emph{and} chocolate pudding to the right of plate'')---L2 collapses to 8\\% while random achieves 52\\% ($-$44\\,pp reversal). L2 scoring systematically undervalues tokens encoding spatial relationships, which carry low norms but are critical for relational reasoning. This per-task sign flip within an architecture where L2 dominates overall reinforces that no single scoring method is universally safe: task semantics, not just connector architecture or suite-level statistics, determine optimal strategy.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_scoring_crossover.pdf}\n\\caption{Scoring method comparison at $k{=}0.9$ across three models and four LIBERO suites. Cell color encodes SR as a fraction of unpruned baseline; blue bars mark the best method per condition; dashed borders indicate method-indifferent cells ($\\Delta{<}3.5$\\,pp). $\\pi_{0.5}$'s linear connector strongly favors L2 selection, while X-VLA's BART encoder is largely method-indifferent. SmolVLA collapses to 0\\% regardless of method. Compact 2$\\times$2 summary in Appendix Table~\\ref{tab:scoring_crossover_summary}.}\n\\label{fig:scoring_crossover}\n\\end{figure}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_margin_profile.pdf}\n\\caption{Importance margin (L2 $-$ Random SR) on $\\pi_{0.5}$ Long across retention ratios (multi-seed mean $\\pm$ s.d.; $n{=}5$). The margin peaks sharply at $k{=}0.9$ (46.8\\,pp) where random pruning is maximally destructive, then declines asymmetrically: one step above the peak ($k{=}0.95$: 25.6\\,pp) versus four steps below before crossing zero at $k{\\approx}0.71$. At $k{=}0.5$, L2 and Random converge ($|\\Delta|{\\approx}1.3$\\,pp), indicating that scoring method choice matters only in the moderate-pruning window.}\n\\label{fig:margin_profile}\n\\end{figure}\n\n\\paragraph{Limitations (extended).}\nAll closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\\pi_{0}$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\\% official, 44.8\\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.\n\n\\paragraph{Non-monotonicity as structural property.}\nX-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\\% (L2) and 54.0\\% (random), while $k{=}0.9$ recovers to 70.2\\% under L2 selection (Table~\\ref{tab:main_results}). The 0.2\\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.\n\n\\paragraph{$\\pi_{0.5}$ random subsampling anomaly and RoPE amplification.}\nRandom selection on $\\pi_{0.5}$ Object collapses from 74.0\\% at $k{=}0.95$ to 9.0\\% at $k{=}0.9$, then recovers to 74.0\\% at $k{=}0.7$ (Table~\\ref{tab:main_results}). The re-indexing step of our pruning protocol (Section~\\ref{sec:pruning_protocol}) contributes to this non-monotonicity. $\\pi_{0.5}$'s linear connector preserves a one-to-one mapping between spatial patches and token positions; when random removal shifts surviving tokens to new positions, the backbone's Rotary Position Embeddings (RoPE)~\\cite{su2024roformer} encode spatial content at unfamiliar positions, amplifying disruption of learned attention patterns. X-VLA's BART encoder, which redistributes spatial information via cross-attention and lacks RoPE, provides a partial control. At $k{=}0.85$, single-step suites degrade smoothly (Spatial~68.2\\%, Object~65.0\\%, Goal~60.4\\%), but Long drops to 35.0\\%, below its $k{=}0.5$ performance of 61.6\\% (Table~\\ref{tab:xvla_k085_crosssuite}). Random re-indexing thus induces non-monotonic behavior for complex tasks even without RoPE, but RoPE amplifies the reversal: $\\pi_{0.5}$ Object drops to 5.6\\% at $k{=}0.85$ versus 69.4\\% at $k{=}0.5$ ($-$63.8\\,pp), more than double X-VLA Long's $-$26.6\\,pp. The V-shaped recovery at $k \\leq 0.7$ remains unexplained.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Random pruning at $k{=}0.85$: X-VLA (BART encoder) vs.\\ $\\pi_{0.5}$ (linear connector). X-VLA degrades smoothly on single-step suites (60--68\\%) but drops to 35.0\\% on Long (below $k{=}0.5$); $\\pi_{0.5}$ exhibits a severe disruption peak on Object.}\n\\label{tab:xvla_k085_crosssuite}\n\\begin{tabular}{lcccc}\n\\toprule\nSuite & X-VLA SR (\\%) & $\\Delta$ & $\\pi_{0.5}$ SR (\\%) & $\\Delta$ \\\\\n\\midrule\nObject & 65.0 & $-$34.2 & 3.6--5.6\\textsuperscript{$\\dagger$} & $-$93 to $-$95 \\\\\nGoal & 60.4 & $-$38.0 & 52.4 & $-$44.0 \\\\\nSpatial & 68.2 & $-$24.8 & --- & --- \\\\\nLong & 35.0 & $-$59.0 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize\\textsuperscript{$\\dagger$}Two seeds: seed42$\\,{=}\\,$5.6\\% (post-fix), seed43$\\,{=}\\,$3.6\\%. $\\Delta$ from respective baselines.}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Small-$N$ interactions.}\nX-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.6\\,pp on Goal and $-$47.0\\,pp on Long (L2 norm selection). Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.\n\n\\paragraph{Design implications.}\nPractitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.\n\n\n\\section{Cross-Suite Task Complexity Analysis}\n\\label{app:cross_suite_extended}\n\nLIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.\n\n$\\pi_{0.5}$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\\% (matching the baseline), Spatial retains 97.8\\% (within noise of the 97.2\\% baseline), and Goal drops to 89.4\\% ($-$7.0\\,pp from 96.4\\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\\% token removal.\n\nX-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 99.2\\% (matching the 99.2\\% baseline), while Goal drops to 70.2\\% ($-$28.2\\,pp from 98.4\\% baseline). Under random pruning at the same ratio, Object loses just 1.4\\,pp (97.8\\%) while Goal loses 27.8\\,pp (70.6\\%), a $20{\\times}$ amplification. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\\% to 47.0\\% (L2) and 48.2\\% (random), a 47.0\\,pp loss with only 1.2\\,pp method gap, while Object at the same ratio loses only 0.2\\,pp.\n\nToken-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\\pi_{0.5}$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.\n\n\n\\section{Pruning Protocol Details}\n\\label{app:pruning_details}\n\nBoth pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\\pi_{0.5}$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\\ three-layer MLP), backbone (PaliGemma vs.\\ Llama-2), and encoder fusion strategy (single SigLIP vs.\\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.\n\n\n\\section{SmolVLA Pruning Ablation}\n\\label{app:smolvla_ablation}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\\% SR. Two independent evaluations of the official HF checkpoint (59.2\\% and 57.2\\% baseline, within CI) confirm the cliff-edge across scoring methods.}\n\\label{tab:smolvla_ablation}\n\\begin{tabular}{llccrr}\n\\toprule\nScoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\\\\n\\midrule\nACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\\\\nACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint, eval protocol A (59.2\\% baseline)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\\\\nRandom & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint, eval protocol B (57.2\\% baseline)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 57.2 & 500 & [52.9, 61.4] \\\\\nRandom & 0.95 & True removal & 0.0 & 500 & [0, 0.76] \\\\\nL2 norm & 0.90 & True removal & 0.0 & 500 & [0, 0.76] \\\\\nL2 norm & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task Breakdown Tables}\n\\label{app:per_task}\n\n\\subsection{SmolVLA Baseline Per-Task Results}\n\nTable~\\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\\ref{tab:smolvla_ablation}) produce 0\\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\\% already reported.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\\%.}\n\\label{tab:smolvla_baseline_pertask}\n\\begin{tabular}{lc}\n\\toprule\nTask & SR (\\%) \\\\\n\\midrule\nalphabet\\_soup & 22 \\\\\nbbq\\_sauce & 60 \\\\\nbutter & 42 \\\\\nchocolate\\_pudding & 38 \\\\\ncream\\_cheese & 58 \\\\\nketchup & 26 \\\\\nmilk & 62 \\\\\norange\\_juice & 38 \\\\\nsalad\\_dressing & 50 \\\\\ntomato\\_sauce & 52 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{44.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Official SmolVLA Checkpoint Per-Task Results}\n\nTable~\\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\\_libero). Under 50\\% random token removal, all tasks produce 0\\% SR, identical to the fine-tuned checkpoint results.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\\%. Under 50\\% random pruning, all tasks collapse to 0\\%. An independent evaluation (protocol B) yields 57.2\\% baseline with identical cliff-edge (Table~\\ref{tab:smolvla_ablation}).}\n\\label{tab:smolvla_official_pertask}\n\\begin{tabular}{lcc}\n\\toprule\nTask & Baseline SR (\\%) & $k{=}0.5$ SR (\\%) \\\\\n\\midrule\nalphabet\\_soup & 64 & 0 \\\\\nbbq\\_sauce & 38 & 0 \\\\\nbutter & 78 & 0 \\\\\nchocolate\\_pudding & 90 & 0 \\\\\ncream\\_cheese & 40 & 0 \\\\\nketchup & 60 & 0 \\\\\nmilk & 52 & 0 \\\\\norange\\_juice & 80 & 0 \\\\\nsalad\\_dressing & 44 & 0 \\\\\ntomato\\_sauce & 46 & 0 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{59.2} & \\textbf{0.0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{OpenVLA Per-Task Results Under Pruning}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA per-task success rates (\\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\\%. Tasks requiring fine-grained discrimination (butter, cream\\_cheese) degrade earliest; visually distinctive targets (orange\\_juice, salad\\_dressing) are most resilient.}\n\\label{tab:openvla_pertask}\n\\begin{tabular}{lccccc}\n\\toprule\nTask & $k{=}0.95$ & $k{=}0.90$ & $k{=}0.70$ & $k{=}0.50$ & $k{=}0.30$ \\\\\n\\midrule\nalphabet\\_soup & 76 & 70 & 74 & 60 & 14 \\\\\nbbq\\_sauce & 38 & 28 & 46 & 44 & 30 \\\\\nbutter & 84 & 76 & 10 & 2 & 0 \\\\\nchocolate\\_pudding & 54 & 56 & 32 & 40 & 10 \\\\\ncream\\_cheese & 84 & 78 & 18 & 8 & 0 \\\\\nketchup & 82 & 70 & 68 & 50 & 30 \\\\\nmilk & 46 & 42 & 40 & 24 & 8 \\\\\norange\\_juice & 74 & 60 & 76 & 72 & 42 \\\\\nsalad\\_dressing & 64 & 54 & 64 & 36 & 64 \\\\\ntomato\\_sauce & 92 & 86 & 62 & 38 & 8 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{69.4} & \\textbf{62.0} & \\textbf{49.0} & \\textbf{37.4} & \\textbf{20.6} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{OpenVLA Full Degradation Curve}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA success rates on LIBERO-Object under random token removal at six retention ratios (50 episodes per task, 500 total per ratio). Baseline SR: 74.0\\%. All confidence intervals are Wilson 95\\%.}\n\\label{tab:openvla_full}\n\\begin{tabular}{ccrr}\n\\toprule\n$k$ & Tokens Retained & SR (\\%) & Wilson 95\\% CI \\\\\n\\midrule\n1.00 (baseline) & 256 & 74.0 & [69.9, 77.7] \\\\\n0.95 & 243 & 69.4 & [65.2, 73.3] \\\\\n0.90 & 230 & 62.0 & [57.7, 66.2] \\\\\n0.70 & 179 & 49.0 & [44.6, 53.4] \\\\\n0.50 & 128 & 37.4 & [33.3, 41.7] \\\\\n0.30 & 77 & 20.6 & [17.2, 24.4] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$\\pi_{0.5}$ LIBERO-Long Five-Seed Results}\n\\label{app:pi05_long_multiseed}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ LIBERO-Long success rates (\\%) across five seeds (500 episodes each). All values are means over seeds 42--46 with sample standard deviation (ddof$\\,{=}\\,$1). The importance margin (L2$-$Random) peaks at $k{=}0.9$ (46.8\\,pp) and crosses zero near $k{\\approx}0.71$. Maximum per-seed range is 5.8\\,pp (L2, $k{=}0.75$).}\n\\label{tab:pi05_long_multiseed}\n\\begin{tabular}{cccc}\n\\toprule\n$k$ & L2 Norm (\\%) & Random (\\%) & Attention (\\%) \\\\\n\\midrule\n0.95 & $86.8 \\pm 0.8$ & $61.2 \\pm 0.7$ & $77.3 \\pm 1.2$ \\\\",
      "numLines": 300,
      "startLine": 1,
      "totalLines": 938
    }
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of the bib entries and their usage in the tex files. Let me read the full grep output for all citations, and then proceed with WebSearch verification for each entry.

Let me compile the complete list of bib entries first:

1. abnar2020quantifying - "Quantifying Attention Flow in Transformers" - Abnar, Zuidema - ACL 2020
2. gao2025compressorvla - "Compressor-VLA..." - Gao et al. - arXiv 2511.18950 - 2025


3. wang2025specprunevla - "SpecPrune-VLA..." - Wang et al. - arXiv 2509.05614 - 2025
4. jiang2026lightvla - "The Better You Learn, The Smarter You Prune..." - Jiang et al. - ICRA 2026 - arXiv 2509.12594
5. feng2026seewhatmatters - "See What Matters..." - Feng et al. - ICML 2026 - arXiv 2605.11817
6. zhang2025sparsevlm - "SparseVLM..." - Zhang et al. - continuing to gather the remaining entries with their publication venues and identifiers. Adding more papers... Continuing through more recent vision-language and efficiency papers, including VLA variants, dynamic vision transformers for token optimization, and robotics datasets like LIBERO. Continuing through the bibliography with more recent vision-language and foundational model papers, including work on model compression, vision encoders, and loss functions for contrastive learning. Continuing through the bibliography with TinyVLA, BART, and several vision transformer optimization papers like TokenLearner, A-ViT, AdaViT, and SparseViT that focus on token reduction and efficiency improvements.

Now adding more recent work on model pruning and vision-language models, including Fit and Prune, CrossGET, faster VLM approaches, LLaVA improvements, and InternVL expansions that push performance boundaries. Continuing through the bibliography with entries on embodied AI systems like CALVIN and Diffusion Policy, time series forecasting research, and a position paper on negative results in machine learning, though I notice DINOv2 appears to be duplicated from earlier in the list.

Now I'm spotting some potential duplicates—both Brohan and Zitkovich claim RT-2 at CoRL 2023, which needs verification. Let me extract all the citation keys actually used in the tex files to see which references are genuinely cited versus which might be orphaned entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "3194a4d9-77b9-41d0-a31b-d9004a1789f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBtkZNsrs3WWLyFBgWPMVt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10752,
      "cache_read_input_tokens": 62508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10752
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

_source line 46_

Let me read the full grep output and check which entries are actually cited.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "7a2ce6ab-9a4f-4332-b5f6-4b47582b26f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBtkZNsrs3WWLyFBgWPMVt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10752,
      "cache_read_input_tokens": 62508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10752
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

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01NKJv7n6sPn9aH7TGzYfc3u`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tool-results/toolu_01F8KqJcAmocH9xZuS1tuny4.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "b528cd17-d84d-4e5b-ac67-467b647d31f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBtkZNsrs3WWLyFBgWPMVt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10752,
      "cache_read_input_tokens": 62508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10752
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

_source line 48 · 2026-05-29T06:30:49.424Z_

<details><summary>↩ Tool result · `toolu_01NKJv7n6sPn9aH7TGzYfc3u`</summary>

```text
1	docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, Token Merging~\cite{bolya2023tome}, and CrossGET~\cite{shi2024crossget} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
2	docs/paper/related_work.tex:8:[Omitted long matching line]
3	docs/paper/related_work.tex:11:Jabbour et al.~\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.
4	docs/paper/related_work.tex:14:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.
5	docs/paper/experiments.tex:7:\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).
6	docs/paper/experiments.tex:9:\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\ref{tab:model_properties}): $\pi_{0.5}$~\cite{black2025pi05}, X-VLA~\cite{zheng2025xvla}, OpenVLA~\cite{kim2024openvla}, and SmolVLA~\cite{shukor2025smolvla}. Two additional models ($\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.
7	docs/paper/results_v2.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
8	docs/paper/results_v2.tex:9:[Omitted long matching line]
9	docs/paper/results_v2.tex:11:[Omitted long matching line]
10	docs/paper/results_v2.tex:16:[Omitted long matching line]
11	docs/paper/results_v2.tex:22:$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
12	docs/paper/results_v2.tex:23:$\pi_0.5$~\cite{black2025pi05} & Linear proj ($\times\!\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\%, R$=$69.4\% ($\Delta{=}$+36pp) & Uniformly critical \\
13	docs/paper/results_v2.tex:24:X-VLA~\cite{zheng2025xvla} & Linear proj$^\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\pm}0.4$, $k{=}0.85$: $67.8$ & Threshold-graded \\
14	docs/paper/results_v2.tex:25:OpenVLA~\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\% SR ($-$49\%) & Smooth graded \\
15	docs/paper/results_v2.tex:26:OFT~\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \approx 0.215$; Ent.\ $0.667 \approx 0.661$$^\S$ & Smooth graded \\
16	docs/paper/results_v2.tex:27:CogACT~\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\% SR under 78\% prune$^\|$ & Smooth graded \\
17	docs/paper/results_v2.tex:28:SmolVLA~\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\% SR & Catastrophic cliff \\
18	docs/paper/results_v2.tex:45:OFT~\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, determines token importance structure. EfficientVLA~\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\cite{li2024cogact} (MLP projector) retains 74.2\% SR under 78\% pruning.
19	docs/paper/sections/analysis.tex:21:DynamicViT~\cite{rao2021dynamicvit} and ToMe~\cite{bolya2023tome} exploit this concentration: tokens that receive low attention contribute little to the classification decision and can be safely removed.
20	docs/paper/sections/analysis.tex:24:We extract attention weights from the LLM backbone (Qwen2-0.5B~\cite{yang2024qwen2}) over all vision tokens across three LIBERO tasks.
21	docs/paper/sections/analysis.tex:31:SigLIP~\cite{zhai2023siglip} encodes images using non-overlapping spatial patches without a \texttt{[CLS]} aggregation token.
22	docs/paper/sections/analysis.tex:123:In ViT classification, attention concentrates on a small subset of discriminative patches~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}.
23	docs/paper/sections/analysis.tex:129:SigLIP~\cite{zhai2023siglip} encodes each non-overlapping spatial patch as a separate token with no \texttt{[CLS]} aggregation, so the VLA's LLM backbone must attend to all patches to reconstruct spatial relationships between the robot end-effector, target objects, and obstacles.
24	docs/paper/sections/related_work_draft.tex:6:[Omitted long matching line]
25	docs/paper/sections/related_work_draft.tex:8:[Omitted long matching line]
26	docs/paper/sections/related_work_draft.tex:12:[Omitted long matching line]
27	docs/paper/sections/related_work_draft.tex:14:[Omitted long matching line]
28	docs/paper/sections/related_work_draft.tex:20:[Omitted long matching line]
29	docs/paper/sections/related_work_draft.tex:22:[Omitted long matching line]
30	docs/paper/sections/related_work_draft.tex:24:[Omitted long matching line]
31	docs/paper/sections/related_work_draft.tex:28:[Omitted long matching line]
32	docs/paper/sections/experiments.tex:17:DynamicViT~\cite{rao2021dynamicvit} removes 30\%--50\% of tokens with less than 0.5\% accuracy loss on ImageNet, and Token Merging (ToMe)~\cite{bolya2023tome} merges up to 40\% of tokens while retaining over 99\% of classification accuracy.
33	docs/paper/sections/experiments.tex:18:EViT~\cite{liang2022evit} similarly discards 50\% of inattentive tokens with negligible degradation.
34	docs/paper/sections/experiments.tex:19:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\cite{xu2025vlacache,cheng2026vlaiap}.
35	docs/paper/sections/experiments.tex:20:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\cite{liu2023libero}.
36	docs/paper/sections/experiments.tex:66:Token merging (following ToMe~\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.
37	docs/paper/sections/experiments.tex:73:\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\% accuracy on classification benchmarks even at aggressive retention ratios~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}
38	docs/paper/sections/results_draft.tex:4:We evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\% confidence intervals.
39	docs/paper/sections/results_draft.tex:9:[Omitted long matching line]
40	docs/paper/sections/results_draft.tex:12:[Omitted long matching line]
41	docs/paper/sections/results_draft.tex:59:OpenVLA~\cite{kim2024openvla} uses a two-layer MLP projector to map vision encoder outputs (from DINOv2 and SigLIP~\cite{zhai2023siglip}) into the Llama-2 language model's embedding space. Unlike pixel-shuffle, the MLP projector processes each patch token independently through a shared linear transformation. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence.
42	docs/paper/appendix.tex:91:[Omitted long matching line]
43	docs/paper/appendix.tex:94:[Omitted long matching line]
44	docs/paper/appendix.tex:138:[Omitted long matching line]
45	docs/paper/appendix.tex:748:X-VLA's 12-layer BART encoder~\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\,pp), confirming it as an architectural property.
46	docs/paper/appendix.tex:750:MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\% SR under 78\% pruning).
47	docs/paper/appendix.tex:878:Table~\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\_last), mean attention across all decoder layers (attn\_mean), and attention rollout~\cite{abnar2020quantifying}.
48	docs/paper/experimental_setup.tex:9:[Omitted long matching line]
49	docs/paper/experimental_setup.tex:11:We evaluate on LIBERO~\cite{liu2023libero} (Object: 10 tasks $\times$ 50 episodes = 500 total; Spatial and Goal for cross-suite validation). Closed-loop success rate (SR) with Wilson 95\% CIs is the primary metric; multi-seed results report mean $\pm$ std. Baselines: SmolVLA 44.8\%, OpenVLA 74.0\%, X-VLA 99.2\%, $\pi_0.5$ 98.2\%.
50	docs/paper/introduction.tex:14:[Omitted long matching line]
51	docs/paper/introduction.tex:16:[Omitted long matching line]
52	docs/paper/results.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
53	docs/paper/results.tex:9:[Omitted long matching line]
54	docs/paper/results.tex:11:[Omitted long matching line]
55	docs/paper/results.tex:16:[Omitted long matching line]
56	docs/paper/results.tex:22:$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
57	docs/paper/results.tex:23:$\pi_0.5$~\cite{black2025pi05} & Linear proj ($\times\!\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\%, R$=$69.4\% ($\Delta{=}$+36pp) & Uniformly critical \\
58	docs/paper/results.tex:24:X-VLA~\cite{zheng2025xvla} & Linear + BART (12L)$^\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\pm}0.4$, $k{=}0.85$: $67.9{\pm}0.3$ & Threshold-graded \\
59	docs/paper/results.tex:25:OpenVLA~\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\% SR ($-$49\%) & Smooth graded \\
60	docs/paper/results.tex:26:OFT~\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \approx 0.215$; Ent.\ $0.667 \approx 0.661$$^\S$ & Smooth graded \\
61	docs/paper/results.tex:27:CogACT~\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\% SR under 78\% prune$^\|$ & Smooth graded \\
62	docs/paper/results.tex:28:SmolVLA~\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\% SR & Catastrophic cliff \\
63	docs/paper/results.tex:45:OFT~\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\cite{li2024cogact} (MLP projector) retains 74.2\% SR under 78\% pruning.
64	docs/paper/sections/background.tex:6:This section describes the two components of our experimental setup: the SmolVLA architecture~\cite{shukor2025smolvla}, in which we study vision token reduction, and the LIBERO benchmark~\cite{liu2023libero}, on which we evaluate closed-loop performance.
65	docs/paper/sections/background.tex:12:SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a modality connector, a language model backbone, and an action head.
66	docs/paper/sections/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
67	docs/paper/sections/background.tex:41:The Qwen2-0.5B language model~\cite{yang2024qwen2} serves as the central reasoning module.
68	docs/paper/sections/background.tex:47:SmolVLA generates actions through conditional flow matching~\cite{lipman2023flow} rather than autoregressive token prediction.
69	docs/paper/sections/background.tex:54:This architecture shares its high-level structure with larger VLA systems such as OpenVLA~\cite{kim2024openvla} and $\pi_0$~\cite{black2024pi0}, making SmolVLA a representative testbed for studying vision token efficiency in VLA policies.
70	docs/paper/sections/background.tex:59:We evaluate on the LIBERO benchmark~\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.
71	docs/paper/sections/experimental_setup.tex:33:  \item \textbf{Token merge}: following the bipartite matching strategy of ToMe~\cite{bolya2023tome}, each pruned token is merged with its nearest retained neighbor by averaging their embeddings. Sequence length and total information content are both preserved.
72	docs/paper/sections/introduction.tex:7:DynamicViT~\cite{rao2021dynamicvit} removes 66\% of patch tokens with less than 0.5\% accuracy loss on ImageNet classification.
73	docs/paper/sections/introduction.tex:8:Token Merging (ToMe)~\cite{bolya2023tome} merges 40\% of tokens while retaining over 99\% of classification accuracy.
74	docs/paper/sections/introduction.tex:9:EViT~\cite{liang2022evit} discards 50\% of inattentive tokens with negligible degradation.
75	docs/paper/sections/introduction.tex:12:Vision-Language-Action (VLA) models~\cite{brohan2023rt2,kim2024openvla,black2024pi0,shukor2025smolvla} use the same ViT encoders as their visual front-ends, producing hundreds of patch tokens that dominate the input sequence to the language model backbone.
76	docs/paper/sections/introduction.tex:17:Current VLA models such as RT-2~\cite{brohan2023rt2} and $\pi_0$~\cite{black2024pi0} use large vision encoders that produce 256 or more tokens per image.
77	docs/paper/sections/introduction.tex:20:SmolVLA~\cite{shukor2025smolvla}, a compact 451.5M-parameter VLA, produces 256 vision tokens from two cameras (128 per view), and these tokens constitute the majority of the LLM backbone's input sequence.
78	docs/paper/sections/introduction.tex:23:FastV~\cite{chen2024fastv} identifies and prunes inattentive visual tokens in VLM inference, achieving 2$\times$ speedup with minimal quality loss on VLM benchmarks.
79	docs/paper/sections/introduction.tex:24:VLA-Cache~\cite{xu2025vlacache} caches vision tokens across timesteps to reduce redundant computation in temporal sequences.
80	docs/paper/sections/introduction.tex:25:VLA-IAP~\cite{cheng2026vlaiap} proposes importance-aware pruning for VLA inference acceleration.
81	docs/paper/sections/introduction.tex:30:Existing evaluations of VLM token reduction rely on offline metrics such as action loss, perplexity, or next-token prediction accuracy~\cite{chen2024fastv,cheng2026vlaiap}.
82	docs/paper/sections/introduction.tex:38:Using SmolVLA on the LIBERO benchmark~\cite{liu2023libero}, we test six pruning configurations spanning three axes: scoring function (a trained Attention-Conditioned Importance Scorer versus random selection), retention ratio ($k \in \{0.5, 0.7, 0.9\}$), and mechanism (zero-masking, true removal, and token merging).
83	docs/paper/sections/introduction.tex:50:This uniformity arises because SigLIP~\cite{zhai2023siglip} encodes non-overlapping spatial patches without a \texttt{[CLS]} aggregation token; each token carries unique, irreplaceable spatial information about the scene.
84	docs/paper/sections/introduction.tex:59:We believe this negative result~\cite{karl2024negative,zeng2023transformers_tsf} carries important implications for the VLA efficiency community: future work on VLA compression should seek alternatives to naive token removal, such as training-time distillation into fewer tokens or architectural modifications that build in spatial redundancy.
85	docs/paper/method.tex:7:[Omitted long matching line]
86	docs/paper/background.tex:6:This section describes the architectures and benchmark used in our study: SmolVLA~\cite{shukor2025smolvla} and OpenVLA~\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\cite{liu2023libero} on which we evaluate closed-loop performance.
87	docs/paper/background.tex:12:SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 450M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.
88	docs/paper/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
89	docs/paper/background.tex:36:The Qwen2-0.5B language model~\cite{yang2024qwen2} serves as the central reasoning module.
90	docs/paper/background.tex:41:SmolVLA generates actions through conditional flow matching~\cite{lipman2023flow} rather than autoregressive token prediction.
91	docs/paper/background.tex:49:OpenVLA~\cite{kim2024openvla} is a 7B-parameter VLA built on the Llama-2 backbone. Its vision pipeline differs from SmolVLA in two respects that are directly relevant to compressibility.
92	docs/paper/background.tex:52:OpenVLA uses a dual encoder combining DINOv2~\cite{oquab2023dinov2} and SigLIP~\cite{zhai2023siglip}. The two encoders produce complementary representations (self-supervised spatial features and language-aligned features) that are concatenated per patch position.
93	docs/paper/background.tex:63:We evaluate on the LIBERO benchmark~\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.
94	docs/paper/experiments_deprecated.tex:6:DynamicViT~\cite{rao2021dynamicvit} removes 30\%--50\% of tokens with less than 0.5\% accuracy loss on ImageNet, and Token Merging (ToMe)~\cite{bolya2023tome} merges up to 40\% of tokens while retaining over 99\% of classification accuracy.
95	docs/paper/experiments_deprecated.tex:7:EViT~\cite{liang2022evit} similarly discards 50\% of inattentive tokens with negligible degradation.
96	docs/paper/experiments_deprecated.tex:8:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\cite{xu2025vlacache,cheng2026vlaiap}.
97	docs/paper/experiments_deprecated.tex:9:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\cite{liu2023libero}.
98	docs/paper/experiments_deprecated.tex:55:Token merging (following ToMe~\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.
99	docs/paper/experiments_deprecated.tex:62:\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\% accuracy on classification benchmarks even at aggressive retention ratios~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "5c35a258-06f8-4d49-991a-0a83008d9da7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tool-results/toolu_01F8KqJcAmocH9xZuS1tuny4.txt",
      "content": "docs/paper/related_work.tex:5:DynamicViT~\\cite{rao2021dynamicvit}, EViT~\\cite{liang2022evit}, A-ViT~\\cite{yin2022avit}, Token Merging~\\cite{bolya2023tome}, and CrossGET~\\cite{shi2024crossget} remove 50--66\\% of tokens with under 0.5\\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.\ndocs/paper/related_work.tex:8:[Omitted long matching line]\ndocs/paper/related_work.tex:11:Jabbour et al.~\\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.\ndocs/paper/related_work.tex:14:LLaVA~\\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.\ndocs/paper/experiments.tex:7:\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\ndocs/paper/experiments.tex:9:\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\ndocs/paper/results_v2.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\ndocs/paper/results_v2.tex:9:[Omitted long matching line]\ndocs/paper/results_v2.tex:11:[Omitted long matching line]\ndocs/paper/results_v2.tex:16:[Omitted long matching line]\ndocs/paper/results_v2.tex:22:$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\ndocs/paper/results_v2.tex:23:$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\ndocs/paper/results_v2.tex:24:X-VLA~\\cite{zheng2025xvla} & Linear proj$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.8$ & Threshold-graded \\\\\ndocs/paper/results_v2.tex:25:OpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\ndocs/paper/results_v2.tex:26:OFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\ndocs/paper/results_v2.tex:27:CogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\ndocs/paper/results_v2.tex:28:SmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\ndocs/paper/results_v2.tex:45:OFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, determines token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\ndocs/paper/sections/analysis.tex:21:DynamicViT~\\cite{rao2021dynamicvit} and ToMe~\\cite{bolya2023tome} exploit this concentration: tokens that receive low attention contribute little to the classification decision and can be safely removed.\ndocs/paper/sections/analysis.tex:24:We extract attention weights from the LLM backbone (Qwen2-0.5B~\\cite{yang2024qwen2}) over all vision tokens across three LIBERO tasks.\ndocs/paper/sections/analysis.tex:31:SigLIP~\\cite{zhai2023siglip} encodes images using non-overlapping spatial patches without a \\texttt{[CLS]} aggregation token.\ndocs/paper/sections/analysis.tex:123:In ViT classification, attention concentrates on a small subset of discriminative patches~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}.\ndocs/paper/sections/analysis.tex:129:SigLIP~\\cite{zhai2023siglip} encodes each non-overlapping spatial patch as a separate token with no \\texttt{[CLS]} aggregation, so the VLA's LLM backbone must attend to all patches to reconstruct spatial relationships between the robot end-effector, target objects, and obstacles.\ndocs/paper/sections/related_work_draft.tex:6:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:8:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:12:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:14:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:20:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:22:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:24:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:28:[Omitted long matching line]\ndocs/paper/sections/experiments.tex:17:DynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/sections/experiments.tex:18:EViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/sections/experiments.tex:19:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{xu2025vlacache,cheng2026vlaiap}.\ndocs/paper/sections/experiments.tex:20:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\ndocs/paper/sections/experiments.tex:66:Token merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\ndocs/paper/sections/experiments.tex:73:\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}\ndocs/paper/sections/results_draft.tex:4:We evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\\% confidence intervals.\ndocs/paper/sections/results_draft.tex:9:[Omitted long matching line]\ndocs/paper/sections/results_draft.tex:12:[Omitted long matching line]\ndocs/paper/sections/results_draft.tex:59:OpenVLA~\\cite{kim2024openvla} uses a two-layer MLP projector to map vision encoder outputs (from DINOv2 and SigLIP~\\cite{zhai2023siglip}) into the Llama-2 language model's embedding space. Unlike pixel-shuffle, the MLP projector processes each patch token independently through a shared linear transformation. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence.\ndocs/paper/appendix.tex:91:[Omitted long matching line]\ndocs/paper/appendix.tex:94:[Omitted long matching line]\ndocs/paper/appendix.tex:138:[Omitted long matching line]\ndocs/paper/appendix.tex:748:X-VLA's 12-layer BART encoder~\\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\\,pp), confirming it as an architectural property.\ndocs/paper/appendix.tex:750:MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\\% SR under 78\\% pruning).\ndocs/paper/appendix.tex:878:Table~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.\ndocs/paper/experimental_setup.tex:9:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:11:We evaluate on LIBERO~\\cite{liu2023libero} (Object: 10 tasks $\\times$ 50 episodes = 500 total; Spatial and Goal for cross-suite validation). Closed-loop success rate (SR) with Wilson 95\\% CIs is the primary metric; multi-seed results report mean $\\pm$ std. Baselines: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%.\ndocs/paper/introduction.tex:14:[Omitted long matching line]\ndocs/paper/introduction.tex:16:[Omitted long matching line]\ndocs/paper/results.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\ndocs/paper/results.tex:9:[Omitted long matching line]\ndocs/paper/results.tex:11:[Omitted long matching line]\ndocs/paper/results.tex:16:[Omitted long matching line]\ndocs/paper/results.tex:22:$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\ndocs/paper/results.tex:23:$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\ndocs/paper/results.tex:24:X-VLA~\\cite{zheng2025xvla} & Linear + BART (12L)$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.9{\\pm}0.3$ & Threshold-graded \\\\\ndocs/paper/results.tex:25:OpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\ndocs/paper/results.tex:26:OFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\ndocs/paper/results.tex:27:CogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\ndocs/paper/results.tex:28:SmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\ndocs/paper/results.tex:45:OFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\ndocs/paper/sections/background.tex:6:This section describes the two components of our experimental setup: the SmolVLA architecture~\\cite{shukor2025smolvla}, in which we study vision token reduction, and the LIBERO benchmark~\\cite{liu2023libero}, on which we evaluate closed-loop performance.\ndocs/paper/sections/background.tex:12:SmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a modality connector, a language model backbone, and an action head.\ndocs/paper/sections/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\ndocs/paper/sections/background.tex:41:The Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\ndocs/paper/sections/background.tex:47:SmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\ndocs/paper/sections/background.tex:54:This architecture shares its high-level structure with larger VLA systems such as OpenVLA~\\cite{kim2024openvla} and $\\pi_0$~\\cite{black2024pi0}, making SmolVLA a representative testbed for studying vision token efficiency in VLA policies.\ndocs/paper/sections/background.tex:59:We evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\ndocs/paper/sections/experimental_setup.tex:33:  \\item \\textbf{Token merge}: following the bipartite matching strategy of ToMe~\\cite{bolya2023tome}, each pruned token is merged with its nearest retained neighbor by averaging their embeddings. Sequence length and total information content are both preserved.\ndocs/paper/sections/introduction.tex:7:DynamicViT~\\cite{rao2021dynamicvit} removes 66\\% of patch tokens with less than 0.5\\% accuracy loss on ImageNet classification.\ndocs/paper/sections/introduction.tex:8:Token Merging (ToMe)~\\cite{bolya2023tome} merges 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/sections/introduction.tex:9:EViT~\\cite{liang2022evit} discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/sections/introduction.tex:12:Vision-Language-Action (VLA) models~\\cite{brohan2023rt2,kim2024openvla,black2024pi0,shukor2025smolvla} use the same ViT encoders as their visual front-ends, producing hundreds of patch tokens that dominate the input sequence to the language model backbone.\ndocs/paper/sections/introduction.tex:17:Current VLA models such as RT-2~\\cite{brohan2023rt2} and $\\pi_0$~\\cite{black2024pi0} use large vision encoders that produce 256 or more tokens per image.\ndocs/paper/sections/introduction.tex:20:SmolVLA~\\cite{shukor2025smolvla}, a compact 451.5M-parameter VLA, produces 256 vision tokens from two cameras (128 per view), and these tokens constitute the majority of the LLM backbone's input sequence.\ndocs/paper/sections/introduction.tex:23:FastV~\\cite{chen2024fastv} identifies and prunes inattentive visual tokens in VLM inference, achieving 2$\\times$ speedup with minimal quality loss on VLM benchmarks.\ndocs/paper/sections/introduction.tex:24:VLA-Cache~\\cite{xu2025vlacache} caches vision tokens across timesteps to reduce redundant computation in temporal sequences.\ndocs/paper/sections/introduction.tex:25:VLA-IAP~\\cite{cheng2026vlaiap} proposes importance-aware pruning for VLA inference acceleration.\ndocs/paper/sections/introduction.tex:30:Existing evaluations of VLM token reduction rely on offline metrics such as action loss, perplexity, or next-token prediction accuracy~\\cite{chen2024fastv,cheng2026vlaiap}.\ndocs/paper/sections/introduction.tex:38:Using SmolVLA on the LIBERO benchmark~\\cite{liu2023libero}, we test six pruning configurations spanning three axes: scoring function (a trained Attention-Conditioned Importance Scorer versus random selection), retention ratio ($k \\in \\{0.5, 0.7, 0.9\\}$), and mechanism (zero-masking, true removal, and token merging).\ndocs/paper/sections/introduction.tex:50:This uniformity arises because SigLIP~\\cite{zhai2023siglip} encodes non-overlapping spatial patches without a \\texttt{[CLS]} aggregation token; each token carries unique, irreplaceable spatial information about the scene.\ndocs/paper/sections/introduction.tex:59:We believe this negative result~\\cite{karl2024negative,zeng2023transformers_tsf} carries important implications for the VLA efficiency community: future work on VLA compression should seek alternatives to naive token removal, such as training-time distillation into fewer tokens or architectural modifications that build in spatial redundancy.\ndocs/paper/method.tex:7:[Omitted long matching line]\ndocs/paper/background.tex:6:This section describes the architectures and benchmark used in our study: SmolVLA~\\cite{shukor2025smolvla} and OpenVLA~\\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\\cite{liu2023libero} on which we evaluate closed-loop performance.\ndocs/paper/background.tex:12:SmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 450M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.\ndocs/paper/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\ndocs/paper/background.tex:36:The Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\ndocs/paper/background.tex:41:SmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\ndocs/paper/background.tex:49:OpenVLA~\\cite{kim2024openvla} is a 7B-parameter VLA built on the Llama-2 backbone. Its vision pipeline differs from SmolVLA in two respects that are directly relevant to compressibility.\ndocs/paper/background.tex:52:OpenVLA uses a dual encoder combining DINOv2~\\cite{oquab2023dinov2} and SigLIP~\\cite{zhai2023siglip}. The two encoders produce complementary representations (self-supervised spatial features and language-aligned features) that are concatenated per patch position.\ndocs/paper/background.tex:63:We evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\ndocs/paper/experiments_deprecated.tex:6:DynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/experiments_deprecated.tex:7:EViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/experiments_deprecated.tex:8:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{xu2025vlacache,cheng2026vlaiap}.\ndocs/paper/experiments_deprecated.tex:9:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\ndocs/paper/experiments_deprecated.tex:55:Token merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\ndocs/paper/experiments_deprecated.tex:62:\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}",
      "numLines": 99,
      "startLine": 1,
      "totalLines": 99
    }
  }
}
```

</details>

---

### Assistant

_source line 49_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of all citations used. Let me also note there's a citation to `karl2024negative` in `sections/introduction.tex` line 59 that doesn't appear in the bib file! That's a problem, though those sections may be drafts.

Let me identify all the unique cite keys used in the main paper files (not draft/deprecated):
- Main files included in main.tex: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex

From these main files, the cited keys are:
1. rao2021dynamicvit


2. liang2022evit
3. yin2022avit
4. bolya2023tome
5. shi2024crossget
6. chen2024fastv
7. shang2024prumerge
8. zhang2025sparsevlm
9. khaki2025sparsevila
10. ye2025fitprune
11. cheng2026vlaiap
12. xu2025vlacache
13. yang2025efficientvla
14. liu2025vlapruner
15. jiang2026lightvla
16. gao2025compressorvla
17. wang2025specprunevla
18. feng2026

seewhatmatters
19. jabbour2025dontrun
20. liu2023llava
21. li2023blip2
22. shi2016subpixel
23. liu2023libero
24. black2025pi05
25. zheng2025xvla
26. kim2024openvla
27. shukor2025smolvla
28. black2024pi0
29. kim2025openoft
30. li2024cogact
31. yang2024qwen2
32. lipman2023flow
33. zhai2023siglip
34. oquab2023dinov2
35. lewis2020bart
36. su2024roformer
37. abnar2020quantifying

Now I'm checking which bibliography entries are actually cited in the paper versus which ones are sitting unused. I notice brohan2023rt2 appears in the introduction section but isn't referenced in the main paper files I've been tracking.

Looking at the main.tex structure, it includes abstract, introduction, related_work, method, experiments, conclusion, limitations, and appendix from the docs/paper directory—not the draft files in docs/paper/sections. So I need to trace through the actual cited keys from introduction.tex and the other included files to see what's really being used versus what's orphaned in the bibliography. I'm cross-referencing the citations across different sections of the paper—experiments and conclusion don't add much new, while the appendix pulls in a few additional references like the attention quantification paper and cognitive action work. Looking at the main.tex structure, it's clear results are integrated into the experiments section rather than being a separate file.

Now I'm scanning through the bibliography to identify entries that aren't actually cited anywhere in the paper—RT-1 and RT-2, Octo, RoboFlamingo, InternVL, Perceiver, and some duplicate or incomplete entries like DINOv2 and LLaVA variants appear to be unused references. I'm noticing that many of these entries appear in draft or deprecated versions of the paper rather than the main version, so I need to be more systematic about this. Let me verify the actual citations used in the main paper and identify any duplicates or unused entries, then use web search to validate the key references across all 62 bibliography entries in parallel batches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "0135b2ad-1aec-45a7-a2ed-ecab375aa7e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkM162ZrB16QhyKUqdRvsM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9522,
      "cache_read_input_tokens": 73260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9522
      },
      "output_tokens": 23,
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

_source line 50_

I now have a full picture of the bib and all citations. I'll verify entries via web search in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "98a103eb-ed18-47b4-bfd2-03de0eb497ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkM162ZrB16QhyKUqdRvsM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9522,
      "cache_read_input_tokens": 73260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9522
      },
      "output_tokens": 23,
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

_source line 51_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SKELkjvrA5b6rqjbDH3kWg`</summary>

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
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "8b07f7a4-bae4-447d-a2eb-6ccd0d2e62b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkM162ZrB16QhyKUqdRvsM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9522,
      "cache_read_input_tokens": 73260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9522
      },
      "output_tokens": 23,
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

_source line 52 · 2026-05-29T06:31:30.977Z_

<details><summary>↩ Tool result · `toolu_01SKELkjvrA5b6rqjbDH3kWg`</summary>

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
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "986033c6-b6f2-45d2-b87e-dbe03cfdf2a6",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  }
}
```

</details>

---

### Assistant

_source line 53_

Now I'll launch parallel agents to verify all 62 bib entries via web search. I'll split them into 4 batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "d05ab488-7721-487c-b13c-5abfd9ed02e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GVs9r5F4VrDB6KQ6RaGwR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 82782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2607
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

_source line 54_

<details open><summary>🔧 Tool call — Agent · `toolu_01RZuCncPC5jZr4xRor2mq6b`</summary>

````json
{
  "description": "Verify bib entries batch 1 (1-16)",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n1. **abnar2020quantifying**: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. ACL 2020, pages 4190-4197.\n\n2. **gao2025compressorvla**: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\" by Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing. arXiv 2511.18950, 2025.\n\n3. **wang2025specprunevla**: \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\" by Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao. arXiv 2509.05614, 2025.\n\n4. **jiang2026lightvla**: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\" by Jiang, Titong et al. ICRA 2026, arXiv 2509.12594.\n\n5. **feng2026seewhatmatters**: \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" by Feng, Yixu et al. ICML 2026, arXiv 2605.11817.\n\n6. **zhang2025sparsevlm**: \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" by Zhang, Yuan et al. ICML 2025, arXiv 2410.04417.\n\n7. **khaki2025sparsevila**: \"SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference\" by Khaki, Samir et al. ICCV 2025, arXiv 2510.17777.\n\n8. **jabbour2025dontrun**: \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" by Jabbour, Jason et al. arXiv 2510.08464, 2025.\n\n9. **li2024roboflamingo**: \"Vision-Language Foundation Models as Effective Robot Imitators\" by Li, Xinghang et al. ICLR 2024, arXiv 2311.01378.\n\n10. **shukor2025smolvla**: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\" by Shukor, Mustafa et al. arXiv 2506.01844, 2025.\n\n11. **kim2024openvla**: \"OpenVLA: An Open-Source Vision-Language-Action Model\" by Kim, Moo Jin et al. CoRL 2024.\n\n12. **brohan2023rt2**: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Brohan, Anthony et al. CoRL 2023.\n\n13. **black2024pi0**: \"π₀: A Vision-Language-Action Flow Model for General Robot Control\" by Black, Kevin et al. arXiv 2410.24164, 2024.\n\n14. **black2025pi05**: \"π₀.₅: a Vision-Language-Action Model with Open-World Generalization\" by Black, Kevin et al. CoRL 2025, PMLR vol 305, pages 17-40, arXiv 2504.16054.\n\n15. **ghosh2024octo**: \"Octo: An Open-Source Generalist Robot Policy\" by Octo Model Team, Ghosh, Dibya et al. RSS 2024.\n\n16. **brohan2023rt1**: \"RT-1: Robotics Transformer for Real-World Control at Scale\" by Brohan, Anthony et al. RSS 2023.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n",
  "run_in_background": true
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "84d5f310-ee67-459d-9852-64252ea29b29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GVs9r5F4VrDB6KQ6RaGwR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 82782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2607
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

_source line 55_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Verify bib entries batch 1 (1-16)",
  "task_type": "local_agent",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n1. **abnar2020quantifying**: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. ACL 2020, pages 4190-4197.\n\n2. **gao2025compressorvla**: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\" by Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing. arXiv 2511.18950, 2025.\n\n3. **wang2025specprunevla**: \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\" by Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao. arXiv 2509.05614, 2025.\n\n4. **jiang2026lightvla**: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\" by Jiang, Titong et al. ICRA 2026, arXiv 2509.12594.\n\n5. **feng2026seewhatmatters**: \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" by Feng, Yixu et al. ICML 2026, arXiv 2605.11817.\n\n6. **zhang2025sparsevlm**: \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" by Zhang, Yuan et al. ICML 2025, arXiv 2410.04417.\n\n7. **khaki2025sparsevila**: \"SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference\" by Khaki, Samir et al. ICCV 2025, arXiv 2510.17777.\n\n8. **jabbour2025dontrun**: \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" by Jabbour, Jason et al. arXiv 2510.08464, 2025.\n\n9. **li2024roboflamingo**: \"Vision-Language Foundation Models as Effective Robot Imitators\" by Li, Xinghang et al. ICLR 2024, arXiv 2311.01378.\n\n10. **shukor2025smolvla**: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\" by Shukor, Mustafa et al. arXiv 2506.01844, 2025.\n\n11. **kim2024openvla**: \"OpenVLA: An Open-Source Vision-Language-Action Model\" by Kim, Moo Jin et al. CoRL 2024.\n\n12. **brohan2023rt2**: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Brohan, Anthony et al. CoRL 2023.\n\n13. **black2024pi0**: \"π₀: A Vision-Language-Action Flow Model for General Robot Control\" by Black, Kevin et al. arXiv 2410.24164, 2024.\n\n14. **black2025pi05**: \"π₀.₅: a Vision-Language-Action Model with Open-World Generalization\" by Black, Kevin et al. CoRL 2025, PMLR vol 305, pages 17-40, arXiv 2504.16054.\n\n15. **ghosh2024octo**: \"Octo: An Open-Source Generalist Robot Policy\" by Octo Model Team, Ghosh, Dibya et al. RSS 2024.\n\n16. **brohan2023rt1**: \"RT-1: Robotics Transformer for Real-World Control at Scale\" by Brohan, Anthony et al. RSS 2023.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n",
  "uuid": "e3bd4a80-2931-4ddd-865d-bbe1db3759c2",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
````

---

### Tool result

_source line 56 · 2026-05-29T06:31:57.771Z_

<details><summary>↩ Tool result · `toolu_01RZuCncPC5jZr4xRor2mq6b`</summary>

```text
Async agent launched successfully.
agentId: a5682b66462dfac8c (internal ID - do not mention to user. Use SendMessage with to: 'a5682b66462dfac8c' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/a5682b66462dfac8c.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "1eda9705-06b1-4344-8094-1320da1adc3c",
  "tool_use_result": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a5682b66462dfac8c",
    "description": "Verify bib entries batch 1 (1-16)",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n1. **abnar2020quantifying**: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. ACL 2020, pages 4190-4197.\n\n2. **gao2025compressorvla**: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\" by Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing. arXiv 2511.18950, 2025.\n\n3. **wang2025specprunevla**: \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\" by Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao. arXiv 2509.05614, 2025.\n\n4. **jiang2026lightvla**: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\" by Jiang, Titong et al. ICRA 2026, arXiv 2509.12594.\n\n5. **feng2026seewhatmatters**: \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" by Feng, Yixu et al. ICML 2026, arXiv 2605.11817.\n\n6. **zhang2025sparsevlm**: \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" by Zhang, Yuan et al. ICML 2025, arXiv 2410.04417.\n\n7. **khaki2025sparsevila**: \"SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference\" by Khaki, Samir et al. ICCV 2025, arXiv 2510.17777.\n\n8. **jabbour2025dontrun**: \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" by Jabbour, Jason et al. arXiv 2510.08464, 2025.\n\n9. **li2024roboflamingo**: \"Vision-Language Foundation Models as Effective Robot Imitators\" by Li, Xinghang et al. ICLR 2024, arXiv 2311.01378.\n\n10. **shukor2025smolvla**: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\" by Shukor, Mustafa et al. arXiv 2506.01844, 2025.\n\n11. **kim2024openvla**: \"OpenVLA: An Open-Source Vision-Language-Action Model\" by Kim, Moo Jin et al. CoRL 2024.\n\n12. **brohan2023rt2**: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Brohan, Anthony et al. CoRL 2023.\n\n13. **black2024pi0**: \"π₀: A Vision-Language-Action Flow Model for General Robot Control\" by Black, Kevin et al. arXiv 2410.24164, 2024.\n\n14. **black2025pi05**: \"π₀.₅: a Vision-Language-Action Model with Open-World Generalization\" by Black, Kevin et al. CoRL 2025, PMLR vol 305, pages 17-40, arXiv 2504.16054.\n\n15. **ghosh2024octo**: \"Octo: An Open-Source Generalist Robot Policy\" by Octo Model Team, Ghosh, Dibya et al. RSS 2024.\n\n16. **brohan2023rt1**: \"RT-1: Robotics Transformer for Real-World Control at Scale\" by Brohan, Anthony et al. RSS 2023.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/a5682b66462dfac8c.output",
    "canReadOutputFile": true
  }
}
````

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Verify bib entries batch 1 (1-16)",
  "usage": {
    "total_tokens": 14446,
    "tool_uses": 1,
    "duration_ms": 5123
  },
  "last_tool_name": "ToolSearch",
  "uuid": "59ad7501-7d57-466b-8158-711a2faa6a79",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Abnar Zuidema \"Quantifying Attention Flow in Tran…",
  "usage": {
    "total_tokens": 16413,
    "tool_uses": 2,
    "duration_ms": 8280
  },
  "last_tool_name": "WebSearch",
  "uuid": "bd401b80-a6ab-4df5-95d6-7fec8995eb6c",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Gao \"Compressor-VLA: Instruction-Guided Visual To…",
  "usage": {
    "total_tokens": 16415,
    "tool_uses": 3,
    "duration_ms": 8798
  },
  "last_tool_name": "WebSearch",
  "uuid": "80452c0c-2940-4456-a16e-9aaca826351a",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Wang \"SpecPrune-VLA\" arXiv 2509.05614",
  "usage": {
    "total_tokens": 16417,
    "tool_uses": 4,
    "duration_ms": 9224
  },
  "last_tool_name": "WebSearch",
  "uuid": "05f8cbb2-6c18-4ecf-bf94-e58cce6e1081",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Jiang \"LightVLA\" \"Differentiable Token Pruning\" a…",
  "usage": {
    "total_tokens": 16419,
    "tool_uses": 5,
    "duration_ms": 9751
  },
  "last_tool_name": "WebSearch",
  "uuid": "ada5e6d4-8ed2-4684-9206-935201e873bd",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Feng \"See What Matters\" \"Differentiable Grid Samp…",
  "usage": {
    "total_tokens": 16421,
    "tool_uses": 6,
    "duration_ms": 10597
  },
  "last_tool_name": "WebSearch",
  "uuid": "60a80761-86a5-4a14-b1e6-d1df612dcd14",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Zhang \"SparseVLM\" \"Visual Token Sparsification\" a…",
  "usage": {
    "total_tokens": 16423,
    "tool_uses": 7,
    "duration_ms": 10704
  },
  "last_tool_name": "WebSearch",
  "uuid": "1b0d1b86-5741-445c-b013-c008c85504ce",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Khaki \"SparseVILA\" arXiv 2510.17777",
  "usage": {
    "total_tokens": 16425,
    "tool_uses": 8,
    "duration_ms": 11168
  },
  "last_tool_name": "WebSearch",
  "uuid": "2bf88bda-5d0c-478e-bc70-8a32a05fda2c",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Jabbour \"Don't Run with Scissors\" pruning VLA arX…",
  "usage": {
    "total_tokens": 16427,
    "tool_uses": 9,
    "duration_ms": 11520
  },
  "last_tool_name": "WebSearch",
  "uuid": "54322011-0fa4-469b-a2ff-4776d12271f0",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Agent · `toolu_015T8UARwnwAJ6nXTLZuQmZf`</summary>

````json
{
  "description": "Verify bib entries batch 2 (17-32)",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n17. **chen2024fastv**: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\" by Chen, Liang et al. ECCV 2024, arXiv 2403.06764.\n\n18. **xu2025vlacache**: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" by Xu, Siyu et al. NeurIPS 2025.\n\n19. **cheng2026vlaiap**: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\" by Cheng, Jintao et al. arXiv 2603.22991, 2026.\n\n20. **rao2021dynamicvit**: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\" by Rao, Yongming et al. NeurIPS 2021.\n\n21. **bolya2023tome**: \"Token Merging: Your ViT But Faster\" by Bolya, Daniel et al. ICLR 2023.\n\n22. **liang2022evit**: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" by Liang, Youwei et al. ICLR 2022.\n\n23. **liu2023libero**: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\" by Liu, Bo et al. NeurIPS 2023.\n\n24. **yang2025efficientvla**: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\" by Yang, Yantai et al. arXiv 2506.10100, 2025.\n\n25. **liu2025vlapruner**: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\" by Liu, Ziyan et al. arXiv 2511.16449, 2025.\n\n26. **shang2024prumerge**: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\" by Shang, Yuzhang et al. Bib says ICCV 2025 (but key says 2024). arXiv not listed.\n\n27. **alayrac2022flamingo**: \"Flamingo: a Visual Language Model for Few-Shot Learning\" by Alayrac, Jean-Baptiste et al. NeurIPS 2022.\n\n28. **liu2023llava**: \"Visual Instruction Tuning\" by Liu, Haotian et al. NeurIPS 2023.\n\n29. **shi2016subpixel**: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" by Shi, Wenzhe et al. CVPR 2016.\n\n30. **chen2024internvl**: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\" by Chen, Zhe et al. arXiv 2404.16821, 2024.\n\n31. **li2023blip2**: \"BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models\" by Li, Junnan et al. ICML 2023.\n\n32. **jaegle2021perceiver**: \"Perceiver: General Perception with Iterative Attention\" by Jaegle, Andrew et al. ICML 2021.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n",
  "run_in_background": true
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "c0fabb96-92fe-46a8-bdb3-c541378d9393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GVs9r5F4VrDB6KQ6RaGwR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 82782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2607
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

_source line 67_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Verify bib entries batch 2 (17-32)",
  "task_type": "local_agent",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n17. **chen2024fastv**: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\" by Chen, Liang et al. ECCV 2024, arXiv 2403.06764.\n\n18. **xu2025vlacache**: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" by Xu, Siyu et al. NeurIPS 2025.\n\n19. **cheng2026vlaiap**: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\" by Cheng, Jintao et al. arXiv 2603.22991, 2026.\n\n20. **rao2021dynamicvit**: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\" by Rao, Yongming et al. NeurIPS 2021.\n\n21. **bolya2023tome**: \"Token Merging: Your ViT But Faster\" by Bolya, Daniel et al. ICLR 2023.\n\n22. **liang2022evit**: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" by Liang, Youwei et al. ICLR 2022.\n\n23. **liu2023libero**: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\" by Liu, Bo et al. NeurIPS 2023.\n\n24. **yang2025efficientvla**: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\" by Yang, Yantai et al. arXiv 2506.10100, 2025.\n\n25. **liu2025vlapruner**: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\" by Liu, Ziyan et al. arXiv 2511.16449, 2025.\n\n26. **shang2024prumerge**: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\" by Shang, Yuzhang et al. Bib says ICCV 2025 (but key says 2024). arXiv not listed.\n\n27. **alayrac2022flamingo**: \"Flamingo: a Visual Language Model for Few-Shot Learning\" by Alayrac, Jean-Baptiste et al. NeurIPS 2022.\n\n28. **liu2023llava**: \"Visual Instruction Tuning\" by Liu, Haotian et al. NeurIPS 2023.\n\n29. **shi2016subpixel**: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" by Shi, Wenzhe et al. CVPR 2016.\n\n30. **chen2024internvl**: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\" by Chen, Zhe et al. arXiv 2404.16821, 2024.\n\n31. **li2023blip2**: \"BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models\" by Li, Junnan et al. ICML 2023.\n\n32. **jaegle2021perceiver**: \"Perceiver: General Perception with Iterative Attention\" by Jaegle, Andrew et al. ICML 2021.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n",
  "uuid": "68e888d1-0b50-4855-8d31-1c1dd762ec75",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
````

---

### Tool result

_source line 68 · 2026-05-29T06:32:14.930Z_

<details><summary>↩ Tool result · `toolu_015T8UARwnwAJ6nXTLZuQmZf`</summary>

```text
Async agent launched successfully.
agentId: a3c32c2b7d5dda9fa (internal ID - do not mention to user. Use SendMessage with to: 'a3c32c2b7d5dda9fa' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/a3c32c2b7d5dda9fa.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "d9149215-c4dc-4855-9218-f58c353f0cde",
  "tool_use_result": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a3c32c2b7d5dda9fa",
    "description": "Verify bib entries batch 2 (17-32)",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n17. **chen2024fastv**: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\" by Chen, Liang et al. ECCV 2024, arXiv 2403.06764.\n\n18. **xu2025vlacache**: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" by Xu, Siyu et al. NeurIPS 2025.\n\n19. **cheng2026vlaiap**: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\" by Cheng, Jintao et al. arXiv 2603.22991, 2026.\n\n20. **rao2021dynamicvit**: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\" by Rao, Yongming et al. NeurIPS 2021.\n\n21. **bolya2023tome**: \"Token Merging: Your ViT But Faster\" by Bolya, Daniel et al. ICLR 2023.\n\n22. **liang2022evit**: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" by Liang, Youwei et al. ICLR 2022.\n\n23. **liu2023libero**: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\" by Liu, Bo et al. NeurIPS 2023.\n\n24. **yang2025efficientvla**: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\" by Yang, Yantai et al. arXiv 2506.10100, 2025.\n\n25. **liu2025vlapruner**: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\" by Liu, Ziyan et al. arXiv 2511.16449, 2025.\n\n26. **shang2024prumerge**: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\" by Shang, Yuzhang et al. Bib says ICCV 2025 (but key says 2024). arXiv not listed.\n\n27. **alayrac2022flamingo**: \"Flamingo: a Visual Language Model for Few-Shot Learning\" by Alayrac, Jean-Baptiste et al. NeurIPS 2022.\n\n28. **liu2023llava**: \"Visual Instruction Tuning\" by Liu, Haotian et al. NeurIPS 2023.\n\n29. **shi2016subpixel**: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" by Shi, Wenzhe et al. CVPR 2016.\n\n30. **chen2024internvl**: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\" by Chen, Zhe et al. arXiv 2404.16821, 2024.\n\n31. **li2023blip2**: \"BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models\" by Li, Junnan et al. ICML 2023.\n\n32. **jaegle2021perceiver**: \"Perceiver: General Perception with Iterative Attention\" by Jaegle, Andrew et al. ICML 2021.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/a3c32c2b7d5dda9fa.output",
    "canReadOutputFile": true
  }
}
````

</details>

---

### System

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Verify bib entries batch 2 (17-32)",
  "usage": {
    "total_tokens": 14336,
    "tool_uses": 1,
    "duration_ms": 3370
  },
  "last_tool_name": "ToolSearch",
  "uuid": "14c2dc21-760b-4390-a0de-ffcb053a3b92",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Li Xinghang \"Vision-Language Foundation Models as…",
  "usage": {
    "total_tokens": 22658,
    "tool_uses": 10,
    "duration_ms": 24636
  },
  "last_tool_name": "WebSearch",
  "uuid": "c894698a-a86e-4be5-97e4-2b250dbe3e99",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for arXiv 2403.06764 \"An Image is Worth 1/2 Tokens Af…",
  "usage": {
    "total_tokens": 15800,
    "tool_uses": 2,
    "duration_ms": 8328
  },
  "last_tool_name": "WebSearch",
  "uuid": "e362c7be-69b6-463d-a2a8-adf3d6ad9047",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Shukor \"SmolVLA\" arXiv 2506.01844",
  "usage": {
    "total_tokens": 22659,
    "tool_uses": 11,
    "duration_ms": 25908
  },
  "last_tool_name": "WebSearch",
  "uuid": "774d92ce-8dad-44d9-83d4-987a24ad0f94",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Kim \"OpenVLA: An Open-Source Vision-Language-Acti…",
  "usage": {
    "total_tokens": 22660,
    "tool_uses": 12,
    "duration_ms": 26576
  },
  "last_tool_name": "WebSearch",
  "uuid": "e9679f48-f54c-46e8-82fd-bb232b05dbff",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Brohan \"RT-2: Vision-Language-Action Models Trans…",
  "usage": {
    "total_tokens": 22661,
    "tool_uses": 13,
    "duration_ms": 27601
  },
  "last_tool_name": "WebSearch",
  "uuid": "d6529bf2-9914-4e0f-9482-ba25e9efed1b",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Black \"π₀ pi0 Vision-Language-Action Flow Model\" …",
  "usage": {
    "total_tokens": 22662,
    "tool_uses": 14,
    "duration_ms": 28662
  },
  "last_tool_name": "WebSearch",
  "uuid": "c2440371-ce78-4e8f-8f77-eea1934b9a80",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Black \"π₀.₅ pi0.5 Vision-Language-Action Open-Wor…",
  "usage": {
    "total_tokens": 22663,
    "tool_uses": 15,
    "duration_ms": 29462
  },
  "last_tool_name": "WebSearch",
  "uuid": "785a02ee-cc64-4568-8e5f-61a946cfd211",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Octo \"Open-Source Generalist Robot Policy\" Ghosh …",
  "usage": {
    "total_tokens": 22664,
    "tool_uses": 16,
    "duration_ms": 30406
  },
  "last_tool_name": "WebSearch",
  "uuid": "4b113c75-d59d-439c-8fdf-aadde80217c4",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 78_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for Brohan \"RT-1: Robotics Transformer for Real-World…",
  "usage": {
    "total_tokens": 22665,
    "tool_uses": 17,
    "duration_ms": 30997
  },
  "last_tool_name": "WebSearch",
  "uuid": "de9b154a-5482-4d9e-950e-17572efb8938",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Agent · `toolu_01E83JnRK5SLSuqYRyRhTcDH`</summary>

````json
{
  "description": "Verify bib entries batch 3 (33-48)",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n33. **oquab2023dinov2**: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime et al. Listed as \"Transactions on Machine Learning Research\", year=2024, but bib key says 2023.\n\n34. **zhai2023siglip**: \"Sigmoid Loss for Language Image Pre-Training\" by Zhai, Xiaohua et al. ICCV 2023.\n\n35. **yang2024qwen2**: \"Qwen2 Technical Report\" by Yang, An et al. arXiv 2407.10671, 2024.\n\n36. **lipman2023flow**: \"Flow Matching for Generative Modeling\" by Lipman, Yaron et al. ICLR 2023.\n\n37. **li2024cogact**: \"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation\" by Li, Qixiu et al. arXiv 2411.19650, 2024.\n\n38. **kim2025openoft**: \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" by Kim, Moo Jin and Finn, Chelsea and Liang, Percy. arXiv 2502.19645, 2025.\n\n39. **li2024tokenpacker**: \"TokenPacker: Efficient Visual Projector for Multimodal LLM\" by Li, Wentong et al. arXiv 2407.02392, 2024.\n\n40. **zheng2025xvla**: \"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" by Zheng, Jinliang et al. ICLR 2026, arXiv 2510.10274.\n\n41. **wen2024tinyvla**: \"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation\" by Wen, Junjie et al. arXiv 2409.12514, 2024.\n\n42. **lewis2020bart**: \"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension\" by Lewis, Mike et al. ACL 2020.\n\n43. **ryoo2021tokenlearner**: \"TokenLearner: Adaptive Space-Time Tokenization for Videos\" by Ryoo, Michael S. et al. NeurIPS 2021, arXiv 2106.11297.\n\n44. **yin2022avit**: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\" by Yin, Hongxu et al. CVPR 2022, arXiv 2112.07658.\n\n45. **meng2022adavit**: \"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition\" by Meng, Lingchen et al. CVPR 2022, arXiv 2111.15668.\n\n46. **chen2023sparsevit**: \"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer\" by Chen, Xuanyao et al. CVPR 2023, arXiv 2303.17605.\n\n47. **ye2025fitprune**: \"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models\" by Ye, Weihao et al. AAAI 2025, arXiv 2409.10197.\n\n48. **shi2024crossget**: \"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers\" by Shi, Dachuan et al. ICML 2024, arXiv 2305.17455.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n",
  "run_in_background": true
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "5194d505-3a05-4487-b036-f75cacf4e493",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GVs9r5F4VrDB6KQ6RaGwR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 82782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2607
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

_source line 80_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Verify bib entries batch 3 (33-48)",
  "task_type": "local_agent",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n33. **oquab2023dinov2**: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime et al. Listed as \"Transactions on Machine Learning Research\", year=2024, but bib key says 2023.\n\n34. **zhai2023siglip**: \"Sigmoid Loss for Language Image Pre-Training\" by Zhai, Xiaohua et al. ICCV 2023.\n\n35. **yang2024qwen2**: \"Qwen2 Technical Report\" by Yang, An et al. arXiv 2407.10671, 2024.\n\n36. **lipman2023flow**: \"Flow Matching for Generative Modeling\" by Lipman, Yaron et al. ICLR 2023.\n\n37. **li2024cogact**: \"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation\" by Li, Qixiu et al. arXiv 2411.19650, 2024.\n\n38. **kim2025openoft**: \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" by Kim, Moo Jin and Finn, Chelsea and Liang, Percy. arXiv 2502.19645, 2025.\n\n39. **li2024tokenpacker**: \"TokenPacker: Efficient Visual Projector for Multimodal LLM\" by Li, Wentong et al. arXiv 2407.02392, 2024.\n\n40. **zheng2025xvla**: \"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" by Zheng, Jinliang et al. ICLR 2026, arXiv 2510.10274.\n\n41. **wen2024tinyvla**: \"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation\" by Wen, Junjie et al. arXiv 2409.12514, 2024.\n\n42. **lewis2020bart**: \"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension\" by Lewis, Mike et al. ACL 2020.\n\n43. **ryoo2021tokenlearner**: \"TokenLearner: Adaptive Space-Time Tokenization for Videos\" by Ryoo, Michael S. et al. NeurIPS 2021, arXiv 2106.11297.\n\n44. **yin2022avit**: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\" by Yin, Hongxu et al. CVPR 2022, arXiv 2112.07658.\n\n45. **meng2022adavit**: \"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition\" by Meng, Lingchen et al. CVPR 2022, arXiv 2111.15668.\n\n46. **chen2023sparsevit**: \"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer\" by Chen, Xuanyao et al. CVPR 2023, arXiv 2303.17605.\n\n47. **ye2025fitprune**: \"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models\" by Ye, Weihao et al. AAAI 2025, arXiv 2409.10197.\n\n48. **shi2024crossget**: \"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers\" by Shi, Dachuan et al. ICML 2024, arXiv 2305.17455.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n",
  "uuid": "a99c1cd8-5a44-4265-bcc0-1aa71af71415",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
````

---

### Tool result

_source line 81 · 2026-05-29T06:32:31.413Z_

<details><summary>↩ Tool result · `toolu_01E83JnRK5SLSuqYRyRhTcDH`</summary>

```text
Async agent launched successfully.
agentId: a263b2a81ff95f84b (internal ID - do not mention to user. Use SendMessage with to: 'a263b2a81ff95f84b' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/a263b2a81ff95f84b.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "f7a59997-4c49-41c2-bc0c-196c2b5c4216",
  "tool_use_result": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a263b2a81ff95f84b",
    "description": "Verify bib entries batch 3 (33-48)",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n33. **oquab2023dinov2**: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime et al. Listed as \"Transactions on Machine Learning Research\", year=2024, but bib key says 2023.\n\n34. **zhai2023siglip**: \"Sigmoid Loss for Language Image Pre-Training\" by Zhai, Xiaohua et al. ICCV 2023.\n\n35. **yang2024qwen2**: \"Qwen2 Technical Report\" by Yang, An et al. arXiv 2407.10671, 2024.\n\n36. **lipman2023flow**: \"Flow Matching for Generative Modeling\" by Lipman, Yaron et al. ICLR 2023.\n\n37. **li2024cogact**: \"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation\" by Li, Qixiu et al. arXiv 2411.19650, 2024.\n\n38. **kim2025openoft**: \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" by Kim, Moo Jin and Finn, Chelsea and Liang, Percy. arXiv 2502.19645, 2025.\n\n39. **li2024tokenpacker**: \"TokenPacker: Efficient Visual Projector for Multimodal LLM\" by Li, Wentong et al. arXiv 2407.02392, 2024.\n\n40. **zheng2025xvla**: \"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" by Zheng, Jinliang et al. ICLR 2026, arXiv 2510.10274.\n\n41. **wen2024tinyvla**: \"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation\" by Wen, Junjie et al. arXiv 2409.12514, 2024.\n\n42. **lewis2020bart**: \"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension\" by Lewis, Mike et al. ACL 2020.\n\n43. **ryoo2021tokenlearner**: \"TokenLearner: Adaptive Space-Time Tokenization for Videos\" by Ryoo, Michael S. et al. NeurIPS 2021, arXiv 2106.11297.\n\n44. **yin2022avit**: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\" by Yin, Hongxu et al. CVPR 2022, arXiv 2112.07658.\n\n45. **meng2022adavit**: \"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition\" by Meng, Lingchen et al. CVPR 2022, arXiv 2111.15668.\n\n46. **chen2023sparsevit**: \"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer\" by Chen, Xuanyao et al. CVPR 2023, arXiv 2303.17605.\n\n47. **ye2025fitprune**: \"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models\" by Ye, Weihao et al. AAAI 2025, arXiv 2409.10197.\n\n48. **shi2024crossget**: \"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers\" by Shi, Dachuan et al. ICML 2024, arXiv 2305.17455.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/a263b2a81ff95f84b.output",
    "canReadOutputFile": true
  }
}
````

</details>

---

### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"VLA-Cache\" \"Adaptive Token Caching\" Xu Siyu visi…",
  "usage": {
    "total_tokens": 16952,
    "tool_uses": 3,
    "duration_ms": 17399
  },
  "last_tool_name": "WebSearch",
  "uuid": "e6ab2e51-f0d4-4371-b68c-f7f1fa5d8bdb",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Verify bib entries batch 3 (33-48)",
  "usage": {
    "total_tokens": 14375,
    "tool_uses": 1,
    "duration_ms": 3290
  },
  "last_tool_name": "ToolSearch",
  "uuid": "5cfc069c-35fb-4c36-876c-72b1f2768d70",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 84_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for DINOv2 Learning Robust Visual Features without Su…",
  "usage": {
    "total_tokens": 15843,
    "tool_uses": 2,
    "duration_ms": 6550
  },
  "last_tool_name": "WebSearch",
  "uuid": "d586ff9c-59bd-41f0-b66d-25aafff14a04",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://arxiv.org/abs/2511.18950",
  "usage": {
    "total_tokens": 29866,
    "tool_uses": 18,
    "duration_ms": 41627
  },
  "last_tool_name": "WebFetch",
  "uuid": "0e748c48-9dc2-4736-ace8-3efb1ebeb3b8",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://arxiv.org/abs/2509.05614",
  "usage": {
    "total_tokens": 29867,
    "tool_uses": 19,
    "duration_ms": 42573
  },
  "last_tool_name": "WebFetch",
  "uuid": "38a76ca4-d28b-41c7-9ed0-0a026302032b",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://arxiv.org/abs/2410.04417",
  "usage": {
    "total_tokens": 29868,
    "tool_uses": 20,
    "duration_ms": 43515
  },
  "last_tool_name": "WebFetch",
  "uuid": "7f124d95-4c6b-444a-b439-6a876beb7ddb",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 88_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://arxiv.org/abs/2510.17777",
  "usage": {
    "total_tokens": 29869,
    "tool_uses": 21,
    "duration_ms": 44463
  },
  "last_tool_name": "WebFetch",
  "uuid": "369a31a0-f202-4674-86ed-df1ebaecfe66",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for arXiv 2603.22991 \"VLA-IAP\" \"Training-Free Visual …",
  "usage": {
    "total_tokens": 17982,
    "tool_uses": 4,
    "duration_ms": 27796
  },
  "last_tool_name": "WebSearch",
  "uuid": "9a304d2f-2d8e-462c-904d-37166968b891",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://arxiv.org/abs/2510.08464",
  "usage": {
    "total_tokens": 29870,
    "tool_uses": 22,
    "duration_ms": 45420
  },
  "last_tool_name": "WebFetch",
  "uuid": "ac52ad9d-91de-4866-ad5a-a37354da0ba5",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://arxiv.org/abs/2410.24164",
  "usage": {
    "total_tokens": 29871,
    "tool_uses": 23,
    "duration_ms": 45880
  },
  "last_tool_name": "WebFetch",
  "uuid": "375ee6d8-02d5-4265-aa09-c247548dbbed",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for SparseVLM Zhang Yuan ICML 2025 accepted conferenc…",
  "usage": {
    "total_tokens": 29872,
    "tool_uses": 24,
    "duration_ms": 46924
  },
  "last_tool_name": "WebSearch",
  "uuid": "fa9bcc03-5165-4f80-a027-28632c1232fc",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for SparseVILA Khaki ICCV 2025 accepted conference",
  "usage": {
    "total_tokens": 29873,
    "tool_uses": 25,
    "duration_ms": 47092
  },
  "last_tool_name": "WebSearch",
  "uuid": "2076113d-95d6-4e87-8f77-62676ce97bb8",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for DINOv2 Oquab Transactions on Machine Learning Res…",
  "usage": {
    "total_tokens": 16883,
    "tool_uses": 3,
    "duration_ms": 17322
  },
  "last_tool_name": "WebSearch",
  "uuid": "08d94096-fa88-4f55-be27-580d26f5a9ea",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### Tool call

_source line 95_

<details open><summary>🔧 Tool call — Agent · `toolu_0184iYNGgFN4oRK4gXehGH4m`</summary>

````json
{
  "description": "Verify bib entries batch 4 (49-62)",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n49. **zhang2024fastervlm**: \"[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make VLM Inference Faster\" by Zhang, Qizhe et al. arXiv 2412.01818, 2024.\n\n50. **liu2024llava15**: \"Improved Baselines with Visual Instruction Tuning\" by Liu, Haotian et al. CVPR 2024, arXiv 2310.03744.\n\n51. **chen2024internvl25**: \"Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling\" by Chen, Zhe et al. arXiv 2412.05271, 2024.\n\n52. **gao2024miniinternvl**: \"Mini-InternVL: A Flexible-Transfer Pocket Multimodal Model with 5% Parameters and 90% Performance\" by Gao, Zhangwei et al. arXiv 2410.16261, 2024.\n\n53. **zitkovich2023rt2**: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Zitkovich, Brianna et al. CoRL 2023, arXiv 2307.15818.\n\n54. **openxembodiment2024**: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\" by Open X-Embodiment Collaboration. ICRA 2024, arXiv 2310.08864.\n\n55. **zhang2023h2o**: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\" by Zhang, Zhenyu et al. NeurIPS 2023, arXiv 2306.14048.\n\n56. **xiao2024streamingllm**: \"Efficient Streaming Language Models with Attention Sinks\" by Xiao, Guangxuan et al. ICLR 2024, arXiv 2309.17453.\n\n57. **mees2022calvin**: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\" by Mees, Oier et al. IEEE Robotics and Automation Letters 2022, arXiv 2112.03227.\n\n58. **chi2023diffusionpolicy**: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\" by Chi, Cheng et al. RSS 2023, arXiv 2303.04137.\n\n59. **zeng2023transformers_tsf**: \"Are Transformers Effective for Time Series Forecasting?\" by Zeng, Ailing et al. AAAI 2023, arXiv 2205.13504.\n\n60. **bouthillier2024negative**: \"Position: Embracing Negative Results in Machine Learning\" by Bouthillier, Xavier et al. ICML 2024, arXiv 2406.03980.\n\n61. **oquab2024dinov2**: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime et al. Transactions on Machine Learning Research 2024, arXiv 2304.07193. NOTE: This appears to be a duplicate of oquab2023dinov2 (entry #33 from another batch).\n\n62. **su2024roformer**: \"RoFormer: Enhanced Transformer with Rotary Position Embedding\" by Su, Jianlin et al. Neurocomputing vol 568, 2024.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n\nALSO check:\n- Are entries 53 (zitkovich2023rt2) and 12 (brohan2023rt2, from batch 1) duplicates referencing the same RT-2 paper?\n- Are entries 61 (oquab2024dinov2) and 33 (oquab2023dinov2, from batch 3) duplicates?\n",
  "run_in_background": true
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "fa7e8fff-990a-4b5d-9a1e-b0aa797391ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GVs9r5F4VrDB6KQ6RaGwR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 82782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2607
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

_source line 96_

````json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Verify bib entries batch 4 (49-62)",
  "task_type": "local_agent",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n49. **zhang2024fastervlm**: \"[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make VLM Inference Faster\" by Zhang, Qizhe et al. arXiv 2412.01818, 2024.\n\n50. **liu2024llava15**: \"Improved Baselines with Visual Instruction Tuning\" by Liu, Haotian et al. CVPR 2024, arXiv 2310.03744.\n\n51. **chen2024internvl25**: \"Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling\" by Chen, Zhe et al. arXiv 2412.05271, 2024.\n\n52. **gao2024miniinternvl**: \"Mini-InternVL: A Flexible-Transfer Pocket Multimodal Model with 5% Parameters and 90% Performance\" by Gao, Zhangwei et al. arXiv 2410.16261, 2024.\n\n53. **zitkovich2023rt2**: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Zitkovich, Brianna et al. CoRL 2023, arXiv 2307.15818.\n\n54. **openxembodiment2024**: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\" by Open X-Embodiment Collaboration. ICRA 2024, arXiv 2310.08864.\n\n55. **zhang2023h2o**: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\" by Zhang, Zhenyu et al. NeurIPS 2023, arXiv 2306.14048.\n\n56. **xiao2024streamingllm**: \"Efficient Streaming Language Models with Attention Sinks\" by Xiao, Guangxuan et al. ICLR 2024, arXiv 2309.17453.\n\n57. **mees2022calvin**: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\" by Mees, Oier et al. IEEE Robotics and Automation Letters 2022, arXiv 2112.03227.\n\n58. **chi2023diffusionpolicy**: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\" by Chi, Cheng et al. RSS 2023, arXiv 2303.04137.\n\n59. **zeng2023transformers_tsf**: \"Are Transformers Effective for Time Series Forecasting?\" by Zeng, Ailing et al. AAAI 2023, arXiv 2205.13504.\n\n60. **bouthillier2024negative**: \"Position: Embracing Negative Results in Machine Learning\" by Bouthillier, Xavier et al. ICML 2024, arXiv 2406.03980.\n\n61. **oquab2024dinov2**: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime et al. Transactions on Machine Learning Research 2024, arXiv 2304.07193. NOTE: This appears to be a duplicate of oquab2023dinov2 (entry #33 from another batch).\n\n62. **su2024roformer**: \"RoFormer: Enhanced Transformer with Rotary Position Embedding\" by Su, Jianlin et al. Neurocomputing vol 568, 2024.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n\nALSO check:\n- Are entries 53 (zitkovich2023rt2) and 12 (brohan2023rt2, from batch 1) duplicates referencing the same RT-2 paper?\n- Are entries 61 (oquab2024dinov2) and 33 (oquab2023dinov2, from batch 3) duplicates?\n",
  "uuid": "c45e40a0-8b0a-414d-8d0d-3e523476821c",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
````

---

### Tool result

_source line 97 · 2026-05-29T06:32:49.983Z_

<details><summary>↩ Tool result · `toolu_0184iYNGgFN4oRK4gXehGH4m`</summary>

```text
Async agent launched successfully.
agentId: adb06fa7cf287f5e3 (internal ID - do not mention to user. Use SendMessage with to: 'adb06fa7cf287f5e3' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/adb06fa7cf287f5e3.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "a4a01915-66c3-46c9-b6e5-a4992501aef9",
  "tool_use_result": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "adb06fa7cf287f5e3",
    "description": "Verify bib entries batch 4 (49-62)",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, search the web (arXiv, Semantic Scholar, Google Scholar) to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given, (7) if arXiv preprint has been accepted at a conference, note that.\n\nReturn a structured checklist for each entry with ✓ or ✗.\n\nENTRIES TO VERIFY:\n\n49. **zhang2024fastervlm**: \"[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make VLM Inference Faster\" by Zhang, Qizhe et al. arXiv 2412.01818, 2024.\n\n50. **liu2024llava15**: \"Improved Baselines with Visual Instruction Tuning\" by Liu, Haotian et al. CVPR 2024, arXiv 2310.03744.\n\n51. **chen2024internvl25**: \"Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling\" by Chen, Zhe et al. arXiv 2412.05271, 2024.\n\n52. **gao2024miniinternvl**: \"Mini-InternVL: A Flexible-Transfer Pocket Multimodal Model with 5% Parameters and 90% Performance\" by Gao, Zhangwei et al. arXiv 2410.16261, 2024.\n\n53. **zitkovich2023rt2**: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Zitkovich, Brianna et al. CoRL 2023, arXiv 2307.15818.\n\n54. **openxembodiment2024**: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\" by Open X-Embodiment Collaboration. ICRA 2024, arXiv 2310.08864.\n\n55. **zhang2023h2o**: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\" by Zhang, Zhenyu et al. NeurIPS 2023, arXiv 2306.14048.\n\n56. **xiao2024streamingllm**: \"Efficient Streaming Language Models with Attention Sinks\" by Xiao, Guangxuan et al. ICLR 2024, arXiv 2309.17453.\n\n57. **mees2022calvin**: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\" by Mees, Oier et al. IEEE Robotics and Automation Letters 2022, arXiv 2112.03227.\n\n58. **chi2023diffusionpolicy**: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\" by Chi, Cheng et al. RSS 2023, arXiv 2303.04137.\n\n59. **zeng2023transformers_tsf**: \"Are Transformers Effective for Time Series Forecasting?\" by Zeng, Ailing et al. AAAI 2023, arXiv 2205.13504.\n\n60. **bouthillier2024negative**: \"Position: Embracing Negative Results in Machine Learning\" by Bouthillier, Xavier et al. ICML 2024, arXiv 2406.03980.\n\n61. **oquab2024dinov2**: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime et al. Transactions on Machine Learning Research 2024, arXiv 2304.07193. NOTE: This appears to be a duplicate of oquab2023dinov2 (entry #33 from another batch).\n\n62. **su2024roformer**: \"RoFormer: Enhanced Transformer with Rotary Position Embedding\" by Su, Jianlin et al. Neurocomputing vol 568, 2024.\n\nFor each entry, output:\n```\n[✓/✗] key | verified_title | verified_year | verified_venue\n- Issues (if any): ...\n```\n\nALSO check:\n- Are entries 53 (zitkovich2023rt2) and 12 (brohan2023rt2, from batch 1) duplicates referencing the same RT-2 paper?\n- Are entries 61 (oquab2024dinov2) and 33 (oquab2023dinov2, from batch 3) duplicates?\n",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/adb06fa7cf287f5e3.output",
    "canReadOutputFile": true
  }
}
````

</details>

---

### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"DynamicViT\" \"Dynamic Token Sparsification\" Rao Y…",
  "usage": {
    "total_tokens": 18766,
    "tool_uses": 5,
    "duration_ms": 38267
  },
  "last_tool_name": "WebSearch",
  "uuid": "7084ac82-edd5-4bdf-baeb-cfd9e189aa87",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Verify bib entries batch 4 (49-62)",
  "usage": {
    "total_tokens": 14400,
    "tool_uses": 1,
    "duration_ms": 3396
  },
  "last_tool_name": "ToolSearch",
  "uuid": "1308d872-d35d-4a51-8a35-bd424dee2f8c",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 100_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2412.01818 \"[CLS] Attention is All You Need…",
  "usage": {
    "total_tokens": 15863,
    "tool_uses": 2,
    "duration_ms": 6473
  },
  "last_tool_name": "WebSearch",
  "uuid": "be63bf29-defa-498e-a898-f14da307634d",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for Sigmoid Loss for Language Image Pre-Training Zhai…",
  "usage": {
    "total_tokens": 17900,
    "tool_uses": 4,
    "duration_ms": 27290
  },
  "last_tool_name": "WebSearch",
  "uuid": "7b02c14f-1a97-4f0e-9967-a4496a70bc3d",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 102_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://dblp.org/rec/conf/corl/ZitkovichYXXXXW23.…",
  "usage": {
    "total_tokens": 32858,
    "tool_uses": 26,
    "duration_ms": 61857
  },
  "last_tool_name": "WebFetch",
  "uuid": "ce2b9b37-6cab-4da8-801c-f3ddc259e9d2",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 103_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://proceedings.mlr.press/v270/kim25c.html",
  "usage": {
    "total_tokens": 32859,
    "tool_uses": 27,
    "duration_ms": 62656
  },
  "last_tool_name": "WebFetch",
  "uuid": "945a85da-174a-4f2d-b860-63e1a5cd0867",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 104_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for SpecPrune-VLA Wang Hanzhen ICML 2026 accepted",
  "usage": {
    "total_tokens": 32860,
    "tool_uses": 28,
    "duration_ms": 63111
  },
  "last_tool_name": "WebSearch",
  "uuid": "9e5e4aea-adcf-4d15-8352-229a3421d484",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### Assistant

_source line 105_

4 verification agents launched in parallel. While they search, let me analyze the structural issues I've already identified from reading the bib and tex files:

**Preliminary findings (no search needed):**

1. **Duplicate RT-2 entries**: `brohan2023rt2` and `zitkovich2023rt2` both reference the same RT-2 paper at CoRL 2023, but with different first authors. The actual RT-2 paper lists Zitkovich as first author on arXiv.

2. **Duplicate DINOv2 entries**: `oquab2023dinov2` and `oquab2024dinov2` reference the same paper. The bib key year differs (2023 vs 2024) but both list TMLR 2024.

3. **Uncited bib entries** (present in bib but not `\cite`d in any file included by main.tex): `brohan2023rt2`, `brohan2023rt1`, `ghosh2024octo`, `li2024roboflamingo`, `chen2024internvl`, `jaegle2021perceiver`, `oquab2024dinov2`, `liu2024llava15`, `chen2024internvl25`, `gao2024miniinternvl`, `zitkovich2023rt2`, `openxembodiment2024`, `zhang2023h2o`, `xiao2024streamingllm`, `mees2022calvin`, `chi2023diffusionpolicy`, `zeng2023transformers_tsf`, `bouthillier2024negative`, `ryoo2021tokenlearner`, `meng2022adavit`, `chen2023sparsevit`, `zhang2024fastervlm`, `li2024tokenpacker`, `wen2024tinyvla`, `alayrac2022flamingo`.

4. **Key/year mismatch**: `shang2024prumerge` has key year 2024 but `year={2025}` in the bib entry.

Waiting for the verification agents to complete their web searches...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "720af473-51d3-419d-bfb6-ddd7693c0a29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cJMc5DRBDAdxb61qfkpFU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6045,
      "cache_read_input_tokens": 85389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6045
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

_source line 106_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for \"pi0\" Black Kevin RSS 2025 accepted Robotics Scie…",
  "usage": {
    "total_tokens": 32861,
    "tool_uses": 29,
    "duration_ms": 63704
  },
  "last_tool_name": "WebSearch",
  "uuid": "16c29447-6e9a-44a1-91cb-bbb41cc3d6ad",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 107_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2310.03744 \"Improved Baselines with Visual …",
  "usage": {
    "total_tokens": 16933,
    "tool_uses": 3,
    "duration_ms": 17317
  },
  "last_tool_name": "WebSearch",
  "uuid": "32cab117-02d8-4dd9-bb39-0b24bc132cb0",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 108_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"Token Merging\" \"Your ViT But Faster\" Bolya Danie…",
  "usage": {
    "total_tokens": 19834,
    "tool_uses": 6,
    "duration_ms": 52708
  },
  "last_tool_name": "WebSearch",
  "uuid": "779f18bb-d6ec-43f2-ada7-b7ad327379c9",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for Qwen2 Technical Report Yang An arXiv 2407.10671",
  "usage": {
    "total_tokens": 18812,
    "tool_uses": 5,
    "duration_ms": 38498
  },
  "last_tool_name": "WebSearch",
  "uuid": "124260c2-d9a1-4656-b72c-9a32f66abea6",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 110_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://roboticsconference.org/program/papers/",
  "usage": {
    "total_tokens": 34920,
    "tool_uses": 30,
    "duration_ms": 75021
  },
  "last_tool_name": "WebFetch",
  "uuid": "de59199c-dc6a-485b-915d-60c083c2ea65",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 111_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://arxiv.org/abs/2307.15818",
  "usage": {
    "total_tokens": 34986,
    "tool_uses": 31,
    "duration_ms": 76421
  },
  "last_tool_name": "WebFetch",
  "uuid": "073e3f41-651a-4de9-9430-d15d1ace32b3",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 112_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://arxiv.org/abs/2509.05614",
  "usage": {
    "total_tokens": 35052,
    "tool_uses": 32,
    "duration_ms": 77712
  },
  "last_tool_name": "WebFetch",
  "uuid": "061fb4b7-74c8-42ec-bb67-7629da6c1e04",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 113_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"Not All Patches are What You Need\" \"Token Reorga…",
  "usage": {
    "total_tokens": 20697,
    "tool_uses": 7,
    "duration_ms": 62350
  },
  "last_tool_name": "WebSearch",
  "uuid": "0fc9b788-e6f3-4a29-878e-9e759472e1bc",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 114_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for Flow Matching for Generative Modeling Lipman ICLR…",
  "usage": {
    "total_tokens": 19744,
    "tool_uses": 6,
    "duration_ms": 49456
  },
  "last_tool_name": "WebSearch",
  "uuid": "afa2cae0-a3f8-4b45-b280-9657160db8ea",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 115_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for RT-2 Brohan CoRL 2023 proceedings PMLR published …",
  "usage": {
    "total_tokens": 35985,
    "tool_uses": 33,
    "duration_ms": 85664
  },
  "last_tool_name": "WebSearch",
  "uuid": "ba5dbd4c-4257-4da5-b970-a5b99c3940dc",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 116_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2412.05271 InternVL 2.5 \"Expanding Performa…",
  "usage": {
    "total_tokens": 17961,
    "tool_uses": 4,
    "duration_ms": 34014
  },
  "last_tool_name": "WebSearch",
  "uuid": "bd4266eb-b09d-49e8-a951-b0b28a7643f4",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 117_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for OpenVLA CoRL 2024 \"8th Conference on Robot Learni…",
  "usage": {
    "total_tokens": 35986,
    "tool_uses": 34,
    "duration_ms": 86235
  },
  "last_tool_name": "WebSearch",
  "uuid": "eaae577c-6d30-419e-9cba-1e9e5a4c7cce",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 118_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for RoboFlamingo Li Xinghang ICLR 2024 accepted",
  "usage": {
    "total_tokens": 35987,
    "tool_uses": 35,
    "duration_ms": 86941
  },
  "last_tool_name": "WebSearch",
  "uuid": "ffb57d8c-4d41-4e87-bd2b-1d0018045cc8",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 119_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"LIBERO\" \"Benchmarking Knowledge Transfer for Lif…",
  "usage": {
    "total_tokens": 21764,
    "tool_uses": 8,
    "duration_ms": 71245
  },
  "last_tool_name": "WebSearch",
  "uuid": "4f965121-cc4d-474f-b1ad-1be70575446e",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 120_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for CogACT Foundational Vision-Language-Action Model …",
  "usage": {
    "total_tokens": 20774,
    "tool_uses": 7,
    "duration_ms": 61103
  },
  "last_tool_name": "WebSearch",
  "uuid": "07017eb6-e029-41b4-bfd6-7ecf3e25cabb",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 121_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://proceedings.mlr.press/v229/zitkovich23a.h…",
  "usage": {
    "total_tokens": 37956,
    "tool_uses": 36,
    "duration_ms": 96345
  },
  "last_tool_name": "WebFetch",
  "uuid": "ba258833-99ea-421b-804f-ab8c90769f68",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 122_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2410.16261 \"Mini-InternVL: A Flexible-Trans…",
  "usage": {
    "total_tokens": 18979,
    "tool_uses": 5,
    "duration_ms": 44608
  },
  "last_tool_name": "WebSearch",
  "uuid": "e9fd42b9-a8ac-4304-80d3-7be3e46c70d0",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 123_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for \"LightVLA\" Jiang ICRA 2026 accepted conference",
  "usage": {
    "total_tokens": 37957,
    "tool_uses": 37,
    "duration_ms": 97075
  },
  "last_tool_name": "WebSearch",
  "uuid": "fb00ecb2-21ef-4bdf-ba09-48cf2e6073bf",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 124_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for arXiv 2506.10100 \"EfficientVLA\" Yang Yantai \"Trai…",
  "usage": {
    "total_tokens": 22848,
    "tool_uses": 9,
    "duration_ms": 82968
  },
  "last_tool_name": "WebSearch",
  "uuid": "b39e0be7-7e3d-4310-aad6-15b1519ee677",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 125_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for OpenOFT Fine-Tuning Vision-Language-Action Models…",
  "usage": {
    "total_tokens": 21974,
    "tool_uses": 8,
    "duration_ms": 71928
  },
  "last_tool_name": "WebSearch",
  "uuid": "fcde52fa-eeb3-475e-a6be-adf7cb06aab9",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 126_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for arXiv 2511.16449 \"VLA-Pruner\" \"Temporal-Aware Dua…",
  "usage": {
    "total_tokens": 23634,
    "tool_uses": 10,
    "duration_ms": 91969
  },
  "last_tool_name": "WebSearch",
  "uuid": "ca5f3213-2f04-46c8-80d8-02fab5e0f0e1",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 127_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2307.15818 \"RT-2: Vision-Language-Action Mo…",
  "usage": {
    "total_tokens": 19896,
    "tool_uses": 6,
    "duration_ms": 57006
  },
  "last_tool_name": "WebSearch",
  "uuid": "09363416-85e6-48b6-9620-17737605dc73",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 128_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Fetching https://icml.cc/virtual/2026/poster/65010",
  "usage": {
    "total_tokens": 39398,
    "tool_uses": 38,
    "duration_ms": 110408
  },
  "last_tool_name": "WebFetch",
  "uuid": "9c24863f-2ea1-4081-98bc-ba09d6464d6d",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 129_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for RT-2 CoRL 2023 first author Brohan or Zitkovich",
  "usage": {
    "total_tokens": 39400,
    "tool_uses": 39,
    "duration_ms": 110491
  },
  "last_tool_name": "WebSearch",
  "uuid": "433b0e9f-e527-413c-8516-98188a27ca8e",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 130_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for TokenPacker Efficient Visual Projector Multimodal…",
  "usage": {
    "total_tokens": 22902,
    "tool_uses": 9,
    "duration_ms": 80202
  },
  "last_tool_name": "WebSearch",
  "uuid": "c619fb22-2a76-46ad-8eaf-c0466c64199e",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 131_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2310.08864 \"Open X-Embodiment: Robotic Lear…",
  "usage": {
    "total_tokens": 20718,
    "tool_uses": 7,
    "duration_ms": 66427
  },
  "last_tool_name": "WebSearch",
  "uuid": "4133eac7-05d5-41fe-bba2-5e5733bd5003",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 132_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for arxiv.org/abs/2511.16449 VLA-Pruner submission da…",
  "usage": {
    "total_tokens": 24466,
    "tool_uses": 11,
    "duration_ms": 103785
  },
  "last_tool_name": "WebSearch",
  "uuid": "ca38036e-ca6d-4adb-a5d9-0e84dfc8d6a2",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 133_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for TokenPacker Li Wentong IJCV 2025 venue accepted c…",
  "usage": {
    "total_tokens": 23970,
    "tool_uses": 10,
    "duration_ms": 91265
  },
  "last_tool_name": "WebSearch",
  "uuid": "f6d8b7c4-cd9c-4baa-b620-0ab483b0327b",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 134_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "description": "Searching for \"pi0.5\" Black CoRL 2025 \"9th Conference on Robot …",
  "usage": {
    "total_tokens": 40551,
    "tool_uses": 40,
    "duration_ms": 125671
  },
  "last_tool_name": "WebSearch",
  "uuid": "a7f44514-96a2-405e-98bd-1656a33ba2f5",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 135_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"LLaVA-PruMerge\" \"Adaptive Token Reduction\" Shang…",
  "usage": {
    "total_tokens": 25018,
    "tool_uses": 12,
    "duration_ms": 111668
  },
  "last_tool_name": "WebSearch",
  "uuid": "6821fa18-8234-4549-b03d-276a096f36cf",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 136_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2306.14048 \"H2O: Heavy-Hitter Oracle for Ef…",
  "usage": {
    "total_tokens": 21705,
    "tool_uses": 8,
    "duration_ms": 77077
  },
  "last_tool_name": "WebSearch",
  "uuid": "4ddaf631-f5be-4ced-9246-c85a33b06c82",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 137_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for X-VLA Soft-Prompted Transformer Scalable Cross-Em…",
  "usage": {
    "total_tokens": 24814,
    "tool_uses": 11,
    "duration_ms": 100771
  },
  "last_tool_name": "WebSearch",
  "uuid": "c1027d4e-9269-4747-88c2-0ff04dfa4271",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 138_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"Flamingo: a Visual Language Model for Few-Shot L…",
  "usage": {
    "total_tokens": 26160,
    "tool_uses": 13,
    "duration_ms": 120784
  },
  "last_tool_name": "WebSearch",
  "uuid": "55dbf5c9-9996-45ea-9c1a-892ad65daeed",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 139_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2309.17453 \"Efficient Streaming Language Mo…",
  "usage": {
    "total_tokens": 22797,
    "tool_uses": 9,
    "duration_ms": 87824
  },
  "last_tool_name": "WebSearch",
  "uuid": "db90283e-12d6-4a41-b61b-9c8b46facc90",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 140_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for TinyVLA Fast Data-Efficient Vision-Language-Actio…",
  "usage": {
    "total_tokens": 25929,
    "tool_uses": 12,
    "duration_ms": 114586
  },
  "last_tool_name": "WebSearch",
  "uuid": "5e242159-eb89-4da3-bb81-a14d51b4c353",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 141_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"Visual Instruction Tuning\" Liu Haotian NeurIPS 2…",
  "usage": {
    "total_tokens": 27228,
    "tool_uses": 14,
    "duration_ms": 131308
  },
  "last_tool_name": "WebSearch",
  "uuid": "d6f473d6-ebf6-47e2-a3a1-f13fd37deb13",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 142_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2112.03227 \"CALVIN: A Benchmark for Languag…",
  "usage": {
    "total_tokens": 23746,
    "tool_uses": 10,
    "duration_ms": 99654
  },
  "last_tool_name": "WebSearch",
  "uuid": "afed00c2-a270-4ad6-b1b9-08f17910f870",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 143_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for BART Denoising Sequence-to-Sequence Pre-training …",
  "usage": {
    "total_tokens": 27018,
    "tool_uses": 13,
    "duration_ms": 124920
  },
  "last_tool_name": "WebSearch",
  "uuid": "a1cdc44a-1fe3-4b65-99fc-0fa358c83e00",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 144_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"Real-Time Single Image and Video Super-Resolutio…",
  "usage": {
    "total_tokens": 28133,
    "tool_uses": 15,
    "duration_ms": 141617
  },
  "last_tool_name": "WebSearch",
  "uuid": "4ced1566-f80c-4e9f-b0fd-cfa16d9a8ef0",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 145_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for CALVIN benchmark Mees Oier IEEE Robotics and Auto…",
  "usage": {
    "total_tokens": 24613,
    "tool_uses": 11,
    "duration_ms": 109642
  },
  "last_tool_name": "WebSearch",
  "uuid": "d53efc77-91a9-4b51-83cf-d2065fa1e6c4",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 146_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for TokenLearner Adaptive Space-Time Tokenization Vid…",
  "usage": {
    "total_tokens": 28015,
    "tool_uses": 14,
    "duration_ms": 134302
  },
  "last_tool_name": "WebSearch",
  "uuid": "11fd57e0-5b9c-43eb-9b46-34e4fd64a00d",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 147_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for arXiv 2404.16821 \"How Far Are We to GPT-4V\" Inter…",
  "usage": {
    "total_tokens": 29188,
    "tool_uses": 16,
    "duration_ms": 151435
  },
  "last_tool_name": "WebSearch",
  "uuid": "ae255366-9c3a-4b4f-8b45-db2c3f7f5503",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 148_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2303.04137 \"Diffusion Policy: Visuomotor Po…",
  "usage": {
    "total_tokens": 25510,
    "tool_uses": 12,
    "duration_ms": 119288
  },
  "last_tool_name": "WebSearch",
  "uuid": "56fc982c-ae79-4495-8c4f-eb21473903b0",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 149_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"BLIP-2: Bootstrapping Language-Image Pre-Trainin…",
  "usage": {
    "total_tokens": 30121,
    "tool_uses": 17,
    "duration_ms": 161195
  },
  "last_tool_name": "WebSearch",
  "uuid": "80b926a4-cfcc-4856-a6d1-ad2a4e889098",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 150_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for TokenLearner arXiv title \"What Can 8 Learned Toke…",
  "usage": {
    "total_tokens": 28969,
    "tool_uses": 15,
    "duration_ms": 144735
  },
  "last_tool_name": "WebSearch",
  "uuid": "ee239694-12ee-46b9-9c2b-7c13127ab3fa",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 151_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for Diffusion Policy Chi Cheng RSS 2023 venue confere…",
  "usage": {
    "total_tokens": 26497,
    "tool_uses": 13,
    "duration_ms": 128128
  },
  "last_tool_name": "WebSearch",
  "uuid": "bd674a1a-0648-4dca-89d8-1885ddf4e083",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 152_

```json
{
  "type": "system",
  "subtype": "task_updated",
  "task_id": "a5682b66462dfac8c",
  "patch": {
    "status": "completed",
    "end_time": 1780036498827
  },
  "uuid": "e535cf3f-9957-48ea-8cc7-593bd2e055b5",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 153_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a5682b66462dfac8c",
  "tool_use_id": "toolu_01RZuCncPC5jZr4xRor2mq6b",
  "status": "completed",
  "output_file": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/a5682b66462dfac8c.output",
  "summary": "Agent \"Verify bib entries batch 1 (1-16)\" completed",
  "usage": {
    "total_tokens": 41362,
    "tool_uses": 40,
    "duration_ms": 181072
  },
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "63914dcd-6f17-4b2d-8c49-4a002893f587"
}
```

---

### System

_source line 154_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
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
    "Write"
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
  "uuid": "114f9329-7b42-427f-8ee0-51fa939efb6e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 155_

Batch 1 complete. Key findings: `wang2025specprunevla` needs ICML 2026 update, `black2024pi0` needs RSS 2025 update, `brohan2023rt2` has a minor author ordering discrepancy with PMLR proceedings. Waiting for remaining batches...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "7e97e549-bf72-4a05-ad88-c52f2c0fc93a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZJenChZ1RCATA8riHqKUe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 91434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3600
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

### System

_source line 156_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"Perceiver: General Perception with Iterative Att…",
  "usage": {
    "total_tokens": 31324,
    "tool_uses": 18,
    "duration_ms": 170488
  },
  "last_tool_name": "WebSearch",
  "uuid": "fc989d33-7b5d-472a-b8f5-b991c75af84d",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 157_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for A-ViT Adaptive Tokens Efficient Vision Transforme…",
  "usage": {
    "total_tokens": 30485,
    "tool_uses": 16,
    "duration_ms": 155220
  },
  "last_tool_name": "WebSearch",
  "uuid": "d4a824a7-91fe-4d61-a37c-c84457dc62ec",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 158_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2205.13504 \"Are Transformers Effective for …",
  "usage": {
    "total_tokens": 27449,
    "tool_uses": 14,
    "duration_ms": 136789
  },
  "last_tool_name": "WebSearch",
  "uuid": "325cb1a5-1d6a-4f27-bf74-d8488997ac15",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 159_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for InternVL 1.5 arXiv 2404.16821 accepted conference…",
  "usage": {
    "total_tokens": 32223,
    "tool_uses": 19,
    "duration_ms": 178627
  },
  "last_tool_name": "WebSearch",
  "uuid": "435f2d03-aaf1-44c1-b6a9-e60030310356",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 160_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for AdaViT Adaptive Vision Transformers Efficient Ima…",
  "usage": {
    "total_tokens": 31517,
    "tool_uses": 17,
    "duration_ms": 164270
  },
  "last_tool_name": "WebSearch",
  "uuid": "ae456b03-cd10-4410-b498-620ac4d00a13",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 161_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2406.03980 \"Position: Embracing Negative Re…",
  "usage": {
    "total_tokens": 28379,
    "tool_uses": 15,
    "duration_ms": 146841
  },
  "last_tool_name": "WebSearch",
  "uuid": "84732a3e-0d1e-465e-b1fe-1098e8e879f6",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 162_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for VLA-Pruner arXiv 2511.16449 authors list first au…",
  "usage": {
    "total_tokens": 33097,
    "tool_uses": 20,
    "duration_ms": 186987
  },
  "last_tool_name": "WebSearch",
  "uuid": "aa0b8f33-51c1-4e8b-9709-4b6544728377",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 163_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for SparseViT Revisiting Activation Sparsity Efficien…",
  "usage": {
    "total_tokens": 32412,
    "tool_uses": 18,
    "duration_ms": 172758
  },
  "last_tool_name": "WebSearch",
  "uuid": "bd0e82ec-0eea-429a-a790-4afe62a428d7",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 164_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2304.07193 \"DINOv2: Learning Robust Visual …",
  "usage": {
    "total_tokens": 29116,
    "tool_uses": 16,
    "duration_ms": 156936
  },
  "last_tool_name": "WebSearch",
  "uuid": "9129322c-e029-4c8c-96bd-92e4f73dba9f",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 165_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for VLA-IAP arXiv 2603.22991 full author list Cheng J…",
  "usage": {
    "total_tokens": 33605,
    "tool_uses": 21,
    "duration_ms": 194800
  },
  "last_tool_name": "WebSearch",
  "uuid": "70f339f2-0150-46cd-a748-1b7c746259a9",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 166_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for \"RoFormer: Enhanced Transformer with Rotary Posit…",
  "usage": {
    "total_tokens": 29910,
    "tool_uses": 17,
    "duration_ms": 166179
  },
  "last_tool_name": "WebSearch",
  "uuid": "bc74b46b-607e-4601-bcdf-7a4a37c745df",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 167_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for Fit and Prune Fast Training-free Visual Token Pru…",
  "usage": {
    "total_tokens": 33666,
    "tool_uses": 19,
    "duration_ms": 184880
  },
  "last_tool_name": "WebSearch",
  "uuid": "e5c5ad6c-ef29-44f7-a0c5-a2e56caf7b8c",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 168_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for EfficientVLA arXiv 2506.10100 first author Yang Y…",
  "usage": {
    "total_tokens": 34134,
    "tool_uses": 22,
    "duration_ms": 205924
  },
  "last_tool_name": "WebSearch",
  "uuid": "8f53a6a6-a4b4-434c-b33d-4a26bea831d6",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 169_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2412.01818 FasterVLM authors Zhang Qizhe fu…",
  "usage": {
    "total_tokens": 30632,
    "tool_uses": 18,
    "duration_ms": 174259
  },
  "last_tool_name": "WebSearch",
  "uuid": "0bee84ed-42da-4187-a6ba-7c76b5b19fd0",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 170_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for CrossGET Cross-Guided Ensemble Tokens Acceleratin…",
  "usage": {
    "total_tokens": 34749,
    "tool_uses": 20,
    "duration_ms": 194623
  },
  "last_tool_name": "WebSearch",
  "uuid": "31ae3877-8360-419b-b91c-56b63464b5e9",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 171_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for FastV arXiv 2403.06764 first author \"Chen, Liang\"…",
  "usage": {
    "total_tokens": 34740,
    "tool_uses": 23,
    "duration_ms": 216990
  },
  "last_tool_name": "WebSearch",
  "uuid": "540b43a7-2b1e-4706-a5a8-f6ffb4ada5e7",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 172_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2412.01818 FasterVLM venue accepted confere…",
  "usage": {
    "total_tokens": 31220,
    "tool_uses": 19,
    "duration_ms": 186277
  },
  "last_tool_name": "WebSearch",
  "uuid": "d1bb6811-bd4f-4329-9d96-4032d15a7c46",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 173_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for CogACT Li Qixiu 2024 conference acceptance ICRA R…",
  "usage": {
    "total_tokens": 35680,
    "tool_uses": 21,
    "duration_ms": 206520
  },
  "last_tool_name": "WebSearch",
  "uuid": "b5e5bb3f-3436-47cf-9543-874d69a8adb1",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 174_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for \"How Far Are We to GPT-4V\" InternVL 1.5 Chen Zhe …",
  "usage": {
    "total_tokens": 35577,
    "tool_uses": 24,
    "duration_ms": 227134
  },
  "last_tool_name": "WebSearch",
  "uuid": "1fbef882-afaf-4f46-93d0-e68151e46acf",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 175_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for arXiv 2406.03980 authors \"Karl Florian\" OR \"Bouth…",
  "usage": {
    "total_tokens": 32028,
    "tool_uses": 20,
    "duration_ms": 194989
  },
  "last_tool_name": "WebSearch",
  "uuid": "a278cdc1-0762-499c-a017-c0ead7886f66",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 176_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for TinyVLA Wen Junjie conference accepted venue 2025…",
  "usage": {
    "total_tokens": 36381,
    "tool_uses": 22,
    "duration_ms": 214909
  },
  "last_tool_name": "WebSearch",
  "uuid": "d371ef51-310d-4d9c-b172-4b8b9e2b163a",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 177_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for EfficientVLA arXiv 2506.10100 accepted conference…",
  "usage": {
    "total_tokens": 36565,
    "tool_uses": 25,
    "duration_ms": 236694
  },
  "last_tool_name": "WebSearch",
  "uuid": "6d688163-5bab-4501-9836-f2ba24140046",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 178_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for \"TinyVLA\" ICRA 2025 accepted",
  "usage": {
    "total_tokens": 36973,
    "tool_uses": 23,
    "duration_ms": 224678
  },
  "last_tool_name": "WebSearch",
  "uuid": "5110cb1c-3e7b-4bc7-9165-8315a46958bb",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 179_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for H2O Heavy-Hitter Oracle Zhang Zhenyu NeurIPS 2023…",
  "usage": {
    "total_tokens": 32699,
    "tool_uses": 21,
    "duration_ms": 208933
  },
  "last_tool_name": "WebSearch",
  "uuid": "4c8b3256-1dc2-4953-b960-f52ca3279b26",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 180_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for \"OpenOFT\" \"OpenVLA-OFT\" Kim Moo Jin conference ac…",
  "usage": {
    "total_tokens": 37829,
    "tool_uses": 24,
    "duration_ms": 233637
  },
  "last_tool_name": "WebSearch",
  "uuid": "01b83a7c-a752-453c-af93-80b039375830",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 181_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for RT-2 paper Brohan Anthony authors 2307.15818 firs…",
  "usage": {
    "total_tokens": 33569,
    "tool_uses": 22,
    "duration_ms": 217028
  },
  "last_tool_name": "WebSearch",
  "uuid": "0c1f2b22-6ac3-4fa8-bab0-f093f7ddb78c",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 182_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "description": "Searching for VLA-Cache arXiv 2502.02175 Xu Siyu full author li…",
  "usage": {
    "total_tokens": 38573,
    "tool_uses": 26,
    "duration_ms": 258173
  },
  "last_tool_name": "WebSearch",
  "uuid": "68e0199a-9b8b-4a09-b211-ce43c0a1b17d",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 183_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for Qwen2 Technical Report Yang An accepted conferenc…",
  "usage": {
    "total_tokens": 38880,
    "tool_uses": 25,
    "duration_ms": 242827
  },
  "last_tool_name": "WebSearch",
  "uuid": "b4159f93-eff2-46a7-b914-2b0376514484",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 184_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for Mini-InternVL Gao Zhangwei accepted conference ve…",
  "usage": {
    "total_tokens": 34251,
    "tool_uses": 23,
    "duration_ms": 226921
  },
  "last_tool_name": "WebSearch",
  "uuid": "ad9bd163-8ae7-4256-8640-03c7782c0cc6",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 185_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for Flow Matching Generative Modeling Lipman authors …",
  "usage": {
    "total_tokens": 39627,
    "tool_uses": 26,
    "duration_ms": 252530
  },
  "last_tool_name": "WebSearch",
  "uuid": "0bfbcc0c-6d54-4f9a-84c5-c8251aade78b",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 186_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for Open X-Embodiment Collaboration authors first aut…",
  "usage": {
    "total_tokens": 35050,
    "tool_uses": 24,
    "duration_ms": 237211
  },
  "last_tool_name": "WebSearch",
  "uuid": "69c33075-dbac-4976-a95a-0f51e4fbb57e",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 187_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for \"OpenVLA-OFT\" Kim 2025 CVPR RSS ICML venue accept…",
  "usage": {
    "total_tokens": 40293,
    "tool_uses": 27,
    "duration_ms": 262813
  },
  "last_tool_name": "WebSearch",
  "uuid": "aa683469-adbb-4a48-b1ce-4b07bffba672",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 188_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for RoFormer Su Jianlin arXiv 2104.09864 authors comp…",
  "usage": {
    "total_tokens": 35618,
    "tool_uses": 25,
    "duration_ms": 244671
  },
  "last_tool_name": "WebSearch",
  "uuid": "0a5fa343-c5d1-4de0-ad3f-44359d86aa43",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 189_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for InternVL 2.5 arXiv 2412.05271 accepted conference…",
  "usage": {
    "total_tokens": 36455,
    "tool_uses": 26,
    "duration_ms": 252215
  },
  "last_tool_name": "WebSearch",
  "uuid": "4d41b93f-3048-4760-8a7a-07f8088fa311",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 190_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for TokenLearner Ryoo 2106.11297 arXiv title \"What Ca…",
  "usage": {
    "total_tokens": 41113,
    "tool_uses": 28,
    "duration_ms": 273917
  },
  "last_tool_name": "WebSearch",
  "uuid": "0b77818d-2855-450c-ab41-278f411fa9f1",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 191_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "description": "Searching for Diffusion Policy Chi Cheng RSS 2023 International…",
  "usage": {
    "total_tokens": 37058,
    "tool_uses": 27,
    "duration_ms": 260534
  },
  "last_tool_name": "WebSearch",
  "uuid": "1131ac5c-1cb0-429a-ae73-2c5aaf17c362",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 192_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for arXiv 2510.10274 X-VLA submission date October 20…",
  "usage": {
    "total_tokens": 42002,
    "tool_uses": 29,
    "duration_ms": 284796
  },
  "last_tool_name": "WebSearch",
  "uuid": "3550f09b-63c3-43ca-b4cf-0f185b0c08b3",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 193_

```json
{
  "type": "system",
  "subtype": "task_updated",
  "task_id": "a3c32c2b7d5dda9fa",
  "patch": {
    "status": "completed",
    "end_time": 1780036638453
  },
  "uuid": "c6276dce-91a2-44c1-8e75-9f43a83a6ad8",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 194_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a3c32c2b7d5dda9fa",
  "tool_use_id": "toolu_015T8UARwnwAJ6nXTLZuQmZf",
  "status": "completed",
  "output_file": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/a3c32c2b7d5dda9fa.output",
  "summary": "Agent \"Verify bib entries batch 2 (17-32)\" completed",
  "usage": {
    "total_tokens": 39233,
    "tool_uses": 26,
    "duration_ms": 303537
  },
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "89765000-1a35-479c-b4ef-cd8236ef9037"
}
```

---

### System

_source line 195_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
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
    "Write"
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
  "uuid": "36a94ee2-bcb3-42f9-86f0-fe7ed4d65cf5",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 196_

Batch 2 complete. `shang2024prumerge` has key/year mismatch (should be 2025 for ICCV), `chen2024internvl` was published in a journal. Waiting for batches 3 and 4...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "68ca6f18-648f-41f3-b2ea-e29515c86c7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e5cPJTw3vbhzdv1YEV5tf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2722,
      "cache_read_input_tokens": 95034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2722
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

### System

_source line 197_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "description": "Searching for \"Fit and Prune\" FitPrune authors Ye Weihao comple…",
  "usage": {
    "total_tokens": 42780,
    "tool_uses": 30,
    "duration_ms": 293937
  },
  "last_tool_name": "WebSearch",
  "uuid": "493acf71-1172-4c73-bdde-b96a96bde13e",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 198_

```json
{
  "type": "system",
  "subtype": "task_updated",
  "task_id": "adb06fa7cf287f5e3",
  "patch": {
    "status": "completed",
    "end_time": 1780036685561
  },
  "uuid": "912481c9-1210-4f57-ab4d-7cc20baafa0d",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 199_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "adb06fa7cf287f5e3",
  "tool_use_id": "toolu_0184iYNGgFN4oRK4gXehGH4m",
  "status": "completed",
  "output_file": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/adb06fa7cf287f5e3.output",
  "summary": "Agent \"Verify bib entries batch 4 (49-62)\" completed",
  "usage": {
    "total_tokens": 37911,
    "tool_uses": 27,
    "duration_ms": 315602
  },
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "f20736d2-3eed-4bf8-be2f-8e19b65073e5"
}
```

---

### System

_source line 200_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
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
    "Write"
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
  "uuid": "86f78bd2-ab24-4d7b-8791-7f40f9915f8f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 201_

Batch 4 complete. Critical finding: `bouthillier2024negative` has **wrong author** (should be Karl, Florian et al., not Bouthillier). Also confirmed the RT-2 and DINOv2 duplicates. Waiting for batch 3...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "307782bb-4b6b-4e28-824b-a8e96899c123",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCrT8U3sZNnHFjpF68DLrJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3243,
      "cache_read_input_tokens": 97756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3243
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

### System

_source line 202_

```json
{
  "type": "system",
  "subtype": "task_updated",
  "task_id": "a263b2a81ff95f84b",
  "patch": {
    "status": "completed",
    "end_time": 1780036695730
  },
  "uuid": "a0035ed2-2697-4042-b2e9-7534a7b1e6a9",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a"
}
```

---

### System

_source line 203_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a263b2a81ff95f84b",
  "tool_use_id": "toolu_01E83JnRK5SLSuqYRyRhTcDH",
  "status": "completed",
  "output_file": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/af4e54b1-f61c-4f79-a066-c45795de6b3a/tasks/a263b2a81ff95f84b.output",
  "summary": "Agent \"Verify bib entries batch 3 (33-48)\" completed",
  "usage": {
    "total_tokens": 43666,
    "tool_uses": 30,
    "duration_ms": 344331
  },
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "e6792a6f-0580-4607-acf5-8baa09df7072"
}
```

---

### System

_source line 204_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
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
    "Write"
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
  "uuid": "6a71f0de-f52f-4692-9823-bf99e8c99c78",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 205_

<details><summary>Logged reasoning block</summary>

```text
All 4 batches are complete. Let me now compile the full verification checklist. Let me organize all findings systematically.

Let me compile the complete checklist, merging results from all 4 batches, and also adding the citation usage check and structural issues I found earlier.

Let me organize the entries by whether they're cited in the main paper or not, and flag all issues.

Here are the cited entries in the main paper (files included by main.tex):
- abnar2020quantifying ✓
- gao2025compressorvla ✓
- wang2025specprunevla ✗ (needs ICML 2026 update)


- jiang2026lightvla ✓
- feng2026seewhatmatters ✓
- zhang2025sparsevlm ✓
- khaki2025sparsevila ✓
- jabbour2025dontrun ✓
- shukor2025smolvla ✓
- kim2024openvla ✓
- black2024pi0 ✗ (needs RSS 2025 update)
- black2025pi05 ✓
- chen2024fastv ✓
- xu2025vl ✓

Continuing through the rest of the bibliography, I'm checking entries like cheng2026vlaiap, rao2021dynamicvit, and bolya2023tome which all look good, but I'm spotting a few issues—shang2024prumerge has a key/year mismatch, oquab2023dinov2 appears to be duplicated with a mismatch, and zheng2025xvla is incomplete.

I've also identified a batch of entries that aren't cited anywhere in the document: brohan2023rt2, brohan2023rt1, ghosh2024octo, li2024roboflamingo, chen2024internvl, jaegle2021perceiver, alayrac2022flamingo, oquab2024dinov2, liu2024llava15, chen2024internvl25, gao2024miniinternvl, zitkovich2023rt2, openxembodiment2024, zhang2023h2o, xiao2024streamingllm, mees2022calvin, and chi2023diff.

Now I'm checking the appendix more carefully since some citations might be hiding there. Looking at the grep results, I can see a few additional citations scattered throughout the appendix file, including some entries I'd already marked as cited plus a couple new ones like li2024cogact, yang2025efficientvla, and abnar2020quantifying.

But when I search for alayrac2022flamingo specifically, it doesn't appear anywhere in the main paper or appendix output, even though it's in the bibliography. Checking the draft files confirms they're not part of the final build. So the genuinely uncited entries are brohan2023rt2, brohan2023rt1, ghosh2024octo, li2024roboflamingo, chen2024internvl, jaegle2021perceiver, alayrac2022flamingo, and oquab2024dinov2.

Looking at the full list of uncited entries, I'm seeing 25 out of 62 total—likely remnants from earlier versions that got cut during revisions. Now I need to verify the citation contexts for the entries that are actually cited, starting with the introduction.

The first few citations check out: the dynamic ViT papers are correctly cited for vision transformer token pruning, the VLA-specific papers are properly attributed for token efficiency work, π₀ is right for linear projections, and OpenVLA is correctly cited for MLP projectors. Let me continue verifying the rest of the citations in context. Continuing through the VLA-specific efficiency methods and verifying the background section details about model architectures and training approaches, then moving into the method section to confirm all citations align with their technical descriptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "0443f183-b079-4317-818a-d4947f6df19f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZRmn36t4jmYcjpbqC7TPu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2997,
      "cache_read_input_tokens": 100999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2997
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

_source line 206_

All 4 batches complete. Now compiling the full verification report.

---

# 引用核对清单 — 完整报告

## 一、已引用条目 (37 entries cited in main paper)

```
[✓] abnar2020quantifying | Abnar, Zuidema | "Quantifying Attention Flow in Transformers" | 2020 | ACL 2020
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | venue正确 ✓
- 正文用法: appendix.tex — attention rollout方法引用，用法准确 ✓
```

```
[✓] gao2025compressorvla | Gao et al. | "Compressor-VLA: Instruction-Guided Visual Token Compression..." | 2025 | arXiv 2511.18950
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | arXiv ID正确 ✓
- 正文用法: related_work.tex — 列为VLA token compression concurrent work ✓
```

```
[✗] wang2025specprunevla | Wang et al. | "SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning" | 2025 | arXiv 2509.05614
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | arXiv ID正确 ✓
- 问题: 已被 ICML 2026 接收，bib 仍标记为 arXiv preprint，year=2025 应更新为 2026，venue 应改为 ICML 2026
- 正文用法: related_work.tex — 列为VLA-specific方法 ✓
```

```
[✓] jiang2026lightvla | Jiang et al. | "The Better You Learn, The Smarter You Prune..." | 2026 | ICRA 2026, arXiv 2509.12594
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | venue正确 ✓ | arXiv ID正确 ✓
- 正文用法: related_work.tex — 列为VLA token pruning方法 ✓
```

```
[✓] feng2026seewhatmatters | Feng et al. | "See What Matters: Differentiable Grid Sample Pruning..." | 2026 | ICML 2026, arXiv 2605.11817
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | venue正确 ✓ | arXiv ID正确 ✓
- 正文用法: related_work.tex — 列为VLA-specific方法 ✓
```

```
[✓] zhang2025sparsevlm | Zhang et al. | "SparseVLM: Visual Token Sparsification..." | 2025 | ICML 2025, arXiv 2410.04417
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency方法 ✓
```

```
[✓] khaki2025sparsevila | Khaki et al. | "SparseVILA: Decoupled Visual Sparsity..." | 2025 | ICCV 2025, arXiv 2510.17777
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency方法 ✓
```

```
[✓] jabbour2025dontrun | Jabbour et al. | "Don't Run with Scissors: Pruning Breaks VLA Models..." | 2025 | arXiv 2510.08464
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — concurrent work, "independently observe that pruning breaks VLA policies" ✓
```

```
[✓] shukor2025smolvla | Shukor et al. | "SmolVLA: A Vision-Language-Action Model..." | 2025 | arXiv 2506.01844
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: 全文多处 — 作为主要评估模型之一 ✓
```

```
[✓] kim2024openvla | Kim et al. | "OpenVLA: An Open-Source Vision-Language-Action Model" | 2024 | CoRL 2024
- 验证: 真实存在 ✓ | 全部正确 ✓ (PMLR vol. 270)
- 正文用法: 全文多处 — 作为主要评估模型之一 ✓
```

```
[✗] black2024pi0 | Black et al. | "π₀: A Vision-Language-Action Flow Model for General Robot Control" | 2024 | arXiv 2410.24164
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | arXiv ID正确 ✓
- 问题: 已被 RSS 2025 接收。bib 仍为 arXiv preprint, year=2024。应更新 venue 为 RSS 2025, year 为 2025
- 正文用法: method.tex — "Linear projection (π₀)" ✓; introduction.tex — VLA model示例 ✓
```

```
[✓] black2025pi05 | Black et al. | "π₀.₅: a Vision-Language-Action Model with Open-World Generalization" | 2025 | CoRL 2025, PMLR vol 305, arXiv 2504.16054
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: 全文多处 — 作为主要评估模型之一 ✓
```

```
[✓] chen2024fastv | Chen et al. | "An Image is Worth 1/2 Tokens After Layer 2..." | 2024 | ECCV 2024 (Oral), arXiv 2403.06764
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency方法 ✓
```

```
[✓] xu2025vlacache | Xu et al. | "VLA-Cache: Efficient VLA Manipulation via Adaptive Token Caching" | 2025 | NeurIPS 2025
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex, introduction.tex — VLA token efficiency ✓
```

```
[✓] cheng2026vlaiap | Cheng et al. | "VLA-IAP: Training-Free Visual Token Pruning..." | 2026 | arXiv 2603.22991
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex — VLA token pruning方法 ✓
```

```
[✓] rao2021dynamicvit | Rao et al. | "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification" | 2021 | NeurIPS 2021
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex — ViT token pruning开创性工作 ✓
```

```
[✓] bolya2023tome | Bolya et al. | "Token Merging: Your ViT But Faster" | 2023 | ICLR 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex, appendix.tex — token merging基线方法 ✓
```

```
[✓] liang2022evit | Liang et al. | "Not All Patches are What You Need..." | 2022 | ICLR 2022
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex — ViT token reorganization ✓
```

```
[✓] liu2023libero | Liu et al. | "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" | 2023 | NeurIPS 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: 全文多处 — 评估benchmark ✓
```

```
[✓] yang2025efficientvla | Yang et al. | "EfficientVLA: Training-Free Acceleration and Compression..." | 2025 | arXiv 2506.10100
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex, results — CogACT的literature corroboration来源 ✓
```

```
[✓] liu2025vlapruner | Liu et al. | "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning..." | 2025 | arXiv 2511.16449
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLA-specific pruning方法 ✓
```

```
[✗] shang2024prumerge | Shang et al. | "LLaVA-PruMerge: Adaptive Token Reduction..." | bib year=2025 | ICCV 2025
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | venue正确 (ICCV 2025) ✓
- 问题: (1) bib key 写 "2024" 但 year={2025}，key-year 不一致; (2) 缺少 arXiv ID 2403.15388
- 正文用法: related_work.tex — VLM token reduction方法 ✓
```

```
[✓] liu2023llava | Liu et al. | "Visual Instruction Tuning" | 2023 | NeurIPS 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — "LLaVA projects patches independently through an MLP" ✓
```

```
[✓] shi2016subpixel | Shi et al. | "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel CNN" | 2016 | CVPR 2016
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — "pixel shuffle folds spatial neighborhoods into channels" ✓
```

```
[✓] li2023blip2 | Li et al. | "BLIP-2: Bootstrapping Language-Image Pre-Training..." | 2023 | ICML 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — "uses cross-attention queries" ✓
```

```
[✗] oquab2023dinov2 | Oquab et al. | "DINOv2: Learning Robust Visual Features without Supervision" | year=2024 | TMLR
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | venue正确 (TMLR 2024) ✓
- 问题: (1) bib key 写 "2023" 但 year={2024}，key-year 不一致; (2) 与 oquab2024dinov2 重复（同一篇论文）
- 正文用法: background.tex — OpenVLA vision encoder ✓
```

```
[✓] zhai2023siglip | Zhai et al. | "Sigmoid Loss for Language Image Pre-Training" | 2023 | ICCV 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: background.tex — SmolVLA vision encoder ✓
```

```
[✓] yang2024qwen2 | Yang et al. | "Qwen2 Technical Report" | 2024 | arXiv 2407.10671
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: background.tex — "Qwen2-0.5B language model" ✓
```

```
[✓] lipman2023flow | Lipman et al. | "Flow Matching for Generative Modeling" | 2023 | ICLR 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: background.tex — "conditional flow matching" action head ✓
```

```
[✓] li2024cogact | Li et al. | "CogACT: A Foundational Vision-Language-Action Model..." | 2024 | arXiv 2411.19650
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: results — "CogACT (MLP projector) retains 74.2% SR under 78% pruning" (来自EfficientVLA) ✓
```

```
[✓] kim2025openoft | Kim et al. | "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" | 2025 | arXiv 2502.19645
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: method.tex, results — OFT as OpenVLA fine-tuning variant for CV calibration ✓
```

```
[✗] zheng2025xvla | Zheng et al. | "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment VLA Model" | 2026 | ICLR 2026, arXiv 2510.10274
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | venue正确 (ICLR 2026) ✓ | arXiv ID正确 ✓
- 问题: bib key 写 "2025" 但 bib year={2026}，key-year 不一致（minor，不影响编译）
- 正文用法: 全文多处 — "learned encoders with cross-token self-attention", BART encoder ✓
```

```
[✓] lewis2020bart | Lewis et al. | "BART: Denoising Sequence-to-Sequence Pre-training..." | 2020 | ACL 2020
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: method.tex — "X-VLA uses a 12-layer BART encoder" ✓
```

```
[✓] su2024roformer | Su et al. | "RoFormer: Enhanced Transformer with Rotary Position Embedding" | 2024 | Neurocomputing vol 568
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: appendix.tex — RoPE position encoding reference ✓
```

```
[✓] ye2025fitprune | Ye et al. | "Fit and Prune: Fast and Training-free Visual Token Pruning..." | 2025 | AAAI 2025, arXiv 2409.10197
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency ✓
```

```
[✓] shi2024crossget | Shi et al. | "CrossGET: Cross-Guided Ensemble of Tokens..." | 2024 | ICML 2024, arXiv 2305.17455
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — ViT token pruning方法 ✓
```

```
[✓] yin2022avit | Yin et al. | "A-ViT: Adaptive Tokens for Efficient Vision Transformer" | 2022 | CVPR 2022, arXiv 2112.07658
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — ViT token pruning方法 ✓
```

---

## 二、未引用条目 (25 entries in bib but NOT cited in main paper)

These entries exist in `references.bib` but are not `\cite`d in any file included by `main.tex`. They appear only in draft/deprecated files or nowhere at all.

| Key | Status | Note |
|-----|--------|------|
| `brohan2023rt2` | ✗ minor | First author discrepancy with PMLR (filed under Zitkovich). Also duplicates `zitkovich2023rt2`. |
| `brohan2023rt1` | ✓ | Verified correct. Uncited. |
| `ghosh2024octo` | ✓ | Verified correct. Uncited. |
| `li2024roboflamingo` | ✓ | Verified correct. Uncited. |
| `chen2024internvl` | ✗ | Published in *Science China Information Sciences*, not just arXiv. Uncited. |
| `jaegle2021perceiver` | ✓ | Verified correct. Uncited. |
| `alayrac2022flamingo` | ✓ | Verified correct. Uncited. |
| `oquab2024dinov2` | ✗ | Duplicate of `oquab2023dinov2`. Uncited. Remove one. |
| `liu2024llava15` | ✓ | Verified correct. Uncited. |
| `chen2024internvl25` | ✓ | Verified correct. Uncited. |
| `gao2024miniinternvl` | ✓ | Verified correct. Uncited. |
| `zitkovich2023rt2` | ✗ | First author listed as Zitkovich, but actual first author is Brohan. Duplicate of `brohan2023rt2`. |
| `openxembodiment2024` | ✓ | Verified correct. Uncited. |
| `zhang2023h2o` | ✓ | Verified correct. Uncited. |
| `xiao2024streamingllm` | ✓ | Verified correct. Uncited. |
| `mees2022calvin` | ✓ | Verified correct. Uncited. |
| `chi2023diffusionpolicy` | ✓ | Verified correct. Uncited. |
| `zeng2023transformers_tsf` | ✓ | Verified correct. Uncited (only in draft sections/introduction.tex). |
| `bouthillier2024negative` | ✗ | **WRONG AUTHOR**: actual authors are Karl, Florian et al., NOT Bouthillier, Xavier. |
| `ryoo2021tokenlearner` | ✗ minor | arXiv title was updated to "What Can 8 Learned Tokens Do for Images and Videos?" vs NeurIPS title. Uncited. |
| `meng2022adavit` | ✓ | Verified correct. Uncited. |
| `chen2023sparsevit` | ✓ | Verified correct. Uncited. |
| `zhang2024fastervlm` | ✓ | Verified correct. Uncited. |
| `li2024tokenpacker` | ✗ | Accepted at IJCV 2025, bib only lists arXiv. Uncited. |
| `wen2024tinyvla` | ✓ | Accepted at RA-L 2025, bib only lists arXiv. Uncited. |

---

## 三、问题汇总（按严重程度排序）

### 严重问题 (会被 reviewer 标记)

| # | Key | 问题 | 建议修复 |
|---|-----|------|----------|
| 1 | `bouthillier2024negative` | **作者完全错误**：实际作者是 Karl, Florian 等人，非 Bouthillier, Xavier | 修正作者，改 key 为 `karl2024negative`。但此条目未被引用，可直接删除。 |
| 2 | `black2024pi0` | 已被 **RSS 2025** 接收，bib 仍为 arXiv 2024 | 更新为 `@inproceedings`, year=2025, venue=RSS 2025 |
| 3 | `wang2025specprunevla` | 已被 **ICML 2026** 接收，bib 仍为 arXiv 2025 | 更新为 `@inproceedings`, year=2026, venue=ICML 2026 |

### 中等问题

| # | Key | 问题 | 建议修复 |
|---|-----|------|----------|
| 4 | `brohan2023rt2` + `zitkovich2023rt2` | **重复条目**，同一篇 RT-2 (arXiv 2307.15818) | 删除其中一个。两者都未被引用，可都删。 |
| 5 | `oquab2023dinov2` + `oquab2024dinov2` | **重复条目**，同一篇 DINOv2 (arXiv 2304.07193) | 保留 `oquab2023dinov2`（已被引用），删除 `oquab2024dinov2` |
| 6 | `shang2024prumerge` | bib key 年份 "2024" 与 year={2025}/venue ICCV 2025 不一致；缺 arXiv ID | 改 key 为 `shang2025prumerge`，添加 eprint={2403.15388} |
| 7 | 25 个未引用条目 | bib 中大量条目未在 main paper 中 cite | 清理未使用条目，避免 reviewer 质疑 |

### 轻微问题

| # | Key | 问题 | 建议修复 |
|---|-----|------|----------|
| 8 | `oquab2023dinov2` | key 写 "2023" 但 year={2024} | key-year 不一致，cosmetic |
| 9 | `zheng2025xvla` | key 写 "2025" 但 year={2026} (ICLR 2026) | key-year 不一致，cosmetic |
| 10 | `brohan2023rt2` | PMLR proceedings 以 Zitkovich 为第一作者，bib 以 Brohan 为第一作者 | 两种都有依据（arXiv vs proceedings），但严格来说应与正式出版版一致 |
| 11 | `chen2024internvl` | 已发表于 *Science China Information Sciences*，bib 仅列 arXiv | 未被引用，可删除或更新 venue |
| 12 | `li2024tokenpacker` | 已被 IJCV 2025 接收 | 未被引用，可删除或更新 |
| 13 | `wen2024tinyvla` | 已被 RA-L 2025 接收 | 未被引用，可删除或更新 |
| 14 | `ryoo2021tokenlearner` | arXiv 标题已更新为 "What Can 8 Learned Tokens Do..." | 未被引用，若后续引用需注意标题版本 |

### 正文引用用法检查

所有 37 个被引用条目的正文上下文均准确：每处 `\cite` 的描述与被引论文的实际内容一致，未发现张冠李戴的情况。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "uuid": "2ae7165b-a10a-4698-adef-e1066de21d4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZRmn36t4jmYcjpbqC7TPu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2997,
      "cache_read_input_tokens": 100999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2997
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

### Task result

_source line 207_

All 4 batches complete. Now compiling the full verification report.

---

# 引用核对清单 — 完整报告

## 一、已引用条目 (37 entries cited in main paper)

```
[✓] abnar2020quantifying | Abnar, Zuidema | "Quantifying Attention Flow in Transformers" | 2020 | ACL 2020
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | venue正确 ✓
- 正文用法: appendix.tex — attention rollout方法引用，用法准确 ✓
```

```
[✓] gao2025compressorvla | Gao et al. | "Compressor-VLA: Instruction-Guided Visual Token Compression..." | 2025 | arXiv 2511.18950
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | arXiv ID正确 ✓
- 正文用法: related_work.tex — 列为VLA token compression concurrent work ✓
```

```
[✗] wang2025specprunevla | Wang et al. | "SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning" | 2025 | arXiv 2509.05614
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | arXiv ID正确 ✓
- 问题: 已被 ICML 2026 接收，bib 仍标记为 arXiv preprint，year=2025 应更新为 2026，venue 应改为 ICML 2026
- 正文用法: related_work.tex — 列为VLA-specific方法 ✓
```

```
[✓] jiang2026lightvla | Jiang et al. | "The Better You Learn, The Smarter You Prune..." | 2026 | ICRA 2026, arXiv 2509.12594
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | venue正确 ✓ | arXiv ID正确 ✓
- 正文用法: related_work.tex — 列为VLA token pruning方法 ✓
```

```
[✓] feng2026seewhatmatters | Feng et al. | "See What Matters: Differentiable Grid Sample Pruning..." | 2026 | ICML 2026, arXiv 2605.11817
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | venue正确 ✓ | arXiv ID正确 ✓
- 正文用法: related_work.tex — 列为VLA-specific方法 ✓
```

```
[✓] zhang2025sparsevlm | Zhang et al. | "SparseVLM: Visual Token Sparsification..." | 2025 | ICML 2025, arXiv 2410.04417
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency方法 ✓
```

```
[✓] khaki2025sparsevila | Khaki et al. | "SparseVILA: Decoupled Visual Sparsity..." | 2025 | ICCV 2025, arXiv 2510.17777
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency方法 ✓
```

```
[✓] jabbour2025dontrun | Jabbour et al. | "Don't Run with Scissors: Pruning Breaks VLA Models..." | 2025 | arXiv 2510.08464
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — concurrent work, "independently observe that pruning breaks VLA policies" ✓
```

```
[✓] shukor2025smolvla | Shukor et al. | "SmolVLA: A Vision-Language-Action Model..." | 2025 | arXiv 2506.01844
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: 全文多处 — 作为主要评估模型之一 ✓
```

```
[✓] kim2024openvla | Kim et al. | "OpenVLA: An Open-Source Vision-Language-Action Model" | 2024 | CoRL 2024
- 验证: 真实存在 ✓ | 全部正确 ✓ (PMLR vol. 270)
- 正文用法: 全文多处 — 作为主要评估模型之一 ✓
```

```
[✗] black2024pi0 | Black et al. | "π₀: A Vision-Language-Action Flow Model for General Robot Control" | 2024 | arXiv 2410.24164
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | arXiv ID正确 ✓
- 问题: 已被 RSS 2025 接收。bib 仍为 arXiv preprint, year=2024。应更新 venue 为 RSS 2025, year 为 2025
- 正文用法: method.tex — "Linear projection (π₀)" ✓; introduction.tex — VLA model示例 ✓
```

```
[✓] black2025pi05 | Black et al. | "π₀.₅: a Vision-Language-Action Model with Open-World Generalization" | 2025 | CoRL 2025, PMLR vol 305, arXiv 2504.16054
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: 全文多处 — 作为主要评估模型之一 ✓
```

```
[✓] chen2024fastv | Chen et al. | "An Image is Worth 1/2 Tokens After Layer 2..." | 2024 | ECCV 2024 (Oral), arXiv 2403.06764
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency方法 ✓
```

```
[✓] xu2025vlacache | Xu et al. | "VLA-Cache: Efficient VLA Manipulation via Adaptive Token Caching" | 2025 | NeurIPS 2025
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex, introduction.tex — VLA token efficiency ✓
```

```
[✓] cheng2026vlaiap | Cheng et al. | "VLA-IAP: Training-Free Visual Token Pruning..." | 2026 | arXiv 2603.22991
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex — VLA token pruning方法 ✓
```

```
[✓] rao2021dynamicvit | Rao et al. | "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification" | 2021 | NeurIPS 2021
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex — ViT token pruning开创性工作 ✓
```

```
[✓] bolya2023tome | Bolya et al. | "Token Merging: Your ViT But Faster" | 2023 | ICLR 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex, appendix.tex — token merging基线方法 ✓
```

```
[✓] liang2022evit | Liang et al. | "Not All Patches are What You Need..." | 2022 | ICLR 2022
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex — ViT token reorganization ✓
```

```
[✓] liu2023libero | Liu et al. | "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" | 2023 | NeurIPS 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: 全文多处 — 评估benchmark ✓
```

```
[✓] yang2025efficientvla | Yang et al. | "EfficientVLA: Training-Free Acceleration and Compression..." | 2025 | arXiv 2506.10100
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex, results — CogACT的literature corroboration来源 ✓
```

```
[✓] liu2025vlapruner | Liu et al. | "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning..." | 2025 | arXiv 2511.16449
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLA-specific pruning方法 ✓
```

```
[✗] shang2024prumerge | Shang et al. | "LLaVA-PruMerge: Adaptive Token Reduction..." | bib year=2025 | ICCV 2025
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | venue正确 (ICCV 2025) ✓
- 问题: (1) bib key 写 "2024" 但 year={2025}，key-year 不一致; (2) 缺少 arXiv ID 2403.15388
- 正文用法: related_work.tex — VLM token reduction方法 ✓
```

```
[✓] liu2023llava | Liu et al. | "Visual Instruction Tuning" | 2023 | NeurIPS 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — "LLaVA projects patches independently through an MLP" ✓
```

```
[✓] shi2016subpixel | Shi et al. | "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel CNN" | 2016 | CVPR 2016
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — "pixel shuffle folds spatial neighborhoods into channels" ✓
```

```
[✓] li2023blip2 | Li et al. | "BLIP-2: Bootstrapping Language-Image Pre-Training..." | 2023 | ICML 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — "uses cross-attention queries" ✓
```

```
[✗] oquab2023dinov2 | Oquab et al. | "DINOv2: Learning Robust Visual Features without Supervision" | year=2024 | TMLR
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | venue正确 (TMLR 2024) ✓
- 问题: (1) bib key 写 "2023" 但 year={2024}，key-year 不一致; (2) 与 oquab2024dinov2 重复（同一篇论文）
- 正文用法: background.tex — OpenVLA vision encoder ✓
```

```
[✓] zhai2023siglip | Zhai et al. | "Sigmoid Loss for Language Image Pre-Training" | 2023 | ICCV 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: background.tex — SmolVLA vision encoder ✓
```

```
[✓] yang2024qwen2 | Yang et al. | "Qwen2 Technical Report" | 2024 | arXiv 2407.10671
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: background.tex — "Qwen2-0.5B language model" ✓
```

```
[✓] lipman2023flow | Lipman et al. | "Flow Matching for Generative Modeling" | 2023 | ICLR 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: background.tex — "conditional flow matching" action head ✓
```

```
[✓] li2024cogact | Li et al. | "CogACT: A Foundational Vision-Language-Action Model..." | 2024 | arXiv 2411.19650
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: results — "CogACT (MLP projector) retains 74.2% SR under 78% pruning" (来自EfficientVLA) ✓
```

```
[✓] kim2025openoft | Kim et al. | "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" | 2025 | arXiv 2502.19645
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: method.tex, results — OFT as OpenVLA fine-tuning variant for CV calibration ✓
```

```
[✗] zheng2025xvla | Zheng et al. | "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment VLA Model" | 2026 | ICLR 2026, arXiv 2510.10274
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | venue正确 (ICLR 2026) ✓ | arXiv ID正确 ✓
- 问题: bib key 写 "2025" 但 bib year={2026}，key-year 不一致（minor，不影响编译）
- 正文用法: 全文多处 — "learned encoders with cross-token self-attention", BART encoder ✓
```

```
[✓] lewis2020bart | Lewis et al. | "BART: Denoising Sequence-to-Sequence Pre-training..." | 2020 | ACL 2020
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: method.tex — "X-VLA uses a 12-layer BART encoder" ✓
```

```
[✓] su2024roformer | Su et al. | "RoFormer: Enhanced Transformer with Rotary Position Embedding" | 2024 | Neurocomputing vol 568
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: appendix.tex — RoPE position encoding reference ✓
```

```
[✓] ye2025fitprune | Ye et al. | "Fit and Prune: Fast and Training-free Visual Token Pruning..." | 2025 | AAAI 2025, arXiv 2409.10197
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency ✓
```

```
[✓] shi2024crossget | Shi et al. | "CrossGET: Cross-Guided Ensemble of Tokens..." | 2024 | ICML 2024, arXiv 2305.17455
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — ViT token pruning方法 ✓
```

```
[✓] yin2022avit | Yin et al. | "A-ViT: Adaptive Tokens for Efficient Vision Transformer" | 2022 | CVPR 2022, arXiv 2112.07658
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — ViT token pruning方法 ✓
```

---

## 二、未引用条目 (25 entries in bib but NOT cited in main paper)

These entries exist in `references.bib` but are not `\cite`d in any file included by `main.tex`. They appear only in draft/deprecated files or nowhere at all.

| Key | Status | Note |
|-----|--------|------|
| `brohan2023rt2` | ✗ minor | First author discrepancy with PMLR (filed under Zitkovich). Also duplicates `zitkovich2023rt2`. |
| `brohan2023rt1` | ✓ | Verified correct. Uncited. |
| `ghosh2024octo` | ✓ | Verified correct. Uncited. |
| `li2024roboflamingo` | ✓ | Verified correct. Uncited. |
| `chen2024internvl` | ✗ | Published in *Science China Information Sciences*, not just arXiv. Uncited. |
| `jaegle2021perceiver` | ✓ | Verified correct. Uncited. |
| `alayrac2022flamingo` | ✓ | Verified correct. Uncited. |
| `oquab2024dinov2` | ✗ | Duplicate of `oquab2023dinov2`. Uncited. Remove one. |
| `liu2024llava15` | ✓ | Verified correct. Uncited. |
| `chen2024internvl25` | ✓ | Verified correct. Uncited. |
| `gao2024miniinternvl` | ✓ | Verified correct. Uncited. |
| `zitkovich2023rt2` | ✗ | First author listed as Zitkovich, but actual first author is Brohan. Duplicate of `brohan2023rt2`. |
| `openxembodiment2024` | ✓ | Verified correct. Uncited. |
| `zhang2023h2o` | ✓ | Verified correct. Uncited. |
| `xiao2024streamingllm` | ✓ | Verified correct. Uncited. |
| `mees2022calvin` | ✓ | Verified correct. Uncited. |
| `chi2023diffusionpolicy` | ✓ | Verified correct. Uncited. |
| `zeng2023transformers_tsf` | ✓ | Verified correct. Uncited (only in draft sections/introduction.tex). |
| `bouthillier2024negative` | ✗ | **WRONG AUTHOR**: actual authors are Karl, Florian et al., NOT Bouthillier, Xavier. |
| `ryoo2021tokenlearner` | ✗ minor | arXiv title was updated to "What Can 8 Learned Tokens Do for Images and Videos?" vs NeurIPS title. Uncited. |
| `meng2022adavit` | ✓ | Verified correct. Uncited. |
| `chen2023sparsevit` | ✓ | Verified correct. Uncited. |
| `zhang2024fastervlm` | ✓ | Verified correct. Uncited. |
| `li2024tokenpacker` | ✗ | Accepted at IJCV 2025, bib only lists arXiv. Uncited. |
| `wen2024tinyvla` | ✓ | Accepted at RA-L 2025, bib only lists arXiv. Uncited. |

---

## 三、问题汇总（按严重程度排序）

### 严重问题 (会被 reviewer 标记)

| # | Key | 问题 | 建议修复 |
|---|-----|------|----------|
| 1 | `bouthillier2024negative` | **作者完全错误**：实际作者是 Karl, Florian 等人，非 Bouthillier, Xavier | 修正作者，改 key 为 `karl2024negative`。但此条目未被引用，可直接删除。 |
| 2 | `black2024pi0` | 已被 **RSS 2025** 接收，bib 仍为 arXiv 2024 | 更新为 `@inproceedings`, year=2025, venue=RSS 2025 |
| 3 | `wang2025specprunevla` | 已被 **ICML 2026** 接收，bib 仍为 arXiv 2025 | 更新为 `@inproceedings`, year=2026, venue=ICML 2026 |

### 中等问题

| # | Key | 问题 | 建议修复 |
|---|-----|------|----------|
| 4 | `brohan2023rt2` + `zitkovich2023rt2` | **重复条目**，同一篇 RT-2 (arXiv 2307.15818) | 删除其中一个。两者都未被引用，可都删。 |
| 5 | `oquab2023dinov2` + `oquab2024dinov2` | **重复条目**，同一篇 DINOv2 (arXiv 2304.07193) | 保留 `oquab2023dinov2`（已被引用），删除 `oquab2024dinov2` |
| 6 | `shang2024prumerge` | bib key 年份 "2024" 与 year={2025}/venue ICCV 2025 不一致；缺 arXiv ID | 改 key 为 `shang2025prumerge`，添加 eprint={2403.15388} |
| 7 | 25 个未引用条目 | bib 中大量条目未在 main paper 中 cite | 清理未使用条目，避免 reviewer 质疑 |

### 轻微问题

| # | Key | 问题 | 建议修复 |
|---|-----|------|----------|
| 8 | `oquab2023dinov2` | key 写 "2023" 但 year={2024} | key-year 不一致，cosmetic |
| 9 | `zheng2025xvla` | key 写 "2025" 但 year={2026} (ICLR 2026) | key-year 不一致，cosmetic |
| 10 | `brohan2023rt2` | PMLR proceedings 以 Zitkovich 为第一作者，bib 以 Brohan 为第一作者 | 两种都有依据（arXiv vs proceedings），但严格来说应与正式出版版一致 |
| 11 | `chen2024internvl` | 已发表于 *Science China Information Sciences*，bib 仅列 arXiv | 未被引用，可删除或更新 venue |
| 12 | `li2024tokenpacker` | 已被 IJCV 2025 接收 | 未被引用，可删除或更新 |
| 13 | `wen2024tinyvla` | 已被 RA-L 2025 接收 | 未被引用，可删除或更新 |
| 14 | `ryoo2021tokenlearner` | arXiv 标题已更新为 "What Can 8 Learned Tokens Do..." | 未被引用，若后续引用需注意标题版本 |

### 正文引用用法检查

所有 37 个被引用条目的正文上下文均准确：每处 `\cite` 的描述与被引论文的实际内容一致，未发现张冠李戴的情况。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 127272,
  "duration_api_ms": 1652308,
  "num_turns": 1,
  "stop_reason": "end_turn",
  "session_id": "af4e54b1-f61c-4f79-a066-c45795de6b3a",
  "total_cost_usd": 6.8566674999999995,
  "usage": {
    "input_tokens": 3,
    "cache_creation_input_tokens": 2997,
    "cache_read_input_tokens": 100999,
    "output_tokens": 8740,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 2997,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 8740,
        "cache_read_input_tokens": 100999,
        "cache_creation_input_tokens": 2997,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2997
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1232078,
      "outputTokens": 43374,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 111,
      "costUSD": 2.5589479999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1296,
      "outputTokens": 42282,
      "cacheReadInputTokens": 3317579,
      "cacheCreationInputTokens": 252064,
      "webSearchRequests": 0,
      "costUSD": 4.2977195,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "origin": {
    "kind": "task-notification"
  },
  "uuid": "76449b5f-aa37-49ad-a83f-79c1747a6f8a"
}
```

</details>

---
