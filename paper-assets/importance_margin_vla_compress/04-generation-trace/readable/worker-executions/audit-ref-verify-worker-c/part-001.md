# audit ref verify worker C — Part 1 of 2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[Transcript overview](../audit-ref-verify-worker-c.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/69/699cdd636c701a61426f.json)

## Before a recorded user message

## Before a recorded user message

60 recorded events


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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
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
  "uuid": "1ce897ee-9c1d-4673-8297-523c1ec6d109",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1780041600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5b810c37-beb7-4133-9cdd-ec38f0cbf39e",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### Assistant

_source line 4_

I'll start by reading the bib file and all tex files to gather the full picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "adf37bc3-cf66-45f5-9e3e-60e904e4120f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUxNWRLQ52Tn2QBCD3qusP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12900,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12900
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

<details open><summary>🔧 Tool call — Read · `toolu_01V1uKhcu8D1TUMTqVMZspjj`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5943c2b5-0311-45bd-87ea-667b78d4616e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUxNWRLQ52Tn2QBCD3qusP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12900,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12900
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

_source line 6 · 2026-05-29T06:49:13.402Z_

<details><summary>↩ Tool result · `toolu_01V1uKhcu8D1TUMTqVMZspjj`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d6b7c5f6-3f35-480f-b752-c2c79397984b",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01UfXkp5HwxCuHdekhFdAfua`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "a973f5f8-134c-442e-a664-d9a1522cc25b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUxNWRLQ52Tn2QBCD3qusP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12900,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12900
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

_source line 8 · 2026-05-29T06:49:13.849Z_

<details><summary>↩ Tool result · `toolu_01UfXkp5HwxCuHdekhFdAfua`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "ab64ac1f-433f-46ce-b003-57de78bb1772",
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
    "durationMs": 19,
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
Let me now read all the tex files to extract citations. I'll read the main ones in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "afcdbb0d-f905-4430-8167-3b22cde409f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "37ea4200-3730-4e16-b648-879654af5683",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

<details open><summary>🔧 Tool call — Read · `toolu_01KDR3DrCNJ3JvSNN7USuKqF`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "3fd0521a-1085-4e1a-9510-31845f54f564",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 12 · 2026-05-29T06:49:19.206Z_

<details><summary>↩ Tool result · `toolu_01KDR3DrCNJ3JvSNN7USuKqF`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "a8f3cc1f-b4a1-44c6-9958-1fbdd75bf944",
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

<details open><summary>🔧 Tool call — Read · `toolu_01BATuHwYnrdBZrEgaXmnJSE`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "29e27004-ffbd-4052-8ab1-788bea8fae96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 14 · 2026-05-29T06:49:19.749Z_

<details><summary>↩ Tool result · `toolu_01BATuHwYnrdBZrEgaXmnJSE`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "9a711fd5-755a-4315-ad18-71cfa07a7e3b",
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

<details open><summary>🔧 Tool call — Read · `toolu_01WHBSNMNT2mQbGfuKgScdvL`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "9008ff79-a7ff-46bc-89f9-4aaac14440c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 16 · 2026-05-29T06:49:20.176Z_

<details><summary>↩ Tool result · `toolu_01WHBSNMNT2mQbGfuKgScdvL`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5466ed0a-6792-4701-bf65-bf20637467c2",
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

<details open><summary>🔧 Tool call — Read · `toolu_017dimc2bKsLGWeFzN18jTzF`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "7db7a372-1c8d-419f-85f8-83b4b75499c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 18 · 2026-05-29T06:49:20.649Z_

<details><summary>↩ Tool result · `toolu_017dimc2bKsLGWeFzN18jTzF`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "24312975-969b-4c02-ba84-a2a4cd59f060",
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

<details open><summary>🔧 Tool call — Read · `toolu_01XnNa52jDLeUZde1CdsBFue`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "91811e22-8319-4abb-ad13-a5da51663818",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 20 · 2026-05-29T06:49:21.604Z_

<details><summary>↩ Tool result · `toolu_01XnNa52jDLeUZde1CdsBFue`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "67ad469e-11c6-4734-a158-17feb0dcc939",
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

<details open><summary>🔧 Tool call — Read · `toolu_01YHy1xW4t8f8dat2PFYoYRh`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d13c9105-748b-4699-ab5f-506106ea0ab2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 22 · 2026-05-29T06:49:22.076Z_

<details><summary>↩ Tool result · `toolu_01YHy1xW4t8f8dat2PFYoYRh`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "de8df5de-5d5b-4611-bb67-0bbdd3cbd858",
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

<details open><summary>🔧 Tool call — Read · `toolu_01GALvuNjb8QUGYgSuqPyZYW`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "07296a63-ffc8-417e-8357-0dae0c346b21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 24 · 2026-05-29T06:49:22.557Z_

<details><summary>↩ Tool result · `toolu_01GALvuNjb8QUGYgSuqPyZYW`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d27ce8a6-0fb1-416a-8f90-36cfbe5d7798",
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

<details open><summary>🔧 Tool call — Read · `toolu_01MzQve8PMkMZs46KVd5CWna`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "2f7dee72-afc2-40c0-ac73-db6d808531fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 26 · 2026-05-29T06:49:23.024Z_

<details><summary>↩ Tool result · `toolu_01MzQve8PMkMZs46KVd5CWna`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "b0613924-b2a7-41c0-a374-58c457d4c66d",
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

<details open><summary>🔧 Tool call — Read · `toolu_01CmYrSZD6SZH6sGMzR2fs5z`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "8a35e975-6698-4a57-8fb0-bf3d488820bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 28 · 2026-05-29T06:49:23.606Z_

<details><summary>↩ Tool result · `toolu_01CmYrSZD6SZH6sGMzR2fs5z`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "c2b9012f-5c69-4ebc-9ef4-499dbdd9ba0f",
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

<details open><summary>🔧 Tool call — Read · `toolu_01WXtsHurc3a8onKKHShRjLe`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d0028bc4-44b2-4124-b73a-ba9c9d20dd44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 30 · 2026-05-29T06:49:24.435Z_

<details><summary>↩ Tool result · `toolu_01WXtsHurc3a8onKKHShRjLe`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "93f6a933-8889-4247-9efe-d0a53176382f",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Ps8xspSMLNYuxVGKBTrPcJ`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "6046a8bc-3e23-4d19-bda4-7e57431f8b40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 32 · 2026-05-29T06:49:24.902Z_

<details><summary>↩ Tool result · `toolu_01Ps8xspSMLNYuxVGKBTrPcJ`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d676e085-5aa6-4ebd-9d5b-967f59d28f3f",
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

<details open><summary>🔧 Tool call — Read · `toolu_01E7e6Xz2mTnuDK7GdFbxHhY`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "fb31e93f-b463-416b-bafc-24a43387f99b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 34 · 2026-05-29T06:49:25.404Z_

<details><summary>↩ Tool result · `toolu_01E7e6Xz2mTnuDK7GdFbxHhY`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "6fa9cee8-8c5e-4327-b858-5fe57a711381",
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

<details open><summary>🔧 Tool call — Read · `toolu_01GU9w8cDtYtJpUFooBs6fe5`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "09c8c979-89fd-4421-99e9-ac10a9debfdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 36 · 2026-05-29T06:49:25.855Z_

<details><summary>↩ Tool result · `toolu_01GU9w8cDtYtJpUFooBs6fe5`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5fad95b1-a069-48e0-b087-d4cb5ecb6b4b",
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

<details open><summary>🔧 Tool call — Read · `toolu_01KNRR9dUHVFjy2n5RphYZvK`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "8d6d0e55-2d72-47e5-9fe9-1eeb86d3621e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQoGoae5GVRHbTcpYzMvHQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10016,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10016
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

_source line 38 · 2026-05-29T06:49:26.802Z_

<details><summary>↩ Tool result · reported error · `toolu_01KNRR9dUHVFjy2n5RphYZvK`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "3a730b01-ff3c-4968-92a7-21efc6cdf9ae",
  "tool_use_result": "Error: File content (27358 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
The appendix is too large to read at once. Let me read it in parts to extract citations from there too. Let me also check the other tex files I haven't read yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "536eca1e-165b-4455-8915-aa10edf0148c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbxtV5RAcTJ67TW5RLd1QT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50637,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 50637
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

Let me read the appendix in parts and check the remaining tex files for citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "4cb9cf49-7806-48ed-89b1-b377c70dd9ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbxtV5RAcTJ67TW5RLd1QT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50637,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 50637
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

<details open><summary>🔧 Tool call — Read · `toolu_018ireueSAZdXvLKfbjEfccY`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "a245178d-23de-4489-9040-94f4b1de9062",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbxtV5RAcTJ67TW5RLd1QT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50637,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 50637
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

_source line 42 · 2026-05-29T06:49:33.049Z_

<details><summary>↩ Tool result · `toolu_018ireueSAZdXvLKfbjEfccY`</summary>

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
301	0.90 & $80.4 \pm 0.5$ & $33.6 \pm 1.2$ & $64.2 \pm 1.0$ \\
302	0.85 & $78.1 \pm 1.0$ & $44.9 \pm 1.3$ & $50.8 \pm 1.3$ \\
303	0.75 & $70.6 \pm 2.7$ & $63.0 \pm 1.7$ & $51.4 \pm 1.2$ \\
304	0.70 & $63.2 \pm 1.5$ & $64.6 \pm 1.8$ & $53.0 \pm 1.1$ \\
305	0.50 & $51.7 \pm 1.5$ & $50.4 \pm 0.6$ & $49.4 \pm 1.5$ \\
306	\bottomrule
307	\end{tabular}
308	\end{table}
309	
310	\subsection{$\pi_{0.5}$ L2 Norm Multi-Seed Consistency}
311	\label{app:pi05_multiseed}
312	
313	\begin{table}[ht]
314	\centering
315	\small
316	\caption{$\pi_{0.5}$ L2 norm-based removal across two seeds (500 episodes each). The V-shaped curve is reproduced with near-identical valleys ($\sigma{=}0.1$\,pp at $k{=}0.5$). V-depth: 17.6\,pp (seed42), 21.8\,pp (seed43).}
317	\label{tab:pi05_l2_multiseed}
318	\begin{tabular}{ccccc}
319	\toprule
320	$k$ & Seed 42 (\%) & Seed 43 (\%) & Mean $\pm$ Std & $\Delta$ (pp) \\
321	\midrule
322	0.70 & 55.0 & 57.8 & $56.4 \pm 2.0$ & $+$2.8 \\
323	0.50 & 33.4 & 33.6 & $33.5 \pm 0.1$ & $+$0.2 \\
324	0.30 & 51.0 & 55.4 & $53.2 \pm 3.1$ & $+$4.4 \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	\subsection{$\pi_{0.5}$ Cross-Suite Comparison}
330	\label{app:pi05_crosssuite}
331	
332	\begin{table}[ht]
333	\centering
334	\small
335	\caption{$\pi_{0.5}$ pruning across LIBERO-Object (baseline 98.2\%) and LIBERO-Spatial (baseline 97.2\%), seed\,42, 500 episodes each. Object random exhibits a deep cliff at $k \in [0.85, 0.925]$ absent on Spatial; L2 norm maintains a plateau across suites at high retention ($\leq 2.4$\,pp difference at $k \geq 0.85$).}
336	\label{tab:pi05_crosssuite}
337	\begin{tabular}{ccccc}
338	\toprule
339	\multirow{2}{*}{$k$} & \multicolumn{2}{c}{LIBERO-Object (\%)} & \multicolumn{2}{c}{LIBERO-Spatial (\%)} \\
340	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
341	 & L2 Norm & Random & L2 Norm & Random \\
342	\midrule
343	1.00 & 98.2 & 98.2 & 97.2 & 97.2 \\
344	0.95 & 98.2 & 74.0 & 97.8 & 76.4 \\
345	0.925 & 99.2 & 27.6 & 97.0 & 60.4 \\
346	0.90 & 98.2 & 9.0 & 95.0 & 54.6 \\
347	0.85 & 98.0 & 5.6 & 90.4 & 58.4 \\
348	0.70 & 55.0 & 74.0 & 67.0 & 74.4 \\
349	0.50 & 33.4 & 69.4 & 55.6 & 71.6 \\
350	0.30 & 51.0 & 36.4 & 57.2 & 49.6 \\
351	\bottomrule
352	\end{tabular}
353	\end{table}
354	
355	\begin{figure}[ht]
356	\centering
357	\includegraphics[width=0.85\linewidth]{figures/paper/fig_crosssuite.pdf}
358	\caption{$\pi_{0.5}$ cross-suite pruning profiles. Object random (green solid) exhibits a deep cliff at $k \in [0.85, 0.925]$ with 68\,pp recovery, absent on Spatial (blue solid). L2 norm (dashed) maintains a plateau on both suites through the cliff zone.}
359	\label{fig:crosssuite}
360	\end{figure}
361	
362	The random cliff at $k \in [0.85, 0.925]$ is task-specific: Object collapses from 74.0\% ($k{=}0.95$) to 5.6\% ($k{=}0.85$), whereas Spatial retains 58.4\% at $k{=}0.85$ ($\Delta{=}53$\,pp between suites). Spatial random also exhibits mild non-monotonicity ($k{=}0.925$: 60.4\% $>$ $k{=}0.9$: 54.6\%, $\Delta{=}5.8$\,pp), but this is an order of magnitude smaller than Object's 68\,pp V-dip. The cliff pattern suggests Object manipulation concentrates critical information in specific token subsets whose removal is catastrophic at narrow retention bands; Spatial tasks distribute critical information more uniformly, tolerating moderate random removal without catastrophic failure.
363	
364	L2 norm selection is consistent across suites at high retention ($k \geq 0.85$): Object and Spatial differ by $\leq 2.4$\,pp (Table~\ref{tab:pi05_crosssuite}). At $k \leq 0.7$, both suites exhibit the L2 V-shape (Object valley: 33.4\% at $k{=}0.5$; Spatial valley: 55.6\% at $k{=}0.5$), with Spatial maintaining higher absolute SR throughout. The method preference (random $>$ L2 at $k{=}0.5$; L2 $>$ random at $k{=}0.3$) is consistent across the two suites tested, suggesting the CV-strategy interaction may extend beyond a single task distribution.
365	
366	\subsection{Token Importance Spatial Distribution}
367	\label{app:token_heatmap}
368	
369	\begin{figure}[ht]
370	\centering
371	\includegraphics[width=0.85\linewidth]{figures/paper/fig_token_heatmap.pdf}
372	\caption{$\pi_{0.5}$ token importance spatial distribution (16$\times$16 grid, averaged over timesteps). Left: LIBERO-Object shows a pronounced center-high, edge-low pattern (center rows 7--9: norm $\sim$265--267; edge rows 0, 14--15: norm $\sim$235--236; CV${=}$0.066). Right: LIBERO-Spatial exhibits a flatter distribution (center-edge gap 14.67 vs.\ 21.87; CV${=}$0.059). The 33\% center-edge gap difference quantitatively explains Object's sharp cliff versus Spatial's graceful degradation under random removal.}
373	\label{fig:token_heatmap}
374	\end{figure}
375	
376	Token importance heatmaps reveal that $\pi_{0.5}$'s 768 vision tokens (reshaped to a 16$\times$16 spatial grid after the $\sqrt{d}$-scaled linear projection) exhibit a center-high, edge-low L2 norm pattern. At $k{=}0.9$ (26 tokens removed), L2 norm-based selection discards predominantly edge tokens: 50\% of removed tokens fall in the outermost ring despite edge positions comprising only 23\% of the grid. This spatial concentration is consistent with the center tokens encoding the robot arm and target object, while edge tokens capture less task-relevant background.
377	
378	Random removal at the same ratio samples deletions uniformly across the spatial grid, creating a combinatorial probability of simultaneously removing multiple high-importance center tokens. As more tokens are removed ($k{=}0.925 \to 0.85$), this probability increases sharply, consistent with the observed cliff onset. The asymmetry explains why L2 norm selection maintains a near-baseline plateau through the cliff zone: it preferentially preserves the high-importance center region that random removal disrupts by chance.
379	
380	\subsection{Hypergeometric Cliff Model}
381	\label{app:cliff_model}
382	
383	\begin{figure}[ht]
384	\centering
385	\includegraphics[width=0.85\linewidth]{figures/paper/fig_cliff_model.pdf}
386	\caption{Hypergeometric cliff model for $\pi_{0.5}$ Object random pruning. (a)~Model-predicted collapse probability (dashed) vs.\ observed success rate (solid) across the cliff zone $k \in [0.85, 0.95]$; RMSE${=}$0.018. (b)~$P(\text{collapse})$ curves for Object ($C{=}106$, concentrated) and Spatial ($C \approx 5$, distributed), illustrating why Object exhibits a sharp phase transition absent on Spatial.}
387	\label{fig:cliff_model}
388	\end{figure}
389	
390	The random cliff on $\pi_{0.5}$ Object (Section~\ref{app:cross_suite_extended}) can be modeled as a hypergeometric sampling problem. Among $N{=}768$ vision tokens, $C{=}106$ are critical. $C$ and $T$ are jointly fit by minimizing RMSE against three cliff-zone data points ($k \in \{0.9, 0.925, 0.95\}$; all post-fix confirmed). When $\lfloor N(1{-}k) \rfloor$ tokens are removed uniformly at random, the number of critical tokens removed follows a hypergeometric distribution $\mathrm{Hypergeometric}(N, C, \lfloor N(1{-}k) \rfloor)$. We define performance collapse as removing $\geq T{=}7$ critical tokens simultaneously; the fit yields $C{=}106$, $T{=}7$ with RMSE${=}$0.018. The fitted $C{=}106$ (13.8\% of tokens) is broadly consistent with the top-importance center region identified in the token heatmap (Figure~\ref{fig:token_heatmap}), providing post-hoc interpretability: the ``critical tokens'' correspond to spatially concentrated, high-norm positions encoding the robot arm and target object.
391	
392	The model predicts three characteristic retention ratios: $k{=}0.960$ where $P(\text{collapse}){=}10\%$ (cliff onset), $k{=}0.937$ where $P(\text{collapse}){=}50\%$ (midpoint), and $k{=}0.904$ where $P(\text{collapse}){=}90\%$ (near-complete collapse). The cliff width $\Delta k \approx 0.056$ between 10\% and 90\% collapse probability matches the observed transition from 74.0\% SR ($k{=}0.95$) to 9.0\% SR ($k{=}0.90$). At $k{=}0.85$ the model predicts near-certain collapse ($P{>}0.999$), consistent with the observed 5.6\% SR. The model captures the cliff onset and sharpness but does not explain the V-shape recovery at $k \leq 0.7$, where success rate rebounds to 74.0\%. The recovery lies outside the model's scope (which assumes monotonic collapse probability). We hypothesize that at aggressive pruning the model transitions to a qualitatively different computation regime, potentially relying on coarser spatial features that survive uniform subsampling, but this remains untested.
393	
394	The cross-suite difference emerges naturally from the critical token count. Object manipulation concentrates critical information in $C{=}106$ tokens (13.8\% of the grid), creating a steep increase in $P(\text{collapse} \geq T)$ over a narrow $k$ range. Spatial tasks distribute critical information across approximately $C \approx 5$ tokens, making the probability of simultaneously removing $\geq T$ critical tokens negligible at all tested retention ratios, consistent with Spatial's graceful degradation (58.4\% at $k{=}0.85$ vs.\ Object's 5.6\%).
395	
396	\subsection{OpenVLA Multi-Seed Consistency}
397	\label{app:openvla_multiseed}
398	
399	\begin{table}[ht]
400	\centering
401	\small
402	\caption{OpenVLA success rates (\%) on LIBERO-Object under random token removal across two seeds (500 episodes each). All values are within 5\,pp, confirming the graded degradation curve is reproducible. Main text (Table~\ref{tab:main_results}) uses seed 42 for both L2 and random.}
403	\label{tab:openvla_multiseed}
404	\begin{tabular}{cccc}
405	\toprule
406	$k$ & Seed 7 (\%) & Seed 43 (\%) & $\Delta$ (pp) \\
407	\midrule
408	0.90 & 62.0 & 62.2 & $+$0.2 \\
409	0.70 & 49.0 & 44.4 & $-$4.6 \\
410	0.50 & 37.4 & 35.6 & $-$1.8 \\
411	\bottomrule
412	\end{tabular}
413	\end{table}
414	
415	\subsection{L2 Norm vs.\ Random Scoring on OpenVLA}
416	\label{app:l2_vs_random}
417	
418	\begin{table}[ht]
419	\centering
420	\small
421	\caption{OpenVLA cross-seed comparison on LIBERO-Object (500 episodes per configuration). L2 uses seed$\,{=}\,$42; random uses seed$\,{=}\,$7. Main text (Table~\ref{tab:main_results}) reports seed-42 random where available ($k{=}0.9$: 62.8\%, $k{=}0.5$: 35.8\%). Same-seed (seed42) random at $k{=}0.3$ yields 21.4\% (L2 outperforms by 3.6\,pp); same-seed at $k{=}0.7$ yields 44.4\% (L2 outperforms by 5.4\,pp). $\Delta$ is defined as L2$-$Random (positive indicates L2 advantage).}
422	\label{tab:openvla_l2_vs_random}
423	\begin{tabular}{cccc}
424	\toprule
425	$k$ & L2 Norm SR (\%) & Random SR (\%) & $\Delta$ (pp) \\
426	\midrule
427	0.95 & 70.6 & 69.4 & $+$1.2 \\
428	0.90 & 70.6 & 62.0 & $+$8.6 \\
429	0.70 & 49.8 & 49.0 & $+$0.8 \\
430	0.50 & 39.2 & 37.4 & $+$1.8 \\
431	0.30 & 25.0 & 20.6 & $+$4.4 \\
432	\bottomrule
433	\end{tabular}
434	\end{table}
435	
436	\subsection{X-VLA Cliff Localization: Per-Task Analysis}
437	\label{app:xvla_cliff}
438	
439	\begin{table}[ht]
440	\centering
441	\small
442	\caption{X-VLA per-task success rates (\%) at $k{=}0.80$ (40 of 50 tokens) and $k{=}0.85$ (42 of 50 tokens) on LIBERO-Object. Per-task breakdown is mean of 2 seeds (50 episodes per task per seed, 100 total); overall values are confirmed across 3 seeds ($89.0 \pm 0.7$\% at $k{=}0.80$, $67.9 \pm 0.3$\% at $k{=}0.85$). Despite retaining \emph{fewer} tokens, $k{=}0.80$ outperforms $k{=}0.85$ by 21.1\,pp overall. Four tasks (\textbf{bold}) suffer catastrophic interference ($\Delta \leq -50$\,pp) from two additional low-importance tokens (L2 rank 41--42 of 50) at $k{=}0.85$; the remaining six are unaffected ($|\Delta| \leq 10$\,pp). Cross-seed variance is $\leq 4$\,pp per task.}
443	\label{tab:xvla_cliff_pertask}
444	\begin{tabular}{lccr}
445	\toprule
446	Task & $k{=}0.80$ (\%) & $k{=}0.85$ (\%) & $\Delta$ (pp) \\
447	\midrule
448	alphabet\_soup & 100.0 & 100.0 & 0 \\
449	bbq\_sauce & 85.0 & 87.0 & $+$2 \\
450	\textbf{butter} & \textbf{57.0} & \textbf{0.0} & $\boldsymbol{-57}$ \\
451	\textbf{chocolate\_pudding} & \textbf{88.0} & \textbf{35.0} & $\boldsymbol{-53}$ \\
452	\textbf{cream\_cheese} & \textbf{98.0} & \textbf{45.0} & $\boldsymbol{-53}$ \\
453	\textbf{ketchup} & \textbf{79.0} & \textbf{27.0} & $\boldsymbol{-52}$ \\
454	milk & 85.0 & 95.0 & $+$10 \\
455	orange\_juice & 96.0 & 98.0 & $+$2 \\
456	salad\_dressing & 100.0 & 100.0 & 0 \\
457	tomato\_sauce & 98.0 & 91.0 & $-$7 \\
458	\midrule
459	\textbf{Overall} & \textbf{89.0} & \textbf{67.9} & $\boldsymbol{-21.1}$ \\
460	\bottomrule
461	\end{tabular}
462	\end{table}
463	
464	The non-monotonic pattern is reproducible across both seeds: the same four tasks (butter, chocolate\_pudding, cream\_cheese, ketchup) exhibit catastrophic drops at $k{=}0.85$, while the remaining six maintain or improve performance. This task-specific sensitivity is consistent with the BART encoder creating entangled dependencies among marginal tokens: at $k{=}0.85$, two additional low-importance tokens (L2 rank 41--42) introduce interference that selectively disrupts tasks requiring fine-grained spatial discrimination. The four affected tasks all involve small, visually similar grocery items, while the robust tasks (alphabet\_soup, salad\_dressing) feature distinctive objects or high-contrast targets.
465	
466	\subsection{VTR Per-Task Comparison}
467	
468	\begin{table}[ht]
469	\centering
470	\small
471	\caption{VTR per-task success rates on LIBERO-Object for $M \in \{32, 64, 128\}$ (seed 42; 3-seed means are reported in Table~\ref{tab:vtr_results}). All three achieve similar overall SR (59.8\%--61.6\%), but individual task performance varies substantially across configurations, with per-task differences up to 30 percentage points.}
472	\label{tab:smart_compress_pertask}
473	\begin{tabular}{lcccc}
474	\toprule
475	Task & $M{=}32$ (\%) & $M{=}64$ (\%) & $M{=}128$ (\%) \\
476	\midrule
477	alphabet\_soup & 68 & 74 & 62 \\
478	bbq\_sauce & 46 & 56 & 34 \\
479	butter & 82 & 84 & 82 \\
480	chocolate\_pudding & 90 & 74 & 82 \\
481	cream\_cheese & 64 & 38 & 58 \\
482	ketchup & 66 & 64 & 62 \\
483	milk & 76 & 62 & 56 \\
484	orange\_juice & 28 & 46 & 58 \\
485	salad\_dressing & 60 & 64 & 54 \\
486	tomato\_sauce & 36 & 54 & 50 \\
487	\midrule
488	\textbf{Overall} & \textbf{61.6} & \textbf{61.6} & \textbf{59.8} \\
489	\bottomrule
490	\end{tabular}
491	\end{table}
492	
493	\subsection{VTR Multi-Seed Results}
494	
495	\begin{table}[ht]
496	\centering
497	\small
498	\caption{VTR success rates across three seeds on LIBERO-Object (500 episodes each). Mean $\pm$ std reported.}
499	\label{tab:multi_seed}
500	\begin{tabular}{lccccr}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "3cef8444-edba-473c-bc34-b6551b1e9152",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
      "content": "\\clearpage\n\\appendix\n\n\\section{Full Pruning Results}\n\\label{app:full_results}\n\nTable~\\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\\ref{tab:main_results} for space.\n\n\\begin{table*}[ht]\n\\centering\n\\footnotesize\n\\caption{Available closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \\textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \\textsuperscript{$\\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}\n\\label{tab:full_results}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 99.2 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{OpenVLA}\n& Object  & \\textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\\textsuperscript{$\\dagger$} & -- / -- & 39.2 / 35.8 \\\\\n& Goal    & \\textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n& Spatial & \\textbf{80.0} & -- / -- & 75.0 / 79.8 / 80.4\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n& Long    & \\textbf{52.8} & -- / -- & 43.6 / 46.8 / 44.0\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Extended Discussion}\n\\label{app:extended_discussion}\n\\label{app:discussion}\n\n\\paragraph{Re-encoding and CV diagnostics.}\nBoth cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \\approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels, differentiating X-VLA's threshold-graded behavior (CV$\\,{=}\\,$0.151) from $\\pi_0$'s uniformly critical profile (CV$\\,{=}\\,$0.038); the interaction reverses at $k{=}0.3$ (Appendices~\\ref{app:cv_strategy_interaction},~\\ref{app:cv_extended}).\n\n\\paragraph{Task complexity compresses the importance margin.}\nCV predicts connector-level compressibility, but task complexity determines \\emph{which} scoring method succeeds within a given connector. OpenVLA illustrates the full pattern across LIBERO's complexity gradient (Figure~\\ref{fig:openvla_sweep}).\n\nOn single-step Object, L2 leads at moderate pruning ($+$7.8\\,pp at $k{=}0.9$), but the three methods exhibit staggered cliffs---L2 earliest ($k{=}0.9{\\to}0.85$, $-$15.4\\,pp), random next, attention latest---each defining a distinct effective compression window before converging at $k{=}0.5$ ($<$4.8\\,pp spread). As task complexity increases, the scoring hierarchy inverts. On Goal, random pruning at $k{=}0.9$ \\emph{exceeds} the unpruned baseline ($+$4.8\\,pp; cross-seed confirmed), suggesting OpenVLA's 256 vision tokens are over-provisioned for goal-conditioned tasks---random removal acts as implicit regularization. On Long, the inversion is complete: at $k{=}0.7$, Random (38.8\\%) $>$ L2 (31.2\\%) $>$ Attention (24.0\\%), with attention degrading $2.5{\\times}$ faster than random. The mechanism is consistent: multi-step tasks distribute critical information across tokens with heterogeneous norm profiles; L2 and attention both cluster on locally salient tokens, sacrificing the spatial diversity that compositional reasoning requires.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_openvla_sweep.pdf}\n\\caption{OpenVLA scoring method comparison across four LIBERO suites. On Object, L2 leads at $k{=}0.9$ ($+$7.8\\,pp) but the margin flips at $k{=}0.85$ ($-$5.2\\,pp, Random wins). Goal degrades smoothly with three-method convergence at $k{=}0.7$. On Long, the ranking inverts with compression. No single scoring method dominates across suites or retention ratios.}\n\\label{fig:openvla_sweep}\n\\end{figure}\n\nThis is a concrete manifestation of the two-axis framework (Section~\\ref{sec:two_axis}): Axis~1 (connector architecture) determines \\emph{whether} pruning is viable; Axis~2 (task complexity) determines \\emph{which} scoring method succeeds. CV remains a valid connector diagnostic, but the optimal scoring strategy requires knowledge of both axes.\n\n\\paragraph{Position encoding mediates the V-shape recovery.}\nThe monotonic L2 curve versus the non-monotonic random curve on $\\pi_{0.5}$ Long (Figure~\\ref{fig:cliff_highlight}) reflects an interaction between token selection strategy and positional encoding. L2 norm scoring preserves spatial locality: retained tokens form near-contiguous clusters in the ViT grid, producing continuous position shifts after re-indexing that Gemma's RoPE accommodates smoothly---hence monotonic degradation (86.8\\% $\\to$ 51.7\\% from $k{=}0.95$ to $k{=}0.5$). Random selection creates scattered gaps that produce position aliasing after re-indexing. At $k{\\approx}0.9$, the aliasing is maximally destructive: a small number of randomly placed gaps create highly irregular inter-token spacing, collapsing SR to 33.6\\%. Per-task analysis reveals this aggregate is driven by specific tasks with position-sensitive spatial reasoning: Task~4 (``put mugs on plates'') drops from 80\\% at $k{=}0.7$ to 12\\% at $k{=}0.85$, contributing disproportionately to the V-shape minimum. At $k{=}0.7$, enough tokens are removed that the surviving positions become approximately uniform again, and SR recovers to 64.6\\%---exceeding the $k{=}0.9$ level by ${\\sim}2{\\times}$. The zero-mask ablation (Section~\\ref{sec:zeromask}) provides causal confirmation: zeroing token content while preserving positions yields 98.0\\% SR, while physically removing the same tokens collapses to 9.0\\%. Position encoding, not information content, is the binding constraint---and scoring method determines whether that constraint is violated.\n\n\\paragraph{Per-task reversal within L2-dominant regimes.} The Long $k{=}0.85$ aggregate ($+$33.2\\,pp for L2) masks extreme per-task heterogeneity (per-task $\\sigma{=}$21.5\\,pp). L2 outperforms random on 9 of 10 tasks ($+$16 to $+$52\\,pp), but on Task~6---a dual-object spatial-relation task (``place white mug on plate \\emph{and} chocolate pudding to the right of plate'')---L2 collapses to 8\\% while random achieves 52\\% ($-$44\\,pp reversal). L2 scoring systematically undervalues tokens encoding spatial relationships, which carry low norms but are critical for relational reasoning. This per-task sign flip within an architecture where L2 dominates overall reinforces that no single scoring method is universally safe: task semantics, not just connector architecture or suite-level statistics, determine optimal strategy.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_scoring_crossover.pdf}\n\\caption{Scoring method comparison at $k{=}0.9$ across three models and four LIBERO suites. Cell color encodes SR as a fraction of unpruned baseline; blue bars mark the best method per condition; dashed borders indicate method-indifferent cells ($\\Delta{<}3.5$\\,pp). $\\pi_{0.5}$'s linear connector strongly favors L2 selection, while X-VLA's BART encoder is largely method-indifferent. SmolVLA collapses to 0\\% regardless of method. Compact 2$\\times$2 summary in Appendix Table~\\ref{tab:scoring_crossover_summary}.}\n\\label{fig:scoring_crossover}\n\\end{figure}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_margin_profile.pdf}\n\\caption{Importance margin (L2 $-$ Random SR) on $\\pi_{0.5}$ Long across retention ratios (multi-seed mean $\\pm$ s.d.; $n{=}5$). The margin peaks sharply at $k{=}0.9$ (46.8\\,pp) where random pruning is maximally destructive, then declines asymmetrically: one step above the peak ($k{=}0.95$: 25.6\\,pp) versus four steps below before crossing zero at $k{\\approx}0.71$. At $k{=}0.5$, L2 and Random converge ($|\\Delta|{\\approx}1.3$\\,pp), indicating that scoring method choice matters only in the moderate-pruning window.}\n\\label{fig:margin_profile}\n\\end{figure}\n\n\\paragraph{Limitations (extended).}\nAll closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\\pi_{0}$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\\% official, 44.8\\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.\n\n\\paragraph{Non-monotonicity as structural property.}\nX-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\\% (L2) and 54.0\\% (random), while $k{=}0.9$ recovers to 70.2\\% under L2 selection (Table~\\ref{tab:main_results}). The 0.2\\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.\n\n\\paragraph{$\\pi_{0.5}$ random subsampling anomaly and RoPE amplification.}\nRandom selection on $\\pi_{0.5}$ Object collapses from 74.0\\% at $k{=}0.95$ to 9.0\\% at $k{=}0.9$, then recovers to 74.0\\% at $k{=}0.7$ (Table~\\ref{tab:main_results}). The re-indexing step of our pruning protocol (Section~\\ref{sec:pruning_protocol}) contributes to this non-monotonicity. $\\pi_{0.5}$'s linear connector preserves a one-to-one mapping between spatial patches and token positions; when random removal shifts surviving tokens to new positions, the backbone's Rotary Position Embeddings (RoPE)~\\cite{su2024roformer} encode spatial content at unfamiliar positions, amplifying disruption of learned attention patterns. X-VLA's BART encoder, which redistributes spatial information via cross-attention and lacks RoPE, provides a partial control. At $k{=}0.85$, single-step suites degrade smoothly (Spatial~68.2\\%, Object~65.0\\%, Goal~60.4\\%), but Long drops to 35.0\\%, below its $k{=}0.5$ performance of 61.6\\% (Table~\\ref{tab:xvla_k085_crosssuite}). Random re-indexing thus induces non-monotonic behavior for complex tasks even without RoPE, but RoPE amplifies the reversal: $\\pi_{0.5}$ Object drops to 5.6\\% at $k{=}0.85$ versus 69.4\\% at $k{=}0.5$ ($-$63.8\\,pp), more than double X-VLA Long's $-$26.6\\,pp. The V-shaped recovery at $k \\leq 0.7$ remains unexplained.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Random pruning at $k{=}0.85$: X-VLA (BART encoder) vs.\\ $\\pi_{0.5}$ (linear connector). X-VLA degrades smoothly on single-step suites (60--68\\%) but drops to 35.0\\% on Long (below $k{=}0.5$); $\\pi_{0.5}$ exhibits a severe disruption peak on Object.}\n\\label{tab:xvla_k085_crosssuite}\n\\begin{tabular}{lcccc}\n\\toprule\nSuite & X-VLA SR (\\%) & $\\Delta$ & $\\pi_{0.5}$ SR (\\%) & $\\Delta$ \\\\\n\\midrule\nObject & 65.0 & $-$34.2 & 3.6--5.6\\textsuperscript{$\\dagger$} & $-$93 to $-$95 \\\\\nGoal & 60.4 & $-$38.0 & 52.4 & $-$44.0 \\\\\nSpatial & 68.2 & $-$24.8 & --- & --- \\\\\nLong & 35.0 & $-$59.0 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize\\textsuperscript{$\\dagger$}Two seeds: seed42$\\,{=}\\,$5.6\\% (post-fix), seed43$\\,{=}\\,$3.6\\%. $\\Delta$ from respective baselines.}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Small-$N$ interactions.}\nX-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.6\\,pp on Goal and $-$47.0\\,pp on Long (L2 norm selection). Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.\n\n\\paragraph{Design implications.}\nPractitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.\n\n\n\\section{Cross-Suite Task Complexity Analysis}\n\\label{app:cross_suite_extended}\n\nLIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.\n\n$\\pi_{0.5}$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\\% (matching the baseline), Spatial retains 97.8\\% (within noise of the 97.2\\% baseline), and Goal drops to 89.4\\% ($-$7.0\\,pp from 96.4\\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\\% token removal.\n\nX-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 99.2\\% (matching the 99.2\\% baseline), while Goal drops to 70.2\\% ($-$28.2\\,pp from 98.4\\% baseline). Under random pruning at the same ratio, Object loses just 1.4\\,pp (97.8\\%) while Goal loses 27.8\\,pp (70.6\\%), a $20{\\times}$ amplification. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\\% to 47.0\\% (L2) and 48.2\\% (random), a 47.0\\,pp loss with only 1.2\\,pp method gap, while Object at the same ratio loses only 0.2\\,pp.\n\nToken-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\\pi_{0.5}$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.\n\n\n\\section{Pruning Protocol Details}\n\\label{app:pruning_details}\n\nBoth pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\\pi_{0.5}$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\\ three-layer MLP), backbone (PaliGemma vs.\\ Llama-2), and encoder fusion strategy (single SigLIP vs.\\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.\n\n\n\\section{SmolVLA Pruning Ablation}\n\\label{app:smolvla_ablation}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\\% SR. Two independent evaluations of the official HF checkpoint (59.2\\% and 57.2\\% baseline, within CI) confirm the cliff-edge across scoring methods.}\n\\label{tab:smolvla_ablation}\n\\begin{tabular}{llccrr}\n\\toprule\nScoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\\\\n\\midrule\nACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\\\\nACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint, eval protocol A (59.2\\% baseline)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\\\\nRandom & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint, eval protocol B (57.2\\% baseline)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 57.2 & 500 & [52.9, 61.4] \\\\\nRandom & 0.95 & True removal & 0.0 & 500 & [0, 0.76] \\\\\nL2 norm & 0.90 & True removal & 0.0 & 500 & [0, 0.76] \\\\\nL2 norm & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task Breakdown Tables}\n\\label{app:per_task}\n\n\\subsection{SmolVLA Baseline Per-Task Results}\n\nTable~\\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\\ref{tab:smolvla_ablation}) produce 0\\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\\% already reported.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\\%.}\n\\label{tab:smolvla_baseline_pertask}\n\\begin{tabular}{lc}\n\\toprule\nTask & SR (\\%) \\\\\n\\midrule\nalphabet\\_soup & 22 \\\\\nbbq\\_sauce & 60 \\\\\nbutter & 42 \\\\\nchocolate\\_pudding & 38 \\\\\ncream\\_cheese & 58 \\\\\nketchup & 26 \\\\\nmilk & 62 \\\\\norange\\_juice & 38 \\\\\nsalad\\_dressing & 50 \\\\\ntomato\\_sauce & 52 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{44.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Official SmolVLA Checkpoint Per-Task Results}\n\nTable~\\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\\_libero). Under 50\\% random token removal, all tasks produce 0\\% SR, identical to the fine-tuned checkpoint results.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\\%. Under 50\\% random pruning, all tasks collapse to 0\\%. An independent evaluation (protocol B) yields 57.2\\% baseline with identical cliff-edge (Table~\\ref{tab:smolvla_ablation}).}\n\\label{tab:smolvla_official_pertask}\n\\begin{tabular}{lcc}\n\\toprule\nTask & Baseline SR (\\%) & $k{=}0.5$ SR (\\%) \\\\\n\\midrule\nalphabet\\_soup & 64 & 0 \\\\\nbbq\\_sauce & 38 & 0 \\\\\nbutter & 78 & 0 \\\\\nchocolate\\_pudding & 90 & 0 \\\\\ncream\\_cheese & 40 & 0 \\\\\nketchup & 60 & 0 \\\\\nmilk & 52 & 0 \\\\\norange\\_juice & 80 & 0 \\\\\nsalad\\_dressing & 44 & 0 \\\\\ntomato\\_sauce & 46 & 0 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{59.2} & \\textbf{0.0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{OpenVLA Per-Task Results Under Pruning}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA per-task success rates (\\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\\%. Tasks requiring fine-grained discrimination (butter, cream\\_cheese) degrade earliest; visually distinctive targets (orange\\_juice, salad\\_dressing) are most resilient.}\n\\label{tab:openvla_pertask}\n\\begin{tabular}{lccccc}\n\\toprule\nTask & $k{=}0.95$ & $k{=}0.90$ & $k{=}0.70$ & $k{=}0.50$ & $k{=}0.30$ \\\\\n\\midrule\nalphabet\\_soup & 76 & 70 & 74 & 60 & 14 \\\\\nbbq\\_sauce & 38 & 28 & 46 & 44 & 30 \\\\\nbutter & 84 & 76 & 10 & 2 & 0 \\\\\nchocolate\\_pudding & 54 & 56 & 32 & 40 & 10 \\\\\ncream\\_cheese & 84 & 78 & 18 & 8 & 0 \\\\\nketchup & 82 & 70 & 68 & 50 & 30 \\\\\nmilk & 46 & 42 & 40 & 24 & 8 \\\\\norange\\_juice & 74 & 60 & 76 & 72 & 42 \\\\\nsalad\\_dressing & 64 & 54 & 64 & 36 & 64 \\\\\ntomato\\_sauce & 92 & 86 & 62 & 38 & 8 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{69.4} & \\textbf{62.0} & \\textbf{49.0} & \\textbf{37.4} & \\textbf{20.6} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{OpenVLA Full Degradation Curve}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA success rates on LIBERO-Object under random token removal at six retention ratios (50 episodes per task, 500 total per ratio). Baseline SR: 74.0\\%. All confidence intervals are Wilson 95\\%.}\n\\label{tab:openvla_full}\n\\begin{tabular}{ccrr}\n\\toprule\n$k$ & Tokens Retained & SR (\\%) & Wilson 95\\% CI \\\\\n\\midrule\n1.00 (baseline) & 256 & 74.0 & [69.9, 77.7] \\\\\n0.95 & 243 & 69.4 & [65.2, 73.3] \\\\\n0.90 & 230 & 62.0 & [57.7, 66.2] \\\\\n0.70 & 179 & 49.0 & [44.6, 53.4] \\\\\n0.50 & 128 & 37.4 & [33.3, 41.7] \\\\\n0.30 & 77 & 20.6 & [17.2, 24.4] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$\\pi_{0.5}$ LIBERO-Long Five-Seed Results}\n\\label{app:pi05_long_multiseed}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ LIBERO-Long success rates (\\%) across five seeds (500 episodes each). All values are means over seeds 42--46 with sample standard deviation (ddof$\\,{=}\\,$1). The importance margin (L2$-$Random) peaks at $k{=}0.9$ (46.8\\,pp) and crosses zero near $k{\\approx}0.71$. Maximum per-seed range is 5.8\\,pp (L2, $k{=}0.75$).}\n\\label{tab:pi05_long_multiseed}\n\\begin{tabular}{cccc}\n\\toprule\n$k$ & L2 Norm (\\%) & Random (\\%) & Attention (\\%) \\\\\n\\midrule\n0.95 & $86.8 \\pm 0.8$ & $61.2 \\pm 0.7$ & $77.3 \\pm 1.2$ \\\\\n0.90 & $80.4 \\pm 0.5$ & $33.6 \\pm 1.2$ & $64.2 \\pm 1.0$ \\\\\n0.85 & $78.1 \\pm 1.0$ & $44.9 \\pm 1.3$ & $50.8 \\pm 1.3$ \\\\\n0.75 & $70.6 \\pm 2.7$ & $63.0 \\pm 1.7$ & $51.4 \\pm 1.2$ \\\\\n0.70 & $63.2 \\pm 1.5$ & $64.6 \\pm 1.8$ & $53.0 \\pm 1.1$ \\\\\n0.50 & $51.7 \\pm 1.5$ & $50.4 \\pm 0.6$ & $49.4 \\pm 1.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$\\pi_{0.5}$ L2 Norm Multi-Seed Consistency}\n\\label{app:pi05_multiseed}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ L2 norm-based removal across two seeds (500 episodes each). The V-shaped curve is reproduced with near-identical valleys ($\\sigma{=}0.1$\\,pp at $k{=}0.5$). V-depth: 17.6\\,pp (seed42), 21.8\\,pp (seed43).}\n\\label{tab:pi05_l2_multiseed}\n\\begin{tabular}{ccccc}\n\\toprule\n$k$ & Seed 42 (\\%) & Seed 43 (\\%) & Mean $\\pm$ Std & $\\Delta$ (pp) \\\\\n\\midrule\n0.70 & 55.0 & 57.8 & $56.4 \\pm 2.0$ & $+$2.8 \\\\\n0.50 & 33.4 & 33.6 & $33.5 \\pm 0.1$ & $+$0.2 \\\\\n0.30 & 51.0 & 55.4 & $53.2 \\pm 3.1$ & $+$4.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$\\pi_{0.5}$ Cross-Suite Comparison}\n\\label{app:pi05_crosssuite}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ pruning across LIBERO-Object (baseline 98.2\\%) and LIBERO-Spatial (baseline 97.2\\%), seed\\,42, 500 episodes each. Object random exhibits a deep cliff at $k \\in [0.85, 0.925]$ absent on Spatial; L2 norm maintains a plateau across suites at high retention ($\\leq 2.4$\\,pp difference at $k \\geq 0.85$).}\n\\label{tab:pi05_crosssuite}\n\\begin{tabular}{ccccc}\n\\toprule\n\\multirow{2}{*}{$k$} & \\multicolumn{2}{c}{LIBERO-Object (\\%)} & \\multicolumn{2}{c}{LIBERO-Spatial (\\%)} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & L2 Norm & Random & L2 Norm & Random \\\\\n\\midrule\n1.00 & 98.2 & 98.2 & 97.2 & 97.2 \\\\\n0.95 & 98.2 & 74.0 & 97.8 & 76.4 \\\\\n0.925 & 99.2 & 27.6 & 97.0 & 60.4 \\\\\n0.90 & 98.2 & 9.0 & 95.0 & 54.6 \\\\\n0.85 & 98.0 & 5.6 & 90.4 & 58.4 \\\\\n0.70 & 55.0 & 74.0 & 67.0 & 74.4 \\\\\n0.50 & 33.4 & 69.4 & 55.6 & 71.6 \\\\\n0.30 & 51.0 & 36.4 & 57.2 & 49.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_crosssuite.pdf}\n\\caption{$\\pi_{0.5}$ cross-suite pruning profiles. Object random (green solid) exhibits a deep cliff at $k \\in [0.85, 0.925]$ with 68\\,pp recovery, absent on Spatial (blue solid). L2 norm (dashed) maintains a plateau on both suites through the cliff zone.}\n\\label{fig:crosssuite}\n\\end{figure}\n\nThe random cliff at $k \\in [0.85, 0.925]$ is task-specific: Object collapses from 74.0\\% ($k{=}0.95$) to 5.6\\% ($k{=}0.85$), whereas Spatial retains 58.4\\% at $k{=}0.85$ ($\\Delta{=}53$\\,pp between suites). Spatial random also exhibits mild non-monotonicity ($k{=}0.925$: 60.4\\% $>$ $k{=}0.9$: 54.6\\%, $\\Delta{=}5.8$\\,pp), but this is an order of magnitude smaller than Object's 68\\,pp V-dip. The cliff pattern suggests Object manipulation concentrates critical information in specific token subsets whose removal is catastrophic at narrow retention bands; Spatial tasks distribute critical information more uniformly, tolerating moderate random removal without catastrophic failure.\n\nL2 norm selection is consistent across suites at high retention ($k \\geq 0.85$): Object and Spatial differ by $\\leq 2.4$\\,pp (Table~\\ref{tab:pi05_crosssuite}). At $k \\leq 0.7$, both suites exhibit the L2 V-shape (Object valley: 33.4\\% at $k{=}0.5$; Spatial valley: 55.6\\% at $k{=}0.5$), with Spatial maintaining higher absolute SR throughout. The method preference (random $>$ L2 at $k{=}0.5$; L2 $>$ random at $k{=}0.3$) is consistent across the two suites tested, suggesting the CV-strategy interaction may extend beyond a single task distribution.\n\n\\subsection{Token Importance Spatial Distribution}\n\\label{app:token_heatmap}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_token_heatmap.pdf}\n\\caption{$\\pi_{0.5}$ token importance spatial distribution (16$\\times$16 grid, averaged over timesteps). Left: LIBERO-Object shows a pronounced center-high, edge-low pattern (center rows 7--9: norm $\\sim$265--267; edge rows 0, 14--15: norm $\\sim$235--236; CV${=}$0.066). Right: LIBERO-Spatial exhibits a flatter distribution (center-edge gap 14.67 vs.\\ 21.87; CV${=}$0.059). The 33\\% center-edge gap difference quantitatively explains Object's sharp cliff versus Spatial's graceful degradation under random removal.}\n\\label{fig:token_heatmap}\n\\end{figure}\n\nToken importance heatmaps reveal that $\\pi_{0.5}$'s 768 vision tokens (reshaped to a 16$\\times$16 spatial grid after the $\\sqrt{d}$-scaled linear projection) exhibit a center-high, edge-low L2 norm pattern. At $k{=}0.9$ (26 tokens removed), L2 norm-based selection discards predominantly edge tokens: 50\\% of removed tokens fall in the outermost ring despite edge positions comprising only 23\\% of the grid. This spatial concentration is consistent with the center tokens encoding the robot arm and target object, while edge tokens capture less task-relevant background.\n\nRandom removal at the same ratio samples deletions uniformly across the spatial grid, creating a combinatorial probability of simultaneously removing multiple high-importance center tokens. As more tokens are removed ($k{=}0.925 \\to 0.85$), this probability increases sharply, consistent with the observed cliff onset. The asymmetry explains why L2 norm selection maintains a near-baseline plateau through the cliff zone: it preferentially preserves the high-importance center region that random removal disrupts by chance.\n\n\\subsection{Hypergeometric Cliff Model}\n\\label{app:cliff_model}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_cliff_model.pdf}\n\\caption{Hypergeometric cliff model for $\\pi_{0.5}$ Object random pruning. (a)~Model-predicted collapse probability (dashed) vs.\\ observed success rate (solid) across the cliff zone $k \\in [0.85, 0.95]$; RMSE${=}$0.018. (b)~$P(\\text{collapse})$ curves for Object ($C{=}106$, concentrated) and Spatial ($C \\approx 5$, distributed), illustrating why Object exhibits a sharp phase transition absent on Spatial.}\n\\label{fig:cliff_model}\n\\end{figure}\n\nThe random cliff on $\\pi_{0.5}$ Object (Section~\\ref{app:cross_suite_extended}) can be modeled as a hypergeometric sampling problem. Among $N{=}768$ vision tokens, $C{=}106$ are critical. $C$ and $T$ are jointly fit by minimizing RMSE against three cliff-zone data points ($k \\in \\{0.9, 0.925, 0.95\\}$; all post-fix confirmed). When $\\lfloor N(1{-}k) \\rfloor$ tokens are removed uniformly at random, the number of critical tokens removed follows a hypergeometric distribution $\\mathrm{Hypergeometric}(N, C, \\lfloor N(1{-}k) \\rfloor)$. We define performance collapse as removing $\\geq T{=}7$ critical tokens simultaneously; the fit yields $C{=}106$, $T{=}7$ with RMSE${=}$0.018. The fitted $C{=}106$ (13.8\\% of tokens) is broadly consistent with the top-importance center region identified in the token heatmap (Figure~\\ref{fig:token_heatmap}), providing post-hoc interpretability: the ``critical tokens'' correspond to spatially concentrated, high-norm positions encoding the robot arm and target object.\n\nThe model predicts three characteristic retention ratios: $k{=}0.960$ where $P(\\text{collapse}){=}10\\%$ (cliff onset), $k{=}0.937$ where $P(\\text{collapse}){=}50\\%$ (midpoint), and $k{=}0.904$ where $P(\\text{collapse}){=}90\\%$ (near-complete collapse). The cliff width $\\Delta k \\approx 0.056$ between 10\\% and 90\\% collapse probability matches the observed transition from 74.0\\% SR ($k{=}0.95$) to 9.0\\% SR ($k{=}0.90$). At $k{=}0.85$ the model predicts near-certain collapse ($P{>}0.999$), consistent with the observed 5.6\\% SR. The model captures the cliff onset and sharpness but does not explain the V-shape recovery at $k \\leq 0.7$, where success rate rebounds to 74.0\\%. The recovery lies outside the model's scope (which assumes monotonic collapse probability). We hypothesize that at aggressive pruning the model transitions to a qualitatively different computation regime, potentially relying on coarser spatial features that survive uniform subsampling, but this remains untested.\n\nThe cross-suite difference emerges naturally from the critical token count. Object manipulation concentrates critical information in $C{=}106$ tokens (13.8\\% of the grid), creating a steep increase in $P(\\text{collapse} \\geq T)$ over a narrow $k$ range. Spatial tasks distribute critical information across approximately $C \\approx 5$ tokens, making the probability of simultaneously removing $\\geq T$ critical tokens negligible at all tested retention ratios, consistent with Spatial's graceful degradation (58.4\\% at $k{=}0.85$ vs.\\ Object's 5.6\\%).\n\n\\subsection{OpenVLA Multi-Seed Consistency}\n\\label{app:openvla_multiseed}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA success rates (\\%) on LIBERO-Object under random token removal across two seeds (500 episodes each). All values are within 5\\,pp, confirming the graded degradation curve is reproducible. Main text (Table~\\ref{tab:main_results}) uses seed 42 for both L2 and random.}\n\\label{tab:openvla_multiseed}\n\\begin{tabular}{cccc}\n\\toprule\n$k$ & Seed 7 (\\%) & Seed 43 (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n0.90 & 62.0 & 62.2 & $+$0.2 \\\\\n0.70 & 49.0 & 44.4 & $-$4.6 \\\\\n0.50 & 37.4 & 35.6 & $-$1.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L2 Norm vs.\\ Random Scoring on OpenVLA}\n\\label{app:l2_vs_random}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA cross-seed comparison on LIBERO-Object (500 episodes per configuration). L2 uses seed$\\,{=}\\,$42; random uses seed$\\,{=}\\,$7. Main text (Table~\\ref{tab:main_results}) reports seed-42 random where available ($k{=}0.9$: 62.8\\%, $k{=}0.5$: 35.8\\%). Same-seed (seed42) random at $k{=}0.3$ yields 21.4\\% (L2 outperforms by 3.6\\,pp); same-seed at $k{=}0.7$ yields 44.4\\% (L2 outperforms by 5.4\\,pp). $\\Delta$ is defined as L2$-$Random (positive indicates L2 advantage).}\n\\label{tab:openvla_l2_vs_random}\n\\begin{tabular}{cccc}\n\\toprule\n$k$ & L2 Norm SR (\\%) & Random SR (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n0.95 & 70.6 & 69.4 & $+$1.2 \\\\\n0.90 & 70.6 & 62.0 & $+$8.6 \\\\\n0.70 & 49.8 & 49.0 & $+$0.8 \\\\\n0.50 & 39.2 & 37.4 & $+$1.8 \\\\\n0.30 & 25.0 & 20.6 & $+$4.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{X-VLA Cliff Localization: Per-Task Analysis}\n\\label{app:xvla_cliff}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{X-VLA per-task success rates (\\%) at $k{=}0.80$ (40 of 50 tokens) and $k{=}0.85$ (42 of 50 tokens) on LIBERO-Object. Per-task breakdown is mean of 2 seeds (50 episodes per task per seed, 100 total); overall values are confirmed across 3 seeds ($89.0 \\pm 0.7$\\% at $k{=}0.80$, $67.9 \\pm 0.3$\\% at $k{=}0.85$). Despite retaining \\emph{fewer} tokens, $k{=}0.80$ outperforms $k{=}0.85$ by 21.1\\,pp overall. Four tasks (\\textbf{bold}) suffer catastrophic interference ($\\Delta \\leq -50$\\,pp) from two additional low-importance tokens (L2 rank 41--42 of 50) at $k{=}0.85$; the remaining six are unaffected ($|\\Delta| \\leq 10$\\,pp). Cross-seed variance is $\\leq 4$\\,pp per task.}\n\\label{tab:xvla_cliff_pertask}\n\\begin{tabular}{lccr}\n\\toprule\nTask & $k{=}0.80$ (\\%) & $k{=}0.85$ (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nalphabet\\_soup & 100.0 & 100.0 & 0 \\\\\nbbq\\_sauce & 85.0 & 87.0 & $+$2 \\\\\n\\textbf{butter} & \\textbf{57.0} & \\textbf{0.0} & $\\boldsymbol{-57}$ \\\\\n\\textbf{chocolate\\_pudding} & \\textbf{88.0} & \\textbf{35.0} & $\\boldsymbol{-53}$ \\\\\n\\textbf{cream\\_cheese} & \\textbf{98.0} & \\textbf{45.0} & $\\boldsymbol{-53}$ \\\\\n\\textbf{ketchup} & \\textbf{79.0} & \\textbf{27.0} & $\\boldsymbol{-52}$ \\\\\nmilk & 85.0 & 95.0 & $+$10 \\\\\norange\\_juice & 96.0 & 98.0 & $+$2 \\\\\nsalad\\_dressing & 100.0 & 100.0 & 0 \\\\\ntomato\\_sauce & 98.0 & 91.0 & $-$7 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{89.0} & \\textbf{67.9} & $\\boldsymbol{-21.1}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe non-monotonic pattern is reproducible across both seeds: the same four tasks (butter, chocolate\\_pudding, cream\\_cheese, ketchup) exhibit catastrophic drops at $k{=}0.85$, while the remaining six maintain or improve performance. This task-specific sensitivity is consistent with the BART encoder creating entangled dependencies among marginal tokens: at $k{=}0.85$, two additional low-importance tokens (L2 rank 41--42) introduce interference that selectively disrupts tasks requiring fine-grained spatial discrimination. The four affected tasks all involve small, visually similar grocery items, while the robust tasks (alphabet\\_soup, salad\\_dressing) feature distinctive objects or high-contrast targets.\n\n\\subsection{VTR Per-Task Comparison}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR per-task success rates on LIBERO-Object for $M \\in \\{32, 64, 128\\}$ (seed 42; 3-seed means are reported in Table~\\ref{tab:vtr_results}). All three achieve similar overall SR (59.8\\%--61.6\\%), but individual task performance varies substantially across configurations, with per-task differences up to 30 percentage points.}\n\\label{tab:smart_compress_pertask}\n\\begin{tabular}{lcccc}\n\\toprule\nTask & $M{=}32$ (\\%) & $M{=}64$ (\\%) & $M{=}128$ (\\%) \\\\\n\\midrule\nalphabet\\_soup & 68 & 74 & 62 \\\\\nbbq\\_sauce & 46 & 56 & 34 \\\\\nbutter & 82 & 84 & 82 \\\\\nchocolate\\_pudding & 90 & 74 & 82 \\\\\ncream\\_cheese & 64 & 38 & 58 \\\\\nketchup & 66 & 64 & 62 \\\\\nmilk & 76 & 62 & 56 \\\\\norange\\_juice & 28 & 46 & 58 \\\\\nsalad\\_dressing & 60 & 64 & 54 \\\\\ntomato\\_sauce & 36 & 54 & 50 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{61.6} & \\textbf{61.6} & \\textbf{59.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{VTR Multi-Seed Results}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR success rates across three seeds on LIBERO-Object (500 episodes each). Mean $\\pm$ std reported.}\n\\label{tab:multi_seed}\n\\begin{tabular}{lccccr}",
      "numLines": 500,
      "startLine": 1,
      "totalLines": 938
    }
  }
}
```

</details>

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Grep · `toolu_01G2dJcoGieeVAFwih35h1h1`</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "output_mode": "content",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "147fec65-df9f-42d7-8f59-08a3c54dfcb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbxtV5RAcTJ67TW5RLd1QT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50637,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 50637
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

_source line 44 · 2026-05-29T06:49:33.807Z_

<details><summary>↩ Tool result · `toolu_01G2dJcoGieeVAFwih35h1h1`</summary>

```text
91:[Omitted long matching line]
94:[Omitted long matching line]
138:[Omitted long matching line]
748:X-VLA's 12-layer BART encoder~\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\,pp), confirming it as an architectural property.
750:MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\% SR under 78\% pruning).
878:Table~\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\_last), mean attention across all decoder layers (attn\_mean), and attention rollout~\cite{abnar2020quantifying}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "48ede605-6cd1-4987-8357-412699de371c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "91:[Omitted long matching line]\n94:[Omitted long matching line]\n138:[Omitted long matching line]\n748:X-VLA's 12-layer BART encoder~\\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\\,pp), confirming it as an architectural property.\n750:MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\\% SR under 78\\% pruning).\n878:Table~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.",
    "numLines": 6
  }
}
```

</details>

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Grep · `toolu_01PVbgEd2ktqTyHb93jQNFyk`</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "head_limit": 0,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "c32d8907-ff4f-4620-a716-9874317c3989",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbxtV5RAcTJ67TW5RLd1QT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 50637,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 50637
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

_source line 46 · 2026-05-29T06:49:34.904Z_

<details><summary>↩ Tool result · `toolu_01PVbgEd2ktqTyHb93jQNFyk`</summary>

```text
&lt;persisted-output>
Output too large (19.8KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/db052317-379b-476d-9ccf-531a6abb0c10/tool-results/toolu_01PVbgEd2ktqTyHb93jQNFyk.txt

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "313a532c-aaca-41a7-ae82-8479d766e4fa",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:5:DynamicViT~\\cite{rao2021dynamicvit}, EViT~\\cite{liang2022evit}, A-ViT~\\cite{yin2022avit}, Token Merging~\\cite{bolya2023tome}, and CrossGET~\\cite{shi2024crossget} remove 50--66\\% of tokens with under 0.5\\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.\ndocs/paper/related_work.tex:8:[Omitted long matching line]\ndocs/paper/related_work.tex:11:Jabbour et al.~\\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.\ndocs/paper/related_work.tex:14:LLaVA~\\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.\ndocs/paper/experiments.tex:7:\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\ndocs/paper/experiments.tex:9:\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\ndocs/paper/appendix.tex:91:[Omitted long matching line]\ndocs/paper/appendix.tex:94:[Omitted long matching line]\ndocs/paper/appendix.tex:138:[Omitted long matching line]\ndocs/paper/appendix.tex:748:X-VLA's 12-layer BART encoder~\\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\\,pp), confirming it as an architectural property.\ndocs/paper/appendix.tex:750:MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\\% SR under 78\\% pruning).\ndocs/paper/appendix.tex:878:Table~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.\ndocs/paper/experimental_setup.tex:9:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:11:We evaluate on LIBERO~\\cite{liu2023libero} (Object: 10 tasks $\\times$ 50 episodes = 500 total; Spatial and Goal for cross-suite validation). Closed-loop success rate (SR) with Wilson 95\\% CIs is the primary metric; multi-seed results report mean $\\pm$ std. Baselines: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%.\ndocs/paper/introduction.tex:14:[Omitted long matching line]\ndocs/paper/introduction.tex:16:[Omitted long matching line]\ndocs/paper/results.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\ndocs/paper/results.tex:9:[Omitted long matching line]\ndocs/paper/results.tex:11:[Omitted long matching line]\ndocs/paper/results.tex:16:[Omitted long matching line]\ndocs/paper/results.tex:22:$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\ndocs/paper/results.tex:23:$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\ndocs/paper/results.tex:24:X-VLA~\\cite{zheng2025xvla} & Linear + BART (12L)$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.9{\\pm}0.3$ & Threshold-graded \\\\\ndocs/paper/results.tex:25:OpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\ndocs/paper/results.tex:26:OFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\ndocs/paper/results.tex:27:CogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\ndocs/paper/results.tex:28:SmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\ndocs/paper/results.tex:45:OFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\ndocs/paper/results_v2.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\ndocs/paper/results_v2.tex:9:[Omitted long matching line]\ndocs/paper/results_v2.tex:11:[Omitted long matching line]\ndocs/paper/results_v2.tex:16:[Omitted long matching line]\ndocs/paper/results_v2.tex:22:$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\ndocs/paper/results_v2.tex:23:$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\ndocs/paper/results_v2.tex:24:X-VLA~\\cite{zheng2025xvla} & Linear proj$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.8$ & Threshold-graded \\\\\ndocs/paper/results_v2.tex:25:OpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\ndocs/paper/results_v2.tex:26:OFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\ndocs/paper/results_v2.tex:27:CogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\ndocs/paper/results_v2.tex:28:SmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\ndocs/paper/results_v2.tex:45:OFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, determines token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\ndocs/paper/sections/analysis.tex:21:DynamicViT~\\cite{rao2021dynamicvit} and ToMe~\\cite{bolya2023tome} exploit this concentration: tokens that receive low attention contribute little to the classification decision and can be safely removed.\ndocs/paper/sections/analysis.tex:24:We extract attention weights from the LLM backbone (Qwen2-0.5B~\\cite{yang2024qwen2}) over all vision tokens across three LIBERO tasks.\ndocs/paper/sections/analysis.tex:31:SigLIP~\\cite{zhai2023siglip} encodes images using non-overlapping spatial patches without a \\texttt{[CLS]} aggregation token.\ndocs/paper/sections/analysis.tex:123:In ViT classification, attention concentrates on a small subset of discriminative patches~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}.\ndocs/paper/sections/analysis.tex:129:SigLIP~\\cite{zhai2023siglip} encodes each non-overlapping spatial patch as a separate token with no \\texttt{[CLS]} aggregation, so the VLA's LLM backbone must attend to all patches to reconstruct spatial relationships between the robot end-effector, target objects, and obstacles.\ndocs/paper/sections/related_work_draft.tex:6:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:8:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:12:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:14:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:20:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:22:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:24:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:28:[Omitted long matching line]\ndocs/paper/sections/experiments.tex:17:DynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/sections/experiments.tex:18:EViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/sections/experiments.tex:19:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{xu2025vlacache,cheng2026vlaiap}.\ndocs/paper/sections/experiments.tex:20:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\ndocs/paper/sections/experiments.tex:66:Token merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\ndocs/paper/sections/experiments.tex:73:\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}\ndocs/paper/sections/results_draft.tex:4:We evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\\% confidence intervals.\ndocs/paper/sections/results_draft.tex:9:[Omitted long matching line]\ndocs/paper/sections/results_draft.tex:12:[Omitted long matching line]\ndocs/paper/sections/results_draft.tex:59:OpenVLA~\\cite{kim2024openvla} uses a two-layer MLP projector to map vision encoder outputs (from DINOv2 and SigLIP~\\cite{zhai2023siglip}) into the Llama-2 language model's embedding space. Unlike pixel-shuffle, the MLP projector processes each patch token independently through a shared linear transformation. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence.\ndocs/paper/sections/background.tex:6:This section describes the two components of our experimental setup: the SmolVLA architecture~\\cite{shukor2025smolvla}, in which we study vision token reduction, and the LIBERO benchmark~\\cite{liu2023libero}, on which we evaluate closed-loop performance.\ndocs/paper/sections/background.tex:12:SmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a modality connector, a language model backbone, and an action head.\ndocs/paper/sections/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\ndocs/paper/sections/background.tex:41:The Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\ndocs/paper/sections/background.tex:47:SmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\ndocs/paper/sections/background.tex:54:This architecture shares its high-level structure with larger VLA systems such as OpenVLA~\\cite{kim2024openvla} and $\\pi_0$~\\cite{black2024pi0}, making SmolVLA a representative testbed for studying vision token efficiency in VLA policies.\ndocs/paper/sections/background.tex:59:We evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\ndocs/paper/sections/experimental_setup.tex:33:  \\item \\textbf{Token merge}: following the bipartite matching strategy of ToMe~\\cite{bolya2023tome}, each pruned token is merged with its nearest retained neighbor by averaging their embeddings. Sequence length and total information content are both preserved.\ndocs/paper/sections/introduction.tex:7:DynamicViT~\\cite{rao2021dynamicvit} removes 66\\% of patch tokens with less than 0.5\\% accuracy loss on ImageNet classification.\ndocs/paper/sections/introduction.tex:8:Token Merging (ToMe)~\\cite{bolya2023tome} merges 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/sections/introduction.tex:9:EViT~\\cite{liang2022evit} discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/sections/introduction.tex:12:Vision-Language-Action (VLA) models~\\cite{brohan2023rt2,kim2024openvla,black2024pi0,shukor2025smolvla} use the same ViT encoders as their visual front-ends, producing hundreds of patch tokens that dominate the input sequence to the language model backbone.\ndocs/paper/sections/introduction.tex:17:Current VLA models such as RT-2~\\cite{brohan2023rt2} and $\\pi_0$~\\cite{black2024pi0} use large vision encoders that produce 256 or more tokens per image.\ndocs/paper/sections/introduction.tex:20:SmolVLA~\\cite{shukor2025smolvla}, a compact 451.5M-parameter VLA, produces 256 vision tokens from two cameras (128 per view), and these tokens constitute the majority of the LLM backbone's input sequence.\ndocs/paper/sections/introduction.tex:23:FastV~\\cite{chen2024fastv} identifies and prunes inattentive visual tokens in VLM inference, achieving 2$\\times$ speedup with minimal quality loss on VLM benchmarks.\ndocs/paper/sections/introduction.tex:24:VLA-Cache~\\cite{xu2025vlacache} caches vision tokens across timesteps to reduce redundant computation in temporal sequences.\ndocs/paper/sections/introduction.tex:25:VLA-IAP~\\cite{cheng2026vlaiap} proposes importance-aware pruning for VLA inference acceleration.\ndocs/paper/sections/introduction.tex:30:Existing evaluations of VLM token reduction rely on offline metrics such as action loss, perplexity, or next-token prediction accuracy~\\cite{chen2024fastv,cheng2026vlaiap}.\ndocs/paper/sections/introduction.tex:38:Using SmolVLA on the LIBERO benchmark~\\cite{liu2023libero}, we test six pruning configurations spanning three axes: scoring function (a trained Attention-Conditioned Importance Scorer versus random selection), retention ratio ($k \\in \\{0.5, 0.7, 0.9\\}$), and mechanism (zero-masking, true removal, and token merging).\ndocs/paper/sections/introduction.tex:50:This uniformity arises because SigLIP~\\cite{zhai2023siglip} encodes non-overlapping spatial patches without a \\texttt{[CLS]} aggregation token; each token carries unique, irreplaceable spatial information about the scene.\ndocs/paper/sections/introduction.tex:59:We believe this negative result~\\cite{karl2024negative,zeng2023transformers_tsf} carries important implications for the VLA efficiency community: future work on VLA compression should seek alternatives to naive token removal, such as training-time distillation into fewer tokens or architectural modifications that build in spatial redundancy.\ndocs/paper/method.tex:7:[Omitted long matching line]\ndocs/paper/background.tex:6:This section describes the architectures and benchmark used in our study: SmolVLA~\\cite{shukor2025smolvla} and OpenVLA~\\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\\cite{liu2023libero} on which we evaluate closed-loop performance.\ndocs/paper/background.tex:12:SmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 450M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.\ndocs/paper/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\ndocs/paper/background.tex:36:The Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\ndocs/paper/background.tex:41:SmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\ndocs/paper/background.tex:49:OpenVLA~\\cite{kim2024openvla} is a 7B-parameter VLA built on the Llama-2 backbone. Its vision pipeline differs from SmolVLA in two respects that are directly relevant to compressibility.\ndocs/paper/background.tex:52:OpenVLA uses a dual encoder combining DINOv2~\\cite{oquab2023dinov2} and SigLIP~\\cite{zhai2023siglip}. The two encoders produce complementary representations (self-supervised spatial features and language-aligned features) that are concatenated per patch position.\ndocs/paper/background.tex:63:We evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\ndocs/paper/experiments_deprecated.tex:6:DynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/experiments_deprecated.tex:7:EViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/experiments_deprecated.tex:8:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{xu2025vlacache,cheng2026vlaiap}.\ndocs/paper/experiments_deprecated.tex:9:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\ndocs/paper/experiments_deprecated.tex:55:Token merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\ndocs/paper/experiments_deprecated.tex:62:\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}",
    "numLines": 99
  }
}
```

</details>

---


### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Let me read the full grep output to get all citations used across the paper, and also read more of the appendix to find additional citations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "161bc63d-1fdf-4468-9e56-af255e214759",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDqY95p6rE1wczGTksUxwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17242,
      "cache_read_input_tokens": 62482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17242
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

_source line 48_

Let me read the full grep output and remaining appendix citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "bb8f37be-9856-4eae-8acf-f7d722a6ea27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDqY95p6rE1wczGTksUxwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17242,
      "cache_read_input_tokens": 62482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17242
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01DH77RWnPqK8X4Fwft5Ujbj`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/db052317-379b-476d-9ccf-531a6abb0c10/tool-results/toolu_01PVbgEd2ktqTyHb93jQNFyk.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "04523806-c455-4cdd-8dbb-27005988d43a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDqY95p6rE1wczGTksUxwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17242,
      "cache_read_input_tokens": 62482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17242
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

_source line 50 · 2026-05-29T06:49:39.511Z_

<details><summary>↩ Tool result · `toolu_01DH77RWnPqK8X4Fwft5Ujbj`</summary>

```text
1	docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, Token Merging~\cite{bolya2023tome}, and CrossGET~\cite{shi2024crossget} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
2	docs/paper/related_work.tex:8:[Omitted long matching line]
3	docs/paper/related_work.tex:11:Jabbour et al.~\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.
4	docs/paper/related_work.tex:14:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.
5	docs/paper/experiments.tex:7:\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).
6	docs/paper/experiments.tex:9:\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\ref{tab:model_properties}): $\pi_{0.5}$~\cite{black2025pi05}, X-VLA~\cite{zheng2025xvla}, OpenVLA~\cite{kim2024openvla}, and SmolVLA~\cite{shukor2025smolvla}. Two additional models ($\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.
7	docs/paper/appendix.tex:91:[Omitted long matching line]
8	docs/paper/appendix.tex:94:[Omitted long matching line]
9	docs/paper/appendix.tex:138:[Omitted long matching line]
10	docs/paper/appendix.tex:748:X-VLA's 12-layer BART encoder~\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\,pp), confirming it as an architectural property.
11	docs/paper/appendix.tex:750:MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\% SR under 78\% pruning).
12	docs/paper/appendix.tex:878:Table~\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\_last), mean attention across all decoder layers (attn\_mean), and attention rollout~\cite{abnar2020quantifying}.
13	docs/paper/experimental_setup.tex:9:[Omitted long matching line]
14	docs/paper/experimental_setup.tex:11:We evaluate on LIBERO~\cite{liu2023libero} (Object: 10 tasks $\times$ 50 episodes = 500 total; Spatial and Goal for cross-suite validation). Closed-loop success rate (SR) with Wilson 95\% CIs is the primary metric; multi-seed results report mean $\pm$ std. Baselines: SmolVLA 44.8\%, OpenVLA 74.0\%, X-VLA 99.2\%, $\pi_0.5$ 98.2\%.
15	docs/paper/introduction.tex:14:[Omitted long matching line]
16	docs/paper/introduction.tex:16:[Omitted long matching line]
17	docs/paper/results.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
18	docs/paper/results.tex:9:[Omitted long matching line]
19	docs/paper/results.tex:11:[Omitted long matching line]
20	docs/paper/results.tex:16:[Omitted long matching line]
21	docs/paper/results.tex:22:$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
22	docs/paper/results.tex:23:$\pi_0.5$~\cite{black2025pi05} & Linear proj ($\times\!\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\%, R$=$69.4\% ($\Delta{=}$+36pp) & Uniformly critical \\
23	docs/paper/results.tex:24:X-VLA~\cite{zheng2025xvla} & Linear + BART (12L)$^\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\pm}0.4$, $k{=}0.85$: $67.9{\pm}0.3$ & Threshold-graded \\
24	docs/paper/results.tex:25:OpenVLA~\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\% SR ($-$49\%) & Smooth graded \\
25	docs/paper/results.tex:26:OFT~\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \approx 0.215$; Ent.\ $0.667 \approx 0.661$$^\S$ & Smooth graded \\
26	docs/paper/results.tex:27:CogACT~\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\% SR under 78\% prune$^\|$ & Smooth graded \\
27	docs/paper/results.tex:28:SmolVLA~\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\% SR & Catastrophic cliff \\
28	docs/paper/results.tex:45:OFT~\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\cite{li2024cogact} (MLP projector) retains 74.2\% SR under 78\% pruning.
29	docs/paper/results_v2.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
30	docs/paper/results_v2.tex:9:[Omitted long matching line]
31	docs/paper/results_v2.tex:11:[Omitted long matching line]
32	docs/paper/results_v2.tex:16:[Omitted long matching line]
33	docs/paper/results_v2.tex:22:$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
34	docs/paper/results_v2.tex:23:$\pi_0.5$~\cite{black2025pi05} & Linear proj ($\times\!\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\%, R$=$69.4\% ($\Delta{=}$+36pp) & Uniformly critical \\
35	docs/paper/results_v2.tex:24:X-VLA~\cite{zheng2025xvla} & Linear proj$^\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\pm}0.4$, $k{=}0.85$: $67.8$ & Threshold-graded \\
36	docs/paper/results_v2.tex:25:OpenVLA~\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\% SR ($-$49\%) & Smooth graded \\
37	docs/paper/results_v2.tex:26:OFT~\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \approx 0.215$; Ent.\ $0.667 \approx 0.661$$^\S$ & Smooth graded \\
38	docs/paper/results_v2.tex:27:CogACT~\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\% SR under 78\% prune$^\|$ & Smooth graded \\
39	docs/paper/results_v2.tex:28:SmolVLA~\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\% SR & Catastrophic cliff \\
40	docs/paper/results_v2.tex:45:OFT~\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, determines token importance structure. EfficientVLA~\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\cite{li2024cogact} (MLP projector) retains 74.2\% SR under 78\% pruning.
41	docs/paper/sections/analysis.tex:21:DynamicViT~\cite{rao2021dynamicvit} and ToMe~\cite{bolya2023tome} exploit this concentration: tokens that receive low attention contribute little to the classification decision and can be safely removed.
42	docs/paper/sections/analysis.tex:24:We extract attention weights from the LLM backbone (Qwen2-0.5B~\cite{yang2024qwen2}) over all vision tokens across three LIBERO tasks.
43	docs/paper/sections/analysis.tex:31:SigLIP~\cite{zhai2023siglip} encodes images using non-overlapping spatial patches without a \texttt{[CLS]} aggregation token.
44	docs/paper/sections/analysis.tex:123:In ViT classification, attention concentrates on a small subset of discriminative patches~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}.
45	docs/paper/sections/analysis.tex:129:SigLIP~\cite{zhai2023siglip} encodes each non-overlapping spatial patch as a separate token with no \texttt{[CLS]} aggregation, so the VLA's LLM backbone must attend to all patches to reconstruct spatial relationships between the robot end-effector, target objects, and obstacles.
46	docs/paper/sections/related_work_draft.tex:6:[Omitted long matching line]
47	docs/paper/sections/related_work_draft.tex:8:[Omitted long matching line]
48	docs/paper/sections/related_work_draft.tex:12:[Omitted long matching line]
49	docs/paper/sections/related_work_draft.tex:14:[Omitted long matching line]
50	docs/paper/sections/related_work_draft.tex:20:[Omitted long matching line]
51	docs/paper/sections/related_work_draft.tex:22:[Omitted long matching line]
52	docs/paper/sections/related_work_draft.tex:24:[Omitted long matching line]
53	docs/paper/sections/related_work_draft.tex:28:[Omitted long matching line]
54	docs/paper/sections/experiments.tex:17:DynamicViT~\cite{rao2021dynamicvit} removes 30\%--50\% of tokens with less than 0.5\% accuracy loss on ImageNet, and Token Merging (ToMe)~\cite{bolya2023tome} merges up to 40\% of tokens while retaining over 99\% of classification accuracy.
55	docs/paper/sections/experiments.tex:18:EViT~\cite{liang2022evit} similarly discards 50\% of inattentive tokens with negligible degradation.
56	docs/paper/sections/experiments.tex:19:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\cite{xu2025vlacache,cheng2026vlaiap}.
57	docs/paper/sections/experiments.tex:20:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\cite{liu2023libero}.
58	docs/paper/sections/experiments.tex:66:Token merging (following ToMe~\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.
59	docs/paper/sections/experiments.tex:73:\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\% accuracy on classification benchmarks even at aggressive retention ratios~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}
60	docs/paper/sections/results_draft.tex:4:We evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\% confidence intervals.
61	docs/paper/sections/results_draft.tex:9:[Omitted long matching line]
62	docs/paper/sections/results_draft.tex:12:[Omitted long matching line]
63	docs/paper/sections/results_draft.tex:59:OpenVLA~\cite{kim2024openvla} uses a two-layer MLP projector to map vision encoder outputs (from DINOv2 and SigLIP~\cite{zhai2023siglip}) into the Llama-2 language model's embedding space. Unlike pixel-shuffle, the MLP projector processes each patch token independently through a shared linear transformation. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence.
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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "60c91a0e-5f2b-4604-9a27-fb8e487f61d7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/db052317-379b-476d-9ccf-531a6abb0c10/tool-results/toolu_01PVbgEd2ktqTyHb93jQNFyk.txt",
      "content": "docs/paper/related_work.tex:5:DynamicViT~\\cite{rao2021dynamicvit}, EViT~\\cite{liang2022evit}, A-ViT~\\cite{yin2022avit}, Token Merging~\\cite{bolya2023tome}, and CrossGET~\\cite{shi2024crossget} remove 50--66\\% of tokens with under 0.5\\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.\ndocs/paper/related_work.tex:8:[Omitted long matching line]\ndocs/paper/related_work.tex:11:Jabbour et al.~\\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.\ndocs/paper/related_work.tex:14:LLaVA~\\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.\ndocs/paper/experiments.tex:7:\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\ndocs/paper/experiments.tex:9:\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\ndocs/paper/appendix.tex:91:[Omitted long matching line]\ndocs/paper/appendix.tex:94:[Omitted long matching line]\ndocs/paper/appendix.tex:138:[Omitted long matching line]\ndocs/paper/appendix.tex:748:X-VLA's 12-layer BART encoder~\\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\\,pp), confirming it as an architectural property.\ndocs/paper/appendix.tex:750:MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\\% SR under 78\\% pruning).\ndocs/paper/appendix.tex:878:Table~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.\ndocs/paper/experimental_setup.tex:9:[Omitted long matching line]\ndocs/paper/experimental_setup.tex:11:We evaluate on LIBERO~\\cite{liu2023libero} (Object: 10 tasks $\\times$ 50 episodes = 500 total; Spatial and Goal for cross-suite validation). Closed-loop success rate (SR) with Wilson 95\\% CIs is the primary metric; multi-seed results report mean $\\pm$ std. Baselines: SmolVLA 44.8\\%, OpenVLA 74.0\\%, X-VLA 99.2\\%, $\\pi_0.5$ 98.2\\%.\ndocs/paper/introduction.tex:14:[Omitted long matching line]\ndocs/paper/introduction.tex:16:[Omitted long matching line]\ndocs/paper/results.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\ndocs/paper/results.tex:9:[Omitted long matching line]\ndocs/paper/results.tex:11:[Omitted long matching line]\ndocs/paper/results.tex:16:[Omitted long matching line]\ndocs/paper/results.tex:22:$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\ndocs/paper/results.tex:23:$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\ndocs/paper/results.tex:24:X-VLA~\\cite{zheng2025xvla} & Linear + BART (12L)$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.9{\\pm}0.3$ & Threshold-graded \\\\\ndocs/paper/results.tex:25:OpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\ndocs/paper/results.tex:26:OFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\ndocs/paper/results.tex:27:CogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\ndocs/paper/results.tex:28:SmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\ndocs/paper/results.tex:45:OFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\ndocs/paper/results_v2.tex:4:We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\ndocs/paper/results_v2.tex:9:[Omitted long matching line]\ndocs/paper/results_v2.tex:11:[Omitted long matching line]\ndocs/paper/results_v2.tex:16:[Omitted long matching line]\ndocs/paper/results_v2.tex:22:$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\ndocs/paper/results_v2.tex:23:$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\ndocs/paper/results_v2.tex:24:X-VLA~\\cite{zheng2025xvla} & Linear proj$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.8$ & Threshold-graded \\\\\ndocs/paper/results_v2.tex:25:OpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\ndocs/paper/results_v2.tex:26:OFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\ndocs/paper/results_v2.tex:27:CogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\ndocs/paper/results_v2.tex:28:SmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\ndocs/paper/results_v2.tex:45:OFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, determines token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\ndocs/paper/sections/analysis.tex:21:DynamicViT~\\cite{rao2021dynamicvit} and ToMe~\\cite{bolya2023tome} exploit this concentration: tokens that receive low attention contribute little to the classification decision and can be safely removed.\ndocs/paper/sections/analysis.tex:24:We extract attention weights from the LLM backbone (Qwen2-0.5B~\\cite{yang2024qwen2}) over all vision tokens across three LIBERO tasks.\ndocs/paper/sections/analysis.tex:31:SigLIP~\\cite{zhai2023siglip} encodes images using non-overlapping spatial patches without a \\texttt{[CLS]} aggregation token.\ndocs/paper/sections/analysis.tex:123:In ViT classification, attention concentrates on a small subset of discriminative patches~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}.\ndocs/paper/sections/analysis.tex:129:SigLIP~\\cite{zhai2023siglip} encodes each non-overlapping spatial patch as a separate token with no \\texttt{[CLS]} aggregation, so the VLA's LLM backbone must attend to all patches to reconstruct spatial relationships between the robot end-effector, target objects, and obstacles.\ndocs/paper/sections/related_work_draft.tex:6:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:8:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:12:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:14:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:20:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:22:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:24:[Omitted long matching line]\ndocs/paper/sections/related_work_draft.tex:28:[Omitted long matching line]\ndocs/paper/sections/experiments.tex:17:DynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/sections/experiments.tex:18:EViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/sections/experiments.tex:19:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{xu2025vlacache,cheng2026vlaiap}.\ndocs/paper/sections/experiments.tex:20:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\ndocs/paper/sections/experiments.tex:66:Token merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\ndocs/paper/sections/experiments.tex:73:\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}\ndocs/paper/sections/results_draft.tex:4:We evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\\% confidence intervals.\ndocs/paper/sections/results_draft.tex:9:[Omitted long matching line]\ndocs/paper/sections/results_draft.tex:12:[Omitted long matching line]\ndocs/paper/sections/results_draft.tex:59:OpenVLA~\\cite{kim2024openvla} uses a two-layer MLP projector to map vision encoder outputs (from DINOv2 and SigLIP~\\cite{zhai2023siglip}) into the Llama-2 language model's embedding space. Unlike pixel-shuffle, the MLP projector processes each patch token independently through a shared linear transformation. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence.\ndocs/paper/sections/background.tex:6:This section describes the two components of our experimental setup: the SmolVLA architecture~\\cite{shukor2025smolvla}, in which we study vision token reduction, and the LIBERO benchmark~\\cite{liu2023libero}, on which we evaluate closed-loop performance.\ndocs/paper/sections/background.tex:12:SmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a modality connector, a language model backbone, and an action head.\ndocs/paper/sections/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\ndocs/paper/sections/background.tex:41:The Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\ndocs/paper/sections/background.tex:47:SmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\ndocs/paper/sections/background.tex:54:This architecture shares its high-level structure with larger VLA systems such as OpenVLA~\\cite{kim2024openvla} and $\\pi_0$~\\cite{black2024pi0}, making SmolVLA a representative testbed for studying vision token efficiency in VLA policies.\ndocs/paper/sections/background.tex:59:We evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\ndocs/paper/sections/experimental_setup.tex:33:  \\item \\textbf{Token merge}: following the bipartite matching strategy of ToMe~\\cite{bolya2023tome}, each pruned token is merged with its nearest retained neighbor by averaging their embeddings. Sequence length and total information content are both preserved.\ndocs/paper/sections/introduction.tex:7:DynamicViT~\\cite{rao2021dynamicvit} removes 66\\% of patch tokens with less than 0.5\\% accuracy loss on ImageNet classification.\ndocs/paper/sections/introduction.tex:8:Token Merging (ToMe)~\\cite{bolya2023tome} merges 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/sections/introduction.tex:9:EViT~\\cite{liang2022evit} discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/sections/introduction.tex:12:Vision-Language-Action (VLA) models~\\cite{brohan2023rt2,kim2024openvla,black2024pi0,shukor2025smolvla} use the same ViT encoders as their visual front-ends, producing hundreds of patch tokens that dominate the input sequence to the language model backbone.\ndocs/paper/sections/introduction.tex:17:Current VLA models such as RT-2~\\cite{brohan2023rt2} and $\\pi_0$~\\cite{black2024pi0} use large vision encoders that produce 256 or more tokens per image.\ndocs/paper/sections/introduction.tex:20:SmolVLA~\\cite{shukor2025smolvla}, a compact 451.5M-parameter VLA, produces 256 vision tokens from two cameras (128 per view), and these tokens constitute the majority of the LLM backbone's input sequence.\ndocs/paper/sections/introduction.tex:23:FastV~\\cite{chen2024fastv} identifies and prunes inattentive visual tokens in VLM inference, achieving 2$\\times$ speedup with minimal quality loss on VLM benchmarks.\ndocs/paper/sections/introduction.tex:24:VLA-Cache~\\cite{xu2025vlacache} caches vision tokens across timesteps to reduce redundant computation in temporal sequences.\ndocs/paper/sections/introduction.tex:25:VLA-IAP~\\cite{cheng2026vlaiap} proposes importance-aware pruning for VLA inference acceleration.\ndocs/paper/sections/introduction.tex:30:Existing evaluations of VLM token reduction rely on offline metrics such as action loss, perplexity, or next-token prediction accuracy~\\cite{chen2024fastv,cheng2026vlaiap}.\ndocs/paper/sections/introduction.tex:38:Using SmolVLA on the LIBERO benchmark~\\cite{liu2023libero}, we test six pruning configurations spanning three axes: scoring function (a trained Attention-Conditioned Importance Scorer versus random selection), retention ratio ($k \\in \\{0.5, 0.7, 0.9\\}$), and mechanism (zero-masking, true removal, and token merging).\ndocs/paper/sections/introduction.tex:50:This uniformity arises because SigLIP~\\cite{zhai2023siglip} encodes non-overlapping spatial patches without a \\texttt{[CLS]} aggregation token; each token carries unique, irreplaceable spatial information about the scene.\ndocs/paper/sections/introduction.tex:59:We believe this negative result~\\cite{karl2024negative,zeng2023transformers_tsf} carries important implications for the VLA efficiency community: future work on VLA compression should seek alternatives to naive token removal, such as training-time distillation into fewer tokens or architectural modifications that build in spatial redundancy.\ndocs/paper/method.tex:7:[Omitted long matching line]\ndocs/paper/background.tex:6:This section describes the architectures and benchmark used in our study: SmolVLA~\\cite{shukor2025smolvla} and OpenVLA~\\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\\cite{liu2023libero} on which we evaluate closed-loop performance.\ndocs/paper/background.tex:12:SmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 450M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.\ndocs/paper/background.tex:23:SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\ndocs/paper/background.tex:36:The Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\ndocs/paper/background.tex:41:SmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\ndocs/paper/background.tex:49:OpenVLA~\\cite{kim2024openvla} is a 7B-parameter VLA built on the Llama-2 backbone. Its vision pipeline differs from SmolVLA in two respects that are directly relevant to compressibility.\ndocs/paper/background.tex:52:OpenVLA uses a dual encoder combining DINOv2~\\cite{oquab2023dinov2} and SigLIP~\\cite{zhai2023siglip}. The two encoders produce complementary representations (self-supervised spatial features and language-aligned features) that are concatenated per patch position.\ndocs/paper/background.tex:63:We evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\ndocs/paper/experiments_deprecated.tex:6:DynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\ndocs/paper/experiments_deprecated.tex:7:EViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\ndocs/paper/experiments_deprecated.tex:8:These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{xu2025vlacache,cheng2026vlaiap}.\ndocs/paper/experiments_deprecated.tex:9:Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\ndocs/paper/experiments_deprecated.tex:55:Token merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\ndocs/paper/experiments_deprecated.tex:62:\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}",
      "numLines": 99,
      "startLine": 1,
      "totalLines": 99
    }
  }
}
```

</details>

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01MiHf5ngyw23HeuBCmfP7T4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "963a883f-fa0e-41a2-94b7-e08bc49803a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDqY95p6rE1wczGTksUxwk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17242,
      "cache_read_input_tokens": 62482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17242
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

_source line 52 · 2026-05-29T06:49:40.361Z_

<details><summary>↩ Tool result · `toolu_01MiHf5ngyw23HeuBCmfP7T4`</summary>

```text
500	\begin{tabular}{lccccr}
501	\toprule
502	$M$ & Seed 42 & Seed 43 & Seed 44 & Mean $\pm$ Std \\
503	\midrule
504	32 & 61.6 & 59.2 & 59.6 & 60.1 $\pm$ 1.3 \\
505	64 & 61.6 & 60.0 & 64.4 & 62.0 $\pm$ 2.2 \\
506	96 & 52.6 & 58.2 & 52.8 & 54.5 $\pm$ 3.2 \\
507	128 & 59.8 & 54.0 & 60.2 & 58.0 $\pm$ 3.5 \\
508	\bottomrule
509	\end{tabular}
510	\end{table}
511	
512	
513	\section{VTR Full Results}
514	\label{app:vtr_full}
515	
516	\begin{table}[ht]
517	\centering
518	\small
519	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\% compression) matches $M{=}128$ (passthrough) within 1.1\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}
520	\label{tab:vtr_results}
521	\begin{tabular}{lccr}
522	\toprule
523	Configuration & $M$ & Compression & SR (\%) \\
524	\midrule
525	\textit{SmolVLA-Base (LoRA)} & 128 & 0\% & 44.8 \\
526	\textit{SmolVLA official} & 128 & 0\% & 59.2 \\
527	\textit{Baseline control (+100K steps)} & 128 & 0\% & 45.0 \\
528	\textit{Hard pruning (any $k$)} & -- & 5--50\% & 0.0 \\
529	\midrule
530	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
531	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
532	Cross-attn VTR & 64 & 50\% & \textbf{62.0 $\pm$ 2.2} \\
533	Cross-attn VTR & 96 & 25\% & 54.5 $\pm$ 3.2 \\
534	Cross-attn VTR & 128 & 0\% & 58.0 $\pm$ 3.5 \\
535	\midrule
536	MLP adapter ($\sim$22M) & 32 & 75\% & 63.4 $\pm$ 2.6 \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	
542	\section{Full VTR Ablation}
543	\label{app:smart_compress_full}
544	
545	Table~\ref{tab:smart_compress_full} reports all five VTR configurations. The cross-attention module improves performance regardless of compression: $M \in \{32, 64, 128\}$ all achieve $\sim$60\% SR, exceeding the 44.8\% baseline by 15--17 points ($p < 0.001$, two-proportion $z$-test). Only at $M = 16$ (87.5\% compression) does performance decline modestly to 55.8\%, still 11 points above baseline. The $M{=}96$ dip (mean 54.5\% across three seeds, Table~\ref{tab:multi_seed}) may reflect an intermediate bottleneck that introduces representational redundancy without the regularization benefit of stronger compression ($M{=}32$, $M{=}64$).
546	
547	Table~\ref{tab:cross_suite} reports performance across task suites. All suites are in-distribution: the training set (HuggingFaceVLA/libero) covers Object, Spatial, Goal, and Long. On LIBERO-Spatial, VTR achieves 53.2\% SR (vs.\ 0\% under hard pruning); on LIBERO-Goal, 56.4\% SR ($-6.6$pp from the 63.0\% unpruned baseline, vs.\ 0\% under pruning). The LIBERO-Goal decline indicates that re-encoding benefits vary across task structures even within the training distribution. Per-task results are in Table~\ref{tab:smart_compress_pertask}.
548	
549	\begin{table}[ht]
550	\centering
551	\small
552	\caption{Full VTR ablation on LIBERO-Object across five compression levels. $M{=}32$ and $M{=}64$ achieve similar SR ($\sim$60\%); $M{=}96$ shows a modest dip; the $M{=}128$ passthrough confirms the gain originates from re-encoding.}
553	\label{tab:smart_compress_full}
554	\begin{tabular}{lcccrr}
555	\toprule
556	Method & $M$ & Reduction & SR (\%) & Episodes & Wilson 95\% CI \\
557	\midrule
558	\textit{Baseline} & 128 & 0\% & 44.8 & 500 & [40.5, 49.2] \\
559	\textit{Extended training} & -- & -- & 45.0 & 500 & [40.7, 49.3] \\
560	\textit{Hard pruning} & -- & 50--90\% & 0.0 & 500+ & [0, 0.76] \\
561	\midrule
562	VTR & 128 & 0\% & 58.0 & 1500 & $\pm$3.5 \\
563	VTR & 96 & 25\% & 52.6 & 500 & [48.2, 56.9] \\
564	VTR & 64 & 50\% & 61.6 & 500 & [57.3, 65.8] \\
565	VTR & 32 & 75\% & 61.6 & 500 & [57.3, 65.8] \\
566	VTR & 16 & 87.5\% & 55.8 & 500 & [51.4, 60.1] \\
567	\bottomrule
568	\end{tabular}
569	
570	\vspace{2pt}
571	{\footnotesize $M{=}128$ reports mean $\pm$ std over 3 seeds (500 episodes each). Other VTR rows report single seed (seed 42) with Wilson 95\% CI. See Table~\ref{tab:multi_seed} for full multi-seed results.}
572	\end{table}
573	
574	
575	\section{VTR Evaluation Across Task Suites}
576	\label{app:cross_suite}
577	
578	Table~\ref{tab:cross_suite} reports the performance of VTR ($M{=}32$) across three LIBERO suites. All suites are in-distribution: the training set (HuggingFaceVLA/libero) covers Object, Spatial, Goal, and Long (40 tasks, 1693 episodes total). On LIBERO-Goal, performance drops from 63.0\% to 56.4\% ($-6.6$pp). On LIBERO-Spatial, VTR achieves 53.2\% SR, where the official SmolVLA checkpoint scores 44.6\% and hard pruning yields near-zero (0.6\%). While 53.2\% nominally exceeds the official Spatial baseline, this difference concentrates in two of ten tasks (+44pp and +48pp respectively); the remaining eight tasks show a net difference of only +0.2pp. We therefore do not treat the Spatial comparison as evidence that re-encoding improves over the uncompressed official baseline. The qualitative pattern (cliff-edge vulnerability and re-encoding recovery) extends across the three tested task structures within the training distribution. The LIBERO-Goal decline indicates that re-encoding benefits vary across task structures.
579	
580	\begin{table}[ht]
581	\centering
582	\small
583	\caption{VTR ($M{=}32$) evaluation across LIBERO task suites. All suites are in-distribution (training covers Object, Spatial, Goal, Long). Hard pruning (any method, $k{=}0.50$) produces 0\% or near-zero on all suites.}
584	\label{tab:cross_suite}
585	\begin{tabular}{lccc}
586	\toprule
587	Suite & Baseline (unpruned) & VTR $M{=}32$ & Hard Pruning $k{=}0.50$ \\
588	\midrule
589	Object & 44.8\% & 61.6\% & 0\% \\
590	Spatial & 51.8\% & 53.2\% & 0.6\% \\
591	Goal & 63.0\% & 56.4\% & 0\% \\
592	\bottomrule
593	\end{tabular}
594	\end{table}
595	
596	
597	\section{VTR Training Details}
598	\label{app:smart_compress_details}
599	
600	The VTR module is a cross-attention pooling layer inserted between SmolVLA's pixel-shuffle vision connector and the SmolLM2 language backbone. It consists of $M$ learned query vectors that attend over the 128 vision tokens through standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compressor adds 22.2M trainable parameters (approximately 5\% of SmolVLA's 450M total). Training is end-to-end: compressor and VLA policy parameters are jointly optimized.
601	
602	\begin{table}[ht]
603	\centering
604	\small
605	\caption{VTR training hyperparameters. All configurations ($M \in \{16, 32, 64, 96, 128\}$) use identical procedures; only the number of query vectors differs.}
606	\label{tab:training_hyperparams}
607	\begin{tabular}{ll}
608	\toprule
609	Hyperparameter & Value \\
610	\midrule
611	\multicolumn{2}{l}{\textit{Model}} \\
612	\quad Base checkpoint & SmolVLA-Base (pretrained, before LIBERO fine-tuning) \\
613	\quad Compressor architecture & Cross-attention, 2 layers, 12 heads, dropout 0.1 \\
614	\quad Compressor parameters & 22.2M \\
615	\quad Total trainable parameters & 122.1M / 472.2M (25.85\%) \\
616	\midrule
617	\multicolumn{2}{l}{\textit{Optimization}} \\
618	\quad Optimizer & AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.95$, weight decay $10^{-10}$) \\
619	\quad Learning rate & $10^{-4}$ \\
620	\quad Schedule & Linear warmup (1K steps, start factor 0.01) $\to$ cosine \\
621	\quad & annealing ($\eta_{\min}{=}2.5 \times 10^{-6}$) \\
622	\quad Max gradient norm & 10.0 \\
623	\quad Total training steps & 100,000 \\
624	\midrule
625	\multicolumn{2}{l}{\textit{Data \& batching}} \\
626	\quad Dataset & HuggingFaceVLA/libero (40 tasks, 1693 episodes across \\
627	\quad & Object, Spatial, Goal, Long suites) \\
628	\quad Batch size & 4 (no gradient accumulation)$^\dagger$ \\
629	\quad Num workers & 4 \\
630	\quad Eval interval & every 5K steps \\
631	\quad Checkpoint interval & every 1K steps \\
632	\midrule
633	\multicolumn{2}{l}{\textit{Hardware \& runtime}} \\
634	\quad Hardware & 1$\times$ NVIDIA RTX 4090 D (24GB) \\
635	\quad Precision & fp32 (no mixed precision) \\
636	\quad Wall clock & $\sim$6h 43m per configuration \\
637	\quad Training speed & 4.1 samples/sec \\
638	\quad Seed & 42 (seeds 43, 44 for multi-seed runs) \\
639	\midrule
640	\multicolumn{2}{l}{\textit{$M=32$ final metrics}} \\
641	\quad Train action loss & 0.11 \\
642	\quad Eval action loss & 0.052 \\
643	\midrule
644	\multicolumn{2}{l}{\textit{$M=64$ final metrics}} \\
645	\quad Train action loss & 0.045 \\
646	\quad Eval action loss & 0.062 \\
647	\bottomrule
648	\end{tabular}
649	
650	\vspace{2pt}
651	{\footnotesize $^\dagger$The official SmolVLA checkpoint uses batch size 64 across 8 GPUs (effective batch size 512). Our batch size 4 on a single GPU contributes to the lower baseline SR (44.8\% vs.\ 87.3\%). All VTR configurations and the extended training control use this same batch size for fair comparison.}
652	\end{table}
653	
654	The loss profile differs between configurations: $M=32$ has higher train loss (0.11 vs.\ 0.045) but lower eval loss (0.052 vs.\ 0.062), consistent with the smaller bottleneck acting as a stronger regularizer. Despite this loss difference, both achieve identical closed-loop success rates (61.6\%), reinforcing the finding that offline loss does not predict closed-loop performance (Section~\ref{sec:metric_disconnect}).
655	
656	\subsection{MLP Adapter Control}
657	\label{app:mlp_adapter}
658	
659	To verify that re-encoding effectiveness is not specific to cross-attention, we train a parameter-matched MLP adapter as a control. The adapter is a 3-layer feed-forward network with expansion ratio 4 (hidden dimension $4 \times d_{\text{model}}$), using average pooling for token reduction from 128 to $M$ tokens. Total parameters: 22.14M, matched to the cross-attention module's 22.2M. Training follows the identical protocol as VTR: SmolVLA-Base checkpoint, 100K steps, learning rate $10^{-4}$, batch size 4, same LIBERO dataset. At $M = 32$ (75\% reduction), the MLP adapter achieves $63.4 \pm 2.6$\% SR over 3 seeds, statistically indistinguishable from the cross-attention result ($60.1 \pm 1.3$\%; two-sample $t$-test, $p = 0.15$). This confirms that the re-encoding benefit does not depend on the specific module architecture.
660	
661	
662	\section{Offline Single-Step Action Error Analysis}
663	\label{app:offline_error}
664	
665	Table~\ref{tab:offline_action_error} reports the single-step action prediction error under pruning, computed over 200 evaluation frames from LIBERO-Object. The unpruned model (bypass mode) produces actions with an L2 distance of 0.414 from ground truth; under ACIS pruning at $k{=}0.50$, this increases to 1.391 ($3.4\times$). The per-dimension breakdown of the pruned-vs-unpruned difference reveals that the gripper dimension dominates (L2 = 1.02), corresponding to complete gripper state inversion on many frames. Position errors (0.20--0.30 per axis) are moderate individually but compound across the 7-dimensional action space. These single-step errors are large enough to push the robot off-trajectory within a few steps, explaining why 0\% of pruned episodes succeed in closed-loop evaluation despite moderate average offline metrics.
666	
667	\begin{table}[ht]
668	\centering
669	\small
670	\caption{Single-step action prediction error (SmolVLA, $k{=}0.50$, ACIS, zero-mask, 200 LIBERO-Object evaluation frames). Pruning increases action error by $3.4\times$ and introduces catastrophic gripper inversions.}
671	\label{tab:offline_action_error}
672	\begin{tabular}{lcc}
673	\toprule
674	Metric & Unpruned & Pruned ($k{=}0.50$) \\
675	\midrule
676	Action L2 vs.\ ground truth & 0.414 & 1.391 \\
677	Pruned vs.\ unpruned L2 & \multicolumn{2}{c}{1.284} \\
678	Relative action error & -- & 111.5\% \\
679	\midrule
680	\multicolumn{3}{l}{\textit{Per-dimension L2 (pruned vs.\ unpruned)}} \\
681	\quad Position $(x, y, z)$ & -- & 0.20, 0.25, 0.30 \\
682	\quad Rotation $(r_x, r_y, r_z)$ & -- & 0.01, 0.02, 0.01 \\
683	\quad Gripper & -- & 1.02 \\
684	\bottomrule
685	\end{tabular}
686	\end{table}
687	
688	
689	\section{Supplementary Figures}
690	\label{app:supplementary_figures}
691	
692	% fig_pixel_shuffle moved to Section~\ref{sec:pixel_shuffle} in main text.
693	
694	\begin{figure}[ht]
695	\centering
696	\includegraphics[width=\linewidth]{figures/paper/fig_entropy_layers.pdf}
697	\caption{Per-layer attention entropy ratio for SmolVLA (16 layers), OpenVLA (32 layers), and $\pi_{0}$ (18 layers). SmolVLA and $\pi_{0}$ maintain near-uniform attention throughout, while OpenVLA progressively sharpens from 0.98 to 0.48. Despite similar entropy, SmolVLA and $\pi_{0}$ exhibit opposite pruning outcomes due to token importance heterogeneity (CV $= 0.314$ vs.\ $0.038$). X-VLA (entropy $= 0.614$, CV $= 0.151$) occupies an intermediate position, consistent with its threshold-graded pattern (onset at $k{=}0.85$).}
698	\label{fig:entropy_layers}
699	\end{figure}
700	
701	
702	\section{Attention Entropy Measurement Details}
703	\label{app:entropy_details}
704	
705	We measure the attention entropy ratio as the normalized Shannon entropy of the attention weights that the action decoder assigns to vision token positions. For a model with $N$ vision tokens, the entropy ratio is:
706	\begin{equation}
707	H_{\text{ratio}} = \frac{-\sum_{i=1}^{N} \alpha_i \log \alpha_i}{\log N}
708	\end{equation}
709	where $\alpha_i$ is the attention weight on the $i$-th vision token. The ratio ranges from 0 (all attention on one token) to 1 (uniform attention).
710	
711	\paragraph{SmolVLA.} Measured on 2400 frames from LIBERO rollouts (overall entropy) and 260 frames across all 10 LIBERO-Object tasks (per-layer analysis across 16 layers). The mean per-layer entropy ratio is 0.95 (range: 0.93 to 0.98), consistent with near-uniform attention across all 128 vision tokens. The per-layer breakdown confirms this uniformity is not an averaging artifact:
712	\begin{itemize}[nosep]
713	    \item All 16 layers: 0.93--0.98 (spread 0.05)
714	    \item Minimum: layer 13 (0.93)
715	\end{itemize}
716	The flat profile across all processing depths confirms that pixel-shuffle tokens resist selective attention at every layer: because each token encodes 16 spatially contiguous patches via channel concatenation, all tokens are comparably information-dense, and the transformer has no basis for developing spatial selectivity.
717	
718	\paragraph{$\pi_{0}$.} Measured on 100 frames from LIBERO-Object (tasks 20--29) across all 18 layers of the Gemma-based PaliGemma backbone (512 vision tokens: 256 per image $\times$ 2 cameras). The mean suffix-to-vision entropy ratio is 0.959 (range: 0.931--0.983, std 0.013), near-uniform across all layers with no progressive sharpening:
719	\begin{itemize}[nosep]
720	    \item All 18 layers: 0.931--0.983 (spread 0.052)
721	    \item Minimum: 0.931; Maximum: 0.983
722	\end{itemize}
723	The flat entropy profile, combined with $\pi_{0}$'s extremely low CV (0.038), is consistent with its high tolerance to pruning: tokens carry near-equal importance and receive near-equal attention. Removing any subset approximates uniform spatial downsampling, preserving a proportional share of the visual field without disrupting the attention distribution.
724	
725	\paragraph{OpenVLA.} Measured on 250 frames from real LIBERO rollouts. The overall entropy ratio is 0.64. The layer-wise breakdown reveals progressive sharpening:
726	\begin{itemize}[nosep]
727	    \item Shallow layers (0--1): 0.95--0.98
728	    \item Early layers (2--4): 0.70--0.80
729	    \item Mid layers (12--20): 0.57--0.66
730	    \item Deep layers (24--30): 0.48--0.57 (minimum 0.48 at layer 29)
731	\end{itemize}
732	12.1\% of total attention weight falls on vision tokens overall, and within that fraction, the distribution is non-uniform in deeper layers. This progressive concentration indicates that OpenVLA has learned to selectively attend to task-relevant spatial locations, a pattern enabled by the MLP projector's preservation of per-patch spatial granularity.
733	
734	\paragraph{Measurement conditions.} All models are measured on real LIBERO rollout data: SmolVLA on 2400 frames (overall entropy) and 260 frames (per-layer analysis), $\pi_{0}$ on 100 frames from LIBERO-Object, OpenVLA on 250 frames from 50 episodes $\times$ 5 initial frames. Sample size differences reflect computational constraints (OpenVLA's 7B forward pass is substantially more expensive), but all measurements use task-relevant visual inputs. Entropy statistics show low variance across frames (std $< 0.02$ for OpenVLA, std $= 0.013$ for $\pi_{0}$).
735	
736	
737	\section{Connector Architecture and Token Independence}
738	\label{app:connector_analysis}
739	
740	The six-architecture taxonomy (Table~\ref{tab:model_properties}) spans a continuous spectrum of token independence structures, each associated with the vision-to-LLM connector rather than model scale or action head design.
741	
742	Pixel-shuffle connectors create maximal entanglement. SmolVLA's $4 \times 4$ spatial folding packs 16 patches into each token by channel concatenation (CV $= 0.314$, the highest in our study). The folding is fixed and irreversible: removing one token eliminates an entire receptive field, and no downstream layer can recover the discarded content. Tokens encode non-overlapping spatial regions with heterogeneous visual content, making every token simultaneously essential and non-redundant.
743	
744	Pure linear projections produce the opposite extreme. $\pi_{0}$ maps each SigLIP patch through a single linear layer with no cross-token interaction, yielding CV $= 0.038$ and near-maximal entropy (0.959). Tokens are genuinely interchangeable: any subset preserves the same per-patch information density as any other subset of equal size.
745	
746	$\pi_{0.5}$ reveals a subtlety that $\pi_{0}$'s offline-only evaluation conceals. The $\times\!\sqrt{d}$ learned scaling preserves near-uniform norms (CV $= 0.055$), yet the closed-loop response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\% SR while L2 norm-based removal collapses to 33.4\%. The 36\,pp gap arises because L2 ranking in a low-CV distribution selects spatially clustered tokens whose slight norm variations correlate with image regions, destroying the spatial coverage that this architecture requires. Token position analysis confirms this mechanism: at $k{=}0.5$, L2 selection produces a single dominant cluster containing 100\% of retained tokens with only 78\% spatial coverage, whereas $k{=}0.7$ yields two clusters with 97\% in the largest and 100\% coverage (Appendix~\ref{app:token_position}).
747	
748	X-VLA's 12-layer BART encoder~\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\,pp), confirming it as an architectural property.
749	
750	MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\% SR under 78\% pruning).
751	
752	Parameter count does not predict pruning tolerance. Ordered by scale: SmolVLA (450M) $<$ X-VLA (0.9B) $<$ $\pi_{0}$ (3.3B) $<$ $\pi_{0.5}$ (4B) $<$ OpenVLA (7B). Ordered by tolerance, SmolVLA remains the minimum, but $\pi_{0}$ and $\pi_{0.5}$ at 3.3--4B surpass OpenVLA at 7B, and X-VLA at 0.9B tolerates more aggressive pruning than OpenVLA. The CV spectrum (0.038 to 0.314) tracks connector complexity rather than parameter count across a 16$\times$ scale range.
753	
754	
755	\section{CV as Diagnostic Metric: Extended Analysis}
756	\label{app:cv_extended}
757	\label{sec:diagnostic}
758	
759	Token importance CV correlates with both the tolerance class of a model and the optimal pruning strategy, a correlation that emerges from a single mechanistic principle: CV measures the strength of the importance gradient that scoring methods can exploit.
760	
761	Low-CV models have near-uniform L2 norms. L2 norm ranking in this regime captures spatial artifacts (slight norm variations that correlate with image position) rather than genuine importance differences. Selection based on these artifacts concentrates retained tokens on spatially correlated patches, destroying the uniform coverage that low-CV architectures depend on. Random selection preserves spatial uniformity by construction. The mechanism predicts that the L2-over-random advantage should grow as CV increases, and the data in Table~\ref{tab:scaling_law} confirm this. On LIBERO-Object at $k{=}0.5$: $\Delta = -$36.0\,pp ($\pi_{0.5}$, CV $= 0.055$) $\to$ $-$26.9\,pp (X-VLA, CV $= 0.151$) $\to$ $+$3.4\,pp (OpenVLA, CV $= 0.215$). At $k{=}0.7$, the same ordering holds for $\pi_{0.5}$ and X-VLA ($-$22.2\,pp $\to$ $-$6.5\,pp); OpenVLA lacks a seed-matched pair at this ratio. The pattern persists across retention ratios, strengthening the interpretation from a coincidence at a single operating point to a structural property of the connector.
762	
763	On simple manipulation tasks (Object), high-CV models present a genuine importance gradient where L2 norm ranking aligns with actual information content. OpenVLA (CV $= 0.215$) sits near the crossover on Object: L2 outperforms random by 7.8\,pp at $k{=}0.9$ where the gradient is most exploitable, shrinking to 3.4\,pp at $k{=}0.5$ as the proportion of removed tokens exceeds the gradient's discriminative range. On complex multi-step tasks, this advantage diminishes or reverses: OpenVLA Long at $k{=}0.9$ shows Random outperforming L2 by 3.2\,pp (46.8\% vs.\ 43.6\%), as compositional tasks distribute critical information across tokens with heterogeneous norm profiles (Section~\ref{sec:analysis}).
764	
765	Extreme compression introduces a partial reversal. At $k{=}0.3$, $\pi_{0.5}$'s L2 selection achieves $53.2 \pm 3.1$\% SR (2 seeds) vs.\ random's 36.4\%. When very few tokens remain, even spatially clustered high-norm tokens provide more signal than a sparse random sample. The V-shaped L2 curve is confirmed across seeds ($\sigma{=}0.1$\,pp at the $k{=}0.5$ valley). The reversal does not invalidate the CV diagnostic; it adds a budget-dependent interaction that future work should characterize across more models.
766	
767	Attention entropy provides a mechanistic supplement that resolves an apparent paradox. SmolVLA's entropy (0.952) is nearly as high as $\pi_{0}$'s (0.959), yet SmolVLA collapses under any pruning. SmolVLA's tokens are uniformly \emph{attended} but carry heterogeneous \emph{content} due to pixel-shuffle folding. Entropy captures how the LLM allocates attention across tokens; CV captures the input-side importance structure. Entropy alone cannot distinguish ``interchangeable'' ($\pi_{0}$) from ``entangled'' (SmolVLA), but CV separates them cleanly (0.038 vs.\ 0.314). OpenVLA's progressive entropy sharpening from 0.98 to 0.48 across layers (Figure~\ref{fig:entropy_layers}) is consistent with a graded regime where the LLM progressively concentrates on higher-importance tokens.
768	
769	
770	\section{Why Re-Encoding Succeeds: Extended Analysis}
771	\label{app:reencoding_analysis}
772	\label{sec:learned_compression}
773	
774	Learned re-encoding overcomes pixel-shuffle failure because it breaks the rigid spatial entanglement that the $4 \times 4$ folding creates. Cross-attention pooling integrates information across receptive field boundaries, redistributing content from the original 128 tokens into $M$ compressed representations no longer tied to fixed spatial blocks.
775	
776	The $M{=}128$ passthrough configuration suggests that re-encoding, not compression, is the key factor. Passthrough adds parameters without reducing token count, yet gains 13\,pp over the baseline (44.8\% $\to$ 58.0\%). The relatively stable M-curve ($M{=}16$: 56.9\% closely matches $M{=}128$: 58.0\%, within 1.1\,pp) shows that once entanglement is broken, token count is secondary.
777	
778	A parameter-matched MLP adapter (22.14M parameters) achieves 63.4\% SR at $M{=}32$, statistically indistinguishable from cross-attention ($p = 0.15$). Re-encoding through any learned mapping that integrates across token boundaries suffices; the attention mechanism itself is not essential.
779	
780	The remedy is specific to the pathology. VTR succeeds precisely on architectures whose rigid spatial entanglement demands learned redistribution; for token-independent connectors where each patch already carries self-contained information, re-encoding is unnecessary.
781	
782	
783	\section{Offline Metrics Underestimate Closed-Loop Failure}
784	\label{app:offline_disconnect}
785	\label{sec:metric_disconnect}
786	
787	Offline evaluation systematically underestimates pruning-induced failure because per-step averages dilute catastrophic single-step events that individually terminate episodes.
788	
789	X-VLA at $k{=}0.3$ demonstrates the gap directly: offline loss is 1.0014 (near-baseline), yet closed-loop SR drops to $22.0 \pm 0.9$\% ($-$77\,pp). A single gripper inversion (L2 $= 1.02$) is a minor perturbation in average action error but terminates an episode irreversibly. $\pi_{0}$'s offline loss at $k{=}0.1$ shows a 2.4\% \emph{improvement} over the unpruned baseline (offline metrics only; no closed-loop evaluation available), a result that closed-loop evaluation may contradict if similar catastrophic events occur at deployment frequency.
790	
791	$\pi_{0.5}$ adds a distinct form of evidence: the 36\,pp gap between L2 and random removal at $k{=}0.5$ is invisible to any offline metric that averages across token subsets or selection methods. Offline evaluation would report degradation for both methods; only closed-loop evaluation reveals that the \emph{choice} of pruning strategy, not just the pruning ratio, is associated with whether the model remains functional.
792	
793	
794	\section{Confounder Analysis}
795	\label{app:confounders}
796	
797	The six architectures span three connector families but differ simultaneously in LLM backbone (PaliGemma for $\pi_{0}$/$\pi_{0.5}$, Llama-2 for OpenVLA, Florence-2 for X-VLA, SmolLM2 for SmolVLA), preventing clean isolation of the connector effect from backbone differences. The $\pi_{0}$--OpenVLA comparison (same 256 SigLIP-based tokens, different connector, backbone, and encoder fusion strategy) provides the closest available approximation, but a matched-backbone experiment remains the ideal control. This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation. Token count also varies across models (50 for X-VLA, 128 for SmolVLA, 256 for $\pi_{0}$/OpenVLA, 768 for $\pi_{0.5}$); the $\pi_{0}$--OpenVLA pair controls for this confounder within the CV analysis while still exhibiting the predicted CV-gap relationship.
798	
799	The spatial clustering hypothesis for L2 failure on low-CV models is confirmed by token position analysis (Appendix~\ref{app:token_position}).
800	
801	OpenVLA main-text results use seed 42 for both L2 and random. Cross-seed (seed 7) random comparison in Table~\ref{tab:openvla_l2_vs_random} confirms the L2 advantage is seed-independent: the gap ranges from $+$0.8 to $+$8.6\,pp across retention ratios regardless of random seed.
802	
803	
804	\section{Token Position Analysis}
805	\label{app:token_position}
806	
807	To validate the spatial clustering hypothesis for L2 norm failure on low-CV models, we analyze the spatial distribution of tokens selected by L2 norm ranking on $\pi_{0.5}$ across three retention ratios.
808	
809	At $k{=}0.7$ (538 of 768 tokens retained): DBSCAN clustering identifies 2 spatial clusters, with 97\% of retained tokens in the largest cluster and 100\% spatial coverage of the original image grid. The broad coverage explains why L2 selection still achieves 55.0\% SR at this retention ratio.
810	
811	At $k{=}0.5$ (384 tokens retained): a single dominant cluster contains 100\% of retained tokens with only 78\% spatial coverage. The complete concentration into one spatial region confirms the clustering hypothesis: L2 norm ranking selects tokens from a contiguous high-norm region while abandoning 22\% of the spatial field. This is the retention ratio where L2 performance reaches its minimum (33.4\% SR, the V-shape valley).
812	
813	At $k{=}0.3$ (230 tokens retained): 3 clusters emerge, with 86\% in the largest and 78\% spatial coverage. The fragmentation into multiple clusters at extreme compression is consistent with the partial L2 recovery observed at this ratio ($53.2 \pm 3.1$\% SR): when the budget is very small, L2 selection is forced to sample from multiple spatial regions, partially restoring coverage.
814	
815	These results directly confirm that L2 norm ranking on low-CV models introduces spatial bias that degrades performance, and that the severity peaks at intermediate retention ratios where concentration is maximal.
816	
817	
818	\section{CV Scaling Law: Full Data}
819	\label{app:cv_scaling_table}
820	
821	\begin{table}[ht]
822	\centering
823	\small
824	\caption{L2 norm vs.\ random removal at two retention ratios. The importance margin $\Delta$(L2$-$R) increases monotonically with CV at both $k{=}0.5$ and $k{=}0.7$: low-CV models require random selection (uniform importance $\rightarrow$ L2 degenerates to spatial clustering), while high-CV models tolerate either strategy on simple tasks (see Section~\ref{sec:analysis} for task-dependent caveats). Data shown for LIBERO-Object; the monotonic ordering holds across retention ratios despite a 2$\times$ change in token budget.}
825	\label{tab:scaling_law}
826	\begin{tabular}{lccccc}
827	\toprule
828	Model & CV & Tokens & L2 SR (\%) & Random SR (\%) & $\Delta$(L2$-$R) \\
829	\midrule
830	\multicolumn{6}{l}{\textit{$k{=}0.5$ (50\% retention)}} \\
831	$\pi_{0.5}$ & 0.055 & 768 & 33.4 & \textbf{69.4} & $-$36.0 \\
832	X-VLA & 0.151 & 50 & 43.4$\pm$0.8 & \textbf{70.3}$\pm$0.9 & $-$26.9 \\
833	OpenVLA & 0.215 & 256 & \textbf{39.2} & 35.8 & $+$3.4 \\
834	\midrule
835	\multicolumn{6}{l}{\textit{$k{=}0.7$ (70\% retention)}} \\
836	$\pi_{0.5}$ & 0.055 & 768 & 55.0 & \textbf{74.0} & $-$19.0 \\
837	X-VLA & 0.151 & 50 & 58.6$\pm$0.4 & \textbf{65.1}$\pm$0.1 & $-$6.5 \\
838	OpenVLA\textsuperscript{$\dagger$} & 0.215 & 256 & -- & -- & -- \\
839	\bottomrule
840	\multicolumn{6}{l}{\footnotesize\textsuperscript{$\dagger$}$k{=}0.7$ omitted: no seed-matched L2/Random pair available.}
841	\end{tabular}
842	\end{table}
843	
844	
845	\section{CV-Strategy Interaction at Extreme Compression}
846	\label{app:cv_strategy_interaction}
847	
848	The monotonic CV-gap relationship (Table~\ref{tab:scaling_law}) holds at $k{=}0.5$ and $k{=}0.7$, but partially reverses at $k{=}0.3$ for $\pi_{0.5}$. At this extreme budget, L2 norm selection achieves $53.2 \pm 3.1$\% SR (2 seeds) vs.\ random's 36.4\%, favoring L2 by $\sim$17\,pp. The reversal is consistent across both seeds (seed42: 51.0\%, seed43: 55.4\%; Table~\ref{tab:pi05_l2_multiseed}).
849	
850	The mechanism is intuitive: when very few tokens remain ($k{=}0.3$ retains 230 of 768 tokens), even spatially clustered high-norm tokens provide more visual signal than a sparse random sample. At intermediate budgets ($k{=}0.5$, 384 tokens), random selection preserves enough spatial coverage to outperform L2's clustered selection; at extreme budgets, coverage from random selection becomes too sparse to be useful, and the concentrated signal from L2 selection dominates.
851	
852	The interaction implies that the optimal pruning strategy depends on both CV and the absolute token budget. For low-CV models, the crossover point between random-preferred and L2-preferred regimes lies between $k{=}0.3$ and $k{=}0.5$. Characterizing this crossover across additional models and budgets is left to future work.
853	
854	
855	\section{Inference Cost-Benefit Analysis}
856	\label{app:cost_benefit}
857	
858	The primary deployment benefit of VTR at this model scale is memory, not latency. Reducing from 128 to 32 vision tokens shrinks the KV-cache footprint for the vision portion by 75\%, a meaningful reduction for memory-constrained robotic hardware where KV-cache size can limit the number of concurrent policy instances or maximum context length.
859	
860	End-to-end inference latency improves only modestly: 154.78\,ms at $M{=}32$ versus 164.33\,ms at full token count, a $1.06\times$ speedup (6\% reduction). At $M{=}64$: 156.16\,ms ($1.05\times$). The gap between token reduction and latency gain reflects SmolVLA's compact size (450M parameters): self-attention over 128 vision tokens is not the inference bottleneck, and the compressor's 22.2M-parameter cross-attention computation partially offsets downstream savings. Token pruning becomes a more compelling latency optimization for VLAs with larger token budgets ($>$256 tokens) or larger backbones (7B+ parameters), where attention cost scales quadratically with sequence length. Whether the training cost (100K steps, 6.5 hours per configuration) is justified depends on deployment context: for VLAs deployed across many tasks, the one-time training cost is amortized; for rapid prototyping, retraining is a barrier.
861	
862	\paragraph{Comparison with the official checkpoint.}
863	VTR at $M = 32$ ($60.1 \pm 1.3$\% over 3 seeds) recovers from 0\% SR under hard pruning to performance comparable to the official SmolVLA checkpoint (59.2\%, CI [54.8\%, 63.4\%]). However, the difference is not statistically significant (two-sample $t$-test, $p \approx 0.72$), and the comparison should be interpreted cautiously given different training conditions (batch size 4 vs.\ 64, single vs.\ 8 GPUs). The primary contribution of VTR is recovering functional performance where all deletion methods yield 0\%, not matching the official baseline.
864	
865	\subsection{Attention-Based Scoring Methods}
866	\label{app:attention_scoring}
867	\label{app:attention_pruning}
868	
869	Attention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer; (ii)~\emph{cross-layer mean scoring} averages column-sum scores across all layers; (iii)~\emph{attention rollout} multiplies attention matrices layer by layer (adding identity for residual connections) to approximate cumulative information flow. These methods require a full LLM forward pass and are backbone-specific. We focus on L2 and random in the main text because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.
870	
871	\subsection{Attention Entropy as Diagnostic}
872	\label{app:attention_entropy}
873	
874	Attention entropy, defined as the mean Shannon entropy of the LLM's attention distribution over vision tokens, provides a complementary but less discriminative signal than CV. Three models with qualitatively different pruning behaviors cluster within a narrow entropy band: $\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \emph{reading pattern} (how attention is distributed), while CV reflects the connector's \emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness.
875	
876	\subsection{Attention-Based Scoring Results}
877	
878	Table~\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\_last), mean attention across all decoder layers (attn\_mean), and attention rollout~\cite{abnar2020quantifying}.
879	
880	\begin{table}[h]
881	\centering
882	\small
883	\caption{X-VLA success rates (\%) at $k{=}0.5$ across five scoring methods. Attention-based scoring recovers near-baseline performance across all suites while L2 norm falls below random on every suite. Bold indicates best per suite. \textsuperscript{*}Best of three attention variants.}
884	\label{tab:attention_pruning}
885	\begin{tabular}{lccccc}
886	\toprule
887	Suite & attn\_last & attn\_mean & attn\_rollout & L2 & Random \\
888	\midrule
889	Object & \textbf{99.2} & 98.4 & 97.4 & 43.4 & 70.6 \\
890	Spatial & 88.8 & 91.6 & \textbf{92.8} & 58.8 & 71.4 \\
891	Long & 90.2 & 94.0 & \textbf{94.8} & 45.0 & 61.6 \\
892	Goal & \textbf{98.2} & 97.4 & 96.8 & 59.0 & 67.2 \\
893	\bottomrule
894	\end{tabular}
895	\end{table}
896	
897	L2 norm selection is anti-informative on X-VLA's entangling connector: L2 falls below random on all four suites, with gaps ranging from $-$8.2\,pp (Goal) to $-$27.2\,pp (Object). Attention-based scoring recovers near-baseline performance across all suites (${\geq}$92.8\%), with rollout peaking at 94.8\% on Long (seed43 confirms $\Delta{\leq}$0.6\,pp). On Object, all three attention variants achieve ${\geq}$97.4\%, far exceeding both L2 (43.4\%) and random (70.6\%). The mode ranking reverses across suites: last-layer attention is best on Object (99.2\%) but worst among attention methods on Spatial (88.8\%) and Long (90.2\%), while rollout shows the opposite pattern.
898	
899	The L2 failure has a structural explanation. The BART encoder's 12-layer self-attention redistributes information across tokens, equalizing activation magnitudes (CV$\,{=}\,$0.151). L2 norms no longer reflect token importance; instead, they select spatially correlated clusters that miss critical information. Goal L2 exhibits non-monotonic behavior ($k{=}0.7$: 53.4\% $<$ $k{=}0.5$: 59.0\%), confirming that retaining more L2-selected tokens is actively harmful. Per-task variance under L2 pruning is extreme on Spatial (std$\,{=}\,$31.5\,pp, range 0--92\%), while attention scoring keeps all tasks above 80\%. The double dissociation extends to $\pi_{0.5}$, where attention scoring at $k{=}0.5$ exhibits suite-dependent failure (Table~\ref{tab:pi05_attention_crosssuite}). On three suites (Goal, Spatial, Long), attention performs within noise of random ($\pm$3\,pp). On Object, attention collapses to 37.8\% ($-$31.6\,pp vs.\ random's 69.4\%), a catastrophic failure unique to tasks requiring spatial discrimination among visually similar alternatives. The linear connector produces an extremely narrow attention score range ($[2{\times}10^{-6},\, 3.6{\times}10^{-3}]$) with systematic position bias favoring early tokens; on Object, this bias selects semantically relevant but spatially uninformative tokens, destroying the fine-grained spatial information needed for target identification.
900	
901	\begin{table}[ht]
902	\centering
903	\small
904	\caption{$\pi_{0.5}$ attention vs.\ random at $k{=}0.5$ across LIBERO suites. Attention is neutral on 3/4 suites but catastrophically harmful on Object.}
905	\label{tab:pi05_attention_crosssuite}
906	\begin{tabular}{lccc}
907	\toprule
908	Suite & Attention (\%) & Random (\%) & $\Delta$ (pp) \\
909	\midrule
910	Goal & 71.2 & 73.6 & $-$2.4 \\
911	Spatial & 72.6 & 71.6 & $+$1.0 \\
912	Long & 49.4 & 46.8 & $+$2.6 \\
913	Object & 37.8 & 69.4 & $-$31.6 \\
914	\bottomrule
915	\end{tabular}
916	\end{table} By contrast, $\pi_{0.5}$'s L2 norms do reflect importance: on Goal, L2 outperforms random by $+$35.2\,pp at $k{=}0.85$, decaying to $+$5.4\,pp at $k{=}0.95$ (log-decay trend across four retention ratios). This yields a connector-dependent scoring reversal: attention is effective on entangling connectors but not token-independent ones, while L2 norm shows the converse (Figure~\ref{fig:scoring_crossover}).
917	
918	\begin{table}[h]
919	\centering
920	\small
921	\caption{Scoring reversal summary: $\Delta$ vs.\ random at $k{=}0.5$, except \textsuperscript{*}Goal suite across $k \in [0.85, 0.95]$. Compact view of the pattern shown in Figure~\ref{fig:scoring_crossover}.}
922	\label{tab:scoring_crossover_summary}
923	\begin{tabular}{lcc}
924	\toprule
925	& Attention & L2 norm \\
926	\midrule
927	Entangling (X-VLA) & Effective ($+$31\,pp) & Anti-inform.\ ($-$8 to $-$27\,pp) \\
928	Token-indep.\ ($\pi_{0.5}$) & Ineffective\textsuperscript{$\dagger$} ($-$2 to $-$32\,pp) & Effective\textsuperscript{*} ($+$35.2$\to$$+$5.4\,pp) \\
929	\bottomrule
930	\multicolumn{3}{l}{\footnotesize\textsuperscript{$\dagger$}Neutral on 3/4 suites ($\pm$3\,pp); harmful on Object ($-$31.6\,pp).}
931	\end{tabular}
932	\end{table}
933	
934	
935	\section{AI Disclosure}
936	\label{app:ai_disclosure}
937	
938	AI tools assisted code development and manuscript drafting; all scientific claims, experimental designs, and interpretations are the authors' own.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "0d1ebb98-ba78-4144-85bf-8fec593b7953",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
      "content": "\\begin{tabular}{lccccr}\n\\toprule\n$M$ & Seed 42 & Seed 43 & Seed 44 & Mean $\\pm$ Std \\\\\n\\midrule\n32 & 61.6 & 59.2 & 59.6 & 60.1 $\\pm$ 1.3 \\\\\n64 & 61.6 & 60.0 & 64.4 & 62.0 $\\pm$ 2.2 \\\\\n96 & 52.6 & 58.2 & 52.8 & 54.5 $\\pm$ 3.2 \\\\\n128 & 59.8 & 54.0 & 60.2 & 58.0 $\\pm$ 3.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{VTR Full Results}\n\\label{app:vtr_full}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\\% compression) matches $M{=}128$ (passthrough) within 1.1\\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}\n\\label{tab:vtr_results}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compression & SR (\\%) \\\\\n\\midrule\n\\textit{SmolVLA-Base (LoRA)} & 128 & 0\\% & 44.8 \\\\\n\\textit{SmolVLA official} & 128 & 0\\% & 59.2 \\\\\n\\textit{Baseline control (+100K steps)} & 128 & 0\\% & 45.0 \\\\\n\\textit{Hard pruning (any $k$)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 64 & 50\\% & \\textbf{62.0 $\\pm$ 2.2} \\\\\nCross-attn VTR & 96 & 25\\% & 54.5 $\\pm$ 3.2 \\\\\nCross-attn VTR & 128 & 0\\% & 58.0 $\\pm$ 3.5 \\\\\n\\midrule\nMLP adapter ($\\sim$22M) & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Full VTR Ablation}\n\\label{app:smart_compress_full}\n\nTable~\\ref{tab:smart_compress_full} reports all five VTR configurations. The cross-attention module improves performance regardless of compression: $M \\in \\{32, 64, 128\\}$ all achieve $\\sim$60\\% SR, exceeding the 44.8\\% baseline by 15--17 points ($p < 0.001$, two-proportion $z$-test). Only at $M = 16$ (87.5\\% compression) does performance decline modestly to 55.8\\%, still 11 points above baseline. The $M{=}96$ dip (mean 54.5\\% across three seeds, Table~\\ref{tab:multi_seed}) may reflect an intermediate bottleneck that introduces representational redundancy without the regularization benefit of stronger compression ($M{=}32$, $M{=}64$).\n\nTable~\\ref{tab:cross_suite} reports performance across task suites. All suites are in-distribution: the training set (HuggingFaceVLA/libero) covers Object, Spatial, Goal, and Long. On LIBERO-Spatial, VTR achieves 53.2\\% SR (vs.\\ 0\\% under hard pruning); on LIBERO-Goal, 56.4\\% SR ($-6.6$pp from the 63.0\\% unpruned baseline, vs.\\ 0\\% under pruning). The LIBERO-Goal decline indicates that re-encoding benefits vary across task structures even within the training distribution. Per-task results are in Table~\\ref{tab:smart_compress_pertask}.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Full VTR ablation on LIBERO-Object across five compression levels. $M{=}32$ and $M{=}64$ achieve similar SR ($\\sim$60\\%); $M{=}96$ shows a modest dip; the $M{=}128$ passthrough confirms the gain originates from re-encoding.}\n\\label{tab:smart_compress_full}\n\\begin{tabular}{lcccrr}\n\\toprule\nMethod & $M$ & Reduction & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\textit{Baseline} & 128 & 0\\% & 44.8 & 500 & [40.5, 49.2] \\\\\n\\textit{Extended training} & -- & -- & 45.0 & 500 & [40.7, 49.3] \\\\\n\\textit{Hard pruning} & -- & 50--90\\% & 0.0 & 500+ & [0, 0.76] \\\\\n\\midrule\nVTR & 128 & 0\\% & 58.0 & 1500 & $\\pm$3.5 \\\\\nVTR & 96 & 25\\% & 52.6 & 500 & [48.2, 56.9] \\\\\nVTR & 64 & 50\\% & 61.6 & 500 & [57.3, 65.8] \\\\\nVTR & 32 & 75\\% & 61.6 & 500 & [57.3, 65.8] \\\\\nVTR & 16 & 87.5\\% & 55.8 & 500 & [51.4, 60.1] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\footnotesize $M{=}128$ reports mean $\\pm$ std over 3 seeds (500 episodes each). Other VTR rows report single seed (seed 42) with Wilson 95\\% CI. See Table~\\ref{tab:multi_seed} for full multi-seed results.}\n\\end{table}\n\n\n\\section{VTR Evaluation Across Task Suites}\n\\label{app:cross_suite}\n\nTable~\\ref{tab:cross_suite} reports the performance of VTR ($M{=}32$) across three LIBERO suites. All suites are in-distribution: the training set (HuggingFaceVLA/libero) covers Object, Spatial, Goal, and Long (40 tasks, 1693 episodes total). On LIBERO-Goal, performance drops from 63.0\\% to 56.4\\% ($-6.6$pp). On LIBERO-Spatial, VTR achieves 53.2\\% SR, where the official SmolVLA checkpoint scores 44.6\\% and hard pruning yields near-zero (0.6\\%). While 53.2\\% nominally exceeds the official Spatial baseline, this difference concentrates in two of ten tasks (+44pp and +48pp respectively); the remaining eight tasks show a net difference of only +0.2pp. We therefore do not treat the Spatial comparison as evidence that re-encoding improves over the uncompressed official baseline. The qualitative pattern (cliff-edge vulnerability and re-encoding recovery) extends across the three tested task structures within the training distribution. The LIBERO-Goal decline indicates that re-encoding benefits vary across task structures.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR ($M{=}32$) evaluation across LIBERO task suites. All suites are in-distribution (training covers Object, Spatial, Goal, Long). Hard pruning (any method, $k{=}0.50$) produces 0\\% or near-zero on all suites.}\n\\label{tab:cross_suite}\n\\begin{tabular}{lccc}\n\\toprule\nSuite & Baseline (unpruned) & VTR $M{=}32$ & Hard Pruning $k{=}0.50$ \\\\\n\\midrule\nObject & 44.8\\% & 61.6\\% & 0\\% \\\\\nSpatial & 51.8\\% & 53.2\\% & 0.6\\% \\\\\nGoal & 63.0\\% & 56.4\\% & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{VTR Training Details}\n\\label{app:smart_compress_details}\n\nThe VTR module is a cross-attention pooling layer inserted between SmolVLA's pixel-shuffle vision connector and the SmolLM2 language backbone. It consists of $M$ learned query vectors that attend over the 128 vision tokens through standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compressor adds 22.2M trainable parameters (approximately 5\\% of SmolVLA's 450M total). Training is end-to-end: compressor and VLA policy parameters are jointly optimized.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR training hyperparameters. All configurations ($M \\in \\{16, 32, 64, 96, 128\\}$) use identical procedures; only the number of query vectors differs.}\n\\label{tab:training_hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nHyperparameter & Value \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Model}} \\\\\n\\quad Base checkpoint & SmolVLA-Base (pretrained, before LIBERO fine-tuning) \\\\\n\\quad Compressor architecture & Cross-attention, 2 layers, 12 heads, dropout 0.1 \\\\\n\\quad Compressor parameters & 22.2M \\\\\n\\quad Total trainable parameters & 122.1M / 472.2M (25.85\\%) \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Optimization}} \\\\\n\\quad Optimizer & AdamW ($\\beta_1{=}0.9$, $\\beta_2{=}0.95$, weight decay $10^{-10}$) \\\\\n\\quad Learning rate & $10^{-4}$ \\\\\n\\quad Schedule & Linear warmup (1K steps, start factor 0.01) $\\to$ cosine \\\\\n\\quad & annealing ($\\eta_{\\min}{=}2.5 \\times 10^{-6}$) \\\\\n\\quad Max gradient norm & 10.0 \\\\\n\\quad Total training steps & 100,000 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Data \\& batching}} \\\\\n\\quad Dataset & HuggingFaceVLA/libero (40 tasks, 1693 episodes across \\\\\n\\quad & Object, Spatial, Goal, Long suites) \\\\\n\\quad Batch size & 4 (no gradient accumulation)$^\\dagger$ \\\\\n\\quad Num workers & 4 \\\\\n\\quad Eval interval & every 5K steps \\\\\n\\quad Checkpoint interval & every 1K steps \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Hardware \\& runtime}} \\\\\n\\quad Hardware & 1$\\times$ NVIDIA RTX 4090 D (24GB) \\\\\n\\quad Precision & fp32 (no mixed precision) \\\\\n\\quad Wall clock & $\\sim$6h 43m per configuration \\\\\n\\quad Training speed & 4.1 samples/sec \\\\\n\\quad Seed & 42 (seeds 43, 44 for multi-seed runs) \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{$M=32$ final metrics}} \\\\\n\\quad Train action loss & 0.11 \\\\\n\\quad Eval action loss & 0.052 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{$M=64$ final metrics}} \\\\\n\\quad Train action loss & 0.045 \\\\\n\\quad Eval action loss & 0.062 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$The official SmolVLA checkpoint uses batch size 64 across 8 GPUs (effective batch size 512). Our batch size 4 on a single GPU contributes to the lower baseline SR (44.8\\% vs.\\ 87.3\\%). All VTR configurations and the extended training control use this same batch size for fair comparison.}\n\\end{table}\n\nThe loss profile differs between configurations: $M=32$ has higher train loss (0.11 vs.\\ 0.045) but lower eval loss (0.052 vs.\\ 0.062), consistent with the smaller bottleneck acting as a stronger regularizer. Despite this loss difference, both achieve identical closed-loop success rates (61.6\\%), reinforcing the finding that offline loss does not predict closed-loop performance (Section~\\ref{sec:metric_disconnect}).\n\n\\subsection{MLP Adapter Control}\n\\label{app:mlp_adapter}\n\nTo verify that re-encoding effectiveness is not specific to cross-attention, we train a parameter-matched MLP adapter as a control. The adapter is a 3-layer feed-forward network with expansion ratio 4 (hidden dimension $4 \\times d_{\\text{model}}$), using average pooling for token reduction from 128 to $M$ tokens. Total parameters: 22.14M, matched to the cross-attention module's 22.2M. Training follows the identical protocol as VTR: SmolVLA-Base checkpoint, 100K steps, learning rate $10^{-4}$, batch size 4, same LIBERO dataset. At $M = 32$ (75\\% reduction), the MLP adapter achieves $63.4 \\pm 2.6$\\% SR over 3 seeds, statistically indistinguishable from the cross-attention result ($60.1 \\pm 1.3$\\%; two-sample $t$-test, $p = 0.15$). This confirms that the re-encoding benefit does not depend on the specific module architecture.\n\n\n\\section{Offline Single-Step Action Error Analysis}\n\\label{app:offline_error}\n\nTable~\\ref{tab:offline_action_error} reports the single-step action prediction error under pruning, computed over 200 evaluation frames from LIBERO-Object. The unpruned model (bypass mode) produces actions with an L2 distance of 0.414 from ground truth; under ACIS pruning at $k{=}0.50$, this increases to 1.391 ($3.4\\times$). The per-dimension breakdown of the pruned-vs-unpruned difference reveals that the gripper dimension dominates (L2 = 1.02), corresponding to complete gripper state inversion on many frames. Position errors (0.20--0.30 per axis) are moderate individually but compound across the 7-dimensional action space. These single-step errors are large enough to push the robot off-trajectory within a few steps, explaining why 0\\% of pruned episodes succeed in closed-loop evaluation despite moderate average offline metrics.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Single-step action prediction error (SmolVLA, $k{=}0.50$, ACIS, zero-mask, 200 LIBERO-Object evaluation frames). Pruning increases action error by $3.4\\times$ and introduces catastrophic gripper inversions.}\n\\label{tab:offline_action_error}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Unpruned & Pruned ($k{=}0.50$) \\\\\n\\midrule\nAction L2 vs.\\ ground truth & 0.414 & 1.391 \\\\\nPruned vs.\\ unpruned L2 & \\multicolumn{2}{c}{1.284} \\\\\nRelative action error & -- & 111.5\\% \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-dimension L2 (pruned vs.\\ unpruned)}} \\\\\n\\quad Position $(x, y, z)$ & -- & 0.20, 0.25, 0.30 \\\\\n\\quad Rotation $(r_x, r_y, r_z)$ & -- & 0.01, 0.02, 0.01 \\\\\n\\quad Gripper & -- & 1.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Supplementary Figures}\n\\label{app:supplementary_figures}\n\n% fig_pixel_shuffle moved to Section~\\ref{sec:pixel_shuffle} in main text.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_entropy_layers.pdf}\n\\caption{Per-layer attention entropy ratio for SmolVLA (16 layers), OpenVLA (32 layers), and $\\pi_{0}$ (18 layers). SmolVLA and $\\pi_{0}$ maintain near-uniform attention throughout, while OpenVLA progressively sharpens from 0.98 to 0.48. Despite similar entropy, SmolVLA and $\\pi_{0}$ exhibit opposite pruning outcomes due to token importance heterogeneity (CV $= 0.314$ vs.\\ $0.038$). X-VLA (entropy $= 0.614$, CV $= 0.151$) occupies an intermediate position, consistent with its threshold-graded pattern (onset at $k{=}0.85$).}\n\\label{fig:entropy_layers}\n\\end{figure}\n\n\n\\section{Attention Entropy Measurement Details}\n\\label{app:entropy_details}\n\nWe measure the attention entropy ratio as the normalized Shannon entropy of the attention weights that the action decoder assigns to vision token positions. For a model with $N$ vision tokens, the entropy ratio is:\n\\begin{equation}\nH_{\\text{ratio}} = \\frac{-\\sum_{i=1}^{N} \\alpha_i \\log \\alpha_i}{\\log N}\n\\end{equation}\nwhere $\\alpha_i$ is the attention weight on the $i$-th vision token. The ratio ranges from 0 (all attention on one token) to 1 (uniform attention).\n\n\\paragraph{SmolVLA.} Measured on 2400 frames from LIBERO rollouts (overall entropy) and 260 frames across all 10 LIBERO-Object tasks (per-layer analysis across 16 layers). The mean per-layer entropy ratio is 0.95 (range: 0.93 to 0.98), consistent with near-uniform attention across all 128 vision tokens. The per-layer breakdown confirms this uniformity is not an averaging artifact:\n\\begin{itemize}[nosep]\n    \\item All 16 layers: 0.93--0.98 (spread 0.05)\n    \\item Minimum: layer 13 (0.93)\n\\end{itemize}\nThe flat profile across all processing depths confirms that pixel-shuffle tokens resist selective attention at every layer: because each token encodes 16 spatially contiguous patches via channel concatenation, all tokens are comparably information-dense, and the transformer has no basis for developing spatial selectivity.\n\n\\paragraph{$\\pi_{0}$.} Measured on 100 frames from LIBERO-Object (tasks 20--29) across all 18 layers of the Gemma-based PaliGemma backbone (512 vision tokens: 256 per image $\\times$ 2 cameras). The mean suffix-to-vision entropy ratio is 0.959 (range: 0.931--0.983, std 0.013), near-uniform across all layers with no progressive sharpening:\n\\begin{itemize}[nosep]\n    \\item All 18 layers: 0.931--0.983 (spread 0.052)\n    \\item Minimum: 0.931; Maximum: 0.983\n\\end{itemize}\nThe flat entropy profile, combined with $\\pi_{0}$'s extremely low CV (0.038), is consistent with its high tolerance to pruning: tokens carry near-equal importance and receive near-equal attention. Removing any subset approximates uniform spatial downsampling, preserving a proportional share of the visual field without disrupting the attention distribution.\n\n\\paragraph{OpenVLA.} Measured on 250 frames from real LIBERO rollouts. The overall entropy ratio is 0.64. The layer-wise breakdown reveals progressive sharpening:\n\\begin{itemize}[nosep]\n    \\item Shallow layers (0--1): 0.95--0.98\n    \\item Early layers (2--4): 0.70--0.80\n    \\item Mid layers (12--20): 0.57--0.66\n    \\item Deep layers (24--30): 0.48--0.57 (minimum 0.48 at layer 29)\n\\end{itemize}\n12.1\\% of total attention weight falls on vision tokens overall, and within that fraction, the distribution is non-uniform in deeper layers. This progressive concentration indicates that OpenVLA has learned to selectively attend to task-relevant spatial locations, a pattern enabled by the MLP projector's preservation of per-patch spatial granularity.\n\n\\paragraph{Measurement conditions.} All models are measured on real LIBERO rollout data: SmolVLA on 2400 frames (overall entropy) and 260 frames (per-layer analysis), $\\pi_{0}$ on 100 frames from LIBERO-Object, OpenVLA on 250 frames from 50 episodes $\\times$ 5 initial frames. Sample size differences reflect computational constraints (OpenVLA's 7B forward pass is substantially more expensive), but all measurements use task-relevant visual inputs. Entropy statistics show low variance across frames (std $< 0.02$ for OpenVLA, std $= 0.013$ for $\\pi_{0}$).\n\n\n\\section{Connector Architecture and Token Independence}\n\\label{app:connector_analysis}\n\nThe six-architecture taxonomy (Table~\\ref{tab:model_properties}) spans a continuous spectrum of token independence structures, each associated with the vision-to-LLM connector rather than model scale or action head design.\n\nPixel-shuffle connectors create maximal entanglement. SmolVLA's $4 \\times 4$ spatial folding packs 16 patches into each token by channel concatenation (CV $= 0.314$, the highest in our study). The folding is fixed and irreversible: removing one token eliminates an entire receptive field, and no downstream layer can recover the discarded content. Tokens encode non-overlapping spatial regions with heterogeneous visual content, making every token simultaneously essential and non-redundant.\n\nPure linear projections produce the opposite extreme. $\\pi_{0}$ maps each SigLIP patch through a single linear layer with no cross-token interaction, yielding CV $= 0.038$ and near-maximal entropy (0.959). Tokens are genuinely interchangeable: any subset preserves the same per-patch information density as any other subset of equal size.\n\n$\\pi_{0.5}$ reveals a subtlety that $\\pi_{0}$'s offline-only evaluation conceals. The $\\times\\!\\sqrt{d}$ learned scaling preserves near-uniform norms (CV $= 0.055$), yet the closed-loop response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\\% SR while L2 norm-based removal collapses to 33.4\\%. The 36\\,pp gap arises because L2 ranking in a low-CV distribution selects spatially clustered tokens whose slight norm variations correlate with image regions, destroying the spatial coverage that this architecture requires. Token position analysis confirms this mechanism: at $k{=}0.5$, L2 selection produces a single dominant cluster containing 100\\% of retained tokens with only 78\\% spatial coverage, whereas $k{=}0.7$ yields two clusters with 97\\% in the largest and 100\\% coverage (Appendix~\\ref{app:token_position}).\n\nX-VLA's 12-layer BART encoder~\\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\\,pp), confirming it as an architectural property.\n\nMLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\\% SR under 78\\% pruning).\n\nParameter count does not predict pruning tolerance. Ordered by scale: SmolVLA (450M) $<$ X-VLA (0.9B) $<$ $\\pi_{0}$ (3.3B) $<$ $\\pi_{0.5}$ (4B) $<$ OpenVLA (7B). Ordered by tolerance, SmolVLA remains the minimum, but $\\pi_{0}$ and $\\pi_{0.5}$ at 3.3--4B surpass OpenVLA at 7B, and X-VLA at 0.9B tolerates more aggressive pruning than OpenVLA. The CV spectrum (0.038 to 0.314) tracks connector complexity rather than parameter count across a 16$\\times$ scale range.\n\n\n\\section{CV as Diagnostic Metric: Extended Analysis}\n\\label{app:cv_extended}\n\\label{sec:diagnostic}\n\nToken importance CV correlates with both the tolerance class of a model and the optimal pruning strategy, a correlation that emerges from a single mechanistic principle: CV measures the strength of the importance gradient that scoring methods can exploit.\n\nLow-CV models have near-uniform L2 norms. L2 norm ranking in this regime captures spatial artifacts (slight norm variations that correlate with image position) rather than genuine importance differences. Selection based on these artifacts concentrates retained tokens on spatially correlated patches, destroying the uniform coverage that low-CV architectures depend on. Random selection preserves spatial uniformity by construction. The mechanism predicts that the L2-over-random advantage should grow as CV increases, and the data in Table~\\ref{tab:scaling_law} confirm this. On LIBERO-Object at $k{=}0.5$: $\\Delta = -$36.0\\,pp ($\\pi_{0.5}$, CV $= 0.055$) $\\to$ $-$26.9\\,pp (X-VLA, CV $= 0.151$) $\\to$ $+$3.4\\,pp (OpenVLA, CV $= 0.215$). At $k{=}0.7$, the same ordering holds for $\\pi_{0.5}$ and X-VLA ($-$22.2\\,pp $\\to$ $-$6.5\\,pp); OpenVLA lacks a seed-matched pair at this ratio. The pattern persists across retention ratios, strengthening the interpretation from a coincidence at a single operating point to a structural property of the connector.\n\nOn simple manipulation tasks (Object), high-CV models present a genuine importance gradient where L2 norm ranking aligns with actual information content. OpenVLA (CV $= 0.215$) sits near the crossover on Object: L2 outperforms random by 7.8\\,pp at $k{=}0.9$ where the gradient is most exploitable, shrinking to 3.4\\,pp at $k{=}0.5$ as the proportion of removed tokens exceeds the gradient's discriminative range. On complex multi-step tasks, this advantage diminishes or reverses: OpenVLA Long at $k{=}0.9$ shows Random outperforming L2 by 3.2\\,pp (46.8\\% vs.\\ 43.6\\%), as compositional tasks distribute critical information across tokens with heterogeneous norm profiles (Section~\\ref{sec:analysis}).\n\nExtreme compression introduces a partial reversal. At $k{=}0.3$, $\\pi_{0.5}$'s L2 selection achieves $53.2 \\pm 3.1$\\% SR (2 seeds) vs.\\ random's 36.4\\%. When very few tokens remain, even spatially clustered high-norm tokens provide more signal than a sparse random sample. The V-shaped L2 curve is confirmed across seeds ($\\sigma{=}0.1$\\,pp at the $k{=}0.5$ valley). The reversal does not invalidate the CV diagnostic; it adds a budget-dependent interaction that future work should characterize across more models.\n\nAttention entropy provides a mechanistic supplement that resolves an apparent paradox. SmolVLA's entropy (0.952) is nearly as high as $\\pi_{0}$'s (0.959), yet SmolVLA collapses under any pruning. SmolVLA's tokens are uniformly \\emph{attended} but carry heterogeneous \\emph{content} due to pixel-shuffle folding. Entropy captures how the LLM allocates attention across tokens; CV captures the input-side importance structure. Entropy alone cannot distinguish ``interchangeable'' ($\\pi_{0}$) from ``entangled'' (SmolVLA), but CV separates them cleanly (0.038 vs.\\ 0.314). OpenVLA's progressive entropy sharpening from 0.98 to 0.48 across layers (Figure~\\ref{fig:entropy_layers}) is consistent with a graded regime where the LLM progressively concentrates on higher-importance tokens.\n\n\n\\section{Why Re-Encoding Succeeds: Extended Analysis}\n\\label{app:reencoding_analysis}\n\\label{sec:learned_compression}\n\nLearned re-encoding overcomes pixel-shuffle failure because it breaks the rigid spatial entanglement that the $4 \\times 4$ folding creates. Cross-attention pooling integrates information across receptive field boundaries, redistributing content from the original 128 tokens into $M$ compressed representations no longer tied to fixed spatial blocks.\n\nThe $M{=}128$ passthrough configuration suggests that re-encoding, not compression, is the key factor. Passthrough adds parameters without reducing token count, yet gains 13\\,pp over the baseline (44.8\\% $\\to$ 58.0\\%). The relatively stable M-curve ($M{=}16$: 56.9\\% closely matches $M{=}128$: 58.0\\%, within 1.1\\,pp) shows that once entanglement is broken, token count is secondary.\n\nA parameter-matched MLP adapter (22.14M parameters) achieves 63.4\\% SR at $M{=}32$, statistically indistinguishable from cross-attention ($p = 0.15$). Re-encoding through any learned mapping that integrates across token boundaries suffices; the attention mechanism itself is not essential.\n\nThe remedy is specific to the pathology. VTR succeeds precisely on architectures whose rigid spatial entanglement demands learned redistribution; for token-independent connectors where each patch already carries self-contained information, re-encoding is unnecessary.\n\n\n\\section{Offline Metrics Underestimate Closed-Loop Failure}\n\\label{app:offline_disconnect}\n\\label{sec:metric_disconnect}\n\nOffline evaluation systematically underestimates pruning-induced failure because per-step averages dilute catastrophic single-step events that individually terminate episodes.\n\nX-VLA at $k{=}0.3$ demonstrates the gap directly: offline loss is 1.0014 (near-baseline), yet closed-loop SR drops to $22.0 \\pm 0.9$\\% ($-$77\\,pp). A single gripper inversion (L2 $= 1.02$) is a minor perturbation in average action error but terminates an episode irreversibly. $\\pi_{0}$'s offline loss at $k{=}0.1$ shows a 2.4\\% \\emph{improvement} over the unpruned baseline (offline metrics only; no closed-loop evaluation available), a result that closed-loop evaluation may contradict if similar catastrophic events occur at deployment frequency.\n\n$\\pi_{0.5}$ adds a distinct form of evidence: the 36\\,pp gap between L2 and random removal at $k{=}0.5$ is invisible to any offline metric that averages across token subsets or selection methods. Offline evaluation would report degradation for both methods; only closed-loop evaluation reveals that the \\emph{choice} of pruning strategy, not just the pruning ratio, is associated with whether the model remains functional.\n\n\n\\section{Confounder Analysis}\n\\label{app:confounders}\n\nThe six architectures span three connector families but differ simultaneously in LLM backbone (PaliGemma for $\\pi_{0}$/$\\pi_{0.5}$, Llama-2 for OpenVLA, Florence-2 for X-VLA, SmolLM2 for SmolVLA), preventing clean isolation of the connector effect from backbone differences. The $\\pi_{0}$--OpenVLA comparison (same 256 SigLIP-based tokens, different connector, backbone, and encoder fusion strategy) provides the closest available approximation, but a matched-backbone experiment remains the ideal control. This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation. Token count also varies across models (50 for X-VLA, 128 for SmolVLA, 256 for $\\pi_{0}$/OpenVLA, 768 for $\\pi_{0.5}$); the $\\pi_{0}$--OpenVLA pair controls for this confounder within the CV analysis while still exhibiting the predicted CV-gap relationship.\n\nThe spatial clustering hypothesis for L2 failure on low-CV models is confirmed by token position analysis (Appendix~\\ref{app:token_position}).\n\nOpenVLA main-text results use seed 42 for both L2 and random. Cross-seed (seed 7) random comparison in Table~\\ref{tab:openvla_l2_vs_random} confirms the L2 advantage is seed-independent: the gap ranges from $+$0.8 to $+$8.6\\,pp across retention ratios regardless of random seed.\n\n\n\\section{Token Position Analysis}\n\\label{app:token_position}\n\nTo validate the spatial clustering hypothesis for L2 norm failure on low-CV models, we analyze the spatial distribution of tokens selected by L2 norm ranking on $\\pi_{0.5}$ across three retention ratios.\n\nAt $k{=}0.7$ (538 of 768 tokens retained): DBSCAN clustering identifies 2 spatial clusters, with 97\\% of retained tokens in the largest cluster and 100\\% spatial coverage of the original image grid. The broad coverage explains why L2 selection still achieves 55.0\\% SR at this retention ratio.\n\nAt $k{=}0.5$ (384 tokens retained): a single dominant cluster contains 100\\% of retained tokens with only 78\\% spatial coverage. The complete concentration into one spatial region confirms the clustering hypothesis: L2 norm ranking selects tokens from a contiguous high-norm region while abandoning 22\\% of the spatial field. This is the retention ratio where L2 performance reaches its minimum (33.4\\% SR, the V-shape valley).\n\nAt $k{=}0.3$ (230 tokens retained): 3 clusters emerge, with 86\\% in the largest and 78\\% spatial coverage. The fragmentation into multiple clusters at extreme compression is consistent with the partial L2 recovery observed at this ratio ($53.2 \\pm 3.1$\\% SR): when the budget is very small, L2 selection is forced to sample from multiple spatial regions, partially restoring coverage.\n\nThese results directly confirm that L2 norm ranking on low-CV models introduces spatial bias that degrades performance, and that the severity peaks at intermediate retention ratios where concentration is maximal.\n\n\n\\section{CV Scaling Law: Full Data}\n\\label{app:cv_scaling_table}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{L2 norm vs.\\ random removal at two retention ratios. The importance margin $\\Delta$(L2$-$R) increases monotonically with CV at both $k{=}0.5$ and $k{=}0.7$: low-CV models require random selection (uniform importance $\\rightarrow$ L2 degenerates to spatial clustering), while high-CV models tolerate either strategy on simple tasks (see Section~\\ref{sec:analysis} for task-dependent caveats). Data shown for LIBERO-Object; the monotonic ordering holds across retention ratios despite a 2$\\times$ change in token budget.}\n\\label{tab:scaling_law}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & CV & Tokens & L2 SR (\\%) & Random SR (\\%) & $\\Delta$(L2$-$R) \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$k{=}0.5$ (50\\% retention)}} \\\\\n$\\pi_{0.5}$ & 0.055 & 768 & 33.4 & \\textbf{69.4} & $-$36.0 \\\\\nX-VLA & 0.151 & 50 & 43.4$\\pm$0.8 & \\textbf{70.3}$\\pm$0.9 & $-$26.9 \\\\\nOpenVLA & 0.215 & 256 & \\textbf{39.2} & 35.8 & $+$3.4 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$k{=}0.7$ (70\\% retention)}} \\\\\n$\\pi_{0.5}$ & 0.055 & 768 & 55.0 & \\textbf{74.0} & $-$19.0 \\\\\nX-VLA & 0.151 & 50 & 58.6$\\pm$0.4 & \\textbf{65.1}$\\pm$0.1 & $-$6.5 \\\\\nOpenVLA\\textsuperscript{$\\dagger$} & 0.215 & 256 & -- & -- & -- \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize\\textsuperscript{$\\dagger$}$k{=}0.7$ omitted: no seed-matched L2/Random pair available.}\n\\end{tabular}\n\\end{table}\n\n\n\\section{CV-Strategy Interaction at Extreme Compression}\n\\label{app:cv_strategy_interaction}\n\nThe monotonic CV-gap relationship (Table~\\ref{tab:scaling_law}) holds at $k{=}0.5$ and $k{=}0.7$, but partially reverses at $k{=}0.3$ for $\\pi_{0.5}$. At this extreme budget, L2 norm selection achieves $53.2 \\pm 3.1$\\% SR (2 seeds) vs.\\ random's 36.4\\%, favoring L2 by $\\sim$17\\,pp. The reversal is consistent across both seeds (seed42: 51.0\\%, seed43: 55.4\\%; Table~\\ref{tab:pi05_l2_multiseed}).\n\nThe mechanism is intuitive: when very few tokens remain ($k{=}0.3$ retains 230 of 768 tokens), even spatially clustered high-norm tokens provide more visual signal than a sparse random sample. At intermediate budgets ($k{=}0.5$, 384 tokens), random selection preserves enough spatial coverage to outperform L2's clustered selection; at extreme budgets, coverage from random selection becomes too sparse to be useful, and the concentrated signal from L2 selection dominates.\n\nThe interaction implies that the optimal pruning strategy depends on both CV and the absolute token budget. For low-CV models, the crossover point between random-preferred and L2-preferred regimes lies between $k{=}0.3$ and $k{=}0.5$. Characterizing this crossover across additional models and budgets is left to future work.\n\n\n\\section{Inference Cost-Benefit Analysis}\n\\label{app:cost_benefit}\n\nThe primary deployment benefit of VTR at this model scale is memory, not latency. Reducing from 128 to 32 vision tokens shrinks the KV-cache footprint for the vision portion by 75\\%, a meaningful reduction for memory-constrained robotic hardware where KV-cache size can limit the number of concurrent policy instances or maximum context length.\n\nEnd-to-end inference latency improves only modestly: 154.78\\,ms at $M{=}32$ versus 164.33\\,ms at full token count, a $1.06\\times$ speedup (6\\% reduction). At $M{=}64$: 156.16\\,ms ($1.05\\times$). The gap between token reduction and latency gain reflects SmolVLA's compact size (450M parameters): self-attention over 128 vision tokens is not the inference bottleneck, and the compressor's 22.2M-parameter cross-attention computation partially offsets downstream savings. Token pruning becomes a more compelling latency optimization for VLAs with larger token budgets ($>$256 tokens) or larger backbones (7B+ parameters), where attention cost scales quadratically with sequence length. Whether the training cost (100K steps, 6.5 hours per configuration) is justified depends on deployment context: for VLAs deployed across many tasks, the one-time training cost is amortized; for rapid prototyping, retraining is a barrier.\n\n\\paragraph{Comparison with the official checkpoint.}\nVTR at $M = 32$ ($60.1 \\pm 1.3$\\% over 3 seeds) recovers from 0\\% SR under hard pruning to performance comparable to the official SmolVLA checkpoint (59.2\\%, CI [54.8\\%, 63.4\\%]). However, the difference is not statistically significant (two-sample $t$-test, $p \\approx 0.72$), and the comparison should be interpreted cautiously given different training conditions (batch size 4 vs.\\ 64, single vs.\\ 8 GPUs). The primary contribution of VTR is recovering functional performance where all deletion methods yield 0\\%, not matching the official baseline.\n\n\\subsection{Attention-Based Scoring Methods}\n\\label{app:attention_scoring}\n\\label{app:attention_pruning}\n\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity for residual connections) to approximate cumulative information flow. These methods require a full LLM forward pass and are backbone-specific. We focus on L2 and random in the main text because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\subsection{Attention Entropy as Diagnostic}\n\\label{app:attention_entropy}\n\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention distribution over vision tokens, provides a complementary but less discriminative signal than CV. Three models with qualitatively different pruning behaviors cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness.\n\n\\subsection{Attention-Based Scoring Results}\n\nTable~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{X-VLA success rates (\\%) at $k{=}0.5$ across five scoring methods. Attention-based scoring recovers near-baseline performance across all suites while L2 norm falls below random on every suite. Bold indicates best per suite. \\textsuperscript{*}Best of three attention variants.}\n\\label{tab:attention_pruning}\n\\begin{tabular}{lccccc}\n\\toprule\nSuite & attn\\_last & attn\\_mean & attn\\_rollout & L2 & Random \\\\\n\\midrule\nObject & \\textbf{99.2} & 98.4 & 97.4 & 43.4 & 70.6 \\\\\nSpatial & 88.8 & 91.6 & \\textbf{92.8} & 58.8 & 71.4 \\\\\nLong & 90.2 & 94.0 & \\textbf{94.8} & 45.0 & 61.6 \\\\\nGoal & \\textbf{98.2} & 97.4 & 96.8 & 59.0 & 67.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nL2 norm selection is anti-informative on X-VLA's entangling connector: L2 falls below random on all four suites, with gaps ranging from $-$8.2\\,pp (Goal) to $-$27.2\\,pp (Object). Attention-based scoring recovers near-baseline performance across all suites (${\\geq}$92.8\\%), with rollout peaking at 94.8\\% on Long (seed43 confirms $\\Delta{\\leq}$0.6\\,pp). On Object, all three attention variants achieve ${\\geq}$97.4\\%, far exceeding both L2 (43.4\\%) and random (70.6\\%). The mode ranking reverses across suites: last-layer attention is best on Object (99.2\\%) but worst among attention methods on Spatial (88.8\\%) and Long (90.2\\%), while rollout shows the opposite pattern.\n\nThe L2 failure has a structural explanation. The BART encoder's 12-layer self-attention redistributes information across tokens, equalizing activation magnitudes (CV$\\,{=}\\,$0.151). L2 norms no longer reflect token importance; instead, they select spatially correlated clusters that miss critical information. Goal L2 exhibits non-monotonic behavior ($k{=}0.7$: 53.4\\% $<$ $k{=}0.5$: 59.0\\%), confirming that retaining more L2-selected tokens is actively harmful. Per-task variance under L2 pruning is extreme on Spatial (std$\\,{=}\\,$31.5\\,pp, range 0--92\\%), while attention scoring keeps all tasks above 80\\%. The double dissociation extends to $\\pi_{0.5}$, where attention scoring at $k{=}0.5$ exhibits suite-dependent failure (Table~\\ref{tab:pi05_attention_crosssuite}). On three suites (Goal, Spatial, Long), attention performs within noise of random ($\\pm$3\\,pp). On Object, attention collapses to 37.8\\% ($-$31.6\\,pp vs.\\ random's 69.4\\%), a catastrophic failure unique to tasks requiring spatial discrimination among visually similar alternatives. The linear connector produces an extremely narrow attention score range ($[2{\\times}10^{-6},\\, 3.6{\\times}10^{-3}]$) with systematic position bias favoring early tokens; on Object, this bias selects semantically relevant but spatially uninformative tokens, destroying the fine-grained spatial information needed for target identification.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ attention vs.\\ random at $k{=}0.5$ across LIBERO suites. Attention is neutral on 3/4 suites but catastrophically harmful on Object.}\n\\label{tab:pi05_attention_crosssuite}\n\\begin{tabular}{lccc}\n\\toprule\nSuite & Attention (\\%) & Random (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nGoal & 71.2 & 73.6 & $-$2.4 \\\\\nSpatial & 72.6 & 71.6 & $+$1.0 \\\\\nLong & 49.4 & 46.8 & $+$2.6 \\\\\nObject & 37.8 & 69.4 & $-$31.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table} By contrast, $\\pi_{0.5}$'s L2 norms do reflect importance: on Goal, L2 outperforms random by $+$35.2\\,pp at $k{=}0.85$, decaying to $+$5.4\\,pp at $k{=}0.95$ (log-decay trend across four retention ratios). This yields a connector-dependent scoring reversal: attention is effective on entangling connectors but not token-independent ones, while L2 norm shows the converse (Figure~\\ref{fig:scoring_crossover}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Scoring reversal summary: $\\Delta$ vs.\\ random at $k{=}0.5$, except \\textsuperscript{*}Goal suite across $k \\in [0.85, 0.95]$. Compact view of the pattern shown in Figure~\\ref{fig:scoring_crossover}.}\n\\label{tab:scoring_crossover_summary}\n\\begin{tabular}{lcc}\n\\toprule\n& Attention & L2 norm \\\\\n\\midrule\nEntangling (X-VLA) & Effective ($+$31\\,pp) & Anti-inform.\\ ($-$8 to $-$27\\,pp) \\\\\nToken-indep.\\ ($\\pi_{0.5}$) & Ineffective\\textsuperscript{$\\dagger$} ($-$2 to $-$32\\,pp) & Effective\\textsuperscript{*} ($+$35.2$\\to$$+$5.4\\,pp) \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize\\textsuperscript{$\\dagger$}Neutral on 3/4 suites ($\\pm$3\\,pp); harmful on Object ($-$31.6\\,pp).}\n\\end{tabular}\n\\end{table}\n\n\n\\section{AI Disclosure}\n\\label{app:ai_disclosure}\n\nAI tools assisted code development and manuscript drafting; all scientific claims, experimental designs, and interpretations are the authors' own.",
      "numLines": 439,
      "startLine": 500,
      "totalLines": 938
    }
  }
}
```

</details>

---


### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me compile:

1. All bib entries
2. All citations used in the paper
3. Cross-reference

Let me list all bib entries:

1. abnar2020quantifying - "Quantifying Attention Flow in Transformers" - Abnar, Zuidema - ACL 2020
2. gao2025compressorvla - "Compressor-VLA..." - Gao et al. - arXiv 2511.18950, 2025
3. wang2025specprunevla - "SpecPrune-VLA..." - Wang et al. - arXiv 2509.05614, 2025


4. jiang2026lightvla - "The Better You Learn..." - Jiang et al. - ICRA 2026, arXiv 2509.12594
5. feng2026seewhatmatters - "See What Matters..." - Feng et al. - ICML 2026, arXiv 2605.11817
6. zhang2025sparsevlm - "SparseVLM..." - Zhang et al. - ICML 2025, arXiv 2410.04417
7. khaki2025sparsevila - "SparseVILA..." - Khaki et al. - ICC V 2025, arXiv 2510.17777
8. jabbour2025dontrun - "Don't Run with Scissors..." - Jabbour et al. - arXiv 2510.08464, 2025
9. li2024roboflamingo - "Vision-Language Foundation Models..." - Li et al. - ICLR 2024, arXiv 2311.01378
10. shukor2025smolvla - "SmolVLA..." - Shukor et al. - arXiv 2506.01844, 2025
11. kim2024openvla - "OpenVLA..." - Kim et al. - CoRL 2024
12. brohan2023rt2 - "RT-2..." - Brohan et al. - CoRL 2023
13. black2024pi0 - "π0..." - Black et al. - arXiv 2410.24164

, 2024
14. black2025pi05 - "π0.5..." - Black et al. - CoRL 2025, PMLR vol 305
15. ghosh2024octo - "Octo..." - Octo Model Team - RSS 2024
16. brohan2023rt1 - "RT-1..." - Brohan et al. - RSS 2023
17. chen2024fastv - "An Image is Worth 1/2 Tokens..." - Chen et al. - ECCV 2024, arXiv 2403.06764
18. xu2025vlacache - "VLA-Cache..." - Xu et al. - NeurIPS 2025
19. cheng2026vlaiap - "VLA-IAP..." - Cheng et al. - arXiv 2603.22991, 2026
20. rao

2021dynamicvit - "DynamicViT..." - Rao et al. - NeurIPS 2021
21. bolya2023tome - "Token Merging..." - Bolya et al. - ICLR 2023
22. liang2022evit - "Not All Patches..." - Liang et al. - ICLR 2022
23. liu2023libero - "LIBERO..." - Liu et al. - NeurIPS 2023
24. yang2025efficientvla - "EfficientVLA..." - Yang et al. - arXiv 2506.10100, 2025
25. liu2025vlapruner - "VLA-Pruner..." - Liu et al. - arXiv 2511.16449, 2025
26. shang2024prumerge - "LLa

Continuing bibliography entries... Continuing through the bibliography with entries 38 through 44, covering Kim's work on fine-tuning vision-language-action models, TokenPacker for efficient token processing, X-VLA for cross-modal learning, TinyVLA for lightweight applications, BART for sequence-to-sequence tasks, TokenLearner for attention mechanisms, and starting into Yin's work. Continuing through more recent vision-language and embodied AI papers, including work on efficient vision transformers, improved instruction tuning approaches, and multimodal models that bridge vision and robotics applications. Finishing up the citation list and now checking which ones are actually referenced in the main paper sections. I'm organizing the bibliography references across different sections of the paper—compiling which citations belong in the related work, background, method, experiments, and discussion sections. I need to verify which files are actually included in the main paper by checking main.tex directly. The sections/ folder appears to be older drafts, so I should focus on the files that main.tex actually references: abstract, introduction, related_work, method, experiments, conclusion, limitations, and appendix, with the bibliography coming from references.bib.

Now I'm going through each of these files to extract all the citation keys that are actually used in the compiled paper.

Looking at the introduction more carefully, I see the citations are clustered around specific claims about token reduction techniques for vision transformers and different projection methods for VLAs. The related work section is starting to list citations on similar topics, with some overlap like the vision transformer papers but also new ones appearing. I'm now going through the appendix citations and cross-referencing them against what's actually cited in the paper to identify which bibliography entries are actually used and which might be unused. Continuing through the reference list, checking off papers on vision-language models, token pruning techniques, and foundational architectures like LLaVA and BLIP-2.

Now I'm verifying the citations for zhai2023siglip more carefully—it appears in the appendix results tables but I need to double-check whether it's actually cited in the method section itself. I'm tracking down which bibliography entries are actually cited in the compiled paper versus just sitting in the bib file. So far I've found that yang2024qwen2, lipman2023flow, and oquab2023dinov2 are all in the bibliography but not cited anywhere in the main document—they only appear in background files that aren't included in the final compilation. Now I'm checking the remaining entries to see which ones are similarly unused. I'm continuing through the bibliography, finding more entries that aren't cited in the compiled paper—TokenLearner, AdaViT, SparseViT, and several others including what looks like a duplicate entry for RT-2 from two different sources. There's also an incomplete entry at the end that cuts off.

Now I'm moving on to verify these papers through web search, starting with the ones that are actually cited in the final document and flagging any issues I find along the way.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "0a9cce6b-bf73-4db1-9157-34315ab73366",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018X4e2nZ3EE2YzRVcQ5L9vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20958,
      "cache_read_input_tokens": 79724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20958
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

_source line 54_

Now I have all bib entries and citation contexts. Let me load WebSearch and verify each entry. I'll run multiple verification agents in parallel to cover all entries efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "47820682-a01c-460a-8c23-82f8927d7ff0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018X4e2nZ3EE2YzRVcQ5L9vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20958,
      "cache_read_input_tokens": 79724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20958
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

_source line 55_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SGaYUBqs9PpFumAUjTtrCU`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "cf37a98f-3f7d-48ed-9719-7e7d06eda285",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018X4e2nZ3EE2YzRVcQ5L9vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20958,
      "cache_read_input_tokens": 79724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20958
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

_source line 56 · 2026-05-29T06:51:16.789Z_

<details><summary>↩ Tool result · `toolu_01SGaYUBqs9PpFumAUjTtrCU`</summary>

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
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "4747d520-3204-4599-8e07-3a5bdf26e7e3",
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

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Now I'll launch multiple verification agents in parallel to cover all bib entries. Let me split them into groups and verify each batch.

Let me organize the 62 bib entries into groups for parallel verification. I'll create several agents, each verifying a batch of entries.

Actually, I'll split them into ~6 agents of ~10 entries each to maximize parallelism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "a835f19b-b0b5-44b7-a227-629fe6004c18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyFVwDpqmf2wFz9bsVHa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 100682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6753
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 58_

Launching parallel verification agents for all bib entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "826d88e2-0029-4377-8a6b-97105a782c47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyFVwDpqmf2wFz9bsVHa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 100682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6753
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 59_

<details open><summary>🔧 Tool call — Agent · `toolu_01NFtBS1um2LsdQ5pgEUrZ76`</summary>

```json
{
  "description": "Verify bib entries batch 1",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. abnar2020quantifying: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. Venue: ACL 2020, pages 4190-4197.\n\n2. gao2025compressorvla: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\" by Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing. arXiv:2511.18950, year 2025.\n\n3. wang2025specprunevla: \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\" by Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao. arXiv:2509.05614, year 2025.\n\n4. jiang2026lightvla: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\" by Jiang, Titong et al. Venue: ICRA 2026, arXiv:2509.12594.\n\n5. feng2026seewhatmatters: \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" by Feng, Yixu et al. Venue: ICML 2026, arXiv:2605.11817.\n\n6. zhang2025sparsevlm: \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" by Zhang, Yuan et al. Venue: ICML 2025, arXiv:2410.04417.\n\n7. khaki2025sparsevila: \"SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference\" by Khaki, Samir et al. Venue: ICCV 2025, arXiv:2510.17777.\n\n8. jabbour2025dontrun: \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" by Jabbour, Jason et al. arXiv:2510.08464, year 2025.\n\n9. li2024roboflamingo: \"Vision-Language Foundation Models as Effective Robot Imitators\" by Li, Xinghang et al. Venue: ICLR 2024, arXiv:2311.01378.\n\n10. shukor2025smolvla: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\" by Shukor, Mustafa et al. arXiv:2506.01844, year 2025.\n\nFor each entry, report:\n- Whether paper exists (real or hallucinated)\n- Any author name issues\n- Title accuracy (word-for-word)\n- Year accuracy\n- Venue accuracy\n- arXiv ID accuracy\n- Whether an arXiv preprint has since been accepted to a conference (needs update)\n\nBe thorough and precise. Search for each paper individually."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "9848378a-1097-44d1-a0fb-200447baf6a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyFVwDpqmf2wFz9bsVHa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 100682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6753
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Verify bib entries batch 1",
  "task_type": "local_agent",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. abnar2020quantifying: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. Venue: ACL 2020, pages 4190-4197.\n\n2. gao2025compressorvla: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\" by Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing. arXiv:2511.18950, year 2025.\n\n3. wang2025specprunevla: \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\" by Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao. arXiv:2509.05614, year 2025.\n\n4. jiang2026lightvla: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\" by Jiang, Titong et al. Venue: ICRA 2026, arXiv:2509.12594.\n\n5. feng2026seewhatmatters: \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" by Feng, Yixu et al. Venue: ICML 2026, arXiv:2605.11817.\n\n6. zhang2025sparsevlm: \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" by Zhang, Yuan et al. Venue: ICML 2025, arXiv:2410.04417.\n\n7. khaki2025sparsevila: \"SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference\" by Khaki, Samir et al. Venue: ICCV 2025, arXiv:2510.17777.\n\n8. jabbour2025dontrun: \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" by Jabbour, Jason et al. arXiv:2510.08464, year 2025.\n\n9. li2024roboflamingo: \"Vision-Language Foundation Models as Effective Robot Imitators\" by Li, Xinghang et al. Venue: ICLR 2024, arXiv:2311.01378.\n\n10. shukor2025smolvla: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\" by Shukor, Mustafa et al. arXiv:2506.01844, year 2025.\n\nFor each entry, report:\n- Whether paper exists (real or hallucinated)\n- Any author name issues\n- Title accuracy (word-for-word)\n- Year accuracy\n- Venue accuracy\n- arXiv ID accuracy\n- Whether an arXiv preprint has since been accepted to a conference (needs update)\n\nBe thorough and precise. Search for each paper individually.",
  "uuid": "32420ba4-14ef-498f-88b3-fbf9bb36d9de",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


## Round 1

## Round 1

17 recorded events


### User

_source line 61 · 2026-05-29T06:51:39.309Z_

You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.

Entries to verify:

1. abnar2020quantifying: "Quantifying Attention Flow in Transformers" by Abnar, Samira and Zuidema, Willem. Venue: ACL 2020, pages 4190-4197.

2. gao2025compressorvla: "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation" by Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing. arXiv:2511.18950, year 2025.

3. wang2025specprunevla: "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning" by Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao. arXiv:2509.05614, year 2025.

4. jiang2026lightvla: "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning" by Jiang, Titong et al. Venue: ICRA 2026, arXiv:2509.12594.

5. feng2026seewhatmatters: "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" by Feng, Yixu et al. Venue: ICML 2026, arXiv:2605.11817.

6. zhang2025sparsevlm: "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference" by Zhang, Yuan et al. Venue: ICML 2025, arXiv:2410.04417.

7. khaki2025sparsevila: "SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference" by Khaki, Samir et al. Venue: ICCV 2025, arXiv:2510.17777.

8. jabbour2025dontrun: "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" by Jabbour, Jason et al. arXiv:2510.08464, year 2025.

9. li2024roboflamingo: "Vision-Language Foundation Models as Effective Robot Imitators" by Li, Xinghang et al. Venue: ICLR 2024, arXiv:2311.01378.

10. shukor2025smolvla: "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics" by Shukor, Mustafa et al. arXiv:2506.01844, year 2025.

For each entry, report:
- Whether paper exists (real or hallucinated)
- Any author name issues
- Title accuracy (word-for-word)
- Year accuracy
- Venue accuracy
- arXiv ID accuracy
- Whether an arXiv preprint has since been accepted to a conference (needs update)

Be thorough and precise. Search for each paper individually.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "295668f6-a44f-4002-9cfa-337f4537bd93"
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
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Verify bib entries batch 1",
  "usage": {
    "total_tokens": 15124,
    "tool_uses": 1,
    "duration_ms": 3348
  },
  "last_tool_name": "ToolSearch",
  "uuid": "bb42902f-27f1-4bdf-a9b2-21b3a8766ac0",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for Abnar Zuidema \"Quantifying Attention Flow in Tran…",
  "usage": {
    "total_tokens": 16597,
    "tool_uses": 2,
    "duration_ms": 6731
  },
  "last_tool_name": "WebSearch",
  "uuid": "215e54c3-9aa2-4a74-a84d-994f03bd1398",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for Gao Ye Zhang Qian \"Compressor-VLA: Instruction-Gu…",
  "usage": {
    "total_tokens": 16599,
    "tool_uses": 3,
    "duration_ms": 7676
  },
  "last_tool_name": "WebSearch",
  "uuid": "7566b1c0-9f0b-4c35-a04b-c03e3300ecae",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for Wang Xu Xiang \"SpecPrune-VLA\" arXiv 2509.05614",
  "usage": {
    "total_tokens": 16601,
    "tool_uses": 4,
    "duration_ms": 8141
  },
  "last_tool_name": "WebSearch",
  "uuid": "a54fbad2-d046-416e-b39c-e1e46e19af9f",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for Jiang Titong \"Differentiable Token Pruning\" VLA a…",
  "usage": {
    "total_tokens": 16603,
    "tool_uses": 5,
    "duration_ms": 8674
  },
  "last_tool_name": "WebSearch",
  "uuid": "4aec21fd-0b10-4d71-8ac7-c52fe6fe408b",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for Feng Yixu \"See What Matters\" \"Differentiable Grid…",
  "usage": {
    "total_tokens": 16605,
    "tool_uses": 6,
    "duration_ms": 9320
  },
  "last_tool_name": "WebSearch",
  "uuid": "3ecf75f1-bdc5-45e4-aa45-3edcc23530a1",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017wURu1dhF6hKUPZdNp6HV5`</summary>

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
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "1958aee6-4370-4a99-98a8-40e1b34ba083",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBVQpkHbZ1REsoJSA4FkXt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15113,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15113,
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

_source line 69 · 2026-05-29T06:51:42.664Z_

<details><summary>↩ Tool result · `toolu_017wURu1dhF6hKUPZdNp6HV5`</summary>

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
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "6f43df06-6cc3-4842-9136-fbe4c30d1525"
}
```

</details>

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012iNTPLfxMvoQXAwfh3WGtw`</summary>

```json
{
  "query": "Abnar Zuidema \"Quantifying Attention Flow in Transformers\" ACL 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "c8a596d8-9057-49ce-9b08-beb3e1e0db83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2AJTAzQf5xnPkXArTCVpk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1469,
      "cache_read_input_tokens": 15113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1469,
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


### Tool call

_source line 71_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0122mtKegtoys2znJW9GBYY3`</summary>

```json
{
  "query": "Gao Ye Zhang Qian \"Compressor-VLA: Instruction-Guided Visual Token Compression\" arXiv 2511.18950"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "df1514b7-b3de-43e5-bb8e-41be23a7cacf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2AJTAzQf5xnPkXArTCVpk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1469,
      "cache_read_input_tokens": 15113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1469,
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


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019JbfpFZQAU3mZvhDd4KggK`</summary>

```json
{
  "query": "Wang Xu Xiang \"SpecPrune-VLA\" arXiv 2509.05614"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "896262fb-86af-4d04-9f55-99b5d2c3411e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2AJTAzQf5xnPkXArTCVpk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1469,
      "cache_read_input_tokens": 15113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1469,
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


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014PcEbtUqgsnsMVpSeP6oMk`</summary>

```json
{
  "query": "Jiang Titong \"Differentiable Token Pruning\" VLA arXiv 2509.12594"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "88dd8a4c-bf69-4730-8a68-959ee2d71f62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2AJTAzQf5xnPkXArTCVpk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1469,
      "cache_read_input_tokens": 15113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1469,
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


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XrY54i6dNgLqUiTA3F5zxQ`</summary>

```json
{
  "query": "Feng Yixu \"See What Matters\" \"Differentiable Grid Sample Pruning\" VLA arXiv 2605.11817"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "db707d79-7615-4116-b849-332d85df5ce2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2AJTAzQf5xnPkXArTCVpk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1469,
      "cache_read_input_tokens": 15113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1469,
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

_source line 75 · 2026-05-29T06:51:51.459Z_

<details><summary>↩ Tool result · `toolu_012iNTPLfxMvoQXAwfh3WGtw`</summary>

```text
Web search results for query: "Abnar Zuidema "Quantifying Attention Flow in Transformers" ACL 2020"

Links: [{"title":"Quantifying Attention Flow in Transformers - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.385/"},{"title":"Quantifying Attention Flow in Transformers","url":"https://notes-vault.pages.dev/Scientific-Literature-References/literature-notes/@abnarQuantifyingAttentionFlow2020"},{"title":"Quantifying Attention Flow in Transformers | MYRIAD","url":"https://creatis-myriad.github.io/2022/07/07/AttentionRollout.html"},{"title":"UvA-DARE (Digital Academic Repository)","url":"https://pure.uva.nl/ws/files/178487922/2020.acl-main.385.pdf"},{"title":"Attention Flow - AmsterdamNLP","url":"https://amsterdamnlp.github.io/blog/attentionflow/"},{"title":"[PDF] Quantifying Attention Flow in Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Attention-Flow-in-Transformers-Abnar-Zuidema/76a9f336481b39515d6cea2920696f11fb686451"},{"title":"dblp: Quantifying Attention Flow in Transformers.","url":"https://dblp.org/rec/conf/acl/AbnarZ20.html"},{"title":"ACL2020: Quantifying Attention Flow in Transformers","url":"https://virtual.acl2020.org/paper_main.385.html"},{"title":"Quantifying Attention Flow in Transformers","url":"https://aclanthology.org/2020.acl-main.385.pdf"},{"title":"(PDF) Quantifying Attention Flow in Transformers","url":"https://www.researchgate.net/publication/341148976_Quantifying_Attention_Flow_in_Transformers"}]

I found the paper you're looking for. Here's what I found:

The paper "Quantifying Attention Flow in Transformers" was authored by Samira Abnar and Willem Zuidema in 2020 and published in the Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 4190–4197.

The paper addresses how in the Transformer model, self-attention combines information from attended embeddings into the representation of the focal embedding in the next layer. Across layers of the Transformer, information originating from different tokens gets increasingly mixed, which makes attention weights unreliable as explanations probes.

The paper proposes two methods for approximating the attention to input tokens given attention weights: attention rollout and attention flow, as post hoc methods when using attention weights as the relative relevance of the input tokens.

The paper has garnered more than 250 citations in 2 years.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d3106caf-5dcb-48a8-aad1-a08f1be46073"
}
```

</details>

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Agent · `toolu_01KK5JZyb7hqmGS5wtjs38Kf`</summary>

```json
{
  "description": "Verify bib entries batch 2",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. kim2024openvla: \"OpenVLA: An Open-Source Vision-Language-Action Model\" by Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others. Venue: CoRL 2024 (8th Conference on Robot Learning).\n\n2. brohan2023rt2: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Brohan, Anthony and Brown, Noah and Carbajal, Justice and others. Venue: CoRL 2023 (7th Conference on Robot Learning).\n\n3. black2024pi0: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" by Black, Kevin and Brown, Noah and Driess, Danny and others. arXiv:2410.24164, year 2024.\n\n4. black2025pi05: \"π0.5: a Vision-Language-Action Model with Open-World Generalization\" by Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others. Venue: CoRL 2025, PMLR volume 305, pages 17-40. arXiv:2504.16054.\n\n5. ghosh2024octo: \"Octo: An Open-Source Generalist Robot Policy\" by Octo Model Team and Ghosh, Dibya and others. Venue: RSS 2024.\n\n6. brohan2023rt1: \"RT-1: Robotics Transformer for Real-World Control at Scale\" by Brohan, Anthony and Brown, Noah and others. Venue: RSS 2023.\n\n7. chen2024fastv: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\" by Chen, Liang et al. Venue: ECCV 2024, arXiv:2403.06764.\n\n8. xu2025vlacache: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" by Xu, Siyu et al. Venue: NeurIPS 2025.\n\n9. cheng2026vlaiap: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\" by Cheng, Jintao et al. arXiv:2603.22991, year 2026.\n\n10. rao2021dynamicvit: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\" by Rao, Yongming et al. Venue: NeurIPS 2021.\n\nFor each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "57b38984-b2f3-44cd-94d1-f553e8cd422d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyFVwDpqmf2wFz9bsVHa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 100682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6753
      },
      "output_tokens": 32,
      "service_tier": "standard",
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
  "subtype": "task_started",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Verify bib entries batch 2",
  "task_type": "local_agent",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. kim2024openvla: \"OpenVLA: An Open-Source Vision-Language-Action Model\" by Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others. Venue: CoRL 2024 (8th Conference on Robot Learning).\n\n2. brohan2023rt2: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Brohan, Anthony and Brown, Noah and Carbajal, Justice and others. Venue: CoRL 2023 (7th Conference on Robot Learning).\n\n3. black2024pi0: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" by Black, Kevin and Brown, Noah and Driess, Danny and others. arXiv:2410.24164, year 2024.\n\n4. black2025pi05: \"π0.5: a Vision-Language-Action Model with Open-World Generalization\" by Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others. Venue: CoRL 2025, PMLR volume 305, pages 17-40. arXiv:2504.16054.\n\n5. ghosh2024octo: \"Octo: An Open-Source Generalist Robot Policy\" by Octo Model Team and Ghosh, Dibya and others. Venue: RSS 2024.\n\n6. brohan2023rt1: \"RT-1: Robotics Transformer for Real-World Control at Scale\" by Brohan, Anthony and Brown, Noah and others. Venue: RSS 2023.\n\n7. chen2024fastv: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\" by Chen, Liang et al. Venue: ECCV 2024, arXiv:2403.06764.\n\n8. xu2025vlacache: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" by Xu, Siyu et al. Venue: NeurIPS 2025.\n\n9. cheng2026vlaiap: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\" by Cheng, Jintao et al. arXiv:2603.22991, year 2026.\n\n10. rao2021dynamicvit: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\" by Rao, Yongming et al. Venue: NeurIPS 2021.\n\nFor each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences.",
  "uuid": "3c024a6e-999f-429d-84e2-10c6718b352c",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


## Round 2

## Round 2

40 recorded events


### User

_source line 78 · 2026-05-29T06:51:52.832Z_

You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.

Entries to verify:

1. kim2024openvla: "OpenVLA: An Open-Source Vision-Language-Action Model" by Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others. Venue: CoRL 2024 (8th Conference on Robot Learning).

2. brohan2023rt2: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" by Brohan, Anthony and Brown, Noah and Carbajal, Justice and others. Venue: CoRL 2023 (7th Conference on Robot Learning).

3. black2024pi0: "π0: A Vision-Language-Action Flow Model for General Robot Control" by Black, Kevin and Brown, Noah and Driess, Danny and others. arXiv:2410.24164, year 2024.

4. black2025pi05: "π0.5: a Vision-Language-Action Model with Open-World Generalization" by Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others. Venue: CoRL 2025, PMLR volume 305, pages 17-40. arXiv:2504.16054.

5. ghosh2024octo: "Octo: An Open-Source Generalist Robot Policy" by Octo Model Team and Ghosh, Dibya and others. Venue: RSS 2024.

6. brohan2023rt1: "RT-1: Robotics Transformer for Real-World Control at Scale" by Brohan, Anthony and Brown, Noah and others. Venue: RSS 2023.

7. chen2024fastv: "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models" by Chen, Liang et al. Venue: ECCV 2024, arXiv:2403.06764.

8. xu2025vlacache: "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching" by Xu, Siyu et al. Venue: NeurIPS 2025.

9. cheng2026vlaiap: "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models" by Cheng, Jintao et al. arXiv:2603.22991, year 2026.

10. rao2021dynamicvit: "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification" by Rao, Yongming et al. Venue: NeurIPS 2021.

For each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "82441c1f-753b-4951-a8e2-89667c1f8483"
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
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Verify bib entries batch 2",
  "usage": {
    "total_tokens": 15001,
    "tool_uses": 1,
    "duration_ms": 3133
  },
  "last_tool_name": "ToolSearch",
  "uuid": "756088e2-5b91-4c9a-969a-e03b3b8848bb",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for OpenVLA Open-Source Vision-Language-Action Model …",
  "usage": {
    "total_tokens": 16465,
    "tool_uses": 2,
    "duration_ms": 6342
  },
  "last_tool_name": "WebSearch",
  "uuid": "31ada81f-a855-4660-aa68-930eef23db0e",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for Zhang Yuan \"SparseVLM: Visual Token Sparsificatio…",
  "usage": {
    "total_tokens": 20798,
    "tool_uses": 7,
    "duration_ms": 20028
  },
  "last_tool_name": "WebSearch",
  "uuid": "282be730-c810-458a-ae21-8059237051b7",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for RT-2 Vision-Language-Action Models Transfer Web K…",
  "usage": {
    "total_tokens": 16467,
    "tool_uses": 3,
    "duration_ms": 6825
  },
  "last_tool_name": "WebSearch",
  "uuid": "6de0557e-e54f-4be7-8222-a00d9bb6acdd",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for π0 pi0 Vision-Language-Action Flow Model General …",
  "usage": {
    "total_tokens": 16469,
    "tool_uses": 4,
    "duration_ms": 7792
  },
  "last_tool_name": "WebSearch",
  "uuid": "1ba560f1-b704-4860-a01b-d01ac0beae87",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 84_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for Khaki Samir \"SparseVILA: Decoupled Visual Sparsit…",
  "usage": {
    "total_tokens": 20799,
    "tool_uses": 8,
    "duration_ms": 21453
  },
  "last_tool_name": "WebSearch",
  "uuid": "6ae25851-00e2-4c46-80f5-c5c4bcd29ac5",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for π0.5 pi0.5 Vision-Language-Action Open-World Gene…",
  "usage": {
    "total_tokens": 16471,
    "tool_uses": 5,
    "duration_ms": 8276
  },
  "last_tool_name": "WebSearch",
  "uuid": "4d331df8-b2c1-4df6-aa28-0c16740f1a9b",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for Octo Open-Source Generalist Robot Policy Ghosh RS…",
  "usage": {
    "total_tokens": 16473,
    "tool_uses": 6,
    "duration_ms": 8736
  },
  "last_tool_name": "WebSearch",
  "uuid": "d80b0205-6f19-4346-9301-50d9f0ecf401",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for Jabbour Jason \"Don't Run with Scissors\" pruning V…",
  "usage": {
    "total_tokens": 20800,
    "tool_uses": 9,
    "duration_ms": 22486
  },
  "last_tool_name": "WebSearch",
  "uuid": "ab6898e4-a3cd-4de7-8113-2781b99f3e75",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 88_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for RT-1 Robotics Transformer Real-World Control Scal…",
  "usage": {
    "total_tokens": 16475,
    "tool_uses": 7,
    "duration_ms": 9230
  },
  "last_tool_name": "WebSearch",
  "uuid": "1b489777-bce0-4dfb-b004-a17e701fcd30",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for \"An Image is Worth 1/2 Tokens After Layer 2\" Fast…",
  "usage": {
    "total_tokens": 16477,
    "tool_uses": 8,
    "duration_ms": 9706
  },
  "last_tool_name": "WebSearch",
  "uuid": "74917f20-77b8-4a91-9b05-f66dd22cd972",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for VLA-Cache Efficient Vision-Language-Action Manipu…",
  "usage": {
    "total_tokens": 16479,
    "tool_uses": 9,
    "duration_ms": 10191
  },
  "last_tool_name": "WebSearch",
  "uuid": "ee9ab886-784b-4c75-80a4-9ffbb864965b",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for VLA-IAP Training-Free Visual Token Pruning Intera…",
  "usage": {
    "total_tokens": 16481,
    "tool_uses": 10,
    "duration_ms": 10632
  },
  "last_tool_name": "WebSearch",
  "uuid": "8d284869-07ff-4011-a572-4fae86d9fd40",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for DynamicViT Efficient Vision Transformers Dynamic …",
  "usage": {
    "total_tokens": 16483,
    "tool_uses": 11,
    "duration_ms": 10894
  },
  "last_tool_name": "WebSearch",
  "uuid": "e6a7fb0b-55d8-4725-9c5c-de0a33fcf55c",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for Li Xinghang \"Vision-Language Foundation Models as…",
  "usage": {
    "total_tokens": 20801,
    "tool_uses": 10,
    "duration_ms": 24472
  },
  "last_tool_name": "WebSearch",
  "uuid": "2c8e102a-0825-43f5-a1b3-ecd59f6baceb",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for Shukor Mustafa \"SmolVLA\" arXiv 2506.01844",
  "usage": {
    "total_tokens": 20802,
    "tool_uses": 11,
    "duration_ms": 24564
  },
  "last_tool_name": "WebSearch",
  "uuid": "4df34866-2b87-4043-a4aa-a134040a5dce",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### Tool result

_source line 95 · 2026-05-29T06:51:54.171Z_

<details><summary>↩ Tool result · `toolu_0122mtKegtoys2znJW9GBYY3`</summary>

```text
Web search results for query: "Gao Ye Zhang Qian "Compressor-VLA: Instruction-Guided Visual Token Compression" arXiv 2511.18950"

Links: [{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"Top-Down Compression: Revisit Efficient Vision Token Projection for Visual Instruction Tuning","url":"https://arxiv.org/pdf/2505.11945"}]

I found the paper you're looking for! Here are the details:

**Title:** Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation

**Authors:** Juntao Gao, Feiyang Ye, Jing Zhang, and Wenjing Qian from Beijing University of Technology and LiAuto Inc.

**arXiv ID:** 2511.18950 (submitted November 24, 2025)

**Summary:** The paper proposes Compressor-VLA, a hybrid instruction-conditioned token compression framework for efficient, task-oriented compression of visual information in VLA (Vision-Language-Action) models. The framework consists of two modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details.

**Key Results:** Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline.

The paper is available on arXiv at https://arxiv.org/abs/2511.18950


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "87d9ee7d-30be-44e7-946c-587742f11f36"
}
```

</details>

---


### Tool result

_source line 96 · 2026-05-29T06:51:54.287Z_

<details><summary>↩ Tool result · `toolu_019JbfpFZQAU3mZvhDd4KggK`</summary>

```text
Web search results for query: "Wang Xu Xiang "SpecPrune-VLA" arXiv 2509.05614"

Links: [{"title":"[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/abs/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"SpecPrune-VLA: A New Pruning Method for VLA Models","url":"https://www.linkedin.com/posts/morris-lee-phd_ainewsclips-ai-ml-activity-7371202929288179713-_ZCm"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | Request PDF","url":"https://www.researchgate.net/publication/395354566_SpecPrune-VLA_Accelerating_Vision-Language-Action_Models_via_Action-Aware_Self-Speculative_Pruning"}]

I found the paper! Here are the search results for the arXiv paper:

**Title:** SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning

**Authors:** Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai

**arXiv ID:** 2509.05614

**Summary:**

The paper proposes SpecPrune-VLA, a training-free, two-level pruning method with heuristic control. It includes: (1) Action-Level Static Pruning that leverages global history and local attention to statically reduce visual tokens per action; (2) Layer-Level Dynamic Pruning that prunes tokens adaptively per layer based on layer-wise importance; and (3) a Lightweight Action-Aware Controller that classifies actions as coarse- or fine-grained by speed and adjusts pruning aggressiveness accordingly.

**Key Results:**

SpecPrune-VLA achieves up to 1.57× speedup in the LIBERO simulation benchmark and an average speedup of 1.70× in real-world robotic tasks, with negligible degradation in task success rate.

The paper addresses the limitation that existing methods focus on local information from the current action step and ignore the global context, but the authors propose that token selection should combine local information with global context by leveraging spatial-temporal consistency observed in VLA tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "4aa25acd-e1ea-4550-b7c7-7c9a9facbb4f"
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-29T06:51:54.310Z_

<details><summary>↩ Tool result · `toolu_014PcEbtUqgsnsMVpSeP6oMk`</summary>

```text
Web search results for query: "Jiang Titong "Differentiable Token Pruning" VLA arXiv 2509.12594"

Links: [{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"LightVLA","url":"https://liauto-research.github.io/LightVLA/"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/html/2605.11817"},{"title":"[2605.11817] See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/abs/2605.11817"}]

I found the paper you're looking for. Here's the information:

The paper "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning" is authored by Titong Jiang and others, and presents LightVLA, a differentiable token pruning framework for vision-language-action (VLA) models.

**Key Details:**

- **arXiv ID:** 2509.12594
- **Title:** The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning
- **Main Focus:** While VLA models can execute real-world robotic tasks, their deployment on resource-constrained platforms is bottlenecked by heavy attention-based computation over visual tokens. LightVLA addresses this through adaptive, performance-driven pruning of visual tokens using dynamic queries to evaluate token importance and Gumbel softmax for differentiable token selection.

- **Key Results:** LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.9% improvement in task success rate.

- **Notable Features:** LightVLA requires no heuristic "magic numbers" and introduces no additional trainable parameters, making it compatible with modern inference frameworks.

The project website is available at https://liauto-research.github.io/LightVLA/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "1332b416-3046-45d4-a223-428d53db9646"
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-29T06:51:55.141Z_

<details><summary>↩ Tool result · `toolu_01XrY54i6dNgLqUiTA3F5zxQ`</summary>

```text
Web search results for query: "Feng Yixu "See What Matters" "Differentiable Grid Sample Pruning" VLA arXiv 2605.11817"

Links: [{"title":"[2605.11817] See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/abs/2605.11817"},{"title":"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/html/2605.11817"},{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"}]

I found the paper you're looking for! Here are the search results:

The paper "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" addresses the fact that Vision-Language-Action (VLA) models have shown promise in robotics manipulation, yet their high computational cost hinders real-time deployment.

The work identifies that existing token pruning methods suffer from a fundamental trade-off where aggressive compression inevitably discards critical geometric details like contact points, leading to severe performance degradation and limiting achievable compression rates.

To address this, the authors propose the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA. By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information.

The paper was published on arXiv as 2605.11817 approximately 2 weeks ago and has also been presented as an ICML poster.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "39250aec-901f-49aa-a4d3-f661097895e4"
}
```

</details>

---


### Tool call

_source line 99_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VY7wpy9JYWAKwu4Tha23fA`</summary>

```json
{
  "query": "Zhang Yuan \"SparseVLM: Visual Token Sparsification\" arXiv 2410.04417"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "9eda2472-9d08-41f6-ab3b-3a4916c32c0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ys5qXBFHMGwcYgJSA8QN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4193,
      "cache_read_input_tokens": 16582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4193,
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


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QJefApza5iiHkcijNoKXG6`</summary>

```json
{
  "query": "Khaki Samir \"SparseVILA: Decoupled Visual Sparsity\" arXiv 2510.17777"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "c3eb3dd1-9ac2-4ea8-9e31-531cd12ef0f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ys5qXBFHMGwcYgJSA8QN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4193,
      "cache_read_input_tokens": 16582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4193,
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


### Tool call

_source line 101_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D9EyCdFcnududFBfEsSsHK`</summary>

```json
{
  "query": "Jabbour Jason \"Don't Run with Scissors\" pruning VLA arXiv 2510.08464"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "8590510c-3a9e-4d5e-925e-37288fe7b478",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ys5qXBFHMGwcYgJSA8QN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4193,
      "cache_read_input_tokens": 16582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4193,
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


### Tool call

_source line 102_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U1HjvvAEG3V6JMSqWgJ4dz`</summary>

```json
{
  "query": "Li Xinghang \"Vision-Language Foundation Models as Effective Robot Imitators\" RoboFlamingo arXiv 2311.01378"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d5c7858e-9f87-4854-aae2-2ccb607a2415",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ys5qXBFHMGwcYgJSA8QN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4193,
      "cache_read_input_tokens": 16582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4193,
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


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DK4V3Tnkdqcrtm6Ke7KJHy`</summary>

```json
{
  "query": "Shukor Mustafa \"SmolVLA\" arXiv 2506.01844"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "cbf1942a-0ec0-45b7-a9f1-aa9f0637400f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ys5qXBFHMGwcYgJSA8QN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4193,
      "cache_read_input_tokens": 16582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4193,
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


### Tool call

_source line 104_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01R4vZBdmFy4J5v45kQbZnjh`</summary>

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
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5ece2d34-2ef9-4ee7-972d-5577a4dd9b4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CTDdVFqY5Q32ZWkehEZH4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6728,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6728,
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

_source line 105 · 2026-05-29T06:51:55.971Z_

<details><summary>↩ Tool result · `toolu_01R4vZBdmFy4J5v45kQbZnjh`</summary>

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
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d49d038e-792e-4a8e-b7d4-7d415fbe1651"
}
```

</details>

---


### Tool call

_source line 106_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ERonvou2v4NbbjZhbNJ1WZ`</summary>

```json
{
  "query": "OpenVLA Open-Source Vision-Language-Action Model Kim Pertsch Karamcheti CoRL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "1791b2df-8536-4367-9dee-e8a050cadb72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq4G4v659gXDPHCRiM5P65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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


### Tool call

_source line 107_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Q8QCLh3PZxqtHveu4ZYNg`</summary>

```json
{
  "query": "RT-2 Vision-Language-Action Models Transfer Web Knowledge Robotic Control Brohan CoRL 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "24439039-b208-4e66-8131-7fae9ad5e4df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq4G4v659gXDPHCRiM5P65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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


### Tool call

_source line 108_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FCVWnVFrGkHMrezEEXmLqe`</summary>

```json
{
  "query": "π0 pi0 Vision-Language-Action Flow Model General Robot Control Black arXiv 2410.24164"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "38b9df9c-5853-4dfc-beb3-c0e36cc60499",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq4G4v659gXDPHCRiM5P65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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


### Tool call

_source line 109_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ydNGaqfAH1oUqbpXxzLSn`</summary>

```json
{
  "query": "π0.5 pi0.5 Vision-Language-Action Open-World Generalization Black arXiv 2504.16054"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "fd3c583b-5cbb-4654-a554-0996a7ab65ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq4G4v659gXDPHCRiM5P65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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


### Tool call

_source line 110_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012t2cjfdSKuDhz6kCyaNYWL`</summary>

```json
{
  "query": "Octo Open-Source Generalist Robot Policy Ghosh RSS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5c391edf-9069-45e5-8c0a-f92fc0552f4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq4G4v659gXDPHCRiM5P65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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


### Tool call

_source line 111_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KMY8xzAW61zGG1WFCDwKRa`</summary>

```json
{
  "query": "RT-1 Robotics Transformer Real-World Control Scale Brohan RSS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "51282c1b-ffa7-4db1-a370-24c5b0d0c3f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq4G4v659gXDPHCRiM5P65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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


### Tool call

_source line 112_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bkat4VHQHCxj6nMFYxfAez`</summary>

```json
{
  "query": "\"An Image is Worth 1/2 Tokens After Layer 2\" FastV Chen ECCV 2024 arXiv 2403.06764"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "6c915958-f65f-4f85-bb02-a9743c90df22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq4G4v659gXDPHCRiM5P65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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


### Tool call

_source line 113_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FNQZjnpHSss6iR8ERHCUoh`</summary>

```json
{
  "query": "VLA-Cache Efficient Vision-Language-Action Manipulation Adaptive Token Caching Xu NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "ce34f28f-4d11-4c41-903f-74a967726397",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq4G4v659gXDPHCRiM5P65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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


### Tool call

_source line 114_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014cGutaUmXAotUmeAfyYQQz`</summary>

```json
{
  "query": "VLA-IAP Training-Free Visual Token Pruning Interaction Alignment Cheng arXiv 2603.22991"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "db9112cd-4796-414a-81a3-3ed667e2c591",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq4G4v659gXDPHCRiM5P65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wn8ontxx1DjnFuBXBterkA`</summary>

```json
{
  "query": "DynamicViT Efficient Vision Transformers Dynamic Token Sparsification Rao NeurIPS 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "e1934fea-a049-4681-b3de-48dfce65d1ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq4G4v659gXDPHCRiM5P65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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


### Tool call

_source line 116_

<details open><summary>🔧 Tool call — Agent · `toolu_01KKaDBJv4mnT99dsNx1Wg5z`</summary>

```json
{
  "description": "Verify bib entries batch 3",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. bolya2023tome: \"Token Merging: Your ViT But Faster\" by Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy. Venue: ICLR 2023.\n\n2. liang2022evit: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" by Liang, Youwei et al. Venue: ICLR 2022.\n\n3. liu2023libero: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\" by Liu, Bo et al. Venue: NeurIPS 2023.\n\n4. yang2025efficientvla: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\" by Yang, Yantai et al. arXiv:2506.10100, year 2025.\n\n5. liu2025vlapruner: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\" by Liu, Ziyan et al. arXiv:2511.16449, year 2025.\n\n6. shang2024prumerge: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\" by Shang, Yuzhang et al. Listed as ICCV 2025, key year 2024. arXiv:2403.15388 (check this - the bib doesn't have arXiv ID).\n\n7. liu2023llava: \"Visual Instruction Tuning\" by Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae. Venue: NeurIPS 2023.\n\n8. shi2016subpixel: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" by Shi, Wenzhe et al. Venue: CVPR 2016.\n\n9. li2023blip2: \"BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models\" by Li, Junnan et al. Venue: ICML 2023.\n\n10. alayrac2022flamingo: \"Flamingo: a Visual Language Model for Few-Shot Learning\" by Alayrac, Jean-Baptiste et al. Venue: NeurIPS 2022.\n\nFor each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "4a1b5c60-b7a7-4270-acf1-c52b4ba2484b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyFVwDpqmf2wFz9bsVHa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 100682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6753
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 117_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Verify bib entries batch 3",
  "task_type": "local_agent",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. bolya2023tome: \"Token Merging: Your ViT But Faster\" by Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy. Venue: ICLR 2023.\n\n2. liang2022evit: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" by Liang, Youwei et al. Venue: ICLR 2022.\n\n3. liu2023libero: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\" by Liu, Bo et al. Venue: NeurIPS 2023.\n\n4. yang2025efficientvla: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\" by Yang, Yantai et al. arXiv:2506.10100, year 2025.\n\n5. liu2025vlapruner: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\" by Liu, Ziyan et al. arXiv:2511.16449, year 2025.\n\n6. shang2024prumerge: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\" by Shang, Yuzhang et al. Listed as ICCV 2025, key year 2024. arXiv:2403.15388 (check this - the bib doesn't have arXiv ID).\n\n7. liu2023llava: \"Visual Instruction Tuning\" by Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae. Venue: NeurIPS 2023.\n\n8. shi2016subpixel: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" by Shi, Wenzhe et al. Venue: CVPR 2016.\n\n9. li2023blip2: \"BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models\" by Li, Junnan et al. Venue: ICML 2023.\n\n10. alayrac2022flamingo: \"Flamingo: a Visual Language Model for Few-Shot Learning\" by Alayrac, Jean-Baptiste et al. Venue: NeurIPS 2022.\n\nFor each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences.",
  "uuid": "eeefd36e-d780-4ff4-8e83-ef69d5570227",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


## Round 3

## Round 3

33 recorded events


### User

_source line 118 · 2026-05-29T06:52:04.810Z_

You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.

Entries to verify:

1. bolya2023tome: "Token Merging: Your ViT But Faster" by Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy. Venue: ICLR 2023.

2. liang2022evit: "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" by Liang, Youwei et al. Venue: ICLR 2022.

3. liu2023libero: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" by Liu, Bo et al. Venue: NeurIPS 2023.

4. yang2025efficientvla: "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models" by Yang, Yantai et al. arXiv:2506.10100, year 2025.

5. liu2025vlapruner: "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference" by Liu, Ziyan et al. arXiv:2511.16449, year 2025.

6. shang2024prumerge: "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models" by Shang, Yuzhang et al. Listed as ICCV 2025, key year 2024. arXiv:2403.15388 (check this - the bib doesn't have arXiv ID).

7. liu2023llava: "Visual Instruction Tuning" by Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae. Venue: NeurIPS 2023.

8. shi2016subpixel: "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network" by Shi, Wenzhe et al. Venue: CVPR 2016.

9. li2023blip2: "BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models" by Li, Junnan et al. Venue: ICML 2023.

10. alayrac2022flamingo: "Flamingo: a Visual Language Model for Few-Shot Learning" by Alayrac, Jean-Baptiste et al. Venue: NeurIPS 2022.

For each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "21b4197e-3460-4176-80e1-a6a7be69bafb"
}
```

</details>

---


### System

_source line 119_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Verify bib entries batch 3",
  "usage": {
    "total_tokens": 14994,
    "tool_uses": 1,
    "duration_ms": 3247
  },
  "last_tool_name": "ToolSearch",
  "uuid": "a80c03ae-4946-46b5-bb1f-3bd0ac618e14",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 120_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for Bolya \"Token Merging: Your ViT But Faster\" ICLR 2…",
  "usage": {
    "total_tokens": 16468,
    "tool_uses": 2,
    "duration_ms": 6306
  },
  "last_tool_name": "WebSearch",
  "uuid": "640edda5-7d50-4189-8b83-1e84bf2a78ee",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 121_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for Liang Youwei \"Not All Patches are What You Need\" …",
  "usage": {
    "total_tokens": 16470,
    "tool_uses": 3,
    "duration_ms": 7277
  },
  "last_tool_name": "WebSearch",
  "uuid": "fd012f08-1633-495f-b605-5b0139fb85d4",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 122_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for Liu Bo \"LIBERO: Benchmarking Knowledge Transfer f…",
  "usage": {
    "total_tokens": 16472,
    "tool_uses": 4,
    "duration_ms": 7677
  },
  "last_tool_name": "WebSearch",
  "uuid": "119a35b1-4d6a-4b4d-a3ac-f0de102742c4",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 123_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for Yang Yantai \"EfficientVLA\" arXiv 2506.10100 2025",
  "usage": {
    "total_tokens": 16474,
    "tool_uses": 5,
    "duration_ms": 8201
  },
  "last_tool_name": "WebSearch",
  "uuid": "6e6bb254-0489-4fa4-bcc3-74ab9b740971",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 124_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for Liu Ziyan \"VLA-Pruner\" arXiv 2511.16449 2025",
  "usage": {
    "total_tokens": 16476,
    "tool_uses": 6,
    "duration_ms": 8209
  },
  "last_tool_name": "WebSearch",
  "uuid": "eca6abd4-a31a-4388-83d9-d820fa143eab",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 125_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for SparseVLM Zhang Yuan ICML 2025 accepted venue con…",
  "usage": {
    "total_tokens": 25282,
    "tool_uses": 12,
    "duration_ms": 35745
  },
  "last_tool_name": "WebSearch",
  "uuid": "f9e8d6d7-638d-4aa9-80d9-1e2c28ddc86c",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### Tool result

_source line 126 · 2026-05-29T06:52:07.293Z_

<details><summary>↩ Tool result · `toolu_01QJefApza5iiHkcijNoKXG6`</summary>

```text
Web search results for query: "Khaki Samir "SparseVILA: Decoupled Visual Sparsity" arXiv 2510.17777"

Links: [{"title":"[2510.17777] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/abs/2510.17777"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/html/2510.17777"},{"title":"[Literature Review] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://www.themoonlight.io/en/review/sparsevila-decoupling-visual-sparsity-for-efficient-vlm-inference"},{"title":"2025-10-21 SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"ICCV Poster SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://iccv.thecvf.com/virtual/2025/poster/1739"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efﬁcient VLM Inference Samir Khaki4","url":"https://www.openaccess.thecvf.com/content/ICCV2025/papers/Khaki_SparseVILA_Decoupling_Visual_Sparsity_for_Efficient_VLM_Inference_ICCV_2025_paper.pdf"},{"title":"SparseVILA-R1: Decoupling Visual Sparsity for Efficient VLM Reasoning","url":"https://openreview.net/pdf/6597aa03e44118e07d8bbbe91433da250c6beb33.pdf"}]

Based on the search results, I found the paper you're looking for:

SparseVILA is a new paradigm for efficient VLM inference that decouples visual sparsity across the prefilling and decoding stages. SparseVILA distributes sparsity across stages by pruning redundant visual tokens during prefill and retrieving only query-relevant tokens during decoding.

This decoupled design matches leading prefill pruning methods while preserving multi-turn fidelity by retaining most of the visual cache so that query-aware tokens can be retrieved at each conversation round. Built on an AWQ-optimized inference pipeline, SparseVILA achieves up to 4.0 times faster prefilling, 2.5 times faster decoding, and an overall 2.6 times end-to-end speedup.

The paper was authored by Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Konstantinos N. Plataniotis, Yao Lu, Song Han, and Zhijian Liu from NVIDIA, MIT, UC San Diego, and the University of Toronto, and was published on October 20, 2025 to arXiv as paper 2510.17777.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "158f8c65-74d9-439d-9946-e229351838ab"
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-29T06:52:08.046Z_

<details><summary>↩ Tool result · `toolu_01D9EyCdFcnududFBfEsSsHK`</summary>

```text
Web search results for query: "Jabbour Jason "Don't Run with Scissors" pruning VLA arXiv 2510.08464"

Links: [{"title":"[2510.08464] Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/abs/2510.08464"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/pdf/2510.08464"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered | OpenReview","url":"https://openreview.net/forum?id=c8g57pKdXD"},{"title":"VLN-CE-Isaac Benchmark | Download Scientific Diagram","url":"https://www.researchgate.net/figure/LN-CE-Isaac-Benchmark_fig2_386502820"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2602.00780"}]

I found the paper! Here's what the search results show:

"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" is authored by Jason Jabbour, Dong-Ki Kim, Max Smith, Jay Patrikar, Radhika Ghosal, Youhui Wang, Ali Agha, Vijay Janapa Reddi, and Shayegan Omidshafiei, with affiliations at FieldAI and Harvard University.

The paper addresses Vision-Language-Action (VLA) models' deployment challenges on resource-limited hardware and finds that pruning VLA models leads to drastic degradation and increased safety violations.

The authors introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits by performing a one-time interpolation between the dense and pruned models in weight-space to compute a corrective term used during inference. GLUESTICK requires no additional training, is agnostic to the pruning algorithm, and introduces a single hyperparameter that controls the tradeoff between efficiency and accuracy.

The paper is available at https://arxiv.org/abs/2510.08464 and additional materials can be found at https://gluestick-vla.github.io/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5b696e68-7238-4d0c-91a0-8f9b5c5cf07e"
}
```

</details>

---


### Tool result

_source line 128 · 2026-05-29T06:52:09.046Z_

<details><summary>↩ Tool result · `toolu_01VY7wpy9JYWAKwu4Tha23fA`</summary>

```text
Web search results for query: "Zhang Yuan "SparseVLM: Visual Token Sparsification" arXiv 2410.04417"

Links: [{"title":"[2410.04417] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/abs/2410.04417"},{"title":"[2410.04417] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://app.apixacrm.com/index.php?q=https%3A%2F%2Farxiv.org%2Fabs%2F2410.04417"},{"title":"SparseVLM","url":"https://leofan90.github.io/SparseVLMs.github.io/"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004417Z/abstract"},{"title":"GitHub - Theia-4869/SparseVLM","url":"https://github.com/Theia-4869/SparseVLM"},{"title":"(PDF) SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://www.researchgate.net/publication/384698552_SparseVLM_Visual_Token_Sparsification_for_Efficient_Vision-Language_Model_Inference"},{"title":"Paper page - SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://huggingface.co/papers/2410.04417"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/html/2410.04417v4"},{"title":"Panasonic HD develops “SparseVLM” technology that doubles the processing speed of Vision-Language Models | Innovations/Technologies | Company | Press Releases | Panasonic Newsroom Global","url":"https://news.panasonic.com/global/zh-CHS/press/en250704-2"}]

I found the paper you're looking for. Here's what I found:

**SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference** is a paper by Yuan Zhang and 10 other authors, with arXiv identifier 2410.04417.

**Key Contributions:**

The paper proposes a text-guided training-free token optimization mechanism called SparseVLM that eliminates the need for extra parameters or fine-tuning costs. The approach selects relevant text tokens to rate the significance of visual tokens using self-attention matrices, then prunes visual tokens to maximize sparsity while retaining information. It introduces a rank-based strategy to adaptively determine the sparsification ratio for each layer, alongside a token recycling method that compresses pruned tokens into more compact representations.

**Results:**

For example, LLaVA when equipped with SparseVLM achieves 54% reduction in FLOPs, 37% decrease in CUDA latency while maintaining 97% of its original accuracy.

The code is available at https://github.com/Gumpest/SparseVLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "63a04ebf-8b9e-41a4-9424-169dfb73eb81"
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-29T06:52:10.161Z_

<details><summary>↩ Tool result · `toolu_01DK4V3Tnkdqcrtm6Ke7KJHy`</summary>

```text
Web search results for query: "Shukor Mustafa "SmolVLA" arXiv 2506.01844"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"[2506.01844v1] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844v1"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://www.researchgate.net/publication/392370918_SmolVLA_A_Vision-Language-Action_Model_for_Affordable_and_Efficient_Robotics"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2506.01844"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"}]

Based on the search results, here's what I found about the paper:

**SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics**

This paper is authored by Mustafa Shukor, Dana Aubakirova, Francesco Capuano, Pepijn Kooijmans, Steven Palma, Adil Zouitine, Michel Aractingi, Caroline Pascal, Martino Russi, Andres Marafioti, Simon Alibert, Matthieu Cord, Thomas Wolf, and Remi Cadene.

**Overview:**
SmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. It is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs.

**Problem It Addresses:**
Existing VLAs are typically massive—often with billions of parameters—leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms.

**Key Features:**
The model introduces an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10× larger.

The paper was submitted to arXiv on June 2, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "7ce27e9f-3245-44d2-bffa-ff6e398f558d"
}
```

</details>

---


### Tool result

_source line 130 · 2026-05-29T06:52:10.861Z_

<details><summary>↩ Tool result · `toolu_01U1HjvvAEG3V6JMSqWgJ4dz`</summary>

```text
Web search results for query: "Li Xinghang "Vision-Language Foundation Models as Effective Robot Imitators" RoboFlamingo arXiv 2311.01378"

Links: [{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"RoboFlamingo | Vision-Language Foundation Models as Effective Robot Imitators","url":"https://roboflamingo.github.io/"},{"title":"RoboFlamingo - Overview","url":"https://github.com/roboflamingo"},{"title":"[PDF] Vision-Language Foundation Models as Effective Robot Imitators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Vision-Language-Foundation-Models-as-Effective-Li-Liu/857efca0d4cbece97da4b904de1d506c2af25f9c"},{"title":"Master Thesis","url":"https://www.ce.cit.tum.de/fileadmin/w00cgn/air/_my_direct_uploads/Improve_Robot_Performance_via_the_in-context_ability_of_Vision-language_Models.pdf"},{"title":"Paper page - Vision-Language Foundation Models as Effective Robot Imitators","url":"https://huggingface.co/papers/2311.01378"},{"title":"Training Data for RoboFlamingo | Data Requirements & Formats | Claru","url":"https://claru.ai/models/roboflamingo"},{"title":"GitHub - RoboFlamingo/RoboFlamingo: Code for RoboFlamingo · GitHub","url":"https://github.com/RoboFlamingo/RoboFlamingo"}]

Based on the search results, I found information about the paper you're looking for:

## Paper Overview

The paper "Vision-Language Foundation Models as Effective Robot Imitators" by Xinghang Li and 11 other authors discusses recent progress in vision language foundation models and their ability to understand multimodal data and resolve complicated vision language tasks, including robotics manipulation.

## RoboFlamingo Framework

The researchers derived a simple and novel vision-language manipulation framework, dubbed RoboFlamingo, built upon the open-source VLMs, OpenFlamingo. Unlike prior works, RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned manipulation datasets.

## Key Results and Implications

By exceeding the state-of-the-art performance with a large margin on the tested benchmark, the authors show RoboFlamingo can be an effective and competitive alternative to adapt VLMs to robot control. Such a decomposition provides RoboFlamingo the flexibility for open-loop control and deployment on low-performance platforms.

The paper was published on arXiv (2311.01378) on November 2, 2023. You can access the full paper at [https://arxiv.org/abs/2311.01378](https://arxiv.org/abs/2311.01378).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "bd8f8477-60c3-47a1-989b-5939dceb05ee"
}
```

</details>

---


### Tool call

_source line 131_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019yAdvN1P8VRSQxrw5ZgY58`</summary>

```json
{
  "query": "SparseVLM Zhang Yuan ICML 2025 accepted venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "666d5a73-1a8e-460b-8ed4-c67a27690d19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Hkfkeg3jTe1hPnsbDJjmL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 909,
      "cache_creation_input_tokens": 3570,
      "cache_read_input_tokens": 20775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3570,
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

_source line 132 · 2026-05-29T06:52:06.147Z_

<details><summary>↩ Tool result · `toolu_01ERonvou2v4NbbjZhbNJ1WZ`</summary>

```text
Web search results for query: "OpenVLA Open-Source Vision-Language-Action Model Kim Pertsch Karamcheti CoRL 2024"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://proceedings.mlr.press/v270/kim25c.html"},{"title":"Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions","url":"https://arxiv.org/html/2505.11214v1"}]

Based on the search results, here's what I found about OpenVLA:

## Overview
OpenVLA is an open-source vision-language-action (VLA) model created by a team of researchers, with large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations.

## Authors and Affiliations
The paper was authored by Moo Jin Kim, Karl Pertsch, and Siddharth Karamcheti (among 15 other co-authors) from institutions including Stanford University, UC Berkeley, Toyota Research Institute, Google DeepMind, Physical Intelligence, and MIT.

## Training and Data
The researchers curated a dataset of 970k robot manipulation trajectories from the Open X-Embodiment (OpenX) dataset, and trained OpenVLA on a cluster of 64 A100 GPUs for 15 days.

## Publication
The paper was published in the Proceedings of The 8th Conference on Robot Learning, PMLR 270:2679-2713, 2025.

## Key Features
OpenVLA can be effectively fine-tuned for new settings with strong generalization results, and can be fine-tuned on consumer GPUs via modern low-rank adaptation methods and served efficiently via quantization. The researchers released model checkpoints, fine-tuning notebooks, and their PyTorch codebase with built-in support for training VLAs at scale on Open X-Embodiment datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "585c9ff7-9349-414a-98be-8e931a326958"
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-29T06:52:06.903Z_

<details><summary>↩ Tool result · `toolu_012Q8QCLh3PZxqtHveu4ZYNg`</summary>

```text
Web search results for query: "RT-2 Vision-Language-Action Models Transfer Web Knowledge Robotic Control Brohan CoRL 2023"

Links: [{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control [Quick Review]","url":"https://liner.com/review/rt2-visionlanguageaction-models-transfer-web-knowledge-to-robotic-control"},{"title":"Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://huggingface.co/papers/2307.15818"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"dblp: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.","url":"https://dblp.org/rec/journals/corr/abs-2307-15818.html"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"}]

Based on the search results, here's what I found about RT-2:

## Overview

RT-2 is a vision-language-action (VLA) model that directly trains state-of-the-art vision-language models to output low-level robot actions.

## Key Innovation

The approach co-fine-tunes state-of-the-art vision-language models on both robotic trajectory data and Internet-scale vision-language tasks, such as visual question answering. To fit both natural language responses and robotic actions into the same format, the actions are expressed as text tokens and incorporated directly into the training set of the model in the same way as natural language tokens.

## Research Goal

The research studies how vision-language models trained on Internet-scale data can be incorporated directly into end-to-end robotic control to boost generalization and enable emergent semantic reasoning, with the goal of enabling a single end-to-end trained model to both learn to map robot observations to actions and enjoy the benefits of large-scale pretraining on language and vision-language data from the web.

## Publication

The paper was published in Proceedings of The 7th Conference on Robot Learning (CoRL) in 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "7c5bc6b2-861d-4039-81af-a120ae810199"
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-29T06:52:06.978Z_

<details><summary>↩ Tool result · `toolu_017ydNGaqfAH1oUqbpXxzLSn`</summary>

```text
Web search results for query: "π0.5 pi0.5 Vision-Language-Action Open-World Generalization Black arXiv 2504.16054"

Links: [{"title":"[2504.16054v1] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054v1"},{"title":"[2504.16054] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"A review of π0.5 — Scaling Open-World Generalization in Vision-Language-Action Models | by Isaac Edelman | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/a-review-of-%CF%800-5-scaling-open-world-generalization-in-vision-language-action-models-e4cb0d74264e"},{"title":"π0.5: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/pdf/2504.16054"},{"title":"$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://www.emergentmind.com/papers/2504.16054"},{"title":"$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250416054I/abstract"},{"title":"(PDF) \\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://www.researchgate.net/publication/391019295_pi_05_a_Vision-Language-Action_Model_with_Open-World_Generalization"}]

Based on the search results, here's what I found about π₀.₅:

π₀.₅ is a new model based on π₀ that uses co-training on heterogeneous tasks to enable broad generalization. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild.

π₀.₅ uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. The system uses a combination of co-training and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions.

π₀.₅ can control a mobile manipulator to clean kitchens and bedrooms in new homes that were not present in the training data, performing complex multi-stage behaviors with durations of 10 to 15 minutes.

The paper was submitted on April 22, 2025 and comes from authors at Physical Intelligence and other institutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "a50f2711-089a-4ebc-9d8c-c09e8fff251d"
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-29T06:52:07.788Z_

<details><summary>↩ Tool result · `toolu_01FCVWnVFrGkHMrezEEXmLqe`</summary>

```text
Web search results for query: "π0 pi0 Vision-Language-Action Flow Model General Robot Control Black arXiv 2410.24164"

Links: [{"title":"[2410.24164] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164"},{"title":"[2410.24164v1] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164v1"},{"title":"[PDF] π0: A Vision-Language-Action Flow Model for General Robot Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/%CF%800:-A-Vision-Language-Action-Flow-Model-for-General-Black-Brown/ef0c2a66b7bc82a2f90ac298310c064a49da8213"},{"title":"$π_0$: A Vision-Language-Action Flow Model for General Robot Control - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241024164B/abstract"},{"title":"Notes on: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" | cloderic.com","url":"https://www.cloderic.com/content/2025-02-27-notes-on-pi0"},{"title":"π0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/pdf/2410.24164v1"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"Paper page - π_0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://huggingface.co/papers/2410.24164"},{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"}]

I found the paper! Here's information about π₀:

## Overview

π₀ is titled "A Vision-Language-Action Flow Model for General Robot Control" and addresses robot learning's potential to unlock flexible, general, and dexterous robot systems.

## Key Approach

The paper proposes a novel flow matching architecture built on top of a pre-trained vision-language model (VLM) to inherit Internet-scale semantic knowledge. The model is trained on a large and diverse dataset from multiple dexterous robot platforms, including single-arm robots, dual-arm robots, and mobile manipulators.

## Application Example

The model is pre-trained on diverse data from 7 distinct robot configurations and 68 tasks, and can be used in zero-shot or fine-tuned to complex downstream tasks, such as laundry folding policies that fetch laundry from a dryer, pack it into a hamper, bring it to a folding table, and fold clothing.

## Authors and Affiliation

The paper was authored by Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, and others, affiliated with Physical Intelligence, a robotics startup.

The paper was published on arXiv on October 31, 2024 (arXiv:2410.24164).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "66bf317b-e7d0-48e2-90f6-a5bf01628ed1"
}
```

</details>

---


### Tool result

_source line 136 · 2026-05-29T06:52:08.054Z_

<details><summary>↩ Tool result · `toolu_012t2cjfdSKuDhz6kCyaNYWL`</summary>

```text
Web search results for query: "Octo Open-Source Generalist Robot Policy Ghosh RSS 2024"

Links: [{"title":"Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1","url":"https://arxiv.org/pdf/2405.12213"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/html/2405.12213v1"},{"title":"[PDF] Octo: An Open-Source Generalist Robot Policy | Semantic Scholar","url":"https://www.semanticscholar.org/paper/1d2753d74025e7a71594506623be81f18b073adb"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/"},{"title":"Octo: An Open-Source Generalist Robot Policy · Robotics: Science and Systems","url":"https://roboticsconference.org/2024/program/papers/90/"},{"title":"[2405.12213] Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/abs/2405.12213"},{"title":"(PDF) Octo: An Open-Source Generalist Robot Policy","url":"https://www.researchgate.net/publication/380730391_Octo_An_Open-Source_Generalist_Robot_Policy"},{"title":"GitHub - octo-models/octo: Octo is a transformer-based robot policy trained on a diverse mix of 800k robot trajectories. · GitHub","url":"https://github.com/octo-models/octo"},{"title":"Octo: An Open-Source Generalist Robot Policy | Request PDF","url":"https://www.researchgate.net/publication/383897130_Octo_An_Open-Source_Generalist_Robot_Policy"}]

Based on the search results, here's what I found about the Octo Open-Source Generalist Robot Policy:

Octo is an open-source, generalist policy for robotic manipulation. The Octo model is a transformer-based diffusion policy, pretrained on 800k robot episodes from the Open X-Embodiment dataset.

It supports flexible task and observation definitions and can be quickly finetuned to new observation and action spaces. It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs.

In experiments across 9 robotic platforms, Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces.

The paper was published at RSS 2024 (Robotics: Science and Systems), held July 15-19, 2024 in Delft, Netherlands. The work was led by Dibya Ghosh and a collaborative team from UC Berkeley, Stanford, Carnegie Mellon University, and Google DeepMind, and includes detailed ablations of design decisions to guide future research on building generalist robot models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "be11aeae-4ef7-45b9-942a-65b58f7582f7"
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-29T06:52:08.179Z_

<details><summary>↩ Tool result · `toolu_01KMY8xzAW61zGG1WFCDwKRa`</summary>

```text
Web search results for query: "RT-1 Robotics Transformer Real-World Control Scale Brohan RSS 2023"

Links: [{"title":"RT-1: Robotics Transformer for Real-World Control at Scale - R Discovery","url":"https://discovery.researcher.life/article/rt-1-robotics-transformer-for-real-world-control-at-scale/a5a1b925066134a18933ad552f843acf?page=5"},{"title":"(PDF) RT-1: Robotics Transformer for Real-World Control at Scale","url":"https://www.researchgate.net/publication/372803068_RT-1_Robotics_Transformer_for_Real-World_Control_at_Scale"},{"title":"dblp: RT-1: Robotics Transformer for Real-World Control at Scale.","url":"https://dblp.org/rec/conf/rss/BrohanBCCDFGHHH23.html"},{"title":"[2212.06817v2] RT-1: Robotics Transformer for Real-World Control at Scale","url":"https://arxiv.org/abs/2212.06817v2"},{"title":"[2212.06817] RT-1: Robotics Transformer for Real-World Control at Scale","url":"https://arxiv.org/abs/2212.06817"},{"title":"[PDF] RT-1: Robotics Transformer for Real-World Control at Scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-1:-Robotics-Transformer-for-Real-World-Control-Brohan-Brown/fd1cf28a2b8caf2fe29af5e7fa9191cecfedf84d"},{"title":"RT-1: Robotics Transformer for real-world control at scale","url":"https://research.google/blog/rt-1-robotics-transformer-for-real-world-control-at-scale/"},{"title":"RT-1: Robotics Transformer for Real-World Control at Scale","url":"https://arxiv.org/pdf/2212.06817"},{"title":"RT-1: Robotics Transformer for Real-World Control at Scale","url":"https://www.roboticsproceedings.org/rss19/p025.pdf"},{"title":"RT-1: Robotics Transformer for Real-World Control at Scale · Robotics: Science and Systems","url":"https://rss2023.github.io/rss2023-website/program/papers/025/"}]

Based on the search results, here's what I found about RT-1:

RT-1: Robotics Transformer for Real-World Control at Scale is a research paper published at Robotics: Science and Systems 2023 with authors including Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, and 47 additional collaborators.

The paper was published on July 10, 2023.

The paper presents a model class called Robotics Transformer that exhibits promising scalable model properties, based on large-scale data collection on real robots performing real-world tasks.

RT-1 can perform over 700 training instructions at 97% success rate, and can generalize to new tasks, distractors, and backgrounds 25%, 36% and 18% better than the next best baseline, respectively.

RT-1 can incorporate data from simulation or even other robot types, retaining performance on the original tasks and improving generalization to new scenarios.

The research demonstrates how transformer-based architectures can be scaled for real-world robotic control, using large diverse datasets to achieve strong generalization capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "3da04542-7ddb-4258-bfa7-670e85b981a2"
}
```

</details>

---


### Tool result

_source line 138 · 2026-05-29T06:52:08.736Z_

<details><summary>↩ Tool result · `toolu_01Bkat4VHQHCxj6nMFYxfAez`</summary>

```text
Web search results for query: ""An Image is Worth 1/2 Tokens After Layer 2" FastV Chen ECCV 2024 arXiv 2403.06764"

Links: [{"title":"GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/pkunlp-icler/FastV"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764"},{"title":"[2403.06764v1] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764v1"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"http://export.arxiv.org/abs/2403.06764"},{"title":"GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/chenllliang/FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference","url":"https://arxiv.org/html/2403.06764v3"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240306764C/abstract"},{"title":"[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"}]

I found the paper you're searching for. Here's what the search reveals:

"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models" is authored by Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, and Baobao Chang, with arXiv ID 2403.06764 (2024).

The paper was selected as an Oral Presentation (2%) at ECCV 2024.

The core contribution is FastV, a versatile plug-and-play method designed to optimize computational efficiency by learning adaptive attention patterns in early layers and pruning visual tokens in subsequent ones. The authors found that the attention computation over visual tokens is of extreme inefficiency in the deep layers of popular Large Vision-Language Models (LVLMs), suggesting a need for a sparser approach compared to textual data handling.

FastV demonstrates the ability to dramatically reduce computational costs (e.g., a 45% reduction in FLOPs for LLaVA-1.5-13B) without sacrificing performance in a wide range of image and video understanding tasks.

The code is available on GitHub at the official repository links found in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d9d782c3-55c7-4d6b-a57a-b54d6bd621de"
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-29T06:52:11.335Z_

<details><summary>↩ Tool result · `toolu_014cGutaUmXAotUmeAfyYQQz`</summary>

```text
Web search results for query: "VLA-IAP Training-Free Visual Token Pruning Interaction Alignment Cheng arXiv 2603.22991"

Links: [{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22991"},{"title":"[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make VLM Inference Faster","url":"https://arxiv.org/html/2412.01818v1"}]

I found the paper! Here are the results from the search:

VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models is authored by Jintao Cheng, Haozhe Wang, Weibin Li, Gang Wang, Yipu Zhang, Xiaoyu Tang, Jin Wu, Xieyuanli Chen, Yunhui Liu, and Wei Zhang, with affiliations at The Hong Kong University of Science and Technology, The Chinese University of Hong Kong, South China Normal University, National University of Defense Technology, and University of Science and Technology Beijing.

The paper addresses Vision-Language-Action (VLA) models that advance embodied intelligence for robots, but notes that inference cost becomes a bottleneck as model capacity and visual context length grow.

The key problem is that existing visual token pruning methods overlook continuous physical interaction in VLA tasks, leading to pruning of visually sparse yet structurally critical regions that support manipulation.

The proposed training-free method VLA-IAP introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment, enabling a conservative-to-aggressive transition.

Experiments show VLA-IAP achieves a 97.8% success rate with a 1.25× speedup on the LIBERO benchmark.

The paper was submitted to arXiv on March 24, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "dbc3c191-58fa-40ad-b64a-cc60f5cc7023"
}
```

</details>

---


### Tool result

_source line 140 · 2026-05-29T06:52:11.436Z_

<details><summary>↩ Tool result · `toolu_01Wn8ontxx1DjnFuBXBterkA`</summary>

```text
Web search results for query: "DynamicViT Efficient Vision Transformers Dynamic Token Sparsification Rao NeurIPS 2021"

Links: [{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://papers.nips.cc/paper/2021/hash/747d3443e319a22747fbb873e8b2f9f2-Abstract.html"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://proceedings.neurips.cc/paper/2021/hash/747d3443e319a22747fbb873e8b2f9f2-Abstract.html"},{"title":"GitHub - raoyongming/DynamicViT: [NeurIPS 2021] [T-PAMI] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification · GitHub","url":"https://github.com/raoyongming/DynamicViT"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token   Sparsification","url":"https://arxiv.org/pdf/2106.02034"},{"title":"[2106.02034] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://arxiv.org/abs/2106.02034"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210602034R/abstract"},{"title":"efficient vision transformers with dynamic token sparsification","url":"https://dl.acm.org/doi/10.5555/3540261.3541329"},{"title":"[PDF] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DynamicViT:-Efficient-Vision-Transformers-with-Rao-Zhao/dbdcabd0444ad50b68ee09e30f39b66e9068f5d2"},{"title":"Dynamic Spatial Sparsification for Efficient Vision Transformers and   Convolutional Neural Networks","url":"https://arxiv.org/pdf/2207.01580"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification | OpenReview","url":"https://openreview.net/forum?id=kR95DuwwXHZ"}]

I found comprehensive information about the DynamicViT paper. Here are the key details:

## Paper Overview

DynamicViT was authored by Yongming Rao, Wenliang Zhao, Benlin Liu, Jiwen Lu, Jie Zhou, and Cho-Jui Hsieh, and published at NeurIPS 2021.

## Main Contribution

The paper observes that attention is sparse in vision transformers and that final prediction is only based on a subset of most informative tokens. Based on this observation, the authors propose a dynamic token sparsification framework to prune redundant tokens progressively and dynamically based on the input, using a lightweight prediction module to estimate the importance score of each token.

## Technical Details

The prediction module is added to different layers to prune redundant tokens hierarchically. The unstructured sparse tokens are hardware friendly due to the nature of self-attention, making the framework easy to achieve actual speed-up.

## Performance Results

By hierarchically pruning 66% of the input tokens, the method greatly reduces 31%~37% FLOPs and improves throughput by over 40% while the accuracy drop is within 0.5% for various vision transformers. DynamicViT models achieve very competitive complexity/accuracy trade-offs compared to state-of-the-art CNNs and vision transformers on ImageNet.

Code is available at https://github.com/raoyongming/DynamicViT.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "e761fa11-0f4c-4385-bd35-68b2ff9e7b34"
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-29T06:52:14.826Z_

<details><summary>↩ Tool result · `toolu_01FNQZjnpHSss6iR8ERHCUoh`</summary>

```text
Web search results for query: "VLA-Cache Efficient Vision-Language-Action Manipulation Adaptive Token Caching Xu NeurIPS 2025"

Links: [{"title":"GitHub - siyuhsu/vla-cache: [NeurIPS 2025] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching · GitHub","url":"https://github.com/siyuhsu/vla-cache"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://vla-cache.github.io/"},{"title":"NeurIPS Poster VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118121"},{"title":"[2502.02175] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/abs/2502.02175"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching | OpenReview","url":"https://openreview.net/forum?id=QZYZ0Xm58q"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/pdf/2502.02175"},{"title":"Paper page - VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://huggingface.co/papers/2502.02175"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175v2"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"}]

I found comprehensive information about VLA-Cache. Here's a summary of this NeurIPS 2025 paper:

## Overview

VLA-Cache is a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames.

## Problem and Motivation

The substantial computational cost of Vision-Language-Action models poses a challenge for real-time robotic control, where rapid decision-making is essential.

## Key Technical Approach

VLA-Cache identifies minimally changed tokens between adjacent frames and reuses their cached key-value representations, thereby circumventing redundant computations. To maintain action precision, VLA-Cache selectively re-computes task-relevant tokens that are environmentally sensitive, ensuring the fidelity of critical visual information. 

The method introduces a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens for recomputation.

## Results

Experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7x speedup in CUDA latency and a 15% increase in control frequency, with negligible loss on task success rate.

## Authors and References

The paper is authored by Siyu Xu, Yunke Wang, Chenghao Xia, Dihao Zhu, Tao Huang, and Chang Xu, with the arXiv preprint available at arXiv:2502.02175. The code and project page are available on GitHub at siyuhsu/vla-cache.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "e2cdd146-7b92-44e2-af46-d5bae9199e10"
}
```

</details>

---


### Tool call

_source line 142_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014cqdEVzTD1w2LpsD36J59U`</summary>

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
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "563df1fe-b4ba-4d5d-8c8f-c80e835a941e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7MG34f9KtzVvNir5CJ2pW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6723,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6723,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 143 · 2026-05-29T06:52:08.063Z_

<details><summary>↩ Tool result · `toolu_014cqdEVzTD1w2LpsD36J59U`</summary>

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
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "3bbf20ac-c493-46c6-b2d1-643e8aaa8b77"
}
```

</details>

---


### Tool call

_source line 144_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GngLbgxc3avfXh6SZ9S5mb`</summary>

```json
{
  "query": "Bolya \"Token Merging: Your ViT But Faster\" ICLR 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "74e6d759-e988-4c67-a5ac-33d3dbffd19f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SucJWojeXs4x9FT4LiDpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1470,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1470,
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


### Tool call

_source line 145_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MrUyfQyvofNGEsVL8xDu5G`</summary>

```json
{
  "query": "Liang Youwei \"Not All Patches are What You Need\" ICLR 2022 EViT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5d7798f9-b298-41ad-930b-e8ce257f7625",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SucJWojeXs4x9FT4LiDpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1470,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1470,
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


### Tool call

_source line 146_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PNwZ3BjGiuKfHjnf9aQU75`</summary>

```json
{
  "query": "Liu Bo \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5248c8b4-fff0-4413-9b17-102bce651ca8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SucJWojeXs4x9FT4LiDpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1470,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1470,
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


### Tool call

_source line 147_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019FhFRMpDNJyfLtV1qTVaor`</summary>

```json
{
  "query": "Yang Yantai \"EfficientVLA\" arXiv 2506.10100 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d201e698-9446-4217-b4be-d0742a1a3659",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SucJWojeXs4x9FT4LiDpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1470,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1470,
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


### Tool call

_source line 148_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RZ6cykuS2mpMtvBaM4Z9aC`</summary>

```json
{
  "query": "Liu Ziyan \"VLA-Pruner\" arXiv 2511.16449 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "0d2a85d1-3e15-461c-8b5a-77580966ef65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SucJWojeXs4x9FT4LiDpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1470,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1470,
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


### Tool call

_source line 149_

<details open><summary>🔧 Tool call — Agent · `toolu_0117x4R1iCNaBL6zf4nmJYMo`</summary>

```json
{
  "description": "Verify bib entries batch 4",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. jaegle2021perceiver: \"Perceiver: General Perception with Iterative Attention\" by Jaegle, Andrew et al. Venue: ICML 2021.\n\n2. oquab2023dinov2: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime et al. Listed as TMLR 2024 in bib body, but key says 2023. Also there's a duplicate entry oquab2024dinov2.\n\n3. zhai2023siglip: \"Sigmoid Loss for Language Image Pre-Training\" by Zhai, Xiaohua et al. Venue: ICCV 2023.\n\n4. yang2024qwen2: \"Qwen2 Technical Report\" by Yang, An et al. arXiv:2407.10671, year 2024.\n\n5. lipman2023flow: \"Flow Matching for Generative Modeling\" by Lipman, Yaron et al. Venue: ICLR 2023.\n\n6. li2024cogact: \"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation\" by Li, Qixiu et al. arXiv:2411.19650, year 2024.\n\n7. kim2025openoft: \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" by Kim, Moo Jin and Finn, Chelsea and Liang, Percy. arXiv:2502.19645, year 2025.\n\n8. li2024tokenpacker: \"TokenPacker: Efficient Visual Projector for Multimodal LLM\" by Li, Wentong et al. arXiv:2407.02392, year 2024.\n\n9. zheng2025xvla: \"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" by Zheng, Jinliang et al. Venue: ICLR 2026, arXiv:2510.10274.\n\n10. wen2024tinyvla: \"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation\" by Wen, Junjie et al. arXiv:2409.12514, year 2024.\n\nFor each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "2ea39199-420c-43d3-bc65-bd666c8c8c19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyFVwDpqmf2wFz9bsVHa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 100682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6753
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 150_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a3d8459fe8a20ddf2",
  "tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "description": "Verify bib entries batch 4",
  "task_type": "local_agent",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. jaegle2021perceiver: \"Perceiver: General Perception with Iterative Attention\" by Jaegle, Andrew et al. Venue: ICML 2021.\n\n2. oquab2023dinov2: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime et al. Listed as TMLR 2024 in bib body, but key says 2023. Also there's a duplicate entry oquab2024dinov2.\n\n3. zhai2023siglip: \"Sigmoid Loss for Language Image Pre-Training\" by Zhai, Xiaohua et al. Venue: ICCV 2023.\n\n4. yang2024qwen2: \"Qwen2 Technical Report\" by Yang, An et al. arXiv:2407.10671, year 2024.\n\n5. lipman2023flow: \"Flow Matching for Generative Modeling\" by Lipman, Yaron et al. Venue: ICLR 2023.\n\n6. li2024cogact: \"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation\" by Li, Qixiu et al. arXiv:2411.19650, year 2024.\n\n7. kim2025openoft: \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" by Kim, Moo Jin and Finn, Chelsea and Liang, Percy. arXiv:2502.19645, year 2025.\n\n8. li2024tokenpacker: \"TokenPacker: Efficient Visual Projector for Multimodal LLM\" by Li, Wentong et al. arXiv:2407.02392, year 2024.\n\n9. zheng2025xvla: \"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" by Zheng, Jinliang et al. Venue: ICLR 2026, arXiv:2510.10274.\n\n10. wen2024tinyvla: \"TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation\" by Wen, Junjie et al. arXiv:2409.12514, year 2024.\n\nFor each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences.",
  "uuid": "06312fc2-0e55-466b-84fd-4878a4c946f1",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


## Round 4

## Round 4

41 recorded events


### User

_source line 151 · 2026-05-29T06:52:15.415Z_

You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.

Entries to verify:

1. jaegle2021perceiver: "Perceiver: General Perception with Iterative Attention" by Jaegle, Andrew et al. Venue: ICML 2021.

2. oquab2023dinov2: "DINOv2: Learning Robust Visual Features without Supervision" by Oquab, Maxime et al. Listed as TMLR 2024 in bib body, but key says 2023. Also there's a duplicate entry oquab2024dinov2.

3. zhai2023siglip: "Sigmoid Loss for Language Image Pre-Training" by Zhai, Xiaohua et al. Venue: ICCV 2023.

4. yang2024qwen2: "Qwen2 Technical Report" by Yang, An et al. arXiv:2407.10671, year 2024.

5. lipman2023flow: "Flow Matching for Generative Modeling" by Lipman, Yaron et al. Venue: ICLR 2023.

6. li2024cogact: "CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation" by Li, Qixiu et al. arXiv:2411.19650, year 2024.

7. kim2025openoft: "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" by Kim, Moo Jin and Finn, Chelsea and Liang, Percy. arXiv:2502.19645, year 2025.

8. li2024tokenpacker: "TokenPacker: Efficient Visual Projector for Multimodal LLM" by Li, Wentong et al. arXiv:2407.02392, year 2024.

9. zheng2025xvla: "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model" by Zheng, Jinliang et al. Venue: ICLR 2026, arXiv:2510.10274.

10. wen2024tinyvla: "TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation" by Wen, Junjie et al. arXiv:2409.12514, year 2024.

For each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "cb3817b7-2121-4a4a-ace6-01a8ad9e42e9"
}
```

</details>

---


### System

_source line 152_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for SpecPrune-VLA ICRA 2026 accepted openreview",
  "usage": {
    "total_tokens": 25283,
    "tool_uses": 13,
    "duration_ms": 36676
  },
  "last_tool_name": "WebSearch",
  "uuid": "9e31bab3-fccb-44bc-987c-178b7f193c39",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 153_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for LightVLA Jiang Titong ICRA 2026 accepted conferen…",
  "usage": {
    "total_tokens": 25284,
    "tool_uses": 14,
    "duration_ms": 37150
  },
  "last_tool_name": "WebSearch",
  "uuid": "758e42db-4469-47c3-ad17-58aa6e7f08aa",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 154_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for RoboFlamingo Li Xinghang ICLR 2024 accepted confe…",
  "usage": {
    "total_tokens": 25285,
    "tool_uses": 15,
    "duration_ms": 38160
  },
  "last_tool_name": "WebSearch",
  "uuid": "ace0dbbb-e41a-460f-8879-dba14635454c",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 155_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for SparseVILA Khaki ICCV 2025 \"Decoupled Visual Spar…",
  "usage": {
    "total_tokens": 25286,
    "tool_uses": 16,
    "duration_ms": 38349
  },
  "last_tool_name": "WebSearch",
  "uuid": "398e333c-9e9c-4e52-9a54-c6ea1ce97014",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 156_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3d8459fe8a20ddf2",
  "tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "description": "Verify bib entries batch 4",
  "usage": {
    "total_tokens": 14944,
    "tool_uses": 1,
    "duration_ms": 2905
  },
  "last_tool_name": "ToolSearch",
  "uuid": "b6c57dbc-384c-431f-9a8c-1b076085b25e",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 157_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for RT-2 CoRL 2023 proceedings PMLR authors Zitkovich…",
  "usage": {
    "total_tokens": 25725,
    "tool_uses": 12,
    "duration_ms": 27209
  },
  "last_tool_name": "WebSearch",
  "uuid": "e9a0f609-3707-4a8a-904b-e3cea0c14879",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 158_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for OpenVLA CoRL 2024 PMLR 270 Kim Pertsch proceedings",
  "usage": {
    "total_tokens": 25726,
    "tool_uses": 13,
    "duration_ms": 28263
  },
  "last_tool_name": "WebSearch",
  "uuid": "4ad548b3-095f-434f-a6cd-8b9a648acbc8",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 159_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3d8459fe8a20ddf2",
  "tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "description": "Searching for Perceiver General Perception with Iterative Atten…",
  "usage": {
    "total_tokens": 16409,
    "tool_uses": 2,
    "duration_ms": 5909
  },
  "last_tool_name": "WebSearch",
  "uuid": "68d48191-d5fc-46ed-a026-beae357db1e1",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 160_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for pi0 π0 Physical Intelligence CoRL 2025 ICML 2025 …",
  "usage": {
    "total_tokens": 25727,
    "tool_uses": 14,
    "duration_ms": 29098
  },
  "last_tool_name": "WebSearch",
  "uuid": "054d3cc1-5eb5-4878-956a-a5e3519d7ca3",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 161_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for pi0.5 π0.5 CoRL 2025 PMLR 305 proceedings accepted",
  "usage": {
    "total_tokens": 25728,
    "tool_uses": 15,
    "duration_ms": 29577
  },
  "last_tool_name": "WebSearch",
  "uuid": "509250a6-9f43-40dd-a532-f622bf2de279",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 162_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for VLA-Cache arXiv 2502.02175 authors Siyu Xu Yunke …",
  "usage": {
    "total_tokens": 25729,
    "tool_uses": 16,
    "duration_ms": 30275
  },
  "last_tool_name": "WebSearch",
  "uuid": "01b091ef-6dd4-4148-a57c-da6eae8542c3",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 163_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for Shang Yuzhang \"LLaVA-PruMerge\" adaptive token red…",
  "usage": {
    "total_tokens": 20622,
    "tool_uses": 7,
    "duration_ms": 20278
  },
  "last_tool_name": "WebSearch",
  "uuid": "9cf7a186-057a-4da3-9857-0fa5f281af8c",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 164_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for Liu Haotian \"Visual Instruction Tuning\" LLaVA Neu…",
  "usage": {
    "total_tokens": 20623,
    "tool_uses": 8,
    "duration_ms": 20747
  },
  "last_tool_name": "WebSearch",
  "uuid": "16bef6c4-2a48-49d9-8cb8-654e7babce7a",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### Tool call

_source line 165_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018k5rXp9mE5DgSQUpBxGd4C`</summary>

```json
{
  "query": "SpecPrune-VLA ICRA 2026 accepted openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5c799355-9b24-4db1-8a69-694a355bdc94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Hkfkeg3jTe1hPnsbDJjmL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 909,
      "cache_creation_input_tokens": 3570,
      "cache_read_input_tokens": 20775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3570,
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


### Tool call

_source line 166_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DB7VViBk4opyApQGPacxz8`</summary>

```json
{
  "query": "LightVLA Jiang Titong ICRA 2026 accepted conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "7b16f60f-1ae1-4dc2-9439-3ef91d686582",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Hkfkeg3jTe1hPnsbDJjmL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 909,
      "cache_creation_input_tokens": 3570,
      "cache_read_input_tokens": 20775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3570,
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


### Tool call

_source line 167_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SowAnuSwm3NxfiWXisgVav`</summary>

```json
{
  "query": "RoboFlamingo Li Xinghang ICLR 2024 accepted conference venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "e8be220c-a6d6-4f3e-9cf1-ed47b32aa1d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Hkfkeg3jTe1hPnsbDJjmL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 909,
      "cache_creation_input_tokens": 3570,
      "cache_read_input_tokens": 20775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3570,
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


### Tool call

_source line 168_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SPDYpMa27Yqn69JgVLQU3y`</summary>

```json
{
  "query": "SparseVILA Khaki ICCV 2025 \"Decoupled Visual Sparsity\" title exact"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "6946fce8-bf0c-4971-9974-5c725de14149",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Hkfkeg3jTe1hPnsbDJjmL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 909,
      "cache_creation_input_tokens": 3570,
      "cache_read_input_tokens": 20775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3570,
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

_source line 169 · 2026-05-29T06:52:20.361Z_

<details><summary>↩ Tool result · `toolu_019yAdvN1P8VRSQxrw5ZgY58`</summary>

```text
Web search results for query: "SparseVLM Zhang Yuan ICML 2025 accepted venue conference"

Links: [{"title":"GitHub - Gumpest/SparseVLMs: [ICML'25] Official implementation of paper \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" and \"SparseVLM+: Visual Token Sparsification with Improved Text-Visual Attention Pattern\" · GitHub","url":"https://github.com/Gumpest/SparseVLMs"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference | OpenReview","url":"https://openreview.net/forum?id=80faIPZ67S"},{"title":"[2410.04417] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/abs/2410.04417"},{"title":"ICML Poster SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://icml.cc/virtual/2025/poster/46297"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"Enhancing Visual-Language Prompt Tuning Through Sparse Knowledge-Guided Context Optimization","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11941247/"}]

Based on the search results, I can provide you with information about SparseVLM and its acceptance at ICML 2025:

SparseVLM was accepted by ICML 2025. The paper is titled "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference" and is authored by Zhang Yuan and co-authors including Fan, Chun-Kai, Ma, Junpeng, and others.

The paper was published as an ICML 2025 poster on May 1, 2025. SparseVLM is an efficient training-free token optimization mechanism that requires no extra parameters or fine-tuning costs, and it focuses on selecting visual-relevant text tokens to rate the significance of vision tokens and uses a rank-based strategy to adaptively determine the sparsification ratio for each layer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5efb1912-c55e-4801-ab98-2bbc6d4b1391"
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-29T06:52:22.170Z_

<details><summary>↩ Tool result · `toolu_01SowAnuSwm3NxfiWXisgVav`</summary>

```text
Web search results for query: "RoboFlamingo Li Xinghang ICLR 2024 accepted conference venue"

Links: [{"title":"Vision-Language Foundation Models as Effective Robot Imitators | OpenReview","url":"https://openreview.net/forum?id=lFYj0oibGR"},{"title":"RoboFlamingo | Vision-Language Foundation Models as Effective Robot Imitators","url":"https://roboflamingo.github.io/"},{"title":"RoboFlamingo Review | gracefullight.dev","url":"https://gracefullight.dev/en/2025/08/31/roboflamingo-review/"},{"title":"[Quick Review] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://liner.com/review/visionlanguage-foundation-models-as-effective-robot-imitators"},{"title":"RoboFlamingo-Plus: Fusion of Depth and RGB Perception with   Vision-Language Models for Enhanced Robotic Manipulation","url":"https://arxiv.org/pdf/2503.19510"},{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"RoboFlamingo - Overview","url":"https://github.com/roboflamingo"},{"title":"(PDF) VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model","url":"https://www.researchgate.net/publication/395418066_VLA-Adapter_An_Effective_Paradigm_for_Tiny-Scale_Vision-Language-Action_Model"}]

Based on the search results, I found information about RoboFlamingo by Li Xinghang and its ICLR 2024 acceptance:

The paper "Vision-Language Foundation Models as Effective Robot Imitators" by Xinghang Li and colleagues was accepted to ICLR 2024.

Regarding the conference venue, the paper was initially presented as an ICLR 2023 paper, but according to the search results, the work was accepted and published in ICLR 2024. Unfortunately, the specific venue location for ICLR 2024 is not mentioned in these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "965969df-95c1-4030-9af7-3c213bb5e203"
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-29T06:52:22.501Z_

<details><summary>↩ Tool result · `toolu_018k5rXp9mE5DgSQUpBxGd4C`</summary>

```text
Web search results for query: "SpecPrune-VLA ICRA 2026 accepted openreview"

Links: [{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"},{"title":"IEEE ICRA 2026 | OpenReview","url":"https://openreview.net/group?id=IEEE.org/ICRA/2026"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/pdf/2509.05614"},{"title":"IEEE ICRA 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=IEEE.org%2FICRA%2F2026%2FWorkshop"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"},{"title":"IEEE ICRA 2026 Workshop From Data to Decisions | OpenReview","url":"https://openreview.net/group?id=IEEE.org%2FICRA%2F2026%2FWorkshop%2FFrom_Data_to_Decisions"},{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"IEEE ICRA 2026 Arts and Robotics | OpenReview","url":"https://openreview.net/group?id=IEEE.org%2FICRA%2F2026%2FArts_and_Robotics"}]

I found relevant information about SpecPrune-VLA. SpecPrune-VLA is a method that includes layer-level dynamic pruning to prune tokens adaptively per layer based on layer-wise importance, and a lightweight action-aware controller that classifies actions as coarse- or fine-grained by the speed of the end effector, adjusting pruning aggressiveness accordingly.

The method achieves up to 1.57× speedup in the LIBERO simulation benchmark across different hardware configurations, and an average speedup of 1.70× in real-world robotic tasks, with negligible degradation in task success rate compared to the OpenVLA-OFT model.

The paper is available on OpenReview at https://openreview.net/forum?id=t85Ni0LwjC. However, based on the search results, I cannot confirm the specific acceptance status for ICRA 2026's main conference track from the information provided. The results show the paper exists on OpenReview and appears to be associated with ICRA 2026, but the detailed acceptance status information is not explicitly stated in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "0513fd5c-cb9b-4131-95d4-0f71efa06d0a"
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-29T06:52:23.224Z_

<details><summary>↩ Tool result · `toolu_01DB7VViBk4opyApQGPacxz8`</summary>

```text
Web search results for query: "LightVLA Jiang Titong ICRA 2026 accepted conference"

Links: [{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"LightVLA/LIBERO.md at main · LiAutoAD/LightVLA","url":"https://github.com/LiAutoAD/LightVLA/blob/main/LIBERO.md"},{"title":"2026 IEEE International Conference on Robotics and Automation (ICRA)","url":"https://2026.ieee-icra.org/"},{"title":"Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline","url":"https://arxiv.org/pdf/2602.22663"},{"title":"ICRA 2026","url":"https://pal-robotics.com/event/icra-2026/"}]

Based on the search results, here's what I found about LightVLA, Titong Jiang, and ICRA 2026:

LightVLA has been accepted by ICRA 2026, and the paper is titled "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning" with Titong Jiang as one of the co-first authors.

LightVLA is an innovative, simple yet effective differentiable token pruning framework designed for Vision-Language-Action (VLA) models. It addresses the challenge of deploying VLA models on resource-constrained platforms by generating dynamic queries to evaluate the importance of visual tokens and employing Gumbel softmax for differentiable token selection, allowing the system to retain the most informative visual tokens while pruning those that do not contribute to task execution.

LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.6% improvement in task success rate. The project website is available at https://liauto-research.github.io/LightVLA/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "087a281e-02b2-4693-85e0-6b6ccad24f5e"
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-29T06:52:25.467Z_

<details><summary>↩ Tool result · `toolu_01SPDYpMa27Yqn69JgVLQU3y`</summary>

```text
Web search results for query: "SparseVILA Khaki ICCV 2025 "Decoupled Visual Sparsity" title exact"

Links: [{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/html/2510.17777v1"},{"title":"[2510.17777] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/abs/2510.17777"},{"title":"2025-10-21 SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efﬁcient VLM Inference Samir Khaki4","url":"https://www.openaccess.thecvf.com/content/ICCV2025/papers/Khaki_SparseVILA_Decoupling_Visual_Sparsity_for_Efficient_VLM_Inference_ICCV_2025_paper.pdf"},{"title":"ICCV Poster SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://iccv.thecvf.com/virtual/2025/poster/1739"},{"title":"Zhijian Liu","url":"https://zhijianliu.com/"},{"title":"[Literature Review] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://www.themoonlight.io/en/review/sparsevila-decoupling-visual-sparsity-for-efficient-vlm-inference"},{"title":"SparseVILA-R1: Decoupling Visual Sparsity for Efficient VLM Reasoning","url":"https://openreview.net/pdf/6597aa03e44118e07d8bbbe91433da250c6beb33.pdf"}]

Based on the search results, I found information about **SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference**:

SparseVILA is a new paradigm for efficient VLM inference that decouples visual sparsity across the prefilling and decoding stages. SparseVILA distributes sparsity across stages by pruning redundant visual tokens during prefill and retrieving only query-relevant tokens during decoding.

The paper was authored by Samir Khaki and colleagues from NVIDIA, MIT, UC San Diego, and University of Toronto. This is an ICCV paper (Open Access version), confirming its acceptance at ICCV 2025.

SparseVILA achieves up to 4.0 times faster prefilling, 2.5 times faster decoding, and an overall 2.6 times end-to-end speedup.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "e5261791-3d2a-4d7c-a928-4168ad2989a8"
}
```

</details>

---


### Tool call

_source line 174_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ld9ReMy7Cqe5QUje2AE7wT`</summary>

```json
{
  "query": "RT-2 CoRL 2023 proceedings PMLR authors Zitkovich Brohan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5ccdea96-e938-4234-8597-8c2547bc10b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wjCWvc11yGe7GLv9pNjNu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1669,
      "cache_creation_input_tokens": 7574,
      "cache_read_input_tokens": 16446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7574,
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


### Tool call

_source line 175_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UeFhQmkvQcYqiotSD39uM5`</summary>

```json
{
  "query": "OpenVLA CoRL 2024 PMLR 270 Kim Pertsch proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "e79493e2-3a63-4a32-9445-9dd7ca68d54f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wjCWvc11yGe7GLv9pNjNu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1669,
      "cache_creation_input_tokens": 7574,
      "cache_read_input_tokens": 16446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7574,
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


### Tool call

_source line 176_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CZQCe5VNXgzysqLfFxkytP`</summary>

```json
{
  "query": "pi0 π0 Physical Intelligence CoRL 2025 ICML 2025 accepted conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "1208b556-3617-4445-aba7-c03311bf7b6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wjCWvc11yGe7GLv9pNjNu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1669,
      "cache_creation_input_tokens": 7574,
      "cache_read_input_tokens": 16446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7574,
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


### Tool call

_source line 177_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L8B5Ms3jw49uACWpCcZs23`</summary>

```json
{
  "query": "pi0.5 π0.5 CoRL 2025 PMLR 305 proceedings accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "2bc3a298-881e-4711-8329-b2a7ecd1022b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wjCWvc11yGe7GLv9pNjNu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1669,
      "cache_creation_input_tokens": 7574,
      "cache_read_input_tokens": 16446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7574,
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


### Tool call

_source line 178_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WG2Ep8r4yDnNzoj3LfUQMt`</summary>

```json
{
  "query": "VLA-Cache arXiv 2502.02175 authors Siyu Xu Yunke Wang NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "129b48fe-c1fa-4698-bbb9-6dd3ea08f470",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wjCWvc11yGe7GLv9pNjNu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1669,
      "cache_creation_input_tokens": 7574,
      "cache_read_input_tokens": 16446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7574,
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

_source line 179 · 2026-05-29T06:52:24.294Z_

<details><summary>↩ Tool result · `toolu_01Ld9ReMy7Cqe5QUje2AE7wT`</summary>

```text
Web search results for query: "RT-2 CoRL 2023 proceedings PMLR authors Zitkovich Brohan"

Links: [{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"7th CoRL 2023: Atlanta, GA, USA","url":"https://dblp.org/db/conf/corl/corl2023.html"},{"title":"General-purpose foundation models for increased autonomy in robot-assisted surgery | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-024-00917-4"},{"title":"CoRL 2023","url":"https://www.corl2023.org/"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"Advancing general robotic manipulation with multimodal foundation models: An embodied AI paradigm | Science China Technological Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11431-024-2910-3"},{"title":"Papers — CoRL 2023","url":"https://www.corl2023.org/papers"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic   Control","url":"https://arxiv.org/pdf/2307.15818"}]

Based on the search results, I found information about the RT-2 paper in the CoRL 2023 proceedings published by PMLR:

The paper "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" was published in Proceedings of The 7th Conference on Robot Learning, PMLR 229:2165-2183, 2023. 

The authors include Brianna Zitkovich as the first author and Anthony Brohan among the 54 total authors listed for this paper.

The official PMLR proceedings page is available at: https://proceedings.mlr.press/v229/zitkovich23a.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "7f4ee9ee-c419-49e9-8256-a780c1850274"
}
```

</details>

---


### Tool result

_source line 180 · 2026-05-29T06:52:17.521Z_

<details><summary>↩ Tool result · `toolu_01GngLbgxc3avfXh6SZ9S5mb`</summary>

```text
Web search results for query: "Bolya "Token Merging: Your ViT But Faster" ICLR 2023"

Links: [{"title":"Token Merging: Your ViT but Faster","url":"https://github.com/facebookresearch/ToMe"},{"title":"Published as a conference paper at ICLR 2023 TOKEN MERGING: YOUR VIT BUT FASTER","url":"https://arxiv.org/pdf/2210.09461"},{"title":"[2210.09461] Token Merging: Your ViT But Faster","url":"https://arxiv-export1.library.cornell.edu/abs/2210.09461"},{"title":"Token Merging: Your ViT But Faster | OpenReview","url":"https://openreview.net/forum?id=JroZRaRw7Eu"},{"title":"CubistMerge: Spatial-Preserving Token Merging For Diverse ViT Backbones","url":"https://arxiv.org/html/2509.21764v1"},{"title":"dbolya/tomesd - Token Merging for Stable Diffusion","url":"https://github.com/dbolya/tomesd"},{"title":"[2210.09461] Token Merging: Your ViT But Faster","url":"https://arxiv.org/abs/2210.09461"},{"title":"Training-Free Acceleration of ViTs with Delayed Spatial Merging","url":"https://arxiv.org/pdf/2303.02331"}]

I found comprehensive information about the paper. Here are the key details about Bolya's "Token Merging: Your ViT But Faster" from ICLR 2023:

## Overview

The paper is authored by Daniel Bolya, Cheng-Yang Fu, Xiaoliang Dai, Peizhao Zhang, Christoph Feichtenhofer, and Judy Hoffman, and was published at the International Conference on Learning Representations in 2023.

## Key Contribution

Token Merging (ToMe) is a simple method to increase the throughput of existing ViT models without needing to train. ToMe gradually combines similar tokens in a transformer using a general and light-weight matching algorithm that is as fast as pruning while being more accurate.

## Performance Results

Off-the-shelf, ToMe can 2x the throughput of state-of-the-art ViT-L @ 512 and ViT-H @ 518 models on images and 2.2x the throughput of ViT-L on video with only a 0.2-0.3% accuracy drop in each case. ToMe can also easily be applied during training, improving in practice training speed up to 2x for MAE fine-tuning on video.

## Recognition

The paper was accepted for an oral presentation at ICLR. It was recognized as a notable top 5% paper at ICLR 2023.

The official implementation is available on GitHub at the Facebook Research repository (facebookresearch/ToMe).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "622a5b96-5546-478f-b0b5-975cee7ef651"
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-29T06:52:18.805Z_

<details><summary>↩ Tool result · `toolu_01MrUyfQyvofNGEsVL8xDu5G`</summary>

```text
Web search results for query: "Liang Youwei "Not All Patches are What You Need" ICLR 2022 EViT"

Links: [{"title":"GitHub - youweiliang/evit: Python code for ICLR 2022 spotlight paper EViT: Expediting Vision Transformers via Token Reorganizations · GitHub","url":"https://github.com/youweiliang/evit"},{"title":"Published as a conference paper at ICLR 2022 NOT ALL PATCHES ARE WHAT YOU NEED:","url":"https://openreview.net/pdf?id=BjyvwnXXVn_"},{"title":"dblp: Youwei Liang","url":"https://dblp.org/pid/257/5626.html"},{"title":"Youwei Liang - Homepage","url":"https://youweiliang.github.io/"},{"title":"(PDF) Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations","url":"https://www.researchgate.net/publication/358655949_Not_All_Patches_are_What_You_Need_Expediting_Vision_Transformers_via_Token_Reorganizations"},{"title":"[2202.07800v1] Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations","url":"https://arxiv.org/abs/2202.07800v1"},{"title":"[2202.07800] Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations","url":"https://arxiv.org/abs/2202.07800"},{"title":"Not All Patches are What You Need: Expediting Vision Transformers via   Token Reorganizations","url":"https://arxiv.org/pdf/2202.07800"},{"title":"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations | DeepAI","url":"https://deepai.org/publication/not-all-patches-are-what-you-need-expediting-vision-transformers-via-token-reorganizations"}]

Based on the search results, I found information about this paper:

"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" is by Youwei Liang, Chongjian Ge, Zhan Tong, Yibing Song, Jue Wang, and Pengtao Xie, published at ICLR (International Conference on Learning Representations) as a Spotlight paper in 2022.

The proposed EViT method reduces computation by progressively discarding or fusing inattentive tokens in Vision Transformers. More specifically, the paper addresses how Vision Transformers take all image patches as tokens and construct multi-head self-attention among them, but complete leverage of these image tokens brings redundant computations since not all tokens are attentive.

The paper demonstrates practical improvements: for instance, the inference speed of DeiT-S is increased by 50% while its recognition accuracy is decreased by only 0.3% for ImageNet classification. Additionally, the method improves the recognition accuracy of DeiT-S by 1% for ImageNet classification at the same computational cost of a vanilla DeiT-S.

The method does not introduce more parameters to ViTs. The code is available on GitHub at https://github.com/youweiliang/evit.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "e1551909-1c41-4d40-ad98-d77edbb125b7"
}
```

</details>

---


### Tool result

_source line 182 · 2026-05-29T06:52:18.987Z_

<details><summary>↩ Tool result · `toolu_019FhFRMpDNJyfLtV1qTVaor`</summary>

```text
Web search results for query: "Yang Yantai "EfficientVLA" arXiv 2506.10100 2025"

Links: [{"title":"[2506.10100] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"Computer Vision and Pattern Recognition Jun 2025","url":"https://arxiv.org/list/cs.CV/2025-06?skip=1000&show=2000"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.10100"},{"title":"Paper page - EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.10100"},{"title":"Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.24941"}]

Based on the search results, I found the paper you're looking for:

**EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models** was submitted on June 11, 2025, with arXiv ID 2506.10100. The authors include Yantai Yang, Yuhao Wang, Zichen Wen, Luo Zhongwei, Chang Zou, Zhipeng Zhang, Chuan Wen, and Linfeng Zhang from institutions including Shanghai Jiao Tong University, Harbin Institute of Technology, Xi'an Jiaotong University, and University of Electronic Science and Technology of China.

The paper addresses how Vision-Language-Action (VLA) models, particularly diffusion-based architectures, are hampered by high computational and memory demands. While existing acceleration efforts target isolated inefficiencies, EfficientVLA introduces a structured, training-free inference acceleration framework that systematically eliminates these barriers.

The framework integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, (2) optimizing the visual processing pathway through task-aware visual token selection, and (3) alleviating temporal computational redundancy within the diffusion-based action head by caching and reusing intermediate features.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "dd729cb3-e7c7-4b0f-90df-8eee468c13ba"
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-29T06:52:19.319Z_

<details><summary>↩ Tool result · `toolu_01RZ6cykuS2mpMtvBaM4Z9aC`</summary>

```text
Web search results for query: "Liu Ziyan "VLA-Pruner" arXiv 2511.16449 2025"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"Computer Science Nov 2025","url":"https://arxiv.org/list/cs/2025-11?skip=7900"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://www.arxiv.org/list/cs.CV/2025?skip=24300&show=50"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449v3"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"}]

Based on the search results, I found the paper you're looking for:

**Title:** VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference

**Authors:** Ziyan Liu, Yeqiu Chen, Hongyi Cai, Tao Lin, Shuo Yang, Zheng Liu, Bo Zhao

**arXiv ID:** 2511.16449

**Overview:**
Vision-Language-Action (VLA) models have shown great promise for embodied AI, yet the heavy computational cost of processing continuous visual streams severely limits their real-time deployment. VLA-Pruner is a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation.

VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance.

The paper is available on arXiv at: https://arxiv.org/abs/2511.16449


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "9b0d19d6-ebcd-40ff-8789-fe729b7b3e3d"
}
```

</details>

---


### Tool result

_source line 184 · 2026-05-29T06:52:21.111Z_

<details><summary>↩ Tool result · `toolu_01PNwZ3BjGiuKfHjnf9aQU75`</summary>

```text
Web search results for query: "Liu Bo "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" NeurIPS 2023"

Links: [{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning [Quick Review]","url":"https://liner.com/review/libero-benchmarking-knowledge-transfer-for-lifelong-robot-learning"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning – Sony AI","url":"https://ai.sony/publications/LIBERO-Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learning/"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning – UT Austin Robot Perception and Learning Lab","url":"https://rpl.cs.utexas.edu/publications/2023/12/10/liu-neurips23-libero/"},{"title":"NeurIPS Poster LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://neurips.cc/virtual/2023/poster/73415"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/pdf/2306.03310"},{"title":"Peter Stone: LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html/b2hd-liu_zhu_NeurIPS2023.html"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"}]

I found comprehensive information about this paper. Here's what I found:

LIBERO is a novel benchmark of lifelong learning for robot manipulation introduced by Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, and Peter Stone at NeurIPS 2023 (Datasets and Benchmarks Track).

Unlike traditional lifelong learning problems in image and text domains, which primarily involve the transfer of declarative knowledge of entities and concepts, lifelong learning in decision-making (LLDM) also necessitates the transfer of procedural knowledge, such as actions and behaviors. LIBERO is designed to advance research in LLDM.

The benchmark highlights five key research topics in LLDM: 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how to design effective policy architectures and 3) effective algorithms for LLDM; 4) the robustness of a lifelong learner with respect to task ordering; and 5) the effect of model pretraining for LLDM.

The paper develops an extendible procedural generation pipeline that can in principle generate infinitely many tasks.

The paper is available on arXiv (2306.03310) and through the official NeurIPS proceedings, along with code available on GitHub at the Lifelong-Robot-Learning/LIBERO repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "f03c88cc-4a5e-4d4f-abca-b627d577e0cc"
}
```

</details>

---


### Tool call

_source line 185_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0169DXnpUg7tiJrFNDryVxpo`</summary>

```json
{
  "query": "Shang Yuzhang \"LLaVA-PruMerge\" adaptive token reduction arXiv 2403.15388"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "04eb5856-0c5c-4535-85e4-adf3837ff6d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdWF1tpcQstPAmsLVFudyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1241,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 16451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2906,
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


### Tool call

_source line 186_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HPUHZffpzfqS2D2BQT9cdP`</summary>

```json
{
  "query": "Liu Haotian \"Visual Instruction Tuning\" LLaVA NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "7b4c5aa1-cd9e-451c-8d46-7b815efba899",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdWF1tpcQstPAmsLVFudyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1241,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 16451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2906,
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


### Tool call

_source line 187_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NMxt6tYYtR1Au5DaQJkiR1`</summary>

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
  "parent_tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "b06fb697-e673-41d1-bc9b-677690ad3d60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkmuPun84pZWaPDBBzwSZn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6673,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6673,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 188 · 2026-05-29T06:52:18.328Z_

<details><summary>↩ Tool result · `toolu_01NMxt6tYYtR1Au5DaQJkiR1`</summary>

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
  "parent_tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "d55af6a8-414d-41ff-a1c6-587bfc41871f"
}
```

</details>

---


### Tool call

_source line 189_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LcFjxtgg4g4frmEA5wBZsE`</summary>

```json
{
  "query": "Perceiver General Perception with Iterative Attention Jaegle ICML 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "f6d9e951-f6d1-48e2-8ec5-282dd16f0271",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ant6soo6oyPJPSFXouESmc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 14931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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


### Tool call

_source line 190_

<details open><summary>🔧 Tool call — Agent · `toolu_01Qkkz3XixZywawXoLKe6w4A`</summary>

```json
{
  "description": "Verify bib entries batch 5",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. lewis2020bart: \"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension\" by Lewis, Mike et al. Venue: ACL 2020.\n\n2. ryoo2021tokenlearner: \"TokenLearner: Adaptive Space-Time Tokenization for Videos\" by Ryoo, Michael S. et al. Venue: NeurIPS 2021, arXiv:2106.11297.\n\n3. yin2022avit: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\" by Yin, Hongxu et al. Venue: CVPR 2022, arXiv:2112.07658.\n\n4. meng2022adavit: \"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition\" by Meng, Lingchen et al. Venue: CVPR 2022, arXiv:2111.15668.\n\n5. chen2023sparsevit: \"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer\" by Chen, Xuanyao et al. Venue: CVPR 2023, arXiv:2303.17605.\n\n6. ye2025fitprune: \"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models\" by Ye, Weihao et al. Venue: AAAI 2025, arXiv:2409.10197.\n\n7. shi2024crossget: \"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers\" by Shi, Dachuan et al. Venue: ICML 2024, arXiv:2305.17455.\n\n8. zhang2024fastervlm: \"[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make VLM Inference Faster\" by Zhang, Qizhe et al. arXiv:2412.01818, year 2024.\n\n9. liu2024llava15: \"Improved Baselines with Visual Instruction Tuning\" by Liu, Haotian et al. Venue: CVPR 2024, arXiv:2310.03744.\n\n10. chen2024internvl25: \"Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling\" by Chen, Zhe et al. arXiv:2412.05271, year 2024.\n\nFor each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "4ee47d28-c6dc-4564-b9b3-6bf90c4f8518",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyFVwDpqmf2wFz9bsVHa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 100682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6753
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 191_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a60bb5211889d0842",
  "tool_use_id": "toolu_01Qkkz3XixZywawXoLKe6w4A",
  "description": "Verify bib entries batch 5",
  "task_type": "local_agent",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. lewis2020bart: \"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension\" by Lewis, Mike et al. Venue: ACL 2020.\n\n2. ryoo2021tokenlearner: \"TokenLearner: Adaptive Space-Time Tokenization for Videos\" by Ryoo, Michael S. et al. Venue: NeurIPS 2021, arXiv:2106.11297.\n\n3. yin2022avit: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\" by Yin, Hongxu et al. Venue: CVPR 2022, arXiv:2112.07658.\n\n4. meng2022adavit: \"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition\" by Meng, Lingchen et al. Venue: CVPR 2022, arXiv:2111.15668.\n\n5. chen2023sparsevit: \"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer\" by Chen, Xuanyao et al. Venue: CVPR 2023, arXiv:2303.17605.\n\n6. ye2025fitprune: \"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models\" by Ye, Weihao et al. Venue: AAAI 2025, arXiv:2409.10197.\n\n7. shi2024crossget: \"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers\" by Shi, Dachuan et al. Venue: ICML 2024, arXiv:2305.17455.\n\n8. zhang2024fastervlm: \"[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make VLM Inference Faster\" by Zhang, Qizhe et al. arXiv:2412.01818, year 2024.\n\n9. liu2024llava15: \"Improved Baselines with Visual Instruction Tuning\" by Liu, Haotian et al. Venue: CVPR 2024, arXiv:2310.03744.\n\n10. chen2024internvl25: \"Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling\" by Chen, Zhe et al. arXiv:2412.05271, year 2024.\n\nFor each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences.",
  "uuid": "3e97de3a-78bd-4ad3-b054-cd861a534bd2",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


## Round 5

## Round 5

55 recorded events


### User

_source line 192 · 2026-05-29T06:52:26.308Z_

You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.

Entries to verify:

1. lewis2020bart: "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension" by Lewis, Mike et al. Venue: ACL 2020.

2. ryoo2021tokenlearner: "TokenLearner: Adaptive Space-Time Tokenization for Videos" by Ryoo, Michael S. et al. Venue: NeurIPS 2021, arXiv:2106.11297.

3. yin2022avit: "A-ViT: Adaptive Tokens for Efficient Vision Transformer" by Yin, Hongxu et al. Venue: CVPR 2022, arXiv:2112.07658.

4. meng2022adavit: "AdaViT: Adaptive Vision Transformers for Efficient Image Recognition" by Meng, Lingchen et al. Venue: CVPR 2022, arXiv:2111.15668.

5. chen2023sparsevit: "SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer" by Chen, Xuanyao et al. Venue: CVPR 2023, arXiv:2303.17605.

6. ye2025fitprune: "Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models" by Ye, Weihao et al. Venue: AAAI 2025, arXiv:2409.10197.

7. shi2024crossget: "CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers" by Shi, Dachuan et al. Venue: ICML 2024, arXiv:2305.17455.

8. zhang2024fastervlm: "[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make VLM Inference Faster" by Zhang, Qizhe et al. arXiv:2412.01818, year 2024.

9. liu2024llava15: "Improved Baselines with Visual Instruction Tuning" by Liu, Haotian et al. Venue: CVPR 2024, arXiv:2310.03744.

10. chen2024internvl25: "Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling" by Chen, Zhe et al. arXiv:2412.05271, year 2024.

For each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Qkkz3XixZywawXoLKe6w4A",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "30cf6ea1-d40b-4403-b65f-762d5667ce57"
}
```

</details>

---


### System

_source line 193_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for Shi Wenzhe \"Real-Time Single Image and Video Supe…",
  "usage": {
    "total_tokens": 20624,
    "tool_uses": 9,
    "duration_ms": 21690
  },
  "last_tool_name": "WebSearch",
  "uuid": "da69d4fa-b113-41ff-a869-4951ce1de8d4",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### Tool call

_source line 194_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TXsqXCxkzr2QQvtpzdezoo`</summary>

```json
{
  "query": "Shi Wenzhe \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" CVPR 2016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "ec8bb1f2-9a63-4a50-b0e3-1fe99cac1b98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdWF1tpcQstPAmsLVFudyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1241,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 16451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2906,
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

_source line 195_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for Li Junnan \"BLIP-2: Bootstrapping Language-Image P…",
  "usage": {
    "total_tokens": 20625,
    "tool_uses": 10,
    "duration_ms": 22786
  },
  "last_tool_name": "WebSearch",
  "uuid": "35b3f39c-3299-40cb-9503-0b42ae15e2b1",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 196_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for Alayrac Jean-Baptiste \"Flamingo: a Visual Languag…",
  "usage": {
    "total_tokens": 20626,
    "tool_uses": 11,
    "duration_ms": 23069
  },
  "last_tool_name": "WebSearch",
  "uuid": "1d64c1bf-cf66-41f6-a320-a33029757b4a",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 197_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a60bb5211889d0842",
  "tool_use_id": "toolu_01Qkkz3XixZywawXoLKe6w4A",
  "description": "Verify bib entries batch 5",
  "usage": {
    "total_tokens": 14985,
    "tool_uses": 1,
    "duration_ms": 3083
  },
  "last_tool_name": "ToolSearch",
  "uuid": "ed24136b-3c2c-4c8f-9316-c579e0a6181f",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 198_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3d8459fe8a20ddf2",
  "tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "description": "Searching for DINOv2 Learning Robust Visual Features without Su…",
  "usage": {
    "total_tokens": 17408,
    "tool_uses": 3,
    "duration_ms": 14383
  },
  "last_tool_name": "WebSearch",
  "uuid": "2e9c9dd8-ab17-4a51-8a91-d933e0561776",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 199_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for arxiv 2511.18950 Compressor-VLA year 2025 confere…",
  "usage": {
    "total_tokens": 29194,
    "tool_uses": 17,
    "duration_ms": 51370
  },
  "last_tool_name": "WebSearch",
  "uuid": "b096309b-a315-424c-8e0c-bd25086c5a48",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 200_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for \"See What Matters\" Feng Yixu authors full list ar…",
  "usage": {
    "total_tokens": 29195,
    "tool_uses": 18,
    "duration_ms": 52437
  },
  "last_tool_name": "WebSearch",
  "uuid": "c203f416-3e4e-49d7-828c-bd5a12def696",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 201_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a60bb5211889d0842",
  "tool_use_id": "toolu_01Qkkz3XixZywawXoLKe6w4A",
  "description": "Searching for BART Denoising Sequence-to-Sequence Pre-training …",
  "usage": {
    "total_tokens": 16450,
    "tool_uses": 2,
    "duration_ms": 5810
  },
  "last_tool_name": "WebSearch",
  "uuid": "2397fcab-5226-466a-b7f9-dfdc5e6b831f",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 202_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for arxiv 2510.08464 \"Don't Run with Scissors\" Jabbou…",
  "usage": {
    "total_tokens": 29196,
    "tool_uses": 19,
    "duration_ms": 53909
  },
  "last_tool_name": "WebSearch",
  "uuid": "dc076e1e-02af-420e-a4ac-044d202f7228",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 203_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acf726f8c121bd88b",
  "tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "description": "Searching for SparseVLM authors full list \"Yuan Zhang\" \"Fan Chu…",
  "usage": {
    "total_tokens": 29197,
    "tool_uses": 20,
    "duration_ms": 54389
  },
  "last_tool_name": "WebSearch",
  "uuid": "779bc986-cbca-4817-95cd-d8c85b25cca3",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 204_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for pi0.5 CoRL 2025 PMLR 305 pages 17-40 proceedings …",
  "usage": {
    "total_tokens": 29687,
    "tool_uses": 17,
    "duration_ms": 43071
  },
  "last_tool_name": "WebSearch",
  "uuid": "db28802d-caf3-42ed-bfe5-955ab2ebe174",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 205_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for RT-1 RSS 2023 Robotics Science Systems proceeding…",
  "usage": {
    "total_tokens": 29688,
    "tool_uses": 18,
    "duration_ms": 44010
  },
  "last_tool_name": "WebSearch",
  "uuid": "d573e22f-223e-452d-b922-f81b697c9c87",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 206_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for LLaVA-PruMerge ICCV 2025 venue accepted conference",
  "usage": {
    "total_tokens": 25661,
    "tool_uses": 12,
    "duration_ms": 32464
  },
  "last_tool_name": "WebSearch",
  "uuid": "a2e16470-3dc8-4971-8a30-4b868ef6a7da",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 207_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3cf991f488a9db47",
  "tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "description": "Searching for Octo model team authors list Ghosh Dibya RSS 2024…",
  "usage": {
    "total_tokens": 29689,
    "tool_uses": 19,
    "duration_ms": 45051
  },
  "last_tool_name": "WebSearch",
  "uuid": "e141ce99-bd9c-424a-b95b-15c2b7e709cf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 208_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for EfficientVLA arXiv 2506.10100 authors Yantai Yang…",
  "usage": {
    "total_tokens": 25662,
    "tool_uses": 13,
    "duration_ms": 33934
  },
  "last_tool_name": "WebSearch",
  "uuid": "5317b04b-2e91-40dd-aae2-81a01ae54597",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 209_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acc826eee85a4dc90",
  "tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "description": "Searching for VLA-Pruner 2511.16449 submission date year confer…",
  "usage": {
    "total_tokens": 25663,
    "tool_uses": 14,
    "duration_ms": 34533
  },
  "last_tool_name": "WebSearch",
  "uuid": "c40502e7-254e-4805-aa42-def1e4587e6e",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### System

_source line 210_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a60bb5211889d0842",
  "tool_use_id": "toolu_01Qkkz3XixZywawXoLKe6w4A",
  "description": "Searching for TokenLearner Adaptive Space-Time Tokenization Vid…",
  "usage": {
    "total_tokens": 17502,
    "tool_uses": 3,
    "duration_ms": 14030
  },
  "last_tool_name": "WebSearch",
  "uuid": "9e1b8b0e-9b7a-46df-b851-6e01d603b8bc",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### Tool call

_source line 211_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WKXCrE7oJJEZwdEB1McirN`</summary>

```json
{
  "query": "arxiv 2511.18950 Compressor-VLA year 2025 conference accepted venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "b4b0b357-64bf-458c-a5cf-7216bbe71d15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tio96i1pHQ21jdMKQQqfPT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 24345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4814,
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


### Tool call

_source line 212_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JUhdGpLu8hzy1WxyAVfUPc`</summary>

```json
{
  "query": "\"See What Matters\" Feng Yixu authors full list arXiv 2605.11817"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "8aca5d7e-d959-46ff-a88e-1f6212ae726c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tio96i1pHQ21jdMKQQqfPT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 24345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4814,
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


### Tool call

_source line 213_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011wfmJYVgKinGoDT2BUssVd`</summary>

```json
{
  "query": "arxiv 2510.08464 \"Don't Run with Scissors\" Jabbour conference accepted venue 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "0ece415a-a2ab-4b50-87bb-08589daf7beb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tio96i1pHQ21jdMKQQqfPT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 24345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4814,
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


### Tool call

_source line 214_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015w9YJeMuHBNXQa4CRvNBE4`</summary>

```json
{
  "query": "SparseVLM authors full list \"Yuan Zhang\" \"Fan Chun-Kai\" arXiv 2410.04417"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "df00f6d3-213b-462a-831c-49e5fb91fb76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tio96i1pHQ21jdMKQQqfPT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 24345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4814,
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

_source line 215 · 2026-05-29T06:52:35.755Z_

<details><summary>↩ Tool result · `toolu_01JUhdGpLu8hzy1WxyAVfUPc`</summary>

```text
Web search results for query: ""See What Matters" Feng Yixu authors full list arXiv 2605.11817"

Links: [{"title":"[2605.11817] See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/abs/2605.11817"},{"title":"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/html/2605.11817"},{"title":"Sample-Efficient Deep Learning for COVID-19 Diagnosis Based on CT Scans","url":"https://www.medrxiv.org/content/10.1101/2020.04.13.20063941.full.pdf"},{"title":"Model stability of COVID-19 mortality prediction with biomarkers","url":"https://www.medrxiv.org/content/10.1101/2020.07.29.20161323.full.pdf"},{"title":"Advancing a Vision Foundation Model for Ming-Style Furniture Image Segmentation: A New Dataset and Method","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11722721/"},{"title":"Deep Learning Fusion for COVID-19 Diagnosis","url":"https://www.medrxiv.org/content/10.1101/2020.12.11.20246546.full.pdf"},{"title":"SCOAT-Net: A Novel Network for Segmenting COVID-19 Lung Opacification from CT Images","url":"https://www.medrxiv.org/content/10.1101/2020.09.23.20191726.full.pdf"}]

Based on the search results, I found the information about the paper "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" with arXiv ID 2605.11817.

The full list of authors is: Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, and Chang Xu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "150ce2d8-01e8-457e-8bd4-82f5ba713395"
}
```

</details>

---


### Tool result

_source line 216 · 2026-05-29T06:52:36.938Z_

<details><summary>↩ Tool result · `toolu_01WKXCrE7oJJEZwdEB1McirN`</summary>

```text
Web search results for query: "arxiv 2511.18950 Compressor-VLA year 2025 conference accepted venue"

Links: [{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950"},{"title":"RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.17639"}]

Based on my search results, I found information about the arxiv paper 2511.18950 "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation." However, the search results do not contain information about a 2025 conference acceptance or the venue where it was accepted.

The paper was authored by Juntao Gao and 3 other authors, and the authors are affiliated with the School of Information Science and Technology at Beijing University of Technology, LiAuto Inc., and the Beijing Key Laboratory of Computational Intelligence and Intelligent System. The paper was posted on arxiv on November 24, 2025.

To find information about the conference acceptance and venue, you may want to check the paper's arxiv page directly or look for announcements from the authors regarding conference submissions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "bb93a906-7f6a-4a18-8355-b44f59901443"
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-29T06:52:38.857Z_

<details><summary>↩ Tool result · `toolu_011wfmJYVgKinGoDT2BUssVd`</summary>

```text
Web search results for query: "arxiv 2510.08464 "Don't Run with Scissors" Jabbour conference accepted venue 2025 2026"

Links: [{"title":"[2510.08464] Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/abs/2510.08464"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered | OpenReview","url":"https://openreview.net/forum?id=c8g57pKdXD"},{"title":"Don't run with scissors: young children's knowledge of home safety rules | Request PDF","url":"https://www.researchgate.net/publication/12148912_Don't_run_with_scissors_young_children's_knowledge_of_home_safety_rules"},{"title":"Michael G. Jabbour's articles on arXiv","url":"https://arxiv.org/a/jabbour_m_1.html"},{"title":"Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking","url":"https://arxiv.org/pdf/2602.24009"},{"title":"Stop DDoS Attacking the Research Community with AI-Generated Survey Papers","url":"https://arxiv.org/pdf/2510.09686"},{"title":"Retraction: Prosthetic shape, but not stiffness or height, affects the maximum speed of sprinters with bilateral transtibial amputations","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9803153/"}]

Based on the search results, I found information about the arxiv paper 2510.08464. "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" was submitted on October 9, 2025, with authors Jason Jabbour and 8 others.

The paper describes GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits.

However, the search results do not contain information about the paper being accepted to a specific conference venue in 2025 or 2026. The results show the paper on arXiv and OpenReview, but don't indicate final conference acceptance status. To find that information, you may want to check the OpenReview page directly or search for more recent announcements about conference decisions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "28cf0e5e-bad0-4688-bbce-59e1670b55f1"
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-29T06:52:39.663Z_

<details><summary>↩ Tool result · `toolu_015w9YJeMuHBNXQa4CRvNBE4`</summary>

```text
Web search results for query: "SparseVLM authors full list "Yuan Zhang" "Fan Chun-Kai" arXiv 2410.04417"

Links: [{"title":"[2410.04417] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/abs/2410.04417"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference · Issue #38509 · huggingface/transformers","url":"https://github.com/huggingface/transformers/issues/38509"},{"title":"SparseVLM","url":"https://leofan90.github.io/SparseVLMs.github.io/"},{"title":"Panasonic HD develops “SparseVLM” technology that doubles the processing speed of Vision-Language Models | Innovations/Technologies | Company | Press Releases | Panasonic Newsroom Global","url":"https://news.panasonic.com/global/zh-CHS/press/en250704-2"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004417Z/abstract"},{"title":"(PDF) SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://www.researchgate.net/publication/384698552_SparseVLM_Visual_Token_Sparsification_for_Efficient_Vision-Language_Model_Inference"},{"title":"Chun-Kai Fan","url":"https://www.catalyzex.com/author/Chun-Kai%20Fan"},{"title":"Paper page - SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://huggingface.co/papers/2410.04417"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/html/2410.04417"}]

Based on the search results, I found the complete list of authors for the SparseVLM paper (arXiv 2410.04417). The authors are: Yuan Zhang, Chun-Kai Fan, Junpeng Ma, Wenzhao Zheng, Tao Huang, Kuan Cheng, Denis Gudovskiy, Tomoyuki Okuno, Yohei Nakata, Kurt Keutzer, and Shanghang Zhang.

According to the search results, this research was developed within the framework of the BAIR Open Research Commons led by UC Berkeley, and is the result of collaboration among Yuan Zhang, Chun-Kai Fan and Shanghang Zhang from Peking University, Junpeng Ma from Fudan University, Wenzhao Zheng and Kurt Keutzer from UC Berkeley, Denis Gudovskiy from PRDCA, and Tomoyuki Okuno and Yohei Nakata from Panasonic HD.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NFtBS1um2LsdQ5pgEUrZ76",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "bb2d7542-1524-4c7e-8d2a-2a3eea79a49e"
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-29T06:52:27.651Z_

<details><summary>↩ Tool result · `toolu_01UeFhQmkvQcYqiotSD39uM5`</summary>

```text
Web search results for query: "OpenVLA CoRL 2024 PMLR 270 Kim Pertsch proceedings"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://proceedings.mlr.press/v270/kim25c.html"},{"title":"CoRL.2024 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/CoRL.2024"},{"title":"Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions","url":"https://arxiv.org/html/2505.11214v1"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"CoRL 2024 - Awards","url":"https://2024.corl.org/program/awards"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"8th CoRL 2024: Munich, Germany","url":"https://dblp.org/db/conf/corl/corl2024.html"}]

I found the information you're looking for. The paper "OpenVLA: An Open-Source Vision-Language-Action Model" was published in the Proceedings of The 8th Conference on Robot Learning (CoRL), PMLR volume 270, pages 2679-2713, 2025.

The authors are Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan P Foster, Pannag R Sanketi, Quan Vuong, Thomas Kollar, Benjamin Burchfiel, Russ Tedrake, Dorsa Sadigh, Sergey Levine, Percy Liang, and Chelsea Finn.

The paper addresses how large policies pretrained on Internet-scale vision-language data and diverse robot demonstrations can enable efficient fine-tuning for new robot skills, but notes that widespread adoption of VLAs for robotics has been challenging because existing VLAs are largely closed and inaccessible to the public, and prior work fails to explore methods for efficiently fine-tuning VLAs for new tasks.

The official proceedings page is available at: https://proceedings.mlr.press/v270/kim25c.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "3d7d8919-9a5b-4f1d-a362-32ae8e736486"
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-29T06:52:27.711Z_

<details><summary>↩ Tool result · `toolu_01CZQCe5VNXgzysqLfFxkytP`</summary>

```text
Web search results for query: "pi0 π0 Physical Intelligence CoRL 2025 ICML 2025 accepted conference"

Links: [{"title":"awesome-physical-ai/README.md at main · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/blob/main/README.md"},{"title":"GitHub - keon/awesome-physical-ai: A curated list of academic papers and resources on Physical AI — focusing on Vision-Language-Action (VLA) models, world models, embodied ai, and robotic foundation models.","url":"https://github.com/keon/awesome-physical-ai"},{"title":"Evaluating \\( \\pi_0 \\) in the Wild: Strengths, Problems, and the Future of Generalist Robot Policies","url":"https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/"},{"title":"A review of π0.5 — Scaling Open-World Generalization in Vision-Language-Action Models | by Isaac Edelman | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/a-review-of-%CF%800-5-scaling-open-world-generalization-in-vision-language-action-models-e4cb0d74264e"},{"title":"π0.6 Model Card Physical Intelligence November 17, 2025 1 Introduction","url":"https://website.pi-asset.com/pi06star/PI06_model_card.pdf"},{"title":"Physical Intelligence (π)","url":"https://www.pi.website/"},{"title":"GitHub - lucidrains/pi-zero-pytorch: Implementation of π₀, the robotic foundation model architecture proposed by Physical Intelligence · GitHub","url":"https://github.com/lucidrains/pi-zero-pytorch"}]

Based on the search results, here's what I found about π0 and related Physical Intelligence models:

**π0.5 at CoRL 2025:**
π0.5: a Vision-Language-Action Model with Open-World Generalization was accepted as an oral presentation at CoRL 2025.

**Physical Intelligence Models:**
π0.5 is described as "A Vision-Language-Action Model with Open-World Generalization" released by Physical Intelligence in April 2025, and π0.6 is described as "A VLA that Learns from Experience" released by Physical Intelligence in 2025.

**Conference Information:**
π0.5 appears in the 9th Annual Conference on Robot Learning (CoRL) in 2025.

The search results show information about π0.5 at CoRL 2025, but I did not find specific information about π0 or ICML 2025 acceptances in these results. If you're looking for more specific information about π0 at ICML 2025 or other details, please let me know and I can search further.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "cb69514c-a9f6-45c0-a124-5f3b4620f5c0"
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-29T06:52:27.797Z_

<details><summary>↩ Tool result · `toolu_01L8B5Ms3jw49uACWpCcZs23`</summary>

```text
Web search results for query: "pi0.5 π0.5 CoRL 2025 PMLR 305 proceedings accepted"

Links: [{"title":"GitHub - mlresearch/v305: Proceedings of CoRL 2025 · GitHub","url":"https://github.com/mlresearch/v305"},{"title":"Decentralized Aerial Manipulation of a Cable-Suspended Load Using Multi-Agent Reinforcement Learning","url":"https://proceedings.mlr.press/v305/zeng25a.html"},{"title":"Learning a Unified Policy for Position and Force Control in Legged Loco-Manipulation","url":"https://proceedings.mlr.press/v305/zhi25a.html"},{"title":"π0.5: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/pdf/2504.16054"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/pdf/2512.06951"},{"title":"GitHub - UT-Austin-RPL/openreview-to-pmlr: Making PMLR Proceedings from CoRL OpenReview Data · GitHub","url":"https://github.com/UT-Austin-RPL/openreview-to-pmlr"},{"title":"Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and associated with a particular workshop or conference. Volumes are published online on the PMLR web site. The Series Editors are Neil D. Lawrence and Mark Reid.","url":"https://proceedings.mlr.press/"}]

Based on the search results, I found information about both π0.5 and CoRL 2025 PMLR 305 proceedings:

π0.5 is a vision-language-action model based on π0 that uses co-training on heterogeneous tasks to enable broad generalization. The π0.5 model transfers knowledge from heterogeneous data sources, including other robots, high-level subtask prediction, verbal instructions, and web data, to enable broad generalization across environments and objects.

Regarding CoRL 2025 and PMLR 305, Volume 305 was published by the Proceedings of Machine Learning Research on October 7, 2025, and this represents the Proceedings of The 9th Conference on Robot Learning.

The search results show that π0.5 has been influential in robotics research, as evidenced by subsequent work building on the π0.5 architecture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "eaf1bd5d-0344-4ded-959b-f7750f8f40bf"
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-29T06:52:32.178Z_

<details><summary>↩ Tool result · `toolu_01WG2Ep8r4yDnNzoj3LfUQMt`</summary>

```text
Web search results for query: "VLA-Cache arXiv 2502.02175 authors Siyu Xu Yunke Wang NeurIPS 2025"

Links: [{"title":"[2502.02175] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/abs/2502.02175"},{"title":"GitHub - siyuhsu/vla-cache: [NeurIPS 2025] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching · GitHub","url":"https://github.com/siyuhsu/vla-cache"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching | OpenReview","url":"https://openreview.net/forum?id=QZYZ0Xm58q"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1554&show=1919"},{"title":"(PDF) VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://www.researchgate.net/publication/388685612_VLA-Cache_Towards_Efficient_Vision-Language-Action_Model_via_Adaptive_Token_Caching_in_Robotic_Manipulation"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/pdf/2502.02175"},{"title":"Paper page - VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://huggingface.co/papers/2502.02175"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

**Authors:** Siyu Xu, Yunke Wang, Chenghao Xia, Dihao Zhu, Tao Huang, and Chang Xu

**arXiv ID:** 2502.02175

**Venue:** Accepted by NeurIPS 2025

**Summary:** VLA-Cache is a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames. It exploits temporal continuity in robotic manipulation by identifying minimally changed tokens between adjacent frames and reusing their cached key-value representations, while selectively re-computing task-relevant tokens that are environmentally sensitive to maintain action precision.

The paper is available on arXiv at https://arxiv.org/abs/2502.02175, and the authors have also released code on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "fab8b5eb-ad47-4257-9c35-b21323f99d3c"
}
```

</details>

---


### Tool call

_source line 223_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019xJsLMVyuev7aBf8mJfqkm`</summary>

```json
{
  "query": "pi0.5 CoRL 2025 PMLR 305 pages 17-40 proceedings mlr press"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "7d1b3622-5535-49c9-8a49-3e50efcb327c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWFT2167b4T3dnaqKZMoHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 24020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5624,
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


### Tool call

_source line 224_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012cXrQRu9etvaExRJPGzZM1`</summary>

```json
{
  "query": "RT-1 RSS 2023 Robotics Science Systems proceedings year 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "45f98484-1aba-421d-af49-26cbd6db5ee4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWFT2167b4T3dnaqKZMoHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 24020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5624,
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


### Tool call

_source line 225_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01My1a2sganjtQSD55bEeoAE`</summary>

```json
{
  "query": "Octo model team authors list Ghosh Dibya RSS 2024 arXiv 2405.12213"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "a4ec71ce-4a65-4586-b463-6f0c3b033794",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWFT2167b4T3dnaqKZMoHq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 24020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5624,
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

_source line 226 · 2026-05-29T06:52:40.397Z_

<details><summary>↩ Tool result · `toolu_019xJsLMVyuev7aBf8mJfqkm`</summary>

```text
Web search results for query: "pi0.5 CoRL 2025 PMLR 305 pages 17-40 proceedings mlr press"

Links: [{"title":"GitHub - mlresearch/v305: Proceedings of CoRL 2025 · GitHub","url":"https://github.com/mlresearch/v305"},{"title":"Decentralized Aerial Manipulation of a Cable-Suspended Load Using Multi-Agent Reinforcement Learning","url":"https://proceedings.mlr.press/v305/zeng25a.html"},{"title":"Learning a Unified Policy for Position and Force Control in Legged Loco-Manipulation","url":"https://proceedings.mlr.press/v305/zhi25a.html"},{"title":"Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and associated with a particular workshop or conference. Volumes are published online on the PMLR web site. The Series Editors are Neil D. Lawrence and Mark Reid.","url":"https://proceedings.mlr.press/"},{"title":"Real-Time Out-of-Distribution Failure Prevention via Multi-Modal Reasoning","url":"https://proceedings.mlr.press/v305/ganai25a.html"},{"title":"Stacked conformal prediction","url":"https://proceedings.mlr.press/v266/marques25a.html"},{"title":"GitHub - mlresearch/v267: Proceedings of ICML 2025 · GitHub","url":"https://github.com/mlresearch/v267"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 9th Conference on Robot Learning Held in Seoul, Korea on 27-30 September 2025 Published as Volume 305 by the Proceedings of Machine Learning Research on 07 October 2025. Volume Edited by: Joseph Lim Shuran Song Hae-Won Park Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v305/"}]

Based on the search results, I found information about the proceedings volume you're looking for. The Proceedings of The 9th Conference on Robot Learning (CoRL 2025) was held in Seoul, Korea on 27-30 September 2025 and published as Volume 305 by the Proceedings of Machine Learning Research on 07 October 2025.

The search results show that pages 17-40 of PMLR 305 contain a paper with multiple authors including Kevin Black, Noah Brown, James Darpinian, and others, but the specific title "pi0.5" doesn't appear in the search results. 

The proceedings are available at the PMLR website (proceedings.mlr.press/v305/), and you can access the full table of contents and individual papers through that volume.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "44aa31fa-de56-4a1a-929c-8127bac5a7e2"
}
```

</details>

---


### Tool call

_source line 227_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AMbbsRjgtGBCC38cnBvjTC`</summary>

```json
{
  "query": "Li Junnan \"BLIP-2: Bootstrapping Language-Image Pre-Training\" ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "c3f89927-bdcd-4306-bd56-35155b34d8a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdWF1tpcQstPAmsLVFudyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1241,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 16451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2906,
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


### Tool call

_source line 228_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YNzYHHNMpFvBBeXY2GtVHr`</summary>

```json
{
  "query": "Alayrac Jean-Baptiste \"Flamingo: a Visual Language Model for Few-Shot Learning\" NeurIPS 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "2ac65a79-7dee-4ab8-86fc-d46034e6f53f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdWF1tpcQstPAmsLVFudyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1241,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 16451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2906,
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

_source line 229 · 2026-05-29T06:52:30.566Z_

<details><summary>↩ Tool result · `toolu_01HPUHZffpzfqS2D2BQT9cdP`</summary>

```text
Web search results for query: "Liu Haotian "Visual Instruction Tuning" LLaVA NeurIPS 2023"

Links: [{"title":"Visual Instruction Tuning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf"},{"title":"[Multimodal] LLaVA鍊成術-視覺指令調節 Visual Instruction Tuning - HackMD","url":"https://hackmd.io/@YungHuiHsu/HyMgBbjSa"},{"title":"NeurIPS Poster Visual Instruction Tuning","url":"https://neurips.cc/virtual/2023/poster/70080"},{"title":"GitHub - haotian-liu/LLaVA: [NeurIPS'23 Oral] Visual Instruction Tuning (LLaVA) built towards GPT-4V level capabilities and beyond.","url":"https://github.com/haotian-liu/LLaVA/tree/main"},{"title":"Visual Instruction Tuning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/visual-instruction-tuning/"},{"title":"GitHub - haotian-liu/LLaVA: [NeurIPS'23 Oral] Visual Instruction Tuning (LLaVA) built towards GPT-4V level capabilities and beyond. · GitHub","url":"https://github.com/haotian-liu/llava"},{"title":"LLaVA","url":"https://llava-vl.github.io/"},{"title":"Visual Instruction Tuning | OpenReview","url":"https://openreview.net/forum?id=w0H2xGHlkw"},{"title":"[2304.08485] Visual Instruction Tuning","url":"https://arxiv.org/abs/2304.08485"}]

Based on the web search results, here's what I found:

## Visual Instruction Tuning - NeurIPS 2023

The paper "Visual Instruction Tuning" was presented as an oral presentation at NeurIPS 2023 by Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee.

### Key Contribution

The paper presents the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data. Through instruction tuning on this generated data, the authors introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an LLM for general-purpose visual and language understanding.

### Performance Results

LLaVA demonstrates impressive multimodal chat abilities and yields an 85.1% relative score compared with GPT-4 on a synthetic multimodal instruction-following dataset. Additionally, when fine-tuned on Science QA, the synergy of LLaVA and GPT-4 achieves a new state-of-the-art accuracy of 92.53%.

### Resources

The authors made GPT-4 generated visual instruction tuning data, their model and code base publicly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "17b933de-c37b-431e-9fe9-d3d334844622"
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-29T06:52:32.043Z_

<details><summary>↩ Tool result · `toolu_0169DXnpUg7tiJrFNDryVxpo`</summary>

```text
Web search results for query: "Shang Yuzhang "LLaVA-PruMerge" adaptive token reduction arXiv 2403.15388"

Links: [{"title":"[2403.15388] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388"},{"title":"[2403.15388v4] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v4"},{"title":"[2403.15388v5] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v5"},{"title":"[Paper Review] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://velog.io/@euisuk-chung/LLaVA-PruMerge-Adaptive-Token-Reduction-for-Efficient-Large-Multimodal-Models"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/pdf/2403.15388"},{"title":"Figure 2 from LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLaVA-PruMerge:-Adaptive-Token-Reduction-for-Large-Shang-Cai/c0ef72d02b93065e77c506e23ce9acbbcd945893/figure/2"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"},{"title":"GitHub - 42Shawn/LLaVA-PruMerge: LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models · GitHub","url":"https://github.com/42Shawn/LLaVA-PruMerge"},{"title":"iLLaVA: An Image is Worth Fewer Than 1/3 Input Tokens in Large Multimodal Models","url":"https://arxiv.org/html/2412.06263v1"}]

I found the paper! Here are the key details about the research:

## LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models

**Authors:** Yuzhang Shang, Mu Cai, Bingxin Xu, Yong Jae Lee, Yan Yan

**ArXiv Identifier:** 2403.15388

**Main Contribution:** PruMerge is a novel adaptive visual token reduction approach, which largely reduces the number of visual tokens while maintaining comparable model performance.

**Problem Addressed:** Recent LMMs incorporate more complex visual inputs, such as high-resolution images and videos, which increase the number of visual tokens significantly. However, due to the design of the Transformer architecture, computational costs associated with these models tend to increase quadratically with the number of input tokens.

**Key Results:** PruMerge significantly reduces the computation cost for text generation in LMMs (around 4-10 times in FLOPs for LMM prefill), while can maintain comparable performance.

**Adaptive Selection:** PruMerge can adaptively select visual tokens based on the information density of the visual input, enabling the LLM to perceive visual input effectively and efficiently. More attentive tokens are sampled in complex images such as ones with text, while fewer are sampled on simpler images.

The code is available on [GitHub](https://github.com/42Shawn/LLaVA-PruMerge).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "329263f0-9830-4e34-93f0-f7cc14a8dc85"
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-29T06:52:32.460Z_

<details><summary>↩ Tool result · `toolu_01TXsqXCxkzr2QQvtpzdezoo`</summary>

```text
Web search results for query: "Shi Wenzhe "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network" CVPR 2016"

Links: [{"title":"CVPR 2016 Open Access Repository","url":"https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Shi_Real-Time_Single_Image_CVPR_2016_paper.html"},{"title":"[1609.05158] Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network","url":"https://arxiv.org/abs/1609.05158"},{"title":"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network - Technical University of Munich","url":"https://portal.fis.tum.de/en/publications/real-time-single-image-and-video-super-resolution-using-an-effici/"},{"title":"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network [Quick Review]","url":"https://liner.com/review/realtime-single-image-and-video-superresolution-using-efficient-subpixel-convolutional"},{"title":"dblp: Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network.","url":"https://dblp.org/rec/conf/cvpr/ShiCHTABRW16.html"},{"title":"[PDF] Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Real-Time-Single-Image-and-Video-Super-Resolution-Shi-Caballero/03a5b2aac53443e6078f0f63b35d4f95d6d54c5d"},{"title":"(PDF) Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network (2016) | Wenzhe Shi | 7465 Citations","url":"https://scispace.com/papers/real-time-single-image-and-video-super-resolution-using-an-4ljje8ipch"},{"title":"Real-Time Single Image and Video Super-Resolution Using an Efficient   Sub-Pixel Convolutional Neural Network","url":"https://arxiv.org/pdf/1609.05158"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network"

**Authors:** Shi, Wenzhe; Caballero, Jose; Huszar, Ferenc; Totz, Johannes; Aitken, Andrew P.; Bishop, Rob; Rueckert, Daniel; and Wang, Zehan

**Conference:** Published at CVPR (IEEE Conference on Computer Vision and Pattern Recognition) in June 2016

**Key Contributions:** The paper introduces an efficient sub-pixel convolution layer which learns an array of upscaling filters to upscale the final LR feature maps into the HR output, replacing the handcrafted bicubic filter in the SR pipeline with more complex upscaling filters specifically trained for each feature map, whilst also reducing the computational complexity.

**Performance:** The proposed approach performs significantly better (+0.15dB on Images and +0.39dB on Videos) and is an order of magnitude faster than previous CNN-based methods.

The paper is available through the CVPR Open Access Repository and on arXiv (arXiv:1609.05158).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "971617f9-4f97-48e0-89be-06b5297c7ad6"
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-29T06:52:32.922Z_

<details><summary>↩ Tool result · `toolu_01YNzYHHNMpFvBBeXY2GtVHr`</summary>

```text
Web search results for query: "Alayrac Jean-Baptiste "Flamingo: a Visual Language Model for Few-Shot Learning" NeurIPS 2022"

Links: [{"title":"Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/960a172bc7fbf0177ccccbb411a7d800-Abstract-Conference.html"},{"title":"28-04-2022 Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/tackling-multiple-tasks-with-a-single-visual-language-model/flamingo.pdf"},{"title":"[2204.14198] Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://arxiv.org/abs/2204.14198"},{"title":"[PDF] Flamingo: a Visual Language Model for Few-Shot Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Flamingo:-a-Visual-Language-Model-for-Few-Shot-Alayrac-Donahue/26218bdcc3945c7edae7aa2adbfba4cd820a2df3"},{"title":"Flamingo: a visual language model for few-shot learning - ORA - Oxford University Research Archive","url":"https://ora.ox.ac.uk/objects/uuid:72fd0848-5ee3-43fa-bdab-d777270d7a58"},{"title":"Flamingo: a Visual - Language Model for Few-Shot Learning","url":"https://faculty.cc.gatech.edu/~zk15/teaching/AY2024_cs8803vlm_fall/slides/L10_Flamingo.pdf"},{"title":"Flamingo: a Visual Language Model for Few-Shot Learning - Samuel Albanie","url":"https://samuelalbanie.com/digests/2022-05-flamingo/"},{"title":"Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://arxiv.org/pdf/2204.14198"}]

I found the search results for your query. Here's what I found:

"Flamingo: a Visual Language Model for Few-Shot Learning" is a paper by Jean-Baptiste Alayrac and colleagues, published at NeurIPS 2022 (Advances in Neural Information Processing Systems 35), that introduces Flamingo, a family of Visual Language Models designed to rapidly adapt to novel tasks using only a handful of annotated examples.

The paper proposes key architectural innovations to bridge powerful pretrained vision-only and language-only models, handle sequences of arbitrarily interleaved visual and textual data, and seamlessly ingest images or videos as inputs. Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which enables them with in-context few-shot learning capabilities.

The paper was initially posted on arXiv in April 2022 and later published at the NeurIPS 2022 conference. The official proceedings can be found at the NeurIPS website, and the PDF is available through multiple sources including arXiv and DeepMind's official channels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "90b0f0b8-2ede-4cd1-b80f-838a9f554fee"
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-29T06:52:33.737Z_

<details><summary>↩ Tool result · `toolu_01AMbbsRjgtGBCC38cnBvjTC`</summary>

```text
Web search results for query: "Li Junnan "BLIP-2: Bootstrapping Language-Image Pre-Training" ICML 2023"

Links: [{"title":"ICML Poster BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://icml.cc/virtual/2023/poster/25182"},{"title":"[Paper Note] BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models, Junnan Li+, ICML'23, 2023.01 · Issue #4464 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4464"},{"title":"BLIP-2: bootstrapping language-image pre-training with ...","url":"https://dl.acm.org/doi/10.5555/3618408.3619222"},{"title":"[2301.12597] BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://arxiv.org/abs/2301.12597"},{"title":"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models [Quick Review]","url":"https://liner.com/review/blip2-bootstrapping-languageimage-pretraining-with-frozen-image-encoders-and-large"},{"title":"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image   Encoders and Large Language Models","url":"https://arxiv.org/pdf/2301.12597"},{"title":"Paper page - BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://huggingface.co/papers/2301.12597"},{"title":"BLIP-2: Bootstrapping Language-Image Pre-training with ...","url":"https://proceedings.mlr.press/v202/li23q/li23q.pdf"},{"title":"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models - Singapore Management University","url":"https://smusg.elsevierpure.com/en/publications/blip-2-bootstrapping-language-image-pre-training-with-frozen-imag"},{"title":"[2201.12086] BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation","url":"https://arxiv.org/abs/2201.12086"}]

I found information about the BLIP-2 paper by Li Junnan and colleagues. Here are the search results:

## Paper Information

The paper "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models" was authored by Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi and presented as a 2023 poster at ICML.

## Paper Details

The paper proposes BLIP-2, a generic and efficient pre-training strategy that bootstraps vision-language pre-training from off-the-shelf frozen pre-trained image encoders and frozen large language models. BLIP-2 bridges the modality gap with a lightweight Querying Transformer, which is pre-trained in two stages.

The first stage bootstraps vision-language representation learning from a frozen image encoder, and the second stage bootstraps vision-to-language generative learning from a frozen language model.

## Key Results

BLIP-2 achieves state-of-the-art performance on various vision-language tasks despite having significantly fewer trainable parameters than existing methods, for example, outperforming Flamingo80B by 8.7% on zero-shot VQAv2 with 54× fewer trainable parameters.

The paper was published on July 23, 2023, and is available through the ICML proceedings and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "cf29c578-3f52-4f8f-b9f5-f07ca27d8005"
}
```

</details>

---


### Tool call

_source line 234_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y9wCWV2yNKGf9PNKGyskSi`</summary>

```json
{
  "query": "LLaVA-PruMerge ICCV 2025 venue accepted conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "7a9f935a-00ec-4b6f-b198-8b6b91e60a53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bhg66Xc4WUXd85GgsYJ4HU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 818,
      "cache_creation_input_tokens": 5456,
      "cache_read_input_tokens": 19357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5456,
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


### Tool call

_source line 235_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011B4FCSnJ4mfKEVLyDzwkWt`</summary>

```json
{
  "query": "EfficientVLA arXiv 2506.10100 authors Yantai Yang full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "efda3e48-97e7-429d-b4a5-4698eab91cf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bhg66Xc4WUXd85GgsYJ4HU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 818,
      "cache_creation_input_tokens": 5456,
      "cache_read_input_tokens": 19357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5456,
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


### Tool call

_source line 236_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FbbzNUJJG7sqpkbCKG29W9`</summary>

```json
{
  "query": "VLA-Pruner 2511.16449 submission date year conference venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KKaDBJv4mnT99dsNx1Wg5z",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "8bfcba61-1598-497c-bb4d-d3ced913bd7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bhg66Xc4WUXd85GgsYJ4HU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 818,
      "cache_creation_input_tokens": 5456,
      "cache_read_input_tokens": 19357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5456,
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

_source line 237 · 2026-05-29T06:52:27.200Z_

<details><summary>↩ Tool result · `toolu_01LcFjxtgg4g4frmEA5wBZsE`</summary>

```text
Web search results for query: "Perceiver General Perception with Iterative Attention Jaegle ICML 2021"

Links: [{"title":"Perceiver: General Perception with Iterative Attention - researchr publication","url":"https://researchr.org/publication/JaegleGBVZC21"},{"title":"Perceiver: General Perception with Iterative Attention - Crossminds","url":"https://crossminds.ai/video/perceiver-general-perception-with-iterative-attention-614bd1eb3c7a224a9090303b/"},{"title":"Perceiver: General Perception with Iterative Attention — Paper summary | by Gowthami Somepalli | ML Summaries | Medium","url":"https://medium.com/ml-summaries/perceiver-paper-s-summary-3c589ec74238"},{"title":"[2103.03206] Perceiver: General Perception with Iterative Attention","url":"https://arxiv.org/abs/2103.03206"},{"title":"[2103.03206v2] Perceiver: General Perception with Iterative Attention","url":"https://arxiv.org/abs/2103.03206v2"},{"title":"[Quick Review] Perceiver: General Perception with Iterative Attention","url":"https://liner.com/review/perceiver-general-perception-with-iterative-attention"},{"title":"Perceiver: General Perception with Iterative Attention","url":"https://proceedings.mlr.press/v139/jaegle21a/jaegle21a.pdf"},{"title":"ICML Poster Perceiver: General Perception with Iterative Attention","url":"https://icml.cc/virtual/2021/poster/10291"},{"title":"ICML 2021 Perceiver: General Perception with Iterative Attention Spotlight","url":"https://icml.cc/virtual/2021/spotlight/10292"},{"title":"Perceiver: General Perception with Iterative Attention","url":"https://arxiv.org/pdf/2103.03206"}]

Based on the search results, here's information about the paper:

## Perceiver: General Perception with Iterative Attention

This paper was authored by Andrew Jaegle, Felix Gimeno, Andy Brock, Oriol Vinyals, Andrew Zisserman, and João Carreira, and was published at ICML 2021 (the 38th International Conference on Machine Learning, July 18-24, 2021).

### Key Innovation
The model leverages an asymmetric attention mechanism to iteratively distill inputs into a tight latent bottleneck, allowing it to scale to handle very large inputs. The Perceiver iteratively attends to the input byte array by alternating cross-attention and latent self-attention blocks.

### Main Contribution
Perceiver is a mode-agnostic transformer without any mode-specific priors which can be applied to raw data without much processing. The architecture is competitive with or outperforms strong, specialized models on classification tasks across various modalities: images, point clouds, audio, video, and video+audio.

### Performance
The Perceiver obtains performance comparable to ResNet-50 and ViT on ImageNet without 2D convolutions by directly attending to 50,000 pixels.

The paper is available on arxiv at https://arxiv.org/abs/2103.03206 and the official PMLR proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "54d89d6f-88e8-4d6c-bfcf-b79cef438610"
}
```

</details>

---


### Tool call

_source line 238_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G1GXryXQJbkLKQP8YHPsEN`</summary>

```json
{
  "query": "DINOv2 Learning Robust Visual Features without Supervision Oquab TMLR 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "eaabbb03-4fbe-4ca3-a882-1dae20748838",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Msg8XZmTunS51DUfJzZdtj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 16392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 945,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
      "service_tier": "standard",
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

_source line 239 · 2026-05-29T06:52:38.526Z_

<details><summary>↩ Tool result · `toolu_01G1GXryXQJbkLKQP8YHPsEN`</summary>

```text
Web search results for query: "DINOv2 Learning Robust Visual Features without Supervision Oquab TMLR 2024 arXiv"

Links: [{"title":"DINOv2: Learning Robust Visual Features Without Supervision | ML Anthology","url":"https://mlanthology.org/tmlr/2024/oquab2024tmlr-dinov2/"},{"title":"DINOv2: Learning Robust Visual Features without Supervision | by Jim Canary | Medium","url":"https://medium.com/@jimcanary/dinov2-learning-robust-visual-features-without-supervision-bfd1cd94cbdd"},{"title":"DINOv2: Learning Robust Visual Features without ...","url":"https://hal.science/hal-04376640v2/file/CVPR_2023_dinov2%20(4).pdf"},{"title":"Published in Transactions on Machine Learning Research (01/2024)","url":"https://arxiv.org/pdf/2304.07193"},{"title":"DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/html/2304.07193v2"},{"title":"[2304.07193] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193"},{"title":"DINOv2: Learning Robust Visual Features without Supervision | OpenReview","url":"https://openreview.net/forum?id=a68SUt6zFt"},{"title":"DINOv2: Learning Robust Visual Features without Supervision | Request PDF","url":"https://www.researchgate.net/publication/370058767_DINOv2_Learning_Robust_Visual_Features_without_Supervision"},{"title":"Accepted papers at TMLR on X: \"DINOv2: Learning Robust Visual Features without Supervision Maxime Oquab, Timothée Darcet, Théo Moutakanni et al.. Action editor: Abhishek Kumar. https://t.co/M0YHJp3SuI #supervised #visual #features\" / X","url":"https://x.com/TmlrPub/status/1749446940125757691"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** DINOv2: Learning Robust Visual Features Without Supervision, published in Transactions on Machine Learning Research, 2024

**Authors:** Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy V. Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, Mahmoud Assran, Nicolas Ballas, Wojciech Galuba, Russell Howes, Po-Yao Huang, Shang-Wen Li, Ishan Misra, Michael Rabbat, Vasu Sharma, Gabriel Synnaeve, Hu Xu, Hervé Jegou, Julien Mairal, Patrick Labatut, Armand Joulin, Piotr Bojanowski from Meta AI Research and Inria.

**Abstract:** The paper addresses how recent breakthroughs in natural language processing for model pretraining on large quantities of data have opened the way for similar foundation models in computer vision, which could produce all-purpose visual features that work across image distributions and tasks without finetuning.

**Key Contributions:** The work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources. They revisit existing approaches and combine different techniques to scale pretraining in terms of data and model size, with most technical contributions aiming at accelerating and stabilizing training at scale. They also propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of uncurated data.

**Available Resources:**
- arXiv paper 2304.07193
- OpenReview and Code
- Official TMLR publication link


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "c2d5f3ee-9172-46f5-8a37-7aa52156f7a7"
}
```

</details>

---


### Tool call

_source line 240_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Po2TsHDP6TubE5PRwysVsc`</summary>

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
  "parent_tool_use_id": "toolu_01Qkkz3XixZywawXoLKe6w4A",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "73ea1fa0-9da0-48fe-9f03-cc3ea16295ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016m32nfgyUyJQXCUepd12YV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6714,
      "cache_read_input_tokens": 8258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6714,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 241 · 2026-05-29T06:52:29.398Z_

<details><summary>↩ Tool result · `toolu_01Po2TsHDP6TubE5PRwysVsc`</summary>

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
  "parent_tool_use_id": "toolu_01Qkkz3XixZywawXoLKe6w4A",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "302a5428-6ee3-41eb-8912-6c771cedc3e5"
}
```

</details>

---


### Tool call

_source line 242_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HjdkvekrRdb7rcutdiVQ1p`</summary>

```json
{
  "query": "BART Denoising Sequence-to-Sequence Pre-training Lewis 2020 ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Qkkz3XixZywawXoLKe6w4A",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "19418450-bffc-4032-840a-14fb1e2396e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNYce6KBiqTD4jTLvr2JT2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 14972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 243 · 2026-05-29T06:52:37.865Z_

<details><summary>↩ Tool result · `toolu_01HjdkvekrRdb7rcutdiVQ1p`</summary>

```text
Web search results for query: "BART Denoising Sequence-to-Sequence Pre-training Lewis 2020 ACL"

Links: [{"title":"BART- Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension","url":"https://hyunyoung2.github.io//2021/01/21/BART/"},{"title":"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.703/"},{"title":"BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/bart-denoising-sequence-to-sequence-pre-training-for-natural-lang-2"},{"title":"(PDF) BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension (2020) | Michael Lewis | 11177 Citations","url":"https://scispace.com/papers/bart-denoising-sequence-to-sequence-pre-training-for-natural-24rhunb8w5"},{"title":"[PDF] BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BART:-Denoising-Sequence-to-Sequence-Pre-training-Lewis-Liu/395de0bd3837fdf4b4b5e5f04835bcc69c279481"},{"title":"Multilingual Denoising Pre-training for Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/2020.tacl-1.47/"},{"title":"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension | Request PDF","url":"https://www.researchgate.net/publication/343301801_BART_Denoising_Sequence-to-Sequence_Pre-training_for_Natural_Language_Generation_Translation_and_Comprehension"}]

Based on the search results, here's information about the BART paper:

## BART: Denoising Sequence-to-Sequence Pre-training

The paper "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension" was published by Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer at the 58th Annual Meeting of the Association for Computational Linguistics in 2020.

### What is BART?

BART is a denoising autoencoder for pretraining sequence-to-sequence models, trained by corrupting text with an arbitrary noising function and learning a model to reconstruct the original text. It uses a standard Transformer-based neural machine translation architecture which can be seen as generalizing BERT (due to the bidirectional encoder), GPT (with the left-to-right decoder), and other recent pretraining schemes.

### Performance

BART is particularly effective when fine-tuned for text generation but also works well for comprehension tasks, matching the performance of RoBERTa on GLUE and SQuAD, and achieving new state-of-the-art results on a range of abstractive dialogue, question answering, and summarization tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Qkkz3XixZywawXoLKe6w4A",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "e500ba33-81c6-4091-b564-9b3043e1ae9a"
}
```

</details>

---


### Tool call

_source line 244_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QxdD2xsxdXQLNh7aR8wRG7`</summary>

```json
{
  "query": "TokenLearner Adaptive Space-Time Tokenization Videos Ryoo NeurIPS 2021 arXiv 2106.11297"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Qkkz3XixZywawXoLKe6w4A",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "2d8534c5-99f1-4f04-90a1-be775462dbc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZwhcZtL9au9Xj5DP4HZ8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 997,
      "cache_read_input_tokens": 16433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 997,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
      "service_tier": "standard",
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

_source line 245_

<details open><summary>🔧 Tool call — Agent · `toolu_01B15dS1MQZV5QHK1jyFbtaw`</summary>

```json
{
  "description": "Verify bib entries batch 6",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. chen2024internvl: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\" by Chen, Zhe et al. arXiv:2404.16821, year 2024.\n\n2. gao2024miniinternvl: \"Mini-InternVL: A Flexible-Transfer Pocket Multimodal Model with 5% Parameters and 90% Performance\" by Gao, Zhangwei et al. arXiv:2410.16261, year 2024.\n\n3. zitkovich2023rt2: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun et al. Venue: CoRL 2023, arXiv:2307.15818. NOTE: There is also a brohan2023rt2 entry for the same paper with different first authors (Brohan, Anthony et al.). This may be a duplicate.\n\n4. openxembodiment2024: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\" by Open X-Embodiment Collaboration. Venue: ICRA 2024, arXiv:2310.08864.\n\n5. zhang2023h2o: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\" by Zhang, Zhenyu et al. Venue: NeurIPS 2023, arXiv:2306.14048.\n\n6. xiao2024streamingllm: \"Efficient Streaming Language Models with Attention Sinks\" by Xiao, Guangxuan et al. Venue: ICLR 2024, arXiv:2309.17453.\n\n7. mees2022calvin: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\" by Mees, Oier et al. Venue: IEEE RA-L 2022, arXiv:2112.03227.\n\n8. chi2023diffusionpolicy: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\" by Chi, Cheng et al. Venue: RSS 2023, arXiv:2303.04137.\n\n9. zeng2023transformers_tsf: \"Are Transformers Effective for Time Series Forecasting?\" by Zeng, Ailing et al. Venue: AAAI 2023, arXiv:2205.13504.\n\n10. bouthillier2024negative: \"Position: Embracing Negative Results in Machine Learning\" by Bouthillier, Xavier et al. Venue: ICML 2024, arXiv:2406.03980.\n\n11. oquab2024dinov2: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime et al. Venue: TMLR 2024, arXiv:2304.07193. NOTE: This appears to be a duplicate of oquab2023dinov2 which lists the same paper.\n\n12. su2024roformer: \"RoFormer: Enhanced Transformer with Rotary Position Embedding\" by Su, Jianlin et al. Venue: Neurocomputing vol 568, 2024.\n\nFor each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "a8a9780b-cfa8-4e47-8b33-79a6478d727c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyFVwDpqmf2wFz9bsVHa2k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6753,
      "cache_read_input_tokens": 100682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6753
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 246_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ad4c2f5491bd07bc7",
  "tool_use_id": "toolu_01B15dS1MQZV5QHK1jyFbtaw",
  "description": "Verify bib entries batch 6",
  "task_type": "local_agent",
  "prompt": "You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.\n\nEntries to verify:\n\n1. chen2024internvl: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\" by Chen, Zhe et al. arXiv:2404.16821, year 2024.\n\n2. gao2024miniinternvl: \"Mini-InternVL: A Flexible-Transfer Pocket Multimodal Model with 5% Parameters and 90% Performance\" by Gao, Zhangwei et al. arXiv:2410.16261, year 2024.\n\n3. zitkovich2023rt2: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun et al. Venue: CoRL 2023, arXiv:2307.15818. NOTE: There is also a brohan2023rt2 entry for the same paper with different first authors (Brohan, Anthony et al.). This may be a duplicate.\n\n4. openxembodiment2024: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\" by Open X-Embodiment Collaboration. Venue: ICRA 2024, arXiv:2310.08864.\n\n5. zhang2023h2o: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\" by Zhang, Zhenyu et al. Venue: NeurIPS 2023, arXiv:2306.14048.\n\n6. xiao2024streamingllm: \"Efficient Streaming Language Models with Attention Sinks\" by Xiao, Guangxuan et al. Venue: ICLR 2024, arXiv:2309.17453.\n\n7. mees2022calvin: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\" by Mees, Oier et al. Venue: IEEE RA-L 2022, arXiv:2112.03227.\n\n8. chi2023diffusionpolicy: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\" by Chi, Cheng et al. Venue: RSS 2023, arXiv:2303.04137.\n\n9. zeng2023transformers_tsf: \"Are Transformers Effective for Time Series Forecasting?\" by Zeng, Ailing et al. Venue: AAAI 2023, arXiv:2205.13504.\n\n10. bouthillier2024negative: \"Position: Embracing Negative Results in Machine Learning\" by Bouthillier, Xavier et al. Venue: ICML 2024, arXiv:2406.03980.\n\n11. oquab2024dinov2: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime et al. Venue: TMLR 2024, arXiv:2304.07193. NOTE: This appears to be a duplicate of oquab2023dinov2 which lists the same paper.\n\n12. su2024roformer: \"RoFormer: Enhanced Transformer with Rotary Position Embedding\" by Su, Jianlin et al. Venue: Neurocomputing vol 568, 2024.\n\nFor each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences.",
  "uuid": "2eb5b35e-fe81-4231-9fa7-16fccc00fd9d",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


## Round 6

## Round 6

229 recorded events


### User

_source line 247 · 2026-05-29T06:52:40.794Z_

You are verifying academic paper references. For each entry below, search the web (use WebSearch) to verify: (1) the paper exists, (2) authors are correct, (3) title is exact, (4) year is correct, (5) venue is correct, (6) arXiv ID is correct if present. Report any discrepancies.

Entries to verify:

1. chen2024internvl: "How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites" by Chen, Zhe et al. arXiv:2404.16821, year 2024.

2. gao2024miniinternvl: "Mini-InternVL: A Flexible-Transfer Pocket Multimodal Model with 5% Parameters and 90% Performance" by Gao, Zhangwei et al. arXiv:2410.16261, year 2024.

3. zitkovich2023rt2: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" by Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun et al. Venue: CoRL 2023, arXiv:2307.15818. NOTE: There is also a brohan2023rt2 entry for the same paper with different first authors (Brohan, Anthony et al.). This may be a duplicate.

4. openxembodiment2024: "Open X-Embodiment: Robotic Learning Datasets and RT-X Models" by Open X-Embodiment Collaboration. Venue: ICRA 2024, arXiv:2310.08864.

5. zhang2023h2o: "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models" by Zhang, Zhenyu et al. Venue: NeurIPS 2023, arXiv:2306.14048.

6. xiao2024streamingllm: "Efficient Streaming Language Models with Attention Sinks" by Xiao, Guangxuan et al. Venue: ICLR 2024, arXiv:2309.17453.

7. mees2022calvin: "CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks" by Mees, Oier et al. Venue: IEEE RA-L 2022, arXiv:2112.03227.

8. chi2023diffusionpolicy: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion" by Chi, Cheng et al. Venue: RSS 2023, arXiv:2303.04137.

9. zeng2023transformers_tsf: "Are Transformers Effective for Time Series Forecasting?" by Zeng, Ailing et al. Venue: AAAI 2023, arXiv:2205.13504.

10. bouthillier2024negative: "Position: Embracing Negative Results in Machine Learning" by Bouthillier, Xavier et al. Venue: ICML 2024, arXiv:2406.03980.

11. oquab2024dinov2: "DINOv2: Learning Robust Visual Features without Supervision" by Oquab, Maxime et al. Venue: TMLR 2024, arXiv:2304.07193. NOTE: This appears to be a duplicate of oquab2023dinov2 which lists the same paper.

12. su2024roformer: "RoFormer: Enhanced Transformer with Rotary Position Embedding" by Su, Jianlin et al. Venue: Neurocomputing vol 568, 2024.

For each entry, report whether paper exists, author accuracy, title accuracy, year accuracy, venue accuracy, arXiv ID accuracy, and whether arXiv preprints have since been accepted to conferences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01B15dS1MQZV5QHK1jyFbtaw",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "cd9c0e9f-e3f4-4886-8ce5-c32b0c41f0c7"
}
```

</details>

---


### System

_source line 248_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3d8459fe8a20ddf2",
  "tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "description": "Searching for Sigmoid Loss for Language Image Pre-Training Zhai…",
  "usage": {
    "total_tokens": 18564,
    "tool_uses": 4,
    "duration_ms": 25415
  },
  "last_tool_name": "WebSearch",
  "uuid": "e6c70178-2fb9-41dd-adfd-d102839f861a",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10"
}
```

---


### Tool call

_source line 249_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017aQpqmBU8uGoHQfqMVM2Ar`</summary>

```json
{
  "query": "Sigmoid Loss for Language Image Pre-Training Zhai SigLIP ICCV 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0117x4R1iCNaBL6zf4nmJYMo",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "19314bf8-138d-4e99-b028-e9e2ef470481",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSHrvHksjbug7A1a57JyTr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 17337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1091,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 250 · 2026-05-29T06:52:41.989Z_

<details><summary>↩ Tool result · `toolu_01My1a2sganjtQSD55bEeoAE`</summary>

```text
Web search results for query: "Octo model team authors list Ghosh Dibya RSS 2024 arXiv 2405.12213"

Links: [{"title":"[2405.12213] Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/abs/2405.12213"},{"title":"Octo: An Open-Source Generalist Robot Policy. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1a75e3795a1c2bc22799e353b067315f2"},{"title":"[2405.12213v2] Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/abs/2405.12213v2"},{"title":"[PDF] Octo: An Open-Source Generalist Robot Policy | Semantic Scholar","url":"https://www.semanticscholar.org/paper/1d2753d74025e7a71594506623be81f18b073adb"},{"title":"Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1","url":"https://arxiv.org/pdf/2405.12213"},{"title":"(PDF) Octo: An Open-Source Generalist Robot Policy","url":"https://www.researchgate.net/publication/380730391_Octo_An_Open-Source_Generalist_Robot_Policy"},{"title":"Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1","url":"https://openreview.net/pdf/e2dabc0a3fd32239dcab07d7bcfa1fae085f49b0.pdf"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/html/2405.12213v1"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/"}]

Based on the search results, here is the complete list of authors for the Octo model paper (arXiv 2405.12213):

The authors are: Octo Model Team, Dibya Ghosh, Homer Walke, Karl Pertsch, Kevin Black, Oier Mees, Sudeep Dasari, Joey Hejna, Tobias Kreiman, Charles Xu, Jianlan Luo, You Liang Tan, Lawrence Yunliang Chen, Pannag Sanketi, Quan Vuong, Ted Xiao, Dorsa Sadigh, Chelsea Finn, and Sergey Levine.

Additionally, the paper includes affiliations from UC Berkeley, Stanford, Carnegie Mellon University, and Google Deepmind.

The paper was published in the Proceedings of Robotics: Science and Systems (RSS) in 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "5f88c522-e474-4b6f-86d8-48c055a58cfb"
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-29T06:52:42.276Z_

<details><summary>↩ Tool result · `toolu_012cXrQRu9etvaExRJPGzZM1`</summary>

```text
Web search results for query: "RT-1 RSS 2023 Robotics Science Systems proceedings year 2022 2023"

Links: [{"title":"RT-1: Robotics Transformer for Real-World Control at Scale · Robotics: Science and Systems","url":"https://roboticsconference.org/2023/program/papers/025/"},{"title":"RSS 2023 : Robotics: Science and Systems","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?copyownerid=90704&eventid=169204"},{"title":"Overview · Robotics: Science and Systems","url":"https://rss2023.github.io/rss2023-website/program/overview/"},{"title":"Accepted Papers · Robotics: Science and Systems","url":"https://rss2023.github.io/rss2023-website/program/papers/"},{"title":"dblp: Robotics: Science and Systems 2023","url":"https://dblp.org/db/conf/rss/rss2023.html"},{"title":"Call for Papers and Demos · Robotics: Science and Systems","url":"https://rss2023.github.io/rss2023-website/information/cfp/"},{"title":"Early Career Spotlight · Robotics: Science and Systems","url":"https://rss2023.github.io/rss2023-website/program/earlycareer/"},{"title":"Robotics: Science and Systems - Online Proceedings","url":"https://www.roboticsproceedings.org/"},{"title":"Robotics: Science and Systems · A Robotics Conference","url":"https://roboticsconference.org/"}]

Based on the search results, here's what I found about RT-1 and RSS 2023:

RT-1: Robotics Transformer for Real-World Control at Scale was authored by Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Joseph Dabis, Chelsea Finn, and many other researchers from Google and related institutions.

The paper was presented at RSS 2023, which took place July 10-14, 2023 in Daegu, Republic of Korea.

RSS 2023 (Robotics: Science and System XIX) was held July 10-14, 2023 at the Daegu Exhibition and Convention Center in Daegu, Republic of Korea, with proceedings edited by Kostas Bekris, Kris Hauser, Sylvia Herbert and Jingjin Yu.

So to clarify the timeline: RT-1 was published in the RSS 2023 proceedings, which corresponds to the 19th edition of the Robotics: Science and Systems conference held in 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KK5JZyb7hqmGS5wtjs38Kf",
  "session_id": "db052317-379b-476d-9ccf-531a6abb0c10",
  "uuid": "97900bdb-351e-4c01-ab46-1bd5a14d769b"
}
```

</details>

---
