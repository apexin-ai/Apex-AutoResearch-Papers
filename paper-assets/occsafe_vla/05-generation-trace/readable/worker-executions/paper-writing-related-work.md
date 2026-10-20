# paper writing related work

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260526T125941.log`
- **Structured JSON:** [`b89605052eb47d3d91b2.json`](../../sessions/b8/b89605052eb47d3d91b2.json)

## Before a recorded user message

20 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
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
    "mcp__agent-ml-research__check_figures_and_layout",
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
  "uuid": "c8864029-5cbe-46a7-863c-754200186a8d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
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
    "resetsAt": 1779814200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2b7cb8fd-3a4c-4cd7-936f-40e0a424f544",
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196"
}
```

---

### Assistant

_source line 4_

I'll start by reading the references.bib to confirm available bibtex keys, then write the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "fbec877a-9c86-4f89-9217-4ee1b65641a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKWMVdDWpT5NmDmVLCRcpR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01K2X2u5jbCouQ7os2BHS9N4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "b9735eaf-52aa-4737-8445-378b924e29b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKWMVdDWpT5NmDmVLCRcpR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
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

_source line 6 · 2026-05-26T12:59:53.278Z_

<details><summary>↩ Tool result · `toolu_01K2X2u5jbCouQ7os2BHS9N4`</summary>

```text
1	% References for OccSafe-VLA
2	% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}
3	
4	% ============================================================
5	% VLA Safety
6	% ============================================================
7	
8	@article{hu2025vlsa,
9	  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},
10	  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
11	  journal   = {arXiv preprint arXiv:2512.11891},
12	  year      = {2025},
13	  note      = {arXiv:2512.11891}
14	}
15	
16	@inproceedings{zhang2025safevla,
17	  author    = {Borong Zhang and others},
18	  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
19	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
20	  year      = {2025},
21	  note      = {Spotlight. arXiv:2503.03480}
22	}
23	
24	@article{zhai2026cofreevla,
25	  author    = {Xuanran Zhai and others},
26	  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},
27	  journal   = {arXiv preprint arXiv:2601.21712},
28	  year      = {2026},
29	  note      = {arXiv:2601.21712}
30	}
31	
32	
33	@article{li2026vlasafety,
34	  author    = {Li and others},
35	  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
36	  journal   = {arXiv preprint arXiv:2604.23775},
37	  year      = {2026},
38	  note      = {arXiv:2604.23775}
39	}
40	
41	% ============================================================
42	% Safety Mechanisms (barrier functions / occupancy-based safety)
43	% ============================================================
44	
45	
46	@article{raja2024ogmcbf,
47	  author    = {Golnaz Raja and Teemu M{\"o}kk{\"o}nen and Reza Ghabcheloo},
48	  title     = {Safe Robot Control using Occupancy Grid Map-based Control Barrier Function ({OGM-CBF})},
49	  journal   = {arXiv preprint arXiv:2405.10703},
50	  year      = {2024},
51	  note      = {arXiv:2405.10703}
52	}
53	
54	
55	
56	% ============================================================
57	% Spatial VLA (3D representation for VLA)
58	% ============================================================
59	
60	@article{liu2025occvla,
61	  author    = {Ruixun Liu and others},
62	  title     = {{OccVLA}: Vision-Language-Action Model with Implicit 3D Occupancy Supervision},
63	  journal   = {arXiv preprint arXiv:2509.05578},
64	  year      = {2025},
65	  note      = {arXiv:2509.05578}
66	}
67	
68	@inproceedings{li2026spatialforcing,
69	  author    = {Fuhao Li and others},
70	  title     = {Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},
71	  booktitle = {International Conference on Learning Representations (ICLR)},
72	  year      = {2026},
73	  note      = {arXiv:2510.12276}
74	}
75	
76	@article{yuan2025depthvla,
77	  author    = {Tianyuan Yuan and others},
78	  title     = {{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},
79	  journal   = {arXiv preprint arXiv:2510.13375},
80	  year      = {2025},
81	  note      = {arXiv:2510.13375}
82	}
83	
84	@article{chen2026gstvla,
85	  author    = {Md Sarowar Morshed and others},
86	  title     = {{GST-VLA}: Structured {Gaussian} Spatial Tokens for 3D Depth-Aware {VLA} Models},
87	  journal   = {arXiv preprint arXiv:2603.09079},
88	  year      = {2026},
89	  note      = {arXiv:2603.09079}
90	}
91	
92	@inproceedings{wu2025spatialvla,
93	  author    = {Delin Qu and others},
94	  title     = {{SpatialVLA}: Exploring Spatial Representations for Visual-Language-Action Model},
95	  booktitle = {Robotics: Science and Systems (RSS)},
96	  year      = {2025},
97	  note      = {arXiv:2501.15830}
98	}
99	
100	@article{li2025qdepthvla,
101	  author    = {Li and others},
102	  title     = {{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},
103	  journal   = {arXiv preprint arXiv:2510.14836},
104	  year      = {2025},
105	  note      = {arXiv:2510.14836}
106	}
107	
108	@article{abouzeid2025geoaware,
109	  author    = {Abouzeid and others},
110	  title     = {{GeoAware-VLA}: Implicit Geometry Aware Vision-Language-Action Model},
111	  journal   = {arXiv preprint arXiv:2509.14117},
112	  year      = {2025},
113	  note      = {arXiv:2509.14117}
114	}
115	
116	@article{rao2026augvla3d,
117	  author    = {Zhifeng Rao and others},
118	  title     = {{AugVLA-3D}: Depth-Driven Feature Augmentation for Vision-Language-Action Models},
119	  journal   = {arXiv preprint arXiv:2602.10698},
120	  year      = {2026},
121	  note      = {arXiv:2602.10698}
122	}
123	
124	
125	@article{tu2026sgvla,
126	  author    = {Tu and others},
127	  title     = {{SG-VLA}: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation},
128	  journal   = {arXiv preprint arXiv:2603.22760},
129	  year      = {2026},
130	  note      = {arXiv:2603.22760}
131	}
132	
133	@article{xiao2026stemvla,
134	  author    = {Xiao and others},
135	  title     = {{StemVLA}: An Open-Source {VLA} with Future 3D Spatial Geometry Knowledge and 4D Historical Representation},
136	  journal   = {arXiv preprint arXiv:2602.23721},
137	  year      = {2026},
138	  note      = {arXiv:2602.23721}
139	}
140	
141	@article{bhat20253dcavla,
142	  author    = {Bhat and others},
143	  title     = {{3D-CAVLA}: Leveraging Depth and 3D Context to Generalize {VLA} for Unseen Tasks},
144	  journal   = {arXiv preprint arXiv:2505.05800},
145	  year      = {2025},
146	  note      = {arXiv:2505.05800}
147	}
148	
149	@article{wu2026stvla,
150	  author    = {Wu and others},
151	  title     = {{ST-VLA}: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation},
152	  journal   = {arXiv preprint arXiv:2603.13788},
153	  year      = {2026},
154	  note      = {arXiv:2603.13788}
155	}
156	
157	@article{li2026corridorvla,
158	  author    = {Li and others},
159	  title     = {{CorridorVLA}: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors},
160	  journal   = {arXiv preprint arXiv:2604.21241},
161	  year      = {2026},
162	  note      = {arXiv:2604.21241}
163	}
164	
165	@article{sun2025geovla,
166	  author    = {Sun and others},
167	  title     = {{GeoVLA}: Empowering 3D Representations in Vision-Language-Action Models},
168	  journal   = {arXiv preprint arXiv:2508.09071},
169	  year      = {2025},
170	  note      = {arXiv:2508.09071}
171	}
172	
173	@article{li2025pointvla,
174	  author    = {Li and others},
175	  title     = {{PointVLA}: Injecting the 3D World into Vision-Language-Action Models},
176	  journal   = {arXiv preprint arXiv:2503.07511},
177	  year      = {2025},
178	  note      = {arXiv:2503.07511}
179	}
180	
181	
182	% ============================================================
183	% 3D Perception (occupancy / BEV / depth)
184	% ============================================================
185	
186	@inproceedings{li2022bevformer,
187	  author    = {Zhiqi Li and Wenhai Wang and Hongyang Li and Enze Xie and Chonghao Sima and Tong Lu and Yu Qiao and Jifeng Dai},
188	  title     = {{BEVFormer}: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers},
189	  booktitle = {European Conference on Computer Vision (ECCV)},
190	  year      = {2022},
191	  note      = {arXiv:2203.17270}
192	}
193	
194	@inproceedings{sima2023occnet,
195	  author    = {Chonghao Sima and Wenwen Tong and Tai Wang and Li Chen and Silei Wu and Hanming Deng and Yi Gu and Lewei Lu and Ping Luo and Dahua Lin and Hongyang Li},
196	  title     = {Scene as Occupancy},
197	  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},
198	  year      = {2023},
199	  note      = {arXiv:2306.02851}
200	}
201	
202	@inproceedings{tian2023occ3d,
203	  author    = {Xiaoyu Tian and Tao Jiang and Longfei Yun and Yucheng Mao and Huitong Yang and Yue Wang and Yilun Wang and Hang Zhao},
204	  title     = {{Occ3D}: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving},
205	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
206	  year      = {2023},
207	  note      = {arXiv:2304.14365}
208	}
209	
210	
211	@inproceedings{yang2024depthanything,
212	  author    = {Lihe Yang and Bingyi Kang and Zilong Huang and Xiaogang Xu and Jiashi Feng and Hengshuang Zhao},
213	  title     = {Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data},
214	  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
215	  year      = {2024},
216	  note      = {arXiv:2401.10891}
217	}
218	
219	% ============================================================
220	% Foundation Models / VLA Infrastructure
221	% ============================================================
222	
223	@article{kim2024openvla,
224	  author    = {Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},
225	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
226	  journal   = {arXiv preprint arXiv:2406.09246},
227	  year      = {2024},
228	  note      = {arXiv:2406.09246}
229	}
230	
231	@article{kim2025oft,
232	  author    = {Moo Jin Kim and others},
233	  title     = {Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},
234	  journal   = {arXiv preprint arXiv:2502.19645},
235	  year      = {2025},
236	  note      = {arXiv:2502.19645}
237	}
238	
239	@inproceedings{brohan2023rt2,
240	  author    = {Anthony Brohan and Noah Brown and Justice Carbajal and others},
241	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
242	  booktitle = {Conference on Robot Learning (CoRL)},
243	  year      = {2023},
244	  note      = {arXiv:2307.15818}
245	}
246	
247	@article{oquab2024dinov2,
248	  author    = {Maxime Oquab and Timoth\'{e}e Darcet and Th\'{e}o Moutakanni and Huy Vo and Marc Szafraniec and Vasil Khalidov and Pierre Fernandez and Daniel Haziza and Francisco Massa and Alaaeldin El-Nouby and Mahmoud Assran and Nicolas Ballas and Wojciech Galuba and Russell Howes and Po-Yao Huang and Shang-Wen Li and Ishan Misra and Michael Rabbat and Vasu Sharma and Gabriel Synnaeve and Hu Xu and Herv\'{e} J\'{e}gou and Julien Mairal and Patrick Labatut and Armand Joulin and Piotr Bojanowski},
249	  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},
250	  journal   = {Transactions on Machine Learning Research (TMLR)},
251	  year      = {2024},
252	  note      = {arXiv:2304.07193}
253	}
254	
255	@inproceedings{zhai2023siglip,
256	  author    = {Xiaohua Zhai and Basil Mustafa and Alexander Kolesnikov and Lucas Beyer},
257	  title     = {Sigmoid Loss for Language Image Pre-Training},
258	  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},
259	  year      = {2023},
260	  note      = {arXiv:2303.15343}
261	}
262	
263	
264	
265	% ============================================================
266	% Benchmarks
267	% ============================================================
268	
269	@inproceedings{liu2023libero,
270	  author    = {Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},
271	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
272	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
273	  year      = {2023},
274	  note      = {arXiv:2306.03310}
275	}
276	
277	% ============================================================
278	% Multi-Task Learning / Regularization
279	% ============================================================
280	
281	@article{caruana1997multitask,
282	  author    = {Rich Caruana},
283	  title     = {Multitask Learning},
284	  journal   = {Machine Learning},
285	  volume    = {28},
286	  number    = {1},
287	  pages     = {41--75},
288	  year      = {1997}
289	}
290	
291	@article{ruder2017overview,
292	  author    = {Sebastian Ruder},
293	  title     = {An Overview of Multi-Task Learning in Deep Neural Networks},
294	  journal   = {arXiv preprint arXiv:1706.05098},
295	  year      = {2017},
296	  note      = {arXiv:1706.05098}
297	}
298	
299	@inproceedings{lippl2024implicit,
300	  author    = {Samuel Lippl and Jack W. Lindsey},
301	  title     = {Implicit Regularization of Multi-Task Learning and Finetuning in Overparameterized Neural Networks},
302	  booktitle = {International Conference on Learning Representations (ICLR)},
303	  year      = {2024},
304	  note      = {arXiv:2310.02396}
305	}
306	
307	
308	@inproceedings{chen2018gradnorm,
309	  author    = {Zhao Chen and Vijay Badrinarayanan and Chen-Yu Lee and Andrew Rabinovich},
310	  title     = {{GradNorm}: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks},
311	  booktitle = {International Conference on Machine Learning (ICML)},
312	  year      = {2018},
313	  note      = {arXiv:1711.02257}
314	}
315	
316	@inproceedings{yu2020pcgrad,
317	  author    = {Tianhe Yu and Saurabh Kumar and Abhishek Gupta and Sergey Levine and Karol Hausman and Chelsea Finn},
318	  title     = {Gradient Surgery for Multi-Task Learning},
319	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
320	  year      = {2020},
321	  note      = {arXiv:2001.06782}
322	}
323	
324	@inproceedings{liu2021cagrad,
325	  author    = {Bo Liu and Xingchao Liu and Xiaojie Jin and Peter Stone and Qiang Liu},
326	  title     = {Conflict-Averse Gradient Descent for Multi-task Learning},
327	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
328	  year      = {2021},
329	  note      = {arXiv:2110.14048}
330	}
331	
332	@inproceedings{navon2022nashmtl,
333	  author    = {Aviv Navon and Aviv Shamsian and Idan Achituve and Haggai Maron and Kenji Kawaguchi and Gal Chechik and Ethan Fetaya},
334	  title     = {Multi-Task Learning as a Bargaining Game},
335	  booktitle = {International Conference on Machine Learning (ICML)},
336	  year      = {2022},
337	  note      = {arXiv:2202.01017}
338	}
339	
340	@inproceedings{pezeshki2021gradient,
341	  author    = {Mohammad Pezeshki and Oumar Kaba and Yoshua Bengio and Aaron Courville and Doina Precup and Guillaume Lajoie},
342	  title     = {Gradient Starvation: A Learning Proclivity in Neural Networks},
343	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
344	  volume    = {34},
345	  pages     = {1256--1272},
346	  year      = {2021}
347	}
348	
349	@article{kirkpatrick2017ewc,
350	  author    = {James Kirkpatrick and others},
351	  title     = {Overcoming Catastrophic Forgetting in Neural Networks},
352	  journal   = {Proceedings of the National Academy of Sciences (PNAS)},
353	  volume    = {114},
354	  number    = {13},
355	  pages     = {3521--3526},
356	  year      = {2017},
357	  note      = {arXiv:1612.00796}
358	}
359	
360	% ============================================================
361	% Parameter-Efficient Fine-Tuning
362	% ============================================================
363	
364	@inproceedings{hu2022lora,
365	  author    = {Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},
366	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
367	  booktitle = {International Conference on Learning Representations (ICLR)},
368	  year      = {2022},
369	  note      = {arXiv:2106.09685}
370	}
371	
372	% ============================================================
373	% Loss Functions
374	% ============================================================
375	
376	@inproceedings{lin2017focal,
377	  author    = {Tsung-Yi Lin and Priya Goyal and Ross Girshick and Kaiming He and Piotr Doll\'{a}r},
378	  title     = {Focal Loss for Dense Object Detection},
379	  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},
380	  year      = {2017},
381	  note      = {arXiv:1708.02002}
382	}
383	
384	@inproceedings{kornblith2019similarity,
385	  author    = {Simon Kornblith and Mohammad Norouzi and Honglak Lee and Geoffrey Hinton},
386	  title     = {Similarity of Neural Network Representations Revisited},
387	  booktitle = {Proceedings of the 36th International Conference on Machine Learning (ICML)},
388	  year      = {2019},
389	  pages     = {3519--3529}
390	}
391	
392	@inproceedings{ioffe2015batchnorm,
393	  author    = {Sergey Ioffe and Christian Szegedy},
394	  title     = {Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift},
395	  booktitle = {Proceedings of the 32nd International Conference on Machine Learning (ICML)},
396	  year      = {2015},
397	  pages     = {448--456}
398	}
399	
400	@inproceedings{lee2015deeply,
401	  author    = {Chen-Yu Lee and Saining Xie and Patrick Gallagher and Zhengyou Zhang and Zhuowen Tu},
402	  title     = {Deeply-Supervised Nets},
403	  booktitle = {Proceedings of the 18th International Conference on Artificial Intelligence and Statistics (AISTATS)},
404	  year      = {2015},
405	  pages     = {562--570}
406	}
407	
408	% ============================================================
409	% BatchNorm in Domain Adaptation / Robustness
410	% ============================================================
411	
412	@inproceedings{li2017adabn,
413	  author    = {Yanghao Li and Naiyan Wang and Jianping Shi and Jiaying Liu and Xiaodi Hou},
414	  title     = {Revisiting Batch Normalization for Practical Domain Adaptation},
415	  booktitle = {International Conference on Learning Representations (ICLR)},
416	  year      = {2017},
417	  note      = {arXiv:1603.04779}
418	}
419	
420	@inproceedings{schneider2020bn,
421	  author    = {Steffen Schneider and Evgenia Rusak and Luisa Eck and Oliver Bringmann and Wieland Brendel and Matthias Bethge},
422	  title     = {Improving Robustness against Common Corruptions by Covariate Shift Adaptation},
423	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
424	  year      = {2020}
425	}
426	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "33156c1d-55e0-4b35-979a-a02f069d76a2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib",
      "content": "% References for OccSafe-VLA\n% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}\n\n% ============================================================\n% VLA Safety\n% ============================================================\n\n@article{hu2025vlsa,\n  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},\n  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},\n  journal   = {arXiv preprint arXiv:2512.11891},\n  year      = {2025},\n  note      = {arXiv:2512.11891}\n}\n\n@inproceedings{zhang2025safevla,\n  author    = {Borong Zhang and others},\n  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2025},\n  note      = {Spotlight. arXiv:2503.03480}\n}\n\n@article{zhai2026cofreevla,\n  author    = {Xuanran Zhai and others},\n  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},\n  journal   = {arXiv preprint arXiv:2601.21712},\n  year      = {2026},\n  note      = {arXiv:2601.21712}\n}\n\n\n@article{li2026vlasafety,\n  author    = {Li and others},\n  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},\n  journal   = {arXiv preprint arXiv:2604.23775},\n  year      = {2026},\n  note      = {arXiv:2604.23775}\n}\n\n% ============================================================\n% Safety Mechanisms (barrier functions / occupancy-based safety)\n% ============================================================\n\n\n@article{raja2024ogmcbf,\n  author    = {Golnaz Raja and Teemu M{\\\"o}kk{\\\"o}nen and Reza Ghabcheloo},\n  title     = {Safe Robot Control using Occupancy Grid Map-based Control Barrier Function ({OGM-CBF})},\n  journal   = {arXiv preprint arXiv:2405.10703},\n  year      = {2024},\n  note      = {arXiv:2405.10703}\n}\n\n\n\n% ============================================================\n% Spatial VLA (3D representation for VLA)\n% ============================================================\n\n@article{liu2025occvla,\n  author    = {Ruixun Liu and others},\n  title     = {{OccVLA}: Vision-Language-Action Model with Implicit 3D Occupancy Supervision},\n  journal   = {arXiv preprint arXiv:2509.05578},\n  year      = {2025},\n  note      = {arXiv:2509.05578}\n}\n\n@inproceedings{li2026spatialforcing,\n  author    = {Fuhao Li and others},\n  title     = {Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2026},\n  note      = {arXiv:2510.12276}\n}\n\n@article{yuan2025depthvla,\n  author    = {Tianyuan Yuan and others},\n  title     = {{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},\n  journal   = {arXiv preprint arXiv:2510.13375},\n  year      = {2025},\n  note      = {arXiv:2510.13375}\n}\n\n@article{chen2026gstvla,\n  author    = {Md Sarowar Morshed and others},\n  title     = {{GST-VLA}: Structured {Gaussian} Spatial Tokens for 3D Depth-Aware {VLA} Models},\n  journal   = {arXiv preprint arXiv:2603.09079},\n  year      = {2026},\n  note      = {arXiv:2603.09079}\n}\n\n@inproceedings{wu2025spatialvla,\n  author    = {Delin Qu and others},\n  title     = {{SpatialVLA}: Exploring Spatial Representations for Visual-Language-Action Model},\n  booktitle = {Robotics: Science and Systems (RSS)},\n  year      = {2025},\n  note      = {arXiv:2501.15830}\n}\n\n@article{li2025qdepthvla,\n  author    = {Li and others},\n  title     = {{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},\n  journal   = {arXiv preprint arXiv:2510.14836},\n  year      = {2025},\n  note      = {arXiv:2510.14836}\n}\n\n@article{abouzeid2025geoaware,\n  author    = {Abouzeid and others},\n  title     = {{GeoAware-VLA}: Implicit Geometry Aware Vision-Language-Action Model},\n  journal   = {arXiv preprint arXiv:2509.14117},\n  year      = {2025},\n  note      = {arXiv:2509.14117}\n}\n\n@article{rao2026augvla3d,\n  author    = {Zhifeng Rao and others},\n  title     = {{AugVLA-3D}: Depth-Driven Feature Augmentation for Vision-Language-Action Models},\n  journal   = {arXiv preprint arXiv:2602.10698},\n  year      = {2026},\n  note      = {arXiv:2602.10698}\n}\n\n\n@article{tu2026sgvla,\n  author    = {Tu and others},\n  title     = {{SG-VLA}: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation},\n  journal   = {arXiv preprint arXiv:2603.22760},\n  year      = {2026},\n  note      = {arXiv:2603.22760}\n}\n\n@article{xiao2026stemvla,\n  author    = {Xiao and others},\n  title     = {{StemVLA}: An Open-Source {VLA} with Future 3D Spatial Geometry Knowledge and 4D Historical Representation},\n  journal   = {arXiv preprint arXiv:2602.23721},\n  year      = {2026},\n  note      = {arXiv:2602.23721}\n}\n\n@article{bhat20253dcavla,\n  author    = {Bhat and others},\n  title     = {{3D-CAVLA}: Leveraging Depth and 3D Context to Generalize {VLA} for Unseen Tasks},\n  journal   = {arXiv preprint arXiv:2505.05800},\n  year      = {2025},\n  note      = {arXiv:2505.05800}\n}\n\n@article{wu2026stvla,\n  author    = {Wu and others},\n  title     = {{ST-VLA}: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation},\n  journal   = {arXiv preprint arXiv:2603.13788},\n  year      = {2026},\n  note      = {arXiv:2603.13788}\n}\n\n@article{li2026corridorvla,\n  author    = {Li and others},\n  title     = {{CorridorVLA}: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors},\n  journal   = {arXiv preprint arXiv:2604.21241},\n  year      = {2026},\n  note      = {arXiv:2604.21241}\n}\n\n@article{sun2025geovla,\n  author    = {Sun and others},\n  title     = {{GeoVLA}: Empowering 3D Representations in Vision-Language-Action Models},\n  journal   = {arXiv preprint arXiv:2508.09071},\n  year      = {2025},\n  note      = {arXiv:2508.09071}\n}\n\n@article{li2025pointvla,\n  author    = {Li and others},\n  title     = {{PointVLA}: Injecting the 3D World into Vision-Language-Action Models},\n  journal   = {arXiv preprint arXiv:2503.07511},\n  year      = {2025},\n  note      = {arXiv:2503.07511}\n}\n\n\n% ============================================================\n% 3D Perception (occupancy / BEV / depth)\n% ============================================================\n\n@inproceedings{li2022bevformer,\n  author    = {Zhiqi Li and Wenhai Wang and Hongyang Li and Enze Xie and Chonghao Sima and Tong Lu and Yu Qiao and Jifeng Dai},\n  title     = {{BEVFormer}: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers},\n  booktitle = {European Conference on Computer Vision (ECCV)},\n  year      = {2022},\n  note      = {arXiv:2203.17270}\n}\n\n@inproceedings{sima2023occnet,\n  author    = {Chonghao Sima and Wenwen Tong and Tai Wang and Li Chen and Silei Wu and Hanming Deng and Yi Gu and Lewei Lu and Ping Luo and Dahua Lin and Hongyang Li},\n  title     = {Scene as Occupancy},\n  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year      = {2023},\n  note      = {arXiv:2306.02851}\n}\n\n@inproceedings{tian2023occ3d,\n  author    = {Xiaoyu Tian and Tao Jiang and Longfei Yun and Yucheng Mao and Huitong Yang and Yue Wang and Yilun Wang and Hang Zhao},\n  title     = {{Occ3D}: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n  note      = {arXiv:2304.14365}\n}\n\n\n@inproceedings{yang2024depthanything,\n  author    = {Lihe Yang and Bingyi Kang and Zilong Huang and Xiaogang Xu and Jiashi Feng and Hengshuang Zhao},\n  title     = {Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data},\n  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year      = {2024},\n  note      = {arXiv:2401.10891}\n}\n\n% ============================================================\n% Foundation Models / VLA Infrastructure\n% ============================================================\n\n@article{kim2024openvla,\n  author    = {Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},\n  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  journal   = {arXiv preprint arXiv:2406.09246},\n  year      = {2024},\n  note      = {arXiv:2406.09246}\n}\n\n@article{kim2025oft,\n  author    = {Moo Jin Kim and others},\n  title     = {Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  journal   = {arXiv preprint arXiv:2502.19645},\n  year      = {2025},\n  note      = {arXiv:2502.19645}\n}\n\n@inproceedings{brohan2023rt2,\n  author    = {Anthony Brohan and Noah Brown and Justice Carbajal and others},\n  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  booktitle = {Conference on Robot Learning (CoRL)},\n  year      = {2023},\n  note      = {arXiv:2307.15818}\n}\n\n@article{oquab2024dinov2,\n  author    = {Maxime Oquab and Timoth\\'{e}e Darcet and Th\\'{e}o Moutakanni and Huy Vo and Marc Szafraniec and Vasil Khalidov and Pierre Fernandez and Daniel Haziza and Francisco Massa and Alaaeldin El-Nouby and Mahmoud Assran and Nicolas Ballas and Wojciech Galuba and Russell Howes and Po-Yao Huang and Shang-Wen Li and Ishan Misra and Michael Rabbat and Vasu Sharma and Gabriel Synnaeve and Hu Xu and Herv\\'{e} J\\'{e}gou and Julien Mairal and Patrick Labatut and Armand Joulin and Piotr Bojanowski},\n  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2024},\n  note      = {arXiv:2304.07193}\n}\n\n@inproceedings{zhai2023siglip,\n  author    = {Xiaohua Zhai and Basil Mustafa and Alexander Kolesnikov and Lucas Beyer},\n  title     = {Sigmoid Loss for Language Image Pre-Training},\n  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year      = {2023},\n  note      = {arXiv:2303.15343}\n}\n\n\n\n% ============================================================\n% Benchmarks\n% ============================================================\n\n@inproceedings{liu2023libero,\n  author    = {Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},\n  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n  note      = {arXiv:2306.03310}\n}\n\n% ============================================================\n% Multi-Task Learning / Regularization\n% ============================================================\n\n@article{caruana1997multitask,\n  author    = {Rich Caruana},\n  title     = {Multitask Learning},\n  journal   = {Machine Learning},\n  volume    = {28},\n  number    = {1},\n  pages     = {41--75},\n  year      = {1997}\n}\n\n@article{ruder2017overview,\n  author    = {Sebastian Ruder},\n  title     = {An Overview of Multi-Task Learning in Deep Neural Networks},\n  journal   = {arXiv preprint arXiv:1706.05098},\n  year      = {2017},\n  note      = {arXiv:1706.05098}\n}\n\n@inproceedings{lippl2024implicit,\n  author    = {Samuel Lippl and Jack W. Lindsey},\n  title     = {Implicit Regularization of Multi-Task Learning and Finetuning in Overparameterized Neural Networks},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  note      = {arXiv:2310.02396}\n}\n\n\n@inproceedings{chen2018gradnorm,\n  author    = {Zhao Chen and Vijay Badrinarayanan and Chen-Yu Lee and Andrew Rabinovich},\n  title     = {{GradNorm}: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2018},\n  note      = {arXiv:1711.02257}\n}\n\n@inproceedings{yu2020pcgrad,\n  author    = {Tianhe Yu and Saurabh Kumar and Abhishek Gupta and Sergey Levine and Karol Hausman and Chelsea Finn},\n  title     = {Gradient Surgery for Multi-Task Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2020},\n  note      = {arXiv:2001.06782}\n}\n\n@inproceedings{liu2021cagrad,\n  author    = {Bo Liu and Xingchao Liu and Xiaojie Jin and Peter Stone and Qiang Liu},\n  title     = {Conflict-Averse Gradient Descent for Multi-task Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2021},\n  note      = {arXiv:2110.14048}\n}\n\n@inproceedings{navon2022nashmtl,\n  author    = {Aviv Navon and Aviv Shamsian and Idan Achituve and Haggai Maron and Kenji Kawaguchi and Gal Chechik and Ethan Fetaya},\n  title     = {Multi-Task Learning as a Bargaining Game},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2022},\n  note      = {arXiv:2202.01017}\n}\n\n@inproceedings{pezeshki2021gradient,\n  author    = {Mohammad Pezeshki and Oumar Kaba and Yoshua Bengio and Aaron Courville and Doina Precup and Guillaume Lajoie},\n  title     = {Gradient Starvation: A Learning Proclivity in Neural Networks},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  volume    = {34},\n  pages     = {1256--1272},\n  year      = {2021}\n}\n\n@article{kirkpatrick2017ewc,\n  author    = {James Kirkpatrick and others},\n  title     = {Overcoming Catastrophic Forgetting in Neural Networks},\n  journal   = {Proceedings of the National Academy of Sciences (PNAS)},\n  volume    = {114},\n  number    = {13},\n  pages     = {3521--3526},\n  year      = {2017},\n  note      = {arXiv:1612.00796}\n}\n\n% ============================================================\n% Parameter-Efficient Fine-Tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Edward J. Hu and Yelong Shen and Phillip Wallis and Zeyuan Allen-Zhu and Yuanzhi Li and Shean Wang and Lu Wang and Weizhu Chen},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n  note      = {arXiv:2106.09685}\n}\n\n% ============================================================\n% Loss Functions\n% ============================================================\n\n@inproceedings{lin2017focal,\n  author    = {Tsung-Yi Lin and Priya Goyal and Ross Girshick and Kaiming He and Piotr Doll\\'{a}r},\n  title     = {Focal Loss for Dense Object Detection},\n  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year      = {2017},\n  note      = {arXiv:1708.02002}\n}\n\n@inproceedings{kornblith2019similarity,\n  author    = {Simon Kornblith and Mohammad Norouzi and Honglak Lee and Geoffrey Hinton},\n  title     = {Similarity of Neural Network Representations Revisited},\n  booktitle = {Proceedings of the 36th International Conference on Machine Learning (ICML)},\n  year      = {2019},\n  pages     = {3519--3529}\n}\n\n@inproceedings{ioffe2015batchnorm,\n  author    = {Sergey Ioffe and Christian Szegedy},\n  title     = {Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift},\n  booktitle = {Proceedings of the 32nd International Conference on Machine Learning (ICML)},\n  year      = {2015},\n  pages     = {448--456}\n}\n\n@inproceedings{lee2015deeply,\n  author    = {Chen-Yu Lee and Saining Xie and Patrick Gallagher and Zhengyou Zhang and Zhuowen Tu},\n  title     = {Deeply-Supervised Nets},\n  booktitle = {Proceedings of the 18th International Conference on Artificial Intelligence and Statistics (AISTATS)},\n  year      = {2015},\n  pages     = {562--570}\n}\n\n% ============================================================\n% BatchNorm in Domain Adaptation / Robustness\n% ============================================================\n\n@inproceedings{li2017adabn,\n  author    = {Yanghao Li and Naiyan Wang and Jianping Shi and Jiaying Liu and Xiaodi Hou},\n  title     = {Revisiting Batch Normalization for Practical Domain Adaptation},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2017},\n  note      = {arXiv:1603.04779}\n}\n\n@inproceedings{schneider2020bn,\n  author    = {Steffen Schneider and Evgenia Rusak and Luisa Eck and Oliver Bringmann and Wieland Brendel and Matthias Bethge},\n  title     = {Improving Robustness against Common Corruptions by Covariate Shift Adaptation},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2020}\n}\n",
      "numLines": 426,
      "startLine": 1,
      "totalLines": 426
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
Now I have all the bibtex keys. Let me catalog them:

**VLA Safety:**
- `hu2025vlsa` — VLSA
- `zhang2025safevla` — SafeVLA (note: key uses `zhang` not `zhan`)
- `zhai2026cofreevla` — CoFreeVLA (note: key uses `zhai` not `chen`)
- `li2026vlasafety` — VLA safety survey
- `raja2024ogmcbf` — OGM-CBF (note: key uses `raja` not `ji`)


- `liu2025occvla` — OccVLA
- `li2026spatialforcing` — Spatial Forcing
- `yuan2025depthvla` — DepthVLA
- `chen2026gstvla` — GST-VLA
- `wu2025spatialvla` — SpatialVLA
- `li2025qdepthvla` — QDepth-VLA
- `abouzeid2025geoaware` — GeoAware-VLA
- `rao2026augvla3d` — AugVLA-3D
- `tu2026sgvla` — SG-VLA
- `xiao2026stemvla` — S-TEM-VLA

**Spatial VLA:**
- `bhat20253dcavla` — 3D-CAVLA
- `wu2026stvla` — ST-VLA
- `li2026corridorvla` — CorridorVLA
- `sun2025geovla` — GeoVLA
- `li2025pointvla` — PointVLA

**3D Perception:**
- `li2022bevformer` — BEVFormer
- `sima2023occnet` — OccNet
- `tian2023occ3d` — Occ3D
- `yang2024depthanything` — Depth Anything

**Foundation / VLA:**
- `kim2024openvla` — OpenVLA
- `kim2025oft` — OFT
- `brohan2023rt2` — RT-2
- `oquab2024dinov2` — DINOv2
- `zhai2023siglip` — SigLIP

**Benchmarks:**
- `liu2023libero` — LIBERO

**Multi-Task Learning:**
- `caruana1997multitask`
- `ruder2017overview`
- `lippl2024implicit`
- `chen2018gradnorm`
- `yu2020pcgrad`
- `liu2021cagrad`
- `navon2022nashmtl`
- `pezeshki2021gradient`
- `kirkpatrick2017ewc`

**PEFT:**
- `hu2022lora`

**Loss / Norm:**
- `lin2017focal`
- `kornblith2019similarity`
- `ioffe2015batchnorm`
- `lee2015deeply`

**BN Domain Adaptation:**
- `li2017adabn`
- `schneider2020bn`

I'm organizing a comprehensive reference list across vision-language models, 3D perception, multi-task learning approaches, and domain adaptation techniques. There's a discrepancy in how some citations are formatted that I need to reconcile.

Looking through the bibliography, I'm finding several key mismatches between what I've been using and the actual author names and citation keys. The corrections span safety-focused VLA work, co-free learning approaches, depth-aware methods, 3D augmentation techniques, and geometric awareness systems—I need to update these references to match the proper author attributions and standardized citation keys.

Now I should check whether there's already a related_work.tex file in the project that I need to update with these corrections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "963765bc-376b-4be4-ba5f-c5aad9fc7053",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWVfDaiBhrDnNRxQ8caKQm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6770,
      "cache_read_input_tokens": 25140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6770
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

_source line 8_

Now let me check if there's an existing file to overwrite.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "3ea69b97-83fc-493a-932d-db570b1d4650",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWVfDaiBhrDnNRxQ8caKQm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6770,
      "cache_read_input_tokens": 25140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6770
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

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_012iWgSn8JGZEtCcGEQJrRPs`</summary>

```json
{
  "pattern": "**/related_work.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "658d4dbe-b375-499a-95f4-76ef644c1683",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWVfDaiBhrDnNRxQ8caKQm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6770,
      "cache_read_input_tokens": 25140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6770
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

_source line 10 · 2026-05-26T13:00:15.180Z_

<details><summary>↩ Tool result · `toolu_012iWgSn8JGZEtCcGEQJrRPs`</summary>

```text
artifacts/_project/paper/related_work.tex
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "d4e1700e-78f5-470b-b4e0-f795d88309d3",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work.tex",
      "docs/paper/related_work.tex"
    ],
    "durationMs": 17,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01QC8JwpqWk1Kibs2tMmVPhX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "af45c65d-565a-4244-88ab-9ab93e82b4a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P66kKXqoKzQCUzBT9f88be",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 31910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1293
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

_source line 12 · 2026-05-26T13:00:19.064Z_

<details><summary>↩ Tool result · `toolu_01QC8JwpqWk1Kibs2tMmVPhX`</summary>

```text
1	
2	\section{Related Work}
3	\label{sec:related}
4	
5	\subsection{VLA Safety and Spatial Representations}
6	
7	VLA models achieve high task success but remain prone to collisions~\cite{li2026vlasafety}. Two strategies address this gap. Runtime constraint methods add safety layers at inference: AEGIS~\cite{hu2025vlsa} filters actions via a CBF constructed from vision-language obstacle detection, improving CAR by 59\,pp on SafeLIBERO; CoFreeVLA~\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm settings; and OGM-CBF~\cite{raja2024ogmcbf} builds CBFs from occupancy grid maps. Training-time methods embed safety into the policy: SafeVLA~\cite{zhang2025safevla} applies constrained RL to reduce safety violations by 84\%. Both strategies treat safety as a behavioral constraint problem without investigating whether the VLA's internal spatial representations contribute to collision avoidance.
8	
9	Separately, a growing body of work injects 3D structure into VLA vision encoders to improve task success. Depth-based methods fuse monocular predictions with visual features~\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware}, building on foundation models like Depth Anything~\cite{yang2024depthanything}. Alignment-based approaches regularize internal representations: Spatial Forcing~\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features (ICLR 2026); SpatialVLA~\cite{wu2025spatialvla} introduces egocentric 3D position encoding (RSS 2025). Point cloud and geometric methods encode explicit 3D structure~\cite{li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla}. In autonomous driving, OccVLA~\cite{liu2025occvla} uses occupancy prediction as auxiliary VLA supervision, drawing on BEV representations~\cite{li2022bevformer, sima2023occnet, tian2023occ3d}. These spatial methods consistently improve task success but none evaluates collision avoidance. Our work bridges this gap: we study whether auxiliary spatial supervision affects safety, and design a factorial ablation to isolate the operative mechanism.
10	
11	\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}
12	
13	Multi-task learning improves generalization by training shared representations on related objectives~\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\cite{lippl2024implicit} show that multi-task training induces implicit $\ell_{1,2}$ regularization in overparameterized networks, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. A parallel line of work addresses gradient conflicts in multi-task optimization through gradient manipulation~\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl}. These methods share a common premise: task gradients may conflict, and the optimizer must resolve the conflict. Our gradient analysis shows that action and auxiliary gradients are approximately orthogonal (cosine similarity $\approx 0$), and that blocking auxiliary gradients causes encoder gradient norms to collapse to 1--13\% of baseline. This pattern is more consistent with intermediate supervision~\cite{lee2015deeply} and continual learning perspectives on preserving pretrained features~\cite{kirkpatrick2017ewc} than with gradient conflict resolution: the auxiliary gradient prevents encoder gradient collapse rather than resolving a directional conflict. The collapse mechanism also resonates with gradient starvation~\cite{pezeshki2021gradient}, where removing a gradient source causes certain feature directions to receive vanishingly small updates.
14	
15	BatchNorm statistics are known to be sensitive to distribution shift: Li et al.~\cite{li2017adabn} show that adapting BN statistics alone achieves effective domain adaptation, and Schneider et al.~\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves corruption robustness. These findings establish that BN running statistics encode distributional assumptions that, when violated, degrade performance. Our work reveals an analogous phenomenon during multi-task training: auxiliary gradients flowing through the shared encoder shift BN statistics in the auxiliary head, and whether this shift is calibrated (by gradient flow) or uncalibrated (under detachment) determines its effect on safety behavior.
16	
17	For VLA fine-tuning with LoRA~\cite{hu2022lora}, the interaction between auxiliary losses and adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports improved convergence, but does not separate the regularization effect of gradient flow from the informational content of the spatial signal. Our factorial design isolates these factors.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "bc3a4f7b-117f-4bff-9eac-b4cc831ef4f7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
      "content": "\n\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{VLA Safety and Spatial Representations}\n\nVLA models achieve high task success but remain prone to collisions~\\cite{li2026vlasafety}. Two strategies address this gap. Runtime constraint methods add safety layers at inference: AEGIS~\\cite{hu2025vlsa} filters actions via a CBF constructed from vision-language obstacle detection, improving CAR by 59\\,pp on SafeLIBERO; CoFreeVLA~\\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm settings; and OGM-CBF~\\cite{raja2024ogmcbf} builds CBFs from occupancy grid maps. Training-time methods embed safety into the policy: SafeVLA~\\cite{zhang2025safevla} applies constrained RL to reduce safety violations by 84\\%. Both strategies treat safety as a behavioral constraint problem without investigating whether the VLA's internal spatial representations contribute to collision avoidance.\n\nSeparately, a growing body of work injects 3D structure into VLA vision encoders to improve task success. Depth-based methods fuse monocular predictions with visual features~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware}, building on foundation models like Depth Anything~\\cite{yang2024depthanything}. Alignment-based approaches regularize internal representations: Spatial Forcing~\\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features (ICLR 2026); SpatialVLA~\\cite{wu2025spatialvla} introduces egocentric 3D position encoding (RSS 2025). Point cloud and geometric methods encode explicit 3D structure~\\cite{li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla}. In autonomous driving, OccVLA~\\cite{liu2025occvla} uses occupancy prediction as auxiliary VLA supervision, drawing on BEV representations~\\cite{li2022bevformer, sima2023occnet, tian2023occ3d}. These spatial methods consistently improve task success but none evaluates collision avoidance. Our work bridges this gap: we study whether auxiliary spatial supervision affects safety, and design a factorial ablation to isolate the operative mechanism.\n\n\\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}\n\nMulti-task learning improves generalization by training shared representations on related objectives~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training induces implicit $\\ell_{1,2}$ regularization in overparameterized networks, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. A parallel line of work addresses gradient conflicts in multi-task optimization through gradient manipulation~\\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl}. These methods share a common premise: task gradients may conflict, and the optimizer must resolve the conflict. Our gradient analysis shows that action and auxiliary gradients are approximately orthogonal (cosine similarity $\\approx 0$), and that blocking auxiliary gradients causes encoder gradient norms to collapse to 1--13\\% of baseline. This pattern is more consistent with intermediate supervision~\\cite{lee2015deeply} and continual learning perspectives on preserving pretrained features~\\cite{kirkpatrick2017ewc} than with gradient conflict resolution: the auxiliary gradient prevents encoder gradient collapse rather than resolving a directional conflict. The collapse mechanism also resonates with gradient starvation~\\cite{pezeshki2021gradient}, where removing a gradient source causes certain feature directions to receive vanishingly small updates.\n\nBatchNorm statistics are known to be sensitive to distribution shift: Li et al.~\\cite{li2017adabn} show that adapting BN statistics alone achieves effective domain adaptation, and Schneider et al.~\\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves corruption robustness. These findings establish that BN running statistics encode distributional assumptions that, when violated, degrade performance. Our work reveals an analogous phenomenon during multi-task training: auxiliary gradients flowing through the shared encoder shift BN statistics in the auxiliary head, and whether this shift is calibrated (by gradient flow) or uncalibrated (under detachment) determines its effect on safety behavior.\n\nFor VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports improved convergence, but does not separate the regularization effect of gradient flow from the informational content of the spatial signal. Our factorial design isolates these factors.\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing file carefully. I notice the task instructions say this is a Plan B ordinal interaction paper, and there are specific constraints:

- **禁止** "crossover interaction" — v2 data is ordinal
- **禁止** "BN-mediated gradient calibration" / "existence regularization"
- **禁止** "gradient collapse" / "no gradient collapse" claims
- **可用** "ordinal interaction", "gradient orthogonality"

Let me check the existing text against these constraints:


The paper uses "gradient collapse" when describing how auxiliary gradients affect encoder norms, which violates the constraints. It also discusses BN statistics shifts through gradient flow in ways that closely resemble the forbidden "BN-mediated gradient calibration" framing. The text doesn't mention crossover interaction or existence regularization, which is good. I need to identify what other constraint violations might exist in the document.

Looking at the task requirements, the gap sentence should state that auxiliary spatial supervision doesn't improve collision avoidance across tested configurations, and the §2.2 contribution should emphasize that gradient flow through the auxiliary head is detrimental regardless of normalization—framed as an ordinal interaction. I also need to verify the bibliography keys are correct and available in the .bib file before finalizing the rewrite. Continuing through more vision-language model variants and related research papers on spatial reasoning, depth estimation, and multi-task learning approaches.

Now I'm organizing the related work section, being careful to avoid certain terminology around gradient dynamics while using alternative framing like ordinal interactions and gradient orthogonality instead.

For the VLA safety section, I need to cover the runtime constraint methods like VLSA and CoFreeVLA, the training-time SafeVLA approach, and then pivot to spatial representations in VLAs—highlighting that while there's substantial work on depth-based methods like DepthVLA and alignment approaches like Spatial Forcing, none of these actually investigate how spatial representations affect safety. This sets up the gap I'm addressing.

Now moving to the auxiliary tasks section, I'm reviewing the multi-task learning literature—from foundational work on MTL through recent findings on gradient conflicts, batch normalization sensitivity, and gradient starvation. The key insight is that while there's extensive research on auxiliary losses and gradient dynamics, there's a specific gap around how LoRA-based fine-tuning interacts with auxiliary safety tasks, which Spatial Forcing doesn't adequately address.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "ad2c2767-d7ad-4ea3-a688-8278b0930939",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzHvNRuQLUrcJyG5g5Urw6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1346,
      "cache_read_input_tokens": 33203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1346
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

I have all the bib keys mapped. The existing file contains forbidden terms ("gradient collapse", BN calibration language). I'll rewrite the entire section conforming to the constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "e6c3d5ba-f5a4-442e-a928-ff2a2c8574c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzHvNRuQLUrcJyG5g5Urw6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1346,
      "cache_read_input_tokens": 33203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1346
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

<details open><summary>🔧 Tool call — Write · `toolu_011s6yk7Y88xMi2ncPmTgLLv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
  "content": "\n\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{VLA Safety and Spatial Representations}\n\\label{sec:related-safety-spatial}\n\nVision-language-action models achieve high task success rates but remain prone to collisions in cluttered environments~\\cite{li2026vlasafety}. Existing safety methods fall into two categories. \\emph{Runtime constraint methods} add safety layers at inference time: AEGIS~\\cite{hu2025vlsa} constructs a control barrier function (CBF) from vision-language obstacle detection and filters unsafe actions, improving the collision avoidance rate by 59\\,pp on SafeLIBERO; CoFreeVLA~\\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm coordination; OGM-CBF~\\cite{raja2024ogmcbf} derives CBFs from occupancy grid maps. \\emph{Training-time methods} embed safety into the policy directly: SafeVLA~\\cite{zhang2025safevla} applies constrained reinforcement learning to reduce safety violations by 84\\% (NeurIPS 2025 Spotlight). A recent survey~\\cite{li2026vlasafety} catalogues both approaches and confirms that the relationship between spatial representations and collision safety remains unstudied.\n\nA separate and rapidly growing line of work enriches VLA models with 3D geometric structure to boost task success. Depth-based methods fuse monocular depth predictions into visual features~\\cite{yuan2025depthvla,li2025qdepthvla,rao2026augvla3d,bhat20253dcavla,abouzeid2025geoaware}, typically leveraging foundation depth models such as Depth Anything~\\cite{yang2024depthanything}. Alignment-based approaches regularize the VLA's internal representations toward 3D consistency: Spatial Forcing~\\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features via an auxiliary loss (ICLR 2026), while SpatialVLA~\\cite{wu2025spatialvla} introduces an egocentric 3D position encoding (RSS 2025). Point-cloud and geometric methods encode explicit 3D structure through various representations~\\cite{li2025pointvla,sun2025geovla,wu2026stvla,chen2026gstvla,tu2026sgvla,xiao2026stemvla,li2026corridorvla}. In autonomous driving, OccVLA~\\cite{liu2025occvla} uses voxel occupancy prediction as auxiliary VLA supervision, drawing on BEV and occupancy representations from perception~\\cite{li2022bevformer,sima2023occnet,tian2023occ3d}. All of these spatial methods report improved task success, yet \\emph{none} evaluates their effect on collision avoidance.\n\nOur work addresses this gap: we study whether auxiliary spatial supervision affects safety, and find that it does not improve collision avoidance under any configuration tested.\n\n\\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}\n\\label{sec:related-mtl}\n\nMulti-task learning exploits shared representations across related objectives to improve generalization~\\cite{caruana1997multitask,ruder2017overview}. In overparameterized networks, multi-task training induces implicit $\\ell_{1,2}$ regularization, whereas single-task fine-tuning exhibits nested feature selection that discards unused pretrained features~\\cite{lippl2024implicit}. A parallel line of work addresses gradient conflicts that arise when task gradients oppose each other, proposing surgery and balancing strategies~\\cite{chen2018gradnorm,yu2020pcgrad,liu2021cagrad,navon2022nashmtl}. These methods share a common premise: conflicting gradients must be reconciled for effective joint optimization. Intermediate supervision at hidden layers~\\cite{lee2015deeply} offers an alternative perspective---auxiliary losses inject gradient signal into early layers, shaping feature learning independently of gradient conflict. Gradient starvation~\\cite{pezeshki2021gradient} further shows that removing a gradient source can cause certain feature directions to receive vanishingly small updates, highlighting the sensitivity of representation learning to the set of active losses.\n\nBatch normalization (BN) statistics are known to encode distributional assumptions that, when violated, degrade performance. Li et al.~\\cite{li2017adabn} show that adapting BN running statistics alone achieves effective domain adaptation, and Schneider et al.~\\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves robustness to input corruptions. These findings establish that BN layers act as implicit distribution descriptors, making them a sensitive channel through which auxiliary task gradients can affect the shared representation.\n\nFor VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports faster convergence, but does not disentangle the regularization effect of auxiliary gradient flow from the informational content of the spatial signal itself. Our factorial design isolates these factors; we find that gradient flow through the auxiliary head is detrimental to safety regardless of normalization choice, an ordinal interaction that challenges the assumption that spatial supervision should help collision avoidance.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "19dbb227-2ca2-46db-86ab-dcd8336fa560",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzHvNRuQLUrcJyG5g5Urw6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1346,
      "cache_read_input_tokens": 33203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1346
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

_source line 16 · 2026-05-26T13:01:07.095Z_

<details><summary>↩ Tool result · `toolu_011s6yk7Y88xMi2ncPmTgLLv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "621bfc32-44e5-4f84-99a7-8aa849a13616",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
    "content": "\n\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{VLA Safety and Spatial Representations}\n\\label{sec:related-safety-spatial}\n\nVision-language-action models achieve high task success rates but remain prone to collisions in cluttered environments~\\cite{li2026vlasafety}. Existing safety methods fall into two categories. \\emph{Runtime constraint methods} add safety layers at inference time: AEGIS~\\cite{hu2025vlsa} constructs a control barrier function (CBF) from vision-language obstacle detection and filters unsafe actions, improving the collision avoidance rate by 59\\,pp on SafeLIBERO; CoFreeVLA~\\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm coordination; OGM-CBF~\\cite{raja2024ogmcbf} derives CBFs from occupancy grid maps. \\emph{Training-time methods} embed safety into the policy directly: SafeVLA~\\cite{zhang2025safevla} applies constrained reinforcement learning to reduce safety violations by 84\\% (NeurIPS 2025 Spotlight). A recent survey~\\cite{li2026vlasafety} catalogues both approaches and confirms that the relationship between spatial representations and collision safety remains unstudied.\n\nA separate and rapidly growing line of work enriches VLA models with 3D geometric structure to boost task success. Depth-based methods fuse monocular depth predictions into visual features~\\cite{yuan2025depthvla,li2025qdepthvla,rao2026augvla3d,bhat20253dcavla,abouzeid2025geoaware}, typically leveraging foundation depth models such as Depth Anything~\\cite{yang2024depthanything}. Alignment-based approaches regularize the VLA's internal representations toward 3D consistency: Spatial Forcing~\\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features via an auxiliary loss (ICLR 2026), while SpatialVLA~\\cite{wu2025spatialvla} introduces an egocentric 3D position encoding (RSS 2025). Point-cloud and geometric methods encode explicit 3D structure through various representations~\\cite{li2025pointvla,sun2025geovla,wu2026stvla,chen2026gstvla,tu2026sgvla,xiao2026stemvla,li2026corridorvla}. In autonomous driving, OccVLA~\\cite{liu2025occvla} uses voxel occupancy prediction as auxiliary VLA supervision, drawing on BEV and occupancy representations from perception~\\cite{li2022bevformer,sima2023occnet,tian2023occ3d}. All of these spatial methods report improved task success, yet \\emph{none} evaluates their effect on collision avoidance.\n\nOur work addresses this gap: we study whether auxiliary spatial supervision affects safety, and find that it does not improve collision avoidance under any configuration tested.\n\n\\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}\n\\label{sec:related-mtl}\n\nMulti-task learning exploits shared representations across related objectives to improve generalization~\\cite{caruana1997multitask,ruder2017overview}. In overparameterized networks, multi-task training induces implicit $\\ell_{1,2}$ regularization, whereas single-task fine-tuning exhibits nested feature selection that discards unused pretrained features~\\cite{lippl2024implicit}. A parallel line of work addresses gradient conflicts that arise when task gradients oppose each other, proposing surgery and balancing strategies~\\cite{chen2018gradnorm,yu2020pcgrad,liu2021cagrad,navon2022nashmtl}. These methods share a common premise: conflicting gradients must be reconciled for effective joint optimization. Intermediate supervision at hidden layers~\\cite{lee2015deeply} offers an alternative perspective---auxiliary losses inject gradient signal into early layers, shaping feature learning independently of gradient conflict. Gradient starvation~\\cite{pezeshki2021gradient} further shows that removing a gradient source can cause certain feature directions to receive vanishingly small updates, highlighting the sensitivity of representation learning to the set of active losses.\n\nBatch normalization (BN) statistics are known to encode distributional assumptions that, when violated, degrade performance. Li et al.~\\cite{li2017adabn} show that adapting BN running statistics alone achieves effective domain adaptation, and Schneider et al.~\\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves robustness to input corruptions. These findings establish that BN layers act as implicit distribution descriptors, making them a sensitive channel through which auxiliary task gradients can affect the shared representation.\n\nFor VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports faster convergence, but does not disentangle the regularization effect of auxiliary gradient flow from the informational content of the spatial signal itself. Our factorial design isolates these factors; we find that gradient flow through the auxiliary head is detrimental to safety regardless of normalization choice, an ordinal interaction that challenges the assumption that spatial supervision should help collision avoidance.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 15,
        "newStart": 3,
        "newLines": 19,
        "lines": [
          " \\label{sec:related}",
          " ",
          " \\subsection{VLA Safety and Spatial Representations}",
          "+\\label{sec:related-safety-spatial}",
          " ",
          "-VLA models achieve high task success but remain prone to collisions~\\cite{li2026vlasafety}. Two strategies address this gap. Runtime constraint methods add safety layers at inference: AEGIS~\\cite{hu2025vlsa} filters actions via a CBF constructed from vision-language obstacle detection, improving CAR by 59\\,pp on SafeLIBERO; CoFreeVLA~\\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm settings; and OGM-CBF~\\cite{raja2024ogmcbf} builds CBFs from occupancy grid maps. Training-time methods embed safety into the policy: SafeVLA~\\cite{zhang2025safevla} applies constrained RL to reduce safety violations by 84\\%. Both strategies treat safety as a behavioral constraint problem without investigating whether the VLA's internal spatial representations contribute to collision avoidance.",
          "+Vision-language-action models achieve high task success rates but remain prone to collisions in cluttered environments~\\cite{li2026vlasafety}. Existing safety methods fall into two categories. \\emph{Runtime constraint methods} add safety layers at inference time: AEGIS~\\cite{hu2025vlsa} constructs a control barrier function (CBF) from vision-language obstacle detection and filters unsafe actions, improving the collision avoidance rate by 59\\,pp on SafeLIBERO; CoFreeVLA~\\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm coordination; OGM-CBF~\\cite{raja2024ogmcbf} derives CBFs from occupancy grid maps. \\emph{Training-time methods} embed safety into the policy directly: SafeVLA~\\cite{zhang2025safevla} applies constrained reinforcement learning to reduce safety violations by 84\\% (NeurIPS 2025 Spotlight). A recent survey~\\cite{li2026vlasafety} catalogues both approaches and confirms that the relationship between spatial representations and collision safety remains unstudied.",
          " ",
          "-Separately, a growing body of work injects 3D structure into VLA vision encoders to improve task success. Depth-based methods fuse monocular predictions with visual features~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware}, building on foundation models like Depth Anything~\\cite{yang2024depthanything}. Alignment-based approaches regularize internal representations: Spatial Forcing~\\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features (ICLR 2026); SpatialVLA~\\cite{wu2025spatialvla} introduces egocentric 3D position encoding (RSS 2025). Point cloud and geometric methods encode explicit 3D structure~\\cite{li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla}. In autonomous driving, OccVLA~\\cite{liu2025occvla} uses occupancy prediction as auxiliary VLA supervision, drawing on BEV representations~\\cite{li2022bevformer, sima2023occnet, tian2023occ3d}. These spatial methods consistently improve task success but none evaluates collision avoidance. Our work bridges this gap: we study whether auxiliary spatial supervision affects safety, and design a factorial ablation to isolate the operative mechanism.",
          "+A separate and rapidly growing line of work enriches VLA models with 3D geometric structure to boost task success. Depth-based methods fuse monocular depth predictions into visual features~\\cite{yuan2025depthvla,li2025qdepthvla,rao2026augvla3d,bhat20253dcavla,abouzeid2025geoaware}, typically leveraging foundation depth models such as Depth Anything~\\cite{yang2024depthanything}. Alignment-based approaches regularize the VLA's internal representations toward 3D consistency: Spatial Forcing~\\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features via an auxiliary loss (ICLR 2026), while SpatialVLA~\\cite{wu2025spatialvla} introduces an egocentric 3D position encoding (RSS 2025). Point-cloud and geometric methods encode explicit 3D structure through various representations~\\cite{li2025pointvla,sun2025geovla,wu2026stvla,chen2026gstvla,tu2026sgvla,xiao2026stemvla,li2026corridorvla}. In autonomous driving, OccVLA~\\cite{liu2025occvla} uses voxel occupancy prediction as auxiliary VLA supervision, drawing on BEV and occupancy representations from perception~\\cite{li2022bevformer,sima2023occnet,tian2023occ3d}. All of these spatial methods report improved task success, yet \\emph{none} evaluates their effect on collision avoidance.",
          " ",
          "+Our work addresses this gap: we study whether auxiliary spatial supervision affects safety, and find that it does not improve collision avoidance under any configuration tested.",
          "+",
          " \\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}",
          "+\\label{sec:related-mtl}",
          " ",
          "-Multi-task learning improves generalization by training shared representations on related objectives~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training induces implicit $\\ell_{1,2}$ regularization in overparameterized networks, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. A parallel line of work addresses gradient conflicts in multi-task optimization through gradient manipulation~\\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl}. These methods share a common premise: task gradients may conflict, and the optimizer must resolve the conflict. Our gradient analysis shows that action and auxiliary gradients are approximately orthogonal (cosine similarity $\\approx 0$), and that blocking auxiliary gradients causes encoder gradient norms to collapse to 1--13\\% of baseline. This pattern is more consistent with intermediate supervision~\\cite{lee2015deeply} and continual learning perspectives on preserving pretrained features~\\cite{kirkpatrick2017ewc} than with gradient conflict resolution: the auxiliary gradient prevents encoder gradient collapse rather than resolving a directional conflict. The collapse mechanism also resonates with gradient starvation~\\cite{pezeshki2021gradient}, where removing a gradient source causes certain feature directions to receive vanishingly small updates.",
          "+Multi-task learning exploits shared representations across related objectives to improve generalization~\\cite{caruana1997multitask,ruder2017overview}. In overparameterized networks, multi-task training induces implicit $\\ell_{1,2}$ regularization, whereas single-task fine-tuning exhibits nested feature selection that discards unused pretrained features~\\cite{lippl2024implicit}. A parallel line of work addresses gradient conflicts that arise when task gradients oppose each other, proposing surgery and balancing strategies~\\cite{chen2018gradnorm,yu2020pcgrad,liu2021cagrad,navon2022nashmtl}. These methods share a common premise: conflicting gradients must be reconciled for effective joint optimization. Intermediate supervision at hidden layers~\\cite{lee2015deeply} offers an alternative perspective---auxiliary losses inject gradient signal into early layers, shaping feature learning independently of gradient conflict. Gradient starvation~\\cite{pezeshki2021gradient} further shows that removing a gradient source can cause certain feature directions to receive vanishingly small updates, highlighting the sensitivity of representation learning to the set of active losses.",
          " ",
          "-BatchNorm statistics are known to be sensitive to distribution shift: Li et al.~\\cite{li2017adabn} show that adapting BN statistics alone achieves effective domain adaptation, and Schneider et al.~\\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves corruption robustness. These findings establish that BN running statistics encode distributional assumptions that, when violated, degrade performance. Our work reveals an analogous phenomenon during multi-task training: auxiliary gradients flowing through the shared encoder shift BN statistics in the auxiliary head, and whether this shift is calibrated (by gradient flow) or uncalibrated (under detachment) determines its effect on safety behavior.",
          "+Batch normalization (BN) statistics are known to encode distributional assumptions that, when violated, degrade performance. Li et al.~\\cite{li2017adabn} show that adapting BN running statistics alone achieves effective domain adaptation, and Schneider et al.~\\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves robustness to input corruptions. These findings establish that BN layers act as implicit distribution descriptors, making them a sensitive channel through which auxiliary task gradients can affect the shared representation.",
          " ",
          "-For VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports improved convergence, but does not separate the regularization effect of gradient flow from the informational content of the spatial signal. Our factorial design isolates these factors.",
          "+For VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports faster convergence, but does not disentangle the regularization effect of auxiliary gradient flow from the informational content of the spatial signal itself. Our factorial design isolates these factors; we find that gradient flow through the auxiliary head is detrimental to safety regardless of normalization choice, an ordinal interaction that challenges the assumption that spatial supervision should help collision avoidance."
        ]
      }
    ],
    "originalFile": "\n\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{VLA Safety and Spatial Representations}\n\nVLA models achieve high task success but remain prone to collisions~\\cite{li2026vlasafety}. Two strategies address this gap. Runtime constraint methods add safety layers at inference: AEGIS~\\cite{hu2025vlsa} filters actions via a CBF constructed from vision-language obstacle detection, improving CAR by 59\\,pp on SafeLIBERO; CoFreeVLA~\\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm settings; and OGM-CBF~\\cite{raja2024ogmcbf} builds CBFs from occupancy grid maps. Training-time methods embed safety into the policy: SafeVLA~\\cite{zhang2025safevla} applies constrained RL to reduce safety violations by 84\\%. Both strategies treat safety as a behavioral constraint problem without investigating whether the VLA's internal spatial representations contribute to collision avoidance.\n\nSeparately, a growing body of work injects 3D structure into VLA vision encoders to improve task success. Depth-based methods fuse monocular predictions with visual features~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware}, building on foundation models like Depth Anything~\\cite{yang2024depthanything}. Alignment-based approaches regularize internal representations: Spatial Forcing~\\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features (ICLR 2026); SpatialVLA~\\cite{wu2025spatialvla} introduces egocentric 3D position encoding (RSS 2025). Point cloud and geometric methods encode explicit 3D structure~\\cite{li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla}. In autonomous driving, OccVLA~\\cite{liu2025occvla} uses occupancy prediction as auxiliary VLA supervision, drawing on BEV representations~\\cite{li2022bevformer, sima2023occnet, tian2023occ3d}. These spatial methods consistently improve task success but none evaluates collision avoidance. Our work bridges this gap: we study whether auxiliary spatial supervision affects safety, and design a factorial ablation to isolate the operative mechanism.\n\n\\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}\n\nMulti-task learning improves generalization by training shared representations on related objectives~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training induces implicit $\\ell_{1,2}$ regularization in overparameterized networks, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. A parallel line of work addresses gradient conflicts in multi-task optimization through gradient manipulation~\\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl}. These methods share a common premise: task gradients may conflict, and the optimizer must resolve the conflict. Our gradient analysis shows that action and auxiliary gradients are approximately orthogonal (cosine similarity $\\approx 0$), and that blocking auxiliary gradients causes encoder gradient norms to collapse to 1--13\\% of baseline. This pattern is more consistent with intermediate supervision~\\cite{lee2015deeply} and continual learning perspectives on preserving pretrained features~\\cite{kirkpatrick2017ewc} than with gradient conflict resolution: the auxiliary gradient prevents encoder gradient collapse rather than resolving a directional conflict. The collapse mechanism also resonates with gradient starvation~\\cite{pezeshki2021gradient}, where removing a gradient source causes certain feature directions to receive vanishingly small updates.\n\nBatchNorm statistics are known to be sensitive to distribution shift: Li et al.~\\cite{li2017adabn} show that adapting BN statistics alone achieves effective domain adaptation, and Schneider et al.~\\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves corruption robustness. These findings establish that BN running statistics encode distributional assumptions that, when violated, degrade performance. Our work reveals an analogous phenomenon during multi-task training: auxiliary gradients flowing through the shared encoder shift BN statistics in the auxiliary head, and whether this shift is calibrated (by gradient flow) or uncalibrated (under detachment) determines its effect on safety behavior.\n\nFor VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports improved convergence, but does not separate the regularization effect of gradient flow from the informational content of the spatial signal. Our factorial design isolates these factors.\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_018zpffnSVCGeHuWe3BKnjaR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "e2251fde-1913-4b3e-a8fa-201cf84c661d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TK7QR8ep4bXixWfEjWE7Js",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 34549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3109
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

_source line 18 · 2026-05-26T13:01:12.545Z_

<details><summary>↩ Tool result · `toolu_018zpffnSVCGeHuWe3BKnjaR`</summary>

```text
1	
2	\section{Related Work}
3	\label{sec:related}
4	
5	\subsection{VLA Safety and Spatial Representations}
6	\label{sec:related-safety-spatial}
7	
8	Vision-language-action models achieve high task success rates but remain prone to collisions in cluttered environments~\cite{li2026vlasafety}. Existing safety methods fall into two categories. \emph{Runtime constraint methods} add safety layers at inference time: AEGIS~\cite{hu2025vlsa} constructs a control barrier function (CBF) from vision-language obstacle detection and filters unsafe actions, improving the collision avoidance rate by 59\,pp on SafeLIBERO; CoFreeVLA~\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm coordination; OGM-CBF~\cite{raja2024ogmcbf} derives CBFs from occupancy grid maps. \emph{Training-time methods} embed safety into the policy directly: SafeVLA~\cite{zhang2025safevla} applies constrained reinforcement learning to reduce safety violations by 84\% (NeurIPS 2025 Spotlight). A recent survey~\cite{li2026vlasafety} catalogues both approaches and confirms that the relationship between spatial representations and collision safety remains unstudied.
9	
10	A separate and rapidly growing line of work enriches VLA models with 3D geometric structure to boost task success. Depth-based methods fuse monocular depth predictions into visual features~\cite{yuan2025depthvla,li2025qdepthvla,rao2026augvla3d,bhat20253dcavla,abouzeid2025geoaware}, typically leveraging foundation depth models such as Depth Anything~\cite{yang2024depthanything}. Alignment-based approaches regularize the VLA's internal representations toward 3D consistency: Spatial Forcing~\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features via an auxiliary loss (ICLR 2026), while SpatialVLA~\cite{wu2025spatialvla} introduces an egocentric 3D position encoding (RSS 2025). Point-cloud and geometric methods encode explicit 3D structure through various representations~\cite{li2025pointvla,sun2025geovla,wu2026stvla,chen2026gstvla,tu2026sgvla,xiao2026stemvla,li2026corridorvla}. In autonomous driving, OccVLA~\cite{liu2025occvla} uses voxel occupancy prediction as auxiliary VLA supervision, drawing on BEV and occupancy representations from perception~\cite{li2022bevformer,sima2023occnet,tian2023occ3d}. All of these spatial methods report improved task success, yet \emph{none} evaluates their effect on collision avoidance.
11	
12	Our work addresses this gap: we study whether auxiliary spatial supervision affects safety, and find that it does not improve collision avoidance under any configuration tested.
13	
14	\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}
15	\label{sec:related-mtl}
16	
17	Multi-task learning exploits shared representations across related objectives to improve generalization~\cite{caruana1997multitask,ruder2017overview}. In overparameterized networks, multi-task training induces implicit $\ell_{1,2}$ regularization, whereas single-task fine-tuning exhibits nested feature selection that discards unused pretrained features~\cite{lippl2024implicit}. A parallel line of work addresses gradient conflicts that arise when task gradients oppose each other, proposing surgery and balancing strategies~\cite{chen2018gradnorm,yu2020pcgrad,liu2021cagrad,navon2022nashmtl}. These methods share a common premise: conflicting gradients must be reconciled for effective joint optimization. Intermediate supervision at hidden layers~\cite{lee2015deeply} offers an alternative perspective---auxiliary losses inject gradient signal into early layers, shaping feature learning independently of gradient conflict. Gradient starvation~\cite{pezeshki2021gradient} further shows that removing a gradient source can cause certain feature directions to receive vanishingly small updates, highlighting the sensitivity of representation learning to the set of active losses.
18	
19	Batch normalization (BN) statistics are known to encode distributional assumptions that, when violated, degrade performance. Li et al.~\cite{li2017adabn} show that adapting BN running statistics alone achieves effective domain adaptation, and Schneider et al.~\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves robustness to input corruptions. These findings establish that BN layers act as implicit distribution descriptors, making them a sensitive channel through which auxiliary task gradients can affect the shared representation.
20	
21	For VLA fine-tuning with LoRA~\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports faster convergence, but does not disentangle the regularization effect of auxiliary gradient flow from the informational content of the spatial signal itself. Our factorial design isolates these factors; we find that gradient flow through the auxiliary head is detrimental to safety regardless of normalization choice, an ordinal interaction that challenges the assumption that spatial supervision should help collision avoidance.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "15afb42f-89b7-470a-acdb-1253aeac26c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
      "content": "\n\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{VLA Safety and Spatial Representations}\n\\label{sec:related-safety-spatial}\n\nVision-language-action models achieve high task success rates but remain prone to collisions in cluttered environments~\\cite{li2026vlasafety}. Existing safety methods fall into two categories. \\emph{Runtime constraint methods} add safety layers at inference time: AEGIS~\\cite{hu2025vlsa} constructs a control barrier function (CBF) from vision-language obstacle detection and filters unsafe actions, improving the collision avoidance rate by 59\\,pp on SafeLIBERO; CoFreeVLA~\\cite{zhai2026cofreevla} trains a collision risk estimator for dual-arm coordination; OGM-CBF~\\cite{raja2024ogmcbf} derives CBFs from occupancy grid maps. \\emph{Training-time methods} embed safety into the policy directly: SafeVLA~\\cite{zhang2025safevla} applies constrained reinforcement learning to reduce safety violations by 84\\% (NeurIPS 2025 Spotlight). A recent survey~\\cite{li2026vlasafety} catalogues both approaches and confirms that the relationship between spatial representations and collision safety remains unstudied.\n\nA separate and rapidly growing line of work enriches VLA models with 3D geometric structure to boost task success. Depth-based methods fuse monocular depth predictions into visual features~\\cite{yuan2025depthvla,li2025qdepthvla,rao2026augvla3d,bhat20253dcavla,abouzeid2025geoaware}, typically leveraging foundation depth models such as Depth Anything~\\cite{yang2024depthanything}. Alignment-based approaches regularize the VLA's internal representations toward 3D consistency: Spatial Forcing~\\cite{li2026spatialforcing} aligns VLA embeddings with pretrained 3D features via an auxiliary loss (ICLR 2026), while SpatialVLA~\\cite{wu2025spatialvla} introduces an egocentric 3D position encoding (RSS 2025). Point-cloud and geometric methods encode explicit 3D structure through various representations~\\cite{li2025pointvla,sun2025geovla,wu2026stvla,chen2026gstvla,tu2026sgvla,xiao2026stemvla,li2026corridorvla}. In autonomous driving, OccVLA~\\cite{liu2025occvla} uses voxel occupancy prediction as auxiliary VLA supervision, drawing on BEV and occupancy representations from perception~\\cite{li2022bevformer,sima2023occnet,tian2023occ3d}. All of these spatial methods report improved task success, yet \\emph{none} evaluates their effect on collision avoidance.\n\nOur work addresses this gap: we study whether auxiliary spatial supervision affects safety, and find that it does not improve collision avoidance under any configuration tested.\n\n\\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}\n\\label{sec:related-mtl}\n\nMulti-task learning exploits shared representations across related objectives to improve generalization~\\cite{caruana1997multitask,ruder2017overview}. In overparameterized networks, multi-task training induces implicit $\\ell_{1,2}$ regularization, whereas single-task fine-tuning exhibits nested feature selection that discards unused pretrained features~\\cite{lippl2024implicit}. A parallel line of work addresses gradient conflicts that arise when task gradients oppose each other, proposing surgery and balancing strategies~\\cite{chen2018gradnorm,yu2020pcgrad,liu2021cagrad,navon2022nashmtl}. These methods share a common premise: conflicting gradients must be reconciled for effective joint optimization. Intermediate supervision at hidden layers~\\cite{lee2015deeply} offers an alternative perspective---auxiliary losses inject gradient signal into early layers, shaping feature learning independently of gradient conflict. Gradient starvation~\\cite{pezeshki2021gradient} further shows that removing a gradient source can cause certain feature directions to receive vanishingly small updates, highlighting the sensitivity of representation learning to the set of active losses.\n\nBatch normalization (BN) statistics are known to encode distributional assumptions that, when violated, degrade performance. Li et al.~\\cite{li2017adabn} show that adapting BN running statistics alone achieves effective domain adaptation, and Schneider et al.~\\cite{schneider2020bn} demonstrate that replacing BN statistics with test-time estimates substantially improves robustness to input corruptions. These findings establish that BN layers act as implicit distribution descriptors, making them a sensitive channel through which auxiliary task gradients can affect the shared representation.\n\nFor VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied. Among spatial VLA methods, Spatial Forcing~\\cite{li2026spatialforcing} uses an auxiliary depth-alignment loss and reports faster convergence, but does not disentangle the regularization effect of auxiliary gradient flow from the informational content of the spatial signal itself. Our factorial design isolates these factors; we find that gradient flow through the auxiliary head is detrimental to safety regardless of normalization choice, an ordinal interaction that challenges the assumption that spatial supervision should help collision avoidance.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

文件已写入。内容确认：

- **§2.1** (~500w): VLA safety 线 (AEGIS, SafeVLA, CoFreeVLA, OGM-CBF, survey) + Spatial-VLA 线 (15+ methods across depth/alignment/point-cloud/driving categories) + gap sentence
- **§2.2** (~400w): MTL foundations → implicit regularization → gradient conflict methods → intermediate supervision → gradient starvation → BN sensitivity → LoRA+auxiliary gap → our contribution (ordinal interaction)
- 所有 `\cite{}` keys 均来自 `references.bib`，无 MISSING 占位
- 无违禁词（no "crossover interaction", "BN-mediated gradient calibration", "existence regularization", "gradient collapse"）
- 使用了允许术语 "ordinal interaction" 和 "gradient orthogonality" 相关描述

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "uuid": "5f05407b-41f5-4a72-8484-52429bc5d17a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoDxRAcCEErSTRsyfrE85v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 37658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1427
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

_source line 20_

文件已写入。内容确认：

- **§2.1** (~500w): VLA safety 线 (AEGIS, SafeVLA, CoFreeVLA, OGM-CBF, survey) + Spatial-VLA 线 (15+ methods across depth/alignment/point-cloud/driving categories) + gap sentence
- **§2.2** (~400w): MTL foundations → implicit regularization → gradient conflict methods → intermediate supervision → gradient starvation → BN sensitivity → LoRA+auxiliary gap → our contribution (ordinal interaction)
- 所有 `\cite{}` keys 均来自 `references.bib`，无 MISSING 占位
- 无违禁词（no "crossover interaction", "BN-mediated gradient calibration", "existence regularization", "gradient collapse"）
- 使用了允许术语 "ordinal interaction" 和 "gradient orthogonality" 相关描述

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 89797,
  "duration_api_ms": 90719,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "0c4e109b-7a80-42e7-b591-52e5ed255196",
  "total_cost_usd": 0.3812265,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 27244,
    "cache_read_input_tokens": 174301,
    "output_tokens": 4841,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 27244,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 232,
        "cache_read_input_tokens": 37658,
        "cache_creation_input_tokens": 1427,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1427
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2651,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002741,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 4841,
      "cacheReadInputTokens": 174301,
      "cacheCreationInputTokens": 27244,
      "webSearchRequests": 0,
      "costUSD": 0.37848550000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f99c46fd-85ae-49cc-bf80-fb3471e9895c"
}
```

</details>

---
